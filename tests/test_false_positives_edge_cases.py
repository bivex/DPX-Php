"""Edge Cases False Positives Test Suite for PHP Design Patterns & SOLID Principles.

Validates that complex and modern PHP idioms (PHP 8.0 - 8.4+ Match Expressions on scalars,
PHP 8 Attributes, Traits, Magic Methods, Closures, Backed Enums, Generators with yield/yield from,
and Readonly Properties) do not produce false positive detections.
"""

from __future__ import annotations

from pattern_detector.adapters.outbound.php_ast.php_parser_adapter import PhpParserAdapter
from pattern_detector.domain.detection import DetectionReport
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.services.pattern_detector import PatternDetectorService
from pattern_detector.domain.value_objects import ConfidenceLevel, PatternType


def _scan_snippet(code_map: dict[str, str]) -> DetectionReport:
    adapter = PhpParserAdapter()
    model = adapter.parse_sources(code_map)
    detector = PatternDetectorService(rules=get_default_rules())
    return detector.detect_all(model)


def test_php8_scalar_match_expression_not_flagged_as_multimethod_dispatch() -> None:
    code = """<?php
class StatusCodeMapper {
    public function getReasonPhrase(int $statusCode): string {
        return match ($statusCode) {
            200 => 'OK',
            201 => 'Created',
            400 => 'Bad Request',
            401 => 'Unauthorized',
            404 => 'Not Found',
            500 => 'Internal Server Error',
            default => 'Unknown Status',
        };
    }
}
"""
    report = _scan_snippet({"StatusCodeMapper.php": code})
    # Scalar primitive match expressions should not trigger multimethod dispatch
    dispatch_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.MULTIMETHOD_DISPATCH
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(dispatch_detections) == 0


def test_php_magic_methods_not_flagged_as_prototype_or_builder() -> None:
    code = """<?php
class JsonPayload {
    public function __construct(private array $data = []) {}

    public function __toString(): string {
        return json_encode($this->data) ?: '{}';
    }

    public function __clone() {
        // Simple clone reset
        $this->data['cloned'] = true;
    }

    public function __invoke(string $key): mixed {
        return $this->data[$key] ?? null;
    }
}
"""
    report = _scan_snippet({"JsonPayload.php": code})
    prototype_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.PROTOTYPE
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    builder_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.BUILDER
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(prototype_detections) == 0
    assert len(builder_detections) == 0


def test_php_trait_usage_not_flagged_as_adapter_or_decorator() -> None:
    code = """<?php
trait TimestampableTrait {
    private ?\\DateTimeImmutable $createdAt = null;
    private ?\\DateTimeImmutable $updatedAt = null;

    public function getCreatedAt(): ?\\DateTimeImmutable {
        return $this->createdAt;
    }

    public function touch(): void {
        $this->updatedAt = new \\DateTimeImmutable();
    }
}

class Article {
    use TimestampableTrait;

    public function __construct(private string $title) {
        $this->createdAt = new \\DateTimeImmutable();
    }
}
"""
    report = _scan_snippet({"Article.php": code})
    adapter_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.ADAPTER
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    decorator_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.DECORATOR
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(adapter_detections) == 0
    assert len(decorator_detections) == 0


def test_php8_attributes_not_flagged_as_decorator_or_proxy() -> None:
    code = r"""<?php
#[\Attribute(\Attribute::TARGET_CLASS | \Attribute::TARGET_METHOD)]
class Route {
    public function __construct(
        public readonly string $path,
        public readonly array $methods = ['GET'],
    ) {}
}

#[\Attribute(\Attribute::TARGET_PROPERTY)]
class EntityColumn {
    public function __construct(public readonly string $name) {}
}
"""
    report = _scan_snippet({"Attributes.php": code})
    decorator_detections = [
        d for d in report.detections
        if d.pattern_type in (PatternType.DECORATOR, PatternType.PROXY)
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(decorator_detections) == 0


def test_php_generator_with_yield_from_not_flagged_as_state_machine() -> None:
    code = """<?php
function generateNumbers(int $max): \\Generator {
    for ($i = 1; $i <= $max; $i++) {
        yield $i;
    }
}

function generateSequence(): \\Generator {
    yield 0;
    yield from generateNumbers(3);
    yield 999;
}
"""
    report = _scan_snippet({"SequenceGenerator.php": code})
    state_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.STATE
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(state_detections) == 0


def test_clean_repository_queries_not_flagged_as_srp_violation() -> None:
    code = """<?php
class ProductRepository {
    private array $items = [];

    public function findById(int $id): ?array {
        return $this->items[$id] ?? null;
    }

    public function findBySku(string $sku): ?array {
        foreach ($this->items as $item) {
            if (($item['sku'] ?? '') === $sku) {
                return $item;
            }
        }
        return null;
    }

    public function save(array $product): void {
        $this->items[$product['id']] = $product;
    }

    public function delete(int $id): void {
        unset($this->items[$id]);
    }
}
"""
    report = _scan_snippet({"ProductRepository.php": code})
    srp_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.SINGLE_RESPONSIBILITY
    ]
    assert len(srp_detections) == 0


def test_higher_order_array_helpers_not_flagged_as_pipeline() -> None:
    code = """<?php
class CollectionUtils {
    public static function pluck(array $items, string $key): array {
        return array_map(fn($item) => $item[$key] ?? null, $items);
    }

    public static function sumField(array $items, string $field): float {
        return array_reduce(
            $items,
            fn(float $acc, array $item) => $acc + (float)($item[$field] ?? 0.0),
            0.0
        );
    }
}
"""
    report = _scan_snippet({"CollectionUtils.php": code})
    pipeline_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.MIDDLEWARE_PIPELINE
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(pipeline_detections) == 0


def test_fluent_mutator_without_terminal_build_not_flagged_as_builder() -> None:
    code = """<?php
class UserNotificationPreference {
    private bool $emailEnabled = true;
    private bool $smsEnabled = false;

    public function setEmailEnabled(bool $enabled): self {
        $this->emailEnabled = $enabled;
        return $this;
    }

    public function setSmsEnabled(bool $enabled): self {
        $this->smsEnabled = $enabled;
        return $this;
    }

    public function isEmailEnabled(): bool {
        return $this->emailEnabled;
    }

    public function isSmsEnabled(): bool {
        return $this->smsEnabled;
    }
}
"""
    report = _scan_snippet({"UserNotificationPreference.php": code})
    builder_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.BUILDER
        and d.confidence.level in (ConfidenceLevel.HIGH, ConfidenceLevel.VERY_HIGH)
    ]
    assert len(builder_detections) == 0


def test_multi_namespace_clean_imports_not_flagged_as_circular_dependency() -> None:
    code_a = """<?php
namespace App\\Domain;

class OrderItem {
    public function __construct(
        public readonly string $productId,
        public readonly int $quantity,
    ) {}
}
"""
    code_b = """<?php
namespace App\\Application;

use App\\Domain\\OrderItem;

class OrderService {
    public function calculateTotal(OrderItem $item): int {
        return $item->quantity * 100;
    }
}
"""
    report = _scan_snippet({
        "OrderItem.php": code_a,
        "OrderService.php": code_b,
    })
    circular_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.CIRCULAR_DEPENDENCY
    ]
    assert len(circular_detections) == 0


def test_simple_switch_statement_not_flagged_as_ocp_violation() -> None:
    code = """<?php
class PriorityCalculator {
    public function getPriorityWeight(string $level): int {
        switch (strtolower($level)) {
            case 'high':
                return 100;
            case 'medium':
                return 50;
            case 'low':
                return 10;
            default:
                return 0;
        }
    }
}
"""
    report = _scan_snippet({"PriorityCalculator.php": code})
    ocp_detections = [
        d for d in report.detections
        if d.pattern_type == PatternType.OPEN_CLOSED
    ]
    assert len(ocp_detections) == 0
