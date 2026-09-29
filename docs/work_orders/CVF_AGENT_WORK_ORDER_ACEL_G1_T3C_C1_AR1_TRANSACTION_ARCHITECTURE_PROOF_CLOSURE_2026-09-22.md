# CVF Agent Work Order - ACEL G1 T3C-C1 AR1 Transaction Architecture Proof Closure

Memory class: governed-worker-dispatch

docType: work_order

Status: APPROVED_FOR_EXECUTION

Date: 2026-09-22

Batch ID: ACEL-G1-T3C-C1-AR1-TRANSACTION-ARCHITECTURE-PROOF-CLOSURE

Dispatch base head: `6e85f0b9ab2c031ec4ccf4efa21a19e8fd1ad8da`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker return path: `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md`

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Dispatch Prompt Envelope

Role: shared-workspace `INTERNAL_AGENT` implementation worker.

Canonical packet: this work order plus
`docs/baselines/CVF_GC018_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_REOPEN_2026-09-22.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the full current HEAD before edits. It must be at or
after dispatch head `6e85f0b9ab2c031ec4ccf4efa21a19e8fd1ad8da` and include the committed
AR1 dispatch packet when the operator forwards this order.

Do-not-misread: AR1 is a fresh operator-authorized architecture chain, not R3
of the stopped chain. Repair exactly four existing pending paths. Do not create
a new return, helper, receipt or test file. Do not run as Party B, read the real
Group 1 source or create the real Group 3 log.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, the AR1 baseline, this order, the R2 terminal review, all four owned
files and the applicable checker sources. Capture HEAD, full status, empty
staging, four starting hashes, thirteen parked hashes and real-log absence.

Return contract: update the canonical return in place, run every required
command after the last edit, bind final gate execution to the return SHA-256,
leave staging empty, do not commit, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Implement the fresh AR1 architecture contract and close all five findings in
the R2 terminal review with deterministic, hermetic proof. Existing passing
record/hash tests are retained but cannot substitute for peer-process,
exception-lifetime, semantic security restoration or final-return identity
evidence.

## Authority Chain

| Authority | Path or instruction | Disposition |
|---|---|---|
| operator reopen | 2026-09-22 instruction: issue a work order to continue repair | ACCEPT |
| active continuity | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V63_2026-09-18.md` | architecture reassessment was the only implementation-reopen route |
| architecture baseline | `docs/baselines/CVF_GC018_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_REOPEN_2026-09-22.md` | ACCEPT |
| terminal review | `docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md` | ACCEPT; five findings and stopped predecessor chain |
| operational source contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | ACCEPT; append-only Group 3 invariants only |

Authority boundary: the stopped R2 chain remains stopped. This new order is
authorized only by the fresh operator instruction and AR1 baseline.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| dispatcher | Local orchestrator/reviewer | architecture contract, source verification and dispatch commit |
| worker | shared-workspace INTERNAL_AGENT | four-path implementation and evidence; no commit |
| reviewer/closer | Local orchestrator/reviewer | independent process/security probes, decision and any accepted commit |
| operator | operator | later real Party B execution only; not needed for hermetic repair |

## Scope / Target / Owner Boundary

Allowed: modify exactly the four paths in Required Artifact Manifest, run
disposable local tests and start child `pwsh` processes only for hermetic
self-tests.

Forbidden: any fifth path; real source read/write; credentials; `runas`;
alternate-user execution; Party C/Group 4; T3E; admission; network/provider;
public-sync; deployment; staging or commit; mutation of thirteen parked paths.

Risk ceiling: P3 elevated local security/concurrency tooling. No external
effect and no durable source effect are authorized.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3C-C1-AR1-TRANSACTION-ARCHITECTURE-PROOF-CLOSURE","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["scripts/acel_g1_party_b_group3_observation_writer.ps1","governance/compat/check_acel_g1_registry_observation_log.py","governance/compat/test_check_acel_g1_registry_observation_log.py","docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md","docs/baselines/CVF_GC018_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_REOPEN_2026-09-22.md","docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts","docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md","docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json","docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md","docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json","docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md","docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md","docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md","docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md","docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md","governance/compat/check_task_class_calibration_owner_evidence.py","governance/compat/test_check_task_class_calibration_owner_evidence.py"],"claims":["hermetic AR1 correction pending independent Local review"],"requiredProof":["real peer-process exclusion","exception-safe guard acquisition and release","exact applied and restored security semantics","extra-allow and deny adversaries","final canonical return hash binding"],"operatorCheckpoints":["Party B real execution","Group 3 source creation","Party C provisioning","Group 4 establishment","T3E wiring","candidate admission"],"forbiddenEffects":["credential access","alternate-user execution","real source read or write","parked path mutation","fifth output path","worker stage or commit","provider live public or deployment effect"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md","completenessClaimChanged":false}}
```

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T3C-C1-AR1-TRANSACTION-ARCHITECTURE-PROOF-CLOSURE

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

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3c-c1-transaction-architecture-v2-problem","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["peer-process-exclusion-proof","exception-safe-guard-lifetime","exact-security-rollback-proof","complete-security-adversary-matrix","final-return-evidence-binding"],"reopened":[],"current":["peer-process-exclusion-proof","exception-safe-guard-lifetime","exact-security-rollback-proof","complete-security-adversary-matrix","final-return-evidence-binding"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3C-C1-AR1-DISPATCH","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: Local independently launches two PowerShell processes against
a disposable log and observes named barrier transitions across validation and
rollback.

negativeMutationClasses: post-acquire initialization failure; peer attempt
during DACL/final validation; rollback with pending peer; extra allow ACE;
deny ACE; inheritance; wrong owner; restored-descriptor mismatch; final return
digest drift.

expectedInformationGain: distinguish real cross-process exclusion and exact
security restoration from passing in-process shape tests.

rerunCostReason: bounded disposable probes decide tooling acceptance without
credentials, alternate users or real sources.

reviewerDecisionOwner: LOCAL

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-G1-T3C-C1-AR1-TRANSACTION-ARCHITECTURE-PROOF-CLOSURE --title "ACEL G1 T3C-C1 AR1 Transaction Architecture Proof Closure" --date 2026-09-22 --base 6e85f0b9a --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence NONE --scec-problem-key acel-g1-t3c-c1-transaction-architecture-v2-problem --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope INTEGRATED_ROOT_CONTRACT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | replaced placeholders with source-verified AR1 architecture, exact dirty-lane accounting and deterministic acceptance oracles |
| checkerReadAheadConfirmation | all files listed in Checker Source Read-Ahead Block were inspected before finalizing the packet |
| docOnlyNewFields | final return preGateHash, postGateHash and NO_POST_GATE_MUTATION evidence |
| claimBoundary | dispatch authoring provenance only; no concurrency, security or source acceptance claim |

## Required Artifact Manifest

| Artifact | Starting SHA-256 | Required worker action |
|---|---|---|
| `scripts/acel_g1_party_b_group3_observation_writer.ps1` | `65ef985f64e7052042224af238d7675a59f6bc76f95d130b30cab710dedecf39` | implement AR1 guard/process/security contract and deterministic self-tests |
| `governance/compat/check_acel_g1_registry_observation_log.py` | `632e22188401379bf3af3b479de718be44db55cfd78a67b49c6cf72860f086d5` | change only for a demonstrated checker-contract dependency; otherwise preserve bytes |
| `governance/compat/test_check_acel_g1_registry_observation_log.py` | `c1c948ee9fad8458b8a66d4422782002d85d260182cc3556ce4b29879d7f0953` | retain existing coverage; add only checker-relevant regression if checker changes |
| `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md` | `f9b1232c44fe2e91adbe750b58f2fbead03e6922bf491d976a73863ad1fa95d8` | replace R1/R2 evidence in place with complete AR1 return; never create another return |

No output path may be added, renamed, copied or deleted.

## Pre-Existing Dirty Path Exemptions

The following thirteen untracked paths predate AR1 and are read-only. Capture
and compare their SHA-256 values before and after work; do not edit or stage:

- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts`
- `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md`
- `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json`
- `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md`
- `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json`
- `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md`
- `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md`
- `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md`
- `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md`
- `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md`
- `governance/compat/check_task_class_calibration_owner_evidence.py`
- `governance/compat/test_check_task_class_calibration_owner_evidence.py`

These paths appear in the routing manifest solely because the shadow router
accounts for the complete dirty worktree. Their exemption and forbidden-effect
classification override mutation: they are not AR1 worker-owned paths.

## Required First Reads

- `CVF_SESSION_MEMORY.md` and the bootstrap-selected active handoff.
- `docs/reference/guard_orientation/README.md` and the literal-format gotchas reference.
- the AR1 baseline, this work order and the R2 terminal review.
- all four files in Required Artifact Manifest.
- every checker named by Checker Source Read-Ahead Block.

## Pre-Flight Checks

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
git diff --cached --name-only
Test-Path governance/sources/registry_observation_log/LOG.jsonl
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected: committed AR1 order is present; staging is empty; exactly thirteen
parked and four AR1 worker paths are untracked; real Group 3 log is absent; the
worker records any out-of-lane historical advisory without editing it.

## Write Ownership

Owned files: exactly the four rows in Required Artifact Manifest.

Write mode: modify-listed in place. No create, rename, copy, delete, stage or
commit permission. Every other repository path is forbidden.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing Group 3 writer, focused checker/test and canonical return only |
| Storage decision | modify in place; create no file, directory, index, aggregate or durable store |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | real Group 3 log remains absent and operator-gated |

## Implementation Contract

### Real peer-process protocol

- Add a test-only peer parameter set to the existing writer script; it must be
  unreachable from `-ExecuteWrite` production flow unless explicitly selected
  by self-test orchestration.
- Launch a genuine second `pwsh` process. Use unique named ready, attempting,
  entered, parent-release and peer-complete events. Dispose every process and
  event in `finally`; fail on nonzero child exit or bounded event timeout.
- Do not use sleeps as correctness evidence. A timeout is only a deadlock
  safety bound, never proof that exclusion worked.
- Hold the parent guard while the peer reports attempting. Prove entered is
  false before DACL read-back/final validation completes. In the rollback
  variant, complete rollback before release; then require peer entry, current
  byte re-read, one append, valid final chain and zero exit.

### Exception-safe acquisition and transaction lifetime

- Guard variable starts null. Caller acquisition, directory/file checks,
  byte/security snapshots and every mutation occur inside one protected
  `try/finally`.
- The acquisition helper must use its own cleanup path so any injected failure
  after OS acquisition releases/disposes before rethrow. Prove with a second
  process acquiring the same guard after the injected failure.
- The guard spans directory/file creation, append/flush, DACL apply/read-back,
  final chain validation, success or fully verified rollback.

### Security application and restoration

- Normalize owner SID, protection flag and every explicit ACE into a semantic
  multiset tuple: SID, allow/deny, numeric rights, inheritance and propagation.
- Exact success policy contains only required Party B, SYSTEM and
  Administrators allow tuples; no deny, inherited or unexpected tuple.
- Read back after apply. Wrong owner, inheritance, one extra allow ACE and one
  deny ACE each fail with stable taxonomy and trigger rollback.
- After rollback, re-read exact bytes and semantic descriptor. Any difference
  raises rollback failure preserving primary and rollback contexts.

### Canonical return and final evidence sequence

1. Update the declared return path completely, including actual final counts,
   commands, full status and `independentProbeDisposition: PENDING_REVIEWER_EXECUTION`.
2. Confirm no alternate AR1/R3 return exists and changed T3C paths equal the
   four-path manifest.
3. Compute canonical return SHA-256 as `preGateHash`.
4. Run the exact worker-return fast command below with this AR1 order.
5. Compute `postGateHash`; require ordinal lowercase equality with
   `preGateHash`. If unequal, the return is not review-ready.
6. Make no file edit after `postGateHash`. The chat response must state the
   canonical path, digest, command, exit code and `NO_POST_GATE_MUTATION`.

## Worker Autonomy / No-Question Rule

Repair allowed-scope failures and rerun without asking the operator. Stop only
for a source contradiction, fifth path requirement, parked drift, credentials,
alternate-user/real-source need, or irreparable mandatory failure outside the
four owned paths.

## Core Guard Self-Protection Authorization

| Field | Value |
|---|---|
| Authorized guard-maintenance scope | bounded AR1 Group 3 writer/checker correction; no hook, catalog or general checker change |
| Protected paths | `governance/compat/check_acel_g1_registry_observation_log.py`; `governance/compat/test_check_acel_g1_registry_observation_log.py` |
| Operator authorization | fresh 2026-09-22 instruction to issue a work order and continue repair |
| Rollback boundary | all four paths remain uncommitted; reviewer may reject the entire AR1 diff without touching parked or real-source state |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

Resolver evidence: `python governance/compat/run_adif_defect_resolver.py --task-class "CODE_CHANGE" --role dispatcher --lifecycle-phase dispatch --json` returned zero candidates on 2026-09-22.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | first dispatch envelope; source table; initial convergence sentinels; protected paths; active work-order return binding; no-commit status; trace; public disposition |
| gateRunPurpose | confirm closeable AR1 dispatch before worker execution |
| claimBoundary | packet and return shape only; not proof that concurrency or security behavior is correct |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| five blocking defects | accepted Local review | `docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md` | Findings / Position | T3C-C1-R2-RV-1 through RV-5 | Local reviewer | ACCEPT |
| stopped predecessor chain | convergence authority | `docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md` | Decision / Disposition; Semantic Convergence Outcome | `STOP_REASSESS_ARCHITECTURE`; `NO_SUCCESSOR` | SCEC | ACCEPT |
| fresh reopen contract | architecture authority | `docs/baselines/CVF_GC018_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_REOPEN_2026-09-22.md` | Architecture Contract | peer process; safe lifetime; exact security; hash binding | AR1 baseline | ACCEPT |
| current guard window | implementation fact | `scripts/acel_g1_party_b_group3_observation_writer.ps1` | `Append-ObservationTransaction` | `New-TransactionGuard` precedes protected transaction try | pending writer | ACCEPT |
| incomplete peer proof | test fact | `scripts/acel_g1_party_b_group3_observation_writer.ps1` | T3C-C1-16 | deterministic name/type checks only | pending writer self-test | ACCEPT |
| canonical return selection | machine fact | `governance/compat/check_independent_review_probe_admission.py` | `_declared_worker_return_path` | `WORKER_RETURN_PATH_RE`; `--active-work-order` | independent probe gate | ACCEPT |

## Current Runtime Freshness Verification

Current pending writer source was re-read on 2026-09-22. `rg` confirms
`New-TransactionGuard` acquisition occurs before the outer protected block and
T3C-C1-16 contains only name/type/acquisition checks. The terminal review and
current source, not a stale provider memory, establish the defect facts. No
claim is made about real Party B or real source behavior.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | AR1 baseline and order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | AR1 packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact four worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | canonical worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact four worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | canonical return and owned code | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| final_return_hash | REVIEW | worker | WORKER_RETURN | canonical return | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned four paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | final_return_hash |
| independent_peer_security_probe | PRE_MATERIAL_COMMIT | reviewer | REVIEW | disposable fixtures only | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted four paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | independent_peer_security_probe |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split material and continuity ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> no-commit INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | DISPATCH_AUTHORING -> IMPLEMENTATION -> REVIEW -> SESSION_SYNC; real execution excluded |
| baseHeadFor(phase) | dispatchBaseHead=`6e85f0b9ab2c031ec4ccf4efa21a19e8fd1ad8da`; executionBaseHead captured by worker; closureBaseHead captured by Local |
| changedSetScope(phase) | exact four worker paths during implementation; baseline and order during dispatch |
| traceScope(phase, actor) | hashes, status, process barriers, failure injections, security descriptors, tests and gates |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; Local owns all commits |
| crossBatchIsolation | thirteen parked paths remain byte-identical and unstaged |
| nextMoveSurfaces | Local review only; real Party B remains a later operator checkpoint |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT after operator forwards this committed order

laneOwnedPaths: exact four paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: canonical return digest, exact four-path delta, thirteen parked hashes, empty staging and no post-gate mutation

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON: bounded local implementation has no discovery-audit manifest

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_acel_g1_registry_observation_log.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The existing return must contain Purpose, Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Decision / Disposition, Changed
Files, Command Evidence, No-Commit Statement, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Machine Closure Package, External Knowledge Intake Routing, Epistemic Process
Block, Public Export Disposition, Claim Boundary, executionBaseHead, full status
and final hash-binding evidence. Non-applicable sections remain present with a
reason.

## Execution Plan

1. Freeze execution base, four owned hashes, thirteen parked hashes, status,
   empty staging and real-log absence.
2. Move acquisition and all fallible transaction state under exception-safe
   guard ownership; add post-acquire failure injection.
3. Add semantic security normalization, applied-state read-back and exact
   restored-state verification.
4. Add true second-process peer mode and named-barrier success/rollback tests,
   plus extra-allow and deny cases.
5. Run focused suites, update only the canonical return, run the final bound
   gate sequence, then make no further edit.

## Evidence Requirements

- child process identity, command, exit code and named barrier transitions;
- proof `ENTERED` is unsignaled during parent validation/rollback and signaled
  only after release;
- post-acquire exception cleanup followed by successful peer acquisition;
- exact applied and restored semantic security descriptor comparisons;
- rejection of extra allow, deny, inheritance and wrong owner;
- final valid chain containing the peer append once after rollback variant;
- exact test counts, real-log absence, four-path delta, parked hash match,
  empty staging and canonical return pre/post gate digest equality.

## Acceptance Criteria

- [ ] Real second process and deterministic named barriers prove exclusion; no sleep-based correctness assertion.
- [ ] Every acquisition and initialization exception releases the mutex.
- [ ] Outer guard spans first possible mutation through validated success or verified rollback.
- [ ] Applied and restored owner/protection/complete ACE multiset read back exactly.
- [ ] Extra allow ACE and deny ACE adversaries fail closed alongside inheritance and wrong owner.
- [ ] Parent rollback cannot erase a later peer append; final chain is valid.
- [ ] Exactly four worker paths change; no alternate return, real source or parked drift.
- [ ] Final active-work-order gate exits zero and canonical return hash is unchanged across it.
- [ ] Return declares `COMPLETE_PENDING_REVIEW` and `independentProbeDisposition: PENDING_REVIEWER_EXECUTION` only after all prior rows pass.

Fail closed on any missing peer, timing-based substitution, mutex leak, partial
security comparison, rollback mismatch, fifth path, hash drift, failed final
gate, staging, parked change or real-source effect.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m pytest governance/compat/test_check_acel_g1_registry_observation_log.py -q
python governance/compat/check_acel_g1_registry_observation_log.py --self-test
pwsh -NoProfile -File scripts/acel_g1_party_b_group3_observation_writer.ps1 -SelfTest
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_acel_g1_registry_observation_log.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

Final binding sequence, after the return is otherwise complete:

```powershell
$returnPath = 'docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md'
$preGateHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $returnPath).Hash.ToLowerInvariant()
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_acel_g1_registry_observation_log.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md
if ($LASTEXITCODE -ne 0) { throw 'FINAL_WORKER_RETURN_GATE_FAILED' }
$postGateHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $returnPath).Hash.ToLowerInvariant()
if ($preGateHash -cne $postGateHash) { throw 'FINAL_WORKER_RETURN_HASH_DRIFT' }
$postGateHash
```

## Review Gate

Local first recomputes the reported return digest and rejects on mismatch.
Local consumes valid aggregate evidence without broad duplication, then runs a
separate two-process barrier probe, post-acquire cleanup probe, semantic DACL
adversaries and final-return gate. Local does not use credentials, alternate
users or real sources.

## Pre-Dispatch Gate Disposition

The full pre-dispatch bundle passed 82 of 83 controls. The sole failure is the
same three pre-existing, out-of-lane T2A/T2B/calibration returns whose older
work orders lack the later independent-probe declaration. They are explicit
read-only parked paths in this packet. The required changed-lane command with
this AR1 work order passes and reports all three as out-of-lane known findings:

```powershell
python governance/compat/check_independent_review_probe_admission.py --enforce --changed-lane-only --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md
```

All other dispatch, routing, architecture, closeability, structure, security,
trace and evidence controls pass. This disposition does not waive an AR1-lane
failure and does not authorize mutation of the three parked returns.

## Closure Checklist

- [ ] Exact four-path manifest and thirteen parked hashes reconcile.
- [ ] Focused Python, checker self-test, writer self-test and final fast gate pass.
- [ ] Independent peer/security probes pass without real-source access.
- [ ] Canonical return digest matches the worker response and no later edit exists.
- [ ] Staging is empty; worker made no commit.
- [ ] Local records acceptance or rejection before any real Party B checkpoint.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | reviewer creates a new completion review only if substantive disposition cannot safely live in the canonical return |
| reviewerOwnedClosurePaths | accepted four worker paths and any required Local review artifact |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | committed dispatch and active-work-order binding | REQUIRED |
| Completion or reviewer artifact | canonical worker return, then Local disposition | final hash, findings and command evidence | REQUIRED |
| Roadmap state | N/A with reason | no roadmap closure in AR1 | N/A with reason |
| Registry JSON | N/A with reason | real Group 3 log must remain absent | N/A with reason |
| Registry Markdown | N/A with reason | no registry companion mutation | N/A with reason |
| External evidence digest | N/A with reason | local hermetic evidence only | N/A with reason |
| System loop interlock | Party B real execution | remains closed | REQUIRED |
| Session continuity | active handoff/state | separate dispatcher and closure sync commits | REQUIRED |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF Local orchestrator/dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | AR1 fresh architecture reopen, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | governed reads, hashes, source inspection, apply_patch, dispatch gates and git |
| Target paths | AR1 baseline and work order; worker later owns exact four pending paths |
| Allowed scope source | fresh operator instruction plus R2 terminal review reassessment route |
| Before status evidence | clean worktree requirement is represented by explicit shared-lane isolation: HEAD `6e85f0b9a`; thirteen parked plus four rejected T3C paths; staging empty |
| After status evidence | AR1 baseline/order prepared; worker and parked paths untouched by dispatcher |
| Diff evidence | `git diff --name-status` limited to AR1 dispatch artifacts before commit |
| Approval boundary | fresh hermetic architecture and implementation dispatch only |
| Claim boundary | no real Party B/source, provider, network, public or deployment effect |
| Agent type | Local dispatcher/orchestrator |
| Invocation ID | `acel-g1-t3c-c1-ar1-dispatch-2026-09-22` |
| Expected manifest | AR1 baseline and AR1 work order |
| Actual changed set | AR1 baseline and AR1 work order before dispatch commit |
| Manifest delta | MATCH before commit |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | exact four-path hermetic AR1 correction |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: terminal review, AR1 baseline, hashes and later worker return |
| actionEvidence | ACTION_EVIDENCE_PRESENT: deterministic child-process/security tests and final gate |
| invocationBoundary | local governed edits and disposable child-process fixtures only |
| interceptionBoundary | no IDE, shell, Git, filesystem or provider interception claim |
| claimLanguage | corrected tooling remains pending independent Local acceptance |
| forbiddenExpansion | credentials, alternate user, real source, Party C/Group 4, T3E, admission, provider, public, deployment or automatic successor |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md` |
| Chain map route | N/A with reason: direct Local review-to-internal implementation route |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | AR1 baseline and this order |
| Disposition | local first-party correction only |
| Claim boundary | no remote research authority, external corpus, CLI/MCP adapter or provider claim |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: AR1 implementation; decision owner: Local.
The operator only copies this committed work order to the shared-workspace
worker. That worker remains internal and must not invoke Claude CLI or an
external research lane.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: AR1 will replace shape-level concurrency evidence
with a real peer process, eliminate every guard-release gap, prove exact
security restoration and bind the final return to its gate execution.

Evidence Comparison Requirement: compare every finding with its dedicated
oracle and report observed barrier/security/hash values, not only totals.

Contradiction Handling Requirement: any contradiction requires a named
Contradiction Or Gap Disposition and narrowed claim; no silent waiver.

Claim Update Requirement: record confirmed, revised, narrowed or invalidated
for T3C-C1-R2-RV-1 through RV-5.

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| peer-process and lifetime proof gaps | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | explicit AR1 process/barrier and acquisition contracts |
| security rollback/adversary gaps | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | semantic descriptor and full negative matrix required |
| final return identity gap | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | AR1 hash binding now; reusable fast-gate receipt stays a separate foundation candidate |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private corrective tooling dispatch; no public-sync authority.

## Claim Boundary

This order authorizes only four-path hermetic AR1 implementation and evidence.
It does not accept existing pending code, revive the stopped R2 chain, permit a
fifth path, commit, credentials, alternate-user execution, real source access,
Party C/Group 4, T3E, candidate admission, provider/network/live proof,
public-sync, deployment or production readiness.

## Operator Checkpoint

No operator action is required during hermetic AR1 implementation. If Local
later accepts the tooling, real Party B execution and Group 3 creation remain a
separate explicit checkpoint with the existing dedicated local account.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for a verified source contradiction, required
fifth path, parked drift, credential/alternate-user/real-source dependency or
mandatory failure that cannot be repaired within the four owned paths. Routine
test, formatting and gate failures inside scope must be repaired and rerun.
