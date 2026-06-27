# CVF Agent Work Order - LWPRM-T0-T4 Local Workspace Projection Read Model Foundation

Memory class: WORK_ORDER

Status: CLOSED_PASS_BOUNDED

Owner: Codex

Base head: `fa3c25e5`

## Dispatch Prompt Envelope

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_FOR_CODEX_2026-06-27.md`

dispatchBaseHead: `fa3c25e5`

executionBaseHead: `fa3c25e5`

closureBaseHead: `fa3c25e5`

workerCommitMode: `CODEX_MAY_COMMIT_AFTER_GATES`

mission: Execute the decision-first Local Workspace Projection Read Model
foundation batch T0 through T4 without runtime, provider, public-sync, adapter,
resolver, package activation, certification, generated workspace state, or
DICE scope.

## Purpose

Define and close a bounded `READ_MODEL_ONLY` foundation tranche for the local
workspace projection read model.

## 1. Mission

Create and close the bounded local workspace projection read-model foundation
batch. Success means the repository contains a source-verified CVF-owned
read-model decision reference and front-door pointer, with closure evidence and
governance gates.

## 2. Authority Chain

- Operator instruction: continue after WLFA-T0-T4 and prioritize CVF foundation
  over DICE.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V23_2026-06-26.md`.
- Handoff contract: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.
- Roadmap: `docs/roadmaps/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_ROADMAP_2026-06-27.md`.
- GC-018: `docs/baselines/CVF_GC018_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_2026-06-27.md`.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | author authority packet |
| Worker | Codex | execute bounded markdown/reference edits |
| Reviewer | Codex | review changed set against work order |
| Closer | Codex | commit material after gates |
| Session-sync steward | Codex | update session surfaces in a separate commit |

## Required First Reads

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |

## Pre-Flight Checks

| Command | Expected result |
|---|---|
| `git status --short` | clean before material edits |
| `git rev-parse --short HEAD` | `fa3c25e5` before material edits |
| `python governance/compat/run_adif_defect_resolver.py --query "taskClass=workspace_projection_read_model role=dispatcher lifecyclePhase=dispatch"` | no returned defect IDs |

## Write Ownership

Allowed material paths:

- `docs/roadmaps/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_ROADMAP_2026-06-27.md`
- `docs/baselines/CVF_GC018_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_2026-06-27.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_FOR_CODEX_2026-06-27.md`
- `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md`
- `docs/reference/agent_workspace/README.md`
- `docs/reviews/CVF_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_COMPLETION_2026-06-27.md`

## Execution Plan

| Step | Action |
|---|---|
| T0 | Author authority artifacts |
| T1 | Source-verify CVF-owned workspace surfaces and retained package inventory |
| T2 | Add stable read-model decision reference |
| T3 | Update workspace front-door discovery |
| T4 | Run gates and commit material |

## Evidence Requirements

- Source Verification Block must cite existing CVF-owned source paths.
- Runtime Expansion Control Block must state `READ_MODEL_ONLY`.
- Agent Operation Trace Block must list the exact material manifest.
- Machine Closure Package must include required rows.
- Session-sync must be separate from material commit.

## 3. Allowed Scope

- Add the roadmap, GC-018, work order, stable read-model decision reference,
  workspace front-door pointer, and completion review named in this packet.
- Run source-verification and governance gates.
- Commit material after gates pass.
- Perform separate session-sync only after material commit succeeds.

## 4. Forbidden Scope

- Runtime queue execution.
- MCP, CLI, or IDE bridge implementation.
- CVF Web source or UI implementation.
- Provider/live proof.
- Public-sync or push.
- Generated workspace state mutation.
- Resolver or adapter mutation.
- Package activation, package import, package instance creation, or package certification.
- DICE work.
- Mixing material commit with session-sync commit.

## Source Inventory

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | READ |
| `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | READ |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | SOURCE_VERIFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Next allowed move is Local Workspace Projection Read Model decision-first | `CVF_SESSION_MEMORY.md` | Startup Acknowledgment; Next Allowed Move | `workspace_layer_full_package_absorption_closed_pass_bounded_pending_projection_read_model_decision` | active session front door | ACCEPT |
| Package absorption inventory recommends this follow-on | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | line 163 | `Next-Roadmap Recommendation` | package absorption inventory | ACCEPT |
| Package projection vocabulary is already mapped as advisory input | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | Useful Patterns; CVF Mapping | `workspace_state.json`; `workflow_state.json`; `governance_state.json`; `agent_state.json`; `evidence_state.json` | package absorption map | ACCEPT |
| Package projection contract exists in retained inventory | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | line 82 | `STATE_PROJECTION_CONTRACT.md` | package absorption inventory | ACCEPT |
| CVF topology owns required workspace-state fields | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | lines 81-106 | Required State Fields | workspace state topology contract | ACCEPT |
| Operator view plan defines read-model sections | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | lines 37-51 | Read Model Sections | operator view plan | ACCEPT |
| Runtime expansion contract accepts `READ_MODEL_ONLY` | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | lines 60-73 | `runtimeMode`; `READ_MODEL_ONLY` | runtime expansion readiness contract | ACCEPT |
| Work order template requires source verification before implementation | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Enforcement / Verification | Source Verification Block | work order template | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`workspace_projection_read_model`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Roadmap-To-Work-Order Trace Matrix

| Roadmap item | Work order task | Evidence |
|---|---|---|
| T0 decision and authority | author roadmap, GC-018, work order | dispatch artifacts |
| T1 source mapping | source verification rows | source anchors |
| T2 stable reference | add read-model decision | reference file |
| T3 front-door pointer | update workspace README | README pointer |
| T4 closure | completion review and gates | completion review |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| routeToken | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | codex_dispatch_implementation_review_closure_session_sync |
| contractSource | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| baseHeadFor(phase) | dispatch=`fa3c25e5`; execution=`fa3c25e5`; closure=`fa3c25e5`; session-sync=material commit |
| changedSetScope(phase) | roadmap, GC-018, work order, reference, front door, completion review |
| traceScope(phase, actor) | Agent Operation Trace Block in roadmap, work order, reference, and completion review |
| commitOwner(phase) | Codex for material after gates; Codex for separate session-sync after material commit |
| crossBatchIsolation | material and session-sync commits must be separate |
| nextMoveSurfaces | update active session, front door, and active handoff only after material commit |

## Runtime Expansion Control Block

| Field | Disposition |
|---|---|
| runtimeMode | READ_MODEL_ONLY |
| contractSource | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| frontDoor | `docs/reference/agent_workspace/README.md` |
| stateSourceOfTruth | existing generated workspace state and active session state; no new aggregate in this batch |
| queueBoundary | N/A with reason: no queue record or executable behavior |
| operatorViewBoundary | read-model decision only; no UI implementation |
| providerBoundary | no-provider |
| publicBoundary | private-only |
| guardOwner | existing workspace design/runtime boundary guards |

## Workspace Two-Layer Control Block

| Field | Disposition |
|---|---|
| targetLayer | BOTH_WITH_BOUNDARY |
| operatorSurface | read-only projection sections only |
| agentExecutionSurface | local projection vocabulary only |
| sourceOfTruth | CVF state, handoff, work order, review, receipt, and guard evidence |
| mutationBoundary | no mutation |
| receiptBoundary | governance gate and completion evidence only |
| forbiddenConflationCheck | Web read model and Local Workspace Runtime are not merged |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | local projection read model for future operator and agent surfaces |
| Contract source | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | stable reference file under `docs/reference/agent_workspace/` |
| Handoff fields | active session and AHB fields remain source of truth |
| State ownership | no generated workspace state mutation in this batch |
| Guard owner | `governance/compat/check_agent_workspace_design.py` |
| Build boundary | reference decision only; no workspace build, runtime source, provider proof, public-sync, registry edits, or runtime implementation |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| stableFoundationPath | `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` |
| datedEvidencePaths | roadmap, GC-018, work order, and completion review |
| indexOrFrontDoor | `docs/reference/agent_workspace/README.md` |
| storageDecision | stable reference is not date-suffixed; evidence artifacts are date-suffixed |
| archivePolicy | future replacement requires governed archive/supersession batch |
| claimBoundary | no raw package import, runtime queue, MCP, CLI, IDE bridge, provider, public-sync, or generated workspace state mutation |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | workspace reference surface | internal agents may cite the reference for future dispatch/review | this work order and reference | N/A with reason: no adapter created | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP projection adapter owner deferred | no executable external-agent support | runtime expansion contract | deferred adapter owner; fresh GC-018 required | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | root/folder lifecycle classification plus absorption map when retained |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_foundation_storage_layout.py` |
| Owner surface | `docs/reference/agent_workspace/` |
| Disposition | ADAPT package projection vocabulary into CVF read-model reference |
| Claim boundary | no raw package authority, runtime, MCP, CLI, IDE bridge, provider, public-sync, generated workspace state mutation, or readiness claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | LWPRM-T0-T4 work order execution |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: source verification and gate output |
| actionEvidence | ACTION_EVIDENCE_PRESENT: material changed-set and completion review |
| invocationBoundary | local source reads and governed markdown edits only |
| interceptionBoundary | no runtime interception or provider route changed |
| claimLanguage | read-model foundation only |
| forbiddenExpansion | no runtime, MCP, CLI, IDE bridge, provider/live proof, public-sync, generated workspace state mutation, resolver mutation, adapter mutation, package activation, certification decision, or DICE work |

## Current Runtime Freshness Verification

| Runtime claim | Current evidence | Disposition |
|---|---|---|
| Runtime implementation | no runtime path is in Write Ownership | NOT_IMPLEMENTED_WITH_REASON |
| MCP or CLI adapter | no MCP or CLI adapter path is in Write Ownership | NOT_IMPLEMENTED_WITH_REASON |
| Provider/live proof | no provider/live command is authorized or run | NOT_IMPLEMENTED_WITH_REASON |
| Generated workspace state mutation | generated workspace state is outside Allowed Scope | NOT_IMPLEMENTED_WITH_REASON |

## Planned Artifact Manifest

| Path | Purpose |
|---|---|
| `docs/roadmaps/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_ROADMAP_2026-06-27.md` | roadmap |
| `docs/baselines/CVF_GC018_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_2026-06-27.md` | baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_FOR_CODEX_2026-06-27.md` | work order |
| `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` | stable reference |
| `docs/reference/agent_workspace/README.md` | front-door pointer |
| `docs/reviews/CVF_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_COMPLETION_2026-06-27.md` | completion review |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Source-verified read-model decision exists | reference file and source verification |
| Front-door pointer exists | README changed |
| Runtime and adapter scope blocked | control blocks and claim boundary |
| Governance gates pass | command output |
| Material commit separate from session-sync | commit history |

## Review Gate

Required gates before material commit:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base fa3c25e5 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base fa3c25e5 --head HEAD --enforce`
- `git diff --check`

## Closure Checklist

- [x] Roadmap authored.
- [x] GC-018 authored.
- [x] Work order authored.
- [x] Stable reference authored.
- [x] Front-door pointer updated.
- [x] Completion review authored.
- [x] Forbidden runtime/provider/public/adapter/generated-state scope remains blocked.

## Operator Checkpoint

No operator checkpoint is required unless a gate demands scope outside this
work order.

## Return-To-Orchestrator Conditions

- Source verification fails for a required field.
- A gate requires runtime, provider, public, adapter, resolver, generated
  workspace state, package activation, certification, or DICE scope.
- Worktree contains unrelated changes outside allowed scope.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_ROADMAP_2026-06-27.md` | `Status: ROADMAP_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | no corpus registry source edit required for this reference-only decision | N/A | BLOCKED with reason: no corpus registry source edit authorized |
| Registry Markdown | no registry Markdown edit authorized | N/A | BLOCKED with reason: no registry Markdown edit authorized |
| External evidence digest | `sha256=52b458d57fc443cf579196db5517811718bdf84e2ad6b84896c92cbc1e182956` for retained package projection contract row in inventory | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | PASS |
| System loop interlock | no system-loop registry mutation in scope | `governance/compat/check_system_loop_interlock.py` via autorun | PASS |
| Session continuity | session-sync required after material commit | active session state and handoff after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Runtime mode | READ_MODEL_ONLY | READ_MODEL_ONLY | PASS |
| Stable reference path | `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` | present in Planned Artifact Manifest | PASS |
| Front-door pointer | `docs/reference/agent_workspace/README.md` updated | present in Planned Artifact Manifest | PASS |
| Runtime mutation | none | no runtime path in Write Ownership | PASS |
| Session-sync split | separate commit after material | required by this work order | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-27 LWPRM-T0-T4 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, python governance gates, git |
| Target paths | roadmap, GC-018, work order, read-model reference, workspace front door, completion review |
| Allowed scope source | active session next allowed move after WLFA-T0-T4 |
| Before status evidence | HEAD `fa3c25e5`; clean worktree |
| After status evidence | material closure pending commit |
| Diff evidence | `git diff --name-status fa3c25e5..HEAD` |
| Approval boundary | decision-first read-model foundation only |
| Claim boundary | no runtime, MCP, CLI, IDE bridge, provider/live, public-sync, generated workspace state mutation, resolver mutation, adapter mutation, package activation, certification decision, or DICE work |
| Agent type | Codex dispatcher/implementer/reviewer/closer |
| Invocation ID | `lwprm-t0-t4-local-workspace-projection-read-model-2026-06-27` |
| Expected manifest | `docs/roadmaps/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_ROADMAP_2026-06-27.md`; `docs/baselines/CVF_GC018_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_FOR_CODEX_2026-06-27.md`; `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md`; `docs/reference/agent_workspace/README.md`; `docs/reviews/CVF_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_COMPLETION_2026-06-27.md` |
| Actual changed set | `docs/roadmaps/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_ROADMAP_2026-06-27.md`; `docs/baselines/CVF_GC018_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_FOR_CODEX_2026-06-27.md`; `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md`; `docs/reference/agent_workspace/README.md`; `docs/reviews/CVF_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_COMPLETION_2026-06-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation. No public-sync batch is authorized.

## Claim Boundary

This work order is closed bounded for read-model foundation only. It does not
authorize runtime, MCP, CLI, IDE bridge, provider/live, public-sync, generated
workspace state mutation, resolver mutation, adapter mutation, package
activation, certification decision, production/public readiness, or DICE work.
