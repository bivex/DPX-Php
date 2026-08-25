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

---

## 🌐 The DPX Multi-Language Static Analysis Family (33 Languages)

| # | Language | Repository | Ecosystem & Focus |
|:---:|---|---|---|
| 1 | **Ada** | [`bivex/DPX-Ada`](https://github.com/bivex/DPX-Ada) | Ada 2012/2022, SPARK Contracts, Ravenscar Tasking, DO-178C Safety |
| 2 | **Clojure** | [`bivex/DPX`](https://github.com/bivex/DPX) | Lisp S-Expressions, Protocols, Multimethods |
| 3 | **C** | [`bivex/DPX-C`](https://github.com/bivex/DPX-C) | Memory Safety, Struct VTables, Idiomatic C11/C23 |
| 4 | **Cairo** | [`bivex/DPX-Cairo`](https://github.com/bivex/DPX-Cairo) | Starknet Smart Contracts, ZK-Rollup Invariants |
| 5 | **C++** | [`bivex/DPX-Cpp`](https://github.com/bivex/DPX-Cpp) | RAII, CRTP, Concepts, Modern C++20/23 |
| 6 | **C#** | [`bivex/DPX-CSharp`](https://github.com/bivex/DPX-CSharp) | .NET 9, Roslyn AST, Linq, Records |
| 7 | **Dart** | [`bivex/DPX-Dart`](https://github.com/bivex/DPX-Dart) | Dart 3.x, Flutter, BLoC, Riverpod, Isolates |
| 8 | **Elixir** | [`bivex/DPX-Elixir`](https://github.com/bivex/DPX-Elixir) | BEAM OTP, GenServer, Supervisors |
| 9 | **Erlang** | [`bivex/DPX-Erlang`](https://github.com/bivex/DPX-Erlang) | Fault Tolerance, Actor Model, OTP Behaviors |
| 10 | **Gleam** | [`bivex/DPX-Gleam`](https://github.com/bivex/DPX-Gleam) | Type-Safe BEAM, Actor Concurrency |
| 11 | **Go** | [`bivex/DPX-Go`](https://github.com/bivex/DPX-Go) | Goroutines, Channels, Composition, Interfaces |
| 12 | **Haskell** | [`bivex/DPX-Haskell`](https://github.com/bivex/DPX-Haskell) | Pure Functional, Monads, Typeclasses, Arrows |
| 13 | **Huff** | [`bivex/DPX-Huff`](https://github.com/bivex/DPX-Huff) | Low-Level EVM Bytecode & Opcodes |
| 14 | **Idris 2** | [`bivex/DPX-Idris2`](https://github.com/bivex/DPX-Idris2) | Dependent Types, QTT Linear Protocols, Totality, Proofs |
| 15 | **Java** | [`bivex/DPX-Java`](https://github.com/bivex/DPX-Java) | Spring Boot, Enterprise Java, JVM Invariants |
| 16 | **Julia** | [`bivex/DPX-Julia`](https://github.com/bivex/DPX-Julia) | Multiple Dispatch, Scientific Computing |
| 17 | **Kotlin** | [`bivex/DPX-Kotlin`](https://github.com/bivex/DPX-Kotlin) | Coroutines, Multiplatform, Functional DSLs |
| 18 | **Lua** | [`bivex/DPX-Lua`](https://github.com/bivex/DPX-Lua) | Metatables, Coroutines, LuaJIT, Neovim |
| 19 | **Mojo** | [`bivex/DPX-Mojo`](https://github.com/bivex/DPX-Mojo) | SIMD Hardware, Memory Lifetimes, AI Systems |
| 20 | **Move** | [`bivex/DPX-Move`](https://github.com/bivex/DPX-Move) | Aptos & Sui Resource Safety, Linear Types |
| 21 | **OCaml** | [`bivex/DPX-OCaml`](https://github.com/bivex/DPX-OCaml) | Algebraic Data Types, Functors, Polymorphism |
| 22 | **PHP** | [`bivex/DPX-Php`](https://github.com/bivex/DPX-Php) | Modern PHP 8.4, Attributes, Traits, Laravel |
| 23 | **Prolog** | [`bivex/DPX-Prolog`](https://github.com/bivex/DPX-Prolog) | ISO Prolog, SWI-Prolog, DCG, CLP(FD/R/Q), CHR, Meta-Interpreters |
| 24 | **Puppet** | [`bivex/DPX-Puppet`](https://github.com/bivex/DPX-Puppet) | Puppet DSL, Roles/Profiles, IaC Security, Hiera |
| 25 | **Python** | [`bivex/DPX-Py`](https://github.com/bivex/DPX-Py) | Metaprogramming, Protocols, Hexagonal DDD |
| 26 | **Ruby** | [`bivex/DPX-Ruby`](https://github.com/bivex/DPX-Ruby) | Ruby 3.x, Rails, Metaprogramming, Dry-RB, Security |
| 27 | **Rust** | [`bivex/DPX-Rust`](https://github.com/bivex/DPX-Rust) | Zero-Cost Abstractions, Borrow Checker, Traits |
| 28 | **Solidity** | [`bivex/DPX-Solidity`](https://github.com/bivex/DPX-Solidity) | DeFi Security, Reentrancy, EVM Yul/Assembly |
| 29 | **SQL** | [`bivex/DPX-SQL`](https://github.com/bivex/DPX-SQL) | PostgreSQL, MySQL, SQLite, T-SQL, PL/SQL |
| 30 | **Swift** | [`bivex/DPX-Swift`](https://github.com/bivex/DPX-Swift) | Protocol-Oriented Programming, Actors |
| 31 | **TypeScript** | [`bivex/DPX-TypeScript`](https://github.com/bivex/DPX-TypeScript) | Generics, Conditional Types, Clean Architecture |
| 32 | **Yul** | [`bivex/DPX-Yul`](https://github.com/bivex/DPX-Yul) | EVM Intermediate Representation Optimization |
| 33 | **Zig** | [`bivex/DPX-Zig`](https://github.com/bivex/DPX-Zig) | Comptime, Manual Memory Allocators, C ABI |

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
