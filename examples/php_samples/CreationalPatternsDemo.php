<?php
/**
 * DPX-Php | Creational Design Patterns Demo
 * Covers: Singleton, Factory Method, Abstract Factory, Builder, Prototype
 */

declare(strict_types=1);

namespace DpxDemo\Creational;

// ─────────────────────────────────────────────────────────────────────────────
// SINGLETON
// ─────────────────────────────────────────────────────────────────────────────

class DatabaseConnection
{
    private static ?DatabaseConnection $instance = null;
    private \PDO $pdo;

    private function __construct(string $dsn)
    {
        $this->pdo = new \PDO($dsn);
    }

    public static function getInstance(string $dsn = 'sqlite::memory:'): static
    {
        if (static::$instance === null) {
            static::$instance = new static($dsn);
        }
        return static::$instance;
    }

    public function query(string $sql): array
    {
        return $this->pdo->query($sql)->fetchAll();
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// FACTORY METHOD
// ─────────────────────────────────────────────────────────────────────────────

interface Logger
{
    public function log(string $message): void;
}

class FileLogger implements Logger
{
    public function __construct(private string $path) {}

    public function log(string $message): void
    {
        file_put_contents($this->path, $message . PHP_EOL, FILE_APPEND);
    }
}

class StdoutLogger implements Logger
{
    public function log(string $message): void
    {
        echo "[LOG] $message\n";
    }
}

abstract class LoggerFactory
{
    abstract public function createLogger(): Logger;

    public function logWithTimestamp(string $message): void
    {
        $logger = $this->createLogger();
        $logger->log('[' . date('Y-m-d H:i:s') . '] ' . $message);
    }
}

class FileLoggerFactory extends LoggerFactory
{
    public function createLogger(): Logger
    {
        return new FileLogger('/tmp/app.log');
    }
}

class StdoutLoggerFactory extends LoggerFactory
{
    public function createLogger(): Logger
    {
        return new StdoutLogger();
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// ABSTRACT FACTORY
// ─────────────────────────────────────────────────────────────────────────────

interface Button
{
    public function render(): string;
}

interface Checkbox
{
    public function render(): string;
}

class DarkButton implements Button
{
    public function render(): string { return '<button class="dark">Click</button>'; }
}

class LightButton implements Button
{
    public function render(): string { return '<button class="light">Click</button>'; }
}

class DarkCheckbox implements Checkbox
{
    public function render(): string { return '<input type="checkbox" class="dark">'; }
}

class LightCheckbox implements Checkbox
{
    public function render(): string { return '<input type="checkbox" class="light">'; }
}

interface UIFactory
{
    public function createButton(): Button;
    public function createCheckbox(): Checkbox;
}

class DarkThemeFactory implements UIFactory
{
    public function createButton(): Button { return new DarkButton(); }
    public function createCheckbox(): Checkbox { return new DarkCheckbox(); }
}

class LightThemeFactory implements UIFactory
{
    public function createButton(): Button { return new LightButton(); }
    public function createCheckbox(): Checkbox { return new LightCheckbox(); }
}

// ─────────────────────────────────────────────────────────────────────────────
// BUILDER (Fluent Interface)
// ─────────────────────────────────────────────────────────────────────────────

class QueryBuilder
{
    private string $table = '';
    private array $conditions = [];
    private array $columns = ['*'];
    private ?int $limitValue = null;
    private ?string $orderByColumn = null;

    public function from(string $table): static
    {
        $this->table = $table;
        return $this;
    }

    public function select(string ...$columns): static
    {
        $this->columns = $columns;
        return $this;
    }

    public function where(string $condition): static
    {
        $this->conditions[] = $condition;
        return $this;
    }

    public function limit(int $limit): static
    {
        $this->limitValue = $limit;
        return $this;
    }

    public function orderBy(string $column): static
    {
        $this->orderByColumn = $column;
        return $this;
    }

    public function build(): string
    {
        $query = 'SELECT ' . implode(', ', $this->columns) . ' FROM ' . $this->table;
        if (!empty($this->conditions)) {
            $query .= ' WHERE ' . implode(' AND ', $this->conditions);
        }
        if ($this->orderByColumn !== null) {
            $query .= ' ORDER BY ' . $this->orderByColumn;
        }
        if ($this->limitValue !== null) {
            $query .= ' LIMIT ' . $this->limitValue;
        }
        return $query;
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// PROTOTYPE
// ─────────────────────────────────────────────────────────────────────────────

class UserProfile
{
    public function __construct(
        public string $name,
        public string $role,
        public array $permissions = [],
    ) {}

    public function clone(): static
    {
        return clone $this;
    }

    public function withRole(string $role): static
    {
        $copy = $this->clone();
        $copy->role = $role;
        return $copy;
    }
}
