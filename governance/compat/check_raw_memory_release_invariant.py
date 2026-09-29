#!/usr/bin/env python3
"""
CVF Raw Memory Release Invariant Gate

FPC-T3-C06 guard for changed governed Markdown that discusses memory-write,
raw-memory, reinjection, retrieval-facing, or promotion surfaces.

The gate requires the artifact to carry an explicit rawMemoryReleased=false
assertion. It is a static documentation/source-fidelity guard only; it does
not inspect runtime behavior, providers, routes, MCP tools, or durable stores.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BASE_CANDIDATES = ("origin/main", "origin/master", "main", "master")

APPLICABLE_PREFIXES: tuple[str, ...] = (
    "docs/baselines/",
    "docs/work_orders/",
    "docs/reviews/",
    "docs/reference/",
)

ARCHIVE_MARKER = "/archive/"

MEMORY_SURFACE_PATTERN = re.compile(
    r"\b("
    r"memory[-\s]write|memory\s+writes?|memory\s+event|memory\s+consolidation|"
    r"durable\s+memory|memory\s+retrieval|retrieval[-\s]facing|"
    r"learning\s+promotion|promotionEligible|raw[-\s]memory|"
    r"canReinject|memory\s+reinjection|reinjection|memory\s+readout|"
    r"MemoryRetrievalPackInput|ConsolidatedMemoryRecord|OperatorMemoryReviewPacket"
    r")\b",
    re.IGNORECASE,
)

RAW_RELEASE_FALSE_PATTERN = re.compile(r"\brawMemoryReleased\s*[:=]\s*false\b")


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


def _is_applicable(path: str) -> bool:
    normalized = path.replace("\\", "/")
    if not normalized.endswith(".md"):
        return False
    if ARCHIVE_MARKER in normalized:
        return False
    return any(normalized.startswith(prefix) for prefix in APPLICABLE_PREFIXES)


def _line_number_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def diagnose_raw_memory_release_invariant(path: str, text: str) -> list[dict[str, str]]:
    if not _is_applicable(path):
        return []
    surface_match = MEMORY_SURFACE_PATTERN.search(text)
    if surface_match is None:
        return []
    if RAW_RELEASE_FALSE_PATTERN.search(text):
        return []
    lineno = _line_number_for_offset(text, surface_match.start())
    return [
        {
            "path": path,
            "line": str(lineno),
            "type": "raw_memory_release_false_missing",
            "matchedSurface": surface_match.group(0),
            "message": (
                f"{path}:{lineno}: memory/raw-memory/reinjection/retrieval-facing "
                "claim surface requires explicit rawMemoryReleased=false assertion"
            ),
        }
    ]


def _classify(changed_paths: dict[str, list[str]]) -> dict[str, Any]:
    scoped_paths = [
        path
        for path, statuses in sorted(changed_paths.items())
        if _is_applicable(path) and not all(status.startswith("D") for status in statuses)
    ]
    violations: list[dict[str, str]] = []
    for path in scoped_paths:
        full = REPO_ROOT / path
        if not full.exists() or full.is_dir():
            continue
        violations.extend(diagnose_raw_memory_release_invariant(path, _read_rel(path)))
    return {
        "checkedPaths": scoped_paths,
        "changedPaths": changed_paths,
        "violations": violations,
        "violationCount": len(violations),
        "compliant": not violations,
    }


def _print_report(report: dict[str, Any], base: str, head: str, range_source: str) -> None:
    print("=== CVF Raw Memory Release Invariant Gate ===")
    print(f"Range: {base}..{head} ({range_source})")
    print(f"Changed paths: {len(report['changedPaths'])}")
    print(f"Checked governed Markdown paths: {len(report['checkedPaths'])}")
    print(f"Violations: {len(report['violations'])}")
    if report["violations"]:
        print("\nViolations:")
        for item in report["violations"]:
            print(f"  - {item['message']}")
    if report["compliant"]:
        print("\nCOMPLIANT - Raw memory release invariant assertions are present.")
    else:
        print("\nVIOLATION - Memory-facing artifacts must state rawMemoryReleased=false.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate rawMemoryReleased=false assertions on memory-facing governed Markdown"
    )
    parser.add_argument("--base", default=None, help="Optional git base ref")
    parser.add_argument("--head", default=None, help="Optional git head ref")
    parser.add_argument("--enforce", action="store_true",
                        help="Return non-zero when violations exist")
    parser.add_argument("--json", action="store_true", help="Print JSON report")
    args = parser.parse_args()

    try:
        base, head, range_source = _resolve_range(args.base, args.head)
        changed_paths = _merge_changed_maps(
            _get_changed_name_status(base, head),
            _get_worktree_name_status(),
        )
        report = _classify(changed_paths)
    except RuntimeError as exc:
        print(str(exc))
        return 1

    report["timestamp"] = (
        dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    )
    report["range"] = {"base": base, "head": head, "source": range_source}
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        _print_report(report, base, head, range_source)
    if args.enforce and not report["compliant"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
