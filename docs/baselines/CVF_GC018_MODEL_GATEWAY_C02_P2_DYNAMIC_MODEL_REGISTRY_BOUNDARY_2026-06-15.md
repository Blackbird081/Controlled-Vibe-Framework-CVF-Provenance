# CVF GC-018 Model Gateway C-02 P2 Dynamic Model Registry Boundary - 2026-06-15

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018_baseline

Date: 2026-06-15

Owner: Codex Orchestrator

Worker target: Claude

Reviewer target: Codex

Commit mode: WORKER_MUST_NOT_COMMIT for worker role; reviewer may commit after review

rawMemoryReleased=false

Base head: 1ec2f2b4

dispatchBaseHead: `1ec2f2b4`

executionBaseHead: WORKER_MUST_CAPTURE_AFTER_DISPATCH

closureBaseHead: REVIEWER_CAPTURE_AFTER_WORKER_RETURN

## Authorization

Operator authorized Codex on 2026-06-15 to review the prepared P2 work order,
commit it, and dispatch Claude for implementation. This baseline converts that
operator instruction into the fresh GC-018 authorization required by the P2
work order.

## Purpose

Authorize the bounded Model Gateway C-02 P2 Dynamic Model Registry Boundary
tranche as a contract-first implementation.

This tranche creates a governed type contract and boundary definition for a
future Dynamic Model Registry. It does not implement the runtime registry.

Authorized outputs:

- types-only contract file under `EXTENSIONS/CVF_MODEL_GATEWAY/src/`;
- barrel export edit in `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`;
- type-level tests under `EXTENSIONS/CVF_MODEL_GATEWAY/tests/`;
- boundary definition document under `docs/reference/`;
- worker-return packet under `docs/reviews/`.

## Decision / Baseline / Proposed Tranche

Decision: proceed with C-02 P2 as a bounded R1 contract-first tranche.

Baseline:

- C-02 provider-routing boundary rewrite planning is closed bounded.
- C-02 P1 routing pipeline is closed bounded.
- Model Gateway legacy absorption coverage row `MGW-001` remains
  `PARTIAL_RECHECK_REQUIRED`.
- P2 implements only the accepted value key
  `dynamicModelRegistryWithHealthMonitoring` as a boundary contract.

Proposed tranche:

- create `DynamicModelRegistryContract`, `DynamicModelRecord`,
  `FindOptimalQuery`, and `ModelTier`;
- reuse existing `ProviderMethodName`, `ProviderStatus`, and
  `ProviderHealthState`;
- document the merge boundary among `PROVIDER_CAPABILITY_REGISTRY`,
  `ProviderRegistry`, and a future `DynamicModelRegistry`;
- prove the contract shape with type-level tests;
- return `COMPLETE_PENDING_REVIEW` without committing.

## Authorized Scope

Worker may write only:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/dynamic-model-registry-contract.ts`;
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`;
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/dynamic-model-registry-contract.test.ts`;
- `docs/reference/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_DEFINITION_2026-06-15.md`;
- `docs/reviews/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_WORKER_RETURN_2026-06-15.md`.

Reviewer owns closure review, GC-051 registry coverage for the new source file,
commits, and session sync.

Forbidden scope:

- runtime `DynamicModelRegistry` class implementation;
- query execution, health-poll scheduling, pricing lookup, or provider calls;
- P3 unified gateway interface;
- strategy-layer components;
- AI Gateway absorption;
- live governance proof, API keys, network requests, public-sync;
- mutation of `provider-capability-registry.ts`, `provider-registry.ts`,
  `provider-health.ts`, `routing-policy.ts`, or `routing-policy-pipeline.ts`;
- governance-kernel mutation, session-state mutation by worker, registry
  mutation by worker, or co-work product development.

Risk ceiling: R1 additive contract/types/doc/tests under Model Gateway.

## Source Authority Table

| Source | Authority use | Disposition |
| --- | --- | --- |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_2026-06-15.md` | P2 work order and worker boundary | ACCEPT |
| `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_ROADMAP_2026-06-15.md` | P2 scope, deliverables, and acceptance criteria | ACCEPT |
| `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | Closed C-02 plan; dynamic registry recommendation | ACCEPT |
| `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md` | Accepted value key `dynamicModelRegistryWithHealthMonitoring` | ACCEPT |
| `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | Coverage row `MGW-001` remains partial until P2/P3/deferred keys close | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | `ProviderMethodName` contract | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | `ProviderStatus`, provider records, and routability owner | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | `ProviderHealthState` and health record owner | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | Static provider method capability registry | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | P1 `RoutingRequest` compatibility surface | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | Model Gateway barrel export surface | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: `ProviderMethodName` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | line 1 | `ProviderMethodName` | provider method contract | ACCEPT |
| EXISTS: `GatewayRiskClass` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 1 | `GatewayRiskClass` | provider registry | ACCEPT |
| EXISTS: `ProviderStatus` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 2 | `ProviderStatus` | provider registry | ACCEPT |
| EXISTS: `ProviderModel` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 4 | `ProviderModel` | provider registry | ACCEPT |
| EXISTS: `ProviderRecord` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 13 | `ProviderRecord` | provider registry | ACCEPT |
| EXISTS: `ProviderRegistry.isRoutable` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 72 | `isRoutable` | provider registry | ACCEPT |
| EXISTS: `PROVIDER_CAPABILITY_REGISTRY` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| EXISTS: `ProviderHealthState` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 1 | `ProviderHealthState` | provider health | ACCEPT |
| EXISTS: `ProviderHealthRecord` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 7 | `ProviderHealthRecord` | provider health | ACCEPT |
| EXISTS: `RoutingRequest` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 13 | `RoutingRequest` | routing policy | ACCEPT |
| EXISTS: Model Gateway provider/health barrel export blocks | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | lines 60-73 | provider and health type exports | model gateway barrel | ACCEPT |

## Negative Search And Collision Discipline

| Search command or query | Result | Disposition |
| --- | --- | --- |
| `rg -n "DynamicModelRegistry\|DynamicModelRecord\|FindOptimalQuery\|ModelTier" --hidden --no-ignore .` | No current source symbol collision before P2 dispatch | Safe to add in P2 |
| `rg -n "findOptimal" EXTENSIONS/CVF_MODEL_GATEWAY` | No existing Model Gateway `findOptimal` symbol before P2 dispatch | Safe to add to contract only |
| `rg -n "ProviderHealthState\|ProviderStatus\|ProviderMethodName" EXTENSIONS/CVF_MODEL_GATEWAY/src` | Existing reusable authoritative types found | Import/reuse; do not redeclare |

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
| --- | --- |
| Coverage index row | `MGW-001` |
| Current coverage status | `PARTIAL_RECHECK_REQUIRED` |
| Accepted value key in this tranche | `dynamicModelRegistryWithHealthMonitoring` |
| Release basis | C-02 rewrite plan `RESUME_WITH_REWRITE`; P1 closed; P2 authorized here |
| Closure rule | P2 closure alone does not upgrade `MGW-001` to complete because P3 and deferred strategy/interface keys remain open |

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | `MGW-001`, recheck plan, and C-02 rewrite plan were read before this baseline | ACCEPT |
| Detailed source files read when present | Current Model Gateway provider method, provider registry, health, capability, routing policy, and barrel files were read | ACCEPT |
| Accepted value normalized into owner surfaces | P2 maps only dynamic registry boundary contract into `EXTENSIONS/CVF_MODEL_GATEWAY/` | ACCEPT |
| Accept/defer/reject dispositions recorded | This baseline accepts P2 contract boundary and defers runtime DMR, P3, strategy, and AI Gateway | ACCEPT |
| Adversarial role review | Orchestrator, worker, reviewer, boundary owner, and operator advocate roles are separated by phase gates | ACCEPT |
| Blind-spot delta | Broad legacy reread is not needed for worker execution because governed recheck and rewrite artifacts are the source authority | ACCEPT_WITH_BOUNDARY |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Source | Handling in this tranche | Status |
| --- | --- | --- | --- |
| Fresh GC-018 before dispatch | P2 roadmap Authorization and work order Authorization Preconditions | This baseline authorizes P2 | SATISFIED_FOR_DISPATCH |
| Types-only DMR contract | P2 roadmap D3/AC1 | Worker creates contract file; no runtime implementation | SATISFIED_FOR_DISPATCH |
| Boundary definition doc | P2 roadmap D4/AC5 | Worker creates governed boundary definition doc | SATISFIED_FOR_DISPATCH |
| Type-level tests | P2 roadmap D5/AC3 | Worker creates focused tests and runs Model Gateway checks | SATISFIED_FOR_DISPATCH |
| GC-051 registry entry | P2 roadmap D6 | Reviewer-owned at closure | SATISFIED_FOR_DISPATCH |
| Keep P3/P4 deferred | P2 roadmap Next Allowed Move and Non-Goals | Forbidden scope here | SATISFIED_FOR_DISPATCH |

## Evidence / Verification

Dispatch verification before implementation:

| Gate | Command | Expected result |
| --- | --- | --- |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 1ec2f2b4 --head HEAD --enforce` | PASS |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 1ec2f2b4 --head HEAD` | PASS |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Diff hygiene | `git diff --check` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch. Public-sync is not
authorized by this baseline.

## Rescan Intelligence Hardening

- Original source artifact: `docs/roadmaps/CVF_MODEL_GATEWAY_C02_P2_DYNAMIC_MODEL_REGISTRY_BOUNDARY_ROADMAP_2026-06-15.md`
- Predecessor intake artifact: `docs/reference/CVF_MODEL_GATEWAY_C02_LEGACY_RECHECK_AND_REWRITE_PLAN_2026-06-14.md`
- Delta ledger status: `NOT_APPLICABLE_WITH_REASON` - this artifact is a dispatch authorization baseline, not a new rescan output or intake refresh.
- Routing matrix status: `NOT_APPLICABLE_WITH_REASON` - follow-up routing is bounded by the P2 roadmap and this baseline.
- Semantic sampling status: `NOT_APPLICABLE_WITH_REASON` - sampling was handled by the prior legacy recheck/rewrite chain; this baseline only gates dispatch.
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

### Original-Intake Delta Ledger

| Delta category | P2 disposition |
| --- | --- |
| UNCHANGED_FROM_INTAKE | P2 keeps the prior accepted value for dynamic model registry with health monitoring. |
| CHANGED_DISPOSITION | No disposition is changed by this baseline. |
| NEW_FINDING | No new legacy/rescan finding is introduced here. |
| REMOVED_OR_REJECTED | No prior accepted legacy item is removed or rejected here. |

### Follow-Up Routing Matrix

| Routing lane | P2 disposition |
| --- | --- |
| DO_NOW | Dispatch the P2 types-only contract and boundary definition to Claude. |
| SEPARATE_RUNTIME_TRANCHE | Runtime registry behavior remains outside P2. |
| STRATEGIC_OPERATOR_DECISION | P3/P4 continuation remains operator-gated after Codex review. |
| OUT_OF_SCOPE | Public-sync, live proof, AI Gateway, and provider runtime changes stay out of scope. |
| RESOLVED_BY_DESIGN | Source-verification and AOT manifest coverage are resolved in this baseline. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| P2-RIH-001 | Legacy Absorption Coverage Index Disposition | P2 can dispatch without broad legacy reread because MGW-001 remains partial and bounded | ACCEPT_WITH_BOUNDARY | Could the worker treat P2 as completing legacy absorption? | PASS - closure text blocks coverage-index completion. |
| P2-RIH-002 | Authorized Scope | P2 is contract-only and does not implement runtime routing | ACCEPT | Could contract additions mutate provider behavior indirectly? | PASS - runtime and policy edits are forbidden. |

## Claim Boundary

This baseline authorizes dispatch only. It does not claim implementation
completion, runtime behavior, live governance proof, provider readiness, public
readiness, production readiness, or coverage-index completion.

Verification boundary: dispatch evidence is limited to source verification,
legacy coverage disposition, work-order dispatch quality, pre-dispatch autorun,
reviewer-fast, and diff hygiene on the dispatch range. Worker completion
evidence must be supplied in the worker return and reviewed by Codex before
closure.

## Closure Boundary

This baseline can close only through a Codex reviewer completion review after
Claude returns `COMPLETE_PENDING_REVIEW` with no commit performed. Closure does
not authorize runtime DMR implementation, provider routing behavior changes,
live proof, public-sync, production readiness, public readiness, or upgrade of
`MGW-001` beyond the bounded P2 note.
