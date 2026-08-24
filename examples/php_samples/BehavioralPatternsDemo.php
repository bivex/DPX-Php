<?php
/**
 * DPX-Php | Behavioral Design Patterns Demo
 * Covers: Observer, Strategy, Command, Template Method, Chain of Responsibility, Iterator
 */

declare(strict_types=1);

namespace DpxDemo\Behavioral;

// ─────────────────────────────────────────────────────────────────────────────
// OBSERVER
// ─────────────────────────────────────────────────────────────────────────────

interface EventListener
{
    public function onEvent(string $event, mixed $payload): void;
}

interface EventEmitter
{
    public function subscribe(string $event, EventListener $listener): void;
    public function unsubscribe(string $event, EventListener $listener): void;
    public function emit(string $event, mixed $payload): void;
}

class OrderService implements EventEmitter
{
    /** @var array<string, EventListener[]> */
    private array $listeners = [];

    public function subscribe(string $event, EventListener $listener): void
    {
        $this->listeners[$event][] = $listener;
    }

    public function unsubscribe(string $event, EventListener $listener): void
    {
        $this->listeners[$event] = array_filter(
            $this->listeners[$event] ?? [],
            fn($l) => $l !== $listener,
        );
    }

    public function emit(string $event, mixed $payload): void
    {
        foreach ($this->listeners[$event] ?? [] as $listener) {
            $listener->onEvent($event, $payload);
        }
    }

    public function placeOrder(array $order): void
    {
        // ... process order logic
        $this->emit('order.placed', $order);
    }
}

class EmailNotifier implements EventListener
{
    public function onEvent(string $event, mixed $payload): void
    {
        echo "[Email] Order placed: " . json_encode($payload) . "\n";
    }
}

class InventoryUpdater implements EventListener
{
    public function onEvent(string $event, mixed $payload): void
    {
        echo "[Inventory] Deducting stock for: " . json_encode($payload) . "\n";
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// STRATEGY
// ─────────────────────────────────────────────────────────────────────────────

interface SortStrategy
{
    public function sort(array $data): array;
}

class QuickSort implements SortStrategy
{
    public function sort(array $data): array
    {
        sort($data);
        return $data;
    }
}

class BubbleSort implements SortStrategy
{
    public function sort(array $data): array
    {
        $n = count($data);
        for ($i = 0; $i < $n - 1; $i++) {
            for ($j = 0; $j < $n - $i - 1; $j++) {
                if ($data[$j] > $data[$j + 1]) {
                    [$data[$j], $data[$j + 1]] = [$data[$j + 1], $data[$j]];
                }
            }
        }
        return $data;
    }
}

class DataSorter
{
    public function __construct(private SortStrategy $strategy) {}

    public function setStrategy(SortStrategy $strategy): void
    {
        $this->strategy = $strategy;
    }

    public function sort(array $data): array
    {
        return $this->strategy->sort($data);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// COMMAND
// ─────────────────────────────────────────────────────────────────────────────

interface Command
{
    public function execute(): void;
    public function undo(): void;
}

class TextEditor
{
    private string $content = '';

    public function insertText(string $text): void
    {
        $this->content .= $text;
    }

    public function removeText(int $length): void
    {
        $this->content = substr($this->content, 0, -$length);
    }

    public function getContent(): string
    {
        return $this->content;
    }
}

class InsertTextCommand implements Command
{
    public function __construct(
        private TextEditor $editor,
        private string $text,
    ) {}

    public function execute(): void
    {
        $this->editor->insertText($this->text);
    }

    public function undo(): void
    {
        $this->editor->removeText(strlen($this->text));
    }
}

class CommandHistory
{
    /** @var Command[] */
    private array $history = [];

    public function execute(Command $command): void
    {
        $command->execute();
        $this->history[] = $command;
    }

    public function undo(): void
    {
        $command = array_pop($this->history);
        $command?->undo();
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// TEMPLATE METHOD
// ─────────────────────────────────────────────────────────────────────────────

abstract class DataExporter
{
    // Template method
    final public function export(array $data, string $destination): void
    {
        $formatted = $this->format($data);
        $compressed = $this->compress($formatted);
        $this->write($compressed, $destination);
    }

    abstract protected function format(array $data): string;

    protected function compress(string $data): string
    {
        return $data; // Default: no compression
    }

    abstract protected function write(string $data, string $destination): void;
}

class JsonExporter extends DataExporter
{
    protected function format(array $data): string
    {
        return json_encode($data, JSON_PRETTY_PRINT);
    }

    protected function write(string $data, string $destination): void
    {
        file_put_contents($destination, $data);
    }
}

class CsvExporter extends DataExporter
{
    protected function format(array $data): string
    {
        $lines = [];
        foreach ($data as $row) {
            $lines[] = implode(',', $row);
        }
        return implode(PHP_EOL, $lines);
    }

    protected function write(string $data, string $destination): void
    {
        file_put_contents($destination, $data);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// CHAIN OF RESPONSIBILITY
// ─────────────────────────────────────────────────────────────────────────────

abstract class RequestHandler
{
    private ?RequestHandler $next = null;

    public function setNext(RequestHandler $handler): RequestHandler
    {
        $this->next = $handler;
        return $handler;
    }

    public function handle(array $request): ?string
    {
        if ($this->next !== null) {
            return $this->next->handle($request);
        }
        return null;
    }
}

class AuthHandler extends RequestHandler
{
    public function handle(array $request): ?string
    {
        if (empty($request['token'])) {
            return 'Unauthorized: no token provided';
        }
        return parent::handle($request);
    }
}

class RateLimitHandler extends RequestHandler
{
    private int $requestCount = 0;
    private int $maxRequests;

    public function __construct(int $maxRequests = 100)
    {
        $this->maxRequests = $maxRequests;
    }

    public function handle(array $request): ?string
    {
        if (++$this->requestCount > $this->maxRequests) {
            return 'Too Many Requests';
        }
        return parent::handle($request);
    }
}

class LoggingHandler extends RequestHandler
{
    public function handle(array $request): ?string
    {
        echo "[Log] Request processed: " . $request['path'] . "\n";
        return parent::handle($request);
    }
}
