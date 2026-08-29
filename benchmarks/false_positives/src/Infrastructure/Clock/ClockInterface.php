<?php

declare(strict_types=1);

namespace App\Infrastructure\Clock;

interface ClockInterface
{
    public function now(): \DateTimeImmutable;
}
