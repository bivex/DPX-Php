<?php

declare(strict_types=1);

namespace App\Domain\Model;

use App\Domain\Exception\InvalidAmountException;

final class Money
{
    public function __construct(
        private readonly int $amountInCents,
        private readonly string $currency = 'USD',
    ) {
        if ($this->amountInCents < 0) {
            throw new InvalidAmountException('Money amount cannot be negative');
        }
    }

    public function getAmountInCents(): int
    {
        return $this->amountInCents;
    }

    public function getCurrency(): string
    {
        return $this->currency;
    }

    public function add(Money $other): Money
    {
        if ($this->currency !== $other->currency) {
            throw new InvalidAmountException('Cannot add money with different currencies');
        }
        return new Money($this->amountInCents + $other->amountInCents, $this->currency);
    }

    public function equals(mixed $other): bool
    {
        if (!$other instanceof self) {
            return false;
        }
        return $this->amountInCents === $other->amountInCents && $this->currency === $other->currency;
    }
}
