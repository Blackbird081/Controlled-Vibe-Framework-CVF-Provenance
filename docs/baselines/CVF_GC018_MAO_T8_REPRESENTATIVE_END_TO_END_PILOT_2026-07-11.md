# CVF GC-018 Baseline - MAO-T8 Representative End-To-End Pilot

Memory class: governed-dispatch-baseline

Status: HOLD_UNTIL_MAO_T7_PASS_AND_FRESH_PILOT_SELECTION

Batch ID: MAO-T8

Dispatch base head: `3294d555a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Reserve one representative worker-reviewer-revision-closer proof lane plus
negative self-approval, duplicate, timeout, cancel, and budget evidence.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-T1 through T7 | T5-T7 not accepted | all prerequisite completion evidence refreshed | HOLD |
| bounded pilot selection | no fresh selected task | operator-approved task and proof class required | HOLD |

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

## Claim Boundary

Held pilot envelope only. A fresh pilot-selection packet must decide whether
real-provider proof is claimed and therefore whether mandatory live governance
proof and diagnostics apply.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Baseline Decision

Source-complete but dependency and pilot-selection held.

## Evidence / Verification

Current source symbols and dependency state were checked locally.
