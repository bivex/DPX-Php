<?php
/**
 * DPX-Php | SOLID Principles & Clean Code Demo
 * Covers: SRP (God Class), OCP, LSP, ISP, DIP, Law of Demeter, KISS, DRY, High Coupling
 */

declare(strict_types=1);

namespace DpxDemo\Principles;

// ─────────────────────────────────────────────────────────────────────────────
// SRP VIOLATION: God Class (does everything in one class)
// ─────────────────────────────────────────────────────────────────────────────

class UserManager
{
    // User CRUD
    public function createUser(array $data): array { return $data; }
    public function updateUser(int $id, array $data): array { return $data; }
    public function deleteUser(int $id): bool { return true; }
    public function getUserById(int $id): array { return ['id' => $id]; }
    public function listAllUsers(): array { return []; }
    // Authentication
    public function login(string $email, string $password): string { return 'token'; }
    public function logout(string $token): void {}
    public function resetPassword(string $email): void {}
    public function changePassword(int $userId, string $newPwd): void {}
    // Email notifications
    public function sendWelcomeEmail(int $userId): void {}
    public function sendPasswordResetEmail(string $email): void {}
    public function sendAccountLockedEmail(int $userId): void {}
    // Billing
    public function chargeUser(int $userId, float $amount): bool { return true; }
    public function refundUser(int $userId, float $amount): bool { return true; }
    public function generateInvoice(int $userId, int $month): string { return 'invoice'; }
    // Analytics
    public function trackEvent(int $userId, string $event): void {}
    public function generateActivityReport(int $userId): array { return []; }
}

// ─────────────────────────────────────────────────────────────────────────────
// OCP VIOLATION: type-switching instead of polymorphism
// ─────────────────────────────────────────────────────────────────────────────

class ShapeCalculator
{
    public function calculateArea(object $shape): float
    {
        if ($shape instanceof \stdClass && $shape->type === 'circle') {
            return M_PI * $shape->radius ** 2;
        } elseif ($shape instanceof \stdClass && $shape->type === 'rectangle') {
            return $shape->width * $shape->height;
        } elseif ($shape instanceof \stdClass && $shape->type === 'triangle') {
            return 0.5 * $shape->base * $shape->height;
        }
        return 0.0;
    }
}

// OCP-COMPLIANT version
interface Shape
{
    public function area(): float;
}

class Circle implements Shape
{
    public function __construct(private float $radius) {}
    public function area(): float { return M_PI * $this->radius ** 2; }
}

class Rectangle implements Shape
{
    public function __construct(private float $width, private float $height) {}
    public function area(): float { return $this->width * $this->height; }
}

// ─────────────────────────────────────────────────────────────────────────────
// LSP VIOLATION: subclass refuses parent contract
// ─────────────────────────────────────────────────────────────────────────────

class Bird
{
    public function fly(): string
    {
        return "Flying...";
    }
}

class Penguin extends Bird
{
    public function fly(): string
    {
        throw new \RuntimeException("Penguins cannot fly!");
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// ISP VIOLATION: Fat Interface
// ─────────────────────────────────────────────────────────────────────────────

interface WorkerInterface
{
    public function work(): void;
    public function eat(): void;
    public function sleep(): void;
    public function takeBreak(): void;
    public function attendMeeting(): void;
    public function submitTimesheet(): void;
    public function requestVacation(): void;
    public function receivePaycheck(): void;
}

// ISP-COMPLIANT: split into role interfaces
interface Workable { public function work(): void; }
interface Eatable { public function eat(): void; }
interface Manageable { public function submitTimesheet(): void; }

// ─────────────────────────────────────────────────────────────────────────────
// DIP VIOLATION: direct concrete instantiation
// ─────────────────────────────────────────────────────────────────────────────

class MySqlUserRepository
{
    public function findById(int $id): array { return ['id' => $id]; }
    public function save(array $user): void {}
}

class UserServiceViolation
{
    private MySqlUserRepository $repository;

    public function __construct()
    {
        // DIP violation: hardwired concrete dependency
        $this->repository = new MySqlUserRepository();
    }

    public function getUser(int $id): array
    {
        return $this->repository->findById($id);
    }
}

// DIP-COMPLIANT:
interface UserRepository
{
    public function findById(int $id): array;
    public function save(array $user): void;
}

class UserService
{
    public function __construct(
        // Injected via abstraction (DIP)
        private readonly UserRepository $repository,
    ) {}

    public function getUser(int $id): array
    {
        return $this->repository->findById($id);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// LAW OF DEMETER VIOLATION: train wreck dot chain
// ─────────────────────────────────────────────────────────────────────────────

class OrderController
{
    public function processOrder(Order $order): void
    {
        // LOD violation: navigating object graph depth 4+
        $postalCode = $order->getCustomer()->getProfile()->getAddress()->getPostalCode();
        $taxRate = $order->getCustomer()->getProfile()->getAddress()->getRegion()->getTaxRate();
        $discount = $order->getCustomer()->getLoyaltyProgram()->getTier()->getDiscount();
        echo "Postal: $postalCode | Tax: $taxRate | Discount: $discount\n";
    }
}

// Stub classes for the LOD violation demo
class Order
{
    public function getCustomer(): Customer { return new Customer(); }
}

class Customer
{
    public function getProfile(): Profile { return new Profile(); }
    public function getLoyaltyProgram(): LoyaltyProgram { return new LoyaltyProgram(); }
}

class Profile
{
    public function getAddress(): Address { return new Address(); }
}

class Address
{
    public function getPostalCode(): string { return '10001'; }
    public function getRegion(): Region { return new Region(); }
}

class Region
{
    public function getTaxRate(): float { return 0.08; }
}

class LoyaltyProgram
{
    public function getTier(): LoyaltyTier { return new LoyaltyTier(); }
}

class LoyaltyTier
{
    public function getDiscount(): float { return 0.15; }
}

// ─────────────────────────────────────────────────────────────────────────────
// KISS VIOLATION: high cyclomatic complexity function
// ─────────────────────────────────────────────────────────────────────────────

function calculateShippingCost(
    float $weight,
    string $destination,
    string $carrier,
    bool $expressShipping,
    bool $insured,
    bool $fragile,
    int $packageCount,
    string $customerTier
): float {
    $base = 5.0;
    if ($weight > 5) {
        $base += ($weight - 5) * 0.5;
    } elseif ($weight > 2) {
        $base += ($weight - 2) * 0.3;
    }
    if ($destination === 'international') {
        $base *= 2.5;
        if ($carrier === 'DHL') {
            $base *= 1.2;
        } elseif ($carrier === 'FedEx') {
            $base *= 1.15;
        }
    } elseif ($destination === 'remote') {
        $base *= 1.8;
    }
    if ($expressShipping) {
        $base *= 1.5;
    }
    if ($insured) {
        $base += $weight * 0.25;
    }
    if ($fragile) {
        $base += 3.0;
        if ($expressShipping) {
            $base += 2.0;
        }
    }
    if ($packageCount > 1) {
        $base += ($packageCount - 1) * 2.0;
    }
    if ($customerTier === 'gold') {
        $base *= 0.8;
    } elseif ($customerTier === 'silver') {
        $base *= 0.9;
    }
    return round($base, 2);
}

// ─────────────────────────────────────────────────────────────────────────────
// HIGH COUPLING VIOLATION
// ─────────────────────────────────────────────────────────────────────────────

class ReportGenerator
{
    // High fan-out: depends on 10+ concrete classes (coupling violation)
    private MySqlUserRepository $userRepo;
    private OrderController $orderCtrl;
    private UserManager $userManager;
    private ShapeCalculator $shapeCalc;
    private VideoConversionFacade $videoFacade;

    public function __construct()
    {
        $this->userRepo = new MySqlUserRepository();
        $this->orderCtrl = new OrderController();
        $this->userManager = new UserManager();
        $this->shapeCalc = new ShapeCalculator();
        $this->videoFacade = new \DpxDemo\Structural\VideoConversionFacade();
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// DRY VIOLATION: duplicated logic across methods
// ─────────────────────────────────────────────────────────────────────────────

class InvoiceService
{
    public function calculateSubtotal(array $items): float
    {
        $total = 0.0;
        foreach ($items as $item) {
            if ($item['active'] ?? false) {
                $total += $item['price'] * $item['quantity'];
            }
        }
        return $total;
    }

    public function calculateTax(array $items): float
    {
        $total = 0.0;
        foreach ($items as $item) {
            if ($item['active'] ?? false) {
                $total += $item['price'] * $item['quantity'];
            }
        }
        return round($total * 0.21, 2); // DRY violation: same loop duplicated
    }
}
