#!/usr/bin/env python3
"""
CVF Absorption Blind-Spot Control Presence Guard (ADIF-0014)

Scope-triggered presence checker: when a changed work order, GC-018 baseline,
or completion review touches an absorption source under
``.private_reference/legacy/`` or ``.private_reference/external_repos/``, the
artifact must carry both the Mandatory Blind-Spot Control Block heading and the
Corpus Completeness And Report Integrity section heading (or an allowed
``NOT_APPLICABLE_WITH_REASON`` / ``SKIPPED_WITH_REASON`` disposition), independent
of any completeness claim.

This closes ADIF-0014: the claim-triggered checkers stay silent when an artifact
simply omits both the claim and the control blocks.  This checker fires when a
changed governed artifact's *content* references an absorption source path
under ``.private_reference/legacy/`` or ``.private_reference/external_repos/``,
not on whether the artifact happens to claim completeness.  The absorption
source files themselves are gitignored and do not appear in the changed set;
the trigger must scan artifact content, not changed paths.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BASE_CANDIDATES = ("origin/main", "origin/master", "main", "master")

THIS_SCRIPT_PATH = "governance/compat/check_absorption_blindspot_control_presence.py"
ARCHIVE_MARKER = "/archive/"

BLIND_SPOT_HEADING = "## Mandatory Blind-Spot Control Block"
CORPUS_HEADING = "## Corpus Completeness And Report Integrity"

ALLOWED_DISPOSITION_PATTERNS = (
    re.compile(r"NOT_APPLICABLE_WITH_REASON", re.IGNORECASE),
    re.compile(r"SKIPPED_WITH_REASON", re.IGNORECASE),
)

ABSORPTION_SOURCE_PREFIXES = (
    ".private_reference/legacy/",
    ".private_reference/external_repos/",
)

GOVERNED_ARTIFACT_PREFIXES = (
    "docs/work_orders/",
    "docs/baselines/",
    "docs/reviews/",
)


def _run_git(args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def _ref_exists(ref: str) -> bool:
    code, _, _ = _run_git(["rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"])
    return code == 0


def _discover_default_base(head: str) -> tuple[str, str]:
    env_base = os.getenv("CVF_COMPAT_BASE")
    if env_base:
        return env_base, "env:CVF_COMPAT_BASE"
    for ref in DEFAULT_BASE_CANDIDATES:
        if not _ref_exists(ref):
            continue
        code, out, _ = _run_git(["merge-base", ref, head])
        if code == 0 and out:
            return out, f"merge-base({ref},{head})"
    return "HEAD~1", "fallback:HEAD~1"


def _resolve_range(base: str | None, head: str | None) -> tuple[str, str, str]:
    resolved_head = head or "HEAD"
    if base:
        return base, resolved_head, "explicit:--base"
    resolved_base, source = _discover_default_base(resolved_head)
    return resolved_base, resolved_head, source


def _parse_name_status_output(output: str) -> dict[str, set[str]]:
    changed: dict[str, set[str]] = {}
    for raw_line in output.splitlines():
        if not raw_line.strip():
            continue
        parts = raw_line.split("\t")
        status = parts[0].strip()
        if status.startswith(("R", "C")):
            if len(parts) < 3:
                continue
            path = parts[2]
        else:
            if len(parts) < 2:
                continue
            path = parts[1]
        normalized = path.replace("\\", "/").strip()
        changed.setdefault(normalized, set()).add(status)
    return changed


def _get_changed_name_status(base: str, head: str) -> dict[str, set[str]]:
    code, out, err = _run_git(["diff", "--name-status", f"{base}..{head}"])
    if code != 0:
        raise RuntimeError(f"git diff failed for range {base}..{head}: {err or out}")
    return _parse_name_status_output(out)


def _get_worktree_name_status() -> dict[str, set[str]]:
    changed: dict[str, set[str]] = {}
    for args in (["diff", "--name-status"], ["diff", "--name-status", "--cached"]):
        code, out, _ = _run_git(args)
        if code == 0 and out:
            for path, statuses in _parse_name_status_output(out).items():
                changed.setdefault(path, set()).update(statuses)
    code, out, _ = _run_git(["ls-files", "--others", "--exclude-standard"])
    if code == 0 and out:
        for raw_line in out.splitlines():
            normalized = raw_line.replace("\\", "/").strip()
            if normalized:
                changed.setdefault(normalized, set()).add("A")
    return changed


def _merge_changed_maps(*maps: dict[str, set[str]]) -> dict[str, list[str]]:
    merged: dict[str, set[str]] = {}
    for item in maps:
        for path, statuses in item.items():
            merged.setdefault(path, set()).update(statuses)
    return {path: sorted(statuses) for path, statuses in sorted(merged.items())}


def _read_rel(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8", errors="replace")


def _artifact_references_absorption_source(path: str) -> bool:
    """Return True if the governed artifact's content references an
    absorption source path under ``.private_reference/legacy/`` or
    ``.private_reference/external_repos/``.

    The absorption source files are gitignored and do not appear in the
    changed set; the trigger must scan artifact content, not changed paths.
    """
    try:
        text = _read_rel(path)
    except OSError:
        return False
    return any(prefix in text for prefix in ABSORPTION_SOURCE_PREFIXES)


def _is_governed_artifact(path: str) -> bool:
    normalized = path.replace("\\", "/")
    if ARCHIVE_MARKER in normalized:
        return False
    if not normalized.endswith(".md"):
        return False
    return any(normalized.startswith(prefix) for prefix in GOVERNED_ARTIFACT_PREFIXES)


def _has_allowed_disposition(text: str, heading: str) -> bool:
    section = _extract_section(text, heading)
    if not section:
        return False
    return any(pattern.search(section) for pattern in ALLOWED_DISPOSITION_PATTERNS)


def _extract_section(text: str, header: str) -> str:
    marker = f"{header}\n"
    start = text.find(marker)
    if start == -1:
        return ""
    section_start = start + len(marker)
    next_header = text.find("\n## ", section_start)
    if next_header == -1:
        return text[section_start:]
    return text[section_start:next_header]


def _check_artifact(path: str) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    try:
        text = _read_rel(path)
    except OSError:
        violations.append({
            "path": path,
            "type": "UNREADABLE",
            "message": f"absorption source artifact `{path}` is unreadable",
        })
        return violations

    has_blind_spot = BLIND_SPOT_HEADING in text
    has_corpus = CORPUS_HEADING in text

    if has_blind_spot and has_corpus:
        return violations

    if not has_blind_spot and _has_allowed_disposition(text, BLIND_SPOT_HEADING):
        pass
    elif not has_blind_spot:
        violations.append({
            "path": path,
            "type": "MISSING_BLIND_SPOT_CONTROL_BLOCK",
            "message": (
                f"absorption source artifact `{path}` touches a legacy/external "
                "source path but does not carry the `## Mandatory Blind-Spot "
                "Control Block` heading or an allowed NOT_APPLICABLE_WITH_REASON / "
                "SKIPPED_WITH_REASON disposition"
            ),
        })

    if not has_corpus and _has_allowed_disposition(text, CORPUS_HEADING):
        pass
    elif not has_corpus:
        violations.append({
            "path": path,
            "type": "MISSING_CORPUS_COMPLETENESS_BLOCK",
            "message": (
                f"absorption source artifact `{path}` touches a legacy/external "
                "source path but does not carry the `## Corpus Completeness And "
                "Report Integrity` heading or an allowed "
                "NOT_APPLICABLE_WITH_REASON / SKIPPED_WITH_REASON disposition"
            ),
        })

    return violations


def run_check(base: str | None = None, head: str | None = None) -> list[dict[str, str]]:
    resolved_base, resolved_head, base_source = _resolve_range(base, head)

    try:
        committed = _get_changed_name_status(resolved_base, resolved_head)
    except RuntimeError:
        committed = {}
    worktree = _get_worktree_name_status()
    merged = _merge_changed_maps(committed, worktree)
    all_changed = sorted(merged.keys())

    violations: list[dict[str, str]] = []
    for path in all_changed:
        if not _is_governed_artifact(path):
            continue
        if not _artifact_references_absorption_source(path):
            continue
        violations.extend(_check_artifact(path))

    return violations


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CVF Absorption Blind-Spot Control Presence Guard (ADIF-0014)",
    )
    parser.add_argument("--base", default=None, help="Base commit/ref for range-aware checking.")
    parser.add_argument("--head", default=None, help="Head commit/ref for range-aware checking.")
    parser.add_argument("--enforce", action="store_true", help="Exit nonzero on violations.")
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    args = parser.parse_args()

    resolved_base, resolved_head, base_source = _resolve_range(args.base, args.head)

    print("=== CVF Absorption Blind-Spot Control Presence Guard ===")
    print(f"Range: {resolved_base}..{resolved_head}")
    print(f"Base source: {base_source}")

    try:
        committed = _get_changed_name_status(resolved_base, resolved_head)
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1

    worktree = _get_worktree_name_status()
    merged = _merge_changed_maps(committed, worktree)
    all_changed = sorted(merged.keys())

    governed_artifacts = [p for p in all_changed if _is_governed_artifact(p)]
    triggered_artifacts = [
        p for p in governed_artifacts if _artifact_references_absorption_source(p)
    ]

    if not triggered_artifacts:
        print("No governed artifacts reference absorption source paths; checker is silent.")
        if args.json:
            print(json.dumps({"violations": [], "scopeTriggered": False}, indent=2))
        print("COMPLIANT")
        return 0

    print(f"Absorption source references detected in {len(triggered_artifacts)} governed artifact(s); checking control blocks.")

    violations: list[dict[str, str]] = []
    for path in triggered_artifacts:
        violations.extend(_check_artifact(path))

    if args.json:
        print(json.dumps({"violations": violations, "scopeTriggered": True}, indent=2))

    if violations:
        print(f"\nViolations: {len(violations)}")
        for v in violations:
            print(f"  - {v['path']}: {v['message']}")
        if args.enforce:
            return 1
        print("\nVIOLATION - absorption blind-spot control presence check failed.")
        return 1

    print("COMPLIANT - all in-scope governed artifacts carry required control blocks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
