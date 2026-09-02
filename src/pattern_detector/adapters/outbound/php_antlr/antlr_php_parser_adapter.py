"""ANTLR4-based PHP AST Parser Adapter implementing ParserPort."""

from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from antlr4 import CommonTokenStream, InputStream, PredictionMode
from antlr4.error.ErrorListener import ErrorListener

from pattern_detector.adapters.outbound.php_antlr.generated import (
    PhpLexer,
    PhpParser,
    PhpParserVisitor,
)
from pattern_detector.adapters.outbound.php_ast.php_parser_adapter import _PhpSourceExtractor
from pattern_detector.domain.code_model import (
    CodeModel,
    FunctionModel,
    MethodSignature,
    NamespaceModel,
    ProtocolModel,
    RecordModel,
    StateModel,
)
from pattern_detector.domain.value_objects import SourceLocation
from pattern_detector.ports.outbound import ParserPort


class SilentErrorListener(ErrorListener):
    """Suppresses syntax error noise to keep parsing resilient on invalid tokens."""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  # type: ignore[no-untyped-def]
        pass


class PhpModelVisitor(PhpParserVisitor):
    """Walks the official ANTLR PHP AST and populates the domain NamespaceModel."""

    def __init__(self, file_path: str, source_code: str, token_stream: CommonTokenStream) -> None:
        super().__init__()
        self.file_path = file_path
        self.source_code = source_code
        self.token_stream = token_stream
        self.namespace_name = "global"
        self.imports: list[str] = []
        self.protocols: dict[str, ProtocolModel] = {}
        self.records: dict[str, RecordModel] = {}
        self.functions: dict[str, FunctionModel] = {}
        self.states: dict[str, StateModel] = {}
        self._helper = _PhpSourceExtractor(self.file_path, self.source_code)

    def _get_node_text(self, ctx: Any) -> str:
        if not ctx or not hasattr(ctx, "start") or not hasattr(ctx, "stop"):
            return ""
        try:
            return self.token_stream.getText(ctx.start, ctx.stop)
        except Exception:  # noqa: BLE001
            return ctx.getText()

    def _extract_params(self, formal_param_list_ctx: Any) -> list[str]:
        if not formal_param_list_ctx:
            return []
        params = []
        for p in formal_param_list_ctx.formalParameter():
            if p.variableInitializer() and p.variableInitializer().VarName():
                params.append(p.variableInitializer().VarName().getText().lstrip("$"))
        return params

    def visitNamespaceDeclaration(self, ctx: PhpParser.NamespaceDeclarationContext) -> Any:  # type: ignore[name-defined]
        if ctx.namespaceNameList():
            self.namespace_name = ctx.namespaceNameList().getText().replace("\\\\", ".").replace("\\", ".").strip(".")
        return self.visitChildren(ctx)

    def visitUseDeclaration(self, ctx: PhpParser.UseDeclarationContext) -> Any:  # type: ignore[name-defined]
        if ctx.useDeclarationContentList():
            for item in ctx.useDeclarationContentList().useDeclarationContent():
                self.imports.append(item.getText().replace("\\\\", ".").replace("\\", ".").strip("."))
        return self.visitChildren(ctx)

    def visitClassDeclaration(self, ctx: PhpParser.ClassDeclarationContext) -> Any:  # type: ignore[name-defined]
        # Interface declaration: Interface identifier typeParameterListInBrackets? (Extends interfaceList)?
        if ctx.Interface() is not None:
            iface_name = ctx.identifier().getText()
            line = ctx.start.line
            extends_list: list[str] = []
            if ctx.interfaceList():
                for ref in ctx.interfaceList().qualifiedStaticTypeRef():
                    extends_list.append(ref.getText().split("\\")[-1])

            methods: list[MethodSignature] = []
            if ctx.classStatement():
                for s in ctx.classStatement():
                    if s.Function_() is not None and s.identifier() is not None:
                        m_name = s.identifier().getText()
                        m_line = s.start.line
                        params = self._extract_params(s.formalParameterList())
                        methods.append(
                            MethodSignature(
                                name=m_name,
                                parameter_lists=[params] if params else [],
                                location=SourceLocation(file_path=self.file_path, line=m_line),
                            )
                        )

            proto = ProtocolModel(
                name=iface_name,
                namespace=self.namespace_name,
                location=SourceLocation(file_path=self.file_path, line=line),
                methods=methods,
            )
            self.protocols[iface_name] = proto
            return None

        # Class or Trait declaration
        if ctx.classEntryType() is not None:
            class_name = ctx.identifier().getText()
            line = ctx.start.line

            is_abstract = False
            if ctx.modifier() and ctx.modifier().Abstract() is not None:
                is_abstract = True

            implements: list[str] = []
            if ctx.Extends() and ctx.qualifiedStaticTypeRef():
                implements.append(ctx.qualifiedStaticTypeRef().getText().split("\\")[-1])
            if ctx.Implements() and ctx.interfaceList():
                for ref in ctx.interfaceList().qualifiedStaticTypeRef():
                    implements.append(ref.getText().split("\\")[-1])

            fields: list[str] = []
            methods: list[FunctionModel] = []
            has_instance_field = False
            has_get_instance = False

            if ctx.classStatement():
                for s in ctx.classStatement():
                    # Property declaration
                    if s.propertyModifiers() is not None and s.variableInitializer():
                        for v in s.variableInitializer():
                            if v.VarName():
                                f_name = v.VarName().getText().lstrip("$")
                                fields.append(f_name)
                                if f_name.lower() in ("instance", "_instance", "s_instance"):
                                    has_instance_field = True

                    # Method declaration
                    elif s.Function_() is not None and s.identifier() is not None:
                        m_name = s.identifier().getText()
                        m_line = s.start.line
                        params = self._extract_params(s.formalParameterList())

                        # Constructor promoted properties
                        if m_name == "__construct" and s.formalParameterList():
                            for p in s.formalParameterList().formalParameter():
                                if p.memberModifier() and p.variableInitializer() and p.variableInitializer().VarName():
                                    p_name = p.variableInitializer().VarName().getText().lstrip("$")
                                    if p_name not in fields:
                                        fields.append(p_name)

                        # Extract method body
                        m_body = ""
                        is_method_abstract = False
                        if s.methodBody():
                            if s.methodBody().blockStatement():
                                block_ctx = s.methodBody().blockStatement()
                                m_body = self._get_node_text(block_ctx)
                                if m_body.startswith("{") and m_body.endswith("}"):
                                    m_body = m_body[1:-1]
                            elif s.methodBody().SemiColon():
                                is_method_abstract = True

                        if s.memberModifiers() and any(m.Abstract() for m in s.memberModifiers().memberModifier()):
                            is_method_abstract = True

                        is_private = s.memberModifiers() is not None and any(
                            m.Private() for m in s.memberModifiers().memberModifier()
                        )

                        calls, r_vars, w_vars, m_vars = self._helper._analyze_php_method_body(m_body)
                        invocations = self._helper._extract_php_invocations(m_body, f"{class_name}.{m_name}", m_line)
                        flow_steps = self._helper._extract_php_flow_steps(
                            params, m_body, f"{class_name}.{m_name}", m_line
                        )

                        fn_model = FunctionModel(
                            name=f"{class_name}.{m_name}",
                            namespace=self.namespace_name,
                            location=SourceLocation(file_path=self.file_path, line=m_line),
                            parameter_lists=[params] if params else [],
                            body_text=m_body,
                            calls=sorted(set(calls)),
                            invocations=invocations,
                            flow_steps=flow_steps,
                            reads_variables=sorted(set(r_vars)),
                            writes_variables=sorted(set(w_vars)),
                            modifies_variables=sorted(set(m_vars)),
                            is_abstract=is_method_abstract,
                            is_private=is_private,
                        )
                        methods.append(fn_model)
                        self.functions[f"{class_name}.{m_name}"] = fn_model

                        if m_name.lower() in (
                            "getinstance",
                            "get_instance",
                            "getdefaultinstance",
                            "shared",
                            "sharedinstance",
                        ):
                            has_get_instance = True

            fields = list(dict.fromkeys(fields))
            rec = RecordModel(
                name=class_name,
                namespace=self.namespace_name,
                location=SourceLocation(file_path=self.file_path, line=line),
                fields=fields,
                implemented_protocols=implements,
                methods=methods,
            )
            self.records[class_name] = rec

            if is_abstract:
                pure_methods = [
                    MethodSignature(
                        name=m.name.split(".")[-1],
                        parameter_lists=m.parameter_lists,
                        location=m.location,
                    )
                    for m in methods
                    if m.is_abstract
                ]
                self.protocols[class_name] = ProtocolModel(
                    name=class_name,
                    namespace=self.namespace_name,
                    location=SourceLocation(file_path=self.file_path, line=line),
                    methods=pure_methods,
                )

            if has_instance_field and has_get_instance:
                state_key = f"{class_name}._instance"
                self.states[state_key] = StateModel(
                    name=state_key,
                    namespace=self.namespace_name,
                    location=SourceLocation(file_path=self.file_path, line=line),
                    kind="singleton_instance",
                    is_once=True,
                )
            return None

        return self.visitChildren(ctx)

    def visitEnumDeclaration(self, ctx: PhpParser.EnumDeclarationContext) -> Any:  # type: ignore[name-defined]
        enum_name = ctx.identifier().getText()
        line = ctx.start.line
        implements: list[str] = []
        if ctx.interfaceList():
            for ref in ctx.interfaceList().qualifiedStaticTypeRef():
                implements.append(ref.getText().split("\\")[-1])

        rec = RecordModel(
            name=enum_name,
            namespace=self.namespace_name,
            location=SourceLocation(file_path=self.file_path, line=line),
            is_type=True,
            implemented_protocols=implements,
        )
        self.records[enum_name] = rec
        return None

    def visitFunctionDeclaration(self, ctx: PhpParser.FunctionDeclarationContext) -> Any:  # type: ignore[name-defined]
        fn_name = ctx.identifier().getText()
        line = ctx.start.line
        params = self._extract_params(ctx.formalParameterList())

        body = ""
        if ctx.blockStatement():
            body = self._get_node_text(ctx.blockStatement())
            if body.startswith("{") and body.endswith("}"):
                body = body[1:-1]

        calls, r_vars, w_vars, m_vars = self._helper._analyze_php_method_body(body)
        invocations = self._helper._extract_php_invocations(body, fn_name, line)
        flow_steps = self._helper._extract_php_flow_steps(params, body, fn_name, line)

        fn_model = FunctionModel(
            name=fn_name,
            namespace=self.namespace_name,
            location=SourceLocation(file_path=self.file_path, line=line),
            parameter_lists=[params] if params else [],
            body_text=body,
            calls=sorted(set(calls)),
            invocations=invocations,
            flow_steps=flow_steps,
            reads_variables=sorted(set(r_vars)),
            writes_variables=sorted(set(w_vars)),
            modifies_variables=sorted(set(m_vars)),
        )
        self.functions[fn_name] = fn_model
        return None


class AntlrPhpParserAdapter(ParserPort):
    """ANTLR4-based PHP AST parser adapter."""

    def parse_source(self, source_code: str, file_path: str = "") -> NamespaceModel:
        if not source_code.strip():
            return NamespaceModel(
                name=self._derive_namespace_from_path(file_path),
                file_path=file_path,
            )

        try:
            input_stream = InputStream(source_code)
            lexer = PhpLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(SilentErrorListener())

            token_stream = CommonTokenStream(lexer)
            parser = PhpParser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(SilentErrorListener())
            parser._interp.predictionMode = PredictionMode.SLL

            try:
                tree = parser.htmlDocument()
            except Exception:  # noqa: BLE001
                token_stream.seek(0)
                parser.reset()
                parser._interp.predictionMode = PredictionMode.LL
                tree = parser.htmlDocument()

            visitor = PhpModelVisitor(file_path=file_path, source_code=source_code, token_stream=token_stream)
            visitor.visit(tree)

            ns_name = visitor.namespace_name
            if ns_name == "global":
                ns_name = self._derive_namespace_from_path(file_path)

            return NamespaceModel(
                name=ns_name,
                file_path=file_path,
                imports=visitor.imports,
                requires=visitor.imports,
                protocols=visitor.protocols,
                records=visitor.records,
                functions=visitor.functions,
                states=visitor.states,
            )
        except Exception:  # noqa: BLE001
            # Fallback to empty namespace on parse failure
            return NamespaceModel(
                name=self._derive_namespace_from_path(file_path),
                file_path=file_path,
            )

    def parse_sources(self, sources: dict[str, str]) -> CodeModel:
        model = CodeModel()
        max_workers = min(32, max(4, os.cpu_count() or 4))

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_path = {executor.submit(self.parse_source, code, path): path for path, code in sources.items()}
            for future in future_to_path:
                ns_model = future.result()
                model.add_namespace(ns_model)

        return model

    def _derive_namespace_from_path(self, file_path: str) -> str:
        if not file_path:
            return "global"
        base = os.path.splitext(os.path.basename(file_path))[0]
        return base or "global"
