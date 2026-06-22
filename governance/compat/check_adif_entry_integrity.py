"""Standalone, read-only ADIF entry-integrity machine guard (ADIF-T5).

Detects entry-integrity drift across the committed ADIF entries:

- dangling `checkerBindings` paths;
- dangling `supersedes` references;
- duplicate `defectId` values;
- stale supersession (an active entry superseded by another active
  entry, or a supersession cycle);
- invalid `severity` / `lifecycleState` / `enforcementLevel` enum values;
- dishonest enforcement claims (`MACHINE_CHECKED` or `PARTIAL_CHECK` whose
  `checkerBindings` path does not exist).

This guard never repairs a violation it finds and is not wired into any
autorun phase or hook chain. It reports a violations list only.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path

_RESOLVER_PATH = Path(__file__).resolve().with_name("run_adif_defect_resolver.py")
_RESOLVER_SPEC = importlib.util.spec_from_file_location("run_adif_defect_resolver", _RESOLVER_PATH)
assert _RESOLVER_SPEC and _RESOLVER_SPEC.loader
resolver = importlib.util.module_from_spec(_RESOLVER_SPEC)
sys.modules[_RESOLVER_SPEC.name] = resolver
_RESOLVER_SPEC.loader.exec_module(resolver)

REPO_ROOT = Path(__file__).resolve().parents[2]

_VALID_SEVERITY = frozenset({"LOW", "MEDIUM", "HIGH"})
_VALID_LIFECYCLE_STATE = frozenset({"PROPOSED", "ACTIVE", "SUPERSEDED", "RETIRED", "REJECTED"})
_VALID_ENFORCEMENT_LEVEL = frozenset({"GUIDANCE_ONLY", "PARTIAL_CHECK", "MACHINE_CHECKED", "RETIRED"})
_ENFORCEMENT_LEVELS_REQUIRING_CHECKER = frozenset({"MACHINE_CHECKED", "PARTIAL_CHECK"})


@dataclass(frozen=True)
class IntegrityViolation:
    """One detected entry-integrity violation. Read-only report row."""

    defect_id: str
    violation_class: str
    detail: str


def _checker_binding_paths(checker_bindings: str) -> tuple[str, ...]:
    if not checker_bindings or checker_bindings.upper().startswith("NOT_APPLICABLE"):
        return ()
    candidates = []
    for token in checker_bindings.replace(",", " ").split():
        cleaned = token.strip("()")
        if cleaned.startswith("governance/compat/") and cleaned.endswith(".py"):
            candidates.append(cleaned)
    return tuple(candidates)


def _check_dangling_checker_bindings(entry, violations: list[IntegrityViolation]) -> None:
    for path in _checker_binding_paths(entry.checker_bindings):
        if not (REPO_ROOT / path).exists():
            violations.append(
                IntegrityViolation(
                    defect_id=entry.defect_id,
                    violation_class="DANGLING_CHECKER_BINDING",
                    detail=f"checkerBindings path does not exist: {path}",
                )
            )


def _check_dishonest_enforcement_claim(entry, violations: list[IntegrityViolation]) -> None:
    level = entry.enforcement_level.upper()
    if level not in _ENFORCEMENT_LEVELS_REQUIRING_CHECKER:
        return
    paths = _checker_binding_paths(entry.checker_bindings)
    if not paths:
        violations.append(
            IntegrityViolation(
                defect_id=entry.defect_id,
                violation_class="DISHONEST_ENFORCEMENT_CLAIM",
                detail=f"enforcementLevel={level} declared with no resolvable checkerBindings path",
            )
        )
        return
    if not any((REPO_ROOT / path).exists() for path in paths):
        violations.append(
            IntegrityViolation(
                defect_id=entry.defect_id,
                violation_class="DISHONEST_ENFORCEMENT_CLAIM",
                detail=f"enforcementLevel={level} declared but no checkerBindings path exists: {paths}",
            )
        )


def _check_invalid_enum_values(entry, violations: list[IntegrityViolation]) -> None:
    if entry.severity.upper() not in _VALID_SEVERITY:
        violations.append(
            IntegrityViolation(
                defect_id=entry.defect_id,
                violation_class="INVALID_ENUM_VALUE",
                detail=f"severity={entry.severity!r} is not one of {sorted(_VALID_SEVERITY)}",
            )
        )
    if entry.lifecycle_state.upper() not in _VALID_LIFECYCLE_STATE:
        violations.append(
            IntegrityViolation(
                defect_id=entry.defect_id,
                violation_class="INVALID_ENUM_VALUE",
                detail=f"lifecycleState={entry.lifecycle_state!r} is not one of {sorted(_VALID_LIFECYCLE_STATE)}",
            )
        )
    if entry.enforcement_level.upper() not in _VALID_ENFORCEMENT_LEVEL:
        violations.append(
            IntegrityViolation(
                defect_id=entry.defect_id,
                violation_class="INVALID_ENUM_VALUE",
                detail=f"enforcementLevel={entry.enforcement_level!r} is not one of {sorted(_VALID_ENFORCEMENT_LEVEL)}",
            )
        )


def _check_duplicate_defect_ids(entries: tuple, violations: list[IntegrityViolation]) -> None:
    seen: dict[str, int] = {}
    for entry in entries:
        seen[entry.defect_id] = seen.get(entry.defect_id, 0) + 1
    for defect_id, count in seen.items():
        if count > 1:
            violations.append(
                IntegrityViolation(
                    defect_id=defect_id,
                    violation_class="DUPLICATE_DEFECT_ID",
                    detail=f"defectId {defect_id} appears {count} times across committed entries",
                )
            )


def _check_dangling_and_stale_supersession(entries: tuple, violations: list[IntegrityViolation]) -> None:
    by_id = {entry.defect_id: entry for entry in entries}
    for entry in entries:
        if not entry.supersedes or entry.supersedes.upper() == "NONE":
            continue
        target = by_id.get(entry.supersedes)
        if target is None:
            violations.append(
                IntegrityViolation(
                    defect_id=entry.defect_id,
                    violation_class="DANGLING_SUPERSESSION",
                    detail=f"supersedes references unknown defectId {entry.supersedes}",
                )
            )
            continue
        if target.lifecycle_state.upper() == "ACTIVE" and entry.lifecycle_state.upper() == "ACTIVE":
            violations.append(
                IntegrityViolation(
                    defect_id=entry.defect_id,
                    violation_class="STALE_SUPERSESSION",
                    detail=(
                        f"entry is ACTIVE and supersedes ACTIVE entry {entry.supersedes}; "
                        "the superseded entry should be SUPERSEDED, not ACTIVE"
                    ),
                )
            )
        if target.supersedes == entry.defect_id:
            violations.append(
                IntegrityViolation(
                    defect_id=entry.defect_id,
                    violation_class="STALE_SUPERSESSION",
                    detail=f"supersession cycle detected between {entry.defect_id} and {entry.supersedes}",
                )
            )


def check_entry_integrity(entries: tuple | None = None) -> tuple[IntegrityViolation, ...]:
    """Read-only integrity scan over the committed (or caller-supplied) entries."""
    candidates = entries if entries is not None else resolver.load_entries()
    violations: list[IntegrityViolation] = []
    _check_duplicate_defect_ids(candidates, violations)
    _check_dangling_and_stale_supersession(candidates, violations)
    for entry in candidates:
        _check_dangling_checker_bindings(entry, violations)
        _check_dishonest_enforcement_claim(entry, violations)
        _check_invalid_enum_values(entry, violations)
    return tuple(violations)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="ADIF entry-integrity guard (read-only)")
    parser.add_argument("--enforce", action="store_true", help="exit non-zero if any violation is found")
    args = parser.parse_args(argv)

    violations = check_entry_integrity()
    print("=== CVF ADIF Entry Integrity Guard ===")
    print(f"Entries checked: {len(resolver.load_entries())}")
    print(f"Violations: {len(violations)}")
    for violation in violations:
        print(f"  - {violation.defect_id} [{violation.violation_class}] {violation.detail}")

    if violations and args.enforce:
        print("\nVIOLATION - repair the listed entries before claiming entry integrity.")
        return 1
    print("\nCOMPLIANT - no entry-integrity violations detected." if not violations else "\nReport-only run; --enforce not set.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
