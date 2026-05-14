#!/usr/bin/env python3
"""Analyze CVF live governance latency/tax evidence.

Input is the JSONL emitted by scripts/run_evt2_live_latency_measurement.js.
The fitness thresholds intentionally match the EA governance-tax contract:
GREEN <10%, AMBER <20%, RED >=20% median governance tax.
"""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATH = REPO_ROOT / "docs" / "assessments" / "CVF_EVT2_LIVE_LATENCY_MEASUREMENT_2026-05-14.jsonl"


def percentile(values: list[float], pct: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, round((pct / 100) * (len(ordered) - 1))))
    return ordered[idx]


def fitness(median_tax_ratio: float | None) -> str:
    if median_tax_ratio is None:
        return "NO_DATA"
    if median_tax_ratio < 0.10:
        return "GREEN"
    if median_tax_ratio < 0.20:
        return "AMBER"
    return "RED"


def read_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            records.append(parsed)
    return records


def summarize(records: list[dict[str, Any]], path: Path) -> dict[str, Any]:
    successes = [r for r in records if r.get("success") is True]
    provider_ms = [float(r["providerExecutionMs"]) for r in successes if isinstance(r.get("providerExecutionMs"), (int, float))]
    total_ms = [float(r["totalMs"]) for r in successes if isinstance(r.get("totalMs"), (int, float))]
    overhead_ms = [
        max(0.0, float(r.get("governanceOverheadMs", 0)))
        for r in successes
        if isinstance(r.get("governanceOverheadMs"), (int, float))
    ]
    tax_ratios = [
        float(r["governanceTaxRatio"])
        for r in successes
        if isinstance(r.get("governanceTaxRatio"), (int, float))
    ]
    median_tax = statistics.median(tax_ratios) if tax_ratios else None

    by_decision: dict[str, int] = {}
    for record in records:
        decision = str(record.get("decision") or "UNKNOWN")
        by_decision[decision] = by_decision.get(decision, 0) + 1

    return {
        "path": str(path),
        "total_records": len(records),
        "successful_records": len(successes),
        "failed_records": len(records) - len(successes),
        "by_decision": by_decision,
        "median_total_ms": statistics.median(total_ms) if total_ms else None,
        "p95_total_ms": percentile(total_ms, 95),
        "median_provider_execution_ms": statistics.median(provider_ms) if provider_ms else None,
        "median_governance_overhead_ms": statistics.median(overhead_ms) if overhead_ms else None,
        "p95_governance_overhead_ms": percentile(overhead_ms, 95),
        "median_governance_tax_ratio": median_tax,
        "median_governance_tax_pct": round(median_tax * 100, 2) if median_tax is not None else None,
        "fitness": fitness(median_tax),
        "low_n_caveat": len(successes) < 20,
        "optimize_next": fitness(median_tax) in {"AMBER", "RED"},
    }


def render_markdown(summary: dict[str, Any]) -> str:
    def val(key: str) -> str:
        value = summary.get(key)
        if value is None:
            return "N/A"
        if isinstance(value, float):
            return f"{value:.2f}"
        return str(value)

    return "\n".join([
        "# CVF EVT-2 Live Governance Latency Measurement",
        "",
        f"**Evidence file:** `{summary['path']}`",
        f"**Fitness:** {summary['fitness']}",
        f"**Low-N caveat:** {summary['low_n_caveat']}",
        "",
        "| Metric | Value |",
        "| --- | --- |",
        f"| Total records | {val('total_records')} |",
        f"| Successful records | {val('successful_records')} |",
        f"| Failed records | {val('failed_records')} |",
        f"| Median total latency | {val('median_total_ms')}ms |",
        f"| P95 total latency | {val('p95_total_ms')}ms |",
        f"| Median provider execution | {val('median_provider_execution_ms')}ms |",
        f"| Median governance overhead | {val('median_governance_overhead_ms')}ms |",
        f"| P95 governance overhead | {val('p95_governance_overhead_ms')}ms |",
        f"| Median governance tax | {val('median_governance_tax_pct')}% |",
        "",
        "Fitness thresholds: GREEN <10%, AMBER <20%, RED >=20%.",
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze CVF EVT-2 governance latency evidence.")
    parser.add_argument("--path", default=str(DEFAULT_PATH), help="Path to EVT-2 JSONL evidence.")
    parser.add_argument("--json", action="store_true", help="Print JSON summary.")
    parser.add_argument("--write-md", help="Optional markdown output path.")
    args = parser.parse_args()

    path = Path(args.path)
    summary = summarize(read_records(path), path)

    if args.write_md:
        out = Path(args.write_md)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_markdown(summary) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print(render_markdown(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
