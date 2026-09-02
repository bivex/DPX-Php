"""Comprehensive tests for the ANTLR4 PHP parser backend and adapter."""

import pytest
from typer.testing import CliRunner

from pattern_detector.adapters.inbound.cli.main import app
from pattern_detector.adapters.outbound.php_antlr import AntlrPhpParserAdapter
from pattern_detector.bootstrap import create_container
from pattern_detector.domain.pattern import PatternType

runner = CliRunner()


@pytest.fixture
def antlr_adapter() -> AntlrPhpParserAdapter:
    return AntlrPhpParserAdapter()


def test_antlr_parse_empty_source(antlr_adapter: AntlrPhpParserAdapter) -> None:
    ns = antlr_adapter.parse_source("", "empty.php")
    assert ns.name == "empty"
    assert len(ns.records) == 0


def test_antlr_parse_class_and_interface(antlr_adapter: AntlrPhpParserAdapter) -> None:
    code = r"""<?php
    namespace App\Services;

    use App\Repositories\UserRepository;

    interface UserServiceInterface {
        public function findUser(int $id): ?object;
    }

    class UserService implements UserServiceInterface {
        private UserRepository $repo;

        public function __construct(UserRepository $repo) {
            $this->repo = $repo;
        }

        public function findUser(int $id): ?object {
            return $this->repo->find($id);
        }
    }
    """
    model = antlr_adapter.parse_sources({"UserService.php": code})
    assert "App.Services" in model.namespaces

    records = list(model.all_records())
    assert len(records) == 1
    rec = records[0]
    assert rec.name == "UserService"
    assert "repo" in rec.fields
    assert "UserServiceInterface" in rec.implemented_protocols
    assert len(rec.methods) == 2

    protocols = list(model.all_protocols())
    assert len(protocols) == 1
    proto = protocols[0]
    assert proto.name == "UserServiceInterface"
    assert proto.has_method("findUser")


def test_antlr_constructor_promotion_and_enums(antlr_adapter: AntlrPhpParserAdapter) -> None:
    code = r"""<?php
    namespace App\Domain;

    enum UserStatus: string {
        case ACTIVE = 'active';
        case INACTIVE = 'inactive';
    }

    class Customer {
        public function __construct(
            public string $id,
            protected string $name,
            private int $age
        ) {}
    }
    """
    model = antlr_adapter.parse_sources({"Domain.php": code})
    records_by_name = {r.name: r for r in model.all_records()}

    assert "UserStatus" in records_by_name
    assert records_by_name["UserStatus"].is_type is True

    assert "Customer" in records_by_name
    customer = records_by_name["Customer"]
    assert "id" in customer.fields
    assert "name" in customer.fields
    assert "age" in customer.fields


def test_antlr_singleton_detection() -> None:
    container = create_container("antlr")
    code = r"""<?php
    namespace App\Patterns;

    class AppConfig {
        private static ?AppConfig $instance = null;

        private function __construct() {}

        public static function getInstance(): AppConfig {
            if (self::$instance === null) {
                self::$instance = new self();
            }
            return self::$instance;
        }
    }
    """
    model = container.parser.parse_sources({"AppConfig.php": code})
    report = container.detector_service.detect_all(model)
    singleton_types = [d.pattern_type for d in report.detections]
    assert PatternType.SINGLETON in singleton_types


def test_antlr_cli_scan_option() -> None:
    result = runner.invoke(app, ["scan", "examples/php_samples/PhpSpecificPatternsDemo.php", "-P", "antlr"])
    assert result.exit_code == 0
    assert "Detection Summary" in result.stdout
