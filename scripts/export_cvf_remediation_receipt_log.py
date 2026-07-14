#!/usr/bin/env python3
"""
Export a markdown evidence log from a file-backed CVF remediation receipt artifact.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PHASE_GOVERNANCE_ARCHIVE = REPO_ROOT / "docs" / "reviews" / "cvf_phase_governance" / "archive"
DEFAULT_INPUT = PHASE_GOVERNANCE_ARCHIVE / "CVF_W4_REMEDIATION_RECEIPTS_LOCAL_BASELINE_2026-03-07.json"
DEFAULT_OUTPUT = REPO_ROOT / "docs" / "reviews" / "cvf_phase_governance" / "CVF_W4_REMEDIATION_RECEIPT_LOG_2026-03-07.md"


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def build_log(input_path: Path) -> str:
    artifact = _read_json(input_path)
    receipts = artifact.get("receipts", [])
    action_counts = Counter(receipt["action"] for receipt in receipts)
    step_counts = Counter(receipt["step"] for receipt in receipts)
    proposal_ids = sorted({receipt["sourceProposalId"] for receipt in receipts})
    recorded_at_values = sorted(receipt["recordedAt"] for receipt in receipts)

    lines = [
        "# CVF W4 Remediation Receipt Log - 2026-03-07",
        "",
        "Memory class: FULL_RECORD",
        "",
        "docType: review",
        "",
        "Status: GENERATED",
        "",
        "## Purpose",
        "",
        "Render the current governance remediation receipts into a reviewable",
        "Markdown log for the W4 phase-governance evidence chain.",
        "",
        "## Target",
        "",
        f"- source artifact: `{_rel(input_path)}`",
        "",
        "## Scope",
        "",
        "This log covers exactly the receipts recorded in the source artifact",
        "above; it makes no claim about receipts outside that file.",
        "",
        "## Header",
        "",
        f"- schemaVersion: `{artifact.get('schemaVersion', 'UNKNOWN')}`",
        f"- adapter: `{artifact.get('adapter', 'UNKNOWN')}`",
        f"- receiptCount: `{artifact.get('receiptCount', len(receipts))}`",
        "",
        "## Action Summary",
        "",
    ]

    for action in sorted(action_counts):
        lines.append(f"- {action}: `{action_counts[action]}`")

    lines.extend(["", "## Step Summary", ""])
    for step in sorted(step_counts):
        lines.append(f"- {step}: `{step_counts[step]}`")

    lines.extend(
        [
            "",
            "## Proposal Scope",
            "",
            f"- proposalIds: `{', '.join(proposal_ids) if proposal_ids else 'none'}`",
            f"- firstRecordedAt: `{recorded_at_values[0] if recorded_at_values else 'UNKNOWN'}`",
            f"- lastRecordedAt: `{recorded_at_values[-1] if recorded_at_values else 'UNKNOWN'}`",
            "",
            "## Receipts",
            "",
            "| Receipt ID | Action | Proposal | Step | Recorded At |",
            "|---|---|---|---|---|",
        ]
    )

    for receipt in receipts:
        lines.append(
            f"| `{receipt['receiptId']}` | `{receipt['action']}` | `{receipt['sourceProposalId']}` | `{receipt['step']}` | `{receipt['recordedAt']}` |"
        )

    lines.extend(
        [
            "",
            "## Findings",
            "",
            f"This log reflects {len(receipts)} recorded receipt(s) at generation time.",
            "No manual finding is asserted beyond the tabulated receipt data above.",
            "",
            "## Risk",
            "",
            "No risk is asserted by this generated log; it is a deterministic",
            "rendering of the source artifact.",
            "",
            "## Decision",
            "",
            "N/A with reason: this is a generated evidence log, not a decision record.",
            "",
            "## Finding-To-Governance Learning Disposition",
            "",
            "| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |",
            "|---|---|---|---|---|---|",
            "| N/A with reason: this generated log states only tabulated receipt data with no asserted defect | RUNTIME_SIGNAL_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | none | N/A |",
            "",
            "EPISTEMIC_PROCESS_NA_WITH_REASON: this is a deterministic rendering of the named source artifact with no prediction, evidence comparison, or claim update",
            "",
            "## Checker Source Read-Ahead Block",
            "",
            "| Field | Value |",
            "|---|---|",
            "| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |",
            "| literalTokensReviewed | `Memory class`; `Status`; `## Purpose`; `## Target`; `## Claim Boundary`; `## Checker Source Read-Ahead Block` |",
            "| gateRunPurpose | confirmation evidence for a deterministically generated log; not first discovery |",
            "| claimBoundary | this log states only the receipts present in the source artifact at generation time |",
            "",
            "## Claim Boundary",
            "",
            "This log is a deterministic rendering of the named source artifact only.",
            "It makes no provider, production, public, scale, certification, or",
            "user-value claim.",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a markdown log from a CVF remediation receipt artifact.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="Input JSON artifact path")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output markdown path")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = (REPO_ROOT / input_path).resolve()

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = (REPO_ROOT / output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    content = build_log(input_path)
    output_path.write_text(content, encoding="utf-8")
    print(f"Exported remediation log: {_rel(output_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
