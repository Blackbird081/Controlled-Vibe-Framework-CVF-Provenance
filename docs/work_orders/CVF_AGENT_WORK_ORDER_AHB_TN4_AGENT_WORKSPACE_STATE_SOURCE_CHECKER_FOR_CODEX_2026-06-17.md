# CVF Agent Work Order - AHB-Tn.4 Agent Workspace State Source Checker For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-17

Batch ID: AHB-Tn.4

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `f8964c7a`

executionBaseHead: `f8964c7a`

closureBaseHead: `f8964c7a`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Prompt:

Implement AHB-Tn.4 as bounded generated workspace state source/checker
foundation. Create the generated aggregate
`CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`, source
fragments under `CVF_SESSION/agent_workspace/state/`, generator
`governance/compat/generate_agent_workspace_state.py`, checker
`governance/compat/check_agent_workspace_state.py`, focused tests, autorun and
local-hook binding, and stable front-door pointers. Do not build workspace UI,
runtime queues, provider routes, public-sync, registry edits, or production
readiness claims.

Execution mode: `WORKER_MAY_COMMIT`.

Reviewer: Codex self-review under governed gates.

## Purpose

Close AHB-Tn.4 by converting the AHB-Tn.3 generated-state candidate into a
source-generated, machine-checked workspace state foundation.

## Scope / Target / Owner Boundary

Target: generated workspace state foundation and drift/topology enforcement.

Owner boundary: Codex owns dispatch, implementation, review, closure, material
commit, and later session-sync. This work order does not authorize a workspace
UI, runtime state table, queue processor, provider/live proof, public-sync,
registry edit, production readiness, or public readiness.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author bounded AHB-Tn.4 dispatch and closure packet |
| Implementer | Codex | Add generated state sources, aggregate, generator, checker, tests, and hook bindings |
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
| baseHeadFor(phase) | `dispatchBaseHead=f8964c7a`; `executionBaseHead=f8964c7a`; `closureBaseHead=f8964c7a` |
| changedSetScope(phase) | material AHB-Tn.4 generated workspace state source/checker changed set only; later session-sync changed set remains separate |
| traceScope(phase, actor) | one Codex Agent Operation Trace Block covers this material batch; session-sync trace is separate if state changes |
| commitOwner(phase) | Codex owns material commit; Codex owns separate session-sync commit after material closure |
| crossBatchIsolation | one-batch-per-clean-worktree; before status evidence records clean worktree at HEAD `f8964c7a` |
| nextMoveSurfaces | material batch records AHB-Tn.4 closure; separate session sync updates state/front-door/handoff next move |
| Closer designation | Codex is the designated closer for this single-agent/multi-role batch |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | Create source-generated active workspace state foundation without building workspace UI/runtime. |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Storage class | generated state aggregate plus generated source fragments; stable foundation references; dated execution evidence |
| Handoff fields | generated item records map route, rolePattern, phase, baseHead, changedSetScope, traceScope, commitOwner, cross-batch boundary, and nextMoveImpact back to AHB fields |
| State ownership | `CVF_SESSION/agent_workspace/state/` is the source of truth; `ACTIVE_AGENT_WORKSPACE_STATE.json` is generated; no runtime state table |
| Guard owner | `governance/compat/check_agent_workspace_state.py` and existing `governance/compat/check_agent_workspace_design.py` |
| Build boundary | runtime source: no; provider proof: no; public-sync: no; registry edits: no |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-17 continue workspace foundation hardening | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| AHB-Tn.3 predecessor | `docs/reviews/CVF_AHB_TN3_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| Workspace state topology | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | ACTIVE_CONTRACT |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md` | CLOSURE_SATISFIED |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reference/agent_workspace/README.md` | Stable workspace front door |
| `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` | Workspace design control block source |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Required state fields and storage topology |
| `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | Generated source layout discipline |
| `docs/reference/foundation_storage/README.md` | Stable folder/index rule |
| `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Ratified handoff Central Core |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Stable foundation folder | `docs/reference/agent_workspace/` remains the reference front door |
| Generated state folder | `CVF_SESSION/agent_workspace/` contains generated active workspace state only |
| Source folder | `CVF_SESSION/agent_workspace/state/` owns source fragments |
| Dated execution evidence | GC-018, work order, and completion stay in normal dated folders |
| Index/front door updates | AGENTS, workspace README, JSON generated aggregate standard, operational index, and roadmap updated |
| Archive policy | No archive movement in this batch; future active workspace state compaction requires separate authorization |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add generated workspace state foundation,
generator, checker, tests, and hook binding so future workspace state changes
are source-generated and machine-checked before dispatch, closure, commit, or
push.

Protected paths:

- `AGENTS.md`
- `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`
- `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`
- `governance/compat/check_agent_workspace_state.py`
- `governance/compat/generate_agent_workspace_state.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_agent_commit_steward_preflight.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/test_agent_workspace_state.py`
- `governance/compat/test_run_agent_commit_steward_preflight.py`

Operator authorization: operator instructed Codex to continue workspace
foundation hardening on 2026-06-17.

Rollback boundary: revert only AHB-Tn.4 generated workspace state foundation,
checker/generator/tests, hook binding, pointers, roadmap update, and matching
evidence if this batch is rejected. Do not alter prior AHB closures.

## Pre-Flight Checks

| Check | Command |
|---|---|
| Generate/check workspace state | `python governance/compat/generate_agent_workspace_state.py --check` |
| Workspace state guard | `python governance/compat/check_agent_workspace_state.py --base f8964c7a --head HEAD --enforce` |
| Focused tests | `python -m pytest governance/compat/test_agent_workspace_state.py governance/compat/test_check_agent_workspace_design.py -q` |
| Governance gates | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base f8964c7a --head HEAD` after material commit |

## Write Ownership

| Path family | Owner | Boundary |
|---|---|---|
| Workspace generated state | Codex | generated aggregate and source fragments only |
| Governance checker scripts/tests | Codex | additive checker/generator/test only |
| Stable front doors | Codex | pointer updates only |
| Runtime/product/public/registry paths | N/A | forbidden in this batch |

## Execution Plan

| Step | Action |
|---|---|
| 1 | Create generated workspace state source layout and aggregate |
| 2 | Add deterministic generator and drift/topology checker |
| 3 | Add focused tests for generation, drift, and canonical item validation |
| 4 | Bind checker into autorun and local hook chains |
| 5 | Update AGENTS and stable front doors |
| 6 | Run focused tests and governance gates |
| 7 | Commit material, then session-sync separately |

## Evidence Requirements

| Evidence | Required disposition |
|---|---|
| Generated aggregate drift check | PASS |
| Workspace state checker | PASS |
| Focused tests | PASS |
| AOT exact manifest | MATCH |
| Machine closure package | PASS |
| No workspace build | explicit N/A with reason |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Generated aggregate | `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | source-generated | PASS |
| Generated source layout | `CVF_SESSION/agent_workspace/state/` | source core and item | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-Tn.4 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no GC-051 registry edit authorized for this workspace-state foundation batch | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized for this workspace-state foundation batch | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof | N/A | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately if next move changes | N/A | N/A with reason |

## Review Gate

Codex must self-review the actual diff, not rely on the intended design. The
review must verify generated aggregate drift, hook binding, source/front-door
markers, no runtime/provider/public/registry changes, and no unchecked closure
residue.

## Closure Checklist

- [x] GC-018 and work order created.
- [x] Generated state source layout created.
- [x] Generator/checker/tests added.
- [x] Autorun and local hook chain bindings added.
- [x] Stable front doors updated.
- [x] Completion review records bounded claim.
- [x] Session-sync remains separate from material commit.

## Return-To-Orchestrator Conditions

Return to operator only if the work requires runtime/product mutation,
provider/live proof, public-sync, registry edit, destructive filesystem action,
or broad workspace build beyond generated-state foundation.

## Operator Checkpoint

No checkpoint is required inside this bounded tranche. The next operator
checkpoint is whether to authorize AHB-Tn.5 workspace build, richer state lanes,
or another foundation tranche after AHB-Tn.4 closure.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Future generated-state candidate layout | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | `## Storage Topology` | `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` | workspace topology contract | ACCEPT |
| Required workspace state fields | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | `## Required State Fields` | `workspaceItemId` and peer fields | workspace topology contract | ACCEPT |
| Generated aggregate discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | `## Rule` | generator/checker/source layout pattern | generated aggregate standard | ACCEPT |
| Active session generator pattern | `governance/compat/generate_active_session_state.py` | functions `load_source_state`, `generate_aggregate`, `validate_aggregate_matches_sources` | generated source layout | generator pattern | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Disposition |
|---|---|---|
| `ACTIVE_AGENT_WORKSPACE_STATE.json` | generated workspace state aggregate path introduced by this batch | DOC_ONLY_NEW |
| `workspaceItemId` | stable workspace item identifier required by topology contract | DOC_ONLY_NEW |
| `itemKind` | bounded workspace state unit class required by topology contract | DOC_ONLY_NEW |
| `nextMoveImpact` | workspace item field that records next-move effect | DOC_ONLY_NEW |

## Generated Aggregate Discipline

Disposition: `GENERATED_SOURCE_LAYOUT_ADDED`.

Agents must edit `CVF_SESSION/agent_workspace/state/` and run
`governance/compat/generate_agent_workspace_state.py --generate`. Aggregate-only
edits to `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json` are
drift defects.

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: AHB-Tn.4 changes governed markdown,
session workspace JSON, and governance checker scripts only. It does not edit
CVF product runtime routes, provider adapters, model registries, hardcoded
provider selection, public-sync content, or live-governance behavior. Model
Gateway `provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are
out-of-scope and untouched.

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| State source layout exists | source core and item JSON paths committed |
| Aggregate generated from sources | `generate_agent_workspace_state.py --check` PASS |
| Drift/topology checker works | checker PASS and focused tests PASS |
| Guard is mandatory | autorun and local hook chain invoke checker |
| Stable front doors updated | AGENTS, workspace README, design standard, topology contract, JSON standard, operational index updated |
| Closure boundary retained | no workspace build/runtime/provider/public/registry claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-17 AHB-Tn.4 agent workspace state source checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, pytest |
| Target paths | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_state.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Allowed scope source | this work order and operator authorization |
| Before status evidence | HEAD `f8964c7a`; clean worktree |
| After status evidence | AHB-Tn.4 material closure pending commit |
| Diff evidence | `git diff --name-status f8964c7a..HEAD` |
| Approval boundary | generated workspace state source/checker foundation only |
| Claim boundary | no workspace build, runtime/provider/live/public/registry implementation claim |
| Agent type | Codex implementer/closer |
| Invocation ID | `ahb-tn4-agent-workspace-state-source-checker-2026-06-17` |
| Expected manifest | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_state.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Actual changed set | `AGENTS.md`; `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`; `CVF_SESSION/agent_workspace/state/ACTIVE_AGENT_WORKSPACE_STATE_CORE.json`; `CVF_SESSION/agent_workspace/state/items/ahb-tn4-workspace-state-foundation-parked.json`; `docs/baselines/CVF_GC018_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_2026-06-17.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`; `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`; `docs/reviews/CVF_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_COMPLETION_2026-06-17.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN4_AGENT_WORKSPACE_STATE_SOURCE_CHECKER_FOR_CODEX_2026-06-17.md`; `governance/compat/check_agent_workspace_state.py`; `governance/compat/generate_agent_workspace_state.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/test_agent_workspace_state.py`; `governance/compat/test_run_agent_commit_steward_preflight.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance foundation. No public-sync batch is
authorized.

## Claim Boundary

This work order closes generated workspace state source/checker foundation
only. It does not implement the agent-interaction workspace, runtime queues,
provider calls, public-sync, registry edits, autonomous mutation, or
production/public readiness.
