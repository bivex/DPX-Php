<?php
/**
 * DPX-Php | Structural Design Patterns Demo
 * Covers: Adapter, Decorator, Facade, Composite, Proxy, Bridge
 */

declare(strict_types=1);

namespace DpxDemo\Structural;

// ─────────────────────────────────────────────────────────────────────────────
// ADAPTER
// ─────────────────────────────────────────────────────────────────────────────

interface PaymentGateway
{
    public function charge(float $amount, string $currency): bool;
    public function refund(string $transactionId, float $amount): bool;
}

class StripeClient
{
    public function createCharge(array $params): array
    {
        // Stripe-specific API
        return ['id' => 'ch_' . uniqid(), 'status' => 'succeeded'];
    }

    public function createRefund(string $chargeId, int $amountCents): array
    {
        return ['id' => 're_' . uniqid(), 'status' => 'succeeded'];
    }
}

class StripeAdapter implements PaymentGateway
{
    public function __construct(private StripeClient $stripe) {}

    public function charge(float $amount, string $currency): bool
    {
        $result = $this->stripe->createCharge([
            'amount' => (int)($amount * 100),
            'currency' => $currency,
        ]);
        return $result['status'] === 'succeeded';
    }

    public function refund(string $transactionId, float $amount): bool
    {
        $result = $this->stripe->createRefund($transactionId, (int)($amount * 100));
        return $result['status'] === 'succeeded';
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// DECORATOR
// ─────────────────────────────────────────────────────────────────────────────

interface CacheStore
{
    public function get(string $key): mixed;
    public function set(string $key, mixed $value, int $ttl = 3600): void;
    public function delete(string $key): void;
}

class RedisCache implements CacheStore
{
    private array $store = [];

    public function get(string $key): mixed
    {
        return $this->store[$key] ?? null;
    }

    public function set(string $key, mixed $value, int $ttl = 3600): void
    {
        $this->store[$key] = $value;
    }

    public function delete(string $key): void
    {
        unset($this->store[$key]);
    }
}

class LoggingCacheDecorator implements CacheStore
{
    public function __construct(private CacheStore $wrapped) {}

    public function get(string $key): mixed
    {
        $value = $this->wrapped->get($key);
        echo "[Cache] GET $key => " . ($value !== null ? 'HIT' : 'MISS') . "\n";
        return $value;
    }

    public function set(string $key, mixed $value, int $ttl = 3600): void
    {
        echo "[Cache] SET $key (ttl={$ttl}s)\n";
        $this->wrapped->set($key, $value, $ttl);
    }

    public function delete(string $key): void
    {
        echo "[Cache] DELETE $key\n";
        $this->wrapped->delete($key);
    }
}

class EncryptedCacheDecorator implements CacheStore
{
    public function __construct(private CacheStore $wrapped, private string $secretKey) {}

    public function get(string $key): mixed
    {
        $encrypted = $this->wrapped->get($key);
        return $encrypted !== null ? $this->decrypt($encrypted) : null;
    }

    public function set(string $key, mixed $value, int $ttl = 3600): void
    {
        $this->wrapped->set($key, $this->encrypt($value), $ttl);
    }

    public function delete(string $key): void
    {
        $this->wrapped->delete($key);
    }

    private function encrypt(mixed $value): string
    {
        return base64_encode(json_encode($value) . $this->secretKey);
    }

    private function decrypt(string $encrypted): mixed
    {
        $decoded = base64_decode($encrypted);
        $json = str_replace($this->secretKey, '', $decoded);
        return json_decode($json, true);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// FACADE
// ─────────────────────────────────────────────────────────────────────────────

class VideoConverter
{
    public function extractAudio(string $file): string { return "audio.wav"; }
    public function encodeVideo(string $file, string $format): string { return "output.$format"; }
}

class AudioEncoder
{
    public function encode(string $file, int $bitrate): string { return "encoded_{$bitrate}.mp3"; }
}

class SubtitleExtractor
{
    public function extract(string $file, string $lang): string { return "subtitles_{$lang}.srt"; }
}

class VideoConversionFacade
{
    private VideoConverter $converter;
    private AudioEncoder $audio;
    private SubtitleExtractor $subtitles;

    public function __construct()
    {
        $this->converter = new VideoConverter();
        $this->audio = new AudioEncoder();
        $this->subtitles = new SubtitleExtractor();
    }

    public function convertToMp4WithSubtitles(string $inputFile, string $language = 'en'): array
    {
        $audioFile = $this->converter->extractAudio($inputFile);
        $encodedAudio = $this->audio->encode($audioFile, 128);
        $videoFile = $this->converter->encodeVideo($inputFile, 'mp4');
        $subFile = $this->subtitles->extract($inputFile, $language);

        return [
            'video' => $videoFile,
            'audio' => $encodedAudio,
            'subtitles' => $subFile,
        ];
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// COMPOSITE
// ─────────────────────────────────────────────────────────────────────────────

interface FileSystemItem
{
    public function getName(): string;
    public function getSize(): int;
    public function render(int $depth = 0): string;
}

class FileItem implements FileSystemItem
{
    public function __construct(
        private readonly string $name,
        private readonly int $size,
    ) {}

    public function getName(): string { return $this->name; }
    public function getSize(): int { return $this->size; }

    public function render(int $depth = 0): string
    {
        return str_repeat('  ', $depth) . "📄 {$this->name} ({$this->size} bytes)\n";
    }
}

class Directory implements FileSystemItem
{
    /** @var FileSystemItem[] */
    private array $children = [];

    public function __construct(private readonly string $name) {}

    public function add(FileSystemItem $item): void
    {
        $this->children[] = $item;
    }

    public function getName(): string { return $this->name; }

    public function getSize(): int
    {
        return array_sum(array_map(fn($child) => $child->getSize(), $this->children));
    }

    public function render(int $depth = 0): string
    {
        $output = str_repeat('  ', $depth) . "📁 {$this->name}/\n";
        foreach ($this->children as $child) {
            $output .= $child->render($depth + 1);
        }
        return $output;
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// PROXY
// ─────────────────────────────────────────────────────────────────────────────

interface ImageRenderer
{
    public function render(): string;
}

class RealImage implements ImageRenderer
{
    private string $bitmap;

    public function __construct(private string $filename)
    {
        // Expensive: load from disk
        $this->bitmap = file_get_contents($filename) ?: "[binary data of $filename]";
    }

    public function render(): string
    {
        return "<img src=\"{$this->filename}\" />";
    }
}

class LazyImageProxy implements ImageRenderer
{
    private ?RealImage $realImage = null;

    public function __construct(private string $filename) {}

    public function render(): string
    {
        if ($this->realImage === null) {
            $this->realImage = new RealImage($this->filename);
        }
        return $this->realImage->render();
    }
}
