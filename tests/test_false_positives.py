"""Comprehensive False Positives Test Suite for DPX-Php.

Verifies that ordinary, standard PHP idioms (DTOs, Value Objects, Readonly Classes,
Pure Utilities, Data Structures, Custom Exceptions, Enums, and Clean Architecture Services)
do not produce false positive detections for Design Patterns or SOLID Principle violations.
"""

from __future__ import annotations

from pathlib import Path

from pattern_detector.adapters.outbound.php_ast.php_parser_adapter import PhpParserAdapter
from pattern_detector.bootstrap.container import create_container
from pattern_detector.domain.detection import DetectionReport
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.services.pattern_detector import PatternDetectorService
from pattern_detector.domain.value_objects import ConfidenceLevel, PatternType

FALSE_POSITIVES_DEMO_PHP = (
    Path(__file__).parent.parent / "examples" / "php_samples" / "FalsePositivesDemo.php"
)
BENCHMARKS_FALSE_POS_DIR = (
    Path(__file__).parent.parent / "benchmarks" / "false_positives"
)


def _scan_snippet(code_map: dict[str, str]) -> DetectionReport:
    adapter = PhpParserAdapter()
    model = adapter.parse_sources(code_map)
    detector = PatternDetectorService(rules=get_default_rules())
    return detector.detect_all(model)


def test_clean_benchmarks_false_positives_project_native_parser() -> None:
    container = create_container(parser_type="native")
    scanner = container.get_scanner()
    report = scanner.scan_path(str(BENCHMARKS_FALSE_POS_DIR))
    assert report.scanned_files_count >= 10
    assert report.total_detections_count == 0


def test_clean_benchmarks_false_positives_project_antlr_parser() -> None:
    container = create_container(parser_type="antlr")
    scanner = container.get_scanner()
    report = scanner.scan_path(str(BENCHMARKS_FALSE_POS_DIR))
    assert report.scanned_files_count >= 10
    assert report.total_detections_count == 0


def test_false_positives_demo_file_has_zero_detections() -> None:
    container = create_container(parser_type="native")
    scanner = container.get_scanner()
    report = scanner.scan_path(str(FALSE_POSITIVES_DEMO_PHP))
    assert report.scanned_files_count == 1
    assert report.total_detections_count == 0


def test_pure_math_and_string_utilities_have_zero_detections() -> None:
    code = """<?php
class MathUtils {
    public static function add(int $a, int $b): int {
        return $a + $b;
    }
    public static function multiply(int $x, int $y): int {
        return $x * $y;
    }
    public static function factorial(int $n): int {
        if ($n <= 1) return 1;
        return $n * MathUtils::factorial($n - 1);
    }
}
"""
    report = _scan_snippet({"MathUtils.php": code})
    assert report.total_detections_count == 0


def test_dto_with_many_fields_and_getters_not_flagged_as_srp_god_object() -> None:
    code = """<?php
class CustomerProfileDto {
    public function __construct(
        public readonly string $id,
        public readonly string $firstName,
        public readonly string $lastName,
        public readonly string $email,
        public readonly string $phoneNumber,
        public readonly string $streetAddress,
        public readonly string $city,
        public readonly string $postalCode,
        public readonly string $country,
        public readonly string $status = 'ACTIVE',
    ) {}

    public function getId(): string { return $this->id; }
    public function getFirstName(): string { return $this->firstName; }
    public function getLastName(): string { return $this->lastName; }
    public function getEmail(): string { return $this->email; }
    public function getPhoneNumber(): string { return $this->phoneNumber; }
    public function getStreetAddress(): string { return $this->streetAddress; }
    public function getCity(): string { return $this->city; }
    public function getPostalCode(): string { return $this->postalCode; }
    public function getCountry(): string { return $this->country; }
    public function getStatus(): string { return $this->status; }
}
"""
    report = _scan_snippet({"CustomerProfileDto.php": code})
    srp_detections = [d for d in report.detections if d.pattern_type == PatternType.SINGLE_RESPONSIBILITY]
    assert len(srp_detections) == 0


def test_standard_equals_method_with_instanceof_not_flagged_as_ocp_violation() -> None:
    code = """<?php
class MoneyValue {
    public function __construct(
        private readonly float $amount,
        private readonly string $currency = 'USD',
    ) {}

    public function equals(mixed $other): bool {
        if (!$other instanceof self) {
            return false;
        }
        return $this->amount === $other->amount && $this->currency === $other->currency;
    }
}
"""
    report = _scan_snippet({"MoneyValue.php": code})
    ocp_detections = [d for d in report.detections if d.pattern_type == PatternType.OPEN_CLOSED]
    assert len(ocp_detections) == 0


def test_service_instantiating_array_or_stdclass_not_flagged_as_dip_violation() -> None:
    code = """<?php
class ItemListingService {
    public function generateSummary(): array {
        $result = [];
        $result[] = "Item A";
        $result[] = "Item B";
        return $result;
    }
}
"""
    report = _scan_snippet({"ItemListingService.php": code})
    dip_detections = [d for d in report.detections if d.pattern_type == PatternType.DEPENDENCY_INVERSION]
    assert len(dip_detections) == 0


def test_similar_simple_entity_getters_not_flagged_as_dry_duplicate_code() -> None:
    code_a = """<?php
class UserEntity {
    public function __construct(private string $userId) {}
    public function getId(): string {
        return $this->userId;
    }
}
"""
    code_b = """<?php
class ProductEntity {
    public function __construct(private string $productId) {}
    public function getId(): string {
        return $this->productId;
    }
}
"""
    report = _scan_snippet({
        "UserEntity.php": code_a,
        "ProductEntity.php": code_b,
    })
    dry_detections = [d for d in report.detections if d.pattern_type == PatternType.DRY]
    assert len(dry_detections) == 0


def test_string_helpers_with_make_or_create_name_not_flagged_as_factory() -> None:
    code = """<?php
class StringHelpers {
    public static function makeUppercase(string $s): string {
        return strtoupper($s);
    }
    public static function createSlug(string $title): string {
        return strtolower(str_replace(' ', '-', $title));
    }
}
"""
    report = _scan_snippet({"StringHelpers.php": code})
    factory_detections = [
        d for d in report.detections
        if d.pattern_type in (PatternType.FACTORY_METHOD, PatternType.ABSTRACT_FACTORY)
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(factory_detections) == 0


def test_immutable_vector2d_math_not_flagged_as_builder() -> None:
    code = """<?php
class Vector2D {
    public function __construct(
        private readonly float $x,
        private readonly float $y,
    ) {}

    public function add(Vector2D $other): Vector2D {
        return new Vector2D($this->x + $other->x, $this->y + $other->y);
    }

    public function scale(float $factor): Vector2D {
        return new Vector2D($this->x * $factor, $this->y * $factor);
    }
}
"""
    report = _scan_snippet({"Vector2D.php": code})
    builder_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.BUILDER
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(builder_detections) == 0


def test_class_with_normal_in_memory_cache_not_flagged_as_singleton() -> None:
    code = """<?php
class ImageCache {
    private array $cache = [];
    private int $hits = 0;
    private int $misses = 0;

    public function getImage(string $key): ?string {
        if (isset($this->cache[$key])) {
            $this->hits++;
            return $this->cache[$key];
        }
        $this->misses++;
        return null;
    }
}
"""
    report = _scan_snippet({"ImageCache.php": code})
    singleton_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.SINGLETON
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(singleton_detections) == 0


def test_linked_list_node_not_flagged_as_chain_of_responsibility() -> None:
    code = """<?php
class ListNode {
    public function __construct(
        public int $val = 0,
        public ?ListNode $next = null,
    ) {}

    public function getLength(): int {
        $count = 0;
        $curr = $this;
        while ($curr !== null) {
            $count++;
            $curr = $curr->next;
        }
        return $count;
    }
}
"""
    report = _scan_snippet({"ListNode.php": code})
    cor_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.CHAIN_OF_RESPONSIBILITY
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(cor_detections) == 0


def test_binary_search_tree_not_flagged_as_composite_pattern() -> None:
    code = """<?php
class TreeNode {
    public ?TreeNode $left = null;
    public ?TreeNode $right = null;

    public function __construct(public int $key) {}

    public function insert(int $val): void {
        if ($val < $this->key) {
            if ($this->left === null) {
                $this->left = new TreeNode($val);
            } else {
                $this->left->insert($val);
            }
        } else {
            if ($this->right === null) {
                $this->right = new TreeNode($val);
            } else {
                $this->right->insert($val);
            }
        }
    }
}
"""
    report = _scan_snippet({"TreeNode.php": code})
    composite_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.COMPOSITE
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(composite_detections) == 0


def test_simple_event_logger_not_flagged_as_observer_subject() -> None:
    code = """<?php
class EventLogger {
    private array $logs = [];

    public function log(string $message): void {
        $this->logs[] = $message;
    }

    public function flush(): void {
        $this->logs = [];
    }
}
"""
    report = _scan_snippet({"EventLogger.php": code})
    observer_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.OBSERVER
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(observer_detections) == 0


def test_batch_script_with_run_method_not_flagged_as_command_pattern() -> None:
    code = """<?php
class DatabaseMigrationScript {
    public function __construct(private string $dbUrl) {}

    public function run(): void {
        // Plain execution script
        echo "Connecting to " . $this->dbUrl;
    }
}
"""
    report = _scan_snippet({"DatabaseMigrationScript.php": code})
    command_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.COMMAND
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(command_detections) == 0


def test_url_crawler_with_visit_method_not_flagged_as_visitor_pattern() -> None:
    code = """<?php
class WebCrawler {
    private array $visitedUrls = [];

    public function visit(string $url): void {
        if (!in_array($url, $this->visitedUrls, true)) {
            $this->visitedUrls[] = $url;
        }
    }
}
"""
    report = _scan_snippet({"WebCrawler.php": code})
    visitor_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.VISITOR
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(visitor_detections) == 0


def test_custom_exception_subclasses_not_flagged_as_lsp_violation() -> None:
    code = r"""<?php
class ValidationError extends \InvalidArgumentException {
    public function __construct(string $message, private int $codeNum = 400) {
        parent::__construct($message, $codeNum);
    }
}
"""
    report = _scan_snippet({"ValidationError.php": code})
    lsp_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.LISKOV_SUBSTITUTION
    ]
    assert len(lsp_detections) == 0


def test_php81_backed_enums_not_flagged_as_strategy_or_composite() -> None:
    code = """<?php
enum TaskStatus: string {
    case Pending = 'PENDING';
    case Running = 'RUNNING';
    case Completed = 'COMPLETED';
    case Failed = 'FAILED';
}

enum LogLevel: int {
    case Debug = 10;
    case Info = 20;
    case Warn = 30;
    case Error = 40;
}
"""
    report = _scan_snippet({"Enums.php": code})
    assert report.total_detections_count == 0


def test_standard_constructor_service_injection_not_flagged_as_high_coupling() -> None:
    code = r"""<?php
interface Clock { public function now(): \DateTimeImmutable; }
interface Logger { public function info(string $m): void; }

class OrderProcessor {
    public function __construct(
        private Clock $clock,
        private Logger $logger,
    ) {}

    public function process(int $orderId): bool {
        $this->logger->info("Processing order " . $orderId);
        return true;
    }
}
"""
    report = _scan_snippet({"OrderProcessor.php": code})
    coupling_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.HIGH_COHESION_LOW_COUPLING
    ]
    assert len(coupling_detections) == 0


def test_small_focused_interface_not_flagged_as_isp_fat_interface() -> None:
    code = """<?php
interface PaymentCharger {
    public function charge(float $amount): bool;
}
"""
    report = _scan_snippet({"PaymentCharger.php": code})
    isp_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.INTERFACE_SEGREGATION
    ]
    assert len(isp_detections) == 0


def test_generator_function_not_flagged_as_iterator_pattern() -> None:
    code = r"""<?php
function readLargeFile(string $filePath, int $chunkSize = 1024): \Generator {
    $fp = fopen($filePath, 'r');
    if ($fp === false) return;
    while (!feof($fp)) {
        yield fread($fp, $chunkSize);
    }
    fclose($fp);
}
"""
    report = _scan_snippet({"GeneratorHelper.php": code})
    assert report.total_detections_count == 0
