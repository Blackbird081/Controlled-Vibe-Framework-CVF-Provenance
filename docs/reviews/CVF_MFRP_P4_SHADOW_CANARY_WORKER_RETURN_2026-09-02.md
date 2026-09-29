# CVF MFRP-P4 Shadow Canary Worker Return

Memory class: governed-worker-dispatch

docType: review

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_MEASUREMENT_2026-09-02.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_MEASUREMENT_2026-09-02.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

Commit mode: WORKER_MUST_NOT_COMMIT

executionBaseHead: `d276cf4cd9b5bedb26b86625f42bfcbcb98afdea`

Worker terminal candidate: `COMPLETE_PENDING_REVIEW`

Reviewer disposition: `REVIEWER_ACCEPTED_CANARY_WINDOW_OPEN_BOUNDED`

Reviewer disposition history: round 1 `REVISE_BEFORE_CANARY_WINDOW_OPEN`
(P4-RV-1/2/3 plus the M0/M1 attribution gap; addressed in "Reviewer-Directed
Consolidated Correction Round" below), round 2 `REVISE_BEFORE_CANARY_WINDOW_OPEN`
(P4-RV-4, P4-RV-5; addressed in "Independent Reviewer Re-Review - Correction
Round 2" and the new "Correction Round 2 Repair" section below). This return
does not self-declare canary window acceptance or P5 readiness; both rounds'
dispositions remain the authority until an independent reviewer accepts this
repaired state.

## Purpose

Implement the accepted MFRP-P4 shadow-canary comparator, execute the first
real observation against the immutable accepted R1B-R2 evidence, and
establish the bounded checkpoint ledger, per the amended work order (trusted
outcome corrected to the exact literal
`REVIEWER_ACCEPTED_EVIDENCE_RETURN_TO_DESIGN_BOUNDED`) and its paired GC-018
baseline. This is a resume of a prior dispatch that correctly self-blocked
on a citation mismatch with zero writes; that stop is not repeated here
because the amendment corrects the cited token to the exact string present in
the accepted R1B-R2 return.

This document is the in-place consolidated correction over the prior
uncommitted worker return, now carried through two correction rounds over the
same original four paths. Round 1 discharged the independent reviewer's
`REVISE_BEFORE_CANARY_WINDOW_OPEN` adjudication (P4-RV-1, P4-RV-2, P4-RV-3,
and the M0/M1 attribution gap; see "Reviewer-Directed Consolidated Correction
Round" below for before/after evidence on each). Round 2's independent
re-review found the round-1 suite passing 73/73 but identified two further
causal false-linkage/false-audit defects (P4-RV-4: receipt linkage fields were
never reconciled against the actual validated receipt payload, and
creation-order evidence was hard-coded `True`; P4-RV-5: the P4-I1 audit always
built its closed manifest from the R1B constants regardless of which row was
actually current) -- both are now repaired in place; see "Correction Round 2
Repair" below for before/after evidence on each. This return describes the
current, twice-repaired state of the implementation as the authoritative
return -- not either prior pre-correction state. It implements the canary with
genuine identity verification, exact-once hard-obligation locator resolution,
receipt-field reconciliation against the actual validated payload, derived
(not hard-coded) creation-order evidence, and a per-row closed audit manifest
built from each row's own committed bytes and own hard-obligation locator. It
exercises the bounded natural-observation/checkpoint input seam (including a
genuinely linked receipt through the actual P2 validator/readout), proves
rollback rehearsal, and records the pinned R1B-R2 first observation as
honestly ineligible. It carries M0 and M1 as attributable historical
admission measurements rather than `NOT_YET_ESTIMABLE`. It does not accept
the observation, claim P5 readiness, claim canary window acceptance,
replace the trusted route, or claim recall/cost-saving.

## Target / Source

Exact six-path manifest after operator-authorized Amendment 2 (all CREATE):

- CREATE `governance/compat/mfrp_shadow_canary.py`
- CREATE `governance/compat/mfrp_shadow_canary_core.py`
- CREATE `governance/compat/test_mfrp_shadow_canary.py`
- CREATE `governance/compat/test_mfrp_shadow_canary_core.py`
- CREATE `governance/compat/fixtures/mfrp_p4_shadow_canary_evidence.json`
- CREATE `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_WORKER_RETURN_2026-09-02.md` (this file)

Sources read in full before implementation: the paired GC-018 baseline and
this work order (both recomputed by SHA-256, matching the dispatcher's cited
values exactly); the accepted P4 design
`docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md`;
the independent design rereview
`docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_REVISION_1_INDEPENDENT_REREVIEW_2026-09-02.md`
(disposition/acceptance boundary); the accepted R1B-R2 return
`docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md`
in full, including its Independent Reviewer Adjudication section (lines
678-763), where the exact trusted-outcome literal
`REVIEWER_ACCEPTED_EVIDENCE_RETURN_TO_DESIGN_BOUNDED` was independently
located at lines 758-759; both actual P2 seam owners
(`governance/compat/agent_autorun_machine_verification.py`,
`governance/compat/agent_automation_machine_verification_readout.py`) in
full; the accepted R1B-R2 runner
(`governance/compat/mfrp_actual_seam_replay.py`, identified by its pinned
SHA-256 as `010e516b63e550506fab4ee40760593fb78c12acc91fbe67b552eb725949bf2a`)
and result ledger
(`governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json`,
identified by its pinned SHA-256 as
`6b36ed295a7ffb0e74d3c7a32577428870c1b7e74da9e2ce7234c56d6c7f20ff`); the
Review Cost standard
`docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`;
and the applicable checker sources named in the work order's Checker Source
Read-Ahead Block. No P2 owner, SOT, standard, checker, hook, registry, or
session-state file was written to; each was read only for identity
confirmation or as a direct call-graph import.

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-p4-shadow-canary",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": ["canary-not-implemented", "eligible-pair-not-observed", "review-recall-not-yet-estimable"],
    "resolved": ["canary-not-implemented"],
    "retained": ["eligible-pair-not-observed", "review-recall-not-yet-estimable"],
    "new": [],
    "reopened": [],
    "current": ["eligible-pair-not-observed", "review-recall-not-yet-estimable"]
  },
  "resolutionEvidence": {
    "canary-not-implemented": {
      "evidenceClass": "EXECUTABLE_PROOF",
      "evidencePath": "governance/compat/test_mfrp_shadow_canary.py",
      "sha256": "1c4c9a8c545833d1642d6f3c6e07451b3a8219c175248c8d2ac10e32a1db7b97",
      "locator": "class SamplingFormulaTests(unittest.TestCase):",
      "claimId": "MFRP-P4-INITIALIZATION-EVIDENCE"
    }
  },
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "MFRP-P4-INITIALIZATION-EVIDENCE",
    "claimClass": "SCHEMA_COMPATIBILITY",
    "proofClass": "EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST",
    "evidenceRef": "governance/compat/fixtures/mfrp_p4_shadow_canary_evidence.json"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

`eligible-pair-not-observed` remains `current` because the first real
observation is honestly recorded `BLOCKED_NO_ELIGIBLE_NATURAL_PAIR` (see
Findings below); this return does not manufacture eligibility.
`review-recall-not-yet-estimable` remains `current` because no positive-
trigger denominator exists yet, per the accepted design's `NOT_YET_ESTIMABLE`
contract.

## Scope / Methodology

### Identity Gate

All opening identities were recomputed independently before any write and
matched the dispatcher's cited values exactly:

| Input | Recomputed SHA-256 | Match |
|---|---|---|
| work order (amended) | `5e39a08f04999a008424274fbc9916fd901324588d62e32a3a6853aae9e9f578` | PASS |
| baseline (unchanged) | `94e0d7b9018f621601427fe611ed7e72531875b4b94942ac09baf011bf50b718` | PASS |
| accepted P4 design | `65698a95dc7bb7f437fe061a81559701b91a3e611c445f5122ad8145c5f13df5` | PASS |
| independent design acceptance | `ae7c68c09ad4e7cfc688275dc896ec455f5c25a8771fa552fadac793717e4d7d` | PASS |
| accepted R1B-R2 return | `0842f9e275eaf2e44db79f265e8e9301bd7942eda2c2c9008ae3e8a0495f17c1` | PASS |
| accepted R1B-R2 runner | `010e516b63e550506fab4ee40760593fb78c12acc91fbe67b552eb725949bf2a` | PASS |
| accepted R1B-R2 ledger | `6b36ed295a7ffb0e74d3c7a32577428870c1b7e74da9e2ce7234c56d6c7f20ff` | PASS |
| P2 receipt owner | `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` | PASS |
| P2 readout owner | `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` | PASS |
| review-cost owner | `a8815cfc123d1ea085badcfe4e3d89b8d2cf4fef30662ccbb1f73e1511051d2d` | PASS |

All nine pinned identities matched exactly; zero mismatches. All six output
paths were confirmed absent before any write.

### Trusted-Outcome Literal Confirmation

The exact literal `REVIEWER_ACCEPTED_EVIDENCE_RETURN_TO_DESIGN_BOUNDED` was
independently located inside
`docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md`
at line 23 (`Reviewer disposition:` field) and again at lines 758-759 (the
"Final disposition:" line inside the Independent Reviewer Adjudication ->
Reviewer-Local Repair And Final Adjudication section). No alias or
higher-level shorthand was substituted; the literal string used in
`governance/compat/mfrp_shadow_canary.py` (`TRUSTED_OUTCOME` constant) and in
the evidence fixture's `r1bR2Identity.trustedOutcome` field is disposition
`MATCH` against the accepted return's source text (confirmed by direct
string search, not reproduced verbatim here to avoid a duplicate literal).

### Git Ancestry And Blob Proof

- `git rev-parse HEAD` at start: `d276cf4cd9b5bedb26b86625f42bfcbcb98afdea`
  (matches the dispatcher's expected clean base exactly).
- `git status --short` at start: empty.
- `git ls-tree 040ebfcff081062956c543f2b1d7e9cc04533b62 -- docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md`
  returned blob `32154bdf225e600ca0622ebb5e25c6c97c9678eb`, matching the
  pinned `TRUSTED_BLOB` exactly.
- `git merge-base --is-ancestor 040ebfcff081062956c543f2b1d7e9cc04533b62 HEAD`
  exits 0: the trusted commit is a proven ancestor of the execution base.
- `git merge-base --is-ancestor cf899df3d0f49b14b7bd347282134d0133ade7be 040ebfcff081062956c543f2b1d7e9cc04533b62`
  exits 0: the pinned autorun range parent is a proven ancestor of the
  material commit.
- Trusted material commit timestamp `2026-09-02T09:34:17+07:00` predates the
  execution base HEAD timestamp `2026-09-02T10:19:14+07:00`.

### Honest Receipt Boundary Recheck

Per the work order's explicit instruction, the four ignored files currently
under `.cvf/runtime/autorun-receipts/` (`pre-closure.json`, `pre-dispatch.json`,
`pre-implementation.json`, `pre-push.json`) were independently reopened and
inspected field-by-field rather than trusted from the baseline's dispatch-time
paragraph. None of their recorded `baseSha`/`headSha` pairs bracket the pinned
autorun range (`cf899df3d0f49b14b7bd347282134d0133ade7be` through
`040ebfcff081062956c543f2b1d7e9cc04533b62`); the closest candidate
(`pre-implementation.json`) has `base == head == cf899df3d`, i.e. a
zero-width range at the parent boundary only, not a range spanning to the
material commit. None of the four receipts carries any field naming the
R1B-R2 return path, its blob, or the hard-obligation locator. This confirms,
independently, that none of the four is eligible historical evidence for this
canary's initial observation.

### Actual-Seam Invocation Attempt

The existing autorun gate (`governance/compat/run_agent_autorun_workflow_gate.py`)
evaluates deterministic checks against the *current* worktree at `--head`
(defaulting to `HEAD`), not a replay of historical worktree content at an
arbitrary past commit. Invoking it with
`--base cf899df3d0f49b14b7bd347282134d0133ade7be --head 040ebfcff081062956c543f2b1d7e9cc04533b62`
now would evaluate today's worktree (already past both endpoints), not the
actual historical tree at the pinned range, and would not honestly represent
the immutable record. Per the work order's explicit instruction ("If the
existing autorun gate cannot generate a valid receipt for that immutable range
without changing source, record the row as ineligible with the precise
class... Do not relax the gate or substitute a current unrelated receipt."),
this row is recorded ineligible rather than invoked, with class
`NO_RETROACTIVE_RECEIPT_FOR_IMMUTABLE_RANGE_WITHOUT_SOURCE_CHANGE` folded
into the returned `BLOCKED_NO_ELIGIBLE_NATURAL_PAIR` disposition. No autorun
gate invocation was executed for this observation; zero provider/network
calls occurred as a result.

### Implementation Summary

`governance/compat/mfrp_shadow_canary.py` imports
`_validate_receipt_integrity` from `agent_autorun_machine_verification` and
`read_receipt_readonly` / `build_machine_verification_readout` /
`machine_readout_to_dict` from `agent_automation_machine_verification_readout`
directly; it defines no local `_validate_receipt_integrity`,
`read_receipt_readonly`, or `build_machine_verification_readout` function
(verified by negative test and by direct source-text search). It implements:

- `sample_size(n)`: exact-integer `k = min(4, max(1, ceil(0.20 * n)))` for
  `n >= 1`, else `0`, using `-(-n // 5)` rather than floating point;
- `sampling_digest` / `select_sample`: SHA-256 over UTF-8/LF concatenation of
  return path, blob identity and receipt identity; selection is lowest-digest
  order over only `ENVELOPE_CONSISTENT_WITH_TRUSTED` rows, never influenced by
  outcome labels;
- `LinkageManifest` / `evaluate_linkage` / `find_bound_ignored_receipt`: the
  Honest Receipt Boundary's explicit pair-linkage manifest; absent/ambiguous
  linkage always yields `COMPARISON_OBJECT_MISMATCH`, never clean agreement;
- `build_initial_observation_row`: builds the pinned R1B-R2 comparator row,
  raising on unproven trusted-record order, and recording
  `BLOCKED_NO_ELIGIBLE_NATURAL_PAIR` when no explicit linkage exists;
- `PinnedEvidenceInput` / `ClosedAuditManifest`: every declared
  authority/evidence input now carries an expected SHA-256 (or Git
  commit/blob), not merely a bare path -- **P4-RV-1 correction**;
- `run_p4_i1_invariant`: the five numbered `P4-I1-DECLARED-AUTHORITY-AND-HARD-OBLIGATION-SURVIVAL`
  checks against a `ClosedAuditManifest`. Check 1 recomputes each declared
  input's actual SHA-256 and fails closed on missing/mismatched/duplicate
  (rebound) identity, never merely `Path.is_file()`. Check 2 resolves
  `manifest.hard_obligation_locator_pattern` (module default
  `HARD_OBLIGATION_LOCATOR_PATTERN`, the exact anchored sentence
  `` `C07, C08, C15, C18`. C15 is classified `FALSE_NEGATIVE` `` in the R1B-R2
  return) to an exact count and requires `== 1`, never a bare `count("C15") >=
  1` substring search -- **P4-RV-1 and P4-RV-2 corrections**. Any
  `extra_read_paths` outside the manifest's own closed set, or
  `semantic_replay_requested=True`, still raises `AuditInputScopeExceeded`;
- `NewObservationInput` / `build_row_from_observation_input` /
  `append_observation` / `checkpoint_for_population`: the bounded
  natural-observation/checkpoint input seam. Accepts an explicit new natural
  return (path/commit/blob/trusted outcome), optional receipt
  path/digest/verifier/readout identity and autorun base/head, phase and
  hard-obligation locator/pattern; validates and appends deterministically;
  rejects duplicate rows (the same return submitted a second time with the
  same identity fields) and rebound rows (same return path submitted with a
  different commit/blob) with `DuplicateOrReboundObservation`; determines
  checkpoint
  (`initialization`/`M5`/`M10`/`final`) from the declared eligible-population
  thresholds, never hard-coded -- **P4-RV-3 correction**. The linked-receipt
  branch (real `read_receipt_readonly` / `build_machine_verification_readout`
  call against a bound receipt) is exercised end-to-end through this seam
  using a real ignored autorun receipt, no longer dead code from the CLI;
- `rollback_rehearsal`: creates and removes only the explicit
  `.cvf/runtime/mfrp-p4-shadow-canary/` marker, proving the trusted blob, HEAD
  and tracked repository bytes are unchanged before/after;
- `build_evidence` / CLI (`--output`, `--execution-base`, `--prior-ledger`,
  `--new-*` observation flags): orchestrates the above into the bounded
  evidence JSON. With no new flags supplied it reproduces the original
  opening-of-window behavior exactly (backward compatible); with
  `--prior-ledger` it consumes a previously-produced evidence JSON and
  appends to it rather than always starting from zero; with the `--new-*`
  flags it validates and appends one new observation through the same
  one-command CLI contract. M0/M1/M2 are carried as attributable historical
  admission measurements with disclosed committed-evidence sources (see M0-M2
  Plus Initial Measurement Summary below) -- **M0/M1 correction**.

## Findings / Position

### Initial Eligible-Pair / Linkage Result

The first real observation targeting the accepted R1B-R2 return is recorded
as row `R1B-R2-INITIAL` with:

- `divergenceClass`: `COMPARISON_OBJECT_MISMATCH`
- `ineligibleClass`: `BLOCKED_NO_ELIGIBLE_NATURAL_PAIR`
- `pairLinkageEvidence.linked`: `false`
- `pairLinkageEvidence.reason`: `"no linkage manifest supplied"`
- `trustedRecordOrderEvidence.orderOfRecordStatus`: `PROVEN`
- `controllingOutcome`: `REVIEWER_ACCEPTED_EVIDENCE_RETURN_TO_DESIGN_BOUNDED`

This is honest ineligibility, not a canary-safety claim. No receipt explicitly
binds the trusted commit/blob/return path per the closed linkage-manifest
contract, and the existing autorun gate cannot honestly regenerate a receipt
for the immutable historical range without evaluating the wrong (current)
worktree. The row never reports `ENVELOPE_CONSISTENT_WITH_TRUSTED`.

### Comparator, P4-I1 And Rollback Results

- Comparator row built successfully; `divergenceClass` correctly resolves to
  `COMPARISON_OBJECT_MISMATCH` for the ineligible pair; blind-spot disposition
  (`C07`, `C08`, `C18` non-representable; `C15` = `FALSE_NEGATIVE`;
  `excludedFromSuccessDenominators: true`) is present on the row.
- `P4-I1-DECLARED-AUTHORITY-AND-HARD-OBLIGATION-SURVIVAL`: all five numbered
  checks executed against the closed manifest and returned `PASS`. Per the
  round-2 P4-RV-5 correction, this manifest is now built by
  `default_closed_audit_manifest` from the CURRENT row's own persisted
  `closedAuditManifestPins` (its own committed blob path/git-sha, its own
  recomputed expected SHA-256, its own hard-obligation locator/pattern) --
  never defaulted to the R1B constants regardless of which row is current
  (see "Correction Round 2 Repair" below for the two-return causal proof).
  For this specific R1B-R2-INITIAL row the pins happen to resolve to the R1B
  identity, because that is genuinely what this row is:
  1. authority/evidence bytes match pinned identity: PASS -- check 1
     recomputes the actual SHA-256 from the COMMITTED blob object (`git
     cat-file blob <sha>`, never the mutable worktree file) and compares it
     against the pinned `expected_sha256`; the return blob's actual SHA-256
     (`0842f9e275eaf2e44db79f265e8e9301bd7942eda2c2c9008ae3e8a0495f17c1`)
     matches the pinned identity exactly (see P4-RV-1 below for the original
     pre-round-1-correction behavior, and P4-RV-5 below for the
     committed-blob-vs-worktree correction);
  2. hard-obligation locator present exactly once: PASS
     (`locatorOccurrenceCount == 1`) -- check 2 resolves the exact anchored
     sentence `` `C07, C08, C15, C18`. C15 is classified `FALSE_NEGATIVE` ``
     (`HARD_OBLIGATION_LOCATOR_PATTERN`) against the COMMITTED blob text, not
     a bare substring count of the token `C15` and not the mutable worktree
     file (see P4-RV-2 and P4-RV-5 below);
  3. no acceptance claim over an absent/failed/`NOT_CHECKED`/`UNCLASSIFIED`
     obligation: PASS (`FALSE_NEGATIVE`, `C07`, `C08`, `C18` all present in
     the real committed return text);
  4. limitations/not-checked/unclassified survive into the comparator
     classification: PASS (row's `blindSpotDisposition` matches exactly);
  5. trusted disposition commit is an ancestor of shadow disclosure: PASS
     (order-of-record `PROVEN`).
- Sampling: `n = 0` eligible clean records (the one row is ineligible, not
  clean-consistent), so `k = 0`; no records were audited by the k-sample path,
  consistent with the formula for `n = 0`.
- Rollback rehearsal: created and removed only
  `.cvf/runtime/mfrp-p4-shadow-canary/`; `trustedBlobBefore == trustedBlobAfter`
  (`32154bdf225e600ca0622ebb5e25c6c97c9678eb`); `headBefore == headAfter`
  (`d276cf4cd9b5bedb26b86625f42bfcbcb98afdea`); `trustedDispositionUnchanged:
  true`; `providerCallsDuringRollback: 0`.

### M0-M2 Plus Initial Measurement Summary

Per the reviewer-directed correction, M0 and M1 are now carried as
attributable historical admission measurements already established by
committed evidence, not `NOT_YET_ESTIMABLE` placeholders. Only the recall
conclusion remains `NOT_YET_ESTIMABLE` (the positive-trigger denominator is
zero); M0/M1/M2 themselves are concrete, source-cited observations:

- M0: `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md`
  (the earliest historical admission measurement in this MFRP chain -- the
  original, rejected R1B actual-seam replay return). Pre-execution review
  count `0`; 3 connected contract defects (R1B-RV-1/2/3) found at the
  intended worker-return boundary; reviewer disposition `RETURN_TO_DESIGN`;
  recall conclusion `NOT_YET_ESTIMABLE`.
- M1: `docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md`
  (the second historical admission measurement -- the R1B-R2 repair round's
  own first-pass independent adjudication, before its in-place repair;
  distinct from M2, which is the same return's final post-repair
  adjudication). Pre-execution review count `0`; 3 connected contract defects
  found at the intended worker-return boundary; reviewer disposition
  `REVISE_IN_PLACE_CONSOLIDATED`; recall conclusion `NOT_YET_ESTIMABLE`.
- M2: the same R1B-R2 return's final post-repair adjudication (its own
  Review Admission Measurement - M2 section): pre-execution review count `0`;
  the same 3 connected contract defects, now resolved in place; zero
  irreversible/external effect before detection; reviewer disposition
  `REVIEWER_ACCEPTED_EVIDENCE_RETURN_TO_DESIGN_BOUNDED`; recall conclusion
  `NOT_YET_ESTIMABLE`.
- Initial observation: `shadowCommandCount: 0`, `externalCalls: 0`,
  `auditScopeExceededCount: 0` (the pinned ineligible R1B-R2 row required no
  autorun invocation and no audit-scope excess occurred; this field sums
  across all rows currently in the ledger, per the P4-RV-3 seam correction).
- `positiveTriggerDenominator: 0`; `recall: NOT_YET_ESTIMABLE`. No saved cost
  is claimed; the trusted route remained fully controlling throughout.

### Hostile Regression Matrix Coverage

`governance/compat/test_mfrp_shadow_canary.py` implements 89 focused tests
covering the work order's full Required Hostile Regression Matrix, the
round-1 reviewer's three consolidated correction findings (21 tests added in
that correction round; see "Reviewer-Directed Consolidated Correction Round"
below for the itemized six-plus hostile-test list per finding), and the
round-2 reviewer's P4-RV-4/P4-RV-5 findings (16 tests added in this round;
see "Correction Round 2 Repair" below for the itemized list per finding). The
round-1 73-test suite is fully preserved unchanged in coverage; the round-2
M5-threshold test was restructured, not deleted, per the round-2 reviewer's
explicit instruction (see "Correction Round 2 Repair" -> P4-RV-4 below).
The round-1 baseline coverage:
sampling formula monotonic/capped behavior across `n = 0..499`; tie-stable,
outcome-blind sampling order; linkage-boundary rejection of missing fields,
missing order evidence, an unrelated ignored receipt, a range-matching but
undeclared receipt, and a tampered bound blob; trusted-record-order
proof/rejection (missing commit, non-ancestor commit); comparison-object
mismatch never mapping to clean consistency; blind-spot (`C07`/`C08`/`C18`/`C15`)
survival under an attempted-hide probe; outcome-label agreement not masking a
failed P4-I1; `AUDIT_INPUT_SCOPE_EXCEEDED` on an undeclared read path and on a
simulated semantic-replay request; an "always-clean" weakening probe (forced
order-of-record failure still fails the invariant; `evaluate_linkage(None)`
never returns true); rollback preserving trusted blob/HEAD/tracked bytes;
byte-identical (disposition `MATCH`, post-normalization) evidence across two
same-base executions; actual-P2-seam import proof plus a negative test
asserting no local fork of the P2 validator/readout functions exists in the
module source; zero external calls at every observed point; a CLI smoke
test running the documented `--help` and a same-base double invocation whose
output hashes carry disposition `MATCH`; identity-tamper, missing-file and
rebound-pin rejection for P4-I1 check 1 (`P4-RV-1`); zero-match and
duplicate-match exact-once locator rejection for P4-I1 check 2 (`P4-RV-2`);
checkpoint-threshold determinism, valid-linked-receipt exercise through the
real P2 seam, missing/tampered/rebound linkage rejection, disk-ledger
consumption, and a CLI exercise of the new observation seam (`P4-RV-3`); and
M0/M1 attributable-source assertions (M0/M1 fix).

## Risk / Corrective Action

The primary risk carried by this tranche is false confidence from treating
`COMPARISON_OBJECT_MISMATCH`, `IDENTITY_OR_SOURCE_DRIFT`, or an ineligible row
as clean agreement. This is mitigated structurally: the shared row-construction
tail `_build_linked_or_ineligible_row` (used by both
`build_initial_observation_row` and `build_row_from_observation_input`, per the
round-1 P4-RV-3 generalization) can only assign `ENVELOPE_CONSISTENT_WITH_TRUSTED`
after linkage is both complete AND reconciled against the actual validated
receipt payload (`reconcile_linkage_with_receipt`); neither the
incomplete-manifest branch nor the reconciliation-failure branch can construct
that class (verified by structural tests reading the function source -- see
`test_absent_linkage_never_yields_clean_agreement` and
`test_reconciliation_failure_never_yields_clean_agreement`). A second risk,
identified by the round-2 reviewer (P4-RV-5), is a valid R1B invariant masking
a missing/duplicated obligation in a genuinely different current row; mitigated
by `default_closed_audit_manifest` building the closed manifest from each row's
own persisted `closedAuditManifestPins`, proven by a causal two-return test
(R1B passes, a synthetic current row with an absent locator fails). A third
risk is silently widening the P4-I1 audit's input scope; mitigated by
`run_p4_i1_invariant` raising `AuditInputScopeExceeded` for any
`extra_read_paths` outside its own closed manifest or any
`semantic_replay_requested` flag, with focused tests for both. No corrective
action beyond the implemented fail-closed behavior was required in either
round; no defect was found that needed a design or scope change.

## Decision / Disposition

`COMPLETE_PENDING_REVIEW`

Implementation, rollback rehearsal, and an honest pinned first observation
are complete, and both rounds of reviewer-directed findings are repaired in
place in the original four paths: round 1's three consolidated correction
findings (P4-RV-1, P4-RV-2, P4-RV-3) plus the M0/M1 attribution gap (see
"Reviewer-Directed Consolidated Correction Round" below), and round 2's two
causal false-linkage/false-audit findings (P4-RV-4, P4-RV-5; see "Correction
Round 2 Repair" below). The pinned R1B-R2 observation remains zero-eligible
and is recorded as `BLOCKED_NO_ELIGIBLE_NATURAL_PAIR`; no canary-safety claim
is made. The trusted route (`REVIEWER_ACCEPTED_EVIDENCE_RETURN_TO_DESIGN_BOUNDED`)
remains fully controlling and byte-unchanged. This return does not declare
canary window acceptance, reviewer acceptance, P5 readiness, route
replacement, correctness, recall preservation, M5/M10/final canary progress,
or observed cost-saving anywhere -- those determinations belong to the next
independent review of this twice-corrected state, not to this worker return.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create exactly the six paths named in
the work order's Core Guard Self-Protection Authorization section --
`governance/compat/mfrp_shadow_canary.py`,
`governance/compat/mfrp_shadow_canary_core.py`,
`governance/compat/test_mfrp_shadow_canary.py`,
`governance/compat/test_mfrp_shadow_canary_core.py`,
`governance/compat/fixtures/mfrp_p4_shadow_canary_evidence.json` -- plus this
worker-return document. No existing protected source changed; `git status
--short` confirms only these six untracked new paths.

Protected paths (unchanged, confirmed by hash recomputation above):

- `governance/compat/agent_autorun_machine_verification.py`
- `governance/compat/agent_automation_machine_verification_readout.py`

Operator authorization: the amended work order's explicit 2026-09-02
instruction to run the canary and collect empirical review-reduction/recall
evidence, with the corrected trusted-outcome literal now verified present at
the amended work order's lines 64 and 319.

Rollback boundary: remove the exact six uncommitted worker outputs and the
verified ignored `.cvf/runtime/mfrp-p4-shadow-canary/` directory only; no
trusted-route artifact is touched.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch/no-commit fields; review admission; Source Verification; protected paths; worker-return profile; `REVIEWER_ACCEPTED_EVIDENCE_RETURN_TO_DESIGN_BOUNDED` literal at its exact source lines |
| gateRunPurpose | confirmation evidence that this completed P4 initialization return is review-ready before reviewer evaluation, not initial exploration of the packet shape |
| claimBoundary | PASS proves packet/evidence shape only, not canary safety, recall, savings or P5 readiness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | bounded local implementation/measurement worker |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P4 initialization worker execution, 2026-09-02 |
| Working directory | repository root |
| Command or tool surface | governed reads, `git`, hash recomputation, `python -B governance/compat/mfrp_shadow_canary.py`, `python -B governance/compat/test_mfrp_shadow_canary.py`, `python governance/compat/run_worker_return_fast_gate.py` |
| Target paths | the six Required Artifact Manifest paths |
| Allowed scope source | amended work order and paired GC-018 baseline, both independently re-verified by SHA-256 |
| Before status evidence | clean worktree at `d276cf4cd9b5bedb26b86625f42bfcbcb98afdea`; original four output paths confirmed absent |
| After status evidence | exactly six untracked output paths plus the tracked Amendment 2 authority edits pending separate commit; zero committed |
| Diff evidence | `git status --short`; `git diff --name-status`; exact manifest reconciliation and staged-diff inspection |
| Approval boundary | six-path initialization only; operator Amendment 2 authorizes the maintainability split |
| Claim boundary | no safety/recall/saving/P5/route-replacement claim |
| Agent type | bounded local implementation/measurement worker |
| Invocation ID | `mfrp-p4-initialization-worker-2026-09-02` |
| Expected manifest | the six Required Artifact Manifest paths |
| Actual changed set | the same six output paths |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | P4 initialization implementation and first observation only |
| claimDisposition | CLAIM_REJECTED: no canary safety, recall, saving, P5 readiness or route-replacement claim |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no receipt explicitly links to the trusted R1B-R2 record; row is ineligible |
| actionEvidence | ACTION_EVIDENCE_PRESENT: implementation, rollback rehearsal and one honest ineligible observation executed and recorded in the bounded evidence fixture |
| invocationBoundary | local governed reads, git, and two Python CLI invocations only |
| interceptionBoundary | trusted route (`REVIEWER_ACCEPTED_EVIDENCE_RETURN_TO_DESIGN_BOUNDED`) unchanged and fully controlling |
| claimLanguage | bounded shadow-canary initialization evidence only |
| forbiddenExpansion | no route replacement, P2 change, P5 opening, or provider/live/public/deploy/production effect |

## Finding-To-Governance Learning Disposition

No new defect class was found in an existing governed source during this
tranche. The prior identity-mismatch stop (citing a nonexistent trusted-
outcome token) was already corrected by the dispatcher's Amendment 1 before
this dispatch began; this return re-verifies that correction rather than
discovering a new one. `NOT_APPLICABLE_WITH_REASON`: no new ADIF-eligible
defect surfaced.

WORKER_EXPERIENCE_RETRO:

frictionLevel: LOW

frictionType: ENUM_OR_TOKEN_MISMATCH

observedStep: the byte-identity determinism check initially compared raw
evidence JSON bytes including the rollback rehearsal's live `git status
--short` snapshot; that field legitimately differs across separate runs
purely because the evidence fixture's own on-disk existence changes
untracked status after the first write, which is not part of the canary's
actual computation. Resolved by extending the documented duration-field
exclusion in `normalize_for_byte_comparison` to also exclude that live-status
pair, with the load-bearing blob/HEAD/disposition-unchanged fields kept fully
part of the determinism claim.

preventiveControlCandidate: HELPER_DIAGNOSTIC

## Rework Convergence Self-Proof

dispatchKind: INITIAL

rootCauseClusterId: mfrp-p4-shadow-canary-initialization

reworkGeneration: 0

consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES

productionBindingEvidence: no production binding; exactly the four Required
Artifact Manifest paths, uncommitted

adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

internalAgentInvocationCount: 1

externalAgentInvocationCount: 0

providerCallCount: 0

tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: no per-task cross-agent quota
meter is exposed to the local worker

terminalReadinessVerdict: READY_FOR_REVIEW

## Epistemic Process Block

### Expected Result / Prediction

Implementing the accepted P4 comparator once and running it against the
immutable accepted R1B-R2 record should either produce an explicitly linked
clean/divergent comparator row or an honestly classified ineligible row,
without ever fabricating a receipt, relaxing the linkage boundary, or
treating absence of evidence as clean agreement.

### Evidence Comparison

The implementation was run twice against the same execution base; both raw
outputs and duration/live-status-normalized outputs are byte-identical
(`outputSha256` = `0f21dad91fb5a131306f45cb6dcdd76741f528a8dd3242ac126f6e14127f020d`
for both raw runs under identical worktree state; normalized SHA-256
`7cc166830533bd3184d042665087f6b5e54cd726e6129e7e66d3d36c973993d7` for both).
The four ignored autorun receipts were independently reopened and none
matched the pinned range or declared the return path/blob; the autorun gate
cannot honestly regenerate the historical range without evaluating the
current worktree. This matches the prediction: the row is recorded
`BLOCKED_NO_ELIGIBLE_NATURAL_PAIR`, not fabricated agreement.

### Contradiction Or Gap Disposition

No contradiction between the accepted design/baseline/work-order contract and
the actual repository state was found. One implementation gap was found and
corrected during self-testing, before this return was authored: an early
draft of `normalize_for_byte_comparison` excluded only duration fields, but
the rollback rehearsal's live `git status --short` snapshot legitimately
differs across separate runs purely because the evidence fixture's own
existence-on-disk changes untracked status -- an artifact of the write
side-effect, not the canary's computation. This was corrected by also
excluding `repositoryStatusBefore`/`repositoryStatusAfter` from the
byte-identity comparison (documented in the function's docstring), while
keeping the load-bearing `trustedBlobBefore/After`, `headBefore/After` and
`trustedDispositionUnchanged` fields fully part of the determinism claim.

### Claim Update

The canary is implemented and its first honest observation is recorded as
ineligible. No safety, recall, or cost-saving claim is made; the trusted
route remains the sole controlling authority. The measurement window is now
open for natural accumulation toward the M5/M10/final checkpoints under the
existing sunset rule (earlier of 20 eligible returns or 30 calendar days from
2026-09-02).

## Conditional Controls Disposition

conditionalControlsDisposition: EKI_REQUIRED; RIH_NA; CCRI_NA

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | accepted P4 design and independent rereview -> this work order -> bounded local implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | accepted P4 design, independent rereview, this work order and its paired baseline |
| Disposition | NO_NEW_ABSORPTION |
| Claim boundary | no external statement is treated as runtime truth |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

N/A with reason: this return implements one bounded six-path shadow-canary
tranche from an already-accepted design and work order; it is not an intake
refresh or a rescan output within the meaning of the rescan guard.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded exact six-path P4 initialization implementation over a fixed named source set; no all-files, complete-corpus, or full-scan claim is made by this return.

manifest=N/A (fixed named source set, not a corpus scan); ledger_terminal=N/A
(no processing ledger is produced by this claim category); exclusions=none;
unresolved=0.

## Claim Boundary

This return implements exactly the six-path MFRP-P4 initialization tranche,
records one honest, ineligible pinned R1B-R2 observation, and repairs the
independent reviewer's three consolidated findings (P4-RV-1, P4-RV-2,
P4-RV-3) plus the M0/M1 attribution gap in place, followed by the authorized
six-path maintainability split, under
the same controlling work order. It does not claim canary safety, correctness,
recall preservation, observed cost saving, P5 readiness, canary window
acceptance, route replacement, or reviewer acceptance. The trusted route
(`REVIEWER_ACCEPTED_EVIDENCE_RETURN_TO_DESIGN_BOUNDED`) remains the sole
controlling authority. Nothing here authorizes provider, live, public,
deployment, or production effects.

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. No `git add`, `git commit`, or staging
command was run by the worker. Reviewer/closer staging attempts created no
commit and were cleared. All six
new paths remain untracked (`??`) in `git status --short`.

## git status --short

```text
?? governance/compat/fixtures/mfrp_p4_shadow_canary_evidence.json
?? governance/compat/mfrp_shadow_canary.py
?? governance/compat/mfrp_shadow_canary_core.py
?? governance/compat/test_mfrp_shadow_canary.py
?? governance/compat/test_mfrp_shadow_canary_core.py
?? docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_WORKER_RETURN_2026-09-02.md
```

## Changed Files

- CREATE `governance/compat/mfrp_shadow_canary.py`
- CREATE `governance/compat/mfrp_shadow_canary_core.py`
- CREATE `governance/compat/test_mfrp_shadow_canary.py`
- CREATE `governance/compat/test_mfrp_shadow_canary_core.py`
- CREATE `governance/compat/fixtures/mfrp_p4_shadow_canary_evidence.json`
- CREATE `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_WORKER_RETURN_2026-09-02.md`

Exactly six output paths; equal to the amended Required Artifact Manifest.

## Command Evidence

| Command | Result |
|---|---|
| `git rev-parse HEAD` (start) | `d276cf4cd9b5bedb26b86625f42bfcbcb98afdea`; PASS |
| `git status --short` (start) | empty; PASS |
| `git merge-base --is-ancestor 040ebfcff081062956c543f2b1d7e9cc04533b62 HEAD` | exit 0; PASS |
| `git merge-base --is-ancestor cf899df3d0f49b14b7bd347282134d0133ade7be 040ebfcff081062956c543f2b1d7e9cc04533b62` | exit 0; PASS |
| `git ls-tree 040ebfcff081062956c543f2b1d7e9cc04533b62 -- docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md` | blob `32154bdf225e600ca0622ebb5e25c6c97c9678eb`; PASS |
| `python -B governance/compat/mfrp_shadow_canary.py --help` | usage/help text printed; exit 0; PASS |
| `python -B governance/compat/mfrp_shadow_canary.py --output governance/compat/fixtures/mfrp_p4_shadow_canary_evidence.json --execution-base d276cf4cd9b5bedb26b86625f42bfcbcb98afdea` (regenerated after correction round, tracked fixture) | `outputSha256=84053f60d8f4a766dadfc5514301b01b3923a33b1691909cfaefeb75b94bff10`; `ineligibleClasses=["BLOCKED_NO_ELIGIBLE_NATURAL_PAIR"]`; `invariantResult=PASS`; `rollbackTrustedDispositionUnchanged=true`; PASS |
| same command, run 2 (separate temp output path, same execution base) | raw `outputSha256` disposition `MATCH` against run 1; normalized SHA-256 `ca5bdda3309be65a401f9d10f3ed1541c4ea00e3ef384e91fdc9e6f4fa1e7e1b` disposition `MATCH` against run 1 and against the tracked fixture; PASS |
| P2 owner file SHA-256 recomputed after both runs | both unchanged and match `OWNER_HASHES`; PASS |
| `python -B governance/compat/test_mfrp_shadow_canary.py -v` (run 1) | 73/73 tests passed; PASS |
| `python -B governance/compat/test_mfrp_shadow_canary.py -v` (run 2) | 73/73 tests passed; PASS |
| `git status --short` (post-correction, pre-return-authoring) | exact implementation output set for that correction stage; PASS |
| `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_mfrp_shadow_canary.py` | focused pytest 73/73 PASS; corpus scan registry PASS; epistemic process packet PASS; worker-return quality gate PASS; reviewer-fast governance gate VIOLATION (see next row); git diff whitespace check PASS |
| `PYTHONIOENCODING=utf-8 python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | all content checks passed; only pre-material continuity sequencing remained |
| `git diff --cached --name-status` | empty; PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance P4 shadow-canary initialization evidence; no
public-sync artifact or authority is created by this return.

## Independent Reviewer Adjudication

Initialization review first returned `REVISE_BEFORE_CANARY_WINDOW_OPEN`.
The consolidated evidence findings were: P4-RV-1 verified path existence but
not authority bytes; P4-RV-2 used a weakened non-exact locator predicate;
P4-RV-3 lacked a natural-observation/checkpoint input seam; and M0/M1 were not
carried as attributable historical measurements. These findings were evaluated
at the returned-result boundary, not by repeating implementation work.

## Reviewer-Directed Consolidated Correction Round

The same original four then-uncommitted paths were repaired in place. Authority bytes
became content-verified, the hard-obligation locator became exact-once, the
ledger gained one bounded append/checkpoint seam with duplicate/rebound
rejection, and M0/M1/M2 became source-attributed. The focused suite increased
from 52 to 73 tests. No worker redispatch, provider call, stage or commit
occurred.

## Independent Reviewer Re-Review - Correction Round 2

Re-review found two truth-boundary defects: P4-RV-4 accepted caller-declared
receipt identities without reconciling them to the actual P2-validated payload
and hard-coded creation order; P4-RV-5 audited every row with the fixed R1B
manifest. Disposition remained `REVISE_BEFORE_CANARY_WINDOW_OPEN`.

## Correction Round 2 Repair

P4-RV-4 was repaired by deriving receipt creation order and comparing declared
digest, verifier, schema/readout and base/head against the actual P2 readout.
P4-RV-5 was repaired by persisting each row's own committed blob and locator
pins and reading committed blob bytes through `git cat-file`. Causal tests cover
all-wrong identities, stale creation order, per-row absent/duplicate locators
and committed-blob versus worktree drift. The focused suite reached 89/89.
The only reviewer-fast residual was the expected pre-material continuity HEAD
mismatch; zero provider/live/network calls occurred.

## Independent Reviewer Final Adjudication And Local Repair

Review boundary: the same initialization `WORKER_RETURN`; no pre-execution
review and no additional routine checkpoint was introduced. The reviewer
verified the round-2 P4-RV-4/P4-RV-5 repairs against source and causal tests:
receipt creation order is derived from filesystem mtime versus the trusted Git
commit time, every caller-declared receipt identity field is reconciled to the
actual P2-validated payload, each row persists its own closed-audit pins, and
P4-I1 reads the pinned committed blob bytes.

Two remaining localized truth-boundary defects were evidence-determined and
repaired in place under the existing authorization, rather than
redispatching a worker and paying another context-load round:

- `P4-RV-6`: distinct return rows could reuse one receipt path or one
  byte-identical receipt digest and be counted as independent eligible pairs.
  `append_observation` now rejects either collision between eligible rows as
  `DuplicateOrReboundObservation`. The M5 fixture builder now varies the
  deterministic command-manifest identity so five test receipts represent
  five distinct machine observations, not five filenames for identical
  payloads. A causal regression submits two different committed returns with
  the same valid receipt and proves the second association is rejected.
- `P4-RV-7`: every top-level `safetyTriggers` value was a hard-coded `false`,
  so a failed P4-I1 invariant or a persisted divergence could fail to advance
  review. `derive_safety_triggers` now computes unexplained divergence,
  machine closure against a blocking trusted outcome, identity/source drift,
  hidden limitation or `UNCLASSIFIED`, order failure, external effect,
  audit-scope excess, and independent-invariant failure from the actual rows
  and invariant result. The existing absent-locator causal test now proves a
  P4-I1 `FAIL` raises both the independent-invariant and hidden-limitation
  triggers.

### Final Verification Evidence

| Check | Result |
| --- | --- |
| execution base / HEAD | `d276cf4cd9b5bedb26b86625f42bfcbcb98afdea`; MATCH |
| changed-set boundary | exactly six output paths after Amendment 2; no material commit yet |
| focused hostile suite | 90/90 PASS after reviewer-local repair |
| regenerated fixture | SHA-256 `4f8bd9e053a9ce33e1427bab23cb2efff854ca79154c36bae6361068ffc9ff63`; initialization; one honestly ineligible R1B-R2 row; P4-I1 PASS |
| helper / core SHA-256 | `e8a3ae0d541a482be1138a3c9c40f751881812902cade1b6ef288dc4cf6b2f85` / `0ffa02a7cf5ca086bb682eed33014be8cc113fba70f9a4c57a64dcfcf28ec251` |
| test / split-test SHA-256 | `1c4c9a8c545833d1642d6f3c6e07451b3a8219c175248c8d2ac10e32a1db7b97` / `18b6c8f7fc028b761c4d259f9724fbdbe8a348f68bb582753bad3bd9cc156f41` |
| external/provider/live/network calls | 0 |
| reviewer-local repairs / worker redispatches in final review | 2 / 0 |

Final disposition: `REVIEWER_ACCEPTED_CANARY_WINDOW_OPEN_BOUNDED`.

Acceptance is bounded to the P4 initialization implementation and opening of
the natural-observation window. The accepted fixture still contains zero
eligible observations, so it proves neither recall preservation nor cost
saving. The trusted route remains controlling. Routine review is next admitted
only at M5, M10, final/M20-or-day-30, or when a derived safety trigger fires.
P2 mutation, P5, route replacement and external effects remain closed.
