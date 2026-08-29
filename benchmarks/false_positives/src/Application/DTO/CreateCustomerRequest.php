<?php

declare(strict_types=1);

namespace App\Application\DTO;

final class CreateCustomerRequest
{
    public function __construct(
        public readonly string $name,
        public readonly string $email,
    ) {}
}
