# CVF GC-018 Baseline - MAO-OA-T3 Operational Worker Launcher And Liveness Wiring

Memory class: FULL_RECORD

Date: 2026-07-17

Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR

GC-018 ID: MAO-OA-T3

Risk class: R2

Commit mode: WORKER_MUST_NOT_COMMIT

Dispatch base: `adff6895b`

Governing roadmap:
`docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md`

Paired work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T3_OPERATIONAL_WORKER_LAUNCHER_AND_LIVENESS_WIRING_2026-07-17.md`

## Purpose

Release one bounded execution-plane implementation tranche that composes the
accepted durable run store, provider-neutral fake/local delegation adapter, and
deterministic lifecycle controller behind one operational worker-launcher
owner. The tranche covers durable admission/start/completion milestones,
liveness-only heartbeat, timeout recording, cooperative cancellation, and
duplicate-launch prevention without a real provider call.

## Baseline Decision

`CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR`.

The operator checkpoint on 2026-07-17 releases T3 authoring and dispatch.
MAO-OA-T2 is independently accepted at material commit `042abf44b`; its
completion review records 21/21 focused tests, package typecheck, 1689 package
tests, generated registry alignment, and reviewer-fast 62/62. T4-T7 remain
parked.

## Scope / Target / Owner Boundary

New owner:
`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts`.

The new owner must compose, not duplicate:

- `MaoFileRunStore` for durable graph/event truth;
- `MaoDelegationAdapter` as the existing provider-neutral fake/local invocation
  implementation; and
- `MaoLifecycleController` for deterministic heartbeat, timeout, cancellation,
  retry classification, and duplicate guards.

The owner is exported only from the existing MAO local barrel. The existing
package-root forwarding export from T1 makes that local export discoverable.

## Non-Goals

- no control-plane import from execution-plane source;
- no direct `ProviderRouterContract` import or duplicated provider-selection
  policy;
- no real provider, network, API key, queue, process, worker-thread, shell,
  server, browser, CLI, MCP, UI, or workspace-state mutation;
- no new task graph, role resolver, event ledger, durable store, delegation
  adapter, lifecycle controller, reviewer, dissent, closer, or readout owner;
- no T4 reviewer/closer execution, T5 operator projection, T6 hard-task/live
  proof, or T7 roadmap closure;
- no automatic commit, session mutation, public-sync, push, or production
  claim; and
- no claim that deterministic heartbeat is durable across process restart or
  that fake/local adapter evidence proves provider behavior.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MAO-OA-T2 accepted closure | material commit `042abf44b`; `docs/reviews/CVF_MAO_OA_T2_COMPLETION_REVIEW_2026-07-16.md`; `Status: REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR` | accepted durable-store owner and replay contract exist before launcher wiring | ACCEPT |
| Operator checkpoint | direct operator continuation instruction on 2026-07-17 | explicit checkpoint required by active next move | ACCEPT |
| Clean base | `git status --short --untracked-files=all` empty; `git rev-parse --short HEAD` = `adff6895b` | one clean dispatch batch | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-OA-T3 --title "MAO Operational Worker Launcher And Liveness Wiring" --date 2026-07-17 --base adff6895b --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MAO-OA-T2 accepted closure 042abf44b" --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced all scaffold blanks with source-verified T3 authority, exact manifest, tests, closure routing, and bounded runtime claims |
| checkerReadAheadConfirmation | dispatch-quality, structural, ADIF, handoff, operation-trace, delta-claim, worker-return, registry, file-size, and public-export checker sources/read models reviewed |
| docOnlyNewFields | launcher names are declared under New Doc-Only Fields; no proposed symbol is presented as current source |
| claimBoundary | dispatch provenance only; no implementation or runtime proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`, surfaceSelector=`MAO`.

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-implementation --surface-selector MAO --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | no additional ADIF-specific worker control; all canonical no-commit and checker controls remain binding |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 roadmap scope is launcher, heartbeat, timeout, cancellation, and provider-neutral adapter wiring | LITERAL_INVARIANT | `docs/roadmaps/CVF_MAO_OPERATIONAL_ADOPTION_AND_AGENT_EXECUTION_ASSURANCE_ROADMAP_2026-07-16.md` | Work Plan And Dependencies T3 row | `MAO-OA-T3` | roadmap tranche table | ACCEPT |
| T2 dependency is accepted and T3 is the next operator-gated tranche | VALUE_SET | `docs/reviews/CVF_MAO_OA_T2_COMPLETION_REVIEW_2026-07-16.md` | Disposition; Next Allowed Move | `REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR` | T2 completion review | ACCEPT |
| durable run creation, replay, and append are existing owners | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 98-203 | `MaoFileRunStore`; `createRun`; `resumeRun`; `appendEvent` | `MaoFileRunStore` | ACCEPT |
| durable append replays through the canonical ledger and writes atomically | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/durable.run.store.ts` | lines 165-203 | `appendEvent` | `MaoFileRunStore` | ACCEPT |
| provider-neutral fake/local invocation and idempotent receipt replay exist | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | lines 149-268 | `MaoDelegationAdapter`; `invoke` | `MaoDelegationAdapter` | ACCEPT |
| adapter rejects authority, admission, role, capability, manifest, and idempotency conflicts before success | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/delegation.adapter.contract.ts` | lines 168-257 | `invoke` | `MaoDelegationAdapter` | ACCEPT |
| deterministic heartbeat, timeout, cancellation, retry, orphan, and duplicate controls exist | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/lifecycle.controller.contract.ts` | lines 240-329 | `MaoLifecycleController` | `MaoLifecycleController` | ACCEPT |
| heartbeat is liveness-only and cannot renew authority or budget | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Idempotency, Retry, Cancel, And Recovery | `Heartbeat proves liveness only` | canonical MAO contract | ACCEPT |
| canonical lifecycle moves planned to admitted to running and then terminal | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Task Lifecycle State Transition Table | `planned`; `admitted`; `running`; `succeeded`; `cancelled`; `timed_out`; `failed` | canonical MAO contract | ACCEPT |
| durable event types include admission, invocation, cancellation, and timeout milestones | VALUE_SET | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | lines 41-52 | `MaoEventType` | `MaoEventType` | ACCEPT |
| durable transition and duplicate checks are owned by the event ledger | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | lines 182-243 | `append` | `MaoEventLedger` | ACCEPT |
| provider policy remains `ProviderRouterContract.route()` ownership and must not be duplicated | LITERAL_INVARIANT | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Provider-Neutral Capability Port | `ProviderRouterContract.route` | canonical MAO contract | ACCEPT |
| execution-plane MAO local barrel is the extension point | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts` | current export list | `export *` | MAO local barrel | ACCEPT |

## New Doc-Only Fields

These are proposed T3 source symbols and are not claimed to exist before worker
implementation.

| Proposed symbol | Intended role | Disposition |
|---|---|---|
| `MaoOperationalWorkerLauncher` | one composition owner for durable milestones plus existing adapter/lifecycle calls | DOC_ONLY_NEW |
| `MaoOperationalLaunchRequest` | explicit graph/task/admission/capability/manifest/idempotency/timeout input | DOC_ONLY_NEW |
| `MaoOperationalLaunchResult` | typed success or fail-closed result with durable and invocation evidence | DOC_ONLY_NEW |
| `launch` | resume durable graph, enforce cancellation/duplicate boundary, call existing adapter, and persist admitted/running/terminal milestones | DOC_ONLY_NEW |
| `heartbeat` | liveness-only call through existing lifecycle controller | DOC_ONLY_NEW |
| `recordTimeout` | deterministic timeout check plus durable `TIMEOUT_DETECTED` milestone when elapsed | DOC_ONLY_NEW |
| `requestCancellation`; `acceptCancellation` | cooperative idempotent cancellation; acceptance persists the terminal cancel milestone | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| planned packet and implementation paths | six `Test-Path` checks returned `False` before authoring | ACCEPT |
| proposed launcher symbols | `rg -n "MaoOperationalWorkerLauncher|operational.worker.launcher"` over execution source/tests and governed packet roots returned no current owner | ACCEPT |
| existing T3 references | search found only roadmap/audit T3 authority and parked-boundary references | ACCEPT_NO_COLLISION |
| owner collision decision | reuse existing adapter, lifecycle, store, ledger, graph, and barrel; add exactly one composition owner | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION_WITH_FRESH_SOURCE_CHECK

priorVerificationArtifact: `docs/reviews/CVF_MAO_OA_T2_COMPLETION_REVIEW_2026-07-16.md`

priorVerificationAnchor: material commit `042abf44b`

freshRecomputeRequired: worker must re-read current source and rerun focused/package checks from execution base

unicodePathHandling: ASCII-authored packet; use literal repository paths and UTF-8-safe readers

extractedTextAuthority: current source and canonical contracts control; prior review is dependency evidence only

## Design Control Gate

The design is additive composition. It does not change any existing contract
enum or transition table. The launcher must surface typed failures for durable
or adapter rejection, must not infer success from silence, and must not turn a
heartbeat into authority, budget, progress, or durable-restart evidence.

## Dual Agent Surface Matrix

| Consumer class | Owner surface | Boundary | Disposition |
|---|---|---|---|
| `INTERNAL_AGENT` | proposed execution-plane operational launcher | local deterministic fake-adapter orchestration and filesystem-backed milestones only | `BOUNDED_INTERNAL_RUNTIME_COMPONENT` |
| `EXTERNAL_AGENT_CLI_MCP` | no adapter owner | no ingress, authentication, remote invocation, or public behavior | `N/A_WITH_REASON` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired T3 work order | `Status: CLOSED_PASS_BOUNDED_WITH_REVIEWER_REPAIR` | PASS |
| Completion or reviewer artifact | T3 completion review | `Status: REVIEWER_ACCEPTED_BOUNDED_WITH_REPAIR` | PASS |
| Roadmap state | governing MAO-OA roadmap | `Status: MAO_OA_T3_PASS_BOUNDED_OPERATOR_CHECKPOINT_NEXT` | PASS |
| Registry JSON | T3 source entry and generated aggregate | generator check and zero coverage violations | PASS |
| Registry Markdown | GC-051 JSON source and aggregate; no separate Markdown owner | generator and coverage checks | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | none | N/A with reason |
| System loop interlock | N/A with reason: no repository governance loop or launcher process is changed | none | N/A with reason |
| Session continuity | protected active state, front door, and handoff | separate session-sync commit follows material closure | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Required evidence | Dispatch state |
|---|---|---|
| launcher contract behavior | 22/22 focused fake/local temp-directory tests | PASS |
| provider acceptance | N/A with reason: real provider invocation forbidden | N/A_WITH_REASON |
| reviewer acceptance | independent completion review | PASS |
| public acceptance | N/A with reason: public action forbidden | N/A_WITH_REASON |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; ADIF Defect Registry Disclosure; Source Verification Block; New Doc-Only Fields; Machine Closure Package; Acceptance Receipt Assertion Matrix; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm source-backed T3 release and exact packet shape before dispatch commit |
| claimBoundary | checker conformance does not prove implementation, provider behavior, production liveness, or user value |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch. No public artifact,
public-sync action, or public claim is authorized.

## Claim Boundary

This baseline releases one bounded execution-plane composition owner using the
accepted durable store, fake/local provider-neutral adapter, lifecycle
controller, and event ledger. It does not authorize or prove a real provider
call, control-plane provider routing, durable heartbeat across restart,
distributed concurrency, process isolation, CLI/MCP/UI ingress, automatic
review/closure/commit/session mutation, public readiness, production readiness,
scale, shipment, or user value.
