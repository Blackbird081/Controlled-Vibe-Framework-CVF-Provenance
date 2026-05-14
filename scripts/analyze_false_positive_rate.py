#!/usr/bin/env python3
"""Analyze CVF false-positive reports from append-only JSONL evidence."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATHS = [
    Path.cwd() / ".data" / "false-positive-events.jsonl",
    REPO_ROOT
    / "EXTENSIONS"
    / "CVF_v1.6_AGENT_PLATFORM"
    / "cvf-web"
    / ".data"
    / "false-positive-events.jsonl",
]


def resolve_default_path() -> Path:
    env_path = os.environ.get("CVF_FALSE_POSITIVE_REPORTS_PATH")
    if env_path:
        return Path(env_path).expanduser().resolve()

    for candidate in DEFAULT_PATHS:
        if candidate.exists():
            return candidate

    return DEFAULT_PATHS[-1]


def iter_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []

    records: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        try:
            parsed = json.loads(stripped)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            records.append(parsed)
    return records


def analyze(records: list[dict[str, Any]]) -> dict[str, Any]:
    observed: dict[str, dict[str, Any]] = {}
    reported: dict[str, dict[str, Any]] = {}

    for record in records:
        receipt_id = str(record.get("receiptId") or "").strip()
        decision = record.get("decision")
        if not receipt_id or decision not in {"BLOCK", "CLARIFY"}:
            continue

        event_type = record.get("eventType")
        if event_type == "REPORTABLE_DECISION_OBSERVED":
            observed[receipt_id] = record
        elif event_type == "FALSE_POSITIVE_REPORTED":
            reported[receipt_id] = record

    # If older evidence contains reports but not observation events, include those
    # reports in the denominator and mark the rate as report-only.
    denominator_ids = set(observed) | set(reported)
    numerator_ids = set(reported)
    denominator = len(denominator_ids)
    numerator = len(numerator_ids)
    rate = (numerator / denominator) if denominator else 0.0

    by_decision: dict[str, dict[str, int]] = {}
    for receipt_id in denominator_ids:
        record = observed.get(receipt_id) or reported.get(receipt_id) or {}
        decision = str(record.get("decision") or "unknown")
        bucket = by_decision.setdefault(decision, {"observed": 0, "reported": 0})
        bucket["observed"] += 1
        if receipt_id in reported:
            bucket["reported"] += 1

    return {
        "observed_reportable_decisions": denominator,
        "false_positive_reports": numerator,
        "false_positive_rate": rate,
        "false_positive_rate_pct": round(rate * 100, 2),
        "by_decision": by_decision,
        "low_n_caveat": denominator < 20,
        "evidence_mode": "observed_and_reported" if observed else "reported_only",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        type=Path,
        default=resolve_default_path(),
        help="Path to false-positive-events.jsonl",
    )
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    path = args.path.expanduser().resolve()
    result = analyze(iter_jsonl(path))
    result["path"] = str(path)

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"False-positive evidence: {path}")
        print(f"Observed BLOCK/CLARIFY decisions: {result['observed_reportable_decisions']}")
        print(f"False-positive reports: {result['false_positive_reports']}")
        print(f"False-positive rate: {result['false_positive_rate_pct']}%")
        print(f"Evidence mode: {result['evidence_mode']}")
        if result["low_n_caveat"]:
            print("Caveat: low sample size (N < 20); do not use for rollout claims.")
        print("By decision:")
        for decision, bucket in sorted(result["by_decision"].items()):
            print(f"  - {decision}: {bucket['reported']} / {bucket['observed']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
