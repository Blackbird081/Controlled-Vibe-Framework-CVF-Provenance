# CVF Agent Work Order - FPC-T4 Strategic Capability Decision And Source-Backed Route Selection

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Date: 2026-07-02

Batch ID: FPC-T4

Dispatch base head: `b284cb70`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated worker role

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_WORKER_RETURN_2026-07-02.md`

## Dispatch Prompt Envelope

Role: delegated worker for FPC-T4.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_2026-07-02.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture with `git rev-parse --short HEAD` at worker start.

Current-time notes: artifact date is 2026-07-02; dispatch base head is
`b284cb70`. Operator has explicitly authorized an FPC-T4 decision-only route
after confirming that this is not a foundation maintenance repair or
FPC-DLR-T2 downstream lane.

Do-not-misread notes: this packet authorizes only source verification,
strategic capability candidate comparison, one worker return that also serves
as the decision packet, and no-commit return for reviewer/closer conversion. It
does not authorize runtime/provider/live proof, Model Gateway or Sandbox
Runtime implementation, model-router work, public-sync, adapter behavior,
package activation, checker implementation, generated-state mutation,
Web/UI/dashboard work, MPI-T6 runtime work, KIOD runtime-candidate reopen, push from
the provenance workspace, or production-readiness claims.

Required first actions: read required startup files, guard orientation,
literal-format gotchas, this work order, the paired GC-018 baseline, parent FPC
roadmap, FMS-T2, FPC-SCG-T0, FPC-SCG-T7, FPC-DLR-T1 worker return, current
Model Gateway bounded evidence, current Sandbox Runtime/deferred capability
evidence where source-backed, KIOD runtime-candidate parking surfaces, and all
checker source listed in the Checker Source Read-Ahead Block before writing the
worker return.

Return contract: create the worker return artifact, select exactly one routing
outcome, run required gates, leave changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Execute the FPC-T4 strategic capability decision. Success means the worker
returns command-backed evidence comparing current strategic capability
candidates against CVF-governed sources, then selects exactly one routing
outcome without implementing any capability.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id FPC-T4 --title "Strategic Capability Decision And Source-Backed Route Selection" --date 2026-07-02 --base b284cb70 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "FMS-T2 holds foundation maintenance; operator explicitly authorizes FPC-T4 decision-only route" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled dispatch envelope, mission, authority chain, source verification, dependency release evidence, negative search, strategic capability evidence matrix, routing outcomes, handoff control, reviewer conversion, ownership, fulfillment manifest, execution plan, trace matrix, acceptance criteria, verification commands, and claim boundaries; removed unresolved scaffold markers from dispatch-ready fields. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_fpc_parked_reopen_inventory.py`; `governance/compat/check_fpc_system_chain_acceptance_ledger.py`; `governance/compat/check_system_loop_interlock.py`; `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_forbidden_filesystem_state.py` |
| docOnlyNewFields | `strategicCapabilityDecision`; `candidateConditionEvidence`; `missingEvidence`; `routingOutcome`; `workerReturnDecisionPacketPath` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | Operator approved FPC-T4 as a decision-only route in the current 2026-07-02 session after source-backed confirmation that option 1 is not a P0/P1 foundation maintenance repair. |
| Active session front door | `CVF_SESSION_MEMORY.md` records the current mode and parked checkpoint. |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` records the compact next allowed move. |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` records the canonical next allowed move and active handoff. |
| Active handoff | `AGENT_HANDOFF_V31_2026-07-02.md` records the next-move boundary and parked work. |
| Parent FPC roadmap | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` |
| FMS-T2 roadmap | `docs/roadmaps/CVF_FPC_FMS_T2_CURRENT_REGISTRY_EVIDENCE_RECONCILIATION_AND_NEXT_CANDIDATE_SELECTION_ROADMAP_2026-06-28.md` |
| FPC-SCG-T0 roadmap refresh | `docs/roadmaps/CVF_FPC_SCG_T0_FOUNDATION_SYSTEM_CHAIN_GAP_CLOSURE_ROADMAP_REFRESH_2026-06-27.md` |
| FPC-SCG-T7 acceptance ledger | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` |
| FPC-DLR-T1 worker return | `docs/reviews/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_WORKER_RETURN_2026-07-02.md` |
| Paired GC-018 baseline | `docs/baselines/CVF_GC018_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_2026-07-02.md` |

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and reconcile
  before implementation.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| dispatcher | Author this GC-018/work-order pair and run pre-dispatch gates. |
| worker | Execute only source verification, strategic capability evidence audit, worker return, and decision selection; do not commit. |
| reviewer/closer | Review worker return, repair only allowed-scope closure defects if needed, and own material commit if accepted. |
| session-sync steward | Update active state and handoff only if reviewer/closer creates an accepted material commit. |
| operator | Approve any scope expansion, implementation, FPC-T4 follow-on build, runtime/provider/live/public/package/checker/adapter/model-router/MPI work, or parked-lane reopen. |

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| Intake summary | FPC-T4 decision-only source-verification route selection for strategic capability candidates; no implementation. |
| Intake classification | strategic capability decision audit, R0 documentation/source-verification dispatch |
| Scope classification | one worker-return decision packet only |
| Risk sensitivity | R0: no runtime/provider/live/public/source mutation; any implementation requires later fresh GC-018 |
| Escalation condition | Escalate to orchestrator if candidate evaluation needs implementation, live/provider proof, public-sync, source mutation, protected paths, product-requirement clarification, or a claim-boundary change. |
| Author role | dispatcher authored GC-018 and work order only |
| Executor role | delegated worker creates only the assigned worker return under WORKER_MUST_NOT_COMMIT |
| Reviewer role | reviewer/closer reviews, may repair allowed-scope packet defects, and owns material commit if accepted |
| Role separation | dispatch authorship does not grant execution or commit authority |
| Selected role route | `SINGLE_AGENT_SINGLE_ROLE` |
| Route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| Claim boundary | This role routing decision controls handoff shape only; it does not authorize implementation, runtime/provider/live proof, public-sync, Model Gateway/Sandbox Runtime mutation, model-router work, or production-readiness claims. |

## Scope

Allowed scope:

- read the startup files, paired baseline, parent FPC roadmap, FMS-T2,
  FPC-SCG-T0, FPC-SCG-T7, FPC-DLR-T1 worker return, current Model Gateway
  bounded evidence, current Sandbox Runtime/deferred capability evidence where
  source-backed, KIOD runtime-candidate parking surfaces, and relevant checker
  source;
- run negative searches and the FPC/parking gates listed below;
- create `docs/reviews/CVF_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_WORKER_RETURN_2026-07-02.md`;
- fill one candidate evidence row for Model Gateway and one for Sandbox
  Runtime;
- include an additional candidate row only if a current CVF-governed source
  names another strategic capability and the worker can source-verify its
  owner surface and gap;
- select exactly one routing outcome: `OPEN_MODEL_GATEWAY_FRESH_GC018`,
  `OPEN_SANDBOX_RUNTIME_FRESH_GC018`,
  `OPEN_OTHER_STRATEGIC_CAPABILITY_FRESH_GC018`,
  `HOLD_NO_SOURCE_BACKED_STRATEGIC_GAP`, or
  `REQUEST_PRODUCT_REQUIREMENT_EVIDENCE`;
- if a later fresh GC-018 is recommended, name the later GC-018 title, selected
  capability, exact condition-met evidence, proof requirements, and forbidden
  scope without implementing it;
- return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Forbidden scope:

- no edit to `docs/baselines/**`, `docs/work_orders/**`, `CVF_SESSION/**`,
  `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF*.md`, `governance/compat/**`,
  `docs/reference/**`, `EXTENSIONS/**`, `.private_reference/**`, `.github/**`,
  public-sync clone paths, package registries, runtime source, or generated
  aggregates;
- no Model Gateway, Sandbox Runtime, model-router, provider-registry, MCP/CLI,
  IDE bridge, adapter, package, certification, runtime source, checker,
  registry, generated-state, Web/UI/dashboard, public-sync, or source-code
  mutation;
- no runtime/provider/live proof, live quota use, action authority, automatic
  invocation, MPI-T6 runtime work, KIOD runtime-candidate reopen, or production
  readiness claim.

Risk ceiling: R0 documentation/source-verification dispatch. Any request for
runtime, provider/live, protected-path, public-sync, package, Web, MCP/CLI,
adapter, checker, generated-state, model-router, Model Gateway/Sandbox Runtime
source mutation, or MPI runtime work exceeds this work order and must return
`BLOCKED_WITH_REASON`.

## Required First Reads

| Path | Required action |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V31_2026-07-02.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/baselines/CVF_GC018_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_2026-07-02.md` | READ |
| this work order | READ |
| `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | SOURCE_VERIFIED |
| `docs/roadmaps/CVF_FPC_FMS_T2_CURRENT_REGISTRY_EVIDENCE_RECONCILIATION_AND_NEXT_CANDIDATE_SELECTION_ROADMAP_2026-06-28.md` | SOURCE_VERIFIED |
| `docs/roadmaps/CVF_FPC_SCG_T0_FOUNDATION_SYSTEM_CHAIN_GAP_CLOSURE_ROADMAP_REFRESH_2026-06-27.md` | SOURCE_VERIFIED |
| `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | SOURCE_VERIFIED |
| `docs/reviews/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_WORKER_RETURN_2026-07-02.md` | SOURCE_VERIFIED |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` KIOD runtime-candidate parking boundaries | SOURCE_VERIFIED |
| Current CVF-governed Model Gateway bounded evidence located by search | SOURCE_VERIFIED |
| Current CVF-governed Sandbox Runtime or deferred capability evidence located by search | SOURCE_VERIFIED |
| Applicable checker files listed in this packet's Checker Source Read-Ahead Block | READ |

## Pre-Flight Checks

Worker must run:

```powershell
git rev-parse --short HEAD
git status --short
```

Before handoff, worker must run the command set in `Verification Commands`.
If a listed command fails inside Allowed scope, repair and rerun. Do not ask
the operator whether to fix owned machine-shape failures.

## Worker Autonomy / No-Question Rule

Worker proceeds without operator confirmation for non-destructive actions
inside Allowed scope: reading files, running search commands, filling evidence
tables, repairing allowed-scope markdown shape, and rerunning gates after
allowed-scope remediation.

Escalation is reserved for source contradiction, missing authority, forbidden
path needs, claim-boundary change, live/provider proof, public-sync, secrets or
quota, destructive action, or higher risk.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No resolver entries were returned for this exact query. Worker must still record any new repeated non-obvious defect pattern in ADIF before closure if one is found. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_fpc_parked_reopen_inventory.py`; `governance/compat/check_fpc_system_chain_acceptance_ledger.py`; `governance/compat/check_system_loop_interlock.py`; `governance/compat/check_kiod_runtime_candidate_reopen_inventory.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_forbidden_filesystem_state.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Role:`; `Canonical packet:`; `Commit mode:`; `executionBaseHead`; `Return contract:`; checker read-ahead table fields; `Source Verification Block`; source table columns; `Dependency Release Evidence`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `WORKER_MUST_NOT_COMMIT`; `COMPLETE_PENDING_REVIEW`; `BLOCKED_WITH_REASON`; `WORKER_MUST_NOT_COMMIT honored`; `OPEN_MODEL_GATEWAY_FRESH_GC018`; `OPEN_SANDBOX_RUNTIME_FRESH_GC018`; `OPEN_OTHER_STRATEGIC_CAPABILITY_FRESH_GC018`; `HOLD_NO_SOURCE_BACKED_STRATEGIC_GAP`; `REQUEST_PRODUCT_REQUIREMENT_EVIDENCE`; `Public Export Disposition`; `DEFERRED_PRIVATE_ONLY`; Delta block evidence tokens |
| gateRunPurpose | Confirmation evidence, not first discovery; checker source and literal tokens were read before this work order was authored. |
| claimBoundary | Read-ahead evidence for this dispatch packet only; worker must repeat read-ahead for its own changed artifact before implementation. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Active session names another high-value foundation lane as an allowed operator choice, while runtime/provider/live/public/model-router/action claims require fresh GC-018 and source verification. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `another high-value foundation lane`; `fresh GC-018 and source-verified work order` | active session bootstrap read model | VALUE_SET | ACCEPT |
| Active handoff records FPC-DLR-T1 closed with `HOLD_ALL_DOWNSTREAM_LANES`. | VALUE_SET | `AGENT_HANDOFF_V31_2026-07-02.md` | `Next Allowed Move` | `HOLD_ALL_DOWNSTREAM_LANES` | active handoff | VALUE_SET | ACCEPT |
| Parent foundation roadmap defines FPC-T4 as a deferred capability reopen decision for Model Gateway, Sandbox Runtime, or other strategic gaps. | VALUE_SET | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `Proposed Tranche Plan` | `FPC-T4` | foundation planes roadmap | VALUE_SET | ACCEPT |
| Parent foundation roadmap says moving to FPC-T4 requires explicit operator decision. | VALUE_SET | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | `FPC-T3-C04+C01 Implementation Closure` | `move to FPC-T4 only after explicit operator decision` | foundation planes roadmap | VALUE_SET | ACCEPT |
| FMS-T2 selected hold for foundation maintenance because no current source-backed P0/P1 gap remains. | VALUE_SET | `docs/roadmaps/CVF_FPC_FMS_T2_CURRENT_REGISTRY_EVIDENCE_RECONCILIATION_AND_NEXT_CANDIDATE_SELECTION_ROADMAP_2026-06-28.md` | `Selected Routing Outcome`; `Reconciliation Matrix` | `HOLD_FOUNDATION_MAINTENANCE_NO_CURRENT_SOURCE_BACKED_GAP` | FMS-T2 roadmap | VALUE_SET | ACCEPT |
| FMS-T2 permits FPC-T4 only when the operator explicitly authorizes the strategic capability decision. | VALUE_SET | `docs/roadmaps/CVF_FPC_FMS_T2_CURRENT_REGISTRY_EVIDENCE_RECONCILIATION_AND_NEXT_CANDIDATE_SELECTION_ROADMAP_2026-06-28.md` | `Allowed next options after this roadmap`; `Work Plan` | `EXPLICITLY_AUTHORIZE_FPC_T4_DECISION` | FMS-T2 roadmap | VALUE_SET | ACCEPT |
| FPC-SCG-T0 records P0 and P1 foundation gaps closed bounded and P2 downstream lanes parked with reopen conditions. | VALUE_SET | `docs/roadmaps/CVF_FPC_SCG_T0_FOUNDATION_SYSTEM_CHAIN_GAP_CLOSURE_ROADMAP_REFRESH_2026-06-27.md` | `Current Gap Disposition` | `P0`; `P1`; `P2` | FPC-SCG-T0 roadmap | VALUE_SET | ACCEPT |
| T7 acceptance ledger records bounded foundation acceptance and parked downstream gates. | VALUE_SET | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | `acceptanceVerdict`; `downstreamReopenGates` | `FOUNDATION_SYSTEM_CHAIN_ACCEPTED_BOUNDED` | T7 acceptance ledger schema | VALUE_SET | ACCEPT |
| FPC-DLR-T1 current worker return selected hold for all downstream lanes. | VALUE_SET | `docs/reviews/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_WORKER_RETURN_2026-07-02.md` | `Selected Routing Outcome` | `HOLD_ALL_DOWNSTREAM_LANES` | FPC-DLR-T1 worker return | VALUE_SET | ACCEPT |
| Current session keeps the KIOD runtime candidates parked by KIOD-R10/KIOD-R11 conditions. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` | `KIOD-R10`; `KIOD-R11` | active session bootstrap read model | VALUE_SET | ACCEPT |
| Handoff front door requires work-order handoff control, WORKER_MUST_NOT_COMMIT split handling, and reviewer closure conversion. | LITERAL_INVARIANT | `docs/reference/agent_handoff/README.md` | `Stable front door`; `Machine guard` | `SINGLE_AGENT_SINGLE_ROLE` | agent handoff front door | VALUE_SET | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned baseline path existence | `Test-Path` returned `False` for the planned FPC-T4 baseline before authoring. | PASS |
| Planned work-order path existence | `Test-Path` returned `False` for the planned FPC-T4 work order before authoring. | PASS |
| Planned worker-return path existence | `Test-Path` returned `False` for the planned FPC-T4 worker return before authoring. | PASS |
| Token collision search | `rg -n "FPC-T4\|FPC_T4\|Strategic Capability Decision And Source-Backed Route Selection\|FPC_T4_STRATEGIC_CAPABILITY_DECISION" docs governance CVF_SESSION AGENT_HANDOFF_V31_2026-07-02.md` found prior FPC-T4 roadmap/session references and no existing FPC-T4 dispatch artifact. | PASS |
| Collision decision | FPC-T4 may dispatch a decision-only route selection packet. Prior roadmap and FMS-T2 evidence do not authorize implementation, runtime proof, or source mutation. | PASS |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| FPC-T3 prerequisite | Parent roadmap status is `FPC_T3_C04_C01_CLOSED_PASS_BOUNDED`; FPC-T3-C04+C01 closure implemented the prerequisite epistemic process checker/template guard. | FPC-T4 may be considered because the FPC-T3 closure evidence exists. | SATISFIED |
| Foundation maintenance hold | FMS-T2 selects `HOLD_FOUNDATION_MAINTENANCE_NO_CURRENT_SOURCE_BACKED_GAP`. | FPC-T4 must not be misread as a P0/P1 repair tranche. | SATISFIED |
| Explicit operator decision | Operator approved FPC-T4 as a decision-only route in the current 2026-07-02 session after reviewing the source-backed option check. | FMS-T2 requires explicit operator choice before FPC-T4. | SATISFIED |
| Downstream hold | FPC-DLR-T1 selected `HOLD_ALL_DOWNSTREAM_LANES`. | FPC-T4 must not reopen downstream lanes unless the worker finds separate source-backed strategic capability evidence and routes only to a later fresh GC-018. | SATISFIED |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker creates only the no-commit worker return; reviewer/closer owns acceptance and commit |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=b284cb70; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | dispatch phase owns only this GC-018 baseline and work order; worker phase owns only the worker return path |
| traceScope(phase, actor) | dispatcher records scaffold/read-ahead/gate evidence; worker records source reads, diff, status, and no-commit evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit if accepted |
| crossBatchIsolation | dispatch begins from clean worktree evidence at `b284cb70`; worker must not edit unrelated files |
| nextMoveSurfaces | reviewer/closer and session-sync steward update active session surfaces only following an accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_COMPLETION_2026-07-02.md` (optional; prefer repairing evidence in the worker return unless a separate completion review is needed for checker shape) |
| reviewerOwnedClosurePaths | `docs/reviews/CVF_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_WORKER_RETURN_2026-07-02.md`; optional completion review path |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Write Ownership

Worker owns only:

- `docs/reviews/CVF_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_WORKER_RETURN_2026-07-02.md`

Forbidden paths:

- `docs/baselines/**`
- `docs/work_orders/**`
- `docs/reference/**`
- `governance/compat/**`
- `CVF_SESSION/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF*.md`
- `EXTENSIONS/**`
- `.private_reference/**`
- `.github/**`
- public-sync clone paths
- runtime source, package registries, generated aggregates, and source mirrors

Write mode: create-only for the worker return.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | FPC-T4 dispatch packet and worker return under governed docs | Internal agents may use the packet to perform source comparison and return uncommitted decision evidence only. No commit, action, runtime, public-sync, model-router, or implementation authority is granted to the worker. | Paired GC-018; this work order; parent foundation roadmap; FMS-T2; active handoff V31. | N/A with reason: internal governed documentation workflow only. | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | No CLI/MCP or external-agent adapter owner is authorized. | External agents may read the governed documents if operating in this repo, but no external CLI/MCP tool, adapter behavior, authentication, public surface, or invocation contract is created. | Dual-agent accounting standard requires explicit disposition; FPC-T4 forbids MCP/CLI adapter work. | N/A_WITH_REASON: adapter work is forbidden by this dispatch and requires a fresh source-verified work order. | N/A_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON |
| Matching local-view guard | N/A with reason: `governance/compat/check_external_knowledge_intake_routing.py` requires this block shape, but no outside material is consumed. |
| Owner surface | Parent foundation roadmap, FMS-T2, FPC-SCG-T0/T7, FPC-DLR-T1, and current source surfaces named in this packet. |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external knowledge intake is present. |
| Claim boundary | No outside source is imported or adapted by this work order. |

## Foundation Storage Layout Block

N/A with reason: FPC-T4 dispatch authorizes one review artifact only; it does
not create, split, relocate, or refactor durable governance foundation files,
source layouts, generated aggregates, registries, or reference indexes.

## Evidence Reuse And Encoding Plan

| Field | Value |
| --- | --- |
| evidenceReuseMode | RECOMPUTE_REQUIRED |
| priorEvidenceUse | Prior roadmap, baseline, review, ledger, and inventory artifacts may be cited as governed sources, but worker must re-read current files and rerun required commands on the worker range before returning. |
| encodingMode | ASCII_ONLY_AGENT_AUTHORED_TEXT |
| pathHandling | Use repo-relative paths exactly as listed in Required First Reads and Write Ownership; do not introduce copied outside-path evidence. |
| workerRequirement | Worker return must include fresh command evidence, source-read evidence, `git diff --name-status`, and `git status --short`; do not close from memory-only or chat-only evidence. |
| claimBoundary | This plan controls evidence reuse and text/path encoding only; it does not authorize external intake, runtime/provider/live proof, public-sync, or implementation work. |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| FPC-T4 parent roadmap row | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | ENRICH_EXISTING | roadmap defines FPC-T4 as held until operator decision | Execute this work order only. |
| FMS-T2 route decision | `docs/roadmaps/CVF_FPC_FMS_T2_CURRENT_REGISTRY_EVIDENCE_RECONCILIATION_AND_NEXT_CANDIDATE_SELECTION_ROADMAP_2026-06-28.md` | ENRICH_EXISTING | operator now selected the explicit FPC-T4 decision option | Dispatch decision-only worker return. |
| P0/P1 foundation maintenance | FPC-SCG-T0 and FMS-T2 | CONFIRMED_EXISTING | no current source-backed maintenance gap remains | Do not open registry/checker repair. |
| Downstream parked lanes | FPC-DLR-T1 and T7 ledger | CONFIRMED_EXISTING | downstream lanes remain held | Do not implement or reopen downstream lanes. |
| Strategic capability candidates | current CVF-governed sources to be re-read by worker | OWNER_SURFACE_NOT_FOUND | worker must prove owner surface and gap before any later fresh GC-018 | Decision-only comparison; no implementation. |

## Strategic Capability Candidate Requirements

Worker return must fill every required row.

| Candidate route | Required source-backed comparison | Missing-evidence field | Default FPC-T4 stance |
| --- | --- | --- | --- |
| Model Gateway | Compare current governed Model Gateway roadmaps, RTAD/WWU closures, source owner surfaces, current tests/proofs if cited, and session boundaries. Identify whether a concrete strategic gap remains beyond bounded local/live/bridge proof and whether a later fresh GC-018 is justified. | missing current gap; missing owner surface; missing product requirement; missing proof plan boundary | HOLD unless all evidence fields are source-backed |
| Sandbox Runtime | Compare current governed Sandbox Runtime or deferred capability evidence. Identify whether a concrete strategic gap exists and whether it is separate from parked runtime/provider/live lanes. | missing current gap; missing owner surface; missing product requirement; missing proof plan boundary | HOLD unless all evidence fields are source-backed |
| Other strategic capability | Include only if a current CVF-governed source names the capability and the worker can source-verify owner surface, gap, and boundary. | missing governed source; missing owner surface; missing operator relevance | HOLD unless source-backed and operator-relevant |

## Selected Routing Outcome Contract

Worker return must select exactly one of:

- `OPEN_MODEL_GATEWAY_FRESH_GC018`
- `OPEN_SANDBOX_RUNTIME_FRESH_GC018`
- `OPEN_OTHER_STRATEGIC_CAPABILITY_FRESH_GC018`
- `HOLD_NO_SOURCE_BACKED_STRATEGIC_GAP`
- `REQUEST_PRODUCT_REQUIREMENT_EVIDENCE`

If an `OPEN_*_FRESH_GC018` token is selected, the worker must name the later
GC-018 title, selected capability, exact condition-met evidence, proof
requirements, and forbidden scope. The worker must not implement that
capability.

## KIOD Runtime Candidate Parking Control

| Candidate | Current parking source | Worker instruction | Disposition |
| --- | --- | --- | --- |
| KIOD runtime candidates | active session state and KIOD-R10/KIOD-R11 boundaries | Do not reopen parked runtime-candidate work. | PARKED |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| providerLiveProofAuthorized | NO |
| publicSyncAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | FPC-T4 authorizes only source comparison and decision-return documentation. It does not claim or mutate runtime/provider behavior. |
| requiredFutureAction | Any runtime/provider/live/public/adapter/MPI/Model Gateway/Sandbox Runtime implementation claim requires a later fresh GC-018, source verification, and live/provider proof when governance behavior is claimed. |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/reviews/CVF_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_WORKER_RETURN_2026-07-02.md` | Create as the only worker-owned artifact; include candidate evidence matrix, selected routing outcome, command evidence, Agent Operation Trace Block, Delta Execution Claim Boundary Control Block, Public Export Disposition, Claim Boundary, git status, changed files, and no-commit statement. |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_FPC_T4_STRATEGIC_CAPABILITY_DECISION_AND_SOURCE_BACKED_ROUTE_SELECTION_WORKER_RETURN_2026-07-02.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated worker role |
| Provider or surface | local governed documentation worker |
| Session or invocation | FPC-T4 Strategic Capability Decision And Source-Backed Route Selection, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, Python governance checkers, rg |
| Target paths | worker return path only |
| Allowed scope source | this work order and paired GC-018 |
| Before status evidence | dispatch authoring clean worktree evidence: `git status --short` was empty at `b284cb70` before creating this dispatch; worker must capture its own clean or dirty before status before edits |
| After status evidence | `git status --short` after edits |
| Diff evidence | `git diff --name-status` |
| Approval boundary | no implementation; no runtime/provider/live/public/package/checker/generated-state/model-router/MPI work |
| Claim boundary | strategic capability decision return only |
| Agent type | delegated worker |
| Invocation ID | `fpc-t4-2026-07-02` |
| Expected manifest | worker return path only |
| Actual changed set | worker must fill from command evidence |
| Manifest delta | worker must fill from command evidence |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Capture executionBaseHead and worktree status before edits. | `git rev-parse --short HEAD`; `git status --short` |
| 2 | Read required sources and checker source before writing. | Source-read evidence and Checker Source Read-Ahead Block in worker return |
| 3 | Re-run system-loop, FPC acceptance, parked reopen, and KIOD runtime-candidate gates on the worker range where applicable. | command evidence |
| 4 | Fill Model Gateway, Sandbox Runtime, and any source-named other strategic capability evidence rows. | Strategic Capability Evidence Matrix |
| 5 | Select exactly one routing outcome. | Selected Routing Outcome |
| 6 | Run required gates and record command evidence. | Command Evidence |
| 7 | Leave changes uncommitted and return for reviewer. | `git status --short`; no-commit statement |

## Evidence Requirements

| Evidence item | Required form |
| --- | --- |
| Source reads | Worker return cites current CVF-governed source files and sections, not memory-only or chat-only claims. |
| Candidate comparison | One row per required candidate with conditionMet value, evidence, missingEvidence, risk, value, and recommendedDisposition. |
| Routing outcome | Exactly one selected token from the Selected Routing Outcome Contract. |
| Command evidence | Required verification commands recorded with PASS, FAIL, or BLOCKED. |
| Diff evidence | `git diff --name-status` and `git status --short` recorded before return. |

## Review Gate

Reviewer/closer must verify that the worker return stayed inside allowed scope,
evaluated required candidates, selected exactly one routing outcome, preserved
`WORKER_MUST_NOT_COMMIT`, and did not edit forbidden paths. If the worker
return selects a later fresh GC-018, reviewer/closer must confirm it names only
a follow-on dispatch title and does not implement the selected capability.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Worker return exists at the assigned path | checked, `N/A with reason`, or `BLOCKED` |
| Required strategic candidates evaluated | checked, `N/A with reason`, or `BLOCKED` |
| One routing outcome selected | checked, `N/A with reason`, or `BLOCKED` |
| Forbidden paths unchanged | checked, `N/A with reason`, or `BLOCKED` |
| Worker did not commit | checked, `N/A with reason`, or `BLOCKED` |
| Required gates run | checked, `N/A with reason`, or `BLOCKED` |
| Public Export Disposition present | checked, `N/A with reason`, or `BLOCKED` |
| Claim Boundary present | checked, `N/A with reason`, or `BLOCKED` |

## Return-To-Orchestrator Conditions

| Return token | Meaning |
| --- | --- |
| `COMPLETE_PENDING_REVIEW` | Worker completed the audit, selected exactly one routing outcome, ran required gates, and left changes uncommitted. |
| `BLOCKED_WITH_REASON` | Worker hit a source contradiction, missing authority, forbidden-scope need, or unrepaired gate failure outside allowed scope. |

## Operator Checkpoint

No operator checkpoint is required for worker execution inside allowed scope.
Operator approval is required before any implementation, runtime/provider/live
proof, public-sync, adapter, package, checker, generated-state,
Web/UI/dashboard, model-router, Model Gateway/Sandbox Runtime source mutation,
KIOD runtime-candidate reopen, or MPI-T6 runtime work.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | FPC-T4 strategic capability decision worker return |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, or universal governed-coding-control claim is made by this work order. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this work order. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed by this work order. |
| invocationBoundary | Manual local source reads, search commands, and governance gate invocation only. |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | Worker-return evidence, source comparison, no-commit role boundary, and reviewer-owned closure only. |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/adapter/MPI/Model Gateway/Sandbox Runtime behavior without a fresh source-verified authorization. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order handling | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| FPC-T4 requires FPC-T3 closure evidence and operator decision | Dependency Release Evidence records both. | dependency table | dispatch-quality gate | PASS |
| FPC-T4 is decision-only for deferred strategic capabilities | Scope and Strategic Capability Candidate Requirements block preserve decision-only route. | worker return decision matrix | reviewer audit | PASS |
| Do not preempt foundation audit with deferred capability work | FMS-T2 and FPC-SCG evidence confirm foundation maintenance is held before FPC-T4 dispatch. | Source Verification Block | system-loop and acceptance-ledger gates | PASS |
| No runtime/provider/live/public/model-router implementation | Forbidden scope and Current Runtime Freshness Verification block prohibit implementation. | git diff and worker return evidence | commit steward | PASS |
| Worker must return a source-backed decision | Work order requires exactly one routing outcome with evidence. | Selected Routing Outcome | worker-return quality gate plus reviewer audit | PASS |

## Acceptance Criteria

| ID | Criterion | Required result |
| --- | --- | --- |
| AC1 | System-loop interlock, FPC acceptance ledger, parked reopen inventory, and KIOD runtime candidate gates run on current worker range where applicable. | PASS |
| AC2 | Model Gateway and Sandbox Runtime are evaluated as strategic capability candidates. | PASS |
| AC3 | Any other candidate appears only if a current governed source names it. | PASS or N/A with reason |
| AC4 | Every candidate condition is compared with current source-backed evidence. | PASS |
| AC5 | Every missing-evidence claim is explicit. | PASS |
| AC6 | Exactly one routing outcome is selected. | PASS |
| AC7 | Any selected later fresh GC-018 names title, capability, evidence, proof requirements, and forbidden scope. | PASS or N/A with reason if no lane selected |
| AC8 | No implementation, live proof, public-sync, adapter, package, registry, checker, generated-state, Web, model-router, source mutation, KIOD runtime-candidate reopen, or MPI mutation occurs. | PASS |
| AC9 | Worker leaves changes uncommitted and returns for reviewer/closer conversion. | PASS |

## Verification Commands

Worker must run before return:

```text
python governance/compat/check_system_loop_interlock.py --enforce
python governance/compat/check_fpc_system_chain_acceptance_ledger.py --enforce
python governance/compat/check_fpc_parked_reopen_inventory.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_kiod_runtime_candidate_reopen_inventory.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_governed_artifact_checker_read_ahead.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_worker_return_quality_gate.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_delta_execution_claim_boundary.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --name-status
git status --short
```

Dispatcher must run before dispatch commit:

```text
python governance/compat/check_dispatch_scaffold_provenance.py --base b284cb70 --head HEAD --enforce
python governance/compat/check_dispatch_prompt_envelope.py --base b284cb70 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base b284cb70 --head HEAD --enforce
python governance/compat/check_governed_artifact_checker_read_ahead.py --base b284cb70 --head HEAD --enforce
python governance/compat/check_adif_defect_registry_disclosure.py --base b284cb70 --head HEAD --enforce
python governance/compat/check_agent_handoff_boundary.py --base b284cb70 --head HEAD --enforce
python governance/compat/check_system_loop_interlock.py --enforce
python governance/compat/check_fpc_system_chain_acceptance_ledger.py --enforce
python governance/compat/check_fpc_parked_reopen_inventory.py --base b284cb70 --head HEAD --enforce
python governance/compat/check_kiod_runtime_candidate_reopen_inventory.py --base b284cb70 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b284cb70 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base b284cb70 --head HEAD --enforce
```

## Fail Conditions

| Condition | Required response |
| --- | --- |
| Worker recommends a later fresh GC-018 without source-backed owner surface, gap evidence, and forbidden-scope boundary. | Select `HOLD_NO_SOURCE_BACKED_STRATEGIC_GAP` or `REQUEST_PRODUCT_REQUIREMENT_EVIDENCE`, not implementation. |
| Worker reopens P0/P1 foundation maintenance without current registry/checker/manifest regression evidence. | Return `BLOCKED_WITH_REASON`; this dispatch is not a maintenance repair lane. |
| Runtime/provider/live, Model Gateway/Sandbox Runtime source mutation, or MPI work is selected without a later fresh GC-018 and required proof boundary. | Return `BLOCKED_WITH_REASON`. |
| Public-sync is proposed without public/provenance boundary evidence and fresh public-sync authorization. | Return `BLOCKED_WITH_REASON`. |
| Implementation paths are edited before the decision closes. | Return `BLOCKED_WITH_REASON` and preserve evidence. |
| Required gates fail and the worker cannot repair inside allowed scope. | Return `BLOCKED_WITH_REASON` with checker output. |

## Claim Boundary

This work order authorizes only a bounded FPC-T4 source-verification,
strategic capability evidence audit, and worker-return decision packet. It
does not reopen or implement Model Gateway, Sandbox Runtime, downstream lanes,
MPI-T6, KIOD runtime candidates, or any runtime/provider/public lane; does not prove
provider behavior; does not export public artifacts; does not mutate package
lifecycle, source, registry, checker, generated state, or session state.
Reviewer/closer owns acceptance, material commit, and session-sync if the
worker return is accepted.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: FPC-T4 is private provenance dispatch work over internal strategic
capability decision evidence. No public-sync export is authorized by this work
order.
