#!/usr/bin/env python3
"""CLI readout for the CVF Skill Control Plane inventory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

HELPER_DIR = Path(__file__).resolve().parent
if str(HELPER_DIR) not in sys.path:
    sys.path.insert(0, str(HELPER_DIR))

from generate_skill_control_plane_inventory import build_inventory  # noqa: E402


def _matching_records(inventory: dict[str, Any], skill_id: str | None) -> list[dict[str, Any]]:
    records = [record for record in inventory.get("records", []) if isinstance(record, dict)]
    if skill_id is None:
        return records
    return [record for record in records if record.get("skillId") == skill_id]


def _human_summary(inventory: dict[str, Any], records: list[dict[str, Any]]) -> str:
    lines = ["CVF Skill Control Plane inventory"]
    summary = inventory.get("summary", {})
    if isinstance(summary, dict):
        lines.extend(
            [
                f"ASSF registry entries: {summary.get('assfRegistryEntries', 0)}",
                f"Package roots: {summary.get('packageRoots', 0)}",
                f"Runtime eligible packages: {summary.get('runtimeEligiblePackages', 0)}",
                f"Activation-ready packages: {summary.get('activeResolverReadyPackages', 0)}",
                f"CLI/MCP adapter packages: {summary.get('cliMcpAdapterPackages', 0)}",
                f"Web projection items: {summary.get('webProjectionItems', 0)}",
                f"Cross-surface drift violations: {summary.get('crossSurfaceDriftViolationCount', 0)}",
            ]
        )
    lines.append(f"Returned records: {len(records)}")
    for record in records:
        registry = record.get("registry", {})
        runtime = record.get("runtime", {})
        activation = record.get("activation", {})
        web = record.get("webProjection", {})
        drift = record.get("drift", {})
        lines.append(
            "- "
            f"{record.get('skillId')} | "
            f"taxonomy={','.join(record.get('taxonomy', []))} | "
            f"status={registry.get('status')} | "
            f"cert={registry.get('certificationState')} | "
            f"runtimeEligible={str(runtime.get('eligible')).lower()} | "
            f"activation={activation.get('decision')} | "
            f"web={web.get('assfProjectionClass') if web.get('present') else 'none'} | "
            f"drift={','.join(drift.get('violations', [])) or 'none'}"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Read the generated-source Skill Control Plane inventory surfaces "
            "and answer where a skill sits in the lifecycle."
        )
    )
    parser.add_argument("--skill-id", default=None)
    parser.add_argument("--summary-only", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    try:
        inventory = build_inventory()
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    records = [] if args.summary_only else _matching_records(inventory, args.skill_id)
    if args.json:
        payload = dict(inventory)
        if args.summary_only or args.skill_id is not None:
            payload["records"] = records
        print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(_human_summary(inventory, records))
    return 0


if __name__ == "__main__":
    sys.exit(main())
