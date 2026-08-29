<?php
/**
 * DPX-Php | False Positives Benchmark & Demo
 * 
 * Contains everyday, standard PHP (7.4 - 8.4+) idioms, DTOs, value objects, pure math/string utilities,
 * simple data structures, enums, exception hierarchies, and small services.
 * 
 * These structures MUST NOT trigger false positive detections for Design Patterns or SOLID Principle violations.
 */

declare(strict_types=1);

namespace DpxDemo\FalsePositives;

// ─────────────────────────────────────────────────────────────────────────────
// 1. PURE UTILITIES & MATH FUNCTIONS (No patterns, No God Object, No SRP)
// ─────────────────────────────────────────────────────────────────────────────

class MathHelper
{
    public static function add(int $a, int $b): int
    {
        return $a + $b;
    }

    public static function multiply(int $x, int $y): int
    {
        return $x * $y;
    }

    public static function factorial(int $n): int
    {
        if ($n <= 1) {
            return 1;
        }
        return $n * self::factorial($n - 1);
    }
}

class StringUtils
{
    public static function capitalize(string $str): string
    {
        return ucfirst(strtolower($str));
    }

    public static function makeSlug(string $title): string
    {
        return strtolower(trim(preg_replace('/[^A-Za-z0-9-]+/', '-', $title) ?? '', '-'));
    }

    public static function truncate(string $text, int $length = 100): string
    {
        if (strlen($text) <= $length) {
            return $text;
        }
        return substr($text, 0, $length) . '...';
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// 2. DATA TRANSFER OBJECTS (DTOs) & VALUE OBJECTS (Not SRP God Object, Not Builder)
// ─────────────────────────────────────────────────────────────────────────────

class CustomerProfileDto
{
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

    public function getFullName(): string
    {
        return $this->firstName . ' ' . $this->lastName;
    }
}

class MoneyValue
{
    public function __construct(
        private readonly float $amount,
        private readonly string $currency = 'USD',
    ) {}

    public function getAmount(): float
    {
        return $this->amount;
    }

    public function getCurrency(): string
    {
        return $this->currency;
    }

    public function equals(mixed $other): bool
    {
        if (!$other instanceof self) {
            return false;
        }
        return $this->amount === $other->amount && $this->currency === $other->currency;
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// 3. VECTOR MATH & COORDINATES (Not Builder, Not Factory)
// ─────────────────────────────────────────────────────────────────────────────

class Vector2D
{
    public function __construct(
        private readonly float $x,
        private readonly float $y,
    ) {}

    public function getX(): float
    {
        return $this->x;
    }

    public function getY(): float
    {
        return $this->y;
    }

    public function add(Vector2D $other): Vector2D
    {
        return new Vector2D($this->x + $other->x, $this->y + $other->y);
    }

    public function scale(float $factor): Vector2D
    {
        return new Vector2D($this->x * $factor, $this->y * $factor);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// 4. DATA STRUCTURES (Not Chain of Responsibility, Not Composite)
// ─────────────────────────────────────────────────────────────────────────────

class LinkedListNode
{
    public function __construct(
        public readonly mixed $value,
        public ?LinkedListNode $next = null,
    ) {}

    public function countNodes(): int
    {
        $count = 0;
        $current = $this;
        while ($current !== null) {
            $count++;
            $current = $current->next;
        }
        return $count;
    }
}

class BinaryTreeNode
{
    public ?BinaryTreeNode $left = null;
    public ?BinaryTreeNode $right = null;

    public function __construct(
        public readonly int $key,
    ) {}

    public function insert(int $val): void
    {
        if ($val < $this->key) {
            if ($this->left === null) {
                $this->left = new BinaryTreeNode($val);
            } else {
                $this->left->insert($val);
            }
        } else {
            if ($this->right === null) {
                $this->right = new BinaryTreeNode($val);
            } else {
                $this->right->insert($val);
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// 5. CACHING & LOGGING UTILITIES (Not Singleton, Not Observer)
// ─────────────────────────────────────────────────────────────────────────────

class SimpleArrayCache
{
    private array $storage = [];
    private int $hits = 0;
    private int $misses = 0;

    public function get(string $key): mixed
    {
        if (array_key_exists($key, $this->storage)) {
            $this->hits++;
            return $this->storage[$key];
        }
        $this->misses++;
        return null;
    }

    public function set(string $key, mixed $value): void
    {
        $this->storage[$key] = $value;
    }

    public function getStats(): array
    {
        return ['hits' => $this->hits, 'misses' => $this->misses];
    }
}

class PlainEventLogger
{
    private array $entries = [];

    public function record(string $message): void
    {
        $this->entries[] = date('Y-m-d H:i:s') . ' ' . $message;
    }

    public function flush(): array
    {
        $dump = $this->entries;
        $this->entries = [];
        return $dump;
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// 6. SCRIPTS & TRAVERSERS (Not Command Pattern, Not Visitor Pattern)
// ─────────────────────────────────────────────────────────────────────────────

class DatabaseMigrationScript
{
    public function __construct(
        private readonly string $dsn,
    ) {}

    public function run(): bool
    {
        // Simple standalone execution routine
        return strlen($this->dsn) > 0;
    }
}

class WebSiteCrawler
{
    private array $visited = [];

    public function visit(string $url): void
    {
        if (!in_array($url, $this->visited, true)) {
            $this->visited[] = $url;
        }
    }

    public function getVisitedCount(): int
    {
        return count($this->visited);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// 7. CUSTOM EXCEPTIONS & ENUMS (Not LSP Violations, Not Strategy)
// ─────────────────────────────────────────────────────────────────────────────

class EntityNotFoundException extends \RuntimeException
{
    public function __construct(string $entityName, string|int $id)
    {
        parent::__construct(sprintf("Entity '%s' with ID '%s' was not found.", $entityName, (string)$id));
    }
}

class ValidationException extends \InvalidArgumentException
{
    public function __construct(
        private readonly array $errors,
        string $message = "Validation failed"
    ) {
        parent::__construct($message, 422);
    }

    public function getErrors(): array
    {
        return $this->errors;
    }
}

enum OrderStatus: string
{
    case Pending = 'pending';
    case Processing = 'processing';
    case Completed = 'completed';
    case Cancelled = 'cancelled';
}

// ─────────────────────────────────────────────────────────────────────────────
// 8. FOCUSED INTERFACES & SERVICES (Not ISP Fat Interface, Not DIP / High Coupling)
// ─────────────────────────────────────────────────────────────────────────────

interface ClockInterface
{
    public function now(): \DateTimeImmutable;
}

class SystemClock implements ClockInterface
{
    public function now(): \DateTimeImmutable
    {
        return new \DateTimeImmutable();
    }
}

class SimpleOrderService
{
    public function __construct(
        private readonly ClockInterface $clock,
    ) {}

    public function createOrder(string $customerId, float $amount): array
    {
        return [
            'customerId' => $customerId,
            'amount' => $amount,
            'createdAt' => $this->clock->now()->format(\DateTimeInterface::ATOM),
            'status' => OrderStatus::Pending->value,
        ];
    }
}
