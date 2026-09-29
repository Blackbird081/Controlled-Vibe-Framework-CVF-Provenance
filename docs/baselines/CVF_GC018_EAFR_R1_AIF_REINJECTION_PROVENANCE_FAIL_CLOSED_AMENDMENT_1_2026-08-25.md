# CVF GC-018 Baseline - EAFR-R1 Amendment 1 Execution Anchor Repair

Memory class: SUMMARY_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-25

Batch ID: EAFR-R1-AMENDMENT-1

Commit mode: `WORKER_MUST_NOT_COMMIT`

rawMemoryReleased=false

Decision owner: current independent orchestrator under explicit operator authority

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1-AMENDMENT-1 --title "EAFR-R1 Amendment 1 Execution Anchor Repair" --date 2026-08-25 --base 8e6447a47 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | execution-anchor negative/control proof only |
| checkerReadAheadConfirmation | autorun, task-route, active-state and dispatch-quality sources read before amendment |
| docOnlyNewFields | none |
| claimBoundary | amendment provenance only; no runtime implementation claim |

## Purpose

Repair only the parent packet's pre-implementation base-anchor command. The
parent pre-dispatch base crosses later continuity commits and therefore mixes
material and session paths. The worker must instead capture the clean current
HEAD as `executionBaseHead` and run pre-implementation on that execution range.

## Source Evidence

| Source | Evidence | Disposition |
| --- | --- | --- |
| parent work order | pre-flight hard-codes `80bf3e850` | ACCEPT_AS_PACKET_DEFECT |
| continuity history | dispatch `4c5040573`, session sync `fda60640c`, handoff sync `8e6447a47` | ACCEPT |
| negative probe | pre-implementation from `80bf3e850` fails mixed-range diagnostics and path-family routing | ACCEPT |
| control probe | pre-implementation with base equal to current clean HEAD passes 80/80 | ACCEPT |

## Scope

This amendment changes command authority only. It does not change any parent
source/test ownership, acceptance invariant, reason token, risk ceiling,
worker-return path, role separation, no-live rule, or no-commit rule.

## Baseline Decision

`REPLACE_PREFLIGHT_BASE_ONLY`: after startup reads and before edits, capture
`$eafrExecutionBase = git rev-parse HEAD`; use that value for the three parent
pre-flight gates. Every other parent instruction remains controlling.

## Evidence Verification

The orchestrator must commit this paired amendment, run dispatch gates, and
sync the handoff. The worker must record the captured execution base and exact
80/80 pre-implementation result before material edits.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_active_session_state.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| literalTokensReviewed | executionBaseHead; `WORKER_MUST_NOT_COMMIT`; `DISPATCH_READY`; pathFamilies |
| gateRunPurpose | confirm and record the command-anchor repair after negative and control probes; not first discovery |
| claimBoundary | gate conformance does not prove the parent runtime implementation |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private dispatch command repair only.

## Claim Boundary

This baseline supersedes only the three hard-coded parent pre-flight base
arguments. It authorizes no implementation by the orchestrator, no scope
expansion, no live/provider/API-key activity, no commit by the worker, and no
closure or readiness claim.
