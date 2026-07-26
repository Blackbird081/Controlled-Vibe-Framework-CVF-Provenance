# CVF GC009 Live T5 Bounded Operator Acceptance Proof

Memory class: FULL_RECORD

docType: review

Status: BLOCKED_WITH_REASON

Date: 2026-07-26

Batch ID: GC009-LIVE-T5

executionBaseHead: `f8b5a66b0`

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_2026-07-26.md`

## Purpose

Create and execute one focused live test proving the accepted GC-009 Web
caller on the actual route: real Alibaba ALLOW, fail-closed BLOCK before
provider execution, durable secret-safe gateway events, receipt correlation,
single-call telemetry, and projection of the persisted events through the
existing admin audit component. Both permitted focused runs failed before
reaching the provider boundary due to a self-inflicted test-authoring defect;
this audit records that finding and the bounded blocked disposition.

## Target / Source

| Surface | Path |
|---|---|
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_2026-07-26.md` |
| Focused live test | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx` |
| Execute route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` |
| Gateway adapter | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` |
| Control-plane event store | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` |
| Final response builder | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-final-response.ts` |
| Safety filter (root cause) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts` |
| Admin audit component | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/admin/AdminAuditLogBody.tsx` |
| Live diagnostic standard | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` |
| T4 latency boundary | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T4_VALUE_LATENCY_FAILURE_ROLLBACK_ASSESSMENT_COMPLETION_2026-07-26.md` |

## Scope / Methodology

At `executionBaseHead` `f8b5a66b0`, with an empty `git status --short` before
this worker began, confirmed all three worker-owned output paths were absent
(`ls` of the focused-test directory, `docs/audits/`, and `docs/reviews/`
showed no `GC009_LIVE_T5`/`gc009-live-t5` matches). Verified at least one
accepted Alibaba key alias (`ALIBABA_API_KEY`, `DASHSCOPE_API_KEY`) is
present in `.env.local` using a presence-only grep that never printed a
value. Ran `python governance/compat/run_agent_autorun_workflow_gate.py
--phase pre-implementation --base f8b5a66b0 --head HEAD`: PASS. Re-verified
the Source Verification Block's cited line numbers against current source:
`route.ts` still calls `runExecuteRouteMandatoryGateway` at line 577 and
`executeAI` at line 777, confirming no drift from the work order's
Current Runtime Freshness Verification.

Authored the single focused live test at the exact worker-owned path,
combining three accepted current patterns: the ALLOW-path real-Alibaba
telemetry assertions from
`route.rte1-runtime-telemetry.alibaba.live.test.ts`, the keyless
authority-gate BLOCK assertions and gateway-event-payload-key assertions from
`route.mandatory-gateway-invocation.test.ts`, and the RTL render assertions
from `AdminAuditLogBody.test.tsx`. Mocked only `evaluateEnforcement`,
`verifySessionCookie`, `checkTeamQuota`, and `@/lib/i18n`'s `useLanguage`
(UI-language selection only, not gateway/guard/provider behavior). Isolated
the control-plane event store via a temporary
`CVF_CONTROL_PLANE_EVENTS_PATH` created and removed per test run. Did not
mock the shared mandatory gateway, guard engine, route-gateway adapter,
event store, final response builder, or Alibaba provider adapter.

### Initial Focused Live Run (Run 1 Of 2)

Command:

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm exec vitest -- run src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx --reporter=verbose
Set-Location ../../../..
```

Result: FAIL. `TypeError: Cannot read properties of undefined (reading
'runtimeTelemetry')` at the assertion line that reads
`allowReceipt.runtimeTelemetry`, because `allowData.governanceEvidenceReceipt`
itself was `undefined`. This is a test-code defect (an unguarded property
read on a response shape the test had not yet verified), not by itself proof
of a provider-stage failure; the exact response shape was unknown at this
point.

Per `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`'s
mandatory rule ("Any live run that fails ... must record a safe diagnostic
object ... before rerunning the same live test"), a diagnostic capture was
added to the test (logging only `httpStatus`, `Object.keys(allowData)`,
`success`, `error` string, and `model` -- no raw key, prompt, output, or
signed header) before any rerun, per the Live Run Diagnostic And Rerun Rule's
concrete-result-changing-action requirement.

### Diagnostic Rerun (Run 2 Of 2, Permitted)

Command: identical to Run 1, rerun once after adding the diagnostic capture
line (the sole permitted rerun; the added logging is a diagnostic capture,
not a behavior or fixture change to the ALLOW/BLOCK requests themselves).

Result: FAIL. The diagnostic captured:

```json
{
  "stage": "request_validation_or_pre_provider",
  "httpStatus": 400,
  "responseKeys": ["success", "error", "details", "provider", "model"],
  "success": false,
  "error": "Safety filter triggered",
  "model": "blocked"
}
```

`httpStatus: 400`, `model: "blocked"`, and `error: "Safety filter triggered"`
place the failure inside `applySafetyFilters` (`safety.ts`), which the route
calls at line 324, well before the mandatory gateway (line 577) or the
Alibaba provider call (line 777). Root-cause source read of `safety.ts`
confirms the exact trigger: the `PII_PATTERNS` regex
`/\bsecret\b|\bapi[_-]?key\b/i` (line 12) matches the literal word "secret"
inside the test's own ALLOW-request `inputs.options` field ("3. Verify no
raw secret leakage"), independently reproduced by evaluating the same regex
against the five input-field strings used in the test
(`node -e "..."`, disposition: MATCH). This is a self-inflicted test-authoring
defect in the focused test's own fixture content, not a provider, gateway,
guard-engine, or runtime-source defect.

## Live Run Diagnostic

| Field | Value |
|---|---|
| `stage` | `request_validation` |
| `class` | `policy_blocked` |
| `retryable` | `false` (retrying the identical request without editing the fixture content would reproduce the same block deterministically) |
| `userAction` | `revise_request` |
| `provider` | not reached; no provider lane was selected before the safety filter blocked the request |
| `model` | `blocked` (the route's own literal model value for a safety-filter block, not an Alibaba model) |
| `httpStatus` | `400` |
| `latencyMs` | not captured; the request never reached a stage this packet's telemetry (`runtimeTelemetry`) instruments |
| `receiptId` | none; no `governanceEvidenceReceipt` was constructed on this path |
| `traceId` | none; no envelope reached the return path |
| `safeMessage` | The focused test's own ALLOW-request `inputs.options` fixture text contained the literal word "secret", which the existing pre-gateway safety filter (`applySafetyFilters`, `safety.ts` line 12, `PII_PATTERNS`) correctly flagged and blocked before the mandatory gateway or any provider routing occurred. No key, prompt content beyond the single matched word, provider output, or signed header is disclosed by this diagnostic. |

## Findings / Position

Both permitted focused live runs failed at the `request_validation` stage,
before the mandatory gateway (`route.ts` line 577) or the Alibaba provider
call (`route.ts` line 777) were ever reached. The root cause is fully
source-verified and reproducible without any further live call: the focused
test's own ALLOW-request fixture text contains the word "secret", which
trips the existing `PII_PATTERNS` safety-filter regex
(`/\bsecret\b|\bapi[_-]?key\b/i`) that the route correctly applies before
routing to any provider. This is not a defect in the mandatory gateway,
guard engine, route-guard-gateway adapter, control-plane event store, final
response builder, Alibaba provider adapter, or the accepted T1-T4 GC-009
chain; it is a defect in this tranche's own test-fixture prose, introduced
while authoring the focused test.

`liveCallCount` for this tranche is **zero**. Neither focused run reached
the provider boundary, so zero real Alibaba API calls were made and zero
provider cost was incurred. `blockRequestCount` is also zero in the proof
sense required by the work order (a `authority_gate`-blocked keyless
request was never attempted, because the ALLOW request that must precede it
in the single test case never passed to let the test reach the BLOCK
section). The safety-filter 400 in both runs is a different code path
(`applySafetyFilters`) from the packet's required proof target (the
mandatory-gateway `authority_gate` BLOCK), and must not be conflated with it.

Per the work order's Live Run Diagnostic And Rerun Rule ("Never perform a
third focused live run") and Return-To-Orchestrator Conditions ("second
focused-run failure ... requires new operator authorization"), this tranche
stops here. A third focused live run, even with the one-word fixture defect
corrected, is explicitly forbidden by this packet's own ceiling and requires
a fresh operator-authorized dispatch, not a self-authorized continuation.

## denominators

- `liveCallCount`: 0 (zero real Alibaba provider calls occurred across both
  permitted runs)
- `blockRequestCount`: 0 (the keyless authority-gate BLOCK request was never
  reached in either run because the test aborts on the ALLOW-side assertion
  failure first)
- test-case denominator: 1 focused test case, 1 `it(...)` block, run twice
  (initial run plus one diagnostic rerun), both FAIL
- event-model denominator: 0 `MANDATORY_GATEWAY_EVALUATED` events were
  produced by either run, because the safety filter short-circuits before
  the gateway is ever invoked

n=1 statement: this tranche did not complete a single successful live
observation. No `providerLatencyMsObserved`, `routeElapsedMsObserved`, p50,
p95, p99, throughput, or any other performance or SLO inference is made or
inferrable from either failed run; both runs are pre-provider validation
failures with `httpStatus: 400`, not provider-stage results.

## Risk / Corrective Action

| Residual risk | Corrective action |
|---|---|
| The focused test at its current worker-owned path contains an unrepaired fixture defect (the word "secret" in `inputs.options`) that will reproduce this exact block on any future run without a source edit | do not rerun this test as-is; a future authorized tranche must revise the ALLOW-request fixture text to avoid `INJECTION_PATTERNS`/`PII_PATTERNS` matches (for example rephrase "Verify no raw secret leakage" to avoid the standalone word "secret") before any further live attempt |
| This tranche consumed its full two-run ceiling without ever exercising the mandatory gateway, guard engine, event store, or Alibaba provider adapter | the GC-009 T1-T4 accepted evidence (mocked-provider-seam local proof) remains the current bounded acceptance evidence; this tranche neither confirms nor weakens it, because it never reached that code path |
| A future worker could misread "zero live calls, test file exists" as partial live proof | this audit explicitly records `liveCallCount: 0` and a `BLOCKED_WITH_REASON` disposition to prevent that misreading |
| The focused test file remains on disk, untracked, at the exact worker-owned path with the unrepaired defect | left in place per this work order's no-commit, no-forbidden-edit scope; the reviewer decides whether to retain it as-is for reviewer inspection, request a corrected redispatch, or discard it |

## Denominator Clarity

| Denominator | Value | Basis |
|---|---|---|
| `liveCallCount` (real Alibaba provider calls) | 0 | neither run reached `route.ts` line 777 (`executeAI`); both were blocked at the pre-gateway safety filter, `httpStatus: 400`, `model: "blocked"` |
| `blockRequestCount` (keyless authority-gate BLOCK proof requests) | 0 | the BLOCK section of the single test case is unreachable after the ALLOW-side assertion throws; the packet's required `authority_gate` proof was never attempted |
| focused test cases run | 1 test case, executed 2 times (initial run, one diagnostic rerun) | both FAIL at `request_validation` |
| `MANDATORY_GATEWAY_EVALUATED` durable events produced | 0 | the mandatory gateway (`route-guard-gateway.ts`) was never invoked in either run |
| secret hygiene | no raw key, signed header, full prompt, or provider body appears in this audit, the test file, or console output; only the single matched word "secret" (already present in the test's own non-secret fixture prose) is named as the root cause | source-verified against `safety.ts`'s regex and this audit's own diagnostic capture |

## Secret Hygiene Statement

No Alibaba/DashScope API key value, signed header, bearer token, or raw
provider request/response body was printed, copied, hashed, embedded, or
committed at any point in this tranche. The presence check for
`ALIBABA_API_KEY`/`DASHSCOPE_API_KEY` used a boolean grep against
`.env.local` that never captured or displayed the value. The diagnostic
capture added during the permitted rerun logs only `httpStatus`,
`Object.keys(allowData)`, `success` (boolean), the `error` string
(`"Safety filter triggered"`, itself secret-free), and `model`
(`"blocked"`). The safety-filter root cause is disclosed only as "the
literal word 'secret' appears in the test's own fixture text," never as a
credential value, because the matched word originates from the test
author's own non-secret prose, not from any environment variable or
provider payload.

## Terminal Evidence Verdict

`LIVE_ACCEPTANCE_BLOCKED_WITH_DIAGNOSTIC`

Both permitted focused runs failed at the `request_validation` stage due to
a self-inflicted test-fixture defect (the word "secret" inside the ALLOW
request's own `inputs.options` field triggering the pre-gateway
`PII_PATTERNS` safety filter). Zero real Alibaba provider calls occurred.
The mandatory-gateway ALLOW, fail-closed BLOCK, durable-event correlation,
and admin-projection proofs required by this work order were not obtained.
The two-run ceiling is exhausted; a third focused live run is forbidden by
this packet. A corrected redispatch requires fresh operator/reviewer
authorization, not worker self-continuation.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Route invokes gateway before provider | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 577 (`runExecuteRouteMandatoryGateway`); line 777 (`executeAI`) | `runExecuteRouteMandatoryGateway`; `executeAI` | execute route `POST` | ACCEPT (re-verified fresh, unchanged from dispatch-base freshness statement) |
| Safety filter runs before the mandatory gateway | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 324 (`applySafetyFilters(saf1Result.sanitized)`) | `applySafetyFilters` | execute route `POST` | ACCEPT |
| Safety filter blocks on the literal word "secret" | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts` | line 12 (`PII_PATTERNS`); line 31 (`blocked: true, reason: 'Safety filter triggered'`) | `applySafetyFilters`; `PII_PATTERNS` | safety filter module | ACCEPT |
| Focused-test ALLOW fixture contains the word "secret" | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx` | `inputs.options` field, "Verify no raw secret leakage" | `inputs` | this tranche's own focused live test | ACCEPT |
| T4 records latency as unmeasured | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T4_VALUE_LATENCY_FAILURE_ROLLBACK_ASSESSMENT_COMPLETION_2026-07-26.md` | Latency Decision | `NOT_MEASURED_NO_LIVE_AUTHORITY` | T4 completion review | ACCEPT (unchanged; this tranche adds no new latency evidence) |

## New Doc-Only Fields

| Proposed item | Meaning | Runtime/source status |
|---|---|---|
| `liveCallCount` | 0 (recorded this tranche) | DOC_ONLY_NEW |
| `blockRequestCount` | 0 (recorded this tranche) | DOC_ONLY_NEW |
| `providerLatencyMsObserved` | not obtained; no provider call occurred | DOC_ONLY_NEW |
| `routeElapsedMsObserved` | not obtained; no provider call occurred | DOC_ONLY_NEW |
| `diagnosticDisposition` | `BLOCKED_AFTER_ONE_DIAGNOSTIC_RERUN_SELF_INFLICTED_FIXTURE_DEFECT` | DOC_ONLY_NEW |

## Epistemic Process Block

- Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION
- Expected result / prediction: given the accepted T1-T4 GC-009 chain and a
  correctly authored focused test following the existing RTE1/T2 patterns,
  the initial live run was expected to reach the Alibaba provider boundary
  and return a real ALLOW result.
- Evidence Comparison: the prediction was not confirmed. Both runs failed
  before the mandatory gateway or provider boundary, at the pre-existing
  `applySafetyFilters` stage, due to a word choice in this tranche's own
  test fixture, not a runtime or provider defect.
- Contradiction or gap disposition: no contradiction was found in the
  accepted T1-T4 evidence, the mandatory gateway, or the Alibaba provider
  adapter; the gap is entirely contained in this tranche's own new test
  file's fixture prose, source-verified by direct regex reproduction
  against the exact input strings used.
- Claim update: this tranche does not extend, weaken, or contradict the
  accepted GC-009 T1-T4 chain. It records `LIVE_ACCEPTANCE_BLOCKED_WITH_DIAGNOSTIC`
  and `liveCallCount: 0`, and identifies the exact one-word fixture defect a
  future authorized redispatch must correct before attempting the live
  proof again.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | review structural heading families (target/source, scope/methodology, findings/position, risk/corrective action, decision/disposition); Delta block Field/Disposition table shape; Machine Closure Package required column set; equivalence-claim trigger words paired with adjacent evidence commands or disposition tokens; ASCII prose discipline; `BLOCKED_WITH_REASON` status token spelling |
| gateRunPurpose | confirm this audit's required shape and literal-format compliance before the worker-return fast gate runs; gates are confirmation evidence, not first discovery |
| claimBoundary | checker compliance is gate-shape evidence only; it does not substitute for the missing live provider call this audit explicitly records as not obtained |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance live-proof attempt only; no public-sync
authorization exists, and this artifact records a blocked (not passed)
proof attempt.

## Claim Boundary

This audit records exactly one focused live test authored and two permitted
focused live runs executed, both of which failed at the `request_validation`
stage before reaching the mandatory gateway or the Alibaba provider. It does
not claim a real Alibaba ALLOW result, a fail-closed authority-gate BLOCK
proof, durable event correlation, admin-component projection, or any
latency observation. `liveCallCount` is 0. It does not authorize a third
focused live run, runtime mutation, broad release proof, production
percentile or SLO claims, public export, push, deployment, rollback,
GC-010 work, or any claim beyond identifying the exact self-inflicted
fixture defect that caused both runs to fail before the provider boundary.
