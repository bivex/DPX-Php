"""ANTLR4-based PHP AST Parser Adapter implementing ParserPort."""

from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from pattern_detector.adapters.outbound.php_antlr.generated.PHPLexer import PHPLexer
from pattern_detector.adapters.outbound.php_antlr.generated.PHPParser import PHPParser
from pattern_detector.adapters.outbound.php_antlr.generated.PHPParserVisitor import PHPParserVisitor
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


class SilentErrorListener(ErrorListener):
    """Suppresses syntax error noise to keep parsing resilient on invalid tokens."""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):  # type: ignore[no-untyped-def]
        pass


class PhpModelVisitor(PHPParserVisitor):
    """Walks the ANTLR PHP AST and populates the domain NamespaceModel."""

    def __init__(self, file_path: str, source_code: str) -> None:
        super().__init__()
        self.file_path = file_path
        self.source_code = source_code
        self.namespace_name = "global"
        self.imports: list[str] = []
        self.protocols: dict[str, ProtocolModel] = {}
        self.records: dict[str, RecordModel] = {}
        self.functions: dict[str, FunctionModel] = {}
        self.states: dict[str, StateModel] = {}
        self.current_class: str | None = None

    def visitNamespaceStatement(self, ctx: PHPParser.NamespaceStatementContext) -> Any:  # type: ignore[name-defined]
        if ctx.qualifiedName():
            self.namespace_name = ctx.qualifiedName().getText().replace("\\", ".")
        return self.visitChildren(ctx)

    def visitUseStatement(self, ctx: PHPParser.UseStatementContext) -> Any:  # type: ignore[name-defined]
        if ctx.useDeclarationList():
            for item in ctx.useDeclarationList().useItem():
                self.imports.append(item.getText().replace("\\", "."))
        return self.visitChildren(ctx)

    def visitInterfaceDeclaration(self, ctx: PHPParser.InterfaceDeclarationContext) -> Any:  # type: ignore[name-defined]
        iface_name = ctx.IDENTIFIER().getText()
        line = ctx.start.line
        methods: list[MethodSignature] = []

        if ctx.classMember():
            for m in ctx.classMember():
                if m.methodDeclaration():
                    m_ctx = m.methodDeclaration()
                    m_name = m_ctx.methodName().getText()
                    m_line = m_ctx.start.line
                    m_params = self._extract_params(m_ctx.parameterList())
                    methods.append(
                        MethodSignature(
                            name=m_name,
                            parameter_lists=[m_params] if m_params else [],
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
        return self.visitChildren(ctx)

    def visitClassDeclaration(self, ctx: PHPParser.ClassDeclarationContext) -> Any:  # type: ignore[name-defined]
        class_name = ctx.IDENTIFIER().getText()
        line = ctx.start.line
        self.current_class = class_name

        # Extends & implements
        implements: list[str] = []
        if ctx.EXTENDS() and ctx.qualifiedName():
            implements.append(ctx.qualifiedName().getText().split("\\")[-1])
        if ctx.IMPLEMENTS() and ctx.qualifiedNameList():
            for qn in ctx.qualifiedNameList().qualifiedName():
                implements.append(qn.getText().split("\\")[-1])

        # Check modifiers
        is_abstract = False
        if ctx.classModifier():
            for mod in ctx.classModifier():
                if mod.ABSTRACT():
                    is_abstract = True

        fields: list[str] = []
        methods: list[FunctionModel] = []
        has_instance_field = False
        has_get_instance = False

        if ctx.classMember():
            for m in ctx.classMember():
                if m.propertyDeclaration():
                    p_ctx = m.propertyDeclaration()
                    for v in p_ctx.VARIABLE():
                        f_name = v.getText().lstrip("$")
                        fields.append(f_name)
                        if f_name.lower() in ("instance", "_instance"):
                            has_instance_field = True
                elif m.methodDeclaration():
                    m_ctx = m.methodDeclaration()
                    m_name = m_ctx.methodName().getText()
                    m_line = m_ctx.start.line
                    m_params = self._extract_params(m_ctx.parameterList())
                    m_body = m_ctx.getText()

                    # Constructor promoted properties
                    if m_name == "__construct" and m_ctx.parameterList():
                        for p in m_ctx.parameterList().parameter():
                            if p.memberModifier():
                                p_var = p.VARIABLE().getText().lstrip("$")
                                if p_var not in fields:
                                    fields.append(p_var)

                    if m_name.lower() in ("getinstance", "get_instance", "getdefaultinstance"):
                        has_get_instance = True

                    fn_model = FunctionModel(
                        name=f"{class_name}.{m_name}",
                        namespace=self.namespace_name,
                        location=SourceLocation(file_path=self.file_path, line=m_line),
                        parameter_lists=[m_params] if m_params else [],
                        body_text=m_body,
                    )
                    methods.append(fn_model)
                    self.functions[f"{class_name}.{m_name}"] = fn_model

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
            sig_methods = [
                MethodSignature(
                    name=m.name.split(".")[-1],
                    parameter_lists=m.parameter_lists,
                    location=m.location,
                )
                for m in methods
            ]
            proto = ProtocolModel(
                name=class_name,
                namespace=self.namespace_name,
                location=SourceLocation(file_path=self.file_path, line=line),
                methods=sig_methods,
            )
            self.protocols[class_name] = proto

        if has_instance_field and has_get_instance:
            state_key = f"{class_name}._instance"
            self.states[state_key] = StateModel(
                name=state_key,
                namespace=self.namespace_name,
                location=SourceLocation(file_path=self.file_path, line=line),
                kind="singleton_instance",
                is_once=True,
            )

        self.current_class = None
        return self.visitChildren(ctx)

    def visitFunctionDeclaration(self, ctx: PHPParser.FunctionDeclarationContext) -> Any:  # type: ignore[name-defined]
        fn_name = ctx.IDENTIFIER().getText()
        line = ctx.start.line
        params = self._extract_params(ctx.parameterList())
        body = ctx.getText()

        fn_model = FunctionModel(
            name=fn_name,
            namespace=self.namespace_name,
            location=SourceLocation(file_path=self.file_path, line=line),
            parameter_lists=[params] if params else [],
            body_text=body,
        )
        self.functions[fn_name] = fn_model
        return self.visitChildren(ctx)

    def _extract_params(self, param_list_ctx: Any) -> list[str]:
        if not param_list_ctx:
            return []
        params = []
        for p in param_list_ctx.parameter():
            if p.VARIABLE():
                params.append(p.VARIABLE().getText().lstrip("$"))
        return params


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
            lexer = PHPLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(SilentErrorListener())

            token_stream = CommonTokenStream(lexer)
            parser = PHPParser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(SilentErrorListener())

            tree = parser.phpFile()
            visitor = PhpModelVisitor(file_path=file_path, source_code=source_code)
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
        except Exception:
            # Fallback to empty namespace on parse failure
            return NamespaceModel(
                name=self._derive_namespace_from_path(file_path),
                file_path=file_path,
            )

    def parse_sources(self, sources: dict[str, str]) -> CodeModel:
        model = CodeModel()
        max_workers = min(32, max(4, os.cpu_count() or 4))

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_path = {
                executor.submit(self.parse_source, code, path): path
                for path, code in sources.items()
            }
            for future in future_to_path:
                ns_model = future.result()
                model.add_namespace(ns_model)

        return model

    def _derive_namespace_from_path(self, file_path: str) -> str:
        if not file_path:
            return "global"
        base = os.path.splitext(os.path.basename(file_path))[0]
        return base or "global"
