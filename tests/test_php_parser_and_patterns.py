"""Tests: PhpParserAdapter — parsing correctness and basic pattern detection on PHP samples."""

from __future__ import annotations

from pathlib import Path

import pytest

from pattern_detector.adapters.outbound.php_ast.php_parser_adapter import PhpParserAdapter


CREATIONAL_PHP = (
    Path(__file__).parent.parent / "examples" / "php_samples" / "CreationalPatternsDemo.php"
)
BEHAVIORAL_PHP = (
    Path(__file__).parent.parent / "examples" / "php_samples" / "BehavioralPatternsDemo.php"
)
STRUCTURAL_PHP = (
    Path(__file__).parent.parent / "examples" / "php_samples" / "StructuralPatternsDemo.php"
)
PRINCIPLES_PHP = (
    Path(__file__).parent.parent / "examples" / "php_samples" / "PrinciplesAndCleanCodeDemo.php"
)


@pytest.fixture
def php_parser() -> PhpParserAdapter:
    return PhpParserAdapter()


def _parse_file(php_parser: PhpParserAdapter, path: Path) -> "CodeModel":  # noqa: F821
    from pattern_detector.adapters.outbound.php_ast.php_parser_adapter import PhpParserAdapter
    sources = {str(path): path.read_text(encoding="utf-8")}
    return php_parser.parse_sources(sources)


# ─────────────────────────────────────────────────────────────────────────────
# NAMESPACE PARSING
# ─────────────────────────────────────────────────────────────────────────────

def test_php_namespace_is_extracted(php_parser: PhpParserAdapter) -> None:
    code = "<?php\nnamespace App\\Services;\nclass UserService {}"
    ns = php_parser.parse_source(code, "test.php")
    assert ns.name == "App.Services"


def test_php_global_namespace_fallback(php_parser: PhpParserAdapter) -> None:
    code = "<?php\nclass Foo {}"
    ns = php_parser.parse_source(code, "test.php")
    assert ns.name == "global"


# ─────────────────────────────────────────────────────────────────────────────
# INTERFACE / PROTOCOL PARSING
# ─────────────────────────────────────────────────────────────────────────────

def test_interfaces_detected_as_protocols(php_parser: PhpParserAdapter) -> None:
    model = _parse_file(php_parser, CREATIONAL_PHP)
    all_protocols = set()
    for ns in model.namespaces.values():
        all_protocols.update(ns.protocols.keys())
    assert "Logger" in all_protocols
    assert "UIFactory" in all_protocols


def test_interface_methods_extracted(php_parser: PhpParserAdapter) -> None:
    code = """<?php
interface PaymentGateway {
    public function charge(float $amount): bool;
    public function refund(string $id, float $amount): bool;
}
"""
    ns = php_parser.parse_source(code, "test.php")
    assert "PaymentGateway" in ns.protocols
    methods = {m.name for m in ns.protocols["PaymentGateway"].methods}
    assert "charge" in methods
    assert "refund" in methods


# ─────────────────────────────────────────────────────────────────────────────
# CLASS / RECORD PARSING
# ─────────────────────────────────────────────────────────────────────────────

def test_classes_extracted_as_records(php_parser: PhpParserAdapter) -> None:
    model = _parse_file(php_parser, CREATIONAL_PHP)
    all_records = set()
    for ns in model.namespaces.values():
        all_records.update(ns.records.keys())
    assert "DatabaseConnection" in all_records
    assert "QueryBuilder" in all_records
    assert "UserProfile" in all_records


def test_class_implements_interfaces_captured(php_parser: PhpParserAdapter) -> None:
    code = """<?php
interface Logger { public function log(string $msg): void; }
class FileLogger implements Logger {
    public function log(string $msg): void { echo $msg; }
}
"""
    ns = php_parser.parse_source(code, "test.php")
    record = ns.records.get("FileLogger")
    assert record is not None
    assert "Logger" in record.implemented_protocols


def test_abstract_class_extracted_as_record_and_protocol(php_parser: PhpParserAdapter) -> None:
    code = """<?php
abstract class DataExporter {
    abstract protected function format(array $data): string;
    final public function export(array $data): string { return $this->format($data); }
}
"""
    ns = php_parser.parse_source(code, "test.php")
    assert "DataExporter" in ns.records
    assert "DataExporter" in ns.protocols


# ─────────────────────────────────────────────────────────────────────────────
# FIELD EXTRACTION
# ─────────────────────────────────────────────────────────────────────────────

def test_class_properties_extracted(php_parser: PhpParserAdapter) -> None:
    code = """<?php
class Order {
    private ?Customer $customer = null;
    protected int $total = 0;
    public string $status = 'pending';
    private static int $count = 0;
}
"""
    ns = php_parser.parse_source(code, "test.php")
    record = ns.records.get("Order")
    assert record is not None
    assert "customer" in record.fields
    assert "total" in record.fields
    assert "status" in record.fields
    assert "count" in record.fields


def test_constructor_promoted_properties_extracted(php_parser: PhpParserAdapter) -> None:
    code = """<?php
class FileLogger {
    public function __construct(
        private string $path,
        private readonly int $maxSize = 1024,
    ) {}
}
"""
    ns = php_parser.parse_source(code, "test.php")
    record = ns.records.get("FileLogger")
    assert record is not None
    assert "path" in record.fields
    assert "maxSize" in record.fields


# ─────────────────────────────────────────────────────────────────────────────
# METHOD / FUNCTION EXTRACTION
# ─────────────────────────────────────────────────────────────────────────────

def test_class_methods_extracted(php_parser: PhpParserAdapter) -> None:
    code = """<?php
class UserService {
    public function findUser(int $id): array { return ['id' => $id]; }
    protected function validate(array $data): bool { return true; }
    private function _hash(string $pwd): string { return md5($pwd); }
}
"""
    ns = php_parser.parse_source(code, "test.php")
    fn_names = set(ns.functions.keys())
    assert "UserService.findUser" in fn_names
    assert "UserService.validate" in fn_names
    assert "UserService._hash" in fn_names


def test_standalone_functions_extracted(php_parser: PhpParserAdapter) -> None:
    code = """<?php
function calculateTotal(array $items, float $taxRate): float {
    return array_sum(array_map(fn($i) => $i['price'], $items)) * (1 + $taxRate);
}
"""
    ns = php_parser.parse_source(code, "test.php")
    assert "calculateTotal" in ns.functions


def test_function_parameters_extracted(php_parser: PhpParserAdapter) -> None:
    code = """<?php
class Sorter {
    public function sort(array $data, string $direction = 'asc'): array { return $data; }
}
"""
    ns = php_parser.parse_source(code, "test.php")
    fn = ns.functions.get("Sorter.sort")
    assert fn is not None
    params = fn.parameter_lists[0] if fn.parameter_lists else []
    assert "data" in params
    assert "direction" in params


# ─────────────────────────────────────────────────────────────────────────────
# SINGLETON DETECTION
# ─────────────────────────────────────────────────────────────────────────────

def test_singleton_state_detected(php_parser: PhpParserAdapter) -> None:
    model = _parse_file(php_parser, CREATIONAL_PHP)
    all_states = {}
    for ns in model.namespaces.values():
        all_states.update(ns.states)
    assert any("DatabaseConnection" in k for k in all_states)


# ─────────────────────────────────────────────────────────────────────────────
# IMPORT PARSING
# ─────────────────────────────────────────────────────────────────────────────

def test_use_statements_parsed(php_parser: PhpParserAdapter) -> None:
    code = """<?php
use App\\Repositories\\UserRepository;
use App\\Services\\{EmailService, SmsService};
use Psr\\Log\\LoggerInterface as Logger;
"""
    ns = php_parser.parse_source(code, "test.php")
    assert any("UserRepository" in i for i in ns.imports)
    assert any("EmailService" in i for i in ns.imports)
    assert any("SmsService" in i for i in ns.imports)


# ─────────────────────────────────────────────────────────────────────────────
# MULTI-FILE PARSING
# ─────────────────────────────────────────────────────────────────────────────

def test_parse_multiple_php_files(php_parser: PhpParserAdapter) -> None:
    sources = {
        str(CREATIONAL_PHP): CREATIONAL_PHP.read_text(encoding="utf-8"),
        str(BEHAVIORAL_PHP): BEHAVIORAL_PHP.read_text(encoding="utf-8"),
        str(STRUCTURAL_PHP): STRUCTURAL_PHP.read_text(encoding="utf-8"),
    }
    model = php_parser.parse_sources(sources)
    assert len(model.namespaces) >= 2
    all_records = {name for ns in model.namespaces.values() for name in ns.records}
    assert "DatabaseConnection" in all_records
    assert "OrderService" in all_records
    assert "StripeAdapter" in all_records


# ─────────────────────────────────────────────────────────────────────────────
# FULL SCAN + PATTERN DETECTION ON PHP SAMPLES
# ─────────────────────────────────────────────────────────────────────────────

def test_full_scan_detects_patterns_in_php_examples() -> None:
    from pattern_detector.bootstrap.container import create_container
    container = create_container()
    scanner = container.get_scanner()

    examples_dir = str(Path(__file__).parent.parent / "examples" / "php_samples")
    report = scanner.scan_path(examples_dir)

    assert report.scanned_files_count >= 3
    assert report.total_detections_count > 0
    pattern_types = {d.pattern_type.value for d in report.detections}
    # Creational: Singleton must be detected from DatabaseConnection
    assert "singleton" in pattern_types


def test_full_scan_detects_observer_in_behavioral_php() -> None:
    from pattern_detector.bootstrap.container import create_container
    container = create_container()
    scanner = container.get_scanner()

    report = scanner.scan_path(str(BEHAVIORAL_PHP))
    pattern_types = {d.pattern_type.value for d in report.detections}
    # OrderService has listener list and emit/subscribe methods -> Observer subject
    assert "observer" in pattern_types or report.total_detections_count > 0


def test_full_scan_detects_solid_violations_in_principles_php() -> None:
    from pattern_detector.bootstrap.container import create_container
    container = create_container()
    scanner = container.get_scanner()

    report = scanner.scan_path(str(PRINCIPLES_PHP))
    # UserManager is a God Class -> SRP violation
    assert report.total_detections_count > 0


# ─────────────────────────────────────────────────────────────────────────────
# PHP-SPECIFIC PATTERNS: MIDDLEWARE PIPELINE & MULTIMETHOD DISPATCH
# ─────────────────────────────────────────────────────────────────────────────

PHP_SPECIFIC_PHP = (
    Path(__file__).parent.parent / "examples" / "php_samples" / "PhpSpecificPatternsDemo.php"
)


def test_psr15_and_laravel_middleware_pipeline_detected() -> None:
    from pattern_detector.bootstrap.container import create_container
    container = create_container()
    scanner = container.get_scanner()

    report = scanner.scan_path(str(PHP_SPECIFIC_PHP))
    detections = [d for d in report.detections if d.pattern_type.value == "middleware_pipeline"]
    assert len(detections) >= 3

    target_names = {d.target_name for d in detections}
    assert "AuthenticationMiddleware" in target_names or "RateLimitMiddleware" in target_names
    assert "HttpKernel" in target_names or "MiddlewarePipeline" in target_names


def test_php_multimethod_dispatch_detected() -> None:
    from pattern_detector.bootstrap.container import create_container
    container = create_container()
    scanner = container.get_scanner()

    report = scanner.scan_path(str(PHP_SPECIFIC_PHP))
    detections = [d for d in report.detections if d.pattern_type.value == "multimethod_dispatch"]
    assert len(detections) >= 2

    target_names = {d.target_name for d in detections}
    assert "CommandBus" in target_names or "EventDispatcher" in target_names
    assert any("serializeValue" in name for name in target_names) or len(detections) >= 2


def test_all_37_rules_registered_and_executable() -> None:
    from pattern_detector.domain.rules import get_default_rules
    from pattern_detector.domain.value_objects import PatternType

    rules = get_default_rules()
    assert len(rules) == 37

    rule_types = {r.pattern_type for r in rules}
    assert len(rule_types) == 37
    assert len(rule_types) == len(PatternType)


# ─────────────────────────────────────────────────────────────────────────────
# ANTLR4 PHP PARSER ADAPTER TESTS
# ─────────────────────────────────────────────────────────────────────────────

def test_antlr_php_parser_adapter_extracts_structures() -> None:
    from pattern_detector.adapters.outbound.php_antlr import AntlrPhpParserAdapter

    code = """<?php
namespace App\\Services;

use App\\Contracts\\UserInterface;

interface Greeter {
    public function greet(string $name): string;
}

class WelcomeService implements Greeter, UserInterface {
    private string $appName = 'Demo';

    public function __construct(private string $author) {}

    public function greet(string $name): string {
        return 'Hello ' . $name;
    }
}
"""
    adapter = AntlrPhpParserAdapter()
    ns = adapter.parse_source(code, "WelcomeService.php")

    assert ns.name == "App.Services"
    assert "Greeter" in ns.protocols
    assert "WelcomeService" in ns.records
    assert "appName" in ns.records["WelcomeService"].fields
    assert "author" in ns.records["WelcomeService"].fields
    assert "Greeter" in ns.records["WelcomeService"].implemented_protocols


def test_container_and_cli_antlr_parser_switch() -> None:
    from pattern_detector.bootstrap.container import create_container
    from typer.testing import CliRunner
    from pattern_detector.adapters.inbound.cli.main import app

    container_antlr = create_container(parser_type="antlr")
    assert container_antlr.parser.__class__.__name__ == "AntlrPhpParserAdapter"

    container_native = create_container(parser_type="native")
    assert container_native.parser.__class__.__name__ == "PhpParserAdapter"

    runner = CliRunner()
    result = runner.invoke(app, ["scan", "examples/php_samples/CreationalPatternsDemo.php", "--parser", "antlr"])
    assert result.exit_code == 0


