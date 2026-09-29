# CVF Agent Work Order - NCR Q001 Local Transaction Store

Memory class: governed-worker-dispatch

docType: work_order

Status: HOLD_PRE_DISPATCH

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-Q001-LOCAL-TRANSACTION-STORE

Dispatch base head: `b93d372bf89e0135f3df3bfa790df335d852627c`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` implementation role

Reviewer/closer: distinct Local reviewer/closer phase

Worker return path: `docs/reviews/CVF_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_WORKER_RETURN_2026-09-29.md`

## Dispatch Prompt Envelope

Role: internal worker for the bounded Q001 local transaction-store repair. Canonical packet: this work order and paired `docs/baselines/CVF_GC018_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_2026-09-29.md`. Commit mode: `WORKER_MUST_NOT_COMMIT`. Capture `executionBaseHead` at start. Read current startup and source owners before any edit. This packet is `HOLD_PRE_DISPATCH`: do not start implementation until dispatcher completes admission, commits the packet, and synchronizes current authority. Return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`; the independent Local probe stays pending in the worker return.

High-Risk Local Transaction Proof Applicability: REQUIRED

## Purpose

Replace the Q001 single-host JSON whole-file rewrite failure boundary with a transactional local store while preserving the existing ledger consumer shape and `DRAFT_UNACCEPTED` artifact boundary.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator direction | continued bounded Q001 work, 2026-09-29 | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`, D028/Q001 | ACCEPT |
| Failure profile | `docs/reference/CVF_NCR_Q001_LEDGER_DURABILITY_FAILURE_PROFILE_2026-09-29.md`, material commit `1722db834` | ACCEPT |
| Paired GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_2026-09-29.md` | HOLD until committed dispatch |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| JSON append truncates source before dump; only process-local lock | defect owner | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/immutable_ledger.py` | `append_event` | `_ledger_lock`, `open(..., "w")` | `ImmutableLedger` | ACCEPT |
| block hash covers timestamp, predecessor and event | compatibility owner | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/block_builder.py` | `build_block` | `BlockBuilder.build_block` | block schema | ACCEPT |
| hash uses sorted-key JSON SHA-256 | compatibility owner | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/hash_engine.py` | `generate_hash` | `HashEngine.generate_hash` | hash schema | ACCEPT |
| API reads JSON file directly | consumer owner | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/server.py` | `/api/v1/ledger` | `ledger()` | engine API | ACCEPT |
| orchestrator appends before receipt construction | consumer owner | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core_orchestrator.py` | lines 208-233 | `append_event`, `ledger_attached` | evaluation flow | ACCEPT |
| existing ledger tests do not exercise process/fault restore | test owner | `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/test_ledger.py` | `TestImmutableLedger` | `test_chain_grows` and adjacent tests | engine tests | ACCEPT |

## Agent Roles And Scope

The worker owns bounded source/tests and a pending return. A distinct Local reviewer probes the result, decides acceptance, and commits. The session-sync steward updates current authority after a material decision. External Web remains advisory; the source and private-CVF decision owner is Local.

## Allowed / Forbidden Scope

Allowed only after dispatch release: the bounded local store, source-compatible consumers, synthetic fault/peer/restore tests and pending worker return defined here. Forbidden scope is the live ledger, secrets, upstream side-effect semantics, deployment, public sync, provider calls and all parked checkpoints.

## Required First Reads

Read `AGENTS.md`, bootstrap/front door/active handoff, paired baseline and this order, guard orientation/literal gotchas, high-risk proof standard, fault profile, the six source owners in Source Verification, and applicable checkers before editing.

## Pre-Flight Checks

Capture `git rev-parse HEAD` and `git status --short`. Verify clean committed packet and current-authority binding; run dispatch-release readiness and bound pre-implementation autorun gate. A HOLD packet fails this check by design and must not be executed.

## Write Ownership

Worker paths must be exact before release. Worker owns no baseline, roadmap, work order, session state, handoff, guard or commit. Reviewer/closer owns correction of this packet and final disposition.

## Execution Plan

After release: establish synthetic failing-before regression; implement local transaction store, validated import and read path; run real peer/fault/restore tests; return evidence without commit; Local reviewer runs independent probe and decides material commit.

## Evidence Requirements

Record source hash, changed paths, barrier events, fault point, pre/post state, duplicate-ID outcomes, import rejection, restored count/tip/IDs, commands/results, final return hash receipt and open boundaries. No credential or live-ledger content is needed.

## Acceptance Criteria

All six baseline invariants require executable synthetic evidence, independent Local probe and required gates. Static contract admission or a self-reported test alone cannot close this order.

## Review Gate

Worker returns `COMPLETE_PENDING_REVIEW` only with a closeable packet and `PENDING_REVIEWER_EXECUTION`. Local reviewer evaluates evidence and runs a distinct adversarial probe before commit.

## Closure Checklist

After reviewer acceptance, capture material diff, run pre-commit, commit accepted material, separately update continuity and run split-range pre-closure. Keep Q001/R0 open until its independent gates are met.

## Return-To-Orchestrator Conditions

Return pending review for passing bounded checks; otherwise `BLOCKED_WITH_REASON` identifying a source, platform, manifest or proof obstacle. Never turn timeout into positive exclusion evidence.

## Operator Checkpoint

Only a changed business scope, live effect, real-ledger cutover, hosted/multi-host selection, retention/RPO/RTO commitment, credential or public/deployment effect returns to the operator. Routine in-scope choices do not.

Allowed implementation is a Python standard-library SQLite backend for **one local host**, behind the existing ledger interface; explicit JSON-to-new-DB migration from a verified immutable input; exact-ID lookup; coherent `/api/v1/ledger` read path; focused tests, real peer process, fault injection and clean restore drill. Candidate paths and any new helper/test file must be fixed in an exact manifest before release. Do not edit the current runtime ledger or change engine configuration during implementation.

Forbidden: multi-host or hosted selection, silent migration/cutover, changes to OAuth or Web route, automatic HTTP retry, duplicate upstream side-effect claim, raw secrets, live provider calls, artifact acceptance, pilot effect, P11, external runtime, deployment, public sync, staging or worker commit.

## Implementation Contract

Use the SQLite transaction as the serialization and rollback boundary: tip read, duplicate-ID classification, block build and insert share one write transaction. Persist and version block order, complete JSON block bytes, request ID and hash; verify the full chain on import and restore. Treat database busy, integrity, schema or commit errors as fail-closed. A same-ID/same-event append may return the committed existing block; same-ID/different-event must reject without mutation. Keep `ledger_attached` and HTTP receipt absent when commit is not confirmed. Source/read-path compatibility tests must exercise the API's limited tail and original block schema.

The current orchestrator performs registry/routing/approval work before ledger append; this order does not certify those earlier operations as exactly-once. The migration must operate on a copied, quiescent, fully validated synthetic JSON source; reject corruption, duplicate IDs, wrong schema and nonempty target without overwriting either. Record a deterministic source digest and resulting DB tip. The engine must not silently switch the currently configured `.json` path to a new DB.

## High-Risk Local Transaction Proof Contract

```json
{
  "transactionTarget": "Q001 local SQLite ledger append, validated JSON import, consistent backup and clean restore",
  "productionPathPeer": {
    "kind": "REAL_SECOND_PROCESS",
    "invocationPath": "EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/q001_sqlite_ledger_peer.py",
    "mutationPath": "EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/immutable_ledger.py#ImmutableLedger.append_event"
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

The fixed security tuple is the required admission schema. No ownership/DACL mutation is authorized; the worker must not invent an ACL rollback claim. Capture the storage file's security state before/after the local drill, disclose any platform observation limit, and stop for contract amendment if a mandatory tuple cannot be represented. Transaction rollback must additionally compare exact block/ID/tip state. Do not report schema admission as execution evidence.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-Q001-LOCAL-TRANSACTION-STORE
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-q001-local-transaction-store","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Independent Review Probe Admission Contract

independentProbeRequired: YES
independentProbeRiskClass: HIGH
independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER
implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH
positiveControl: reviewer opens a clean synthetic DB and independently checks production append/read/restore against block hashes
negativeMutationClasses: pre-release peer entry; lost second append; partial pre-commit block; duplicate/conflicting request ID; corrupt migration accepted; inconsistent restored tip
expectedInformationGain: distinguish a real transaction boundary from worker fixtures that merely mirror implementation
rerunCostReason: one compact independent peer/fault/restore probe decides the safety claim without recreating the worker suite
reviewerDecisionOwner: LOCAL

## Acceptance And Independent Probe

Worker tests must inject failure before commit and after acquisition, compare prior complete state, prove a later peer can append, observe an explicit second process attempting while the parent owns the transaction, reject any pre-release ENTERED event, then observe post-release ENTERED and COMPLETE. A timeout is a deadlock guard only. Test duplicate-same/conflicting ID, crash/response ambiguity by exact-ID lookup, corrupt import, uninterrupted source bytes, consistent online backup, clean-instance restore, count/tip/hash/request-ID reconciliation, and API tail compatibility. Use synthetic content under a verified disposable workspace path. Local reviewer executes a distinct probe with independent assertions after worker return; worker records `PENDING_REVIEWER_EXECUTION`.

The return names the final required gate and detached receipt location. Hash exact return bytes before and after that gate, require equal SHA-256 and no post-gate mutation. Any correction repeats capture/gate/capture. No power-loss, storage-device durability, off-machine encryption, RPO/RTO, hosted or production claim follows from the local tests.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order outcome | Status |
|---|---|---|
| D028 write failure and empty reader window | transactional append and complete snapshot reads with fault proof | PLANNED |
| Q001 exact receipt reconciliation | unique request ID plus exact lookup, without automatic retry | PLANNED |
| Q001 backup/restore gap | local consistent backup and clean restore drill | PLANNED_BOUNDED |
| Q004 hosted and RPO/RTO choice | preserve as separate operator/profile gate | PARKED |

## Pre-Dispatch Hold And Next Action

This order intentionally remains `HOLD_PRE_DISPATCH`. Dispatcher must inspect the high-risk security-tuple applicability for this DB-only task, finalize exact new-file manifest and gate-to-role graph, run author/pre-dispatch gates, commit the paired packet, then sync its material SHA to active continuity before worker edits. A static high-risk contract check may pass before these steps; that does not release execution. The Local reviewer owns the final technical disposition.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`. Returned defects: none; `totalCandidates=0`, `truncated=false`. No defect item confers execution authority.

Returned defects: NONE_RETURNED

## Foundation Storage Layout Block

N/A with reason: this tranche does not create, split or relocate a durable governance foundation owner. The word foundation occurs only in source/control naming. The proposed SQLite file is a runtime data store under an existing engine owner, and it is not created by this HOLD packet.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_COMPLETION_2026-09-29.md` only if separate closure evidence is required |
| reviewerOwnedClosurePaths | accepted worker paths, reviewer probe/disposition, roadmap and continuity as separately authorized |
| closureOwner | Local reviewer/closer distinct from worker phase |
| workerCommitPermission | FORBIDDEN |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one internal implementation worker followed by distinct Local reviewer/closer |
| phase | Q001 transaction-store design packet HOLD before worker release |
| baseHeadFor(phase) | dispatchBaseHead=`b93d372bf89e0135f3df3bfa790df335d852627c`; executionBaseHead=worker capture only after release; closureBaseHead=reviewer capture |
| changedSetScope(phase) | paired HOLD packet and roadmap D029 only; worker manifest must be finalized before release |
| traceScope(phase, actor) | worker later records process barriers, fault/restore results and exact changed set |
| commitOwner(phase) | Local closer only; worker commit forbidden |
| crossBatchIsolation | P11, live ledger, external runtime, public and deployment stay parked |
| nextMoveSurfaces | dispatcher admission, committed packet, then separate continuity release |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF workspace |
| Session or invocation | Q001 local transaction-store packet, 2026-09-29 |
| Working directory | repository root |
| Command or tool surface | governed source reads, Git and static guard commands |
| Target paths | paired baseline, this work order and NCR roadmap D029 |
| Allowed scope source | operator continuation, D028/Q001 and committed Local fault profile |
| Before status evidence | clean HEAD `b93d372bf` |
| After status evidence | three pending governed-document paths, implementation not started |
| Diff evidence | `git status --short` and `git diff --check` before commit |
| Approval boundary | no real-ledger cutover, pilot, provider/live, public or deployment effect |
| Claim boundary | HOLD design and source verification only |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-q001-local-transaction-store-20260929 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_2026-09-29.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_2026-09-29.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `AGENT_HANDOFF_V63_2026-09-18.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_2026-09-29.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_Q001_LOCAL_TRANSACTION_STORE_2026-09-29.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `AGENT_HANDOFF_V63_2026-09-18.md` |
| Manifest delta | MATCH in worktree; handoff is excluded from material stage and remains for separate continuity sync |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py` |
| literalTokensReviewed | `REQUIRED`, nine-key JSON contract, `REAL_SECOND_PROCESS`, ordered barriers, exact return hash, distinct Local probe, `HOLD_PRE_DISPATCH` |
| gateRunPurpose | Confirmation of authored contract evidence, not first discovery of gate shape; not target-runtime proof. |
| claimBoundary | Design/hold packet only. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Q001 design packet; public export has separate authority.

## Claim Boundary

No implementation, migration, live ledger change, recovery measurement, provider-governance proof, or Q001/R0 acceptance is claimed.
