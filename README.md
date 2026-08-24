# 🐘 DPX-Php: Design Pattern Detector & Software Architecture Scanner for PHP

> **Hexagonal Architecture (Ports & Adapters) + Domain-Driven Design (DDD)** static analysis and software design pattern detection engine for **PHP (7.4 - 8.4+)** with dual-engine AST parsing (Ultrafast Native & Formal ANTLR4).

[![PyPI Version](https://img.shields.io/pypi/v/dpx-php.svg?style=flat&color=blue)](https://pypi.org/project/dpx-php/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=flat&logo=python)](https://www.python.org/)
[![PHP](https://img.shields.io/badge/PHP-7.4%20--%208.4%2B-8892BF.svg?style=flat&logo=php)](https://www.php.net/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/Tests-42%20passed%20(100%25)-success.svg?style=flat)]()
[![Rules](https://img.shields.io/badge/Supported%20Rules-37%20Rules-orange.svg?style=flat)]()
[![SARIF](https://img.shields.io/badge/SARIF-v2.1.0%20OASIS-blue.svg?style=flat)]()

---

## 📦 Installation

```bash
# Using pip
pip install dpx-php

# Using uv
uv tool install dpx-php
```

---

## ✨ Key Capabilities

### 🔍 All 23 Gang of Four (GoF) Design Patterns + 2 PHP-Specific Idioms:
* **Creational**: Abstract Factory, Builder (Fluent method chaining returning `$this`/`static`), Factory Method, Prototype (`clone`/`withX()` idioms), Singleton (`static $instance` + `getInstance()`).
* **Structural**: Adapter, Bridge, Composite (hierarchical trees with component interfaces), Decorator (wrapping same interface), Facade, Flyweight, Proxy (Lazy loading, Security, Caching).
* **Behavioral**: Chain of Responsibility (`setNext()` handler chains), Command (execute/undo), Interpreter, Iterator (`Iterator`/`IteratorAggregate` interface), Mediator, Memento, Observer (`subscribe`/`emit` / `EventEmitter` + `EventListener`), State, Strategy (PHP `interface` polymorphic dispatch), Template Method (abstract + final method combinations), Visitor.
* **PHP-Specific Architecture**:
  * **PSR-15 Middleware Pipeline**: `MiddlewareInterface` / `RequestHandlerInterface` pipelines, Slim 4 `$app->add()` / `$app->pipe()` stacks, and Laravel HTTP Kernel `$middlewareGroups` / `$routeMiddleware`.
  * **Multimethod / Dynamic Type Dispatch**: PHP 8.0+ `match($type)` expression dispatch branches, Command/Event Bus dispatcher maps (`$handlers[$commandClass]->handle($command)`), and type discriminator registries.

### 🛡️ 10 SOLID Principles & Clean Code Rules:
* **SRP**: God Class detection (≥15 methods mixing multiple concerns).
* **OCP**: `instanceof`/`type` inspection cascades vs. polymorphic interface dispatch.
* **LSP**: Subclasses overriding parent methods with `throw new \RuntimeException(...)`.
* **ISP**: Fat Interfaces (≥8 methods) forcing unnecessary obligations.
* **DIP**: Direct `new ConcreteClass()` instantiation vs. constructor interface injection.
* **Law of Demeter**: Deep train wreck chains (`$order->getCustomer()->getProfile()->getAddress()->...`).
* **KISS**: High cyclomatic complexity functions and long parameter lists (≥5).
* **DRY**: Duplicate method bodies across classes and modules.
* **High Cohesion / Low Coupling**: High fan-out (≥10 dependencies in constructor).
* **Circular Dependency**: Inter-namespace import cycle detection via Tarjan's SCC.

### 🎨 Interactive HTML Dashboards:
* **Pattern Scanner Dashboard**: Semantic UI Dark Theme, KPI stats, category filter pills, Evidence Trail heuristic inspector, instant search, live `[ 🛡️ Hide SOLID & Principles ]` toggle, and **AI Architectural Map** with one-click copy for LLM analysis.

### 📤 Multi-Format Export:
* Rich CLI Console, JSON, Markdown, OASIS SARIF v2.1.0 (GitHub Code Scanning & CI/CD), interactive HTML dashboards, and `--llm` XML/Markdown context prompt.

---

## 🚀 Usage & CLI Commands

```bash
# Basic scan (terminal output)
dpx scan /path/to/php/project

# Scan and export standalone interactive HTML dashboard
dpx scan /path/to/php/project -H reports/dashboard.html

# Scan GoF & Architecture patterns only (exclude SOLID/Clean code rules)
dpx scan /path/to/php/project -H reports/patterns_only.html --no-principles

# Filter by minimum confidence (low, medium, high, very_high)
dpx scan /path/to/php/project -c high

# Scan specific patterns only
dpx scan /path/to/php/project -p singleton -p factory_method -p strategy

# Use formal ANTLR4 parser engine
dpx scan /path/to/php/project --parser antlr

# Generate SARIF v2.1.0 report for GitHub Security / Code Scanning
dpx scan /path/to/php/project -S report.sarif

# Generate AI Architectural Context Prompt (paste to Claude / ChatGPT / Gemini)
dpx scan /path/to/php/project --llm
```

---

## ⚙️ Parser Engines (Pluggable via Hexagonal Ports)

| Engine | Flag | Description | Performance |
|---|---|---|---|
| **Native Regex & Balanced Braces** | `--parser native` *(default)* | Pure Python, zero external dependencies, ultrafast and resilient on all PHP dialects (7.4 – 8.4+) | **270–1 400 files/s** |
| **ANTLR4 PHP Grammar** | `--parser antlr` | Formal AST/CST conforming strictly to PHP language specification (`PHPLexer.g4` & `PHPParser.g4`) | **10–50 files/s** |

---

## 📊 Real-World Framework Benchmarks

| Project / Framework | Production Files | Findings | Scan Time | Speed |
|---|:---:|:---:|:---:|:---:|
| **Symfony Components Monorepo** | **7 797** | **5 755** | 71.6s | **109 files/s** |
| **Laravel Framework Core** | **1 600** | **1 753** | 9.0s | **177 files/s** |
| **Monolog Logger** | **121** | **140** | 0.23s | **527 files/s** |
| **Guzzle HTTP Client** | **70** | **76** | 0.51s | **137 files/s** |
| **Slim 4 Micro-Framework** | **72** | **68** | 0.09s | **803 files/s** |

---

## 🧪 Running Tests

```bash
uv run pytest -v
```

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

