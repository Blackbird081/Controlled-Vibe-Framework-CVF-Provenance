# CVF GC-018 Baseline - MAO-T6 Timeout, Heartbeat, Cancel, Retry, And Recovery

Memory class: governed-dispatch-baseline

Status: HOLD_UNTIL_MAO_T5_PASS

Batch ID: MAO-T6

Dispatch base head: `3294d555a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Prepare, but do not dispatch, deterministic lifecycle-controller work covering
timeout, heartbeat, cooperative cancel, retry classification, duplicate
protection, orphan recovery, clock tests, and diagnostics.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T3 and T4 | accepted commits `052845fa1` and `f71ba01f6` | accepted material exists | ACCEPT |
| MAO-T5 | packet authored in this batch; no accepted execution evidence | accepted MAO-T5 completion and refreshed anchors required | HOLD |

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

Held design packet only; no lifecycle implementation may start before MAO-T5
acceptance and refreshed dependency-release evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Baseline Decision

Source-complete but dependency-held.

## Evidence / Verification

Current source symbols and dependency state were checked locally.
