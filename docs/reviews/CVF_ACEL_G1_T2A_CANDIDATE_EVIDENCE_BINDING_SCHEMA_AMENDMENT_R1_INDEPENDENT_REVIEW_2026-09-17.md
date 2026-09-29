# CVF ACEL G1 T2A Candidate Evidence Binding Schema Amendment R1 Independent Review

Memory class: governed-review

docType: review

Status: REVIEW_REWORK_REQUIRED

Date: 2026-09-17

Batch ID: ACEL-G1-T2A-CANDIDATE-EVIDENCE-BINDING-SCHEMA-AMENDMENT

Review disposition: `REWORK_REQUIRED_CONSOLIDATED_R1`

## Purpose

Independently review the three uncommitted T2A schema-amendment outputs against
the governing work order, accepted T1 design, R2 rejection, and current local
repository evidence. This review accepts valid integrity evidence without
recreating implementation and consolidates all currently known semantic defects
before one bounded R1 repair.

## Target / Source

| Source | Role | Review use |
|---|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md` | governing contract | eight acceptance criteria and exact three-path scope |
| `docs/reviews/CVF_ACEL_G1_T2_R2_INDEPENDENT_REVIEW_2026-09-17.md` | rejection authority | F1-F4 counterexamples and reopen requirements |
| `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` | unchanged design authority | fixture-set, comparability and provenance baseline |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md` | returned human design | semantic review target |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json` | returned machine design | parity and exact-schema target |
| `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md` | returned evidence | integrity, gate and convergence claims |

Provider-local memory and the worker's narrative about tool use or internal
reasoning are `NOT_CVF_SOURCE`. Only repository artifacts and observable Git/
checker evidence are used for disposition.

## Scope / Methodology

Read all three returned artifacts, compared their field and rule claims, checked
all seven frozen-path SHA-256 values against the work order and return ledger,
parsed the JSON, and performed focused contradiction searches over coverage,
extra-fixture behavior, canonicalization, invalidation mapping, parity, SCEC
authority and gate receipts. No TypeScript/Python implementation was changed or
rerun because this tranche is design-only and semantic contradictions already
determine the R1 disposition.

## Findings / Position

### R1-RV-F1 - Required Fixture-Set Authority And Coverage Remain Undefined - CRITICAL

The new `requiredFixtureEvidenceSet` is a candidate-local collection, but the
schema does not define the authoritative required fixture-set descriptor or an
exact membership comparison. It refers to a task-class-bound declaration while
providing no normalized required member list, required-set identity/content
hash recomputation, or equality edge proving the candidate covers exactly that
set. Therefore the design cannot distinguish a missing required fixture from an
extra fixture by schema evidence.

The returned rules also contradict each other: audit lines 150-158 and manifest
`perFixtureBoundRequirement` say every entry must reach `PASS_WITH_EVIDENCE` and
one failing entry blocks the whole candidate, while audit lines 171-177 and the
manifest's `extra_unrequired_fixture_fails` case say a failing extra is excluded
and does not block. Acceptance criteria 1 and 3 are not satisfied.

### R1-RV-F2 - Cross-Candidate Reuse Is An Enforcement Invariant, Not Structurally Impossible - HIGH

Nesting evidence under a candidate does not make pooling impossible: a future
implementation can still iterate across candidate envelopes and construct a
round-level pool. The audit's own risk table admits that a schema document
cannot force future code structure. The correct claim is a mandatory
TypeScript decision-owner invariant with an exact per-candidate evaluation
boundary and negative regression, unless a future executable API type truly
makes cross-candidate access impossible. The current structural-impossibility
claim overstates what this documentation schema proves.

### R1-RV-F3 - Nested Provenance Components Are Not Canonically Recomputable - HIGH

The top-level ten-component list uses length-prefixing, but three new digest
components remain underspecified:

- `acceptedCandidateReceiptHash` does not state the exact receipt fields,
  receipt-content binding, normalization, item ordering or duplicate behavior;
- `acceptedCandidateTraceBindingHash` does not state the complete nested
  fixture/trace ordering and canonical serialization;
- `preferenceValueDigest` does not define the allowed numeric domain and exact
  decimal normalization (`-0`, exponent form, non-finite values and equivalent
  textual representations).

`orderedEvidenceEnvelopeHashes` is named as envelope hashes but is defined as a
flattened pair of existing hashes and does not directly bind fixture ID/class or
the complete envelope. This does not yet meet the work order's complete,
versioned, typed, independently recomputable preimage requirement.

### R1-RV-F4 - Two Declared Invalidation Triggers Are Not Provenance-Bound - HIGH

Acceptance criterion 5 requires every declared invalidation trigger to map to
provenance-bound content. The human and JSON designs explicitly leave provider
lane readiness and budget-ceiling invalidation as later eligibility
re-evaluation, not provenance-hashed content, while self-assessing criterion 5
as PASS. The amended binding must record canonical readiness and budget
snapshot/digest inputs, or another exact provenance-bound representation, so a
change is detectable against the persisted binding.

### R1-RV-F5 - Human/JSON Parity And Review Authority Are Overclaimed - HIGH

The human owner table says `recompute(all nine preimage components)` while the
human list and JSON manifest define ten. More importantly, the worker-return
SCEC marks four blockers resolved with `evidenceClass: ACCEPTED_REVIEW` pointing
to the worker-authored audit before any Local acceptance exists. A worker cannot
self-create accepted-review authority. For the R1 return, the four blockers must
remain current/retained with no false resolution evidence; a later Local
completion review may resolve them if the repaired design passes.

### R1-RV-F6 - Worker-Return Fast-Gate Receipt Is Incomplete - MEDIUM

The return claims the required fast gate but its dedicated section says the
actual output is in an accompanying live command and provides neither the
reported `68/68` summary nor a complete command result. Repository evidence must
carry the exact observed terminal result; the operator's relayed statement is
not a substitute. Repair the return with the actual command, count, disposition
and any scope reconciliation.

## Accepted Returned Evidence

| Item | Disposition |
|---|---|
| exactly three new worker-owned paths; staging empty; HEAD unchanged during worker execution | ACCEPT |
| seven frozen paths byte-identical to the worker start ledger; four dispatch-pinned hashes also match | ACCEPT |
| GC-026 duplicate outer fields removed in favor of hashed inner record as the single source of record/time | ACCEPT_BOUNDED |
| registry-snapshot honesty statement | ACCEPT |
| migration dispositions for seven rejected paths | ACCEPT_BOUNDED; retain while repairing terminology and successor references |
| JSON syntax and structural gate evidence | ACCEPT_AS_SHAPE_EVIDENCE_ONLY |
| no implementation/provider/live/runtime/configuration/G4 authority | ACCEPT |

## Acceptance Resolution

| Work-order criterion | Result |
|---|---|
| 1. human/JSON parity | FAIL_R1_RV_F1_F5 |
| 2. each R2 finding maps to rule/regression | PASS_BOUNDED |
| 3. same candidate covers every required fixture | FAIL_R1_RV_F1_F2 |
| 4. GC-026 contradiction impossible or rejected | PASS |
| 5. every invalidation trigger provenance-bound | FAIL_R1_RV_F4 |
| 6. independent recomputation, not shape-only | FAIL_R1_RV_F3 |
| 7. frozen paths/exact three outputs/no commit | PASS |
| 8. gates pass or truthful block | FAIL_R1_RV_F5_F6 |

## Consolidated R1 Repair Contract

Repair only the same three T2A worker outputs. Do not create a fourth worker
artifact, edit any frozen G1 T2 path, commit, or spawn a nested subagent.

1. Add one authoritative candidate-scoped required-fixture-set descriptor that
   binds task class, partition/comparability identity, exact canonical member
   identities/content hashes/classes and set content hash. Define exact coverage
   equality. Either forbid extras in the required set or place supplemental
   evidence in a separate field with non-contradictory semantics.
2. State cross-candidate non-pooling as an enforced decision-owner invariant,
   mandatory path and regression unless an executable type boundary truly makes
   it structurally impossible. Remove every unsupported structural-impossibility
   claim.
3. Define version/domain tags, exact fields, normalization, ordering, duplicate
   behavior and serialization for every nested digest. Bind complete fixture
   envelope identity, producer receipt identity and content, trace identity/
   capture mode/content and deterministic preference value.
4. Bind provider-lane readiness and budget snapshot/content into provenance so
   every declared invalidation trigger satisfies criterion 5.
5. Reconcile human and JSON field-for-field, including ten-versus-nine wording,
   negative cases, owner table, bypass and fail behavior.
6. Correct SCEC: do not cite worker-authored output as `ACCEPTED_REVIEW` or mark
   the four blockers resolved before Local review. Record R1 as rework with the
   blockers retained/current and increment the applicable correction counters.
7. Record the actual worker-return fast-gate terminal evidence in the return.
   Gate success remains shape evidence and cannot override this semantic review.

Return `COMPLETE_PENDING_REVIEW` only after all seven repairs reconcile across
the human audit, JSON manifest and worker return. Otherwise return
`BLOCKED_WITH_REASON`.

## Review Cost Telemetry And Stop Disposition

| Field | Value |
|---|---|
| reviewRoundCount | 1 for T2A |
| workerRepairTurnCount | 0 before this disposition |
| newRootCauseCountThisRound | 3: required-set authority, nested canonicalization, invalidation binding |
| dependentFindingCountThisRound | 3: structural overclaim, parity/SCEC authority, missing gate receipt |
| providerCallCount | 0 |
| tokenOrQuotaUsage | `NOT_AVAILABLE_WITH_REASON: provider-neutral usage telemetry is unavailable` |
| valueDelta | prevented a design artifact with unresolved coverage and provenance ambiguity from becoming the implementation root contract |
| stopDisposition | CONSOLIDATED_R1_REWORK_REQUIRED |
| preRepairAuditDisposition | COMPLETE_BEFORE_REPAIR |
| successorTrancheOpened | NO |

## Risk / Corrective Action

Accepting now would recreate the R2 failure mode at a higher authority layer:
green structural gates over a schema whose oracle and canonical preimage remain
ambiguous. The corrective action is one bounded R1 repair of the same three
uncommitted outputs. G1 implementation/R3, G4, calibration, provider/live,
runtime, public sync and deployment remain parked.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | allowed SCEC evidence classes; review structural headings; trace fields; Delta eight-field block; review-cost telemetry labels |
| gateRunPurpose | confirmation after semantic inspection, not first discovery; no checker is treated as proof of schema correctness |
| claimBoundary | focused checks cannot accept or repair the returned design |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | G1 T2A R1 independent review, 2026-09-17 |
| Working directory | repository root |
| Command or tool surface | direct reads, SHA-256, focused `rg`, JSON/source comparison, governed review checks |
| Target paths | exact three returned outputs, work order, R2 review, T1 manifest and seven frozen inputs |
| Allowed scope source | operator submitted `COMPLETE_PENDING_REVIEW`; governing work order assigns Local review |
| Before status evidence | HEAD `a14111e1e`; seven frozen plus three T2A outputs untracked; staging empty |
| After status evidence | one Local review artifact added; worker/frozen paths untouched; staging remains empty before Local commit choreography |
| Diff evidence | `git status --short`; exact hashes; review artifact diff |
| Approval boundary | review/rework disposition only |
| Claim boundary | no worker repair, implementation, provider/live, runtime or successor dispatch |
| Agent type | reviewer |
| Invocation ID | `acel-g1-t2a-r1-independent-review-20260917` |
| Expected manifest | one Local review artifact plus ten unchanged untracked worker/frozen paths |
| Actual changed set | same |
| Manifest delta | MATCH |

## Epistemic Process Block

- Expected Result / Prediction: the returned schema would either define exact
  candidate-scoped coverage and canonical recomputation or expose a bounded
  contradiction before implementation.
- Evidence Comparison: GC-026 and integrity evidence matched; focused comparison
  found coverage, canonicalization, invalidation and authority contradictions.
- Contradiction or Gap Disposition: consolidated into R1-RV-F1 through F6; no
  serial repair was attempted before completing the dependency sweep.
- Claim Update: `COMPLETE_PENDING_REVIEW` is rejected for now;
  `REWORK_REQUIRED_CONSOLIDATED_R1` replaces it.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | independent design review and consolidated R1 disposition |
| claimDisposition | CLAIM_REJECTED: schema acceptance and implementation readiness are not established |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no provider/runtime/calibration receipt is relevant or produced |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source comparison, exact hashes and focused contradiction evidence |
| invocationBoundary | local read-only review plus this review artifact |
| interceptionBoundary | no runtime/provider/worker interception |
| claimLanguage | returned integrity evidence accepted; semantic design requires bounded R1 repair |
| forbiddenExpansion | worker-output repair by reviewer, implementation, G4, live/provider, runtime, configuration mutation, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private review of rejected/uncommitted provenance artifacts; no public
export requested or authorized.

## Claim Boundary

This artifact records a Local `REWORK_REQUIRED_CONSOLIDATED_R1` disposition.
It does not modify or accept the three returned outputs, does not touch the
seven frozen G1 T2 paths, and does not authorize implementation or any external
effect. Final acceptance requires a repaired return and a later Local review.
