# CVF Agent Work Order - AHB-Tn.5 Agent Workspace Option Readiness For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-17

Batch ID: AHB-Tn.5

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `8cfe709e`

executionBaseHead: `8cfe709e`

closureBaseHead: `8cfe709e`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Prompt:

Implement AHB-Tn.5 as bounded agent-workspace option readiness. Create a
stable option-readiness matrix, seed generated workspace state with three
parked future options, supersede the AHB-Tn.4 parked marker, update workspace
front doors and AHB roadmap, and close the AHB foundation roadmap as option
ready. Do not build workspace UI, runtime queues, provider routes, public-sync,
registry edits, or production/public readiness claims.

Execution mode: `WORKER_MAY_COMMIT`.

Reviewer: Codex self-review under governed gates.

## Purpose

Close the remaining AHB workspace candidate by making future choices explicit
and machine-visible instead of leaving "continue workspace" as an ambiguous
instruction.

## Scope / Target / Owner Boundary

Target: option-readiness matrix and generated active workspace state option
items.

Owner boundary: Codex owns dispatch, implementation, review, closure, material
commit, and later session-sync. This work order does not authorize a workspace
UI, runtime state table, queue processor, provider/live proof, public-sync,
registry edit, production readiness, or public readiness.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author bounded AHB-Tn.5 dispatch and closure packet |
| Implementer | Codex | Add option matrix, generated state items, and front-door pointers |
| Reviewer / closer | Codex | Run focused gates, close with bounded evidence, and commit material |
| Session-sync steward | Codex | Update session continuity after material closure |
| Operator | Human operator | Select a later option or redirect future foundation work |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex holds dispatcher, implementer, reviewer, closer, and session-sync roles across distinct phases |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=8cfe709e`; `executionBaseHead=8cfe709e`; `closureBaseHead=8cfe709e` |
| changedSetScope(phase) | material AHB-Tn.5 option-readiness changed set only; later session-sync changed set remains separate |
| traceScope(phase, actor) | one Codex Agent Operation Trace Block covers this material batch; session-sync trace is separate if state changes |
| commitOwner(phase) | Codex owns material commit; Codex owns separate session-sync commit after material closure |
| crossBatchIsolation | one-batch-per-clean-worktree; before status evidence records clean worktree at HEAD `8cfe709e` |
| nextMoveSurfaces | material batch records AHB-Tn.5 closure; separate session sync updates state/front-door/handoff next move |
| Closer designation | Codex is the designated closer for this single-agent/multi-role batch |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | Prepare explicit future workspace options without building workspace UI/runtime. |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Storage class | stable option matrix plus generated state source fragments; dated execution evidence |
| Handoff fields | generated option records map route, rolePattern, phase, baseHead, changedSetScope, traceScope, commitOwner, and nextMoveImpact back to AHB fields |
| State ownership | `CVF_SESSION/agent_workspace/state/` is the source of truth; `ACTIVE_AGENT_WORKSPACE_STATE.json` is generated; no runtime state table |
| Guard owner | `governance/compat/check_agent_workspace_state.py` and existing `governance/compat/check_agent_workspace_design.py` |
| Build boundary | runtime source: no; provider proof: no; public-sync: no; registry edits: no |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-17 complete AHB foundation roadmap and prepare options | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| AHB-Tn.4 predecessor | `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| Workspace state topology | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | ACTIVE_CONTRACT |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_2026-06-17.md` | CLOSURE_SATISFIED |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reference/agent_workspace/README.md` | Stable workspace front door |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Workspace design control block source |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Required state fields and storage topology |
| `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | Generated active workspace state |
| `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Ratified handoff Central Core |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Workspace state aggregate exists | `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | root keys | `items` | workspace state aggregate schema | ACCEPT |
| Workspace source items are canonical source | `governance/compat/generate_agent_workspace_state.py` | constants | `ITEMS_DIR` | `load_source_items` | ACCEPT |
| Allowed parked status exists | `governance/compat/generate_agent_workspace_state.py` | `STATUS_VALUES` | `PARKED_PENDING_OPERATOR_DECISION` | `_validate_item` | ACCEPT |
| Closed bounded status exists | `governance/compat/generate_agent_workspace_state.py` | `STATUS_VALUES` | `CLOSED_PASS_BOUNDED` | `_validate_item` | ACCEPT |
| Workspace design standard requires control block | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Work Order Requirement | `Agent Workspace Design Control Block` | workspace design standard | ACCEPT |
| Topology contract defines parked lane | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Lane Topology | `Parked lane` | workspace state topology contract | ACCEPT |

## New Doc-Only Fields

| Field or label | Scope | Disposition |
|---|---|---|
| `OPTION_READY_PARKED` | option matrix readiness label only | DOC_ONLY_NEW |
| `AHB-Tn.5-A` / `AHB-Tn.5-B` / `AHB-Tn.5-C` | option IDs in stable matrix | DOC_ONLY_NEW |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Stable foundation folder | `docs/reference/agent_workspace/` remains the reference front door |
| Stable matrix | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md` |
| Generated state folder | `CVF_SESSION/agent_workspace/` contains generated active workspace state only |
| Source folder | `CVF_SESSION/agent_workspace/state/` owns source fragments |
| Dated execution evidence | GC-018, work order, and completion stay in normal dated folders |
| Archive policy | No archive movement in this batch; option items remain active until superseded by future committed decisions |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update generated workspace state option
items and stable workspace front doors so future AHB work starts from explicit
option choices instead of ambiguous continuation prose.

Protected paths:

- `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn5-richer-state-lanes-option-parked.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn5-foundation-hardening-option-parked.json`

Operator authorization: operator instructed Codex on 2026-06-17 to continue
and complete AHB foundation tranches and build readiness options.

Rollback boundary: revert only AHB-Tn.5 option-readiness matrix, generated
state item changes, front-door pointers, roadmap update, and matching evidence
if this batch is rejected. Do not alter prior AHB closures.

## Pre-Flight Checks

| Check | Command |
|---|---|
| Generate/check workspace state | `python governance/compat/generate_agent_workspace_state.py --check` |
| Workspace state guard | `python governance/compat/check_agent_workspace_state.py --base 8cfe709e --head HEAD --enforce` |
| Focused tests | `python -m pytest governance/compat/test_agent_workspace_state.py governance/compat/test_check_agent_workspace_design.py -q` |
| Governance gates | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 8cfe709e --head HEAD` after material commit |

## Write Ownership

| Path family | Owner | Boundary |
|---|---|---|
| Workspace generated state | Codex | generated aggregate and source item updates only |
| Stable workspace references | Codex | option matrix and pointer updates only |
| Runtime/product/public/registry paths | N/A | forbidden in this batch |

## Execution Plan

| Step | Action |
|---|---|
| 1 | Add stable option-readiness matrix |
| 2 | Add three parked option items and supersede the AHB-Tn.4 parked marker |
| 3 | Regenerate active workspace state aggregate |
| 4 | Update workspace front doors and AHB roadmap |
| 5 | Run focused tests and governance gates |
| 6 | Commit material, then session-sync separately |

## Evidence Requirements

| Requirement | Evidence source | Required disposition |
|---|---|---|
| Option matrix is stable and indexed | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/README.md` | PASS |
| Generated state source layout remains authoritative | `CVF_SESSION/agent_workspace/state/items/` and generated aggregate check | PASS |
| Three future options are explicit and parked | AHB-Tn.5 option source items and aggregate | PASS |
| Prior AHB-Tn.4 parked marker is superseded | `ahb-tn4-workspace-state-foundation-parked.json` | PASS |
| No runtime/provider/public/registry build claim | changed-set evidence and claim boundary | PASS |

## Acceptance Criteria

| Criterion | Closure evidence | Disposition |
|---|---|---|
| AHB foundation roadmap is option-ready | roadmap status and AHB-Tn.5 row closed bounded | PASS |
| Future workspace work requires operator selection | option matrix selection rules and parked state items | PASS |
| Future work remains gated by fresh GC-018 | option matrix and work-order claim boundary | PASS |
| Central Core + Local View is preserved | workspace front door, topology contract, option matrix, and generated state | PASS |
| No workspace build is performed | absence of runtime/UI/provider/public/registry paths in changed set | PASS |

## Review Gate

| Gate | Command or artifact | Disposition |
|---|---|---|
| Workspace state generator | `python governance/compat/generate_agent_workspace_state.py --check` | REQUIRED |
| Workspace state checker | `python governance/compat/check_agent_workspace_state.py --base 8cfe709e --head HEAD --enforce` | REQUIRED |
| Workspace design checker | `python governance/compat/check_agent_workspace_design.py --base 8cfe709e --head HEAD --enforce` | REQUIRED |
| Handoff boundary checker | `python governance/compat/check_agent_handoff_boundary.py --base 8cfe709e --head HEAD --enforce` | REQUIRED |
| AOT checker | `python governance/compat/check_agent_operation_trace.py --base 8cfe709e --head HEAD --enforce` | REQUIRED |
| Focused tests | `python -m pytest governance/compat/test_agent_workspace_state.py governance/compat/test_check_agent_workspace_design.py -q` | REQUIRED |

## Closure Checklist

| Item | Status |
|---|---|
| Stable option matrix added under the workspace reference folder | DONE |
| Workspace front door and operational index point to the option matrix | DONE |
| Three option items are present in generated workspace state | DONE |
| AHB-Tn.4 parked marker is superseded | DONE |
| AHB roadmap records AHB-Tn.5 closure and option-ready boundary | DONE |
| Runtime, provider, public-sync, and registry paths remain out of scope | DONE |

## Return-To-Orchestrator Conditions

| Condition | Return action |
|---|---|
| Any required gate fails inside allowed scope | repair within AHB-Tn.5 and rerun |
| A future option must be selected or built | return to operator; fresh GC-018 required |
| Runtime/provider/public/registry work becomes necessary | stop and open separate authorized batch |
| Generated aggregate drifts from source items | regenerate from source and rerun drift check |

## Operator Checkpoint

Operator checkpoint after closure: choose one future option from the matrix, or
leave all AHB workspace options parked. AHB-Tn.5 does not itself authorize any
workspace build, richer state lane implementation, runtime mutation, provider
proof, public-sync, or registry edit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_FOR_CODEX_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Option matrix | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md` | stable matrix | PASS |
| Generated aggregate | `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | source-generated | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-Tn.5 row `CLOSED_PASS_BOUNDED` | PASS |
| Runtime workspace build | N/A with reason: no workspace build authorized | N/A | N/A with reason |
| Registry JSON | BLOCKED with reason: no registry edit authorized for this option-readiness batch | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized for this option-readiness batch | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof | N/A | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately if next move changes | N/A | N/A with reason |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RULE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `OPTION_READINESS_MATRIX_ADDED`; `GENERATED_STATE_OPTIONS_ADDED` |
| Next control action | Future operator-selected option requires fresh GC-018 and source-verified work order |
| Worker blame | `N/A_WITH_REASON`: AHB-Tn.5 removes ambiguous next-work routing from the workspace foundation |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: AHB-Tn.5 changes governed markdown and
session workspace JSON only. It does not edit CVF product runtime routes,
provider adapters, model registries, hardcoded provider selection, public-sync
content, or live-governance behavior. Model Gateway `provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY` are out-of-scope and untouched.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.5 agent workspace option readiness |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-richer-state-lanes-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-foundation-hardening-option-parked.json`; `docs/baselines/CVF_GC018_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_FOR_CODEX_2026-06-17.md` |
| Allowed scope source | operator authorization to complete AHB foundation roadmap on 2026-06-17 |
| Before status evidence | HEAD `8cfe709e`; clean worktree |
| After status evidence | AHB-Tn.5 material closure pending commit |
| Diff evidence | `git diff --name-status 8cfe709e..HEAD` |
| Approval boundary | option-readiness foundation only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn5-agent-workspace-option-readiness-2026-06-17` |
| Expected manifest | `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-richer-state-lanes-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-foundation-hardening-option-parked.json`; `docs/baselines/CVF_GC018_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_FOR_CODEX_2026-06-17.md` |
| Actual changed set | `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-richer-state-lanes-option-parked.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn5-foundation-hardening-option-parked.json`; `docs/baselines/CVF_GC018_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_2026-06-17.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN5_AGENT_WORKSPACE_OPTION_READINESS_FOR_CODEX_2026-06-17.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order closes option readiness only. It does not select a future
option, build a workspace, mutate runtime/product code, run provider proof,
public-sync, edit registries, or claim production/public readiness.
