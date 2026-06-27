# CVF Model Gateway C-02 P3 Unified Gateway Interface Roadmap - 2026-06-15

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-15

Owner: Operator

Authorized by: Operator instruction 2026-06-15 (SINGLE_AGENT_MULTI_ROLE pattern
authorized; Claude soans roadmap P3 -> GC-018 -> work order -> thi cong)

rawMemoryReleased=false

---

## Purpose

Define the P3 roadmap tranche for Model Gateway C-02: Unified Gateway Interface.
P2 delivered the Dynamic Model Registry contract boundary. P3 unifies the
existing fragment contracts (`stream-contract.ts`, `embedding-contract.ts`,
`provider-health.ts`, `gateway-policy.ts`) into a single governed entry-point
interface boundary with standard error envelope and credential-shielding
declaration, so that future P4 implementation and EPF integration have a stable
contract surface to reference.

---

## Why P3 After P2

P2 defined what a Dynamic Model Registry owns versus the two static registries.
The remaining gap is the **entry point**: there is no single interface that
governs how callers invoke `execute`, `stream`, `embedding`, or `health` against
the gateway. Currently:

| Fragment | File | Gap |
|---|---|---|
| `StreamCapableProvider` | `stream-contract.ts` 35L | No unified caller entry, no error envelope |
| `EmbeddingCapableProvider` | `embedding-contract.ts` 38L | No unified caller entry, no error envelope |
| `ProviderHealthMonitor` | `provider-health.ts` 74L | Runtime class, not an interface contract |
| `GatewayPolicyContext` | `gateway-policy.ts` 18L | Policy context only, not a dispatch contract |

P3 fixes this by defining a single `UnifiedGatewayInterfaceContract` that:

1. Declares the four method signatures (`execute`, `stream`, `embedding`, `health`).
2. Declares a standard `GatewayErrorEnvelope` with error class and shielding markers.
3. Declares `GatewayExecuteRequest` / `GatewayExecuteResponse` types that reuse
   existing P1 `RoutingRequest` fields and P2 `DynamicModelRecord` types by import.
4. Stays doc/contract-first -- no runtime class, no provider call.

---

## Scope

### In scope (doc/contract only)

- New contract file `unified-gateway-interface-contract.ts` -- interfaces and
  type aliases only, no runtime implementation.
- New type declarations: `GatewayExecuteRequest`, `GatewayExecuteResponse`,
  `GatewayStreamRequest`, `GatewayStreamChunk`, `GatewayEmbeddingRequest`,
  `GatewayEmbeddingResponse`, `GatewayHealthResponse`, `GatewayErrorEnvelope`,
  `GatewayErrorClass`, `UnifiedGatewayInterfaceContract`.
- Reuse by import: `RoutingRequest` (P1, `routing-policy.ts`),
  `DynamicModelRecord` (P2, `dynamic-model-registry-contract.ts`),
  `GatewayPolicyContext` (`gateway-policy.ts`),
  `ProviderHealthState` (`provider-health.ts`).
- Barrel export additions to `index.ts`.
- Boundary definition document stating what each fragment contract covers versus
  what the unified interface contract adds.
- Type-level tests (compile-time only; no network, no provider, no runtime).
- GC-051 registry entries for new source and test files.
- GC-018 baseline (this tranche).
- Work order + worker return + completion review.

### Explicitly out of scope

- Runtime implementation of `UnifiedGatewayInterface` class.
- Provider/API calls, live proof, network requests.
- Mutation of `stream-contract.ts`, `embedding-contract.ts`, `provider-health.ts`,
  `gateway-policy.ts`, `routing-policy.ts`, `provider-registry.ts`,
  `provider-capability-registry.ts`, or `dynamic-model-registry-contract.ts`.
- EPF integration wiring (separate tranche).
- Strategy Layer (Planner, Taxonomy, Feedback Loop) -- deferred.
- AI Gateway family absorption -- `DEFERRED_PRIVATE_ONLY` per LHW17 T2.
- Public-sync -- not authorized for this tranche.

---

## Tranche Sequence

| Tranche | Scope | Status |
|---|---|---|
| C-02 Rewrite Planning | 3-layer / 5-component boundary rewrite plan | `CLOSED_PASS_BOUNDED` 2026-06-14 |
| C-02 P1 Routing Pipeline | Routing context, pluggable pipeline, snapshot fields | `CLOSED_PASS_BOUNDED` 2026-06-14 |
| C-02 P2 Dynamic Model Registry Boundary | DMR contract + boundary doc + type tests | `CLOSED_PASS_BOUNDED` 2026-06-15 |
| **C-02 P3 Unified Gateway Interface** | **Unified entry-point contract + boundary doc + type tests (this tranche)** | `CLOSED_PASS_BOUNDED` |
| C-02 P4 Implementation (TBD) | Runtime DMR class + UnifiedGatewayInterface class | `PARKED` -- after P3; requires separate GC-018 |

---

## Current Source Baseline

All files re-read 2026-06-15 at HEAD `c6c09ae3`.

| File | Lines | Role in P3 |
|---|---|---|
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` | 35 | Fragment; `StreamRequest`, `StreamContract`, `StreamCapableProvider` -- retained fragment authority, reference only |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/embedding-contract.ts` | 38 | Fragment; `EmbeddingRequest`, `EmbeddingContract`, `EmbeddingCapableProvider` -- retained fragment authority, reference only |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | 74 | `ProviderHealthState`, `ProviderHealthRecord` -- reuse by import |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | 18 | `GatewayPolicyContext`, `GatewayPolicyResult` -- reuse by import |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | 204 | P1 `RoutingRequest` -- reuse by import |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | 37 | P2 `DynamicModelRecord`, `ModelTier` -- reuse by import |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | 290 | Barrel; P3 adds contract exports |

---

## Contract Design Sketch (advisory -- worker refines at dispatch)

### `GatewayErrorClass`

```typescript
export type GatewayErrorClass =
  | "policy_denied"
  | "no_candidate"
  | "quota_exceeded"
  | "provider_unavailable"
  | "invalid_request"
  | "credential_shielded"
  | "internal_error";
```

### `GatewayErrorEnvelope`

```typescript
export interface GatewayErrorEnvelope {
  errorClass: GatewayErrorClass;
  traceId: string;
  message: string;
  credentialShielded: true;
  providerIdShielded?: true;
  retryable: boolean;
}
```

### `GatewayExecuteRequest`

```typescript
export interface GatewayExecuteRequest {
  traceId: string;
  prompt: string;
  systemPrompt?: string;
  policy: GatewayPolicyContext;          // reuse gateway-policy.ts
  routing?: RoutingRequest;              // reuse routing-policy.ts (P1)
  preferredModel?: DynamicModelRecord;   // reuse dynamic-model-registry-contract.ts (P2)
  metadata?: Record<string, unknown>;
}
```

### `GatewayExecuteResponse`

```typescript
export interface GatewayExecuteResponse {
  traceId: string;
  text: string;
  usage?: { inputTokens: number; outputTokens: number };
  receiptObligation?: string;
  model?: { providerId: string; modelId: string };
}
```

### `GatewayStreamRequest` / `GatewayStreamChunk`

```typescript
export interface GatewayStreamRequest extends GatewayExecuteRequest {}

export interface GatewayStreamChunk {
  traceId: string;
  chunk: string;
  done: boolean;
  receiptObligation?: string;
}
```

### `GatewayEmbeddingRequest` / `GatewayEmbeddingResponse`

```typescript
export interface GatewayEmbeddingRequest {
  traceId: string;
  input: string | string[];
  model?: string;
  policy: GatewayPolicyContext;
  metadata?: Record<string, unknown>;
}

export interface GatewayEmbeddingResponse {
  traceId: string;
  embeddings: number[][];
  dimensions: number;
  receiptObligation?: string;
}
```

### `GatewayHealthResponse`

```typescript
export interface GatewayHealthResponse {
  traceId: string;
  status: "ok" | "degraded" | "unavailable";
  providerHealthSummary?: Record<string, ProviderHealthState>; // reuse provider-health.ts
  checkedAt: string;
}
```

### `UnifiedGatewayInterfaceContract`

```typescript
export interface UnifiedGatewayInterfaceContract {
  execute(request: GatewayExecuteRequest): Promise<GatewayExecuteResponse | GatewayErrorEnvelope>;
  stream(request: GatewayStreamRequest): AsyncIterable<GatewayStreamChunk | GatewayErrorEnvelope>;
  embedding(request: GatewayEmbeddingRequest): Promise<GatewayEmbeddingResponse | GatewayErrorEnvelope>;
  health(traceId: string): Promise<GatewayHealthResponse>;
}
```

---

## Deliverables

| # | Artifact | Path | Owner |
|---|---|---|---|
| D1 | GC-018 baseline | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_2026-06-15.md` | Orchestrator |
| D2 | Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_FOR_CLAUDE_2026-06-15.md` | Orchestrator |
| D3 | Unified gateway contract file | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | Worker |
| D4 | Boundary definition doc | `docs/reference/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_BOUNDARY_DEFINITION_2026-06-15.md` | Worker |
| D5 | Type-level tests | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-interface-contract.test.ts` | Worker |
| D6 | GC-051 registry entries | `docs/corpus-intelligence/registry/entries/model-gateway-c02-p3-*.json` | Worker |
| D7 | Worker return | `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_WORKER_RETURN_2026-06-15.md` | Worker |
| D8 | Completion review | `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_COMPLETION_2026-06-15.md` | Reviewer |

---

## Execution Gates

| Gate | Condition | Blocks |
|---|---|---|
| G1 | Fresh GC-018 issued | Work order dispatch |
| G2 | Source verification of all reused types in work order | Worker execution |
| G3 | Contract file is types-only -- no class body, no `new`, no runtime logic | Completion review |
| G4 | Type-level tests compile and pass (`npm test` in `CVF_MODEL_GATEWAY`) | Completion review |
| G5 | GC-051 entries created for D3 and D5 | Closure |
| G6 | No mutation of any existing source file | Completion review |
| G7 | `rawMemoryReleased=false` on all closure artifacts | Handoff |

---

## Acceptance Criteria

| # | Criterion | Gate |
|---|---|---|
| AC1 | `unified-gateway-interface-contract.ts` contains only interfaces and types -- no class body, no `new`, no runtime logic | G3 |
| AC2 | All existing fragment contracts (`stream-contract.ts`, `embedding-contract.ts`, `provider-health.ts`, `gateway-policy.ts`, `routing-policy.ts`, `dynamic-model-registry-contract.ts`) are unchanged | G6 |
| AC3 | Contract reuses `GatewayPolicyContext`, `RoutingRequest`, `DynamicModelRecord`, `ProviderHealthState` by import | G2 |
| AC4 | Type-level tests compile and pass | G4 |
| AC5 | Boundary definition doc explicitly states what each fragment covers vs. what the unified contract adds | D4 |
| AC6 | `rawMemoryReleased=false` on all closure artifacts | G7 |
| AC7 | No live provider calls, network traffic, or API keys used | G3 |

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance planning roadmap. Public-sync not authorized.

---

## Roadmap Closure Reconciliation - 2026-06-27

This roadmap top status was reconciled by the roadmap status reconciliation
sweep after existing closure evidence showed P3 had already closed.

| Item | Evidence | Disposition |
|---|---|---|
| P3 completion review | `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_COMPLETION_2026-06-15.md` | `Status: CLOSED_PASS_BOUNDED` |
| P3 material implementation | commit `5d46bc62` | CLOSED_PASS_BOUNDED |
| P3/P4A closure sync | commit `21c8a9e2` | CLOSED_PASS_BOUNDED |
| Session state closure entry | `CVF_SESSION/state/entries/modelGatewayC02P3P4AUnifiedGatewayClosure20260615.json` | `status: CLOSED_PASS_BOUNDED` |

Reconciliation boundary: status evidence only. No P3 implementation,
provider/live proof, public-sync, resolver, adapter, or generated corpus
registry mutation occurs in this sweep.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_FOR_CLAUDE_2026-06-15.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_COMPLETION_2026-06-15.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | P3 registry coverage existed before this sweep | PASS |
| Registry Markdown | N/A with reason: no roadmap-local Markdown registry mutation in this sweep | no Markdown registry change in this sweep | BLOCKED with reason: out of scope |
| External evidence digest | N/A with reason: repo-local governed closure artifacts only | no external digest | N/A with reason |
| System loop interlock | N/A with reason: no system-loop mutation | no system-loop path in changed set | N/A with reason |
| Session continuity | active front door/state/handoff after material commit | session-sync follows material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| P3-ROADMAP-STATUS | this roadmap | top-level `Status:` | CLOSED_PASS_BOUNDED | CLOSED_PASS_BOUNDED | PASS |
| P3-COMPLETION | P3 completion review | top-level `Status:` | CLOSED_PASS_BOUNDED | CLOSED_PASS_BOUNDED | PASS |
| P3-STATE-ENTRY | active session state source | `value.status` | CLOSED_PASS_BOUNDED | CLOSED_PASS_BOUNDED | PASS |

---

## Authorization And Decision

Authority: Operator instruction 2026-06-15 (SINGLE_AGENT_MULTI_ROLE pattern
authorized). P2 `CLOSED_PASS_BOUNDED` at commit `24d455f8`.

Decision: proceed with P3 doc/contract-first boundary definition only.
No implementation, runtime mutation, live provider, or public-sync
is authorized by this roadmap.

Prior planning authority:
- `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md`
  (section 9, `gatewayUnifiedInterfaceBoundary`, `INCLUDE_IN_BOUNDARY`)
- `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_2026-06-15.md`

---

## Non-Goals

- Runtime implementation of `UnifiedGatewayInterface` class (class body,
  execute/stream/embedding/health runtime logic) -- deferred, requires
  separate implementation GC-018.
- Mutation of `stream-contract.ts`, `embedding-contract.ts`, `provider-health.ts`,
  `gateway-policy.ts`, `routing-policy.ts`, `dynamic-model-registry-contract.ts`,
  `provider-capability-registry.ts`, or `provider-registry.ts`.
- Live provider API calls, pricing lookups, or health-check network traffic.
- Strategy Layer components (Planner, Taxonomy, Feedback Loop).
- AI Gateway family absorption -- `DEFERRED_PRIVATE_ONLY` per LHW17 T2.
- Public-sync or external repo mutation.
- EPF integration wiring (separate tranche).

---

## Work Plan

| Step | Action | Prerequisite |
|---|---|---|
| W1 | Issue GC-018 for C-02 P3 | Roadmap approved |
| W2 | Author source-verified work order | GC-018 issued |
| W3 | Worker reads current source baseline | Work order dispatched |
| W4 | Worker authors `unified-gateway-interface-contract.ts` (types only) | Step W3 |
| W5 | Worker authors boundary definition doc | Step W4 |
| W6 | Worker adds type-level tests | Step W4 |
| W7 | Worker adds GC-051 registry entries | Step W4 |
| W8 | Worker authors worker return | Steps W4-W7 |
| W9 | Reviewer inspects diff, repairs if needed, authors completion review | Step W8 |
| W10 | Commit closure | Step W9 |

---

## Current Runtime Freshness Verification

Symbols verified at HEAD `c6c09ae3` on 2026-06-15.

| Surface | Freshness check | Expected |
|---|---|---|
| GatewayPolicyContext | `rg -n "GatewayPolicyContext" EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | found at line 3 |
| ProviderHealthState | `rg -n "ProviderHealthState" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | found at line 1 |
| RoutingRequest | `rg -n "RoutingRequest" EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | found at line 14 |
| DynamicModelRecord | `rg -n "DynamicModelRecord" EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | found at line 13 |

---

## Verification And Evidence

Pre-closure autorun gate:

```sh
python governance/compat/run_agent_autorun_workflow_gate.py \
  --phase pre-closure --base c6c09ae3 --head HEAD
```

Must PASS on material closure commit range before completion review can
declare ACCEPT.

Pre-commit hook runs automatically at every `git commit`.

Closure is `CLOSED_PASS_BOUNDED` when completion review disposition is ACCEPT,
pre-closure autorun gate PASSes on the material range, and pre-commit hook
PASSes on the closure commit.

---

## Claim And Verification Boundary

This roadmap is a planning artifact only. It does not claim:

- Runtime behavior of any existing or future `UnifiedGatewayInterface` class.
- That the P3 contract file contains any runtime implementation.
- Production readiness, hosted readiness, or public readiness.
- Provider or API call behavior.

Evidence of types-only constraint is in `git diff` of
`unified-gateway-interface-contract.ts`: no class body, no `new`, no runtime
statement beyond declarations and one optional literal version constant.

---

## Design Control Gate

Dispatch boundary: worker may not begin until GC-018 is issued and a
source-verified work order names current line ranges for all reused types.

Protected surfaces during P3 (READ ONLY):

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/embedding-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`

Additive-only surfaces:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` (NEW)
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-interface-contract.test.ts` (NEW)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (EDIT -- barrel only)
- `docs/reference/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_BOUNDARY_DEFINITION_2026-06-15.md` (NEW)

---

## Next Allowed Move After P3 Closure

After P3 is `CLOSED_PASS_BOUNDED`:

- **C-02 P4 Implementation** -- runtime `DynamicModelRegistry` class implementing
  `DynamicModelRegistryContract` AND runtime `UnifiedGatewayInterface` class
  implementing `UnifiedGatewayInterfaceContract`; requires fresh GC-018.
- **EPF integration wiring** -- separate tranche, separate GC-018.

All P4 work requires fresh operator authorization, fresh GC-018, and a
source-verified work order naming both P2 and P3 contracts as authority.
