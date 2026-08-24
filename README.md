# 🐘 DPX-Php: Pattern Scanner, Software Architecture Analyzer & Data Flow Engine for PHP

> **Hexagonal Architecture (Ports & Adapters) + Domain-Driven Design (DDD)** static analysis and software design pattern detection engine for **PHP (7.4 - 8.4+)** powered by a high-performance **native Regex/AST PHP parser** (zero external grammar dependencies).

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=flat&logo=python)](https://www.python.org/)
[![PHP](https://img.shields.io/badge/PHP-7.4%20--%208.4%2B-8892BF.svg?style=flat&logo=php)](https://www.php.net/)
[![Architecture](https://img.shields.io/badge/Architecture-Hexagonal%20%2B%20DDD-brightgreen.svg?style=flat)]()
[![Parser](https://img.shields.io/badge/Parser-Native%20PHP%20AST%20(Regex)-red.svg?style=flat)]()
[![Tests](https://img.shields.io/badge/Tests-18%20passed%20(100%25)-success.svg?style=flat)]()
[![Rules](https://img.shields.io/badge/Supported%20Rules-35%20(23%20GoF%20%2B%2010%20SOLID%2FPrinciples%20%2B%202%20Arch)-orange.svg?style=flat)]()
[![SARIF](https://img.shields.io/badge/SARIF-v2.1.0%20OASIS-blue.svg?style=flat)]()

---

## ✨ Key Capabilities

### 🔍 All 23 Gang of Four (GoF) Design Patterns Detected in PHP:
* **Creational**: Abstract Factory, Builder (Fluent method chaining returning `$this`/`static`), Factory Method, Prototype (`clone`/`withX()` idioms), Singleton (`static $instance` + `getInstance()`).
* **Structural**: Adapter, Bridge, Composite (hierarchical trees with component interfaces), Decorator (wrapping same interface), Facade, Flyweight, Proxy (Lazy loading, Security, Caching).
* **Behavioral**: Chain of Responsibility (`setNext()` handler chains), Command (execute/undo), Interpreter, Iterator (`Iterator`/`IteratorAggregate` interface), Mediator, Memento, Observer (`subscribe`/`emit` / `EventEmitter` + `EventListener`), State, Strategy (PHP `interface` polymorphic dispatch), Template Method (abstract + final method combinations), Visitor.

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
* **Pattern Scanner Dashboard**: Semantic UI Dark Theme, KPI stats, category filter pills, Evidence Trail heuristic inspector, instant search, and **AI Architectural Map** with one-click copy for LLM analysis.

### 📤 Multi-Format Export:
* Rich CLI Console, JSON, Markdown, OASIS SARIF v2.1.0 (GitHub Code Scanning), interactive HTML dashboards, and `--llm` XML/Markdown context.

---

## 🚀 Quick Start

```bash
git clone https://github.com/bivex/DPX-Php.git
cd DPX-Php
uv sync

# Scan a PHP project
uv run dpx scan /path/to/php/project

# Export interactive HTML dashboard
uv run dpx scan /path/to/php/project -H reports/dashboard.html

# Generate LLM architectural map (copy-paste to Claude / ChatGPT / Gemini)
uv run dpx scan /path/to/php/project --llm
```

---

## 📊 Benchmark

| Input | Files | Detections | Time |
|---|:---:|:---:|:---:|
| **4 PHP sample files** | 4 | 58 | **~0.06s** |

---

## 📄 License

Distributed under the MIT License.
