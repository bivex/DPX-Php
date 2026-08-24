"""PHP Middleware Pipeline Pattern Detection Rule.

In PHP, Middleware Pipeline is the de-facto HTTP request processing pattern:
- PSR-15 MiddlewareInterface / RequestHandlerInterface (used by Laravel, Slim, Symfony, Mezzio)
- Laravel-style: $this->middleware([...]) chaining in controllers & kernel
- Slim 4 style: $app->add(new Middleware()) layered pipeline assembly
- Custom: callable/Closure middleware stacks with $next($request) delegation
"""

from __future__ import annotations

from typing import Any

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


# PSR-15 / PHP middleware interface markers
_MIDDLEWARE_INTERFACE_NAMES = frozenset({
    "MiddlewareInterface",
    "RequestHandlerInterface",
    "HttpMiddlewareInterface",
    "MiddlewarePipe",
    "Pipeline",
})

# Common PHP middleware method names (PSR-15: process, Laravel: handle)
_MIDDLEWARE_PROCESS_METHODS = frozenset({
    "process",
    "handle",
    "invoke",
    "__invoke",
})

# $next($request) delegation — core PSR-15 / Slim / Laravel middleware signature
_NEXT_DELEGATE_PATTERNS = frozenset({
    "next",
    "handler",
    "delegate",
})

# Pipeline assembly method names (add/pipe/push/through/middleware)
_PIPELINE_ASSEMBLY_CALLS = frozenset({
    "add",
    "pipe",
    "push",
    "through",
    "middleware",
    "addMiddleware",
    "append",
    "prepend",
    "stack",
})


class MiddlewarePipelineRule(BasePatternRule):
    """Detects PHP Middleware Pipeline Pattern instances.

    In PHP ecosystems (Laravel, Slim, Symfony, Mezzio/Laminas, PSR-15), middleware
    pipelines are the canonical HTTP request/response processing pattern. This rule
    detects:

    1. **PSR-15 Middleware classes** implementing MiddlewareInterface / RequestHandlerInterface
       with a process($request, $handler) or handle($request, $next) method that delegates
       down the chain via $next($request) / $handler->handle($request).

    2. **Laravel Kernel / RouteMiddleware** - classes that register middleware stacks
       via $this->middleware([...]) or $this->middlewareGroups arrays.

    3. **Pipeline builder classes** that assemble a stack by calling add/pipe/push/through
       multiple times to build the handler chain.

    4. **Callable/Closure middleware** - __invoke($request, $response, $next) signatures
       that are the classic Slim 3 / PSR-15 pre-standard middleware style.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.MIDDLEWARE_PIPELINE

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        detections.extend(self._detect_psr15_middleware(model))
        detections.extend(self._detect_pipeline_builder(model))
        detections.extend(self._detect_laravel_kernel(model))
        return detections

    # ──────────────────────────────────────────────────────────────────────────
    # 1. PSR-15 Middleware: implements MiddlewareInterface + process/handle + $next
    # ──────────────────────────────────────────────────────────────────────────

    def _detect_psr15_middleware(self, model: CodeModel) -> list[Detection]:
        results: list[Detection] = []
        for rec in model.all_records():
            det = self._analyze_psr15_class(rec)
            if det:
                results.append(det)
        return results

    def _analyze_psr15_class(self, rec: Any) -> Detection | None:
        # Must implement a known middleware interface
        implements_middleware_iface = any(
            iface in _MIDDLEWARE_INTERFACE_NAMES
            for iface in rec.implemented_protocols
        )

        # Find process / handle / __invoke method
        process_methods = [
            m for m in rec.methods
            if m.name.split(".")[-1] in _MIDDLEWARE_PROCESS_METHODS
        ]

        if not process_methods:
            return None

        # Check for $next($request) / $handler->handle() delegation in the method body
        has_next_delegation = False
        next_param: str | None = None
        for m in process_methods:
            params = m.parameter_lists[0] if m.parameter_lists else []
            for p in params:
                if any(keyword in p.lower() for keyword in _NEXT_DELEGATE_PATTERNS):
                    has_next_delegation = True
                    next_param = p
                    break

        evidences: list[Evidence] = []

        if implements_middleware_iface:
            iface_names = [i for i in rec.implemented_protocols if i in _MIDDLEWARE_INTERFACE_NAMES]
            evidences.append(self.evidence(
                description=f"Implements PSR-15 middleware interface(s): {', '.join(iface_names)}",
                weight=0.55,
                location=rec.location,
                code_suffix="PSR15_MIDDLEWARE_INTERFACE",
            ))
        elif not has_next_delegation:
            return None  # Without interface AND without $next delegation, skip

        for m in process_methods:
            evidences.append(self.evidence(
                description=f"Defines PSR-15 middleware processing method '{m.name.split('.')[-1]}(Request, Handler)'",
                weight=0.40,
                location=m.location,
                code_suffix="MIDDLEWARE_PROCESS_METHOD",
            ))

        if has_next_delegation:
            evidences.append(self.evidence(
                description=f"Delegates request to next middleware in pipeline via '${next_param}'",
                weight=0.35,
                location=process_methods[0].location,
                code_suffix="MIDDLEWARE_NEXT_DELEGATION",
            ))

        if not evidences or sum(e.weight for e in evidences) < 0.40:
            return None

        return self.create_detection(
            target_name=rec.name,
            target_kind="middleware_class",
            evidences=evidences,
            primary_location=rec.location,
            summary=f"Middleware Pipeline: class '{rec.name}' is a PSR-15 middleware that intercepts and delegates HTTP requests",
        )

    # ──────────────────────────────────────────────────────────────────────────
    # 2. Pipeline builder: assembles stack with add/pipe/push/through calls
    # ──────────────────────────────────────────────────────────────────────────

    def _detect_pipeline_builder(self, model: CodeModel) -> list[Detection]:
        results: list[Detection] = []
        for rec in model.all_records():
            det = self._analyze_pipeline_builder(rec)
            if det:
                results.append(det)
        return results

    def _analyze_pipeline_builder(self, rec: Any) -> Detection | None:
        name_lower = rec.name.lower()
        is_pipeline_named = any(k in name_lower for k in (
            "pipeline", "pipe", "kernel", "stack", "dispatcher", "router"
        ))

        # Count assembly calls in ALL methods of this class
        assembly_calls: list[str] = []
        assembly_fields: list[str] = []

        for m in rec.methods:
            for call in m.calls:
                call_name = call.split("->")[-1].split("::")[-1].lower()
                if call_name in {a.lower() for a in _PIPELINE_ASSEMBLY_CALLS}:
                    assembly_calls.append(call)

        for field in rec.fields:
            if any(k in field.lower() for k in ("middleware", "stack", "pipeline", "layers", "handlers")):
                assembly_fields.append(field)

        if len(assembly_calls) < 2 and not (assembly_fields and is_pipeline_named):
            return None

        evidences: list[Evidence] = []

        if is_pipeline_named:
            evidences.append(self.evidence(
                description=f"Class '{rec.name}' follows Pipeline/Kernel/Stack naming convention",
                weight=0.35,
                location=rec.location,
                code_suffix="PIPELINE_CLASS_NAMING",
            ))

        if assembly_fields:
            evidences.append(self.evidence(
                description=f"Stores middleware stack as field(s): {', '.join(assembly_fields[:4])}",
                weight=0.40,
                location=rec.location,
                code_suffix="PIPELINE_MIDDLEWARE_FIELDS",
            ))

        if assembly_calls:
            unique_calls = list(dict.fromkeys(assembly_calls))[:5]
            evidences.append(self.evidence(
                description=f"Assembles pipeline by calling {len(assembly_calls)} middleware add/pipe/push operations: {', '.join(unique_calls)}",
                weight=min(0.55, 0.25 + 0.05 * len(assembly_calls)),
                location=rec.location,
                code_suffix="PIPELINE_ASSEMBLY_CALLS",
            ))

        return self.create_detection(
            target_name=rec.name,
            target_kind="middleware_pipeline_builder",
            evidences=evidences,
            primary_location=rec.location,
            summary=f"Middleware Pipeline: class '{rec.name}' assembles a layered request/response processing pipeline",
        )

    # ──────────────────────────────────────────────────────────────────────────
    # 3. Laravel HTTP Kernel: $middlewareGroups / $routeMiddleware arrays
    # ──────────────────────────────────────────────────────────────────────────

    def _detect_laravel_kernel(self, model: CodeModel) -> list[Detection]:
        results: list[Detection] = []
        for rec in model.all_records():
            det = self._analyze_laravel_kernel(rec)
            if det:
                results.append(det)
        return results

    def _analyze_laravel_kernel(self, rec: Any) -> Detection | None:
        # Detect Laravel-style kernel by field names
        has_middleware_groups = any(
            f in ("middleware", "middlewareGroups", "routeMiddleware", "middlewarePriority")
            for f in rec.fields
        )
        has_kernel_base = any(
            base in ("Kernel", "HttpKernel", "ConsoleKernel")
            for base in rec.implemented_protocols
        )
        name_lower = rec.name.lower()
        is_kernel_named = "kernel" in name_lower

        if not (has_middleware_groups and (has_kernel_base or is_kernel_named)):
            return None

        evidences: list[Evidence] = []

        if has_middleware_groups:
            mw_fields = [
                f for f in rec.fields
                if f in ("middleware", "middlewareGroups", "routeMiddleware", "middlewarePriority")
            ]
            evidences.append(self.evidence(
                description=f"Declares Laravel middleware stack via protected array field(s): {', '.join(mw_fields)}",
                weight=0.55,
                location=rec.location,
                code_suffix="LARAVEL_MIDDLEWARE_GROUPS",
            ))

        if has_kernel_base:
            evidences.append(self.evidence(
                description=f"Extends Laravel HTTP/Console Kernel base class: {', '.join(rec.implemented_protocols)}",
                weight=0.45,
                location=rec.location,
                code_suffix="LARAVEL_KERNEL_EXTENDS",
            ))
        elif is_kernel_named:
            evidences.append(self.evidence(
                description=f"Class '{rec.name}' follows Laravel Kernel naming convention",
                weight=0.30,
                location=rec.location,
                code_suffix="LARAVEL_KERNEL_NAMING",
            ))

        return self.create_detection(
            target_name=rec.name,
            target_kind="laravel_http_kernel",
            evidences=evidences,
            primary_location=rec.location,
            summary=f"Middleware Pipeline: class '{rec.name}' is a Laravel HTTP Kernel registering application middleware groups and route middleware",
        )
