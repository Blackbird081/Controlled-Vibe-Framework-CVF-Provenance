# CVF Agent Work Order - AHB-Tn.2 Agent Workspace Design Checker For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-17

Batch ID: AHB-Tn.2

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `5c79881e`

executionBaseHead: `5c79881e`

closureBaseHead: `5c79881e`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Prompt:

Implement AHB-Tn.2 as bounded workspace-foundation hardening. Add and bind a
dedicated `check_agent_workspace_design.py` guard so changed workspace work
orders must include the Agent Workspace Design Control Block defined by
AHB-Tn.1. Add focused tests, update the stable workspace front door and
standard, update AGENTS/index/roadmap, and close with GC-018, work order,
completion evidence, material commit, and separate session sync. Do not build
the workspace, mutate product runtime/source, run provider/live proof,
public-sync, edit registries, or claim production/public readiness.

Execution mode: `WORKER_MAY_COMMIT`.

Reviewer: Codex self-review under governed gates.

## Purpose

Close AHB-Tn.2 by converting the future workspace pre-build control block from
artifact guidance into machine enforcement.

## Scope / Target / Owner Boundary

Target: governance-control checker and stable reference update for the
agent-interaction workspace design boundary.

Owner boundary: Codex owns implementation, review, commit, closure, and session
sync in this single-agent/multi-role batch.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author bounded AHB-Tn.2 dispatch and closure packet |
| Implementer | Codex | Add checker, tests, hook bindings, and reference updates |
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
| baseHeadFor(phase) | `dispatchBaseHead=5c79881e`; `executionBaseHead=5c79881e`; `closureBaseHead=5c79881e` |
| changedSetScope(phase) | material AHB-Tn.2 checker changed set only; later session-sync changed set remains separate |
| traceScope(phase, actor) | one Codex Agent Operation Trace Block covers this material batch; session-sync trace is separate if state changes |
| commitOwner(phase) | Codex owns material commit; Codex owns separate session-sync commit after material closure if next move changes |
| crossBatchIsolation | one-batch-per-clean-worktree; before status evidence records clean worktree at HEAD `5c79881e` |
| nextMoveSurfaces | material batch records AHB-Tn.2 closure; separate session sync updates state/front-door/handoff next move |
| Closer designation | Codex is the designated closer for this single-agent/multi-role batch |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | Machine-enforce the future agent-interaction workspace pre-build boundary only. |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Storage class | stable foundation files, governance checker source, focused tests, and dated execution evidence |
| Handoff fields | CF-01 through CF-09 remain inherited from AHB-T2 and AHB-T3; this checker guards workspace-specific pre-build fields. |
| State ownership | no new runtime state file, generated aggregate, queue, inbox, or workspace database in this batch |
| Guard owner | `governance/compat/check_agent_workspace_design.py` |
| Build boundary | runtime source: no; provider proof: no; public-sync: no; registry edits: no |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-17 continue AHB-Tn.2 workspace foundation hardening | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| AHB-Tn.1 predecessor | `docs/reviews/CVF_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| Ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACTIVE_RATIFIED |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_2026-06-17.md` | CLOSURE_SATISFIED |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reference/agent_workspace/README.md` | Stable workspace front door |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Control block source |
| `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Ratified handoff Central Core |
| `docs/reference/agent_handoff/README.md` | Machine-enforced handoff local view |
| `docs/reference/foundation_storage/README.md` | Stable foundation folder/index rule |
| `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-Tn route |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AHB-Tn.1 defined Agent Workspace Design Control Block | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Minimum Pre-Build Control Block | `Agent Workspace Design Control Block` | workspace design standard | ACCEPT |
| AHB-Tn.1 stable front door exists | `docs/reference/agent_workspace/README.md` | Central Core / Required Read Trigger | `docs/reference/agent_workspace/README.md` | workspace front door | ACCEPT |
| AHB-T2 remains the handoff Central Core | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Contract Fields | `CF-01` through `CF-09` | Agent Handoff Contract | ACCEPT |
| AHB-T3 provides machine-enforced handoff work-order local view | `governance/compat/check_agent_handoff_boundary.py` | constants and validation functions | `Agent Handoff Contract Control Block` | AHB-T3 checker | ACCEPT |
| Foundation folders require stable README front doors | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Required Folder Front Door | `README.md` | foundation storage standard | ACCEPT |
| Operational index is the cross-CVF lookup front door | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Maintenance Rule | `Lookup Table` | operational reference index | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Final artifact or evidence | Disposition |
|---|---|---|---|
| Machine-harden workspace design after AHB-Tn.1 | add workspace checker and tests | `check_agent_workspace_design.py`; focused tests | PASS |
| Preserve Central Core + Local View | cite AHB-T2, AHB-T3, and workspace front door | checker and standard | PASS |
| Include foundation folder/index storage | update stable `agent_workspace` README and standard in place | stable folder front door | PASS |
| Keep build out of scope | forbidden scope and claim boundary | no workspace/runtime path changed | PASS |

## Allowed Scope

- Add `governance/compat/check_agent_workspace_design.py`.
- Add `governance/compat/test_check_agent_workspace_design.py`.
- Update `governance/compat/run_agent_autorun_workflow_gate.py`.
- Update `governance/compat/run_local_governance_hook_chain.py`.
- Update `docs/reference/agent_workspace/README.md`.
- Update
  `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`.
- Update `AGENTS.md`.
- Update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`.
- Update AHB roadmap, GC-018, this work order, and completion review.
- Run governance gates.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `AGENTS.md`; AHB roadmap |
| Storage class | Stable local-view foundation folder plus governance checker source/tests and execution/evidence artifacts |
| Index/front door | `docs/reference/agent_workspace/README.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `AGENTS.md` |
| Date policy | Stable filenames inside `docs/reference/agent_workspace/`; dated GC-018/work-order/completion evidence |
| Archive disposition | N/A with reason: no superseded workspace reference file exists |
| Deferred layout work | N/A with reason: checker, README, standard, AGENTS pointer, and operational-index row are included now |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and bind the workspace design checker so
future workspace work has machine-enforced pre-build control evidence.

Protected paths:

- `AGENTS.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`
- `governance/compat/check_agent_workspace_design.py`
- `governance/compat/test_check_agent_workspace_design.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: operator instructed Codex to continue with AHB-Tn.2
workspace-foundation hardening on 2026-06-17.

Rollback boundary: revert only AHB-Tn.2 workspace checker, tests, bindings,
pointers, roadmap update, and matching evidence if this batch is rejected. Do
not alter prior AHB/AOT closures.

## Execution Plan

1. Add workspace design checker and focused tests.
2. Bind the checker into autorun and local governance hook chains.
3. Update workspace front door, design standard, AGENTS, and operational index.
4. Update AHB roadmap to close AHB-Tn.2 and leave build as a future candidate.
5. Add GC-018, work order, and completion evidence.
6. Run focused governance gates, pre-closure autorun, steward preflight, and
   diff hygiene.

## Pre-Flight Checks

Required before material closure:

```powershell
pytest governance/compat/test_check_agent_workspace_design.py -q
python governance/compat/check_agent_workspace_design.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_agent_handoff_boundary.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_foundation_storage_layout.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 5c79881e --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 5c79881e --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 5c79881e --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 5c79881e --head HEAD --enforce
git diff --check
```

## Forbidden Scope

- No `EXTENSIONS/**` product runtime/source mutation.
- No provider/API/live proof.
- No public-sync or public catalog claim.
- No interlock registry edit.
- No workspace build, queue, UI, generated state aggregate, or runtime route.
- No broad archive movement.
- No registry edit or GC-051 entry.

## Write Ownership

| Path | Ownership |
|---|---|
| `AGENTS.md` | Codex may add workspace checker instruction |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Codex may update workspace reference row |
| `docs/reference/agent_workspace/README.md` | Codex may add checker pointer |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Codex may mark machine enforcement |
| `governance/compat/check_agent_workspace_design.py` | Codex may add workspace design checker |
| `governance/compat/test_check_agent_workspace_design.py` | Codex may add focused tests |
| `governance/compat/run_agent_autorun_workflow_gate.py` | Codex may bind checker |
| `governance/compat/run_local_governance_hook_chain.py` | Codex may bind checker |
| AHB-Tn.2 GC-018, work order, completion, and AHB roadmap | Codex owns closure evidence |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Workspace checker exists and validates changed workspace work orders. |
| AC2 | Focused tests pass. |
| AC3 | Workspace standard names the checker and machine-enforced status. |
| AC4 | AGENTS and operational index route future agents to the checker/front door. |
| AC5 | Autorun and local hook chains run the checker. |
| AC6 | Governance gates pass. |

## Evidence Requirements

Required evidence:

- focused pytest for workspace design checker;
- workspace checker self-run on `5c79881e..HEAD`;
- handoff boundary checker run on `5c79881e..HEAD`;
- foundation storage checker run on `5c79881e..HEAD`;
- markdown structural, AOT, machine closure, and pre-closure autorun results;
- closure steward preflight;
- `git diff --check`;
- committed changed-set evidence.

## Review Gate

Codex must reject or repair the batch before commit if any required gate fails
inside allowed scope. Operator escalation is required only if remediation would
build the workspace, touch runtime/product source, public-sync, run
provider/live proof, edit registries, or alter the claim boundary.

## Closure Checklist

| Item | Disposition |
|---|---|
| GC-018, work order, completion review, roadmap, checker, tests, and stable reference files are aligned | PASS |
| Workspace checker exists | PASS |
| Focused tests exist | PASS |
| Autorun and local hooks include the checker | PASS |
| AGENTS and operational index route future agents to the checker/front door | PASS |
| Workspace build/runtime/provider/public/registry scope remains forbidden | PASS |
| Governance gates pass before commit | PASS |

## Return-To-Orchestrator Conditions

Return status is `CLOSED_PASS_BOUNDED` after all acceptance criteria pass and
the material closure is committed. Return to orchestrator/operator if any
required gate failure would require workspace build, runtime source mutation,
provider/live proof, public-sync, registry edit, or a broader claim boundary
than this machine-hardening batch.

## Operator Checkpoint

Operator checkpoint is satisfied for AHB-Tn.2 only: operator authorized bounded
workspace foundation hardening on 2026-06-17. Any AHB-Tn.3 build, runtime state,
provider proof, public-sync, registry edit, or production/public readiness
claim requires a fresh operator decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_FOR_CODEX_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Workspace checker | `governance/compat/check_agent_workspace_design.py` | gate PASS | PASS |
| Workspace checker tests | `governance/compat/test_check_agent_workspace_design.py` | focused pytest PASS | PASS |
| Stable workspace front door | `docs/reference/agent_workspace/README.md` | checker pointer present | PASS |
| Stable workspace design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | `Status: ACTIVE_STANDARD_AND_MACHINE_ENFORCED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-Tn.2 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no GC-051 registry edit authorized for this checker batch | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized for this checker batch | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof | N/A | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit | N/A | N/A with reason |
| Runtime workspace build | N/A with reason: forbidden by this checker batch | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately if next move changes | N/A | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.2 agent workspace design checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/test_check_agent_workspace_design.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Allowed scope source | operator authorization for AHB-Tn.2 workspace-foundation hardening on 2026-06-17 |
| Before status evidence | HEAD `5c79881e`; clean worktree |
| After status evidence | AHB-Tn.2 material closure pending commit |
| Diff evidence | `git diff --name-status 5c79881e..HEAD` |
| Approval boundary | bounded workspace design checker and foundation hardening only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn2-agent-workspace-design-checker-2026-06-17` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/test_check_agent_workspace_design.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Actual changed set | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_design.py`; `governance/compat/test_check_agent_workspace_design.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this batch changes governance checkers,
tests, and governed markdown only. It does not edit CVF product runtime routes,
provider adapters, model registries, hardcoded provider selection, public-sync
content, or live-governance behavior. Model Gateway `provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance enforcement. No public-sync batch is
authorized.

## Claim Boundary

This work order closes AHB-Tn.2 as bounded workspace design machine
enforcement. It does not implement the agent-interaction workspace, alter
runtime behavior, run provider/live proof, public-sync, or claim
production/public readiness.
