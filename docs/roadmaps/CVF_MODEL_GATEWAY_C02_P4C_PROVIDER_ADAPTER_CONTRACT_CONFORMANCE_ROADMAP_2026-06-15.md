# CVF Model Gateway C-02 P4C Provider Adapter Contract Conformance Roadmap

Memory class: POINTER_RECORD

rawMemoryReleased: false

Date: 2026-06-15

Status: P4C_DISPATCH_READY

Roadmap class: model-gateway-implementation

## Authorization / Decision

Operator authorization on 2026-06-15 permits Codex to create the provider-
agnostic P4C roadmap, GC-018, and Claude work order. Claude is authorized to
implement only after the dispatch packet passes pre-dispatch gates.

Decision: release P4C deterministic provider adapter conformance; keep P4B-B
live provider proof on hold.

## Purpose

P4B-A closed the provider-neutral `ProviderExecutionBridge`. P4C adds the next
deterministic foundation layer: a provider-agnostic adapter conformance
boundary that validates whether a user-supplied adapter can be admitted to the
bridge contract before any live provider call is considered.

P4C deliberately does not promote Alibaba, DeepSeek, or any current adapter as
canonical. They are current live-run samples only. CVF core controls adapter
contracts, traceability, capability declarations, credential boundaries, and
diagnostics for any provider the operator or user chooses.

## Authority

- Operator instruction: 2026-06-15, create a provider-agnostic work order for
  Claude and do not make Alibaba/DeepSeek the design center.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- P4B-A closure:
  `docs/reviews/CVF_MODEL_GATEWAY_C02_P4B_A_PROVIDER_EXECUTION_BRIDGE_COMPLETION_2026-06-15.md`.
- GC-018:
  `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_2026-06-15.md`.
- Work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_FOR_CLAUDE_2026-06-15.md`.

## Roadmap Decision

P4C is released as a deterministic, no-network implementation tranche. It is
the highest-value next move because it reduces future live-proof risk without
opening P4B-B credential or network scope.

P4B-B remains `HOLD_PENDING_EXPLICIT_LIVE_CREDENTIAL_AUTHORIZATION`.

## Scope

### In Scope

- Add a provider-agnostic conformance helper under
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/`.
- Validate candidate adapter identity against the requested provider.
- Validate provider/model/method capability using current provider method
  contract helpers.
- Return a deterministic conformance report with status, reasons,
  normalized method, supported methods, and execution authorization boundary.
- Keep `liveExecutionAuthorized=false` for every P4C result.
- Add deterministic tests with fake adapters and fake capability records only.
- Add additive barrel exports.
- Add GC-051 entries and regenerate the aggregate.
- Author an uncommitted worker return.

### Out Of Scope

- Live provider calls, `fetch`, HTTP clients, provider URLs, `.env.local`, API
  keys, `resolveSecretForRuntime()`, quota spend, or live-run diagnostics.
- Selecting Alibaba, DeepSeek, or any concrete provider as canonical.
- Modifying existing concrete provider adapters.
- Provider/model addition.
- EPF wiring, Strategy Layer implementation, AI Gateway absorption, public sync,
  production readiness, or public readiness.

## Non-Goals

- Do not select or prefer a provider.
- Do not prove live provider behavior.
- Do not bind a concrete adapter to `ProviderExecutionBridge`.
- Do not implement provider transport.
- Do not change credential, quota, health, routing, or receipt owner behavior.
- Do not promote `MGW-001` beyond `PARTIAL_RECHECK_REQUIRED`.

## Design Control Gate

| Control | P4C decision |
|---|---|
| Scope boundary | provider-agnostic deterministic conformance only |
| Provider binding | forbidden |
| Credential boundary | metadata availability flag only; no secret access |
| Live lane | P4B-B remains hold |
| Existing owner reuse | provider method contract, method gate, capability registry, P4B-A adapter contract |
| Legacy disposition | cite `MGW-001`; no new scan |
| Claim boundary | local deterministic conformance behavior only |

## Provider-Specific Sample Boundary

Alibaba and DeepSeek adapters may be read only as current source examples of
method-specific adapters. They are not source authority for the generic P4C
contract and must not appear as hardcoded accepted providers in the
implementation.

The conformance layer must be BYO-provider compatible: any future adapter can
pass when it satisfies the declared CVF contract.

## Design Contract

The P4C helper should expose a deterministic conformance API. Symbol names are
new implementation symbols and are not pre-existing source claims:

| New symbol | Required role |
|---|---|
| `ProviderAdapterConformanceInput` | candidate adapter, provider/model/method, capability registry, and metadata-only boundary inputs |
| `ProviderAdapterConformanceReport` | deterministic status, reasons, supported methods, normalized method, and authorization fields |
| `ProviderAdapterConformanceStatus` | `conformant` or `blocked` |
| `evaluateProviderAdapterConformance` | pure local conformance evaluator |

The result must never authorize live execution. It may authorize only local
adapter admission to the already governed P4B-A bridge.

## Work Plan

| Step | Owner | Output | Stop condition |
|---|---|---|---|
| 1 | Codex | P4C roadmap, GC-018, work order | pre-dispatch gate failure |
| 2 | Claude | conformance helper and tests | source owner mismatch or forbidden scope |
| 3 | Claude | GC-051 entries and worker return | gate failure outside allowed scope |
| 4 | Codex | review, allowed repair, completion, commit | blocking code or governance finding |
| 5 | Codex | session sync | active-state or generated-state failure |

## Source Verification Table

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Provider-neutral adapter contract exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 25-39 | `ProviderExecutionAdapter` | provider execution bridge | ACCEPT |
| Provider execution bridge exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 55-221 | `ProviderExecutionBridge` | provider execution bridge | ACCEPT |
| Provider method names exist | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | lines 1-10 | `ProviderMethodName` | provider method contract | ACCEPT |
| Capability file shape exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | lines 35-40 | `ProviderCapabilityFile` | provider method contract | ACCEPT |
| Method contract lookup exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | lines 47-76 | `getProviderMethodContract` | provider method gate | ACCEPT |
| Registry method support check exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | lines 78-87 | `assertRegistryProviderMethodSupported` | provider method gate | ACCEPT |
| Method normalization exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts` | lines 25-27 | `normalizeProviderMethodName` | provider method gate | ACCEPT |
| Gateway execute interface exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | lines 75-76 | `UnifiedGatewayInterfaceContract.execute` | unified gateway interface contract | ACCEPT |
| Current static capability registry exists | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | lines 43-98 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| Alibaba source is method-specific sample only | `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/stream-adapter.ts` | lines 28-36 | `createAlibabaQwenTurboStreamAdapter` | Alibaba stream adapter | ACCEPT |
| DeepSeek source is method-specific sample only | `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/deepseek/json-mode-adapter.ts` | lines 28-36 | `createDeepSeekChatJsonModeAdapter` | DeepSeek JSON-mode adapter | ACCEPT |

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row | `MGW-001` |
| Current status | `PARTIAL_RECHECK_REQUIRED` |
| P4C contribution | Adds provider-agnostic adapter conformance before live binding |
| Closure rule | P4C must not promote `MGW-001` to complete |
| P4B-B rule | Live proof remains a separate operator-authorized checkpoint |

No new legacy scan is authorized or required.

## Acceptance Criteria

| ID | Criterion | Evidence |
|---|---|---|
| AC1 | Conformance helper is provider-agnostic and contains no hardcoded accepted provider IDs | source review and tests |
| AC2 | Adapter provider identity mismatch blocks admission | deterministic tests |
| AC3 | Missing provider/model capability blocks admission | deterministic tests |
| AC4 | Unsupported method blocks admission using existing method gate semantics | deterministic tests |
| AC5 | Supported aliases normalize correctly without provider-specific branching | deterministic tests |
| AC6 | Conformant fake adapter returns `adapterExecutionAuthorized=true` and `liveExecutionAuthorized=false` | deterministic tests |
| AC7 | No source/test reads secrets, calls network, imports concrete adapters, or uses provider URLs | negative search |
| AC8 | Type check, full Model Gateway tests, GC-051 drift check, worker fast gate, and diff hygiene pass | command evidence |
| AC9 | Worker leaves HEAD unchanged | base/head evidence |

## Verification

- `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`.
- `npm test -- --run` in `EXTENSIONS/CVF_MODEL_GATEWAY`.
- `python governance/compat/generate_corpus_scan_registry.py --check`.
- `python governance/compat/run_worker_return_fast_gate.py`.
- `git diff --check`.
- Negative search over P4C files for `fetch(`, `http://`, `https://`,
  `.env.local`, API key tokens, `resolveSecretForRuntime`, and concrete adapter
  imports.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance runtime-foundation work. Public sync is not
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-15 P4C dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source inspection, apply_patch, governance gates |
| Target paths | P4C roadmap, GC-018, and Claude work order |
| Allowed scope source | operator instruction 2026-06-15 |
| Before status evidence | HEAD `1baba8c9`; P4B-A closed; P4B-B held |
| After status evidence | P4C dispatch packet ready |
| Diff evidence | pre-dispatch range `1baba8c9..HEAD` |
| Approval boundary | provider-agnostic deterministic conformance only |
| Claim boundary | no live provider, credential use, quota spend, provider preference, or public claim |
| Agent type | Codex orchestrator |
| Invocation ID | `p4c-provider-adapter-conformance-dispatch-2026-06-15` |
| Expected manifest | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_ROADMAP_2026-06-15.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4C_PROVIDER_ADAPTER_CONTRACT_CONFORMANCE_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This roadmap releases only deterministic P4C adapter conformance. It does not
authorize P4B-B, a live provider/API call, credential access, provider/model
addition, provider preference, EPF wiring, Strategy Layer, AI Gateway
absorption, public sync, production readiness, or public readiness.
