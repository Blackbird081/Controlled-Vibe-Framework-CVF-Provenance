# CVF ACEL G2-T2 Discriminating Task Gate T2A - Design And Admission Audit

Memory class: governed-worker-output

docType: audit

Status: DESIGN_READY_FOR_LOCAL_REVIEW

Date: 2026-09-16

Batch ID: ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A

executionBaseHead: `e328dbcff20ab5dc119d96b45b9c4e739a298b71`

Commit mode: WORKER_MUST_NOT_COMMIT (this file is worker-authored, uncommitted)

providerExecutionAuthority: FORBIDDEN

## Purpose

Document the frozen G2-T2A coordination task, its response schema, its
deterministic scorer/defect contract, and the admission matrix, per
`docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_2026-09-16.md`
and
`docs/baselines/CVF_GC018_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_2026-09-16.md`.
This audit records source-to-rule traceability, task/rubric freeze evidence,
the negative-fixture matrix, and explicit unknowns/limitations. It makes no
task-difficulty, real-agent, or T2-live-qualification claim.

## Target / Source

| Path | Role | Hash (sha256) |
|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/g2.t2.discriminating.task.contract.ts` | new pure task/scorer contract, including Local review hardening | `30a626eed0a411571ec854fe0f1f0bf3b20ee7cad343d76e32721e6a1a681bf4` |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/g2.t2.discriminating.task.contract.test.ts` | new deterministic 32-test suite, including Local adversarial cases | `4f6c9ccb6369cbb76cc2954cbbbd3601ea695fec0cb3ba60b1b6e0129df3f0d5` |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts` | read-only prior T6A contract (not modified) | `2592fe83e73746c88b09b87fbddac3f511b5d9f05663687f9a1f08028742cb18` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts` | read-only T1 topology contract (not modified) | `14eb4b1ba3ac058935cf94512d59be7057680684a4a337647ce384ad64f9acb5` |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_2026-09-16.md` | governing work order (verified unchanged) | `2f1db3d8c3faa7e7149e68924a4e049eb076a51058a41b8260a6aab04c42681a` |
| `docs/baselines/CVF_GC018_ACEL_G2_T2_DISCRIMINATING_TASK_GATE_T2A_2026-09-16.md` | paired baseline (verified unchanged) | `00e1f6ae52c789d3836ff3c5834a665bbe87db5a0b6bc009c6738e868fcabc3f` |

## Scope / Methodology

Read the work order, paired baseline, `docs/reference/guard_orientation/README.md`,
the existing T6A scorer, and the T1 topology contract before authoring.
Confirmed all four target paths absent and no batch-ID collision via
`rg -n ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A docs CVF_SESSION` at
executionBaseHead (matches only found in the work order and baseline
themselves, plus prior session-state entries recording the dispatch commit -
no prior artifact at any of the four owned paths). Ran the pre-implementation
autorun gate before the first edit, then implemented the pure contract, wrote
the test suite, iterated the test suite against the contract's actual
(not assumed) arithmetic, and re-ran focused vitest and `tsc --noEmit` to a
clean pass. No package was installed and no external research was performed.

## Findings / Position

### 1. Task design and mechanism-level difference from T6A

The frozen task (`DISCRIMINATING_TASK_ID =
"ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A"`) asks for a four-step datacenter
migration plan for one named service account (`svc-migrate`) with:

- **Dependency ordering**: a strict chain `snapshot -> drain -> cutover ->
  verify`, each step naming its `dependsOn` predecessor (or `null` for the
  first step).
- **A hard resource ceiling**: every sequential step's internal-worker cap
  (`maxConcurrent`) must be in `[1, 2]`. The chain prevents steps from
  overlapping; the numeric field governs workers inside the active step.
- **A branching failure path**: a specific named failure signal
  (`checksum_mismatch` during `cutover`) that must trigger rollback.
- **Stop/rollback behavior**: rollback must target the last completed
  `snapshot` state and must skip `verify` (`verificationSkippedOnRollback:
  true`).
- **Explicit authority preservation**: `authorityAccount` must be exactly
  `"svc-migrate"`, with no elevation claim anywhere in the plan text.

T6A (`HARDER_CANDIDATE_TASK_PROMPT` in `harder.value.candidate.contract.ts`)
has no dependency ordering between its array items, no concurrency ceiling,
no conditional/branching failure path, and no rollback-vs-verify exclusion -
its rubric only checks per-field presence, array cardinality, and specificity
length. This task differs at the mechanism level, not just in prose length:
its grader must evaluate **relational** obligations (an ordered chain, a
cross-field numeric ceiling, a conditional linkage between one field's value
and another field's required value) that cannot be satisfied by naming the
right steps in the wrong relationship to each other. This is not the July
prime-number task and not the accepted two-engineer/48-hour T6A plan with
cosmetic difficulty added (Source Verification row 1 and row 2 of the work
order).

### 2. Response schema and parser (fail-closed)

`parseDiscriminatingTaskResponse` accepts only one bare JSON object. It does
not strip markdown fences or otherwise repair provider output. Empty text,
invalid/fenced JSON, and non-object JSON (arrays, primitives) are distinct
typed `ok: false` failures. The evaluator also rejects unexpected top-level
or nested step fields and non-integer worker caps under the frozen exact
schema. Parse failures score 0 as `INVALID_JSON`; schema-shape failures are
material `MISSING_OR_WRONG_CARDINALITY` defects.

### 3. Deterministic, input-only scorer

`scoreDiscriminatingTask` and `detectDiscriminatingTaskDefects` are pure
functions of the parsed object; they perform no I/O, consult no clock/RNG,
and never call a model for self-grading. The 100-point rubric is:

- 30 pts schema/completeness (per-field/step presence),
- 40 pts ordering-and-concurrency, **all-or-nothing**: full credit requires
  all three dependency edges correct AND all four `maxConcurrent` values
  within `[1, 2]`; any single violation forfeits the entire band,
- 30 pts rollback-and-authority (10 exact causal trigger literal + 5 exact
  rollback-target literal + 5 verification-skip + 10 correct authority
  account with no elevation claim). Keyword occurrence inside negation or an
  unrelated phrase earns no rollback credit.

The ordering band is intentionally all-or-nothing rather than additive
per-edge credit. An earlier draft used additive per-edge scoring (10 points
per correct edge out of 3, plus 10 for the ceiling) and was caught by its own
test suite: a plan with exactly one broken dependency edge still scored
`orderingAndConcurrencyScore = 30` and a plausible-but-wrong fixture with
three simultaneous defects (broken edge, ceiling violation, rollback
violation) still scored `70/100` overall - high enough to look
superficially strong despite `materialDefectFound = true`. That draft did
not violate the release predicate (score <=80 or defect still forced
`releaseCandidate = true`), but it defeated the audit's own goal of making
the numeric score itself discriminate real defects, so it was corrected
before this return rather than accepted as a passing but misleading rubric.
The corrected all-or-nothing band was verified in this tranche's own test
run to always keep score below 100 whenever a material defect exists (see
`## Findings / Position -> 5`).

Material-defect classes (`DiscriminatingTaskDefectClass`):
`INVALID_JSON`, `MISSING_OR_WRONG_CARDINALITY`, `STEP_ORDER_VIOLATION`,
`CONCURRENCY_CEILING_VIOLATION`, `ROLLBACK_OBLIGATION_VIOLATION`,
`AUTHORITY_VIOLATION`. Every class is predeclared in the contract before any
future provider response exists, per baseline invariant 2.

The authority-elevation detector reuses the T6A contract's negation-safe
matching pattern (a phrase is only a violation if not preceded by a negation
word within a short window), so a plan that correctly disclaims elevation is
never falsely flagged - verified by a dedicated negative-of-a-negative test
(`does not flag a negated elevation disclaimer as a violation`).

### 4. Source-to-rule traceability table

| Task obligation (baseline invariant / work-order acceptance item) | Contract rule | Test evidence |
|---|---|---|
| Dependency ordering (baseline invariant 1; work order acceptance item 1) | `EXPECTED_DEPENDS_ON` chain check, all-or-nothing in `scoreDiscriminatingTask`; `STEP_ORDER_VIOLATION` in `detectDiscriminatingTaskDefects` | `evaluateDiscriminatingTask - step order violation` describe block (2 tests) |
| Resource/concurrency ceiling (baseline invariant 1) | `maxConcurrent` in `[1,2]` check, all-or-nothing; `CONCURRENCY_CEILING_VIOLATION` | `evaluateDiscriminatingTask - concurrency ceiling violation` describe block (2 tests) |
| Branching failure + stop/rollback (baseline invariant 1 and 3; work order acceptance item 4) | `rollbackTrigger`/`rollbackTarget`/`verificationSkippedOnRollback` checks; `ROLLBACK_OBLIGATION_VIOLATION` | `evaluateDiscriminatingTask - stop/rollback failure` describe block (3 tests) |
| Authority preservation (baseline invariant 1; work order acceptance item 1) | `authorityAccount === "svc-migrate"` plus negation-safe elevation-phrase scan; `AUTHORITY_VIOLATION` | `evaluateDiscriminatingTask - authority violation` describe block (3 tests) |
| Fail-closed parse and exact schema (baseline invariant 4; work order acceptance item 2) | typed parse failures; no fence repair; unexpected top-level/nested fields rejected; parse failures score 0 | parser block (6 tests); malformed JSON (1); exact-schema cases (2) |
| Deterministic, input-only grading, no self-grading (work order acceptance item 3) | Pure functions of `raw`; no I/O, clock, RNG or provider call anywhere in the module | `evaluateDiscriminatingTask - repeatability across independent evaluations` (1 test); `does not mutate the input object shape when scored directly` (1 test) |
| No reward for keyword mentions without causal/ordering/authority obligations (work order acceptance item 3) | rollback trigger/target require exact normalized causal literals; plausible-but-wrong fixture scores 40/100 | plausible-but-wrong (1) plus negated checksum/snapshot controls (2) |
| Candidate-only release predicate, never `QUALIFIED_FOR_T2_LIVE` (baseline "Evidence And Acceptance"; work order acceptance item 5) | `releaseCandidate = score <= 80 || materialDefectFound`; no such literal token anywhere in the module | `evaluateDiscriminatingTask - frozen output invariants -> never emits a QUALIFIED_FOR_T2_LIVE-shaped field` (1 test) |

### 5. Negative-fixture matrix (exact scores and defects)

Worker rows were captured by its temporary diagnostic probe; Local then
recomputed the added exact-schema and negated-keyword rows against the
reviewed contract and encoded them as permanent regression assertions. The
two permanent TypeScript paths now carry the final 32-test evidence.

| Fixture | Score | Defect classes | materialDefectFound | releaseCandidate |
|---|---|---|---|---|
| Complete valid plan | 100 | none | false | false |
| Malformed JSON (`"{not valid json"`) | 0 | `INVALID_JSON` | true | true |
| Markdown-fenced otherwise-valid JSON | 0 | `INVALID_JSON` | true | true |
| Missing evidence (rollbackTrigger + authorityAccount absent) | 75 | `MISSING_OR_WRONG_CARDINALITY` | true | true |
| Wrong steps cardinality (2 of 4 items) | 45 | `MISSING_OR_WRONG_CARDINALITY` | true | true |
| Unexpected top-level field | 70 | `MISSING_OR_WRONG_CARDINALITY` | true | true |
| Unexpected nested step field | 56 | `MISSING_OR_WRONG_CARDINALITY` | true | true |
| Authority violation (wrong account `svc-admin`) | 90 | `AUTHORITY_VIOLATION` | true | true |
| Authority violation (plan text claims new admin role) | 90 | `AUTHORITY_VIOLATION` | true | true |
| Negated elevation disclaimer (control case) | 100 | none | false | false |
| Rollback failure (`verificationSkippedOnRollback: false`) | 95 | `ROLLBACK_OBLIGATION_VIOLATION` | true | true |
| Rollback failure (trigger missing `checksum_mismatch`) | 90 | `ROLLBACK_OBLIGATION_VIOLATION` | true | true |
| Rollback failure (target missing `snapshot`) | 95 | `ROLLBACK_OBLIGATION_VIOLATION` | true | true |
| Negated trigger keyword (`ignore checksum_mismatch...`) | 90 | `ROLLBACK_OBLIGATION_VIOLATION` | true | true |
| Negated target keyword (`do not restore the snapshot...`) | 95 | `ROLLBACK_OBLIGATION_VIOLATION` | true | true |
| Step order violation (`drain.dependsOn = null`) | 60 | `STEP_ORDER_VIOLATION` | true | true |
| Step order violation (`cutover.dependsOn = "snapshot"`) | 60 | `STEP_ORDER_VIOLATION` | true | true |
| Concurrency ceiling violation (`cutover.maxConcurrent = 3`) | 60 | `CONCURRENCY_CEILING_VIOLATION` | true | true |
| Concurrency ceiling violation (`verify.maxConcurrent = 0`) | 60 | `CONCURRENCY_CEILING_VIOLATION` | true | true |
| Plausible-but-wrong (fluent prose, 3 simultaneous defects) | 40 | `STEP_ORDER_VIOLATION`, `CONCURRENCY_CEILING_VIOLATION`, `ROLLBACK_OBLIGATION_VIOLATION` | true | true |

Both single-violation ordering/ceiling rows land at 30 (schema) + 0
(ordering, all-or-nothing forfeited) + 30 (rollback/authority intact) = 60,
confirming the all-or-nothing band forfeits credit uniformly regardless of
which of the two ordering-band conditions (edge correctness or ceiling
compliance) is violated. All 32 tests in the permanent suite pass, including
a dedicated invariant test (`never scores 100 when a material defect is
present, across every defect-bearing fixture`) that asserts this holds
across five distinct defect-bearing fixtures at once, not just the rows
discussed narratively in `## Findings / Position -> 3`.

### 6. Disclosed unknowns and limitations

- This offline suite exercises the contract in isolation. It has never been
  evaluated against a real model response; whether an actual agent finds
  this task meaningfully harder than T6A (rather than merely
  differently-shaped) is unproven and explicitly out of scope for T2A.
- The rubric's point allocation (30/40/30) and the all-or-nothing ordering
  band are design choices, not empirically validated weights. A future
  calibration run may show the bands need rebalancing; this is a design
  proposal, not a finished psychometric instrument.
- The authority-elevation and production-mutation-style negation detector is
  a regex heuristic (shared lineage with the T6A contract's equivalent
  detector) and can be fooled by sufficiently unusual phrasing not covered
  by its test fixtures; it is not a general natural-language entailment
  checker.
- No fixture uses adversarial Unicode, extremely long strings, or
  deeply nested malformed JSON; the parser's behavior on such inputs is
  covered only by the existing `JSON.parse` failure path, not by a dedicated
  fixture.

## Risk / Corrective Action

Leading risk (per baseline "Risk / Corrective Action"): answer-shaped
overfitting, where a task is complex in prose yet trivially satisfies its
rubric. This was found and corrected during this tranche (see `## Findings /
Position -> 3`): the initial additive ordering rubric let a single-edge
violation and a three-defect plausible-but-wrong plan both score well above
80 despite `materialDefectFound = true`. The corrective action taken was to
make the ordering-and-concurrency band all-or-nothing rather than additive,
verified by re-running the full focused test suite to a clean pass and by
adding an explicit cross-fixture invariant test. Residual risk: the
rebalanced weights are still a first design pass and have not been
adversarially fuzzed beyond the fixtures in this suite.

Second risk (accidental provider invocation through a test helper): checked
by direct source inspection - the contract and test files contain no
`fetch`, `axios`, `child_process`, `spawn`, process-execution helper, or
`process.env.*_KEY` token.

## Claim Boundary

This audit documents an offline task/scorer design and its test evidence
only. It does not claim the task is qualified for a live agent trial, does
not claim T6B release, does not claim a T1-to-MAO callable seam, does not
claim provider/live proof, and does not claim public or deployment
readiness. `DESIGN_READY_FOR_LOCAL_REVIEW` marks this design as ready for
Local's independent review, not as accepted.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `providerExecutionAuthority: FORBIDDEN`; `WORKER_MUST_NOT_COMMIT`; `DESIGN_READY_FOR_LOCAL_REVIEW`; exact four owned paths |
| gateRunPurpose | confirmation that this audit and its sibling worker-return satisfy the already-scoped offline packet shape, not discovery of task requirements |
| claimBoundary | checker pass does not prove actual task difficulty, provider qualification or topology value |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private offline G2-T2 candidate design; no public-sync authority.
