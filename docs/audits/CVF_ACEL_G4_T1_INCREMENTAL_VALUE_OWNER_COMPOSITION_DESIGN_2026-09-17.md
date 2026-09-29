# CVF ACEL G4 T1 Incremental Value Owner Composition Design

Memory class: governed-worker-audit

docType: audit

Status: COMPLETE_PENDING_REVIEW

Batch ID: ACEL-G4-T1-INCREMENTAL-VALUE-OWNER-COMPOSITION-DESIGN

executionBaseHead: `9ceec78bc3ec60e5c121d76f3aa966f6beda00cf`

Manifest: `docs/audits/CVF_ACEL_G4_T1_INCREMENTAL_VALUE_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-17.json`

## Purpose

Design, on paper only, which current CVF owner should consume paired G3-style
behavioral outcomes and existing review-cost evidence to describe an
incremental capability/delegation value assessment, and specify a fail-closed
comparison contract that cannot mistake an absolute-quality receipt, a
readiness receipt, or a process/compliance counter for marginal value. No
code is written or executed, no provider is called, no benchmark is run, and
no configuration is mutated by this tranche.

## Target / Source

Eight current private-CVF sources read and hashed completely at
`executionBaseHead`. Full ledger in the machine manifest; summary here.

| # | Path | SHA-256 | Status |
|---|---|---|---|
| G4-S1 | `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md` | `107808cde5991393786949a9b7a2bae4c40b53620342bd181791031c69729cae` | READ |
| G4-S2 | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_2026-09-15.md` | `5073932e1bcb18754ff914003b1bbac80037dad2b7599b50c29fb497f2eea39a` | READ |
| G4-S3 | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_EVIDENCE_T0_2026-09-15.json` | `a1ec2a5ce31e15dc5ca369c0b9587c7a61f54a517f1439355bd6f49b5caaefe3` | READ |
| G4-S4 | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | `f4daec03545cfcd4a13d5f3a4d6f340cff68f3b4afb846fe79dc6d348f86b68f` | READ |
| G4-S5 | `governance/compat/check_review_cost_control.py` | `e840de6bd489b1031c2bffb20b1d8335556fd18df73989eece812e53dadb3946` | READ |
| G4-S6 | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts` | `83201e79a1172e50bcaaecd444b3dc5c7709658f0a83256f1c7d23b5cfd659cd` | READ |
| G4-S7 | `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md` | `752762a04a897f188af5ea479b96f4d95f6ff1609e7ec1ad75aea35a205c7648` | READ |
| G4-S8 | `docs/reference/CVF_NON_CODER_VALUE_MEASUREMENT_STANDARD_2026-04-14.md` | `f76c6423f46fc1314fada27ae75e8fc3012e46d99639aa351b47283ff236cd01` | READ |

All eight hashes were recomputed directly with SHA-256 file digests (not
`git hash-object`) at `executionBaseHead` and match the paired GC-018
baseline and governing work order's Target / Source table exactly, with zero
drift.

## Scope / Methodology

Read-only design audit. Every one of the eight sources was read in full, not
sampled, and independently rehashed. No experiment, benchmark run, provider
call, or configuration mutation occurred. The design resolves one bounded
owner question -- which current CVF owner should consume paired G3-style
behavioral outcomes and existing cost/review evidence to describe an
incremental capability/delegation value assessment -- then composes an owner
graph, a fail-closed comparison contract, decision-state machine, negative-case
table, provenance/invalidation rule, and an exact successor manifest, per the
work order's Evidence Requirements section.

Role: `INTERNAL_AGENT` design and source-verification worker. Phase: offline
owner-composition design. Decision owner: Local reviewer/closer.

## G4-C1 Reconciliation And Freshness Delta

| Claim | T0 disposition | Current-source check | Freshness delta |
|---|---|---|---|
| G4-C1 (review-cost standard and its checker explicitly leave independence, criticality, and incremental value to reviewer judgment; the checker never scores value delta) | ADAPT, MEDIUM (T0); confirmed HIGH here | Source G4-S4 line ~516 area still reads "independence, criticality, and incremental value remain reviewer judgment." Source G4-S5 docstring (module header) still states "It never scores semantic review quality, root-cause independence, or value delta; those remain reviewer judgment." | NONE |

G4-C1 is unchanged at current source. No new counter-evidence was found. This
confirms the T0 gap is still open and the design may proceed on the accepted
`ADAPT` basis.

## New Evidence Found During This Design Pass (Not In T0 Ledger)

Three current-source facts materially inform this design and were not part of
the original six-gap T0 ledger, because T0 scoped to G1-G6 gap existence, not
G4's later composition design:

- **G3 (source G4-S6) already implements the exact WITH/WITHOUT paired-input
  admission primitive G4 needs**: `admitBaselinePair` mandates a
  complementary fixture with byte-identical `canonicalInputBytes` whenever a
  fixture declares `baselineRole: WITH` or `WITHOUT`, and fails closed with a
  named token (`MISSING_PAIR`, `SAME_ROLE_PAIR`, `MALFORMED_ROLE`,
  `NONEQUIVALENT_INPUT_BYTES`, `UNEXPECTED_PAIR_FOR_NONE_ROLE`) on any
  structural defect. Its own claim boundary states this is "a pure
  structural admission check of a WITH/WITHOUT baseline pairing; does not
  grade either fixture and does not imply PASS_WITH_EVIDENCE." This is the
  strongest existing comparability primitive in current CVF, and G4 must
  reuse it rather than invent a second pairing admission function.
- **The G1 design (source G4-S7) already names G4 explicitly as a
  deferred future consumer** of its `OperatingPointAssessment`/
  `RegressionBinding` output pairs, stating this "creates no interface, hook,
  or promise toward that." The design *document* G4-S7 itself still reads
  `Status: COMPLETE_PENDING_REVIEW` / `DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER`
  because it predates Local's repair pass; the governing current authority is
  the active session continuity and handoff record, which state
  `ACEL-G1-T1-EMPIRICAL-CALIBRATION-OWNER-COMPOSITION-DESIGN` is
  `CLOSED_PASS_BOUNDED` at material commit `d87aadaec` (ten source hashes
  matched, corrected-base pre-implementation 84/84 PASS, reviewer-fast 68/68,
  material pre-commit 89/89). This design cites G1's status as
  `CLOSED_PASS_BOUNDED` (accepted design, still unimplemented), not the raw
  file's own pre-repair self-declaration. G4's owner composition must honor
  this: G1 is an optional future evidence source once separately
  implemented, never a dependency this design creates or requires.
- **The lane-specific non-coder value standard (source G4-S8) is a real,
  scoped, currently-governing precedent for a controlled WITH/WITHOUT
  comparison that already exists in CVF** (`W93-T1`: "same task, same
  provider, same model family, same template, with only one controlled
  variable changed: with knowledge-native support / without knowledge-native
  support," required to end in exactly one of three named outcome tokens,
  "supported by rubric deltas and evidence excerpts, not narrative
  preference"). This is decisive counterevidence against any claim that CVF
  has zero precedent for comparable-condition value measurement anywhere.
  It is lane-specific (non-coder wave `W90`-`W94` only) and does not itself
  close the general G4 gap; source G4-S1's `ADAPT` disposition and source
  G4-S3's `G4-C1` claim remain correctly scoped to the *general*
  capability/delegation/provider-lane/topology case, which `W93-T1` does not
  cover (it is bound to one product feature comparison, not an arbitrary
  capability or delegation decision).

Neither finding changes G4's `ADAPT` disposition; all three strengthen the
case that a G4 owner should compose (not duplicate) G3's pairing primitive
and should explicitly disclose, not override, the lane-specific precedent.

## Owner Question Resolution

**Question:** which current CVF owner should consume paired G3-style
behavioral outcomes and existing cost/review evidence to describe an
incremental capability/delegation value assessment?

**Resolution:** No current owner can be extended in place to perform this
role without violating its own claim boundary. The review-cost standard and
checker (G4-S4/G4-S5) are the closest candidate by subject matter, but both
explicitly and repeatedly disclaim scoring value delta; folding a value-delta
computation directly into them would contradict their own accepted, tested,
first-party self-declaration and would silently convert a documented
process/compliance-counter owner into a semantic-scoring owner without a
separate acceptance review of that boundary change. G3 (G4-S6) is a required
upstream evidence supplier (paired WITH/WITHOUT admission and grading), not a
value-delta owner itself; its own claim boundary is "pure structural
admission," not comparison verdict. No owner in the eight-source set already
performs a general capability/delegation/provider-lane/topology
marginal-value computation.

**Disposition: `ADAPT` via one new, thin composition owner**, analogous in
shape to the `CLOSED_PASS_BOUNDED` (at `d87aadaec`), still-unimplemented G1
design's new decision layer. This is not `ADOPT`:
the new owner is a pure, offline, non-mutating composition/decision function
over already-produced evidence, calling G3 and review-cost evidence as
read-only sources; it creates no new grading engine, no new pairing-admission
mechanism, and no new counter/telemetry mechanism (those remain G3's and the
review-cost owner's respectively). This satisfies the work order's `ADOPT`
bar test (positive Local absence proof plus a non-mappable architectural
responsibility) being deliberately NOT met: the responsibility *is* mappable
to a thin composition layer over two existing owners, exactly as G1 required
a thin decision layer over four existing owners.

## Owner Matrix

| Existing surface | Disposition | Role in the new owner |
|---|---|---|
| `CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` / `check_review_cost_control.py` (G4-S4/G4-S5) | REUSE (evidence only, unmodified) | Supplies process/compliance counters (invocation counts, quota usage, round/rework disposition) as one optional cost-dimension input; never itself asked to emit a value verdict; its own disclaimer stays exactly as accepted |
| `assf.behavioral.evaluation.contract.ts` (`admitBaselinePair`, `gradeBehavioralEvaluation`, `admitFixtureSet`) (G4-S6) | REUSE | Mandatory WITH/WITHOUT paired-condition admission and outcome grading; the new owner verifies the candidate/task binding envelope G3 does not provide and never re-implements pairing admission |
| G1 design, `CLOSED_PASS_BOUNDED` at `d87aadaec` (`OperatingPointAssessment` / `RegressionBinding`, not yet implemented) (G4-S7) | DEFER (optional future input, no dependency created) | May later supply accepted/rejected candidate-configuration comparable pairs as one additional WITH/WITHOUT-shaped evidence stream; G1 design is accepted but its owner remains unimplemented, and this design creates no interface, hook, or promise toward it |
| `CVF_NON_CODER_VALUE_MEASUREMENT_STANDARD_2026-04-14.md` (`W93-T1`) (G4-S8) | REUSE (precedent, not import) | Cited as the existing scoped counterexample to any blanket "CVF never measures value" claim; its rubric/threshold machinery is lane-specific to the non-coder wave and is not imported, generalized, or extended by this design |
| G2 (runtime topology reallocation) | DEFER | Independent T0 gap; not composed into this owner |
| G6 (change-aware verification selection) | DEFER | Independent T0 gap; not composed into this owner |
| A new independent value-scoring engine, universal scalar benefit score, or modification of the review-cost checker's disclaimer | REJECT_DUPLICATE / REJECT_SCOPE_VIOLATION | Not proposed. Would duplicate G3's grading/pairing primitives, would contradict the review-cost owner's own accepted claim boundary, and would violate the work order's explicit prohibition on inventing a universal scalar benefit score or threshold |

No new architectural component, runtime service, storage layer, or grading
engine is proposed. This design's only new artifact class (in a later,
separately governed implementation tranche) is a thin **incremental-value
composition/decision layer**: a pure function set that takes an admitted G3
WITH/WITHOUT pair (baseline candidate vs. treatment candidate) plus
optionally the review-cost owner's process/compliance counters for the same
bounded task population, verifies comparability preconditions, and emits a
non-mutating, explicitly classified delta assessment. It calls existing
owners; it does not replace, wrap opaquely, or reinterpret their disclaimers.

## Owner And Dependency Direction Graph

```text
intervention declaration (new, thin: baseline identity + candidate identity + task population ref)
        |
        v
frozen task/case population (reused from G3's admitted fixture-set shape)
        |
        +--> [G3 owner] admitFixtureSet(fixtures) ------------------> fixture-set admission (ADMITTED | MISSING_POSITIVE_CASE | MISSING_NEGATIVE_CASE | MALFORMED_FIXTURE_SET)
        |
        +--> [G3 owner] admitBaselinePair(candidateFixture, baselineFixture) --> pairing admission (ADMITTED_PAIR | ADMITTED_NO_PAIR_REQUIRED | MISSING_PAIR | SAME_ROLE_PAIR | MALFORMED_ROLE | NONEQUIVALENT_INPUT_BYTES | UNEXPECTED_PAIR_FOR_NONE_ROLE)
        |
        +--> per bound pair: [G3 owner] gradeBehavioralEvaluation(fixture, traces, pairedFixture) --> BehavioralEvaluation (WITH) + BehavioralEvaluation (WITHOUT)
        |
        +--> per bound pair (optional, cost/process dimension only):
        |         [review-cost owner] declared telemetry fields (invocation counts, quota usage, round/rework disposition) -- disclosed, never scored, for the same bounded task population and time window
        |
        +--> (optional, future, no dependency created here):
        |         [G1 owner, once implemented] OperatingPointAssessment / RegressionBinding pairs, consumed only if independently comparable under this design's own preconditions
        |
        all evidence streams above feed into:
        v
[NEW: incremental-value composition function] (pure, offline, no I/O)
        - declared intervention-variable check (exactly one permitted-to-vary dimension named)
        - comparability precondition filter over the remaining held-fixed conditions (baseline/candidate identity, environment, policy, budget, time-window, and provider lane whenever it is not the intervention variable)
        - paired aggregation across the frozen population with uncertainty disclosure
        - classification into one of the five allowed output classes (never a universal scalar)
        |
        v
IncrementalValueAssessment (new: baseline/candidate identity, bound evidence refs, comparability fingerprint, outcome/defect/risk/resource/latency dimension table with units and direction, classification, uncertainty disclosure, provenance fingerprint)
        |
        v
invalidation trigger evaluation (population change | environment/policy/provider/budget change | pairing admission change | stale evidence)
        -> on trigger: mark IncrementalValueAssessment STALE; require a fresh assessment before the prior classification is relied on again
        -> never auto-mutates configuration; never auto-promotes a candidate; never auto-rolls back
```

Dependency direction is strictly downstream: the new decision layer calls G3
and the review-cost owner as read-only evidence sources, and may optionally
call the (not-yet-implemented) G1 owner once it exists. None of those owners
is modified, wrapped with side effects, or given a new consumer obligation by
this design. The review-cost checker's own disclaimer text is unchanged; the
new layer never asks it to compute a value verdict.

## Comparison Admission Contract

**Baseline and candidate identity**: `baselineId` and `candidateId` are
stable, immutable strings bound to G3 `baselineRole: WITHOUT` and
`baselineRole: WITH` fixtures respectively (or vice versa, but never both the
same role). A fixture declaring `baselineRole: NONE` cannot participate in a
G4 comparison; it is `admitted_no_pair_required` at the G3 layer and
therefore has no comparison partner at the G4 layer.

**Frozen task/case population**: identical to G3's `fixtureSetContentHash`
for the bound comparison round; every candidate and baseline evidence record
must reference the same `fixtureSetContentHash`, exactly mirroring G3's own
byte-identical `canonicalInputBytes` pairing rule extended to the population
level.

**Candidate/trace/evaluation receipt linkage**: each side of the pair
supplies `{baselineOrCandidateId, fixtureId, fixtureContentHash, traceIds[],
traceContentHashes[], traceCaptureModes[], g3ResultHash, producerReceiptRef}`.
The decision layer verifies these against the supplied G3
`BehavioralEvaluation` and `BaselinePairAdmissionEvaluation` outputs and
requires a producer receipt tying each trace to the declared baseline or
candidate identity. G3's result shape alone does not attest which side
produced a trace or that execution was live; a missing, ambiguous, or
reused-across-sides binding is `insufficient_evidence`.

**Intervention variable versus held-fixed conditions (explicit separation)**:
every comparison round declares exactly one **intervention variable** --
the single dimension the round exists to measure the incremental value of
(for example: a capability change, a delegation decision, a provider/model
lane swap, or a topology change). The intervention variable is the one
dimension **permitted, and required, to differ** between baseline and
candidate. Its identity is bound in the `comparabilityFingerprint`, while
its baseline/candidate values are bound in provenance and excluded from the
held-fixed equality comparison. Every
other declared dimension -- environment, policy, budget, time-window, and,
whenever the intervention variable is *not* the provider/model lane, the
provider/model lane itself -- is a **held-fixed condition**: it must be
declared once per round and match exactly between baseline and candidate.
A round whose baseline and candidate evidence differ on any held-fixed
condition is `incomparable`, with the specific mismatched dimension named.
A round that varies more than one dimension at once (the declared
intervention variable plus any other dimension) is also `incomparable`,
named `MULTIPLE_UNCONTROLLED_VARIABLES`, because it can no longer attribute
an observed difference to the declared intervention alone.
The baseline and candidate must each declare a content-hashed value for the
intervention variable, and those hashes must differ. Missing declarations are
`INSUFFICIENT_EVIDENCE`; identical intervention values are `INCOMPARABLE`.
One-variable control and G3 pairing make a descriptive comparison admissible,
but do not alone establish causal attribution or randomized assignment.

**Worked resolution for the provider-lane case**: this design measures
incremental value *of* a capability, delegation decision, provider/model
lane, or topology (per the work order's Purpose); it does not simultaneously
require every one of those to be identical between baseline and candidate.
When a round's declared intervention variable is the provider/model lane
itself (for example, comparing `qwen3-max` against `qwen-plus-2025-07-28`
on the same task/fixture set), the provider-lane identity is deliberately
excluded from the held-fixed set and is instead the value being compared;
environment, policy, budget, and time-window remain held-fixed as usual.
When the round's declared intervention variable is something else (a
capability or delegation-decision change), the provider/model lane is a
held-fixed condition and must match exactly, exactly as originally stated.
The round's declaration of which dimension is the intervention variable is
mandatory and immutable for that round; a two-sided round without an
explicit, named intervention-variable declaration is
`INSUFFICIENT_EVIDENCE` at classification stage 3.

**Outcome, defect/risk, resource, and latency dimensions**: each declared
metric carries an explicit name, unit, and direction (higher-is-better or
lower-is-better) declared before measurement, never inferred after seeing
results. Review-cost counters (invocation count, quota usage) may populate
the resource dimension only as disclosed process counters, never as an
implicit value proxy; the review-cost owner's own disclaimer that it "never
scores semantic review quality, root-cause independence, or value delta"
remains true and unmodified by this usage.

**Paired aggregation, intersection threshold, and uncertainty**: the round
aggregates only over the population held in common between baseline and
candidate (the intersection of admitted fixture IDs on both sides). The
round declares, before evidence is examined, a required minimum intersection
coverage as a fraction of the declared frozen population (`fixtureSetContentHash`
membership count), with `0 < minimum <= 1`; a missing or out-of-range
declaration is `INSUFFICIENT_EVIDENCE`. This design does not set a single fixed default fraction,
because the appropriate minimum depends on population size and is a
reviewer/operator judgment call, but the threshold itself, once declared,
is fixed for the round and cannot be adjusted after evidence is seen. Three
disjoint cases are evaluated during admission stages 2-3, before either
delta classification becomes terminal:

1. **Intersection coverage meets or exceeds the declared minimum**: the
   round aggregates over the intersection and proceeds to its otherwise-due
   classification (`DESCRIPTIVE_NONCAUSAL_DELTA` or
   `MEASURED_COMPARABLE_DELTA`). Every fixture present on only one side is
   disclosed as `asymmetric_population_member` in the report, listed by ID
   and by which side lacks it; it is never silently dropped or silently
   counted into the aggregate.
2. **Intersection coverage falls below the declared minimum**: the round is
   reclassified `INCOMPARABLE` with the named reason
   `INTERSECTION_BELOW_DECLARED_MINIMUM`, carrying the observed coverage
   fraction and the declared minimum in the report. A delta is never
   computed on a population that has been narrowed below its own declared
   comparability threshold, regardless of how confident the delta on the
   narrowed subset might look.
3. **Intersection is empty** (zero fixtures admitted on both sides): the
   round is `INSUFFICIENT_EVIDENCE` with `EMPTY_INTERSECTION`, distinct from
   case 2's below-threshold-but-nonempty case, because an empty intersection
   means no paired evidence exists at all, not merely an under-covered
   comparison.

Uncertainty is disclosed per dimension (for example, a repeat-count summary
reused from G3's `repeatsObserved` / `repeatsRequired` fields for
`STOCHASTIC` fixtures) rather than collapsed into a single number. This
design explicitly does **not** define a statistical confidence-interval or
variance-estimation method for that repeat count: absent such a defined
estimator, the report discloses only the descriptive repeat counts
themselves (`repeatsObserved`/`repeatsRequired` per fixture, and how many
fixtures in the intersection met the required repeat count), not a derived
"confidence" value. A future implementation tranche may define and cite a
concrete uncertainty-estimation method (for example, a named interval
formula over the repeat counts); until one is defined and accepted, no
`IncrementalValueAssessment` may present a numeric confidence figure.

**Missing/partial evidence, selection bias, holdout leakage**: reused
directly from G1's search/held-out separation pattern -- a fixture exposed to
candidate tuning before the comparison round cannot supply accepted evidence
for that round, and this design's decision layer rejects any candidate or
baseline evidence whose fixture ID, canonical input hash, or source hash
appears in a declared search/tuning set, with the same
`REUSED_HELDOUT_SEARCH_DATA`-shaped rejection G1 defines.

**No-effect and negative-effect cases**: explicitly first-class output
states (see Deterministic Classification States below), never silently
folded into a generic `PASS` or omitted from the report.

**Tie/incomparability**: a round where baseline and candidate evidence is
equal or indistinguishable under the declared dimensions (without an
unsupported statistical-significance claim) is
dimensions is reported as `DESCRIPTIVE_NONCAUSAL_DELTA` or
`INCOMPARABLE`, never as an implicit preference for either side.

**Reproducible provenance and invalidation**: see Provenance Fingerprint And
Invalidation Triggers below.

## Deterministic Classification States

| State | Meaning |
|---|---|
| `MEASURED_COMPARABLE_DELTA` | Both sides are admitted G3 WITH/WITHOUT pairs under one matching comparability fingerprint, with complete bound evidence and a predeclared metric/unit/direction; the aggregated observed difference across the common population is reported with descriptive repeat counts, not a causal-effect or statistical-confidence claim |
| `DESCRIPTIVE_NONCAUSAL_DELTA` | Evidence exists and is comparable in population/environment, but the pairing was not produced under a controlled, admitted G3 WITH/WITHOUT design (for example, an absolute-score or readiness receipt compared informally across two runs); reported as description only, never as a causal claim |
| `INCOMPARABLE` | Baseline and candidate evidence have mismatched held-fixed conditions, no intervention contrast, multiple uncontrolled variables, or a nonempty fixture intersection below the predeclared minimum; never merged or scored against each other |
| `INSUFFICIENT_EVIDENCE` | Missing intervention or coverage declaration, ambiguous candidate/baseline binding, unadmitted or contaminated held-out set, empty fixture intersection, or incomplete G3 trace/repeat evidence |
| `NO_MEASUREMENT` | No comparison was attempted or no second (baseline or candidate) side exists at all -- for example, only a single side's absolute-pass or readiness receipt is available with nothing to compare it against. This state is about the *absence of a second side*, never about the *quality* of a pairing between two sides that do exist; a genuine, complete, two-sided but uncontrolled comparison is `DESCRIPTIVE_NONCAUSAL_DELTA`, not `NO_MEASUREMENT`. This state must never be silently reported as `MEASURED_COMPARABLE_DELTA` or as `DESCRIPTIVE_NONCAUSAL_DELTA` |

These five states are jointly exhaustive and mutually exclusive per
comparison round; the decision function assigns exactly one state, never
leaves a round unclassified, and never uses a sixth ad hoc state.
Classification precedence, evaluated in this fixed order and never
collapsed:

1. **No baseline evidence exists at all** (no candidate-side evidence, or no
   declared baseline identity, or only one side's absolute-pass/readiness
   receipt is available with nothing to compare it against) ->
   `NO_MEASUREMENT`. This stage tests only for the *absence* of a second
   side, never for the *quality* of a pairing that does exist.
2. **Baseline and candidate evidence both exist, but under mismatched
   `comparabilityFingerprint` values, with a forbidden dimension varying,
   with identical intervention values, or with a nonempty fixture
   intersection below the predeclared minimum** -> `INCOMPARABLE`.
3. **Baseline and candidate evidence both exist and are otherwise comparable,
   but intervention declaration/value binding, coverage declaration,
   binding, admission, or trace/repeat evidence is missing, ambiguous, or
   contaminated, or the fixture intersection is empty** ->
   `INSUFFICIENT_EVIDENCE`.
4. **Baseline and candidate evidence both exist, are comparable, and are
   complete, but the pairing was not produced under an admitted G3
   WITH/WITHOUT design** (for example, two independently run absolute-score
   or readiness receipts compared informally after the fact) ->
   `DESCRIPTIVE_NONCAUSAL_DELTA`. This stage is reachable precisely because
   stage 1 requires only "no second side at all," not "no controlled
   pairing"; a genuine two-sided, uncontrolled comparison always falls
   through stages 1-3 and lands here, never at `NO_MEASUREMENT`.
5. **Baseline and candidate evidence both exist, are comparable, are
   complete, and were produced under an admitted G3 WITH/WITHOUT pairing
   with a predeclared metric/unit/direction** -> `MEASURED_COMPARABLE_DELTA`.

No later stage can overturn an earlier stage's classification, and no stage
may be skipped: a round must be evaluated against stage 1 first, then 2,
then 3, then 4, before it can ever reach stage 5.

## Negative Cases

| Case | Required decision-layer behavior |
|---|---|
| Missing baseline or candidate | `NO_MEASUREMENT`; no `IncrementalValueAssessment` with a delta claim is emitted |
| Unmatched task sets, fixture versions, or any held-fixed condition (environment/policy/budget/time-window, and provider lane whenever it is not the declared intervention variable) | `INCOMPARABLE` with the specific mismatched dimension named |
| More than one dimension varies at once (the declared intervention variable plus any other dimension) | `INCOMPARABLE` with `MULTIPLE_UNCONTROLLED_VARIABLES`; the round can no longer attribute an observed difference to the declared intervention alone |
| No intervention variable or intervention-value binding declared for a two-sided round | `INSUFFICIENT_EVIDENCE`; two existing sides are not `NO_MEASUREMENT` merely because the intervention declaration is missing |
| Identical baseline and candidate intervention values | `INCOMPARABLE`; no actual intervention contrast is present |
| Missing or out-of-range minimum intersection coverage | `INSUFFICIENT_EVIDENCE`; the minimum must be predeclared with `0 < minimum <= 1` |
| Duplicate or ambiguous trace binding | `INSUFFICIENT_EVIDENCE`; a trace that could belong to either side is never assigned by inference |
| Held-out contamination | `INSUFFICIENT_EVIDENCE` with `REUSED_HELDOUT_SEARCH_DATA`, reused from G1's contamination rule; that side's evidence is never trusted even if otherwise complete |
| Unequal exposure or repeat counts | `INSUFFICIENT_EVIDENCE` using G3's own `repeatsObserved`/`repeatsRequired`; never rounded up, averaged, or treated as equivalent exposure |
| Missing cost units | The affected resource/cost dimension is excluded and logged `UNKNOWN_UNIT_EXCLUDED`; if no dimension remains with a valid unit, the round cannot reach `MEASURED_COMPARABLE_DELTA` |
| Incomplete runs | `INSUFFICIENT_EVIDENCE`, using G3's `INCOMPLETE_TRACE` defect where applicable; never partial-credited |
| Regression/negative gain | First-class, disclosed result: the round may classify as `MEASURED_COMPARABLE_DELTA` with a negative-direction outcome; a negative delta is never suppressed, hidden, or reclassified as `NO_MEASUREMENT` |
| Absolute-pass or readiness receipts presented as incremental value | Explicitly rejected as proof of a delta. Per the fixed classification precedence: if only one side's absolute-pass/readiness receipt exists with no second side to compare, the round is `NO_MEASUREMENT` (stage 1); if two sides' absolute-pass/readiness receipts both exist and are otherwise comparable and complete, the round is `DESCRIPTIVE_NONCAUSAL_DELTA` (stage 4), never `MEASURED_COMPARABLE_DELTA`, because an absolute-pass receipt alone is never an admitted G3 WITH/WITHOUT pairing; a single PASS/CERTIFIED/CLOSED_PASS_BOUNDED-shaped receipt can never by itself justify `MEASURED_COMPARABLE_DELTA` under either path |
| Review-cost counters presented as value delta | Rejected by design: review-cost/process counters (invocation count, quota usage) may populate only the disclosed resource dimension of an already-`MEASURED_COMPARABLE_DELTA` or `DESCRIPTIVE_NONCAUSAL_DELTA` round; they can never by themselves establish the classification, matching the review-cost owner's own accepted disclaimer |
| Ties / equal observed outcomes | `DESCRIPTIVE_NONCAUSAL_DELTA` (if evidence is comparable but not an admitted controlled pairing) or an explicitly disclosed zero/near-zero `MEASURED_COMPARABLE_DELTA` (if it is); no statistical significance or causal effect is inferred |
| Intersection of admitted fixtures below the round's declared minimum coverage | `INCOMPARABLE` with `INTERSECTION_BELOW_DECLARED_MINIMUM`; never aggregated on the narrowed subset regardless of apparent confidence |
| Empty intersection of admitted fixtures | `INSUFFICIENT_EVIDENCE` with `EMPTY_INTERSECTION`; distinct from a below-threshold-but-nonempty intersection |
| Intervention variable and a held-fixed condition both vary at once | `INCOMPARABLE` with `MULTIPLE_UNCONTROLLED_VARIABLES`; never attributed to the declared intervention alone |
| Numeric confidence/uncertainty figure requested without a defined estimator | Rejected; report discloses only descriptive repeat counts (`repeatsObserved`/`repeatsRequired`), never a derived confidence value, until a future tranche defines and cites a concrete estimation method |

## Provenance Fingerprint And Invalidation Triggers

`comparabilityFingerprint = SHA-256(canonicalVersion | interventionVariable |
baselineId | candidateId | fixtureSetContentHash | environmentDescriptorHash
| policyId | budgetCeilingDeclaration | timeWindowDeclaration |
heldFixedProviderLaneId)`, computed once per comparison round and attached
to every evidence record. `interventionVariable` names which one dimension
this round is permitted to vary (for example `PROVIDER_LANE`,
`CAPABILITY_CHANGE`, `DELEGATION_DECISION`, or `TOPOLOGY_CHANGE`).
`heldFixedProviderLaneId` is included in the fingerprint only when
`interventionVariable != PROVIDER_LANE`; when the provider/model lane
itself is the declared intervention variable, that field is the explicit
sentinel `NOT_HELD_FIXED_IS_INTERVENTION` and is excluded from the
comparability check between baseline and candidate.

`provenanceFingerprint = SHA-256(canonicalVersion | comparabilityFingerprint
| baselineInterventionValueHash | candidateInterventionValueHash |
classification | orderedEvidenceEnvelopeHashes[] | dimensionDeclarationHash)`,
attached to every emitted `IncrementalValueAssessment`.

**Invalidation triggers** (any one marks the assessment `STALE`, never
auto-mutates or auto-promotes a candidate):

- fixture-set content hash changes for the bound population;
- baseline or candidate identity, bound trace/result digest, or producer
  receipt changes;
- environment descriptor, policy, provider-lane identity, budget ceiling
  declaration, or time-window declaration changes;
- G3 admission or grading result for either side changes (for example, a
  re-grade after a G3 defect repair);
- the review-cost owner's disclosed counters for the bound population are
  superseded by a later review round.

On any trigger, the owner's only required action is to mark the assessment
`STALE` and require a fresh `IncrementalValueAssessment` before the prior
classification is relied on again; it never writes a new configuration,
never retriggers a live call, and never silently keeps serving a stale
classification without a visible `STALE` marker.

## G1, G3, And Review-Cost Boundaries (Explicit)

- G3 evidence is consumed **structurally** (its typed `BehavioralEvaluation`
  and `BaselinePairAdmissionEvaluation` outputs) as the required paired-input
  stream. The new owner supplies identity/binding G3 does not contain. This
  design does **not** claim G3 results by themselves establish a value
  delta; G3 supplies admission and grading only. G3 itself remains
  `CLOSED_PASS_BOUNDED_G3_PARKED`; this design adds no obligation back onto
  G3 and does not reopen it.
- G1 (empirical calibration owner composition) is **excluded from any
  dependency** and referenced only as a possible future, optional evidence
  source once separately implemented. No G1 output, interface, or promise is
  created or required by this design; G1's design is `CLOSED_PASS_BOUNDED` at
  `d87aadaec` (accepted by Local review), but its owner contract itself
  remains unimplemented -- no `task.class.calibration.owner.contract.ts` or
  successor path exists yet in this repository.
- Review-cost evidence (`CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`
  / `check_review_cost_control.py`) is used strictly as an **optional
  resource-dimension input**, never as classification evidence by itself,
  and never promoted beyond the disclaimed role stated in its own accepted
  claim boundary ("independence, criticality, and incremental value remain
  reviewer judgment").
- The lane-specific non-coder value standard (`W93-T1`) is **not** imported,
  extended, or generalized by this design; it is cited solely as the
  existing scoped counterexample per the work order's requirement to
  disclose existing scoped value proof and avoid a blanket absence claim.

## Findings / Position

All eight sources are read, hashed, and terminally reconciled (8/8, zero
drift, zero contradiction). G4-C1 remains unchanged at current source. The
owner question resolves to a new, thin composition/decision layer, not an
existing-owner extension and not a new grading/scoring engine: no current
owner can absorb a value-delta responsibility without contradicting its own
accepted claim boundary (review-cost) or exceeding its own stated scope (G3
admission-only; G1 design accepted `CLOSED_PASS_BOUNDED` but unimplemented).
Exactly one canonical composition owner is proposed, reusing G3's
WITH/WITHOUT admission and grading exactly as accepted, disclosing but never
modifying review-cost counters, and leaving G1 and G2/G6 explicitly deferred.
Full detail is in the Owner Matrix, Owner And Dependency Direction Graph,
Comparison Admission Contract, and Deterministic Classification States
sections above.

**R1 repair pass (this revision)**: reviewer verification identified four
internal-consistency defects in the initial submission, all corrected in
this same revision before any Local acceptance: (1) the classification
precedence made `DESCRIPTIVE_NONCAUSAL_DELTA` structurally unreachable
because stage 1 tested for "no controlled pairing" rather than "no second
side at all" -- fixed by narrowing stage 1 to test only for evidence
absence; (2) the contract required the provider/model lane to match exactly
while simultaneously claiming to measure incremental value of a provider
lane -- fixed by introducing an explicit per-round `interventionVariable`
declaration that separates the one permitted-to-vary dimension from every
held-fixed condition; (3) the intersection-of-admitted-fixtures aggregation
rule had no declared floor, permitting an arbitrarily narrow subset to
produce a delta -- fixed by adding a mandatory per-round minimum-coverage
threshold with explicit `INCOMPARABLE`/`INSUFFICIENT_EVIDENCE` outcomes
below it; (4) G1 was cited from its own raw, pre-repair design document
self-declaration (`COMPLETE_PENDING_REVIEW`) instead of current session
authority, and "repeat-count-derived confidence" implied an undefined
statistical estimator -- both corrected to cite G1 as `CLOSED_PASS_BOUNDED`
at `d87aadaec` and to disclose only descriptive repeat counts, not a derived
confidence figure. See the Risk / Corrective Action table for the paired
risk-to-fix mapping.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| Silently folding review-cost process counters into a value verdict | Design restricts review-cost evidence to an optional disclosed resource dimension only; it can never by itself establish a classification (see Negative Cases table) |
| Treating an absolute-pass or readiness receipt as proof of marginal value | Explicit negative case rejects this; at most `DESCRIPTIVE_NONCAUSAL_DELTA`, never `MEASURED_COMPARABLE_DELTA`, from a single-side receipt |
| Inventing a universal scalar benefit score contrary to the work order's explicit prohibition | Design uses five named classification states plus per-dimension unit/direction disclosure; no scalar aggregate score is defined anywhere in this design |
| G1/G3 boundary drift (implying G3 alone proves a delta, or creating a hard G1 dependency) | Explicit "G1, G3, And Review-Cost Boundaries" section states G3 supplies admission/grading only; G1 is optional and unimplemented, with zero interface obligation created |
| Contradicting the review-cost checker's own accepted disclaimer | Design never asks the review-cost checker to compute or score value delta; its text and behavior are read as unmodified evidence only |
| Circular or contaminated holdout selection undermining comparability | Reuses G1's SEARCH/HELD_OUT separation and `REUSED_HELDOUT_SEARCH_DATA` rejection pattern directly rather than inventing a second one |
| Successor implementation scope creep beyond this design | Successor manifest is capped at exactly five named paths and one separately governed implementation tranche; no automatic successor is authorized |
| Classification precedence accidentally routing a genuine, complete, two-sided but uncontrolled comparison to `NO_MEASUREMENT` instead of `DESCRIPTIVE_NONCAUSAL_DELTA` (R1 repair) | Stage 1 of the classification precedence was narrowed to test only for the *absence of a second side*, never for pairing quality; a two-sided uncontrolled comparison now falls through to stage 4 (`DESCRIPTIVE_NONCAUSAL_DELTA`) as intended |
| Contract requiring the provider/model lane to match exactly while the work order's own Purpose requires measuring incremental value *of* a provider lane (R1 repair) | Introduced an explicit per-round `interventionVariable` identity in the fingerprint; its baseline/candidate values are bound in provenance and excluded from held-fixed equality comparison. Provider lane is held-fixed only when it is not the declared intervention variable |
| Paired aggregation over an intersection of admitted fixtures with no declared floor, permitting a delta on an arbitrarily narrow subset (R1 repair) | Added a mandatory per-round declared minimum intersection-coverage threshold with three disjoint outcomes (aggregate, `INCOMPARABLE` below threshold, `INSUFFICIENT_EVIDENCE` on empty intersection); a delta is never computed on a population narrowed below its own declared threshold |
| G1 status cited from the raw pre-repair design file's own self-declaration instead of current session authority (R1 repair) | G1 is now cited throughout as `CLOSED_PASS_BOUNDED` at material commit `d87aadaec` per the active handoff/session continuity record, not the unmodified design document's own `COMPLETE_PENDING_REVIEW` self-declaration |
| Undefined "repeat-count-derived confidence" implying a statistical estimator that does not exist in this design (R1 repair) | Replaced with an explicit statement that no confidence-interval/variance estimator is defined by this design; the report discloses only descriptive repeat counts until a future tranche defines and cites a concrete estimation method |

No unresolved risk blocks the `DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER`
disposition below.

## Terminal Disposition

**`DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER`**

All eight sources are read, hashed, and terminally reconciled (8/8, zero
drift, zero contradiction). Exactly one canonical composition owner is
proposed (a thin new decision layer that calls G3's admission/grading
functions and the review-cost owner's disclosed counters as read-only
evidence sources; no parallel grading/scoring/counter-tracking owner is
created). Dependency directions are explicit and one-way (decision layer
depends on G3 and, optionally, review-cost and a future G1; none of them
depends on or is modified by the new layer). Classification states, negative
cases, comparability fingerprint, holdout/contamination rule, and
provenance/invalidation are complete per the Evidence Requirements list. No
universal scalar benefit score or threshold is invented anywhere in this
design. The exact successor implementation manifest is below.

## Exact Successor Implementation Manifest

A later, separately governed implementation work order (not opened by this
design) would create exactly these paths, none of which exist yet in this
repository:

| Path | Role |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/incremental.value.owner.contract.ts` | pure decision-layer implementation: comparability precondition filter, paired aggregation, classification-state assignment, `IncrementalValueAssessment` emission |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/incremental.value.owner.contract.test.ts` | adversarial test suite covering every negative case in this design's Negative Cases table |
| `governance/compat/check_incremental_value_owner_evidence.py` | read-only evidence/schema checker mirroring `check_review_cost_control.py`'s narrow, evidence-shape-only enforcement pattern for the new owner's persisted evidence shape |
| `governance/compat/test_check_incremental_value_owner_evidence.py` | checker test suite |
| `docs/reference/agent_system_skills/CVF_INCREMENTAL_VALUE_OWNER_CONTRACT.md` | normative reference contract, mirroring the accepted G1 design's successor-contract structure |

No more than this one separately governed implementation tranche is implied.
No automatic successor is authorized by this design; a fresh GC-018
baseline/work order pair and operator checkpoint are required before any of
the five paths above is created.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is a worker-owned design/audit artifact
returned `COMPLETE_PENDING_REVIEW`, not a closure artifact. This document
cites `CLOSED_PASS_BOUNDED_G3_PARKED` and
`DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER` only as quoted facts
about the already-closed G3 T2 tranche and the accepted G1 design (sources
G4-S6/G4-S7); it does not itself close anything. Machine closure packaging
for this G4 T1 design tranche belongs to Local after the three returned
worker outputs are reviewed and materially committed, per the governing work
order's own Machine Closure Package section.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G4_T1_INCREMENTAL_VALUE_OWNER_COMPOSITION_DESIGN_2026-09-17.md` | still `DISPATCH_READY` pending Local review | N/A with reason: worker cannot close a work order |
| Completion or reviewer artifact | N/A with reason: not yet authored | N/A with reason: Local decides whether a separate completion review is needed | N/A with reason: pending Local |
| Roadmap state | active ACEL continuity | G4 T1 design tranche pending Local review; no roadmap state change made by this worker | N/A with reason: session-sync steward acts only after Local acceptance |
| Registry JSON | `docs/audits/CVF_ACEL_G4_T1_INCREMENTAL_VALUE_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-17.json` | 8/8 ledger rows, valid JSON (`python -m json.tool` exit 0) | PASS |
| Registry Markdown | this file | eight-source ledger, owner matrix, comparison admission contract, negative cases | PASS |
| External evidence digest | N/A with reason: no external evidence entered this internal G4 design tranche | zero external inputs consumed | N/A with reason |
| System loop interlock | N/A with reason: no runtime consumer exists | design only; no runtime mutation | N/A with reason: static design |
| Session continuity | active continuity sources | not updated by this worker | N/A with reason: session-sync steward acts only after Local acceptance |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Source ledger completeness | 8/8 exact hashes and terminal statuses | 8/8, all `READ`, zero drift | PASS |
| Owner composition | one canonical owner plus explicit dependencies | one thin decision layer; two REUSE dependencies (G3, review-cost evidence), one DEFER (G1), one REUSE-as-precedent (non-coder standard), zero REJECT_DUPLICATE proposals opened as new engines | PASS |
| Comparison admission contract | intervention/baseline, population, binding, comparability, dimensions, aggregation, missing-evidence, no/negative-effect, tie, provenance, invalidation all specified | complete per Comparison Admission Contract, Deterministic Classification States, Negative Cases, and Provenance Fingerprint And Invalidation Triggers sections | PASS |
| No universal scalar | forbidden by work order | zero scalar benefit score or threshold defined anywhere in this design | PASS |
| G1/G3/review-cost isolation | no merged contract or forced dependency | explicit boundaries section; G1 optional/unimplemented, G3 admission-only, review-cost disclosed-only | PASS |
| Existing scoped value proof disclosed | no blanket absence claim | `W93-T1` explicitly cited as existing scoped precedent, not imported | PASS |
| Provider authority | zero calls; forbidden | zero provider/live/benchmark/credential calls | PASS |
| Worker commit | forbidden; Local owns commit | zero `git add`/`git commit` executed | PASS |
| Manifest JSON validity | parses under `python -m json.tool` | exit code 0 | PASS |
| `DESCRIPTIVE_NONCAUSAL_DELTA` reachable | precedence stage 1 tests evidence absence only, not pairing quality | stage 1 narrowed to "no second side"; stage 4 reachable for genuine uncontrolled two-sided comparisons | PASS |
| Intervention variable vs. held-fixed separation | provider lane not required to match when it is the declared intervention | intervention identity is fingerprinted; its differing values are provenance-bound and excluded from held-fixed equality | PASS |
| Intersection-of-fixtures floor declared | no delta on an arbitrarily narrowed subset | mandatory per-round minimum coverage threshold with `INCOMPARABLE`/`INSUFFICIENT_EVIDENCE` outcomes below it | PASS |
| G1 status citation | current session authority, not raw pre-repair self-declaration | cited as `CLOSED_PASS_BOUNDED` at `d87aadaec` throughout | PASS |
| Confidence claim boundary | no undefined statistical estimator implied | descriptive repeat counts only; no numeric confidence figure without a defined future estimator | PASS |

## Claim Boundary

This audit is a documentation-only design decision. It does not implement,
execute, benchmark, call a provider, mutate a configuration, compute a real
incremental-value number, or authorize G1 implementation, runtime wiring,
public sync, or deployment. All dispositions are subject to independent
Local review before any successor work order.
