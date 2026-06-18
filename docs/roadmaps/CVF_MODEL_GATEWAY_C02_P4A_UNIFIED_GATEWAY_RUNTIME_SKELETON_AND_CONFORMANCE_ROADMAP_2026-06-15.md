# CVF Model Gateway C-02 P4A Unified Gateway Runtime Skeleton And Conformance Roadmap 2026-06-15

Memory class: FULL_RECORD

Status: ROADMAP_CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-15

rawMemoryReleased=false

Tranche: Model Gateway C-02 P4A Unified Gateway Runtime Skeleton And Conformance

---

## Purpose

P3 defined `UnifiedGatewayInterfaceContract` as a types-only boundary. P4A
makes that contract machine-verifiable by providing a **local deterministic
skeleton** -- a runtime class that implements the contract against existing
Model Gateway primitives (routing, policy, health, quota, receipt) without
calling any live provider API. This produces a testable seam that P4B can
later wire to real providers.

P4A is explicitly bounded to:
- A single implementation class (`UnifiedGatewaySkeletonImpl`) that satisfies
  `UnifiedGatewayInterfaceContract` using only local/deterministic logic.
- Conformance tests for all four methods (`execute`, `stream`, `embedding`,
  `health`) verifying error envelope, credential shielding, and receipt
  generation against a local stub provider.
- Error envelope and `credentialShielded: true` invariant tests.
- GC-051 registry entries for the new source and test files.

P4A is NOT:
- A live provider integration (no `fetch`, no API keys, no network).
- EPF wiring, workflow app changes, or session routing.
- A replacement for P3 contracts -- all fragment contracts and P3 types are
  reused by import.
- A production gateway or public-sync artifact.

---

## Authorization And Decision

| Field | Value |
|---|---|
| Operator instruction | 2026-06-15: operator authorized P4A scope as next tranche after P3 COMPLETE_PENDING_REVIEW |
| Prior tranche authority | P3 COMPLETE_PENDING_REVIEW; reviewer-fast 16/16 PASS; worker return at `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_WORKER_RETURN_2026-06-15.md` |
| P4A planning authority | This roadmap |
| Rewrite plan authority | `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` (section 9, `gatewayUnifiedInterfaceBoundary`, `INCLUDE_IN_BOUNDARY`; P4 implementation advisory) |
| P3 contract authority | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` |
| Pattern precedent | `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-runtime-adapter.ts` (factory-function local adapter with injected fetch) |
| Integration test precedent | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/model-gateway-runtime.integration.test.ts` |

---

## Non-Goals

The following are explicitly deferred from P4A:

| Item | Deferral reason |
|---|---|
| Live provider API calls | P4B; requires authorized credentials and live-proof roadmap |
| EPF / workflow-app wiring | Separate governed work order; different extension boundary |
| Strategy layer (Planner, Taxonomy, Feedback Loop) | Deferred per C-02 rewrite plan |
| AI Gateway family absorption | PARKED_PENDING_PRIVACY_OPERATOR_AUTHORIZATION |
| Public-sync | Not authorized under any current GC-018 |
| DynamicModelRegistry runtime | May be wired in P4B; P4A uses static provider list |
| Streaming over real network | P4B; requires live provider |
| Embedding over real provider | P4B; requires live provider |

---

## Tranche Sequence Summary

| Tranche | Status | Scope |
|---|---|---|
| C-02 P1 | CLOSED_PASS_BOUNDED | Routing Pipeline (RoutingPolicyEngine, fallback, quota, health, receipt) |
| C-02 P2 | CLOSED_PASS_BOUNDED | Dynamic Model Registry boundary (DynamicModelRegistryContract, types-only) |
| C-02 P3 | COMPLETE_PENDING_REVIEW | Unified Gateway Interface contract (UnifiedGatewayInterfaceContract, types-only) |
| C-02 P4A | ROADMAP_READY | Unified Gateway Runtime Skeleton (local deterministic impl, conformance tests) |
| C-02 P4B | PARKED | Live provider wiring (requires credentials, live-proof roadmap, separate GC-018) |

---

## Scope -- In Detail

### IS-1: UnifiedGatewaySkeletonImpl class

Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-skeleton.ts`.

The class must:
- Implement `UnifiedGatewayInterfaceContract` (imported from P3 contract).
- Accept constructor arguments:
  - `registry: ProviderRegistry` (existing primitive)
  - `health: ProviderHealthMonitor` (existing primitive)
  - `quota: QuotaLedger` (existing primitive)
  - `policy: GatewayPolicyContext` injected per-request or at construction
  - Optional: `receiptBuilder: GatewayReceiptBuilder`
  - Optional: `localExecuteFn`: injectable deterministic executor
    (`(request: GatewayExecuteRequest) => Promise<string>`) for tests.

Method contracts:
- `execute(request)` -- runs policy check; if denied returns `GatewayErrorEnvelope`
  with `credentialShielded: true`, `errorClass: "policy_denied"`. If allowed,
  calls `localExecuteFn` (or returns a deterministic stub response) and returns
  `GatewayExecuteResponse`. No live fetch.
- `stream(request)` -- yields at least one `GatewayStreamChunk` with `done: true`.
  If policy denied, yields single `GatewayErrorEnvelope`. No live fetch.
- `embedding(request)` -- returns `GatewayEmbeddingResponse` with a
  deterministic `[[0, 0, 0]]` embedding and `dimensions: 3`, or
  `GatewayErrorEnvelope` if policy denied. No live fetch.
- `health(traceId)` -- assembles `GatewayHealthResponse` from
  `ProviderHealthMonitor.get()` for each registered provider. No live fetch.

Credential shielding invariant:
- All `GatewayErrorEnvelope` values must have `credentialShielded: true`.
- No providerId, API key, or secret value may appear in any response field.
- `providerIdShielded?: true` on error envelopes when provider selection
  must not be disclosed.

File-size discipline: must stay under `.ts` advisory threshold (700 lines).
Hard limit: 1000 lines.

### IS-2: Barrel export update

Add `UnifiedGatewaySkeletonImpl` and any new public types to `index.ts` barrel.

### IS-3: Conformance tests

Create `EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-skeleton.test.ts`.

Required test cases (minimum):
- `execute` with allowed policy returns `GatewayExecuteResponse` shape.
- `execute` with denied policy returns `GatewayErrorEnvelope` with
  `errorClass: "policy_denied"` and `credentialShielded: true`.
- `stream` with allowed policy yields at least one `GatewayStreamChunk`.
- `stream` with denied policy yields `GatewayErrorEnvelope`.
- `embedding` with allowed policy returns `GatewayEmbeddingResponse` shape
  with `embeddings` array and `dimensions` number.
- `embedding` with denied policy returns `GatewayErrorEnvelope`.
- `health` returns `GatewayHealthResponse` with `status` one of
  `"ok" | "degraded" | "unavailable"`.
- Credential shielding: `JSON.stringify(response)` must not contain any
  secret value injected into the test setup.
- `UnifiedGatewaySkeletonImpl` satisfies `UnifiedGatewayInterfaceContract`
  (compile-time type check).
- No live network call in any test (injected localExecuteFn only).

File-size discipline: must stay under `.test.ts` advisory threshold (800 lines).
Hard limit: 1200 lines.

### IS-4: GC-051 registry entries

Add entries for:
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-skeleton.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-skeleton.test.ts`

---

## Required First Reads

| File | Required use |
|---|---|
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | P3 contract; implementation target |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | RoutingRequest, RoutingPolicyEngine reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | GatewayPolicyContext, isPolicyAllowed reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | ProviderHealthMonitor, ProviderHealthState reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | ProviderRegistry reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | QuotaLedger reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | GatewayReceiptBuilder reuse |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | CredentialBoundary shielding pattern |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-runtime-adapter.ts` | Adapter factory pattern precedent |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/model-gateway-runtime.integration.test.ts` | Integration test pattern precedent |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | Barrel surface; avoid name collisions |
| `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | GC-023 thresholds |

---

## Deliverables

| ID | Artifact | Owner | Status |
|---|---|---|---|
| D1 | GC-018 baseline | orchestrator | REQUIRED before dispatch |
| D2 | Work order | orchestrator | REQUIRED before dispatch |
| D3 | `unified-gateway-skeleton.ts` (runtime class) | worker | REQUIRED |
| D4 | `index.ts` barrel edit | worker | REQUIRED |
| D5 | `unified-gateway-skeleton.test.ts` (conformance tests) | worker | REQUIRED |
| D6 | GC-051 registry entries (2 files + aggregate regenerate) | worker | REQUIRED |
| D7 | Worker return | worker | REQUIRED |
| D8 | Completion review | reviewer | REQUIRED |

---

## Acceptance Criteria

| # | Criterion | Verification |
|---|---|---|
| AC1 | `UnifiedGatewaySkeletonImpl` satisfies `UnifiedGatewayInterfaceContract` at compile time | `npm run check` PASS |
| AC2 | All four methods return correct shape on happy path | conformance tests PASS |
| AC3 | All four methods return `GatewayErrorEnvelope` with `credentialShielded: true` when policy denied | conformance tests PASS |
| AC4 | `JSON.stringify(response)` never contains injected secret values | credential shielding test PASS |
| AC5 | No live network call in any test or source file | no `fetch`, no `http`, no provider URL in new files |
| AC6 | All existing tests continue to PASS | `npm test` PASS |
| AC7 | `rawMemoryReleased=false` on all closure artifacts | front-matter literal |
| AC8 | GC-051 entries added for new source and test files | registry entries present |

---

## Gates

| Gate | Command | Required |
|---|---|---|
| G1 | TypeScript type check | `npm run check` PASS |
| G2 | Full test suite | `npm test` PASS (all existing + new conformance tests) |
| G3 | reviewer-fast | `python governance/compat/run_worker_return_fast_gate.py` 16/16 PASS |
| G4 | GC-051 aggregate drift | `generate_corpus_scan_registry.py --check` PASS |
| G5 | git diff whitespace | `git diff --check` PASS |
| G6 | No live call | changed file set inspection; no fetch/http/provider-URL in new files |
| G7 | Pre-closure autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <dispatchBaseHead> --head HEAD` PASS |

---

## Work Plan

| Step | Action | Output |
|---|---|---|
| 1 | GC-018 baseline (orchestrator) | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P4A_...md` |
| 2 | Work order (orchestrator) | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4A_...md` |
| 3 | Read all Required First Reads; capture executionBaseHead | preflight evidence |
| 4 | Implement IS-1 skeleton class | `unified-gateway-skeleton.ts` |
| 5 | Implement IS-2 barrel edit | `index.ts` updated |
| 6 | Implement IS-3 conformance tests | `unified-gateway-skeleton.test.ts` |
| 7 | Add IS-4 GC-051 registry entries; regenerate aggregate | 2 JSON + aggregate |
| 8 | Run gates G1-G6; repair allowed-scope issues; run G3 reviewer-fast PASS | gate evidence |
| 9 | Author worker return with COMPLETE_PENDING_REVIEW | worker return doc |
| 10 | Reviewer: run G7 pre-closure autorun; author completion review; commit | closure artifacts |

---

## Current Runtime Freshness Verification

All source symbols verified at HEAD `c6c09ae3` on 2026-06-15.

| Surface | Verified command | Result |
|---|---|---|
| `UnifiedGatewayInterfaceContract` | `rg -n "UnifiedGatewayInterfaceContract" EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | found (P3 untracked, confirmed in worktree) |
| `GatewayPolicyContext` | `rg -n "GatewayPolicyContext" EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | found at line 2 |
| `ProviderHealthMonitor` | `rg -n "ProviderHealthMonitor" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | found |
| `RoutingPolicyEngine` | `rg -n "RoutingPolicyEngine" EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | found |
| `ProviderRegistry` | `rg -n "ProviderRegistry" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | found |
| `QuotaLedger` | `rg -n "QuotaLedger" EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | found |
| `GatewayReceiptBuilder` | `rg -n "GatewayReceiptBuilder" EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | found |
| `isPolicyAllowed` | `rg -n "isPolicyAllowed" EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | found |

---

## Verification And Evidence

Pre-closure autorun gate must PASS on material closure commit range before
completion review declares ACCEPT. Pre-commit hook runs automatically at
every `git commit`. Reviewer must inspect real diff before any commit.

---

## Design Control Gate

| Gate | Requirement | Status |
|---|---|---|
| GC-018 | Baseline issued before dispatch | REQUIRED (D1) |
| GC-023 | File size thresholds checked before authoring | .ts hard=1000/advisory=700; .test.ts hard=1200/advisory=800 |
| GC-051 | Corpus scan registry entries for all new governed files | REQUIRED (D6) |
| Work order source verification | All named tokens verified in current runtime source | REQUIRED (D2) |
| reviewer-fast 16/16 | Worker return passes all 16 gate checks | REQUIRED before D8 |

---

## Machine Closure Package

Status: ROADMAP_READY -- Final status column will be updated by reviewer at tranche closure.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_FOR_CLAUDE_2026-06-15.md` | final status, no stale ready/pending residue, closure anchor policy | BLOCKED with reason: worker return not yet authored; reviewer updates to PASS at D8 |
| Completion or reviewer artifact | `docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_WORKER_RETURN_2026-06-15.md` | final disposition, changed files, claim boundary, gate evidence | BLOCKED with reason: worker return not yet authored; reviewer updates to PASS at D8 |
| Roadmap state | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_AND_CONFORMANCE_ROADMAP_2026-06-15.md` | tranche row final state and next dependency state | BLOCKED with reason: tranche not yet closed; reviewer updates tranche row to CLOSED_PASS_BOUNDED at D8 |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 entries added for P4A skeleton source and test files; aggregate regenerated | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | operator/reviewer quick lookup companion | BLOCKED with reason: Registry Markdown companion not updated in P4A worker scope; reviewer updates at D8 or separate governed batch |
| External evidence digest | N/A with reason: no external paths, no CVF-Workspace artifacts in P4A scope | no external evidence required | N/A with reason: P4A is local deterministic skeleton with no external evidence surfaces |
| System loop interlock | N/A with reason: no system loop interlock registry entry required for local skeleton tranche | no live external loop in P4A | N/A with reason: P4A has no live provider loop; system loop interlock not applicable |
| Session continuity | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, active handoff | current mode, next allowed move, handoff HEAD or accepted parent marker | BLOCKED with reason: session state update performed by reviewer at D8 commit; not worker scope |

### Acceptance Receipt Assertion Matrix

This matrix satisfies the receipt-class closure requirement for P4A (GatewayReceiptBuilder is reused as a primitive; P4A does not introduce new receipt acceptance logic).

| Criterion | Required value | Observed value | Status |
|---|---|---|---|
| GatewayReceiptBuilder reuse only | existing primitive imported, not extended | `gateway-receipt.ts` imported but not modified | PENDING confirmation in worker return |
| receiptObligation field on responses | string constant per response type | present in execute/stream/embedding responses in skeleton | PENDING confirmation in worker return |
| No new receipt acceptance surface | P4A adds no new receipt query or acceptance gate | confirmed: skeleton passes obligation through; no new acceptance logic | PENDING confirmation in worker return |

---

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: P4A is an internal governed tranche producing a local deterministic skeleton with no live provider proof. No GC-018 or operator instruction authorizes public-sync for Model Gateway skeleton source or tests. Public export requires a separate operator decision after P4B live-provider proof closes and MGW-001 reaches CLOSED_VERIFIED.

| Artifact | Public export status | Reason |
|---|---|---|
| `unified-gateway-skeleton.ts` | DEFERRED_PRIVATE_ONLY | Reason: internal governed source; no public-sync authorization |
| `unified-gateway-skeleton.test.ts` | DEFERRED_PRIVATE_ONLY | Reason: internal conformance tests; not a public API |
| GC-018 baseline | DEFERRED_PRIVATE_ONLY | Reason: internal authorization record per public-sync rule |
| Worker return | DEFERRED_PRIVATE_ONLY | Reason: internal audit record per public-sync rule |
| Completion review | DEFERRED_PRIVATE_ONLY | Reason: internal audit record per public-sync rule |

---

## Claim Boundary

This roadmap defines P4A scope and deliverables only. It does not claim
runtime behavior, live provider behavior, production readiness, or public
readiness. No implementation is claimed before the worker return is authored
and reviewed. `MGW-001` in the legacy coverage index stays
`PARTIAL_RECHECK_REQUIRED` until P4A and P4B both close (P3 alone was
insufficient; P4A adds skeleton but not live provider proof).

## GFC-T3 Closure Note (2026-06-18)

This roadmap is closed bounded per GFC-T3 Roadmap State Hygiene Remediation
(work order `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md`).
Closure evidence: `docs/reviews/CVF_MODEL_GATEWAY_C02_P4A_UNIFIED_GATEWAY_RUNTIME_SKELETON_COMPLETION_2026-06-15.md`
(status `CLOSED_PASS_BOUNDED`); session memory records material commit `5d46bc62`. Status line
updated from `ROADMAP_READY` to `ROADMAP_CLOSED_PASS_BOUNDED` by GFC-T3 worker, fulfilling
the reviewer-closure instruction documented at line 281 of this file.
