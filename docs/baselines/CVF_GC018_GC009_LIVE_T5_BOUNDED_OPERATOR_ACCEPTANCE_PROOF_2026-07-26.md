# CVF GC-018 Baseline - GC009 Live T5 Bounded Operator Acceptance Proof

Memory class: governed-dispatch-baseline

Status: REVIEWER_ACCEPTED_DISPATCH_READY

Batch ID: GC009-LIVE-T5

Dispatch base head: `4249194c4`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Dispatcher/reviewer/closer: Codex

Worker target: one live-proof worker

## Purpose

Release one bounded private live-proof tranche for the already-composed GC-009
Web production caller. The tranche must prove one real Alibaba ALLOW request,
one fail-closed BLOCK request with no provider key available, durable
`MANDATORY_GATEWAY_EVALUATED` evidence, operator readout projection, and
secret-safe route/provider latency evidence.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| GC-009 T1 composition | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T1_RUNTIME_COMPOSITION_COMPLETION_2026-07-26.md`; material commit `29e7d6956` | live proof may exercise the accepted caller without runtime mutation | PASS |
| GC-009 T2 invocation proof | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T2_DETERMINISTIC_INVOCATION_PROOF_COMPLETION_2026-07-26.md`; material commit `2e4412c88` | focused live test must preserve the real gateway/engine path | PASS |
| GC-009 T3 projection | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T3_EXISTING_AUDIT_READOUT_PROJECTION_COMPLETION_2026-07-26.md`; material commit `76fcd6b0e` | live durable events may be projected through the accepted component | PASS |
| GC-009 T4 assessment | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T4_VALUE_LATENCY_FAILURE_ROLLBACK_ASSESSMENT_COMPLETION_2026-07-26.md`; material commit `cb1f34cee` | replace only the unmeasured live-value boundary with bounded evidence | PASS |
| Operator authorization | operator accepted the proposed `GC009-LIVE-T5` one-provider, three-call-ceiling tranche on 2026-07-26 | release exact proof scope only | PASS |
| Live key continuity | key names exist in the gitignored cvf-web environment file; values were not read into governed evidence or printed | worker must verify presence without exposing values | PASS |

## Scope / Target / Owner Boundary

Worker-owned create-only paths:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx`;
2. `docs/audits/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_2026-07-26.md`;
3. `docs/reviews/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_WORKER_RETURN_2026-07-26.md`.

The focused test may import current runtime and UI owners but may not modify
them. Runtime source, existing tests, provider adapters, package metadata,
lockfiles, environment files, governance checkers, session state, public-sync,
deployment, and GC-010 are forbidden.

Live-call ceiling: one provider call in the initial focused run. At most one
rerun is permitted only after a recorded diagnostic and a concrete
result-changing action. Therefore the packet ceiling is two provider calls,
below the operator-authorized maximum of three.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Execute route invokes the mandatory gateway before provider execution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 577-586 and 777 | `runExecuteRouteMandatoryGateway`; `executeAI` | execute route `POST` | ACCEPT |
| Gateway writes one durable event and links its ID | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 49-69 | `evaluateRouteMandatoryGateway` | route gateway adapter | ACCEPT |
| Fail-closed result returns before provider routing | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 82-131 | `isRouteMandatoryGatewayFailClosed`; `runExecuteRouteMandatoryGateway` | route gateway adapter | ACCEPT |
| Durable audit store supports an isolated path and readback | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 96-107 and 140-166 | `CVF_CONTROL_PLANE_EVENTS_PATH`; `appendAuditEvent`; `readAuditEvents` | control-plane event store | ACCEPT |
| Successful receipt exposes secret-safe provider and route latency | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` | lines 133-163 | `providerLatencyMs`; `routeElapsedMs`; `runtimeTelemetry` | final execute response builder | ACCEPT |
| Current live-test pattern resolves an Alibaba key and skips safely when absent | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.rte1-runtime-telemetry.alibaba.live.test.ts` | lines 35-43 and 72-130 | `resolveAlibabaApiKey`; `describe.skipIf`; `runtimeTelemetry` | existing focused live test | ACCEPT |
| Audit page reads durable events and supplies them to the accepted component | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/admin/audit-log/page.tsx` | lines 1-28 | `readAuditEvents`; `AdminAuditLogBody` | admin audit page | ACCEPT |
| T4 left production latency unmeasured | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T4_VALUE_LATENCY_FAILURE_ROLLBACK_ASSESSMENT_COMPLETION_2026-07-26.md` | Findings / Position; Latency Assessment | `NOT_MEASURED_NO_LIVE_AUTHORITY` | T4 completion review | ACCEPT |

## Current Runtime Freshness Verification

At dispatch base `4249194c4`, direct source inspection confirms that the route
still calls the mandatory gateway before `executeAI`, the gateway still writes
the linked event, the fail-closed response still returns before provider
routing, and the final response still exposes secret-safe latency telemetry.
The worker must repeat the cited searches at its captured execution base and
return `BLOCKED_WITH_REASON` on any contradiction.

## New Doc-Only Fields

| Proposed item | Meaning | Disposition |
|---|---|---|
| `liveCallCount` | count of real provider calls consumed by this packet | DOC_ONLY_NEW |
| `blockRequestCount` | count of fail-closed requests that must not reach a provider | DOC_ONLY_NEW |
| `providerLatencyMsObserved` | single-call receipt observation, not a percentile | DOC_ONLY_NEW |
| `routeElapsedMsObserved` | single-call route receipt observation, not production SLO evidence | DOC_ONLY_NEW |
| `diagnosticDisposition` | secret-safe first-failure handling and rerun decision | DOC_ONLY_NEW |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | live-proof worker invoking the current cvf-web test surface | may create one focused test and two evidence documents only | this baseline and companion work order | real Alibaba adapter is consumed but not modified | `LIVE_PROOF_BOUNDED` |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI or MCP consumer participates | no command ingress, external-agent launch, or adapter claim | explicit forbidden scope | unchanged and uninvoked | `DEFERRED_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-provider-live`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class runtime-provider-live --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 0 |
| Disclosed defectIds | none |
| Dispatch impact | the packet still applies live diagnostic, no-blind-rerun, secret hygiene, exact manifest, and no-commit controls |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id GC009-LIVE-T5 --title "GC009 Bounded Live Operator Acceptance Proof" --date 2026-07-26 --base 4249194c4 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "T4 completion cb1f34cee" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source facts, proof design, live-call ceiling, artifact manifest, diagnostics, and claim boundaries |
| checkerReadAheadConfirmation | dispatch-quality, prompt-envelope, handoff, structural, trace, worker-return, machine-closure, and Delta checker sources read |
| docOnlyNewFields | live-call, block-request, latency-observation, and diagnostic fields |
| claimBoundary | scaffold use proves packet provenance only |

## Decision / Baseline / Proposed Tranche

Decision: release exactly one focused private live proof. This is not the broad
release bundle and is not a release-quality, production-SLO, deployment, or
public claim.

## Evidence / Verification

Evidence must come from the actual route, actual shared gateway and guard
engine, actual control-plane event store, actual Alibaba provider on the ALLOW
request, fail-closed response with provider keys removed for the BLOCK request,
receipt telemetry, and rendering the persisted events through the accepted
audit component.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch-ready status; Source Verification columns; dependency evidence; ADIF query; no-commit route; exact manifests; live diagnostic fields; public disposition |
| gateRunPurpose | confirm the packet shape after source and live-proof-boundary verification; gates are not first discovery |
| claimBoundary | checker compliance does not prove live behavior or production readiness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | GC009-LIVE-T5 dispatch authoring, 2026-07-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, source searches, redacted environment-name check, scaffold helper, patch editing, governance gates |
| Target paths | this baseline; companion work order; companion roadmap |
| Allowed scope source | operator accepted the bounded live-proof recommendation |
| Before status evidence | clean HEAD `4249194c4` |
| After status evidence | exact three-path dispatcher packet pending commit |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | packet authoring and dispatch for one bounded live proof |
| Claim boundary | no live call occurs during packet authoring |
| Agent type | Codex |
| Invocation ID | `gc009-live-t5-dispatch-2026-07-26` |
| Expected manifest | this baseline; companion work order; companion roadmap |
| Actual changed set | must match expected manifest |
| Manifest delta | MATCH expected |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | dispatch authorization for one focused live provider proof |
| claimDisposition | CLAIM_REJECTED: packet authoring itself does not prove runtime execution |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: worker receipt evidence is pending |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no provider call in this authoring batch |
| invocationBoundary | future worker invokes only the focused test command |
| interceptionBoundary | no arbitrary process or external-agent interception |
| claimLanguage | dispatch-ready live-proof packet only |
| forbiddenExpansion | no runtime mutation, broad release bundle, public-sync, deployment, CLI/MCP, GC-010, or production-readiness claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance live-proof packet; no public-sync authority.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current runtime and provider proof route |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py`; live governance and diagnostic controls in `AGENTS.md` |
| Owner surface | current cvf-web route, receipt, event store, and audit projection |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external knowledge is absorbed |
| Claim boundary | provider execution evidence is runtime input, not external documentation authority |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: REVIEWER_ACCEPTED_DISPATCH_READY` | PASS |
| Work order status | companion work order | same dispatch-ready status | PASS |
| Completion review | reserved reviewer-owned path | pending worker execution | N/A with reason: dispatch stage |
| Roadmap state | companion roadmap | T5 dispatch-ready marker | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | N/A with reason | N/A with reason |

## Claim Boundary

This baseline authorizes a focused private proof using at most two real
provider calls under the diagnostic rule. It does not authorize runtime
mutation, broad release proof, production latency percentiles, public export,
push, deployment, rollback, GC-010 work, or arbitrary external-agent action.
