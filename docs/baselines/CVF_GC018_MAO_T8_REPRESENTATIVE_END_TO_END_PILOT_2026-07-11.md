# CVF GC-018 Baseline - MAO-T8 Representative End-To-End Pilot

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED

Batch ID: MAO-T8

Dispatch base head: `47ed44b12`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Reserve one representative worker-reviewer-revision-closer proof lane plus
negative self-approval, duplicate, timeout, cancel, and budget evidence.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T1 through T7 | accepted completion chain through T7 material commit `2ae63592e` and session sync `47ed44b12` | prerequisite evidence exists | ACCEPT |
| bounded pilot selection | `docs/reviews/CVF_MAO_T8_REPRESENTATIVE_PILOT_SELECTION_CHECKPOINT_2026-07-11.md` selects `MAO-T8-LOCAL-STALE-READOUT-REPAIR` | task, proof class, and provider disposition recorded | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | pilot dependency and live-proof boundary |
| gateRunPurpose | confirmation for a held packet |
| claimBoundary | no pilot execution or live claim |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| pilot concurrency ceiling exists | LITERAL_INVARIANT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | budget validation | `PILOT_MAX_CONCURRENT_ROLES` | task graph contract | ACCEPT |
| self-approval guard exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/reviewer.isolation.contract.ts` | identity guard | `checkSelfApproval` | reviewer isolation contract | ACCEPT |
| stale readout classifier exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | freshness policy | `classifyReadoutFreshness` | evidence/readout contract | ACCEPT |
| one-revision ceiling exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/dissent.revision.contract.ts` | revision ceiling | `checkRevisionCeiling` | dissent/revision contract | ACCEPT |
| designated closer validation exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/closer.interlock.contract.ts` | closer identity | `checkCloserIdentity` | closer interlock contract | ACCEPT |

## Claim Boundary

One deterministic local stale-readout repair pilot only. No provider, network,
production runtime, UI, public-sync, or durable-queue claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Baseline Decision

Dependencies, pilot selection, and reviewer-repaired local proof are accepted.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_2026-07-11.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MAO_T8_REPRESENTATIVE_END_TO_END_PILOT_COMPLETION_2026-07-11.md` | reviewer acceptance | PASS |
| Roadmap state | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | T8 bounded pilot complete; T9 remains | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated GC-051 aggregate | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | no Markdown regeneration required | PASS |
| External evidence digest | N/A with reason: local deterministic proof only | no external evidence | N/A with reason: not applicable |
| System loop interlock | T8 completion review | monotonic revision evidence required | PASS |
| Session continuity | active state and handoff | refreshed after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| focused pilot tests | PASS | 25/25 PASS | PASS |
| revision time order | monotonic | backward-time revision rejected | PASS |
| fresh revision evidence | new receipt before re-review | revision OUTPUT receipt appended | PASS |

## Evidence / Verification

Current source symbols and dependency state were checked locally.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind direct --batch-id MAO-T8 --title "Representative End To End Pilot" --date 2026-07-11 --base 47ed44b12 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | direct no-commit dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | selected pilot, accepted dependencies, sources, anchors, and boundaries |
| checkerReadAheadConfirmation | dispatch, handoff, ADIF, and scaffold checkers read |
| docOnlyNewFields | pilot task ID and proof class live only in selection checkpoint |
| claimBoundary | authoring provenance only |
