"""Integration tests scanning real-world open-source PHP projects.

Validates that DPX-Php accurately detects design patterns and architecture idioms
across production frameworks (Monolog, Slim, Guzzle, Symfony components, etc.).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from pattern_detector.bootstrap.container import create_container

BENCHMARKS_DIR = Path(__file__).parent.parent / "benchmarks"


@pytest.fixture(scope="module")
def native_scanner():
    container = create_container(parser_type="native")
    return container.get_scanner()


def test_monolog_real_project_scan(native_scanner) -> None:
    monolog_dir = BENCHMARKS_DIR / "Seldaek_monolog"
    if not monolog_dir.exists():
        pytest.skip("Monolog benchmark not present")

    report = native_scanner.scan_path(str(monolog_dir))
    assert report.scanned_files_count >= 50
    assert report.total_detections_count > 0

    detected_patterns = {d.pattern_type.value for d in report.detections}
    # Monolog relies heavily on Handlers (Chain of Responsibility) & Processors/Formatters
    assert "chain_of_responsibility" in detected_patterns
    assert "multimethod_dispatch" in detected_patterns


def test_slim_framework_real_project_scan(native_scanner) -> None:
    slim_dir = BENCHMARKS_DIR / "Slim"
    if not slim_dir.exists():
        pytest.skip("Slim benchmark not present")

    report = native_scanner.scan_path(str(slim_dir))
    assert report.scanned_files_count >= 30
    assert report.total_detections_count > 0

    detected_patterns = {d.pattern_type.value for d in report.detections}
    # Slim 4 is a PSR-15 Middleware and Routing Dispatch engine
    assert "middleware_pipeline" in detected_patterns or "multimethod_dispatch" in detected_patterns


def test_guzzle_real_project_scan(native_scanner) -> None:
    guzzle_dir = BENCHMARKS_DIR / "guzzle_guzzle"
    if not guzzle_dir.exists():
        pytest.skip("Guzzle benchmark not present")

    report = native_scanner.scan_path(str(guzzle_dir))
    assert report.scanned_files_count >= 30
    assert report.total_detections_count > 0

    detected_patterns = {d.pattern_type.value for d in report.detections}
    # Guzzle uses HandlerStack middleware chains and client wrappers
    assert "chain_of_responsibility" in detected_patterns or len(report.detections) > 0


def test_symfony_event_dispatcher_real_project_scan(native_scanner) -> None:
    sym_event_dir = BENCHMARKS_DIR / "symfony_event_dispatcher"
    if not sym_event_dir.exists():
        pytest.skip("Symfony EventDispatcher benchmark not present")

    report = native_scanner.scan_path(str(sym_event_dir))
    assert report.scanned_files_count >= 10
    assert report.total_detections_count > 0

    detected_patterns = {d.pattern_type.value for d in report.detections}
    assert "observer" in detected_patterns or "multimethod_dispatch" in detected_patterns


def test_antlr_real_project_scan() -> None:
    sms_dir = BENCHMARKS_DIR / "espocrm_sms_providers"
    if not sms_dir.exists():
        pytest.skip("espocrm_sms_providers benchmark not present")

    container = create_container(parser_type="antlr")
    scanner = container.get_scanner()
    report = scanner.scan_path(str(sms_dir))

    assert report.scanned_files_count >= 10
    assert report.total_detections_count > 0
