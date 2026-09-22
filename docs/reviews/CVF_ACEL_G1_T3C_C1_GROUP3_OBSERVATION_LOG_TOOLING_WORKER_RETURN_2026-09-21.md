# CVF ACEL G1 T3C-C1 AR1 Transaction Architecture Proof Closure Worker Return

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Date: 2026-09-22

docType: review

Batch ID: ACEL-G1-T3C-C1-AR1-TRANSACTION-ARCHITECTURE-PROOF-CLOSURE

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md`

executionBaseHead: d61080c46d2e4073e617c1acd55748dd8beb2580

rawMemoryReleased=false

contractProfile: WORKER_RETURN_FULL_GATE_V1

independentProbeRequired: YES

independentProbeDisposition: PENDING_REVIEWER_EXECUTION

## Rework Convergence Self-Proof

rootCauseClusterId: acel-g1-t3c-c1-transaction-architecture-v2-problem

reworkGeneration: 0

consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES

productionBindingEvidence: NOT_APPLICABLE_WITH_REASON: hermetic tooling tranche; real Party B execution and source creation remain forbidden

adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

internalAgentInvocationCount: 1

externalAgentInvocationCount: 0

providerCallCount: 0

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: no provider or quota was consumed

terminalReadinessVerdict: READY_FOR_REVIEW

## Purpose

Close the five AR1 transaction-architecture findings with deterministic,
hermetic evidence: real second-process serialization, exception-safe mutex
lifetime, exact owner/DACL restoration, complete DACL adversaries, and a
canonical-return gate bound to the AR1 work order.

## Target / Source

| Source | Use |
| --- | --- |
| `docs/baselines/CVF_GC018_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_REOPEN_2026-09-22.md` | fresh architecture authority |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_AR1_TRANSACTION_ARCHITECTURE_PROOF_CLOSURE_2026-09-22.md` | exact four-path implementation and proof contract |
| `docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md` | five terminal findings from the stopped predecessor chain |
| four Required Artifact Manifest paths | bounded implementation and evidence |

## Scope / Methodology

Only the four AR1-owned paths were used. The writer now owns one cross-process
mutex from before any filesystem mutation through DACL read-back, final chain
validation, or verified rollback. Disposable self-tests launch the same writer
in a genuine second `pwsh` process and coordinate unique named events:
`READY -> START_ATTEMPT -> ATTEMPTING -> PARENT_RELEASE -> ENTERED -> COMPLETE`.
No sleep or elapsed-time observation is used as exclusion evidence; timeouts
are deadlock bounds only.

The real Group 1 source was not read, the real Group 3 log was not created,
and no credential, `runas`, Party B session, network, provider or public
surface was used.

## Findings / Position

| Finding | Position | Evidence |
| --- | --- | --- |
| T3C-C1-R2-RV-1 peer exclusion/rollback race | FIXED | T3C-C1-21/22 use a real second writer process; `ENTERED` remains false at deterministic attempt barriers and after final validation; rollback completes before `PARENT_RELEASE`; peer re-reads and appends exactly once |
| T3C-C1-R2-RV-2 post-acquire leak | FIXED | `New-TransactionGuard -InjectPostAcquireFailureForTest` throws after OS acquisition, cleans up internally, then a real peer acquires and appends |
| T3C-C1-R2-RV-3 incomplete applied-security proof | FIXED | owner SID, protection flag and the complete ACE semantic multiset are read back; only Party B, SYSTEM and Administrators Allow/FullControl tuples pass |
| T3C-C1-R2-RV-4 incomplete rollback/adversary proof | FIXED | rollback snapshots/restores Owner+Access descriptor and re-compares owner, protection and every sorted ACE tuple; extra allow, deny, inheritance and wrong owner fail closed |
| T3C-C1-R2-RV-5 final return identity | FIXED_PENDING_FINAL_EXTERNAL_RECEIPT | canonical return is updated in place and the mandated pre/post digest sequence is the final operation; digest is reported without editing this file afterward |

## Risk / Corrective Action

| Risk | Control |
| --- | --- |
| peer enters during DACL or validation | named ATTEMPTING and ENTERED events plus OS mutex; zero-time state assertions before and after final validation |
| rollback erases later peer append | rollback completes while guard is held; parent signals release before unlocking; peer then re-reads current bytes and appends once |
| mutex leaked by acquisition helper | deterministic post-acquire throw plus real peer acquisition |
| partial DACL comparison | complete normalized semantic tuple multiset and owner/protection comparison |
| evidence drift | AR1-bound fast gate and pre/post SHA-256 equality with no later edit |

## Decision / Disposition

`COMPLETE_PENDING_REVIEW`. All AR1 implementation oracles pass. The return is
pending Local reviewer execution and acceptance only; it makes no source
establishment, activation, admission, T3E, public or deployment claim.

## P4 Automatic Evidence Observation Block

p4ObservationEligibility: AUTO

p4ObservationPhase: N/A with reason: not a natural P4 observation candidate

p4HardObligationLocator: N/A with reason: not a natural P4 observation candidate

p4HardObligationPattern: N/A with reason: not a natural P4 observation candidate

p4SourceAuthorityLocator: N/A with reason: not a natural P4 observation candidate

## Architecture Readiness Echo

architectureMatrixSchema: NOT_APPLICABLE_WITH_REASON: AR1 uses a paired architecture baseline, not an architecture-readiness matrix

architectureMatrixCanonicalDigest: N/A with reason: no architecture matrix applies

architectureSemanticReviewPath: N/A with reason: no architecture matrix applies

architectureSemanticReviewCommit: N/A with reason: no architecture matrix applies

architectureSemanticReviewFileSha256: N/A with reason: no architecture matrix applies

architectureBindingEchoDisposition: N/A with reason: no architecture matrix applies

## Evidence Readiness Disposition

evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON: bounded local
implementation has no discovery-audit manifest.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3c-c1-transaction-architecture-v2-problem","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["peer-process-exclusion-proof","exception-safe-guard-lifetime","exact-security-rollback-proof","complete-security-adversary-matrix","final-return-evidence-binding"],"reopened":[],"current":["peer-process-exclusion-proof","exception-safe-guard-lifetime","exact-security-rollback-proof","complete-security-adversary-matrix","final-return-evidence-binding"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3C-C1-AR1-WORKER-RETURN","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"scripts/acel_g1_party_b_group3_observation_writer.ps1"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: N/A with reason: all AR1 worker obligations pass; Local reviewer owns acceptance

workerRedispatchAllowed: NO

## Core Guard Self-Protection Authorization

The AR1 work order authorizes only the existing Group 3 writer, checker,
focused checker test and canonical return. No hook, catalog or general guard
was changed. The two unrelated task-class checker paths are parked, read-only
and byte-preserved.

Authorized guard-maintenance scope: bounded Group 3 checker/test preservation
and writer correction under the committed AR1 order; no general guard change.

Protected paths:

- `governance/compat/check_acel_g1_registry_observation_log.py`
- `governance/compat/test_check_acel_g1_registry_observation_log.py`
- `governance/compat/check_task_class_calibration_owner_evidence.py`
- `governance/compat/test_check_task_class_calibration_owner_evidence.py`

Operator authorization: the operator authorized Local to finish AR1 so the
workspace can move to the CVF foundation-learning tranche.

Rollback boundary: Group 3 checker/test remain uncommitted until Local
acceptance; the two task-class checker paths are unrelated parked inputs and
were not mutated.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_gate_to_role_closeability.py` |
| literalTokensReviewed | required worker-return headings, status, dispatch binding, independent-probe disposition, operation trace, claim-boundary and no-commit tokens |
| gateRunPurpose | structural confirmation after implementation, not implementation discovery |
| claimBoundary | checker conformance is packet evidence, not real source or runtime proof |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | INTERNAL_AGENT implementation worker followed by Local reviewer-fixer |
| Provider or surface | shared private CVF workspace |
| Session or invocation | ACEL-G1-T3C-C1-AR1, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | governed reads, apply_patch, Python focused tests, PowerShell hermetic multi-process self-test, git status/hash |
| Target paths | exact four AR1 Required Artifact Manifest paths |
| Allowed scope source | committed AR1 baseline and work order plus operator authorization for reviewer to finish |
| Before status evidence | HEAD `d61080c46d2e4073e617c1acd55748dd8beb2580`; staging empty; thirteen parked paths; four pending AR1 paths; real log absent |
| After status evidence | four pending AR1 paths only; staging empty; thirteen parked paths preserved; real log absent |
| Diff evidence | `git diff --name-status` plus exact path/hash reconciliation and full status |
| Approval boundary | hermetic correction/review only |
| Claim boundary | no Party B execution, real source, provider, public or deployment effect |
| Agent type | INTERNAL_AGENT worker / Local reviewer-fixer |
| Invocation ID | `acel-g1-t3c-c1-ar1-proof-closure-20260922` |
| Expected manifest | exact four paths |
| Actual changed set | exact four paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | exact four-path hermetic AR1 correction |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: named event transitions, child exit zero, focused test results and final hash receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Python 42/42; writer 56/56; checker self-test exit 0 |
| invocationBoundary | local disposable fixtures and child `pwsh` processes only |
| interceptionBoundary | no IDE, shell, filesystem, Git or provider interception claim |
| claimLanguage | corrected tooling is complete pending independent Local acceptance |
| forbiddenExpansion | no credentials, alternate user, real source, Party C/Group 4, T3E, admission, provider, public or deployment |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Input type disclosure | inputs are internal Local review and governed AR1 authority; no external intake was used |
| Internal source | `docs/reviews/CVF_ACEL_G1_T3C_C1_R2_TRANSACTION_LIFETIME_AND_SECURITY_VERIFICATION_COMPLETION_2026-09-21.md` |
| Chain map route | N/A_NO_NEW_EXTERNAL_INPUT: direct internal implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this canonical return |
| Disposition | local first-party correction only |
| Claim Boundary | no external source authority or remote implementation claim |

## External/Local Coordination Binding

Role: INTERNAL_AGENT; phase: AR1 implementation return; decision owner: LOCAL.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason: not a rescan.
- Predecessor intake artifact: N/A with reason: no intake refresh.
- Delta ledger status: N/A with reason: bounded named implementation.
- Routing matrix status: N/A with reason: no rescan routing.
- Semantic sampling status: N/A with reason: deterministic executable probes replace sampling.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: AR1 repairs named local findings; it does not refresh an external or
internal discovery corpus.

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected Result / Prediction: one outer mutex plus deterministic process
  barriers and semantic descriptor snapshots will prevent peer/lost-update and
  partial-security false positives.
- Evidence Comparison: confirmed by a genuine child writer process, exact final
  record counts, deterministic post-acquire failure, semantic DACL adversaries,
  42/42 focused Python tests and 56/56 writer cases.
- Contradiction or Gap Disposition: Claude's partial implementation used a raw
  thread without a PowerShell runspace and a mutex-only peer; both were
  replaced, not waived.
- Claim Update: AR1 findings are CONFIRMED_RESOLVED_PENDING_LOCAL_ACCEPTANCE.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded named-file implementation; no repository-wide completeness claim.
- Corpus root: AR1 baseline, work order, terminal review and exact four outputs.
- Snapshot time: 2026-09-22 at execution base HEAD `d61080c46d2e4073e617c1acd55748dd8beb2580`.
- Enumeration command: filesystem-backed direct reads of the exact named paths; no directory enumeration was required.
- Manifest artifact or inline manifest: Required Artifact Manifest in the AR1 work order.
- Manifest hash: N/A with reason: authoritative inline manifest.
- Processing ledger artifact or inline ledger: named paths only.
- Allowed terminal statuses: `READ`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`. Observed: all named inputs `READ`; zero `SKIPPED_WITH_REASON`/`DEFERRED`/`BLOCKED_UNREADABLE`.
- Reconciliation: manifest=17; ledger_terminal=17; exclusions=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: all paths outside the AR1 manifest.
- Unreadable or unsupported files: none.
- Aggregation check: exact four owned paths plus thirteen parked read-only paths.
- Drift check: staging empty and real log absent.
- Output traceability: this return and command evidence.
- Adversarial verification: real second-process disposable probes.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

| Field | Value |
| --- | --- |
| Defect class | ORCHESTRATOR_PACKET_GAP_AND_WORKER_EXECUTION_ERROR |
| Learning lane | GOVERNANCE_CONTROL_PLANE |
| Finding | shape-only concurrency evidence and incomplete security rollback let a mutex-only peer and raw-thread probe appear sufficient |
| Disposition | RULE_ADDED_IN_AR1 |
| Next control action | carry deterministic cross-process barriers, exception-lifetime injection and semantic security restoration into the later CVF foundation tranche |
| Runtime/provider/cost learning lane | N/A_WITH_REASON: pure offline hermetic tooling |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private corrective tooling; no public-sync authority.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is a `COMPLETE_PENDING_REVIEW` return.
Local reviewer/closer owns final acceptance, material commit and continuity.

## Claim Boundary

This return proves only the four uncommitted AR1 tooling/evidence outputs
against disposable fixtures. It does not establish Group 3, run Party B,
authorize credentials, create a real source, wire T3E, admit a candidate, call
a provider, publish or deploy.

## git status --short

Exactly thirteen parked untracked paths plus these four AR1 paths are present;
staging is empty and
`governance/sources/registry_observation_log/LOG.jsonl` is absent. The full
status was captured immediately before the final gate.

## Changed Files

- `scripts/acel_g1_party_b_group3_observation_writer.ps1` - AR1 mutex lifetime,
  same-writer peer mode, deterministic barriers, semantic DACL apply/restore,
  adversaries and cleanup probes.
- `governance/compat/check_acel_g1_registry_observation_log.py` - preserved
  byte-for-byte; no demonstrated checker dependency required a change.
- `governance/compat/test_check_acel_g1_registry_observation_log.py` -
  preserved byte-for-byte; existing 42-test coverage passes.
- `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md` -
  replaced stale R1/R2 evidence with this AR1 return.

The thirteen parked paths remain read-only and unstaged.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:

frictionLevel: HIGH

frictionType: ENUM_OR_TOKEN_MISMATCH

observedStep: a raw .NET thread executing a PowerShell script block crashed
because it had no runspace, while a separate mutex-only child did not exercise
the writer transaction that the proof claimed.

preventiveControlCandidate: HELPER_DIAGNOSTIC

preventiveControlCandidateNote: concurrency proof must invoke the production
transaction path in a real process and bind attempt/entry/release events; DACL
rollback proof must compare normalized owner, protection and all ACE tuples.

## Command Evidence

- `python -m pytest governance/compat/test_check_acel_g1_registry_observation_log.py -q` - PASS: 42 passed.
- `python governance/compat/check_acel_g1_registry_observation_log.py --self-test` - PASS: exit 0.
- `pwsh -NoProfile -File scripts/acel_g1_party_b_group3_observation_writer.ps1 -SelfTest` - PASS: 56/56, exit 0.
- `git diff --check` - PASS.
- AR1-bound worker-return fast gate - PASS when the final content-frozen command exits 0.
- Final return SHA-256 binding - PASS when the externally reported pre/post digests are identical; no file edit is allowed after the post-gate digest.

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored throughout worker execution: staging is empty
and no worker commit was created. Local reviewer/closer owns any accepted
material and continuity commits.
