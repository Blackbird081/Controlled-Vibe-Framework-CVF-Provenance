# CVF GC-018 Baseline - SCEC-E2 Evidence-Binding Effectiveness Validation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: SCEC-E2

Dispatch base head: `a5a4fbbc78fc8ad3f2e9541ee5572a8730d3fe7e`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

Worker target: external governance validation worker

successorTrancheOpened: NO

## Purpose

Run one bounded, adversarial effectiveness validation of the SCEC blocker-resolution
evidence contract closed at `cb6d4bc3879a753eb9abc7283b55148c141c46d1`.
The test must determine whether the live checker rejects unsupported resolution,
mutated or stale evidence, and predecessor evidence drift while accepting a valid
resolution control. This is the final validation step for this named hardening
claim, not another GC010 product tranche.

## Root Problem

SCEC-E1 showed that blocker counts could shrink in a replay even when accepted
review evidence did not support the claimed resolution. T1-R2 added explicit
`resolutionEvidence` binding and reviewer-corrected predecessor hash
revalidation. Machine tests passing inside the implementation tranche are not
alone sufficient evidence that the control works as a user-visible governance
constraint. One independent, source-derived adversarial evaluation is required.

## Accepted Authority

- The active SCEC standard owns evidence-binding invariant 13 and predecessor
  consumption rules.
- The committed checker at material commit `cb6d4bc38` owns executable behavior.
- The T1-R2 worker return records the reviewer corrections and accepted proof.
- Focused checker tests are implementation evidence, not an oracle to copy.
- GC010 product/runtime and all automatic same-problem successors remain parked.

## Decision / Baseline

The worker must construct fresh temporary cases independently of the committed
test fixtures and exercise the live checker or its public validation functions.
The minimum matrix is:

1. valid accepted-review resolution evidence is accepted;
2. missing evidence for a resolved blocker is rejected;
3. an extra evidence key not present in `resolved` is rejected;
4. unsafe, missing, or non-file evidence paths are rejected;
5. malformed, stale, or content-mismatched SHA-256 is rejected;
6. missing or unresolved locator is rejected;
7. executable proof missing its claim link or required proof relationship is rejected;
8. a successor whose predecessor evidence hash drifted is rejected through
   `PREDECESSOR_BLOCK_INVALID` and the underlying mismatch;
9. a valid successor consuming an unchanged valid predecessor is accepted.

Allowed verdicts are exactly:

- `EFFECTIVE`
- `EFFECTIVE_WITH_HARDENING_REQUIRED`
- `INEFFECTIVE_REOPEN_FOUNDATION`

Any required negative case being accepted, or either valid control being
rejected for an actual contract defect, forces `INEFFECTIVE_REOPEN_FOUNDATION`.
Every verdict retains `successorTrancheOpened: NO`.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Every resolved blocker requires exact evidence-key coverage and bound path/hash/locator data | contract | `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | Resolution Evidence Binding; invariant 13 | `resolutionEvidence` | SCEC control plane | ACCEPT |
| The checker validates evidence paths, hash shape/content, locator presence, evidence class, and executable claim linkage | executable source | `governance/compat/check_semantic_convergence_control.py` | resolution-evidence validators | `_validate_resolution_evidence` | SCEC checker | ACCEPT |
| Successor validation revalidates predecessor evidence through the same resolver | executable source | `governance/compat/check_semantic_convergence_control.py` | predecessor validation | `validate_block` predecessor call | SCEC checker | ACCEPT |
| Reviewer found and repaired the initial inheritance bypass and size defects | accepted review | `docs/reviews/CVF_SCEC_T1_R2_BLOCKER_RESOLUTION_EVIDENCE_BINDING_AND_HISTORICAL_REPLAY_CORRECTION_WORKER_RETURN_2026-08-31.md` | Independent Reviewer Correction; Decision | predecessor hash revalidation | SCEC-T1-R2 review | ACCEPT |
| Focused tests cover implementation behavior but must not replace independent case construction | regression source | `governance/compat/test_check_semantic_convergence_control.py` | resolution-evidence test classes | focused SCEC unit suite | SCEC regression suite | ACCEPT |

## Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/assessments/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_2026-08-31.md` | CREATE the independent case matrix, observed violation ledger, verdict, and next-move recommendation |
| `docs/reviews/CVF_SCEC_E2_EVIDENCE_BINDING_EFFECTIVENESS_VALIDATION_WORKER_RETURN_2026-08-31.md` | CREATE the exact no-commit worker return with a checker-valid successor SCEC block |

No other path is authorized. Both outputs remain uncommitted for independent
reviewer inspection.

## Acceptance Strategy

Acceptance requires fresh case construction, exact expected-versus-observed
violation codes, both positive controls, all mandatory negative families, a
single allowed verdict, no source edit, no provider/network use, and an exact
two-path uncommitted manifest. The worker must distinguish checker behavior
from semantic truth: this test proves declared evidence binding and drift
detection only.

## Evidence / Verification

Run the pre-implementation gate, focused SCEC unit suite, direct SCEC checker,
the independently constructed case runner, worker-return fast gate,
`git diff --check`, and exact `git status --short --untracked-files=all`.
No release-quality live proof is applicable or authorized.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring dispatch SCEC effectiveness validation`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring dispatch SCEC effectiveness validation" --role dispatcher --lifecycle-phase dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE |
| Dispatch impact | Direct reads of the SCEC standard, checker, T1-R2 return, literal gotchas, and applicable dispatch checkers remain mandatory. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Commit mode: WORKER_MUST_NOT_COMMIT`; Source Verification dispositions; exact SCEC fields and violation tokens; prompt-envelope fields; worker-return headings; `successorTrancheOpened: NO` |
| gateRunPurpose | Confirm the completed packet against known contracts; gates are not the first discovery mechanism. |
| claimBoundary | Read-ahead covers dispatch and declared-evidence shape only; independent review owns semantic acceptance. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SCEC-E2 --title "Evidence-Binding Effectiveness Validation" --date 2026-08-31 --base a5a4fbbc7 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --scec-problem-key scec-evidence-binding-effectiveness-validation --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit external-worker profile and initial SCEC state |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with exact two-path scope, nine-case adversarial matrix, verdict rules, proof boundary, and gates. |
| checkerReadAheadConfirmation | Applicable checker sources named above were inspected before completing this packet. |
| docOnlyNewFields | effectiveness case identifiers and observed-violation ledger only |
| claimBoundary | Dispatch provenance only; no product/runtime or semantic-truth claim. |

## Claim Boundary

This baseline authorizes one validation-only SCEC-E2 assessment and return. It
does not authorize SCEC source/checker/test edits, GC010 product/runtime work,
T1J-R4, T1K, T2, provider/live/network use, public sync, deployment,
production, or an automatic successor.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-effectiveness validation; no public-sync
batch is authorized.
