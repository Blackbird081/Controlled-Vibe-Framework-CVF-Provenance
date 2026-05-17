#!/usr/bin/env python3
"""
CVF Anti-Collusion Evidence Trace Advisory Gate (Phase 0.B)

Reports review packets under docs/reviews/ and .private_reference/ that are
missing Evidence Trace Blocks as required by GC-046. This checker is advisory
only (always exits 0). It will remain advisory until Phase 0.C hard-fail is
authorized (requires 3 review packets using the protocol as worked examples).

GC-046: governance/toolkit/05_OPERATION/CVF_AGENT_REVIEW_ANTI_COLLUSION_GUARD.md
Phase 0.B gate: at least 3 review packets using GC-046 protocol before hard-fail.
Phase 0.C: pre-commit hard-fail — requires separate GC-018 + Phase 0.B evidence.

Evidence Trace Block markers (any one of these in a review packet satisfies the
check for that packet):
  - "Evidence Trace Block"
  - "Evidence Trace:"
  - "exact command" (inline trace without the block header)

Review packet scope: files whose names match the pattern
  *REVIEW* | *REBUTTAL* | *RESPONSE* | *VERDICT* | *ABSORPTION*
  in docs/reviews/ or .private_reference/
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

# Directories to scan for review packets
SCAN_DIRS = [
    REPO_ROOT / "docs" / "reviews",
    REPO_ROOT / ".private_reference",
]

# Name fragments that identify a file as a review/rebuttal/response packet
REVIEW_NAME_FRAGMENTS = (
    "REVIEW",
    "REBUTTAL",
    "RESPONSE",
    "VERDICT",
    "ABSORPTION",
    "CONVERGENCE",
)

# Any of these strings in file content satisfies the Evidence Trace requirement
EVIDENCE_TRACE_MARKERS = (
    "Evidence Trace Block",
    "Evidence Trace:",
    "exact command",
    "exact query",
)

# Phase 0.B acceptance gate: this many compliant packets required before
# Phase 0.C hard-fail is authorized.
PHASE_0B_THRESHOLD = 3


def _is_review_packet(path: Path) -> bool:
    name = path.name.upper()
    return path.suffix.lower() == ".md" and any(frag in name for frag in REVIEW_NAME_FRAGMENTS)


def _has_evidence_trace(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return any(marker in text for marker in EVIDENCE_TRACE_MARKERS)


def _scan() -> tuple[list[Path], list[Path]]:
    """Return (compliant_packets, missing_trace_packets)."""
    compliant: list[Path] = []
    missing: list[Path] = []

    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue
        for path in sorted(scan_dir.rglob("*.md")):
            if not _is_review_packet(path):
                continue
            if _has_evidence_trace(path):
                compliant.append(path)
            else:
                missing.append(path)

    return compliant, missing


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CVF Anti-Collusion Evidence Trace Advisory Gate (Phase 0.B)"
    )
    parser.add_argument(
        "--enforce",
        action="store_true",
        help="Reserved for Phase 0.C hard-fail (currently ignored — always advisory)",
    )
    args = parser.parse_args()

    print("=== CVF Anti-Collusion Evidence Trace Advisory (GC-046 Phase 0.B) ===")
    print(f"Scope: {', '.join(str(d) for d in SCAN_DIRS if d.exists())}")

    compliant, missing = _scan()
    total = len(compliant) + len(missing)

    print(f"Review packets found: {total}")
    print(f"  Compliant (Evidence Trace present): {len(compliant)}")
    print(f"  Missing Evidence Trace:             {len(missing)}")
    print(f"Phase 0.B threshold (compliant needed before hard-fail): {PHASE_0B_THRESHOLD}")

    if compliant:
        print("\nCompliant packets:")
        for p in compliant:
            print(f"  + {p.relative_to(REPO_ROOT)}")

    if missing:
        print("\nAdvisory — missing Evidence Trace Block (GC-046 Rule 1):")
        for p in missing:
            print(f"  ! {p.relative_to(REPO_ROOT)}")
        print(
            "\nAction: add an Evidence Trace Block to each flagged packet before it is"
            " cited as convergence evidence. See GC-046 for the required format."
        )
    else:
        print("\nAll detected review packets contain an Evidence Trace Block.")

    # Phase 0.B gate status
    if len(compliant) >= PHASE_0B_THRESHOLD:
        print(
            f"\nPhase 0.B threshold met ({len(compliant)} >= {PHASE_0B_THRESHOLD})."
            " Phase 0.C hard-fail may be proposed with a fresh GC-018."
        )
    else:
        remaining = PHASE_0B_THRESHOLD - len(compliant)
        print(
            f"\nPhase 0.B threshold NOT yet met ({len(compliant)}/{PHASE_0B_THRESHOLD})."
            f" {remaining} more compliant packet(s) needed before Phase 0.C is authorized."
        )

    # Always advisory — exit 0 regardless of findings.
    # Phase 0.C hard-fail requires a separate GC-018 after Phase 0.B threshold is met.
    print("\nADVISORY ONLY — this check never blocks a commit (Phase 0.B).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
