#!/usr/bin/env python3
"""
CVF Agent Autorun Workflow Gate

Runs the phase-specific guard bundle agents must pass before dispatch,
implementation, closure, or push. The wrapper does not replace the underlying
guards; it makes the autorun stop points explicit and repeatable.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import subprocess
import sys
from pathlib import Path

import run_agent_commit_steward_preflight as steward


REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class GateCommand:
    name: str
    command: tuple[str, ...]


RANGE_GATE_NAMES = (
    "docs governance compatibility",
    "markdown structural completeness",
    "work-order dispatch quality",
)


def _range_command(name: str, script: str, base: str, head: str) -> GateCommand:
    return GateCommand(
        name,
        (
            "python",
            script,
            "--base",
            base,
            "--head",
            head,
            "--enforce",
        ),
    )


def _common_commands(base: str, head: str) -> tuple[GateCommand, ...]:
    return (
        GateCommand(
            "closure packaging preflight",
            ("python", "governance/compat/check_closure_packaging_preflight.py", "--base", base, "--head", head, "--enforce"),
        ),
        GateCommand(
            "core guard self-protection",
            ("python", "governance/compat/check_core_guard_self_protection.py", "--base", base, "--head", head, "--enforce"),
        ),
        _range_command(
            "docs governance compatibility",
            "governance/compat/check_docs_governance_compat.py",
            base,
            head,
        ),
        _range_command(
            "markdown structural completeness",
            "governance/compat/check_markdown_structural_completeness.py",
            base,
            head,
        ),
        _range_command(
            "work-order dispatch quality",
            "governance/compat/check_work_order_dispatch_quality.py",
            base,
            head,
        ),
        _range_command(
            "dispatch prompt envelope",
            "governance/compat/check_dispatch_prompt_envelope.py",
            base,
            head,
        ),
        _range_command(
            "agent operation trace integrity",
            "governance/compat/check_agent_operation_trace.py",
            base,
            head,
        ),
        _range_command(
            "agent handoff boundary",
            "governance/compat/check_agent_handoff_boundary.py",
            base,
            head,
        ),
        _range_command(
            "agent workspace design boundary",
            "governance/compat/check_agent_workspace_design.py",
            base,
            head,
        ),
        _range_command(
            "agent workspace state",
            "governance/compat/check_agent_workspace_state.py",
            base,
            head,
        ),
        _range_command(
            "agent workspace skeleton",
            "governance/compat/check_agent_workspace_skeleton.py",
            base,
            head,
        ),
        _range_command(
            "machine closure package",
            "governance/compat/check_machine_closure_package.py",
            base,
            head,
        ),
        _range_command(
            "multi-provider execution log quality",
            "governance/compat/check_multi_provider_execution_log.py",
            base,
            head,
        ),
        _range_command(
            "finding-to-governance learning quality",
            "governance/compat/check_finding_to_governance_learning.py",
            base,
            head,
        ),
        _range_command(
            "foundation storage layout",
            "governance/compat/check_foundation_storage_layout.py",
            base,
            head,
        ),
        _range_command(
            "public export disposition quality",
            "governance/compat/check_public_export_disposition.py",
            base,
            head,
        ),
        _range_command(
            "corpus completeness and report integrity",
            "governance/compat/check_corpus_completeness_report_integrity.py",
            base,
            head,
        ),
        _range_command(
            "rescan intelligence hardening",
            "governance/compat/check_rescan_intelligence_hardening.py",
            base,
            head,
        ),
        _range_command(
            "corpus-to-knowledge-map reconciliation",
            "governance/compat/check_corpus_to_knowledge_map_reconciliation.py",
            base,
            head,
        ),
        _range_command(
            "corpus intelligence classification",
            "governance/compat/check_corpus_intelligence_classification.py",
            base,
            head,
        ),
        _range_command(
            "corpus packet source hash (NR-04)",
            "governance/compat/check_corpus_packet_source_hash.py",
            base,
            head,
        ),
        _range_command(
            "corpus packet normalized path (NR-05)",
            "governance/compat/check_corpus_packet_normalized_path.py",
            base,
            head,
        ),
        _range_command(
            "corpus packet disposition canonical (NR-11)",
            "governance/compat/check_corpus_packet_disposition_canonical.py",
            base,
            head,
        ),
        _range_command(
            "corpus scan registry",
            "governance/compat/check_corpus_scan_registry.py",
            base,
            head,
        ),
        _range_command(
            "system loop interlock",
            "governance/compat/check_system_loop_interlock.py",
            base,
            head,
        ),
        GateCommand(
            "ERH CI public-evaluation workflow chain",
            ("python", "governance/compat/check_erh_ci_public_evaluation_workflow.py", "--enforce"),
        ),
        GateCommand(
            "ERH public-surface drift workflow chain",
            ("python", "governance/compat/check_erh_public_surface_drift_workflow.py", "--enforce"),
        ),
        GateCommand(
            "ERH dependency risk workflow chain",
            ("python", "governance/compat/check_erh_dependency_risk_workflow.py", "--enforce"),
        ),
        GateCommand(
            "ERH cvf-web dependency audit workflow chain",
            ("python", "governance/compat/check_erh_cvf_web_dependency_audit_workflow.py", "--enforce"),
        ),
        GateCommand(
            "ERH SAF1 safety workflow chain",
            ("python", "governance/compat/check_erh_safety_workflow_chain.py", "--enforce"),
        ),
        GateCommand(
            "ERH SAF2 output safety workflow chain",
            ("python", "governance/compat/check_erh_output_safety_workflow_chain.py", "--enforce"),
        ),
        GateCommand(
            "ERH DUR1 durable evidence policy snapshot workflow chain",
            ("python", "governance/compat/check_erh_durable_evidence_policy_snapshot.py", "--enforce"),
        ),
        GateCommand(
            "ERH DUR2 external storage adapter workflow chain",
            ("python", "governance/compat/check_erh_external_storage_adapter.py", "--enforce"),
        ),
        GateCommand(
            "active session state compatibility",
            ("python", "governance/compat/check_active_session_state.py", "--enforce"),
        ),
        GateCommand(
            "next-move freshness",
            ("python", "governance/compat/check_next_move_freshness.py", "--enforce"),
        ),
        GateCommand(
            "governed file size compatibility",
            ("python", "governance/compat/check_governed_file_size.py", "--enforce"),
        ),
    )

PRE_PUSH_COMMANDS: tuple[GateCommand, ...] = (
    GateCommand("git remote verification", ("git", "remote", "-v")),
    GateCommand(
        "local pre-push governance hook chain",
        (
            "python",
            "governance/compat/run_local_governance_hook_chain.py",
            "--hook",
            "pre-push",
            "--parallel",
            "--max-workers",
            "6",
        ),
    ),
)


def _run(command: GateCommand) -> int:
    print(f"\n=== {command.name} ===")
    print(" ".join(command.command))
    proc = subprocess.run(
        list(command.command),
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.stdout:
        print(proc.stdout.rstrip())
    if proc.returncode == 0:
        print(f"PASS: {command.name}")
    else:
        print(f"FAIL: {command.name} exited {proc.returncode}")
    return proc.returncode


def _git_status_short() -> str:
    proc = subprocess.run(
        ["git", "status", "--short"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.stdout.strip()


def _git_rev_parse(ref: str) -> str:
    proc = subprocess.run(
        ["git", "rev-parse", "--short", ref],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout.strip() or f"failed to resolve {ref}")
    return proc.stdout.strip()


def _git_diff_name_status(base: str, head: str) -> str:
    proc = subprocess.run(
        ["git", "diff", "--name-status", f"{base}..{head}"],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        return proc.stdout.strip()
    return proc.stdout.strip()


def _range_shape_preflight(phase: str, base: str, head: str) -> int:
    if phase not in {"pre-closure", "pre-push"}:
        return 0

    plan = steward.build_path_plan(base, head)
    if not plan.exact_manifest_collision_risk:
        return 0

    print("\n=== committed range shape preflight ===")
    print(
        "FAIL: range mixes Agent Operation Trace exact-manifest artifacts with "
        "protected session/handoff paths."
    )
    print("This range is not valid closure evidence for a single exact-manifest batch.")
    print("Run split ranges instead: material range first, then closure/session range.")
    print(f"Recommended steward lane: {steward._recommended_mode(plan)}")
    if plan.trace_artifact_paths:
        print("Trace artifacts:")
        for path in plan.trace_artifact_paths:
            print(f"  - {path}")
    if plan.protected_session_paths:
        print("Protected session/handoff paths:")
        for path in plan.protected_session_paths:
            print(f"  - {path}")
    return 1


def _default_base_for_phase(phase: str) -> str:
    if phase in {"pre-closure", "pre-push"}:
        return "HEAD~1"
    return "HEAD"


def _run_phase(phase: str, base: str | None, head: str) -> int:
    resolved_base = base or _default_base_for_phase(phase)
    print("=== CVF Agent Autorun Workflow Gate ===")
    print(f"Phase: {phase}")
    print("Policy: docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md")
    print(f"Range: {resolved_base}..{head}")

    try:
        base_sha = _git_rev_parse(resolved_base)
        head_sha = _git_rev_parse(head)
    except RuntimeError as exc:
        print(f"FAIL: could not resolve autorun gate range: {exc}")
        return 1
    print(f"Base HEAD anchor: {base_sha}")
    print(f"Head anchor: {head_sha}")

    failures = 0
    commands: list[GateCommand] = list(_common_commands(resolved_base, head))
    if phase == "pre-push":
        commands.extend(PRE_PUSH_COMMANDS)

    # Fix (B): at pre-implementation, check that no forbidden-path files
    # already exist on disk before a worker begins. This catches the pattern
    # where a prior tranche left untracked files in paths the current work
    # order explicitly forbids.
    if phase == "pre-implementation":
        commands.insert(0, GateCommand(
            "forbidden filesystem state",
            ("python", "governance/compat/check_forbidden_filesystem_state.py",
             "--base", resolved_base, "--head", head, "--enforce"),
        ))

    if phase in {"pre-closure", "pre-push"} and base_sha == head_sha:
        print(
            "FAIL: closure/push autorun gates require a non-empty committed "
            "range. Pass --base <baseHead> --head HEAD or run after a commit "
            "with default HEAD~1..HEAD."
        )
        failures += 1
    elif phase in {"pre-closure", "pre-push"}:
        changed = _git_diff_name_status(resolved_base, head)
        print("\n=== committed range evidence ===")
        print(changed if changed else "No committed files changed in range.")
        if not changed:
            print("FAIL: closure/push range has no committed diff evidence.")
            failures += 1
        range_shape_failures = _range_shape_preflight(phase, resolved_base, head)
        if range_shape_failures:
            print(
                f"\nVIOLATION: {phase} blocked by committed range shape before "
                "running the full guard bundle."
            )
            return 1

    for command in commands:
        failures += 1 if _run(command) != 0 else 0

    if phase == "pre-closure":
        print("\n=== closure worktree finality ===")
        status = _git_status_short()
        if status:
            print(status)
            print(
                "FAIL: pre-closure cannot claim CLOSED while worktree changes are "
                "uncommitted, untracked, or otherwise unresolved."
            )
            failures += 1
        else:
            print("PASS: worktree is clean for closure claim finality.")

    if failures:
        print(f"\nVIOLATION: {phase} blocked by {failures} failing gate(s).")
        return 1

    print(f"\nCOMPLIANT: {phase} autorun gate passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run CVF agent autorun workflow gate")
    parser.add_argument(
        "--phase",
        choices=("pre-dispatch", "pre-implementation", "pre-closure", "pre-push"),
        required=True,
    )
    parser.add_argument(
        "--base",
        default=None,
        help="Base commit/ref for range-aware gates. Defaults to HEAD for pre-dispatch/pre-implementation and HEAD~1 for pre-closure/pre-push.",
    )
    parser.add_argument("--head", default="HEAD", help="Head commit/ref for range-aware gates.")
    args = parser.parse_args()
    return _run_phase(args.phase, args.base, args.head)


if __name__ == "__main__":
    sys.exit(main())
