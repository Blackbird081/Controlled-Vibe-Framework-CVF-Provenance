# CVF ACEL G1 T2A Candidate Evidence Binding Schema Amendment R2 Independent Review

Status: REVIEW_REJECTED_STOP_REASSESS_ARCHITECTURE

Terminal disposition: `PARKED_ARCHITECTURE_REASSESSMENT_REQUIRED`

Memory class: FULL_RECORD

Date: 2026-09-17

Review base HEAD: `d68aece8212a0b7bca80ecf707db991a504418e1`

Decision owner: Local orchestrator/reviewer

## Purpose

Independently review the Consolidated R1 repair return for
`ACEL-G1-T2A-CANDIDATE-EVIDENCE-BINDING-SCHEMA-AMENDMENT` against the exact R1
repair contract, preserve valid returned evidence, and stop same-scope repair
when the chain's own semantic-convergence threshold requires architecture
reassessment.

## Target / Source

Primary returned artifacts:

- `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md`
- `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json`
- `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md`

Review authority:

- `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_R1_INDEPENDENT_REVIEW_2026-09-17.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md`
- accepted G1 T1 design and Local G1 T2 R2 rejection named by those artifacts

## Scope / Methodology

Local consumed the returned hashes and command evidence, verified the seven
frozen paths byte-for-byte, parsed the JSON, compared the human/JSON topology,
and ran contradiction probes only at the four remaining semantic boundaries.
No implementation, provider/live call, real calibration, configuration
mutation, G4 work, runtime wiring, public sync or deployment was performed.

This is a review of returned evidence, not a recreation of the worker's design.
The worker narrative and `COMPLETE_PENDING_REVIEW` label are not acceptance
evidence.

## Findings / Position

### R2-RV-F1 - Required-Set Topology Violates The Exact R1 Repair Contract - CRITICAL

The R1 contract required one authoritative candidate-scoped descriptor binding
task class, partition/comparability identity, exact canonical members and set
hash. It also required either forbidding extras in the required set or moving
supplemental evidence to a separate field.

The repair instead defines `RequiredFixtureSetDeclaration` as round-scoped
(human lines 149-168), with only `taskClassId`, `fixtureSetContentHash` and
`requiredMembers`; it does not carry partition or comparability identity. It
then keeps extras inside the field named `requiredFixtureEvidenceSet` and
allows failing extras to be excluded without blocking the candidate (human
lines 238-248; JSON negative cases). This is neither allowed R1 topology.

The result improves missing-member detection but does not satisfy the selected
root-contract boundary. The authority that creates and freezes the declaration
also remains unnamed; saying an individual candidate does not author it does
not identify the authoritative owner or bind it to the predeclared HELD_OUT
membership ledger.

### R2-RV-F2 - Canonical Serialization Remains Ambiguous And Has A Concrete Collision - HIGH

`RequiredFixtureSetDeclaration.fixtureSetContentHash` is specified only as
`recompute(sort(requiredMembers by fixtureId) then hash)` (human line 156 and
JSON equivalent). Exact member-field order, per-member serialization, domain
tag, duplicate behavior and outer-list serialization are not defined, so the
claimed `BOTH_INDEPENDENT` recomputation edge has no single algorithm.

The receipt digest also serializes `traceIds` as one comma-joined string before
length-prefixing that whole string (human lines 458-478). With no comma
restriction or escaping rule for `traceId`, `['a,b','c']` and `['a','b,c']`
both canonicalize to `a,b,c`. Distinct receipt content can therefore produce
the same declared preimage without a SHA-256 collision. The outer provenance
preimage likewise does not define how the `canonicalHash[]` component is
serialized into its one length-prefixed component. Acceptance criteria 1 and
6 remain open.

### R2-RV-F3 - Current-State Invalidation Is Not Bound By An Accept-Time Snapshot - HIGH

The new eligibility snapshot binds the accept-time readiness and budget triple,
which is useful audit evidence. It does not bind a later readiness downgrade or
budget-ceiling change. The design explicitly says the snapshot is never
compared with current state (human lines 577-588), while also claiming every
trigger's change provably alters provenance (lines 590-604).

A later external/current-state change cannot alter an immutable historical
fingerprint. The architecture must distinguish acceptance provenance from a
persisted re-evaluation/invalidation receipt, including the current-state
source and comparison result. Mapping a future trigger to an old snapshot field
does not make the future event provenance-bound or detectable against the
persisted binding. Acceptance criterion 5 remains open.

### R2-RV-F4 - Required Gate Failure Was Disclosed But The Terminal Label Was Wrong - MEDIUM

The return truthfully records that pre-implementation and reviewer-fast did not
pass because Local commits advanced HEAD and the active-handoff marker became
stale. Attribution as `CONCURRENT_OUT_OF_SCOPE` is accepted, and Local repaired
its own continuity defect separately at `d68aece82`.

However, the work order and R1 repair contract require gates to pass or the
return to be truthfully blocked. A disclosed `67/68` violation does not support
`COMPLETE_PENDING_REVIEW`; the correct worker terminal state at return time was
`BLOCKED_WITH_REASON`. Local's later continuity repair does not retroactively
turn the recorded worker run into a pass.

## Accepted Returned Evidence

| Evidence | Review disposition |
|---|---|
| Exactly three worker-owned T2A outputs; staging empty; worker made no commit or nested delegation | ACCEPT |
| Seven rejected G1 T2 paths retain their dispatch-pinned SHA-256 values | ACCEPT |
| GC-026 single-source topology and removal of unsupported cross-candidate structural-impossibility language | ACCEPT |
| Cross-candidate non-pooling is now stated as a mandatory decision-owner invariant plus regression | ACCEPT_AS_DESIGN_DIRECTION |
| SCEC no longer self-creates `ACCEPTED_REVIEW`; blockers remain current and correction counters advance | ACCEPT |
| Gate failure and concurrent scope are reported rather than rewritten as PASS | ACCEPT_EVIDENCE, REJECT_TERMINAL_LABEL |
| Provider/live, runtime, implementation, G4, public and deployment claims remain excluded | ACCEPT |

## Acceptance Resolution

| Criterion | Result |
|---|---|
| 1. Human/JSON topology and canonicalization parity | FAIL_R2_RV_F1_F2 |
| 2. R2 findings map to design rules and future regressions | PARTIAL_PASS_NO_CLOSURE |
| 3. Same candidate covers every authoritative required fixture | FAIL_R2_RV_F1 |
| 4. GC-026 contradiction impossible or rejected | PASS |
| 5. Every invalidation trigger maps to provenance-bound content | FAIL_R2_RV_F3 |
| 6. Checker responsibility independently recomputable | FAIL_R2_RV_F2 |
| 7. Frozen paths and exact worker scope | PASS |
| 8. Gates pass or return is truthfully blocked | FAIL_R2_RV_F4 |

The return is not accepted as the future implementation root contract.

## Architecture Reassessment Requirement

Do not dispatch another repair of the same three artifacts. The worker's own
SCEC correctly reaches `STOP_REASSESS_ARCHITECTURE` after two non-decreasing
blocker transitions. Local accepts that escalation.

A future Local decision may open a new root-contract tranche only after choosing:

1. one fixture-authority owner and immutable HELD_OUT declaration that binds
   task class, partition/comparability and exact canonical members;
2. separate `requiredEvidence` and optional `supplementalEvidence` collections,
   or an explicit no-extras invariant;
3. one reusable typed canonical serialization primitive for every scalar,
   tuple and list, rather than field-local delimiter conventions; and
4. separate immutable acceptance provenance from later invalidation-event
   evidence and current-state re-evaluation.

The seven rejected implementation paths and three T2A worker outputs remain
uncommitted evidence. G1 implementation/R3, G4 implementation/experiment,
real calibration, provider/live, configuration mutation, Core runtime, package
lifecycle, public sync and deployment remain parked.

## Review Cost Telemetry And Stop Disposition

| Field | Value |
|---|---|
| reviewRoundCount | 2 for T2A |
| workerRepairTurnCount | 1 consolidated R1 repair |
| newRootCauseCountThisRound | 2: required-set authority topology; invalidation event/provenance separation |
| dependentFindingCountThisRound | 2: canonical serialization collision; incorrect gate terminal label |
| providerCallCount | 0 |
| tokenOrQuotaUsage | `NOT_AVAILABLE_WITH_REASON: provider-neutral usage telemetry is unavailable` |
| valueDelta | prevented an ambiguous root contract from authorizing another implementation/rework cycle |
| stopDisposition | `STOP_REASSESS_ARCHITECTURE_ACCEPTED_AND_PARKED` |
| successorTrancheOpened | NO |

## Risk / Corrective Action

Another same-scope repair would continue local patching of a root contract whose
fixture authority, serialization primitive and time-varying invalidation model
are not yet composed. The bounded corrective action is to park the returned
artifacts and require a fresh Local architecture choice before any successor.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | SCEC stop threshold; review structural headings; trace fields; Delta eight-field block; review-cost telemetry labels |
| gateRunPurpose | confirmation after semantic contradiction probes, not first discovery |
| claimBoundary | machine gates prove artifact conformance, not correctness of the proposed root contract |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | G1 T2A Consolidated R1 return review, 2026-09-17 |
| Working directory | repository root |
| Command or tool surface | governed reads, SHA-256 reconciliation, JSON parse, focused text probes, apply_patch and review gates |
| Target paths | three returned T2A outputs read-only; this independent review authored |
| Allowed scope source | governing work order plus operator return for review |
| Before status evidence | HEAD `183f26fea`; ten untracked worker/frozen evidence paths; staging empty |
| After status evidence | Local continuity defect corrected at `d68aece82`; independent review pending material commit |
| Diff evidence | this review only; worker artifacts and frozen inputs remain untracked |
| Approval boundary | Local review/disposition and commit only |
| Claim boundary | no implementation, provider/live, runtime, G4, public or deployment effect |
| Agent type | reviewer/closer |
| Invocation ID | `acel-g1-t2a-r2-independent-review-20260917` |
| Expected manifest | one Local review path |
| Actual changed set | one Local review path |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Epistemic Process Block

- Expected Result / Prediction: the R1 repair should close the six prior
  findings without changing the exact selected topology.
- Evidence Comparison: frozen-scope, SCEC and non-pooling corrections held;
  focused comparison found the descriptor/extras topology did not implement
  the R1 contract, and canonical/invalidation claims remain stronger than their
  algorithms.
- Contradiction or Gap Disposition: reject the root-contract claim, preserve
  useful repairs as advisory design evidence, accept the worker's own
  `STOP_REASSESS_ARCHITECTURE` escalation and park same-scope rework.
- Claim Update: the return is bounded evidence, not an accepted schema or
  implementation authority.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | independent review, terminal rejection and parking only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: review evidence and stop disposition only |
| receiptEvidence | CVF_RECEIPT_PRESENT: worker hashes/commands consumed; Local focused contradiction evidence recorded here |
| actionEvidence | ACTION_EVIDENCE_PRESENT: review artifact and separate Local continuity correction only |
| invocationBoundary | private repository; no provider or external invocation |
| interceptionBoundary | no runtime, CLI-worker, OS or MCP interception claim |
| claimLanguage | returned design rejected; architecture reassessment required before successor |
| forbiddenExpansion | same-scope redispatch, implementation, G4, live calibration, runtime, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance review with rejected implementation paths and
repository-internal contradiction evidence; no public export was requested.

## Claim Boundary

This review rejects and parks the returned schema as a root contract. It does
not reject every design idea in the return, attribute the failure to Claude or
any model, prove a model-quality ranking, modify the ten untracked evidence
paths, authorize another worker repair, or open implementation, G4, live,
runtime, public-sync or deployment work.
