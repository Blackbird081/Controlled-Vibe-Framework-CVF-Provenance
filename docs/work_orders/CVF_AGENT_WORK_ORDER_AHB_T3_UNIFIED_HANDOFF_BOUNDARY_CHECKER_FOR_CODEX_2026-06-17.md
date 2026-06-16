# CVF Agent Work Order - AHB-T3 Unified Handoff Boundary Checker For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-17

Batch ID: AHB-T3

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `230565e4`

executionBaseHead: `230565e4`

closureBaseHead: `230565e4`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Prompt:

Implement AHB-T3 as bounded machine enforcement for the ratified Agent Handoff
Contract. Add a stable `docs/reference/agent_handoff/` front door, a machine
check standard, the checker, focused tests, autorun/local-hook bindings, AGENTS
and operational-index routing, roadmap closure, completion evidence, and
session continuity after material commit. Do not build the agent-interaction
workspace, mutate product runtime/source, run provider/live proof, public-sync,
or edit registries.

Execution mode: `WORKER_MAY_COMMIT`.

Reviewer: Codex self-review under governed gates.

## Purpose

Close AHB-T3 by making the ratified Agent Handoff Contract machine-enforced for
changed governed handoff work orders and closure artifacts.

## Scope / Target / Owner Boundary

Target: governance-control checker and stable reference layout.

Owner boundary: Codex owns implementation, review, commit, closure, and session
sync in this single-agent/multi-role batch.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author bounded AHB-T3 dispatch and closure packet |
| Implementer | Codex | Add checker, tests, stable reference folder, and hook bindings |
| Reviewer / closer | Codex | Run focused gates, close with bounded evidence, and commit material |
| Session-sync steward | Codex | Update session continuity after material closure if next move changes |
| Operator | Human operator | Redirect only if scope would exceed this work order |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex holds dispatcher, implementer, reviewer, closer, and session-sync roles across distinct phases |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=230565e4`; `executionBaseHead=230565e4`; `closureBaseHead=230565e4` |
| changedSetScope(phase) | material AHB-T3 changed set only; later session-sync changed set remains separate |
| traceScope(phase, actor) | one Codex Agent Operation Trace Block covers this material batch; session-sync trace is separate if state changes |
| commitOwner(phase) | Codex owns material commit; Codex owns separate session-sync commit after material closure |
| crossBatchIsolation | one-batch-per-clean-worktree; before status evidence records clean worktree at HEAD `230565e4` |
| nextMoveSurfaces | material batch records AHB-T3 closure; separate session sync updates state/front-door/handoff next move |
| Closer designation | Codex is the designated closer for this single-agent/multi-role batch |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-17 proceed with AHB-T3 | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| AHB-T2-F2 predecessor | `docs/reviews/CVF_AHB_T2_F2_FOUNDATION_STORAGE_AND_MEMORY_LEARNING_ENFORCEMENT_COMPLETION_2026-06-16.md` | PREDECESSOR_SATISFIED |
| Ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACTIVE_RATIFIED |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_2026-06-17.md` | CLOSURE_SATISFIED |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Ratified handoff Central Core |
| `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-T3 tranche route |
| `governance/compat/check_agent_operation_trace.py` | AOT local-view boundary to preserve |
| `governance/compat/run_agent_autorun_workflow_gate.py` | Autorun binding point |
| `governance/compat/run_local_governance_hook_chain.py` | Local hook binding point |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AHB contract ratifies CF-01 through CF-09 | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Ratified Contract Field Set | `CF-01`; `CF-09` | Agent Handoff Contract | ACCEPT |
| AHB-T3 may implement unified checker | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | AHB-T3 Implementation Boundary | `AHB-T3` | Agent Handoff Contract | ACCEPT |
| AHB roadmap keeps AHB-T3 after T2 | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | Tranche Plan | `AHB-T3` | AHB roadmap | ACCEPT |
| Autorun gate hosts range-aware checks | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `_common_commands` | autorun workflow gate | ACCEPT |
| Local hook chain hosts local checks | `governance/compat/run_local_governance_hook_chain.py` | `HOOK_CHAINS` | `HOOK_CHAINS` | local hook chain | ACCEPT |
| AOT checker already owns trace/manifest validation | `governance/compat/check_agent_operation_trace.py` | `find_trace_violations`; `_check_manifest_delta` | `Expected manifest`; `Actual changed set` | AOT checker | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Final artifact or evidence | Disposition |
|---|---|---|---|
| Implement unified handoff-boundary machine check | add checker and focused tests | `check_agent_handoff_boundary.py`; tests | PASS |
| Derive rule from AHB contract | stable standard cites contract and CF fields | `docs/reference/agent_handoff/` | PASS |
| Enforce at earliest applicable gate phase | bind into autorun and local hooks | autorun/hook edits | PASS |
| Preserve AOT-T3 | checker remains separate from AOT manifest logic | no AOT checker mutation | PASS |
| Keep workspace out of scope | forbidden scope and claim boundary | no workspace path changed | PASS |

## Allowed Scope

- Add `governance/compat/check_agent_handoff_boundary.py`.
- Add `governance/compat/test_check_agent_handoff_boundary.py`.
- Add stable `docs/reference/agent_handoff/README.md`.
- Add stable `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`.
- Update `governance/compat/run_agent_autorun_workflow_gate.py`.
- Update `governance/compat/run_local_governance_hook_chain.py`.
- Update `AGENTS.md`.
- Update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`.
- Update AHB roadmap, GC-018, this work order, and completion review.
- Run focused tests and governance gates.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `AGENTS.md`; AHB roadmap |
| Storage class | Stable local-view foundation folder plus execution/evidence artifacts |
| Index/front door | `docs/reference/agent_handoff/README.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `AGENTS.md` |
| Date policy | Stable filenames inside `docs/reference/agent_handoff/`; dated GC-018/work-order/completion evidence |
| Archive disposition | N/A with reason: no superseded handoff reference file is moved in this batch |
| Deferred layout work | N/A with reason: stable folder, README, standard, AGENTS pointer, and operational-index row are included now |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and bind a bounded agent handoff
boundary checker, with tests and stable reference index, so future governed
handoff work orders must cite and instantiate the ratified AHB contract.

Protected paths:

- `AGENTS.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/agent_handoff/README.md`
- `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`
- `governance/compat/check_agent_handoff_boundary.py`
- `governance/compat/test_check_agent_handoff_boundary.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: operator instructed Codex to proceed with AHB-T3 on
2026-06-17.

Rollback boundary: revert only AHB-T3 checker, tests, hook bindings, stable
handoff reference folder, and matching docs if this batch fails; do not alter
prior AHB/AOT closures.

## Execution Plan

1. Add stable handoff reference front door and standard.
2. Add `check_agent_handoff_boundary.py`.
3. Add focused tests for missing contract block, valid single-agent/multi-role
   work order, C4 reviewer conversion, C3 closer designation, clean-worktree
   evidence, and non-handoff ignore.
4. Bind checker into autorun and local hook chains.
5. Update AGENTS, operational index, AHB roadmap, GC-018, and completion.
6. Run focused tests, checker self-run, pre-closure autorun, steward preflight,
   and diff hygiene.

## Pre-Flight Checks

Required before material closure:

```powershell
pytest governance/compat/test_check_agent_handoff_boundary.py -q
python governance/compat/check_agent_handoff_boundary.py --base 230565e4 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 230565e4 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 230565e4 --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 230565e4 --head HEAD --enforce
python governance/compat/check_foundation_storage_layout.py --base 230565e4 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 230565e4 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 230565e4 --head HEAD --enforce
git diff --check
```

## Forbidden Scope

- No `EXTENSIONS/**` product runtime/source mutation.
- No provider/API/live proof.
- No public-sync or public catalog claim.
- No interlock registry edit.
- No agent-interaction workspace build.
- No broad archive movement.
- No weakening or rewiring of AOT-T3 dispatch-manifest scope logic.

## Write Ownership

| Path | Ownership |
|---|---|
| `AGENTS.md` | Codex may add AHB boundary guard instruction |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Codex may add handoff reference row |
| `docs/reference/agent_handoff/README.md` | Codex may add stable front door |
| `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | Codex may add stable machine-check standard |
| `governance/compat/check_agent_handoff_boundary.py` | Codex may add checker |
| `governance/compat/test_check_agent_handoff_boundary.py` | Codex may add focused tests |
| `governance/compat/run_agent_autorun_workflow_gate.py` | Codex may add checker binding |
| `governance/compat/run_local_governance_hook_chain.py` | Codex may add checker binding |
| AHB-T3 GC-018, work order, completion, and AHB roadmap | Codex owns closure evidence |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Stable `docs/reference/agent_handoff/` front door exists. |
| AC2 | Machine-check standard names the ratified contract and checker. |
| AC3 | Checker catches missing Agent Handoff Contract Control Block. |
| AC4 | Checker catches missing Reviewer Closure Conversion for `WORKER_MUST_NOT_COMMIT`. |
| AC5 | Checker catches missing C3 closer designation. |
| AC6 | Checker catches missing clean-worktree evidence for dispatch-ready handoff packets. |
| AC7 | Checker is bound into autorun and local hooks. |
| AC8 | Focused tests and governance gates pass. |

## Evidence Requirements

Required evidence:

- focused pytest output for `test_check_agent_handoff_boundary.py`;
- handoff boundary checker self-run on `230565e4..HEAD`;
- markdown structural, AOT, machine closure, foundation storage, and
  pre-closure autorun results;
- closure steward preflight;
- `git diff --check`;
- committed changed-set evidence.

## Review Gate

Codex must reject or repair the batch before commit if any required gate fails
inside allowed scope. Operator escalation is required only if remediation would
build the workspace, touch runtime/product source, public-sync, run
provider/live proof, edit registries, or alter the claim boundary.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_FOR_CODEX_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Stable handoff front door | `docs/reference/agent_handoff/README.md` | file exists | PASS |
| Stable handoff standard | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | `Status: ACTIVE_STANDARD_AND_MACHINE_ENFORCED` | PASS |
| Handoff boundary checker | `governance/compat/check_agent_handoff_boundary.py` | file exists and gate passes | PASS |
| Handoff boundary tests | `governance/compat/test_check_agent_handoff_boundary.py` | focused pytest passes | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-T3 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no registry edit authorized for AHB-T3 governance-control enforcement | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized for AHB-T3 governance-control enforcement | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof | N/A | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately | N/A | N/A with reason |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `MACHINE_GATE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_ADDED`; `STANDARD_ADDED`; `HOOK_PHASE_ADDED` |
| Next control action | Use the handoff boundary checker as a mandatory guard for future handoff work orders |
| Worker blame | `N/A_WITH_REASON`: AHB-T3 closes a shared handoff-boundary control gap, not individual worker fault |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this work order changes governance
checkers, tests, and governed markdown only. It does not edit CVF product
runtime routes, provider adapters, model registries, hardcoded provider
selection, or live-governance behavior. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`
and `PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Closure Checklist

| Closure item | Disposition |
|---|---|
| Stable handoff front door added | PASS |
| Stable handoff standard added | PASS |
| Handoff checker added | PASS |
| Focused tests added | PASS |
| Autorun and local hooks updated | PASS |
| AGENTS and operational index updated | PASS |
| AHB roadmap updated | PASS |
| Completion review authored | PASS |
| Workspace/runtime/provider/public-sync remain out of scope | PASS |

## Return-To-Orchestrator Conditions

Return status is `CLOSED_PASS_BOUNDED` after all acceptance criteria pass and
the material closure is committed. Return `BLOCKED` only if a required source
artifact is missing or a gate failure requires forbidden-scope remediation.

## Operator Checkpoint

No operator checkpoint is required unless remediation would require workspace
build, runtime/source edits, public-sync, provider/live proof, registry edits,
destructive actions, or claim-boundary expansion.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-T3 unified handoff-boundary checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Allowed scope source | operator authorization for AHB-T3 on 2026-06-17 |
| Before status evidence | HEAD `230565e4`; clean worktree |
| After status evidence | AHB-T3 material closure pending commit |
| Diff evidence | `git diff --name-status 230565e4..HEAD` |
| Approval boundary | bounded governance-control checker and stable reference front door |
| Claim boundary | no runtime/provider/live/public/workspace implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-t3-unified-handoff-boundary-checker-2026-06-17` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Actual changed set | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_handoff/README.md`; `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`; `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/test_check_agent_handoff_boundary.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.

## Claim Boundary

This work order closes AHB-T3 as bounded governance-control machine
enforcement. It does not implement the workspace, alter runtime behavior, run
provider/live proof, public-sync, or claim production/public readiness.
