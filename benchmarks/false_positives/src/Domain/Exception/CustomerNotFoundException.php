<?php

declare(strict_types=1);

namespace App\Domain\Exception;

final class CustomerNotFoundException extends \RuntimeException
{
    public function __construct(string $customerId)
    {
        parent::__construct(sprintf('Customer with ID %s was not found.', $customerId));
    }
}
