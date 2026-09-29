# CVF ACEL G1 T1 Empirical Calibration Owner Composition Design

Memory class: governed-worker-audit

docType: audit

Status: COMPLETE_PENDING_REVIEW

Batch ID: ACEL-G1-T1-EMPIRICAL-CALIBRATION-OWNER-COMPOSITION-DESIGN

executionBaseHead: `ff7a0ed68e5b2cdcd6e40f4477903ee7a4bac5b6`

Manifest: `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`

## Purpose

Design, on paper only, the CVF-native owner composition that closes the
documented G1 gap: `task class -> candidate configuration set -> comparable
measured evaluation -> bounded operating-point decision ->
regression/invalidation`. This audit decides whether to reuse/extend existing
CVF owners (benchmark harness, G3 behavioral evaluation, direct candidate
calibration, provider-lane readiness) into one coherent owner, or to block/
reject. No code is written or executed, no provider is called, no benchmark
is run, and no configuration is mutated by this tranche.

## Target / Source

Ten current private-CVF sources read and hashed completely at
`executionBaseHead`. Full ledger in the machine manifest; summary here.

| # | Path | SHA-256 | Status |
|---|---|---|---|
| 1 | `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md` | `107808cde5991393786949a9b7a2bae4c40b53620342bd181791031c69729cae` | READ |
| 2 | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_2026-09-15.md` | `5073932e1bcb18754ff914003b1bbac80037dad2b7599b50c29fb497f2eea39a` | READ |
| 3 | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_EVIDENCE_T0_2026-09-15.json` | `a1ec2a5ce31e15dc5ca369c0b9587c7a61f54a517f1439355bd6f49b5caaefe3` | READ |
| 4 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/performance.benchmark.harness.contract.ts` | `c95914c1cd541a6f6cd95af91b7c145830c12cfb78aa3ccc06a9742ce2a9ea51` | READ |
| 5 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/performance.benchmark.harness.contract.test.ts` | `0a57107408356853da407b6fa20b5ae30d25bf4b5afa07fe88107647066a9840` | READ |
| 6 | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts` | `2592fe83e73746c88b09b87fbddac3f511b5d9f05663687f9a1f08028742cb18` | READ |
| 7 | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts` | `9d25bcf04bb035a6d756a124829bf70f9893482f8a0727b038f1d1af9204fcb4` | READ |
| 8 | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts` | `83201e79a1172e50bcaaecd444b3dc5c7709658f0a83256f1c7d23b5cfd659cd` | READ |
| 9 | `docs/reviews/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_COMPLETION_2026-09-16.md` | `b5172077f17ac11b28677c00ccefc6864332ef42e5545e61e72bf1fd6e4c30af` | READ |
| 10 | `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | `c7a2ece2ccabdf4d74423b8ddbec6c688558e6f04c2f2cba152a9eaf24169460` | READ |

Sources 2 and 3 hashes exactly match the values already cited by the G1 T1
baseline's Source Verification Block and the T0 completion review
(`5073932e1...` and `a1ec2a5ce...`), confirming no drift since T0 acceptance.
Source 8 hash exactly matches the G3 T2 completion review's cited final
SHA-256 (`83201e79a...`), confirming the G3 grader consumed here is the
closed, accepted `CLOSED_PASS_BOUNDED_G3_PARKED` version, not a stale draft.

Full path/hash/status/extracted-fact/claim-ID ledger: see manifest `ledger`
array (ten rows, `G1T1-L01`..`G1T1-L10`).

## Scope / Methodology

Read-only design audit. Every one of the ten sources was read in full (not
sampled) and hashed with a direct SHA-256 file digest (not `git hash-object`).
No experiment, benchmark run, provider call, or configuration mutation
occurred. The design re-evaluates G1-C1..C3 (the three G1 claims accepted at
T0) against the current byte-identical sources, then composes an owner graph,
a closed-loop contract, decision-state machine, negative-case table,
provenance/invalidation rule, and an exact successor manifest, per the work
order's Evidence Requirements section.

Role: `INTERNAL_AGENT` design and source-verification worker. Phase: offline
owner-composition design. Decision owner: Local reviewer/closer.

## G1-C1..C3 Reconciliation And Freshness Delta

| Claim | T0 disposition | Current-source check | Freshness delta |
|---|---|---|---|
| G1-C1 (performance thresholds are PROPOSAL ONLY pending GC-026 promotion) | ADAPT, HIGH | Source 4 `EvidenceClass` type is still locked to the single literal `"PROPOSAL_ONLY"` (line 42); the module comment at lines 4-7 still states "no path to baseline truth within this contract" | NONE |
| G1-C2 (provider-lane canary calibrates lane availability, not task-class configuration selection) | ADAPT, HIGH | Source 10 confirms `CANARY_PASS`/`CERTIFIED` remain lane-level (`qwen-flash` `EXPERIMENTAL`, `deepseek-chat` `CERTIFIED`); its own Claim Boundary states "Multi-provider operability is proven. Provider parity is not claimed" | NONE |
| G1-C3 (benchmark harness has no consumer that reads a report to select a configuration) | ADAPT, HIGH | Source 4/5 confirm `generateReport` always returns `evidenceClass: "PROPOSAL_ONLY"` (line 283) and no `BenchmarkReport` field or export exists that a selection function could consume; all 60+ test cases in source 5 test lifecycle transitions only, none test configuration selection | NONE |

All three G1 claims are unchanged at current source. No new counter-evidence
was found. This confirms the T0 gap is still open and the design contract may
proceed on the accepted `ADAPT` basis.

## New Evidence Found During This Design Pass (Not In T0 Ledger)

Two current-source facts materially inform the design and were not part of
the original six-gap T0 ledger, because T0 scoped to G1-G6 gap existence, not
G1's later composition design:

- **G3 (source 8) already implements almost exactly the fixture/trace/
  evidence primitives G1 needs**: `BehavioralFixture` (identity, repeat
  policy, baseline role), `BehavioralTrace` (capture mode, provenance,
  outcome values), `admitBaselinePair` (WITH/WITHOUT equal-input-bytes
  pairing, fail-closed on `MISSING_PAIR`/`SAME_ROLE_PAIR`/
  `NONEQUIVALENT_INPUT_BYTES`), `admitFixtureSet` (positive+negative
  admission), and `gradeBehavioralEvaluation`'s repeat-count enforcement
  (`repeatsRequired` exactly 1 for `DETERMINISTIC`, exactly 3 for
  `STOCHASTIC`, with `INSUFFICIENT_REPEAT_EVIDENCE` on partial runs). This
  is a stronger, more directly reusable primitive set for G1's comparability/
  holdout/repeat semantics than the T0 audit's G1 section identified, because
  G3 did not exist as an accepted artifact until 2026-09-16 (T0 predates it
  by one day).
- **`evaluateHarderCandidate` (source 6) is a real, deterministic,
  fail-closed rubric evaluator** (`score`, `materialDefectFound`,
  `releaseCandidate`) that already separates eligibility
  (`materialDefectFound`) from a graded score, and its own doc comment states
  "Only the reviewer may release T6B; this module never sets or claims a
  release decision itself" - i.e. it already implements the
  eligibility-before-preference ordering this design contract requires, at
  the single-candidate level, not yet across a candidate set.

Neither finding changes G1's `ADAPT` disposition; both strengthen the case
that a task-class calibration owner should compose (not duplicate) G3's
grading primitives and G2/T6A's rubric-evaluator pattern.

## Confirm / Revise / Reject The Preferred Hypothesis

Work-order preferred hypothesis:

```text
task-class calibration owner
  consumes candidate identity + comparable G3 evaluation evidence
  references performance/provider evidence without promoting it
  emits a non-mutating operating-point assessment
  binds the accepted choice to regression/invalidation evidence
```

**Disposition: CONFIRMED WITH BOUNDED BINDING REFINEMENT.** The dependency
direction remains sound, but G3's `BehavioralEvaluation` has no candidate ID,
configuration hash, trace ID, or capture mode. The new owner must verify a
separate immutable candidate-to-trace-to-evaluation envelope before consuming
that result. G3 admission and held-out evidence are mandatory for a
`preferred` decision in this G1 contract. An `evaluateHarderCandidate`-style
rubric adapter is optional secondary evidence, never a rubric-only bypass of
the G3 fixture and holdout gate. Neither source is a live-execution receipt.

## Owner Matrix

| Existing surface | Disposition | Role in the new owner |
|---|---|---|
| `PerformanceBenchmarkHarnessContract` (source 4/5) | REUSE | Supplies optional `PROPOSAL_ONLY` measurements for exploratory comparison only. Raw reports cannot establish `preferred` or create a regression binding; GC-026 promotion is separately required before a performance metric can be an authoritative preference basis |
| `docs/reference/CVF_PERFORMANCE_ACCEPTANCE_POLICY_BASELINE_2026-03-29.md` (GC-026 promotion path) | REUSE | Unchanged; remains the only path from `PROPOSAL_ONLY` benchmark evidence to baseline truth. The calibration owner never bypasses or shortcuts this path |
| `assf.behavioral.evaluation.contract.ts` (`gradeBehavioralEvaluation`, `admitFixtureSet`, `admitBaselinePair`) (source 8) | REUSE | Mandatory held-out behavioral evidence. The new owner supplies and verifies the candidate binding envelope that G3 does not provide; G3 retains fixture/trace validation and repeat/pair admission |
| `harder.value.candidate.contract.ts` (`evaluateHarderCandidate`) (source 6) | ADAPTER_ONLY | Fixed-task reference pattern for an optional deterministic rubric adapter alongside G3 evidence, never instead of a full admitted held-out fixture set. Its `releaseCandidate` flag means possible T6B release, not G1 eligibility or preference |
| `run-mao-oa-t6a-candidate-calibration.ts` (source 7) | ADAPTER_ONLY | Reference pattern only: one-call, no-retry, receipt-gated, sanitize-before-persist live invocation shape. The calibration owner's live-evidence-collection step (a later, separately governed implementation, not this design) should follow this pattern, but this exact script remains task-specific (`MAO-OA-T6A-HARDER-CANDIDATE`) and is not imported or generalized by this design |
| `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` (source 10) | REUSE (gating only) | A separately declared policy admits only exact statuses `CANARY_PASS` or `CERTIFIED` when that minimum is required; statuses are a taxonomy, not an ordered numeric scale. The matrix is never preference evidence or proof of credential availability |
| G3 lifecycle/certification schema (`certificationState`/`uatState`) | DEFER | Skill-level certification lifecycle is a separate owner from task-class operating-point selection; the calibration owner does not read or write certification/UAT state |
| G2/G6 (runtime topology reallocation; change-aware verification selection) | DEFER | Independent T0 gaps; not composed into this owner |
| G4 (incremental/marginal value measurement) | DEFER | Explicitly excluded per work order; G4 may later consume this owner's accepted-candidate/rejected-candidate comparable pairs as an input, but this design creates no G4 output, hook, or interface obligation |
| A new, independent calibration-evidence data model or grading engine | REJECT_DUPLICATE | Not proposed. G3's fixture/trace/evidence shapes and G2/T6A's rubric-evaluator shape already cover the required primitives; a parallel implementation would violate the work order's `ADAPT`, not `ADOPT`, mandate and the Anti-Bloat posture the T0 audit already established |

No new architectural component, runtime service, storage layer, or grading
engine is proposed. This design's only new artifact class (in a later,
separately governed implementation tranche) is a thin **composition/decision
layer**: a pure function set that takes already-produced G3
`BehavioralEvaluation` results (and optional rubric-evaluator results) for a
declared candidate set under one task class, verifies their immutable producer
bindings, applies eligibility, and emits a non-mutating
`OperatingPointAssessment`. A `RegressionBinding` is emitted only when one
candidate has an admissible, governed preference basis. It calls existing
owners; it does not replace or wrap them opaquely.

## Owner And Dependency Direction Graph

```text
task-class declaration (new, thin: task class id + fixture-set ref + eligibility policy)
        |
        v
candidate-configuration set (new, thin: candidate id + declared dimensions)
        |
        +--> [G3 owner] admitFixtureSet(fixtures) ------------------> fixture-set admission (ADMITTED | MISSING_POSITIVE_CASE | MISSING_NEGATIVE_CASE | MALFORMED_FIXTURE_SET)
        |
        +--> per candidate: immutable candidate/evidence envelope -> verify config, fixture, trace and result digests
        |         -> [G3 owner] gradeBehavioralEvaluation(fixture, traces, pairedFixture?)
        |         -> BehavioralEvaluation (no candidate or trace identity in G3 output)
        |
        +--> per candidate (optional, task classes with a deterministic rubric):
        |         [rubric-evaluator adapter, e.g. evaluateHarderCandidate-shaped] -> { score, materialDefectFound, eligible }
        |
        +--> per candidate (optional, cost/latency/throughput only):
        |         [benchmark owner] PerformanceBenchmarkHarnessContract.generateReport() -> BenchmarkReport (evidenceClass=PROPOSAL_ONLY, referenced not promoted)
        |
        +--> per candidate (gating only, when candidate names a provider/model lane):
                  [provider-readiness owner] CVF_PROVIDER_LANE_READINESS_MATRIX status lookup -> eligibility precondition only

        all four evidence streams above feed into:
        v
[NEW: calibration decision function] (pure, offline, no I/O)
        - eligibility filter (quality/risk BEFORE cost/latency)
        - deterministic decision-state assignment per candidate
        - preferred-candidate selection only with an admissible, governed preference basis
        |
        v
OperatingPointAssessment (new: candidate/config hash, decision state, bound evidence refs, comparability fingerprint, provenance fingerprint, proposal-only flag)
        |
        v
[NEW: regression binding] RegressionBinding (only for one admissibly preferred candidate; config/evidence hashes + required re-grade triggers)
        |
        v
invalidation trigger evaluation (fingerprint mismatch | fixture-set change | provider-lane downgrade | GC-026 threshold repromotion)
        -> on trigger: mark RegressionBinding STALE; require a fresh OperatingPointAssessment before the accepted point is relied on again
        -> never auto-mutates configuration; never auto-rolls back
```

Dependency direction is strictly downstream: the new decision layer calls G3,
the rubric-evaluator pattern, the benchmark harness, and the provider-
readiness matrix as read-only evidence sources. None of those four existing
owners is modified, wrapped with side effects, or given a new consumer
obligation by this design. The new layer has exactly one write surface in a
later implementation: emitting `OperatingPointAssessment` and
`RegressionBinding` records to a to-be-named governed path; it never writes
into G3's, the benchmark harness's, or the provider matrix's data.

## Stable Task-Class And Candidate-Configuration Identity

- **Task-class identity**: `taskClassId` (stable string, dispatcher-declared,
  never regenerated), bound to exactly one held-out G3 fixture-set reference
  (`admitFixtureSet` input) whose `positiveCount >= 1` and
  `negativeCount >= 1` per G3's existing admission rule. A task class without
  an admitted held-out fixture set cannot produce `preferred` or a regression
  binding in this contract; rubric-only evidence is not a fallback.
- **Candidate-configuration identity**: `candidateId` (stable string, unique
  within one calibration round for one `taskClassId`), plus a frozen
  `declaredDimensions` record capturing every allowed dimension (below).
  `candidateConfigHash` hashes canonical, versioned serialization of that
  record. The round rejects one ID with multiple hashes and duplicate hashes
  under different IDs; labels cannot substitute for content identity.

**Evidence binding required before grading or decision:** each candidate's
immutable envelope records `{taskClassId, candidateId, candidateConfigHash,
comparabilityFingerprint, fixtureSetContentHash, fixtureId, fixtureContentHash,
traceIds[], traceContentHashes[], traceCaptureModes[], g3ResultHash,
producerReceiptRef}` per required fixture. The decision layer verifies the
fixture/trace hashes and IDs against supplied G3 inputs, recomputes the G3
result digest, and requires a producer receipt tying each trace to the same
candidate/configuration. A missing, ambiguous, reused-across-candidates, or
contradictory binding is `insufficient_evidence`; a mismatched round fingerprint
is `incomparable`. G3's result shape itself does not attest candidate identity
or live execution. No envelope may claim live proof from G3's offline modes.

## Allowed Vs Forbidden Candidate Dimensions

| Class | Dimensions | Rule |
|---|---|---|
| ALLOWED | effort/reasoning-level profile; prompt/scaffolding profile; tool-set selection; context/window policy; budget ceiling (token/cost/call count); topology (single-agent vs delegated, when G2 later supplies a reallocation primitive); provider/model lane (subject to readiness gating) | May vary between candidates under comparison; each is a named field in `declaredDimensions` |
| FORBIDDEN FROM SILENT COMPARISON | task/case set (fixture set) per candidate; environment/sandbox tier; policy/risk ceiling; acceptance criteria; grading rubric or fixture version | Must be identical across every candidate in one comparison round. A candidate that varies any forbidden dimension is not comparable and must be rejected into `incomparable`, never silently scored against the others |

This mirrors G3's own `admitBaselinePair` rule (WITH/WITHOUT pairs must share
byte-identical `canonicalInputBytes`) generalized from a two-way pair to an
N-way candidate set: every candidate must share the same fixture set,
environment, and policy; only the allowed dimensions may differ.

## Comparability Fingerprint

`comparabilityFingerprint = SHA-256(canonicalVersion | taskClassId |
fixtureSetContentHash | environmentDescriptorHash | policyId |
acceptanceCriteriaVersion | gradingRubricVersionHash | heldoutPartitionHash)`, computed once
per calibration round and attached to every candidate's evidence record.

- **Input/case-set**: bound by `fixtureSetContentHash` (derived from each
  fixture's existing `fixtureContentHash`/`sourceContentHash` fields, already
  present in G3's `BehavioralFixture` shape).
- **Environment**: content hash of the named sandbox/tool-availability
  descriptor declared once per round, not per candidate.
- **Rubric**: exact rubric/version content hash, or the explicit `NONE` sentinel
  when no optional rubric adapter is used. A rubric change invalidates the
  comparison even when its label stays the same.
- **Partition**: hash of the predeclared search/held-out membership ledger.
- **Model/provider**: not part of the fingerprint itself (it is a candidate
  dimension), but every candidate's declared provider/model lane must pass
  the provider-readiness gate independently.
- **Budget**: not part of the fingerprint (it is a candidate dimension); the
  eligibility filter, not the fingerprint, enforces that a stated budget
  ceiling was not exceeded.
- **Policy**: `policyId` (risk/quality policy in force) is part of the
  fingerprint; a policy change invalidates the round.

**Mismatch behavior**: a candidate whose evidence was produced under a
different `comparabilityFingerprint` than the round's current fingerprint is
never merged into the same comparison; the calibration decision function
rejects it with decision state `incomparable` and a named mismatch reason
(fixture-set changed, environment changed, or policy changed).

## Search/Training Vs Held-Out Separation

The owner predeclares separate `SEARCH` and `HELD_OUT` membership ledgers,
each binding fixture ID, input/content hashes, task class, and partition
version before candidate tuning. Only the held-out set may contribute
acceptance evidence, and that set must pass G3 `admitFixtureSet`. G3
`baselineRole` is **not** a partition label: `NONE` means no WITH/WITHOUT
pair is required, while `WITH`/`WITHOUT` govern paired-fixture admission.
The new decision layer, not G3, enforces partition membership and rejects
any held-out fixture whose ID, canonical input hash, source hash, or content
hash appears in SEARCH or has been exposed to candidate tuning. Rejection
is `insufficient_evidence` with decision-layer defect
`REUSED_HELDOUT_SEARCH_DATA`; G3's defect vocabulary is unchanged.

## Repeat, Uncertainty, Missing-Data, Partial-Run Semantics

Reused directly from G3 (source 8), not reinvented: `repeatsRequired` is
exactly 1 for `DETERMINISTIC` fixtures and exactly 3 for `STOCHASTIC`
fixtures; `gradeBehavioralEvaluation` already returns
`INSUFFICIENT_REPEAT_EVIDENCE` with `repeatsObserved` when fewer than the
required consecutive passing repeats are observed, and `INCOMPLETE_TRACE`
when no trace was supplied. Missing trace, incomplete repeats, stale/invalid
producer binding, or contamination produce `insufficient_evidence`; a
complete, bound `FAIL_WITH_DEFECTS` or other substantive G3 defect produces
`ineligible`. Neither category earns partial credit.

## Eligibility Before Preference (No Score Laundering)

Two-stage decision, evaluated in this fixed order and never collapsed into
one weighted scalar:

1. **Classification and eligibility**, with exclusive precedence: (a)
   mismatched round fingerprint or forbidden dimension -> `incomparable`;
   (b) absent/ambiguous binding, unadmitted or contaminated held-out set,
   `INCOMPLETE_TRACE` or `INSUFFICIENT_REPEAT_EVIDENCE` ->
   `insufficient_evidence`; (c) complete bound behavioral defect, material
   rubric defect, explicit provider-lane gate failure, or exceeded declared
   budget -> `ineligible`; (d) only complete, bound G3 PASS evidence for all
   required fixtures proceeds to preference. The provider gate uses an
   explicit allowed-status set, never a numeric ordering of the matrix's
   status labels. No score overturns (a)-(c).
2. **Preference ranking**, only among eligible candidates: the round declares
   metric names, units, direction, tie rule, and an authoritative evidence
   basis before measurement. Raw benchmark `PROPOSAL_ONLY` rows may produce
   an explicitly `PROPOSAL_ONLY` exploratory ranking, but cannot assign
   `preferred` or create `RegressionBinding`. A performance-based preferred
   choice requires separately GC-026-promoted trace-backed evidence. A
   rubric-based preferred choice requires a predeclared, version-bound,
   comparable deterministic rubric for every candidate; no undeclared metric
   or implicit secondary tie-break is allowed. If no admissible preference
   basis exists, all eligible candidates remain `eligible_nonpreferred` and
   the assessment says `NO_ADMISSIBLE_PREFERENCE_EVIDENCE`.

## Deterministic Decision States

| State | Meaning |
|---|---|
| `ineligible` | Complete bound evidence establishes a substantive quality/risk/budget/readiness failure |
| `eligible_nonpreferred` | Passed eligibility; not selected as the round's preferred candidate |
| `preferred` | Passed eligibility and is the sole best candidate under a predeclared, admissible preference basis; never based on raw `PROPOSAL_ONLY` metrics |
| `incomparable` | Evidence exists under a different `comparabilityFingerprint`, or the candidate varies a forbidden dimension; never compared |
| `insufficient_evidence` | Missing/ambiguous candidate binding or held-out admission, incomplete G3 evidence, or `REUSED_HELDOUT_SEARCH_DATA` contamination |

These five states are jointly exhaustive and mutually exclusive per
candidate per round; the decision function assigns exactly one state to
every declared candidate, never leaves a candidate unclassified, and never
uses a sixth ad hoc state.

## Negative Cases

| Case | Required decision-layer behavior |
|---|---|
| Empty candidate set | Round is `BLOCKED_EMPTY_CANDIDATE_SET`; no `OperatingPointAssessment` is emitted |
| Duplicate candidate IDs or hashes | One `candidateId` with different `candidateConfigHash`, or two IDs with the same hash, blocks the round; never silently overwrite or double-count |
| Mixed task/case sets among candidates | Every candidate with a different `fixtureSetContentHash` than the round's declared set is `incomparable`; the round proceeds only over the comparable subset, and the report discloses the excluded candidates by ID and reason |
| Unequal budgets/policies among candidates | Budget: enforced per-candidate at the eligibility filter (exceeding stated ceiling is `ineligible`, not silently allowed). Policy: any candidate under a different `policyId` is `incomparable`, never merged |
| Missing held-out evidence or candidate binding | `insufficient_evidence`; neither a G3 result nor a label alone attests which candidate produced a trace |
| Reused held-out/search data (contamination) | `insufficient_evidence` with `REUSED_HELDOUT_SEARCH_DATA`; that candidate's acceptance evidence is never trusted even if it otherwise passed |
| Stale fingerprints | `incomparable` with the mismatch reason named; the round never silently mixes stale and current evidence |
| Incomplete repeats | `insufficient_evidence`, using G3's own `repeatsObserved`/`repeatsRequired` fields; never rounded up or averaged into a pass |
| Unknown metrics or units | Exclude and log `UNKNOWN_METRIC_EXCLUDED`; if no admissible declared preference basis remains, emit `NO_ADMISSIBLE_PREFERENCE_EVIDENCE`, never `preferred` |
| Ties (two or more `eligible` candidates with identical ranking under the declared preference policy) | Decision state is `eligible_nonpreferred` for all tied candidates; the round's `OperatingPointAssessment` records `TIE_NO_AUTOMATIC_PREFERENCE` and requires an explicit reviewer/operator tie-break input before any candidate is marked `preferred`; the decision layer never auto-breaks a tie by an undeclared secondary metric |
| No eligible candidate | Round result is `NO_ELIGIBLE_CANDIDATE`; no `preferred` state is assigned to any candidate, and no prior accepted operating point is disturbed |
| Proposal-only performance advantage | May be reported as exploratory `PROPOSAL_ONLY` ranking; cannot emit `preferred` or `RegressionBinding` before separate GC-026 promotion |

## Provenance Fingerprint And Invalidation Triggers

`provenanceFingerprint = SHA-256(canonicalVersion |
comparabilityFingerprint | acceptedCandidateId | candidateConfigHash |
orderedEvidenceEnvelopeHashes[] | preferencePolicyHash |
promotionEvidenceRefOrRubricHash)`, attached to an assessment with one
admissibly `preferred` candidate. `acceptedAt` is recorded separately as
metadata, not as a replacement for content identity.

**Invalidation triggers** (any one marks the bound `RegressionBinding`
`STALE`, never auto-mutates or auto-rolls back the running configuration):

- fixture-set content hash changes for the bound `taskClassId`;
- candidate configuration hash, bound trace/result digest, producer receipt,
  search/held-out partition, rubric version, environment descriptor,
  `policyId`, acceptance criteria, or preference policy changes;
- the accepted candidate's provider/model lane readiness status downgrades
  below the required minimum (per source 10's `DEGRADED`/`BLOCKED` states);
- a GC-026 promotion changes or is withdrawn for performance evidence used
  in the accepted preference decision;
- the accepted candidate's declared budget ceiling is lowered below its
  recorded consumption.

On any trigger, the owner's only required action is to mark the binding
`STALE` and require a fresh `OperatingPointAssessment` before that operating
point is relied on again; it never writes a new configuration, never
retriggers a live call, and never silently keeps serving a stale accepted
point without a visible `STALE` marker.

## Regression Binding

`RegressionBinding` = `{ taskClassId, acceptedCandidateId,
candidateConfigHash, comparabilityFingerprint, provenanceFingerprint,
orderedEvidenceEnvelopeHashes, preferenceAuthorityRef, boundAt,
invalidationStatus: "CURRENT" | "STALE", requiredRegradeTriggerSet }`.
Binding is created only when a round produces exactly one admissibly
`preferred` candidate (never on a tie, no eligible candidate, missing
preference evidence, or raw `PROPOSAL_ONLY` performance ranking). The binding
record itself is evidence only; a
separate, later-governed promotion/mutation owner (explicitly out of scope
here, same boundary as GC-026 for benchmark evidence) is required before an
accepted operating point can change what actually executes.

## G3, G4, And Provider-Readiness Boundaries (Explicit)

- G3 evidence is consumed **structurally** (its typed `BehavioralEvaluation`
  result and admission functions) as a required held-out input stream. The
  new candidate/evidence envelope supplies identity G3 does not contain. This design
  does **not** claim that G3 results by themselves select or certify an
  operating point; G3 supplies one of up to three evidence streams (fixture
  evidence, optional rubric evidence, optional benchmark evidence) that the
  new decision layer combines under the eligibility-before-preference rule.
  G3 itself remains `CLOSED_PASS_BOUNDED_G3_PARKED`; this design adds no
  obligation back onto the G3 module and does not reopen it.
- G4 (marginal/incremental value measurement) is **excluded and deferred**
  throughout. No G4 output, score, or ratio is computed or consumed here.
  This design does note (informationally, not as an obligation) that a
  future G4 owner could consume `OperatingPointAssessment`/`RegressionBinding`
  pairs as WITH/WITHOUT evidence, but creates no interface, hook, or promise
  toward that.
- Provider-lane readiness (`CERTIFIED`, `CANARY_PASS`, etc.) is used strictly
  as an **eligibility precondition**, never as ranking or preference
  evidence, and never promoted beyond the adjacent/certification role stated
  in source 10's own Claim Boundary ("Multi-provider operability is proven.
  Provider parity is not claimed").

## Findings / Position

All ten sources are read, hashed, and terminally reconciled (10/10, zero
drift, zero contradiction). G1-C1..C3 remain unchanged at current source.
The work order's preferred hypothesis is confirmed with bounded binding
refinements: the new owner verifies candidate/trace/result identity around
G3's `gradeBehavioralEvaluation` output; it requires held-out G3 evidence
and may accept an optional rubric-evaluator adapter (in the shape of
`evaluateHarderCandidate`) for task classes with a deterministic scoring
rubric. Exactly one canonical composition owner is proposed: a thin new
decision layer that reuses `PerformanceBenchmarkHarnessContract`,
`assf.behavioral.evaluation.contract.ts` (G3), the harder-candidate
rubric-evaluator pattern (adapter-only), and
`CVF_PROVIDER_LANE_READINESS_MATRIX.md` (eligibility gate only) as read-only
evidence sources. No parallel benchmark/evaluation/provider owner is
proposed. G4 remains independent and deferred throughout. Full detail is in
the Owner Matrix, Owner And Dependency Direction Graph, and Confirm/Revise/
Reject sections above.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Citing a stale pre-repair draft of the G3 grader as accepted evidence | Verified source 8's SHA-256 exactly matches the G3 T2 completion review's cited final accepted hash before relying on its exported functions |
| Score laundering (a weighted composite trading away a required quality/risk constraint) | Design enforces a strict two-stage eligibility-before-preference order (see Eligibility Before Preference section); no numeric score can overturn an eligibility failure |
| G3/G4 boundary drift (implying G3 alone selects an operating point, or folding G4 in) | Explicit "G3, G4, And Provider-Readiness Boundaries" section states G3 supplies one structural evidence stream, not a certifier; G4 is excluded with zero interface obligation created |
| Provider-readiness overclaim beyond its adjacent/certification role | Provider-lane status is restricted to an eligibility precondition only, citing the matrix's own Claim Boundary language directly |
| Circular or contaminated holdout selection undermining comparability | The new owner predeclares a distinct SEARCH/HELD_OUT ledger and rejects shared ID/input/source/content hashes; G3 `baselineRole` remains solely a WITH/WITHOUT pairing field |
| Candidate misattribution and stale configuration | The decision-layer envelope binds candidate configuration hash, trace IDs/content hashes, G3 result hash and producer receipt; changes invalidate the regression record |
| Proposal-only benchmark promoted by an apparent `preferred` decision | Raw benchmark rows support only exploratory proposal; performance preference and regression binding require separate GC-026-promoted evidence |
| Successor implementation scope creep beyond this design | Successor manifest is capped at exactly five named paths and one separately governed implementation tranche; no automatic successor is authorized |

No unresolved risk blocks the `DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER`
disposition below.

## Terminal Disposition

**`DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER`**

All ten sources are read, hashed, and terminally reconciled (10/10, zero
drift, zero contradiction). Exactly one canonical composition owner is
proposed (a thin new decision layer that calls G3, the rubric-evaluator
pattern, the benchmark harness, and the provider-readiness matrix as
read-only evidence sources; no parallel grading/benchmark/certification
owner is created). Dependency directions are explicit and one-way
(decision layer depends on the four existing owners; none of them depends on
or is modified by the new layer). State/decision semantics, negative cases,
comparability fingerprint, holdout/contamination rule, provenance/
invalidation, and regression binding are complete per the Evidence
Requirements list. G4 remains excluded and deferred. Provider-readiness and
`PROPOSAL_ONLY` benchmark evidence are not promoted; without an admissible
preference basis there is no binding. The exact successor
implementation manifest is below.

## Exact Successor Implementation Manifest

A later, separately governed implementation work order (not opened by this
design) would create exactly these paths, none of which exist yet in this
repository:

| Path | Role |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | pure decision-layer implementation: eligibility filter, preference ranking, decision-state assignment, `OperatingPointAssessment`/`RegressionBinding` emission |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts` | adversarial test suite covering every negative case in this design's Negative Cases table |
| `governance/compat/check_task_class_calibration_owner_evidence.py` | read-only evidence/schema checker mirroring `check_assf_behavioral_evaluation_evidence.py`'s pattern for the new owner's persisted evidence shape |
| `governance/compat/test_check_task_class_calibration_owner_evidence.py` | checker test suite |
| `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md` | normative reference contract, mirroring `CVF_ASSF_BEHAVIORAL_EVALUATION_CONTRACT.md`'s structure |

No more than this one separately governed implementation tranche is implied.
No automatic successor is authorized by this design; a fresh GC-018
baseline/work order pair and operator checkpoint are required before any of
the five paths above is created.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is a worker-owned design/audit artifact
returned `COMPLETE_PENDING_REVIEW`, not a closure artifact. This document
cites `CLOSED_PASS_BOUNDED_G3_PARKED` only as a quoted fact about the
already-closed G3 T2 tranche (source 8/9); it does not itself close
anything. Machine closure packaging for this G1 T1 design tranche belongs to
Local after the three returned worker outputs are reviewed and materially
committed, per the governing work order's own Machine Closure Package
section.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md` | still `DISPATCH_READY` pending Local review | N/A with reason: worker cannot close a work order |
| Completion or reviewer artifact | N/A with reason: not yet authored | N/A with reason: Local decides whether a separate completion review is needed | N/A with reason: pending Local |
| Roadmap state | active ACEL continuity | G1 T1 design tranche pending Local review; no roadmap state change made by this worker | N/A with reason: session-sync steward acts only after Local acceptance |
| Registry JSON | `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` | 10/10 ledger rows, valid JSON (`python -m json.tool` exit 0) | PASS |
| Registry Markdown | this file | ten-source ledger, owner matrix, closed-loop contract, negative cases | PASS |
| External evidence digest | N/A with reason: no external evidence entered this internal G1 design tranche | zero external inputs consumed | N/A with reason |
| System loop interlock | N/A with reason: no runtime consumer exists | design only; no runtime mutation | N/A with reason: static design |
| Session continuity | active continuity sources | not updated by this worker | N/A with reason: session-sync steward acts only after Local acceptance |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Source ledger completeness | 10/10 exact hashes and terminal statuses | 10/10, all `READ`, zero drift | PASS |
| Owner composition | one canonical owner plus explicit dependencies | one thin decision layer; four REUSE/ADAPTER_ONLY dependencies; zero REJECT_DUPLICATE proposals | PASS |
| Closed loop | task class through regression/invalidation | complete per Owner And Dependency Direction Graph and Regression Binding sections | PASS |
| G4 isolation | no merged contract or output | explicit DEFER; zero G4 interface/hook created | PASS |
| Provider authority | zero calls; forbidden | zero provider/live/benchmark/credential calls | PASS |
| Worker commit | forbidden; Local owns commit | zero `git add`/`git commit` executed | PASS |
| Manifest JSON validity | parses under `python -m json.tool` | exit code 0 | PASS |

## Claim Boundary

This audit is a documentation-only design decision. It does not implement,
execute, benchmark, call a provider, mutate a configuration, select or
certify a real operating point, or authorize G4, runtime wiring, public
sync, or deployment. All dispositions are subject to independent Local
review before any successor work order.
