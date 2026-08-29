<?php

declare(strict_types=1);

namespace App\Infrastructure\Utils;

final class MathUtils
{
    public static function clamp(int|float $val, int|float $min, int|float $max): int|float
    {
        return max($min, min($max, $val));
    }

    public static function percentage(float $part, float $total): float
    {
        if ($total <= 0.0) {
            return 0.0;
        }
        return ($part / $total) * 100.0;
    }
}
