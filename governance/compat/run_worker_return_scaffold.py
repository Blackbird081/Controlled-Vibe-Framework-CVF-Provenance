#!/usr/bin/env python3
"""
Emit or create an L1 worker-return scaffold.

Safety boundary: this helper only prints a skeleton or creates one new markdown
file under docs/reviews/. It refuses overwrite and paths outside docs/reviews/.
It does not stage, commit, apply patches, run provider calls, or make a closure
decision.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
ALLOWED_DIR = "docs/reviews/"
SCAFFOLD_TODO = "TODO: worker fills this section before returning for review."
SCAFFOLD_TABLE_TODO = "TODO: fill before review"

WORKER_RETURN_SCAFFOLD_SECTIONS = (
    "Source Inventory",
    "Purpose",
    "Scope / Methodology",
    "Findings / Position",
    "Risk / Corrective Action",
    "Claim Boundary",
    "Gate Evidence",
    "Actual Changed Set",
    "Core Guard Self-Protection Authorization",
    "Corpus Completeness And Report Integrity",
    "Worker Experience Retrospective",
    "Agent Operation Trace Block",
    "Delta Execution Claim Boundary Control Block",
    "Public Export Disposition",
)


def _section_body(section: str) -> list[str]:
    if section == "Source Inventory":
        return ["| File | Action |", "|---|---|", f"| {SCAFFOLD_TABLE_TODO} | READ |"]
    if section == "Gate Evidence":
        return [
            "| Command | Result |",
            "|---|---|",
            "| `python governance/compat/run_worker_return_fast_gate.py` | TODO_PASS_FAIL_BLOCKED |",
            "",
            "receiptEvidence: CVF_RECEIPT_PRESENT - TODO_receipt_or_reason",
        ]
    if section == "Actual Changed Set":
        return [
            "- `TODO/path/to/changed-file.ext`",
            "",
            "List real paths; do not replace this with prose.",
        ]
    if section == "Core Guard Self-Protection Authorization":
        return [
            "Authorized guard-maintenance scope: TODO or N/A with reason",
            "",
            "Protected paths:",
            "- `TODO/protected/path.py`",
            "",
            "Operator authorization: TODO or N/A with reason",
            "",
            "Rollback boundary: TODO or N/A with reason",
        ]
    if section == "Corpus Completeness And Report Integrity":
        return [
            "- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus completeness claim in this worker return.",
        ]
    if section == "Worker Experience Retrospective":
        return [
            "WORKER_EXPERIENCE_RETRO_NA_WITH_REASON - TODO or replace with concise retrospective.",
        ]
    if section == "Agent Operation Trace Block":
        return [
            "| Field | Evidence |",
            "|---|---|",
            f"| Actor | {SCAFFOLD_TABLE_TODO} |",
            f"| Provider or surface | {SCAFFOLD_TABLE_TODO} |",
            f"| Session or invocation | {SCAFFOLD_TABLE_TODO} |",
            f"| Working directory | {SCAFFOLD_TABLE_TODO} |",
            f"| Command or tool surface | {SCAFFOLD_TABLE_TODO} |",
            f"| Target paths | {SCAFFOLD_TABLE_TODO} |",
            f"| Allowed scope source | {SCAFFOLD_TABLE_TODO} |",
            f"| Before status evidence | {SCAFFOLD_TABLE_TODO} |",
            f"| After status evidence | {SCAFFOLD_TABLE_TODO} |",
            f"| Diff evidence | {SCAFFOLD_TABLE_TODO} |",
            f"| Approval boundary | {SCAFFOLD_TABLE_TODO} |",
            f"| Claim boundary | {SCAFFOLD_TABLE_TODO} |",
            "| Agent type | worker |",
            f"| Invocation ID | {SCAFFOLD_TABLE_TODO} |",
            f"| Expected manifest | {SCAFFOLD_TABLE_TODO} |",
            f"| Actual changed set | {SCAFFOLD_TABLE_TODO} |",
            "| Manifest delta | TODO_MATCH_OR_EXPLAIN |",
            "| Deletion or rename disposition | N/A with reason: no deletion or rename in this scaffold |",
        ]
    if section == "Delta Execution Claim Boundary Control Block":
        return [
            "executionBaseHead: `TODO_EXECUTION_BASE_HEAD`",
            "",
            "receiptEvidence: CVF_RECEIPT_PRESENT - TODO_receipt_or_reason",
            "",
            "Runtime/provider/live/public-sync claims: N/A with reason unless explicitly authorized.",
        ]
    if section == "Public Export Disposition":
        return [
            "DEFERRED_PRIVATE_ONLY",
            "",
            "Reason: worker return in private provenance workspace; no public-sync authorization.",
        ]
    return [SCAFFOLD_TODO]


def build_scaffold(title: str = "") -> str:
    heading = title.strip() or "Worker Return Scaffold"
    lines = [
        f"# {heading}",
        "",
        "Memory class: FULL_RECORD",
        "",
        "docType: review",
        "",
        "Status: TODO_WORKER_STATUS",
        "",
        "dispatchWorkOrder: `TODO_WORK_ORDER_PATH`",
        "",
        "executionBaseHead: `TODO_EXECUTION_BASE_HEAD`",
        "",
        "NOTE: L1 scaffold only. Replace every TODO line before returning for review.",
        "",
    ]
    for section in WORKER_RETURN_SCAFFOLD_SECTIONS:
        lines.append(f"## {section}")
        lines.append("")
        lines.extend(_section_body(section))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _path_is_allowed(path: Path) -> bool:
    allowed_root = (REPO_ROOT / ALLOWED_DIR).resolve()
    try:
        resolved = path.resolve()
    except (OSError, RuntimeError):
        return False
    return resolved != allowed_root and allowed_root in resolved.parents


def write_scaffold(target: str, title: str = "") -> Path:
    candidate = Path(target)
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate
    if candidate.suffix.lower() != ".md":
        raise ValueError(f"target must be a .md file under {ALLOWED_DIR}: {target}")
    if not _path_is_allowed(candidate):
        raise ValueError(f"target must be inside {ALLOWED_DIR}: {target}")
    if candidate.exists():
        raise ValueError(f"refusing to overwrite existing file: {target}")
    candidate.parent.mkdir(parents=True, exist_ok=True)
    derived_title = title.strip() or candidate.stem.replace("_", " ")
    with open(candidate, "x", encoding="utf-8") as handle:
        handle.write(build_scaffold(derived_title))
    return candidate


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Emit or write a worker-return scaffold")
    parser.add_argument("--emit", action="store_true", help="Print scaffold to stdout")
    parser.add_argument("--write", metavar="PATH", help="Create one new scaffold file")
    parser.add_argument("--title", default="", help="Optional scaffold title")
    args = parser.parse_args(argv)
    if args.emit == bool(args.write):
        print("VIOLATION: choose exactly one of --emit or --write", file=sys.stderr)
        return 2
    if args.emit:
        print(build_scaffold(args.title), end="")
        return 0
    try:
        written = write_scaffold(args.write, args.title)
    except ValueError as exc:
        print(f"VIOLATION: {exc}", file=sys.stderr)
        return 2
    print(f"Wrote worker-return scaffold: {written}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
