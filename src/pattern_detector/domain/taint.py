"""Taint Analysis Domain Models, Source/Sink Catalog, and Vulnerability Flow Definitions."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from pattern_detector.domain.value_objects import SourceLocation


class TaintCategory(str, Enum):
    """Categories of security and architectural taint vulnerabilities."""

    SQL_INJECTION = "sql_injection"
    COMMAND_INJECTION = "command_injection"
    CODE_INJECTION = "code_injection"
    PATH_TRAVERSAL = "path_traversal"
    SSRF = "ssrf"
    SENSITIVE_DATA_LEAK = "sensitive_data_leak"
    UNVALIDATED_INPUT = "unvalidated_input"


@dataclass(frozen=True)
class TaintSourcePattern:
    """Pattern identifying an untrusted or sensitive data entrypoint."""

    pattern: str  # substring or regex matching variable, attribute, or call
    category: TaintCategory
    description: str
    is_sensitive: bool = False


@dataclass(frozen=True)
class TaintSinkPattern:
    """Pattern identifying a dangerous operation or sensitive sink."""

    pattern: str  # function or method name (e.g. 'cursor.execute', 'subprocess.run')
    category: TaintCategory
    severity: str  # 'CRITICAL', 'HIGH', 'MEDIUM'
    cwe_id: str  # e.g. 'CWE-89'
    description: str


# Standard PHP Taint Sources Catalog
DEFAULT_TAINT_SOURCES: tuple[TaintSourcePattern, ...] = (
    # Superglobals & HTTP Inputs
    TaintSourcePattern("$_GET", TaintCategory.UNVALIDATED_INPUT, "PHP $_GET query parameters"),
    TaintSourcePattern("$_POST", TaintCategory.UNVALIDATED_INPUT, "PHP $_POST form payload"),
    TaintSourcePattern("$_REQUEST", TaintCategory.UNVALIDATED_INPUT, "PHP $_REQUEST parameters"),
    TaintSourcePattern("$_COOKIE", TaintCategory.UNVALIDATED_INPUT, "PHP $_COOKIE request cookies"),
    TaintSourcePattern("$_SERVER", TaintCategory.UNVALIDATED_INPUT, "PHP $_SERVER environment and headers"),
    TaintSourcePattern("$_FILES", TaintCategory.UNVALIDATED_INPUT, "PHP $_FILES uploaded file data"),
    # Framework Inputs (Laravel, Symfony, PSR-7)
    TaintSourcePattern("$request->input", TaintCategory.UNVALIDATED_INPUT, "Laravel Request input payload"),
    TaintSourcePattern("$request->query", TaintCategory.UNVALIDATED_INPUT, "Request query parameters"),
    TaintSourcePattern("$request->get", TaintCategory.UNVALIDATED_INPUT, "Request parameter lookup"),
    TaintSourcePattern("$request->all", TaintCategory.UNVALIDATED_INPUT, "All request input parameters"),
    TaintSourcePattern("$request->getQueryParams", TaintCategory.UNVALIDATED_INPUT, "PSR-7 query parameters"),
    TaintSourcePattern("$request->getParsedBody", TaintCategory.UNVALIDATED_INPUT, "PSR-7 parsed request body"),
    TaintSourcePattern("$request->getHeaders", TaintCategory.UNVALIDATED_INPUT, "PSR-7 request headers"),
    # CLI & Environment
    TaintSourcePattern("$argv", TaintCategory.UNVALIDATED_INPUT, "Command-line arguments array"),
    TaintSourcePattern("getenv", TaintCategory.UNVALIDATED_INPUT, "Environment variable lookup"),
    TaintSourcePattern("$_ENV", TaintCategory.UNVALIDATED_INPUT, "Environment superglobal array"),
    TaintSourcePattern("php://input", TaintCategory.UNVALIDATED_INPUT, "Raw HTTP request body stream"),
    # Sensitive Data Sources
    TaintSourcePattern("password", TaintCategory.SENSITIVE_DATA_LEAK, "Sensitive password field", is_sensitive=True),
    TaintSourcePattern("token", TaintCategory.SENSITIVE_DATA_LEAK, "Sensitive authentication token", is_sensitive=True),
    TaintSourcePattern("api_key", TaintCategory.SENSITIVE_DATA_LEAK, "Sensitive API key secret", is_sensitive=True),
    TaintSourcePattern("secret_key", TaintCategory.SENSITIVE_DATA_LEAK, "Cryptographic master key", is_sensitive=True),
    TaintSourcePattern("auth_header", TaintCategory.SENSITIVE_DATA_LEAK, "Authorization bearer header", is_sensitive=True),
    TaintSourcePattern("credit_card", TaintCategory.SENSITIVE_DATA_LEAK, "Payment card information", is_sensitive=True),
)

# Standard PHP Taint Sinks Catalog
DEFAULT_TAINT_SINKS: tuple[TaintSinkPattern, ...] = (
    # SQL Injection Sinks
    TaintSinkPattern("mysqli_query", TaintCategory.SQL_INJECTION, "CRITICAL", "CWE-89", "MySQLi Raw Query Execution"),
    TaintSinkPattern("mysql_query", TaintCategory.SQL_INJECTION, "CRITICAL", "CWE-89", "Legacy MySQL Query Execution"),
    TaintSinkPattern("PDO::query", TaintCategory.SQL_INJECTION, "CRITICAL", "CWE-89", "PDO Raw SQL Query Execution"),
    TaintSinkPattern("PDO::exec", TaintCategory.SQL_INJECTION, "CRITICAL", "CWE-89", "PDO Raw SQL Statement Execution"),
    TaintSinkPattern("DB::raw", TaintCategory.SQL_INJECTION, "HIGH", "CWE-89", "Laravel DB::raw Query Expression"),
    TaintSinkPattern("DB::select", TaintCategory.SQL_INJECTION, "HIGH", "CWE-89", "Laravel DB::select Query Execution"),
    # Command Injection Sinks
    TaintSinkPattern("system", TaintCategory.COMMAND_INJECTION, "CRITICAL", "CWE-78", "Direct Shell Command Execution"),
    TaintSinkPattern("exec", TaintCategory.COMMAND_INJECTION, "CRITICAL", "CWE-78", "Command Execution"),
    TaintSinkPattern("passthru", TaintCategory.COMMAND_INJECTION, "CRITICAL", "CWE-78", "Raw Command Passthrough"),
    TaintSinkPattern("shell_exec", TaintCategory.COMMAND_INJECTION, "CRITICAL", "CWE-78", "Shell Command Execution via Backticks"),
    TaintSinkPattern("proc_open", TaintCategory.COMMAND_INJECTION, "CRITICAL", "CWE-78", "Process Resource Open"),
    TaintSinkPattern("popen", TaintCategory.COMMAND_INJECTION, "HIGH", "CWE-78", "Piped Command Execution"),
    # Code Injection Sinks
    TaintSinkPattern("eval", TaintCategory.CODE_INJECTION, "CRITICAL", "CWE-94", "Dynamic PHP Code Evaluation"),
    TaintSinkPattern("unserialize", TaintCategory.CODE_INJECTION, "CRITICAL", "CWE-502", "Unsafe Object Deserialization"),
    TaintSinkPattern("assert", TaintCategory.CODE_INJECTION, "HIGH", "CWE-94", "Dynamic String Assertion Evaluation"),
    TaintSinkPattern("create_function", TaintCategory.CODE_INJECTION, "CRITICAL", "CWE-94", "Anonymous Function Creation from String"),
    # Path Traversal & Inclusion Sinks
    TaintSinkPattern("include", TaintCategory.PATH_TRAVERSAL, "CRITICAL", "CWE-98", "Dynamic File Inclusion (LFI/RFI)"),
    TaintSinkPattern("require", TaintCategory.PATH_TRAVERSAL, "CRITICAL", "CWE-98", "Dynamic File Requirement (LFI/RFI)"),
    TaintSinkPattern("include_once", TaintCategory.PATH_TRAVERSAL, "CRITICAL", "CWE-98", "Dynamic File Inclusion Once"),
    TaintSinkPattern("require_once", TaintCategory.PATH_TRAVERSAL, "CRITICAL", "CWE-98", "Dynamic File Requirement Once"),
    TaintSinkPattern("file_get_contents", TaintCategory.PATH_TRAVERSAL, "HIGH", "CWE-22", "Arbitrary File Read"),
    TaintSinkPattern("file_put_contents", TaintCategory.PATH_TRAVERSAL, "HIGH", "CWE-22", "Arbitrary File Write"),
    TaintSinkPattern("unlink", TaintCategory.PATH_TRAVERSAL, "HIGH", "CWE-22", "File Deletion"),
    TaintSinkPattern("fopen", TaintCategory.PATH_TRAVERSAL, "MEDIUM", "CWE-22", "File Pointer Open"),
    # SSRF Sinks
    TaintSinkPattern("curl_exec", TaintCategory.SSRF, "HIGH", "CWE-918", "cURL Network Resource Request (SSRF)"),
    TaintSinkPattern("file_get_contents_http", TaintCategory.SSRF, "HIGH", "CWE-918", "HTTP URL File Fetch (SSRF)"),
    # Sensitive Data Leak Sinks (Logging / Output)
    TaintSinkPattern("Log::info", TaintCategory.SENSITIVE_DATA_LEAK, "MEDIUM", "CWE-532", "Sensitive Information in System Log"),
    TaintSinkPattern("Log::error", TaintCategory.SENSITIVE_DATA_LEAK, "MEDIUM", "CWE-532", "Sensitive Information in Error Log"),
    TaintSinkPattern("error_log", TaintCategory.SENSITIVE_DATA_LEAK, "MEDIUM", "CWE-532", "PHP Error Log Output"),
    TaintSinkPattern("var_dump", TaintCategory.SENSITIVE_DATA_LEAK, "LOW", "CWE-532", "Variable Dump Output"),
    TaintSinkPattern("print_r", TaintCategory.SENSITIVE_DATA_LEAK, "LOW", "CWE-532", "Print Representation Output"),
    TaintSinkPattern("echo", TaintCategory.SENSITIVE_DATA_LEAK, "LOW", "CWE-532", "Direct Output of Sensitive Variable"),
)


@dataclass
class TaintFlowStep:
    """Represents an atomic transition step in a taint propagation path."""

    step_number: int
    expression: str
    kind: str  # 'SOURCE', 'ASSIGN', 'ACCESS_PATH', 'ARGUMENT', 'PARAM_BIND', 'RETURNS_TO', 'SINK'
    location: SourceLocation | None = None
    description: str = ""


@dataclass
class TaintFlow:
    """Represents a validated end-to-end vulnerability flow from Source to Sink."""

    id: str
    category: TaintCategory
    severity: str
    cwe_id: str
    source_expr: str
    sink_target: str
    primary_location: SourceLocation
    steps: list[TaintFlowStep] = field(default_factory=list)
    summary: str = ""
    remediation_hint: str = ""


@dataclass
class TaintFlowRequest:
    """Parameter Object capturing all inputs needed to build a TaintFlow.

    Replaces the 6-parameter signature of _build_taint_flow, reducing cognitive
    load and making call-sites explicit and extensible (KISS / Parameter Object).
    """

    src_name: str
    src_pattern: TaintSourcePattern
    sink_id: str
    sink_pattern: TaintSinkPattern
    path_graph: object  # DataFlowGraph — kept as object to avoid circular import
    src_loc: SourceLocation
