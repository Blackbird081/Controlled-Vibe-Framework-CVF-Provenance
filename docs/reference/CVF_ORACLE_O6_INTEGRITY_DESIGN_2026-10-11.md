# CVF Oracle O6 Integrity Design

Memory class: bounded-design-reference
docType: reference
Status: DESIGN_PENDING_LOCAL_REVIEW
Date: 2026-10-11
Batch ID: CVF-ORACLE-O6-DESIGN-20261011
Dispatch base head: 140d73fd65b8d4fca30b609223bb9ff6b63cf5b1
Execution base head: bd13e1a8057cfbc6c753053b290cd21ee76c45e3
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
Work order: docs/work_orders/CVF_AGENT_WORK_ORDER_ORACLE_O6_DESIGN_2026-10-11.md

## Purpose

This design sets one bounded, opt-in precondition that a negative oracle must pass before its failure can be attributed to a product or worker defect. It answers the O6 finding: a negative fixture shared its initial and accepted pin objects, so its mutation changed both sides and created no drift, while the oracle still reported a result. The design names the existing owners, the precondition chain, the source-derived mutation contract, the planned cases, and the value decision. It implements no control.

## Scope / Applies To

The design applies to the reviewed-outcome consumer and to the Local independent-review oracle written against it. It is a subordinate reference. It creates no authoritative guard owner, no checker, no hook, no registry entry, and no generated aggregate. The named sources are read as pinned in the work order. Expense, S5, PLL, scoring, Gateway, source-R2, media, provider, public, deployment, and P11 items remain parked.

## Owner And Overlap Map

| Concern | Existing owner and source | What it already checks | Gap for O6 | Disposition |
|---|---|---|---|---|
| Oracle and evidence binding of an independent probe | docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md, section Oracle Fingerprint And Evidence Binding | worker and probe oracle digests and evidence references must be present and unequal | shape and distinctness only; substantive independence stays reviewer judgment | existing owner applies; no change |
| Probe admission fields | governance/compat/check_independent_review_probe_admission.py, PASS_ORACLE_DIGEST_FIELDS (line 394) and _normalize_identity (line 409) | actor, invocation, digest, and evidence separation at closure | does not inspect whether a negative fixture mutates the bytes it claims to mutate | existing owner applies; no change |
| Product invariants of the reviewed outcome | governance/compat/model_selection_reviewed_outcome.py, validate_outcome_record (line 701) and _cross_outcome (line 653) | record joins, repair attribution, review independence | does not test whether the oracle that drives it is valid | consumer only |
| Finding and disposition | docs/reviews/CVF_MODEL_SELECTION_ORCHESTRATOR_LEARNING_DISPOSITION_2026-10-11.md, O6 row and Candidate Proof section | names the aliased fixture and the five code expectations | design obligation only | finding owner |
| Historical mutation evidence | docs/reviews/evidence/model-selection-orchestrator-learning-20261011.json, boundedMechanismProbes.originalOracleMutation (lines 289 to 295) | originalPinObjectAliased true; acceptedMutationAlsoChangedInitialPin true | historical and retained | evidence owner |
| Acceptance join of this return | governance/compat/check_work_order_acceptance_ledger.py | requirement and proof join; observed Git paths | not semantic | existing owner applies |

Overlap conclusion: only one element is incremental. It is a reviewer precondition that a declared negative mutation changes exactly its declared bytes, on snapshots that share no mutable container, and reaches the real consumer. Source-assigned code discipline already belongs to the source-verification rules and to the independent reviewer. This design adds a reviewer checklist for that discipline and no new global rule.

## Failure Being Designed Against

Historical facts, retained and not re-run:

- The retained oracle source defines one product object (line 29) and places it in both initialReturn.artifacts and acceptedArtifacts inside one return statement (line 31). A mutation that edits the accepted pin in place therefore also edits the initial pin.
- The case product-repair-laundering (line 110) edits /outcome/acceptedArtifacts/0/sha256 through the setp helper (lines 33 to 37). Both sides change, no drift exists, and the case cannot demonstrate the intended REPAIR_ATTRIBUTION.
- The S2-R2 completion counts one fixture aliasing defect, two affected cases, and five corrected diagnostic expectations. The named sources do not enumerate the two cases or the five expectations, so this design does not name them.
- The historical oracle file matches the sourceSha256 pinned in the evidence file. Its raw initial results are not read by this design.

## Precondition Chain

Each step names its producer, verifier, consumer, failure disposition, and stop behavior.

| Step | Producer | Verifier | Consumer | Failure disposition | Stop behavior |
|---|---|---|---|---|---|
| P0 valid control | oracle author (Local reviewer) | reviewer checklist; helper only if separately admitted | validator CLI or API on the unmutated bytes | ORACLE_INVALID_CONTROL | stop every case built on this control |
| P1 independent snapshot | oracle author | precondition helper | none (in memory) | ORACLE_ALIASED_SNAPSHOT | stop before any mutation |
| P2 declared mutation | oracle author | declared case table | none | ORACLE_UNDECLARED_MUTATION | stop before any mutation |
| P3 actual changed bytes | precondition helper | canonical diff of the two parsed trees | none | ORACLE_NO_OP or ORACLE_SIBLING_DRIFT | stop before the consumer |
| P4 non-target invariants | precondition helper | pin and digest comparison of every unchanged Ref | none | ORACLE_SIBLING_DRIFT | stop before the consumer |
| P5 real consumer input | case runner | input digest and invocation/input binding | CLI path or API tree parsed from mutated bytes | ORACLE_CONSUMER_INPUT_MISMATCH | accept no result |
| P6 source-derived assertion | oracle author | static check of each code and pointer against validator source | reviewer | ORACLE_CODE_NOT_SOURCE_ASSIGNED, or a mismatch to be compared with the implementation | an oracle label is never an implementation defect |
| P7 attributed result | reviewer | first failure kept, never overwritten | later reviewer | PASS, an ORACLE_ label, or IMPLEMENTATION_DEFECT | record every attempt in order |

The ORACLE_ labels are design-local dispositions for oracle precondition failures. They are not validator diagnostic codes, must not join the validator code set, and must never be emitted as product diagnostics. A P0 to P5 failure is an oracle-level result. Only a case that passes P6 and reaches the consumer can show IMPLEMENTATION_DEFECT.

## Source-Derived Mutation Contract

1. Each negative case is data: a caseId, an explicit ordered mutation list (JSON pointer, SET/REMOVE/APPEND operation, and new value) and a source-assigned assertion. Ordinary drift cases declare one edit; compound malformed-sibling cases declare both edits and their joint intent before mutation. Undeclared edits remain oracle errors.
2. Independent snapshots: the control bytes are read once from a file. The control, before, and after trees come from separate json loads of the same bytes. A shallow copy is not acceptable. The helper compares the object identity of every dict and list in the before and after trees and requires the two sets to be disjoint.
3. Pin alias check: when a case names an initial Ref and an accepted Ref that correspond to the same product, the two objects must be distinct and must have equal canonical bytes before mutation. The original O6 failure is exactly this check failing.
4. Semantic delta: compare parsed trees recursively and collect the smallest edit paths: a changed scalar is its leaf pointer; added/removed key or appended index is that member pointer; replacement of a container by a scalar is the container pointer. Canonical ancestor digests are audit evidence, not extra edits. The resulting set must equal the declared mutation pointer set exactly. Unchanged siblings retain their structural values/digests; the named container replacement covers only its descendants. An empty set is ORACLE_NO_OP. Any extra pointer is ORACLE_SIBLING_DRIFT.
5. Unchanged pins: every locator and sha256 of every Ref outside the declared set must equal the control.
6. Code assertion: an expected code is admissible only if the validator emits that literal on a diagnostic call site. This worker's static literal scan found 18 such codes: ATTEMPT_HISTORY, ATTEMPT_JOIN, CHRONOLOGY, CONFIGURATION_DISPOSITION, COST_BASIS, COST_UNITS, DECISION_DRIFT, DECISION_JOIN, DUPLICATE_ID, ENUM, FORMAT, IDENTITY_BASIS, OUTCOME_INVARIANT, REPAIR_ATTRIBUTION, RETURN_INVARIANT, REVIEW_INDEPENDENCE, SHAPE, and TYPE. The loader and CLI section (lines 709 to 771) assigns INPUT_DEPTH, INPUT_ENCODING, INPUT_ERROR, INPUT_IO, INPUT_JSON, INPUT_SIZE, DUPLICATE_KEY, and NONFINITE_NUMBER. Every uppercase token that the historical oracle asserts is a literal in the validator source, except two non-code labels: an API mode name and an actor string.
7. Consumer binding: the mutated bytes are written to a scratch file. The runner records that file's SHA-256, runs the real CLI on that path or parses those exact bytes into the tree passed to validate_outcome_record, and binds the observed input digest to the mutated digest, distinct from the control digest. The unmutated P0 control is the explicit exception to digest inequality. This is a cooperative evidence contract, not runtime interception or race protection.

## Case Matrix

The eight planned cases from the work order are listed with their expected invariant. Expectations are readings of the validator source. They are not executed results, and the exact expected set is fixed at execution.

| Case ID | Precondition | Intended delta | Unchanged invariants | Actual consumer | Expected disposition | Source-assigned code |
|---|---|---|---|---|---|---|
| CTRL-VALID | P0 on the unmutated record | none | every pointer and every Ref | CLI --input | VALID_OUTCOME_RECORD_ONLY with exit 0 (profile Interface and Failure Contract, line 81) | none |
| TGT-INDEPENDENT-DRIFT | P1 snapshots distinct | SET /outcome/acceptedArtifacts/0/sha256 on the accepted object only, with no LOCAL_REVIEW repair row | every other pointer | CLI | one REPAIR_ATTRIBUTION at /outcome/acceptedArtifacts | REPAIR_ATTRIBUTION (validator line 675) |
| ALIAS-BOTH-SIDES | P1 alias check fails | the same SET applied through a shared object | none beyond the declared pointer | none reached | ORACLE_ALIASED_SNAPSHOT, since two pointers change | not applicable |
| NOOP-MUTATION | P3 | SET the sha256 to its current value | every pointer | none reached | ORACLE_NO_OP | not applicable |
| SIBLING-DRIFT | P3 and P4 | also SET /outcome/review/reviewedAt | every pointer except the declared one | none reached | ORACLE_SIBLING_DRIFT | not applicable |
| CODE-INVENTED | P6 | expected token UNREPAIRED_CLAIM, a hypothetical token never emitted by the validator | every pointer | none reached | ORACLE_CODE_NOT_SOURCE_ASSIGNED | none; the token is absent from the literal set |
| MALFORMED-SIBLING-RETAINED | P0 and P4 | SET /decision/candidates to null and SET /outcome/decisionId to a wrong identifier | every other pointer | CLI and API | DECISION_JOIN at /outcome/decisionId, plus diagnostics under the /decision prefix; the API must not raise | DECISION_JOIN (profile Decision And Attempt Joins, rule 1, line 48) |
| CONSUMER-ORIGINAL-BYTES | P5 | the mutated record is written to a scratch file, but the consumer is pointed at the control path | every pointer | CLI on the control path | ORACLE_CONSUMER_INPUT_MISMATCH; no result accepted | not applicable |

Notes on the expectations: in MALFORMED-SIBLING-RETAINED, DECISION_DRIFT may also fire because the digest is computed over the changed embedded subtree. The design requires only that the DECISION_JOIN sibling survives, so the exact expected set must be fixed from source at execution, not from this table.

## Alternatives, Value, And Cost

| Option | What changes | Incremental value | Cost and risk | Decision |
|---|---|---|---|---|
| A. No code change; documented reviewer checklist | this design only | covers the original failure class at the independent-review step; the Local review caught the original failure | zero code; relies on reviewer discipline; recurrence is not excluded mechanically | RECOMMENDED: smallest option the evidence supports |
| B. Opt-in helper: one standard-library module and one focused test file, called only by oracles that declare negative mutations | two new files and a case table | mechanical P1 to P5 for negative-heavy oracles | a new executable control that needs separate authority, a fresh baseline, and a core guard self-protection listing; cost not measured | DEFERRED_WITH_REASON |
| C. Global gate expansion: mutation checks in every probe admission or pre-dispatch gate | changes to shared gates | broad coverage | duplicates the probe-admission owner and applies to lanes with no negative oracle; not supported by evidence beyond one incident | REJECTED |

Reason for deferring B: the evidence is one observed incident in one lane. The Local review already caught it, and the value of B concentrates in oracles with many negatives, a pattern not yet observed to recur. Reopen trigger: a second mutation-validity defect in any oracle, or a planned negative oracle that the reviewer judges too large for manual P1 to P5 review.

Historically observed cost, not a benchmark: the S2-R2 completion records a Local review interval of about 297 seconds for one closure. No delivery, review, or rework time exists for the O6 design, and no savings claim is made.

Claim status:

| Claim | Status |
|---|---|
| the retained oracle aliased both pins | HISTORICALLY_OBSERVED and FRESHLY_VERIFIED in source by this worker |
| five diagnostic expectations were corrected | HISTORICALLY_OBSERVED as a count only |
| the validator literal set in the Source-Derived Mutation Contract | FRESHLY_VERIFIED by a static literal scan this session |
| the precondition chain would prevent the original failure | PROPOSED_ONLY |
| the cost or savings of any option | UNKNOWN; not measured |

## Rollout And Rollback Proposal

Now: documentary adoption only. Use the precondition chain P0 to P7 as a reviewer checklist for any future negative oracle. Rollback: revert the three outputs of this batch; no other file changes.

If option B is reopened: a separate baseline and work order are required; the exact helper and test paths must be listed; any governance/compat path needs a core guard self-protection authorization; focused tests replay only the eight planned cases against the retained fixture, not the historical suite; the Local reviewer decides acceptance. Rollback removes the helper and its test file. No existing gate is wired, so nothing else needs unwinding.

## Local Clarifications At Review

Local clarified mutation-list cardinality, minimal edit paths versus propagated ancestor hashes, and API parsed-byte/control binding. These are documentary repairs; the original worker return/evidence and submitted design hash are retained in the Local review evidence. P0-P7 verifier/helper labels describe proposed responsibility; the selected implementation is manual review, with executable helper deferred. No planned case was executed by this repair.

## Evidence Limits

- The twelve pinned sources and the historical oracle were verified by SHA-256. Hash equality does not show read depth; the read depth of each source is recorded in the evidence file.
- The historical oracle is ignored runtime input. Only its fixture function and case table were read. Its raw initial results were not read.
- No planned case was executed. Expectations are readings of validator source.
- No corpus completeness is claimed. The listed sources are named sources only.
- Runtime identity, effort mapping, token usage, and cost of this worker are not exposed to this session and are recorded as unknown.
- The release-continuity blocker (DR-04 and DR-05) seen at the first pre-implementation attempt was resolved by Local before this worker started. It lies outside the O6 design.

## Claim Boundary

Documentary design only. It is not an implemented control, not an executed oracle, not a validator change, and not a runtime, provider, public, deployment, or closure claim. Local owns the final technical disposition. This document is not a completion review and does not close the batch.

## Epistemic Process Block

Expected Result / Prediction: an opt-in precondition chain would classify the retained alias and sibling-drift negatives as oracle errors before any consumer result is attributed to a product or worker.

Evidence Comparison: source-pinned historical evidence and the fixture source show the alias. The validator literal scan confirms that the oracle's diagnostic tokens are source literals. The effectiveness of the precondition is unmeasured.

Contradiction Or Gap Disposition: the existing probe-admission owner checks digest and actor separation but not mutation validity. That gap is the incremental element. The five historical expectations are not enumerated in the named sources, so they are recorded as a count only.

Claim Update: design proposed. The recommendation is documentary adoption with the helper deferred. No implementation acceptance and no global prevention claim is made.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | INTERNAL_AGENT shared-workspace design worker, operator-started |
| Provider or surface | private shared workspace; no provider or external surface |
| Session or invocation | O6 design worker session, 2026-10-11 |
| Working directory | repository root |
| Command or tool surface | read-only source reads and hashes; static literal scan; pre-implementation gate; file writes to the three owned outputs; worker-return fast gate |
| Target paths | docs/reference/CVF_ORACLE_O6_INTEGRITY_DESIGN_2026-10-11.md; docs/reviews/CVF_ORACLE_O6_DESIGN_WORKER_RETURN_2026-10-11.md; docs/reviews/evidence/oracle-o6-design-worker-20261011.json |
| Allowed scope source | docs/work_orders/CVF_AGENT_WORK_ORDER_ORACLE_O6_DESIGN_2026-10-11.md, Write Ownership, released at bd13e1a80 |
| Before status evidence | HEAD bd13e1a8057cfbc6c753053b290cd21ee76c45e3; clean worktree; empty staged set |
| After status evidence | three untracked owned outputs; no tracked file modified |
| Diff evidence | git status --short before and after the three writes |
| Approval boundary | three documentary outputs only; no code, checker, hook, generator, registry, roadmap, session state, handoff, or historical evidence edit |
| Claim boundary | proposed documentary design; no implementation, execution, runtime, or provider claim |
| Agent type | INTERNAL_AGENT |
| Invocation ID | oracle-o6-design-worker-20261011 |
| Expected manifest | docs/reference/CVF_ORACLE_O6_INTEGRITY_DESIGN_2026-10-11.md; docs/reviews/CVF_ORACLE_O6_DESIGN_WORKER_RETURN_2026-10-11.md; docs/reviews/evidence/oracle-o6-design-worker-20261011.json |
| Actual changed set | docs/reference/CVF_ORACLE_O6_INTEGRITY_DESIGN_2026-10-11.md; docs/reviews/CVF_ORACLE_O6_DESIGN_WORKER_RETURN_2026-10-11.md; docs/reviews/evidence/oracle-o6-design-worker-20261011.json |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this batch |
