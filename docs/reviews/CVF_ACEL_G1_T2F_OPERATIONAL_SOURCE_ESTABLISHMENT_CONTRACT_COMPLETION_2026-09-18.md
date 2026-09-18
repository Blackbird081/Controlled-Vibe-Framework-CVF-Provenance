# CVF ACEL G1 T2F Operational Source Establishment Contract Completion Review

Memory class: governed-completion-review

docType: completion_review

Status: REWORK_REQUIRED_CONSOLIDATED_R1

Date: 2026-09-18

Batch ID: ACEL-G1-T2F-OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT-R1-REVIEW

Review base HEAD: `bcc346d0c15f5270ec350736b6407f72023650ef`

Decision owner: Local orchestrator/reviewer

Review-Cost Telemetry: REQUIRED

## Purpose

Independently evaluate the two uncommitted T2F worker outputs against the
committed baseline, work order, T2E source-owner contract and T2C verifier
consumer contract. Preserve valid returned evidence, consolidate every known
dependent design defect before repair and decide whether the return is
acceptable, locally repairable or requires one worker R1.

## Target / Source

| Artifact | Identity / role | Review use |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | worker output SHA-256 `eb169f99a39d43050e15102c7bcdc2294a274b1cde524fcc23f261e4101e38e6` | proposed integrated source contract |
| `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md` | worker output SHA-256 `8735b7b7c5874e30219fd55599d5f6af508caf9d81cc19e87d535792f512fbb4` | returned scope, hashes and gate evidence |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | material dispatch `1909c5a72` | acceptance and evidence contract |
| `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | accepted T2E design input | source-owner and independence requirements |
| `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | accepted hypothetical consumer contract | exact key-registry, observation and lookup joins |

## Scope / Methodology

Applied `EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION`. Local
consumed the worker's valid command evidence, independently reconciled the
13-path SHA-256 ledger, ran the reviewer-return steward preflight once and
performed focused contradiction checks only where the proposed schemas join
the accepted T2C consumer. No broad source scan, implementation, provider/live
call, credential access, key action, registry creation, public sync or
deployment occurred.

The single-pass matrix covered contract/schema fields, authority and source
claims, path boundaries, negative cases, consumer joins, verification
evidence, closure range and commit choreography before any repair dispatch.

## Reviewer Dependency-Closure Matrix

| Area | Returned evidence | Result | Disposition |
|---|---|---|---|
| exact worker manifest | two required T2F outputs plus thirteen pre-existing parked paths; staging empty | PASS | preserve |
| frozen-path integrity | worker ledger recomputed 13/13; Local found 13/13 exact matches | PASS | preserve |
| role/authority separation | Parties A/B/C and activation approver remain distinct as appointed | PASS | preserve |
| source-existence boundary | every group remains `SOURCE_NOT_CREATED`; admission remains `UNVERIFIED` | PASS | preserve |
| canonical hash contract | Group 1/3 use an underspecified serializer and Group 3 hashes a row containing its own hash | FAIL | R1-01 |
| schema/version/receipt completeness | fields consumed later are absent from their declared schemas; Group 1 lifecycle receipt has no exact source contract | FAIL | R1-02 |
| T2C consumer joins | observation records cannot provide `snapshotId`, `snapshot_content`, `authority` or `observedAt`; key-role and issuer lookup bindings are incomplete | FAIL | R1-03 |
| activation conflict semantics | automatic most-recent-approved activation contradicts conflict rejection and independent explicit activation | FAIL | R1-04 |
| proposed-path collision evidence | generic tranche-token search does not test any proposed operational path or path-family collision | FAIL | R1-05 |
| tests/gates | return-shape and reviewer-fast gates pass, but those gates do not prove semantic contract coherence | PASS_BOUNDED | consume without overclaim |
| closure range | worker outputs remain uncommitted; proposed R1 may modify only those same two paths | CLOSEABLE | one consolidated R1 |
| commit choreography | one material dispatch/review commit then one continuity commit | CLOSEABLE | Local commit owner |

## Findings / Position

### T2F-R1-01 - Canonical Hash Profile Is Ambiguous And Self-Referential - HIGH

Groups 1 and 3 specify "UTF-8 JSON serialization with sorted keys" rather
than the RFC 8785 JCS profile already fixed by T2C. That leaves string,
number, array and nested-object encoding underdetermined. More critically,
Group 3 declares `entryHashHex` as a required row field and then defines
`entryHashHex` as the hash of the current row's canonical bytes plus the prior
hash. The hash field is therefore inside its own preimage and cannot be
recomputed as written. The design also omits explicit domain separation,
profile version, prior-hash field and unambiguous preimage framing.

### T2F-R1-02 - Declared Schemas Do Not Carry Their Own Version And Receipt Contracts - HIGH

Group 1 later relies on `registrySnapshotVersion`, `writeTimestamp`, row hash,
role authorization, duplicate-key/public-key-alias rejection and a lifecycle
log, but those fields and the lifecycle-receipt path/schema are absent from
the declared registry schema. Group 4 later relies on `entryVersion` and an
observed registry snapshot, but its registry schema declares neither a global
snapshot identity/version nor a snapshot hash. Its lookup-response rows lack
the registry snapshot, result enum, error/ambiguity outcome, entry version,
observation binding and response integrity fields needed to be durable proof.

### T2F-R1-03 - The Proposed Sources Cannot Satisfy The Accepted T2C Consumer - CRITICAL

T2C calls `sourceObservationLog.lookup(snapshotId)` and then consumes
`observation.snapshot_content`, `observation.observedAt` and
`observation.authority`, verifies the snapshot hash, checks temporal order and
passes the snapshot content to `sourceRegistry.lookup(...)`. The Group 3 row
schema provides none of those four values and defines no immutable snapshot
artifact reference. Its correction rule also permits multiple records while
T2C rejects more than one unresolved observation for a snapshot; active-head
and fork semantics are not reconciled. Group 1 omits the key role binding T2C
requires for `verificationAuthority`, and Group 4's durable response cannot
be joined back to the exact observed snapshot.

### T2F-R1-04 - Automatic Latest-Wins Activation Contradicts Fail-Closed Conflict Handling - HIGH

Group 2 says the "most recent approved" version becomes active, while the
Negative Cases table rejects automatic latest-wins resolution when versions
conflict. The decision schema has no explicit event type for activation or
supersession, no unique-active invariant and no deterministic conflict rule.
Approval and activation are therefore conflated despite the separately
appointed activation authority.

### T2F-R1-05 - Proposed Operational Paths Were Not Collision-Checked - MEDIUM

The worker reran the dispatch packet's tranche-token query. That query cannot
find collisions for `governance/sources/verifier_key_registry/REGISTRY.json`,
the specification family, observation store, issuer registry or receipt-log
paths because none of those path strings is in its search expression. The
required proposed-path collision ledger is absent, so the "proposed exact
future path" claim has not received its required evidence.

## Accepted Returned Evidence

| Evidence | Local disposition |
|---|---|
| correct `executionBaseHead`, unchanged HEAD, empty staging and no worker commit | ACCEPT |
| exact two worker-owned outputs | ACCEPT |
| thirteen parked paths present and byte-identical to the worker ledger | ACCEPT |
| all four source groups remain uncreated and candidate admission unverified | ACCEPT |
| accountable-party and forbidden-role matrix | ACCEPT |
| no provider, network, credential, key, runtime, public or deployment effect | ACCEPT |
| return-shape, pre-implementation and reviewer-fast machine evidence | ACCEPT_AS_SHAPE_EVIDENCE_ONLY |
| proposed paths, schemas, hashes and consumer joins | REWORK_REQUIRED |

## Decision / Disposition

Reviewer verdict: `REWORK_REQUIRED_CONSOLIDATED_R1`.

The return is not accepted as implementation authority or as a sufficiently
complete operational-source establishment contract. The defect set changes
architecture/schema design and consumer binding, so it is not a small,
fully-determined reviewer-local edit. One consolidated INTERNAL_AGENT R1 may
modify the same two uncommitted outputs in place. No new output, source,
implementation or successor tranche is opened.

## Risk / Corrective Action

The principal risk is that a machine-clean but internally non-recomputable
contract becomes implementation authority, causing future source writers and
consumers to implement incompatible hashes, snapshots and activation states.
The bounded corrective action is one consolidated R1 over the same two
documentation outputs, with exact consumer joins and negative probes fixed
before any proposed path may be cited by an implementation work order.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: INTERNAL_AGENT_CONSOLIDATED_R1

workerRedispatchAllowed: YES

The existing two-path ownership, no-commit rule, authority ceiling and
external-effect class are unchanged. All R1 repairs fit within the same two
documentation files. Local owns the review, dispatch artifacts, commits and
final disposition.

## Review Cost Telemetry And Stop Disposition

reviewRoundCount: 1

workerRepairTurnCount: 0

newRootCauseCountThisRound: 3

dependentFindingCountThisRound: 2

elapsedReviewMinutes: NOT_AVAILABLE_WITH_REASON: the interface exposes no reliable per-review wall-clock ledger

providerCallCount: 0

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: provider-neutral token accounting is unavailable

valueDelta: prevented a self-referential hash and non-joinable observation schema from becoming implementation authority; consolidated every known dependent defect before R1

stopDisposition: CONSOLIDATE_SINGLE_REPAIR

preRepairAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

materialCommitCount: 1

continuityCommitCount: 1

commitPlanDisposition: DEFAULT_ONE_MATERIAL_ONE_CONTINUITY

latencyDisposition: NOT_MEASURED_WITH_REASON: no reliable governed wall-clock source is exposed

avoidableDelayClass: NONE

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Finding-To-Governance Learning Disposition

| Finding cluster | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| incomplete consumer/schema dependency closure in the initial packet and return | `ORCHESTRATOR_PACKET_GAP` | `GOVERNANCE_CONTROL_PLANE` | `WORK_ORDER_UPDATED` | R1 freezes exact consumer-join and canonical-preimage obligations |
| self-referential and under-specified record hashes | `DESIGN_DEFECT` | `GOVERNANCE_CONTROL_PLANE` | `REGRESSION_REQUIRED` | R1 requires independently recomputable positive and mutation probes |
| generic token search used as operational-path collision evidence | `EVIDENCE_INTERPRETATION_ERROR` | `GOVERNANCE_CONTROL_PLANE` | `WORK_ORDER_UPDATED` | R1 requires literal per-path and family collision ledger |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | completion-review declaration; review-cost scalar fields and enums; structural review headings; finding defect-class vocabulary; trace labels; private export token |
| gateRunPurpose | confirm review and R1 dispatch shape after semantic inspection, not discover semantic defects |
| claimBoundary | machine conformity cannot accept the returned design |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | T2F initial worker-return review, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, SHA-256 reconciliation, focused contract joins, reviewer-return preflight, apply_patch and governance gates |
| Target paths | two returned T2F outputs read-only during review; this review and paired R1 dispatch artifacts authored by Local |
| Allowed scope source | committed T2F work order plus standing operator instruction to continue orchestration/review |
| Before status evidence | HEAD `bcc346d0c`; two T2F outputs and thirteen parked paths untracked; staging empty |
| After status evidence | consolidated five-finding R1 decision; worker outputs remain uncommitted and unchanged pending R1 |
| Diff evidence | Local staging is restricted to this review and paired R1 dispatch packet; worker/parked paths excluded |
| Approval boundary | review rejection and one documentation-only R1 dispatch |
| Claim boundary | no source, key, credential, implementation, live/runtime/public/deploy effect |
| Agent type | Local orchestrator/reviewer and commit owner |
| Invocation ID | `acel-g1-t2f-initial-return-review-20260918` |
| Expected manifest | this review plus paired R1 baseline and work order |
| Actual changed set | reconciled before material commit |
| Manifest delta | pending exact staging reconciliation |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | independent review and consolidated documentation-only R1 dispatch |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | `CVF_RECEIPT_PRESENT`: worker hashes, status and machine evidence consumed; no runtime/source receipt claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Local review and dispatch authoring only |
| invocationBoundary | private local repository; no provider or external-agent invocation |
| interceptionBoundary | no runtime, IDE, CLI-worker or MCP interception claim |
| claimLanguage | worker evidence accepted where valid; source-contract design rejected pending R1 |
| forbiddenExpansion | source creation, key/credential action, implementation, live lookup, admission, runtime, public sync, deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Chain map route | committed T2F packet -> INTERNAL_AGENT return -> Local review -> one internal R1 |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this Local review and paired R1 work order |
| Internal source | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source intake |
| Claim boundary | shared-workspace provider identity does not change INTERNAL_AGENT status or Local decision ownership |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Expected Result / Prediction: the initial return should define four
recomputable source contracts that join the accepted T2C consumer without
claiming source existence.

Evidence Comparison Requirement: scope and authority boundaries passed, but
the canonical preimages, declared schemas, observation/lookup joins,
activation state and collision evidence fail the dependency matrix above.

Contradiction Or Gap Disposition: reject acceptance, preserve valid evidence
and issue one consolidated R1 within the unchanged documentation-only scope.

Claim Update Requirement: the two outputs remain proposed evidence pending
R1; no proposed path or schema is accepted implementation authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private rejected-return review and internal rework dispatch; no public
export authority exists.

## Claim Boundary

This review rejects the initial contract as incomplete and authorizes only one
consolidated documentation repair. It does not modify or create operational
sources, approve proposed paths, open implementation, perform a live lookup,
admit a candidate, or make runtime/public/deployment claims.
