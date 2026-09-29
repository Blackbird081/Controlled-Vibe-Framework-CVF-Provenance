# CVF GC-018 Baseline - MFRP-P3-R1B-R2 Actual-Seam Replay Repair

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Batch ID: MFRP-P3-R1B-R2

Dispatch base head: `5cf4d663b7b0f25e2faff24c12d1a0d8b363df05`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one bounded repair and replay of the existing R1B helper against the
reviewer-ratified R1A-R2 oracle. The repair closes the three adjudicated R1B
evidence gaps without changing P2, oracle semantics, review routes, or P4.

## Root Problem

The first R1B replay is useful rejected evidence but incomplete:

1. it did not recompute the seven historical source hashes or execute each
   locator/range/excerpt binding before replay;
2. its hostile source-drift test mutated oracle copies rather than the cited
   source bytes;
3. its ledger omitted same-domain base/mutated receipt digests and explicit
   false-negative/false-positive classification.

R1A-R2 corrected and ratified the oracle source binding at commit
`e15cf55d8060a44056f44dd819b399ae3aec1fb0`. This tranche consumes that
identity; it may not refresh or edit it.

## Frozen Input Identity

| Input | Required SHA-256 / identity |
|---|---|
| oracle containing commit | `e15cf55d8060a44056f44dd819b399ae3aec1fb0` |
| oracle raw file | `c6a8006265ff1968760101e380c779e2a031c870aa7ff3c6d0296df94dbebd43` |
| oracle all-field JCS | `5a6751a7b6cda0291792a476799594dde63bdfa7e13997b8a093f3cecfd8e97d` |
| oracle required-set JCS | `04be6dc1fa061e13af195c5490769bf88fba3309e2ddb4aa0ed24a8fd6440fca` |
| P2 receipt owner | `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` |
| P2 readout owner | `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` |
| R1 redesign | `22a086d7742dbdaec5b887fd377890962ad34396953f48287ce865f743766011` |
| accepted P4 design | `65698a95dc7bb7f437fe061a81559701b91a3e611c445f5122ad8145c5f13df5` |

All identities are recomputed before editing. Any mismatch stops the worker.

## Decision / Baseline

The worker modifies exactly the existing runner, its focused test, and its
deterministic result ledger, then creates one new R1B-R2 worker return. The old
R1B return stays immutable rejected evidence.

Before any case calls a P2 seam, the runner must:

- recompute all seven `sourceManifest` file hashes;
- reject unknown or path-mismatched source IDs;
- enforce `UTF8_NO_BOM_LF_NORMALIZED_LINE_RANGE_V1` exactly;
- reject BOM, invalid range, missing/duplicate locator inside the declared
  range, and excerpt digest drift;
- verify exact oracle/required-set/P2 owner identities and 19/18/7 coverage.

The hostile suite must drift the actual bytes supplied as one cited source
while leaving oracle pins unchanged, and prove rejection occurs before any P2
seam call. A test that merely edits oracle labels or expected hashes does not
satisfy this control.

## Receipt Digest And Classification Contract

For every case, ledger fields `baseReceiptDigest` and
`mutatedReceiptDigest` are SHA-256 over RFC 8785 JCS bytes of the complete
in-memory receipt payload, excluding no field. Both use the same byte domain.
Every representable non-control mutation must change the digest; the
`NO_MUTATION` control must preserve it.

Each case records one closed classification:

| Case condition | Classification |
|---|---|
| `NO_MUTATION`, valid control accepted and predicate satisfied | `TRUE_NEGATIVE` |
| `NO_MUTATION`, valid control rejected or predicate missed | `FALSE_POSITIVE` |
| representable mutation and required safety predicate satisfied | `TRUE_POSITIVE` |
| representable mutation and predicate missed | `FALSE_NEGATIVE` |
| feasibility is unrepresentable by current P2 | `NOT_REPRESENTABLE_BY_CURRENT_P2` |

The ledger also records explicit booleans `falseNegative` and `falsePositive`
consistent with the classification. Unrepresentable cases are excluded from
both booleans and every safety denominator. C15 remains an honest expected
false negative if its non-secret sentinel is emitted by current P2.

## Exact Artifact Manifest

| Artifact | Required action |
|---|---|
| `governance/compat/mfrp_actual_seam_replay.py` | MODIFY source binding, digest and classification evidence |
| `governance/compat/test_mfrp_actual_seam_replay.py` | MODIFY hostile regressions including genuine cited-source drift |
| `governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json` | MODIFY deterministic ledger from repaired runner |
| `docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md` | CREATE full evidence return |

No other repository path may change. Temporary test trees must be outside the
repository and removed by the test framework.

## Acceptance Criteria

- Frozen identities and current runner/test/ledger starting hashes match.
- Source binding executes before case replay and validates 7/19 bindings.
- Genuine cited-source byte drift fails before any seam call.
- Both real P2 seams observe the identical in-memory mutated payload.
- All representable cases record base/mutated full-receipt JCS digests.
- Every case has exactly one classification and consistent booleans.
- 19 cases, 18 families and seven required zero-tolerance classes reconcile.
- C07/C08/C18 remain visible and excluded as unrepresentable; C15 is not
  laundered.
- Two same-base runs produce byte-identical ledger output.
- Focused suite, worker-return gate and pre-implementation gate pass.
- Exactly four paths, zero provider/live/network calls, nothing staged or
  committed.

## Evidence / Verification

Worker evidence includes all frozen hashes, source-binding totals, cited-source
drift calibration, seam-call order, same-object proof, digest/classification
reconciliation, failed predicates, deterministic ledger identity, gate output,
exact manifest and no-commit proof. Reviewer reruns the helper/tests and
challenges one source byte, one classification and one owner-observed field;
reviewer does not recreate the implementation.

## Stop Conditions

Stop for oracle/P2/source identity drift, need to change P2 or oracle, inability
to reject cited-source drift before seam calls, unknown predicate/operator,
secret risk, fifth repository path, provider/live/network need, or any attempt
to hide an actual miss. Do not self-repair P4 prerequisites by altering the
measured system.

## P4 Boundary

Even a complete R1B-R2 replay does not automatically open P4. Reviewer must
first accept the replay and confirm zero unexplained divergence for
representable zero-tolerance cases. C07/C08/C18 stay outside the safety
denominator. P4 then still requires its own named invariant, work order and
rollback rehearsal under the accepted canary design.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| actual seam and ledger contract | governed design | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | Actual P2 Seam Contract; Source And Locator Binding; Result Ledger Contract | R1B runner and ledger | R1 redesign | ACCEPT |
| three repair findings | adjudicated evidence | `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md` | Independent Reviewer Adjudication | R1B-RV-1 through R1B-RV-3 | reviewer disposition | ACCEPT |
| corrected oracle identity | accepted evidence | `docs/reviews/CVF_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_WORKER_RETURN_2026-09-02.md` | Independent Reviewer Adjudication | `ORACLE_RATIFIED_BOUNDED` | R1A-R2 oracle | ACCEPT |
| P4 remains conditional | accepted design | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` | Dependency And Opening Rule | accepted R1B prerequisite | P4 design | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch/no-commit markers; review admission fields; Source Verification columns; protected paths; full worker-return profile |
| gateRunPurpose | confirm the completed authority packet and collect pre-dispatch evidence |
| claimBoundary | checker PASS cannot prove replay correctness, accept R1B-R2 or open P4 |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`actual seam replay repair`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "actual seam replay repair" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defect count: 0
- Returned defects: `NONE_RETURNED`
- Disclosed defectIds: `NONE`

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3-R1B-R2 --title "Actual-Seam Replay Repair" --date 2026-09-02 --base 5cf4d663b7b0f25e2faff24c12d1a0d8b363df05 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id mfrp-p3-r1b-replay-evidence --prior-finding-set-digest a042f80260042b7f71675edc57a8fb4e33ad5a1c70963c87a471d2123d85df5c --stdout` |
| generatedProfile | protected-governance-path internal no-commit rework |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact frozen identities, four-path repair, source-drift, digest/classification and P4 boundary |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | baseReceiptDigest, mutatedReceiptDigest, classification booleans |
| claimBoundary | dispatch provenance only; no replay outcome is predeclared |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify only the existing R1B runner/test
and deterministic result fixture, and create the named return. No P2 owner,
oracle, checker, hook, standard, catalog, registry or session file may change.

Protected paths:

- `governance/compat/mfrp_actual_seam_replay.py`
- `governance/compat/test_mfrp_actual_seam_replay.py`
- `governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json`

Operator authorization: explicit 2026-09-02 R1B repair authorization after
accepted R1A-R2 oracle correction.

Rollback boundary: restore the three existing artifacts to their pinned
starting bytes and remove only the new uncommitted R1B-R2 return.

## Claim Boundary

This baseline authorizes one local no-commit replay repair. It does not accept
R1B-R2, change P2/oracle, run P4, change review authority, or claim safety,
latency, quota, provider/live, public, deployment or production improvement.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair authority; no public sync is authorized.
