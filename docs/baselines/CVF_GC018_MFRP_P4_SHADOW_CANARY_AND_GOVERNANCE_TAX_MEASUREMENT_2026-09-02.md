# CVF GC-018 Baseline - MFRP-P4 Shadow Canary And Governance-Tax Measurement

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: MFRP-P4

Dispatch base head: `0b495a7177eaeb2af58141cea0069d7b01b925dc`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one bounded shadow-canary harness and its first real observation.
The tranche measures whether machine-first evidence can reduce redundant review
without lowering observed recall, while the existing trusted route remains the
only controlling authority.

The canary is not a new review system. It has a fixed sunset at the earlier of
20 eligible natural returns or 30 calendar days, uses one bounded evidence
artifact, and admits routine review only at M5, M10 and the closing checkpoint.

## Decision / Baseline

Proceed with one four-path, no-commit P4 initialization under the accepted
design. The trusted route remains controlling; the canary may measure and
classify but cannot authorize, replace review, or open P5.

## Opening Evidence

| Input | Required identity |
|---|---|
| accepted P4 design | SHA-256 `65698a95dc7bb7f437fe061a81559701b91a3e611c445f5122ad8145c5f13df5`; containing commit `7890f8274e4471a2994e2e078ab307fd7df3e73d` |
| independent design acceptance | SHA-256 `ae7c68c09ad4e7cfc688275dc896ec455f5c25a8771fa552fadac793717e4d7d`; containing commit `25aaade8b8bbf68d22f6648e9a2250fca4e37647` |
| accepted R1B-R2 return | SHA-256 `0842f9e275eaf2e44db79f265e8e9301bd7942eda2c2c9008ae3e8a0495f17c1`; material commit `040ebfcff081062956c543f2b1d7e9cc04533b62`; blob `32154bdf225e600ca0622ebb5e25c6c97c9678eb` |
| accepted R1B-R2 runner | SHA-256 `010e516b63e550506fab4ee40760593fb78c12acc91fbe67b552eb725949bf2a` |
| accepted R1B-R2 ledger | SHA-256 `6b36ed295a7ffb0e74d3c7a32577428870c1b7e74da9e2ce7234c56d6c7f20ff` |
| P2 receipt owner | SHA-256 `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` |
| P2 readout owner | SHA-256 `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` |
| review-cost owner | SHA-256 `a8815cfc123d1ea085badcfe4e3d89b8d2cf4fef30662ccbb1f73e1511051d2d` |

Every identity is recomputed before editing. A mismatch stops execution.

## Honest Receipt Boundary

The ignored files under `.cvf/runtime/autorun-receipts/` are mutable runtime
caches. They are not durable historical evidence and may not be paired
retrospectively with a committed return merely because their phase label looks
compatible.

For each eligible record, the canary generates or consumes a receipt only when
one explicit invocation manifest binds all of these values:

- repository-relative phase-return path;
- immutable trusted commit and blob;
- autorun base/head range;
- receipt path, digest, verifier identity and readout identity;
- creation time/order evidence after the trusted commit;
- the declared source/authority locator and hard-obligation locator.

Absent or ambiguous linkage is `COMPARISON_OBJECT_MISMATCH`, never clean
agreement. A generated shadow receipt is preserved in the bounded P4 evidence
ledger by content and digest; the ignored cache path is not the evidence owner.

## Current Runtime Freshness Verification

Current runtime inspection on 2026-09-02 found four ignored mutable receipt
files under `.cvf/runtime/autorun-receipts/`. Their phase/base/head/digest and
file hashes were read directly. None binds the accepted R1B-R2 return commit
and blob through an explicit pair-linkage manifest. Therefore they are not
eligible historical canary evidence. This is a dispatch-time fact only; the
worker must recheck rather than trust this paragraph.

## Canary Population And Checkpoints

Only naturally occurring returns already subject to an ordinary trusted route
are eligible. No task, phase, packet or review may be manufactured to fill the
population. Missing phases are `NOT_OBSERVED`.

The window closes at 20 eligible returns or 30 calendar days, whichever occurs
first. The same four-path tranche is updated at these checkpoints only:

- initialization: implementation plus first eligible R1B-R2 observation;
- M5: when five eligible returns exist;
- M10: when ten eligible returns exist;
- final: M20 or day 30.

There is no routine per-return reviewer invocation. Before a checkpoint, the
worker may collect deterministic rows without reviewer acceptance. An early
review is admitted only by a declared safety trigger: unexplained divergence,
machine closure where trusted route blocks, identity/source drift, hidden
limitation or `UNCLASSIFIED`, order-of-record failure, external effect, or
audit-scope excess.

## Comparator And Sampling Contract

Each row carries the exact fields defined by the accepted P4 design. The
trusted semantic outcome and machine receipt outcome are different comparison
objects. `ENVELOPE_CONSISTENT_WITH_TRUSTED` asserts consistency only on fields
both represent; it never asserts correctness or equivalence.

High-risk, divergent, incomplete and `UNCLASSIFIED` records receive 100%
independent audit. At a closed checkpoint, clean non-divergent records are
selected by the lowest digest, with:

`k = min(4, max(1, ceil(0.20 * n)))` for `n >= 1`; otherwise `k = 0`.

The digest domain is UTF-8/LF concatenation of repository-relative return
path, Git blob identity and controlling receipt identity. Sampling is selected
only after the checkpoint population closes and before machine outcomes are
revealed to the auditor.

## Named Independent Invariant

Invariant ID: `P4-I1-DECLARED-AUTHORITY-AND-HARD-OBLIGATION-SURVIVAL`.

For every sampled clean record, use only the immutable return blob, the exact
authority/evidence path named by its `Source Verification Block`, the exact
hard-obligation locator named in the canary invocation manifest, the associated
receipt and comparator row. Verify:

1. the named authority/evidence bytes match their pinned identity;
2. the hard-obligation locator exists once in the declared evidence envelope;
3. the return does not claim acceptance when that obligation is absent, failed,
   `NOT_CHECKED` or `UNCLASSIFIED`;
4. receipt limitations, not-checked scope and unclassified items survive into
   the machine readout and comparator classification;
5. the trusted disposition commit is an ancestor of shadow disclosure.

The audit may not reopen design reasoning, regenerate the deliverable, rerun
the phase, or search beyond the closed manifest. Any extra input or semantic
re-execution is `AUDIT_INPUT_SCOPE_EXCEEDED` and duplicated semantic work.

## Governance-Tax And Recall Ledger

The bounded evidence artifact reuses Review Cost fields and records:

- M0, M1 and M2 historical admission measurements already established by
  committed evidence;
- eligible count and observed phase coverage;
- pre-execution review count, routine review-boundary count and safety-trigger
  review count;
- admission false negatives, defined only where a required trigger existed
  before execution but admission skipped it;
- worker-return findings, reviewer-local repairs and worker redispatches;
- machine command count/duration, audit minutes, cache/reuse status, external
  calls and observable `AUDIT_INPUT_SCOPE_EXCEEDED` count;
- positive-trigger denominator and recall when estimable; otherwise
  `NOT_YET_ESTIMABLE` with no safety claim.

A defect correctly found at the normal worker-return boundary is not an
admission false negative. Zero observed escapes with zero positive triggers
does not establish recall.

## Rollback Rehearsal

Before the first observation, prove that removing the ignored shadow receipt
directory and withholding the comparator output leaves the trusted disposition
and repository bytes unchanged. Rollback is stopping the shadow command and
preserving committed evidence; it does not assume a production feature flag.

Expected rehearsal result: the trusted R1B-R2 acceptance remains exactly the
same commit/blob, no provider call occurs, and only ignored temporary receipt
files disappear. The worker must use an explicit repository-bounded temporary
directory and may remove only that verified directory.

## Exact Artifact Manifest

| Artifact | Required action |
|---|---|
| `governance/compat/mfrp_shadow_canary.py` | CREATE bounded comparator/checkpoint helper |
| `governance/compat/test_mfrp_shadow_canary.py` | CREATE focused hostile and rollback tests |
| `governance/compat/fixtures/mfrp_p4_shadow_canary_evidence.json` | CREATE bounded, sunset-marked evidence ledger |
| `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_WORKER_RETURN_2026-09-02.md` | CREATE implementation/observation return and checkpoint owner |

No fifth path may change during worker execution. The ledger and return are
bounded tranche evidence, not standards, registries or new receipt families.

## Acceptance Criteria

- all opening identities and Git ordering evidence match;
- actual P2 validator/readout owners are used without copied evaluators;
- first real R1B-R2 pair has explicit linkage or is honestly ineligible;
- rollback rehearsal preserves trusted outcome and repository bytes;
- comparator classes, sampling formula and blind spots C07/C08/C18 remain exact;
- P4-I1 executes only from the closed input manifest;
- M0-M2 remain attributable and the new observation does not fabricate recall;
- exactly four paths, deterministic tests, zero provider/live/network calls,
  nothing staged or committed by worker;
- status is `CANARY_WINDOW_OPEN_EVIDENCE_CANDIDATE`, `ROLLBACK_SHADOW`,
  `SIMPLIFY_CANARY_TAX_EXCEEDED`, or `BLOCKED_WITH_REASON`;
- no P5, route replacement, safety success or cost-saving claim is emitted.

## Evidence / Verification

The worker returns recomputed source hashes, Git ancestry/blob evidence,
receipt-generation and linkage inputs, actual P2 observations, normalized
comparator rows, sampling and invariant results, rollback before/after hashes,
M0-M2 plus initial metrics, focused test output, exact manifest and no-commit
status. Reviewer challenges those proofs without recreating the implementation.

## Stop Conditions

Stop for identity mismatch, inability to prove return/receipt linkage,
non-ancestor trusted record, copied/weakened P2 evaluator, fifth path, secret
risk, external call need, semantic re-execution, sampling after outcome
disclosure, or any attempt to map incomplete evidence to clean consistency.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P4 population/comparator/tax contract | accepted design | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` | Dependency And Opening Rule through Acceptance Criteria | P4 shadow canary | accepted P4 design | ACCEPT |
| independent acceptance | adjudicated review | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_REVISION_1_INDEPENDENT_REREVIEW_2026-09-02.md` | disposition and acceptance boundary | design identity | reviewer evidence | ACCEPT |
| actual-seam prerequisite | accepted evidence | `docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md` | Independent Reviewer Adjudication | R1B-R2 identities and M2 | committed worker return | ACCEPT |
| receipt validator | executable source | `governance/compat/agent_autorun_machine_verification.py` | receipt integrity functions | `_validate_receipt_integrity` | P2 receipt owner | ACCEPT |
| receipt readout | executable source | `governance/compat/agent_automation_machine_verification_readout.py` | read/build/serialize functions | `read_receipt_readonly`; `build_machine_verification_readout` | P2 readout owner | ACCEPT |
| review admission and local repair | canonical standard | `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md` | review admission; reviewer-local repair | cost/admission fields | Review Cost owner | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch/no-commit markers; review-admission fields; Source Verification columns; protected paths; worker-return profile |
| gateRunPurpose | confirm the completed P4 authority packet and collect dispatch evidence |
| claimBoundary | checker PASS proves packet shape only, not canary safety, recall or cost outcome |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`shadow canary governance tax measurement`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

Disclosed defectIds: NONE

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P4 --title "Shadow Canary And Governance-Tax Measurement" --date 2026-09-02 --base 0b495a7177eaeb2af58141cea0069d7b01b925dc --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --root-cause-cluster-id mfrp-machine-first-review-canary --stdout` |
| generatedProfile | protected-governance-path internal no-commit initial |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | accepted identities, natural population, checkpoints, invariant, receipt linkage, measurement and rollback |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | bounded comparator and measurement fields |
| claimBoundary | dispatch provenance only; no canary result predeclared |

## Core Guard Self-Protection Authorization

Authorized scope is exactly the four-path manifest. No P2 owner, accepted R1B
artifact, checker, hook, standard, catalog, registry, session surface or route
authority may change.

Operator authorization: explicit instruction to proceed with the canary and
empirically measure redundant-review reduction without recall loss.

Rollback boundary: remove only the four uncommitted worker outputs and the
verified ignored P4 receipt directory; trusted-route artifacts remain intact.

## Claim Boundary

This baseline authorizes a local shadow canary and bounded evidence window. It
does not change the trusted route, prove correctness/recall/cost saving, open
P5, or authorize provider/live/public/deployment/production effects.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance canary evidence; no public sync is authorized.
