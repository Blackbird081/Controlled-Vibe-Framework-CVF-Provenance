# CVF Model Gateway C-02 P4B Governed Provider Execution And Live Proof Roadmap

Memory class: POINTER_RECORD

rawMemoryReleased: false

Date: 2026-06-15

Status: P4B_A_DISPATCH_READY_P4B_B_HOLD

Roadmap class: model-gateway-implementation

## Authorization / Decision

Operator authorization on 2026-06-15 permits Claude to implement the bounded
deterministic P4B-A provider execution bridge under `WORKER_MUST_NOT_COMMIT`.

P4B-B remains `HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION`. This
roadmap does not interpret implementation authorization as permission to read
or consume a provider credential, make a network call, spend quota, or claim
live provider behavior.

GC-018:
`docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_2026-06-15.md`

Work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_A_PROVIDER_EXECUTION_BRIDGE_FOR_CLAUDE_2026-06-15.md`

## Purpose

P4A delivered `UnifiedGatewaySkeletonImpl`, but its execution hook is only an
injected local function. P4B-A adds a governed execution bridge that:

1. accepts an injected provider-execution adapter contract;
2. obtains a routing decision from the existing `RoutingPolicyEngine`;
3. stops on denied, approval-required, no-candidate, health, quota, or missing
   credential metadata conditions;
4. calls the injected adapter only after all existing gates pass;
5. records health and quota outcomes;
6. returns a gateway response plus a `GatewayReceipt` built by the existing
   `GatewayReceiptBuilder`.

P4B-A is deterministic and network-free. It establishes the stable contract
that a later P4B-B live binding may use without embedding provider-specific
transport behavior in the control pipeline.

## Checkpoint Split

| Checkpoint | Status | Scope | Network or credential use |
|---|---|---|---|
| P4B-A | DISPATCH_READY | Injected adapter contract, execution bridge, deterministic tests | Forbidden |
| P4B-B | HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION | Bind one existing provider adapter and run one bounded live proof | Not authorized |

P4B-A may close independently. P4B-B requires a refreshed GC-018, source
verification against the selected provider adapter, explicit operator
authorization for credential use, and the live-run diagnostic standard.

## Scope

### P4B-A In Scope

- Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts`.
- Define the new `ProviderExecutionAdapter` contract in that file.
- Define `ProviderExecutionBridgeOptions` and `ProviderExecutionBridgeResult`.
- Implement `ProviderExecutionBridge.execute(request)`.
- Reuse `RoutingPolicyEngine.decide()`, `CredentialBoundary.resolveMetadata()`,
  `ProviderHealthMonitor`, `QuotaLedger`, and `GatewayReceiptBuilder.build()`.
- Inject adapters by provider ID; tests use local stubs only.
- Update `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` with additive exports.
- Create deterministic tests at
  `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-execution-bridge.test.ts`.
- Add GC-051 source/test entries and regenerate the aggregate.
- Author the worker return.

### P4B-B Held Scope

- Selecting Alibaba, DeepSeek, or another concrete provider binding.
- Calling `resolveSecretForRuntime()`.
- Reading `.env.local` or any provider credential.
- Calling `fetch`, a provider endpoint, or another network surface.
- Authoring a live proof receipt or live-run diagnostic.
- Consuming quota or claiming provider behavior.

### Out Of Scope

- New provider or model registration.
- Changing existing provider adapters.
- Modifying the P4A skeleton.
- EPF wiring, Strategy Layer, AI Gateway absorption, OCR, retrieval, or public
  sync.
- Production or public readiness claims.
- Session-state mutation by the worker.

## Non-Goals

- Implementing a provider transport in P4B-A.
- Replacing existing method-specific provider adapters.
- Proving live routing, provider quality, cost, latency, or availability.
- Completing the Strategy Layer or AI Gateway legacy families.
- Promoting `MGW-001` beyond `PARTIAL_RECHECK_REQUIRED`.

## Design Control Gate

| Control | P4B-A decision |
|---|---|
| Scope boundary | one provider-neutral deterministic bridge |
| Provider binding | injected stub contract only |
| Credential boundary | metadata probe only; runtime secret method forbidden |
| Live lane | P4B-B remains HOLD |
| Existing owner reuse | routing engine, health, quota, credential metadata, receipt builder |
| Legacy disposition | cite `MGW-001`; no new scan |
| Claim boundary | local deterministic behavior only |

## Design Contract

The following symbols are new P4B-A runtime symbols and are not represented as
pre-existing Source Verification `ACCEPT` rows:

| New symbol | Required shape |
|---|---|
| `ProviderExecutionAdapter` | `providerId` plus `execute(input)` returning text and optional token usage |
| `ProviderExecutionAdapterInput` | trace ID, selected provider/model, prompt, optional system prompt and metadata |
| `ProviderExecutionAdapterResult` | text plus optional input/output token counts |
| `ProviderExecutionBridgeOptions` | routing engine, credential boundary, health monitor, quota ledger, receipt builder, credential references, adapter map |
| `ProviderExecutionBridgeResult` | gateway response or shielded error envelope plus `GatewayReceipt` |
| `ProviderExecutionBridge` | deterministic `execute(GatewayExecuteRequest)` orchestration |

The bridge must not import either existing method-specific provider adapter.
Alibaba currently exposes `stream()` and DeepSeek currently exposes
`jsonMode()`; neither is a source-backed common execute contract.

## Execution Sequence

1. Build a `RoutingRequest` from the `GatewayExecuteRequest`.
2. Call `RoutingPolicyEngine.decide()`.
3. For `denied`, `requires_approval`, or `no_candidate`, build a corresponding
   receipt and return without adapter invocation.
4. For `selected`, verify that an injected adapter exists for the selected
   provider.
5. Resolve credential metadata only. P4B-A must not call
   `resolveSecretForRuntime()`.
6. If credential metadata is unavailable, return a shielded
   `credential_shielded` error and receipt.
7. Invoke the local injected adapter.
8. On success, call `recordSuccess()` and `recordUse()`, then build a selected
   receipt and response.
9. On adapter error, call `recordFailure()`, build a shielded internal-error
   receipt, and do not leak provider error bodies or credentials.

## Work Plan

| Step | Owner | Output | Stop condition |
|---|---|---|---|
| 1 | Codex | corrected roadmap, GC-018, work order | machine pre-dispatch failure |
| 2 | Claude | bridge contract and implementation | existing owner mismatch or forbidden scope |
| 3 | Claude | deterministic tests and additive exports | network or concrete adapter required |
| 4 | Claude | GC-051 entries and worker return | gate failure outside allowed scope |
| 5 | Codex | review, completion, material commit | blocking code or governance finding |
| 6 | Codex | session sync | active-state or generated-state failure |

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Gateway execute request and response shapes exist | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | lines 26-42 | `GatewayExecuteRequest` | unified gateway interface contract | ACCEPT |
| Shielded gateway error shape exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | lines 8-24 | `GatewayErrorEnvelope` | unified gateway interface contract | ACCEPT |
| Existing routing owner returns selected or stopped decisions | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | lines 82-178 | `RoutingPolicyEngine` | routing policy engine | ACCEPT |
| Routing entry method exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | lines 90-167 | `decide` | `RoutingPolicyEngine` | ACCEPT |
| Credential metadata probe exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | lines 21-31 | `resolveMetadata` | `CredentialBoundary` | ACCEPT |
| Runtime secret method exists but is held from P4B-A | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | lines 33-35 | `resolveSecretForRuntime` | `CredentialBoundary` | ACCEPT |
| Health success and failure recording exist | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | lines 32-57 | `recordSuccess` | `ProviderHealthMonitor` | ACCEPT |
| Quota precheck exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | lines 52-77 | `canUse` | `QuotaLedger` | ACCEPT |
| Quota usage recording exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | lines 79-89 | `recordUse` | `QuotaLedger` | ACCEPT |
| Receipt builder exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | lines 59-115 | `GatewayReceiptBuilder` | gateway receipt builder | ACCEPT |
| Receipt construction method exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | lines 65-92 | `build` | `GatewayReceiptBuilder` | ACCEPT |
| Alibaba adapter is stream-specific | `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts` | lines 28-73 | `createAlibabaQwenTurboStreamAdapter` | Alibaba stream adapter factory | ACCEPT |
| DeepSeek adapter is JSON-mode-specific | `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/json-mode-adapter.ts` | lines 28-70 | `createDeepSeekChatJsonModeAdapter` | DeepSeek JSON-mode adapter factory | ACCEPT |

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P4B-A contribution | Adds the governed provider execution bridge only |
| Closure rule | P4B-A must not promote `MGW-001` to complete |
| P4B-B rule | Reassess `MGW-001` only after an authorized live binding closes; Strategy Layer and AI Gateway deferrals remain independent |

No new legacy scan is authorized or required. The bounded Model Gateway legacy
recheck and `RESUME_WITH_REWRITE` decision remain the source of disposition.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | New adapter contract is provider-neutral and injected | source review and compile check |
| AC2 | Routing stopped decisions never invoke an adapter | deterministic tests |
| AC3 | Missing adapter or credential metadata fails shielded | deterministic tests |
| AC4 | Adapter invocation occurs only after routing, health/quota, and credential metadata checks | ordered call assertions |
| AC5 | Success records health/quota and emits selected receipt | deterministic tests |
| AC6 | Adapter failure records health failure and emits shielded receipt/error | deterministic tests |
| AC7 | No source or test uses `fetch`, provider URL, real key, `.env.local`, or `resolveSecretForRuntime()` | negative search |
| AC8 | Type check, full module tests, GC-051 drift check, and reviewer-fast pass | command evidence |
| AC9 | Worker leaves HEAD unchanged | base/head evidence |

## Verification

- `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`.
- `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY`.
- `python governance/compat/generate_corpus_scan_registry.py --check`.
- `python governance/compat/run_worker_return_fast_gate.py`.
- `git diff --check`.
- Negative search for `fetch(`, provider endpoints, key literals,
  `.env.local`, and `resolveSecretForRuntime` in P4B-A files.

## Risk And Corrective Action

| Risk | Control |
|---|---|
| Worker invents a common shape from method-specific adapters | New provider-neutral injected contract is specified explicitly |
| P4B-A silently consumes secrets | Only `resolveMetadata()` allowed; runtime secret resolution is forbidden |
| Provider call occurs during tests | No existing concrete adapter import; local stub only |
| Receipt missing on stopped/error path | Result contract always includes a receipt |
| Quota is recorded before successful execution | `recordUse()` occurs only after adapter success |
| Roadmap is mistaken for live authorization | P4B-B remains HOLD and requires fresh operator authorization |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: this is private provenance runtime-foundation work. Public sync is not
authorized.

## Machine Closure Package

| Closure item | Required evidence | Current status |
|---|---|---|
| P4B-A work order | source-verified dispatched work order | READY |
| Worker return | no-commit return with exact changed set | PENDING |
| Completion review | Codex review after worker return | PENDING |
| P4B-B | explicit operator and credential authorization | HOLD |
| MGW-001 | remains `PARTIAL_RECHECK_REQUIRED` | REQUIRED |
| Public sync | N/A with reason: not authorized | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 P4B-A dispatch repair |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source inspection, apply_patch, governance gates |
| Target paths | P4B roadmap, GC-018, P4B-A work order |
| Allowed scope source | operator instruction 2026-06-15 |
| Before status evidence | Claude draft present and uncommitted at HEAD `55e4a829` |
| After status evidence | corrected P4B-A dispatch packet |
| Diff evidence | material commit range and pre-dispatch gates |
| Approval boundary | P4B-A deterministic implementation only |
| Claim boundary | no live provider, credential use, quota spend, or public claim |
| Agent type | Codex orchestrator |
| Invocation ID | `p4b-a-dispatch-repair-2026-06-15` |
| Expected manifest | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_A_PROVIDER_EXECUTION_BRIDGE_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4B_GOVERNED_PROVIDER_EXECUTION_AND_LIVE_PROOF_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4B_A_PROVIDER_EXECUTION_BRIDGE_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This roadmap releases P4B-A only. It does not authorize P4B-B, any provider
API call, credential access, quota consumption, provider/model addition, EPF
wiring, Strategy Layer, AI Gateway absorption, public sync, or readiness claim.
