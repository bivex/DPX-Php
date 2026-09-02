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


def test_class_with_instance_id_field_not_flagged_as_singleton() -> None:
    code = """<?php
class ServiceHolder {
    public string $instanceId;
    private object $instance;
    public function get(): object { return $this->instance; }
}
"""
    report = _scan_snippet({"ServiceHolder.php": code})
    singleton_dets = [d for d in report.detections if d.pattern_type == PatternType.SINGLETON]
    assert len(singleton_dets) == 0


def test_auditable_interface_with_created_at_not_flagged_as_abstract_factory() -> None:
    code = r"""<?php
interface AuditableInterface {
    public function createdAt(): \DateTime;
    public function createdBy(): string;
}
"""
    report = _scan_snippet({"AuditableInterface.php": code})
    factory_dets = [
        d for d in report.detections
        if d.pattern_type in (PatternType.ABSTRACT_FACTORY, PatternType.FACTORY_METHOD)
    ]
    assert len(factory_dets) == 0


def test_service_provider_without_creation_methods_not_flagged_as_factory() -> None:
    code = """<?php
interface AuthProvider {
    public function authenticate(string $user, string $pass): bool;
}
class LdapAuthProvider implements AuthProvider {
    public function authenticate(string $user, string $pass): bool { return true; }
}
"""
    report = _scan_snippet({"AuthProvider.php": code})
    factory_dets = [
        d for d in report.detections
        if d.pattern_type in (PatternType.FACTORY_METHOD, PatternType.ABSTRACT_FACTORY)
    ]
    assert len(factory_dets) == 0


def test_password_validator_not_flagged_as_composite() -> None:
    code = """<?php
interface ValidatorInterface {
    public function validate(string $v): bool;
}
class EmailValidator implements ValidatorInterface {
    public function validate(string $v): bool { return true; }
}
class PasswordValidator implements ValidatorInterface {
    public function validate(string $v): bool { return true; }
}
"""
    report = _scan_snippet({"Validator.php": code})
    composite_dets = [d for d in report.detections if d.pattern_type == PatternType.COMPOSITE]
    assert len(composite_dets) == 0


def test_controller_with_multiple_injected_services_not_flagged_as_facade() -> None:
    code = """<?php
class OrderController {
    public function __construct(
        private UserService $userService,
        private PaymentService $paymentService
    ) {}
    public function createOrder(): void {}
}
"""
    report = _scan_snippet({"OrderController.php": code})
    facade_dets = [d for d in report.detections if d.pattern_type == PatternType.FACADE]
    assert len(facade_dets) == 0


def test_repository_with_first_method_not_flagged_as_iterator() -> None:
    code = """<?php
interface UserRepositoryInterface {
    public function find(int $id): ?object;
    public function first(): ?object;
}
"""
    report = _scan_snippet({"UserRepositoryInterface.php": code})
    iter_dets = [d for d in report.detections if d.pattern_type == PatternType.ITERATOR]
    assert len(iter_dets) == 0


def test_entity_with_views_counter_not_flagged_as_observer() -> None:
    code = """<?php
class Article {
    private int $views = 0;
    public function getViews(): int { return $this->views; }
}
"""
    report = _scan_snippet({"Article.php": code})
    obs_dets = [d for d in report.detections if d.pattern_type == PatternType.OBSERVER]
    assert len(obs_dets) == 0


def test_transaction_interface_not_flagged_as_command() -> None:
    code = """<?php
interface TransactionInterface {
    public function commit(): void;
    public function rollback(): void;
}
class DatabaseTransaction implements TransactionInterface {
    public function commit(): void {}
    public function rollback(): void {}
}
"""
    report = _scan_snippet({"Transaction.php": code})
    cmd_dets = [d for d in report.detections if d.pattern_type == PatternType.COMMAND]
    assert len(cmd_dets) == 0


def test_prepared_statement_interface_not_flagged_as_state() -> None:
    code = """<?php
interface PreparedStatementInterface {
    public function execute(array $params = []): bool;
}
"""
    report = _scan_snippet({"PreparedStatement.php": code})
    state_dets = [d for d in report.detections if d.pattern_type == PatternType.STATE]
    assert len(state_dets) == 0


def test_callable_f_parameter_not_flagged_as_decorator() -> None:
    code = """<?php
function applyMath(callable $f, float $x): float {
    return $f($x);
}
"""
    report = _scan_snippet({"Math.php": code})
    dec_dets = [d for d in report.detections if d.pattern_type == PatternType.DECORATOR]
    assert len(dec_dets) == 0


def test_task_try_catch_not_flagged_as_template_method() -> None:
    code = r"""<?php
function runTask(string $task): void {
    try {
        doSomething($task);
    } catch (\Exception $e) {}
}
"""
    report = _scan_snippet({"Task.php": code})
    tm_dets = [d for d in report.detections if d.pattern_type == PatternType.TEMPLATE_METHOD]
    assert len(tm_dets) == 0


def test_command_handler_without_delegation_not_flagged_as_middleware() -> None:
    code = """<?php
class UserCommandHandler {
    public function handle(object $command, object $handler): void {
        echo 'Handling';
    }
}
"""
    report = _scan_snippet({"UserCommandHandler.php": code})
    mw_dets = [d for d in report.detections if d.pattern_type == PatternType.MIDDLEWARE_PIPELINE]
    assert len(mw_dets) == 0


def test_factory_with_instanceof_not_flagged_as_multimethod_dispatch() -> None:
    code = """<?php
class UserFactory {
    public function execute(mixed $spec): object {
        if ($spec instanceof UserSpec) {
            return new User();
        }
        return new GuestUser();
    }
}
"""
    report = _scan_snippet({"UserFactory.php": code})
    mm_dets = [d for d in report.detections if d.pattern_type == PatternType.MULTIMETHOD_DISPATCH]
    assert len(mm_dets) == 0


def test_method_calling_repository_getter_not_flagged_as_dip_violation() -> None:
    code = """<?php
class OrderService {
    public function getRDBRepository() { return null; }
    public function execute(): void {
        $this->getRDBRepository();
    }
}
"""
    report = _scan_snippet({"OrderService.php": code})
    dip_dets = [
        d for d in report.detections
        if d.pattern_type == PatternType.DEPENDENCY_INVERSION
        and "violation" in d.summary.lower()
    ]
    assert len(dip_dets) == 0


def test_php_chained_method_calls_detected_as_law_of_demeter() -> None:
    code = """<?php
class OrderService {
    public function getCustomerCity(Order $order): string {
        return $order->getCustomer()->getAddress()->getCity();
    }
}
"""
    report = _scan_snippet({"OrderService.php": code})
    lod_dets = [d for d in report.detections if d.pattern_type == PatternType.LAW_OF_DEMETER]
    assert len(lod_dets) >= 1


def test_php_overriding_method_throwing_bad_method_call_detected_as_lsp() -> None:
    code = r"""<?php
interface ReadOnlyCollection {
    public function add(string $item): void;
}
class ImmutableList implements ReadOnlyCollection {
    public function add(string $item): void {
        throw new \BadMethodCallException('Cannot mutate immutable list');
    }
}
"""
    report = _scan_snippet({"ImmutableList.php": code})
    lsp_dets = [d for d in report.detections if d.pattern_type == PatternType.LISKOV_SUBSTITUTION]
    assert len(lsp_dets) >= 1


def test_php_instanceof_cascade_detected_as_ocp_violation() -> None:
    code = """<?php
class ShapeRenderer {
    public function render(object $shape): void {
        if ($shape instanceof Circle) {
            renderCircle();
        } elseif ($shape instanceof Square) {
            renderSquare();
        } elseif ($shape instanceof Triangle) {
            renderTriangle();
        }
    }
}
"""
    report = _scan_snippet({"ShapeRenderer.php": code})
    ocp_violations = [
        d for d in report.detections
        if d.pattern_type == PatternType.OPEN_CLOSED and "violation" in d.summary.lower()
    ]
    assert len(ocp_violations) >= 1


def test_constructor_promoted_properties_not_duplicated_in_fields() -> None:
    code = """<?php
class Product {
    public function __construct(
        private string $sku,
        public readonly float $price,
    ) {}
}
"""
    adapter = PhpParserAdapter()
    model = adapter.parse_sources({"Product.php": code})
    rec = next((r for r in model.all_records() if r.name == "Product"), None)
    assert rec is not None
    assert rec.fields.count("sku") == 1
    assert rec.fields.count("price") == 1
