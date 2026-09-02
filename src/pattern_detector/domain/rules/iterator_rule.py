"""Iterator Pattern Detection Rule."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BasePatternRule
from pattern_detector.domain.value_objects import PatternType


class IteratorPatternRule(BasePatternRule):
    """Detects Iterator / Lazy Sequence Generator pattern instances in Clojure.

    Indicators:
    - Functions building lazy stream iterators using `lazy-seq` and recursion.
    - Protocols defining `next`, `has-next?`, `current`, or `iterate`.
    - Extensions to `clojure.lang.Seqable` or `java.lang.Iterable`.
    """

    @property
    def pattern_type(self) -> PatternType:
        return PatternType.ITERATOR

    def detect(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []

        # 1. Custom Iterator Protocols / Interfaces
        for proto in model.all_protocols():
            if proto.name.endswith("Rule") or proto.name.endswith("Test"):
                continue
            methods_lower = [m.name.split(".")[-1].lower() for m in proto.methods]
            has_iteration_mechanics = (
                ("current" in methods_lower and "next" in methods_lower)
                or ("next" in methods_lower and any(k in methods_lower for k in ("has_next", "hasnext", "valid", "rewind")))
                or ("current_item" in methods_lower and any(k in methods_lower for k in ("next", "is_done")))
                or ("iterator" in proto.name.lower() and any(m in ("next", "has_next", "hasnext", "current") for m in methods_lower))
                or ("iterable" in proto.name.lower() and any(m in ("getiterator", "iterator") for m in methods_lower))
            )
            if has_iteration_mechanics:
                evidences = [
                    self.evidence(
                        description=f"Protocol '{proto.name}' defines iterator traversal methods: {', '.join(m.name for m in proto.methods)}",
                        weight=0.65,
                        location=proto.location,
                        code_suffix="ITERATOR_PROTOCOL",
                    ),
                ]
                detections.append(
                    self.create_detection(
                        target_name=proto.name,
                        target_kind="iterator_protocol",
                        evidences=evidences,
                        primary_location=proto.location,
                        related_locations=[],
                        summary=f"Iterator pattern: protocol '{proto.name}' defines sequential iteration contract",
                        base_score=0.30,
                    )
                )

        return detections
