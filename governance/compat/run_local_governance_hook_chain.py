#!/usr/bin/env python3
"""
CVF Local Governance Hook Chain

Runs the standard local governance checks used by Git hooks in one place so
the hook files stay small and output remains consistent.

Default mode: pre-push
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import subprocess
import sys
import time
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

HOOK_CHAINS: dict[str, list[tuple[str, list[str]]]] = {
    # Local hooks use HEAD..HEAD intentionally as worktree/index validation.
    # Closure evidence must still come from autorun gates with
    # --base <baseHead> --head HEAD over a real committed range.
    "pre-commit": [
        (
            "core guard self-protection",
            ["python", "governance/compat/check_core_guard_self_protection.py", "--enforce"],
        ),
        (
            "governed file size compatibility",
            ["python", "governance/compat/check_governed_file_size.py", "--enforce"],
        ),
        (
            "governed exception registry integrity",
            ["python", "governance/compat/check_governed_exception_registry.py", "--enforce"],
        ),
        (
            "active archive hygiene compatibility",
            [
                "python",
                "governance/compat/check_active_archive_hygiene.py",
                "--max-stale",
                "10",
                "--fail-on-changed-stale",
                "--enforce",
            ],
        ),
        (
            "active session state compatibility",
            ["python", "governance/compat/check_active_session_state.py", "--enforce"],
        ),
        (
            "docs governance compatibility",
            ["python", "governance/compat/check_docs_governance_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "markdown structural completeness",
            ["python", "governance/compat/check_markdown_structural_completeness.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "work-order dispatch quality",
            ["python", "governance/compat/check_work_order_dispatch_quality.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "machine closure package",
            ["python", "governance/compat/check_machine_closure_package.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "multi-provider execution log quality",
            ["python", "governance/compat/check_multi_provider_execution_log.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "finding-to-governance learning quality",
            ["python", "governance/compat/check_finding_to_governance_learning.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "public export disposition quality",
            ["python", "governance/compat/check_public_export_disposition.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus completeness and report integrity",
            ["python", "governance/compat/check_corpus_completeness_report_integrity.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus-to-knowledge-map reconciliation",
            ["python", "governance/compat/check_corpus_to_knowledge_map_reconciliation.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus intelligence classification",
            ["python", "governance/compat/check_corpus_intelligence_classification.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus packet source hash (NR-04)",
            ["python", "governance/compat/check_corpus_packet_source_hash.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus packet normalized path (NR-05)",
            ["python", "governance/compat/check_corpus_packet_normalized_path.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus packet disposition canonical (NR-11)",
            ["python", "governance/compat/check_corpus_packet_disposition_canonical.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus scan registry",
            ["python", "governance/compat/check_corpus_scan_registry.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "system loop interlock",
            ["python", "governance/compat/check_system_loop_interlock.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "governed pack contract compatibility",
            ["python", "governance/compat/check_governed_pack_contract.py", "--enforce"],
        ),
        (
            "continuation chain compatibility",
            ["python", "governance/compat/check_continuation_chain.py", "--enforce"],
        ),
        (
            "execute route step sequence compatibility",
            ["python", "governance/compat/check_execute_route_step_sequence.py", "--enforce"],
        ),
        (
            "anti-collusion evidence trace (GC-046 Phase 0.C)",
            ["python", "governance/compat/check_anti_collusion_evidence_trace.py", "--enforce", "--base", "HEAD", "--head", "HEAD"],
        ),
        (
            "public catalog update advisory (GC-024)",
            ["python", "governance/compat/check_catalog_update_advisory.py"],
        ),
    ],
    "pre-push": [
        (
            "core guard self-protection",
            ["python", "governance/compat/check_core_guard_self_protection.py", "--enforce"],
        ),
        (
            "docs governance compatibility",
            ["python", "governance/compat/check_docs_governance_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "governed artifact authoring compatibility",
            ["python", "governance/compat/check_governed_artifact_authoring.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "markdown structural completeness",
            ["python", "governance/compat/check_markdown_structural_completeness.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "work-order dispatch quality",
            ["python", "governance/compat/check_work_order_dispatch_quality.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "machine closure package",
            ["python", "governance/compat/check_machine_closure_package.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "multi-provider execution log quality",
            ["python", "governance/compat/check_multi_provider_execution_log.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "finding-to-governance learning quality",
            ["python", "governance/compat/check_finding_to_governance_learning.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "public export disposition quality",
            ["python", "governance/compat/check_public_export_disposition.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus completeness and report integrity",
            ["python", "governance/compat/check_corpus_completeness_report_integrity.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus-to-knowledge-map reconciliation",
            ["python", "governance/compat/check_corpus_to_knowledge_map_reconciliation.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus intelligence classification",
            ["python", "governance/compat/check_corpus_intelligence_classification.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus packet source hash (NR-04)",
            ["python", "governance/compat/check_corpus_packet_source_hash.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus packet normalized path (NR-05)",
            ["python", "governance/compat/check_corpus_packet_normalized_path.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "corpus packet disposition canonical (NR-11)",
            ["python", "governance/compat/check_corpus_packet_disposition_canonical.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "system loop interlock",
            ["python", "governance/compat/check_system_loop_interlock.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "cpf public surface maintainability",
            ["python", "governance/compat/check_cpf_public_surface_maintainability.py", "--enforce"],
        ),
        (
            "cpf shared batch helper adoption",
            ["python", "governance/compat/check_cpf_batch_helper_adoption.py", "--enforce"],
        ),
        (
            "batch contract determinism",
            ["python", "governance/compat/check_batch_contract_determinism.py", "--enforce"],
        ),
        (
            "canon summary evidence separation",
            ["python", "governance/compat/check_canon_summary_evidence_separation.py", "--enforce"],
        ),
        (
            "bug documentation compatibility",
            ["python", "governance/compat/check_bug_doc_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "test documentation compatibility",
            ["python", "governance/compat/check_test_doc_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "incremental test log rotation compatibility",
            ["python", "governance/compat/check_incremental_test_log_rotation.py", "--enforce"],
        ),
        (
            "baseline update compatibility",
            ["python", "governance/compat/check_baseline_update_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "agent handoff guard compatibility",
            ["python", "governance/compat/check_agent_handoff_guard_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "active session state compatibility",
            ["python", "governance/compat/check_active_session_state.py", "--enforce"],
        ),
        (
            "session governance bootstrap compatibility",
            ["python", "governance/compat/check_session_governance_bootstrap.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "progress tracker sync compatibility",
            ["python", "governance/compat/check_progress_tracker_sync.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "surface scan continuity compatibility",
            ["python", "governance/compat/check_surface_scan_registry.py", "--enforce"],
        ),
        (
            "product value validation guard compatibility",
            ["python", "governance/compat/check_product_value_validation_guard_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "knowledge absorption priority guard compatibility",
            ["python", "governance/compat/check_knowledge_absorption_priority_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "template skill standard guard compatibility",
            ["python", "governance/compat/check_template_skill_standard_guard_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "governed pack contract compatibility",
            ["python", "governance/compat/check_governed_pack_contract.py", "--enforce"],
        ),
        (
            "continuation chain compatibility",
            ["python", "governance/compat/check_continuation_chain.py", "--enforce"],
        ),
        (
            "execute route step sequence compatibility",
            ["python", "governance/compat/check_execute_route_step_sequence.py", "--enforce"],
        ),
        (
            "multi-agent review governance compatibility",
            ["python", "governance/compat/check_multi_agent_review_governance_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "boardroom runtime governance compatibility",
            ["python", "governance/compat/check_boardroom_runtime_governance_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "extension package check compatibility",
            ["python", "governance/compat/check_extension_package_check.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "fast-lane governance compatibility",
            ["python", "governance/compat/check_fast_lane_governance_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "memory governance compatibility",
            ["python", "governance/compat/check_memory_governance_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "depth-audit continuation compatibility",
            ["python", "governance/compat/check_depth_audit_continuation_compat.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "gc-018 stop-boundary semantics compatibility",
            ["python", "governance/compat/check_gc018_stop_boundary_semantics.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "governed file size compatibility",
            ["python", "governance/compat/check_governed_file_size.py", "--enforce"],
        ),
        (
            "test partition ownership compatibility",
            ["python", "governance/compat/check_test_partition_ownership.py", "--enforce"],
        ),
        (
            "guard registry compatibility",
            ["python", "governance/compat/check_guard_registry.py", "--enforce"],
        ),
        (
            "guard authoring standard compatibility",
            ["python", "governance/compat/check_guard_authoring_standard.py", "--enforce"],
        ),
        (
            "active window registry compatibility",
            ["python", "governance/compat/check_active_window_registry.py", "--enforce"],
        ),
        (
            "active archive hygiene compatibility",
            [
                "python",
                "governance/compat/check_active_archive_hygiene.py",
                "--max-stale",
                "10",
                "--fail-on-changed-stale",
                "--enforce",
            ],
        ),
        (
            "audit retention registry compatibility",
            ["python", "governance/compat/check_audit_retention_registry.py", "--enforce"],
        ),
        (
            "review retention registry compatibility",
            [
                "python",
                "governance/compat/check_review_retention_registry.py",
                "--base",
                "HEAD",
                "--head",
                "HEAD",
                "--scan-mode",
                "fast",
                "--enforce",
            ],
        ),
        (
            "foundational guard surfaces compatibility",
            ["python", "governance/compat/check_foundational_guard_surfaces.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
        ),
        (
            "cross-channel guard contract compatibility",
            ["python", "governance/compat/check_guard_contract_compat.py", "--enforce"],
        ),
        (
            "conformance trace rotation compatibility",
            ["python", "governance/compat/check_conformance_trace_rotation.py", "--enforce"],
        ),
        (
            "repository lifecycle classification compatibility",
            ["python", "governance/compat/check_repository_lifecycle_classification.py", "--enforce"],
        ),
        (
            "repository exposure classification compatibility",
            ["python", "governance/compat/check_repository_exposure_classification.py", "--enforce"],
        ),
        (
            "pre-public p3 readiness compatibility",
            ["python", "governance/compat/check_prepublic_p3_readiness.py", "--enforce"],
        ),
    ]
}


@dataclass(frozen=True)
class StepResult:
    index: int
    label: str
    command: list[str]
    returncode: int
    duration_s: float
    stdout: str
    stderr: str


def _run_step(label: str, command: list[str], index: int | None = None, total: int | None = None) -> int:
    prefix = f"[{index}/{total}] " if index is not None and total is not None else ""
    print(f"[CVF hook] Enforcing {prefix}{label}...", flush=True)
    proc = subprocess.run(command, cwd=REPO_ROOT)
    return proc.returncode


def _run_step_captured(index: int, total: int, label: str, command: list[str]) -> StepResult:
    started_at = time.perf_counter()
    print(f"[CVF hook] START [{index}/{total}] {label}", flush=True)
    proc = subprocess.run(
        command,
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    duration_s = time.perf_counter() - started_at
    return StepResult(
        index=index,
        label=label,
        command=command,
        returncode=proc.returncode,
        duration_s=duration_s,
        stdout=proc.stdout,
        stderr=proc.stderr,
    )


def _print_step_output(result: StepResult, *, show_success_output: bool) -> None:
    should_print = result.returncode != 0 or show_success_output
    if result.stdout and should_print:
        print(result.stdout.rstrip(), flush=True)
    if result.stderr and should_print:
        print(result.stderr.rstrip(), file=sys.stderr, flush=True)


def _run_parallel_chain(
    chain: list[tuple[str, list[str]]],
    *,
    max_workers: int,
    show_success_output: bool,
) -> int:
    total = len(chain)
    worker_count = max(1, min(max_workers, total))
    print(
        f"[CVF hook] Parallel preflight enabled: {total} checks, max_workers={worker_count}.",
        flush=True,
    )
    failures: list[StepResult] = []
    completed = 0

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = [
            executor.submit(_run_step_captured, index, total, label, command)
            for index, (label, command) in enumerate(chain, start=1)
        ]
        for future in as_completed(futures):
            result = future.result()
            completed += 1
            status = "PASS" if result.returncode == 0 else "FAIL"
            print(
                f"[CVF hook] {status} [{completed}/{total}] {result.label} "
                f"({result.duration_s:.2f}s)",
                flush=True,
            )
            _print_step_output(result, show_success_output=show_success_output)
            if result.returncode != 0:
                failures.append(result)

    if failures:
        print("[CVF hook] Parallel preflight failures:", file=sys.stderr, flush=True)
        for result in sorted(failures, key=lambda item: item.index):
            print(
                f"  - [{result.index}/{total}] {result.label} exited {result.returncode}",
                file=sys.stderr,
                flush=True,
            )
        return failures[0].returncode

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the CVF local governance hook chain")
    parser.add_argument(
        "--hook",
        default="pre-push",
        choices=sorted(HOOK_CHAINS.keys()),
        help="Hook chain to run",
    )
    parser.add_argument(
        "--parallel",
        action="store_true",
        help="Run the selected hook chain in parallel for local preflight visibility.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=6,
        help="Maximum parallel checks when --parallel is set.",
    )
    parser.add_argument(
        "--show-success-output",
        action="store_true",
        help="Print stdout/stderr for passing checks in --parallel mode.",
    )
    args = parser.parse_args()

    chain = HOOK_CHAINS[args.hook]
    if args.parallel:
        code = _run_parallel_chain(
            chain,
            max_workers=args.max_workers,
            show_success_output=args.show_success_output,
        )
        if code != 0:
            return code
    else:
        total = len(chain)
        for index, (label, command) in enumerate(chain, start=1):
            code = _run_step(label, command, index, total)
            if code != 0:
                print(f"[CVF hook] FAILED at: {label}", file=sys.stderr, flush=True)
                return code

    print(f"[CVF hook] All {args.hook} governance checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
