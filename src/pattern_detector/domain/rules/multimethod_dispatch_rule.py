"""PHP Multimethod / Type-Based Polymorphic Dispatch Pattern Detection Rule.

In PHP, Clojure's `defmulti/defmethod` maps to several dynamic dispatch idioms:
1. **Match expressions** (PHP 8.0+): `match($type) { ... }` replacing type-switching if/elseif chains.
2. **Dispatcher maps** (array of callables): `$this->handlers[$type]($payload)` runtime dispatch.
3. **Tagged union / discriminated union** patterns: dispatch on a `->getType()` / `->kind` field.
4. **Event/Command bus dispatch**: `$handler = $this->resolveHandler($command)` style handler maps.
"""

from __future__ import annotations

from typing import Any

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import Evidence, PatternType


# Handler/dispatcher registry field names
_DISPATCHER_FIELD_NAMES = frozenset({
    "handlers",
    "dispatch",
    "dispatchers",
    "map",
    "routes",
    "resolvers",
    "registry",
    "commandHandlers",
    "eventHandlers",
    "strategies",
    "processors",
    "actions",
})

# Dispatch resolution method name patterns
_DISPATCH_METHOD_NAMES = frozenset({
    "dispatch",
    "resolve",
    "handle",
    "execute",
    "route",
    "process",
    "register",
})

# Body keywords indicating match/dynamic dispatch
_MATCH_KEYWORDS = frozenset({
    "match(",
    "match (",
    "gettype(",
    "get_class(",
})

# Builder-style registration patterns in body text
_REGISTER_PATTERNS = frozenset({
    "->register(",
    "->add(",
    "->map(",
    "[$type]",
    "[$command]",
    "[$event]",
    "[$key]",
    "[$name]",
})


class MultimethodDispatchRule(BasePatternRule):
    """Detects PHP Multimethod / Type-Based Polymorphic Dispatch Pattern instances.

    This rule detects PHP equivalents of Clojure's defmulti/defmethod dispatch:

    1. **Match-expression dispatch** (PHP 8.0+): `match($type) { 'foo' => ..., 'bar' => ... }`
       or `match(true)` pattern-matching blocks that dispatch to different algorithms
       based on a type/kind discriminator value. Replaces long if/elseif instanceof chains.

    2. **Callable dispatcher map**: Class holding an array/map of callables/handlers
       (`$this->handlers[$type]($payload)`) that resolves and executes a handler
       by a runtime key — the PHP equivalent of `(defmulti f dispatch-fn)`.

    3. **Command/Event Bus dispatch**: Service classes that resolve a specific
       `HandlerInterface` implementation by command/event class name at runtime
       (`$this->resolveHandler(get_class($command))`), enabling open-closed
       extensible dispatch without switch/match.

    4. **Self-registering handler map**: Handler registries built via
       `$this->register('type', fn($x) => ...)` or `$this->handlers['type'] = new FooHandler()`
       that accumulate callable dispatch branches dynamically.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.MULTIMETHOD_DISPATCH

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        detections.extend(self._detect_dispatcher_maps(model))
        detections.extend(self._detect_match_dispatch_functions(model))
        return detections

    # ──────────────────────────────────────────────────────────────────────────
    # 1. Dispatcher map: class with handler registry field + resolve/dispatch method
    # ──────────────────────────────────────────────────────────────────────────

    def _detect_dispatcher_maps(self, model: CodeModel) -> list[Detection]:
        results: list[Detection] = []
        for rec in model.all_records():
            det = self._analyze_dispatcher_class(rec)
            if det:
                results.append(det)
        return results

    def _analyze_dispatcher_class(self, rec: Any) -> Detection | None:
        name_lower = rec.name.lower()
        is_dispatcher_named = any(k in name_lower for k in (
            "dispatcher", "dispatch", "bus", "router", "resolver",
            "registry", "locator",
        ))

        # Find dispatcher-style fields
        dispatcher_fields = [
            f for f in rec.fields
            if f.lower() in {d.lower() for d in _DISPATCHER_FIELD_NAMES}
        ]

        # Find dispatch/resolve methods
        dispatch_methods = [
            m for m in rec.methods
            if any(kw in m.name.split(".")[-1].lower() for kw in _DISPATCH_METHOD_NAMES)
        ]

        # Check method bodies for handler map access patterns: $this->handlers[$type]
        has_dynamic_lookup = False
        has_registration = False
        registration_count = 0

        for m in rec.methods:
            body = m.body_text
            if not body:
                continue
            # Array dispatch lookup: $this->handlers[$type] / $handlers[$command] etc.
            if "handlers[" in body or "dispatchers[" in body or "map[" in body or "registry[" in body:
                has_dynamic_lookup = True
            # get_class() / match() dispatch
            if any(kw in body for kw in _MATCH_KEYWORDS):
                has_dynamic_lookup = True
            # Registration patterns
            for pat in _REGISTER_PATTERNS:
                if pat in body:
                    has_registration = True
                    registration_count += 1

        # Score threshold: must have actual handler map mechanics (fields, dynamic lookup, or registration)
        if not (len(dispatcher_fields) > 0 or has_dynamic_lookup or has_registration):
            return None

        indicators = sum([
            is_dispatcher_named,
            len(dispatcher_fields) > 0,
            len(dispatch_methods) > 0,
            has_dynamic_lookup,
            has_registration,
        ])

        if indicators < 2:
            return None

        evidences: list[Evidence] = []

        if is_dispatcher_named:
            evidences.append(self.evidence(
                description=f"Class '{rec.name}' follows Dispatcher/Bus/Router/Registry naming convention",
                weight=0.30,
                location=rec.location,
                code_suffix="DISPATCHER_CLASS_NAMING",
            ))

        if dispatcher_fields:
            evidences.append(self.evidence(
                description=f"Maintains callable handler registry in field(s): {', '.join(dispatcher_fields[:4])}",
                weight=0.45,
                location=rec.location,
                code_suffix="DISPATCHER_HANDLER_MAP",
            ))

        if has_dynamic_lookup:
            evidences.append(self.evidence(
                description="Performs dynamic handler lookup at runtime: $handlers[$type]($payload) — PHP equivalent of Clojure defmulti dispatch",
                weight=0.50,
                location=rec.location,
                code_suffix="DYNAMIC_TYPE_DISPATCH_LOOKUP",
            ))

        if has_registration:
            evidences.append(self.evidence(
                description=f"Dynamically registers {registration_count} dispatch branch(es) at runtime (self-registering handler map)",
                weight=min(0.45, 0.20 + 0.05 * registration_count),
                location=rec.location,
                code_suffix="DYNAMIC_HANDLER_REGISTRATION",
            ))

        if dispatch_methods:
            method_names = [m.name.split(".")[-1] for m in dispatch_methods[:4]]
            evidences.append(self.evidence(
                description=f"Provides dispatch/resolve entry point method(s): {', '.join(method_names)}",
                weight=0.35,
                location=dispatch_methods[0].location,
                code_suffix="DISPATCH_ENTRY_METHOD",
            ))

        return self.create_detection(
            target_name=rec.name,
            target_kind="dispatcher_map_class",
            evidences=evidences,
            primary_location=rec.location,
            summary=f"Multimethod Dispatch: class '{rec.name}' implements PHP runtime type-based dispatch — maps type/command keys to interchangeable handler callables",
        )

    # ──────────────────────────────────────────────────────────────────────────
    # 2. Match / switch dispatch functions with 3+ branches on a type value
    # ──────────────────────────────────────────────────────────────────────────

    def _detect_match_dispatch_functions(self, model: CodeModel) -> list[Detection]:
        results: list[Detection] = []
        for fn in model.all_functions():
            det = self._analyze_match_dispatch_function(fn)
            if det:
                results.append(det)
        return results

    def _analyze_match_dispatch_function(self, fn: Any) -> Detection | None:
        body = fn.body_text
        if not body:
            return None

        # Count match expression arms ('=>' occurrences inside match block)
        match_arm_count = 0
        has_match_expr = "match(" in body or "match (" in body
        has_switch = "switch(" in body or "switch (" in body

        if has_match_expr:
            # Count '=>' arms (rough heuristic: each arm is a dispatch branch)
            import re
            match_blocks = re.findall(r'match\s*\([^)]+\)\s*\{([^}]+)\}', body, re.DOTALL)
            for block in match_blocks:
                match_arm_count += block.count("=>")

        if has_switch:
            import re
            case_count = len(re.findall(r'\bcase\b', body))
            match_arm_count += case_count

        # Must have at least 3 distinct dispatch branches
        if match_arm_count < 3:
            return None

        # Dispatch key indicators in function name/params
        fn_name_lower = fn.name.split(".")[-1].lower()
        is_dispatch_fn = any(k in fn_name_lower for k in (
            "dispatch", "resolve", "handle", "route", "process", "execute", "create"
        ))

        params = fn.parameter_lists[0] if fn.parameter_lists else []
        has_type_param = any(
            any(kw in p.lower() for kw in ("type", "kind", "action", "event", "command", "message"))
            for p in params
        )

        # At least one more signal required
        if not (is_dispatch_fn or has_type_param or any(kw in body for kw in ("get_class(", "gettype("))):
            return None

        evidences: list[Evidence] = []

        if has_match_expr:
            evidences.append(self.evidence(
                description=f"Uses PHP 8.0+ `match()` expression with {match_arm_count} dispatch branches — idiomatic type-based multimethod dispatch",
                weight=min(0.60, 0.30 + 0.05 * match_arm_count),
                location=fn.location,
                code_suffix="PHP8_MATCH_DISPATCH",
            ))
        elif has_switch:
            evidences.append(self.evidence(
                description=f"Uses `switch/case` with {match_arm_count} case branches dispatching by type/kind discriminator value",
                weight=min(0.45, 0.25 + 0.04 * match_arm_count),
                location=fn.location,
                code_suffix="SWITCH_TYPE_DISPATCH",
            ))

        if has_type_param:
            type_params = [
                p for p in params
                if any(kw in p.lower() for kw in ("type", "kind", "action", "event", "command"))
            ]
            evidences.append(self.evidence(
                description=f"Accepts type discriminator parameter(s): {', '.join(f'${p}' for p in type_params)}",
                weight=0.30,
                location=fn.location,
                code_suffix="TYPE_DISCRIMINATOR_PARAM",
            ))

        if any(kw in body for kw in ("get_class(", "gettype(")):
            evidences.append(self.evidence(
                description="Uses get_class() / gettype() for runtime type introspection — dynamic dispatch on object type",
                weight=0.35,
                location=fn.location,
                code_suffix="RUNTIME_TYPE_INTROSPECTION",
            ))

        return self.create_detection(
            target_name=fn.name,
            target_kind="match_dispatch_function",
            evidences=evidences,
            primary_location=fn.location,
            summary=f"Multimethod Dispatch: function '{fn.name}' implements PHP type-based polymorphic dispatch with {match_arm_count} interchangeable algorithm branches",
        )
