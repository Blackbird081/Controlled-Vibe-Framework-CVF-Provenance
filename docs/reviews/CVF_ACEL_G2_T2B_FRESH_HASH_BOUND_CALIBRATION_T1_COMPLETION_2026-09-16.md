# CVF ACEL G2 T2B Fresh Hash-Bound Calibration T1 Completion

Memory class: governed-completion-review

Status: CLOSED_PASS_BOUNDED

docType: completion_review

Date: 2026-09-16

Batch ID: ACEL-G2-T2B-FRESH-HASH-BOUND-CALIBRATION-T1

Reviewer: Local reviewer/orchestrator

## Purpose

Record the operator-approved single-call calibration of the frozen ACEL G2 T2A
discriminating task against `qwen3.7-flash`, independently rescore the persisted
sanitized candidate, and issue the bounded Local disposition. This tranche does
not open runtime, T6B, a comparative trial, production, public sync, or
deployment.

## Target / Source

| Artifact | Role |
|---|---|
| operator instruction dated 2026-09-16 | direct authority for exactly one bounded live call |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/g2.t2.discriminating.task.contract.ts` | frozen task, parser, rubric, and release predicate |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/g2.t2.discriminating.task.contract.test.ts` | frozen negative and positive fixture corpus |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-acel-g2-t2b-fresh-hash-bound-calibration-t1.ts` | hash-bound one-call runner |
| `docs/reviews/evidence/acel-g2-t2b-fresh-hash-bound-calibration-t1-live-2026-09-16.json` | canonical secret-safe live receipt |

## Scope / Target / Owner Boundary

Scope was one direct `qwen3.7-flash` calibration request and offline review of
its persisted sanitized result. Target was the exact frozen T2A task. The
operator owned live authorization; Local owned preflight, execution, scoring,
technical disposition, and closure. Runtime composition, T6B, retries, task
redesign, comparison, production, public sync, and deployment were excluded.

## Scope / Methodology

Local verified clean starting state, recomputed the two frozen SHA-256 values,
confirmed the new receipt path was absent, checked credential-alias presence
without reading or printing the secret, ran the focused scorer suite and
TypeScript check, and passed pre-implementation autorun. The runner then made
one request through the governed Model Gateway harness and persisted only the
raw-output hash plus a parsed sanitized candidate. Reviewer phase independently
recomputed the rubric from that candidate and compared it with the receipt.

## Authority And Role Boundary

The operator explicitly approved `ACEL-G2-T2B-FRESH-HASH-BOUND-CALIBRATION-T1`
with exactly one `qwen3.7-flash` call, no retry, the two named hashes,
fail-closed behavior, and no runtime/T6B opening. The Local agent performed the
execution phase and then switched to reviewer phase after the receipt existed.
No subagent or external research agent was invoked. Local remains the technical
decision owner.

The bounded grant was limited to provider `alibaba`, `maxCalls: 1`, and subject
and delegation `ACEL-G2-T2B-FRESH-HASH-BOUND-CALIBRATION-T1`. The one attempted
call consumed the complete tranche budget. Repeat-live authority is absent.

## Frozen Inputs

| Input | Required SHA-256 | Observed SHA-256 | Disposition |
|---|---|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/g2.t2.discriminating.task.contract.ts` | `30a626eed0a411571ec854fe0f1f0bf3b20ee7cad343d76e32721e6a1a681bf4` | `30a626eed0a411571ec854fe0f1f0bf3b20ee7cad343d76e32721e6a1a681bf4` | MATCH |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/g2.t2.discriminating.task.contract.test.ts` | `4f6c9ccb6369cbb76cc2954cbbbd3601ea695fec0cb3ba60b1b6e0129df3f0d5` | `4f6c9ccb6369cbb76cc2954cbbbd3601ea695fec0cb3ba60b1b6e0129df3f0d5` | MATCH |

The runner recomputed both hashes before credential resolution or network
execution and would have persisted a zero-call blocked receipt on mismatch.

## Live Evidence

Canonical receipt:
`docs/reviews/evidence/acel-g2-t2b-fresh-hash-bound-calibration-t1-live-2026-09-16.json`

Receipt SHA-256:
`034c698c38eb462bed9b36ed4d32dca87c893a964df684760ca2bd08fc7ab204`

| Field | Evidence |
|---|---|
| provider/model | `alibaba` / `qwen3.7-flash` |
| endpoint host | `dashscope-intl.aliyuncs.com` |
| call count | `1` |
| retry count | `0` |
| latency | `26002 ms` |
| usage | `371` input tokens, `2001` output tokens |
| raw response | not persisted; SHA-256 `20eaf33d87bebd42f6d4ed99b06ab40a99a2cafa866d4a9ff747e38e74d38bd9`, length `605` |
| diagnostic | `null` |
| secret handling | only alias `DASHSCOPE_API_KEY` recorded; no value persisted or printed |

## Independent Review

The reviewer re-ran `evaluateDiscriminatingTask` offline against
`JSON.stringify(receipt.sanitizedCandidate)`. The recomputed result was:

```json
{"score":100,"defects":[],"materialDefectFound":false,"releaseCandidate":false}
```

This exactly matches the receipt. The candidate has the exact four-item step
order and dependency chain, every `maxConcurrent` is within the hard ceiling,
the rollback literals and skip behavior are exact, and the authority account is
exactly `svc-migrate` with no elevation claim.

## Findings And Decision

The live call succeeded and the calibration evidence is valid, but the task did
not discriminate this model: score is `100/100`, no material defect was found,
and the frozen candidate predicate is `false`. The approved selection rule was
that only score `<=80` or a material defect could produce a candidate for a
later comparative T2. Therefore:

- `FRESH_HASH_BOUND_CALIBRATION`: PASS;
- `DISCRIMINATING_VALUE_FOR_COMPARATIVE_T2`: NOT_ESTABLISHED;
- `QUALIFIED_FOR_T2_LIVE`: NO;
- `T6B_OR_RUNTIME_OPENED`: NO;
- terminal disposition: `CLOSED_PASS_BOUNDED_NO_RELEASE_CANDIDATE`.

No second call is justified or authorized. A future attempt requires a new
operator-approved task design and a new grant; this tranche cannot be retried.

## Risk / Corrective Action

| Risk | Evidence | Corrective action | Disposition |
|---|---|---|---|
| input drift before live execution | runner recomputed both named hashes before credential resolution | mismatch branch writes a zero-call blocked receipt | RESOLVED |
| accidental second call or overwrite | unique receipt collision guard plus `maxCalls: 1` grant | receipt now exists; no rerun performed or authorized | RESOLVED |
| secret leakage | receipt contains only alias and endpoint host; raw response stored only as hash plus sanitized parsed object | secret-safe local inspection; no raw credential or bearer header persisted | RESOLVED |
| treating success as comparative qualification | frozen predicate returned `false` at 100/no defects | terminal decision explicitly keeps comparative T2, runtime, and T6B closed | RESOLVED |
| paid exposure | operator explicitly authorized one bounded call after prior toggle uncertainty was disclosed | exposure capped to one call and actual usage recorded | ACCEPTED_BY_OPERATOR_BOUNDED |

## Verification Evidence

| Check | Result |
|---|---|
| pre-implementation autorun | PASS, 84/84 checks |
| focused scorer suite | PASS, 32/32 tests |
| TypeScript `--noEmit` | PASS |
| frozen hash check | PASS, 2/2 exact |
| live runner | PASS, one call, zero retries |
| independent persisted-candidate rescore | PASS, exact 100/no defects/false candidate |
| receipt collision guard | PASS; path was absent before execution and now blocks another invocation |
| secret-safe evidence review | PASS; alias only, no raw credential |

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE

outsideAuthorityBlockers: NONE

nextRepairRoute: NOT_APPLICABLE_CLOSEABLE

workerRedispatchAllowed: NO

providerCallCount: 1

retryCount: 0

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | direct operator instruction for this self-executed tranche | named T2B authority consumed; no delegated work order required | PASS |
| Completion or reviewer artifact | this completion review | `CLOSED_PASS_BOUNDED_NO_RELEASE_CANDIDATE` | PASS |
| Roadmap state | active ACEL program continuity | G2 T2 calibration closed; comparative/runtime lanes remain parked | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated GC-051 aggregate covers the runner | PASS |
| Registry Markdown | this review plus the GC-051 source entry | bounded calibration disposition recorded | PASS |
| External evidence digest | canonical secret-safe receipt | receipt sha256 `034c698c38eb462bed9b36ed4d32dca87c893a964df684760ca2bd08fc7ab204`; one provider response hash and sanitized candidate | PASS |
| System loop interlock | isolated runner and existing Model Gateway harness | no runtime or T6B consumer opened | N/A with reason: direct calibration was intentionally isolated |
| Session continuity | active front door/bootstrap/state/handoff | post-material synchronization required | N/A with reason: separate continuity commit follows material commit |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `CLOSED_PASS_BOUNDED`; `Review-Cost Telemetry: REQUIRED`; Machine Closure Package; Agent Operation Trace Block; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm bounded live closure packaging after the one permitted call; never discover or justify another call |
| claimBoundary | one calibration observation only; no runtime/T6B/retry/public authority |

## Review Cost Telemetry And Stop Disposition

Review-Cost Telemetry: REQUIRED

reviewRoundCount: 1

workerRepairTurnCount: 0

newRootCauseCountThisRound: 0

dependentFindingCountThisRound: 7

elapsedReviewMinutes: NOT_AVAILABLE_WITH_REASON: no reliable end-to-end review timer is recorded

providerCallCount: 1

tokenOrQuotaUsage: 2372

valueDelta: produced one valid fresh hash-bound calibration point and decisively rejected opening comparative T2/T6B for this task

stopDisposition: COMPLETE_REVIEW

preRepairAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

materialCommitCount: 0

continuityCommitCount: 0

commitPlanDisposition: DEFAULT_ONE_MATERIAL_ONE_CONTINUITY

latencyDisposition: EXPECTED_LONG_RUNNING_PROOF

avoidableDelayClass: GATE_DISCOVERY_LOOP

## Epistemic Process Block

### Expected Result / Prediction

The frozen task would be useful for a later comparison only if the fresh model
scored at most 80 or produced a material defect. Otherwise the tranche would
close without opening comparative execution.

### Evidence Comparison

The live candidate scored 100, produced no defect, and independently rescored
to the same result. This contradicts the hoped-for discrimination while
confirming the runner, frozen hashes, and deterministic grader behaved as
specified.

### Contradiction Or Gap Disposition

The lack of discrimination is a terminal negative calibration result, not a
runner defect. It is preserved without retry. The missing comparative-value
basis remains closed rather than being filled with another call.

### Claim Update

CVF now has one accepted fresh direct observation for the frozen T2A task. The
task is not a release candidate for comparative T2, and no runtime/T6B claim is
added.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/orchestrator, temporally separated execution and review roles |
| Provider or surface | private CVF workspace and governed Alibaba Model Gateway lane |
| Session or invocation | `ACEL-G2-T2B-FRESH-HASH-BOUND-CALIBRATION-T1`, 2026-09-16 |
| Working directory | repository root; runner invoked from `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION` |
| Command or tool surface | read-only preflight, apply_patch, vitest, TypeScript, autorun gate, one `npx tsx` runner invocation, offline rescore, reviewer gates |
| Target paths | runner, canonical receipt, completion review, GC-051 entry/aggregate, later continuity surfaces |
| Allowed scope source | explicit operator authorization for the named tranche and exact live boundary |
| Before status evidence | clean HEAD `914cb79f0460f9272724d204ea44464e072558f8`; receipt absent; two frozen hashes matched |
| After status evidence | one new runner, one new receipt, this review, and GC-051 coverage pending material commit; provider call budget exhausted |
| Diff evidence | `git status --short`, `git diff --check`, exact receipt and hash inspection |
| Approval boundary | one `qwen3.7-flash` call, zero retry, exact two hashes, fail-closed, no runtime/T6B |
| Claim boundary | direct calibration only; no comparative, production, public, or deployment claim |
| Agent type | INTERNAL_AGENT / Local decision owner |
| Invocation ID | `acel-g2-t2b-fresh-hash-bound-calibration-t1-2026-09-16` |
| Expected manifest | runner; receipt; completion review; GC-051 source entry; generated aggregate |
| Actual changed set | same five material paths before continuity synchronization |
| Manifest delta | MATCH |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| model | `qwen3.7-flash` | `qwen3.7-flash` | PASS |
| call budget | exactly 1 | `callCount: 1` | PASS |
| retry budget | 0 | `retryCount: 0` | PASS |
| contract hash | `30a626...1bf4` | exact match | PASS |
| test hash | `4f6c9c...0d5` | exact match | PASS |
| response safety | raw hash plus sanitized candidate only | no raw response or credential value persisted | PASS |
| release predicate | score `<=80` or material defect | score 100, no defect, predicate false | PASS |
| runtime/T6B boundary | closed | no runtime or T6B surface changed | PASS |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: this is private provenance calibration evidence. No public artifact,
public-sync remote, catalog claim, or export was authorized.

## Claim Boundary

This review proves one hash-bound direct calibration observation for
`qwen3.7-flash` on 2026-09-16. It does not prove general model capability,
cross-model value, MAO value, runtime readiness, T6B readiness, production
readiness, or public export readiness. It grants no repeat-live authority.

## Terminal Decision

`CLOSED_PASS_BOUNDED_NO_RELEASE_CANDIDATE`
