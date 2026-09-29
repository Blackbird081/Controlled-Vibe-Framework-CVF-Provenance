# CVF ODVR-T2 Representative Operator Value Proof

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_VALUE_NOT_PROVEN

docType: review

Date: 2026-07-12

Batch ID: ODVR-T2-DISPATCH

executionBaseHead: `99c2875cd`

## Purpose

Measure whether the committed ODVR readout (`governance/compat/run_odvr_readout.py`,
accepted at ODVR-T1 material commit `16364f797`) reduces operator navigation
for a fixed set of canonical questions across one closed lane and one
parked/reopen lane, without losing or changing any canonical fact.

## Scope / Methodology

Per the Measurement Protocol in
`docs/work_orders/CVF_AGENT_WORK_ORDER_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_2026-07-12.md`,
the worker froze one 7-question operator question set (current lane
status/verdict; latest material decision and commit; claim boundary;
parked/blocked condition and checkable reopen condition when applicable; next
allowed move; public export disposition; source freshness), recorded
canonical expected answers with exact source anchors before timing either
path, then ran MANUAL first and COMPOSED second for two scenarios:

- Scenario 1 (closed lane): ODVR-T1 closure
  (`CVF_SESSION/state/entries/odvrT1Closure20260712.json`, material commit
  `16364f797`).
- Scenario 2 (parked/reopen lane): MAO-LIVE-T1 value pilot
  (`docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md`,
  `Status: REVIEWER_ACCEPTED_VALUE_NOT_PROVEN`, 5-condition reopen gate).

All raw events, step/file counts, elapsed milliseconds, composed JSON outputs,
and fact comparisons are recorded in the sibling JSON receipt
(`docs/evidence/odvr/CVF_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_RECEIPT_2026-07-12.json`)
and are independently recomputable from its `rawEvents` arrays.

## Design Note: Composer Has No Lane-Scoping Parameter

The committed CLI (`python governance/compat/run_odvr_readout.py --json`)
always composes a readout from the entire repository's generated state; it
has no argument to scope composition to one named lane. For Scenario 1 (the
CLI's actual highest-eligible-`stateOrder` target at execution time), the
worker used the CLI directly. For Scenario 2, invoking the unscoped CLI would
not measure the MAO-LIVE lane at all (it would return the same Scenario-1
answer again, since MAO-LIVE is not the globally-highest eligible entry). The
work order's Measurement Protocol step 4 explicitly permits using "the
committed helper/CLI or its injected composer for the same scenario," so the
worker invoked `run_odvr_readout.build_odvr_readout()` directly (the pure,
already-committed composer function, unmodified) with `ComposerInputs` scoped
to only the three MAO-LIVE state entries. This is not a new implementation;
it is the existing committed function called with a smaller, honestly-scoped
input, matching the same code path the CLI itself uses internally.

## Findings / Position

**Scenario 1 (closed lane): 3 of 7 facts preserved; 4 facts mismatched or
lost.**

- Q1 (status), Q2 (decision+commit), Q7 (freshness): MATCH between MANUAL and
  COMPOSED.
- Q3 (claim boundary): MISMATCH. The composed value is a shorter state-entry
  summary, not the canonical completion-review Claim Boundary answer. Semantic
  similarity does not satisfy the exact fact-preservation threshold.
- Q4 (parked/reopen condition): MISMATCH. The composed
  `parkedOrBlockedConditions` array contains one sentence, but it is the
  *current session's* next-move prose (about the ODVR-T2 dispatch itself),
  not a lane-scoped answer about ODVR-T1. MANUAL correctly reports "N/A" for
  this closed lane.
- Q5 (next allowed move): MISMATCH. `canonicalNextAllowedMove` returns the
  global session's next move, not the lane-specific `nextAllowedMove` that
  the cited state entry (`odvrT1Closure20260712.json`) itself carries.
  MANUAL reads the correct lane-scoped value directly from the entry.
- Q6 (public export disposition): FACT LOST. The T0 JSON Schema has no field
  at all for public export disposition. This is answerable by MANUAL (reads
  `## Public Export Disposition` directly from the cited artifact) but is
  categorically unanswerable from any composed output, regardless of
  implementation correctness.

**Scenario 2 (parked/reopen lane): 0 of 7 facts preserved.**

The three MAO-LIVE state entries store their `value` as a plain string
(free-form summary prose), not as an object carrying `materialCommit` plus a
governed artifact path field. The T1 composer's eligibility rule (correctly,
per its own contract) excludes such entries, so the composed output is
`MISSING_SOURCE` with every substantive field literally `"UNKNOWN"`. Every
one of the 7 canonical facts - status, decision+commit, claim boundary, the
5-condition reopen gate, next allowed move, public export disposition, and a
true freshness signal - is recoverable only from MANUAL, not from the
composed output. The composed output is schema-valid and its
`MISSING_SOURCE`/fail-closed behavior is contractually correct (it does not
guess), but it provides zero usable answers for this lane.

**Step/file counts, not just facts, also do not favor the composed path
consistently.** In Scenario 2, the COMPOSED path required as many
file-reads (3) and the same step count (4) as MANUAL (4 files, 4 steps),
because scoping the composer to the correct lane still required first
reading each raw state entry to construct the injected input - the CLI
itself would have used 0 explicit file reads for the *wrong* answer. Only in
Scenario 1 did COMPOSED reduce steps (1 vs 4) and files (0 vs 3).

## Risk / Corrective Action

The dominant risk is that the composed readout's schema and lane-selection
design conflate "the single globally-latest material decision across the
whole repository" with "the operator's currently-relevant lane." An operator
asking "what happened with MAO-LIVE?" cannot get that answer from the
composed output at all today; they must already know to read the roadmap and
its state entries directly, at which point the composed tool has provided no
navigation reduction and one categorical fact loss (Q6) even in its best
case (Scenario 1). Corrective options for the reviewer to consider, none of
which this worker is authorized to implement: (a) add a lane/entry selector
argument to the CLI so the composer can be pointed at any named entry, not
only the globally-latest one; (b) add a `publicExportDisposition` field to
the T0 schema and composer; (c) accept the current scope as intentionally
narrow (single-latest-decision only) and update the ODVR roadmap's Required
Readout Contract to state that explicitly rather than implying full
cross-lane coverage.

## Target / Source

- `governance/compat/run_odvr_readout.py` (ODVR-T1 composer, unmodified, read
  and invoked only).
- `docs/reference/operator_decision_value_readout/CVF_ODVR_T0_READOUT_SCHEMA.json`
  (T0 schema, read and validated against only).
- `CVF_SESSION/state/entries/odvrT1Closure20260712.json`,
  `CVF_SESSION/state/entries/maoLiveRoadmapProposed20260712.json`,
  `CVF_SESSION/state/entries/maoLiveT1Dispatch20260712.json`,
  `CVF_SESSION/state/entries/maoLiveT1Closure20260712.json` (canonical
  scenario evidence, read only).
- `docs/reviews/CVF_ODVR_T1_DETERMINISTIC_LOCAL_COMPOSER_COMPLETION_2026-07-12.md`,
  `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md`
  (canonical fact sources, read only).

## Decision Matrix

| Criterion | Scenario 1 | Scenario 2 | Roadmap threshold |
|---|---|---|---|
| Files read: COMPOSED < MANUAL | 0 < 3 (PASS) | 3 = 4 (roughly equal, not clearly fewer) | required |
| Steps: COMPOSED < MANUAL | 1 < 4 (PASS) | 4 = 4 (not fewer) | required |
| Zero fact loss/change | FAIL (Q4, Q5 changed meaning; Q6 lost entirely) | FAIL (all 7 facts lost) | required |

Per the roadmap's Acceptance Criteria ("T2 may recommend continued use only
if the composed path reduces file reads and operator steps without losing or
altering a canonical fact"), both scenarios fail the fact-preservation
requirement, and Scenario 2 additionally fails the file/step-reduction
requirement.

## Independent Reviewer Decision

`VALUE_NOT_PROVEN`.

The reviewer independently recomputed all four event totals, reran the 22-test
suite and worker-return fast gate, inspected both composed outputs, and checked
the canonical sources. The reviewer corrected Scenario 1 from 4/7 to 3/7
because Q3 was only semantically similar, not an exact canonical answer. Both
scenarios therefore fail the zero-fact-loss threshold, and Scenario 2 also
fails the required step reduction. No repair within this evidence-only tranche
can convert the result to value-positive.

## Tests / Gates Run

```
python -m unittest governance.compat.test_run_odvr_readout -v
-> Ran 22 tests in 0.762s, OK (22/22 pass; no composer/test file was edited)

python governance/compat/generate_active_session_state.py --check
-> ACTIVE_SESSION_STATE aggregate and bootstrap read model match generated sources. (no drift)

Both composed outputs (Scenario 1 CLI output; Scenario 2 injected-composer output)
validated against docs/reference/operator_decision_value_readout/CVF_ODVR_T0_READOUT_SCHEMA.json
-> PASS for both

Receipt raw-event recomputation: stepCount == len(rawEvents) and
filesRead == count(FILE_READ actions) verified programmatically for all 4 traces
-> PASS for all 4

Secrets scan of receipt JSON for api_key/apikey/secret/password/bearer/access_token
-> only the scan-description sentence and unrelated policy prose ("no secret/policy
   regression") matched; no actual secret value present
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | required review-section headings, public export disposition tokens, epistemic process block sections |
| gateRunPurpose | confirmatory evidence after source-backed authoring |
| claimBoundary | ODVR-T2 measurement report only |

## Epistemic Process Block

### Expected Result / Prediction

The committed ODVR-T1 composer would likely reduce navigation for the exact
scenario it was built and tested against (the globally-latest material
decision, i.e. Scenario 1's closed lane), but might not generalize cleanly to
an arbitrary named lane not currently at the top of the generated state order.

### Evidence Comparison

Measurement confirmed both halves of the prediction: Scenario 1 showed a real
file/step reduction (0 files/1 step vs 3 files/4 steps) with partial but
incomplete fact preservation (3/7), while Scenario 2 showed no fact
preservation (0/7) and no clear file/step reduction, because the MAO-LIVE
lane's state entries do not match the composer's eligibility shape at all.

### Contradiction Or Gap Disposition

No canonical source contradiction was found. A genuine design gap was found
and is documented, not silently resolved: the T0 schema has no field for
public export disposition, and the composer has no lane-scoping input.

### Claim Update

ODVR-T2 evidence does not currently support a positive operator-value claim
for the committed readout across representative lanes; the worker proposes
`VALUE_NOT_PROVEN`, subject to the independent reviewer's own recomputation
and terminal decision.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | independent reviewer/closer |
| Provider or surface | local private provenance repository |
| Session or invocation | ODVR-T2 reviewer closure 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | canonical reads, JSON recomputation, tests, governance gates, apply_patch |
| Target paths | three worker outputs plus reviewer-owned baseline, work order, and roadmap closure |
| Allowed scope source | ODVR-T2 Reviewer Closure Conversion |
| Before status evidence | exactly three untracked worker outputs at `99c2875cd` |
| After status evidence | reviewer-corrected value-negative material closure prepared for commit |
| Diff evidence | receipt recomputation, 22 tests, worker-return fast gate, status and commit steward |
| Approval boundary | reviewer closure only; no implementation repair or UI authorization |
| Claim boundary | ODVR-T2 evidence closure and terminal value verdict |
| Agent type | reviewer/closer role |
| Invocation ID | odvr-t2-reviewer-closure-2026-07-12 |
| Expected manifest | three worker outputs plus reviewer-owned closure paths |
| Actual changed set | checked by git status and commit steward before commit |
| Manifest delta | reviewer count correction and closure conversion within ownership |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private measurement report. Public-sync boundary: this report and its
sibling receipt are not copied, committed, or pushed to any public-sync
repository by this tranche.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ODVR_T2_REPRESENTATIVE_OPERATOR_VALUE_PROOF_2026-07-12.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this report | `Status: REVIEWER_ACCEPTED_VALUE_NOT_PROVEN` | PASS |
| Roadmap state | `docs/roadmaps/CVF_OPERATOR_DECISION_AND_VALUE_READOUT_ROADMAP_2026-07-12.md` | `Status: CLOSED_VALUE_NOT_PROVEN` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no mutation; aggregate drift check passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no mutation required | PASS |
| External evidence digest | N/A with reason: internal local measurement | no external evidence | N/A with reason |
| System loop interlock | T2 receipt and canonical sources | value threshold fails without mutation | PASS |
| Session continuity | separate session-sync after material commit | not part of material closure | N/A with reason |

## Claim Boundary

This report measures navigation cost and fact preservation for the committed
ODVR-T1 composer against two representative scenarios only. It does not
authorize any composer change, UI/Web surface, provider/live call, state
mutation, public-sync, or outside-source absorption, and it does not itself
constitute the terminal value verdict - that is the independent reviewer's
sole decision per the Review Gate.
