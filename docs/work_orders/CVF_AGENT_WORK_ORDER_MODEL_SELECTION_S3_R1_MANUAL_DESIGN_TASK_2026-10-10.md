# CVF Agent Work Order - Model Selection S3-R1 Manual Design Task

Memory class: governed-worker-dispatch
docType: work_order
Status: CLOSED_PASS_BOUNDED
Date: 2026-10-10
Batch ID: CVF-MODEL-SELECTION-S3-R1-20261010
Dispatch base head: 95ed2e98fbe034adf7f632e503a7844db4b02235
Commit mode: WORKER_MUST_NOT_COMMIT
Worker return path: `docs/reviews/CVF_MODEL_SELECTION_S3_R1_WORKER_RETURN_2026-10-10.md`
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT shared-workspace design worker; Local orchestrator is the reviewer and final decision owner.
Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md`; paired baseline `docs/baselines/CVF_GC018_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md`.
Commit mode: WORKER_MUST_NOT_COMMIT. executionBaseHead: WORKER_MUST_CAPTURE_AT_START from a clean committed release.
Current-time notes: selected worker-seat candidate is the operator-started Claude Haiku 5.5 Max/Max configuration, identity OPERATOR_REPORTED and snapshot UNKNOWN; Local must confirm the actual seat, role/context eligibility and current grant before dispatch. No API route or additional provider invocation is granted.
Do-not-misread notes (dispatch-time condition, now historical): clean committed release and current seat/context admission were required before worker invocation; Expense, Gateway API, external research, public-sync and deployment remain parked.
Required first actions: read session bootstrap/front door and active handoff, guard orientation/literal gotchas, this order and baseline, the four named owner inputs, then applicable checker sources; capture start time and execution HEAD before edits.
Return contract: exact two design drafts plus evidence and worker return; `COMPLETE_PENDING_REVIEW` or one consolidated `BLOCKED_WITH_REASON`, with uncommitted diff and first-disposition/repair/cost evidence.

## Purpose

Make the accepted Web critique operationally usable in the private R2 doctrine and contract through one bounded, real documentation task. Keep the original R2 review evidence intact and produce a reviewable worker return. This first AGENT_SEAT manual loop tests whether a rationale can be bound to a real work order and output; it cannot establish comparative model quality, savings or an automated selector.

## Scope / Target / Owner Boundary

Worker may change only the two private design drafts and its exact return/evidence files. Local owns admission, independent inspection, any in-scope reviewer repair, commit and continuity. The existing roadmap S3 is demand-gated; the operator's 2026-10-10 instruction to proceed with the first work order selects this bounded design-maintenance task. It does not open S2 schema, S4 later consumption or S5 runtime.

## Authority Chain

| Source | Binding |
|---|---|
| Operator instruction 2026-10-10 | Local is final technical decision owner; proceed to first work order without a model question to the Non coder |
| `docs/roadmaps/CVF_ORCHESTRATOR_MODEL_SELECTION_SYSTEM_CHAIN_ROADMAP_2026-10-10.md`, S3 | manual B task -> execution -> independent review; no benchmark-only task |
| `docs/reviews/CVF_MODEL_SELECTION_WEB_REVIEW_LOCAL_DISPOSITION_2026-10-10.md`, 01/04/06 and 02/03/07 | Local-accepted design deltas and owner pointers |
| `docs/baselines/CVF_GC018_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md` | exact task boundary and source-verified preimages |
| `AGENT_HANDOFF_V63_2026-09-18.md` and `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | active mode/parked boundaries; actual execution authority remains separate |

## Manual B Selection Rationale

TaskProfile: private documentation change; worker role only; AGENT_SEAT; reversible Git diff; no secret, protected-control, auth, credential, external or production effect; observable text/negative-matrix acceptance. Operator delegated the technical choice by directing Local to make the final decision and proceed, while retaining topology and effect authority. Acceptance owner is Local, a different actor from the worker; different model is not required by this task. Choice grant does not grant invocation.

Candidate selected for this *proposed* dispatch: Claude Haiku 5.5 Max/Max in an operator-started shared-workspace seat. The exact model label and effort are operator-reported in the six-task Local report; immutable snapshot, current seat configuration and usage bill are UNKNOWN. Prior four accepted bounded worker tasks included guides/returns and source-constrained edits. This is relevant positive process/output evidence but not a matched governance-design trial. Applicability is PARTIAL; quality disposition PROVISIONAL for this low-effect, independently reviewed task only. Sonnet High has two accepted UI-worker observations, also non-comparable, so this choice is a bounded preference, not a ranking or fixed mapping. No published score or price is transferred, and no cost savings are claimed.

SelectionDecision: SELECT one worker-seat candidate provisionally; `executionAuthorized=false` until current availability, model/effort/harness/tool profile, seat context, choice grant, task budget and independent review route are checked at dispatch. `operatorAssignmentDisposition=NOT_APPLICABLE_DELEGATED_CHOICE`; no `HONORED_WITH_EVIDENCE_GAP` claim is needed. If the seat differs materially, is unavailable, lacks mandatory admission proof, or a hard requirement is known to fail, HOLD the dependent dispatch and record a successor decision. Do not silently substitute another model. Unknown predictive quality evidence cannot waive authority, context or budget admission. This is neither selection of the active orchestrator's own seat nor a Gateway API call.

CostBasis: no monetary hard cap or dated comparable tariff was supplied; money, tokens and subscription allocation remain null/UNKNOWN. Local sets one bounded worker attempt of at most 45 elapsed minutes from first read to frozen return, no delegated helper/provider/API call and no automatic retry. Worker and Local review minutes, repair minutes, elapsed time and exposed usage are separate fields. A cash cap added before dispatch requires a supported bound in the same currency or HOLD; a token count is not money. The worker records initial return/first gate disposition, all failed attempts, assistance/repair attribution and parent-task budget consumed, including abandoned attempts.

## Allowed Paths

- `docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_DOCTRINE_DESIGN_2026-10-10.md`
- `docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_CONTRACT_DESIGN_2026-10-10.md`
- `docs/reviews/CVF_MODEL_SELECTION_S3_R1_WORKER_RETURN_2026-10-10.md`
- `docs/reviews/evidence/model-selection-s3-r1-worker-20261010.json`

Ignored `.cvf/runtime/model-selection-s3-r1-worker-20261010/` may hold time, diff and gate logs; no tracked file outside the four-path ledger may change in the worker lane.

## Forbidden Paths

Roadmap, original Claude/Web returns and their hash evidence, previous Local reconciliation, baseline/order, session state, public guide, Gateway code, governance checkers, active product source, Expense and all other tracked paths are read-only. No source download, credential/environment inspection, direct provider/API call, model replacement, install, network write, public-sync, deployment, runtime activation or commit.

## Implementation Contract

1. In doctrine Selection Surfaces and Decision Procedure, bound the assigned-model evidence-gap exception to predictive quality history only. Keep SELECT and dispatch/admission separate; a missing mandatory context/authority/budget/effect proof remains pending with its existing owner. Preserve R1-B1: missing quality history alone is not a known failed hard requirement.
2. In contract Record Families/Minimum Manual Record, enrich ReviewedOutcomeLink with initial worker return and first disposition, repair/help attribution, final accepted artifact, failed/abandoned attempt references and remaining parent-task spend. Separate artifact acceptance from evidence about the originally selected configuration; do not create a second ledger.
3. In contract LearningConsumptionLink/Freeze And Transition, make the later decision check current supersession/retraction and applicability of the pinned original source plus present disposition. PARENT_CONTROL follows existing typed PLL obligations; LOCAL_OBSERVATION does not claim parent DELIVERY/APPLICATION. Preserve zero/one/many consumer semantics and frozen-history immutability.
4. Add three compact static negative rows: quality gap plus missing mandatory context proof; accepted artifact only after material reviewer repair; later decision citing retracted evidence. Include the expected hold/narrowed claim and owner. Do not claim these are executed tests.
5. Keep R2/Claude evidence as historical exact-byte proof. Mark the edits as a post-Web R3 design delta; prior conditional concurrence applies only to R2. Do not change the external review return or retroactively claim independent R3 acceptance.

## Acceptance Criteria

Exactly four worker-owned files changed. Three accepted corrections agree across doctrine/contract without changing the surface split, operator precedence, delegated evidence floor or current code. The negative rows discriminate quality absence from missing admission and an accepted artifact from initial model quality; retracted evidence cannot be silently reused. The worker provides before/after hashes, four-path diff, no hidden snapshot assertion, actual gate results and a candid initial/repair/total-burden record. Local reviewer reconstructs claims from source/diff/return and checks independence/actor metadata before acceptance.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap obligation | Work-order implementation | Exit evidence |
|---|---|---|
| S3 manual B task with real outcome | Two R2 design drafts receive needed Web clarification as R3 | exact diff, worker return, independent Local review |
| Selection rationale before task | Manual B Selection Rationale above | actual seat/authority verification and frozen decision at dispatch |
| No fabricated cost or model ranking | CostBasis and return fields | nulls/units/attribution reviewed; no savings claim |
| S4/S2/S5 separately demand-gated | Forbidden Paths and Claim Boundary | no later-consumption, schema or runtime promotion |

## Agent Roles

Operator supplies outcome/constraints and retains topology/effect authority. Local orchestrator selects one bounded worker configuration, checks admission, dispatches only after release, and independently reviews/commits. Shared-workspace worker implements the exact four-file task without commit. Session-sync steward updates continuity only after Local disposition.

## Required First Reads

Progressive startup front door and active handoff; guard orientation and literal gotchas; paired baseline; this order; the two R2 design sources, S3 roadmap and Local Web disposition; actual owner/checker sections for the four outputs. Read the exact current source hashes before edits. Do not use provider memory as CVF authority.

## Pre-Flight Checks

Local checks clean committed worktree, current worker seat/model/effort/harness availability, private context eligibility, choice/invocation distinction, a bounded time/cost envelope, different-actor acceptance route and no new mandatory proof gap. If any fails, hold the dependent dispatch and record its owner. At worker start record `executionBaseHead`, start time and four-path preimage/absence status; run the bound pre-implementation gate before modification.

## Write Ownership

Worker owns only the four Allowed Paths. Local owns this work order, baseline, independent completion review, commit and continuity. The original Claude/Web returns and hash evidence are read-only. No agent may widen a path family or mutate the active handoff as a worker repair.

## Evidence Requirements

Worker evidence JSON records before/after hashes, exact changed set, three negative rows, first-return disposition, any failed/abandoned attempts, repair/help attribution, time boundaries and separate measured or null money/token/quota fields. Return names actual model/configuration as observed or operator-reported, with immutable snapshot UNKNOWN unless a real source verifies it. Static gate logs are not model-quality measurements.

## Review Gate

Local consumes the worker's valid proof, checks exact four-path diff and each accepted clarification, then independently challenges the three negative rows. Do not recreate worker implementation or call a provider for routine review. Any repair is grouped into one digest and scoped to allowed paths; if a different actor gate cannot be met, hold the independent-acceptance claim.

## Closure Checklist

Reviewer records actor independence, initial versus final outcome, repair attribution, unknown cost, no forbidden changes, required gate result, material commit and separate continuity commit. S3 closes only at its own bounded actual outcome; S4 learning use, S2 validator and S5 runtime need separate decisions.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with four owned files, a frozen diff and honest gate/evidence record. Return `BLOCKED_WITH_REASON` for changed seat identity, missing hard proof, out-of-scope requirement, invalid preimage or time ceiling. No silent fallback or second worker attempt.

## Operator Checkpoint

No model-selection question is routed to the Non coder. Local verifies the actual worker seat and existing operator-granted task authority before dispatch. If the operator changes outcome, rights, spend or topology, pause only the dependent action and incorporate that decision without expanding this order automatically.

## Work-Order Fulfillment Manifest

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"DOCTRINE","mandatory":true,"expectedArtifacts":["docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_DOCTRINE_DESIGN_2026-10-10.md"],"requiredProofIds":["R3_DOCTRINE_DIFF"]},{"requirementId":"CONTRACT","mandatory":true,"expectedArtifacts":["docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_CONTRACT_DESIGN_2026-10-10.md"],"requiredProofIds":["R3_CONTRACT_DIFF"]},{"requirementId":"RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_MODEL_SELECTION_S3_R1_WORKER_RETURN_2026-10-10.md","docs/reviews/evidence/model-selection-s3-r1-worker-20261010.json"],"requiredProofIds":["R3_RETURN_GATE"]}],"proofCatalog":[{"proofId":"R3_DOCTRINE_DIFF","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/model-selection-s3-r1-worker-20261010.json#doctrineDiff"},{"proofId":"R3_CONTRACT_DIFF","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/model-selection-s3-r1-worker-20261010.json#contractDiff"},{"proofId":"R3_RETURN_GATE","kind":"LOCAL_STATIC","locator":"docs/reviews/evidence/model-selection-s3-r1-worker-20261010.json#workerReturnGate"}]}
```

## Execution Plan

1. Local confirms actual worker seat/configuration, context and budget, records the frozen selection rationale and commits a released dispatch packet before transfer. Worker captures `executionBaseHead` and start time.
2. Worker reads exact owner sections and applicable checker sources, runs the bound pre-implementation gate, then edits only the two design drafts.
3. Worker checks the three negative cases against the text, records original and observed identity separately, runs scoped document/reviewer-fast checks, and prepares the evidence/return. One grouped repair is allowed within the same 45-minute attempt.
4. Worker freezes the four-file diff and returns uncommitted `COMPLETE_PENDING_REVIEW`; Local independently reviews and closes or issues one consolidated blocker. No automatic S4/S2 follow-on.

## Verification Commands

From repository root, after a clean committed release: `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md`; `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md`; `git diff --check`; `git status --short`. Worker reads checker source before authoring the worker return, uses the required checker-safe skeleton, and preserves first-run failures rather than replacing them with final PASS. Static documentation checks cannot prove a real provider-governance chain.

## Worker Autonomy / No-Question Rule

Worker resolves ordinary wording and grouped in-scope gate repairs. At a source contradiction, changed seat/configuration, mandatory authority/context/budget gap, out-of-scope file need or time ceiling, return one consolidated `BLOCKED_WITH_REASON` with exact owner and evidence. Do not ask the Non coder to pick a model. No worker self-selection, second model, tool-delegated subagent or automatic retry.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-MODEL-SELECTION-S3-R1-20261010
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"model-selection-s3-r1-design","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["post_web_r3_corrections_not_yet_applied"],"reopened":[],"current":["post_web_r3_corrections_not_yet_applied"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"MODEL-SELECTION-S3-R1-DISPATCH","claimClass":"DOCUMENTATION_ONLY","proofClass":"PROPOSAL_ONLY_NO_RUNTIME_READINESS","evidenceRef":"docs/baselines/CVF_GC018_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON - shared-workspace worker; no external architecture invocation.
High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - no locking, durable transaction, ownership/DACL or rollback implementation.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Manual B precedes schema/runtime | `docs/roadmaps/CVF_ORCHESTRATOR_MODEL_SELECTION_SYSTEM_CHAIN_ROADMAP_2026-10-10.md` | Work Plan And Exit Criteria | S3/S4/S2/S5 | roadmap | ACCEPT |
| Post-Web corrections | `docs/reviews/CVF_MODEL_SELECTION_WEB_REVIEW_LOCAL_DISPOSITION_2026-10-10.md` | Required Absorption Table | CVF-MS-WEB-01/04/06 | Local final review | ACCEPT |
| Selection and identity semantics | `docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_CONTRACT_DESIGN_2026-10-10.md` | Decision And Cost Semantics; Identity And Evidence Semantics | SelectionDecision; VersionEvidence | R2 contract design | ACCEPT |
| Six prior worker observations | `docs/reviews/CVF_WORKER_MODEL_SELECTION_PRELIMINARY_REPORT_2026-10-10.md` | Target / Source; Decision / Disposition | Haiku Max and Sonnet High worker-only rows | Local empirical review | ACCEPT |
| Dispatch and context owner | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | Required Fields; Context Eligibility Before Transfer | Dispatch Prompt Envelope | dispatch standard | ACCEPT |
| Parent learning branch | `docs/reference/downstream_gate_profile/CVF_PROJECT_LEARNING_LOOP_STANDARD.md` | Value Admission; Forward Application Binding | parent control receipts | PLL owner | ACCEPT |

The six-observation ACCEPT is bounded by the report itself: no exact snapshot, matched governance-design trial or bill exists.

## Intake Role Routing Decision

`INTERNAL_AGENT` worker in the shared private workspace; Local remains dispatcher and different-actor reviewer/closer. The completed Web phase was `EXTERNAL_ADVISORY_REVIEWER` and ended at Local disposition; no Web/remote actor is assigned implementation, review or closure. Provider/model identity does not change this workspace classification.

Intake summary: three accepted post-Web clarifications require one bounded private design edit and worker return.
Scope classification: two existing design drafts plus exact evidence and return; no executable implementation.
Risk sensitivity: private source and multi-role handoff, reversible documentation change, no external effect.
Selected role route: MULTI_AGENT_MULTI_ROLE.
Escalation condition: unavailable or mismatched selected seat, missing context/authority/budget proof, changed R2 source pin, extra path or 45-minute ceiling; hold dependent dispatch or return one consolidated blocker.
MULTI_AGENT_MULTI_ROLE: Local dispatcher -> shared-workspace INTERNAL_AGENT worker -> different-actor Local reviewer/closer; no Web implementation role.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/reviews/CVF_ACEL_AKOE_U1_UNREAL_AGENT_LOCAL_SOURCE_RECONCILIATION_2026-09-26.md"}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | Web advisory return -> integrity and Local seven-item disposition -> bounded INTERNAL_AGENT R3 design task |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | private R2 doctrine/contract drafts and Local Web disposition |
| Disposition | ADAPT findings 01/04/06 in existing design homes; 02/03/07 remain owner pointers; 05 remains deferred |
| Claim boundary | external review is advisory; Local owns private verification, implementation admission and final decision |

## Learning Application Plan

```learning-application-plan-json
{"schemaVersion":"cvf.learningApplicationPlan@1.0.0","bindings":[{"findingId":"NCR-LEARNING-APPLICATION-OBSERVABILITY","control":{"path":"governance/compat/learning_application_binding.py","sha256":"84068b6f197c19404a23daa643266d7f9ed334f313cd2d8bbe2f2e6d37d7b7b8"},"action":"Apply active first-return observability: initial disposition, failed attempts, repair/help attribution and separate parent-task burden while incorporating the three Local-accepted Web clarifications as an R3 design delta.","verificationPlan":"Compare pinned R2 sources, Local disposition and R3 four-file diff; inspect three static negative cases plus initial-return and repair fields during independent Local review."}]}
```

This dispatch plan does not claim that the worker has applied the learning or that a later decision has consumed it.

## Dated Owner Dependency Discovery

| Owned dated reference | Classification and reason |
|---|---|
| docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_DOCTRINE_DESIGN_2026-10-10.md | NOT_BINDING_REFERENCE_WITH_REASON: R2 design draft, not an active-window binding standard; edit remains inside its design scope |
| docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_CONTRACT_DESIGN_2026-10-10.md | NOT_BINDING_REFERENCE_WITH_REASON: R2 logical contract draft, not an active-window binding standard; edit remains inside its design scope |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py` |
| literalTokensReviewed | `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `acceptance-ledger-json`; `READY_FOR_REVIEW`; `COMPLETE_PENDING_REVIEW`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm reviewable packet structure; dispatch and implementation gates remain separate |
| claimBoundary | source/literal checks do not prove actual seat, cost, worker output or review acceptance |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`model-selection-design`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`. Returned defects: NONE_RETURNED, count 0. Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class model-selection-design --role dispatcher --lifecycle-phase pre-dispatch`. No returned ADIF ID waives substantive admission.

## Negative Search And Collision Discipline

The S3-R1 baseline/order and worker-output paths were absent before authoring; prior R2 drafts/reviews are deliberate inputs. The keyword search for `MODEL_SELECTION_S3_R1` under governed docs found no existing active order. No all-file or corpus-completeness claim is made.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MODEL_SELECTION_S3_R1_WORKER_RETURN_2026-10-10.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; Command Evidence; No-Commit Statement.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. Use N/A with reason when genuinely inapplicable. The worker also records source, checker read-ahead, first gate disposition and grouped repair.

## Reviewer Closure Conversion

Local reviewer owns the acceptance decision, completion review if required by the current closure rule, material commit and separate handoff/session sync. The worker must not commit or amend the previous Claude/Web evidence. Review by the same worker under a new role label is not independent; Local records actor separation and reconstructs the diff/source/return. Any claim about provider/model quality needs its own applicable evidence and risk-specific independent gate.

completionReviewPath: `docs/reviews/CVF_MODEL_SELECTION_S3_R1_COMPLETION_2026-10-10.md`
reviewerOwnedClosurePaths: `docs/reviews/CVF_MODEL_SELECTION_S3_R1_COMPLETION_2026-10-10.md`; active continuity only in a separate session-sync commit.

independentProbeRequired: YES

## Independent Review Probe Admission Contract

independentProbeRiskClass: DESIGN_SEMANTICS_AND_EVIDENCE_ATTRIBUTION
independentProbeDispositionAtDispatch: PLANNED_FOR_LOCAL_REVIEW
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: Worker checks its own edited text; Local independently compares the three negative cases to the pinned R2 sources and Local Web disposition.
positiveControl: Explicit assignment with only a predictive quality-history gap may SELECT, subject to separate admission and independent acceptance.
negativeMutationClasses: Missing mandatory context proof; material reviewer repair hidden by final artifact acceptance; retracted source cited as current evidence.
expectedInformationGain: Detect whether the R3 wording accidentally waives admission, inflates selected-model quality, or consumes stale evidence.
rerunCostReason: Three targeted text challenges are cheaper and more informative than duplicating the worker's entire edit or rerunning broad gates.
reviewerDecisionOwner: LOCAL

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_DOCTRINE_DESIGN_2026-10-10.md` | Minimal R3 clarification of assigned quality gap versus hard admission |
| `docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_CONTRACT_DESIGN_2026-10-10.md` | Outcome/learning links and three static negative rows |
| `docs/reviews/evidence/model-selection-s3-r1-worker-20261010.json` | Source/diff/gate/attempt/time/cost evidence |
| `docs/reviews/CVF_MODEL_SELECTION_S3_R1_WORKER_RETURN_2026-10-10.md` | Honest uncommitted return for independent Local review |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> shared-workspace worker -> Local independent reviewer/closer -> session-sync steward |
| phase | packet authoring; admitted design execution; review; closure |
| baseHeadFor(phase) | dispatchBaseHead=95ed2e98fbe034adf7f632e503a7844db4b02235; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact four worker-owned paths; baseline/order and continuity separately owned |
| traceScope(phase, actor) | each actor records own actual reads/actions/results |
| commitOwner(phase) | Local closer; WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | no other dirty tracked files at worker release |
| nextMoveSurfaces | active handoff and session state are steward-only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF
activeLaneOwner: distinct INTERNAL_AGENT design worker after committed dispatch
laneOwnedPaths: exact four Required Artifact Manifest paths
dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE
laneReleaseEvidence: terminal worker return, four-path changed-set reconciliation and empty staged set

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | Existing shared private workspace is the execution surface for the bounded internal worker |
| Contract source | archive-handled historical AHB contract `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; current `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | Existing dated design drafts plus return/evidence; no workspace storage is created |
| Handoff fields | AHB block above and explicit lane handoff own route, base, paths, return and commit |
| State ownership | Local session-sync steward updates active continuity after material disposition |
| Guard owner | Existing handoff, workspace-design, trace and autorun checkers |
| Build boundary | runtime source: no; provider proof: no; public-sync: no; registry edits: no; workspace UI/queue/runtime: no |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | Two existing dated model-selection reference design drafts only |
| Storage decision | Enrich the existing doctrine/contract homes; create no durable owner or parallel registry |
| Existing aggregate impact | none |
| Generated state impact | none during worker task |
| Durable governance boundary | design text remains a draft; R2 evidence is immutable; a later implementation needs its own authority |
| Duplicate-owner control | no new standard, checker, store or model-task map |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0
closeabilityDisposition: CLOSEABLE
outsideAuthorityBlockers: NONE
returnTimeRecheck: REQUIRED_BEFORE_REPAIR
implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT
foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | baseline/order | EXACT_PATHS | Local-closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | baseline/order | EXACT_PATHS | Local-closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | AGENT_HANDOFF_V63_2026-09-18.md material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| pre_implementation_autorun | IMPLEMENTATION | worker | IMPLEMENTATION | four allowed worker paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | two design drafts | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | dispatch_continuity,pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | evidence and return | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | focused_checker_tests |
| worker_return_fast | WORKER_RETURN | worker | WORKER_RETURN | four allowed worker paths | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | adif_integrity |
| reviewer_fast | REVIEW | reviewer | REVIEW | four worker paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | PRE_MATERIAL_COMMIT | reviewed worker paths and Local completion | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | POST_MATERIAL | reviewer | REVIEW | Local completion review | EXACT_PATHS | Local-closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | current continuity surfaces | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL_CLOSURE | reviewed material/continuity ranges | EXACT_PATHS | Local-closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

This graph assigns repair and commit owners; it does not report those future gates as passed. Actual seat admission and pre-dispatch release remain separate.

## Dual Agent Surface Matrix

| Surface | Role and use | Effect/cost boundary |
|---|---|---|
| INTERNAL_AGENT | selected AGENT_SEAT worker, Local reviewer/closer | one bounded shared-workspace task; seat invocation separately admitted |
| EXTERNAL_AGENT_CLI_MCP | none in this order | no research, tool delegate or external call |
| Adapter / Gateway API | not a worker path | no receipt, registry or API provider grant inferred |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-MODEL-SELECTION-S3-R1-20261010","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/CVF_GC018_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md","docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md","docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_DOCTRINE_DESIGN_2026-10-10.md","docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_CONTRACT_DESIGN_2026-10-10.md","docs/reviews/CVF_MODEL_SELECTION_S3_R1_WORKER_RETURN_2026-10-10.md","docs/reviews/evidence/model-selection-s3-r1-worker-20261010.json"],"claims":["POST_WEB_R3_DESIGN_CLARIFICATION_ONLY","MANUAL_B_SELECTION_WITH_SEPARATE_DISPATCH","NO_COST_SUPERIORITY_CLAIM"],"requiredProof":["R3_DOCTRINE_DIFF","R3_CONTRACT_DIFF","R3_RETURN_GATE"],"operatorCheckpoints":["ACTUAL_SEAT_CONTEXT_AND_BUDGET_ADMISSION_BEFORE_DISPATCH"],"forbiddenEffects":["PROVIDER_CALL","NETWORK_WRITE","PUBLIC_WRITE","DEPLOYMENT","REAL_DATA_MUTATION"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":null,"completenessClaimChanged":false}}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named source files and seven-item advisory disposition only; no repository corpus scan.

## Knowledge System Applicability

NOT_APPLICABLE_WITH_REASON: no corpus-to-knowledge map or new global learning store.

## Epistemic Process Block

Expected Result / Prediction: a bounded manual selection record can support a useful R3 documentation correction without model choice by the Non coder. Evidence Comparison: R2 contract, six limited worker observations and seven-item Local Web disposition are pinned; actual seat and outcome are not yet observed. Contradiction Or Gap Disposition: exact model snapshot, bill and task-matched quality remain unknown; dispatch binding is separate. Claim Update: proposed first work order only, no S3 execution or savings proof.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | manual AGENT_SEAT selection packet for private R3 design clarification |
| claimDisposition | CLAIM_REJECTED: no runtime model selector, universal agent-control or execution-enforcement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no worker, provider or runtime receipt exists for this packet |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source hashes, packet diff, ADIF resolver and dispatch gates only |
| invocationBoundary | packet authoring uses local read/write/checker tools; separate current-time worker admission required |
| interceptionBoundary | no wrapper, proxy, agent action interception or Gateway API control |
| claimLanguage | At packet creation, dispatch eligibility only; S3 outcome then awaited worker and independent Local review. See current Local Closure Receipt. |
| forbiddenExpansion | Expense, S2/S4/S5, direct provider call, runtime activation, public-sync, deployment |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-MODEL-SELECTION-S3-R1-20261010 --title "Model Selection S3-R1 Manual Design Task" --date 2026-10-10 --base 95ed2e98fbe034adf7f632e503a7844db4b02235 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_MODEL_SELECTION_WEB_REVIEW_LOCAL_DISPOSITION_2026-10-10.md --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key model-selection-s3-r1-design --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | generic-worker-dispatch, internal no-commit |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | task-specific source, selection, evidence, three negative cases, path manifest and review route authored directly |
| checkerReadAheadConfirmation | dispatch, convergence, learning, external-intake, workspace, storage, Delta, handoff, trace, scaffold and autorun checker families |
| docOnlyNewFields | R3 design clarifications only; no new runtime/schema/registry field |
| claimBoundary | authoring provenance only; no worker outcome or acceptance proof |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator acting as dispatcher and final technical decision owner |
| Provider or surface | private CVF workspace; no worker or provider invocation |
| Session or invocation | S3-R1 packet authoring, 2026-10-10 |
| Working directory | repository root |
| Command or tool surface | progressive startup and source reads; source hashes; Git status; ADIF resolver; packet edits; focused dispatch gates |
| Target paths | paired S3-R1 baseline and work order |
| Allowed scope source | operator instruction to proceed with the first work order; S3 roadmap and Local Web disposition |
| Before status evidence | clean worktree at `95ed2e98fbe034adf7f632e503a7844db4b02235` |
| After status evidence | two new dispatcher-owned artifacts staged; worker-owned paths unchanged |
| Diff evidence | `git status --short`; `git diff --cached --check` |
| Approval boundary | packet authoring and bounded Local selection only; actual seat dispatch requires current-time admission |
| Claim boundary | no worker outcome, model snapshot verification, live API, savings, public or production proof |
| Agent type | dispatcher |
| Invocation ID | `cvf-model-selection-s3-r1-packet-author-20261010` |
| Expected manifest | `docs/baselines/CVF_GC018_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_SELECTION_S3_R1_MANUAL_DESIGN_TASK_2026-10-10.md` |
| Manifest delta | MATCH at packet authoring; recheck before commit |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

At creation, this packet defined a concrete first work order and did not itself prove a worker invocation or S3 completion. The provisional choice was worker-only and did not choose or replace the active orchestrator seat. No provider/live, Gateway API, Expense, public or production claim follows.

## Local Closure Receipt

CLOSED_PASS_BOUNDED on 2026-10-11. Local completion: `docs/reviews/CVF_MODEL_SELECTION_S3_R1_COMPLETION_2026-10-10.md`; independent evidence: `docs/reviews/evidence/model-selection-s3-r1-local-review-20261011.json`. Earlier dispatch-time conditions describe packet creation, not the present state. The two worker R3 drafts and worker evidence JSON are accepted unchanged; Local added one attributed verdict-label format correction to the return. First gate FAIL and two worker self-repair rounds remain attributed to the worker. Model snapshot, effort and bill remain unknown; no S4/S2/S5 successor is opened.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | CLOSED_PASS_BOUNDED Local receipt | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MODEL_SELECTION_S3_R1_COMPLETION_2026-10-10.md` | independent Local probe and bounded disposition | PASS |
| Roadmap state | `docs/roadmaps/CVF_ORCHESTRATOR_MODEL_SELECTION_SYSTEM_CHAIN_ROADMAP_2026-10-10.md` | S3-R1 closed; S4/S2/S5 parked | PASS |
| Registry JSON | `docs/reviews/evidence/model-selection-s3-r1-local-review-20261011.json` | source pins, probe results and limitations | PASS |
| Registry Markdown | Local completion and worker return | distinct decision and original worker attribution | PASS |
| External evidence digest | `docs/reviews/CVF_MODEL_SELECTION_WEB_REVIEW_LOCAL_DISPOSITION_2026-10-10.md` | previously reconciled advisory; no new external intake | N/A with reason: internal worker return |
| System loop interlock | this work order | no Gateway, runtime or provider activation | PASS |
| Session continuity | active handoff and generated state/bootstrap | separate actual-material-SHA sync follows | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Worker return | `docs/reviews/CVF_MODEL_SELECTION_S3_R1_WORKER_RETURN_2026-10-10.md` present with four bounded changed paths | PASS |
| Independent Local acceptance | Local completion and source-derived probe identify distinct reviewer invocation and limited static result | PASS |
| Live runtime or provider receipt | N/A with reason: documentation design task did not exercise selector runtime or provider API | N/A_WITH_REASON |
| Closure claim | `CLOSED_PASS_BOUNDED` for S3-R1 manual design task only | PASS |
