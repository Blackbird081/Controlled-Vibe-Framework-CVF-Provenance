# CVF Agent Work Order - ACEL G1 T3D-C3 Actual-Token Disposable Runner

Memory class: governed-worker-dispatch

docType: work_order

Status: APPROVED_FOR_EXECUTION

providerExecutionAuthority: FORBIDDEN

Batch ID: ACEL-G1-T3D-C3-ACTUAL-TOKEN-DISPOSABLE-RUNNER

Dispatch base head: `3ad4903dec375121b0af1a3c6774078ca199b8cf`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: shared-workspace INTERNAL_AGENT Local implementation role

Reviewer/closer: Local reviewer role after worker return; same-thread role switch is not independent actor review

Worker return path: `docs/reviews/CVF_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_WORKER_RETURN_2026-09-23.md`

## Dispatch Prompt Envelope

Role: INTERNAL_AGENT implementation worker for the bounded Group 4 disposable
actual-token runner.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_2026-09-23.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker must capture exact HEAD before the first material edit.

Current-time notes: the operator approved Local continuation on 2026-09-23.

Do-not-misread notes: implement and hermetically test only. Do not invoke Party
B/C, prompt for a password, mutate an account or real source, or claim
actual-token proof.

Required first actions: read startup continuity, guard orientation, literal
gotchas, this packet, paired baseline, controlling C0-R1 amendment, proof
packet, readiness audit and listed checker sources before editing.

Return contract: leave all worker outputs uncommitted and return
`COMPLETE_PENDING_REVIEW` with `independentProbeDisposition:
PENDING_REVIEWER_EXECUTION`, or `BLOCKED_WITH_REASON` for an authority/scope
contradiction that cannot be repaired inside the manifest.

## Purpose

Implement the governed execution boundary that is missing between accepted
C1-R2 primitives and the later operator-run Party B/C proof. Success is a
three-script, schema-bound, fail-closed runner with current-token hermetic tests
and no alternate-principal or real-source action.

## Authority Chain

- Operator instruction: approval to continue, 2026-09-23.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Readiness decision: `docs/audits/CVF_ACEL_G1_T3D_C1_R2_POST_CLOSURE_ACTUAL_TOKEN_EXECUTION_READINESS_AUDIT_2026-09-23.md` at `a765880e4`.
- Controlling contract: `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md`.
- Static proof packet: `docs/audits/CVF_ACEL_G1_T3D_GROUP4_DISPOSABLE_ROOT_PROOF_PACKET_2026-09-23.md`.
- GC-018: `docs/baselines/CVF_GC018_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_2026-09-23.md`.
- Active handoff: `AGENT_HANDOFF_V63_2026-09-18.md`.

Authority boundary: conflicts stop implementation; this order cannot widen the
accepted matrix, real-source paths, principal identities or operator checkpoint.

## Agent Roles

| Role | Responsibility |
|---|---|
| Local orchestrator/dispatcher | authors exact contract and manifests |
| Local implementation worker | creates three scripts, hermetic tests and worker return without commit |
| Local reviewer/closer | evaluates returned evidence; does not call same-thread review independent actor proof |
| operator | later enters credentials only after a separately opened checkpoint |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3D-C3-ACTUAL-TOKEN-DISPOSABLE-RUNNER","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"SINGLE_ROLE","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reviews/","scripts/"],"claims":["disposable actual-token runner implementation only; no alternate-principal or real-source proof"],"requiredProof":["strict disposable containment","exact principal and action binding","complete C0-R1 matrix plan","semantic security capture","real second-process hermetic peer","fail-closed Local finalizer","pending independent Local probe"],"operatorCheckpoints":["Party B/C actual-token execution","Group 4 source creation","T3E wiring","candidate admission"],"forbiddenEffects":["credential access","Party B or Party C execution","real Group 4 source read/write","worker commit","provider/live/public/deployment","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G1_T3D_C1_R2_POST_CLOSURE_ACTUAL_TOKEN_EXECUTION_READINESS_AUDIT_2026-09-23.md","completenessClaimChanged":false}}
```

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one Local same-thread actor for dispatch and implementation |
| role set | dispatcher, implementation worker, later bounded reviewer; never independent reviewer actor |
| delegation depth | zero; subagents forbidden for this tranche |
| evidence basis | governed sources, executable hermetic tests and final file hashes |
| gate sequence | pre-dispatch, pre-implementation, focused tests, worker-return fast, reviewer gate |
| self-review boundary | implementation worker leaves probe pending and cannot claim independent acceptance |
| role separation ledger | explicit phase switch and operation trace; commit owned only by closer phase |
| escalation condition | Party B/C execution, credential, account/ACL outside disposable fixture, real source, writer modification or scope expansion |

## Scope

Allowed scope:

- create exactly three PowerShell runner scripts and one worker return;
- generate a complete later-run command packet without launching it;
- exercise all logic with current-token hermetic fixtures below `%TEMP%`;
- use separate real OS child processes in hermetic peer/crash tests;
- capture complete file/security state and exact evidence hashes;
- repair allowed-scope test or gate defects without asking the operator.

Forbidden scope:

- Party B/C process creation, `runas`, credential prompt/read/store, account mutation;
- real `governance/sources/issuer_registry/` creation or access;
- modifying accepted C1-R2 writer or recovery scripts;
- opening T3E, provider/live/public/deployment or candidate admission;
- staging or committing worker output.

Risk ceiling: R3 high-risk local transaction tooling, hermetic execution only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`PURE_LOCAL_IMPLEMENTATION`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "PURE_LOCAL_IMPLEMENTATION" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | no matched historical defect changes this packet; active foundation controls still apply |

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, bootstrap and active handoff.
2. `docs/reference/guard_orientation/README.md` and literal gotchas.
3. Paired baseline, readiness audit, C0-R1 amendment, proof packet and C1-R2 review.
4. The four accepted Group 4 scripts and all checker sources below.

## Pre-Flight Checks

- capture `git rev-parse HEAD` and `git status --short --untracked-files=all`;
- confirm every required new path is absent and forbidden source path absent;
- run ADIF resolver and both autorun phases;
- stop on any out-of-scope change or failed gate not repairable inside manifest.

## Worker Autonomy / No-Question Rule

Repair every allowed-scope implementation, test, encoding and gate defect
directly. Routine algorithms, schema fields and test repairs are worker-owned.
Stop only when completion requires a forbidden action,
authority change, principal execution, credential or real-source mutation.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| actual-token matrix is mandatory before source authority | contract | `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | Required Actual-Token Proof Matrix | eleven probe classes and complete postconditions | C0-R1 contract | ACCEPT |
| current runner gap and seven-gate checkpoint | readiness | `docs/audits/CVF_ACEL_G1_T3D_C1_R2_POST_CLOSURE_ACTUAL_TOKEN_EXECUTION_READINESS_AUDIT_2026-09-23.md` | Required Successor Tooling Boundary; Exact Operator Checkpoint | `BLOCKED_ACTUAL_TOKEN_ENTRYPOINT_REQUIRED` | Local readiness decision | ACCEPT |
| accepted writer functions are hermetic primitives, not actual-token proof | review | `docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_LOCAL_REVIEW_2026-09-23.md` | Claim Update | current-token TestPolicy scope | Local C1-R2 review | ACCEPT |

## Current Runtime Freshness Verification

`rg` of current script parameter sets confirms that the real writer modes bind
canonical repository paths, peer/crash modes are test-only, and the disposable
harness accepts only `-SelfTest` and returns `realPrincipalClaimed=false`.
Exact script hashes are frozen in the readiness audit at `a765880e4`.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned artifacts | exact six-path `Test-Path` before authoring returned false for all paths | NO_COLLISION |
| existing actual-token runner | `rg -n "actual.token|actual_token" scripts docs/audits docs/work_orders` found only contract/readiness references, not an accepted runner | OWNER_SURFACE_NOT_FOUND_EXPECTED |
| collision decision | create the exact manifest paths below; do not reuse canonical writer entrypoints | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_forbidden_filesystem_state.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | first-section envelope, source-verification columns, no-question rule, required manifests, high-risk applicability and nine-key JSON, operator checkpoint, trace labels, worker-return contract and closeability graph |
| gateRunPurpose | confirm packet readiness after source inspection; gates are not source evidence |
| claimBoundary | dispatch/static shape only; no runtime proof |

## High-Risk Local Transaction Proof Contract

High-Risk Local Transaction Proof Applicability: REQUIRED

```json
{
  "transactionTarget": "disposable Group 4 reservation publication, denial matrix, evidence capture and exact recovery",
  "productionPathPeer": {
    "kind": "REAL_SECOND_PROCESS",
    "invocationPath": "scripts/acel_g1_group4_actual_token_principal_probe.ps1",
    "mutationPath": "role-bound disposable reservation transaction and negative operation matrix"
  },
  "deterministicBarrierProtocol": {
    "events": ["READY", "START_ATTEMPT", "ATTEMPTING", "PARENT_RELEASE", "ENTERED", "COMPLETE"],
    "timeoutRole": "DEADLOCK_SAFETY_ONLY"
  },
  "enteredBeforeReleaseOracle": "REJECT_ENTRY_BEFORE_PARENT_RELEASE",
  "postAcquireFailureInjection": {
    "point": "AFTER_ACQUIRE_BEFORE_MUTATION",
    "cleanupProof": "SUBSEQUENT_PEER_ACQUIRES"
  },
  "semanticSecurityTuple": {
    "fields": ["ownerSid", "protectionState", "inheritanceState", "aces"],
    "aceFields": ["sid", "rights", "accessType", "isInherited", "inheritanceFlags", "propagationFlags"],
    "normalization": "SORT_COMPLETE_ACE_TUPLES"
  },
  "rollbackExactness": {
    "comparison": "SEMANTIC_PRESTATE_EQUALS_POST_ROLLBACK",
    "adversaries": ["EXTRA_ALLOW", "DENY", "INHERITED", "WRONG_OWNER"]
  },
  "finalEvidenceHashBinding": {
    "algorithm": "SHA256",
    "scope": "EXACT_RETURN_BYTES",
    "capture": "BEFORE_AND_AFTER_FINAL_REQUIRED_GATE",
    "equality": "REQUIRED",
    "postGateMutation": "FORBIDDEN"
  },
  "independentProbeRequired": {
    "required": true,
    "owner": "LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER",
    "workerReturnDisposition": "PENDING_REVIEWER_EXECUTION"
  }
}
```

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T3D-C3-ACTUAL-TOKEN-DISPOSABLE-RUNNER
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
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "acel-g1-t3d-c3-actual-token-disposable-runner",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": ["ACTUAL_TOKEN_ENTRYPOINT_MISSING", "ACTUAL_TOKEN_PROOF_PENDING", "GROUP4_SOURCE_NOT_CREATED", "T3E_NOT_OPEN"],
    "resolved": [],
    "retained": ["ACTUAL_TOKEN_ENTRYPOINT_MISSING", "ACTUAL_TOKEN_PROOF_PENDING", "GROUP4_SOURCE_NOT_CREATED", "T3E_NOT_OPEN"],
    "new": [],
    "reopened": [],
    "current": ["ACTUAL_TOKEN_ENTRYPOINT_MISSING", "ACTUAL_TOKEN_PROOF_PENDING", "GROUP4_SOURCE_NOT_CREATED", "T3E_NOT_OPEN"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON

Reason: internal shared-workspace implementation; no external invocation is
used or counted.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired dispatch packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact four worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact four worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact four worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| independent_local_probe | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer-owned disposable fixture | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | exact worker range and optional completion review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | independent_local_probe |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local terminal completion evidence | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | same Local thread dispatches and implements; independent actor review is not claimed |
| phase | dispatch then implementation then pending review |
| baseHeadFor(phase) | dispatchBaseHead=`3ad4903dec375121b0af1a3c6774078ca199b8cf`; executionBaseHead=worker capture; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exact six-path worker manifest plus paired dispatch artifacts |
| traceScope(phase, actor) | one operation trace per governed artifact with explicit role phase |
| commitOwner(phase) | worker forbidden; Local closer only after review |
| crossBatchIsolation | clean worktree required; no parked or unrelated paths |
| nextMoveSurfaces | worker return, Local disposition, then separate continuity |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: Local implementation role after committed dispatch

laneOwnedPaths: exact four paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact manifest and empty staged set

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: reviewer independently builds a disposable command packet,
executes current-token test policy and verifies containment, identity binding,
matrix completeness, semantic state and finalizer fail-closed behavior.

negativeMutationClasses: real-source path, wrong SID/role/action, elevated
token, missing or duplicate matrix row, altered evidence hash, early peer
entry, unknown residue and non-target/parent drift.

expectedInformationGain: detect a runner that passes worker-owned selftests but
can escape containment, omit matrix evidence or self-certify a PASS.

rerunCostReason: one bounded disposable fixture is proportionate to the
high-risk future cross-principal boundary; broad duplicate review is forbidden.

reviewerDecisionOwner: LOCAL

## Required Artifact Manifest

| Path | Status | Purpose |
|---|---|---|
| `scripts/acel_g1_group4_actual_token_coordinator.ps1` | NEW | Local-only setup, command packet and hermetic orchestration |
| `scripts/acel_g1_group4_actual_token_principal_probe.ps1` | NEW | exact-token bounded principal action surface |
| `scripts/acel_g1_group4_actual_token_local_finalizer.ps1` | NEW | Local-only evidence adjudication and cleanup decision |
| `docs/reviews/CVF_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_WORKER_RETURN_2026-09-23.md` | NEW | worker evidence and pending independent probe |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `governance/sources/issuer_registry/` | real Group 4 source remains unopened |
| `scripts/acel_g1_party_c_group4_registry_writer.ps1` | accepted C1-R2 source, modification requires new authority |
| `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` | accepted C1-R2 source, modification requires new authority |
| `scripts/acel_g1_group4_admin_recovery.ps1` | accepted recovery source, modification requires new authority |
| `scripts/acel_g1_group4_disposable_acl_probe.ps1` | accepted reviewer harness, modification requires new authority |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `governance/sources/issuer_registry/` | ABSENT | ABSENT | stop and return to Local reviewer |

## Pre-Existing Dirty Path Exemptions

N/A with reason: dispatch worktree is clean.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing `scripts/` ACEL Group 4 operational tooling family |
| Storage decision | add three adjacent bounded runner scripts; no new framework root or aggregate |
| Existing aggregate impact | none |
| Generated state impact | none during worker implementation |
| Durable governance boundary | C0-R1 owns semantics; work order owns runner scope; scripts own implementation |
| Duplicate-owner control | runner orchestrates accepted primitives and does not create a second contract/checker owner |

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| containment | coordinator | `PROBE_REAL_SOURCE_REACHED` and reparse rejection | Yes |
| identity | principal probe | exact account/SID and non-elevated checks | Yes |
| complete matrix | coordinator and worker return | all eleven C0-R1 probe classes | Yes |
| local verdict | finalizer | `PASS_ACTUAL_TOKEN_PROOF` and `INCONCLUSIVE_OR_FAILED` | Yes |
| no credential storage | all scripts | no password parameter, file or log field | Yes |
| pending review | worker return | `PENDING_REVIEWER_EXECUTION` | Yes |

## Write Ownership

Write mode: create-only for the exact four worker paths. No other source,
session, state or accepted Group 4 path may be edited by the worker.

## Execution Plan

1. Capture execution base and run pre-implementation gate.
2. Create coordinator schema, containment, exact setup plan and command packet.
3. Create principal probe with identity/action allowlist and evidence capture.
4. Create Local finalizer with completeness/hash/poststate verdict rules.
5. Add selftests inside the three scripts, including real child-process barrier
   and failure-injection cases under current-token TestPolicy only.
6. Create worker return, freeze exact bytes, run final gates and return without
   staging or commit.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: three bounded scripts can make the later
principal proof reproducible without launching a principal in this tranche.

Evidence Comparison Requirement: worker return compares hermetic results and
source hashes to that prediction.

Contradiction Handling Requirement: any need to alter accepted writer scripts,
touch real source or weaken the matrix returns `BLOCKED_WITH_REASON`.

Claim Update Requirement: return states whether entrypoint implementation is
ready for reviewer probe while actual-token proof remains pending.

## Evidence Requirements

- exact script hashes, selftest counts and commands after final edit;
- negative identity, path, schema, hash, missing-row and residue cases;
- real second-process barrier and post-acquire cleanup evidence;
- `git diff --check`, exact changed set and no-commit status;
- detached pre/post worker-return SHA-256 around the final required gate.

Base-anchor evidence:

- `dispatchBaseHead`: `3ad4903dec375121b0af1a3c6774078ca199b8cf`
- `executionBaseHead`: worker captures before edit
- `closureBaseHead`: pending reviewer
- Commit mode: WORKER_MUST_NOT_COMMIT

## Verification Commands

```powershell
pwsh -NoProfile -NonInteractive -File scripts/acel_g1_group4_actual_token_coordinator.ps1 -SelfTest
pwsh -NoProfile -NonInteractive -File scripts/acel_g1_group4_actual_token_principal_probe.ps1 -SelfTest
pwsh -NoProfile -NonInteractive -File scripts/acel_g1_group4_actual_token_local_finalizer.ps1 -SelfTest
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

## Acceptance Criteria

- [ ] exact manifest only; no accepted/real-source path changed;
- [ ] three selftests pass after final edit with sourceMutation=false and realPrincipalClaimed=false;
- [ ] eleven matrix classes are represented and completeness is fail closed;
- [ ] identity/path/elevation/role/action/schema/hash mismatches reject before mutation;
- [ ] finalizer cannot emit PASS for missing, duplicate, altered or self-certified evidence;
- [ ] no credential is accepted, emitted or persisted;
- [ ] worker return and detached digest binding pass required gate;
- [ ] `independentProbeDisposition` remains `PENDING_REVIEWER_EXECUTION`.

Fail conditions: any principal launch, password interaction, real-source touch,
accepted-writer edit, incomplete matrix, optimistic cleanup or self-accepted
independent proof blocks closure.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_WORKER_RETURN_2026-09-23.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk /
Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git
status --short; External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Machine Closure Package.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | optional; reviewer records bounded corrections in the worker return unless a separate decision is needed |
| reviewerOwnedClosurePaths | reviewer probe/receipt and optional completion review |
| closureOwner | Local reviewer/closer distinct from implementation phase |
| workerCommitPermission | FORBIDDEN |

## Review Gate

Implementation starts only after paired dispatch artifacts pass pre-dispatch.
Worker return is not acceptance. Closure requires reviewer-owned probe,
reviewer-fast, pre-commit and material/continuity choreography. Same-thread role
switch must remain disclosed and cannot satisfy the independent actor claim.

## Operator Checkpoint

`CLOSED_PENDING_TOOLING`. No operator command or credential action is requested
by this work order. A later reviewed packet must explicitly change the status
to `READY_FOR_OPERATOR_EXECUTION` before Party B/C can run.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | three-script disposable runner implementation and current-token hermetic tests |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: hermetic JSON test outputs and detached worker-return hash receipt only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: current-token disposable fixture mutations only |
| invocationBoundary | manual local script selftests; generated later-run commands are not invoked |
| interceptionBoundary | no shell/credential/runtime interception or mandatory wrapper claim |
| claimLanguage | entrypoint implementation pending Local independent probe |
| forbiddenExpansion | no Party B/C, password, real source, T3E, provider/live/public/deployment action |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T3D_C1_R2_POST_CLOSURE_ACTUAL_TOKEN_EXECUTION_READINESS_AUDIT_2026-09-23.md` |
| Chain map route | N/A with reason: direct internal implementation from committed CVF-governed sources |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | C0-R1 amendment, proof packet and this work order |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external knowledge intake |
| Claim boundary | local private runner implementation only |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: bounded local implementation; decision owner:
Local reviewer. External research is outside this work order and conveys no
private-CVF verification authority.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher |
| Provider or surface | private shared workspace |
| Session or invocation | ACEL G1 T3D-C3 runner dispatch, 2026-09-23 |
| Working directory | repository root |
| Command or tool surface | governed reads, scaffold helper, ADIF resolver, apply_patch, gates and Git |
| Target paths | paired baseline, this work order and exact worker manifest |
| Allowed scope source | user authorization plus readiness audit `a765880e4` and active continuity `3ad4903de` |
| Before status evidence | clean worktree at HEAD `3ad4903dec375121b0af1a3c6774078ca199b8cf`; six planned paths absent; real source absent |
| After status evidence | dispatch artifacts authored; no source implementation or principal execution yet |
| Diff evidence | exact paired dispatch paths before dispatch commit |
| Approval boundary | runner dispatch and hermetic implementation only |
| Claim boundary | no actual-token proof, credential, real source, T3E, provider/live/public/deployment effect |
| Agent type | Local orchestrator/dispatcher |
| Invocation ID | `acel-g1-t3d-c3-actual-token-disposable-runner-dispatch-20260923` |
| Expected manifest | paired baseline and work order for dispatch; four paths for worker return |
| Actual changed set | verified before dispatch commit |
| Manifest delta | MATCH expected paired dispatch set |
| Deletion or rename disposition | none |

## Closure Checklist

- [ ] exact manifest and all acceptance criteria pass;
- [ ] return-time closeability recheck has no unresolved implementation blocker;
- [ ] final return hash is unchanged across the final required gate;
- [ ] reviewer executes the pending probe before acceptance;
- [ ] material and continuity commits remain separate;
- [ ] operator checkpoint remains closed unless separately reviewed and opened.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for authority contradiction, forbidden path
need, real principal/credential requirement, inability to contain the fixture,
or an unrepairable high-risk contract failure. Routine allowed-scope failures
must be repaired and rerun.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Windows identity/ACL tooling; no public-sync action authorized.

## Claim Boundary

This work order authorizes only the exact current-token implementation and test
manifest. It does not authorize actual Party B/C execution, credential access,
real Group 4 source creation, issuer observation, lookup response, T3E consumer
binding, candidate admission, provider/live proof, public export or deployment.
