# CVF Local Workspace Projection Read Model Foundation Roadmap

Memory class: ROADMAP

Status: ROADMAP_CLOSED_PASS_BOUNDED

Owner: Codex

Date: 2026-06-27

Base head: `fa3c25e5`

## Authorization / Decision

Decision: execute T0 through T4 as a bounded read-model foundation batch.

Authorization source: active session next allowed move after WLFA-T0-T4
closure.

## Purpose

Close the decision-first Local Workspace Projection Read Model foundation
tranche requested by the active session next allowed move.

## Scope / Methodology

Scope: T0 through T4 foundation only. The tranche creates a CVF-owned
projection read-model decision reference, source-verifies package projection
vocabulary against existing CVF workspace contracts, updates the workspace
front door, records GC-018 and work-order authority, and closes with a bounded
completion review.

Methodology: read active session surfaces, read workspace front door and
workspace contracts, source-verify line anchors, write artifacts inside the
allowed paths, run governance gates, and commit material separately from
session-sync.

## Findings / Position

Position: the highest-value next foundation move is not DICE or runtime. It is
a stable read-model decision that tells future agents exactly how package
projection vocabulary maps to CVF state and evidence without converting the raw
package into authority.

## Non-Goals

- Runtime queue execution.
- MCP, CLI, or IDE bridge implementation.
- CVF Web source or UI implementation.
- Provider/live proof.
- Public-sync or push.
- Generated workspace state mutation.
- Resolver or adapter mutation.
- Package activation, package import, package instance creation, or package certification.
- DICE work.

## Design Control Gate

| Control | Disposition |
|---|---|
| Decision-first posture | PASS - reference decision before implementation |
| Source verification | PASS - CVF-owned sources and inventory lines are cited |
| Runtime boundary | PASS - `READ_MODEL_ONLY` |
| Two-layer boundary | PASS - Web and Local Workspace Runtime are not conflated |
| External package boundary | PASS - package remains comparison input only |

## Roadmap Tranches

| Tranche | Purpose | Result |
|---|---|---|
| T0 | Decision and authority packet | Complete through this roadmap and GC-018 |
| T1 | Source map package projection vocabulary to CVF-owned workspace contracts | Complete through source verification |
| T2 | Create stable read-model decision reference | Complete at `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` |
| T3 | Update workspace front-door discovery | Complete through `docs/reference/agent_workspace/README.md` pointer update |
| T4 | Closure evidence and material commit | Complete through completion review and gates |

## Work Plan

| Step | Action | Status |
|---|---|---|
| T0 | File roadmap and GC-018 | COMPLETE |
| T1 | Source-verify CVF-owned workspace surfaces and package inventory | COMPLETE |
| T2 | Add stable read-model decision reference | COMPLETE |
| T3 | Add workspace front-door pointer | COMPLETE |
| T4 | Add completion review and run gates | COMPLETE |

## Source Inventory

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/agent_workspace/README.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | SOURCE_VERIFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active session next allowed move is decision-first Local Workspace Projection Read Model | `CVF_SESSION_MEMORY.md` | Startup Acknowledgment; Next Allowed Move | `workspace_layer_full_package_absorption_closed_pass_bounded_pending_projection_read_model_decision` | active session front door | ACCEPT |
| Package inventory recommends a local workspace projection read-model roadmap | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | line 163 | `Next-Roadmap Recommendation` | package absorption inventory | ACCEPT |
| Package projection vocabulary is already mapped as advisory input | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | Useful Patterns; CVF Mapping | `workspace_state.json`; `workflow_state.json`; `governance_state.json`; `agent_state.json`; `evidence_state.json` | package absorption map | ACCEPT |
| Package projection contract exists in retained inventory | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | line 82 | `STATE_PROJECTION_CONTRACT.md` | package absorption inventory | ACCEPT |
| CVF topology owns required workspace-state fields | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | lines 81-106 | Required State Fields | workspace state topology contract | ACCEPT |
| Operator view plan owns read-model section vocabulary | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | lines 37-51 | Read Model Sections | operator view plan | ACCEPT |
| Read-model work uses runtime expansion control block | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | lines 60-73 | Runtime Expansion Control Block | runtime expansion readiness contract | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`workspace_projection_read_model`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `docs/reference/agent_workspace/` read-model reference | internal agents may use the reference for future dispatch and review only | workspace front door and read-model decision reference | N/A with reason: no adapter created | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP projection adapter is not opened by this roadmap | no executable external-agent support or ingress claim | dual-surface standard and runtime expansion contract | deferred adapter owner; fresh GC-018 required | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | root/folder lifecycle classification plus absorption map when retained |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_foundation_storage_layout.py` |
| Owner surface | `docs/reference/agent_workspace/` |
| Disposition | ADAPT package projection vocabulary into a CVF-owned read-model reference |
| Claim boundary | no raw package authority, runtime, MCP, CLI, IDE bridge, provider, public-sync, generated workspace state mutation, or readiness claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local workspace projection read-model roadmap T0-T4 |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: source verification and governance gate output |
| actionEvidence | ACTION_EVIDENCE_PRESENT: roadmap, GC-018, work order, reference, front-door pointer, and completion review |
| invocationBoundary | local source reads and governed markdown edits only |
| interceptionBoundary | no runtime interception or provider route changed |
| claimLanguage | decision-first read-model foundation only |
| forbiddenExpansion | no runtime queue, MCP tool, CLI adapter, IDE bridge, provider/live proof, public-sync, generated workspace state mutation, resolver mutation, adapter mutation, package activation, certification decision, or DICE work |

## Current Runtime Freshness Verification

| Runtime claim | Current evidence | Disposition |
|---|---|---|
| Runtime implementation | no runtime path is authorized by this roadmap | NOT_IMPLEMENTED_WITH_REASON |
| MCP or CLI adapter | no MCP or CLI adapter path is authorized by this roadmap | NOT_IMPLEMENTED_WITH_REASON |
| Provider/live proof | no provider/live proof is authorized or run | NOT_IMPLEMENTED_WITH_REASON |
| Generated workspace state mutation | generated workspace state is outside roadmap scope | NOT_IMPLEMENTED_WITH_REASON |

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

| Assertion | Receipt source | Disposition |
|---|---|---|
| Read-model decision exists | `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` | PASS |
| Package projection vocabulary is source-verified | Source Verification Block | PASS |
| Runtime remains blocked | Claim Boundary and Runtime Expansion Control Block | PASS |
| Workspace front door points to the decision | `docs/reference/agent_workspace/README.md` | PASS |

## Acceptance Criteria

| Criterion | Evidence |
|---|---|
| Roadmap and GC-018 exist | this file and GC-018 baseline |
| Stable read-model decision exists | `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` |
| Front-door pointer exists | `docs/reference/agent_workspace/README.md` |
| Runtime remains blocked | Runtime Expansion Control Block |

## Verification / Evidence

Required verification before material commit:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base fa3c25e5 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base fa3c25e5 --head HEAD --enforce`
- `git diff --check`

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
| Agent type | Codex multi-role dispatcher/implementer/reviewer/closer |
| Invocation ID | `lwprm-t0-t4-local-workspace-projection-read-model-2026-06-27` |
| Expected manifest | `docs/roadmaps/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_ROADMAP_2026-06-27.md`; `docs/baselines/CVF_GC018_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_FOR_CODEX_2026-06-27.md`; `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md`; `docs/reference/agent_workspace/README.md`; `docs/reviews/CVF_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_COMPLETION_2026-06-27.md` |
| Actual changed set | `docs/roadmaps/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_ROADMAP_2026-06-27.md`; `docs/baselines/CVF_GC018_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_2026-06-27.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_FOR_CODEX_2026-06-27.md`; `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md`; `docs/reference/agent_workspace/README.md`; `docs/reviews/CVF_LWPRM_T0_T4_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_FOUNDATION_COMPLETION_2026-06-27.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance workspace foundation. No public-sync batch is
authorized.

## Claim Boundary

This roadmap is closed bounded at foundation/read-model level only. It does not
authorize runtime queue execution, MCP or CLI tools, IDE bridge work,
provider/live proof, public-sync, generated workspace state mutation, resolver
mutation, adapter mutation, package activation, certification decision,
production/public readiness, or DICE work.
