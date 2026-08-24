"""PHP AST / Grammar Parser Adapter implementing ParserPort."""

from __future__ import annotations

import os
import re
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from pattern_detector.domain.code_model import (
    CodeModel,
    ExpressionFlowStep,
    FunctionInvocation,
    FunctionModel,
    MethodSignature,
    NamespaceModel,
    ProtocolModel,
    RecordModel,
    StateModel,
)
from pattern_detector.domain.value_objects import SourceLocation
from pattern_detector.ports.outbound import ParserPort

_PHP_BUILTINS_AND_KEYWORDS = frozenset(
    {
        "self",
        "parent",
        "static",
        "this",
        "null",
        "true",
        "false",
        "int",
        "string",
        "float",
        "bool",
        "array",
        "object",
        "callable",
        "iterable",
        "void",
        "never",
        "mixed",
        "echo",
        "print",
        "isset",
        "empty",
        "unset",
        "die",
        "exit",
        "include",
        "include_once",
        "require",
        "require_once",
        "eval",
        "count",
        "sizeof",
        "strlen",
        "array_merge",
        "array_map",
        "array_filter",
        "in_array",
        "is_array",
        "is_string",
        "is_int",
        "is_null",
        "is_object",
        "is_a",
        "instanceof",
        "Exception",
        "Throwable",
        "RuntimeException",
        "InvalidArgumentException",
        "LogicException",
        "Stringable",
        "Countable",
        "Iterator",
        "IteratorAggregate",
        "ArrayAccess",
        "Serializable",
        "Closure",
        "Generator",
    }
)


class _PhpSourceExtractor:
    """Extracts structural and semantic domain models from PHP source code."""

    def __init__(self, file_path: str, source_code: str) -> None:
        self.file_path = file_path
        self.source_code = source_code
        self.namespace_name = "global"

        self.imports: list[str] = []
        self.requires: list[str] = []
        self.protocols: dict[str, ProtocolModel] = {}
        self.records: dict[str, RecordModel] = {}
        self.functions: dict[str, FunctionModel] = {}
        self.states: dict[str, StateModel] = {}

    def extract(self) -> None:
        """Parse source code into domain models."""
        # 1. Extract Namespace
        ns_match = re.search(r'\bnamespace\s+([a-zA-Z0-9_\\]+)\s*[;{]', self.source_code)
        if ns_match:
            self.namespace_name = ns_match.group(1).replace("\\", ".")

        # 2. Extract use statements (imports)
        use_pattern = re.compile(r'\buse\s+(?:function\s+|const\s+)?([a-zA-Z0-9_\\,\s{}]+);')
        for match in use_pattern.finditer(self.source_code):
            raw_use = match.group(1).strip()
            # Handle group use: use App\Services\{A, B as C};
            if "{" in raw_use and "}" in raw_use:
                prefix_match = re.match(r'([a-zA-Z0-9_\\]+)\s*\{\s*(.+)\s*\}', raw_use)
                if prefix_match:
                    prefix = prefix_match.group(1).rstrip("\\")
                    items = [i.strip() for i in prefix_match.group(2).split(",") if i.strip()]
                    for item in items:
                        item_clean = item.split(" as ")[0].strip()
                        full_name = f"{prefix}\\{item_clean}".replace("\\", ".")
                        self.imports.append(full_name)
                        base_pkg = full_name.split(".")[0]
                        if base_pkg not in self.requires:
                            self.requires.append(base_pkg)
            else:
                for single_use in raw_use.split(","):
                    single_use = single_use.strip()
                    if single_use:
                        item_clean = single_use.split(" as ")[0].strip()
                        full_name = item_clean.replace("\\", ".")
                        self.imports.append(full_name)
                        base_pkg = full_name.split(".")[0]
                        if base_pkg not in self.requires:
                            self.requires.append(base_pkg)

        # 3. Extract Interfaces, Classes, Traits, Enums
        self._extract_interfaces()
        self._extract_classes()
        self._extract_standalone_functions()

    def _get_line_number(self, index: int) -> int:
        return self.source_code.count("\n", 0, index) + 1

    def _extract_interfaces(self) -> None:
        # Match interface Name [extends Base1, Base2] { ... }
        pattern = re.compile(
            r'(?:/\*\*(?P<doc>[\s\S]*?)\*/\s*)?'
            r'(?:#\[[^\]]+\]\s*)*'
            r'\binterface\s+(?P<name>[a-zA-Z0-9_]+)'
            r'(?:\s+extends\s+(?P<extends>[a-zA-Z0-9_\\,\s]+))?\s*\{',
            re.MULTILINE,
        )

        for match in pattern.finditer(self.source_code):
            iface_name = match.group("name")
            start_pos = match.start()
            line = self._get_line_number(start_pos)
            loc = SourceLocation(file_path=self.file_path, line=line, column=1)
            doc = (match.group("doc") or "").strip()

            body = self._extract_balanced_braces_content(self.source_code, match.end() - 1)
            methods = self._extract_interface_methods(body, line)

            self.protocols[iface_name] = ProtocolModel(
                name=iface_name,
                namespace=self.namespace_name,
                location=loc,
                methods=methods,
                docstring=doc,
            )

    def _extract_classes(self) -> None:
        pattern = re.compile(
            r'(?:/\*\*(?P<doc>[\s\S]*?)\*/\s*)?'
            r'(?P<attrs>(?:#\[[^\]]+\]\s*)*)'
            r'(?P<modifiers>(?:abstract\s+|final\s+|readonly\s+)*)'
            r'(?P<kind>class|trait|enum)\s+(?P<name>[a-zA-Z0-9_]+)'
            r'(?:\s+extends\s+(?P<extends>[a-zA-Z0-9_\\]+))?'
            r'(?:\s+implements\s+(?P<implements>[a-zA-Z0-9_\\,\s]+))?\s*\{',
            re.MULTILINE,
        )

        for match in pattern.finditer(self.source_code):
            class_name = match.group("name")
            kind = match.group("kind")
            modifiers = match.group("modifiers") or ""
            is_abstract = "abstract" in modifiers
            doc = (match.group("doc") or "").strip()
            attrs = match.group("attrs") or ""
            is_singleton_attr = "singleton" in attrs.lower()

            extends_val = match.group("extends")
            implements_val = match.group("implements")

            bases: list[str] = []
            if extends_val:
                bases.append(extends_val.strip().split("\\")[-1])
            if implements_val:
                for impl in implements_val.split(","):
                    impl_clean = impl.strip().split("\\")[-1]
                    if impl_clean:
                        bases.append(impl_clean)

            start_pos = match.start()
            line = self._get_line_number(start_pos)
            loc = SourceLocation(file_path=self.file_path, line=line, column=1)

            body = self._extract_balanced_braces_content(self.source_code, match.end() - 1)
            fields, constructor_promoted = self._extract_class_fields(body)
            fields.extend(constructor_promoted)

            methods = self._extract_class_methods(class_name, body, line)

            # Check if class is abstract or interface-like
            pure_methods = [
                MethodSignature(name=m.name.split(".")[-1], location=m.location) for m in methods if m.is_abstract
            ]

            record = RecordModel(
                name=class_name,
                namespace=self.namespace_name,
                location=loc,
                fields=fields,
                implemented_protocols=bases,
                methods=methods,
                is_type=is_abstract,
                docstring=doc,
            )
            self.records[class_name] = record

            # Register as protocol if abstract or defines pure methods
            if is_abstract or (len(pure_methods) > 0):
                self.protocols[class_name] = ProtocolModel(
                    name=class_name,
                    namespace=self.namespace_name,
                    location=loc,
                    methods=pure_methods if pure_methods else [MethodSignature(name=m.name.split(".")[-1], location=m.location) for m in methods],
                    docstring=doc,
                )

            # Singleton State Detection
            has_instance_field = any(f in ("instance", "_instance", "instances", "_instances") for f in fields)
            has_get_instance = any("getinstance" in m.name.lower() or "instance" == m.name.split(".")[-1].lower() for m in methods)
            if is_singleton_attr or (has_instance_field and has_get_instance):
                self.states[f"{class_name}::$instance"] = StateModel(
                    name=f"{class_name}::$instance",
                    namespace=self.namespace_name,
                    location=loc,
                    kind="atom",
                    is_once=True,
                    is_dynamic=True,
                )

    def _extract_class_fields(self, body: str) -> tuple[list[str], list[str]]:
        fields: list[str] = []
        promoted: list[str] = []

        # Standard properties: private/protected/public [static] [readonly] [type] $varName;
        prop_pattern = re.compile(
            r'(?:private|protected|public|var)\s+(?:static\s+)?(?:readonly\s+)?(?:[a-zA-Z0-9_\\?|&]+\s+)?\$([a-zA-Z0-9_]+)'
        )
        for match in prop_pattern.finditer(body):
            fields.append(match.group(1))

        # Constructor property promotion: __construct(private string $foo, ...)
        ctor_match = re.search(r'function\s+__construct\s*\((.*?)\)', body, re.DOTALL)
        if ctor_match:
            params_str = ctor_match.group(1)
            promoted_pattern = re.compile(r'(?:private|protected|public)\s+(?:readonly\s+)?(?:[a-zA-Z0-9_\\?|&]+\s+)?\$([a-zA-Z0-9_]+)')
            for p_match in promoted_pattern.finditer(params_str):
                promoted.append(p_match.group(1))

        return fields, promoted

    def _extract_interface_methods(self, body: str, parent_line: int) -> list[MethodSignature]:
        methods: list[MethodSignature] = []
        pattern = re.compile(r'public\s+function\s+([a-zA-Z0-9_]+)\s*\(', re.MULTILINE)
        for match in pattern.finditer(body):
            m_name = match.group(1)
            line = parent_line + body.count("\n", 0, match.start())
            loc = SourceLocation(file_path=self.file_path, line=line, column=1)
            methods.append(MethodSignature(name=m_name, location=loc))
        return methods

    def _extract_class_methods(self, class_name: str, body: str, parent_line: int) -> list[FunctionModel]:
        methods: list[FunctionModel] = []
        pattern = re.compile(
            r'(?:/\*\*(?P<doc>[\s\S]*?)\*/\s*)?'
            r'(?P<attrs>(?:#\[[^\]]+\]\s*)*)'
            r'(?P<modifiers>(?:abstract\s+|final\s+|public\s+|protected\s+|private\s+|static\s+)*)'
            r'function\s+(?P<name>[a-zA-Z0-9_]+)\s*\((?P<params>.*?)\)'
            r'(?:\s*:\s*(?P<return>[a-zA-Z0-9_\\?|&]+))?\s*(?P<body>\{|;)',
            re.DOTALL,
        )

        for match in pattern.finditer(body):
            fn_name = match.group("name")
            qualified_name = f"{class_name}.{fn_name}"
            modifiers = match.group("modifiers") or ""
            is_abstract = "abstract" in modifiers or match.group("body") == ";"
            is_private = "private" in modifiers or fn_name.startswith("_")

            raw_params = match.group("params") or ""
            param_names = [p.strip().split("$")[-1].split("=")[0].strip() for p in raw_params.split(",") if "$" in p]

            line = parent_line + body.count("\n", 0, match.start())
            loc = SourceLocation(file_path=self.file_path, line=line, column=1)
            doc = (match.group("doc") or "").strip()

            method_body = ""
            if match.group("body") == "{":
                method_body = self._extract_balanced_braces_content(body, match.end() - 1)

            calls, r_vars, w_vars, m_vars = self._analyze_php_method_body(method_body)
            invocations = self._extract_php_invocations(method_body, qualified_name, line)
            flow_steps = self._extract_php_flow_steps(param_names, method_body, qualified_name, line)

            fn_model = FunctionModel(
                name=qualified_name,
                namespace=self.namespace_name,
                location=loc,
                parameter_lists=[param_names],
                body_text=method_body,
                calls=sorted(set(calls)),
                invocations=invocations,
                flow_steps=flow_steps,
                reads_variables=sorted(set(r_vars)),
                writes_variables=sorted(set(w_vars)),
                modifies_variables=sorted(set(m_vars)),
                decorators=[a.strip() for a in (match.group("attrs") or "").splitlines() if a.strip()],
                docstring=doc,
                is_private=is_private,
                is_abstract=is_abstract,
            )
            methods.append(fn_model)
            self.functions[qualified_name] = fn_model

        return methods

    def _extract_standalone_functions(self) -> None:
        # Match free functions outside classes
        pattern = re.compile(
            r'function\s+([a-zA-Z0-9_]+)\s*\((.*?)\)\s*(?::\s*[a-zA-Z0-9_\\?|&]+\s*)?\{',
            re.MULTILINE,
        )
        for match in pattern.finditer(self.source_code):
            fn_name = match.group(1)
            if any(fn_name == m.name.split(".")[-1] for rec in self.records.values() for m in rec.methods):
                continue
            line = self._get_line_number(match.start())
            loc = SourceLocation(file_path=self.file_path, line=line, column=1)

            raw_params = match.group(2)
            param_names = [p.strip().split("$")[-1].split("=")[0].strip() for p in raw_params.split(",") if "$" in p]

            body = self._extract_balanced_braces_content(self.source_code, match.end() - 1)
            calls, r_vars, w_vars, m_vars = self._analyze_php_method_body(body)

            fn_model = FunctionModel(
                name=fn_name,
                namespace=self.namespace_name,
                location=loc,
                parameter_lists=[param_names],
                body_text=body,
                calls=sorted(set(calls)),
                invocations=self._extract_php_invocations(body, fn_name, line),
                flow_steps=self._extract_php_flow_steps(param_names, body, fn_name, line),
                reads_variables=sorted(set(r_vars)),
                writes_variables=sorted(set(w_vars)),
                modifies_variables=sorted(set(m_vars)),
                is_private=fn_name.startswith("_"),
            )
            self.functions[fn_name] = fn_model

    def _analyze_php_method_body(self, body: str) -> tuple[list[str], list[str], list[str], list[str]]:
        calls: list[str] = []
        reads: list[str] = []
        writes: list[str] = []
        modifies: list[str] = []

        # 1. Method calls: $this->foo(), $obj->bar(), Class::baz()
        for call_match in re.finditer(r'(?:\$([a-zA-Z0-9_]+)->|([a-zA-Z0-9_]+)::)([a-zA-Z0-9_]+)\s*\(', body):
            obj = call_match.group(1) or call_match.group(2)
            method = call_match.group(3)
            call_full = f"{obj}->{method}" if call_match.group(1) else f"{obj}::{method}"
            calls.append(call_full)
            if method in ("append", "push", "add", "attach", "detach", "set", "update"):
                modifies.append(obj)

        # 2. Standalone function calls: foo(...)
        for fn_call in re.finditer(r'\b([a-zA-Z0-9_]+)\s*\(', body):
            fn = fn_call.group(1)
            if fn not in _PHP_BUILTINS_AND_KEYWORDS and not fn.startswith("$"):
                calls.append(fn)

        # 3. Variable writes: $var = ..., $this->field = ...
        for w_match in re.finditer(r'\$([a-zA-Z0-9_]+(?:\s*->\s*[a-zA-Z0-9_]+)?)\s*=(?!=)', body):
            var_name = re.sub(r'\s+', '', w_match.group(1))
            writes.append(var_name)

        # 4. Variable reads: $varName
        for r_match in re.finditer(r'\$([a-zA-Z0-9_]+)', body):
            var = r_match.group(1)
            if var not in ("this", "_GET", "_POST", "_SESSION", "_SERVER", "_ENV"):
                reads.append(var)

        return calls, reads, writes, modifies

    def _extract_php_invocations(self, body: str, caller_name: str, parent_line: int) -> list[FunctionInvocation]:
        invocations: list[FunctionInvocation] = []
        call_pattern = re.compile(r'(?:\$([a-zA-Z0-9_]+)->|([a-zA-Z0-9_]+)::|(?:\b([a-zA-Z0-9_]+)))\s*\((.*?)\)', re.DOTALL)

        for match in call_pattern.finditer(body):
            target = match.group(1) or match.group(2) or match.group(3)
            if not target or target in _PHP_BUILTINS_AND_KEYWORDS:
                continue

            args_str = match.group(4).strip()
            args = [a.strip() for a in args_str.split(",") if a.strip()]
            line = parent_line + body.count("\n", 0, match.start())
            loc = SourceLocation(file_path=self.file_path, line=line, column=1)

            invocations.append(
                FunctionInvocation(
                    caller_name=caller_name,
                    target_name=target,
                    location=loc,
                    argument_count=len(args),
                    argument_snippets=args,
                )
            )
        return invocations

    def _extract_php_flow_steps(
        self, params: list[str], body: str, func_name: str, parent_line: int
    ) -> list[ExpressionFlowStep]:
        steps: list[ExpressionFlowStep] = []

        # 1. Parameter steps
        for p in params:
            steps.append(
                ExpressionFlowStep(
                    source_expr=f"param:${p}",
                    target_expr=f"${p}",
                    step_kind="param",
                    location=SourceLocation(file_path=self.file_path, line=parent_line, column=1),
                )
            )

        # 2. Assignment steps: $target = $source
        assign_pattern = re.compile(r'\$([a-zA-Z0-9_]+)\s*=\s*([^;]+);')
        for match in assign_pattern.finditer(body):
            target = f"${match.group(1)}"
            source = match.group(2).strip()
            line = parent_line + body.count("\n", 0, match.start())
            loc = SourceLocation(file_path=self.file_path, line=line, column=1)

            step_kind = "call" if "(" in source and ")" in source else "assign"
            steps.append(
                ExpressionFlowStep(
                    source_expr=source,
                    target_expr=target,
                    step_kind=step_kind,
                    location=loc,
                )
            )

        # 3. Return steps: return $expr;
        return_pattern = re.compile(r'\breturn\s+([^;]+);')
        for match in return_pattern.finditer(body):
            ret_expr = match.group(1).strip()
            line = parent_line + body.count("\n", 0, match.start())
            loc = SourceLocation(file_path=self.file_path, line=line, column=1)
            steps.append(
                ExpressionFlowStep(
                    source_expr=ret_expr,
                    target_expr=f"{func_name}.return",
                    step_kind="return",
                    location=loc,
                )
            )

        return steps

    def _extract_balanced_braces_content(self, text: str, start_brace_index: int) -> str:
        if start_brace_index < 0 or start_brace_index >= len(text) or text[start_brace_index] != "{":
            return ""
        depth = 1
        i = start_brace_index + 1
        n = len(text)

        while i < n and depth > 0:
            c = text[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return text[start_brace_index + 1 : i]
            elif c in ("'", '"'):
                # Skip string literal
                quote = c
                i += 1
                while i < n:
                    if text[i] == "\\" and i + 1 < n:
                        i += 2
                    elif text[i] == quote:
                        break
                    else:
                        i += 1
            i += 1

        return text[start_brace_index + 1 : i]


class PhpParserAdapter(ParserPort):
    """Outbound port adapter implementing high-performance PHP parsing for CodeModel."""

    def parse_source(self, source_code: str, file_path: str = "") -> NamespaceModel:
        """Parse single PHP file into a domain NamespaceModel."""
        extractor = _PhpSourceExtractor(file_path=file_path, source_code=source_code)
        extractor.extract()

        return NamespaceModel(
            name=extractor.namespace_name,
            file_path=file_path,
            docstring="",
            requires=extractor.requires,
            imports=extractor.imports,
            protocols=extractor.protocols,
            records=extractor.records,
            functions=extractor.functions,
            states=extractor.states,
        )

    def parse_sources(self, sources: dict[str, str], max_workers: int | None = None) -> CodeModel:
        """Parse multiple PHP files into a unified domain CodeModel."""
        model = CodeModel()
        if not sources:
            return model

        if len(sources) > 3:
            workers = max_workers or min(16, (os.cpu_count() or 4) * 2)
            with ThreadPoolExecutor(max_workers=workers) as executor:
                namespaces = list(
                    executor.map(
                        lambda item: self.parse_source(item[1], file_path=item[0]),
                        sources.items(),
                    )
                )
            for ns in namespaces:
                model.add_namespace(ns)
        else:
            for path, code in sources.items():
                ns = self.parse_source(code, file_path=path)
                model.add_namespace(ns)

        return model
