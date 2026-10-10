# CVF Orchestrator Model Selection Contract Design

Memory class: FULL_RECORD
docType: reference
Status: DESIGN_DRAFT
Date: 2026-10-10
Batch ID: CVF-WORKER-SELECTION-FOUNDATION-20261010
Proposed contract ID: cvf.orchestrator-model-selection-advisory@0.2.1
Revision: R2 - R1-B1 corrected; conditional reviewer concurrence recorded by Local

## Purpose

Specify a prospective selection-rationale block owned by the existing work order
and dispatch envelope for AGENT_SEAT (surface B). Begin with manual records on an
admitted real task. The field families below are logical sections, not six new stores
or a prerequisite schema service. GATEWAY_API (surface A) is deferred; GatewayReceipt
owns only its future companion. No executable schema or persistence owner is installed.

## Scope / Applies To

Optional orchestrator selection for an admitted task. Normative wording below is
reviewed design semantics, with conditional R2 concurrence recorded. A manual decision would bind
to an independently admitted task/order. Any schema/validator implementation requires
a fresh implementation work order. B authority: existing work-order template,
dispatch envelope, role matrix and delegation standard named in the doctrine.
For A, docs/reference/CVF_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_2026-06-28.md,
Receipt Advisory requires fresh GC-018 for a companion; this design does not grant it.
Doctrine proposal: docs/reference/CVF_ORCHESTRATOR_MODEL_SELECTION_DOCTRINE_DESIGN_2026-10-10.md.

## Record Families And Required Joins

| Record | Proposed required fields | Producer -> verifier -> consumer |
|---|---|---|
| TaskProfile | taskId, taskArtifactRef, surface, role, outcome, acceptanceCriteriaRefs, requiredMethods/tools, integration/proofNovelty, risk/dataClassification, hardConstraints, budgetUnits, authorityRefs, choiceAuthorityRef (assignment or delegated choice), operatorAssignment or null, provisionalEnvelopeDisposition | intake/dispatcher -> existing task/authority owners -> orchestrator |
| CandidateConfiguration | candidateId, provider/productId, modelId/alias, snapshot or null, identityBasis per observed field, aliasResolution, channel, effort, harness product/version/settings with unknowns, tool profile, hashes only for captured material, role, capabilityRefs, surfaceAdmissionRefs, contextEligibilityRef where required | seat configuration for B or registry for A -> applicable admission owners -> orchestrator |
| VersionEvidence | evidenceId, candidateId, evidenceClass, claim, locator/section, sourceRevision or capturedHash, retrievedAt, sourceAsOf, methodologyRef, configurationMatch, taskApplicability, limitations, freshnessDisposition | source intake -> Local applicability review -> orchestrator |
| SelectionDecision | decisionId, contractVersion, taskProfileRef/hash, candidateSnapshotRef/hash, evidenceSnapshotRef/hash, decisionOwner, decidedAt, candidateDispositions, selectedCandidateId or null, rationale, qualityDisposition, confidenceReason, costBasis, learningInputs, operatorAssignmentDisposition, predecessorDecisionRef or null, executionAuthorized=false | orchestrator -> existing dispatcher/admission review -> future dispatch |
| ReviewedOutcomeLink | outcomeId, decisionRef/hash, executionAttemptRef, observedConfiguration, identityEvidence, returnRef/hash, independentReviewRef/hash, technicalDisposition, procedureDisposition, repairAttribution, telemetry, deviations | execution/reviewer -> existing review and custody owners -> learning intake |
| LearningConsumptionLink | laterDecisionId, branch (PARENT_CONTROL or LOCAL_OBSERVATION), sourceRef/hash, applicabilityReason, actionOrNoChangeReason, verificationRef/hash or null; branch-specific disposition | later orchestrator -> later reviewer -> later task's existing decision/review evidence |

B surfaceAdmissionRefs name the admitted seat/task, permitted tools, topology and
role/context declaration. A instead requires current policy/registry/capability/health
evidence. A seat cannot fabricate an isRoutable result or GatewayReceipt. Report
missing owner evidence as unresolved; do not mark the other surface's checks PASS.

All references are explicit locator plus revision/hash and read scope. Evidence-only
web sources never become authorityRefs. Required nulls have reasons; no unknown values
default to zero, SUPPORTED or SELECT. Final implementation must define strict types,
required/optional fields, enums and cross-record validation under existing owners.

## Minimum Manual Record And Evidence Homes

For the first B task, one selection-rationale section in the governed work order
records: task/role/surface and choice authority; observable floor and provisional
envelope; candidates with configuration/evidence pins and rejection reasons; chosen
candidate or hold; cost/capacity units and unknowns; consumed controls/observations;
freeze anchor and next verification. Existing release/admission rules still apply.
The dispatcher owns that record; the admitted task's reviewer owns its outcome links.

Outcome facts remain in the task's single existing review/evidence record. The six-row
legacy tranche ledger remains read-only evidence, not backfilled or a second future
outcome store. ReviewedOutcomeLink references that canonical task record. Later
consumption lives in the later task's decision/review section, not a global new ledger.
Exact future artifact paths are declared by that task before execution; none is created
here. Machine format and validation are demand-gated after useful manual-loop evidence.

## Identity And Evidence Semantics

Candidate identity is the tuple provider/model/snapshot/channel/effort/harness/tools/role.
Identity basis: VERIFIED_RUNTIME, OFFICIAL_CATALOG, OPERATOR_REPORTED or UNRESOLVED.
Catalog evidence identifies a published option; only execution telemetry can verify
the actual invoked configuration. Keep requested and observed identities separate.
Matching operator labels never upgrades an execution identity to VERIFIED_RUNTIME.
B identity normally remains OPERATOR_REPORTED unless actual harness telemetry verifies
the claimed fields. Product/version/settings and tool access may be recorded even when
the harness exposes no snapshot or byte hash; unknowns stay null with reasons.

Evidence classes: OFFICIAL_TECHNICAL_REPORT, OFFICIAL_MODEL_OR_SYSTEM_CARD,
ORIGINAL_BENCHMARK_METHOD, PROVIDER_REPORTED_EVALUATION, INDEPENDENT_PUBLISHER_EVALUATION,
LOCAL_REVIEWED_OUTCOME, OFFICIAL_TARIFF and MEASURED_BILLING. Classification records
who measured the result; hosting on a benchmark site does not imply independence.
Paper publication does not imply peer review. Scores require metric, dataset/version,
sampling/scaffold, effort/tools, evaluation date and tested version; unknowns disclosed.

Freshness dispositions: CURRENT_FOR_DECISION, STALE, CONFLICTING or UNRESOLVED.
Compatibility: EXACT, PARTIAL or NONTRANSFERABLE with reason. An old version may
inform a hypothesis via PARTIAL; it cannot supply a new version's Local pass or score.
Absence of official technical papers is a recorded limitation, not invented evidence.

| Configuration evidence | Maximum applicability | Required treatment |
|---|---|---|
| Both references bind the same immutable snapshot and all material effort/harness/tool conditions through official metadata or observed telemetry | EXACT for those documented conditions | still distinguish catalog identity from executed identity; undisclosed material dimensions prevent EXACT |
| Same alias/effort but snapshot or harness version hidden | PARTIAL | record evidence window, known settings, source basis and next refresh trigger; no score inheritance |
| Different version or material harness/tool change | PARTIAL only for a justified transferable mechanism; otherwise NONTRANSFERABLE | never relabel the old outcome as a pass for the new configuration |
| No usable model/configuration identity | NONTRANSFERABLE | HOLD_EVIDENCE for configuration-dependent claims |

An official catalog entry alone does not prove a worker ran that snapshot. EXACT is
claim-relative configuration matching, not a proof class or automatic SUPPORTED.
PARTIAL can support a bounded quality judgment; admission depends on the actual floor.
Each alias-only record declares observedFrom/observedThrough and reassessAt (next
dispatch); check visible version/settings changes and new material conflicts then.
Unknown hidden changes remain a confidence limit even when no visible drift appears.
Retain source locator/revision, bounded excerpt or summary, retrieval time and retained
content hash. A hash of an uncaptured page cannot reconstruct historical evidence.

## Decision And Cost Semantics

Decision outcomes: SELECT, HOLD_NO_ELIGIBLE_CANDIDATE, HOLD_EVIDENCE or
HOLD_OPERATOR_CONSTRAINT. Each candidate has a separate admission disposition,
quality disposition and preference explanation. SELECT requires at least one eligible
candidate and exactly one selected candidate, within a recorded assignment or delegated
choice and an explicit applicable acceptance floor; a hold has selectedCandidateId=null.
An empty candidate set cannot pass. Absent quality evidence holds delegated selection;
the explicit-assignment branch below records the gap without treating it as quality PASS.

No choice delegation and no explicit assignment yields HOLD_OPERATOR_CONSTRAINT
for autonomous SELECT; a recommendation is still allowed. For an explicit operator
assignment, absence of quality evidence alone does not hold: SELECT the assigned
candidate and record `operatorAssignmentDisposition=HONORED_WITH_EVIDENCE_GAP`,
the missing evidence, confidence limit and mandatory independent acceptance against
the unchanged floor. Keep qualityDisposition=INSUFFICIENT when warranted; this is
an assignment disposition, not a quality upgrade or invocation grant.
Hold an explicit assignment for unavailability, authority/policy/method/context
conflicts, or a known failed hard requirement. Existing task/budget/effect admission
remains required. Missing quality evidence must not be relabeled as known failure.
The orchestrator seat itself is excluded from self-selection.
For delegated selections, SUPPORTED/PROVISIONAL follow the doctrine's Decision
Procedure And Uncertainty: PROVISIONAL needs relevant positive evidence and the
bounded reviewed-task envelope; INSUFFICIENT, zero quality evidence, unresolved
material contradiction or a known failed hard floor holds. Explicit assignments use
the branch above. Each hold records a concrete reason and its authority owner.
Reviewer model eligibility is additional to actor/context eligibility under
docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md,
Context Eligibility Before Transfer. A disallowed context yields a hold even for
a well-qualified model. This proposal cannot waive existing review/authority gates.

CostBasis separates measured amounts, estimates and unknowns. For each stage
(orchestration, preparation, execution, review, rework), record amount or null,
currency/unit, telemetry/sourceRef, time boundary and confidence. Provider request
cost uses a dated tariff with its actual channel, prompt thresholds and modifiers.
Total estimates are valid only with disclosed missing stages and assumptions;
measured total requires complete comparable stage receipts. Hard limits require
a defensible bound in that limit's units or hold. Capacity units may be money,
tokens, quota units/share with denominator and reset window, rate limits or wall-clock.
Do not sum unlike units. For a quota-only cap, unknown currency does not block capacity
admission; for a monetary cap, unknown monetary exposure still blocks. Evidence of
zero incremental charge must be explicit. Subscription allocation needs an explicit method.
Never compare estimatedTokens directly to a monetary costBudget.

## Freeze, Drift And Transition Contract

Proposed decision states: DRAFT -> FROZEN -> BOUND_TO_DISPATCH -> OUTCOME_LINKED
-> LEARNING_DISPOSITIONED. A hold may terminate a
decision without execution. These are selection record states, not replacement CVF
lifecycle phases, dispatch authority or parent learning states.

FROZEN pins source bytes and task/configuration/evidence identity before execution.
Binding requires an independently admitted work order and its actual authority.
Record each transition as an appended event referencing the frozen decision hash;
never edit frozen decision bytes to update a state. Store successors on material drift.
Fallback may use only an admitted alternative and retry/attempt budget; otherwise hold.
Reassess data/role/method/version/effort/harness changes before dispatch. Returned
identity mismatch is reviewed as a deviation; an outcome cannot silently validate
the originally selected configuration.

LEARNING_DISPOSITIONED means evidence routing is decided, including no reusable lesson;
it does not mean a lesson was delivered, applied or effective. The earlier decision
can end with zero consumers. One or many later decisions each own a separate link
to it, so later use never mutates or reopens the earlier record.

PARENT_CONTROL links identify parentFindingId, exact control and existing typed PLL
DELIVERY/APPLICATION receipts under
docs/reference/downstream_gate_profile/CVF_PROJECT_LEARNING_PARENT_EVIDENCE_CONTRACT.md.
APPLIED requires its existing authorization and verification; a plan/citation is not
enough. LOCAL_OBSERVATION links instead record CITED, ACTION_VERIFIED or
NO_CHANGE_REASONED in the later decision/review. These are evidence-use labels, not
PLL states or a new learning lifecycle. ACTION_VERIFIED needs a reviewer-checked
action/result; NO_CHANGE_REASONED records justified applicability without improvement.
Both branches retain concrete source pins and limits. Local outcomes only enter
F2G/PLL if the separate value-admission checks justify an actual reusable control.

B freeze and identity checks are cooperative evidence controls, not host interception.
Observed or reported deviations are disclosed; unobserved silent changes remain unknown.

## Prospective Acceptance And Negative Matrix

| Scenario | Required disposition | Proof boundary |
|---|---|---|
| Exact version/task evidence, admitted candidate, frozen rationale | SELECT and explicit dispatch binding only when separate grant exists | static contract plus future actual use |
| Non coder supplies outcome without model | orchestrator derives candidates; no required technical picker | actual intake/decision use |
| Cheap candidate violates applicable seat/route policy or method | reject before cost comparison | existing authority plus future composed negative |
| Empty candidate set | HOLD_NO_ELIGIBLE_CANDIDATE | no vacuous eligibility |
| Delegated selection with empty quality evidence | HOLD_EVIDENCE | no autonomous evidence-free quality selection |
| New snapshot reuses old score as exact | reject transfer; preserve old record | identity/applicability negative |
| Operator assignment conflicts with authority | hold and name constraint; no silent override | admission and operator boundary |
| Worker qualified, reviewer role requested | require reviewer evidence/authority or hold | cross-role negative |
| Token count used as money, missing bill set to zero | reject units/default; preserve null | cost-dimensional negative |
| Task/harness changes after freeze | successor decision and revalidation before effect | drift negative |
| Selected/observed model mismatch | outcome deviation; no original-configuration promotion | execution identity join |
| Retry without remaining grant | hold; preserve prior failed attempt | existing attempt authority |
| Learning plan with no actual result | PARENT_CONTROL remains NOT_APPLIED; LOCAL_OBSERVATION at most CITED | separate parent-control and local-evidence semantics |
| Expense parked | no project edit/test/benchmark for learning | operator scope boundary |
| B seat has no GatewayReceipt | use task/dispatch admission and selection block; no gateway prerequisite | surface split |
| No model-choice authority | HOLD_OPERATOR_CONSTRAINT; recommendation only | role matrix |
| Explicitly assigned model with a known failed hard requirement | HOLD_OPERATOR_CONSTRAINT; no silent substitution | actual conflict/failure distinguished from absent evidence |
| Explicitly assigned available model with no quality evidence and no other hard conflict | SELECT assigned model; HONORED_WITH_EVIDENCE_GAP; mandatory independent acceptance | unchanged acceptance floor; no SUPPORTED upgrade |
| Alias-only identity with relevant evidence on an admitted low-risk independently reviewed task | at most PARTIAL; PROVISIONAL SELECT within the defined envelope | no fabricated snapshot or extra Non coder model question |
| Delegated high-risk task with insufficient quality/version evidence | technical/authority-owner disposition or HOLD_EVIDENCE | explicit assignment uses its own branch; no waiver of actual hard constraints |
| Qualified reviewer model in a prohibited author context | hold before transfer | context eligibility owner |
| Earlier outcome has zero, one or many later consumers | earlier decision terminal; each later task owns its own link | append-only one-to-many joins |
| Quota-only cap with currency unknown | compare quota/window; no currency conversion | unit-safe capacity evidence |
| Two candidates pass | choose exactly one with rationale | no exactly-one-eligible restriction |

This matrix specifies future checks; none are reported as executed behavior here.

## Epistemic Process Block

Expected Result / Prediction: explicit identities and joins should prevent stale
evidence transfer and unsupported learning-use claims.
Evidence Comparison: existing registry, receipt and PLL owners supply boundaries;
this artifact supplies proposed fields and negative obligations only.
Contradiction Or Gap Disposition: machine validation, persistence, exact runtime
identity capture and composed use remain unimplemented by this design.
Claim Update: DESIGN_DRAFT; no executed contract acceptance or runtime receipt.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Local INTERNAL_AGENT; internal design; final technical decision owner=Local.
Conditional R2 concurrence is from the original reviewer, verified against the
corrected paragraphs by Local; it is not a second independent review.
No new schema authority, dispatch, router,
provider/live proof, public export, production or universal compliance claim.
