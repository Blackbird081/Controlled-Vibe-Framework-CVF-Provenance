# CVF Model Gateway C-02 P2 Dynamic Model Registry Boundary Roadmap - 2026-06-15

Memory class: FULL_RECORD

Status: ROADMAP_READY

docType: roadmap

Date: 2026-06-15

Owner: Operator

Authorized by: Operator instruction 2026-06-15

---

## Purpose

Define the P2 roadmap tranche for Model Gateway C-02: Dynamic Model Registry
Boundary. This tranche separates the current static
`PROVIDER_CAPABILITY_REGISTRY` / `ProviderRegistry` surfaces from the future
dynamic model registry design, and produces a doc/contract-first boundary
artifact that enables P3 (Unified Gateway Interface) and any subsequent
provider/live routing work to reference a governed registry contract.

---

## Why P2 Before P3

P1 delivered routing context fields and a pluggable routing-policy pipeline.
The pipeline can now accept policy decisions, but the source of truth for
which providers and models exist -- their tier, capability, health/performance
state, pricing/cost, limits, and status -- is split across two static surfaces:

| Surface | File | What it covers | Gap |
| --- | --- | --- | --- |
| `PROVIDER_CAPABILITY_REGISTRY` | `provider-capability-registry.ts` | Static method-capability table per provider | No tier, no cost, no health query, no findOptimal |
| `ProviderRegistry` | `provider-registry.ts` | Runtime provider store, `isRoutable`, `assertAllowed` | No tier model, no findOptimal, no static+runtime merge |

Without a governed boundary for what a Dynamic Model Registry owns, P3's
unified gateway interface (`execute/stream/embedding/health`) becomes a
facade over an undefined backend. P2 fixes that by:

1. Naming the boundary explicitly (what DMR owns vs. what current registries keep).
2. Defining the contract shape (`DynamicModelRecord`, `ModelTier`, `findOptimal`).
3. Specifying the merge strategy (static capability table + runtime health state).
4. Keeping implementation deferred until operator authorizes a fresh GC-018
   pointing at the contract produced here.

---

## Scope

### In scope (doc/contract only)

- Boundary definition document: what Dynamic Model Registry owns, what it does
  not own, and where the current static registries remain authoritative.
- TypeScript contract file (`dynamic-model-registry-contract.ts`) -- interfaces
  and type definitions only, no runtime implementation.
- Source Verification Table referencing current `provider-capability-registry.ts`
  and `provider-registry.ts` line ranges.
- Focused tests for the contract shapes (type-level / compile-time only;
  no live provider calls, no network).
- GC-051 corpus scan registry entry for the new contract file.
- GC-018 baseline for this P2 tranche.
- Worker return + completion review.

### Explicitly out of scope

- Live provider calls, API keys, network requests.
- Implementation of `DynamicModelRegistry` class (execution logic, findOptimal
  runtime, health-poll loop) -- requires a separate implementation GC-018.
- Strategy Layer (Planner, Taxonomy, Feedback Loop) -- deferred, separate GC-018.
- AI Gateway family absorption -- `DEFERRED_PRIVATE_ONLY` per LHW17 T2.
- Public-sync -- not authorized for this tranche.
- `ProviderRegistry` mutation or `PROVIDER_CAPABILITY_REGISTRY` mutation.
- Routing-Policy-Engine pluggable pipeline changes (P1 closed; P2 does not
  re-open P1 scope).
- Unified Gateway Interface boundary (P3 scope).

---

## Tranche Sequence

| Tranche | Scope | Status |
| --- | --- | --- |
| C-02 Rewrite Planning | 3-layer / 5-component boundary rewrite plan, boundary disposition matrix | `CLOSED_PASS_BOUNDED` 2026-06-14 |
| C-02 P1 Routing Pipeline | Routing context fields, pluggable policy pipeline, snapshot fields, focused tests | `CLOSED_PASS_BOUNDED` 2026-06-14 |
| **C-02 P2 Dynamic Model Registry Boundary** | **DMR boundary doc + contract file + type tests + GC-018 (this tranche)** | `ROADMAP_READY` |
| C-02 P3 Unified Gateway Interface | `execute/stream/embedding/health` interface boundary | `PARKED` -- after P2 closure |
| C-02 P4 Implementation (TBD) | Runtime `DynamicModelRegistry` impl, `findOptimal` | `PARKED` -- requires separate GC-018 after P3 |

---

## Current Source Baseline

Both files must be re-read at dispatch time; line numbers below are current
as of 2026-06-15.

| File | Lines | Role in P2 |
| --- | --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | 98 | Static capability table; P2 boundary must clarify what DMR supersedes here |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | 113 | Runtime provider store; P2 boundary must clarify what DMR extends here |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | 206 | P1 routing context; P2 contract must be compatible with `RoutingRequest` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy-pipeline.ts` | 257 | P1 pipeline; P2 contract is consumed by pipeline, not changed |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | -- | Health record surface; P2 must reconcile `ProviderHealthRecord` with DMR health fields |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | -- | Barrel; P2 adds contract export |

---

## Contract Design Sketch (advisory -- worker refines at dispatch)

### `ModelTier`

```typescript
export type ModelTier = "frontier" | "standard" | "economy" | "experimental";
```

Rationale: tier is the primary dimension for `findOptimal` routing when cost
or capability budgets are specified. Frontier = highest capability / cost;
economy = lowest cost; experimental = gated by `allowExperimental` flag
(mirrors existing `ProviderRegistry` pattern).

### `DynamicModelRecord`

```typescript
export interface DynamicModelRecord {
  providerId: string;
  modelId: string;
  tier: ModelTier;
  supportedMethods: ProviderMethodName[];        // re-uses P1 contract type
  maxContextTokens?: number;
  costPerInputToken?: number;                    // normalized unit -- no live pricing
  costPerOutputToken?: number;
  latencyClass?: "low" | "medium" | "high";
  rateLimit?: { requestsPerMinute: number; tokensPerMinute?: number };
  healthStatus?: "healthy" | "degraded" | "unavailable";
  status: ProviderStatus;                        // re-uses provider-registry.ts type
}
```

### `FindOptimalQuery`

```typescript
export interface FindOptimalQuery {
  requiredMethod: ProviderMethodName;
  preferredTier?: ModelTier;
  maxCostPerInputToken?: number;
  latencyClass?: "low" | "medium" | "high";
  allowExperimental?: boolean;
  allowedProviderIds?: string[];
  blockedProviderIds?: string[];
}
```

### `DynamicModelRegistryContract`

```typescript
export interface DynamicModelRegistryContract {
  /** Look up a single record -- undefined if not registered or not routable. */
  getModel(providerId: string, modelId: string): DynamicModelRecord | undefined;

  /** Return all records matching the query constraints, ordered by tier preference. */
  findOptimal(query: FindOptimalQuery): DynamicModelRecord[];

  /** All routable records (status != "disabled", respects allowExperimental). */
  listRoutable(options?: { allowExperimental?: boolean }): DynamicModelRecord[];
}
```

### Merge Strategy Boundary

The contract document must state:

- `PROVIDER_CAPABILITY_REGISTRY` remains authoritative for method-capability
  validation (`supportedMethods` truth source at deploy time).
- `ProviderRegistry` remains authoritative for runtime routable-provider
  decisions (`isRoutable`, `assertAllowed`).
- `DynamicModelRegistry` (future implementation) merges both: static capability
  facts + runtime health state + tier/cost/latency metadata.
- No mutation of either existing surface is authorized in P2.

---

## Deliverables

| # | Artifact | Path | Owner |
| --- | --- | --- | --- |
| D1 | GC-018 baseline | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md` | Operator/reviewer |
| D2 | Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md` | Reviewer |
| D3 | DMR contract file | `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | Worker |
| D4 | Boundary definition doc | `docs/reference/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_DEFINITION_2026-06-15.md` | Worker |
| D5 | Type-level tests | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/dynamic-model-registry-contract.test.ts` | Worker |
| D6 | GC-051 registry entry | `docs/corpus-intelligence/registry/entries/model-gateway-c02-p2-dynamic-model-registry-contract.json` | Worker |
| D7 | Worker return | `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_WORKER_RETURN_2026-06-15.md` | Worker |
| D8 | Completion review | `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_COMPLETION_2026-06-15.md` | Reviewer |

---

## Execution Gates

| Gate | Condition | Blocks |
| --- | --- | --- |
| G1 | Fresh GC-018 issued and signed | Work order dispatch |
| G2 | Source Verification Table in work order names current line ranges in `provider-capability-registry.ts` and `provider-registry.ts` | Worker execution |
| G3 | Contract file is types-only -- no class body, no runtime logic, no `new` calls | Completion review |
| G4 | Type-level tests compile and pass with `npm test` in `CVF_MODEL_GATEWAY` | Completion review |
| G5 | GC-051 entry created for D3 | Closure |
| G6 | No mutation of `provider-capability-registry.ts`, `provider-registry.ts`, or any P1 file | Completion review |
| G7 | `rawMemoryReleased=false` on all closure artifacts | Handoff |

---

## Next Allowed Move After P2 Closure

After P2 is `CLOSED_PASS_BOUNDED`:

- **C-02 P3 Unified Gateway Interface** -- boundary definition for
  `execute/stream/embedding/health`; cites P2 contract as input.
- **C-02 P4 Implementation** (separate operator decision) -- runtime
  `DynamicModelRegistry` class implementing `DynamicModelRegistryContract`;
  requires fresh GC-018 naming this roadmap as planning authority.

All P3/P4 work requires fresh operator authorization, fresh GC-018, and a
source-verified work order. This roadmap does not pre-authorize either.

---

## Parked Lanes (unchanged from V18 handoff)

1. Live Redis proof -- `PARKED_PENDING_CREDENTIALS`
2. DEP2 next-auth -- `HARD_BLOCKED`
3. External receipt-anchor provider -- `PARKED_PENDING_OPERATOR_DECISION`
4. AI Gateway family absorption -- `PARKED_PENDING_PRIVACY_OPERATOR_AUTHORIZATION`
5. Strategy Layer implementation -- `DEFERRED_REQUIRES_SEPARATE_GC018`

---

## Legacy Value Key Traceability

Key `dynamicModelRegistryWithHealthMonitoring` from
`docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md`
(row 10 in the accepted value map,
`docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md`
line 180):

> `INCLUDE_IN_BOUNDARY` (advisory: distinguish static registry from future
> dynamic registry; recommend boundary definition in next tranche)

This tranche fulfills that advisory recommendation as a doc/contract-first
boundary definition. It does not fulfill the implementation requirement --
that remains `DEFERRED_REQUIRES_SEPARATE_GC018`.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance planning roadmap. Public-sync is not authorized by
this document or the operator instruction that authorizes it.

---

## Authorization

Authority: Operator instruction 2026-06-15. This roadmap is authorized for
doc/contract-first planning work only. No implementation, runtime mutation,
live provider, or public-sync is authorized by this document.

Prior planning authority that this tranche extends:

- Rewrite plan: `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md`
- GC-018 (P1): `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_2026-06-14.md`

Fresh GC-018 for P2 is required before any work order is dispatched.

---

## Non-Goals

- Runtime implementation of `DynamicModelRegistry` (class body, query execution,
  health-poll scheduling) -- deferred, requires separate implementation GC-018.
- Mutation of `PROVIDER_CAPABILITY_REGISTRY` or `ProviderRegistry`.
- Live provider API calls, pricing lookups, or health-check network traffic.
- Strategy Layer components (Planner, Taxonomy, Feedback Loop).
- AI Gateway family absorption.
- Public-sync or external repo mutation.
- Unified Gateway Interface implementation (P3 scope).

---

## Design Control Gate

Dispatch boundary: worker may not begin until GC-018 is issued and a
source-verified work order names current line ranges in
`provider-capability-registry.ts` and `provider-registry.ts`.

Protected surfaces during P2:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` -- READ ONLY
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` -- READ ONLY
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` -- READ ONLY
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy-pipeline.ts` -- READ ONLY

Additive-only surfaces:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` -- NEW (types only)
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/dynamic-model-registry-contract.test.ts` -- NEW
- `docs/reference/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_DEFINITION_2026-06-15.md` -- NEW
- `docs/corpus-intelligence/registry/entries/model-gateway-c02-p2-dynamic-model-registry-contract.json` -- NEW

---

## Work Plan

| Step | Action | Prerequisite |
| --- | --- | --- |
| W1 | Issue GC-018 for C-02 P2 | Roadmap approved |
| W2 | Author source-verified work order | GC-018 issued |
| W3 | Worker reads current source baseline (re-read at dispatch time) | Work order dispatched |
| W4 | Worker authors `dynamic-model-registry-contract.ts` (types only) | Step W3 |
| W5 | Worker authors boundary definition doc | Step W4 |
| W6 | Worker adds type-level tests | Step W4 |
| W7 | Worker adds GC-051 registry entry | Step W4 |
| W8 | Worker authors worker return | Steps W4-W7 |
| W9 | Reviewer reads worker return, repairs if needed, authors completion review | Step W8 |
| W10 | Commit closure | Step W9 |

---

## Acceptance Criteria

| # | Criterion | Gate |
| --- | --- | --- |
| AC1 | `dynamic-model-registry-contract.ts` contains only interfaces and types -- no class body, no `new`, no runtime logic | G3 |
| AC2 | All existing `PROVIDER_CAPABILITY_REGISTRY` and `ProviderRegistry` files are unchanged | G6 |
| AC3 | Type-level tests compile and pass (`npm test` in `CVF_MODEL_GATEWAY`) | G4 |
| AC4 | GC-051 entry created for the new contract file | G5 |
| AC5 | Boundary definition doc explicitly states merge-strategy boundary | D4 |
| AC6 | `rawMemoryReleased=false` on all closure artifacts | G7 |
| AC7 | No live provider calls, network traffic, or API keys used | G3 |

---

## Verification

Pre-closure autorun gate: `python governance/compat/run_local_governance_hook_chain.py
--hook pre-commit` must pass on the closure commit range.

Evidence artifacts:

- Worker return at D7 confirms AC1-AC7 with source line evidence.
- Completion review at D8 verifies worker return evidence and closes the tranche.
- Reviewer runs `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY/` and records pass/fail.

Closure is `CLOSED_PASS_BOUNDED` when completion review disposition is ACCEPT
or ACCEPT_AFTER_REVIEWER_REPAIR and all autorun gates pass.
