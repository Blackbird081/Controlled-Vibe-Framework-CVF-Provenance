# CVF GC-018 Baseline - AHB-Tn.7 Bounded Agent Workspace Build Skeleton

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-17

Owner: Codex

Baseline ID: GC-018-AHB-Tn.7

baseHead: `338c34e2`

## Purpose

Authorize the bounded execution of AHB-Tn.5-A as a local agent workspace
skeleton: stable skeleton front door, lane index, lane folders, skeleton guard,
state disposition, roadmap closure, and session-ready evidence.

## Scope / Target / Owner Boundary

Target: bounded local skeleton under `CVF_SESSION/agent_workspace/workspace/`
and machine guard under `governance/compat/`.

Owner boundary: Codex owns dispatch, implementation, review, closure, material
commit, and later session-sync. This baseline does not authorize runtime
queues, scheduler queues, UI, provider/live proof, public-sync, registry edit,
product runtime mutation, production readiness, or public readiness.

## Source Authority

| Source | Path | Disposition |
|---|---|---|
| Operator instruction | chat on 2026-06-17 approving AHB-Tn.5-A | ACCEPT |
| Active next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Workspace front door | `docs/reference/agent_workspace/README.md` | ACCEPT |
| Workspace topology | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | ACCEPT |
| Lane taxonomy | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md` | ACCEPT |
| Item template | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_ITEM_TEMPLATE.json` | ACCEPT |
| Option matrix | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md` | ACCEPT |

## Decision

Proceed with AHB-Tn.7 as a single-agent/multi-role Codex batch. This closes
AHB-Tn.5-A at skeleton level only.

## Claim Boundary

No runtime queue, scheduler, UI, provider/live proof, public-sync, registry
edit, product runtime mutation, production readiness, or public readiness is
authorized or claimed.

## Evidence / Verification

Required verification:

- `python governance/compat/check_agent_workspace_skeleton.py --base 338c34e2 --head HEAD --enforce`
- `python governance/compat/check_agent_workspace_state.py --base 338c34e2 --head HEAD --enforce`
- `python -m pytest governance/compat/test_agent_workspace_skeleton.py governance/compat/test_agent_workspace_state.py governance/compat/test_check_agent_workspace_design.py -q`
- `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit --parallel --max-workers 6`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance workspace foundation. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.7 bounded agent workspace build skeleton |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `.gitignore`; `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn7-bounded-workspace-build-skeleton-closed.json`; `CVF_SESSION/agent_workspace/workspace/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/intake/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/dispatch/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/execution/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/worker_return/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/review/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/accepted_material/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/session_sync/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/parked/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/blocked/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/archive_ready/README.md`; `docs/baselines/CVF_GC018_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_workspace_skeleton.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_skeleton.py` |
| Allowed scope source | operator authorization to execute bounded AHB-Tn.5-A skeleton on 2026-06-17 |
| Before status evidence | HEAD `338c34e2`; clean worktree |
| After status evidence | AHB-Tn.7 material closure pending commit |
| Diff evidence | `git diff --name-status 338c34e2..HEAD` |
| Approval boundary | bounded local workspace skeleton only |
| Claim boundary | no runtime/provider/live/public/registry/product-readiness implementation claim |
| Agent type | Codex dispatcher/implementer/reviewer/closer |
| Invocation ID | `ahb-tn7-bounded-agent-workspace-build-skeleton-2026-06-17` |
| Expected manifest | `.gitignore`; `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn7-bounded-workspace-build-skeleton-closed.json`; `CVF_SESSION/agent_workspace/workspace/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/intake/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/dispatch/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/execution/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/worker_return/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/review/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/accepted_material/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/session_sync/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/parked/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/blocked/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/archive_ready/README.md`; `docs/baselines/CVF_GC018_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_workspace_skeleton.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_skeleton.py` |
| Actual changed set | `.gitignore`; `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn7-bounded-workspace-build-skeleton-closed.json`; `CVF_SESSION/agent_workspace/workspace/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/intake/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/dispatch/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/execution/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/worker_return/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/review/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/accepted_material/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/session_sync/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/parked/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/blocked/README.md`; `CVF_SESSION/agent_workspace/workspace/lanes/archive_ready/README.md`; `docs/baselines/CVF_GC018_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_workspace_skeleton.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_skeleton.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
