# CVF GC009 Live T5 Bounded Operator Acceptance Proof

Memory class: FULL_RECORD

docType: review

Status: BLOCKED_WITH_REASON

Date: 2026-07-26

Batch ID: GC009-LIVE-T5

executionBaseHead (first attempt): `f8b5a66b0`

executionBaseHead (R1): `7825c02e5`

executionBaseHead (R2): `259076d37`

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_2026-07-26.md`

## Purpose

Create and execute one focused live test proving the accepted GC-009 Web
caller on the actual route: real Alibaba ALLOW, fail-closed BLOCK before
provider execution, durable secret-safe gateway events, receipt correlation,
single-call telemetry, and projection of the persisted events through the
existing admin audit component. The first attempt's two permitted focused
runs failed before reaching the provider boundary due to a self-inflicted
test-authoring defect (below, preserved as historical evidence). Codex
independently reviewed that attempt
(`docs/reviews/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_COMPLETION_2026-07-26.md`)
and authorized one R1 redispatch: a corrected fixture, a mandatory offline
safety preflight, and exactly one new focused run with zero reruns under
every outcome. This audit's R1 section below records that corrected run,
which reached the real Alibaba provider but failed on this tranche's own
over-strict test assertion, and closes with `BLOCKED_WITH_REASON` per R1's
no-rerun rule.

## R2 Correction To The R1 Evidence Underclaim (Read This Before The R1 Section Below)

The R1 section below (as originally written) understated what the R1 focused
live run actually proved before it failed on the topic-echo assertion. Per
the operator-authorized R2 redispatch, this correction is recorded here
rather than by rewriting the R1 prose in place, to preserve the original R1
section as historical evidence.

`liveCallCount` for R1 is confirmed as 1, not merely "likely." Before the R1
run's own `expect(allowSerialized).not.toContain(inputs.topic)` assertion
failed (the assertion R2 has since deleted as over-strict), the same test
execution had already passed, in order: `expect(allowResponse.status).toBe(200)`,
`expect(allowData.success).toBe(true)`, `expect(allowData.provider).toBe('alibaba')`,
`expect(allowReceipt.decision).toBe('ALLOW')`, the nonempty-`output` string
checks, `expect(typeof allowTelemetry!.providerLatencyMs).toBe('number')`,
`expect(typeof allowTelemetry!.routeElapsedMs).toBe('number')`, the
`claimBoundary` equality check, and
`expect(allowSerialized).not.toContain(ALIBABA_API_KEY)`, because all of
those assertions execute, in the same order they appear in the test file, on
lines strictly before the line-186 assertion that actually threw. A thrown
`expect(...).not.toContain(...)` assertion failure only halts execution at
its own line; it does not retroactively unprove synchronous assertions on
earlier lines that already returned without throwing.

`blockRequestCount` for R1 remained 0: the BLOCK-request section (test lines
189 onward) is textually after the failing line-186 assertion and was never
reached.

Exact numeric telemetry values (`providerLatencyMs`, `routeElapsedMs`,
`receiptId`, `envelopeId`) were not retained in the R1 documentation, because
the R1 worker's process for extracting safe summary facts from the failure
output used a targeted grep for `Test Files`/`Tests`/`Duration` lines only
and did not separately capture those receipt-telemetry numeric fields before
deleting the raw output file. This is a documentation completeness gap in
how much of the already-passed evidence was extracted and recorded, not a
gap in what the R1 run itself actually executed.

R1's durable-event correlation and admin-projection proof were correctly
recorded as not reached: `readAuditEvents()` (test line 231) and the
`AdminAuditLogBody` render (test line 281 in the pre-R2 file) are both
textually after line 186, so R1 truly never reached them.

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

## First-Attempt Terminal Evidence Verdict (Historical, Superseded By R1 Below)

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

Independently reviewed and accepted (with one correction to the worker's
rerun-compliance claim) at
`docs/reviews/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_COMPLETION_2026-07-26.md`,
material commit `6b6cd6ab1`, disposition
`REVIEWER_ACCEPTED_BLOCKED_WITH_DIAGNOSTIC_R1_AUTHORIZED`. This first-attempt
verdict is retained here as historical evidence and is superseded by the R1
section immediately below for the tranche's current status.

## R1 Redispatch Evidence

### R1 Scope And Authorization

Per the work order's `## R1 Redispatch Override` section (superseding the
initial-dispatch two-run/one-diagnostic-rerun rule), R1 authorized exactly
one corrected focused live run with these mandatory preconditions: (1)
replace only the literal fixture text `Verify no raw secret leakage` with
`Verify no credential value leakage` in the focused test; (2) run an
offline preflight applying current `INJECTION_PATTERNS`/`PII_PATTERNS`
behavior to the complete generated ALLOW intent before any provider use,
requiring `NO_MATCH`; (3) execute exactly one focused live run; (4) zero
reruns under every outcome, including logging, fixture, configuration,
credential, or provider-state changes.

### R1 Fixture Correction

Applied the exact literal replacement in
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx`'s
`inputs.options` field: `Verify no raw secret leakage` ->
`Verify no credential value leakage`. No other line in the focused test was
changed for this correction.

### R1 Offline Safety Preflight (No Provider Call)

Before any provider use, constructed the complete generated ALLOW intent
using the real `getTemplateById`/`generateIntent` functions against the
corrected `inputs` object, and the complete built execution prompt using
the real `buildExecutionPrompt` function (the same function `route.ts` line
274 calls), then ran the real `applySafetyFilters` function (the same
function `route.ts` line 324 calls) against both strings using a disposable
Vitest file created and deleted before any live run, containing no route
invocation, no network call, and no provider credential use.

Result: `NO_MATCH` on both.

```json
{
  "intentBlocked": false,
  "intentDetails": undefined,
  "promptBlocked": false,
  "promptDetails": undefined
}
```

Per R1 step 2, this cleared the corrected fixture for the single permitted
live run. The disposable preflight file was deleted immediately after this
result was captured and before the live run; it is not one of the three
worker-owned paths and was never a live-call attempt.

### R1 Focused Live Run (Exactly One, Zero Reruns)

Command:

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm exec vitest -- run src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx --reporter=verbose
Set-Location ../../../..
```

Result: FAIL after 18.46s total (13.45s inside the test body -- a duration
consistent with a completed real network round trip to the Alibaba API,
not a pre-provider short-circuit).

`AssertionError: expected '{"allowData":...}' not to contain
'GC009 Live T5 bounded operator accept...'` at the assertion
`expect(allowSerialized).not.toContain(inputs.topic)`
(focused test line 186). The immediately preceding assertion at line 185,
`expect(allowSerialized).not.toContain(ALIBABA_API_KEY)`, did not fail,
confirming the key-leak check passed before the topic-echo check failed.
Because the failure is a `not.toContain` assertion on the response body
rather than a thrown route-level or network-level error, and because the
elapsed time (13.45s) is consistent with a real provider round trip rather
than an immediate pre-gateway 400 (both first-attempt runs completed in
under 600ms), the ALLOW request reached HTTP 200 with `success: true` and a
real Alibaba `output` string before this assertion executed.

Root cause: the real Alibaba model's response output naturally referenced
or restated the supplied `inputs.topic` text
("GC009 Live T5 bounded operator acceptance proof") as part of its
analysis, which the test's own `expect(...).not.toContain(inputs.topic)`
assertion (added to prove no *raw secret* leakage) incorrectly also
rejects, because the topic string is ordinary non-secret fixture text that
a real language model is expected to reference when producing an on-topic
analysis. This is a test-assertion design defect in this tranche's own
focused test, not a secret leak, not a provider defect, and not a defect in
the mandatory gateway, guard engine, route-guard-gateway adapter, or
control-plane event store, none of which had executed yet at the point of
failure (the BLOCK-request section, gateway-event assertions, and
`AdminAuditLogBody` projection all appear later in the same test body,
after this failed assertion, and were never reached).

### R1 Secret-Safe Diagnostic

Per R1 step 5 and the live diagnostic standard's mandatory rule, this
diagnostic is recorded immediately on failure. No rerun follows it.

| Field | Value |
|---|---|
| `stage` | `output_validation` (the failure occurred in the test's own post-response content assertion, after a completed provider round trip) |
| `class` | `output_validation_failed` |
| `retryable` | `false` under R1 (R1 permits zero reruns regardless of retryability; recorded for completeness only) |
| `userAction` | `revise_request` (the test's own assertion, not the request, needs revision) |
| `provider` | `alibaba` |
| `model` | `qwen-turbo` (the requested model; the response `model` field was not read before the assertion failed, so the provider-echoed model value is not separately confirmed) |
| `httpStatus` | not read into a variable before the failing assertion; the 200-consistent timing (13.45s, matching a real provider round trip) and the fact that the immediately prior `ALIBABA_API_KEY`-absence assertion passed are the basis for inferring a completed ALLOW response, not a direct `response.status` capture, because the test does not log status before this assertion |
| `latencyMs` | not captured into a named field before the failing assertion; total test-body duration was 13.45s (test infra timing, not `routeElapsedMs`/`providerLatencyMs` from the receipt, which the test never reached reading) |
| `receiptId` | not captured; the assertion failed before the test read `allowReceipt.receiptId` |
| `traceId` | not captured; the assertion failed before the test read `allowReceipt.envelopeId` |
| `safeMessage` | The real Alibaba provider call appears to have completed (based on elapsed time and the passing key-absence check immediately before the failure), but this tranche's own test assertion incorrectly treated the model's natural reference to the supplied topic text as a leakage failure. No credential value, signed header, or raw model output beyond the already-known non-secret topic string is disclosed by this diagnostic. |

### R1 Denominators (Reported Separately From The First Attempt)

- `liveCallCount` (R1): likely 1 real Alibaba provider call was attempted
  and its HTTP round trip appears to have completed (13.45s elapsed,
  consistent with a real network call; the immediately preceding
  key-absence assertion passed). This audit does not claim a *confirmed*
  ALLOW result, because the test failed before reading `allowResponse.status`,
  `allowData.success`, or `allowReceipt.decision` into evidence, and R1's
  no-rerun rule means this cannot be independently reconfirmed by rerunning.
- `blockRequestCount` (R1): 0. The keyless authority-gate BLOCK section
  (test lines 189 onward) was never reached because the ALLOW-side
  assertion at line 186 threw first.
- test-case denominator (R1): 1 focused test case, run exactly once, FAIL.
- event-model denominator (R1): unknown. The test never reached
  `readAuditEvents()` (line 231), so this audit cannot confirm whether zero,
  one, or two `MANDATORY_GATEWAY_EVALUATED` events were persisted to the
  isolated temporary event store before the process's `afterEach` cleanup
  removed that temporary directory. No further inspection is authorized
  under R1's zero-rerun rule.
- combined tranche total (first attempt + R1): 3 focused live-test
  executions across two dispatches (2 in the first attempt, 1 in R1); 0
  confirmed-and-evidenced ALLOW results; 0 confirmed BLOCK results; 0
  confirmed durable event pairs; 0 confirmed admin-projection renders.

n=1 statement (R1): even if the R1 run's ALLOW request did complete
against the real provider, this audit does not read or report
`providerLatencyMsObserved` or `routeElapsedMsObserved` from it, because
the test failed before those fields were read into evidence. No latency,
percentile, or SLO claim is made from R1.

### R1 Secret Hygiene Statement

No Alibaba/DashScope API key value, signed header, bearer token, or raw
provider request/response body was printed, copied, hashed, embedded, or
committed at any point in R1. The vitest failure output containing the
full serialized response (including the real model's output text) was
inspected only for safe summary facts (pass/fail count, total duration)
using targeted extraction, was never displayed in full, and the file
capturing it was deleted immediately after those safe facts were extracted.
The only fixture-originated string named in this section
("GC009 Live T5 bounded operator acceptance proof") is the test author's
own non-secret topic text, not a credential, prompt secret, or provider
output.

### R1 Terminal Evidence Verdict

`LIVE_ACCEPTANCE_BLOCKED_WITH_DIAGNOSTIC`

The R1 focused live run failed on the test's own topic-echo assertion after
an apparently completed real Alibaba provider round trip. Because the test
failed before reading the response status, decision, receipt, or event
data into evidence, this audit cannot confirm the required ALLOW proof,
BLOCK proof, durable-event correlation, or admin-projection proof, even
though a real provider call very likely occurred. R1 permits zero reruns
under any outcome; no further live attempt is authorized without a fresh
operator/reviewer-authorized redispatch that also repairs the topic-echo
assertion defect identified here.

## R2 Redispatch Evidence

### R2 Scope And Authorization

Per the work order's `## R2 Redispatch Override` section, R2 authorized: (1)
deleting exactly the two response-level assertions
`expect(allowSerialized).not.toContain(inputs.topic)` and
`expect(allowSerialized).not.toContain(inputs.context)`, without adding a
replacement response-level sentinel assertion; (2) retaining
`expect(allowSerialized).not.toContain(ALIBABA_API_KEY);` and the
event-level topic/context exclusions against `eventsSerialized`; (3)
re-running the offline generated-intent safety preflight before provider
use, requiring `NO_MATCH`; (4) exactly one focused live run with zero
reruns under any outcome.

### R2 Test Diff Scope Confirmation

Before provider use, `git diff --stat` and `git diff` on the focused test
path were inspected and confirmed the only change was a two-line deletion
at the `allowSerialized` assertion block (former lines 186-187), with no
other line touched:

```text
 1 file changed, 2 deletions(-)
-        expect(allowSerialized).not.toContain(inputs.topic);
-        expect(allowSerialized).not.toContain(inputs.context);
```

`expect(allowSerialized).not.toContain(ALIBABA_API_KEY);` (line 185) and the
event-level exclusions `expect(eventsSerialized).not.toContain(inputs.topic);`
and `expect(eventsSerialized).not.toContain(inputs.context);` (test lines
263-264 in the pre-R2 numbering) were confirmed present and unchanged.

### R2 Offline Safety Preflight (No Provider Call)

Before any provider use, built the complete generated ALLOW intent via the
real `getTemplateById`/`generateIntent` functions and the complete built
execution prompt via the real `buildExecutionPrompt` function (`route.ts`
line 274) against the same `inputs` object the corrected focused test uses,
then ran the real `runSafetyWorkflowChain` and `applySafetyFilters`
functions (the same functions `route.ts` calls) against both strings in a
disposable Vitest file with no route invocation, network call, or provider
credential use.

Result: `NO_MATCH` on both.

```json
{
  "intentWorkflowBlocked": false,
  "intentBlocked": false,
  "intentDetails": undefined,
  "promptWorkflowBlocked": false,
  "promptBlocked": false,
  "promptDetails": undefined
}
```

The disposable preflight file was deleted immediately after this result was
captured and before the live run; it was never one of the three worker-owned
paths and consumed no live-call budget.

### R2 Focused Live Run (Exactly One, Zero Reruns)

Command:

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npm exec vitest -- run src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx --reporter=verbose
Set-Location ../../../..
```

Result: FAIL after 27.02s total (12.70s inside the test body).

```text
AssertionError: expected [ 'gatewayAllowed', ...(4) ] to deeply equal [ 'gatewayAllowed', ...(6) ]
- Expected
+ Received
  [
    "gatewayAllowed",
-   "gatewayBlockedBy",
    "gatewayBypassed",
    "gatewayControlMode",
    "gatewayDecision",
-   "gatewayEscalatedBy",
    "gatewayRequestId",
  ]
 > expect(allowPayloadKeys).toEqual(expectedKeys);
```

The failure is at the ALLOW gateway-event payload key-set assertion (test
line 255 in the R2 file), which is textually far later in the test body than
R1's line-186 failure. Because this assertion executes only after every
assertion between it and the start of the test body has already passed
without throwing, this R2 run's own execution order proves, in sequence,
strictly more than R1 proved: HTTP 200, `success=true`, provider `alibaba`,
decision `ALLOW`, nonempty `output`, numeric `providerLatencyMs`, numeric
`routeElapsedMs`, the `claimBoundary` string, `ALIBABA_API_KEY`
non-leakage in the ALLOW response, the keyless-authority BLOCK request
reaching HTTP 400 with `model: 'guard-blocked'` and `guardResult.finalDecision
: 'BLOCK'` and `governanceEvidenceReceipt.decision: 'BLOCK'`,
`ALIBABA_API_KEY` non-leakage in the BLOCK response, exactly two
`MANDATORY_GATEWAY_EVALUATED` events read back from the isolated durable
store, both `allowEvent` and `blockEvent` found and correlated by
`gatewayRequestId`, `allowEvent!.outcome === 'ALLOW'`, and
`blockEvent!.outcome === 'BLOCK'`. All of those assertions are on lines
strictly before line 255 in the corrected test file and all returned without
throwing.

### R2 Root Cause (Source-Verified, No Rerun Performed To Confirm)

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts`
(`evaluateRouteMandatoryGateway`, lines 58-66) always constructs the event
payload object with all seven literal keys, including
`gatewayBlockedBy: gatewayResult.evidence?.blockedBy` and
`gatewayEscalatedBy: gatewayResult.evidence?.escalatedBy`. On a real ALLOW
decision, `gatewayResult.evidence?.blockedBy` and
`gatewayResult.evidence?.escalatedBy` are both `undefined` (these fields are
only populated on a BLOCK/escalation path). The event store's persistence
path serializes event payloads with `JSON.stringify`
(`control-plane-events.ts`), and per standard JavaScript/JSON semantics,
`JSON.stringify` omits object keys whose value is `undefined`. The ALLOW
event therefore legitimately round-trips through the durable store with only
5 payload keys (`gatewayAllowed`, `gatewayBypassed`, `gatewayControlMode`,
`gatewayDecision`, `gatewayRequestId`), while the BLOCK event round-trips
with all 7. The test's own `expectedKeys` constant asserts the same 7-key
array against both `allowPayloadKeys` and `blockPayloadKeys`
(`expect(allowPayloadKeys).toEqual(expectedKeys)`), which is correct for the
BLOCK event but incorrect for the ALLOW event. This is a test-assertion
design defect in this tranche's own focused test (an expectation that does
not account for `JSON.stringify`'s `undefined`-key-omission behavior on the
ALLOW path), not a defect in the mandatory gateway, guard engine,
route-guard-gateway adapter, control-plane event store, final response
builder, or Alibaba provider adapter. This root cause is established by
direct source reading of the already-executed code paths and standard
JSON.stringify semantics, not by any further live call, rerun, or
inspection of provider output.

### R2 Secret-Safe Diagnostic

Per R2 rule 8 and the live diagnostic standard's mandatory rule, this
diagnostic is recorded immediately on failure. No rerun follows it.

| Field | Value |
|---|---|
| `stage` | `output_validation` (the failure occurred in the test's own post-response event-payload-shape assertion, after a completed provider round trip, a completed BLOCK round trip, and completed durable-event readback) |
| `class` | `output_validation_failed` |
| `retryable` | `false` under R2 (R2 permits zero reruns regardless of retryability; recorded for completeness only) |
| `userAction` | `revise_request` (the test's own `expectedKeys` assertion, not the request, needs revision to expect a 5-key ALLOW payload and a 7-key BLOCK payload separately) |
| `provider` | `alibaba` |
| `model` | `qwen-turbo` (requested model only; the exact response model value was not asserted or separately logged) |
| `httpStatus` | 200 for the ALLOW request and 400 for the BLOCK request, both proven by the corresponding `expect(...).toBe(200)`/`expect(...).toBe(400)` assertions passing before line 255 |
| `latencyMs` | total test-body duration 12.70s (test infra timing, consistent with two completed HTTP round trips); the receipt's own numeric `providerLatencyMs`/`routeElapsedMs` values were proven numeric by `typeof ... === 'number'` assertions but the exact numeric values were not separately logged before the later failure |
| `receiptId` | not captured into this diagnostic; `allowReceipt.receiptId` was not read into a logged variable before the line-255 failure, even though `allowReceipt.decision` (a sibling field on the same object) was already proven equal to `'ALLOW'` |
| `traceId` | not captured into this diagnostic for the same reason |
| `safeMessage` | The real Alibaba ALLOW call and the keyless-authority BLOCK call both completed successfully through the actual route, and both were durably persisted and correlated by request ID. This tranche's own test asserted an identical 7-key payload shape for both the ALLOW and BLOCK gateway events, but the ALLOW event legitimately serializes with only 5 keys because `JSON.stringify` omits its two `undefined`-valued fields (`gatewayBlockedBy`, `gatewayEscalatedBy`), which are only populated on a BLOCK/escalation path. No credential value, signed header, or raw model output is disclosed by this diagnostic. |

### R2 Denominators (Reported Separately From The First Attempt And R1)

- `liveCallCount` (R2): 1 confirmed real Alibaba provider ALLOW call. HTTP
  200, `success=true`, provider `alibaba`, decision `ALLOW`, nonempty
  `output`, numeric `providerLatencyMs`, numeric `routeElapsedMs`, the
  `claimBoundary` string, and `ALIBABA_API_KEY` non-leakage in the ALLOW
  response are all confirmed passed assertions from this run.
- `blockRequestCount` (R2): 1 confirmed keyless authority-gate BLOCK
  request. HTTP 400, `success=false`, `model: 'guard-blocked'`,
  `guardResult.finalDecision: 'BLOCK'`,
  `governanceEvidenceReceipt.decision: 'BLOCK'`, and `ALIBABA_API_KEY`
  non-leakage in the BLOCK response are all confirmed passed assertions.
- durable event correlation (R2): 2 `MANDATORY_GATEWAY_EVALUATED` events
  confirmed read back from the isolated store; `allowEvent` and `blockEvent`
  both found and correlated by `gatewayRequestId`; `allowEvent!.outcome ===
  'ALLOW'` and `blockEvent!.outcome === 'BLOCK'` both confirmed passed.
- event payload shape (R2): the ALLOW event's observed 5-key set was the exact
  point of assertion failure. The BLOCK 7-key equality assertion, the
  `gatewayBlockedBy` assertion, and all event-level serialization exclusions
  are textually later and did not execute. Direct source reading explains the
  ALLOW shape, but this run does not prove the later BLOCK-shape, blocker-field,
  or event-minimization assertions.
- projection (R2): not reached. The `AdminAuditLogBody` render and its
  screen-text assertions are textually after line 255 and were never
  executed.
- identifiers (R2): `allowRequestId = 'gc009-live-t5-allow-request'` and
  `blockRequestId = 'gc009-live-t5-block-request'` are the fixed literal
  request IDs the test itself defines (not live-generated secrets); the
  live-generated `allowReceipt.receiptId`, `allowReceipt.envelopeId`,
  `allowEvent!.id`, and `blockEvent!.id` values were not captured into this
  diagnostic or audit, because the test's own final `console.log` block
  (test lines 297-313) that would have emitted them is textually after line
  255 and was never reached.
- telemetry (R2): `providerLatencyMs` and `routeElapsedMs` are confirmed
  numeric (via `typeof` assertions) but their exact numeric values are not
  retained in this audit, for the same reason.
- test-case denominator (R2): 1 focused test case, run exactly once, FAIL.
- combined tranche total (first attempt + R1 + R2): 4 focused live-test
  executions across three dispatches (2 in the first attempt, 1 in R1, 1 in
  R2); 2 confirmed real Alibaba provider calls (1 in R1 and 1 in R2); 2
  confirmed ALLOW results (1 in R1 and 1 in R2); 1 confirmed keyless guard
  BLOCK result (R2); 1 confirmed
  two-event durable correlation (R2); 0 confirmed admin-projection renders
  (not reached in any attempt).

n=1 statement (R2): this audit confirms `providerLatencyMs` and
`routeElapsedMs` are numeric from exactly one real ALLOW observation. No
exact numeric value, percentile, throughput, or SLO inference is made or
inferrable from this single observation.

### R2 Secret Hygiene Statement

No Alibaba/DashScope API key value, signed header, bearer token, or raw
provider request/response body was printed, copied, hashed, embedded, or
committed at any point in R2. The vitest failure output was inspected only
for the safe summary facts recorded above (assertion path, pass/fail
sequence, total duration, the diff of the two payload key arrays, which
contain only literal field-name strings and no secret or model-output
content) using targeted extraction; the raw output file was deleted
immediately after those safe facts were extracted. The disposable offline
preflight file was deleted immediately after its `NO_MATCH` result was
captured, before the live run.

### R2 Terminal Evidence Verdict

`LIVE_ACCEPTANCE_BLOCKED_WITH_DIAGNOSTIC`

The R2 focused live run confirmed, via passed assertions strictly preceding
the point of failure, a real Alibaba ALLOW result, a fail-closed
keyless-authority BLOCK result, and two-event durable correlation with
correct outcome/request-ID linkage -- substantially more of the work order's
required proof manifest than either prior attempt reached. It failed on the
test's own over-strict payload-key-set assertion, which incorrectly expects
the ALLOW event's `JSON.stringify`-serialized payload to contain the same 7
keys as the BLOCK event's payload, when the ALLOW event legitimately
contains only 5 (the 2 BLOCK/escalation-only fields are `undefined` and
omitted by standard JSON serialization). Admin-projection proof was not
reached. R2 permits zero reruns under any outcome; no further live attempt
is authorized without a fresh operator/reviewer-authorized redispatch that
also repairs the payload-key-set assertion defect identified here (for
example, asserting the ALLOW event's actual 5-key subset separately from the
BLOCK event's 7-key set, or filtering `expectedKeys` to only the keys with
defined values per event before comparison).

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Route invokes gateway before provider | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 577 (`runExecuteRouteMandatoryGateway`); line 777 (`executeAI`) | `runExecuteRouteMandatoryGateway`; `executeAI` | execute route `POST` | ACCEPT (re-verified fresh, unchanged from dispatch-base freshness statement) |
| Gateway event payload always includes both BLOCK-only fields as literal keys | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` | lines 58-66 (`gatewayBlockedBy: gatewayResult.evidence?.blockedBy`; `gatewayEscalatedBy: gatewayResult.evidence?.escalatedBy`) | `evaluateRouteMandatoryGateway` | route-guard-gateway adapter | ACCEPT |
| Event store persists payloads via `JSON.stringify`, which omits `undefined`-valued keys | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | line 86 (`JSON.stringify(event.payload ?? {})`, CSV path); `writeEvents`/`_eventAdapter.writeAll` (lines 102-104) for the JSON durable-store write path | `writeEvents`; `_eventAdapter.writeAll` | control-plane event store | ACCEPT |
| Safety filter runs before the mandatory gateway | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 324 (`applySafetyFilters(saf1Result.sanitized)`) | `applySafetyFilters` | execute route `POST` | ACCEPT |
| Safety filter blocks on the literal word "secret" | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts` | line 12 (`PII_PATTERNS`); line 31 (`blocked: true, reason: 'Safety filter triggered'`) | `applySafetyFilters`; `PII_PATTERNS` | safety filter module | ACCEPT |
| Focused-test ALLOW fixture contains the word "secret" | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx` | `inputs.options` field, "Verify no raw secret leakage" | `inputs` | this tranche's own focused live test | ACCEPT |
| T4 records latency as unmeasured | VALUE_SET | `docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T4_VALUE_LATENCY_FAILURE_ROLLBACK_ASSESSMENT_COMPLETION_2026-07-26.md` | Latency Decision | `NOT_MEASURED_NO_LIVE_AUTHORITY` | T4 completion review | ACCEPT (unchanged; this tranche adds no new latency evidence) |
| First-attempt review accepted the blocked diagnosis and authorized R1 | VALUE_SET | `docs/reviews/CVF_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_COMPLETION_2026-07-26.md` | Decision / Disposition | `REVIEWER_ACCEPTED_BLOCKED_WITH_DIAGNOSTIC_R1_AUTHORIZED` | first-attempt completion review | ACCEPT |
| R1 override requires zero reruns under every outcome | LITERAL_INVARIANT | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_LIVE_T5_BOUNDED_OPERATOR_ACCEPTANCE_PROOF_2026-07-26.md` | `## R1 Redispatch Override`, item 4 | `No rerun is authorized` | R1 work order section | ACCEPT |
| Corrected fixture text is present in the focused test | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx` | `inputs.options` field, "Verify no credential value leakage" | `inputs` | this tranche's own focused live test | ACCEPT |
| Route builds the execution prompt via `buildExecutionPrompt` before the safety filter | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | line 274 (`buildExecutionPrompt`); line 324 (`applySafetyFilters`) | `buildExecutionPrompt`; `applySafetyFilters` | execute route `POST` | ACCEPT |

## New Doc-Only Fields

| Proposed item | Meaning | Runtime/source status |
|---|---|---|
| `liveCallCount` (first attempt) | 0 | DOC_ONLY_NEW |
| `liveCallCount` (R1, corrected by R2) | confirmed 1 real Alibaba ALLOW call reached and passed HTTP 200/success/decision/provider/output/telemetry/key-non-leakage assertions before the topic-echo assertion failed; exact numeric telemetry values were not retained in the R1 document | DOC_ONLY_NEW |
| `blockRequestCount` (first attempt) | 0 | DOC_ONLY_NEW |
| `blockRequestCount` (R1) | 0 (BLOCK section never reached; confirmed unchanged by R2 correction) | DOC_ONLY_NEW |
| `liveCallCount` (R2) | 1 confirmed real Alibaba ALLOW call, same denominator meaning as R1's corrected value | DOC_ONLY_NEW |
| `blockRequestCount` (R2) | 1 confirmed keyless guard BLOCK request, reaching HTTP 400/`guard-blocked`/BLOCK decision; the later `gatewayBlockedBy === 'authority_gate'` assertion did not execute | DOC_ONLY_NEW |
| `providerLatencyMsObserved` | confirmed numeric in R2 (via `typeof` assertion) but exact value not retained in this audit; not obtained in the first attempt or R1 | DOC_ONLY_NEW |
| `routeElapsedMsObserved` | confirmed numeric in R2 (via `typeof` assertion) but exact value not retained in this audit; not obtained in the first attempt or R1 | DOC_ONLY_NEW |
| `diagnosticDisposition` (first attempt) | `BLOCKED_AFTER_ONE_DIAGNOSTIC_RERUN_SELF_INFLICTED_FIXTURE_DEFECT` (historical; reviewer rejected the rerun-compliance claim, retained the blocked diagnosis) | DOC_ONLY_NEW |
| `diagnosticDisposition` (R1) | `BLOCKED_WITH_REASON_ZERO_RERUN_TOPIC_ECHO_ASSERTION_DEFECT` | DOC_ONLY_NEW |
| `diagnosticDisposition` (R2) | `BLOCKED_WITH_REASON_ZERO_RERUN_ALLOW_EVENT_PAYLOAD_KEYSET_ASSERTION_DEFECT` | DOC_ONLY_NEW |

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

### R2 Epistemic Process Addendum

- Expected result / prediction (R2): given the exact two-assertion deletion
  authorized by the R2 override and a passing offline preflight, the R2 run
  was expected to reach at least the ALLOW proof, BLOCK proof, and
  durable-event correlation targets, and possibly complete the full test.
- Evidence Comparison: the prediction was partially confirmed. The R2 run
  did confirm real Alibaba ALLOW, fail-closed BLOCK, and two-event durable
  correlation with correct outcome/request-ID linkage, all via assertions
  that executed and passed before the failure point. It did not complete,
  failing on a previously undiscovered assertion (the ALLOW/BLOCK
  event-payload key-set equality check) that neither the first attempt nor
  R1 ever reached.
- Contradiction or gap disposition: no contradiction was found in the
  accepted T1-T4 chain, the mandatory gateway, the route-guard-gateway
  adapter, the control-plane event store, or the Alibaba provider adapter;
  the gap is fully contained in and explained by this tranche's own test
  assertion not accounting for `JSON.stringify`'s standard
  `undefined`-key-omission behavior on the ALLOW-only payload subset,
  confirmed by direct source reading of `route-guard-gateway.ts` and
  `control-plane-events.ts`.
- Claim update: this tranche now confirms, for the first time across all
  three dispatches, a real Alibaba ALLOW result and a fail-closed keyless
  guard BLOCK result with durable two-event correlation. It still
  does not confirm admin-component projection, exact numeric telemetry
  values, or full test-case PASS. It does not extend or weaken the accepted
  GC-009 T1-T4 chain. R2 permits zero reruns; final reviewer closure stops
  without a further live attempt.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | review structural heading families (target/source, scope/methodology, findings/position, risk/corrective action, decision/disposition); Delta block Field/Disposition table shape; Machine Closure Package required column set; equivalence-claim trigger words paired with adjacent evidence commands or disposition tokens; ASCII prose discipline; `BLOCKED_WITH_REASON` status token spelling |
| gateRunPurpose | confirm this audit's required shape and literal-format compliance before the worker-return fast gate runs; gates are confirmation evidence, not first discovery |
| claimBoundary | checker compliance is gate-shape evidence only; direct live evidence is limited to the assertions reached in R1/R2 and excludes later R2 payload, minimization, and projection assertions |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance live-proof attempt only; no public-sync
authorization exists, and this artifact records a blocked (not passed)
proof attempt.

## Claim Boundary

This audit records one focused live test authored and modified in place
across three dispatches (first attempt: two permitted runs; R1: one
corrected run with zero reruns; R2: one further corrected run with zero
reruns), for a combined four focused live-test executions. The first
attempt's two runs failed at `request_validation` before reaching the
mandatory gateway or provider; that finding is independently reviewed and
accepted, and is preserved here as historical evidence. The R1 run reached
the real Alibaba provider and passed every assertion up to and including
`ALIBABA_API_KEY` non-leakage, then failed on this tranche's own
over-strict topic-echo assertion, as corrected and confirmed by R2's
execution order. The R2 run, after the R2-authorized deletion of that
  topic-echo assertion pair, confirmed a real Alibaba ALLOW result, a
  fail-closed keyless guard BLOCK result, and two-event durable correlation
with correct outcome/request-ID linkage -- all via assertions that executed
and passed before the run's own failure point -- then failed on a
previously unreached assertion comparing the ALLOW and BLOCK gateway
events' payload key sets, which does not account for `JSON.stringify`
omitting the two `undefined`-valued BLOCK-only fields from the ALLOW
event's persisted payload. This audit does not claim a completed PASS,
admin-component projection, or exact numeric telemetry values from any
attempt. It does not authorize any further rerun (R2 permits zero under any
outcome), runtime mutation, broad release proof, production percentile or
SLO claims, public export, push, deployment, rollback, GC-010 work, or any
claim beyond identifying the exact defects (a fixture word in the first
attempt; a topic-echo assertion in R1; an ALLOW/BLOCK payload-key-set
equality assertion in R2) that prevented any attempt from producing a fully
  accepted end-to-end live-proof result. Across R1 and R2, the provider-call
  denominator is 2, not 1. The R2 failure also means the later BLOCK payload
  equality, blocker-field, event-level exclusion, and UI projection assertions
  remain unexecuted.
