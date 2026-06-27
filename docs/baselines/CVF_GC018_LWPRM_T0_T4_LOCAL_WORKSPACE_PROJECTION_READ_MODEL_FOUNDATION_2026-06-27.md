# GC-018 - LWPRM-T0-T4 Local Workspace Projection Read Model Foundation

Memory class: GC_018_BASELINE

Status: CLOSED_PASS_BOUNDED

Owner: Codex

Date: 2026-06-27

Base head: `fa3c25e5`

## Baseline Decision

Decision: authorize and close a bounded `READ_MODEL_ONLY` foundation batch for
the local workspace projection read model.

## Purpose

Authorize the bounded local workspace projection read-model foundation batch.

## Scope / Methodology

Scope: roadmap, baseline, work order, stable read-model decision reference,
workspace front-door pointer, and completion review.

Methodology: source-verify active CVF workspace contracts and package
projection vocabulary, adapt only decision/reference content, run governance
gates, and keep session-sync separate after material commit.

## Findings / Position

This is a foundation/read-model batch. It is useful because it turns the
package projection concept into a CVF-owned mapping before any future runtime
or UI work can cite it.

## Proposed Tranche

| Tranche | Scope | Disposition |
|---|---|---|
| LWPRM-T0 | Decision and authority | COMPLETE |
| LWPRM-T1 | Source mapping | COMPLETE |
| LWPRM-T2 | Stable read-model reference | COMPLETE |
| LWPRM-T3 | Front-door pointer | COMPLETE |
| LWPRM-T4 | Closure and gates | COMPLETE |

## Source Inventory

| File | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | SOURCE_VERIFIED |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | SOURCE_VERIFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Follow-on roadmap recommendation is local workspace projection read model | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | line 163 | `Next-Roadmap Recommendation` | package absorption inventory | ACCEPT |
| Package projection concepts are CVF-mapped as advisory input | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | Useful Patterns; CVF Mapping | `workspace_state.json`; `workflow_state.json`; `governance_state.json`; `agent_state.json`; `evidence_state.json` | package absorption map | ACCEPT |
| Package projection contract exists in retained inventory | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | line 82 | `STATE_PROJECTION_CONTRACT.md` | package absorption inventory | ACCEPT |
| CVF topology owns workspace-state required fields | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md` | lines 81-106 | Required State Fields | workspace state topology contract | ACCEPT |
| Operator view plan defines read model sections | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_OPERATOR_VIEW_PLAN.md` | lines 37-51 | Read Model Sections | operator view plan | ACCEPT |
| Runtime expansion contract recognizes `READ_MODEL_ONLY` | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | lines 60-73 | `runtimeMode`; `READ_MODEL_ONLY` | runtime expansion readiness contract | ACCEPT |
| Two-layer standard separates Web Workspace from Local Workspace Runtime | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | lines 81-109 | Forbidden Conflations; CVF Web Upgrade Boundary | workspace two-layer standard | ACCEPT |
| Package workspace schema exists in retained inventory | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | line 135 | `workspace_state.schema.json` | package absorption inventory | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`workspace_projection_read_model`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Roadmap-To-Work-Order Trace Matrix

| Roadmap item | Work order section | Completion evidence |
|---|---|---|
| T0 decision and authority | Mission; Authority Chain | roadmap, GC-018, work order |
| T1 source map | Source Verification Block | read-model decision and completion review |
| T2 stable reference | Allowed Scope; Planned Artifact Manifest | `CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md` |
| T3 front-door pointer | Allowed Scope | `docs/reference/agent_workspace/README.md` |
| T4 closure | Acceptance Criteria; Closure Evidence | completion review and gates |

## Allowed Scope

- Add this GC-018 baseline.
- Add the matching work order.
- Add the matching roadmap.
- Add `docs/reference/agent_workspace/CVF_LOCAL_WORKSPACE_PROJECTION_READ_MODEL_DECISION.md`.
- Update `docs/reference/agent_workspace/README.md` with a pointer to the new reference.
- Add the matching completion review.

## Forbidden Scope

- Runtime queue execution.
- MCP, CLI, or IDE bridge implementation.
- CVF Web source or UI implementation.
- Provider/live proof.
- Public-sync or push.
- Generated workspace state mutation.
- Active session generated aggregate mutation before separate session-sync.
- Resolver or adapter mutation.
- Package activation, package import, package instance creation, or package certification.
- DICE work.

## Runtime Expansion Control Block

| Field | Disposition |
|---|---|
| runtimeMode | READ_MODEL_ONLY |
| contractSource | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| frontDoor | `docs/reference/agent_workspace/README.md` |
| stateSourceOfTruth | existing generated workspace state and active session state; no new aggregate in this batch |
| queueBoundary | N/A with reason: no queue records or executable behavior |
| operatorViewBoundary | read-model decision only |
| providerBoundary | no-provider |
| publicBoundary | private-only |
| guardOwner | existing workspace design/runtime boundary guards |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | workspace reference surface | internal agents may cite the read-model decision for future dispatch | source verification rows | N/A with reason: no adapter created | CONTRACT_ONLY |
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
| claimScope | GC-018 authorization for read-model foundation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: source verification and gate output |
| actionEvidence | ACTION_EVIDENCE_PRESENT: planned material manifest and completion evidence |
| invocationBoundary | local source reads and governed markdown edits only |
| interceptionBoundary | no runtime interception or provider route changed |
| claimLanguage | foundation authorization only |
| forbiddenExpansion | no runtime, MCP, CLI, IDE bridge, provider/live proof, public-sync, generated workspace state mutation, resolver mutation, adapter mutation, package activation, certification decision, or DICE work |

## Current Runtime Freshness Verification

| Runtime claim | Current evidence | Disposition |
|---|---|---|
| Runtime implementation | no runtime path is authorized by this baseline | NOT_IMPLEMENTED_WITH_REASON |
| MCP or CLI adapter | no MCP or CLI adapter path is authorized by this baseline | NOT_IMPLEMENTED_WITH_REASON |
| Provider/live proof | no provider/live proof is authorized or run | NOT_IMPLEMENTED_WITH_REASON |
| Generated workspace state mutation | generated workspace state is outside baseline scope | NOT_IMPLEMENTED_WITH_REASON |

## Acceptance Criteria

| Criterion | Evidence |
|---|---|
| Read-model reference exists and is CVF-owned | stable reference file |
| Package projection vocabulary is mapped to CVF surfaces | source verification and projection sections |
| Front door discovers the reference | README pointer |
| Forbidden runtime and adapter scope remains blocked | control blocks and claim boundary |
| Governance gates pass | command output before material commit |

## Evidence / Verification

Required verification before material commit:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base fa3c25e5 --head HEAD`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base fa3c25e5 --head HEAD --enforce`
- `git diff --check`

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

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation. No public-sync batch is authorized.

## Claim Boundary

This GC-018 authorizes only read-model foundation documentation and front-door
discovery. It does not authorize runtime, MCP, CLI, IDE bridge, provider/live,
public-sync, generated workspace state mutation, resolver mutation, adapter
mutation, package activation, certification decision, production/public
readiness, or DICE work.
