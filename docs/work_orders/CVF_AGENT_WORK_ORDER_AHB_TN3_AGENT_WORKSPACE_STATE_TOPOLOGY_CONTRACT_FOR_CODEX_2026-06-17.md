# CVF Agent Work Order - AHB-Tn.3 Agent Workspace State Topology Contract For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-17

Batch ID: AHB-Tn.3

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `3b340823`

executionBaseHead: `3b340823`

closureBaseHead: `3b340823`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Prompt:

Implement AHB-Tn.3 as bounded workspace state topology contract work. Add a
stable `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`
that defines workspace state units, lanes, required fields, storage topology,
future generated-state candidate layout, and archive policy. Update workspace
front doors, AGENTS, operational index, AHB roadmap, GC-018, work order, and
completion evidence. Do not build the workspace, create generated state,
mutate runtime/source, implement a checker, run provider/live proof, public-sync,
edit registries, or claim production/public readiness.

Execution mode: `WORKER_MAY_COMMIT`.

Reviewer: Codex self-review under governed gates.

## Purpose

Close AHB-Tn.3 by defining the workspace state topology before any workspace
state, queue, inbox, dashboard, generated aggregate, or runtime build begins.

## Scope / Target / Owner Boundary

Target: governance-foundation topology contract for future agent-interaction
workspace state.

Owner boundary: Codex owns implementation, review, commit, closure, and session
sync in this single-agent/multi-role batch.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author bounded AHB-Tn.3 dispatch and closure packet |
| Implementer | Codex | Add topology contract and reference pointers |
| Reviewer / closer | Codex | Run focused gates, close with bounded evidence, and commit material |
| Session-sync steward | Codex | Update session continuity after material closure |
| Operator | Human operator | Redirect only if scope would exceed this work order |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex holds dispatcher, implementer, reviewer, closer, and session-sync roles across distinct phases |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=3b340823`; `executionBaseHead=3b340823`; `closureBaseHead=3b340823` |
| changedSetScope(phase) | material AHB-Tn.3 topology-contract changed set only; later session-sync changed set remains separate |
| traceScope(phase, actor) | one Codex Agent Operation Trace Block covers this material batch; session-sync trace is separate if state changes |
| commitOwner(phase) | Codex owns material commit; Codex owns separate session-sync commit after material closure |
| crossBatchIsolation | one-batch-per-clean-worktree; before status evidence records clean worktree at HEAD `3b340823` |
| nextMoveSurfaces | material batch records AHB-Tn.3 closure; separate session sync updates state/front-door/handoff next move |
| Closer designation | Codex is the designated closer for this single-agent/multi-role batch |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | Define state topology for future agent-interaction workspace without building it. |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Storage class | stable foundation file plus dated execution evidence; generated state remains candidate only |
| Handoff fields | CF-01 through CF-09 remain inherited from AHB-T2 and AHB-T3; topology maps future state records back to those fields. |
| State ownership | no new runtime state file, generated aggregate, queue, inbox, or workspace database in this batch; future ownership fields are defined by the topology contract |
| Guard owner | `governance/compat/check_agent_workspace_design.py`; future state checker is candidate only |
| Build boundary | runtime source: no; provider proof: no; public-sync: no; registry edits: no |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-17 proceed with AHB-Tn.3 topology contract | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| AHB-Tn.2 predecessor | `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| Ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACTIVE_RATIFIED |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_2026-06-17.md` | CLOSURE_SATISFIED |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reference/agent_workspace/README.md` | Stable workspace front door |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Control block source |
| `governance/compat/check_agent_workspace_design.py` | Machine enforcement for this work order |
| `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Ratified handoff Central Core |
| `docs/reference/foundation_storage/README.md` | Stable foundation folder/index rule |
| `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-Tn route |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AHB-Tn.2 added workspace design checker | `docs/reviews/CVF_AHB_TN2_AGENT_WORKSPACE_DESIGN_CHECKER_COMPLETION_2026-06-17.md` | Agent Workspace Design Checker Evidence | `check_agent_workspace_design.py` | AHB-Tn.2 checker closure | ACCEPT |
| Workspace design standard requires workspace state decision before build | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Required Workspace Design Model | `Workspace state` | workspace design standard | ACCEPT |
| Workspace front door owns workspace reference family | `docs/reference/agent_workspace/README.md` | Purpose / Local Views | `docs/reference/agent_workspace/` | workspace front door | ACCEPT |
| AHB-T2 remains the handoff Central Core | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Contract Fields | `CF-01` through `CF-09` | Agent Handoff Contract | ACCEPT |
| Foundation folders require stable README front doors | `docs/reference/foundation_storage/CVF_FOUNDATION_FILE_STORAGE_AND_INDEX_STANDARD.md` | Required Folder Front Door | `README.md` | foundation storage standard | ACCEPT |
| Generated aggregate discipline requires source layout plus generator | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | Current generated JSON aggregates | generated source layout | JSON generated aggregate discipline | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Final artifact or evidence | Disposition |
|---|---|---|---|
| Continue foundation hardening after AHB-Tn.2 | add topology contract only | `CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | PASS |
| Preserve Central Core + Local View | cite AHB-T2/AHB-T3/Tn.2 and workspace front door | contract and pointers | PASS |
| Keep build out of scope | forbidden scope and claim boundary | no workspace/runtime/generated-state path changed | PASS |
| Keep future build as separate decision | roadmap row and next-move boundary | AHB-Tn.4 candidate | PASS |

## Allowed Scope

- Add `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`.
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
| Foundation files touched | `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `AGENTS.md`; AHB roadmap |
| Storage class | Stable local-view foundation folder plus dated execution/evidence artifacts |
| Index/front door | `docs/reference/agent_workspace/README.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `AGENTS.md` |
| Date policy | Stable filenames inside `docs/reference/agent_workspace/`; dated GC-018/work-order/completion evidence |
| Archive disposition | N/A with reason: no superseded workspace reference file exists |
| Deferred layout work | Future generated workspace state layout remains candidate and is not created in this batch |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update governed front doors and reference
pointers so future workspace state work routes through a stable topology
contract before implementation.

Protected paths:

- `AGENTS.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`
- `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`

Operator authorization: operator instructed Codex to proceed with AHB-Tn.3
workspace state topology contract on 2026-06-17.

Rollback boundary: revert only AHB-Tn.3 topology contract, pointers, roadmap
update, and matching evidence if this batch is rejected. Do not alter prior
AHB/AOT closures.

## Execution Plan

1. Add stable workspace state topology contract.
2. Update workspace front door, design standard, AGENTS, and operational index.
3. Update AHB roadmap to close AHB-Tn.3 and leave build/generated state as a
   future candidate.
4. Add GC-018, work order, and completion evidence.
5. Run focused governance gates, pre-closure autorun, steward preflight, and
   diff hygiene.

## Pre-Flight Checks

Required before material closure:

```powershell
python governance/compat/check_agent_workspace_design.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_agent_handoff_boundary.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_foundation_storage_layout.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base 3b340823 --head HEAD --enforce
python governance/compat/check_machine_closure_package.py --base 3b340823 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 3b340823 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 3b340823 --head HEAD --enforce
git diff --check
```

## Forbidden Scope

- No product runtime/source mutation.
- No provider/API/live proof.
- No public-sync or public catalog claim.
- No interlock registry edit.
- No workspace build, queue, inbox, UI, generated state aggregate, or runtime route.
- No checker implementation.
- No registry edit or GC-051 entry.

## Write Ownership

| Path | Ownership |
|---|---|
| `AGENTS.md` | Codex may add topology-contract instruction |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Codex may update workspace reference row |
| `docs/reference/agent_workspace/README.md` | Codex may add topology contract pointer |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Codex may add topology contract pointer |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Codex may add stable topology contract |
| AHB-Tn.3 GC-018, work order, completion, and AHB roadmap | Codex owns closure evidence |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | Topology contract exists and is stable under `docs/reference/agent_workspace/`. |
| AC2 | Topology contract defines state units, lanes, required fields, storage topology, generated-state candidate layout, and archive policy. |
| AC3 | Front doors and roadmap point to the topology contract. |
| AC4 | Build/generated-state/runtime/provider/public/registry scope remains forbidden. |
| AC5 | Governance gates pass. |

## Evidence Requirements

Required evidence:

- workspace design checker run on `3b340823..HEAD`;
- handoff boundary checker run on `3b340823..HEAD`;
- foundation storage checker run on `3b340823..HEAD`;
- markdown structural, AOT, machine closure, and pre-closure autorun results;
- closure steward preflight;
- `git diff --check`;
- committed changed-set evidence.

## Review Gate

Codex must reject or repair the batch before commit if any required gate fails
inside allowed scope. Operator escalation is required only if remediation would
build the workspace, create generated workspace state, touch runtime/product
source, public-sync, run provider/live proof, edit registries, implement a
checker, or alter the claim boundary.

## Closure Checklist

| Item | Disposition |
|---|---|
| GC-018, work order, completion review, roadmap, and stable reference files are aligned | PASS |
| Topology contract exists | PASS |
| Front doors point to topology contract | PASS |
| Workspace build/generated-state/runtime/provider/public/registry scope remains forbidden | PASS |
| Governance gates pass before commit | PASS |

## Return-To-Orchestrator Conditions

Return status is `CLOSED_PASS_BOUNDED` after all acceptance criteria pass and
the material closure is committed. Return to orchestrator/operator if any
required gate failure would require workspace build, generated workspace state,
runtime source mutation, provider/live proof, public-sync, registry edit,
checker implementation, or a broader claim boundary than this topology-contract
batch.

## Operator Checkpoint

Operator checkpoint is satisfied for AHB-Tn.3 only: operator authorized bounded
workspace state topology contract work on 2026-06-17. Any AHB-Tn.4 workspace
build, generated workspace state, checker, runtime state, provider proof,
public-sync, registry edit, or production/public readiness claim requires a
fresh operator decision.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_FOR_CODEX_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Topology contract | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | `Status: ACTIVE_CONTRACT` | PASS |
| Stable workspace front door | `docs/reference/agent_workspace/README.md` | topology pointer present | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-Tn.3 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no GC-051 registry edit authorized for this topology-contract batch | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized for this topology-contract batch | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof | N/A | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit | N/A | N/A with reason |
| Generated workspace state | N/A with reason: forbidden by this topology-contract batch | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately if next move changes | N/A | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.3 workspace state topology contract |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch |
| Target paths | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_FOR_CODEX_2026-06-17.md` |
| Allowed scope source | operator authorization for AHB-Tn.3 workspace state topology contract on 2026-06-17 |
| Before status evidence | HEAD `3b340823`; clean worktree |
| After status evidence | AHB-Tn.3 material closure pending commit |
| Diff evidence | `git diff --name-status 3b340823..HEAD` |
| Approval boundary | bounded workspace state topology contract only |
| Claim boundary | no workspace build, generated state/runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn3-agent-workspace-state-topology-contract-2026-06-17` |
| Expected manifest | `AGENTS.md`; `docs/baselines/CVF_GC018_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_FOR_CODEX_2026-06-17.md` |
| Actual changed set | AHB-Tn.3 material changed set, verified in completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this batch changes governed markdown
and reference routing only. It does not edit CVF product runtime routes,
provider adapters, model registries, hardcoded provider selection, public-sync
content, or live-governance behavior. Model Gateway `provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation. No public-sync batch is
authorized.

## Claim Boundary

This work order closes AHB-Tn.3 as bounded workspace state topology contract
work. It does not implement the agent-interaction workspace, create generated
workspace state, alter runtime behavior, run provider/live proof, public-sync,
or claim production/public readiness.
