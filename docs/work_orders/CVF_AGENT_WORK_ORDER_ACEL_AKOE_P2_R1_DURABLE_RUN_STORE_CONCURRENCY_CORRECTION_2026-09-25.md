# CVF Agent Work Order - ACEL AKOE-P2-R1 Durable Run Store Concurrency Correction

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: ACEL-AKOE-P2-R1

Dispatch base head: `fee4316f1affdcf2675c4e9832d96ebc7b917402`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` runtime-correction role

Reviewer/closer: Local reviewer/closer distinct from the worker phase

Worker return path: `docs/reviews/CVF_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_WORKER_RETURN_2026-09-25.md`

## Dispatch Prompt Envelope

Role: internal worker for bounded AKOE-P2-R1 durable run-store concurrency
correction.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_2026-09-25.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_2026-09-25.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker captures the committed dispatch-continuity HEAD
before edits.

Current-time notes: authored 2026-09-25 from clean material base `fee4316f1`,
which commits the truthful blocked P2 return and ADIF-0059 gate hardening.

Do-not-misread notes: fix exactly one confirmed lost-update defect. Do not
change delegation-lock semantics, add dependencies, create another runtime
owner, open P3/P4, invoke provider/live/network surfaces, or commit.

Required first actions: read startup/bootstrap/front door/active handoff,
guard orientation, literal gotchas, paired baseline, this work order, blocked
P2 return, exact source/test owners, high-risk transaction standard, and named
checker sources before editing.

Return contract: create the exact worker return from the governed scaffold,
implement and test the bounded repair, capture the detached final return hash
receipt, run required gates, leave all changes uncommitted, and return only
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Repair `MaoFileRunStore.appendEvent` so the complete per-run
load/replay/append/write sequence has one cross-instance and cross-process
writer, and replace the P2 bug-preserving probe with deterministic
fail-closed/durable-winner evidence.

## Authority Chain

1. Operator confirmation on 2026-09-25 authorizing P2-R1 runtime correction
   and machine-gate hardening.
2. `docs/roadmaps/CVF_ACEL_APPLIED_KNOWLEDGE_OWNER_ENRICHMENT_ROADMAP_2026-09-25.md`.
3. P2 blocked return, SHA-256
   `a44fe1cf35db9b4b65a5b4439432665a80fa814a50b204ef82f96214bc6762d1`.
4. Material evidence and guard-hardening commit `fee4316f1`.
5. Paired P2-R1 GC-018 baseline and this exact work order.

If these sources conflict, stop. The worker cannot expand authority.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| P2 blocker evidence | blocked return above, committed at `fee4316f1` | exact blocker is `run_store_concurrent_write_lost_race` | SATISFIED |
| Operator scope decision | explicit 2026-09-25 confirmation | exact runtime owner and evidence paths only | SATISFIED |
| Paired GC-018 | same dispatch batch | material commit required before worker release | SATISFIED_FOR_DISPATCH |
| Dispatch continuity | no P2-R1 marker exists before material commit | session-sync steward records real material SHA and current authority before implementation | REQUIRED_BEFORE_IMPLEMENTATION |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | owns any new authority, dependency, external effect, or P3/P4 checkpoint |
| Local dispatcher | owns packet correctness, commits, continuity, and release |
| Internal worker | owns exact source/test repair, evidence, and uncommitted return |
| Local reviewer/closer | consumes returned evidence, runs independent probe, repairs only authorized closure defects, accepts or blocks, and commits |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | committed Local defect evidence from P2; no new external intake |
| scope classification | named-file stateful local correction with real second-process proof |
| risk sensitivity | durable file mutation and cross-process locking; Git-reversible source changes; no external effect |
| selected role route | `SINGLE_AGENT_SINGLE_ROLE` worker followed by distinct Local review/closure |
| role separation basis | worker cannot execute the independent reviewer probe, accept, stage, commit, or synchronize its own result |
| escalation condition | source contradiction, forbidden-path need, new dependency/owner, non-local effect, or claim expansion |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-AKOE-P2-R1","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"STATEFUL_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reviews/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/"],"claims":["bounded durable run-store concurrency correction","deterministic fail-closed durable-winner proof"],"requiredProof":["failing-before passing-after defect regression","real second-process lock proof","post-acquire cleanup proof","stale-lock fail-closed proof","focused and package tests","exact changed set","worker-return full gate","detached final-return hash equality"],"operatorCheckpoints":["new runtime owner or package dependency","path outside manifest","P3 or P4","provider live public deployment action"],"forbiddenEffects":["worker commit","network or provider invocation","new runtime engine","delegation-lock semantic change","public write","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md","completenessClaimChanged":false}}
```

## Allowed Scope

Implementation outcome:

- derive a deterministic per-run lock path from the canonical snapshot path;
- reuse `acquireLock` and `releaseLock` from the existing delegation
  persistence helper;
- hold ownership from before `loadAndReplay` until after atomic persistence or
  any fail-closed return;
- map lock contention/staleness to explicit durable-run-store failure reasons
  without performing an unguarded write;
- use `try/finally` or equivalent exception-safe ownership release;
- keep different run identities independently writable;
- replace the P2 defect-preserving launcher test with a desired-state
  assertion: exactly one conflicting terminal attempt succeeds, the loser
  fails closed, and durable replay contains exactly the successful winner;
- add focused production-path tests for cross-process exclusion, stale-lock
  rejection, failure cleanup, and no residue.

Implementation choice remains with the worker inside these evidence outcomes.
Do not duplicate the lock algorithm or change sibling semantics when reuse is
sufficient.

## Forbidden Scope

- any file outside the Maximum Worker Path Manifest;
- changes to `durable.delegation.ledger.persistence.ts` or
  `durable.delegation.ledger.store.ts`;
- package manifests, dependency installation, exports/barrels, launcher
  production source, MAO contracts, governance checkers, packet files,
  roadmaps, session state, or active handoff;
- automatic stale-lock takeover/deletion, lease renewal, distributed locking,
  multi-host claims, or production-readiness claims;
- provider/model/network/live/public/deployment/production action;
- staging, committing, pushing, or stashing.

## Required First Reads

| Path | Action | Purpose |
|---|---|---|
| `AGENTS.md`; bootstrap; `CVF_SESSION_MEMORY.md`; active handoff | FULL_READ | current authority and next move |
| guard orientation; literal gotchas; high-risk transaction standard | FULL_READ | role, packet, and proof rules |
| paired P2-R1 baseline and this work order | FULL_READ | exact authority and manifest |
| P2 blocked worker return and ADIF-0059 | FULL_READ | defect evidence and terminal-status rule |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | FULL_READ | production defect owner |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts` | FULL_READ | focused test owner |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts` | FULL_READ | defect-probe owner |
| delegation persistence/store lock implementation and lock tests | FULL_READ | reuse semantics and adversaries |
| checker sources named below | FULL_READ | return and gate shape before authoring |

## Pre-Flight Checks

Before any worker-owned edit:

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
git log -1 --format=%H -- docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_2026-09-25.md
rg -n "material-SHA marker|ACEL-AKOE-P2-R1" AGENT_HANDOFF_V63_2026-09-18.md
python governance/compat/check_dispatch_release_readiness.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_2026-09-25.md --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_2026-09-25.md
```

Expected: clean committed base; committed paired packet; later committed
handoff material-SHA marker; dispatch-release PASS; bound pre-implementation
PASS. Otherwise return `BLOCKED_WITH_REASON` before edits.

## Worker Autonomy / No-Question Rule

Repair routine in-manifest source, test, encoding, and worker-return gate
defects directly. Do not ask implementation-style questions. Stop only for a
real source contradiction, forbidden-path requirement, new dependency/owner,
external effect, risk expansion, or missing dispatch continuity.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| unguarded run-store append spans replay through atomic replace | defect owner | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 186-215 | `appendEvent(` | durable run store | ACCEPT |
| local atomic writer alone does not prevent lost update | defect mechanism | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 443-466 | `atomicWriteJson` | durable run store | ACCEPT |
| existing lock primitive is cross-process exclusive-create and stale fail-closed | reusable owner | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.delegation.ledger.persistence.ts` | lines 104-174 | `acquireLock`; `releaseLock` | delegation persistence | ACCEPT |
| sibling transaction holds the same primitive across read/mutate/write | precedent | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.delegation.ledger.store.ts` | `withCas`, lines 688-742 | `withCas` | delegation ledger store | ACCEPT |
| P2 defect probe asserts known broken behavior | test correction target | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts` | test at line 470 | cancel/completion race defect probe | launcher tests | ACCEPT |
| focused run-store tests exist | test owner | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts` | `describe("MaoFileRunStore")` | run-store tests | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

P2 evidence identifies the defect but does not prove the correction. The
worker reruns the original probe, records failing-before behavior against the
desired assertion, verifies current source hashes, and produces fresh tests.
New text is UTF-8 and ASCII unless an explicit encoding exception is required.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | committed Local P2 evidence -> exact current-owner correction -> independent Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py` |
| Owner surface | existing durable run store and its tests |
| Disposition | comparison-only predecessor evidence; no absorption or external research |
| Claim boundary | Local evidence controls; no external source authority or public claim |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: bounded P2-R1 correction.
Decision owner: Local. External research is closed.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md"}
```

## Foundation Storage Layout Block

- N/A with reason: the word foundation appears only in the existing package
  name; this work order creates no durable governance reference, folder,
  front door, index, template, addendum, standard, or storage-layout owner.
- The only new source-side artifact is an executable Vitest peer under the
  existing package test folder; no governance foundation registration applies.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap/P2 requirement | P2-R1 handling | Verdict |
|---|---|---|
| cancel/completion race has one deterministic durable outcome | serialize same-run append transaction and assert one durable terminal winner | PASS |
| durable ledger remains execution truth | correct the existing run-store owner; do not add a projection or second truth owner | PASS |
| implementation follows deterministic negative evidence | committed P2 defect probe plus desired-state failing-before assertion | PASS |
| no new runtime engine | reuse existing store and lock helper under exact manifest | PASS |
| P3/P4 remain gated | explicitly forbidden and absent from acceptance/next move | PASS |
| independent Local review | worker leaves probe pending and cannot commit or accept | PASS |

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Worker action | Purpose |
|---|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | Yes | modify | production lock ownership and failure mapping |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts` | Yes | modify | focused concurrency, stale lock, cleanup, unrelated-run tests |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts` | Yes | modify | replace known-bug assertion with durable-winner assertion |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.concurrent.peer.test.ts` | Yes | create | real second-process production-path peer |
| `docs/reviews/CVF_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_WORKER_RETURN_2026-09-25.md` | Yes | create | uncommitted evidence and closeability recheck |
| `docs/reviews/evidence/cvf-acel-akoe-p2-r1-final-return-hash-2026-09-25.json` | Yes | create | detached pre/post gate exact-byte hash receipt |

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.delegation.ledger.persistence.ts` | read-only reusable lock owner; semantics must not drift |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.delegation.ledger.store.ts` | sibling owner is evidence only |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/package.json` | no dependency change |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` | launcher production behavior is not the root cause |
| `governance/**`; `CVF_SESSION/**`; `AGENT_HANDOFF*.md` | worker owns no guard or continuity surface |
| `docs/baselines/**`; `docs/work_orders/**`; `docs/roadmaps/**` | worker cannot rewrite authority |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.concurrent.peer.test.ts` | ABSENT | ABSENT | stop; do not overwrite an unreviewed file |
| `docs/reviews/CVF_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_WORKER_RETURN_2026-09-25.md` | ABSENT | ABSENT | stop; preserve prior evidence |
| `docs/reviews/evidence/cvf-acel-akoe-p2-r1-final-return-hash-2026-09-25.json` | ABSENT | ABSENT | stop; preserve prior receipt |

## Pre-Existing Dirty Path Exemptions

None. Dispatch requires a clean committed continuity HEAD.

## Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| desired terminal race outcome | launcher test | `ONE_DURABLE_TERMINAL_WINNER` | Yes |
| peer ready | peer plus run-store tests | `READY` | Yes |
| parent releases attempt | peer plus run-store tests | `START_ATTEMPT` | Yes |
| peer attempts lock | peer plus run-store tests | `ATTEMPTING` | Yes |
| parent releases ownership | peer plus run-store tests | `PARENT_RELEASE` | Yes |
| peer enters transaction | peer plus run-store tests | `ENTERED` | Yes |
| peer completes transaction | peer plus run-store tests | `COMPLETE` | Yes |
| fail-closed pre-release oracle | run-store tests | `REJECT_ENTRY_BEFORE_PARENT_RELEASE` | Yes |
| post-acquire cleanup | run-store tests | `SUBSEQUENT_PEER_ACQUIRES` | Yes |
| stale lock | run-store tests | `LOCK_HELD_PAST_STALE_THRESHOLD` | Yes |
| final return integrity | detached receipt | `NO_POST_GATE_MUTATION` | Yes |

## Write Ownership

Modify-listed/create-listed only. The worker owns exactly the six required
artifact paths above. Read-only sources do not become writable. Any additional
path requirement returns to the orchestrator before editing.

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: REQUIRED

## High-Risk Local Transaction Proof Contract

```json
{
  "transactionTarget": "MaoFileRunStore per-run append load replay mutate atomic-write transaction",
  "productionPathPeer": {
    "kind": "REAL_SECOND_PROCESS",
    "invocationPath": "EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.concurrent.peer.test.ts",
    "mutationPath": "EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts#MaoFileRunStore.appendEvent"
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

The security-tuple and rollback fields are the fixed nine-key admission schema.
This tranche performs no owner/DACL mutation and makes no security-rollback
claim; transaction rollback evidence is exact snapshot bytes/event history and
lock-residue state only. The worker must not fabricate ACL evidence.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-AKOE-P2

reviewRoundCount: 1

priorFindingSetDigest: a44fe1cf35db9b4b65a5b4439432665a80fa814a50b204ef82f96214bc6762d1

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: run_store_concurrent_write_lost_race

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT

quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: run_store_concurrent_write_lost_race

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
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "acel-akoe-p2-r1-run-store-race-correction",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "ACEL-AKOE-P2-R1-DISPATCH",
    "claimClass": "SCHEMA_COMPATIBILITY",
    "proofClass": "EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST",
    "evidenceRef": "docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md"
  }],
  "requiredDisposition": "READY_WITH_EXECUTABLE_PROOF",
  "successorScope": "EXECUTABLE_IMPLEMENTATION"
}
```

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON

Reason: internal-agent correction only; external invocation is forbidden.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_FIXTURE_AND_ASSERTION_PATH

positiveControl: reviewer independently launches two store instances against
one run and verifies exactly one valid terminal winner is durable.

negativeMutationClasses: pre-release peer entry; two-success/one-event lost
update; stale-lock takeover; stranded lock after rejected append; cross-run
over-serialization.

expectedInformationGain: distinguish production transaction safety from a
self-consistent worker fixture or assertion-only repair.

rerunCostReason: one bounded independent probe tests the decision-changing
concurrency claim without duplicating the full suite.

reviewerDecisionOwner: LOCAL

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
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact six-path manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| high_risk_transaction_proof | WORKER_RETURN | worker | IMPLEMENTATION | production source, peer fixture, tests, detached receipt | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | high_risk_transaction_proof |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | worker return and allowed edits | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted worker paths | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material paths | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer disposition or completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | material and continuity ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one internal worker followed by distinct Local reviewer/closer |
| phase | P2-R1 bounded runtime correction pending Local review |
| baseHeadFor(phase) | dispatchBaseHead=`fee4316f1`; executionBaseHead=worker capture after continuity; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact six-path worker manifest |
| traceScope(phase, actor) | worker return records commands, process barriers, hashes, and actual pending set |
| commitOwner(phase) | worker forbidden; Local closer after acceptance |
| crossBatchIsolation | clean committed dispatch-continuity base; no unrelated dirty paths |
| nextMoveSurfaces | worker return, Local review, material commit, separate continuity sync |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: internal worker after dispatch continuity passes

laneOwnedPaths: exact six-path worker manifest only

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: terminal worker return, exact changed/staged sets, focused
tests, full worker gate, and detached hash receipt

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution (WORKER_MUST_NOT_COMMIT)`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: 12 shown of 16 candidates; resolver output was truncated.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Worker execution (WORKER_MUST_NOT_COMMIT)" --role worker --lifecycle-phase pre-implementation --max-results 12 --json` |
| Returned defect count | 16 candidates; 12 returned |
| Returned defects | ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0020, ADIF-0021, ADIF-0047, ADIF-0048, ADIF-0050, ADIF-0051, ADIF-0055, ADIF-0056, ADIF-0057 |
| Disclosed defectIds | returned twelve plus controlling ADIF-0059 |
| Dispatch impact | preserve exact scope, source fidelity, current execution base, semantic convergence, truthful blocked/completion status, and no-commit separation |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_forbidden_filesystem_state.py` |
| literalTokensReviewed | work-order dispatch status; rework convergence fields; high-risk declaration and nine-key JSON; exact closeability graph fields; return status/recheck invariant; worker-return shape; detached digest terms |
| gateRunPurpose | confirm the completed packet after source inspection; not discover the runtime design or accept future evidence |
| claimBoundary | dispatch/output admission only; no implementation correctness, P2 closure, or production readiness claim |

## Worker Output Checker Read-Ahead Mandate

Before writing the return, read checker sources for `docs/reviews/`, worker-
return quality, structural headings, trace, delta boundary, corpus/value/
rescan sections, closeability, review cost, high-risk proof, and public export.
Use real headings and N/A-with-reason values where conditional sections do not
apply.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_WORKER_RETURN_2026-09-25.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts --pytest-target EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts --pytest-target EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.concurrent.peer.test.ts`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Checker Source
Read-Ahead Block; External Knowledge Intake Routing; Epistemic Process Block;
Agent Operation Trace Block; Delta Execution Claim Boundary Control Block;
Public Export Disposition; executionBaseHead; git status --short; Changed
Files; No-Commit Statement; Return-Time Closeability Recheck.

Conditional terms: Rescan Intelligence Hardening; Corpus Completeness And
Report Integrity; Finding-To-Governance Learning Disposition; Machine Closure
Package. Include each with N/A-with-reason when not applicable.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_COMPLETION_2026-09-25.md` only if separate closure evidence is necessary |
| reviewerOwnedClosurePaths | accepted six worker paths, reviewer disposition/optional completion, roadmap and continuity as separately authorized |
| closureOwner | Local reviewer/closer distinct from worker phase |
| workerCommitPermission | FORBIDDEN |

## Execution Plan

1. Complete pre-flight from the clean continuity HEAD and scaffold the exact
   return before long-form edits.
2. Recast the P2 probe as the desired durable-winner assertion and record its
   failure against pre-repair production bytes.
3. Add focused tests and the real second-process peer with deterministic
   barriers; confirm tests fail for the intended defect, not fixture setup.
4. Implement the smallest `appendEvent` transaction correction by reusing the
   existing lock primitive and exception-safe release.
5. Run focused tests, package typecheck/full suite, and exact changed-set checks.
6. Finalize return evidence with `PENDING_REVIEWER_EXECUTION`, capture its
   SHA-256, run the final worker gate, recapture SHA-256, write the detached
   receipt without editing the frozen return, and stop without staging/commit.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE because this tranche changes a
durable local state transaction and makes a concurrency-safety claim.

Expected Result / Prediction: serializing the entire same-run append
transaction with the existing exclusive-create lock should produce exactly one
durable winner for conflicting terminal attempts, preserve unrelated-run
parallelism, fail closed on stale/contended ownership, and release on every
return path.

Evidence Comparison Requirement: compare pre-repair desired assertions with
post-repair production-path, process-ordering, residue, replay, focused-suite,
and full-suite evidence.

Contradiction Handling Requirement: do not relax the oracle. Return blocked if
the fix requires forbidden paths, new dependencies, automatic stale takeover,
or cannot provide real peer and cleanup proof.

Claim Update Requirement: report the P2 blocker as resolved only with passing
executable proof and no new blocker; otherwise retain it explicitly.

## Evidence Requirements

- pre-repair desired-state assertion failure against committed source bytes;
- post-repair desired-state assertion pass and exact durable winner identity;
- ordered real second-process barrier transcript and command;
- post-acquire cleanup, stale-lock, no-residue, and different-run evidence;
- pre/post SHA-256 for every modified tracked file;
- focused tests, package typecheck, full package suite, bound
  pre-implementation gate, and worker-return full gate;
- exact changed and staged sets with staged set empty;
- detached final return-byte receipt with equal pre/post gate SHA-256 and
  `NO_POST_GATE_MUTATION`;
- `PENDING_REVIEWER_EXECUTION` for the Local-only independent probe;
- zero dependency installation, external invocation, provider/live/public
  action, stash, stage, or commit.

## Verification Commands

Run package commands from `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` except
the repository-root governance/Git commands:

```powershell
npx vitest run tests/mao.durable.run.store.test.ts tests/mao.operational.worker.launcher.test.ts tests/mao.durable.run.store.concurrent.peer.test.ts
npm run check
npm test -- --run
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_AKOE_P2_R1_DURABLE_RUN_STORE_CONCURRENCY_CORRECTION_2026-09-25.md
python governance/compat/run_worker_return_fast_gate.py --pytest-target EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.test.ts --pytest-target EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.operational.worker.launcher.test.ts --pytest-target EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.durable.run.store.concurrent.peer.test.ts
git diff --name-status
git diff --check
git diff --cached --name-only
git status --short --untracked-files=all
```

The worker records the exact command actually used to start the second process
and the six ordered barrier events. Test timeout is deadlock safety only.

## Acceptance Criteria

- [ ] Pre-flight proves committed packet and continuity release from a clean HEAD.
- [ ] Desired-state race assertion fails before production repair and passes after it.
- [ ] Exactly one conflicting terminal attempt succeeds and replay identifies the same winner.
- [ ] Real second-process ordering proves no ENTERED before PARENT_RELEASE.
- [ ] Post-acquire rejection/failure leaves no stranded lock; a later peer acquires.
- [ ] Stale lock fails closed without takeover, deletion, snapshot mutation, or false success.
- [ ] Different run identities remain independent.
- [ ] Existing replay/idempotency/discovery behavior passes focused and full regression suites.
- [ ] Exact six-path manifest, no staging, no commit, worker gate, and final hash receipt pass.
- [ ] Return is `COMPLETE_PENDING_REVIEW` only with `CLOSEABLE` and `outsideAuthorityBlockers: NONE`.

Fail conditions: any unmet checkbox; nondeterministic-only evidence; timeout
used as positive exclusion proof; both conflicting calls report success while
one event is absent; automatic stale takeover; forbidden-path need; unexpected
dependency; external effect; or failed required gate.

## Review Gate

The Local reviewer evaluates returned evidence without recreating the worker's
implementation. Required reviewer work is one independent process/concurrency
probe with a different fixture/assertion path, changed-set/hash review,
reviewer-fast, and pre-commit. Broader reruns require a named contradiction,
expected information gain, and cost reason.

## Operator Checkpoint

No further checkpoint is required inside the exact six-path manifest. A fresh
operator decision is required for a new dependency or runtime owner, any path
outside the manifest, automatic stale-lock recovery, multi-host/distributed
claims, P3/P4, provider/live/network/public/deployment action, or a higher risk
or claim ceiling.

## Closure Checklist

- [ ] Exact defect and dependent failure classes are resolved.
- [ ] Production source, three test artifacts, return, and receipt are the only worker paths.
- [ ] Independent probe remains pending in the worker return and is executed by Local review.
- [ ] No outside-authority blocker or status/closeability contradiction remains.
- [ ] Worker full gate and exact return-byte hash equality pass.
- [ ] Worker did not stage, commit, stash, or alter continuity.
- [ ] Local material commit and separate continuity remain pending.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` before edits if dispatch release is incomplete.
Stop during execution for any fail condition or scope contradiction. Return
`COMPLETE_PENDING_REVIEW` only when every acceptance item passes and the
Return-Time Closeability Recheck is `CLOSEABLE` with
`outsideAuthorityBlockers: NONE`. The strengthened machine gate enforces this
status/recheck join.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher/orchestrator |
| Provider or surface | private shared CVF workspace |
| Session or invocation | ACEL-AKOE-P2-R1 dispatch authoring, 2026-09-25 |
| Working directory | repository root |
| Command or tool surface | governed reads, hashes/searches, scaffold preview, apply_patch, gates, Git |
| Target paths | paired P2-R1 baseline and work order |
| Allowed scope source | operator confirmation plus P2 blocked evidence at `fee4316f1` |
| Before status evidence | clean worktree at `fee4316f1`; P2 blocked honestly; gate hardening committed |
| After status evidence | paired bounded packet; implementation remains gated by material and continuity commits |
| Diff evidence | exact paired packet paths against dispatch base |
| Approval boundary | dispatch authoring/release only; no worker implementation or P2 acceptance |
| Claim boundary | no fix correctness, P2 closure, provider/live/public/deployment/production claim |
| Agent type | Local orchestrator/reviewer as dispatch author |
| Invocation ID | `acel-akoe-p2-r1-dispatch-20260925` |
| Expected manifest | paired baseline and work order |
| Actual changed set | verified before handoff |
| Manifest delta | expected zero after authoring repair |
| Deletion or rename disposition | N/A with reason: none authorized or performed |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | bounded local durable-run-store source/test correction and evidence |
| claimDisposition | N/A with reason: dispatch only; repair behavior is pending worker evidence and Local review |
| receiptEvidence | N/A with reason: packet authoring creates no runtime receipt; worker must create the detached final-return hash receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source locators, hashes, committed defect evidence, exact manifest, and governance gates |
| invocationBoundary | local `MaoFileRunStore` test seams and one child Vitest process only |
| interceptionBoundary | no IDE/shell/filesystem/provider interception or mandatory wrapper claim |
| claimLanguage | deterministic local correction pending independent Local acceptance |
| forbiddenExpansion | new runtime/owner, sibling lock-semantic edit, dependency, external/provider/live/public/P3/P4/deployment, worker commit |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-AKOE-P2-R1 --title "ACEL AKOE-P2-R1 Durable Run Store Concurrency Correction" --date 2026-09-25 --base fee4316f1affdcf2675c4e9832d96ebc7b917402 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id run_store_concurrent_write_lost_race --prior-finding-set-digest a44fe1cf35db9b4b65a5b4439432665a80fa814a50b204ef82f96214bc6762d1 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence run_store_concurrent_write_lost_race --scec-problem-key acel-akoe-p2-durable-intent-projection --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/reviews/CVF_ACEL_AKOE_P2_DURABLE_INTENT_AND_PROJECTION_RECONCILIATION_WORKER_RETURN_2026-09-25.md --scec-predecessor-sha256 a44fe1cf35db9b4b65a5b4439432665a80fa814a50b204ef82f96214bc6762d1 --scec-required-disposition READY_WITH_EXECUTABLE_PROOF --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | generic worker rework dispatch with no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed exact authority, source, transaction, manifest, evidence, closeability, and return contracts |
| checkerReadAheadConfirmation | dispatch, high-risk, closeability, convergence, trace, ADIF, review-probe, forbidden-state, and export checkers inspected |
| docOnlyNewFields | deterministic peer barriers, desired durable-winner oracle, detached final-return receipt |
| claimBoundary | dispatch provenance only; no implementation acceptance or closure claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private-provenance runtime correction with no public-sync authority or
public artifact evidence.

## Claim Boundary

This order authorizes one no-commit internal worker to modify exactly the
durable run-store source, two existing tests, one new peer test, one return,
and one detached hash receipt. It does not authorize edits to sibling lock
owners, dependencies, runtime architecture, governance/session surfaces,
P3/P4, provider/live/network/public/deployment/production behavior, or commit.
