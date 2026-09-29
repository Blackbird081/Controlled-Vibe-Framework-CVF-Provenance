# CVF Agent Work Order - ACEL G1 T3D-C3 R1 Actual ACL Setup And Cleanup Correction

Memory class: governed-worker-dispatch

docType: work_order

Status: CLOSED_STOPPED_FAIL_CLOSED

providerExecutionAuthority: FORBIDDEN

Batch ID: ACEL-G1-T3D-C3-R1-ACTUAL-ACL-SETUP-AND-CLEANUP-CORRECTION

Dispatch base head: `a31ec4bcd13fb69b0fc76d6f4b261e48e0d68396`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: Local implementation role

Reviewer/closer: Local reviewer distinct from implementation phase

Worker return path: `docs/reviews/CVF_ACEL_G1_T3D_C3_R1_ACTUAL_ACL_SETUP_AND_CLEANUP_CORRECTION_WORKER_RETURN_2026-09-24.md`

## Dispatch Prompt Envelope

Role: Local implementation worker for the bounded coordinator repair.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C3_R1_ACTUAL_ACL_SETUP_AND_CLEANUP_CORRECTION_2026-09-24.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker captures the committed dispatch HEAD before edits.

Current-time notes: packet authored on 2026-09-24 after the operator approved
one final bounded G1 repair and parked G2-G6.

Do-not-misread notes: implementation is hermetic/current-token only. It does
not authorize UAC prepare-only, Party B/C, credentials or real-source access.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, this packet, exact sources and checker sources below.

Return contract: create the exact worker return, run required gates, leave all
worker output uncommitted and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Correct the observed root-first ACL ordering defect and make failed setup
cleanup exact and exception-preserving. Retain every containment, identity,
matrix and no-credential invariant from the accepted predecessor.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3D-C3-R1-ACTUAL-ACL-SETUP-AND-CLEANUP-CORRECTION --title "ACEL G1 T3D-C3 R1 Actual ACL Setup And Cleanup Correction" --date 2026-09-24 --base a31ec4bcd --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id ACEL-G1-T3D-C3-R1-ACL-ORDERING --prior-finding-set-digest 6cb7547879201819361278efbb5c52910151f8b859a3bdbb3d94a3ebeb4aac99 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence true --scec-problem-key ACEL-G1-T3D-C3-ACTUAL-ACL-SETUP --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_2026-09-23.md --scec-predecessor-sha256 6dc845e66df98b645f6116fafc1a07e8930429b45ddefc5193f99fd7280bbc4d --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope EXECUTABLE_IMPLEMENTATION --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic worker rework dispatch with no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed exact source, scope, proof, routing, role and stop contracts |
| checkerReadAheadConfirmation | dispatch-quality, high-risk, closeability, trace, return and structural checker sources |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no implementation or runtime result |

## Authority Chain

- operator authorization in the active session to perform one bounded G1 repair;
- active handoff mode `acel_g1_group4_actual_token_prepare_failed_closed_repair_selection_next`;
- paired GC-018 baseline for this batch;
- predecessor work order and completion at the exact paths in Source Verification;
- prepare-failure continuity entry committed at `a31ec4bcd`.

Any conflict stops implementation. This order cannot authorize actual-mode
prepare, principal execution or source creation during the worker phase.

## Agent Roles

| Role | Responsibility |
|---|---|
| Local dispatcher | binds the two-defect repair and exact manifest |
| Local implementation worker | changes coordinator and writes worker return without commit |
| Local reviewer/closer | evaluates returned evidence and runs the independent actual-mode prepare-only probe |
| operator | owns any later principal-execution checkpoint; no credential action in this tranche |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3D-C3-R1-ACTUAL-ACL-SETUP-AND-CLEANUP-CORRECTION","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"SINGLE_ROLE","novelty":"DEFECT_REPAIR"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reviews/","scripts/"],"claims":["actual ACL ordering and exact cleanup correction only"],"requiredProof":["child-before-root ACL order","primary exception preservation","exact cleanup containment","hermetic regression","pending independent Local prepare-only probe"],"operatorCheckpoints":["actual-mode prepare-only reviewer probe","Party B/C execution","Group 4 source creation","T3E wiring"],"forbiddenEffects":["credential access","Party B or Party C execution","real Group 4 source access","worker commit","provider/live/public/deployment","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"CVF_SESSION/state/entries/acelG1T3dC3ActualTokenPrepareOnlyFailure20260923.json","completenessClaimChanged":false}}
```

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one Local same-thread actor for dispatch and implementation |
| role set | dispatcher and implementation worker; never independent reviewer actor |
| delegation depth | zero; no subagent used |
| evidence basis | governed failure receipt, source diff and executable hermetic tests |
| gate sequence | pre-dispatch, pre-implementation, focused tests, worker-return fast, reviewer gate |
| self-review boundary | worker leaves actual-mode probe pending and cannot claim independent acceptance |
| role separation ledger | explicit implementation phase; commit owned only by later closer |
| escalation condition | scope expansion, actual principal, credential, real source or inability to recover exact test root |

## Scope

Allowed scope:

- modify `scripts/acel_g1_group4_actual_token_coordinator.ps1` only;
- create the exact worker return only;
- apply child directory ACLs before root ACL protection;
- add exact-root cleanup access restoration and preserve primary setup errors;
- add hermetic self-tests for ordering and cleanup/error behavior;
- run current-token disposable tests under `%TEMP%`;
- machine-gate remediation inside allowed scope is mandatory worker-owned work.
- create `docs/reviews/CVF_ACEL_G1_G6_TERMINAL_STOP_CLOSURE_2026-09-24.md`
  only when the preregistered no-retry stop condition is reached.
- update `AGENT_HANDOFF_V63_2026-09-18.md`;
- update `CVF_SESSION_MEMORY.md`;
- update `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
- regenerate `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
- update `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`;
- update `CVF_SESSION/state/entries/activeExternalAbsorptionProgram.json`;
- create `CVF_SESSION/state/entries/acelG1G6TerminalStopClosure20260924.json`;
- update `CVF_SESSION/state/entries/nextAllowedMove.json`.

Forbidden scope:

- UAC/elevated actual-mode prepare during worker phase;
- Party B/C process creation, `runas`, password prompt/read/store or account mutation;
- real `governance/sources/issuer_registry/` access or creation;
- changes to principal probe, finalizer, accepted writers or governance checkers;
- G2-G6 work, T3E, provider/live, public-sync, deployment or admission;
- staging or committing worker output.

Risk ceiling: R3 high-risk local ACL transaction repair, hermetic worker phase.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`high-risk-local-transaction-repair`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "high-risk-local-transaction-repair" --role worker --lifecycle-phase implementation --max-results 8 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | retain predecessor controls and add regressions for the observed actual-mode defect |

## Required First Reads

- `AGENTS.md` and active startup surfaces;
- paired baseline and this work order;
- predecessor work order and completion;
- prepare-failure state entry;
- coordinator source;
- applicable checker sources listed below.

## Pre-Flight Checks

- capture `executionBaseHead` and `git status --short`;
- verify only the two manifest paths will change;
- verify real Group 4 source remains absent;
- verify no prior disposable root is selected or deleted;
- run pre-implementation gate before source edits.

## Worker Autonomy / No-Question Rule

Repair every allowed-scope source, self-test, encoding and packet defect
directly. Stop only for a source contradiction, forbidden effect, missing
authority, actual principal requirement or cleanup target ambiguity.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| actual root is protected before its pre-created children | implementation defect | `scripts/acel_g1_group4_actual_token_coordinator.ps1` | `New-ProofPacket`, actual-mode security loop | root is first in the ACL-order array | coordinator setup transaction | ACCEPT |
| directory ACE helper is explicitly non-inheriting | source fact | `scripts/acel_g1_group4_actual_token_coordinator.ps1` | `Add-Ace` | `InheritanceFlags.None` | coordinator security helper | ACCEPT |
| catch cleanup masks the setup failure when recursive delete is denied | implementation defect | `scripts/acel_g1_group4_actual_token_coordinator.ps1` | `New-ProofPacket` catch | direct `Remove-Item` before rethrow | coordinator failure transaction | ACCEPT |
| actual prepare failed before packet materialization and exact root was removed | runtime evidence | `CVF_SESSION/state/entries/acelG1T3dC3ActualTokenPrepareOnlyFailure20260923.json` | complete state value | six-path partial inventory and exact recovery | active continuity source | ACCEPT |
| predecessor acceptance excludes actual ACL proof | review boundary | `docs/reviews/CVF_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_COMPLETION_2026-09-23.md` | claim boundary | TestPolicy-only acceptance | Local completion review | ACCEPT |

## Current Runtime Freshness Verification

At dispatch HEAD `a31ec4bcd`, coordinator SHA-256 remains
`11b449af03b8504682add9cb39c77fe03b9be4b2ac65c9069810358418f3290f`.
The exact failed disposable root is absent. The approved payload evidence is
secret-free and remains outside the repository; worker tests do not consume it.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned baseline/work-order paths | `Test-Path` returned false before authoring | NO_COLLISION |
| batch token | `rg -n` across `docs` and `CVF_SESSION` returned no match before authoring | NO_COLLISION |
| worker paths | coordinator exists; exact worker-return path is absent | REPAIR_EXISTING_OWNER_AND_CREATE_RETURN |
| collision decision | reuse the accepted coordinator owner; create no second runner | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | first-section envelope, source-verification columns, no-question rule, high-risk applicability and exact nine-key JSON, operator checkpoint, exact manifests, trace labels, return contract and closeability graph |
| gateRunPurpose | confirm completed packet admission after source inspection; gate output is not source evidence |
| claimBoundary | static dispatch shape only; no successful repair or runtime proof |

## High-Risk Local Transaction Proof Contract

High-Risk Local Transaction Proof Applicability: REQUIRED

```json
{
  "transactionTarget": "disposable Group 4 actual-mode ACL setup, failure cleanup and primary-error preservation",
  "productionPathPeer": {"kind": "REAL_SECOND_PROCESS", "invocationPath": "scripts/acel_g1_group4_actual_token_principal_probe.ps1", "mutationPath": "role-bound disposable reservation transaction and negative operation matrix"},
  "deterministicBarrierProtocol": {"events": ["READY", "START_ATTEMPT", "ATTEMPTING", "PARENT_RELEASE", "ENTERED", "COMPLETE"], "timeoutRole": "DEADLOCK_SAFETY_ONLY"},
  "enteredBeforeReleaseOracle": "REJECT_ENTRY_BEFORE_PARENT_RELEASE",
  "postAcquireFailureInjection": {"point": "AFTER_ACQUIRE_BEFORE_MUTATION", "cleanupProof": "SUBSEQUENT_PEER_ACQUIRES"},
  "semanticSecurityTuple": {"fields": ["ownerSid", "protectionState", "inheritanceState", "aces"], "aceFields": ["sid", "rights", "accessType", "isInherited", "inheritanceFlags", "propagationFlags"], "normalization": "SORT_COMPLETE_ACE_TUPLES"},
  "rollbackExactness": {"comparison": "SEMANTIC_PRESTATE_EQUALS_POST_ROLLBACK", "adversaries": ["EXTRA_ALLOW", "DENY", "INHERITED", "WRONG_OWNER"]},
  "finalEvidenceHashBinding": {"algorithm": "SHA256", "scope": "EXACT_RETURN_BYTES", "capture": "BEFORE_AND_AFTER_FINAL_REQUIRED_GATE", "equality": "REQUIRED", "postGateMutation": "FORBIDDEN"},
  "independentProbeRequired": {"required": true, "owner": "LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER", "workerReturnDisposition": "PENDING_REVIEWER_EXECUTION"}
}
```

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T3D-C3-R1-ACTUAL-ACL-SETUP-AND-CLEANUP-CORRECTION
reviewRoundCount: 1
priorFindingSetDigest: 6cb7547879201819361278efbb5c52910151f8b859a3bdbb3d94a3ebeb4aac99
dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS
newIndependentCriticalEvidence: true
regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: ONE_CONSOLIDATED_REWORK
rootCauseClusterId: ACEL-G1-T3D-C3-R1-ACL-ORDERING
reworkGeneration: 1
consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3d-c3-actual-token-disposable-runner","chainMode":"SUCCESSOR","chainOrdinal":1,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_2026-09-23.md","sha256":"6dc845e66df98b645f6116fafc1a07e8930429b45ddefc5193f99fd7280bbc4d"},"blockerDelta":{"prior":["ACTUAL_TOKEN_ENTRYPOINT_MISSING","ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN"],"resolved":["ACTUAL_TOKEN_ENTRYPOINT_MISSING"],"retained":["ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN"],"new":[],"reopened":[],"current":["ACTUAL_TOKEN_PROOF_PENDING","GROUP4_SOURCE_NOT_CREATED","T3E_NOT_OPEN"]},"resolutionEvidence":{"ACTUAL_TOKEN_ENTRYPOINT_MISSING":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_COMPLETION_2026-09-23.md","sha256":"13a1db3d979202fe20ca86cf6c43055b288208e3f9cd9d1fcd4d7997a95873ea","locator":"Reviewer verdict: `TOOLING_ACCEPTED_SOURCE_NOT_CREATED`."}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":1,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON

Reason: internal Local implementation; no external invocation is admitted.

## Gate-To-Role Closeability Contract

| Gate | Phase | Owner | Evidence | Next gate |
|---|---|---|---|---|
| pre_dispatch | PRE_DISPATCH | dispatcher | paired packet and clean base | pre_implementation |
| pre_implementation | IMPLEMENTATION | worker | committed dispatch HEAD and exact manifest | focused_tests |
| focused_tests | IMPLEMENTATION | worker | three selftests plus 22-row TestPolicy packet | worker_return_fast |
| worker_return_fast | RETURN | worker | exact worker return | independent_local_probe |
| independent_local_probe | REVIEW | reviewer | one fresh actual-mode prepare-only probe | reviewer_fast |
| reviewer_fast | REVIEW | reviewer | exact returned range | pre_commit |
| pre_commit | REVIEW | closer | accepted material | material_commit |
| material_commit | MATERIAL_COMMIT | closer | exact accepted paths | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | same Local thread dispatches and implements; independent actor review is not claimed |
| phase | dispatch then implementation then pending review |
| baseHeadFor(phase) | dispatchBaseHead=`a31ec4bcd`; executionBaseHead=worker capture; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exact two-path worker manifest plus paired dispatch artifacts |
| traceScope(phase, actor) | one trace per governed artifact with explicit role phase |
| commitOwner(phase) | worker forbidden; Local closer only after review |
| crossBatchIsolation | clean worktree required; no parked or unrelated paths |
| nextMoveSurfaces | worker return, Local review, then separate continuity |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: Local implementation role after committed dispatch

laneOwnedPaths: exact two paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact manifest and empty staged set

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | operator request accepts one final bounded G1 tranche |
| scope classification | bounded two-path source/return change with exact changed paths |
| risk sensitivity | high-risk local ACL setup; provider/live, secret, public-sync and production forbidden |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` for dispatch and implementation, followed by distinct reviewer phase |
| role separation basis | worker cannot claim independent reviewer probe or commit |
| escalation condition | stop on forbidden scope, ambiguous cleanup target, actual principal need or second failed prepare-only attempt |

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: reviewer uses the approved payload and a fresh exact absent
root, runs elevated `-PrepareProof`, verifies manifest, 22 envelopes, command
packet, ACL reachability and zero principal launches, then performs exact
cleanup without wildcard use.

negativeMutationClasses: root-first ACL order, inaccessible child, missing
envelope, unexpected residue, payload hash drift, real-source overlap and
cleanup that replaces the primary exception.

expectedInformationGain: prove the correction works under actual Windows ACLs
that TestPolicy cannot model.

rerunCostReason: one fresh prepare-only fixture is proportionate and is the
operator-approved final G1 repair attempt.

reviewerDecisionOwner: LOCAL

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/acel_g1_group4_actual_token_coordinator.ps1` | repair ACL order, exact cleanup and hermetic regressions |
| `docs/reviews/CVF_ACEL_G1_T3D_C3_R1_ACTUAL_ACL_SETUP_AND_CLEANUP_CORRECTION_WORKER_RETURN_2026-09-24.md` | create terminal worker return with exact evidence |
| `docs/reviews/CVF_ACEL_G1_G6_TERMINAL_STOP_CLOSURE_2026-09-24.md` | Local reviewer records terminal stop only after the final actual-mode attempt fails closed |

## Work-Order Fulfillment Manifest

| Obligation | Owning artifact | Terminal evidence |
|---|---|---|
| ACL ordering and cleanup implementation | coordinator | focused selftests and source diff |
| worker evidence and no-commit boundary | worker return | worker-return fast gate |
| actual-mode proof | reviewer later | pending independent probe |

## Forbidden Path Manifest

- `scripts/acel_g1_group4_actual_token_principal_probe.ps1`;
- `scripts/acel_g1_group4_actual_token_local_finalizer.ps1`;
- all `governance/sources/` paths;
- all account, credential, provider, public and deployment surfaces;
- all G2-G6 artifacts.

## Forbidden Filesystem State At Dispatch

No selected disposable proof root may exist. Historical temporary inputs and
the secret-free diagnostic bundle are outside worker mutation scope.

## Pre-Existing Dirty Path Exemptions

None. Dispatch requires a clean worktree.

## Foundation Storage Layout Block

No new foundation storage is created. The worker return stays under
`docs/reviews/`; test roots are direct `%TEMP%` children and must be removed.

## Required Proof Manifest

| Proof | Worker status |
|---|---|
| child-before-root ACL order | required hermetic assertion |
| setup primary exception survives successful cleanup | required hermetic assertion |
| cleanup remains exact-root bounded | required hermetic assertion |
| predecessor selftests remain green | required |
| actual-mode prepare-only | pending reviewer execution |

## Write Ownership

Worker owns only the two required artifact paths and must not commit. Reviewer
owns probe evidence, any completion review and material commit.

## Execution Plan

1. capture clean execution base and run pre-implementation gate;
2. refactor actual directory security order into a testable helper;
3. add exact cleanup-access restoration inside the validated root;
4. preserve primary failure, adding cleanup failure only as secondary detail;
5. add hermetic self-tests for both defects;
6. run coordinator, probe and finalizer selftests plus fresh TestPolicy packet;
7. author return, run worker-return fast gate and stop pending review.

## Epistemic Process Block

- Expected Result / Prediction: child-first explicit ACLs should keep setup
  reachable until the root is protected; exact cleanup access should remove a
  partial root without replacing the originating failure.
- Evidence Comparison: actual prepare evidence showed root readable but every
  pre-created child inaccessible, matching the source ordering and no-inherit
  flags; catch output exposed only cleanup denial.
- Contradiction or Gap Disposition: predecessor TestPolicy acceptance did not
  exercise actual DACL inheritance, so the real failure reopens only this
  coordinator boundary, not the principal probe/finalizer acceptance.
- Claim Update: repair evidence remains pending until worker tests and the
  separate reviewer actual-mode prepare-only probe pass.

## Evidence Requirements

- exact pre/post script SHA-256;
- execution base and actual changed set;
- named selftest counts and fresh root identifiers;
- no real-source existence change;
- no Party B/C or credential action;
- worker return exact-byte hash before and after final worker gate.

## Verification Commands

```powershell
pwsh -NoProfile -NonInteractive -File scripts/acel_g1_group4_actual_token_coordinator.ps1 -SelfTest
pwsh -NoProfile -NonInteractive -File scripts/acel_g1_group4_actual_token_principal_probe.ps1 -SelfTest
pwsh -NoProfile -NonInteractive -File scripts/acel_g1_group4_actual_token_local_finalizer.ps1 -SelfTest
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Acceptance Criteria

- exact two-path worker delta;
- ordering and error-preservation regressions pass;
- all predecessor hermetic tests remain green;
- TestPolicy packet remains 22/22, no principal process, no actual proof claim;
- all test roots removed exactly;
- return says `COMPLETE_PENDING_REVIEW` and actual-mode probe remains pending.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3D_C3_R1_ACTUAL_ACL_SETUP_AND_CLEANUP_CORRECTION_WORKER_RETURN_2026-09-24.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead
Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control
Block; Public Export Disposition; executionBaseHead; git status --short;
Changed Files; No-Commit Statement.

Conditional sections use `N/A with reason` when inapplicable.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | optional; reviewer may record evidence in the worker return |
| reviewerOwnedClosurePaths | actual-mode probe receipt, optional completion review, exact material paths |
| closureOwner | Local reviewer/closer distinct from worker phase |
| workerCommitPermission | FORBIDDEN |

## Review Gate

Reviewer consumes returned evidence, runs exactly one fresh actual-mode
prepare-only probe, inspects the complete packet and cleanup, then either
accepts, records only reviewer-owned evidence or stops G1. No broad duplicate
execution and no principal launch.

## Operator Checkpoint

The current tranche and one reviewer prepare-only proof are already authorized.
Party B/C execution remains separately unopened. A second implementation round
or another prepare attempt requires new direction.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | coordinator source change and hermetic evidence only |
| claimDisposition | CLAIM_REJECTED: worker evidence cannot establish actual ACL success or principal behavior |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: actual-mode reviewer receipt does not exist in worker phase |
| actionEvidence | ACTION_EVIDENCE_PRESENT: current-token disposable tests only |
| invocationBoundary | no UAC, Party B/C, password, provider or network invocation |
| interceptionBoundary | no production interception or mandatory runtime wrapper is created |
| claimLanguage | bounded source change pending independent actual-mode proof |
| forbiddenExpansion | G2-G6, source/T3E, provider/live/public/deployment and principal execution |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `CVF_SESSION/state/entries/acelG1T3dC3ActualTokenPrepareOnlyFailure20260923.json` |
| Chain map route | active continuity to Local repair and later Local proof |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and predecessor coordinator |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source admitted |
| Claim boundary | external absence is not used as private proof |

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: bounded Local implementation; decision owner:
Local reviewer. External research is closed and supplies no private authority.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | ACEL G1 T3D-C3 R1 repair dispatch, 2026-09-24 |
| Working directory | repository root |
| Command or tool surface | governed reads, source inspection, scaffold preview, apply_patch, pre-dispatch gates and Git |
| Target paths | paired baseline and work order |
| Allowed scope source | operator authorization of one bounded final G1 repair; G2-G6 parked |
| Before status evidence | clean worktree at HEAD `a31ec4bcd`; actual prepare failed closed; exact partial root absent |
| After status evidence | bounded two-path worker packet ready; no implementation yet |
| Diff evidence | exact paired dispatch paths |
| Approval boundary | dispatch only; no worker source mutation in this phase |
| Claim boundary | no repair success, actual-mode proof, principal, source, T3E or external effect |
| Agent type | Local dispatcher |
| Invocation ID | `acel-g1-t3d-c3-r1-actual-acl-setup-cleanup-dispatch-20260924` |
| Expected manifest | paired baseline and work order |
| Actual changed set | verified before dispatch commit |
| Manifest delta | MATCH |

## Acceptance Receipt Assertion Matrix

| Assertion | Required | Dispatch value | Status |
|---|---|---|---|
| exact defect set | ACL ordering plus cleanup/error preservation only | bound | PASS |
| worker manifest | coordinator plus return | exact | PASS |
| actual-mode action | forbidden in worker phase | none | PASS |
| independent proof | reviewer-owned | pending | PASS |
| successor | no automatic successor | closed | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `CLOSED_STOPPED_FAIL_CLOSED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ACEL_G1_G6_TERMINAL_STOP_CLOSURE_2026-09-24.md` | terminal fail-closed decision and G1-G6 disposition | PASS |
| Roadmap state | N/A with reason: this bounded correction has no separate roadmap | terminal work-order disposition | PASS |
| Registry JSON | N/A with reason: no registry source was created or changed | real source absent | PASS |
| Registry Markdown | N/A with reason: no registry catalog was created or changed | real source absent | PASS |
| External evidence digest | terminal review local receipt ledger | prepare error SHA-256 `b9d2e86bed1da81dc30fd13898763fc5f27c8372f87ad891c2f490496eb490ba`; cleanup SHA-256 `2c8a42366f7dabafb0d7fe7d0e6177743032b1c26a116d1a9266ce08efc7e18e` | PASS |
| System loop interlock | terminal review G1-G6 disposition table | no automatic successor | PASS |
| Session continuity | active handoff and generated state | terminal stop projection in the same closure batch | PASS |

## Closure Checklist

- worker leaves changes uncommitted;
- actual-mode probe stays pending in worker return;
- reviewer must verify exact cleanup and zero principal launches;
- any second failure stops G1 and returns to operator;
- G2-G6 remain parked.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any forbidden-path need, scope contradiction,
test-root cleanup ambiguity or source-state change. Otherwise return
`COMPLETE_PENDING_REVIEW` after the full worker gate.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private machine-specific ACL repair; no public artifact authorized.

## Claim Boundary

This work order authorizes only the Local two-path repair implementation and
hermetic worker evidence. It does not authorize or prove actual-mode setup,
Party B/C execution, source creation, T3E, runtime, provider, public or
production readiness.
