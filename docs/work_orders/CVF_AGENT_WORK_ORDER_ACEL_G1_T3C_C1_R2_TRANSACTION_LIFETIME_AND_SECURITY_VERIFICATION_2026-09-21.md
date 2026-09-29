# CVF Agent Work Order - ACEL G1 T3C-C1 R2 Transaction Lifetime And Security Verification

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-21

Batch ID: ACEL-G1-T3C-C1-R2-TRANSACTION-LIFETIME-AND-SECURITY-VERIFICATION

Dispatch base head: `dcba5f7f017af96ae2f61c1ddc5cbf54fe69945d`

dispatchBaseHead: `dcba5f7f017af96ae2f61c1ddc5cbf54fe69945d`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: N/A_PENDING_REVIEW

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: shared-workspace `INTERNAL_AGENT` R2 correction worker. Repair the same
four uncommitted T3C-C1 outputs; Local independently reviews and commits.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_2026-09-21.md`.

Paired baseline: `docs/baselines/CVF_GC018_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_2026-09-21.md`.

Independent review: `docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: R1 repaired the original five findings and all returned
suites pass. Local found three residual transaction-lifetime/security-proof
defects. HEAD is `dcba5f7f0`; thirteen unrelated parked paths remain outside
this lane; the real Group 3 log remains absent.

Do-not-misread notes: do not restart the five accepted R1 repairs, create a
fifth worker path, use credentials, run as Party B, read the real registry,
create the real log, edit dispatcher artifacts, stage or commit.

Required first actions: acknowledge startup authority; capture HEAD/status and
empty staging; read this packet, paired R2 baseline, R1 completion review, R1
work order and all four pending outputs; run pre-implementation before editing.

Return contract: leave exactly four worker outputs uncommitted and staging
empty. Return `COMPLETE_PENDING_REVIEW` only after every R2 item and the
worker-return fast gate pass. Use `BLOCKED_WITH_REASON` only for an irreparable
out-of-scope blocker.

Worker: bounded internal correction worker

Reviewer/closer: CVF Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md`

successorTrancheOpened: NO

## Purpose

Close the three residual R1 findings with a transaction-wide exclusion guard,
rollback ownership from the first filesystem mutation, exact security-state
capture/read-back verification and adversarial hermetic regressions.

## Agent Roles

- Worker: shared-workspace `INTERNAL_AGENT`, implementation and hermetic proof.
- Reviewer/closer: CVF Local orchestrator/reviewer, independent probe and commit.
- Operator: retains every real-principal and real-source checkpoint.

## Required First Reads

Read `CVF_SESSION_MEMORY.md`, the bootstrap model, active handoff, guard
orientation README, literal-format gotchas, this work order, paired R2
baseline, R1 completion review, R1 work order and all four owned outputs.

## Pre-Flight Checks

Capture exact HEAD/status/staging, reconcile the four worker paths and thirteen
parked paths, verify the real log is absent, then run the pre-implementation
autorun gate. Stop before editing on any unexplained drift.

## Write Ownership

The worker may edit only the exact four paths in Required Artifact Manifest.
The R2 baseline/work order/review, continuity surfaces, parked paths and real
source paths are read-only. Local alone stages and commits accepted work.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator role instruction | operator authorized Local audit and worker dispatch | ACCEPT |
| R1 completion rejection | `docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md`; SHA-256 `877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8` | ACCEPT |
| paired R2 baseline | `docs/baselines/CVF_GC018_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_2026-09-21.md` | ACCEPT |
| Group 3 contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`; Source Group 3 | ACCEPT |
| R1 work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_2026-09-21.md` | ACCEPT_UNAFFECTED_RULES_ONLY |

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE` within one shared workspace. The worker
owns implementation and hermetic evidence only. Local owns independent probes,
disposition, commit, real-principal checkpoints and session sync. External
research is not applicable.

Intake summary: one Local-reviewed internal correction lane reuses the exact
four-path manifest; there is no external intake, live run or real-principal
source action.

Scope classification: bounded local code/test/evidence correction with durable
append and filesystem-security sensitivity.

Risk sensitivity: high because premature exclusion release or rollback can
destroy a peer append or leave an incorrectly secured source artifact.

Escalation condition: source contradiction, forbidden fifth path, credential/
alternate-user/real-source need, parked drift or irreparable mandatory gate
outside the four owned paths.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3C-C1-R2-TRANSACTION-LIFETIME-AND-SECURITY-VERIFICATION","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reviews/","docs/audits/","docs/reference/","scripts/","governance/compat/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/"],"claims":["corrected transaction lifetime and security verification only; no real source"],"requiredProof":["transaction-wide exclusion","pre-write cleanup","security descriptor read-back","rollback under adversarial scheduling","independent Local probe"],"operatorCheckpoints":["Party B real observation","Local source verification","Party C provisioning","Group 4 establishment","T3E wiring","candidate admission"],"forbiddenEffects":["credential access","alternate-user execution","real source read/write","parked-path mutation","worker commit","provider/live/public/deployment","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-G1-T3C-C1-R2-TRANSACTION-LIFETIME-AND-SECURITY-VERIFICATION --title "ACEL G1 T3C-C1 R2 Transaction Lifetime And Security Verification" --date 2026-09-21 --base dcba5f7f0 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 2 --root-cause-cluster-id acel-g1-t3c-c1-observation-transaction-integrity --prior-finding-set-digest 877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8 --new-independent-critical-evidence TRANSACTION_GUARD_RELEASED_BEFORE_SECURITY_AND_POSTVALIDATION --scec-problem-key acel-g1-t3c-c1-group3-observation-log-tooling-problem --scec-chain-mode SUCCESSOR --scec-chain-ordinal 4 --scec-predecessor-path docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md --scec-predecessor-sha256 877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8 --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope INTEGRATED_ROOT_CONTRACT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path plus no-commit R2 rework profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with three residual findings, exact four-path scope and adversarial transaction/security tests |
| checkerReadAheadConfirmation | dispatch-quality, core-guard, gate-to-role, worker-return, scaffold-provenance, convergence and operation-trace controls applied |
| docOnlyNewFields | none |
| claimBoundary | dispatch authoring only; no runtime/source/provider/public effect |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T3C-C1-R2-TRANSACTION-LIFETIME-AND-SECURITY-VERIFICATION

reviewRoundCount: 2

priorFindingSetDigest: 877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: TRANSACTION_GUARD_RELEASED_BEFORE_SECURITY_AND_POSTVALIDATION

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT

quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: acel-g1-t3c-c1-observation-transaction-integrity

reworkGeneration: 2

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: Local uses disposable paths to prove a competing transaction
cannot enter while ACL verification or final validation remains in progress.

negativeMutationClasses: deterministic peer attempt after stream disposal;
failure after new-directory and empty-file creation; wrong owner, inheritance,
extra allow ACE, deny ACE and security read-back mismatch.

expectedInformationGain: prove that exclusion and rollback cover the whole
durable transaction, rather than repeat record/hash unit tests.

rerunCostReason: bounded disposable probes directly decide safe real-mode
eligibility without Party B or real-source execution.

reviewerDecisionOwner: LOCAL

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3c-c1-group3-observation-log-tooling-problem","chainMode":"SUCCESSOR","chainOrdinal":4,"predecessor":{"path":"docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md","sha256":"877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8"},"blockerDelta":{"prior":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING","transaction-wide-exclusion-gap","pre-write-artifact-rollback-gap","security-postcondition-proof-gap"],"resolved":["transaction-wide-exclusion-gap","pre-write-artifact-rollback-gap","security-postcondition-proof-gap"],"retained":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING"],"new":["R2_NOT_ACCEPTED"],"reopened":[],"current":["REAL_OBSERVATION_PENDING","PARTY_C_AND_GROUP4_PENDING","T3E_PENDING","R2_NOT_ACCEPTED"]},"resolutionEvidence":{"transaction-wide-exclusion-gap":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md","sha256":"877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8","locator":"TRANSACTION_WIDE_GUARD_REQUIRED"},"pre-write-artifact-rollback-gap":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md","sha256":"877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8","locator":"CREATION_ROLLBACK_BOUNDARY_REQUIRED"},"security-postcondition-proof-gap":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md","sha256":"877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8","locator":"SECURITY_POSTCONDITION_AND_RESTORE_REQUIRED"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":2,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3C-C1-R2-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_2026-09-21.md"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/acel_g1_party_b_group3_observation_writer.ps1` | repair transaction guard, mutation ownership, security snapshot/read-back and self-tests |
| `governance/compat/check_acel_g1_registry_observation_log.py` | change only if required by a proven R2 contract dependency; otherwise preserve |
| `governance/compat/test_check_acel_g1_registry_observation_log.py` | retain 42 tests or add only checker-relevant regression coverage |
| `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md` | update in place for R2 evidence and exact manifest reconciliation |

No fifth worker path is allowed. Dispatcher-owned R2 artifacts and thirteen
parked paths are read-only.

## Work-Order Fulfillment Manifest

| Obligation | Owned output | Required proof | Completion owner |
|---|---|---|---|
| transaction-wide exclusion | writer | deterministic competing-transaction oracle proves the outer guard spans ACL and post-validation | worker, then Local reviewer |
| creation-aware rollback | writer | injected directory/file creation failures leave exact initial filesystem state | worker, then Local reviewer |
| security postcondition | writer | read-back proves owner, protection and exact normalized ACE policy | worker, then Local reviewer |
| regression preservation | writer, checker and focused test | R1 suites remain green with exact counts reported | worker |
| return reconciliation | existing worker return | R2 binding, exact four paths, parked disclosure, empty staging and pending independent probe | worker |

## Preconditions

Capture HEAD, full untracked status, empty staging, hashes of all thirteen
parked paths and real-log absence. Verify exactly the four worker paths are the
only T3C-C1 pending outputs. Run pre-implementation before editing.

## Implementation Contract

### Transaction-wide exclusion

- Establish a cross-process exclusion guard before creating the output
  directory or opening/creating the log. The guard identity must be derived
  deterministically from the canonical target path and must not expose secrets.
- Hold the guard continuously through exact-byte read/validation, row build,
  append/flush, DACL application and read-back, final exact-chain validation,
  and either success completion or completed rollback.
- If the data stream must close before ACL operations, the outer exclusion
  guard must remain held. `FileShare.None` alone is insufficient.
- A competing transaction must fail closed or wait and then re-read/revalidate
  the new current state; it must never operate from stale bytes. Rollback must
  not overwrite a peer append.

### Mutation ownership and rollback

- Enter rollback ownership before the first durable mutation, including new
  directory creation and `OpenOrCreate` creation of an empty file.
- Failure at directory-create, file-create/open, locked-chain validation,
  row-build, write, flush, ACL, ACL verification or final validation leaves
  exact prior data/security for an existing path. For an initially absent
  target, remove the new file and only the newly created empty directory.
- Never remove a pre-existing directory or unrelated content. Preserve the
  distinct rollback-failure taxonomy with primary and rollback context.

### Security state and postcondition proof

- Snapshot the exact restorable owner and DACL state under the outer exclusion
  guard before changing either. SACL access is not required.
- After applying policy, re-read the descriptor and assert: expected Party B
  owner; access-rule protection enabled; exactly the allowed Party B, SYSTEM
  and Administrators allow rules with the required rights; no inherited or
  unexpected allow/deny ACE remains. Compare normalized semantic rules rather
  than relying on insertion order.
- A read-back mismatch is a stable nonzero DACL verification failure and
  triggers complete rollback before the guard is released.
- After rollback, re-read and prove exact prior owner/DACL semantics as well as
  exact prior bytes. Failure to prove restoration is rollback failure.

### Required regressions

- Inject a peer modification attempt after stream disposal but before ACL or
  final validation. Prove the peer cannot enter the protected transaction and
  rollback cannot erase its data. Use deterministic synchronization, not sleeps.
- Inject failure after new directory creation and after new empty-file creation;
  prove no artifact remains. Also prove pre-existing directory preservation.
- Inject an applied-ACL mismatch/read-back failure for new and existing files;
  prove cleanup or exact bytes plus owner/DACL restoration.
- Prove successful read-back accepts the exact policy and rejects one extra
  allow ACE, one deny ACE, inheritance enabled and wrong owner.
- Preserve all R1 exact two/three append, same-length replacement, DACL,
  post-validation, blank-line and no-mutation regressions.

### Return readiness

- Top-level status is `COMPLETE_PENDING_REVIEW` only on full pass.
- Include `independentProbeDisposition: PENDING_REVIEWER_EXECUTION`.
- `evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON` remains unchanged.
- Changed Files, trace and git status name exactly the four owned outputs plus
  separately disclosed thirteen parked paths. No real source is created.

## Worker Autonomy / No-Question Rule

Repair routine allowed-scope defects directly. Return only for a true source
conflict, fifth path, credential/alternate-user/real-source need, parked drift
or irreparable mandatory gate outside the four owned paths.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | same writer, checker, focused test and return |
| Storage decision | integrated root contract is implemented in place; no new path, index or runtime store |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | real Group 3 log remains absent and operator-gated |

## Core Guard Self-Protection Authorization

| Field | Value |
|---|---|
| Authorized guard-maintenance scope | bounded Group 3 writer/checker focused correction; no hook/catalog/general guard changes |
| Protected path | `governance/compat/check_acel_g1_registry_observation_log.py` |
| Protected path | `governance/compat/test_check_acel_g1_registry_observation_log.py` |
| Operator authorization | operator authorized Local audit and worker dispatch; original committed order owns both paths |
| Rollback boundary | all four outputs stay uncommitted until Local accepts |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_agent_operation_trace.py`; Group 3 checker/test |
| literalTokensReviewed | protected paths; source-verification columns; convergence; probe; trace; no-commit and evidence-readiness fields |
| gateRunPurpose | confirm R2 packet and later exact four-path return |
| claimBoundary | structure and hermetic behavior only; no real-source acceptance |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| three residual findings | accepted review | `docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md` | Findings / Position; Independent Probe Evidence | T3C-C1-R1-RV-1 through RV-3 | Local reviewer | ACCEPT |
| exact four-path scope | dispatch invariant | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_2026-09-21.md` | Required Artifact Manifest | four worker paths | R1 dispatch | ACCEPT |
| durable source transaction | source invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 3 | append-only observation chain | Group 3 contract | ACCEPT |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | R2 baseline/work order/review | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | R2 packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact four outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned four paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> no-commit INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC; real Party B excluded |
| baseHeadFor(phase) | dispatchBaseHead=`dcba5f7f017af96ae2f61c1ddc5cbf54fe69945d`; executionBaseHead captured by worker; closureBaseHead set by Local |
| changedSetScope(phase) | exact four outputs during execution; three R2 dispatcher artifacts during dispatch |
| traceScope(phase, actor) | reads, commands, tests, hashes, status, cleanup and real-source absence |
| commitOwner(phase) | Local only |
| crossBatchIsolation | thirteen parked paths byte-identical and disclosed |
| nextMoveSurfaces | Local review, then explicit Party B checkpoint |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT R2 worker after operator forwards this packet

laneOwnedPaths: exact four paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact delta and parked reconciliation

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON: bounded local tooling correction has no discovery audit or manifest artifact

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_2026-09-21.md`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Claim Boundary;
Changed Files; Command Evidence; No-Commit Statement; Checker Source Read-
Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Machine Closure Package; External Knowledge Intake Routing;
Epistemic Process Block; Public Export Disposition; exact executionBaseHead and
full `git status --short --untracked-files=all`.

## Execution Plan

1. Freeze HEAD/status/staging, parked hashes and real-source absence.
2. Add an outer transaction guard and move mutation ownership before creation.
3. Capture, apply, read back and restore exact owner/DACL semantics.
4. Add deterministic adversarial guard/creation/security regressions.
5. Preserve all R1 evidence; update the same return; run final commands once.

## Evidence Requirements

Required final evidence: all R1 suites; deterministic competing-transaction
probe; failures after directory creation and empty-file creation; exact ACL
read-back acceptance and mismatch rejection; exact bytes/security rollback;
worker-return fast PASS; real-log absence; parked hash match; empty staging.

## Acceptance Criteria

- Exactly four worker paths change; no real/parked/dispatcher path changes.
- One outer guard spans first possible mutation through success or rollback.
- A peer cannot enter the transaction window or have its append overwritten.
- Every pre-write new-artifact failure leaves the initial filesystem state.
- Applied owner/DACL is read back and semantically proven; mismatch rolls back.
- Existing bytes and prior owner/DACL semantics restore exactly on every failure.
- All R1 regressions remain green and each R2 finding has a deterministic oracle.
- Return binds R2 and retains `PENDING_REVIEWER_EXECUTION`.

## Review Gate

Local consumes returned evidence and runs only the admitted transaction-lifetime,
pre-write cleanup and security read-back probes plus the focused suites. Local
does not use credentials, execute as Party B, read the real registry or write
the real Group 3 log during tooling review.

## Closure Checklist

- [ ] T3C-C1-R1-RV-1 through RV-3 each have a failing-before/passing-after oracle.
- [ ] Exact four paths and thirteen parked hashes reconcile; staging empty.
- [ ] Worker-return fast and Local independent probes pass.
- [ ] Real `governance/sources/registry_observation_log/LOG.jsonl` remains absent.
- [ ] Material and continuity commits remain separate.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for a source contradiction, forbidden fifth
path, credential/alternate-user/real-source requirement, parked drift or an
irreparable mandatory gate outside allowed scope. Repair owned-lane failures
without operator interruption.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m pytest governance/compat/test_check_acel_g1_registry_observation_log.py -q
python governance/compat/check_acel_g1_registry_observation_log.py --self-test
pwsh -NoProfile -File scripts/acel_g1_party_b_group3_observation_writer.ps1 -SelfTest
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_2026-09-21.md
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

No release-gate/provider call applies: this is local hermetic tooling, not a
live AI-governance or production-readiness claim.

## Pre-Dispatch Gate Disposition

The full pre-dispatch bundle passed 82/83 controls. Its sole failure is three
pre-existing, unrelated untracked T2A/T2B/calibration worker returns whose
historical work orders predate the independent-probe declaration. They are
among the thirteen parked paths and are outside this lane. The required
changed-lane probe-admission command for this R2 work order passes with those
three entries reported explicitly as out-of-lane. All other R2 dispatch,
SCEC, closeability, handoff, structural and protection controls pass. This
disposition does not waive an in-lane failure or authorize touching parked
paths.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md` |
| reviewerOwnedClosurePaths | exact four worker outputs plus bounded reviewer repair inside those paths |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |
| materialCommitBoundary | accepted four-path implementation first |
| sessionSyncBoundary | separate later commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF dispatcher/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | ACEL G1 T3C-C1 R2 dispatch, 2026-09-21 |
| Working directory | repository root |
| Command or tool surface | governed reads, retained/focused tests, scaffold stdout, apply_patch, dispatch gates and git |
| Target paths | R2 baseline/work order and R1 completion review; worker later owns exact four outputs |
| Allowed scope source | operator review/delegation authority; committed R1 packet; independent completion review |
| Before status evidence | clean worktree requirement is represented by explicit shared-lane isolation: HEAD `dcba5f7f017af96ae2f61c1ddc5cbf54fe69945d`; thirteen parked plus four T3C-C1 outputs; staging empty before dispatcher staging |
| After status evidence | R2 packet authored for dispatch commit; worker and parked paths untouched by dispatcher |
| Diff evidence | three-finding transaction-lifetime/security contract |
| Approval boundary | corrective dispatch only |
| Claim boundary | no credentials, Party B, real source, Party C/Group 4, T3E, provider/live/public/deploy effect |
| Agent type | Local dispatcher/orchestrator |
| Invocation ID | `acel-g1-t3c-c1-r2-transaction-lifetime-security-dispatch-2026-09-21` |
| Expected manifest | R2 baseline, R2 work order, R1 completion review |
| Actual changed set | R2 baseline, R2 work order, R1 completion review |
| Manifest delta | MATCH before commit |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | four-path hermetic transaction-lifetime/security correction |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: dispatch/tests create no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: R1 review and final worker tests |
| invocationBoundary | local governed edits and disposable fixtures only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | corrected tooling pending Local acceptance |
| forbiddenExpansion | credentials, alternate principal, real source, Party C/Group 4, T3E, admission, provider/live/public/deploy |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md` |
| Chain map route | N/A with reason: direct internal correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2F Group 3 contract and this R2 dispatch |
| Disposition | local first-party correction only |
| Claim boundary | no external source authority, corpus, remote implementation or provider claim |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: R2 implementation; decision owner: Local
reviewer. External research ends outside this packet and has no authority here.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one outer exclusion guard plus creation-aware
rollback and security read-back will close all three residual failure windows.

Evidence Comparison Requirement: the worker must compare deterministic
adversarial results with this prediction, not only report aggregate counts.

Contradiction Handling Requirement: record a Contradiction Or Gap Disposition
and narrow the claim; no silent waiver.

Claim Update Requirement: record confirmed/revised/narrowed/invalidated for
each T3C-C1-R1-RV finding.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private corrective tooling dispatch; no public-sync authority.

## Claim Boundary

This work order authorizes correction and hermetic verification of four
uncommitted files only. It does not authorize credentials, `runas`, Party B
execution, real registry testing, real Group 3 creation, Party C/Group 4, T3E,
candidate admission, worker commit, provider/live/network/public/deployment or
automatic successor effects.

## Operator Checkpoint

No operator action is needed during R2. After Local acceptance, the first real
Party B observation remains a separate explicit checkpoint. R2 must not run it.
