# CVF GC-018 Baseline - MAO-T5 Designated Closer And Commit/Session Interlock

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MAO-RUNTIME-T5

Dispatch base head: `f1f895f31`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one local contract-and-test tranche for exactly-one-closer selection,
integration decision, closure conversion, commit-steward interlock, no-auto-
commit behavior, and a separate session-sync projection boundary.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T4 accepted | `f71ba01f6`; completion review records 78/78 tests and bounded acceptance | accepted T4 material commit exists | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`, role=`worker`, lifecyclePhase=`implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "multi-agent orchestration runtime" --role worker --lifecycle-phase implementation`

Returned defects: NONE_RETURNED

Disclosed defectIds: none.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | dependency evidence, Source Verification columns, no-commit route, reviewer closure conversion |
| gateRunPurpose | confirmation before dispatch |
| claimBoundary | dispatch structure only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| closer is a task role | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | `MaoTaskRole` | `MaoTaskRole` | task graph contract | ACCEPT |
| closer identity is carried by authority | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | authority envelope | `closerActorId` | task graph contract | ACCEPT |
| material and session sync commits are separate | LITERAL_INVARIANT | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | Commit Split Rule | `Commit Split Rule` | commit steward protocol | ACCEPT |

## Claim Boundary

Local deterministic contracts and tests only. No adapter receives commit
authority; no git mutation, provider call, durable runtime, public-sync, or
production claim is authorized for the worker.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T5 --title "Designated Closer And Commit Session Interlock" --date 2026-07-11 --base 3294d555a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic no-commit dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, dependency release, exact scope and gates |
| checkerReadAheadConfirmation | dispatch, handoff and ADIF checkers read |
| docOnlyNewFields | none in baseline |
| claimBoundary | authoring provenance only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation packet.

## Baseline Decision

Source and dependency accepted; dispatch waits only for session release.

## Evidence / Verification

Source searches, resolver output, dependency commit, and gates are evidence.
