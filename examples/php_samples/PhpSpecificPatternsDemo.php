<?php
/**
 * DPX-Php | PHP-Specific Patterns Demo
 * Covers: Middleware Pipeline (PSR-15) + Multimethod / Type-based Dispatch
 */

declare(strict_types=1);

namespace DpxDemo\PhpSpecific;

use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Server\MiddlewareInterface;
use Psr\Http\Server\RequestHandlerInterface;

// ─────────────────────────────────────────────────────────────────────────────
// MIDDLEWARE PIPELINE — PSR-15 Style
// ─────────────────────────────────────────────────────────────────────────────

class AuthenticationMiddleware implements MiddlewareInterface
{
    public function __construct(
        private string $secret,
        private array $publicPaths = ['/health'],
    ) {}

    public function process(
        ServerRequestInterface $request,
        RequestHandlerInterface $handler,
    ): ResponseInterface {
        if (in_array($request->getUri()->getPath(), $this->publicPaths, true)) {
            return $handler->handle($request);
        }

        $token = $request->getHeaderLine('Authorization');
        if (empty($token) || !$this->verifyToken($token)) {
            return new JsonResponse(['error' => 'Unauthorized'], 401);
        }

        return $handler->handle($request->withAttribute('user', $this->decodeToken($token)));
    }

    private function verifyToken(string $token): bool
    {
        return str_starts_with($token, 'Bearer ') && strlen($token) > 10;
    }

    private function decodeToken(string $token): array
    {
        return ['id' => 1, 'role' => 'user'];
    }
}

class RateLimitMiddleware implements MiddlewareInterface
{
    private array $requestCounts = [];

    public function __construct(
        private int $maxRequests = 60,
        private int $windowSeconds = 60,
    ) {}

    public function process(
        ServerRequestInterface $request,
        RequestHandlerInterface $handler,
    ): ResponseInterface {
        $clientIp = $request->getServerParams()['REMOTE_ADDR'] ?? '0.0.0.0';
        $key = $clientIp . ':' . floor(time() / $this->windowSeconds);

        $this->requestCounts[$key] = ($this->requestCounts[$key] ?? 0) + 1;

        if ($this->requestCounts[$key] > $this->maxRequests) {
            return new JsonResponse(['error' => 'Too Many Requests'], 429);
        }

        return $handler->handle($request->withAttribute('requestCount', $this->requestCounts[$key]));
    }
}

class CorsMiddleware implements MiddlewareInterface
{
    public function __construct(
        private array $allowedOrigins = ['*'],
        private array $allowedMethods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    ) {}

    public function process(
        ServerRequestInterface $request,
        RequestHandlerInterface $handler,
    ): ResponseInterface {
        if ($request->getMethod() === 'OPTIONS') {
            return new JsonResponse([], 204);
        }

        $response = $handler->handle($request);
        return $response
            ->withHeader('Access-Control-Allow-Origin', implode(', ', $this->allowedOrigins))
            ->withHeader('Access-Control-Allow-Methods', implode(', ', $this->allowedMethods));
    }
}

class RequestLoggingMiddleware implements MiddlewareInterface
{
    public function process(
        ServerRequestInterface $request,
        RequestHandlerInterface $handler,
    ): ResponseInterface {
        $start = microtime(true);
        $response = $handler->handle($request);
        $elapsed = round((microtime(true) - $start) * 1000, 2);
        echo sprintf("[%s] %s %s %dms\n",
            date('Y-m-d H:i:s'),
            $request->getMethod(),
            $request->getUri()->getPath(),
            $elapsed,
        );
        return $response;
    }
}

// Pipeline builder assembling the PSR-15 stack
class MiddlewarePipeline
{
    /** @var MiddlewareInterface[] */
    private array $middleware = [];
    private array $stack = [];

    public function pipe(MiddlewareInterface $middleware): static
    {
        $this->middleware[] = $middleware;
        return $this;
    }

    public function add(MiddlewareInterface $middleware): static
    {
        $this->stack[] = $middleware;
        return $this;
    }

    public function push(MiddlewareInterface $middleware): static
    {
        array_unshift($this->stack, $middleware);
        return $this;
    }

    public function process(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface
    {
        $pipeline = array_merge($this->middleware, $this->stack);
        $runner = array_reduce(
            array_reverse($pipeline),
            fn($carry, $mw) => new class($mw, $carry) implements RequestHandlerInterface {
                public function __construct(
                    private MiddlewareInterface $middleware,
                    private RequestHandlerInterface $next,
                ) {}
                public function handle(ServerRequestInterface $request): ResponseInterface {
                    return $this->middleware->process($request, $this->next);
                }
            },
            $handler,
        );
        return $runner->handle($request);
    }
}

// Laravel-style HTTP Kernel
class HttpKernel
{
    protected array $middleware = [
        RequestLoggingMiddleware::class,
        CorsMiddleware::class,
    ];

    protected array $middlewareGroups = [
        'web' => [
            AuthenticationMiddleware::class,
            RateLimitMiddleware::class,
        ],
        'api' => [
            AuthenticationMiddleware::class,
            RateLimitMiddleware::class,
            CorsMiddleware::class,
        ],
    ];

    protected array $routeMiddleware = [
        'auth' => AuthenticationMiddleware::class,
        'throttle' => RateLimitMiddleware::class,
        'cors' => CorsMiddleware::class,
    ];

    public function handle(ServerRequestInterface $request): ResponseInterface
    {
        return new JsonResponse(['status' => 'ok'], 200);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MULTIMETHOD / TYPE-BASED DISPATCH — PHP Equivalents
// ─────────────────────────────────────────────────────────────────────────────

// 1. PHP 8.0+ match() expression dispatch (cleanest equivalent of defmulti)
function renderNotification(string $type, array $payload): string
{
    return match($type) {
        'email'    => "📧 Sending email to {$payload['to']}: {$payload['subject']}",
        'sms'      => "📱 Sending SMS to {$payload['phone']}: {$payload['message']}",
        'push'     => "🔔 Pushing notification to device {$payload['device_id']}",
        'webhook'  => "🌐 POST to {$payload['url']} with " . json_encode($payload['data']),
        'slack'    => "💬 Slack message to #{$payload['channel']}: {$payload['text']}",
        default    => throw new \InvalidArgumentException("Unknown notification type: $type"),
    };
}

// 2. Command Bus — dispatcher map (array of callable handlers per command type)
interface Command {}

class CreateUserCommand implements Command
{
    public function __construct(
        public readonly string $email,
        public readonly string $name,
    ) {}
}

class DeleteUserCommand implements Command
{
    public function __construct(public readonly int $userId) {}
}

class SendWelcomeEmailCommand implements Command
{
    public function __construct(
        public readonly int $userId,
        public readonly string $email,
    ) {}
}

interface CommandHandler
{
    public function handle(Command $command): mixed;
}

class CreateUserHandler implements CommandHandler
{
    public function handle(Command $command): mixed
    {
        assert($command instanceof CreateUserCommand);
        return ['id' => 42, 'email' => $command->email, 'name' => $command->name];
    }
}

class DeleteUserHandler implements CommandHandler
{
    public function handle(Command $command): mixed
    {
        assert($command instanceof DeleteUserCommand);
        return ['deleted' => $command->userId];
    }
}

class SendWelcomeEmailHandler implements CommandHandler
{
    public function handle(Command $command): mixed
    {
        assert($command instanceof SendWelcomeEmailCommand);
        echo "Welcome email sent to {$command->email}\n";
        return true;
    }
}

// Command Bus: dispatcher map class
class CommandBus
{
    /** @var array<string, CommandHandler> */
    private array $handlers = [];

    public function register(string $commandClass, CommandHandler $handler): void
    {
        $this->handlers[$commandClass] = $handler;
    }

    public function dispatch(Command $command): mixed
    {
        $commandClass = get_class($command);
        if (!isset($this->handlers[$commandClass])) {
            throw new \RuntimeException("No handler registered for: $commandClass");
        }
        return $this->handlers[$commandClass]->handle($command);
    }
}

// 3. Event Bus — same dispatcher map pattern for events
interface DomainEvent {}

class UserRegisteredEvent implements DomainEvent
{
    public function __construct(
        public readonly int $userId,
        public readonly string $email,
    ) {}
}

class OrderPlacedEvent implements DomainEvent
{
    public function __construct(
        public readonly int $orderId,
        public readonly float $total,
    ) {}
}

class EventDispatcher
{
    /** @var array<string, callable[]> */
    private array $handlers = [];
    private array $dispatchers = [];

    public function subscribe(string $eventClass, callable $listener): void
    {
        $this->handlers[$eventClass][] = $listener;
    }

    public function dispatch(DomainEvent $event): void
    {
        $eventClass = get_class($event);
        foreach ($this->handlers[$eventClass] ?? [] as $listener) {
            $listener($event);
        }
    }
}

// 4. Switch-based type dispatch for serialization (classic defmulti equivalent)
function serializeValue(mixed $value, string $format): string
{
    switch (gettype($value)) {
        case 'integer':
        case 'double':
            return match($format) {
                'json' => (string)$value,
                'xml'  => "<number>$value</number>",
                'csv'  => (string)$value,
                default => (string)$value,
            };
        case 'string':
            return match($format) {
                'json' => "\"$value\"",
                'xml'  => "<string>$value</string>",
                'csv'  => "\"$value\"",
                default => $value,
            };
        case 'boolean':
            $str = $value ? 'true' : 'false';
            return match($format) {
                'json' => $str,
                'xml'  => "<bool>$str</bool>",
                default => $str,
            };
        case 'array':
            return match($format) {
                'json' => json_encode($value),
                'xml'  => '<array>' . implode('', array_map(fn($v) => serializeValue($v, $format), $value)) . '</array>',
                default => implode(',', $value),
            };
        default:
            return '';
    }
}

// Stub classes for PSR-15 demo (since we don't have the PSR interfaces installed)
class JsonResponse
{
    public function __construct(
        private array $data,
        private int $status = 200,
        private array $headers = [],
    ) {}

    public function withHeader(string $name, string $value): static
    {
        $clone = clone $this;
        $clone->headers[$name] = $value;
        return $clone;
    }

    public function getStatusCode(): int { return $this->status; }
    public function getBody(): string { return json_encode($this->data); }
}
