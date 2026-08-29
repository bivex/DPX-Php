<?php

declare(strict_types=1);

namespace App\Domain\Model;

final class CustomerId
{
    public function __construct(
        private readonly string $value,
    ) {
        if (strlen($value) < 3) {
            throw new \InvalidArgumentException('CustomerId is too short');
        }
    }

    public function toString(): string
    {
        return $this->value;
    }

    public function equals(CustomerId $other): bool
    {
        return $this->value === $other->value;
    }
}
