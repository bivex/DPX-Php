<?php

declare(strict_types=1);

namespace App\Domain\Model;

class Customer
{
    public function __construct(
        private readonly CustomerId $id,
        private string $name,
        private string $email,
        private bool $active = true,
    ) {}

    public function getId(): CustomerId
    {
        return $this->id;
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function getEmail(): string
    {
        return $this->email;
    }

    public function isActive(): bool
    {
        return $this->active;
    }

    public function deactivate(): void
    {
        $this->active = false;
    }

    public function updateEmail(string $newEmail): void
    {
        $this->email = $newEmail;
    }
}
