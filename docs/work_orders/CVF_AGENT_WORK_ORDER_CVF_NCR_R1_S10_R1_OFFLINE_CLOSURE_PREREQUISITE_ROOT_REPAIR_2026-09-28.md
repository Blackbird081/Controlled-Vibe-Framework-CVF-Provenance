# CVF Agent Work Order - NCR-R1/S10-R1 Offline Closure Prerequisite Root Repair

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: CVF-NCR-R1-S10-R1

Dispatch base head: `d4346da270bdff06257aa2def3510cf956512ea5`

providerExecutionAuthority: FORBIDDEN

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one delegated shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_WORKER_RETURN_2026-09-28.md`

## Dispatch Prompt Envelope

Role: delegated internal worker for CVF-NCR-R1-S10-R1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_2026-09-28.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture clean committed `HEAD` at start.

Current-time notes: artifact date is 2026-09-28; test-only positive quota data
must not depend on a near-term calendar date.

Do-not-misread notes: the P9 provider call already succeeded and is immutable.
Do not call the provider, read credentials, rerun the adapter live, edit the
receipt, change lifecycle state or start P10.

Required first actions: read startup/bootstrap surfaces, guard orientation,
literal gotchas, this packet, paired baseline, exact two input owners and all
checker sources named below. Run the exact pre-implementation gate before edits.

Return contract: perform the full bounded repair without operator questions,
create the exact worker return, run all required offline gates, leave every
change unstaged/uncommitted, and return `COMPLETE_PENDING_REVIEW` only if all
mandatory gates pass; otherwise return `BLOCKED_WITH_REASON` to Local.

## Purpose

Make S10 terminal review reproducible by repairing one wall-clock-sensitive
test fixture and one historical receipt-trace shape. Preserve behavior,
historical truth and the existing P9 receipt.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id CVF-NCR-R1-S10-R1 --title "Offline Closure Prerequisite Root Repair" --date 2026-09-28 --base d4346da270bdff06257aa2def3510cf956512ea5 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_COMPLETION_2026-09-28.md --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id CVF-NCR-S10-P9-OFFLINE-CLOSURE-PREREQUISITE-DRIFT --prior-finding-set-digest 789d77ea22ee25b30003c6db4d265647f2eb084a37a0346cc826954d47fa4c5f --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence VALID_P9_RECEIPT_AND_TWO_OFFLINE_PREREQUISITE_DEFECTS --scec-problem-key CVF-NCR-TEST-EVIDENCE-AUDIT-P9 --scec-chain-mode SUCCESSOR --scec-chain-ordinal 2 --scec-predecessor-path docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_COMPLETION_2026-09-28.md --scec-predecessor-sha256 789d77ea22ee25b30003c6db4d265647f2eb084a37a0346cc826954d47fa4c5f --scec-required-disposition STOP_REASSESS_ARCHITECTURE --scec-successor-scope INTEGRATED_ROOT_CONTRACT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path REWORK plus no-commit internal worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact three-path manifest, deterministic fixture and hostile expiry contract, canonical S09 trace rows, inherited S10 gate and no-live boundary |
| checkerReadAheadConfirmation | work-order, worker-return, protection, receipt-trace, closeability, convergence and review-cost owners |
| docOnlyNewFields | none |
| claimBoundary | dispatch authority only; no implementation or S10 closure claim |

## Machine Closure Package

| Closure item | Required evidence | Dispatch status |
|---|---|---|
| fixture repair | focused suite passes with explicit expired hostile coverage | REQUIRED |
| S09 trace repair | exact eight-row `NOT_USED_WITH_REASON` table | REQUIRED |
| original S10 closure gate | exact prior work-order fast gate passes offline | REQUIRED |
| S10-R1 return | exact path, fast gate pass, empty staging | REQUIRED |

## Acceptance Receipt Assertion Matrix

| Assertion | Required evidence | Prohibited substitute |
|---|---|---|
| positive fixture is time-stable | deterministic far-future test-only expiry or equivalently non-bit-rotting fixture plus passing positive tests | removing expiry enforcement |
| expiry remains fail-closed | explicit test with expired ledger and denial before package/provider action | prose assurance |
| S09 truth is preserved | all eight trace values state no usage/no receipt/no consumed output with reason | invented receipt or retroactive use claim |
| P9 evidence is unchanged | receipt file SHA-256 remains `e13fc1106f90d146948ed042df9464a318d38c9618b47fca77ea9abbbfee3556` | regenerated or edited receipt |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-R1-S10-R1","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["governance/compat/","docs/baselines/","docs/work_orders/","docs/reviews/"],"claims":["the focused test fixture can be made time-stable without weakening expiry semantics","the S09 trace can be backfilled without changing historical execution truth"],"requiredProof":["focused pytest pass including hostile expiry","receipt-trace checker pass","original S10 fast gate pass","exact three-path reconciliation","immutable P9 receipt hash"],"operatorCheckpoints":["provider/live retry remains forbidden","P10 remains closed"],"forbiddenEffects":["provider or network call","credential read","receipt mutation","production adapter or checker change","lifecycle P10 public deployment or production action","worker commit stage stash or push"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_COMPLETION_2026-09-28.md","completenessClaimChanged":false}}
```

| Field | Value |
|---|---|
| task class | governance checker test maintenance plus governed historical evidence-shape backfill |
| active role | internal worker |
| reviewer | Local orchestrator/reviewer |
| execution boundary | offline-only, exact three paths |
| decision owner | Local |

## Authority Chain

1. Frozen doctrine and operating model.
2. Guard orientation, work-order template, receipt-trace checker and test owner.
3. Committed S10 completion review at material commit `80b6e6c1fb5a63ac7590cc305b8d49d1e55f3d27`.
4. This paired baseline and work order after committed release.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| S10 completion review | committed review SHA-256 `789d77ea22ee25b30003c6db4d265647f2eb084a37a0346cc826954d47fa4c5f` | own only the two blockers it names | RELEASED_FOR_ROOT_REWORK |
| valid P9 receipt | committed file SHA-256 `e13fc1106f90d146948ed042df9464a318d38c9618b47fca77ea9abbbfee3556` | read-only reuse; zero provider calls | ACCEPT_AND_IMMUTABLE |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_COMPLETION_2026-09-28.md` |
| Chain map route | N/A with reason: no external research or absorption |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Local reviewer/closer |
| Disposition | NOT_APPLICABLE_WITH_REASON: exact local owners are known |
| Claim boundary | no external claim promotion or public/private inference |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: bounded S10-R1 repair.
Decision owner: Local. External research is inactive.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_COMPLETION_2026-09-28.md"}
```

## Scope And Maximum Worker Path Manifest

The worker may modify exactly:

1. `governance/compat/test_run_assf_package_use_proof_adapter.py`
2. `docs/reviews/CVF_CVF_NCR_R1_S09_TEST_EVIDENCE_AUDIT_ACTIVATION_READINESS_WORKER_RETURN_2026-09-27.md`

The worker may create exactly:

3. `docs/reviews/CVF_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_WORKER_RETURN_2026-09-28.md`

No fourth dirty path is permitted. Existing P9 receipt and S10 review/return
are read-only inputs.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | two exact offline closure prerequisites |
| scope classification | protected test plus governed historical evidence repair |
| risk sensitivity | no runtime mutation; receipt integrity is high-value |
| selected role route | one INTERNAL_AGENT worker, then Local independent review |
| escalation condition | source contradiction or unavoidable fourth path |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| decision owner | Local technical disposition |

## Required Root Contract

1. Run pre-implementation before any edit.
2. Make positive fixture validity deterministic beyond ordinary test horizon.
3. Add or retain an explicit expired-ledger hostile test that proves denial.
4. Backfill the S09 trace with all eight canonical rows and no false use claim.
5. Do not edit adapter/checker production source or weaken expiration logic.
6. Reuse the existing S10 receipt/return; never call the provider or adapter live.
7. Run every verification command and reconcile exact three-path scope.
8. Return directly to Local; never open an operator question.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| fixture dates cause the focused failures | reproduced test defect | `governance/compat/test_run_assf_package_use_proof_adapter.py` | `_write_free_quota_ledger` | `_write_free_quota_ledger`; `expirationDate` | focused test suite | ACCEPT |
| trace checker requires exact rows and allowed disposition | machine contract | `governance/compat/check_cvf_skill_usage_receipt_trace.py` | `REQUIRED_ROWS`; `validate_trace_section` | `NOT_USED_WITH_REASON` | receipt-trace checker | ACCEPT |
| S09 section is prose-only | historical evidence | `docs/reviews/CVF_CVF_NCR_R1_S09_TEST_EVIDENCE_AUDIT_ACTIVATION_READINESS_WORKER_RETURN_2026-09-27.md` | CVF Skill Usage Receipt Trace | eight rows absent | governed return | ACCEPT |
| P9 receipt passed independent recomputation | Local review decision | `docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_COMPLETION_2026-09-28.md` | Independent Probe Evidence | receipt ID | completion review | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| baseline and work-order paths | both `Test-Path` results false before authoring | NO_COLLISION |
| batch/title search | exact `rg` returned no prior artifact before authoring | NO_COLLISION |
| worker return path | reserved by this packet; absent at dispatch authoring | CREATE_NEW |

## Required First Reads And Pre-Flight

Read the current startup surfaces, guard orientation, literal gotchas, paired
baseline, this work order, the S10 completion review, exact two mutation owners,
receipt-trace checker, worker-return checker and every applicable checker in
the read-ahead block. Capture `HEAD`, full status and empty staging.

## Agent Roles

- Worker: implements exact bounded repair and returns evidence without commit.
- Reviewer/closer: independently inspects, reruns bounded offline probes and commits if accepted.
- Session-sync steward: updates continuity after material disposition.
- Operator: no checkpoint is required inside this already-authorized repair.

## Write Ownership

Exact three-path manifest only. `WORKER_MUST_NOT_COMMIT`; no stage, stash,
commit, push, network action, receipt write or unrelated cleanup.

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - no lock, durable concurrent append, DACL/ownership change or rollback-sensitive production transaction is in scope.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: repair the focused use-proof adapter test
fixture and add/retain hostile expiration coverage.

Protected path: `governance/compat/test_run_assf_package_use_proof_adapter.py`.

Operator authorization: operator directed Local to continue after the S10
completion review identified these root prerequisites.

Rollback boundary: revert only the exact S10-R1 three-path worker batch; retain
material commit `80b6e6c1fb5a63ac7590cc305b8d49d1e55f3d27` and its receipt.

Not authorized: production adapter/checker changes, credential access, provider
or network calls, receipt mutation, lifecycle/package/truth/index/inventory/Web
mutation, P10, public sync, deployment, staging or commit.

## Execution Plan

1. Pass pre-implementation and record clean base/status.
2. Repair the isolated positive ledger without weakening expiry logic.
3. Add/verify an expired-ledger hostile denial case.
4. Replace the S09 prose-only block with the canonical eight-row N/A table.
5. Run focused tests and receipt-trace checker.
6. Run the original S10 fast gate against preserved artifacts.
7. Create the S10-R1 worker return and run its exact fast gate.
8. Reconcile three paths, empty staging, no receipt diff and no live action.

## Evidence Requirements

- focused pytest count and PASS;
- explicit hostile expiry assertion and denial evidence;
- receipt-trace PASS with eight exact rows;
- original S10 fast-gate PASS without receipt modification;
- P9 receipt SHA-256 remains exact;
- exact three dirty paths and empty cached diff;
- provider call count for this tranche is zero.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_COMPLETION_2026-09-28.md`

priorVerificationAnchor: receipt ID `sha256:b0f8a1030650a5c5544e3583b17ae9e64eaa05166dff7e9223be3ff6228c942e`

freshRecomputeRequired: focused offline tests, trace checker, both worker-return gates, receipt file hash and Git scope only

unicodePathHandling: use literal repository-relative paths and UTF-8-safe readers

extractedTextAuthority: governed source text and checker output only

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_2026-09-28.md
python -m pytest governance/compat/test_run_assf_package_use_proof_adapter.py -q
python governance/compat/check_cvf_skill_usage_receipt_trace.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_2026-09-28.md --pytest-target governance/compat/test_run_assf_package_use_proof_adapter.py
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_WORKER_RETURN_2026-09-28.md --title "CVF NCR R1 S10-R1 Offline Closure Prerequisite Root Repair Worker Return"
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_2026-09-28.md --pytest-target governance/compat/test_run_assf_package_use_proof_adapter.py
Get-FileHash -Algorithm SHA256 docs/reviews/evidence/cvf-ncr-r1-s10-test-evidence-audit-use-proof.json
git diff --check
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
```

Forbidden commands include any live use-proof adapter invocation, provider CLI,
credential or environment-secret read, network command, stage, commit, stash or push.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: CVF-NCR-R1-S10-R1

reviewRoundCount: 1

priorFindingSetDigest: 789d77ea22ee25b30003c6db4d265647f2eb084a37a0346cc826954d47fa4c5f

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: VALID_P9_RECEIPT_AND_TWO_OFFLINE_PREREQUISITE_DEFECTS

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT

quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: CVF-NCR-S10-P9-OFFLINE-CLOSURE-PREREQUISITE-DRIFT

reworkGeneration: 1

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

reviewerLocalRepairBoundary: WORK_ORDER_FORBIDS_REVIEWER_REPAIR

reviewerLocalRepairBasis: S10 completion findings S10-RV-2 and S10-RV-3 require test implementation plus historical evidence mutation, outside bounded reviewer evidence repair

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"CVF-NCR-TEST-EVIDENCE-AUDIT-P9","chainMode":"SUCCESSOR","chainOrdinal":2,"predecessor":{"path":"docs/reviews/CVF_CVF_NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF_COMPLETION_2026-09-28.md","sha256":"789d77ea22ee25b30003c6db4d265647f2eb084a37a0346cc826954d47fa4c5f"},"blockerDelta":{"prior":["EXPIRED_USE_PROOF_TEST_FIXTURE","S09_RECEIPT_TRACE_SHAPE_GAP"],"resolved":[],"retained":["EXPIRED_USE_PROOF_TEST_FIXTURE","S09_RECEIPT_TRACE_SHAPE_GAP"],"new":[],"reopened":[],"current":["EXPIRED_USE_PROOF_TEST_FIXTURE","S09_RECEIPT_TRACE_SHAPE_GAP"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":1,"reviewerScopeExpansions":0,"sameClaimCorrections":1,"nonDecreasingBlockerTransitions":2},"claims":[{"claimId":"EXPIRED_USE_PROOF_TEST_FIXTURE","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"governance/compat/test_run_assf_package_use_proof_adapter.py"},{"claimId":"S09_RECEIPT_TRACE_SHAPE_GAP","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reviews/CVF_CVF_NCR_R1_S09_TEST_EVIDENCE_AUDIT_ACTIVATION_READINESS_WORKER_RETURN_2026-09-27.md"}],"requiredDisposition":"STOP_REASSESS_ARCHITECTURE","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker and active session sources | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact three paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | focused test file | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| receipt_trace | WORKER_RETURN | worker | IMPLEMENTATION | S09 trace block | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| original_s10_fast_gate | WORKER_RETURN | worker | IMPLEMENTATION | preserved S10 evidence | EXACT_PATHS | closer | MATERIAL_COMMIT | receipt_trace |
| worker_return_fast | WORKER_RETURN | worker | IMPLEMENTATION | S10-R1 worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | original_s10_fast_gate |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned three-path set | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | optional completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted set | EXACT_PATHS | closer | MATERIAL_COMMIT | terminal_completion_review |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split material/continuity ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | S10_R1_OFFLINE_ROOT_REPAIR |
| baseHeadFor(phase) | dispatchBaseHead=`d4346da270bdff06257aa2def3510cf956512ea5`; executionBaseHead=worker capture; closureBaseHead=Local-set |
| changedSetScope(phase) | exact three worker paths |
| traceScope(phase, actor) | test, trace, receipt-hash, gate and Git evidence |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | no unrelated dirty path; no receipt mutation |
| nextMoveSurfaces | terminal worker return to Local only |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: one INTERNAL_AGENT after committed release

laneOwnedPaths: exact three-path manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal return, exact manifest and empty staging

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-checker-hardening`, role=`worker`, lifecyclePhase=`WORKER_EXECUTION`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class governance-checker-hardening --role worker --lifecycle-phase WORKER_EXECUTION --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | no registered defect widens the exact repair |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_cvf_skill_usage_receipt_trace.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | exact trace row labels; `NOT_USED_WITH_REASON`; protected-path authorization; REWORK convergence fields; SCEC chain; closeability gate graph; worker-return status and trace labels |
| gateRunPurpose | confirm this source-designed dispatch packet as evidence, not first-discover repair semantics or return shape |
| claimBoundary | dispatch admission only; no test correctness, historical truth acceptance or S10 closure claim |

## Worker Output Checker Read-Ahead Mandate

Before authoring the return, read the current worker-return, finding-learning,
operation-trace, delta-boundary, receipt-trace, epistemic, review-cost and public-
export checker sources. Use real section headings only at their actual sections,
and explicit N/A with reason for conditional non-applicability.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_WORKER_RETURN_2026-09-28.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_2026-09-28.md --pytest-target governance/compat/test_run_assf_package_use_proof_adapter.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead
Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control
Block; Public Export Disposition; executionBaseHead; git status --short;
Changed Files; No-Commit Statement.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Machine Closure Package; CVF
Skill Usage Receipt Trace. Use N/A with reason when inapplicable.

## Work-Order Fulfillment Manifest

| Requirement | Required evidence in worker return |
|---|---|
| deterministic fixture repair | exact change and why it cannot expire soon |
| hostile expiry preservation | test name, assertion and PASS |
| historical trace | exact eight-row table and checker PASS |
| immutable receipt | unchanged SHA-256 |
| zero live actions | explicit provider/live call count zero |
| scope | exact three paths, empty staging, no commit/stash |

## Required Artifact Manifest

| Path | Required at handoff | Rule |
|---|---|---|
| `governance/compat/test_run_assf_package_use_proof_adapter.py` | YES | minimal test-only repair plus hostile expiry coverage |
| `docs/reviews/CVF_CVF_NCR_R1_S09_TEST_EVIDENCE_AUDIT_ACTIVATION_READINESS_WORKER_RETURN_2026-09-27.md` | YES | eight canonical historical N/A rows only |
| `docs/reviews/CVF_CVF_NCR_R1_S10_R1_OFFLINE_CLOSURE_PREREQUISITE_ROOT_REPAIR_WORKER_RETURN_2026-09-28.md` | YES | terminal checker-safe return |

## Dated Owner Dependency Discovery

No new dated owner is required. This is a repair of two existing owners and
one dated worker return.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: no source-mirror or external corpus absorption.

## Forbidden Path Manifest

Every path outside the exact three-path manifest is forbidden, especially the
P9 receipt, adapter production source, receipt-trace checker, package trio,
registry, truth/index/inventory/Web, roadmap, work-order/baseline, continuity,
credentials, environment files and public-sync surfaces.

## Forbidden Filesystem State At Dispatch

Clean worktree and empty staging are required at worker start. Stop and return
to Local if any unrelated dirty path exists; do not stash, reset or clean it.

## Pre-Existing Dirty Path Exemptions

NONE.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | optional S10-R1 completion review only if Local needs a distinct disposition artifact |
| reviewerOwnedClosurePaths | returned exact three-path set plus separately authorized continuity |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Autonomy / No-Question Rule

The worker has authority to implement any minimal solution inside the exact
three paths that satisfies the stated invariants and gates. Do not ask the
operator to choose a technical implementation. On a genuine contradiction or
forbidden-path need, return `BLOCKED_WITH_REASON` directly to Local with exact
evidence; never invoke an operator question surface.

## Parked Effect Checkpoints

Provider/live use, credentials, receipt mutation, lifecycle promotion, P10,
production adapter/checker changes, network, public export and deployment are
all parked with no worker release path.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`.

Current phase: P9 evidence exists; terminal review is blocked only by two offline prerequisites.

Target lifecycle state: unchanged.

Prior phase evidence: committed S10 receipt, worker return and Local completion review.

Next forbidden skip: P10 production package runtime.

Runtime/provider proof: reuse only; no new provider or runtime invocation.

Claim boundary: repair does not promote package state or add runtime authority.

## Package Skill Target-State Feasibility Contract

```json
{
  "schemaVersion": "cvf.packageSkillTargetStateFeasibility.v1",
  "skillId": "cvf-engineering-test-evidence-audit",
  "sopPhase": "P9",
  "targetState": {
    "status": "ACTIVE",
    "candidateState": "ACTIVE",
    "uatState": "PASSED",
    "certificationState": "CERTIFIED",
    "internalAgentDisposition": "IMPLEMENTED",
    "externalCliMcpDisposition": "DEFERRED_WITH_REASON",
    "truthApprovalStatus": "APPROVED",
    "truthAssuranceLevel": "STRICT",
    "adapterContract": "N/A with reason: internal-only P9 evidence",
    "adapterEvidence": "N/A with reason: external use is not claimed"
  },
  "externalUseClaimed": false,
  "expectedDecisions": {
    "internalActivation": "ACTIVATION_READY",
    "externalBodyRead": "DENIED_EXTERNAL_BODY_READ_NOT_IMPLEMENTED",
    "externalOutputUse": "DENIED_EXTERNAL_OUTPUT_USE_NOT_IMPLEMENTED"
  },
  "checkerSources": [
    "governance/compat/check_assf_certified_metadata_admission.py",
    "governance/compat/check_package_skill_productionization_pipeline.py",
    "governance/compat/generate_skill_control_plane_inventory.py",
    "governance/compat/run_assf_active_resolver.py",
    "governance/compat/run_assf_cli_mcp_adapter_projection.py"
  ],
  "mutations": ["USE_PROOF_RECEIPT"],
  "blockerRouting": {
    "technicalDecisionOwner": "LOCAL",
    "workerTerminalReturn": "BLOCKED_WITH_REASON",
    "operatorQuestionAllowed": false
  }
}
```

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: OFFLINE_CLOSURE_PREREQUISITE_SEMANTICS

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: worker changes fixtures and trace shape; Local independently inspects expiry semantics and reruns bounded commands

positiveControl: non-expired isolated ledger passes all positive adapter tests and both offline fast gates

negativeMutationClasses: expired ledger accepted, expiration enforcement removed, false S09 usage claim, receipt mutation, provider call or fourth path

expectedInformationGain: distinguish a time-stable test-only repair from weakened production expiry behavior and prove historical trace fidelity

rerunCostReason: bounded offline tests and checkers directly decide closure at zero provider cost

reviewerDecisionOwner: LOCAL

independentProbeOwner: Local reviewer/closer

independentProbeScope: inspect hostile expiry semantics, recompute receipt file
hash, rerun focused pytest, receipt-trace checker and both offline fast gates.

independentProbeForbidden: provider/live call, credential read, receipt edit,
implementation recreation or unrelated broad suite.

## Foundation Storage Layout Block

N/A with reason: no new foundation, folder, front door, index, template,
standard or durable storage owner is created.

## Current Runtime Freshness Verification

Runtime freshness is not recomputed because runtime/provider action is
forbidden. The only fresh evidence required is offline test/checker output and
the unchanged committed receipt file hash.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated INTERNAL_AGENT worker |
| Provider or surface | private local workspace; offline only |
| Session or invocation | CVF-NCR-R1-S10-R1, 2026-09-28 |
| Working directory | repository root |
| Command or tool surface | governed reads, apply-patch edits, pytest and offline checkers |
| Target paths | exact three-path manifest |
| Allowed scope source | this committed work order and paired baseline |
| Before status evidence | clean worktree at committed execution base and empty staging |
| After status evidence | exact three paths dirty and empty staging |
| Diff evidence | `git diff --name-status`; `git status --short --untracked-files=all` |
| Approval boundary | offline prerequisite repair only |
| Claim boundary | no live/provider/runtime/lifecycle/public claim |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | `cvf-ncr-r1-s10-r1-offline-root-repair-20260928` |
| Expected manifest | exact three paths |
| Actual changed set | worker must fill at return |
| Manifest delta | worker must fill at return |
| Deletion or rename disposition | none authorized |

## Epistemic Process Block

Expected Result / Prediction: fixing time-sensitive positive test data while
retaining a hostile expired case and adding canonical historical N/A rows will
make both S10 closure gates pass without a repeated live action.

Evidence Comparison Requirement: compare all focused test results, exact trace
rows, receipt hash and both fast-gate outputs to the prediction.

Contradiction Handling Requirement: stop on a production-source need, receipt
change, provider-call need, or fourth path; report exact evidence to Local.

Claim Update Requirement: distinguish offline prerequisite repair from P9
evidence validity and from final S10 lifecycle closure.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | offline test and governed evidence-shape repair |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: existing committed P9 receipt remains immutable and hash-checked |
| actionEvidence | ACTION_EVIDENCE_PRESENT: pytest/checker commands only; provider action count zero |
| invocationBoundary | local offline commands named in this work order |
| interceptionBoundary | no direct interception, wrapper, provider, credential or network behavior |
| claimLanguage | proves only that the two named offline prerequisites are repaired |
| forbiddenExpansion | no lifecycle, P10, deployment, production, public or new live-proof claim |

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every required command passes, the
receipt hash is unchanged, the dirty set is exactly three paths and staging is
empty. Otherwise return `BLOCKED_WITH_REASON` directly to Local with the first
root contradiction and no operator question.

## Acceptance Criteria

1. Pre-implementation gate passes before edits.
2. Focused suite passes all tests, including explicit expired hostile coverage.
3. Receipt-trace checker passes with exact historical N/A truth.
4. Original S10 fast gate passes using preserved receipt/return.
5. S10-R1 fast gate passes.
6. Receipt hash remains exact and provider/live call count is zero.
7. Exact three-path dirty set, empty staging and no commit/stash/push.

## Review Gate

Local must inspect the semantic test change and historical trace values, then
rerun only the bounded offline independent probes. Passing worker output does
not itself close S10 or authorize P10.

## Closure Checklist

- [ ] Exact execution base captured.
- [ ] Three-path scope reconciled.
- [ ] Hostile expired fixture test present and passing.
- [ ] Eight canonical N/A trace rows present.
- [ ] Original and repair fast gates pass.
- [ ] Receipt hash unchanged; zero live calls.
- [ ] Empty staging; no worker commit/stash/push.
- [ ] Local independent review completed.

## Claim Boundary

This work order authorizes only a private, reversible, offline repair in three
paths. It does not authorize production source/checker changes, credentials,
provider/network/live action, receipt mutation, lifecycle/package/truth/index/
inventory/Web changes, P10, public sync, deployment or worker commit.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private offline repair with no public-sync authority.

## Operator Checkpoint

No operator checkpoint is open. The operator already authorized continuation;
technical issues return to Local reviewer/orchestrator, not to AskUserQuestion.
