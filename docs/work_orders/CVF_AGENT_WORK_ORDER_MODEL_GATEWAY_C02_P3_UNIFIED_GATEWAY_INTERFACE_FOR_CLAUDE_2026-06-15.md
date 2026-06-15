# CVF Agent Work Order: Model Gateway C-02 P3 Unified Gateway Interface - 2026-06-15

Memory class: FULL_RECORD

Status: DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT

Worker: Claude

Orchestrator / reviewer: Codex (or Claude under SINGLE_AGENT_MULTI_ROLE)

Worker commit policy: WORKER_MUST_NOT_COMMIT

Commit mode: WORKER_MUST_NOT_COMMIT

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_FOR_CLAUDE_2026-06-15.md`
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_COMPLETION_2026-06-15.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`

dispatchBaseHead: c6c09ae3

executionBaseHead: WORKER_MUST_CAPTURE_AFTER_DISPATCH

closureBaseHead: REVIEWER_CAPTURE_AFTER_WORKER_RETURN

rawMemoryReleased=false

riskCeiling: R1 (additive contract/types/doc/tests in one extension; no runtime
logic, no provider/live/public, no mutation of existing source beyond barrel)

---

## Authorization Preconditions (BLOCKING)

Both prerequisites are satisfied:

1. Fresh GC-018 baseline:
   `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_2026-06-15.md`
2. Operator authorized P3 scope and SINGLE_AGENT_MULTI_ROLE pattern in 2026-06-15
   session instruction.

Dispatch status: `DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance contract-first work order. Public-sync not authorized.

## Claim Boundary

This work order authorizes only the C-02 P3 unified gateway interface boundary
contract definition inside `EXTENSIONS/CVF_MODEL_GATEWAY/`. It authorizes a
types-only contract file, a boundary definition document, type-level tests, and
GC-051 registry entries. It does NOT authorize the runtime
`UnifiedGatewayInterface` class, `DynamicModelRegistry` runtime implementation,
EPF integration wiring, provider/API calls, live proof, public-sync, mutation of
any existing source file other than `index.ts` barrel, governance-kernel changes,
or production/public readiness claims.

---

## Purpose

Define the Unified Gateway Interface (UGI) boundary as a doc/contract-first
artifact so that P4 implementation and EPF integration reference a governed
entry-point contract rather than scattered fragment contracts.

P3 fulfills the rewrite plan advisory key `gatewayUnifiedInterfaceBoundary`
(`INCLUDE_IN_BOUNDARY`, section 9) by:

1. Authoring a types-only contract file (`unified-gateway-interface-contract.ts`)
   declaring `GatewayErrorClass`, `GatewayErrorEnvelope`, `GatewayExecuteRequest`,
   `GatewayExecuteResponse`, `GatewayStreamRequest`, `GatewayStreamChunk`,
   `GatewayEmbeddingRequest`, `GatewayEmbeddingResponse`, `GatewayHealthResponse`,
   and `UnifiedGatewayInterfaceContract`.
2. Authoring a boundary definition document stating what each existing fragment
   covers versus what the unified interface adds.
3. Adding type-level tests proving the contract shapes are internally consistent
   and reuse existing types correctly.
4. Adding GC-051 corpus scan registry entries for the new files.

The contract file MUST contain only interfaces and type aliases. It MUST NOT
contain a class body, runtime logic, `new` calls, or any executable statement
beyond type declarations and at most one literal version constant.

---

## Authority Chain

| Authority | Role |
|---|---|
| `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_2026-06-15.md` | Implementation authorization for C-02 P3 |
| Operator instruction 2026-06-15 | Approves P3 scope and SINGLE_AGENT_MULTI_ROLE pattern |
| `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_ROADMAP_2026-06-15.md` | P3 roadmap: scope, deliverables, contract sketch, acceptance criteria |
| `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | Closed C-02 plan; `gatewayUnifiedInterfaceBoundary` disposition (section 9) |
| P2 closure at commit `24d455f8` | P2 `DynamicModelRegistryContract` is stable input to P3 |
| This work order | Worker execution scope |
| Reviewer agent | Closure, commits, allowed repairs, session sync |

---

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
|---|---|
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row id | `MGW-001` |
| Coverage status | `PARTIAL_RECHECK_REQUIRED` |
| Release basis | P3 implements the `gatewayUnifiedInterfaceBoundary` advisory contract boundary |
| Required disposition in worker return | Confirm P3 implements only the unified gateway interface contract; all strategy-layer, AI Gateway, and runtime implementation keys remain deferred |
| P3 closure coverage note | `MGW-001` stays `PARTIAL_RECHECK_REQUIRED` until P4 closes; P3 alone does not upgrade the row |

## Freeze Posture Disposition

| Field | Evidence |
|---|---|
| Active freeze posture | `governance_kernel_freeze_recommended` |
| Freeze rule | `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md` |
| Kernel surface check | `CVF_MODEL_GATEWAY` is NOT one of the 12 governance-kernel owner-map surfaces |
| Disposition | Contract-first work permitted under fresh GC-018; no freeze-release packet required |

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator / reviewer / committer | Reviewer agent | Review returned contract/doc/tests, run gates, author closure artifact, commit accepted artifacts, sync session continuity |
| Worker | Worker agent | Author P3 contract + doc + type tests only, run worker gates, return `COMPLETE_PENDING_REVIEW` without committing |
| Operator | Human operator | Authorizes scope and assignment; approves any scope change |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | Operator authorized Model Gateway C-02 P3 Unified Gateway Interface per SINGLE_AGENT_MULTI_ROLE pattern |
| Scope classification | Bounded R1 single-extension Model Gateway contract/doc/type-test authoring |
| Risk sensitivity | No public-sync, no provider/live proof, no secrets, no runtime logic, no production/readiness claim |
| Selected route mode | SINGLE_AGENT_MULTI_ROLE |
| routeMode | SINGLE_AGENT_MULTI_ROLE |
| Role separation basis | Phase gates, separate base heads, worker no-commit boundary, reviewer closure conversion |
| Escalation condition | Stop for scope expansion beyond P3 contract boundary, runtime implementation, provider/live proof, public-sync, secrets, package install, existing-source mutation, governance-kernel mutation |
| Disposition | DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT |

## Single-Agent Multi-Role Control Block

| Field | Decision |
|---|---|
| Single agent owns implementation and review | YES if operator assigns multi-role, bounded by this block |
| Role separation ledger | Orchestrator owns GC-018 and dispatch; worker owns contract/doc/tests and worker return; reviewer owns closure artifact and acceptance; committer owns commits and session sync |
| Evidence basis independent of memory-only claims | GC-018, work order, source verification, type-level tests, diff evidence, governance gates |
| Self-review boundary | Independent review is not claimed; reviewer must inspect real diff and gate evidence before any commit |
| Gate sequence | pre-dispatch by orchestrator, baseline tests by worker, type-level tests by worker, reviewer-fast and pre-closure by reviewer, pre-push only if later authorized |
| Escalation conditions | Stop for forbidden paths, runtime/P4/strategy scope, provider/live proof, public-sync, secrets, package install, existing-source mutation, governance-kernel mutation |
| Worker | Assigned worker role |
| Reviewer / committer | Assigned reviewer and committer roles |
| Human escalation checkpoint | Scope expansion only |
| Collusion boundary | Single-agent result is bounded governance evidence, not independent review |

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_COMPLETION_2026-06-15.md`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`

---

## Pre-Flight Checks

Worker must:

1. Capture `executionBaseHead` (`git rev-parse HEAD`).
2. Run `git status --short` and confirm clean worktree.
3. Confirm the fresh GC-018 baseline and operator authorization both exist.
4. Read all Required First Reads.
5. Re-read all source baseline files and re-confirm line ranges.
6. Run baseline test suite for `CVF_MODEL_GATEWAY` to capture green pre-state.

## Write Ownership

Worker may write only:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` (create)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (edit, barrel exports only)
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-interface-contract.test.ts` (create)
- `docs/reference/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_BOUNDARY_DEFINITION_2026-06-15.md` (create)
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_WORKER_RETURN_2026-06-15.md` (create)
- GC-051 source entries under `docs/corpus-intelligence/registry/entries/` (create, allowed-scope repair)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (regenerate, allowed-scope repair)

Worker must NOT write to any other extension, any session/handoff/registry file,
or any existing source file other than `index.ts` barrel.

## Required First Reads

| File | Required use |
|---|---|
| `AGENTS.md` | Active governance instructions |
| `CVF_SESSION_MEMORY.md` | Current mode and next allowed move |
| `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_ROADMAP_2026-06-15.md` | P3 scope, deliverables, contract sketch |
| `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_2026-06-15.md` | Implementation authorization |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` | `StreamRequest`, `StreamContract` retained fragment authority (reference only) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/embedding-contract.ts` | `EmbeddingRequest`, `EmbeddingContract` retained fragment authority (reference only) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | `ProviderHealthState` (reuse) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | `GatewayPolicyContext` (reuse) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | `RoutingRequest` (reuse) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | `DynamicModelRecord` (reuse) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | Barrel surface; avoid name collisions |
| `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | GC-023 thresholds |

## Source Verification Block

All symbols verified against current source at HEAD `c6c09ae3` on 2026-06-15.
Disposition column uses canonical values only: ACCEPT, REJECT, or BLOCKED-SOURCE-NOT-FOUND (hyphenated when used as prose; backtick form only in table cells).

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Implementation action | Disposition |
|---|---|---|---|---|---|---|
| Referenced: StreamRequest | `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` | line 1 | `StreamRequest` | stream-contract | REFERENCE_ONLY | ACCEPT |
| Referenced: StreamContract | `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` | line 7 | `StreamContract` | stream-contract | REFERENCE_ONLY | ACCEPT |
| Referenced: EmbeddingRequest | `EXTENSIONS/CVF_MODEL_GATEWAY/src/embedding-contract.ts` | line 1 | `EmbeddingRequest` | embedding-contract | REFERENCE_ONLY | ACCEPT |
| Referenced: EmbeddingContract | `EXTENSIONS/CVF_MODEL_GATEWAY/src/embedding-contract.ts` | line 7 | `EmbeddingContract` | embedding-contract | REFERENCE_ONLY | ACCEPT |
| Reused: ProviderHealthState | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 1 | `ProviderHealthState` | provider-health | REUSE_BY_IMPORT | ACCEPT |
| Reused: GatewayPolicyContext | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | line 2 | `GatewayPolicyContext` | gateway-policy | REUSE_BY_IMPORT | ACCEPT |
| Reused: GatewayPolicyResult | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | line 1 | `GatewayPolicyResult` | gateway-policy | REFERENCE_ONLY | ACCEPT |
| Reused: RoutingRequest | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 13 | `RoutingRequest` | routing-policy | REUSE_BY_IMPORT | ACCEPT |
| Reused: DynamicModelRecord | `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | line 8 | `DynamicModelRecord` | dynamic-model-registry-contract | REUSE_BY_IMPORT | ACCEPT |
| Reused: index.ts barrel | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | lines 1-290 | barrel export blocks | model gateway barrel | EXTEND_BARREL_ONLY | ACCEPT |

Note: worker must re-confirm these at execution time.

## Negative Search And Collision Discipline

| Structured query | Search roots | Expected result | Disposition |
|---|---|---|---|
| `rg -n "UnifiedGatewayInterfaceContract\|GatewayExecuteRequest\|GatewayExecuteResponse\|GatewayStreamRequest\|GatewayStreamChunk\|GatewayEmbeddingRequest\|GatewayEmbeddingResponse\|GatewayHealthResponse\|GatewayErrorEnvelope\|GatewayErrorClass" --hidden --no-ignore .` | All source, tests, docs, JSON | Zero current occurrence; no same-token collision | ABSENT; SAFE_TO_ADD, binding |
| `rg -n "UNIFIED_GATEWAY_INTERFACE_CONTRACT_VERSION" EXTENSIONS/CVF_MODEL_GATEWAY` | Model Gateway source and tests | No existing occurrence | ABSENT; SAFE_TO_ADD if constant added |
| `rg -n "GatewayPolicyContext\|RoutingRequest\|ProviderHealthState\|DynamicModelRecord" EXTENSIONS/CVF_MODEL_GATEWAY/src` | Model Gateway source | Existing reusable types in authoritative definition files | COLLISION_IS_AUTHORITATIVE_SOURCE; contract must import, not redeclare |

Collision note: the contract MUST reuse `GatewayPolicyContext`, `RoutingRequest`,
`ProviderHealthState`, and `DynamicModelRecord` by import. It MUST NOT redeclare
any parallel type for these concepts.

## Current Runtime Freshness Verification

| Surface | Freshness check | Expected |
|---|---|---|
| StreamRequest | `rg -n "StreamRequest" EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` | found at line 1 |
| EmbeddingRequest | `rg -n "EmbeddingRequest" EXTENSIONS/CVF_MODEL_GATEWAY/src/embedding-contract.ts` | found at line 1 |
| ProviderHealthState | `rg -n "ProviderHealthState" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | found at line 1 |
| GatewayPolicyContext | `rg -n "GatewayPolicyContext" EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | found at line 2 |
| RoutingRequest | `rg -n "RoutingRequest" EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | found at line 13 |
| DynamicModelRecord | `rg -n "DynamicModelRecord" EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` | found at line 8 |

---

## Implementation Specification

### IS-1: Contract file (types only)

Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts`
containing ONLY type aliases, interfaces, and at most one literal version
constant. Import all reused types from existing files.

Required declarations:

- `UNIFIED_GATEWAY_INTERFACE_CONTRACT_VERSION` -- optional literal constant,
  e.g. `"cvf.unifiedGatewayInterface.v1"`.
- `GatewayErrorClass` -- string-literal union:
  `"policy_denied" | "no_candidate" | "quota_exceeded" | "provider_unavailable" | "invalid_request" | "credential_shielded" | "internal_error"`.
- `GatewayErrorEnvelope` -- interface: `errorClass: GatewayErrorClass`,
  `traceId: string`, `message: string`, `credentialShielded: true`,
  `providerIdShielded?: true`, `retryable: boolean`.
- `GatewayExecuteRequest` -- interface: `traceId: string`, `prompt: string`,
  `systemPrompt?: string`, `policy: GatewayPolicyContext` (imported),
  `routing?: RoutingRequest` (imported), `preferredModel?: DynamicModelRecord`
  (imported), `metadata?: Record<string, unknown>`.
- `GatewayExecuteResponse` -- interface: `traceId: string`, `text: string`,
  `usage?: { inputTokens: number; outputTokens: number }`,
  `receiptObligation?: string`,
  `model?: { providerId: string; modelId: string }`.
- `GatewayStreamRequest` -- interface extending `GatewayExecuteRequest` (or
  equivalent fields; worker decides).
- `GatewayStreamChunk` -- interface: `traceId: string`, `chunk: string`,
  `done: boolean`, `receiptObligation?: string`.
- `GatewayEmbeddingRequest` -- interface: `traceId: string`,
  `input: string | string[]`, `model?: string`,
  `policy: GatewayPolicyContext` (imported),
  `metadata?: Record<string, unknown>`.
- `GatewayEmbeddingResponse` -- interface: `traceId: string`,
  `embeddings: number[][]`, `dimensions: number`, `receiptObligation?: string`.
- `GatewayHealthResponse` -- interface: `traceId: string`,
  `status: "ok" | "degraded" | "unavailable"`,
  `providerHealthSummary?: Record<string, ProviderHealthState>` (imported),
  `checkedAt: string`.
- `UnifiedGatewayInterfaceContract` -- interface with method signatures only:
  - `execute(request: GatewayExecuteRequest): Promise<GatewayExecuteResponse | GatewayErrorEnvelope>;`
  - `stream(request: GatewayStreamRequest): AsyncIterable<GatewayStreamChunk | GatewayErrorEnvelope>;`
  - `embedding(request: GatewayEmbeddingRequest): Promise<GatewayEmbeddingResponse | GatewayErrorEnvelope>;`
  - `health(traceId: string): Promise<GatewayHealthResponse>;`

### IS-2: Barrel exports

Add all new types and the optional version constant to `index.ts` using
`export type { ... } from "./unified-gateway-interface-contract"` and a separate
value export for the constant. Do not collide with existing names.

### IS-3: Boundary definition document

Create
`docs/reference/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_BOUNDARY_DEFINITION_2026-06-15.md`
stating:

- What each fragment contract (`stream-contract.ts`, `embedding-contract.ts`,
  `provider-health.ts`, `gateway-policy.ts`) currently covers and retains authority for.
- What `UnifiedGatewayInterfaceContract` adds: a single caller entry point,
  standard error envelope, credential shielding markers.
- P3 mutates no existing fragment contract.
- Future P4 runtime class must implement `UnifiedGatewayInterfaceContract` and
  cite this boundary definition as its interface authority.

Include standard governed-markdown structural sections (Purpose, Scope,
Boundary, Claim Boundary) to pass the markdown structural completeness gate.

### IS-4: Type-level tests

Create
`EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-interface-contract.test.ts`
with compile-time / type-level assertions only. No network, no provider call,
no runtime class instantiation beyond a local test-only stub.

Required test cases:

- `GatewayExecuteRequest` literal type-checks with `GatewayPolicyContext` field.
- `GatewayStreamChunk` literal type-checks.
- `GatewayEmbeddingRequest` literal type-checks.
- `GatewayHealthResponse` literal type-checks with `ProviderHealthState` in summary.
- `GatewayErrorEnvelope` literal type-checks with `credentialShielded: true`.
- Local test-only stub satisfies `UnifiedGatewayInterfaceContract` (returns
  empty/undefined stubs for all four methods).
- `providerHealthSummary` accepts `ProviderHealthState` values.
- `GatewayErrorClass` union is assignable to `errorEnvelope.errorClass`.

### IS-5: File-size discipline (GC-023)

Contract file should be well under `.ts` advisory threshold (700 lines).
Test file must stay under `.test.ts` advisory threshold (800 lines).

---

## Test Specification

| Test | Requirement |
|---|---|
| Request shape | `GatewayExecuteRequest`, `GatewayEmbeddingRequest` literals type-check |
| Response shape | `GatewayExecuteResponse`, `GatewayStreamChunk`, `GatewayHealthResponse` literals type-check |
| Error envelope | `GatewayErrorEnvelope` literal type-checks; `credentialShielded: true` required |
| Interface implementable | Local test stub satisfies `UnifiedGatewayInterfaceContract` |
| Type reuse | `GatewayPolicyContext`, `RoutingRequest`, `DynamicModelRecord`, `ProviderHealthState` accepted without redeclaration |
| No runtime logic in src | Contract file has no class body, no `new`, no executable statement beyond declarations |
| Existing suite intact | `CVF_MODEL_GATEWAY` `npm test` continues to pass |

---

## Execution Plan

| Step | Input | Action | Output | Stop condition |
|---|---|---|---|---|
| 1 | Required first reads + GC-018 + operator auth | Capture executionBaseHead; confirm authorizations; re-confirm source baseline line ranges; run baseline tests green | preflight evidence | Stop if GC-018/operator auth missing or baseline red |
| 2 | stream-contract.ts, embedding-contract.ts, provider-health.ts, gateway-policy.ts, routing-policy.ts, dynamic-model-registry-contract.ts | Implement IS-1 contract file importing reusable types | types-only contract | Stop if a reused type does not exist or a runtime statement would be required |
| 3 | index.ts | Implement IS-2 barrel exports without collision | updated barrel | Stop on export name collision |
| 4 | boundary inputs | Implement IS-3 boundary definition doc | governed doc | Stop if doc would claim runtime or readiness |
| 5 | contract | Implement IS-4 type-level tests | passing tests | Stop if a test would require runtime class instantiation beyond local stub |
| 6 | gates | Run type check, MG tests, reviewer-fast | evidence in worker return | Stop and repair allowed-scope issues before return |

## Evidence Requirements

The worker must provide source-backed evidence for every claim in the worker return:

- Each reuse claim: cite the imported type and its source line.
- The types-only claim: `git diff` of the new contract file showing zero class
  bodies, zero `new`, zero runtime statements beyond declarations.
- The existing-sources-unchanged claim: `git diff --name-status` showing NO
  change to any protected file.
- The no-provider/no-live claim: changed file set limited to new contract file,
  barrel edit, new test, boundary doc, GC-051 entries, and worker return.
- The no-commit claim: `git rev-parse HEAD` equal to `executionBaseHead`.
- Type-check and test results: actual command output summaries, not predicted results.
- The credential-shielding claim: cite that `GatewayErrorEnvelope.credentialShielded`
  is typed as literal `true`, not `boolean`.

Evidence may be command-output summaries, cited governed file lines/sections,
or explicit N/A with reason where a proof class does not apply.

## Worker Autonomy / No-Question Rule

Allowed-scope failures (type errors, failing new tests, missing sections, trace
updates, diff hygiene, GC-023 file split, markdown structural sections, ASCII
encoding, GC-051 coverage) must be repaired and rerun without escalation.

Worker must stop and return `BLOCKED_SCOPE_EXPANSION` only when a repair would:
require editing an extension other than `CVF_MODEL_GATEWAY`; require editing any
existing source file other than `index.ts` barrel; require runtime class
implementation; require a provider/API/live call; require package install, secret
access, public-sync, registry mutation, session-state mutation, governance-kernel
mutation, or any destructive action.

## Worker Pending-Return Gate

| Gate | Required evidence | Status |
|---|---|---|
| Authorizations present | GC-018 + operator authorization cited | PENDING |
| Scope-limited mutation | Changes limited to new contract, barrel edit, new test, boundary doc, GC-051 entries, worker return | PENDING |
| Existing sources unchanged | All fragment contracts and registries show zero diff | PENDING |
| Types-only contract | Contract file has no class body, no `new`, no runtime statement | PENDING |
| Type reuse | All reused types imported, not redeclared | PENDING |
| New tests present | Shape, stub, type-reuse cases added | PENDING |
| Type check | `npm run check` PASS | PENDING |
| Test run | `npm test` PASS | PENDING |
| GC-023 | No file exceeds hard threshold | PENDING |
| No provider/live | No provider/API/live proof, package install, secret read | PENDING |
| Name collision avoided | All new symbols absent from repo before authoring | PENDING |
| Agent Operation Trace Block | Expected and actual changed set recorded | PENDING |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` in worker return | PENDING |
| Worker did not commit | HEAD stayed `executionBaseHead` | PENDING |
| Diff hygiene | `git diff --check` PASS | PENDING |
| Reviewer-fast | `python governance/compat/run_worker_return_fast_gate.py` PASS | PENDING |

---

## Acceptance Criteria

| # | Criterion | Verification |
|---|---|---|
| AC1 | `unified-gateway-interface-contract.ts` contains only interfaces, type aliases, and at most one literal version constant | `git diff` of the file |
| AC2 | All existing fragment contracts unchanged | `git diff --name-status` shows no change to any protected file |
| AC3 | Contract reuses `GatewayPolicyContext`, `RoutingRequest`, `DynamicModelRecord`, `ProviderHealthState` by import | cited import lines |
| AC4 | Type-level tests compile and pass | `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY/` |
| AC5 | Boundary definition doc states fragment coverage vs. unified interface additions | doc section content |
| AC6 | `rawMemoryReleased=false` on all closure artifacts | front-matter literal |
| AC7 | No live provider calls, network traffic, or API keys used | changed file set + worker statement |

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap deliverable | Roadmap ref | Work order section | Owner |
|---|---|---|---|
| D1 GC-018 baseline | Deliverables D1 | Authorization Preconditions | orchestrator |
| D2 Work order | Deliverables D2 | this document | orchestrator |
| D3 Contract file | Deliverables D3 | IS-1, Write Ownership | worker |
| D4 Boundary definition doc | Deliverables D4 | IS-3 | worker |
| D5 Type-level tests | Deliverables D5 | IS-4, Test Specification | worker |
| D6 GC-051 registry entries | Deliverables D6 | Write Ownership | worker |
| D7 Worker return | Deliverables D7 | Write Ownership | worker |
| D8 Completion review | Deliverables D8 | Reviewer Closure Conversion Block | reviewer |
| AC1 types-only | AC1 | Acceptance Criteria AC1 | worker |
| AC2 sources unchanged | AC2 | Acceptance Criteria AC2 | worker |
| AC3 type reuse | AC3 | Acceptance Criteria AC3 | worker |
| AC4 tests pass | AC4 | Acceptance Criteria AC4 | worker |
| AC5 boundary doc | AC5 | Acceptance Criteria AC5 | worker |
| AC6 rawMemoryReleased=false | AC6 | Acceptance Criteria AC6 | worker/reviewer |
| AC7 no live | AC7 | Acceptance Criteria AC7 | worker |

## Review Gate

The reviewer must verify, on the committed range, before declaring ACCEPT:

- All Acceptance Criteria AC1-AC7 are satisfied with cited evidence.
- The contract file is types-only (no class body, no `new`, no runtime statement
  beyond declarations and at most one literal version constant).
- All existing fragment contracts and registries are unchanged.
- `GatewayErrorEnvelope.credentialShielded` is typed as literal `true`.
- `npm run check` and `npm test` PASS in `EXTENSIONS/CVF_MODEL_GATEWAY/`.
- The pre-closure autorun gate PASSes on the material range.

The reviewer must not accept memory-only claims; real diff and gate output are
required. Reviewer-allowed repairs are limited to GC-051 registry entries,
completion review, work-order status field, and session continuity.

## Closure Checklist

- [ ] Fresh GC-018 baseline exists and is cited.
- [ ] Operator authorization exists and is cited.
- [ ] Worker return records changed files, gate output, and AC evidence.
- [ ] Contract file is types-only (AC1).
- [ ] Existing fragment contracts unchanged (AC2).
- [ ] Type reuse confirmed (AC3).
- [ ] Type-level tests pass (AC4).
- [ ] Boundary definition doc states fragment coverage vs. unified interface additions (AC5).
- [ ] `rawMemoryReleased=false` on all closure artifacts (AC6).
- [ ] No live/provider proof used (AC7).
- [ ] GC-051 registry entries added for the new contract and test files.
- [ ] `MGW-001` coverage note recorded: stays `PARTIAL_RECHECK_REQUIRED`.
- [ ] Pre-closure autorun gate PASS on the material range.
- [ ] Completion review authored with disposition.
- [ ] Session continuity synced (front door, state, handoff).

## Operator Checkpoint

The operator must intervene only for:

- Scope expansion beyond the P3 contract boundary.
- A decision to authorize the future runtime `UnifiedGatewayInterface`
  implementation (a separate GC-018 and work order required).
- Any request to lift a forbidden-scope boundary (provider/live, public-sync,
  existing-source mutation, governance-kernel surface).

No operator checkpoint is parked inside the normal worker-to-reviewer flow;
routine allowed-scope repairs proceed under the Worker Autonomy /
No-Question Rule without operator escalation.

## Verification

Pre-closure autorun gate:

```sh
python governance/compat/run_agent_autorun_workflow_gate.py \
  --phase pre-closure --base c6c09ae3 --head HEAD
```

Must PASS on the material closure commit range before completion review declares ACCEPT.

Pre-commit hook runs automatically at every `git commit`.

---

## Return-To-Orchestrator Conditions

- `COMPLETE_PENDING_REVIEW` -- all deliverables authored, worker gates PASS, no commit.
- `BLOCKED_SCOPE_EXPANSION` -- repair would cross forbidden boundary.
- `BLOCKED_MISSING_AUTHORIZATION` -- GC-018 or operator authorization absent.

Worker must NOT commit, sync session state, or upgrade work-order status.

---

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude (orchestrator role -- authoring dispatch package) |
| Provider or surface | Claude Code (VSCode extension) |
| Session or invocation | 2026-06-15 P3 dispatch from HEAD `c6c09ae3` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read (source files, P2 roadmap, rewrite plan), Write (roadmap, GC-018, work order, contract, tests, boundary doc, GC-051 entries, worker return), Edit (index.ts barrel), Generate (GC-051 aggregate) |
| Target paths | P3 roadmap, GC-018 baseline, work order, contract file, barrel edit, test file, boundary doc, GC-051 entries, aggregate registry, worker return |
| Allowed scope source | Operator instruction 2026-06-15; P2 closure at `c6c09ae3`; nextAllowedMove in session state |
| Before status evidence | `git status --short` empty; HEAD `c6c09ae3` |
| After status evidence | `git status --short` shows the P3 material package before commit; HEAD still `c6c09ae3` |
| Diff evidence | `git diff --check` PASS; no staged changes to existing files |
| Approval boundary | Operator authorized; fresh GC-018 exists; work order status DISPATCHED |
| Claim boundary | Repo-local trace only; no OS-level attribution, endpoint telemetry, public readiness, or production readiness claim |
| Agent type | Claude (orchestrator / worker) |
| Invocation ID | Dispatch from HEAD `c6c09ae3` on 2026-06-15 |
| Expected manifest | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-interface-contract.test.ts`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_2026-06-15.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p3-unified-gateway-interface-contract-tests.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p3-unified-gateway-interface-contract.json`; `docs/reference/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_BOUNDARY_DEFINITION_2026-06-15.md`; `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_WORKER_RETURN_2026-06-15.md`; `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_ROADMAP_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_FOR_CLAUDE_2026-06-15.md` |
| Actual changed set | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/tests/unified-gateway-interface-contract.test.ts`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_2026-06-15.md`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p3-unified-gateway-interface-contract-tests.json`; `docs/corpus-intelligence/registry/entries/model-gateway-c02-p3-unified-gateway-interface-contract.json`; `docs/reference/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_BOUNDARY_DEFINITION_2026-06-15.md`; `docs/reviews/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_WORKER_RETURN_2026-06-15.md`; `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_ROADMAP_2026-06-15.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P3_UNIFIED_GATEWAY_INTERFACE_FOR_CLAUDE_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no protected path deleted or renamed |
