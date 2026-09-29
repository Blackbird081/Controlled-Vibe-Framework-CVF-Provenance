# CVF ACEL G1 T3D-C1 Group 4 Issuer Registry And Lookup Tooling Worker Return

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Date: 2026-09-23

docType: review

Batch ID: ACEL-G1-T3D-C1-GROUP4-ISSUER-REGISTRY-LOOKUP-TOOLING

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md`

executionBaseHead: f15d552b557700fae1898e16052b2bc1dd9c3232

rawMemoryReleased=false

contractProfile: WORKER_RETURN_FULL_GATE_V1

independentProbeRequired: YES

independentProbeDisposition: PENDING_REVIEWER_EXECUTION

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Rework Convergence Self-Proof

rootCauseClusterId: acel-g1-t3d-c1-group4-tooling-problem

reworkGeneration: 3

consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES

productionBindingEvidence: NOT_APPLICABLE_WITH_REASON: hermetic tooling tranche; real Party C/Party B source execution remains forbidden

adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

internalAgentInvocationCount: 1

externalAgentInvocationCount: 0

providerCallCount: 0

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: no provider or quota was consumed

terminalReadinessVerdict: READY_FOR_REVIEW

## Purpose

Return the exact five uncommitted T3D-C1 outputs implementing and hermetically
testing the accepted Group 4 registry and lookup-response contract. The result
is tooling-only and does not create a real Group 4 source or execute T3E.

## Target / Source

| Source | Use |
| --- | --- |
| `docs/baselines/CVF_GC018_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md` | exact five-path dispatch baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_2026-09-22.md` | implementation, proof, gate and no-commit contract |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | closed Group 4 schemas, hash domains, identities and lifecycle |
| `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_COMPLETION_2026-09-22.md` | accepted T3D-C0 byte/security joins |
| five Required Artifact Manifest paths | bounded implementation and evidence |

## Source Inventory

| Item | Processing status | Disposition |
| --- | --- | --- |
| active continuity front doors and handoff | READ | current dispatch confirmed |
| paired T3D-C1 baseline and work order | READ | controlling authority |
| T2F Group 4 contract and T3D-C0 completion | READ | exact implementation contract |
| Party B/C Local verification records | READ | exact account/SID boundary |
| accepted T3C transaction architecture | READ | reused process/security proof pattern |
| worker-return and applicable governance checker sources | READ | literal output/gate shape resolved before final gate |
| thirteen parked untracked paths | HASHED_NOT_READ_FOR_SEMANTICS | byte-preservation boundary only |

## Scope / Methodology

The worker created only the two PowerShell tools, the read-only Python checker,
its focused tests, and this return. The Python implementation is deliberately
limited to the closed ASCII/no-floating-point Group 4 JCS domain. It performs
strict UTF-8, unpadded base64url, exact-schema, byte-identity, digest, lifecycle,
snapshot, chain, UUID and identity checks without repairing any input.

Each PowerShell writer defaults to `-SelfTest`. Real modes require the exact
verified principal, exact SID, explicit confirmation, canonical Git root, and
exact governed path. Disposable self-tests use same-directory pre-hardened
copy-on-write publication, atomic rollback, deterministic hard process
termination, ordered and semantic security read-back, and a real second `pwsh`
process that executes the guarded production transaction, coordinated by
`READY -> START_ATTEMPT -> ATTEMPTING -> PARENT_RELEASE -> ENTERED -> COMPLETE`.
Timeouts are deadlock bounds only; no sleep is used as an exclusion oracle.

## Findings / Position

| Contract area | Position | Evidence |
| --- | --- | --- |
| content and registry vectors | PASS | 91-byte content JCS recomputes `db76dcc...d12ca`; 618-byte envelope recomputes `d31e0c...27f2` |
| strict content profile | PASS | exact three keys, fixed authority, row/content identity, ASCII identity and bounded integer policy version; extra/missing/type/encoding/JCS/hash drift rejects |
| registry lifecycle | PASS | positive versions, one active row, terminal revocation and timestamp/nullability rules checked; ordering compares parsed UTC instants, including unequal fractional precision |
| response framing and chain | PASS | zero-byte empty log; compact JCS plus LF; BOM/CRLF/blank/partial/non-JCS rejects; exact prior prefix and chain recomputation; every stored row is outcome-replayed at its own `queriedAt` |
| evaluator and observation binding | PASS | accepted Group 3 checker validates the closed record, chain and timestamps before response replay; the shared deterministic classifier receives only strictly decoded observed snapshot bytes; exact unique ID/version/hash/bytes, Party B observer, authority and freshness policy are enforced; found-observation version/hash/content drift is hard no-append |
| idempotency | PASS | identical immutable tuple returns the fully replay-validated stored row without append; tuple drift is `LOOKUP_ID_CONFLICT`; duplicate durable ID and hash-consistent forged terminal outcome reject |
| result taxonomy | PASS | malformed/incomplete/unavailable/schema/issuer/ambiguity/conflict stay no-append; stored-content, attested or claimed cryptographic mismatch yields one rejected/null-code receipt; observation uncertainty precedes ACTIVE/status and yields one unresolved/exact-code receipt; `queriedAt` is minted by the wrapper |
| Party C transaction | PASS | 53 executable checks cover component-walk containment, explicit resolved Python/checker validation of captured bytes inside the guard, existing-target and competitor-race preservation, a same-target successor process after injected acquisition failure, actual competing validated publish, three hard-kill barriers and orphan recovery |
| Party B transaction | PASS | 51 executable checks cover zero-byte initialization, competitor-race preservation, concurrent identical-UUID production appends leaving one row, same-target successor entry after injected acquisition failure, three production-append hard-kill barriers, exception-safe temp hardening, exact reachable arbitrary-descriptor rollback, pre-mutation security rejection, framing and checker taxonomy |
| security | PASS | owner/protection and every complete ACE tuple are checked as an exact ordered vector and separately as a semantic multiset; actual rollback checks both for extra-allow, deny, inherited and unprotected descriptors; wrong owner is rejected by the complete-state oracle and production prevalidation, while actual Administrators-owner fixture creation is truthfully recorded as OS-denied under the unprivileged worker token |
| real source boundary | PASS | registry and response-log paths remained absent; Group 3 source bytes remained unchanged |

## Risk / Corrective Action

| Risk | Control |
| --- | --- |
| general-JCS overclaim | checker accepts only the closed Group 4 primitive domain and explicitly rejects unsupported JSON types |
| target visible under ambient DACL | both writers harden and read back a same-directory temp before atomic publication/replacement |
| peer/lost-update race | one named mutex spans pre-state capture through final byte/security validation or exact rollback |
| initial-create ownership race | rollback deletes an absent pre-state target only after this transaction's no-overwrite move succeeds; injected competing publication remains byte-exact |
| guard leak or unsafe restoration | acquisition-helper failure releases internally; restoration begins only after caller acquisition and pre-state capture; an existing target survives the injected failure |
| interrupted transaction | actual worker processes are terminated after acquisition, after hardened-temp flush and immediately before replace; the next guarded transaction removes deterministic orphan names and proceeds |
| partial security comparison | exact owner/protection plus ordered complete ACE tuples and separately sorted complete tuple multisets are checked on final state and rollback |
| dedicated-principal Python discovery | both real interfaces require an explicit executable path and preflight it under the executing identity; hermetic modes resolve `py -3` then `python` and pass the resolved runtime through every checker call |
| schema-complete registry integrity mismatch | strict publisher checking still rejects it, while the lookup receipt context admits the structural/canonical envelope, derives snapshot metadata and deterministically emits rejected/null without treating malformed input as receipt-eligible |
| forged historical receipt | one shared classifier prepares new rows and replays every stored row against captured registry plus fully parsed Group 3 at stored `queriedAt`; terminal result, error code or selected entry-version drift rejects |
| hard observation snapshot drift | a found ID with version, digest or decoded-byte drift raises a stable binding failure and produces no receipt; only missing ID, authority and freshness retain closed unresolved outcomes |
| intermediate reparse escape | both test-only interfaces walk each existing component from the canonical system temp root through disposable inputs, fixture roots and target parents; nested-junction adversaries reject |
| widened response-log prestate | production append validates exact Party B owner/protection/ordered ACE vector/semantic multiset before orphan cleanup, temp creation or replacement |
| distinct-owner test privilege | the current token cannot assign Administrators ownership (`The security identifier is not allowed to be the owner of this object.`); no wrong-owner rollback is claimed, and executable proof instead covers OS denial plus oracle rejection and pre-mutation fail-closed behavior |
| rollback masks primary failure | rollback mismatch produces a distinct failure retaining primary and rollback context |
| scope expansion | exact-five manifest, empty staging, source absence and 13/13 parked hashes are rechecked at return |

## Decision / Disposition

`COMPLETE_PENDING_REVIEW`. The five owned outputs satisfy the worker-side
hermetic acceptance contract. Local still owns the independent process/security
probe, acceptance, staging, commit and any later source-creation decision.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: N/A with reason: all worker-owned obligations pass; Local reviewer owns the pending independent probe

workerRedispatchAllowed: NO

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3d-c1-group4-tooling-problem","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":["REVIEWER_REWORK_REQUIRED"],"resolved":["REVIEWER_REWORK_REQUIRED"],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{"REVIEWER_REWORK_REQUIRED":{"evidenceClass":"EXECUTABLE_PROOF","evidencePath":"governance/compat/test_check_acel_g1_issuer_registry.py","sha256":"18239b60f7217da5d84b76f8bf77a455edc3270f00a88b6f4564820aed84be97","locator":"class DurablePreparationTests","claimId":"ACEL-G1-T3D-C1-TOOLING-WORKER-RETURN"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":3,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3D-C1-TOOLING-WORKER-RETURN","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_WORKER_RETURN_2026-09-22.md"}],"requiredDisposition":"READY_WITH_EXECUTABLE_PROOF","successorScope":"EXECUTABLE_IMPLEMENTATION"}
```

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create only the Group 4 source-specific
read-only checker and its focused test under the committed T3D-C1 packet. The
two task-class checker paths below are pre-existing parked files and are listed
solely so changed-set accounting cannot mistake their untracked presence for
this worker's authority.

Protected paths:

- `governance/compat/check_acel_g1_issuer_registry.py`
- `governance/compat/test_check_acel_g1_issuer_registry.py`
- `governance/compat/check_task_class_calibration_owner_evidence.py`
- `governance/compat/test_check_task_class_calibration_owner_evidence.py`

Operator authorization: committed T3D-C1 work order with source-specific
checker/test scope and mandatory preservation of the thirteen parked paths.

Rollback boundary: reject or remove only the five uncommitted T3D-C1 outputs;
do not mutate the accepted sources, continuity, general guards, or parked files.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/run_worker_return_fast_gate.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | required headings; complete-pending status; dispatch binding; exact independent-probe disposition; trace and manifest fields; no-commit token; private export enum |
| gateRunPurpose | post-implementation confirmation of completed behavior and return shape |
| claimBoundary | structural conformance and hermetic evidence only; no source, T3E or runtime authority |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | INTERNAL_AGENT implementation worker |
| Provider or surface | shared private CVF workspace |
| Session or invocation | ACEL-G1-T3D-C1 tooling implementation, 2026-09-22 |
| Working directory | repository root |
| Command or tool surface | governed direct reads, apply_patch, Python compile/pytest/checker, PowerShell multi-process self-tests, Git status/hash |
| Target paths | exact five Required Artifact Manifest paths |
| Allowed scope source | committed T3D-C1 baseline/work order and active handoff |
| Before status evidence | HEAD `f15d552b557700fae1898e16052b2bc1dd9c3232`; staging empty; thirteen parked paths only; all five outputs and all three forbidden paths absent |
| After status evidence | exactly five new worker paths plus thirteen parked paths; staging empty; all three forbidden paths absent |
| Diff evidence | `git diff --name-status` and `git status --short --untracked-files=all` exact-manifest reconciliation |
| Approval boundary | hermetic implementation and no-commit return only |
| Claim boundary | no credentials, alternate-principal execution, source creation, second observation, T3E, provider/live/public/deployment effect |
| Agent type | INTERNAL_AGENT |
| Invocation ID | `acel-g1-t3d-c1-group4-tooling-worker-20260922` |
| Expected manifest | `scripts/acel_g1_party_c_group4_registry_writer.ps1`; `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1`; `governance/compat/check_acel_g1_issuer_registry.py`; `governance/compat/test_check_acel_g1_issuer_registry.py`; `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_WORKER_RETURN_2026-09-22.md` |
| Actual changed set | `scripts/acel_g1_party_c_group4_registry_writer.ps1`; `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1`; `governance/compat/check_acel_g1_issuer_registry.py`; `governance/compat/test_check_acel_g1_issuer_registry.py`; `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_WORKER_RETURN_2026-09-22.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | exact five-path hermetic Group 4 tooling implementation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: focused test counts, checker receipt, writer self-test receipts, status and hash reconciliation |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Python 82/82; checker 9/9; Party C 53/53; Party B 51/51 |
| invocationBoundary | disposable local fixtures and same-writer child `pwsh` processes only |
| interceptionBoundary | no IDE, shell, Git, filesystem, credential or provider interception claim |
| claimLanguage | tooling is complete pending distinct Local review; source remains absent |
| forbiddenExpansion | no credentials, Party B/C execution, real source, second observation, T3E, admission, live/provider, public or deployment |

## Machine Closure Package

| Closure item | Worker evidence | Disposition |
| --- | --- | --- |
| work order | committed T3D-C1 packet | AUTHORITY_READ |
| exact five worker paths | this return and status reconciliation | COMPLETE_PENDING_REVIEW |
| focused tooling | 82 Python tests plus 9/53/51 self-test receipts | PASS |
| real Group 4 source | both paths absent | BLOCKED with reason: later operator checkpoint |
| independent Local probe | reviewer-owned | PENDING_REVIEWER_EXECUTION |
| material/continuity commits | closer/session-sync owned | NOT_PERFORMED |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Input type disclosure | only repository-governed CVF authority and local implementation evidence were used |
| Internal source | `docs/reviews/CVF_ACEL_G1_T3D_C0_GROUP4_CONTRACT_COHERENCE_AMENDMENT_COMPLETION_2026-09-22.md` |
| Chain map route | N/A_NO_NEW_EXTERNAL_INPUT: shared-workspace internal implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this worker return |
| Disposition | local first-party implementation only |
| Claim Boundary | no external research, remote implementation, MCP/CLI or public evidence authority |

## External/Local Coordination Binding

Role: INTERNAL_AGENT; phase: T3D-C1 implementation and no-commit return;
decision owner: LOCAL. External research remained closed.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Rescan Intelligence Hardening

- Original source artifact: N/A with reason: not a rescan.
- Predecessor intake artifact: N/A with reason: no intake refresh.
- Delta ledger status: N/A with reason: bounded named implementation.
- Routing matrix status: N/A with reason: no rescan routing.
- Semantic sampling status: N/A with reason: executable deterministic tests replace sampling.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: this tranche implements an already accepted local contract and does
not discover, refresh, or absorb a corpus.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded named-file implementation; no repository-wide completeness claim.
- Corpus root: current-authority startup surfaces, paired T3D-C1 packet, named T2F/T3D/T3C sources, applicable checker sources and exact five outputs.
- Snapshot time: 2026-09-22 at execution base HEAD `f15d552b557700fae1898e16052b2bc1dd9c3232`.
- Manifest artifact or inline manifest: Required Artifact Manifest in the T3D-C1 work order.
- Manifest hash: N/A with reason: authoritative inline exact-five manifest.
- Processing ledger artifact or inline ledger: Source Inventory in this return.
- Allowed terminal statuses: `READ`, `HASHED_NOT_READ_FOR_SEMANTICS`, `SKIPPED_WITH_REASON`, `DEFERRED`, `BLOCKED_UNREADABLE`.
- Enumeration command: `rg --files --hidden --no-ignore` constrained against the bounded inline manifest, followed by exact status/hash reconciliation.
- Reconciliation: `manifest=5 owned outputs + 13 parked preservation paths`; `ledger_terminal=5 CREATED_AND_TESTED + 13 HASHED_NOT_READ_FOR_SEMANTICS`; `exclusions=all paths outside the bounded named authority and implementation manifest`; `unresolved=0`.
- Unresolved files: 0 (`unresolved_count=0`).
- Declared exclusions: all paths outside the bounded named authority and exact-five implementation manifest.
- Unreadable or unsupported files: none.
- Aggregation check: exact five worker outputs plus thirteen parked read-only paths.
- Drift check: staging empty, forbidden paths absent and parked hashes equal before/after.
- Output traceability: Changed Files and Command Evidence below.
- Adversarial verification: strict mutation matrix, failure injection and real second-process barriers.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected Result / Prediction: the closed T3D-C0 contract can be implemented
  in five paths with exact byte/security behavior and no governed source effect.
- Evidence Comparison: confirmed by 82 focused tests, independent checker
  vectors, two real-peer writer suites, exact source absence and parked hashes.
- Contradiction or Gap Disposition: independent review found acquisition-state,
  peer-path, observation-validation, receipt-taxonomy, timestamp trust,
  complete-ACE, hard-termination and placeholder-test defects. R2 then found
  test-mode containment, dedicated-principal Python, receipt-eligible stored
  integrity mismatch, production-append concurrency, descriptor restoration and
  temp-cleanup gaps. R3 found historical-receipt semantic replay, hard snapshot
  drift, intermediate-reparse, initial-create race, guard-release process proof,
  lifecycle instant ordering and response prestate-security gaps. All reachable
  behavior was repaired in the same five paths and made executable; Windows
  denied creation of a distinct-owner fixture, so no such rollback is claimed.
- Claim Update: prediction confirmed for hermetic tooling only; independent
  Local probe and any source/T3E lifecycle movement remain pending.

## Finding-To-Governance Learning Disposition

| Field | Value |
| --- | --- |
| Defect class | WORKER_EXECUTION_ERROR |
| Learning lane | GOVERNANCE_CONTROL_PLANE |
| Finding | a failure injected inside acquisition can precede caller-owned pre-state capture, so the transaction catch must not infer an absent pre-state and delete an existing target |
| Disposition | LOCAL_FIX_COMPLETE |
| Next control action | preserve the guard-helper cleanup oracle and separate `guardAcquired` marker in future copy-on-write writers |
| Runtime/provider/cost learning lane | N/A_WITH_REASON: pure offline hermetic tooling |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private local-principal tooling; no public-sync authority.

## Claim Boundary

This return proves only five uncommitted hermetic tooling/evidence outputs.
It does not use credentials or Party B/C execution; create `REGISTRY.json` or
`LOOKUP_RESPONSES.jsonl`; append a second observation; perform T3E; bind a
consumer; promote/admit; invoke a provider; publish; deploy; or claim
production readiness.

## git status --short

Exactly thirteen parked untracked paths plus the five T3D-C1 worker outputs
are present. Staging is empty. The full status is captured again immediately
before the final active-work-order gate.

## Changed Files

- `scripts/acel_g1_party_c_group4_registry_writer.ps1` - principal/path-bound,
  initial-create-only captured-byte registry transaction and 53-check self-test.
- `scripts/acel_g1_party_b_group4_lookup_response_writer.ps1` - response-log
  initializer, idempotent guarded lookup wrapper, copy-on-write append and
  51-check self-test with actual concurrent/crashed append pipelines.
- `governance/compat/check_acel_g1_issuer_registry.py` - independent read-only
  schema/JCS/hash/snapshot/chain/identity/security checker and pure evaluator.
- `governance/compat/test_check_acel_g1_issuer_registry.py` - 82 disposable
  positive/adversarial, writer-process, rollback and non-mutation tests.
- `docs/reviews/CVF_ACEL_G1_T3D_C1_GROUP4_ISSUER_REGISTRY_LOOKUP_TOOLING_WORKER_RETURN_2026-09-22.md` - this canonical return.

The thirteen parked paths remain byte-identical, read-only and unstaged.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:

frictionLevel: MEDIUM

frictionType: HELPER_GAP

observedStep: repeated independent review showed historical durable rows need
the same deterministic outcome classifier as new preparation, and that safe
test-mode containment and create-only rollback require component walks and an
explicit successful-publication ownership marker.

preventiveControlCandidate: HELPER_DIAGNOSTIC

preventiveControlCandidateNote: restoration is gated by explicit acquisition,
pre-state and successful-publication markers; future high-risk writer self-tests should use
the complete production transaction in child processes, hard-kill barriers,
exception-safe temp helpers and exact arbitrary-descriptor restoration.

## Command Evidence

- pre-implementation autorun - 84/85; the sole failure is the work-order-documented three parked historical returns outside the active lane; no T3D-C1 finding.
- `python -m py_compile governance/compat/check_acel_g1_issuer_registry.py governance/compat/test_check_acel_g1_issuer_registry.py` - PASS.
- `python -m pytest governance/compat/test_check_acel_g1_issuer_registry.py -q` - PASS: 82 passed.
- `python governance/compat/check_acel_g1_issuer_registry.py --self-test` - PASS: 9 checks, sourceMutation false.
- Party C writer `-SelfTest` - PASS: 53 executable checks, component-contained validated production publish peers, same-target post-failure acquisition, create-race preservation, three hard-kill recovery barriers, sourceMutation false.
- Party B writer `-SelfTest` - PASS: 51 executable checks, actual concurrent/idempotent and post-failure successor production append, create-race preservation, three production-append hard-kill recovery barriers, exact reachable adversarial descriptor rollback, prestate security rejection, sourceMutation false.
- `git diff --check` - PASS when the final command sequence completes.
- active-work-order worker-return fast gate - PASS when the content-frozen final command exits zero.
- final return SHA-256 binding - PASS when externally captured pre/post digests match; the digest is not self-embedded and no later edit is permitted.

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored throughout worker execution: staging remains
empty and no commit was created. Local reviewer/closer owns any accepted
material and continuity commits.
