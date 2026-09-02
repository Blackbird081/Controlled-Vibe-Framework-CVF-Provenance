# CVF Agent Work Order - MFRP-P4 Shadow Canary And Governance-Tax Measurement

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-02

Batch ID: MFRP-P4

Dispatch base head: `0b495a7177eaeb2af58141cea0069d7b01b925dc`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: bounded local P4 shadow-canary implementation and measurement worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_MEASUREMENT_2026-09-02.md`.

Paired baseline: `docs/baselines/CVF_GC018_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_MEASUREMENT_2026-09-02.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: P4 design and R1B-R2 evidence are accepted. P4 authoring
is open. This packet opens bounded implementation and the first real shadow
observation only; the trusted route remains controlling and P5 is closed.

Do-not-misread notes: do not use ignored historical receipts as evidence; do
not create phase work; do not review every return; do not treat consistency as
correctness; do not change P2 or reproduce phase semantics.

Required first actions: complete startup acknowledgement; capture clean HEAD;
read this packet/baseline and all pinned owners; recompute identities; run
pre-implementation; then touch exactly four paths.

Return contract: leave changes uncommitted and return one of
`CANARY_WINDOW_OPEN_EVIDENCE_CANDIDATE`, `ROLLBACK_SHADOW`,
`SIMPLIFY_CANARY_TAX_EXCEEDED`, or `BLOCKED_WITH_REASON`. Never emit reviewer
acceptance, P5 readiness or route replacement.

Worker: bounded local implementation/measurement worker

Reviewer/closer: reviewer/closer at initialization return, then M5, M10 and
final only unless a safety trigger fires

Worker return path: `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_WORKER_RETURN_2026-09-02.md`

successorTrancheOpened: NO

## Purpose

Implement the accepted comparator exactly once, execute a real shadow
observation against immutable R1B-R2 evidence, rehearse rollback, and establish
a bounded checkpoint ledger for empirical review-admission, recall and tax
measurement.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

Roles are execution labels only. Trust comes from immutable SOT identities,
actual P2 seams, explicit pair linkage, closed audit inputs and reviewer
adjudication of returned evidence.

Risk sensitivity: protected local governance code and false-confidence risk;
all provider/live/public/destructive effects are forbidden.

Intake summary: implement the already accepted P4 shadow design, generate one
honestly linked initial observation, and establish only the bounded checkpoint
measurement surface.

Scope classification: bounded local protected-governance implementation and
deterministic evidence measurement; no route, provider or external effect.

Escalation condition: only the safety and stop triggers in this packet.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP-P4
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

No pre-execution review is admitted. After initialization, no routine review
occurs per return; review is aggregated at M5, M10 and final. A safety trigger
may open an earlier evidence review but never a repeat of the phase work.

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-p4-shadow-canary",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["canary-not-implemented", "eligible-pair-not-observed", "review-recall-not-yet-estimable"],
    "reopened": [],
    "current": ["canary-not-implemented", "eligible-pair-not-observed", "review-recall-not-yet-estimable"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "MFRP-P4-DISPATCH",
    "claimClass": "SCHEMA_COMPATIBILITY",
    "proofClass": "EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST",
    "evidenceRef": "docs/baselines/CVF_GC018_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_MEASUREMENT_2026-09-02.md"
  }],
  "requiredDisposition": "READY_WITH_EXECUTABLE_PROOF",
  "successorScope": "EXECUTABLE_IMPLEMENTATION"
}
```

## Worker Autonomy / No-Question Rule

Resolve routine in-scope implementation and test details. Use reviewer-local
repair later for small evidence-determined findings under the Review Cost
standard; do not redispatch merely to reload worker context. Stop only for a
real authority/source/scope contradiction.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator canary instruction | operator messages dated 2026-09-02 | ACCEPT |
| accepted P4 contract | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` | ACCEPT |
| independent design acceptance | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_REVISION_1_INDEPENDENT_REREVIEW_2026-09-02.md` | ACCEPT |
| accepted actual-seam evidence | `docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md` | ACCEPT |
| proportional review/local repair | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | ACCEPT |

## Agent Roles

- Operator owns authorization and any material scope expansion.
- Dispatcher owns this contract.
- Worker implements four paths and records deterministic evidence.
- Reviewer evaluates returned evidence without recreating implementation.
- Closer commits accepted material and syncs continuity.

## Scope / Target / Owner Boundary

Allowed writes are exactly the Required Artifact Manifest. Read-only inputs are
the paired baseline/work order, accepted design/review/R1B evidence, actual P2
owners, autorun gate/AAF owners, Review Cost standard and checker sources.

Forbidden writes include every accepted input, P2 owner, gate/AAF owner,
standard, checker, hook, catalog, registry, session surface and roadmap.

## Required First Reads

1. startup surfaces required by `AGENTS.md`;
2. guard orientation and literal-format gotchas;
3. this work order and paired baseline;
4. accepted P4 design and independent rereview;
5. accepted R1B-R2 return, runner and ledger;
6. actual P2 receipt/readout owners and autorun/AAF call seams;
7. Review Cost standard and applicable checker sources.

## Pre-Flight Checks

- Capture clean `executionBaseHead` and confirm dispatch-base ancestry.
- Recompute every Opening Evidence identity.
- Confirm all four output paths are absent.
- Confirm ignored runtime receipts are not treated as historical evidence.
- Run pre-implementation against the captured base.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "MFRP-P4",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["governance/compat", "governance/compat/fixtures", "docs/reviews", "docs/baselines", "docs/work_orders"],
  "claims": ["bounded shadow-canary evidence only"],
  "requiredProof": [
    "accepted design R1B and P2 identities",
    "explicit return receipt linkage and trusted ordering",
    "actual P2 comparator and closed-input invariant",
    "deterministic sampling and rollback rehearsal",
    "M0-M2 plus initial observation metrics and exact four-path no-commit return"
  ],
  "operatorCheckpoints": ["fifth path", "P2 or SOT change", "P5 opening", "external effect"],
  "forbiddenEffects": ["trusted-route replacement", "worker commit", "provider network live public deploy production", "automatic P5 opening"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named source set",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P3_ELEVATED`; shadow route only. Full legacy gates remain.

## Required Artifact Manifest

| Path | Action |
|---|---|
| `governance/compat/mfrp_shadow_canary.py` | CREATE |
| `governance/compat/test_mfrp_shadow_canary.py` | CREATE |
| `governance/compat/fixtures/mfrp_p4_shadow_canary_evidence.json` | CREATE |
| `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_WORKER_RETURN_2026-09-02.md` | CREATE |

## Work-Order Fulfillment Manifest

Fulfillment is exact equality between the four required paths, the four actual
changed paths and the four paths named in the worker return. Any addition,
deletion or rename is a blocking manifest delta.

## Forbidden Path Manifest

Every repository path not listed above is forbidden for worker writes.
Temporary receipts must remain under one explicit ignored repository-bounded
`.cvf/runtime/mfrp-p4-shadow-canary/` directory and are not evidence owners.

## Required Proof Manifest

- identity and Git ancestry proof;
- actual P2 import/call proof and copied-evaluator negative test;
- explicit return/receipt pair-linkage manifest;
- trusted-record-before-shadow proof;
- comparator and deterministic sampling proof;
- P4-I1 closed-input audit proof;
- rollback rehearsal proof;
- M0-M2 plus initial observation tax/admission ledger;
- exact four-path, no-stage/no-commit and zero-provider proof.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | new bounded compat helper/test/evidence fixture plus review return |
| Storage decision | reuse existing directories; no folder, index, registry, cache owner or hidden durable store |
| Existing aggregate impact | none |
| Generated state impact | sunset-marked deterministic P4 evidence fixture only |
| Durable governance boundary | accepted design, P2 and trusted return remain owners; canary ledger is evidence only |

## Write Ownership

The worker owns uncommitted writes only to the four Required Artifact Manifest
paths. Reviewer/closer owns acceptance, material commit and continuity sync.
Checkpoint row additions remain within the same bounded evidence paths and do
not transfer authority to the worker.

## Actual-Seam And One-Command Contract

The helper must import the canonical P2 validator/readout behavior. It may
invoke the existing autorun gate inside one top-level shadow command when no
valid explicitly linked receipt exists. It records every internal subprocess
and duration; one top-level command cannot hide extra provider/network calls.

For the initial real record, bind:

- return path `docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md`;
- trusted commit `040ebfcff081062956c543f2b1d7e9cc04533b62` and blob
  `32154bdf225e600ca0622ebb5e25c6c97c9678eb`;
- trusted outcome `ACCEPT_R1B_R2_EVIDENCE_BOUNDED` as located in Independent
  Reviewer Adjudication;
- autorun range parent `cf899df3d0f49b14b7bd347282134d0133ade7be`
  through material commit `040ebfcff081062956c543f2b1d7e9cc04533b62`;
- hard-obligation locator: the return's Independent Reviewer Adjudication must
  retain C15 `FALSE_NEGATIVE`, C07/C08/C18 exclusions and P4 non-opening.

If the existing autorun gate cannot generate a valid receipt for that immutable
range without changing source, record the row as ineligible with the precise
class. Do not relax the gate or substitute a current unrelated receipt.

## Comparator, Sampling And Independent Audit

Implement every comparator field and allowed class from the baseline/design.
Reject unknown fields/classes, weak linkage, non-ancestor ordering and hidden
limitations fail-closed.

Implement the exact sample size formula and identity digest. Hostile tests
cover n=0..499 monotonic/capped behavior, tie-stable ordering and outcome-blind
selection.

Implement `P4-I1-DECLARED-AUTHORITY-AND-HARD-OBLIGATION-SURVIVAL` exactly from
the baseline. The audit receives an explicit closed manifest and refuses any
undeclared path or semantic re-execution command with
`AUDIT_INPUT_SCOPE_EXCEEDED`.

## Measurement And Checkpoint Contract

Initialize the evidence ledger with attributable M0-M2 values and the first
real observation. Use `NOT_YET_ESTIMABLE` where no positive-trigger recall
denominator exists. Do not claim saved cost during shadow mode.

The JSON top level must include schema/profile, design/R1B identities, opening
and sunset dates, checkpoint, population count, phase coverage, rows, sampling,
blind spots, admission metrics, tax metrics, safety triggers, rollback result,
limitations and claim boundary. It is bounded P4 evidence, not a registry.

After initialization acceptance, the same ledger/return may be updated at M5,
M10 and final without a new work order or pre-execution review, provided the
four-path boundary and pinned owners remain unchanged. Any implementation
change after initialization requires ordinary returned-result review; mere
deterministic row addition waits for the scheduled checkpoint unless a safety
trigger fires.

## Required Hostile Regression Matrix

- unrelated ignored receipt cannot be linked;
- tampered receipt/digest/verifier identity rejects;
- trusted commit missing/non-ancestor or machine-before-trusted rejects;
- comparison-object mismatch cannot map to clean consistency;
- C07/C08/C18 and C15 cannot be hidden or added to success denominators;
- outcome label agreement with failed P4-I1 still triggers finding;
- limitation/notChecked/UNCLASSIFIED removal rejects;
- sampling formula and ordering cannot be outcome-selected;
- undeclared audit input and semantic replay command produce scope excess;
- always-clean comparator/evaluator weakening is caught;
- rollback leaves trusted blob/outcome and repository tracked bytes unchanged;
- two same-base executions produce byte-identical evidence except explicitly
  excluded duration fields.

## Execution Plan

1. Freeze identities and run pre-implementation.
2. Implement fail-closed comparator, linkage, sampling and P4-I1 audit.
3. Implement hostile tests and rollback rehearsal.
4. Execute the first real R1B-R2 shadow observation.
5. Write bounded evidence JSON and full worker return.
6. Run focused suite twice, reconcile exact four paths and stop uncommitted.

## Acceptance Criteria

- exact four-path changed set and clean starting base;
- all pinned identities and ordering evidence match;
- actual P2 seams run without copied evaluator;
- first pair is explicitly linked or honestly classified ineligible;
- comparator/sampling/P4-I1/rollback hostile suite passes;
- M0-M2 and initial metrics are evidence-bound without false recall/saving;
- trusted outcome remains controlling and byte-unchanged;
- zero external/provider/live/network calls;
- worker stages/commits nothing and opens no successor.

## Evidence Requirements

Record execution base, every pinned/recomputed identity, actual subprocess and
input manifest, receipt linkage and ordering, comparator/audit/sampling output,
rollback hashes, M0-M2 and initial measurement totals, limitations, focused
tests, exact changed set, zero external calls and no-stage/no-commit evidence.

## Stop Conditions

Stop for any baseline stop condition, need for a fifth path or P2/design/SOT
change, inability to keep trusted outcome controlling, secret risk, provider
need, nondeterminism, or pressure to manufacture population/safety/cost claims.

## Return-To-Orchestrator Conditions

Return `CANARY_WINDOW_OPEN_EVIDENCE_CANDIDATE` only if implementation, rollback
and honest first observation are complete. A zero-eligible result may still be
complete only when it records `BLOCKED_NO_ELIGIBLE_NATURAL_PAIR` and makes no
canary-safety claim. Use the other exact terminal tokens when their conditions
apply. Never return reviewer acceptance or P5 opening.

## Operator Checkpoint

No further operator input or pre-execution review is required for exact
four-path initialization. Routine reviewer checkpoints are initialization
return, M5, M10 and final; safety triggers may advance a review. Scope/P2/SOT,
external effect or P5 requires operator authority.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short
git diff --cached --name-status
python -B governance/compat/test_mfrp_shadow_canary.py
python -B governance/compat/mfrp_shadow_canary.py --help
python governance/compat/run_worker_return_fast_gate.py
```

Use the helper's documented CLI for the initial observation and run it twice
against the same immutable input; compare normalized evidence bytes.

## Evidence Reuse And Encoding Plan

| Evidence | Mode | Encoding |
|---|---|---|
| accepted design/R1B/P2 owners | RECOMPUTE_REQUIRED | raw SHA-256 and Git commit/blob |
| M0-M2 admission evidence | REUSE_PRIOR_VERIFICATION | committed UTF-8 Markdown locators |
| new receipt/readout/comparator | REVIEWER_RECOMPUTE_ONLY | RFC 8785 JCS where owned; UTF-8 JSON/Markdown |

Provider-specific memory is `NOT_CVF_SOURCE`.

## Negative Search And Collision Discipline

All four output paths were absent at dispatch authoring. Existing runtime
receipt filenames collide only as ignored mutable caches and are forbidden as
historical evidence without the new explicit linkage manifest.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P4 contract | accepted design | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` | population through rollback | shadow canary | accepted design | ACCEPT |
| P4 acceptance | review evidence | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_REVISION_1_INDEPENDENT_REREVIEW_2026-09-02.md` | disposition/acceptance boundary | design identity | reviewer | ACCEPT |
| trusted initial record | accepted evidence | `docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md` | adjudication and M2 | commit/blob/return | R1B-R2 evidence | ACCEPT |
| P2 receipt mechanics | executable source | `governance/compat/agent_autorun_machine_verification.py` | validator/digest | `_validate_receipt_integrity` | P2 receipt owner | ACCEPT |
| P2 readout mechanics | executable source | `governance/compat/agent_automation_machine_verification_readout.py` | read/build/serialize | readout functions | P2 readout owner | ACCEPT |
| review tax routing | canonical standard | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | admission/local repair | review cost | standard owner | ACCEPT |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: bounded named local evidence; no corpus scan or
external knowledge absorption claim.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | prior critique/review evidence -> CVF adjudication -> accepted P4 contract -> local canary |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | accepted P4 design, independent rereview and this work order |
| Disposition | NO_NEW_ABSORPTION |
| Claim boundary | external statements are not runtime truth |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`shadow canary governance tax measurement`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

Disclosed defectIds: NONE

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch/no-commit fields; review admission; Source Verification; protected paths; worker-return profile |
| gateRunPurpose | confirm the completed P4 packet and later collect returned evidence |
| claimBoundary | PASS does not prove safety, recall, savings or P5 readiness |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P4 --title "Shadow Canary And Governance-Tax Measurement" --date 2026-09-02 --base 0b495a7177eaeb2af58141cea0069d7b01b925dc --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --root-cause-cluster-id mfrp-machine-first-review-canary --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence ACCEPTED_R1B_R2_AND_ACCEPTED_P4_DESIGN --scec-problem-key mfrp-p4-shadow-canary --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | protected-governance-path internal no-commit initial |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact P4 identities, natural population, checkpoints, P4-I1, receipt linkage, tax/recall and rollback |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | bounded comparator and measurement ledger fields |
| claimBoundary | provenance only; no outcome predeclared |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create exactly the helper, focused test,
bounded evidence fixture and worker return. No existing protected source may
change.

Protected paths:

- `governance/compat/mfrp_shadow_canary.py`
- `governance/compat/test_mfrp_shadow_canary.py`
- `governance/compat/fixtures/mfrp_p4_shadow_canary_evidence.json`

Operator authorization: explicit 2026-09-02 instruction to run the canary and
collect empirical review-reduction/recall evidence.

Rollback boundary: remove the exact four uncommitted outputs and verified
ignored P4 receipt directory only.

## Commit Mode And Base-Anchor Lifecycle

dispatchBaseHead: `0b495a7177eaeb2af58141cea0069d7b01b925dc`

executionBaseHead: worker captures a clean descendant at start.

closureBaseHead: reviewer captures after accepted material commit.

Worker commit is forbidden; reviewer/closer owns material and continuity.

## Single-Agent Multi-Role Control Block

Route is MULTI_AGENT_MULTI_ROLE. Authority does not transfer if one runtime
performs multiple labels. Worker self-checks are not acceptance; reviewer
checks returned evidence without repeating implementation or phase work.

| Control | Binding |
|---|---|
| role separation ledger | operator authorizes; dispatcher scopes; worker implements/measures; reviewer evaluates; closer commits |
| self-review boundary | worker tests and self-report are evidence candidates, never independent acceptance |
| escalation conditions | identity/order/linkage contradiction, fifth path, P2/SOT need, safety trigger, secret or external effect |
| evidence basis independent of memory | pinned repository bytes, Git commit/blob ancestry, actual P2 output and deterministic ledger |
| gate sequence | pre-dispatch -> pre-implementation -> focused suite -> worker-return gate -> reviewer/closure |

## Dual Agent Surface Matrix

| Surface | Status | Authority boundary |
|---|---|---|
| INTERNAL_AGENT | AUTHORIZED | exact four-path local no-commit worker |
| EXTERNAL_AGENT_CLI_MCP | FORBIDDEN | zero invocation/quota |
| adapter boundary | NOT_APPLICABLE_WITH_REASON | direct local P2 imports only |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator -> dispatcher -> bounded worker -> reviewer/closer |
| phase | P4 initialization pending worker return |
| baseHeadFor(phase) | dispatch base fixed; execution base worker capture; closure base reviewer capture |
| changedSetScope(phase) | exactly four new paths |
| traceScope(phase, actor) | identities, pair linkage, comparator, audit, rollback, metrics and gates |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no P2/design/R1B/standard/checker/session change |
| nextMoveSurfaces | initialization review, then M5/M10/final or safety trigger |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_COMPLETION_2026-09-02.md`

reviewerOwnedClosurePaths: the exact four worker outputs, conventional
completion review only if materially needed, and later continuity sync.

Reviewer reruns focused tests, recomputes identities/linkage, challenges one
hostile case and confirms rollback. Reviewer does not recreate comparator code
or phase work. Small localized evidence-determined defects are repaired once
in place under the Review Cost standard.

## Worker Output Checker Read-Ahead Mandate

Read all return-shape checkers before writing the return. Use the wrapper gate;
individual checker substitution is forbidden.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Return includes the full governed shape, exact work-order binding, execution
base, four changed paths, command/identity/linkage/comparator/audit/rollback
evidence, cost/admission metrics, no-commit proof and claim boundary.

## Review Gate

Routine review occurs once at initialization return, then M5, M10 and final.
Safety triggers may cause early review. Reviewer evaluates evidence and does
not repeat the phase, implementation or agent reasoning.

## Closure Checklist

- [ ] clean base and exact four paths;
- [ ] opening identities and order-of-record pass;
- [ ] actual P2/linkage/comparator/sampling/P4-I1 tests pass;
- [ ] rollback preserves trusted result;
- [ ] M0-M2 and initial metrics remain honest;
- [ ] zero provider calls and no worker commit;
- [ ] `successorTrancheOpened: NO` exact.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/author |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P4 dispatch authoring |
| Working directory | repository root |
| Command or tool surface | governed reads, hashes, apply_patch and gates |
| Target paths | paired P4 baseline and work order |
| Allowed scope source | operator canary instruction and accepted P4/R1B evidence |
| Before status evidence | clean worktree at `0b495a7177eaeb2af58141cea0069d7b01b925dc` |
| After status evidence | exactly two untracked dispatch artifacts |
| Diff evidence | status plus unstaged/staged name-status |
| Approval boundary | dispatch authoring only; no worker outcome |
| Claim boundary | no safety/recall/saving/P5/external claim |
| Agent type | dispatcher/author |
| Invocation ID | `mfrp-p4-dispatch-authoring-2026-09-02` |
| Expected manifest | paired P4 baseline and work order |
| Actual changed set | paired P4 baseline and work order |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | P4 dispatch authority only |
| claimDisposition | CLAIM_REJECTED: no canary outcome, recall, saving or P5 readiness claimed |
| receiptEvidence | N/A with reason: worker has not generated the linked shadow receipt |
| actionEvidence | N/A with reason: implementation has not executed |
| invocationBoundary | local authoring and gates only |
| interceptionBoundary | trusted route unchanged |
| claimLanguage | dispatch-ready bounded shadow measurement |
| forbiddenExpansion | no route replacement, P2, P5, provider/live/public/deploy effect |

## Claim Boundary

This work order authorizes exactly one four-path no-commit P4 initialization
and a bounded M5/M10/final evidence window. It does not change controlling
review, prove correctness/recall/savings, open P5, or authorize external
effects.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance canary dispatch; public sync is forbidden.
