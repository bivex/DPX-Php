<?php

declare(strict_types=1);

namespace App\Application\DTO;

final class CustomerResponse
{
    public function __construct(
        public readonly string $id,
        public readonly string $name,
        public readonly string $email,
        public readonly bool $active,
    ) {}
}
