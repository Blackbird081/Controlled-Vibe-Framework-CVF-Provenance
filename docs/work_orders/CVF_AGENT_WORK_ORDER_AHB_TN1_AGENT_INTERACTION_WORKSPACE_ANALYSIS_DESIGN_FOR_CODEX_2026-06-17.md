# CVF Agent Work Order - AHB-Tn.1 Agent Interaction Workspace Analysis Design For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-17

Batch ID: AHB-Tn.1

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `05f3f795`

executionBaseHead: `05f3f795`

closureBaseHead: `05f3f795`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Prompt:

Implement AHB-Tn.1 as bounded analysis/design for the future
agent-interaction workspace. Add a stable `docs/reference/agent_workspace/`
front door, a design standard, AGENTS and operational-index pointers, roadmap
closure, GC-018, work-order evidence, completion evidence, and session
continuity after material commit if next move changes. Do not build the
workspace, mutate product runtime/source, run provider/live proof, public-sync,
edit registries, or create a dedicated workspace checker in this batch.

Execution mode: `WORKER_MAY_COMMIT`.

Reviewer: Codex self-review under governed gates.

## Purpose

Close AHB-Tn.1 by turning the future agent-interaction workspace from a vague
candidate into a governed design surface with a stable retrieval path and an
explicit pre-build boundary.

## Scope / Target / Owner Boundary

Target: governance-foundation workspace design packet and stable reference
layout.

Owner boundary: Codex owns implementation, review, commit, closure, and session
sync in this single-agent/multi-role batch.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author bounded AHB-Tn.1 dispatch and closure packet |
| Implementer | Codex | Add workspace front door, design standard, and routing pointers |
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
| baseHeadFor(phase) | `dispatchBaseHead=05f3f795`; `executionBaseHead=05f3f795`; `closureBaseHead=05f3f795` |
| changedSetScope(phase) | material AHB-Tn.1 design changed set only; later session-sync changed set remains separate |
| traceScope(phase, actor) | one Codex Agent Operation Trace Block covers this material batch; session-sync trace is separate if state changes |
| commitOwner(phase) | Codex owns material commit; Codex owns separate session-sync commit after material closure if next move changes |
| crossBatchIsolation | one-batch-per-clean-worktree; before status evidence records clean worktree at HEAD `05f3f795` |
| nextMoveSurfaces | material batch records AHB-Tn.1 closure; separate session sync updates state/front-door/handoff next move if needed |
| Closer designation | Codex is the designated closer for this single-agent/multi-role batch |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-17 proceed with AHB-Tn analysis/design | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| AHB-T3 predecessor | `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| Ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACTIVE_RATIFIED |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_2026-06-17.md` | CLOSURE_SATISFIED |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Ratified handoff Central Core |
| `docs/reference/agent_handoff/README.md` | Machine-enforced handoff local view |
| `docs/reference/foundation_storage/README.md` | Stable foundation folder/index rule |
| `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-Tn route |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active state permits AHB-Tn analysis/design after AHB-T3 | `CVF_SESSION/state/entries/nextAllowedMove.json` | `value` | `AHB-Tn agent-interaction workspace analysis/design` | active session state | ACCEPT |
| AHB-T2 leaves workspace build out of scope but contract applies to all role configurations | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Scope / Applies-To | `C1`; `C4`; workspace boundary | Agent Handoff Contract | ACCEPT |
| AHB-T3 provides machine-enforced handoff work-order local view | `docs/reviews/CVF_AHB_T3_UNIFIED_HANDOFF_BOUNDARY_CHECKER_COMPLETION_2026-06-17.md` | Agent Handoff Boundary Checker Evidence | `check_agent_handoff_boundary.py` | AHB-T3 checker | ACCEPT |
| AHB roadmap keeps agent-interaction workspace as AHB-Tn scope after AHB-T3 | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-T3 Closure Note | `AHB-Tn` | AHB roadmap | ACCEPT |
| Foundation folders require stable README front doors | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Required Folder Front Door | `README.md` | foundation storage standard | ACCEPT |
| Operational index is the cross-CVF lookup front door | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Maintenance Rule | `Lookup Table` | operational reference index | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Final artifact or evidence | Disposition |
|---|---|---|---|
| Keep workspace as post-AHB-T3 scope | create analysis/design tranche only | AHB-Tn.1 documents | PASS |
| Preserve Central Core + Local View | cite AHB-T2 contract and AHB-T3 checker | `agent_workspace` front door and standard | PASS |
| Include foundation folder/index storage | add stable `docs/reference/agent_workspace/README.md` | stable folder front door | PASS |
| Keep build out of scope | forbidden scope and claim boundary | no workspace/runtime path changed | PASS |

## Allowed Scope

- Add `docs/reference/agent_workspace/README.md`.
- Add `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`.
- Update `AGENTS.md`.
- Update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`.
- Update AHB roadmap, GC-018, this work order, and completion review.
- Run governance gates.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation files touched | `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `AGENTS.md`; AHB roadmap |
| Storage class | Stable local-view foundation folder plus execution/evidence artifacts |
| Index/front door | `docs/reference/agent_workspace/README.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `AGENTS.md` |
| Date policy | Stable filenames inside `docs/reference/agent_workspace/`; dated GC-018/work-order/completion evidence |
| Archive disposition | N/A with reason: no superseded workspace reference file exists |
| Deferred layout work | N/A with reason: stable folder, README, standard, AGENTS pointer, and operational-index row are included now |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add the stable agent-workspace design front
door and pointers so future workspace work has a governed retrieval path before
any build or runtime mutation is proposed.

Protected paths:

- `AGENTS.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`

Operator authorization: operator instructed Codex to proceed with AHB-Tn
analysis/design on 2026-06-17.

Rollback boundary: revert only AHB-Tn.1 workspace design files, pointers,
roadmap update, and matching evidence if this batch is rejected. Do not alter
prior AHB/AOT closures.

## Execution Plan

1. Add stable workspace reference front door and design standard.
2. Update AGENTS and operational index so future agents route through the
   workspace front door.
3. Update AHB roadmap to close AHB-Tn.1 and leave build as a future candidate.
4. Add GC-018, work order, and completion evidence.
5. Run focused governance gates, pre-closure autorun, steward preflight, and
   diff hygiene.

## Pre-Flight Checks

Required before material closure:

```powershell
python governance/compat/check_agent_handoff_boundary.py --base 05f3f795 --head HEAD --enforce
python governance/compat/check_foundation_storage_layout.py --base 05f3f795 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 05f3f795 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 05f3f795 --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 05f3f795 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 05f3f795 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 05f3f795 --head HEAD --enforce
git diff --check
```

## Forbidden Scope

- No `EXTENSIONS/**` product runtime/source mutation.
- No provider/API/live proof.
- No public-sync or public catalog claim.
- No interlock registry edit.
- No workspace build, queue, UI, generated state aggregate, or runtime route.
- No broad archive movement.
- No dedicated workspace checker implementation.

## Write Ownership

| Path | Ownership |
|---|---|
| `AGENTS.md` | Codex may add workspace design boundary instruction |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Codex may add workspace reference row |
| `docs/reference/agent_workspace/README.md` | Codex may add stable front door |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Codex may add stable design standard |
| AHB-Tn.1 GC-018, work order, completion, and AHB roadmap | Codex owns closure evidence |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Stable `docs/reference/agent_workspace/` front door exists. |
| AC2 | Design standard names the ratified contract, AHB-T3 checker, and foundation storage standard. |
| AC3 | Future workspace build is explicitly blocked behind fresh authorization. |
| AC4 | AGENTS and operational index route future agents to the workspace front door. |
| AC5 | Roadmap records AHB-Tn.1 closure and later build candidate. |
| AC6 | Governance gates pass. |

## Evidence Requirements

Required evidence:

- handoff boundary checker run on `05f3f795..HEAD`;
- foundation storage checker run on `05f3f795..HEAD`;
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
| GC-018, work order, completion review, roadmap, and stable reference files are aligned | PASS |
| Stable workspace front door exists | PASS |
| Stable workspace design standard exists | PASS |
| AGENTS and operational index route future agents to the front door | PASS |
| Workspace build/runtime/provider/public/registry scope remains forbidden | PASS |
| Governance gates pass before commit | PASS |

## Return-To-Orchestrator Conditions

Return status is `CLOSED_PASS_BOUNDED` after all acceptance criteria pass and
the material closure is committed. Return to orchestrator/operator if any
required gate failure would require workspace build, runtime source mutation,
provider/live proof, public-sync, registry edit, new dedicated checker
implementation, or a broader claim boundary than this analysis/design batch.

## Operator Checkpoint

Operator checkpoint is satisfied for AHB-Tn.1 only: operator authorized bounded
analysis/design on 2026-06-17. Any AHB-Tn.2 build, runtime state, machine
checker, provider proof, public-sync, registry edit, or production/public
readiness claim requires a fresh operator decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_FOR_CODEX_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Stable workspace front door | `docs/reference/agent_workspace/README.md` | file exists | PASS |
| Stable workspace design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | `Status: ACTIVE_STANDARD` | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-Tn.1 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no GC-051 registry edit authorized for this design-only batch | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized for this design-only batch | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof | N/A | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit | N/A | N/A with reason |
| Runtime workspace build | N/A with reason: forbidden by this design-only batch | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately if next move changes | N/A | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.1 agent-interaction workspace analysis/design |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_FOR_CODEX_2026-06-17.md` |
| Allowed scope source | operator authorization for AHB-Tn analysis/design on 2026-06-17 |
| Before status evidence | HEAD `05f3f795`; clean worktree |
| After status evidence | AHB-Tn.1 material closure pending commit |
| Diff evidence | `git diff --name-status 05f3f795..HEAD` |
| Approval boundary | bounded workspace analysis/design foundation only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn1-agent-interaction-workspace-analysis-design-2026-06-17` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_FOR_CODEX_2026-06-17.md` |
| Actual changed set | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reviews/CVF_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN1_AGENT_INTERACTION_WORKSPACE_ANALYSIS_DESIGN_FOR_CODEX_2026-06-17.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this batch changes governed markdown
and reference indexes only. It does not edit CVF product runtime routes,
provider adapters, model registries, hardcoded provider selection, public-sync
content, or live-governance behavior. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`
and `PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance design. No public-sync batch is
authorized.

## Claim Boundary

This work order closes AHB-Tn.1 as bounded workspace analysis/design
foundation. It does not implement the agent-interaction workspace, alter
runtime behavior, run provider/live proof, public-sync, or claim
production/public readiness.
