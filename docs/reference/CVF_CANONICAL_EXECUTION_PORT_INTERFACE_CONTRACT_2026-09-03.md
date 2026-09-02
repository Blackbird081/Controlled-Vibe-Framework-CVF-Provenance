# CVF Canonical Execution Port Interface Contract

Memory class: FULL_RECORD

docType: reference

Status: CLOSED_PASS_BOUNDED

Batch ID: CSCC-R1-T1

Date: 2026-09-03

executionBaseHead: `a232e2e7a`

Owner package: `CVF_MODEL_GATEWAY`

## Purpose

Freeze the exact TypeScript names, field tables, invocation ordering, and
compatibility/rollback rules for `CanonicalExecutionPort`, the caller-neutral
execution port that CSCC-R1-T0A selected as the future stable contract
between a Web (or later MAO) caller and the concrete `ProviderExecutionBridge`
provider boundary inside `CVF_MODEL_GATEWAY`. This document names types and
behavior only. No source, test, or package-export file is created or edited
by this tranche; `CanonicalExecutionPort`, `CanonicalExecutionAdapter`, and
every field below remain design-only names until an independently accepted
T2 implements them.

## Scope / Applies To

Applies to a planned addition inside `CVF_MODEL_GATEWAY/src`, most naturally
alongside `unified-gateway-interface-contract.ts` or `index.ts` (exact file
left to T2). Does not apply to and does not modify
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts`,
`EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts`,
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`,
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-attempt-admission.ts`,
any test file, or any package export. Does not authorize MAO submission/launch
wiring or any provider/live call.

## Current Runtime Freshness Verification

Exact search results re-run at `executionBaseHead` `a232e2e7a`:

1. `GatewayExecuteRequest|ProviderExecutionBridgeExecuteOptions|ProviderExecutionBridge|adapter.execute`
   over `EXTENSIONS/CVF_MODEL_GATEWAY/src` (files-with-matches mode) returns
   eight files: `lpci-safe.ts`, `p4b-b-live-proof-harness.ts`, `index.ts`,
   `material-context-manifest.ts`, `provider-execution-bridge.ts`,
   `unified-gateway-interface-contract.ts`, `unified-gateway-skeleton.ts`,
   `provider-adapter-conformance.ts`. Direct read of
   `provider-execution-bridge.ts` confirms `ProviderExecutionBridgeExecuteOptions`
   (line 64) currently declares exactly one field, `signal?: AbortSignal`
   (line 65), and that `adapter.execute` (line 194) is called exactly once,
   after routing (line 105), adapter lookup (line 110-111), credential
   lookup/metadata (lines 121-132), health (line 143), quota (line 153-158),
   `checkBridgeAdmission` (line 171), and material-context-manifest
   build/validate (lines 185-192) all pass. This matches T0A's finding
   unchanged: the additive seam is real, currently one-field, and the
   ordering is unchanged since T0A.
2. `CanonicalExecutionPort|canonicalExecutionId|beforeProviderInvoke` across
   `EXTENSIONS` (excluding `node_modules`) returns zero files. No competing
   symbol exists. This matches T0A's negative-search finding; no source
   contradiction is present.

No newly existing competing symbol and no changed invocation order were
found. T0A's accepted ownership and ordering stand unmodified at this
execution base.

## Distinguishing The Port From `ProviderExecutionBridge`

`CanonicalExecutionPort` is the stable, caller-facing contract that a Web
adapter and a future MAO adapter both import from `CVF_MODEL_GATEWAY`.
`ProviderExecutionBridge` is the concrete Gateway-internal class that already
owns routing, credential, health, quota, static adapter eligibility, and
adapter dispatch (`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts`,
class `ProviderExecutionBridge`, method `execute`, lines 68-268). The port
does not replace the bridge and does not re-implement any of its five
pre-adapter concerns; it wraps `ProviderExecutionBridge.execute` behind a
narrower, caller-neutral method shape and carries one additive field so a
caller-supplied atomic attempt-boundary callback can reach the bridge without
Gateway ever importing a Web type. `CVF_MODEL_GATEWAY` continues to own both
symbols in the same package; only their roles differ.

## Stable Port And Concrete Adapter Types

The exact stable caller contract is:

```
export interface CanonicalExecutionPort {
  execute(request: CanonicalExecutionPortRequest):
    Promise<CanonicalExecutionPortResult>;
}
```

Candidate concrete class name: `CanonicalExecutionAdapter`.

```
export declare class CanonicalExecutionAdapter implements CanonicalExecutionPort {
  constructor(bridge: ProviderExecutionBridge);
  execute(request: CanonicalExecutionPortRequest):
    Promise<CanonicalExecutionPortResult>;
}
```

`CanonicalExecutionAdapter` is Gateway-owned composition code, not a provider
adapter. It maps `canonicalExecutionId` to both the underlying
`GatewayExecuteRequest.traceId` and its additive optional
`GatewayExecuteRequest.canonicalExecutionId` carrier, maps the remaining
request fields without making a second routing or credential decision,
transports `attemptBoundary` as
`ProviderExecutionBridgeExecuteOptions.beforeProviderInvoke`, calls
`ProviderExecutionBridge.execute` exactly once, and maps that result into the
port result. It never calls a provider adapter directly.

## Additive Gateway Request Identity Carrier

T2 adds one optional field to the existing Gateway request:

| Owner | Additive field | Required | Rule |
| --- | --- | --- | --- |
| `GatewayExecuteRequest` | `canonicalExecutionId?: string` | no | `CanonicalExecutionAdapter` sets it equal to `traceId` from the port request. `ProviderExecutionBridge` propagates it unchanged to callback input, `GatewayReceipt`, and `MaterialContextManifest`. Legacy callers omit it, so the bridge must not infer canonical composition merely from an arbitrary legacy `traceId`. |

This carrier is the only way the bridge distinguishes a port-composed request
from a legacy request for conditional join-field population. It is never a
second identity generator.

## Port Request Type

Candidate name: `CanonicalExecutionPortRequest`.

| Field | Type | Required | Source / Notes |
| --- | --- | --- | --- |
| `canonicalExecutionId` | `string` | yes | Seeded from `WebGovernanceEnvelope.envelopeId`; mapped to both `GatewayExecuteRequest.traceId` and its optional `canonicalExecutionId` carrier; see the paired identity contract for the single canonical name shared by both documents. |
| `prompt` | `string` | yes | Passed through unchanged to `GatewayExecuteRequest.prompt`. |
| `systemPrompt` | `string` | no | Passed through unchanged to `GatewayExecuteRequest.systemPrompt`. |
| `policy` | `GatewayPolicyContext` | yes | Passed through unchanged to `GatewayExecuteRequest.policy`. |
| `preferredProviderId` | `string` | no | Carries Web's current `routedProvider` value as a policy hint into `RoutingRequest.preferredProviderId`; never a final decision (T0A seam 3). |
| `routing` | `RoutingRequest` (minus `traceId`, `preferredProviderId`) | no | Remaining routing hints (`requestedModelId`, `estimatedTokens`, `executionStage`, `complexityScore`, `riskScore`, `requiredCapabilities`, `costBudget`, `latencyBudgetMs`); passed through to `GatewayExecuteRequest.routing`. |
| `metadata` | `Record<string, unknown>` | no | Passed through unchanged to `GatewayExecuteRequest.metadata`. |
| `attemptBoundary` | `CanonicalExecutionAttemptBoundary` | yes | The atomic callback described below. It is mandatory on the stable canonical port request. Legacy Gateway callers do not construct this port request and remain compatible by omitting only the additive bridge option described below (see Compatibility / Rollback Matrix). |
| `signal` | `AbortSignal` | no | Passed through unchanged to the underlying bridge execute-options signal field. |

`CanonicalExecutionPortRequest` never carries a raw provider API key,
`apiKeyMap` entry, or Gateway `CredentialReference`; credential resolution
remains exclusively inside `ProviderExecutionBridge` via `CredentialBoundary`
(T0A seam 3).

## Port Result Type

Candidate name: `CanonicalExecutionPortResult`.

| Field | Type | Present when | Notes |
| --- | --- | --- | --- |
| `canonicalExecutionId` | `string` | always | Echoes the request identity; never re-derived. |
| `response` | `GatewayExecuteResponse` | adapter execution succeeded | Passed through unchanged from `ProviderExecutionBridgeResult.response`. |
| `error` | `GatewayErrorEnvelope` | any pre-adapter stop, callback denial, callback throw, or adapter error | Passed through unchanged from `ProviderExecutionBridgeResult.error`; `errorClass` distinguishes the stop reason (see Pre-Adapter Stop Table and Callback Outcome Table). |
| `receipt` | `GatewayReceipt` | always | Passed through unchanged from `ProviderExecutionBridgeResult.receipt`. The paired identity contract adds `canonicalExecutionId` onto this schema as an additive join field; the port result does not duplicate that field a second time inside a nested payload. |
| `materialContextManifest` | `MaterialContextManifest` | only when `materialContextManifestDisposition` is `"attached"` | Passed through unchanged. |
| `materialContextManifestDisposition` | `GatewayMaterialContextManifestDisposition` | always | Passed through unchanged; `"not_built_precondition_stopped"` covers every pre-manifest pre-adapter stop, `"invalid"` covers manifest build/validate failure, `"attached"` covers both adapter success and adapter error (matching current `ProviderExecutionBridge` behavior exactly). |
| `attemptOutcome` | `CanonicalExecutionAttemptOutcomeSummary` | always | New port-only field. `"not_reached"` for every pre-adapter stop (routing, adapter lookup, credential, health, quota, `checkBridgeAdmission`, manifest failure); `"denied"` for callback denial; `"callback_error"` for callback throw; `"invoked"` for callback allow (regardless of whether the subsequent adapter call itself succeeds or errors). This field lets a caller distinguish "no attempt was ever made" from "an attempt was made and the adapter later failed" without inspecting `errorClass` string matching. |

Candidate name and exact shape:

```
type CanonicalExecutionAttemptOutcomeSummary =
  | "not_reached"
  | "denied"
  | "callback_error"
  | "invoked";
```

## Atomic Callback Input Type

Candidate name: `CanonicalExecutionAttemptBoundaryInput`.

| Field | Type | Notes |
| --- | --- | --- |
| `canonicalExecutionId` | `string` | Same value as the port request; never regenerated at the callback boundary. |
| `providerId` | `string` | The Gateway-selected provider, from `RoutingDecision`, after `RoutingPolicyEngine.decide` has already run. |
| `modelId` | `string` | The Gateway-selected model, from the same decision. |
| `traceId` | `string` | The underlying `GatewayExecuteRequest.traceId` value used for this bridge execution (mapped 1:1 from `canonicalExecutionId` by the concrete port adapter; see identity contract propagation rule). |

`attemptIndex` is intentionally absent from this input. Gateway constructs the
input before invoking the Web-owned callback, whereas only the callback's
subsequent `admitProviderAttempt` call can allocate the fresh index. Supplying
an index here would reverse that data dependency.

## Atomic Callback Outcome Type

Candidate name: `CanonicalExecutionAttemptBoundaryOutcome`.

| Variant | Shape | Meaning |
| --- | --- | --- |
| `{ decision: "allow"; attemptIndex: number }` | `attemptIndex` is the fresh index returned by `admitProviderAttempt` | The Web callback has already completed `admitProviderAttempt` (admitted) and `recordProviderCallStart` for this same `attemptIndex`, in that order, before returning. Gateway proceeds immediately to `adapter.execute`. |
| `{ decision: "deny"; attemptIndex: number; reason: string; retryAfterSeconds?: number }` | `attemptIndex` is the denied-attempt record allocated by `admitProviderAttempt`; `reason` is a short non-secret string | The Web callback's `admitProviderAttempt` call was denied. `recordProviderCallStart` was never called. Gateway does not call `adapter.execute` and maps this to a typed no-invocation error (see Callback Outcome Table). |

## Atomic Callback Type

Candidate name: `CanonicalExecutionAttemptBoundary`.

```
type CanonicalExecutionAttemptBoundary =
  (input: CanonicalExecutionAttemptBoundaryInput) =>
    Promise<CanonicalExecutionAttemptBoundaryOutcome>;
```

This is the exact function type carried on `CanonicalExecutionPortRequest.attemptBoundary`
and, after the concrete port adapter maps it, on the additive bridge
execute-option below. Gateway invokes it exactly once per bridge execution,
only when every pre-adapter stop has already passed, and only ever
immediately before its own single `adapter.execute` call.

The canonical Web callback has exactly one awaited/fallible operation:
`admitProviderAttempt`. If that operation rejects, the callback rejects before
any admission-ledger mutation attributable to a returned result. After it
returns an allowed result, the callback performs the current synchronous,
non-throwing `recordProviderCallStart(ledger, attemptIndex)` call and returns
the allow outcome without another `await` or branch. This closes the interval
in which an admitted attempt could be stranded without call-start accounting.
Any future change that introduces a fallible operation in that interval must
first define an explicit ledger reconciliation mechanism and revise this
contract; it cannot rely on the generic callback-throw path.

## Additive Bridge Execute-Option

Candidate name: extend `ProviderExecutionBridgeExecuteOptions`
(`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts`, line 64,
currently `{ signal?: AbortSignal }`) with one new optional field:

| Field | Type | Required | Compatibility rule |
| --- | --- | --- | --- |
| `beforeProviderInvoke` | `(input: CanonicalExecutionAttemptBoundaryInput) => Promise<CanonicalExecutionAttemptBoundaryOutcome>` | no (additive optional) | When omitted, `ProviderExecutionBridge.execute` behaves exactly as it does today: no callback is invoked, and `adapter.execute` runs immediately once all pre-adapter stops pass. When present, `ProviderExecutionBridge.execute` invokes it exactly once, immediately before its one `adapter.execute` call, only after every pre-adapter stop already passed, and only calls `adapter.execute` if the outcome is `{ decision: "allow" }`. A `{ decision: "deny" }` outcome or a thrown exception from `beforeProviderInvoke` short-circuits before `adapter.execute` and produces a typed no-invocation error result (see Callback Outcome Table) instead of a normal bridge result. |

`ProviderExecutionBridgeExecuteOptions` remains an object type with two
optional fields (`signal`, `beforeProviderInvoke`) after this addition; no
existing field is renamed, removed, or made required. Every current caller
that constructs `{}` or `{ signal }` continues to compile and behave
identically (Legacy-Caller row below).

## Pre-Adapter Stop Table

Every row below is a stop inside `ProviderExecutionBridge.execute` that
occurs strictly before `beforeProviderInvoke` would be called. None of them
ever invoke the callback, and none of them ever touch `admittedCount` or
`providerCallCount` (T0A seam 4, ordered-sequence steps 7-10).

| Stop | Current source location | `errorClass` | `attemptOutcome` |
| --- | --- | --- | --- |
| Routing denied / requires approval / no candidate | `provider-execution-bridge.ts` line 106, `buildStoppedResult` | `policy_denied` or `no_candidate` | `not_reached` |
| No adapter registered for selected provider | line 111, `buildShieldedErrorResult` | `provider_unavailable` | `not_reached` |
| No credential reference configured | line 122 | `credential_shielded` | `not_reached` |
| Credential metadata unavailable | line 133 | `credential_shielded` | `not_reached` |
| Health check failed | line 143 | `provider_unavailable` | `not_reached` |
| Quota exceeded | line 158 | `quota_exceeded` | `not_reached` |
| `checkBridgeAdmission` blocked | line 171 | `admission_blocked` | `not_reached` |
| Material-context-manifest build or validate failed | lines 186, 190 | `invalid_request` | `not_reached` |

## Callback Outcome Table

| Callback result | Adapter called | `admittedCount` | `providerCallCount` | `errorClass` (when applicable) | `attemptOutcome` |
| --- | --- | --- | --- | --- | --- |
| Denial (`{ decision: "deny" }`) | no | unchanged | unchanged | `admission_blocked` | `denied` |
| Throw before admission returns (including admission rejection) | no | unchanged | unchanged | `internal_error` (typed no-invocation subtype; see Compatibility / Rollback Matrix note) | `callback_error` |
| Allow (`{ decision: "allow", attemptIndex }`) | yes, exactly once | +1 | +1 | n/a on success; `internal_error` on adapter throw | `invoked` |

A callback denial leaves `admittedCount` and `providerCallCount` unchanged
while recording one denied attempt (`deniedCount` increases by one). A
callback rejection before admission returns leaves both counters unchanged.
The Web callback's own `admitProviderAttempt`/`recordProviderCallStart` pair is
the only place either admitted or call-start count changes. The canonical
implementation has no fallible gap after an allowed admission, as frozen
above; therefore the generic throw path is not permitted to describe a throw
after `admittedCount` has changed.

## Adapter Success / Error / Retry / Legacy-Caller Outcomes

| Case | Behavior |
| --- | --- |
| Adapter success | Unchanged from current `ProviderExecutionBridge.execute` (lines 193-237): health success recorded, quota use recorded, receipt built with `validationState: "passed"`, response returned. `attemptOutcome: "invoked"`. |
| Adapter error (thrown inside `adapter.execute`) | Unchanged from current bridge behavior (lines 238-266): health failure recorded, receipt built with `validationState: "failed"`, `errorClass: "internal_error"`, `retryable: true`. `attemptOutcome: "invoked"` (the attempt was made; only the adapter call itself failed). |
| Retry | A retry starts a fresh port call (fresh `CanonicalExecutionPortRequest`, same `canonicalExecutionId`). It reaches `beforeProviderInvoke` again only if every pre-adapter stop passes again. The Web callback's fresh `admitProviderAttempt` call produces a fresh `attemptIndex`, which the callback returns in its allow or deny outcome; no prior attempt index or admission state is reused across port calls. |
| Legacy Gateway caller (omits `beforeProviderInvoke`) | `ProviderExecutionBridge.execute` behaves exactly as today: no callback path exists, `adapter.execute` runs immediately once pre-adapter stops pass, and no `CanonicalExecutionPortResult`-shaped value is produced (legacy callers keep consuming `ProviderExecutionBridgeResult` directly, unaffected by the port's existence). |

## Compatibility / Rollback Matrix

| Dimension | Rule |
| --- | --- |
| Port declaration location | `CVF_MODEL_GATEWAY` only (T0A seam 2 correction R1). Never declared inside `cvf-web` or `CVF_EXECUTION_PLANE_FOUNDATION`. |
| Import direction | `cvf-web` may import the port from `CVF_MODEL_GATEWAY`. `CVF_EXECUTION_PLANE_FOUNDATION` (MAO) may import the port from `CVF_MODEL_GATEWAY`, extending its existing precedent of importing `GatewayExecuteRequest`/`CredentialReference`/`runLiveProof` directly from the same package. `CVF_MODEL_GATEWAY` imports from neither. `cvf-web` and `CVF_EXECUTION_PLANE_FOUNDATION` never import from each other through or around the port. |
| Legacy Gateway callers | Callers that construct `ProviderExecutionBridgeExecuteOptions` without `beforeProviderInvoke` (including every current non-`/api/execute` consumer named in T0A's Source Verification Block) remain fully source- and behavior-compatible; the new field is additive and optional. |
| Legacy Gateway request identity | Existing callers may omit `GatewayExecuteRequest.canonicalExecutionId`; their existing `traceId` remains authoritative for legacy behavior and does not cause a canonical join field to be synthesized. |
| Canonical Web composition | The Web adapter that wires the port must supply `attemptBoundary` on every `CanonicalExecutionPortRequest`; a port adapter that would omit it must not be selected as the canonical Web wiring. |
| Exclusive adapter selection | Web owns exactly one composition-root choice per route build: either the current direct `executeAI` plus `admitAndInvokeProvider` path, or the canonical port-backed Gateway adapter. Both are never wired active on the same route build (T0A seam 4 rollback rule). |
| Rollback target | Until T2 is independently accepted, the direct `executeAI`/`admitAndInvokeProvider` path remains the rollback target; the port and its bridge option exist as additive, uncalled surface only. |
| Internal error subtype naming | This document does not add a new `GatewayErrorClass` enum member for callback-throw; it reuses `internal_error` (already present in `GatewayErrorClass`, `unified-gateway-interface-contract.ts` line 21) and requires a future implementation to record the throw as a distinct receipt `reason` string (for example `"attempt_boundary_callback_threw"`) rather than overloading `"adapter_execution_error"`, so a caller can still distinguish callback-throw from an adapter-level throw by receipt `reason` even though both share `errorClass: "internal_error"`. This naming choice is a T1 design freeze; T2 may implement it verbatim or propose a narrower enum addition subject to independent review. |

## Future T2 Deterministic Test-Name Manifest

These are names and expected assertions only. No test file is created or
edited by this tranche.

Planned file: `EXTENSIONS/CVF_MODEL_GATEWAY/tests/canonical-execution-port.test.ts`.

| # | Risk class | Test name | Expected assertion |
| --- | --- | --- | --- |
| 1 | Every pre-adapter stop leaves both counts zero | `"every pre-adapter stop leaves admittedCount and providerCallCount unchanged"` | For each of the eight Pre-Adapter Stop Table rows, run the port with a `beforeProviderInvoke` spy; assert the spy was never called and any test-double ledger counters remain at their pre-call value. |
| 2 | Callback denial invokes no adapter, increments neither admitted nor provider-call count | `"callback denial short-circuits before adapter.execute with no admitted or provider-call count change"` | Let the Web callback call `admitProviderAttempt` and return `{ decision: "deny", attemptIndex, reason: "..." }`; assert the adapter's `execute` spy was never called, `admittedCount` and `providerCallCount` are unchanged, and exactly one denied-attempt record was added. |
| 3 | Callback allow increments both exactly once immediately before one adapter call | `"callback allow returns its fresh attemptIndex after incrementing admittedCount and providerCallCount exactly once before the single adapter.execute call"` | Let the Web callback call `admitProviderAttempt`, synchronously call `recordProviderCallStart` with the returned index, and return `{ decision: "allow", attemptIndex }`; assert both counters increment by exactly 1 and the adapter `execute` spy is called exactly once after the callback resolves. |
| 4 | Callback throw produces typed no-invocation error | `"callback rejection before admission maps to a typed internal_error result without invoking the adapter or mutating the attempt ledger"` | Configure `beforeProviderInvoke` to reject before calling admission; assert the result carries `errorClass: "internal_error"`, `attemptOutcome: "callback_error"`, the adapter `execute` spy was never called, and the attempt ledger is unchanged. |
| 5 | Retry receives a fresh attempt index | `"a second port call after retry returns a fresh attemptIndex, never reusing the prior one"` | Run the port twice with the same `canonicalExecutionId`; capture the `attemptIndex` returned by each callback outcome and assert the second differs from the first and no state from the first call's admission is reused. |
| 6 | Legacy Gateway caller omission preserves behavior | `"ProviderExecutionBridge.execute without beforeProviderInvoke behaves exactly as before this addition"` | Call `ProviderExecutionBridge.execute` with `options` containing only `signal` (or `{}`); assert the result and call sequence are byte-identical to the pre-addition golden behavior captured in `provider-execution-bridge.test.ts`. |
| 7 | Canonical Web adapter requires the callback | `"the canonical Web port adapter refuses to construct a CanonicalExecutionPortRequest without attemptBoundary"` | Attempt to build a canonical Web port request without `attemptBoundary`; assert a compile-time or constructor-time rejection, not a silent Gateway-side default. |
| 8 | Direct and port adapters cannot both be active | `"exactly one of the direct executeAI adapter or the canonical port adapter is wired per route build"` | Inspect the Web composition-root wiring for a single route build; assert exactly one adapter implementation is registered and the other is absent, never both. |
| 9 | MAO imports no Web package | `"CVF_EXECUTION_PLANE_FOUNDATION imports the canonical port only from CVF_MODEL_GATEWAY, never from cvf-web"` | Static-import-graph assertion over `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src` confirming zero imports of any `cvf-web` path alongside the existing `CVF_MODEL_GATEWAY` import precedent. |
| 10 | All terminal receipts share the identity without payload copying | `"GatewayReceipt, MaterialContextManifest, and Sot3ActivationEvidenceRecord all carry the same canonicalExecutionId for one request without duplicating prompt or payload content"` | Run one full canonical Web execution (SOT3 activation plus the subsequent port call); assert all three schemas' identity field values are equal and that none of them contains the raw `prompt`, `systemPrompt`, or any credential-shaped field value (per the identity/receipt-join contract's prohibition). The port alone does not create SOT3 evidence. |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE.

Expected Result / Prediction: current `ProviderExecutionBridge.execute` and
`ProviderExecutionBridgeExecuteOptions` shapes, as verified by T0A, still
support one additive callback field and one unchanged five-stage pre-adapter
sequence at this execution base, with no competing `CanonicalExecutionPort`
symbol already present.

Evidence Comparison: the Current Runtime Freshness Verification section's
direct re-read of `provider-execution-bridge.ts` confirms
`ProviderExecutionBridgeExecuteOptions` still declares exactly the one field
`signal?: AbortSignal`, the five pre-adapter stages remain in the same order
at the cited line numbers, and the `CanonicalExecutionPort|canonicalExecutionId|beforeProviderInvoke`
search over `EXTENSIONS` returns zero files, matching the prediction exactly.

Contradiction Or Gap Disposition: no contradiction was found; no gap remains
open in this document's own scope.

Claim Update: the port design proposed here remains consistent with current
source and with T0A's accepted decisions; this document does not itself
confirm, narrow, or block the root contract, which is the worker return's
role.

## Claim Boundary

This document freezes exact candidate names, field tables, ordering, and
compatibility/rollback rules for `CanonicalExecutionPort` and its supporting
types. It does not implement any of these types, does not modify
`ProviderExecutionBridge`, `unified-gateway-interface-contract.ts`, or any
route/test/package-export file, does not invoke a provider, and does not
authorize T2, MAO launch, or any runtime composition. All named tests in the
Future T2 Deterministic Test-Name Manifest are proposed names and expected
assertions only; no test file exists yet.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation-only contract design; public sync is forbidden
per the governing work order and baseline.
