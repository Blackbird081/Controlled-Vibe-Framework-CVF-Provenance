# CVF GC-018 AHB-Tn.8-Tn.10 Workspace Runtime Readiness, Queue Skeleton, and Operator View

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-17

Owner: Codex

## Purpose

Authorize one bounded foundation batch that closes three useful AHB workspace
tranches together:

- AHB-Tn.8: runtime expansion readiness contract;
- AHB-Tn.9: minimal runtime queue skeleton;
- AHB-Tn.10: operator-facing workspace read-model plan.

## Scope / Target / Owner Boundary

Target: workspace runtime-readiness governance foundation.

Owner boundary: Codex owns dispatch, implementation, review, closure, and
commit for this batch.

## Authorized Work

| Tranche | Authorized output | Boundary |
|---|---|---|
| AHB-Tn.8 | Runtime expansion readiness contract and runtime boundary guard | no executable runtime |
| AHB-Tn.9 | Local queue skeleton and queue-family README pointers | no queue records, scheduler, worker daemon, provider calls |
| AHB-Tn.10 | Operator-facing read-model plan | no UI implementation |

## Baseline Decision

Decision: approve the combined AHB-Tn.8 through AHB-Tn.10 foundation batch
because the three outputs form one Central Core plus Local View chain for
future workspace runtime expansion.

## Evidence / Verification

Verification requires the runtime boundary checker, workspace state checker,
workspace design checker, handoff boundary checker, AOT checker, machine
closure package checker, and local pre-commit hook chain.

## Source Verification

| Source | Verified marker | Disposition |
|---|---|---|
| `docs/reference/agent_workspace/README.md` | `Status: ACTIVE_INDEX` | ACCEPT |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | `Status: ACTIVE_STANDARD_AND_MACHINE_ENFORCED` | ACCEPT |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | `Status: ACTIVE_CONTRACT` | ACCEPT |
| `CVF_SESSION/agent_workspace/workspace/README.md` | `Status: ACTIVE_SKELETON` | ACCEPT |
| `governance/compat/check_agent_workspace_skeleton.py` | `SKELETON_ROOT` | ACCEPT |
| `governance/compat/check_agent_workspace_state.py` | `ACTIVE_AGENT_WORKSPACE_STATE.json` | ACCEPT |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and bind the agent workspace runtime
boundary guard, update generated workspace state, and update protected control
surfaces required for this foundation batch.

Protected paths:

- `AGENTS.md`
- `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn8-runtime-expansion-readiness-contract-closed.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn9-minimal-runtime-queue-skeleton-closed.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn10-operator-facing-workspace-view-plan-closed.json`
- `governance/compat/check_agent_workspace_runtime_boundary.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/test_agent_workspace_runtime_boundary.py`

Operator authorization: operator approved doing all three useful workspace
foundation tranches together in this session.

Rollback boundary: revert only this AHB-Tn.8 through AHB-Tn.10 material batch
before session-sync commit if a gate fails; do not revert unrelated user work.

## Expected Artifact Existence

- `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md`
- `CVF_SESSION/agent_workspace/runtime_queue/README.md`
- `CVF_SESSION/agent_workspace/runtime_queue/queues/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md`
- `governance/compat/check_agent_workspace_runtime_boundary.py`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN8_TN10_WORKSPACE_RUNTIME_READINESS_QUEUE_SKELETON_OPERATOR_VIEW_FOR_CODEX_2026-06-17.md`
- `docs/reviews/CVF_AHB_TN8_TN10_WORKSPACE_RUNTIME_READINESS_QUEUE_SKELETON_OPERATOR_VIEW_COMPLETION_2026-06-17.md`

## Claim Boundary

This GC-018 does not authorize executable runtime queues, provider/live proof,
public-sync, registry edits, UI implementation, product runtime mutation,
production readiness, or public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance workspace foundation. No public-sync batch is
authorized.
