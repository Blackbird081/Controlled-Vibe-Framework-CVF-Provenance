# CVF GC-018 Baseline - DARA-T3 R1 WP-ARCH-003 Historical Replay Repair

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-07

Batch ID: DARA-T3-R1-WP-ARCH-003-HISTORICAL-REPLAY-REPAIR

Dispatch base head: `537dad6ce752f75d6dc2e36e272639758e7ca829`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: orchestrator/reviewer

Worker target: one bounded external replay-repair worker reached only by
operator manual relay

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Authorize one consolidated repair of the rejected DARA-T3 exact-five replay
packet. The repair must replace tautological seeded results with observed
output from the accepted DARA admission validator, make error accounting
input-sensitive, and prove fixture/ledger byte freeze. It does not repair or
accept `WP-ARCH-003`.

## Accepted Authority

| Authority | Accepted fact |
|---|---|
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_COMPLETION_REVIEW_2026-09-07.md` at `537dad6ce752f75d6dc2e36e272639758e7ca829` | Initial return is `RETURN_TO_DESIGN`; findings DARA-T3-R1-01 through R1-03 are frozen. |
| operator instruction, 2026-09-07 | Codex remains orchestrator/reviewer; operator will manually relay one repair packet to Claude. |
| `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md` | Current DARA schema and fail-closed admission rules remain the replay oracle. |
| original paired baseline and work order | Seven source identities, three raw cases, exact-five manifest and all parked boundaries remain binding except where this amendment is stricter. |

## Source / Predecessor Evidence

The predecessor is the rejected exact-five return at execution base
`b23f0b7db8b24993f999ba38d9f445b89a06fa76`; its byte identities are recorded
in the committed completion review. The review commit
`537dad6ce752f75d6dc2e36e272639758e7ca829` is the immutable R1 authority.

## Scope / Target / Owner Boundary

Target: repair the same five pending DARA-T3 paths only. The worker owns code,
fixture, tests and worker evidence within those paths. The orchestrator/reviewer
owns acceptance, closure artifacts, commits and continuity. All other paths and
all runtime/external effects remain outside scope.

## Decision / Baseline

The original worker material is retained in place as a rejected candidate.
R1 may edit exactly the same five uncommitted files. It must not create a new
return, fixture, ledger, helper or test path.

Seeded cases must contain defect-bearing structured stimulus. For every seeded
case the helper must derive actual output solely from that stimulus, current
accepted DARA code and frozen repository sources. Expected result fields,
`sourceFinding`, `note`, case ID and family labels must not influence actual
classification.

The preferred oracle entrypoint is the existing
`check_work_order_dispatch_quality_range._validate_architecture_readiness_admission`
function applied to deterministic synthetic work-order text built from the
structured stimulus. Equivalent composition of existing DARA validation
primitives is allowed only if no semantic validation rule is copied into the
new helper. Do not add or edit an active checker.

## Consolidated Repair Contract

| Finding | Required repair | Mandatory regression |
|---|---|---|
| DARA-T3-R1-01 | add structured stimulus for all ten seeded families and compute actual earliest stop/violation from accepted DARA validation | changing/removing defect-bearing stimulus changes the observed result or blocks the case; changing only expected/prose fields never changes observed output |
| DARA-T3-R1-02 | compute false-positive, false-negative and zero-tolerance metrics from observed versus expected values | an intentionally uncaught zero-tolerance stimulus forces `RETURN_TO_DESIGN`; a wrong expectation is counted rather than copied; no metric is constant |
| DARA-T3-R1-03 | capture fixture and ledger SHA-256 externally before replay and again afterward | pre/post hashes for both artifacts are equal and recorded without self-referential editing |

The raw Initial/R1/R2 source-hash and declaration measurements may be retained
when unchanged and reverified. Their prior PASS does not excuse seeded replay
or freeze-evidence failure.

## Required Artifact Manifest

| Path | Worker action |
|---|---|
| `governance/compat/fixtures/dara_t3_wp_arch_003_historical_replay.json` | MODIFY in place: add structured seeded stimuli; preserve seven frozen source hashes and three raw source identities. |
| `governance/compat/dara_t3_historical_replay.py` | MODIFY in place: execute accepted DARA validation and derive real metrics. |
| `governance/compat/test_dara_t3_historical_replay.py` | MODIFY in place: add input-sensitivity, false-positive/negative and exit-code regressions. |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_LEDGER_2026-09-07.md` | MODIFY in place: reconcile R1 results and freeze receipts without erasing rejected history. |
| `docs/reviews/CVF_DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY_WORKER_RETURN_2026-09-07.md` | MODIFY in place: preserve initial review history, add R1 command/result evidence and truthful terminal status. |

No sixth path may change. Historical sources, DARA production checkers,
roadmap, baselines, work orders, completion review, hooks, session state and
`WP-ARCH-003` artifacts are read-only to the worker.

## Minimum Replay Contract

- Exactly three raw cases and at least ten seeded cases remain.
- Every seeded case includes an `oracleInput` or equivalent structured field
  sufficient to execute the accepted validator without reading expected fields.
- Every result names oracle entrypoint, observed issue tokens, expected issue
  token, actual earliest stop, actual violation class and match disposition.
- Duplicate owner, missing registration, missing runtime consumer, unresolved
  trust source, placeholder path, rollback escape, self-authored acceptance,
  unknown usage, exhausted ceiling and unclassified applicability are each
  independently stimulated.
- One clean control case must pass without a violation so false-positive
  measurement is executable rather than a constant. The control may be an
  additional seeded case, raising the total above thirteen.
- Zero-tolerance recall is calculated from observed blocked results; a missed
  required class returns `RETURN_TO_DESIGN`.
- Source drift returns `BLOCKED_WITH_REASON`.
- CLI exits nonzero for `RETURN_TO_DESIGN`, `BLOCKED_WITH_REASON` or malformed
  input and zero only for `REPLAY_BLOCKS_AVOIDABLE_INVOCATIONS`.
- Two clean runs produce byte-identical normalized JSON.

## Freeze Evidence Contract

The fixture and ledger may be repaired before the first R1 replay. Immediately
before that replay, write neither artifact again. Capture their hashes into an
external command-output file outside the repository or the operator transcript,
run both replay commands and all post-freeze checks, capture both hashes again,
then add the pre/post values to the worker return only. The ledger itself must
not embed a hash that changes its own bytes. Any required post-first-replay
fixture or ledger edit returns `RETURN_TO_DESIGN`.

## Reviewer Strategy

The reviewer consumes the R1 diff and returned evidence, recomputes seven
source hashes, samples one matrix, semantic, quota and clean-control stimulus,
and reruns focused helper/tests plus standard fast gates. The reviewer must not
recreate the fixture or full case analysis.

## Evidence / Verification

Dispatch evidence consists of the committed rejection, the unchanged seven
source hashes, exact-five pending status, operator rework direction, ADIF
resolver output, scaffold provenance and successful pre-dispatch gates.
Implementation effectiveness remains unverified until the R1 worker return is
independently reviewed.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: DARA-T3-WP-ARCH-003-HISTORICAL-REPLAY

reviewRoundCount: 1

priorFindingSetDigest: 88aabb6fcc1043945efde94d0010f67c508bf0fdffc883ace2406a9ad260b63d

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: DARA-T3-R1-01,DARA-T3-R1-02,DARA-T3-R1-03

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 1

externalInvocationCeiling: 2

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY

reworkGeneration: 1

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

successorTrancheOpened: NO

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-readiness historical replay repair`,
role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch status, REWORK convergence fields, exact manifest, architecture admission, no-commit return, private export and trace fields |
| gateRunPurpose | confirm the bounded R1 dispatch contract before operator relay |
| claimBoundary | structural conformance does not prove the repaired replay |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id DARA-T3-R1-WP-ARCH-003-HISTORICAL-REPLAY-REPAIR --title "DARA T3 R1 WP-ARCH-003 Historical Replay Repair" --date 2026-09-07 --base 537dad6ce752f75d6dc2e36e272639758e7ca829 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind REWORK --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 1 --root-cause-cluster-id DARA_T3_WP_ARCH_003_HISTORICAL_REPLAY --prior-finding-set-digest 88aabb6fcc1043945efde94d0010f67c508bf0fdffc883ace2406a9ad260b63d --cumulative-external-invocation-count 1 --external-invocation-ceiling 2 --new-independent-critical-evidence DARA-T3-R1-01,DARA-T3-R1-02,DARA-T3-R1-03 --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit external REWORK profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | bound committed review, exact-five in-place repair, real-oracle stimulus, error accounting and external freeze receipts |
| checkerReadAheadConfirmation | dispatch, convergence, source, protected-path, return, trace and public guards read |
| docOnlyNewFields | `oracleInput`, `observedIssueTokens`, and external freeze receipt fields are evidence schema only |
| claimBoundary | dispatch provenance only; no replay success claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes one final same-parent external R1 repair of the exact
five pending DARA-T3 artifacts through operator manual relay. It does not
accept the current replay, implement `WP-ARCH-003`, open DARA-T4, authorize a
third external invocation, let Codex invoke Claude/CLI/MCP, run a provider or
live call, expose credentials, publish, deploy, push or claim production
readiness.
