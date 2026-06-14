# CVF Agent Work Order: Model Gateway C-02 P1 Routing Pipeline Implementation - 2026-06-14

Memory class: FULL_RECORD

Status: DISPATCHED_SELF_ORCHESTRATED

Worker: Codex worker role

Orchestrator / reviewer: Codex orchestrator and reviewer roles

Worker commit policy: WORKER_MUST_NOT_COMMIT

Commit mode: WORKER_MUST_NOT_COMMIT

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_COMPLETION_2026-06-14.md`

reviewerOwnedClosurePaths:
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_COMPLETION_2026-06-14.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

dispatchBaseHead: `89128582`

executionBaseHead: WORKER_MUST_CAPTURE_AFTER_DISPATCH

closureBaseHead: REVIEWER_CAPTURE_AFTER_WORKER_RETURN

rawMemoryReleased=false

riskCeiling: R2 (runtime/source/test mutation in one extension; no provider/live/public)

## Authorization Preconditions (BLOCKING)

This work order is an implementation tranche. It MUST NOT be dispatched until both:

1. A fresh GC-018 baseline authorizes Model Gateway C-02 P1 implementation,
   citing
   `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md`.
   Satisfied by
   `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_2026-06-14.md`.
2. Operator authorizes the implementation scope and worker/reviewer assignment.
   Satisfied by the 2026-06-14 operator instruction assigning Codex to assume
   multiple roles and execute this work order.

This packet is dispatched for the bounded self-orchestrated Codex execution
described above. The worker role still honors `WORKER_MUST_NOT_COMMIT`;
reviewer role owns acceptance, commit, and session sync.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation work order. Public-sync is not
authorized by this work order. Public catalog update is deferred to a later
capability tranche if the implementation reaches a proven status.

## Claim Boundary

This work order authorizes only the C-02 P1 routing pipeline implementation
inside `EXTENSIONS/CVF_MODEL_GATEWAY/`. It does not authorize the dynamic model
registry (P2), the unified gateway interface (P3), strategy-layer components,
AI Gateway absorption, provider/API calls, live proof, public-sync, registry
mutation, governance-kernel changes, or production/public readiness claims.

---

## Purpose

Implement the C-02 P1 routing pipeline boundary that the closed C-02 rewrite plan
recommended as the highest-priority next tranche:

1. Extend `RoutingRequest` and `RoutingDecision` with additive optional routing
   context fields (execution stage, complexity score, risk score, required
   capabilities, cost budget, latency budget, fallback chain).
2. Add a pluggable policy pipeline to `RoutingPolicyEngine` with a routing-scoped
   `RoutingStageDecision` interface (NOT `PolicyDecision`, which already exists as
   a RUNTIME_ADAPTER_HUB re-export in `index.ts`), ordered stage/risk/cost
   policies, a merge engine, and an escalation policy that orchestrates the
   already-existing `FallbackPolicy`, `QuotaLedger`, and `ProviderHealthMonitor`
   primitives.

The implementation must be strictly backward compatible: the existing
`decide()` and `decideWithSnapshot()` behavior for a minimal request must be
unchanged, and the existing `CVF_GUARD_CONTRACT` phase2b coherence test must keep
passing without edits.

## Scope / Applies To

Applies to: `EXTENSIONS/CVF_MODEL_GATEWAY/` only (source + tests).

Governs: routing pipeline extension (P1). Reuses existing fallback/quota/health
primitives. Does NOT govern P2 dynamic registry, P3 gateway interface, strategy
layer, AI Gateway, EPF, facades, or provider adapters.

---

## Authority Chain

| Authority | Role |
| --- | --- |
| `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_2026-06-14.md` | Implementation authorization for C-02 P1 |
| Operator instruction on 2026-06-14 | Approves implementation scope and Codex multi-role assignment |
| `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | Closed C-02 plan; P1 scope and boundary recommendations (sections 7, 12) |
| `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md` | C-02 closure; `CLOSED_PASS_BOUNDED` |
| `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` row `MGW-001` | Legacy coverage status `PARTIAL_RECHECK_REQUIRED` |
| `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md` | Accepted value keys `routingContextFullInterface`, `routingPolicyEnginePluggablePipeline` |
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
| Release basis | C-02 planning closed `RESUME_WITH_REWRITE`; P1 is the routing-pipeline subset of the rewrite plan |
| Required disposition in worker return | Confirm P1 implements only `routingContextFullInterface` and `routingPolicyEnginePluggablePipeline`; all other accepted value keys remain deferred |
| Forbidden shortcut | Do not implement P2 dynamic registry, P3 gateway interface, or strategy-layer keys under this P1 work order |
| P1 closure coverage note | Reviewer notes at P1 closure that `MGW-001` stays `PARTIAL_RECHECK_REQUIRED` until P2/P3 also close; P1 closure alone does not upgrade the row to `COVERED_SOURCE_BACKED` |

## Freeze Posture Disposition

| Field | Evidence |
| --- | --- |
| Active freeze posture | `governance_kernel_freeze_recommended` (`CVF_SESSION/ACTIVE_SESSION_STATE.json`) |
| Freeze rule | `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md` |
| Kernel surface check | `CVF_MODEL_GATEWAY` is NOT one of the 12 governance-kernel owner-map surfaces; the active owner map does not list it. Freeze release is NOT required. |
| Disposition | Implementation permitted under fresh GC-018; no freeze-release packet required because no governance-kernel surface is touched |

## Agent Roles

| Role | Owner | Boundary |
| --- | --- | --- |
| Orchestrator / reviewer / committer | Reviewer agent | Review returned source/tests, run gates, author closure artifact, commit accepted artifacts, sync session continuity |
| Worker | Worker agent | Implement P1 source + tests only, run worker gates, return `COMPLETE_PENDING_REVIEW` without committing |
| Operator | Human operator | Authorizes implementation and assignment; approves any scope change |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake summary | Operator asked Codex to assume multiple roles and execute the prepared Model Gateway C-02 P1 routing pipeline work order |
| Scope classification | bounded R2 single-extension Model Gateway source/test implementation plus governed worker-return evidence |
| Risk sensitivity | No public-sync, no provider/live proof, no secrets, no legal/current-law, no production/readiness claim; source/test mutation is limited to `EXTENSIONS/CVF_MODEL_GATEWAY/` |
| Selected route mode | SINGLE_AGENT_MULTI_ROLE |
| Selected role route | Codex orchestrator dispatches, Codex worker implements without committing, Codex reviewer closes, Codex committer commits accepted artifacts |
| routeMode | SINGLE_AGENT_MULTI_ROLE |
| Role separation basis | Phase gates, separate base heads, worker no-commit boundary, reviewer closure conversion, and committed-range closure checks |
| Escalation condition | Stop for scope expansion beyond P1, provider/live proof, public-sync, secrets, package install, registry mutation, governance-kernel mutation, destructive action, or P2/P3/strategy-layer work |
| Disposition | DISPATCHED_SELF_ORCHESTRATED |

## Single-Agent Multi-Role Control Block

| Field | Decision |
| --- | --- |
| Single agent owns implementation and review | YES, bounded by this block and operator authorization |
| Role separation ledger | Orchestrator owns GC-018 and dispatch update; worker owns source/tests and worker return; reviewer owns closure artifact and acceptance; committer owns commits and session sync |
| Evidence basis independent of memory-only claims | GC-018, work order, source verification, focused tests, diff evidence, and governance gates |
| Self-review boundary | Independent review is not claimed; Codex reviewer must inspect real diff and gate evidence before any commit |
| Gate sequence | pre-dispatch by orchestrator, baseline tests by worker, focused implementation tests by worker, reviewer-fast and pre-closure by reviewer, pre-push only if a later push is authorized |
| Escalation conditions | Stop for forbidden paths, P2/P3/strategy scope, provider/live proof, public-sync, secrets, package install, registry mutation, governance-kernel mutation, destructive action, or readiness/public claims |
| Worker | Codex worker role |
| Reviewer / committer | Codex reviewer and committer roles |
| Human escalation checkpoint | Scope expansion only |
| Collusion boundary | Single-agent result is bounded governance evidence, not independent review |

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_COMPLETION_2026-06-14.md`

reviewerOwnedClosurePaths:
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_COMPLETION_2026-06-14.md`
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
5. Run the baseline test suite for `CVF_MODEL_GATEWAY` and `CVF_GUARD_CONTRACT` to capture a green pre-state.

## Write Ownership

Worker may write only:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` (edit)
- New routing pipeline source file(s) under `EXTENSIONS/CVF_MODEL_GATEWAY/src/`
  (recommended `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy-pipeline.ts`)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (edit, exports only)
- Test files under `EXTENSIONS/CVF_MODEL_GATEWAY/tests/`
- The worker return (suggested
  `docs/reviews/CVF_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_WORKER_RETURN_2026-06-14.md`)

Reviewer owns completion review, commits, session sync, and the `MGW-001`
coverage note. Worker must not write to any other extension, any session/handoff/
registry file, or any governance-kernel surface.

## Required First Reads

| File | Required use |
| --- | --- |
| `AGENTS.md` | active governance instructions and provider-memory boundary |
| `CVF_SESSION_MEMORY.md` | current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | generated state registry; freeze posture |
| `AGENT_HANDOFF_V18_2026-06-12.md` | active handoff and parked checkpoints |
| `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | P1 scope (sections 5, 7, 12); boundary dispositions |
| `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md` | C-02 closure |
| `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md` | accepted value keys for P1; legacy decision-pipeline detail |
| The fresh GC-018 baseline | implementation authorization and blind-spot block |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | worker return and closure structure |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Agent Operation Trace Block contract |
| `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | GC-023 thresholds (`.ts` hard=1000, advisory=700) |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | current `RoutingRequest`, `RoutingDecision`, `RoutingPolicyEngine`, snapshot builder |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderRegistry`, `ProviderRecord`, `ProviderModel`, `isRoutable` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | `ProviderHealthMonitor`, `isUsable` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | `QuotaLedger`, `QuotaDecision`, `canUse` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts` | `FallbackPolicy`, `FallbackDecision`, escalation source |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | `GatewayPolicyContext`, `GatewayPolicyResult` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | barrel exports; what P1 must add to public surface |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/routing-policy.test.ts` | existing routing tests that must keep passing |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phase2b-runtime-coherence.test.ts` | external consumer (P-06 node); must keep passing unedited |

Do not read broad `.private_reference/legacy/` content. Use the governed recheck
plan as legacy authority.

## Source Verification Block

Disposition column uses the dispatch standard values only: `ACCEPT`,
`REJECT`, or `BLOCKED_SOURCE_NOT_FOUND`. The implementation action for each
verified symbol is recorded in the separate `Implementation action` column.
All rows are `ACCEPT` because every symbol was verified to exist at the cited
definition line.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Implementation action | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| EXISTS: RoutingRequest | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 6 | `RoutingRequest` | routing policy | EXTEND_ADDITIVE | ACCEPT |
| EXISTS: RoutingDecision | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 14 | `RoutingDecision` | routing policy | EXTEND_ADDITIVE | ACCEPT |
| EXISTS: ROUTING_POLICY_CONTRACT_VERSION | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 30 | `ROUTING_POLICY_CONTRACT_VERSION` | routing policy | KEEP_STABLE | ACCEPT |
| EXISTS: RoutingPolicyContractSnapshot | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 32 | `RoutingPolicyContractSnapshot` | routing policy | EXTEND_ADDITIVE_OPTIONAL | ACCEPT |
| EXISTS: buildRoutingPolicyContractSnapshot | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 43 | `buildRoutingPolicyContractSnapshot` | routing policy | PRESERVE_SIGNATURE | ACCEPT |
| EXISTS: RoutingPolicyEngine.decide | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 67 | `decide` | routing policy engine | EXTEND_PIPELINE | ACCEPT |
| EXISTS: RoutingPolicyEngine.decideWithSnapshot | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 123 | `decideWithSnapshot` | routing policy engine | PRESERVE_BEHAVIOR | ACCEPT |
| EXISTS: orderedProviders | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 134 | `orderedProviders` | routing policy engine | MAY_REFACTOR_INTERNAL | ACCEPT |
| EXISTS: ProviderRegistry.isRoutable | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 72 | `isRoutable` | provider registry | REUSE | ACCEPT |
| EXISTS: ProviderHealthMonitor.isUsable | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 60 | `isUsable` | provider health | REUSE | ACCEPT |
| EXISTS: QuotaLedger.canUse | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | line 52 | `canUse` | quota ledger | REUSE | ACCEPT |
| EXISTS: FallbackPolicy.decide | `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts` | line 44 | `decide` | fallback policy | REUSE_FOR_ESCALATION | ACCEPT |
| EXISTS: GatewayPolicyContext | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | line 2 | `GatewayPolicyContext` | gateway policy | UPSTREAM_BOUNDARY_PRESERVED | ACCEPT |
| EXISTS: phase2b P-06 routing node uses snapshot | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phase2b-runtime-coherence.test.ts` | lines 251-273 | `buildRoutingPolicyContractSnapshot` | guard contract coherence | MUST_NOT_BREAK | ACCEPT |
| EXISTS: routing barrel exports | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | routing export block | `routing-policy` re-exports | model gateway barrel | EXTEND_EXPORTS | ACCEPT |

Note: `ROUTING_POLICY_CONTRACT_VERSION` value is `phase2b-routing-policy-1`
(verified at line 31) and must stay unchanged; the value assignment is recorded
here as context, not in the `Verified path or symbol` column.

## Negative Search And Collision Discipline

| Search command or query | Search roots | Expected result | Disposition |
| --- | --- | --- | --- |
| `rg -n "RoutingPolicyEngine\|RoutingRequest\|RoutingDecision\|buildRoutingPolicyContractSnapshot" EXTENSIONS` | all extensions | Real consumers: Model Gateway src/tests; `CVF_GUARD_CONTRACT` phase2b test; `CVF_PLANE_FACADES` (own `ModelRoutingRequest` interface, not the engine). EPF `feedback.routing.*` is a different domain (feedback signal routing), not a Model Gateway routing consumer. | VERIFY_BEFORE_EDIT |
| `rg -n "PolicyDecision" EXTENSIONS/CVF_MODEL_GATEWAY/src` | Model Gateway src | No existing `PolicyDecision` symbol in Model Gateway (the `PolicyDecision` in `index.ts` re-export is from RUNTIME_ADAPTER_HUB contracts) | AVOID_NAME_COLLISION: use the routing-scoped name `RoutingStageDecision` |
| `rg -n "execution_stage\|complexityScore\|riskScore\|fallbackChain" EXTENSIONS/CVF_MODEL_GATEWAY/src` | Model Gateway src | The four new routing-context tokens have zero current occurrence in Model Gateway source; no symbol collision exists for them | SAFE_TO_ADD |

Name-collision note: `index.ts` already re-exports a `PolicyDecision` type from
`CVF_v1.7.3_RUNTIME_ADAPTER_HUB`. The new routing pipeline decision type MUST use
the distinct routing-scoped name `RoutingStageDecision` to avoid export collision
in the barrel.

## Current Runtime Freshness Verification

| Runtime/source surface | Freshness check | Expected |
| --- | --- | --- |
| Model Gateway routing | `rg -n "RoutingPolicyEngine\|RoutingRequest" EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | found at lines cited above |
| Reused primitives | `rg -n "isRoutable\|isUsable\|canUse\|FallbackPolicy" EXTENSIONS/CVF_MODEL_GATEWAY/src` | found |
| Guard contract consumer | `rg -n "RoutingPolicyEngine" EXTENSIONS/CVF_GUARD_CONTRACT/src` | found in phase2b coherence test |

## Evidence Requirements

The worker must provide source-backed evidence for every claim in the worker
return:

- Each backward-compat claim: cite the passing existing test run output summary.
- Each new behavior claim: cite the new test name and its passing result.
- The external-consumer-intact claim: cite the `CVF_GUARD_CONTRACT` phase2b
  coherence test passing unedited (test command + result).
- The no-provider/no-live claim: `git diff --name-status` and `git status --short`
  showing source/test changes only under `EXTENSIONS/CVF_MODEL_GATEWAY/` and the
  one documentation change being the worker return under `docs/reviews/`.
- The no-commit claim: `git rev-parse HEAD` equal to `executionBaseHead`.
- Type-check and test-suite results: actual command output summaries, not
  predicted results.

Evidence may be command-output summaries, cited governed file lines/sections, or
explicit N/A with reason where a proof class does not apply.

## Implementation Specification

### IS-1: Additive RoutingContext fields on RoutingRequest

Extend `RoutingRequest` with all-optional fields. No existing field changes type
or becomes required.

Recommended additive optional fields (final names at worker discretion if
documented in the worker return; keep snake_case OR camelCase consistent with the
existing file which uses camelCase):

- `executionStage?: string` (or a bounded union if the worker can source one)
- `complexityScore?: number`
- `riskScore?: number`
- `requiredCapabilities?: ProviderMethodName[]`
- `costBudget?: number`
- `latencyBudgetMs?: number`

Extend `RoutingDecision` `selected` branch with an optional `fallbackChain?:
Array<{ providerId: string; modelId: string }>` recording ordered fallback
candidates considered. The `denied | requires_approval | no_candidate` branch
stays unchanged.

Backward-compat requirement: a `RoutingRequest` with only `traceId` + `policy`
(+ optional `requestedModelId`, `preferredProviderId`, `estimatedTokens`) MUST
produce the same `decide()` result as today.

### IS-2: Pluggable policy pipeline in RoutingPolicyEngine

Add an ordered, pluggable policy pipeline that runs AFTER the existing
fail-closed guards (missing policy -> deny; policyResult deny/requires_approval)
and BEFORE / DURING provider selection. Each policy returns a routing-scoped
stage decision.

Required pipeline elements (orchestrate existing primitives; do not reimplement):

1. A routing-scoped decision interface, e.g.:

   ```ts
   export interface RoutingStageDecision {
     stage: string;             // e.g. "capability", "stage", "risk", "cost"
     candidates: ProviderRecord[];
     reason: string;
   }
   ```

2. An ordered policy list. Recommended order (worker may justify a different
   order in the worker return):
   - capability filter (uses `requiredCapabilities` against
     `PROVIDER_CAPABILITY_REGISTRY` / provider method gate, when provided)
   - stage filter (uses `executionStage`, no-op when absent)
   - risk filter (uses `riskScore` / `GatewayPolicyContext.requestRiskClass`)
   - cost filter (uses `costBudget` against quota, no-op when absent)

3. A merge engine that composes ordered policy outputs into a single ordered
   candidate list, preserving the existing `orderedProviders` preference
   (preferred provider first).

4. An escalation policy that, when the primary candidate fails the existing
   health/quota gate, records the next candidate into `fallbackChain` by reusing
   `FallbackPolicy` semantics. This is decision-time ordering only; NO provider
   call, NO live retry is performed.

When NONE of the optional context fields are provided, every policy is a no-op
pass-through and `decide()` returns exactly the current behavior.

### IS-3: Snapshot additive fields (version stable)

`RoutingPolicyContractSnapshot` may gain optional fields (e.g.
`appliedPolicies?: string[]`, `fallbackChainLength?: number`). The existing
fields (`version`, `source`, `traceId`, `status`, `reason`, `selectedProviderId`,
`selectedModelId`, `policyResult`) and `ROUTING_POLICY_CONTRACT_VERSION` value
MUST stay unchanged so the `CVF_GUARD_CONTRACT` phase2b P-06 node keeps reading
`source` and `policyResult` identically.

### IS-4: Barrel exports

Add new routing types to `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` routing
export block. Do not collide with the existing re-exported `PolicyDecision` from
RUNTIME_ADAPTER_HUB.

### IS-5: File-size discipline (GC-023)

`routing-policy.ts` is currently 144 lines. If the pipeline implementation would
push it past the advisory threshold (700) it has room, but for readability the
worker SHOULD extract the policy pipeline into a dedicated new file (e.g.
`routing-policy-pipeline.ts`) and keep `routing-policy.ts` as the engine entry.
Do not exceed the `.ts` hard threshold (1000) on any file.

## Test Specification

| Test | Requirement |
| --- | --- |
| Existing `routing-policy.test.ts` | MUST keep passing with zero edits to existing assertions; worker may ADD new test cases in the same file or a new file |
| Backward-compat case | Add a test proving a minimal request (`traceId` + `policy` + `requestedModelId`) returns the identical decision shape as before the change |
| Capability policy | Test that `requiredCapabilities` filters out providers lacking the method |
| Risk/cost policy | Test that `riskScore` / `costBudget` influence candidate ordering or denial as specified |
| Escalation / fallbackChain | Test that `fallbackChain` records ordered candidates without performing any provider call |
| No-op pass-through | Test that absent optional fields yield current behavior |
| Guard contract phase2b | `CVF_GUARD_CONTRACT` coherence test MUST pass unedited; worker runs it and records the result |

## Scope

Allowed:

- Edit `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` and add new routing
  pipeline source file(s) under `EXTENSIONS/CVF_MODEL_GATEWAY/src/`.
- Edit `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` to export new routing types.
- Add/extend tests under `EXTENSIONS/CVF_MODEL_GATEWAY/tests/`.
- Run local type checks and the affected test suites.
- Write the single worker return documentation file under `docs/reviews/`.

Forbidden:

- P2 dynamic model registry, P3 unified gateway interface, strategy-layer
  components (Execution Planner, Strategy Taxonomy, Feedback Loop).
- Editing `CVF_GUARD_CONTRACT`, `CVF_EXECUTION_PLANE_FOUNDATION`,
  `CVF_PLANE_FACADES`, provider adapters, or any extension other than
  `CVF_MODEL_GATEWAY`.
- Changing `ROUTING_POLICY_CONTRACT_VERSION` or the existing snapshot field set.
- Provider/API calls, live governance proof, provider/model addition, package
  install, secret inspection, public-sync, public catalog claim.
- Registry mutation (legacy coverage index, corpus scan registry).
- Session-state, handoff, front-door, or active review queue mutation.
- Governance-kernel surface changes; AI Gateway absorption; OS/endpoint control.
- Autonomous mutation; commit.

Risk ceiling: R2 single-extension implementation.

## Execution Plan

| Step | Input | Action | Output | Stop condition |
| --- | --- | --- | --- | --- |
| 1 | Required first reads + GC-018 + operator auth | Capture executionBaseHead; confirm authorizations; run baseline tests green | preflight evidence | Stop if GC-018/operator auth missing or baseline red |
| 2 | routing-policy.ts + reused primitives | Implement IS-1 additive fields | extended types | Stop if any existing field must change to non-optional |
| 3 | routing-policy.ts + new pipeline file | Implement IS-2 pipeline orchestrating existing primitives | pluggable pipeline | Stop if a primitive would need reimplementation outside scope |
| 4 | snapshot builder | Implement IS-3 additive snapshot fields, version stable | extended snapshot | Stop if version or existing field must change |
| 5 | index.ts | Implement IS-4 exports without collision | updated barrel | Stop on `PolicyDecision` name collision |
| 6 | tests | Implement Test Specification | passing tests | Stop if existing assertion would need editing to pass |
| 7 | gates | Run type check, MG tests, guard-contract phase2b test, reviewer-fast | evidence in worker return | Stop and repair allowed-scope issues before return |

## Worker Pending-Return Gate

| Gate | Required evidence | Status |
| --- | --- | --- |
| Authorizations present | GC-018 baseline + operator authorization cited | PENDING |
| Scope-limited mutation | `git diff --name-status` / `git status --short` show source/test changes only under `EXTENSIONS/CVF_MODEL_GATEWAY/`, and the only documentation change is the worker return under `docs/reviews/` | PENDING |
| Backward compatibility | Existing `routing-policy.test.ts` assertions unchanged and passing | PENDING |
| External consumer intact | `CVF_GUARD_CONTRACT` phase2b coherence test passes unedited | PENDING |
| Contract version stable | `ROUTING_POLICY_CONTRACT_VERSION` unchanged; existing snapshot fields unchanged | PENDING |
| New tests present | Capability, risk/cost, escalation, no-op, backward-compat cases added | PENDING |
| Type check | Model Gateway / Guard Contract `npm run check` (or tsc) PASS | PENDING |
| Test run | `npm test` (Vitest) PASS for affected packages; results recorded | PENDING |
| GC-023 | No `.ts` file exceeds 1000 lines; near-advisory files split if applicable | PENDING |
| No provider/live | No provider/API/live proof, model addition, package install, or secret read | PENDING |
| Name collision avoided | New routing decision type does not collide with re-exported `PolicyDecision` | PENDING |
| Agent Operation Trace Block | Expected and actual changed set recorded | PENDING |
| Public Export Disposition | `DEFERRED_PRIVATE_ONLY` in worker return | PENDING |
| Worker did not commit | HEAD unchanged from executionBaseHead | PENDING |
| Diff hygiene | `git diff --check` PASS | PENDING |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` PASS, or failure recorded with allowed-scope repair | PENDING |

## Worker Autonomy / No-Question Rule

Allowed-scope failures (type errors, failing new tests, missing sections, trace
updates, diff hygiene, GC-023 file split) must be repaired and rerun without
escalation.

Worker must stop and return `BLOCKED_SCOPE_EXPANSION` only when a repair would:
require editing an extension other than `CVF_MODEL_GATEWAY`; change
`ROUTING_POLICY_CONTRACT_VERSION` or existing snapshot fields; break the
guard-contract phase2b test in a way that needs editing that test; require a
provider/API/live call, secret, package install, registry mutation, public-sync,
governance-kernel change, or a commit; or exceed P1 into P2/P3/strategy scope.

## Acceptance Criteria

| Criterion | Acceptance condition |
| --- | --- |
| Additive only | All new `RoutingRequest`/`RoutingDecision`/snapshot fields are optional; no existing field changed |
| Backward compatible | Existing routing tests and guard-contract phase2b test pass unedited |
| Pipeline implemented | Pluggable policy pipeline orchestrates existing fallback/quota/health primitives; no primitive reimplemented |
| Version stable | `ROUTING_POLICY_CONTRACT_VERSION` and existing snapshot fields unchanged |
| Single-extension boundary | Source/test changes only under `EXTENSIONS/CVF_MODEL_GATEWAY/`; the only documentation change is the worker return under `docs/reviews/` |
| Test coverage | New tests cover capability, risk/cost, escalation, no-op, and backward-compat |
| GC-023 | No file exceeds hard threshold |
| Public boundary | `DEFERRED_PRIVATE_ONLY` present |

## Review Gate

Reviewer runs `npm run check`, the Vitest suites for `CVF_MODEL_GATEWAY` and
`CVF_GUARD_CONTRACT`, reviewer-fast, and dispatch/closure gates before accepting,
committing, or closing. Failures inside worker scope return to the worker;
reviewer-owned closure defects are repaired only within reviewer-owned scope.

## Closure Checklist

| Item | Closure owner | Status before worker return |
| --- | --- | --- |
| Source + tests implemented | Worker | PENDING |
| Worker gates recorded | Worker | PENDING |
| Reviewer closure artifact created | Reviewer | N/A before return |
| Accepted artifacts committed | Reviewer | N/A before worker return |
| Session continuity synced | Reviewer | N/A before worker return |
| `MGW-001` row note (stays PARTIAL until P2/P3) | Reviewer | N/A before worker return |

## Return-To-Orchestrator Conditions

Return `BLOCKED_SCOPE_EXPANSION` if the work requires editing another extension,
changing the contract version or existing snapshot fields, breaking/editing the
guard-contract phase2b test, provider/live proof, secrets, package install,
public-sync, registry mutation, governance-kernel change, or a commit.

## Operator Checkpoint

Operator authorization is a BLOCKING precondition for dispatch. After dispatch,
operator approval is required only if scope expands beyond P1 or touches a parked
lane.

## Required Artifact Manifest

| Path | Owner | Required at handoff | Purpose |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` (edit) | Worker | YES | Extended request/decision/snapshot + engine pipeline entry |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy-pipeline.ts` (new, recommended) | Worker | CONDITIONAL | Pluggable policy pipeline if extracted for GC-023/readability |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (edit) | Worker | YES | New routing type exports |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/routing-policy.test.ts` (edit) or new test file | Worker | YES | New routing pipeline test coverage |
| Worker return (suggested `docs/reviews/CVF_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_WORKER_RETURN_2026-06-14.md`) | Worker | YES | Gate evidence and trace |
| Reviewer closure artifact | Reviewer | NO | Closure conversion |

## Work-Order Fulfillment Manifest

| Requirement | Required artifact or proof | Closure owner |
| --- | --- | --- |
| Fresh GC-018 authorization | `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_2026-06-14.md` | Orchestrator |
| P1 source implementation | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` and optional `routing-policy-pipeline.ts` | Worker |
| P1 exports | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | Worker |
| P1 tests | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/` | Worker |
| Worker return | `docs/reviews/CVF_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_WORKER_RETURN_2026-06-14.md` | Worker |
| Completion review | `docs/reviews/CVF_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_COMPLETION_2026-06-14.md` | Reviewer |
| Session sync if needed | `AGENT_HANDOFF_V18_2026-06-12.md` | Committer |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Work order author (Claude, planning/authoring role) |
| Provider or surface | Claude Code CLI / VSCode extension |
| Session or invocation | dispatchBaseHead `5841ae43` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read, Grep, Bash (git, rg, wc, find), Write (this work order) |
| Target paths | this work order; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_2026-06-14.md`; worker artifact paths named in Required Artifact Manifest |
| Allowed scope source | Operator instruction 2026-06-14 to audit and author a detailed C-02 P1 implementation work order |
| Before status evidence | HEAD `5841ae43`; clean worktree at authoring start |
| After status evidence | one new untracked work order file created |
| Diff evidence | documentation-only authoring; no `EXTENSIONS/` mutation by this authoring step |
| Approval boundary | Authoring only; implementation requires fresh GC-018 + operator authorization before dispatch |
| Claim boundary | Work order authoring; no implementation, runtime, provider, or public claim |
| Agent type | Claude |
| Invocation ID | `dispatchBaseHead=5841ae43` |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_IMPLEMENTATION_2026-06-14.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_2026-06-14.md` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_IMPLEMENTATION_2026-06-14.md`; `docs/baselines/CVF_GC018_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_2026-06-14.md` |
| Manifest delta | MATCH -- work order dispatched and GC-018 baseline authored |
| Deletion or rename disposition | N/A with reason: no protected path deleted or renamed; one new file created |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: The routing pipeline extension can be implemented
strictly additively because the only external runtime consumer
(`CVF_GUARD_CONTRACT` phase2b coherence test) reads `decide()` with a minimal
request and only `source` + `policyResult` from the snapshot. The reused
primitives (`FallbackPolicy`, `QuotaLedger`, `ProviderHealthMonitor`,
`ProviderRegistry`) already exist and can be orchestrated without
reimplementation.

Evidence Comparison: Audit confirmed the prediction. The phase2b test
(lines 251-273) builds a minimal `routingRequest` and reads `routingSnapshot.source`
and `routingSnapshot.policyResult`. EPF `feedback.routing.*` is a different domain
(feedback signal routing) and is not a Model Gateway routing consumer. The four
reused primitives are present at the cited source lines. `routing-policy.ts` is
144 lines with room under GC-023.

Contradiction Or Gap Disposition: One naming collision risk found and recorded:
`index.ts` already re-exports a `PolicyDecision` from RUNTIME_ADAPTER_HUB, so the
new routing decision type must use a distinct name. This is recorded in the
Negative Search And Collision Discipline section.

Claim Update: P1 is implementation-ready as a bounded, backward-compatible,
single-extension tranche, contingent on a fresh GC-018 and operator
authorization. P2/P3 and strategy-layer remain deferred.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Implementation tranche could touch an external consumer test unexpectedly | INTEGRATION_BLAST_RADIUS | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Work order names the exact external consumer (phase2b coherence test) and requires it to pass unedited |
| Name collision with re-exported `PolicyDecision` | NAMING_COLLISION_RISK | RUNTIME_BEHAVIOR_LEARNING | RECORDED | Worker must use a routing-scoped decision type name |
| Scope creep from P1 into P2/P3/strategy | SCOPE_EXPANSION_RISK | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | Forbidden scope and BLOCKED_SCOPE_EXPANSION rule constrain the tranche to P1 |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation work order. Public-sync and public
catalog update are not authorized by this authoring step.
