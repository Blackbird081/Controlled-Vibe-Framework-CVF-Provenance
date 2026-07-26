# CVF Agent Work Order - GC009 Live T5 Bounded Operator Acceptance Proof

Memory class: governed-worker-dispatch

Status: REVIEWER_ACCEPTED_BLOCKED_WITH_DIAGNOSTIC_R1_AUTHORIZED

Batch ID: GC009-LIVE-T5

Dispatch base head: `4249194c4`

dispatchBaseHead: `4249194c4`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AFTER_WORKER_RETURN

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: one live-proof worker

Reviewer/closer: Codex

Worker return path: `docs/reviews/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_WORKER_RETURN_2026-07-26.md`

## Dispatch Prompt Envelope

Role: live-proof worker for `GC009-LIVE-T5`.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_2026-07-26.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture current committed HEAD before any edit.

Current-time notes: GC-009 T1-T4 are independently closed. GC-010 is
value-parked and is not part of this packet. Operator authorization releases
one focused private Alibaba proof with a maximum of two real provider calls.

Do-not-misread notes: this is not the broad release bundle, production SLO
measurement, provider soak, public proof, deployment, rollback, runtime repair,
or GC-010 work. Do not print or copy any key value.

Required first actions: read startup front doors, guard orientation, literal
gotchas, live diagnostic standard, companion baseline, this complete packet,
T1-T4 completions, all source in the Source Verification Block, and checker
source before editing. Capture HEAD and clean status, then run
pre-implementation.

Return contract: create exactly the three worker-owned artifacts, perform one
initial focused live run, apply the diagnostic rule before any single permitted
rerun, run non-live regressions and gates, leave all changes unstaged and
uncommitted, then return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create and execute one focused live test proving the accepted GC-009 Web
caller on the actual route: real Alibaba ALLOW, fail-closed BLOCK before
provider execution, durable secret-safe gateway events, receipt correlation,
single-call telemetry, and projection of the persisted events through the
existing admin audit component.

## Authority Chain

1. `AGENTS.md`;
2. `CVF_SESSION_MEMORY.md`;
3. active state and handoff;
4. paired production-caller roadmap;
5. T1-T4 completion reviews;
6. companion GC-018 baseline;
7. this work order;
8. current runtime, test, provider, event-store, and audit-component source.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T1 runtime composition | completion at material commit `29e7d6956` | exercise without modifying runtime | PASS |
| T2 deterministic invocation | completion at material commit `2e4412c88` | preserve real gateway/engine and ALLOW/BLOCK semantics | PASS |
| T3 audit projection | completion at material commit `76fcd6b0e` | reuse existing component | PASS |
| T4 bounded assessment | completion at material commit `cb1f34cee` | measure only bounded live observations left unmeasured | PASS |
| Operator live authority | explicit acceptance on 2026-07-26 | one focused initial call and at most one diagnostic rerun | PASS |
| Packet isolation | clean HEAD `4249194c4` before packet authoring | worker starts only from committed dispatch packet and clean worktree | PASS |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | bounded private live proof for the current GC-009 Web caller |
| scopeClassification | focused test plus live evidence; no runtime mutation |
| riskSensitivity | R2 because a real provider key and paid call are used |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | Codex dispatches and reviews; a separate worker executes and returns no-commit |
| escalationCondition | source contradiction, missing credential, concurrent drift, or need outside exact manifest |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | authorizes the bounded provider-call ceiling and owns credentials |
| Dispatcher | source-verifies, gates, commits, and supplies the complete packet |
| Live-proof worker | creates the focused test and evidence; executes within quota; does not commit |
| Reviewer/closer | independently reviews semantics and diagnostics, reruns only safe local checks, closes or rejects, commits, and syncs |

## Scope

Allowed worker actions:

1. Create exactly one focused live test at the owned test path.
2. Reuse current authentication, enforcement, and quota mock patterns only to
   isolate the accepted route proof.
3. Use the actual route `POST`, shared mandatory gateway, guard engine,
   route-gateway adapter, event store, final response builder, Alibaba provider
   adapter, and audit component.
4. Use an isolated temporary `CVF_CONTROL_PLANE_EVENTS_PATH`.
5. Run one real Alibaba ALLOW request using the existing secret loader.
6. Remove all provider-key environment aliases before the BLOCK request and
   prove the response is `guard-blocked`, decision `BLOCK`, blocker
   `authority_gate`, with a linked durable event.
7. Read persisted events and render them through `AdminAuditLogBody`; assert
   both request IDs, both decisions, and the blocker are projected.
8. Record secret-safe receipt, event, request, provider/model, HTTP status,
   `providerLatencyMs`, `routeElapsedMs`, and command duration evidence.
9. Run the exact non-live regression and governance commands.

Forbidden:

- modifying runtime source, existing tests, provider adapters, UI components,
  package metadata, lockfiles, configuration, `.env.local`, governance
  checkers, session state, public-sync, or deployment files;
- mocking the shared mandatory gateway, guard engine, route-gateway adapter,
  event store, final response builder, or Alibaba provider in the ALLOW path;
- printing, copying, hashing, or embedding raw credential values;
- running the broad release bundle, any other live spec, provider soak,
  benchmark loop, or more than one permitted rerun;
- claiming p50, p95, p99, throughput, production SLO, release readiness,
  public readiness, deployment readiness, or GC-010 progress;
- staging, commit, push, public-sync, deployment, or rollback.

## Write Ownership

Worker-owned create-only paths:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx`
2. `docs/audits/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_2026-07-26.md`
3. `docs/reviews/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_WORKER_RETURN_2026-07-26.md`

Everything else is read-only or forbidden to the worker.

## Required First Reads

1. startup front doors and active handoff;
2. `docs/reference/guard_orientation/README.md`;
3. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
4. `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`;
5. companion baseline and this work order;
6. T1, T2, T3, and T4 completion reviews;
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`;
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts`;
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts`;
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts`;
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.rte1-runtime-telemetry.alibaba.live.test.ts`;
12. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.mandatory-gateway-invocation.test.ts`;
13. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/admin/AdminAuditLogBody.tsx`;
14. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/admin/AdminAuditLogBody.test.tsx`;
15. checker sources listed below.

## Pre-Flight Checks

1. Capture `$workerExecutionBaseHead = git rev-parse --short HEAD`.
2. Confirm `git status --short` is empty.
3. Confirm all three worker-owned output paths are absent.
4. Confirm baseline and work order are committed and dispatch-ready.
5. Verify that at least one accepted Alibaba key alias is present without
   printing its value. Absence returns `BLOCKED_WITH_REASON`.
6. Run pre-implementation with the captured execution base before editing.
7. Stop on HEAD drift, concurrent changes, output collision, source
   contradiction, or forbidden-path need.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Route invokes gateway before provider | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 577-586 and 777 | `runExecuteRouteMandatoryGateway`; `executeAI` | execute route `POST` | ACCEPT |
| Gateway persists and links a seven-field event | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 49-69 | `MANDATORY_GATEWAY_EVALUATED`; `gatewayRequestId` | `evaluateRouteMandatoryGateway` | ACCEPT |
| Fail-closed response precedes provider routing | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 82-131 | `isRouteMandatoryGatewayFailClosed` | `runExecuteRouteMandatoryGateway` | ACCEPT |
| Event store supports isolated durable write/read | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 96-107 and 140-166 | `CVF_CONTROL_PLANE_EVENTS_PATH`; `readAuditEvents` | control-plane event store | ACCEPT |
| Final receipt exposes latency telemetry | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | lines 133-163 | `providerLatencyMs`; `routeElapsedMs` | final execute response builder | ACCEPT |
| Current focused live pattern uses real Alibaba and secret-safe telemetry | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.rte1-runtime-telemetry.alibaba.live.test.ts` | lines 35-43 and 72-130 | `resolveAlibabaApiKey`; `runtimeTelemetry` | existing focused live test | ACCEPT |
| Current capability registry declares Alibaba `qwen-turbo` completion support | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | `PROVIDER_CAPABILITY_REGISTRY` Alibaba entry | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| T2 request fixtures reach ALLOW and authority BLOCK | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.mandatory-gateway-invocation.test.ts` | two test cases | `t2-gateway-allow-request`; `delete_governance` | focused route test | ACCEPT |
| Existing component projects decision, request ID, and blocker | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/admin/AdminAuditLogBody.tsx` | lines 41-83 and render call sites | `GatewayDetailsForEvent`; `AdminAuditLogBody` | admin audit component | ACCEPT |
| T4 records latency as unmeasured | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T4_VALUE_LATENCY_FAILURE_ROLLBACK_ASSESSMENT_COMPLETION_2026-07-26.md` | Latency Assessment | `NOT_MEASURED_NO_LIVE_AUTHORITY` | T4 completion review | ACCEPT |

## New Doc-Only Fields

| Proposed item | Meaning | Runtime/source status |
|---|---|---|
| `liveCallCount` | real paid provider-call denominator | DOC_ONLY_NEW |
| `blockRequestCount` | fail-closed non-provider request denominator | DOC_ONLY_NEW |
| `providerLatencyMsObserved` | one receipt observation | DOC_ONLY_NEW |
| `routeElapsedMsObserved` | one receipt observation | DOC_ONLY_NEW |
| `diagnosticDisposition` | first-failure and rerun decision | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

At dispatch base `4249194c4`, current source still places the mandatory gateway
at route lines 577-586 before the provider call at line 777, persists the
seven-field event, exposes latency telemetry, retains the accepted audit
component, and declares Alibaba `qwen-turbo` completion support in
`PROVIDER_CAPABILITY_REGISTRY`. The worker must re-run the cited searches
before editing and must return blocked on any contradiction.

## Focused Test Contract

The single focused test must:

1. use `describe.skipIf` only for verified missing live credentials;
2. isolate the control-plane store in a temporary directory and remove it in
   cleanup;
3. reset rate-limit, shared gateway, and guard-engine state;
4. mock authentication, enforcement, and quota only;
5. execute one ALLOW request through the real Alibaba provider;
6. assert HTTP 200, `success=true`, decision `ALLOW`, provider `alibaba`,
   non-mock output, live receipt, linked audit event ID, and numeric latency;
7. remove all Alibaba/DashScope aliases before the negative request;
8. execute one source-valid `delete_governance` request;
9. assert HTTP 400, model `guard-blocked`, decision `BLOCK`,
   `authority_gate`, and linked audit event ID;
10. read exactly two matching gateway events, validate the seven sorted
    payload keys, and reject key/prompt leakage;
11. render those actual persisted events through `AdminAuditLogBody` and assert
    both decisions, request IDs, and the blocker appear;
12. restore environment and singleton state even on failure.

## Live Run Diagnostic And Rerun Rule

The initial live run consumes one provider call. On PASS, do not rerun it.

On failure, before any rerun record:

| Field | Required evidence |
|---|---|
| `stage` | stable stage from the diagnostic standard |
| `class` | stable failure class |
| `retryable` | true or false |
| `userAction` | stable operator action |
| `provider` | `alibaba` when known |
| `model` | model when known |
| `httpStatus` | status when available |
| `latencyMs` | elapsed time when available |
| `receiptId` | secret-safe ID when available |
| `traceId` | secret-safe ID when available |
| `safeMessage` | no key, raw prompt, raw output, or signed header |

Exactly one rerun is allowed only when the diagnostic identifies a concrete
result-changing action and retry is expected to help. Otherwise return
`BLOCKED_WITH_REASON`. Never perform a third focused live run.

## Required Artifact Manifest

### Focused Live Test

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx`

### Live Proof Audit

`docs/audits/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_2026-07-26.md`

### Worker Return

`docs/reviews/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_WORKER_RETURN_2026-07-26.md`

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| focused test | create, run once live, and retain for reproducible reviewer inspection |
| live proof audit | record call/request denominators, secret-safe IDs, telemetry, diagnostics, and bounded verdict |
| worker return | record exact commands, changed set, gates, no-commit evidence, and terminal disposition |

## Forbidden Path Manifest

All paths outside the three worker-owned paths are read-only. In particular,
do not edit route runtime, adapters, components, existing tests, `.env.local`,
package or lock files, governance, session, roadmap, work order, baseline,
public-sync, or deployment paths.

## Required Proof Manifest

| Proof | Required evidence |
|---|---|
| real ALLOW | one real Alibaba result with live receipt and non-mock output |
| fail-closed BLOCK | provider aliases removed, HTTP 400 `guard-blocked`, authority blocker |
| durable correlation | two event IDs linked to their envelopes and matching request IDs |
| projection | actual persisted events rendered by accepted audit component |
| latency | numeric provider and route observations with n=1 boundary |
| secret hygiene | no raw key, prompt, output, signed header, or provider body in documents |
| denominator clarity | provider calls, block requests, events, and test cases reported separately |
| bounded rerun | zero reruns on PASS; at most one after diagnostic on failure |

## Evidence Requirements

The audit must include:

- `liveCallCount` and `blockRequestCount`;
- test-case and event-model denominators separately;
- request IDs, receipt ID, envelope ID, and gateway audit event IDs;
- HTTP statuses and final decisions;
- `providerLatencyMsObserved` and `routeElapsedMsObserved`;
- explicit n=1 statement forbidding percentile or SLO inference;
- first-run result and any diagnostic/rerun disposition;
- exact command results and no-commit status;
- one terminal evidence verdict:
  `LIVE_ACCEPTANCE_PASS_BOUNDED`,
  `LIVE_ACCEPTANCE_BLOCKED_WITH_DIAGNOSTIC`, or
  `LIVE_ACCEPTANCE_FAIL_BOUNDED`.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Required output |
|---|---|---|
| real production caller value | actual route plus real Alibaba ALLOW | focused test and audit |
| fail-closed boundary | keyless authority BLOCK | focused test and audit |
| durable evidence | isolated store and readback | exact event assertions |
| operator projection | render persisted events through existing component | projection assertions |
| latency boundary | receipt telemetry, n=1 only | audit observations |
| quota control | one initial call and at most one diagnostic rerun | call denominator |
| no expansion | exact three-path worker manifest | worker return |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | live-proof worker using cvf-web focused test | exact three-path write scope and two-call ceiling | packet, test output, receipts, audit | consumes current Alibaba adapter without mutation | `LIVE_PROOF_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no CLI/MCP or external-agent invocation | forbidden path and command manifests | unchanged | `DEFERRED_WITH_REASON` |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Codex dispatcher -> live-proof worker -> Codex reviewer/closer -> Codex session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`4249194c4`; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_MUST_CAPTURE_AFTER_WORKER_RETURN |
| changedSetScope(phase) | dispatch=baseline/work order/roadmap; execution=exact three worker paths; closure=accepted worker paths plus reviewer completion/work-order/roadmap; session-sync=front-door/state/handoff only |
| traceScope(phase, actor) | dispatcher traces packet; worker traces commands, live calls, diagnostics, and changed set; reviewer traces acceptance and closure; steward traces continuity |
| commitOwner(phase) | dispatcher commits packet; worker commits nothing; reviewer/closer commits accepted material; steward commits continuity |
| crossBatchIsolation | worker must start from clean committed packet and stop on concurrent drift |
| nextMoveSurfaces | reviewer/closer updates current roadmap; once material closure is accepted, session-sync steward updates state, front door, and active handoff |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_COMPLETION_2026-07-26.md` |
| reviewerOwnedClosurePaths | completion review; this work order; companion roadmap; accepted worker paths |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Evidence Reuse And Encoding Plan

| Field | Value |
|---|---|
| verificationMode | RECOMPUTE_REQUIRED for live behavior; prior T1-T4 evidence may be cited only for predecessor boundaries |
| evidenceEncoding | ASCII summaries and secret-safe identifiers only |
| Unicode exception | N/A with reason: no user-facing localization text is authored; existing Vietnamese component strings are read-only |
| raw secret handling | environment only; never printed, copied, hashed, or committed |
| prior evidence boundary | prior local mock evidence cannot substitute for this live call |

## Foundation Storage Layout Block

N/A with reason: this packet creates one focused test and two dated execution
artifacts in their established folders. It does not create, split, relocate,
or refactor a stable governance foundation, reference family, index, or front
door.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_WORKER_RETURN_2026-07-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections, written as real headings rather than quoted heading
literals: Purpose; Scope / Methodology; Target / Source; Findings / Position;
Risk / Corrective Action; Live Run Diagnostic; Command Evidence; Checker
Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim
Boundary Control Block; Public Export Disposition; External Knowledge Intake
Routing; Rescan Intelligence Hardening; Corpus Completeness And Report
Integrity; Finding-To-Governance Learning Disposition; Epistemic Process
Block; Machine Closure Package; Claim Boundary; git status --short; Changed
Files; Worker Experience Retrospective; No-Commit Statement.

## Verification Commands

Before editing:

```powershell
$workerExecutionBaseHead = git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $workerExecutionBaseHead --head HEAD
```

Initial focused live run, exactly once:

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm exec vitest -- run src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx --reporter=verbose
Set-Location ../../../..
```

Non-live regressions:

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm exec vitest -- run src/app/api/execute/route.mandatory-gateway-invocation.test.ts src/components/admin/AdminAuditLogBody.test.tsx --reporter=verbose
npm exec tsc -- --noEmit
Set-Location ../../../..
```

Governance and final evidence:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $workerExecutionBaseHead --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git diff --name-status
git status --short
```

Do not run `scripts/run_cvf_release_gate_bundle.py`; its broad live suite would
exceed this packet's call and scope ceiling.

## Acceptance Criteria

- [x] Predecessor closure and operator authority are source-recorded.
- [x] Exact three-path worker manifest is declared.
- [x] Live-call and rerun ceilings are explicit.
- [x] Required real and mocked boundaries are explicit.
- [x] Durable audit and projection proof are required.
- [x] Latency evidence is bounded to single observations.
- [x] Secret-safe diagnostic fields and no-blind-rerun rule are explicit.
- [x] No runtime, public, deployment, GC-010, or release claim is authorized.
- [x] Worker cannot stage or commit.

## Execution Plan

1. Complete startup, source, checker, key-presence, and clean-worktree checks.
2. Create the focused test without editing any existing file.
3. Execute the initial live run once.
4. If it fails, record a diagnostic before deciding whether the single rerun
   is justified.
5. Create the audit and worker return from secret-safe evidence.
6. Run non-live regression, typecheck, governance, size, and diff checks.
7. Leave all three paths unstaged and return the terminal disposition.

## Review Gate

Codex independently verifies mock boundaries, call denominator, receipt and
event correlation, event projection, telemetry semantics, secret hygiene,
diagnostic/rerun discipline, exact changed set, test/regression results, and
no-commit status before accepting any live claim.

## Closure Checklist

- [x] Dispatch packet contains no missing dependency.
- [x] Source facts use current repo paths and symbols.
- [x] Live and non-live denominators are distinct.
- [x] Failure diagnostics precede any rerun.
- [x] Reviewer owns completion and commit.
- [x] Public export remains deferred.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for a missing key, source contradiction, output
collision, HEAD drift, forbidden-path need, provider failure with no justified
rerun, second focused-run failure, secret exposure, or inability to satisfy
the exact proof manifest.

## Operator Checkpoint

No operator checkpoint remains before the initial focused call; it is
explicitly authorized. Any third call, broader live suite, runtime repair,
public action, deployment, rollback, or production claim requires new
operator authorization.

## Worker Autonomy / No-Question Rule

Repair allowed-scope test or document defects directly. Do not ask whether to
fix an allowed-scope checker failure. Stop only for a return condition above.

## Terminal Worker Disposition Enum

Return exactly one:

- `COMPLETE_PENDING_REVIEW`
- `BLOCKED_WITH_REASON`

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-provider-live`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class runtime-provider-live --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 0 |
| Disclosed defectIds | none |
| Dispatch impact | live diagnostics, no-blind-rerun, secret hygiene, exact manifest, and no-commit controls remain mandatory despite an empty resolver result |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status; prompt-envelope fields; Source Verification columns; handoff fields; worker-return full profile; live diagnostic fields; manifests; no-commit evidence; public disposition |
| gateRunPurpose | confirm source-verified dispatch shape after direct checker-source review; gates are confirmation evidence, not first discovery |
| claimBoundary | checker PASS cannot substitute for a real provider call or independent semantic review |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | GC009-LIVE-T5 dispatch, 2026-07-26 |
| Working directory | repository root |
| Command or tool surface | source reads, searches, redacted key-name check, scaffold helper, patch editing, dispatch gates |
| Target paths | companion baseline; this work order; companion roadmap |
| Allowed scope source | operator accepted the bounded live-proof recommendation |
| Before status evidence | clean HEAD `4249194c4` |
| After status evidence | exact three dispatcher-owned packet paths |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | one focused live-proof dispatch; two-call hard ceiling |
| Claim boundary | packet authoring only; no call executed by dispatcher |
| Agent type | Codex |
| Invocation ID | `gc009-live-t5-dispatch-2026-07-26` |
| Expected manifest | baseline; work order; roadmap |
| Actual changed set | must match expected manifest |
| Manifest delta | MATCH expected |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | future focused GC-009 live proof through current cvf-web route |
| claimDisposition | CLAIM_REJECTED: no live action occurs in the dispatch-authoring batch |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker evidence pending |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: worker invocation pending |
| invocationBoundary | one focused Vitest command and at most one diagnostic rerun |
| interceptionBoundary | no CLI/MCP, arbitrary process, external-agent, or provider interception |
| claimLanguage | dispatch authorization only until worker evidence is independently accepted |
| forbiddenExpansion | no runtime mutation, broad release suite, public-sync, deployment, rollback, GC-010, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance proof only; no public-sync authority or artifact.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current runtime and provider proof route |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py`; mandatory live governance and live diagnostic controls in `AGENTS.md` |
| Owner surface | current cvf-web route, receipt, event store, and audit projection |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external knowledge is absorbed |
| Claim boundary | provider execution evidence is runtime input, not external documentation authority |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | `Status: REVIEWER_ACCEPTED_BLOCKED_WITH_DIAGNOSTIC_R1_AUTHORIZED` | PASS |
| Baseline status | companion baseline | same dispatch-ready status | PASS |
| Worker artifacts | exact three-path manifest | blocked diagnostic, zero provider calls | PASS |
| Completion review | reviewer-owned path | independent blocker acceptance and rerun-policy correction | PASS |
| Roadmap state | companion roadmap | T5 blocked, R1 authorized | PASS |
| Public export | this work order | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | ALLOW evidence | BLOCK evidence |
|---|---|---|
| HTTP | 200 | 400 |
| decision | ALLOW | BLOCK |
| provider action | one real Alibaba call | no provider key available; guard-blocked before provider |
| durable event | one linked gateway event | one linked gateway event |
| request correlation | ALLOW request ID | BLOCK request ID |
| projection | decision and request ID rendered | decision, request ID, and `authority_gate` rendered |
| latency | provider and route observations | N/A with reason: no provider call |

## Claim Boundary

This work order authorizes one focused private live proof and at most one
diagnostic rerun. It does not authorize runtime mutation, broad release proof,
production percentile or SLO claims, public export, push, deployment,
rollback, GC-010 work, CLI/MCP invocation, or arbitrary external-agent action.
