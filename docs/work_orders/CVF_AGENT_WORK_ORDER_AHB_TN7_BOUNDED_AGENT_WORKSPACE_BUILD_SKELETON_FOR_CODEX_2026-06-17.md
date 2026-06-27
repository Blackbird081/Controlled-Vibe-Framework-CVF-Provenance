# CVF Agent Work Order - AHB-Tn.7 Bounded Agent Workspace Build Skeleton For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-17

Batch ID: AHB-Tn.7

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `338c34e2`

executionBaseHead: `338c34e2`

closureBaseHead: `338c34e2`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Prompt:

Execute the remaining AHB-Tn.5-A option as a bounded local agent workspace
build skeleton. Create only the repo-local skeleton front door, lane index,
lane folder placeholders, generated workspace state disposition, skeleton
machine guard, hook/autorun binding, and closure evidence. Do not create
runtime queues, scheduler queues, UI, provider/live proof, public-sync,
registry edits, product runtime mutation, production readiness, or public
readiness.

Execution mode: `WORKER_MAY_COMMIT`.

Reviewer: Codex self-review under governed gates.

## Purpose

Close AHB-Tn.5-A at skeleton level so agents have a stable local workspace
surface before any runtime implementation is considered.

## Scope / Target / Owner Boundary

Target: `CVF_SESSION/agent_workspace/workspace/`, skeleton checker, generated
workspace state item disposition, and reference/front-door updates.

Owner boundary: Codex owns dispatch, implementation, review, closure, material
commit, and later session-sync. Runtime queues, scheduler queues, UI,
provider/live proof, public-sync, registry edits, product runtime mutation,
production readiness, and public readiness are forbidden in this batch.

## Write Ownership

Codex owns all files listed in the AHB-Tn.7 Agent Operation Trace Block for
this material batch. Session-sync files are not part of the material commit and
must be committed separately if next-move surfaces change.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author bounded AHB-Tn.7 packet |
| Implementer | Codex | Add local skeleton and checker |
| Reviewer / closer | Codex | Run focused gates, close evidence, and commit material |
| Session-sync steward | Codex | Update session continuity after material closure |
| Operator | Human operator | Later authorize runtime expansion or keep parked |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex holds dispatcher, implementer, reviewer, closer, and session-sync roles across distinct phases |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=338c34e2`; `executionBaseHead=338c34e2`; `closureBaseHead=338c34e2` |
| changedSetScope(phase) | material AHB-Tn.7 workspace skeleton changed set only; later session-sync changed set remains separate |
| traceScope(phase, actor) | one Codex Agent Operation Trace Block covers this material batch; session-sync trace is separate if state changes |
| commitOwner(phase) | Codex owns material commit; Codex owns separate session-sync commit after material closure |
| crossBatchIsolation | one-batch-per-clean-worktree; before status evidence records clean worktree at HEAD `338c34e2` |
| nextMoveSurfaces | material batch records AHB-Tn.7 closure; separate session sync updates state/front-door/handoff next move |
| Closer designation | Codex is the designated closer for this single-agent/multi-role batch |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | Bounded local skeleton for agent-to-agent workspace orientation before runtime exists. |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `docs/reference/agent_workspace/README.md`; local skeleton front door `CVF_SESSION/agent_workspace/workspace/README.md` |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Storage class | stable local skeleton files, generated workspace state source fragments, and dated execution evidence |
| Handoff fields | skeleton points back to AHB route, rolePattern, phase, baseHead, changed-set scope, trace, commit owner, and next-move surfaces through generated state and work order evidence |
| State ownership | `CVF_SESSION/agent_workspace/state/` owns active state; `CVF_SESSION/agent_workspace/workspace/` owns local skeleton orientation only |
| Guard owner | `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_workspace_skeleton.py`; existing state guard remains `governance/compat/check_agent_workspace_state.py` |
| Build boundary | runtime source: no; provider proof: no; public-sync: no; registry edits: no |

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-17 approve AHB-Tn.5-A bounded workspace build skeleton | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPTED |
| AHB-Tn.6 predecessor | `docs/reviews/CVF_AHB_TN6_AGENT_WORKSPACE_FOUNDATION_READINESS_BUNDLE_COMPLETION_2026-06-17.md` | PREDECESSOR_SATISFIED |
| Workspace option matrix | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md` | ACTIVE_MATRIX |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_2026-06-17.md` | CLOSURE_SATISFIED |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reference/agent_workspace/README.md` | Stable workspace front door |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | Required state fields and skeleton topology |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_LANE_TAXONOMY.md` | Required lane vocabulary |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md` | AHB-Tn.5-A parked option |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AHB-Tn.5-A is the bounded workspace build option | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPTION_READINESS_MATRIX.md` | `Option Matrix` | `AHB-Tn.5-A` | option-readiness matrix | ACCEPT |
| Workspace state source items are canonical source | `governance/compat/generate_agent_workspace_state.py` | `ITEMS_DIR` | `ITEMS_DIR` | `load_source_items` | ACCEPT |
| Lane values are canonical | `governance/compat/generate_agent_workspace_state.py` | `LANE_VALUES` | `LANE_VALUES` | `_validate_item` | ACCEPT |
| Skeleton checker owns skeleton root | `governance/compat/check_agent_workspace_skeleton.py` | `SKELETON_ROOT` | `SKELETON_ROOT` | `run_check` | ACCEPT |
| Skeleton checker owns lane list | `governance/compat/check_agent_workspace_skeleton.py` | `LANES` | `LANES` | `_validate_paths` | ACCEPT |
| Workspace design guard remains active | `governance/compat/check_agent_workspace_design.py` | `CONTROL_BLOCK` | `CONTROL_BLOCK` | workspace design gate | ACCEPT |
| Workspace state guard remains active | `governance/compat/check_agent_workspace_state.py` | `STATE_PATH`; `THIS_SCRIPT_PATH` | `STATE_PATH` | workspace state gate | ACCEPT |

## New Doc-Only Fields

| Field or label | Scope | Disposition |
|---|---|---|
| `ACTIVE_SKELETON` | local skeleton README status | DOC_ONLY_NEW |
| `CLOSED_BY_AHB_TN7` | option matrix readiness label | DOC_ONLY_NEW |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Stable foundation folder | `docs/reference/agent_workspace/` remains the canonical reference front door |
| Local skeleton folder | `CVF_SESSION/agent_workspace/workspace/` owns local skeleton orientation |
| Lane folder index | `CVF_SESSION/agent_workspace/workspace/lanes/README.md` |
| Generated state folder | `CVF_SESSION/agent_workspace/` contains generated active workspace state |
| Source folder | `CVF_SESSION/agent_workspace/state/` owns source fragments |
| Dated execution evidence | GC-018, work order, and completion stay in normal dated folders |
| Archive policy | No archive movement in this batch; closed skeleton items stay active until future archive cleanup |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add skeleton checker, hook/autorun binding,
stable workspace skeleton, and generated workspace state item disposition so
future workspace work starts from an indexed local surface.

Protected paths:

- `.gitignore`
- `AGENTS.md`
- `CVF_SESSION/agent_workspace/ACTIVE_AGENT_WORKSPACE_STATE.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn5-workspace-build-option-parked.json`
- `CVF_SESSION/agent_workspace/state/items/ahb-tn7-bounded-workspace-build-skeleton-closed.json`
- `CVF_SESSION/agent_workspace/workspace/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/intake/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/dispatch/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/execution/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/worker_return/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/review/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/accepted_material/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/session_sync/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/parked/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/blocked/README.md`
- `CVF_SESSION/agent_workspace/workspace/lanes/archive_ready/README.md`
- `governance/compat/check_agent_operation_trace.py`
- `governance/compat/check_agent_workspace_skeleton.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/test_agent_workspace_skeleton.py`

Operator authorization: operator instructed Codex on 2026-06-17 to execute
AHB-Tn.5-A after agreeing with the bounded skeleton approach.

Rollback boundary: revert only AHB-Tn.7 skeleton changes if this batch is
rejected. Do not alter prior AHB closures.

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: AHB-Tn.7 changes governed markdown,
generated workspace JSON, local skeleton files, and governance checker/test
code only. It does not edit product runtime routes, provider adapters, model
registries, hardcoded provider selection, public-sync content, or
live-governance behavior. Specifically,
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY` are out of scope and untouched.

## Acceptance Criteria

- Local skeleton README exists under `CVF_SESSION/agent_workspace/workspace/`.
- Lane index exists and names all canonical lane folders.
- Skeleton checker and tests exist.
- Autorun and local hook chains run the skeleton checker.
- Generated workspace state marks AHB-Tn.5-A closed by AHB-Tn.7 and adds the
  AHB-Tn.7 accepted-material item.
- Roadmap and option matrix show AHB-Tn.7 closure at skeleton level.
- No runtime/provider/live/public/registry/product-readiness claim is made.

## Execution Plan

1. Add the local skeleton front door and lane index.
2. Add canonical lane folder placeholders.
3. Add skeleton checker and focused tests.
4. Bind the skeleton checker into autorun and local hook chains.
5. Update generated workspace state source fragments and regenerate the
   aggregate.
6. Update reference front doors, option matrix, roadmap, and closure evidence.
7. Run focused checks, steward preflight, local pre-commit chain, and
   pre-closure after commit.

## Evidence Requirements

Evidence must include:

- generated workspace state drift check;
- skeleton checker pass;
- workspace state checker pass;
- focused pytest pass;
- local pre-commit hook chain pass;
- committed material diff over `338c34e2..HEAD`;
- separate session-sync if next-move surfaces change.

## Review Gate

Codex must review the actual changed files and gate output before material
commit. Acceptance is blocked by any checker failure inside allowed scope.

## Closure Checklist

- [x] Dispatch prompt envelope present near top of work order.
- [x] Source Verification Block uses existing sources or doc-only declarations.
- [x] Agent Handoff Contract Control Block present.
- [x] Agent Workspace Design Control Block present.
- [x] Foundation Storage Layout Block present.
- [x] Machine Closure Package present.
- [x] Public Export Disposition present.
- [x] Runtime/provider/live/public/registry/product-readiness claims excluded.

## Return-To-Orchestrator Conditions

Allowed-scope machine-gate failures must be repaired and rerun by Codex before
closure. Return to orchestrator only if a required repair would exceed allowed
scope, touch runtime/product/provider/public/registry surfaces, consume
secrets/quota, or change the claim boundary.

## Operator Checkpoint

No operator checkpoint remains inside AHB-Tn.7 allowed scope. Future runtime
expansion requires fresh operator authorization, GC-018, and source-verified
work order.

## Claim Boundary

Final claim is limited to a bounded local workspace skeleton and machine guard.
Verification does not prove runtime behavior, live governance behavior, public
surface readiness, provider routing, registry readiness, or production
readiness.

## Pre-Flight Checks

| Check | Command |
|---|---|
| Generate/check workspace state | `python governance/compat/generate_agent_workspace_state.py --check` |
| Workspace skeleton guard | `python governance/compat/check_agent_workspace_skeleton.py --base 338c34e2 --head HEAD --enforce` |
| Workspace state guard | `python governance/compat/check_agent_workspace_state.py --base 338c34e2 --head HEAD --enforce` |
| Focused tests | `python -m pytest governance/compat/test_agent_workspace_skeleton.py governance/compat/test_agent_workspace_state.py governance/compat/test_check_agent_workspace_design.py -q` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance workspace skeleton. No public-sync batch is
authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_FOR_CODEX_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | `Status: ROADMAP_CLOSED_PASS_BOUNDED_SKELETON_READY_PRE_RUNTIME` | PASS |
| Completion review | `docs/reviews/CVF_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_COMPLETION_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_TN7_BOUNDED_AGENT_WORKSPACE_BUILD_SKELETON_2026-06-17.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Local skeleton | `CVF_SESSION/agent_workspace/workspace/README.md` | `Status: ACTIVE_SKELETON` | PASS |
| Skeleton checker | `governance/compat/check_agent_workspace_skeleton.py` | `SKELETON_ROOT` | PASS |
| Registry JSON | BLOCKED with reason: no registry JSON edit authorized for this skeleton closure | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized for this skeleton closure | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof authorized | N/A | N/A with reason |
| System loop interlock | N/A with reason: no interlock registry edit authorized | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately if next move changes | N/A | N/A with reason |
| Runtime implementation | N/A with reason: no runtime implementation authorized | N/A | N/A with reason |
| Provider/live proof | N/A with reason: no provider/live proof authorized | N/A | N/A with reason |
| Public-sync | N/A with reason: private provenance foundation only | N/A | N/A with reason |
| Registry edit | N/A with reason: no registry edit authorized | N/A | N/A with reason |

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
