# CVF Agent Work Order: Model Gateway C-02 P2 Dynamic Model Registry Boundary - 2026-06-15

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Worker: Claude

Orchestrator / reviewer: Codex

Worker commit policy: WORKER_MUST_NOT_COMMIT

Commit mode: WORKER_MUST_NOT_COMMIT

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md`
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_COMPLETION_2026-06-15.md`
- `docs/corpus-intelligence/registry/entries/model-gateway-c02-p2-dynamic-model-registry-contract.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`

dispatchBaseHead: 1ec2f2b4

executionBaseHead: e01d298c

closureBaseHead: 24d455f8

rawMemoryReleased=false

riskCeiling: R1 (additive contract/types/doc/tests in one extension; no runtime logic, no provider/live/public, no mutation of existing registries)

## Authorization Preconditions (BLOCKING)

This work order is a contract-first planning tranche. Dispatch authorization is
released because both prerequisites are now satisfied:

1. A fresh GC-018 baseline authorizes Model Gateway C-02 P2 dynamic model
   registry boundary, citing
   `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_ROADMAP_2026-06-15.md`.
   Expected baseline path:
   `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md`.
2. Operator authorized the P2 scope and Claude/Codex worker-reviewer assignment
   in the 2026-06-15 session instruction: "commit de Claude thi cong".

Closure status is `CLOSED_PASS_BOUNDED` after material implementation commit
`24d455f8` and reviewer closure conversion.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance contract-first planning work order. Public-sync is
not authorized by this work order. Public catalog update is deferred to a later
capability tranche if a future implementation reaches a proven status.

## Claim Boundary

This work order authorizes only the C-02 P2 dynamic model registry boundary
contract definition inside `EXTENSIONS/CVF_MODEL_GATEWAY/`. It authorizes a
types-only contract file, a boundary definition document, type-level tests, and
the GC-051 registry entry for the new file. It does NOT authorize the runtime
`DynamicModelRegistry` class implementation, query execution, health-poll
scheduling, the unified gateway interface (P3), strategy-layer components, AI
Gateway absorption, provider/API calls, live proof, public-sync, mutation of
`PROVIDER_CAPABILITY_REGISTRY` or `ProviderRegistry`, governance-kernel changes,
or production/public readiness claims.

---

## Purpose

Define the Dynamic Model Registry (DMR) boundary as a doc/contract-first
artifact so that P3 (unified gateway interface) and any future implementation
tranche reference a governed registry contract rather than an undefined backend.

The roadmap closed the advisory legacy value key
`dynamicModelRegistryWithHealthMonitoring` (`INCLUDE_IN_BOUNDARY`). P2 fulfills
that recommendation by:

1. Authoring a types-only contract file (`dynamic-model-registry-contract.ts`)
   declaring `ModelTier`, `DynamicModelRecord`, `FindOptimalQuery`, and
   `DynamicModelRegistryContract`.
2. Authoring a boundary definition document that states the merge-strategy
   boundary between the existing static `PROVIDER_CAPABILITY_REGISTRY`, the
   runtime `ProviderRegistry`, and the future `DynamicModelRegistry`.
3. Adding type-level (compile-time) tests proving the contract shapes are
   internally consistent and reuse existing Model Gateway types where applicable.
4. Adding the GC-051 corpus scan registry entry for the new source file.

The contract file MUST contain only interfaces and type aliases. It MUST NOT
contain a class body, runtime logic, `new` calls, or any executable statement
beyond type declarations.

## Scope / Applies To

Applies to: `EXTENSIONS/CVF_MODEL_GATEWAY/` only (one new source file, one
barrel export edit, one new test file) plus reviewer-owned closure docs.

Governs: the DMR contract boundary (P2). Reuses existing Model Gateway types.
Does NOT govern P3 gateway interface, runtime DMR implementation, strategy
layer, AI Gateway, EPF, facades, or provider adapters.

---

## Authority Chain

| Authority | Role |
| --- | --- |
| `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md` (expected) | Implementation authorization for C-02 P2 |
| Operator instruction on 2026-06-15 | Approves P2 scope and worker/reviewer assignment |
| `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_ROADMAP_2026-06-15.md` | P2 roadmap: scope, deliverables, contract sketch, acceptance criteria |
| `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | Closed C-02 plan; `dynamicModelRegistryWithHealthMonitoring` disposition (line 180) |
| `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` row `MGW-001` | Legacy coverage status `PARTIAL_RECHECK_REQUIRED` |
| `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md` | Accepted value key `dynamicModelRegistryWithHealthMonitoring` |
| This work order | Worker execution scope |
| Reviewer agent | Closure, commits, allowed repairs, session sync |

`AGENTS.md` is canonical CVF authority and must be read as active governance
instruction. Provider-specific memory files (`CLAUDE.md`, Codex memory, Claude
memory, IDE summaries) are NOT CVF source authority. Re-verify every named source
token against governed runtime source before completion.

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
| --- | --- |
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row id | `MGW-001` |
| Coverage status | `PARTIAL_RECHECK_REQUIRED` |
| Release basis | C-02 planning closed `RESUME_WITH_REWRITE`; P2 is the dynamic-model-registry-boundary subset of the rewrite plan |
| Required disposition in worker return | Confirm P2 implements only the `dynamicModelRegistryWithHealthMonitoring` boundary contract; all other accepted value keys remain deferred |
| Forbidden shortcut | Do not implement the runtime DMR class, P3 gateway interface, or strategy-layer keys under this P2 work order |
| P2 closure coverage note | Reviewer notes at P2 closure that `MGW-001` stays `PARTIAL_RECHECK_REQUIRED` until P3 also closes; P2 closure alone does not upgrade the row to `COVERED_SOURCE_BACKED` |

## Freeze Posture Disposition

| Field | Evidence |
| --- | --- |
| Active freeze posture | `governance_kernel_freeze_recommended` (`CVF_SESSION/ACTIVE_SESSION_STATE.json`) |
| Freeze rule | `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md` |
| Kernel surface check | `CVF_MODEL_GATEWAY` is NOT one of the 12 governance-kernel owner-map surfaces; the active owner map does not list it. Freeze release is NOT required. |
| Disposition | Contract-first work permitted under fresh GC-018; no freeze-release packet required because no governance-kernel surface is touched |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Orchestrator / reviewer / committer | Reviewer agent | Review returned contract/doc/tests, run gates, author closure artifact, commit accepted artifacts, sync session continuity |
| Worker | Worker agent | Author P2 contract + doc + type tests only, run worker gates, return `COMPLETE_PENDING_REVIEW` without committing |
| Operator | Human operator | Authorizes scope and assignment; approves any scope change |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | Operator authorized the prepared Model Gateway C-02 P2 dynamic model registry boundary roadmap and asked for a work order to dispatch implementation |
| Scope classification | bounded R1 single-extension Model Gateway contract/doc/type-test authoring plus governed worker-return evidence |
| Risk sensitivity | No public-sync, no provider/live proof, no secrets, no runtime logic, no production/readiness claim; mutation is limited to one new source file, one barrel export, one new test under `EXTENSIONS/CVF_MODEL_GATEWAY/` |
| Selected route mode | SINGLE_AGENT_MULTI_ROLE (operator may instead assign separate worker and reviewer agents) |
| routeMode | SINGLE_AGENT_MULTI_ROLE |
| Role separation basis | Phase gates, separate base heads, worker no-commit boundary, reviewer closure conversion, committed-range closure checks |
| Escalation condition | Stop for scope expansion beyond the P2 contract boundary, runtime implementation, provider/live proof, public-sync, secrets, package install, registry mutation, governance-kernel mutation, destructive action, or P3/strategy-layer work |
| Disposition | CLOSED_PASS_BOUNDED |

## Single-Agent Multi-Role Control Block

| Field | Decision |
| --- | --- |
| Single agent owns implementation and review | YES if operator assigns multi-role, bounded by this block and operator authorization |
| Role separation ledger | Orchestrator owns GC-018 and dispatch update; worker owns contract/doc/tests and worker return; reviewer owns closure artifact and acceptance; committer owns commits and session sync |
| Evidence basis independent of memory-only claims | GC-018, work order, source verification, type-level tests, diff evidence, governance gates |
| Self-review boundary | Independent review is not claimed; reviewer must inspect real diff and gate evidence before any commit |
| Gate sequence | pre-dispatch by orchestrator, baseline tests by worker, type-level tests by worker, reviewer-fast and pre-closure by reviewer, pre-push only if a later push is authorized |
| Escalation conditions | Stop for forbidden paths, runtime/P3/strategy scope, provider/live proof, public-sync, secrets, package install, registry mutation, governance-kernel mutation, destructive action, or readiness/public claims |
| Worker | Assigned worker role |
| Reviewer / committer | Assigned reviewer and committer roles |
| Human escalation checkpoint | Scope expansion only |
| Collusion boundary | Single-agent result is bounded governance evidence, not independent review |

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_COMPLETION_2026-06-15.md`

reviewerOwnedClosurePaths:
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_COMPLETION_2026-06-15.md`
- `docs/corpus-intelligence/registry/entries/model-gateway-c02-p2-dynamic-model-registry-contract.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`

Reviewer role must convert a successful handoff packet into a completion review,
run closure gates on the committed range, commit accepted artifacts, and then
sync session continuity in a separate handoff commit if required.

## Pre-Flight Checks

Worker must:

1. Capture `executionBaseHead` (`git rev-parse HEAD`).
2. Run `git status --short` and confirm clean worktree (stop if unrelated dirty files exist).
3. Confirm the fresh GC-018 baseline and operator authorization both exist; stop if either is missing.
4. Read all Required First Reads.
5. Re-read the current source baseline files and re-confirm their line ranges
   (the roadmap requires re-read at dispatch time).
6. Run the baseline test suite for `CVF_MODEL_GATEWAY` to capture a green pre-state.

## Write Ownership

Worker may write only:

- New contract source file `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` (create)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (edit, exports only)
- New test file `EXTENSIONS/CVF_MODEL_GATEWAY/tests/dynamic-model-registry-contract.test.ts` (create)
- New boundary definition doc `docs/reference/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_DEFINITION_2026-06-15.md` (create)
- The worker return
  `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_WORKER_RETURN_2026-06-15.md` (create)

Reviewer owns the completion review, commits, session sync, the GC-051 registry
entry, and the `MGW-001` coverage note. Worker must NOT write to any other
extension, any session/handoff/registry file, the existing
`provider-capability-registry.ts` or `provider-registry.ts`, or any
governance-kernel surface.

Allowed scope:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/dynamic-model-registry-contract.test.ts`
- `docs/reference/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_DEFINITION_2026-06-15.md`
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_WORKER_RETURN_2026-06-15.md`
- (reviewer-owned at closure) `docs/corpus-intelligence/registry/entries/model-gateway-c02-p2-dynamic-model-registry-contract.json`
- (reviewer-owned at closure) `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- (reviewer-owned at closure) `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md`
- (reviewer-owned at closure) `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_COMPLETION_2026-06-15.md`
- (reviewer-owned session sync) `CVF_SESSION_MEMORY.md`
- (reviewer-owned session sync) `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- (reviewer-owned session sync) `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- (reviewer-owned session sync) `CVF_SESSION/state/entries/modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615.json`
- (reviewer-owned session sync) `CVF_SESSION/state/entries/nextAllowedMove.json`
- (reviewer-owned session sync) `AGENT_HANDOFF_V18_2026-06-12.md`

The `docs/corpus-intelligence/` paths are reviewer-owned GC-051 closure coverage
for the new governed source file, not Model Gateway runtime registry or legacy
coverage index mutation.

The session-sync paths are reviewer-owned continuity updates only. They do not
authorize runtime, provider, public-sync, or governance-kernel behavior changes.

## Required First Reads

| File | Required use |
| --- | --- |
| `AGENTS.md` | active governance instructions and provider-memory boundary |
| `CVF_SESSION_MEMORY.md` | current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated state registry; freeze posture |
| `AGENT_HANDOFF_V18_2026-06-12.md` | active handoff and parked checkpoints |
| `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_ROADMAP_2026-06-15.md` | P2 scope, deliverables, contract sketch, acceptance criteria |
| `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | `dynamicModelRegistryWithHealthMonitoring` disposition |
| The fresh GC-018 baseline | implementation authorization and blind-spot block |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | worker return and closure structure |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Agent Operation Trace Block contract |
| `docs/reference/CVF_TEXT_ENCODING_AND_SYMBOL_DISCIPLINE_STANDARD_2026-06-07.md` | ASCII discipline for authored text |
| `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | GC-023 thresholds (`.ts` hard=1000, advisory=700; `.test.ts` hard=1200, advisory=800) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | current `PROVIDER_CAPABILITY_REGISTRY`; static method-capability table (READ ONLY) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRegistry`, `ProviderRecord`, `ProviderModel`, `ProviderStatus`, `GatewayRiskClass`, `isRoutable` (READ ONLY) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | `ProviderMethodName` union (reuse in contract) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | `ProviderHealthState`, `ProviderHealthRecord` (reconcile DMR health field) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | P1 `RoutingRequest` (contract must be compatible, not edited) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | barrel exports; what P2 must add to public surface |

Do not read broad `.private_reference/legacy/` content. Use the governed roadmap
and rewrite plan as legacy authority.

## Source Verification Block

Disposition column uses the dispatch standard values only: `ACCEPT`,
`REJECT`, or `BLOCKED_SOURCE_NOT_FOUND`. All rows are `ACCEPT` because every
symbol was verified to exist at the cited definition line on 2026-06-15.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Implementation action | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| EXISTS: ProviderMethodName | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | line 1 | `ProviderMethodName` | provider method contract | REUSE_IN_CONTRACT | ACCEPT |
| EXISTS: ProviderStatus | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 2 | `ProviderStatus` | provider registry | REUSE_IN_CONTRACT | ACCEPT |
| EXISTS: GatewayRiskClass | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 1 | `GatewayRiskClass` | provider registry | MAY_REUSE | ACCEPT |
| EXISTS: ProviderModel | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 4 | `ProviderModel` | provider registry | REFERENCE_ONLY | ACCEPT |
| EXISTS: ProviderRecord | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 13 | `ProviderRecord` | provider registry | REFERENCE_ONLY | ACCEPT |
| EXISTS: ProviderRegistry.isRoutable | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 72 | `isRoutable` | provider registry | BOUNDARY_REFERENCE | ACCEPT |
| EXISTS: PROVIDER_CAPABILITY_REGISTRY | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | BOUNDARY_REFERENCE | ACCEPT |
| EXISTS: ProviderHealthState | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 1 | `ProviderHealthState` | provider health | REUSE_FOR_HEALTH_FIELD | ACCEPT |
| EXISTS: ProviderHealthRecord | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 7 | `ProviderHealthRecord` | provider health | RECONCILE_REFERENCE | ACCEPT |
| EXISTS: RoutingRequest | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 13 | `RoutingRequest` | routing policy | COMPAT_REFERENCE | ACCEPT |
| EXISTS: model gateway barrel exports | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | export blocks lines 60-73 | provider/health type re-exports | model gateway barrel | EXTEND_EXPORTS | ACCEPT |

Note: `provider-capability-registry.ts` is 94 lines and `provider-registry.ts`
is 99 lines as of 2026-06-15 (verified by `Measure-Object -Line`). The worker
must re-confirm these at execution time.

## Negative Search And Collision Discipline

Evidence coverage spans all required domains: source files, tests, docs, JSON
registry entries, and external evidence. The structured query, search roots,
and absent-versus-collision disposition are recorded per row.

| Structured query / search command | Search roots | Coverage domain | Expected result / collision result | Absent-versus-collision disposition |
| --- | --- | --- | --- | --- |
| `rg -n "DynamicModelRegistry\|DynamicModelRecord\|FindOptimalQuery\|ModelTier" --hidden --no-ignore .` | all source, tests, docs, JSON, and external evidence roots | source + tests + docs + json + external | Zero current occurrence of these P2 contract symbols; no same-token collision exists anywhere | ABSENT (not a collision); SAFE_TO_ADD, binding |
| `rg -n "findOptimal" EXTENSIONS/CVF_MODEL_GATEWAY` | Model Gateway source and tests | source + tests | No existing `findOptimal` occurrence in Model Gateway source or tests | ABSENT; SAFE_TO_ADD, binding |
| `rg -n "ProviderHealthState\|ProviderStatus\|ProviderMethodName" EXTENSIONS/CVF_MODEL_GATEWAY/src` | Model Gateway source | source | Existing reusable types; the same-token occurrence is the authoritative definition the contract imports | COLLISION_IS_AUTHORITATIVE_SOURCE; contract must import, not redeclare; binding |

Collision note: the contract MUST reuse `ProviderMethodName`, `ProviderStatus`,
and `ProviderHealthState` by import. It MUST NOT redeclare a parallel health or
status union. The roadmap sketch used a 3-value health placeholder; the worker
MUST instead reuse the existing 5-value `ProviderHealthState`
(`healthy | degraded | rate_limited | unavailable | unknown`) for the DMR health
field, and record this reconciliation in the worker return.

## Current Runtime Freshness Verification

| Runtime/source surface | Freshness check | Expected |
| --- | --- | --- |
| Provider capability registry | `rg -n "PROVIDER_CAPABILITY_REGISTRY" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | found at line 43 |
| Provider registry types | `rg -n "ProviderStatus\|GatewayRiskClass\|ProviderRecord" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | found |
| Provider health types | `rg -n "ProviderHealthState\|ProviderHealthRecord" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | found |
| Provider method name | `rg -n "ProviderMethodName" EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | found at line 1 |

## Evidence Requirements

The worker must provide source-backed evidence for every claim in the worker
return:

- Each reuse claim: cite the imported type and its source line.
- The types-only claim: `git diff` of the new contract file showing zero class
  bodies, zero `new`, zero runtime statements.
- The existing-registries-unchanged claim: `git diff --name-status` and
  `git status --short` showing NO change to `provider-capability-registry.ts` or
  `provider-registry.ts`.
- The no-provider/no-live claim: changed file set is limited to the new contract
  file, the barrel export edit, the new test file, the boundary definition doc,
  and the worker return.
- The no-commit claim: `git rev-parse HEAD` equal to `executionBaseHead`.
- Type-check and test results: actual command output summaries, not predicted
  results.
- The health-reconciliation claim: cite that the DMR health field reuses the
  5-value `ProviderHealthState`.

Evidence may be command-output summaries, cited governed file lines/sections, or
explicit N/A with reason where a proof class does not apply.

## Implementation Specification

### IS-1: Contract file (types only)

Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts`
containing ONLY type aliases and interfaces. Import reusable types from existing
Model Gateway source; do not redeclare them.

Required declarations (final field names at worker discretion if documented in
the worker return; keep camelCase consistent with the existing files):

- `ModelTier` -- a string-literal union. Recommended:
  `"frontier" | "standard" | "economy" | "experimental"`.
- `DynamicModelRecord` -- interface with at minimum: `providerId: string`,
  `modelId: string`, `tier: ModelTier`,
  `supportedMethods: ProviderMethodName[]` (imported), optional
  `maxContextTokens?: number`, optional `costPerInputToken?: number`,
  optional `costPerOutputToken?: number`,
  optional `latencyClass?: "low" | "medium" | "high"`,
  optional `rateLimit?: { requestsPerMinute: number; tokensPerMinute?: number }`,
  optional `healthState?: ProviderHealthState` (imported, 5-value),
  `status: ProviderStatus` (imported).
- `FindOptimalQuery` -- interface with at minimum:
  `requiredMethod: ProviderMethodName` (imported), optional
  `preferredTier?: ModelTier`, optional `maxCostPerInputToken?: number`,
  optional `latencyClass?: "low" | "medium" | "high"`, optional
  `allowExperimental?: boolean`, optional `allowedProviderIds?: string[]`,
  optional `blockedProviderIds?: string[]`.
- `DynamicModelRegistryContract` -- interface declaring method signatures only
  (no bodies):
  - `getModel(providerId: string, modelId: string): DynamicModelRecord | undefined;`
  - `findOptimal(query: FindOptimalQuery): DynamicModelRecord[];`
  - `listRoutable(options?: { allowExperimental?: boolean }): DynamicModelRecord[];`

The worker MAY add a `DYNAMIC_MODEL_REGISTRY_CONTRACT_VERSION` string constant
(e.g. `"cvf.dynamicModelRegistry.v1"`) for downstream version pinning, since a
single `export const` of a literal is a declaration, not runtime logic. Any
other executable statement is forbidden.

### IS-2: Barrel exports

Add the new types to `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` using a
`export type { ... } from "./dynamic-model-registry-contract"` block (and a
separate `export { DYNAMIC_MODEL_REGISTRY_CONTRACT_VERSION }` value export if the
constant is added). Do not collide with existing exported names.

### IS-3: Boundary definition document

Create
`docs/reference/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_DEFINITION_2026-06-15.md`
stating the merge-strategy boundary explicitly:

- `PROVIDER_CAPABILITY_REGISTRY` remains authoritative for method-capability
  validation (`supportedMethods` truth source at deploy time).
- `ProviderRegistry` remains authoritative for runtime routable-provider
  decisions (`isRoutable`, `assertAllowed`).
- The future `DynamicModelRegistry` (NOT implemented in P2) merges static
  capability facts + runtime health state + tier/cost/latency metadata.
- P2 mutates neither existing registry.

The doc must include the standard governed-markdown structural sections so it
passes the markdown structural completeness gate (Purpose, Scope, a
claim/verification boundary section). Keep it ASCII-disciplined.

### IS-4: Type-level tests

Create
`EXTENSIONS/CVF_MODEL_GATEWAY/tests/dynamic-model-registry-contract.test.ts`
with compile-time / type-level assertions only. No network, no provider call, no
runtime registry instantiation. Acceptable patterns:

- Construct sample `DynamicModelRecord` and `FindOptimalQuery` object literals
  typed against the contract and assert their shape with a trivial runtime
  assertion (e.g. `expect(record.tier).toBe("frontier")`).
- Provide a local stub object that satisfies `DynamicModelRegistryContract`
  (returning empty arrays / undefined) purely to prove the interface is
  implementable; this stub lives in the TEST file only, never in src.
- Assert that `supportedMethods` accepts a `ProviderMethodName` value and that
  `healthState` accepts a `ProviderHealthState` value, proving the imports line
  up.

### IS-5: File-size discipline (GC-023)

The new contract file should be well under the `.ts` advisory threshold (700).
The test file must stay under the `.test.ts` advisory threshold (800). Do not
exceed any hard threshold.

## Test Specification

| Test | Requirement |
| --- | --- |
| Contract shape | Sample `DynamicModelRecord` and `FindOptimalQuery` literals type-check and a trivial field assertion passes |
| Interface implementable | A test-local stub satisfies `DynamicModelRegistryContract` and compiles |
| Type reuse | `supportedMethods` accepts `ProviderMethodName`; `healthState` accepts `ProviderHealthState`; `status` accepts `ProviderStatus` |
| No runtime logic in src | The src contract file contains no class body, no `new`, no executable statement beyond declarations |
| Existing suite intact | `CVF_MODEL_GATEWAY` `npm test` continues to pass with the new test added |

## Scope

Allowed:

- Create `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts` (types only).
- Edit `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` to export new types.
- Create the type-level test under `EXTENSIONS/CVF_MODEL_GATEWAY/tests/`.
- Create the boundary definition doc under `docs/reference/`.
- Run local type checks and the affected test suites.
- Write the single worker return documentation file under `docs/reviews/`.

Forbidden:

- Runtime `DynamicModelRegistry` class implementation, query execution logic,
  health-poll scheduling, or any executable statement beyond type declarations
  and one optional version constant in the contract file.
- P3 unified gateway interface, strategy-layer components (Execution Planner,
  Strategy Taxonomy, Feedback Loop).
- Editing `provider-capability-registry.ts`, `provider-registry.ts`,
  `provider-health.ts`, `routing-policy.ts`, `routing-policy-pipeline.ts`, or any
  extension other than `CVF_MODEL_GATEWAY`.
- Provider/API calls, live governance proof, provider/model addition, package
  install, secret inspection, public-sync, public catalog claim.
- Registry mutation (legacy coverage index, corpus scan registry) by the worker;
  the GC-051 entry is reviewer-owned at closure.
- Session-state, handoff, front-door, or active review queue mutation.
- Governance-kernel surface changes; AI Gateway absorption; OS/endpoint control.
- Autonomous mutation; commit.

Risk ceiling: R1 single-extension contract-first definition.

## Execution Plan

| Step | Input | Action | Output | Stop condition |
| --- | --- | --- | --- | --- |
| 1 | Required first reads + GC-018 + operator auth | Capture executionBaseHead; confirm authorizations; re-confirm source baseline line ranges; run baseline tests green | preflight evidence | Stop if GC-018/operator auth missing or baseline red |
| 2 | provider-method-contract.ts, provider-registry.ts, provider-health.ts | Implement IS-1 contract file importing reusable types | types-only contract | Stop if a reused type does not exist or a runtime statement would be required |
| 3 | index.ts | Implement IS-2 exports without collision | updated barrel | Stop on export name collision |
| 4 | boundary inputs | Implement IS-3 boundary definition doc | governed doc | Stop if the doc would claim runtime or readiness |
| 5 | contract | Implement IS-4 type-level tests | passing tests | Stop if a test would require runtime registry instantiation |
| 6 | gates | Run type check, MG tests, reviewer-fast | evidence in worker return | Stop and repair allowed-scope issues before return |

## Worker Pending-Return Gate

| Gate | Required evidence | Status |
| --- | --- | --- |
| Authorizations present | GC-018 baseline + operator authorization cited | PASS |
| Scope-limited mutation | Changes limited to the new contract file, barrel edit, new test, boundary doc, GC-051 entries, aggregate, and worker return | PASS |
| Existing registries unchanged | `provider-capability-registry.ts` and `provider-registry.ts` show zero diff | PASS |
| Types-only contract | Contract file has no class body, no `new`, no runtime statement beyond declarations and one literal version constant | PASS |
| Type reuse | `ProviderMethodName`, `ProviderStatus`, `ProviderHealthState` imported, not redeclared | PASS |
| Health reconciliation | DMR health field reuses 5-value `ProviderHealthState`; recorded in worker return | PASS |
| New tests present | Shape, implementable-interface, type-reuse cases added | PASS |
| Type check | Model Gateway `npm run check` PASS | PASS |
| Test run | Model Gateway `npm test` PASS, 22 files / 105 tests | PASS |
| GC-023 | No touched `.ts`/`.test.ts` file exceeds its hard threshold | PASS |
| No provider/live | No provider/API/live proof, model addition, package install, or secret read | PASS |
| Name collision avoided | New symbols `ModelTier`, `DynamicModelRecord`, `FindOptimalQuery`, `DynamicModelRegistryContract` have no prior occurrence before P2 | PASS |
| Agent Operation Trace Block | Expected and actual changed set recorded | PASS |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` in worker return and completion | PASS |
| Worker did not commit | HEAD stayed `executionBaseHead` through worker return | PASS |
| Diff hygiene | `git diff --check` PASS, CRLF warnings only | PASS |
| Reviewer-fast | `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base e01d298c --head HEAD --enforce` PASS | PASS |

## Worker Autonomy / No-Question Rule

Allowed-scope failures (type errors, failing new tests, missing sections, trace
updates, diff hygiene, GC-023 file split, markdown structural sections, ASCII
encoding) must be repaired and rerun without escalation.

Worker must stop and return `BLOCKED_SCOPE_EXPANSION` only when a repair would:
require editing an extension other than `CVF_MODEL_GATEWAY`; require editing the
existing `provider-capability-registry.ts` / `provider-registry.ts` /
`provider-health.ts` / `routing-policy.ts`; require runtime registry
implementation; require a provider/API/live call; require package install,
secret access, public-sync, registry mutation, session-state mutation,
governance-kernel mutation, or any destructive action.

## Acceptance Criteria

| # | Criterion | Verification |
| --- | --- | --- |
| AC1 | `dynamic-model-registry-contract.ts` contains only interfaces, type aliases, and at most one literal version constant | `git diff` of the file; no class body, no `new`, no executable statement |
| AC2 | `provider-capability-registry.ts` and `provider-registry.ts` unchanged | `git diff --name-status` shows no change to either file |
| AC3 | Contract reuses `ProviderMethodName`, `ProviderStatus`, `ProviderHealthState` by import | cited import lines |
| AC4 | Type-level tests compile and pass | `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY/` |
| AC5 | Boundary definition doc states the merge-strategy boundary | doc section content |
| AC6 | `rawMemoryReleased=false` on all closure artifacts | front-matter literal |
| AC7 | No live provider calls, network traffic, or API keys used | changed file set + worker statement |

## Verification

Two distinct gate runs are required:

Pre-closure autorun gate (closure evidence):

```sh
python governance/compat/run_agent_autorun_workflow_gate.py \
  --phase pre-closure --base <dispatchBaseHead> --head HEAD
```

Must PASS on the material closure commit range before the completion review can
declare ACCEPT. This is the governed closure gate, not the commit hook.

Pre-commit hook (commit gate):

```sh
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

Runs automatically at every `git commit`. Passes are necessary but not
sufficient for closure.

Closure is `CLOSED_PASS_BOUNDED` when the completion review disposition is
ACCEPT or ACCEPT_AFTER_REVIEWER_REPAIR, the pre-closure autorun gate PASSes on
the material range, and the pre-commit hook PASSes on the closure commit.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap deliverable | Roadmap ref | Work order section | Owner |
| --- | --- | --- | --- |
| D1 GC-018 baseline | roadmap Deliverables D1 | Authorization Preconditions | reviewer/operator |
| D2 Work order | roadmap Deliverables D2 | this document | reviewer |
| D3 DMR contract file | roadmap Deliverables D3 | IS-1, Write Ownership | worker |
| D4 Boundary definition doc | roadmap Deliverables D4 | IS-3 | worker |
| D5 Type-level tests | roadmap Deliverables D5 | IS-4, Test Specification | worker |
| D6 GC-051 registry entry | roadmap Deliverables D6 | Reviewer Closure Conversion Block | reviewer |
| D7 Worker return | roadmap Deliverables D7 | Write Ownership | worker |
| D8 Completion review | roadmap Deliverables D8 | Reviewer Closure Conversion Block | reviewer |
| AC1 types-only | roadmap AC1 | Acceptance Criteria AC1 | worker |
| AC2 registries unchanged | roadmap AC2 | Acceptance Criteria AC2 | worker |
| AC3 type tests pass | roadmap AC3 | Acceptance Criteria AC4 | worker |
| AC4 GC-051 entry | roadmap AC4 | Reviewer Closure Conversion Block | reviewer |
| AC5 merge boundary doc | roadmap AC5 | IS-3, Acceptance Criteria AC5 | worker |
| AC6 rawMemoryReleased=false | roadmap AC6 | Acceptance Criteria AC6 | worker/reviewer |
| AC7 no live | roadmap AC7 | Acceptance Criteria AC7 | worker |

## Review Gate

The reviewer must verify, on the committed range, before declaring ACCEPT:

- All Acceptance Criteria AC1-AC7 are satisfied with cited evidence.
- The contract file is types-only (no class body, no `new`, no runtime statement
  beyond declarations and at most one literal version constant).
- `provider-capability-registry.ts` and `provider-registry.ts` are unchanged.
- The DMR health field reuses the 5-value `ProviderHealthState`.
- `npm run check` and `npm test` PASS in `EXTENSIONS/CVF_MODEL_GATEWAY/`.
- The pre-closure autorun gate PASSes on the material range.

The reviewer must not accept memory-only claims; real diff and gate output are
required. Reviewer-allowed repairs are limited to the GC-051 registry entry, the
completion review, the work-order status field, and session continuity.

## Closure Checklist

- [x] Fresh GC-018 baseline exists and is cited.
- [x] Operator authorization exists and is cited.
- [x] Worker return records changed files, gate output, and AC evidence.
- [x] Contract file is types-only (AC1).
- [x] Existing registries unchanged (AC2).
- [x] Type reuse confirmed (AC3).
- [x] Type-level tests pass (AC4).
- [x] Boundary definition doc states the merge-strategy boundary (AC5).
- [x] `rawMemoryReleased=false` on all closure artifacts (AC6).
- [x] No live/provider proof used (AC7).
- [x] GC-051 registry entry added for the new contract file and tests.
- [x] `MGW-001` coverage note recorded: stays `PARTIAL_RECHECK_REQUIRED`.
- [x] Material pre-closure autorun gate run on `e01d298c..24d455f8`; material gates PASS and active-session sync is handled by reviewer closure batch.
- [x] Completion review authored with disposition.
- [x] Session continuity synced (front door, state, handoff).

## Return-To-Orchestrator Conditions

The worker returns to the orchestrator/reviewer with one of:

- `COMPLETE_PENDING_REVIEW` -- all in-scope deliverables authored, worker gates
  PASS, no commit performed, worker return written.
- `BLOCKED_SCOPE_EXPANSION` -- a required repair would cross the forbidden
  boundary (other extension, runtime implementation, existing-registry edit,
  provider/live, package install, secret, public-sync, registry/session/kernel
  mutation).
- `BLOCKED_MISSING_AUTHORIZATION` -- the GC-018 baseline or operator
  authorization is absent at pre-flight.

The worker must NOT commit, sync session state, or upgrade the work-order status
under any return condition; those are reviewer-owned.

## Operator Checkpoint

The operator must intervene only for:

- scope expansion beyond the P2 contract boundary;
- a decision to authorize the future runtime `DynamicModelRegistry`
  implementation (a separate GC-018 and work order);
- any request to lift a forbidden-scope boundary (provider/live, public-sync,
  existing-registry mutation, governance-kernel surface).

No operator checkpoint is parked inside the normal worker-to-reviewer flow;
routine allowed-scope repairs proceed under the Worker Autonomy / No-Question
Rule without operator escalation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_COMPLETION_2026-06-15.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_ROADMAP_2026-06-15.md` | Roadmap remains the planning parent; P2 closure is recorded by this work order and completion review without roadmap mutation | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 aggregate drift check PASS | PASS |
| Registry Markdown | N/A with reason: no markdown registry owner exists for this GC-051 source entry | BLOCKED with reason: JSON aggregate and per-entry source are the required registry surfaces | BLOCKED with reason |
| External evidence digest | N/A with reason: repo-local source, tests, and governance gates only | N/A_WITH_REASON | N/A with reason |
| System loop interlock | N/A with reason: P2 did not change system-loop registry or interlock surfaces | N/A_WITH_REASON | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V18_2026-06-12.md` | reviewer-owned closure sync updates current mode, next allowed move, and HEAD pointer | PASS |
| Worker return reviewed | `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_WORKER_RETURN_2026-06-15.md` | reviewer-return steward PASS and completion accepted | PASS |
| Source implementation | Model Gateway P2 source/tests named in Allowed scope | Model Gateway check/test evidence recorded in completion review | PASS |
| Public export disposition recorded | this file and completion review | `DEFERRED_PRIVATE_ONLY` | PASS |
| Runtime/provider/live proof | N/A with reason: no provider/API/live behavior claim authorized or made | N/A_WITH_REASON | N/A with reason |
| Public-sync | N/A with reason: private provenance implementation only | N/A_WITH_REASON | N/A with reason |

## Agent Operation Trace Block

This block records the reviewer closure conversion update to THIS work order.
The worker execution trace remains in the worker return.

| Field | Evidence |
| --- | --- |
| Actor | Codex reviewer / closer |
| Provider or surface | Codex CLI |
| Session or invocation | closureBaseHead `24d455f8` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, `rg`, governance gates, `apply_patch`, active-state generator, `git diff --check` |
| Target paths | this work order, completion review, active session state source/aggregate, session front door, active handoff |
| Allowed scope source | Reviewer Closure Conversion Block in this work order; completion review Core Guard Self-Protection Authorization |
| Before status evidence | material implementation commit `24d455f8`; worktree clean before closure sync |
| After status evidence | P2 closure/sync packet ready for commit |
| Diff evidence | `git status --short`; `git diff --check`; closure-sync gates |
| Approval boundary | P2 reviewer closure and session continuity only; no runtime/provider/public expansion |
| Claim boundary | Repo-local P2 contract closure only; no OS-level user attribution, endpoint telemetry, provider-internal logs, physical-machine identity, public readiness, or production readiness claim |
| Agent type | Codex |
| Invocation ID | `closureBaseHead=24d455f8` |
| Expected manifest | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V18_2026-06-12.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md`; `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_COMPLETION_2026-06-15.md` |
| Actual changed set | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V18_2026-06-12.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md`; `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_COMPLETION_2026-06-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no protected path was deleted or renamed during this authoring session |

## Runtime Boundary

This work order produces type declarations, a governed document, and type-level
tests only. No runtime `DynamicModelRegistry` exists after P2. No provider call,
network request, or live proof is performed or claimed. The future runtime
implementation requires a separate GC-018 and a source-verified implementation
work order naming this contract as the interface authority.
