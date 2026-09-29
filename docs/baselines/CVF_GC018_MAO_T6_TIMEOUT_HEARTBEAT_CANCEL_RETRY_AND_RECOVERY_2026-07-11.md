# CVF GC-018 Baseline - MAO-T6 Timeout, Heartbeat, Cancel, Retry, And Recovery

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED

Batch ID: MAO-RUNTIME-T6

Dispatch base head: `cbf56ff50`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize the completed deterministic lifecycle-controller work covering
timeout, heartbeat, cooperative cancel, retry classification, duplicate
protection, orphan recovery, clock tests, and diagnostics.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T3 and T4 | accepted commits `052845fa1` and `f71ba01f6` | accepted material exists | ACCEPT |
| MAO-T5 | material `9b225f0e4`; completion review `REVIEWER_ACCEPTED_BOUNDED`; 54/54 tests and typecheck PASS | accepted material and review exist | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | HOLD dependency vocabulary and Source Verification columns |
| gateRunPurpose | confirmation for a held packet |
| claimBoundary | packet preparation only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| terminal timeout/cancel outcomes exist | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/read.model.contract.ts` | terminal outcome type | `MaoTerminalOutcome` | read model contract | ACCEPT |
| delegation diagnostics exist | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | diagnostic class | `MaoDiagnosticClass` | delegation adapter contract | ACCEPT |

## Claim Boundary

One local deterministic lifecycle contract/test tranche only. No provider,
real clock, queue, UI, public-sync, or production claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Baseline Decision

Dependency released; source-verified local worker dispatch ready.

## Evidence / Verification

Current source symbols and dependency state were checked locally.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T6 work order | CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | dated T6 completion review | REVIEWER_ACCEPTED_BOUNDED | PASS |
| Roadmap state | MAO roadmap T6 | accepted; T7 held | PASS |
| Registry JSON | GC-051 aggregate | generated and aligned | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | existing governed registry front door | PASS |
| External evidence digest | N/A with reason: local evidence only | N/A | N/A with reason: local evidence only |
| System loop interlock | current registry | unchanged | PASS |
| Session continuity | separate steward commit | pending | PASS |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id MAO-T6 --title "Timeout Heartbeat Cancel Retry And Recovery" --date 2026-07-11 --base 3294d555a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | held dependency promoted to no-commit dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | refreshed T5 evidence, anchors, exact outputs and gates |
| checkerReadAheadConfirmation | dispatch, handoff and ADIF checkers read |
| docOnlyNewFields | none in baseline |
| claimBoundary | authoring provenance only |
