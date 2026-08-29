<?php

declare(strict_types=1);

namespace App\Application\Service;

use App\Application\DTO\CreateCustomerRequest;
use App\Application\DTO\CustomerResponse;
use App\Domain\Model\Customer;
use App\Domain\Model\CustomerId;
use App\Infrastructure\Cache\ArrayCache;

final class CustomerService
{
    private array $customers = [];

    public function __construct(
        private readonly ArrayCache $cache,
    ) {}

    public function registerCustomer(CreateCustomerRequest $request): CustomerResponse
    {
        $id = new CustomerId(uniqid('cust_', true));
        $customer = new Customer($id, $request->name, $request->email);
        $this->customers[$id->toString()] = $customer;
        $this->cache->set($id->toString(), $customer);

        return new CustomerResponse(
            $customer->getId()->toString(),
            $customer->getName(),
            $customer->getEmail(),
            $customer->isActive(),
        );
    }
}
