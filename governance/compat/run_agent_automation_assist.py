#!/usr/bin/env python3
"""
CVF Agent Automation Assist (AAF-T1).

A deterministic, read-only helper that reduces CVF workflow latency for noncoder
operators and external agents connected through CLI/MCP. It classifies the
current changed batch, recommends the correct commit-steward lane, lists missing
Worker Return Packet Shape Contract blocks for changed WORKER_MUST_NOT_COMMIT
work orders, and prints the exact next command.

This helper is read-only by design. It never writes, stages, commits, pushes,
deletes, moves, runs provider/live checks, or shells into arbitrary user
commands. It only inspects the git changed set and changed-file text, and prints
recommended commands for the operator or reviewer to run themselves.

It reuses the canonical commit-steward path classification
(`run_agent_commit_steward_preflight.build_path_plan`) instead of duplicating it,
and mirrors the machine-enforced worker-return packet-shape vocabulary from
`check_work_order_dispatch_quality` so its diagnostics match the real gate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    from run_agent_commit_steward_preflight import (
        PathPlan,
        build_path_plan,
    )
except ModuleNotFoundError:  # imported as governance.compat.run_agent_automation_assist
    import sys as _sys

    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from run_agent_commit_steward_preflight import (
        PathPlan,
        build_path_plan,
    )

REPO_ROOT = Path(__file__).resolve().parents[2]

# Mirror of the machine-enforced contract vocabulary in
# check_work_order_dispatch_quality.py. Kept as a local mirror so this advisory
# helper has no hard import-time dependency on that gate's heavy module, but the
# terms must stay aligned with the gate.
WORKER_RETURN_PACKET_SHAPE_CONTRACT_MARKER = "Worker Return Packet Shape Contract"
WORKER_RETURN_PACKET_SHAPE_REQUIRED_TERMS = (
    "Purpose",
    "Scope / Methodology",
    "Findings / Position",
    "Risk / Corrective Action",
    "Claim Boundary",
    "Agent Operation Trace Block",
    "Delta Execution Claim Boundary Control Block",
    "Public Export Disposition",
    "executionBaseHead",
    "git status --short",
)
WORKER_RETURN_PACKET_SHAPE_CONDITIONAL_TERMS = (
    "External Knowledge Intake Routing",
    "Rescan Intelligence Hardening",
    "Corpus Completeness And Report Integrity",
    "Finding-To-Governance Learning Disposition",
    "Epistemic Process Block",
    "Machine Closure Package",
)

ALLOWED_MODES = (
    "auto",
    "dispatch",
    "implementation",
    "reviewer-return",
    "closure",
    "session-sync",
    "handoff-sync",
)

_WORK_ORDER_RE = re.compile(r"docs/work_orders/.*\.md$", re.IGNORECASE)
_BASELINE_RE = re.compile(r"docs/baselines/.*\.md$", re.IGNORECASE)
_REVIEW_RE = re.compile(r"docs/reviews/.*\.md$", re.IGNORECASE)
_WORKER_MUST_NOT_COMMIT_RE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?Commit mode:\s*`?WORKER_MUST_NOT_COMMIT`?\s*$"
)
_DISPATCH_STATUS_RE = re.compile(
    r"(?im)^\s*Status:\s*(?:DISPATCH_READY|DISPATCHED|DISPATCHED_TO_WORKER)\s*$"
)
_WORKER_RETURN_RE = re.compile(
    r"\b(?:COMPLETE_PENDING_REVIEW|BLOCKED_WITH_REASON|WORKER_MUST_NOT_COMMIT|worker-return|Worker Return)\b",
    re.IGNORECASE,
)


def _configure_stdout() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def _extract_section(text: str, heading_fragment: str) -> str:
    pattern = re.compile(
        rf"^##\s+.*{re.escape(heading_fragment)}.*$([\s\S]*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.IGNORECASE,
    )
    match = pattern.search(text)
    return match.group(1) if match else ""


def _is_no_commit_work_order(path: str, text: str) -> bool:
    return bool(_WORK_ORDER_RE.search(path)) and bool(
        _WORKER_MUST_NOT_COMMIT_RE.search(text)
    )


def _read_changed_text(path: str) -> str:
    full = REPO_ROOT / path
    if not full.exists() or full.is_dir():
        return ""
    return full.read_text(encoding="utf-8", errors="replace")


@dataclass(frozen=True)
class WorkOrderDiagnostic:
    path: str
    has_contract: bool
    missing_required: tuple[str, ...]
    missing_conditional: tuple[str, ...]
    missing_na_instruction: bool

    @property
    def is_clean(self) -> bool:
        return (
            self.has_contract
            and not self.missing_required
            and not self.missing_conditional
            and not self.missing_na_instruction
        )


def diagnose_no_commit_work_order(path: str, text: str) -> WorkOrderDiagnostic:
    """Mirror the dispatch-quality gate's packet-shape contract check."""
    section = _extract_section(text, WORKER_RETURN_PACKET_SHAPE_CONTRACT_MARKER)
    if not section:
        return WorkOrderDiagnostic(
            path=path,
            has_contract=False,
            missing_required=WORKER_RETURN_PACKET_SHAPE_REQUIRED_TERMS,
            missing_conditional=WORKER_RETURN_PACKET_SHAPE_CONDITIONAL_TERMS,
            missing_na_instruction=True,
        )
    missing_required = tuple(
        term for term in WORKER_RETURN_PACKET_SHAPE_REQUIRED_TERMS if term not in section
    )
    missing_conditional = tuple(
        term
        for term in WORKER_RETURN_PACKET_SHAPE_CONDITIONAL_TERMS
        if term not in section
    )
    missing_na = (
        "N/A with reason" not in section
        and "NOT_APPLICABLE_WITH_REASON" not in section
    )
    return WorkOrderDiagnostic(
        path=path,
        has_contract=True,
        missing_required=missing_required,
        missing_conditional=missing_conditional,
        missing_na_instruction=missing_na,
    )


def recommend_mode(plan: PathPlan) -> str:
    """Map the changed-path plan to one of the supported steward modes."""
    if plan.handoff_sync_only:
        return "handoff-sync"
    if plan.protected_session_paths and not plan.material_paths:
        return "session-sync"
    if plan.mixed_material_and_session:
        return "split"
    if _has_dispatch_packet(plan.changed_paths):
        return "dispatch"
    if _has_worker_return_packet(plan.changed_paths):
        return "reviewer-return"
    if plan.material_paths:
        return "implementation"
    return "none"


def _has_dispatch_packet(paths: tuple[str, ...]) -> bool:
    for path in paths:
        if not (_WORK_ORDER_RE.search(path) or _BASELINE_RE.search(path)):
            continue
        text = _read_changed_text(path)
        if _DISPATCH_STATUS_RE.search(text):
            return True
    return False


def _has_worker_return_packet(paths: tuple[str, ...]) -> bool:
    for path in paths:
        if not _REVIEW_RE.search(path):
            continue
        text = _read_changed_text(path)
        if _WORKER_RETURN_RE.search(text):
            return True
    return False


def _next_command(mode: str, base: str, head: str) -> str:
    if mode in {"dispatch", "implementation", "closure"}:
        phase = {
            "dispatch": "pre-dispatch",
            "implementation": "pre-implementation",
            "closure": "pre-closure",
        }[mode]
        return (
            "python governance/compat/run_agent_autorun_workflow_gate.py "
            f"--phase {phase} --base {base} --head {head} --reuse-valid-receipt"
        )
    if mode == "reviewer-return":
        return "python governance/compat/run_worker_return_fast_gate.py"
    if mode == "session-sync":
        return (
            "python governance/compat/run_agent_commit_steward_preflight.py "
            f"--mode session-sync --base {base} --head {head}"
        )
    if mode == "handoff-sync":
        return (
            "python governance/compat/run_agent_commit_steward_preflight.py "
            f"--mode handoff-sync --base {base} --head {head}"
        )
    if mode == "split":
        return (
            "Commit material paths first, then run "
            "`python governance/compat/run_agent_commit_steward_preflight.py "
            f"--mode session-sync --base {base} --head {head}` for the session/handoff sync commit."
        )
    return "No changed paths detected; no steward command required."


@dataclass
class AssistReport:
    base: str
    head: str
    requested_mode: str
    resolved_mode: str
    changed_paths: tuple[str, ...]
    material_paths: tuple[str, ...]
    protected_session_paths: tuple[str, ...]
    no_commit_work_orders: tuple[WorkOrderDiagnostic, ...]
    next_command: str
    session_sync_hint: str
    defects: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "base": self.base,
            "head": self.head,
            "requestedMode": self.requested_mode,
            "resolvedMode": self.resolved_mode,
            "changedPaths": list(self.changed_paths),
            "materialPaths": list(self.material_paths),
            "protectedSessionPaths": list(self.protected_session_paths),
            "noCommitWorkOrders": [
                {
                    "path": d.path,
                    "hasContract": d.has_contract,
                    "missingRequired": list(d.missing_required),
                    "missingConditional": list(d.missing_conditional),
                    "missingNaInstruction": d.missing_na_instruction,
                    "isClean": d.is_clean,
                }
                for d in self.no_commit_work_orders
            ],
            "nextCommand": self.next_command,
            "sessionSyncHint": self.session_sync_hint,
            "defects": list(self.defects),
        }


def build_report(base: str, head: str, requested_mode: str) -> AssistReport:
    if requested_mode not in ALLOWED_MODES:
        raise ValueError(f"unsupported mode: {requested_mode}")

    plan = build_path_plan(base, head)
    resolved = recommend_mode(plan) if requested_mode == "auto" else requested_mode

    diagnostics: list[WorkOrderDiagnostic] = []
    for path in plan.changed_paths:
        text = _read_changed_text(path)
        if _is_no_commit_work_order(path, text):
            diagnostics.append(diagnose_no_commit_work_order(path, text))

    command_mode = resolved
    if requested_mode == "auto" and resolved in {"none", "split"}:
        command_mode = resolved
    next_command = _next_command(command_mode, base, head)

    if plan.protected_session_paths and not plan.material_paths:
        session_hint = (
            "Only session/handoff paths changed. Use the session-sync or "
            "handoff-sync steward lane; do not mix with a material commit."
        )
    elif plan.mixed_material_and_session:
        session_hint = (
            "Material and session/handoff paths are mixed. Commit material "
            "first, then session-sync second to keep exact-manifest traces clean."
        )
    else:
        session_hint = "N/A with reason: no session-sync-only condition detected."

    defects: list[str] = []
    for d in diagnostics:
        if not d.has_contract:
            defects.append(
                f"{d.path}: changed WORKER_MUST_NOT_COMMIT work order is missing "
                f"`## {WORKER_RETURN_PACKET_SHAPE_CONTRACT_MARKER}`"
            )
            continue
        for term in d.missing_required:
            defects.append(
                f"{d.path}: packet-shape contract missing required term `{term}`"
            )
        for term in d.missing_conditional:
            defects.append(
                f"{d.path}: packet-shape contract missing conditional term `{term}`"
            )
        if d.missing_na_instruction:
            defects.append(
                f"{d.path}: packet-shape contract missing `N/A with reason` instruction"
            )

    return AssistReport(
        base=base,
        head=head,
        requested_mode=requested_mode,
        resolved_mode=resolved,
        changed_paths=plan.changed_paths,
        material_paths=plan.material_paths,
        protected_session_paths=plan.protected_session_paths,
        no_commit_work_orders=tuple(diagnostics),
        next_command=next_command,
        session_sync_hint=session_hint,
        defects=defects,
    )


def _print_human(report: AssistReport) -> None:
    print("=== CVF Agent Automation Assist ===")
    print(f"Range: {report.base}..{report.head}")
    print(f"Requested mode: {report.requested_mode}")
    print(f"Resolved steward lane: {report.resolved_mode}")
    print(f"\nChanged paths: {len(report.changed_paths)}")
    for path in report.changed_paths:
        print(f"  - {path}")
    print(f"Material paths: {len(report.material_paths)}")
    print(f"Protected session/handoff paths: {len(report.protected_session_paths)}")
    print(f"\nSession-sync hint: {report.session_sync_hint}")

    if report.no_commit_work_orders:
        print(f"\nNo-commit work orders inspected: {len(report.no_commit_work_orders)}")
        for d in report.no_commit_work_orders:
            status = "CLEAN" if d.is_clean else "NEEDS PACKET-SHAPE REPAIR"
            print(f"  - {d.path}: {status}")
    else:
        print("\nNo changed WORKER_MUST_NOT_COMMIT work orders detected.")

    print(f"\nExact next command:\n  {report.next_command}")

    if report.defects:
        print(f"\nLocal helper-detectable defects: {len(report.defects)}")
        for defect in report.defects:
            print(f"  ! {defect}")
    else:
        print("\nNo local helper-detectable defects.")


def main(argv: list[str] | None = None) -> int:
    _configure_stdout()
    parser = argparse.ArgumentParser(
        description="CVF read-only agent automation assist helper."
    )
    parser.add_argument("--base", default="HEAD", help="Base ref for the changed range.")
    parser.add_argument("--head", default="HEAD", help="Head ref for the changed range.")
    parser.add_argument(
        "--mode",
        default="auto",
        choices=ALLOWED_MODES,
        help="Steward lane to recommend. 'auto' infers from changed paths.",
    )
    parser.add_argument("--json", action="store_true", help="Emit a JSON report.")
    parser.add_argument(
        "--enforce",
        action="store_true",
        help="Exit non-zero on local helper-detectable defects.",
    )
    args = parser.parse_args(argv)

    try:
        report = build_report(args.base, args.head, args.mode)
    except ValueError as exc:
        print(f"VIOLATION: {exc}", file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(f"VIOLATION: unable to inspect changed set: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        _print_human(report)

    if args.enforce and report.defects:
        if not args.json:
            print(
                f"\nVIOLATION: {len(report.defects)} local helper-detectable defect(s)."
            )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
