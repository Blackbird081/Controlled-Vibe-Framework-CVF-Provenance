# CVF GC-018 Baseline - MAO-LIVE-T1 Provider Adapter Value Pilot

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_VALUE_NOT_PROVEN

Batch ID: MAO-LIVE-T1

Dispatch base head: `93662e2a2`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one bounded same-task live comparison between a direct Model Gateway
call and a governed MAO worker-reviewer-revision-closer chain.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| deterministic MAO foundation | closed at `29c55ca36` | ACCEPT |
| current live provider health | canonical bundle PASS at `a0b40ecfb` | ACCEPT |
| decision-first roadmap | `docs/roadmaps/CVF_MAO_LIVE_PROVIDER_ADAPTER_VALUE_PILOT_ROADMAP_2026-07-12.md` at `82b3fb511` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`live multi-agent provider adapter pilot`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | source table, live diagnostic boundary, handoff fields, export token, trace labels |
| gateRunPurpose | dispatch confirmation |
| claimBoundary | one bounded live value pilot only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| live execute adapter factory | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported factory | `createOpenAiCompatibleExecuteAdapter` | Model Gateway live harness | ACCEPT |
| live harness options | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | exported interface | `LiveProofHarnessOptions` | Model Gateway live harness | ACCEPT |
| MAO invocation request | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | request interface | `MaoInvocationRequest` | MAO delegation adapter | ACCEPT |
| MAO local review chain | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/representative.pilot.contract.ts` | pilot orchestration | `runPilotChain` | MAO representative pilot | ACCEPT |
| live key bootstrap | RUNTIME_BEHAVIOR | `scripts/run_cvf_release_gate_bundle.py` | provider env bootstrap | `bootstrap_live_provider_env` | release gate bundle | ACCEPT |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES |
| runtimeMutationAuthorized | YES_BOUNDED |
| freshnessVerificationMode | FRESH_LIVE_RECOMPUTE_REQUIRED |
| prior evidence | `a0b40ecfb` proves CVF live health, not MAO live orchestration |
| requiredFutureAction | run MAO-LIVE-T1 once within four-call budget and capture diagnostics |

## Claim Boundary

One provider lane, one task/rubric, maximum four calls, private provenance only.
No durable queue, UI, public-sync, provider parity, production, or broad tuning.

## Baseline Decision

Bounded live comparison completed; value was not proven on the selected task.

## Evidence / Verification

Source symbols, prior live receipt, call ceiling, and clean base HEAD were checked locally.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id MAO-LIVE-T1 --title "Live Provider Adapter Value Pilot" --date 2026-07-12 --base 93662e2a2 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | runtime-provider-live plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | dependencies, sources, live budget, exact boundary |
| checkerReadAheadConfirmation | dispatch, handoff, public, trace checkers read |
| docOnlyNewFields | value verdict and comparative metrics only |
| claimBoundary | dispatch authoring provenance only |
