# CVF GC-018 Model Gateway C-02 P1 Routing Pipeline - 2026-06-14

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018_baseline

Date: 2026-06-14

Owner: Codex Orchestrator

Worker target: Codex worker role

Reviewer target: Codex reviewer role

Commit mode: WORKER_MUST_NOT_COMMIT for worker role; reviewer may commit after review

rawMemoryReleased=false

Base head: 89128582

dispatchBaseHead: `89128582`

executionBaseHead: WORKER_MUST_CAPTURE_AFTER_DISPATCH

closureBaseHead: REVIEWER_CAPTURE_AFTER_WORKER_RETURN

## Authorization

Operator authorized Codex on 2026-06-14 to assume multiple roles and execute the
prepared work order. This baseline converts that operator instruction into the
fresh GC-018 authorization required by the P1 work order.

## Purpose

Authorize the bounded Model Gateway C-02 P1 implementation tranche for the
routing context and pluggable routing policy pipeline.

This tranche implements only the P1 subset recommended by the closed C-02
provider-routing boundary rewrite plan:

- additive optional routing context fields on `RoutingRequest`;
- optional fallback-chain evidence on selected `RoutingDecision`;
- a routing-scoped `RoutingStageDecision` and pluggable policy pipeline;
- snapshot additive optional fields while preserving the existing contract
  version and existing snapshot fields;
- focused source exports and tests under `EXTENSIONS/CVF_MODEL_GATEWAY/`.

## Decision / Baseline / Proposed Tranche

Decision: proceed with C-02 P1 as a bounded implementation tranche.

Baseline:

- C-02 provider-routing boundary rewrite planning is closed bounded.
- Model Gateway legacy absorption row `MGW-001` remains
  `PARTIAL_RECHECK_REQUIRED`.
- P1 implements only `routingContextFullInterface` and
  `routingPolicyEnginePluggablePipeline`.

Proposed tranche:

- implement the P1 routing pipeline under `EXTENSIONS/CVF_MODEL_GATEWAY/`;
- add focused unit tests for backward compatibility, capability filtering,
  risk/cost behavior, no-op pass-through, and fallback-chain evidence;
- produce a worker return with no-provider/no-live/no-public evidence.

Authorized scope:

- edit `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts`;
- add routing pipeline source files under `EXTENSIONS/CVF_MODEL_GATEWAY/src/`;
- edit `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` for exports only;
- edit or add tests under `EXTENSIONS/CVF_MODEL_GATEWAY/tests/`;
- create one worker-return packet under `docs/reviews/`.

Forbidden scope:

- dynamic model registry P2;
- unified gateway interface P3;
- strategy layer, Execution Planner, feedback loop, or EPF step lifecycle;
- AI Gateway absorption or environment signal capture;
- provider/API calls, live governance proof, secrets, package install, public-sync;
- registry mutation, governance-kernel mutation, session-state mutation by the
  worker role, or co-work product development.

Risk ceiling: R2 single-extension source/test implementation.

## Source Authority Table

| Source | Authority use | Disposition |
| --- | --- | --- |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_MODEL_GATEWAY_C02_P1_ROUTING_PIPELINE_IMPLEMENTATION_2026-06-14.md` | P1 work order and worker boundary | ACCEPT |
| `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | Closed C-02 plan; P1 recommendation | ACCEPT |
| `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md` | Codex reviewer acceptance of C-02 planning closure | ACCEPT |
| `docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md` | Accepted value keys and `MGW-001` release basis | ACCEPT |
| `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | Coverage row `MGW-001` remains partial until P2/P3 close | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | Current routing request, decision, engine, and snapshot owner | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | Current provider-method capability registry | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | `ProviderMethodName` contract | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | Current `ProviderRegistry` and provider records | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | Current health usability gate | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | Current quota decision primitive | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts` | Current fallback decision primitive | ACCEPT |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | Upstream governance policy context | ACCEPT |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phase2b-runtime-coherence.test.ts` | External P-06 routing snapshot consumer | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: `RoutingRequest` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 6 | `RoutingRequest` | routing policy | ACCEPT |
| EXISTS: `RoutingDecision` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 14 | `RoutingDecision` | routing policy | ACCEPT |
| VALUE_SET: routing contract version remains `phase2b-routing-policy-1` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 30 | `ROUTING_POLICY_CONTRACT_VERSION` | routing policy snapshot | ACCEPT |
| EXISTS: `RoutingPolicyContractSnapshot` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 32 | `RoutingPolicyContractSnapshot` | routing policy snapshot | ACCEPT |
| EXISTS: `buildRoutingPolicyContractSnapshot` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 43 | `buildRoutingPolicyContractSnapshot` | routing policy snapshot | ACCEPT |
| EXISTS: `RoutingPolicyEngine.decide` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 67 | `decide` | routing policy engine | ACCEPT |
| EXISTS: `RoutingPolicyEngine.decideWithSnapshot` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 123 | `decideWithSnapshot` | routing policy engine | ACCEPT |
| EXISTS: `orderedProviders` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | line 134 | `orderedProviders` | routing policy engine | ACCEPT |
| EXISTS: `ProviderRegistry.isRoutable` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | line 72 | `isRoutable` | provider registry | ACCEPT |
| EXISTS: `ProviderHealthMonitor.isUsable` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-health.ts` | line 60 | `isUsable` | provider health | ACCEPT |
| EXISTS: `QuotaLedger.canUse` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | line 52 | `canUse` | quota ledger | ACCEPT |
| EXISTS: `FallbackPolicy.decide` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts` | line 44 | `decide` | fallback policy | ACCEPT |
| EXISTS: `GatewayPolicyContext` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts` | line 2 | `GatewayPolicyContext` | gateway policy | ACCEPT |
| EXISTS: `PROVIDER_CAPABILITY_REGISTRY` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 42 | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| EXISTS: `ProviderMethodName` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | line 1 | `ProviderMethodName` | provider method contract | ACCEPT |
| EXISTS: phase2b P-06 uses routing snapshot | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phase2b-runtime-coherence.test.ts` | lines 251-270 | `buildRoutingPolicyContractSnapshot` | guard contract coherence | ACCEPT |

## Negative Search And Collision Discipline

| Search command or query | Result | Disposition |
| --- | --- | --- |
| `rg -n "PolicyDecision" EXTENSIONS/CVF_MODEL_GATEWAY/src` | Only `index.ts` re-exports `PolicyDecision` from `CVF_v1.7.3_RUNTIME_ADAPTER_HUB` | Use `RoutingStageDecision`; do not add `PolicyDecision` |
| `rg -n "RoutingStageDecision\|executionStage\|complexityScore\|riskScore\|requiredCapabilities\|costBudget\|latencyBudgetMs\|fallbackChain" EXTENSIONS/CVF_MODEL_GATEWAY/src` | No existing source symbols found before this tranche | Safe to add as new routing-scoped symbols |
| `rg -n "RoutingPolicyEngine" EXTENSIONS` | Model Gateway source/tests and Guard Contract phase2b coherence test are the real consumers | Guard Contract test must pass unedited |

## Legacy Absorption Coverage Index Disposition

| Field | Evidence |
| --- | --- |
| Coverage index row | `MGW-001` |
| Current coverage status | `PARTIAL_RECHECK_REQUIRED` |
| P1 accepted value keys | `routingContextFullInterface`; `routingPolicyEnginePluggablePipeline` |
| Explicitly deferred keys | dynamic registry, gateway interface, strategy layer, observability decomposition, AI Gateway family |
| Closure rule | P1 closure alone does not upgrade `MGW-001` to complete because P2/P3 and deferred strategy/interface keys remain open |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Source | Handling in this tranche | Status |
| --- | --- | --- | --- |
| Fresh GC-018 before implementation | C-02 rewrite plan section 11 and P1 work order Authorization Preconditions | This baseline authorizes P1 only | SATISFIED_FOR_DISPATCH |
| Implement routing context fields | C-02 plan section 7; work order IS-1 | Add optional fields only | SATISFIED_FOR_DISPATCH |
| Implement pluggable routing policy pipeline | C-02 plan section 7; work order IS-2 | Add routing-scoped pipeline and tests | SATISFIED_FOR_DISPATCH |
| Preserve external consumer | Guard Contract phase2b P-06 | Require unedited test pass | SATISFIED_FOR_DISPATCH |
| Keep P2/P3/strategy deferred | C-02 plan sections 6, 8, 9, 10 | Forbidden scope in this baseline and work order | SATISFIED_FOR_DISPATCH |

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | `MGW-001`, the recheck plan, and C-02 rewrite plan were read before this baseline | ACCEPT |
| Detailed source files read when present | Current Model Gateway routing, capability, registry, health, quota, fallback, gateway policy, and Guard Contract consumer files were read | ACCEPT |
| Accepted value normalized into owner surfaces | P1 maps only routing context and routing policy pipeline into `EXTENSIONS/CVF_MODEL_GATEWAY/` | ACCEPT |
| Accept/defer/reject dispositions recorded | This baseline accepts P1 and defers P2/P3/strategy/AI Gateway | ACCEPT |
| Adversarial role review | Orchestrator, worker, reviewer, boundary owner, and operator advocate roles are assigned internally with separate gates | ACCEPT |
| Blind-spot delta | Implementation is allowed only after this baseline; broad legacy reread is not needed because the governed recheck plan is the source authority | ACCEPT_WITH_BOUNDARY |

## Rescan Intelligence Hardening

- Original source artifact:
`docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md`

- Predecessor intake artifact:
`docs/reference/CVF_MODEL_GATEWAY_LEGACY_ABSORPTION_RECHECK_PLAN_2026-06-13.md`

- Delta ledger status: COMPLETE

- Routing matrix status: COMPLETE

- Semantic sampling status: COMPLETE

- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| Category | Current finding | Predecessor finding | New disposition | Reason |
| --- | --- | --- | --- | --- |
| UNCHANGED_FROM_INTAKE | `MGW-001` remains the governing coverage row | Recheck plan set `PARTIAL_RECHECK_REQUIRED` | RETAIN | P1 does not complete P2/P3 or deferred strategy/interface keys |
| CHANGED_DISPOSITION | Routing pipeline moves from planning recommendation to implementation authorization | C-02 plan said implementation requires fresh GC-018 | AUTHORIZE_P1_ONLY | This baseline supplies the fresh GC-018 for the bounded P1 subset |
| NEW_FINDING | Single-agent multi-role execution is acceptable only with explicit controls | Operator authorized Codex multi-role execution | CONTROLLED_ROUTE | Work order now includes routing and multi-role control blocks |
| REMOVED_OR_REJECTED | Broad legacy reread during P1 implementation | Recheck plan already absorbed the needed legacy value | REJECTED_FOR_THIS_TRANCHE | Worker consumes governed recheck evidence rather than reopening legacy content |

### Follow-Up Routing Matrix

| Lane | Item | Routing disposition |
| --- | --- | --- |
| DO_NOW | C-02 P1 routing context and policy pipeline | authorized by this baseline |
| SEPARATE_RUNTIME_TRANCHE | Dynamic registry P2 and unified gateway interface P3 | requires separate GC-018 |
| STRATEGIC_OPERATOR_DECISION | Strategy layer and AI Gateway privacy/GDPR absorption | remains separate operator decision |
| OUT_OF_SCOPE | Provider/live proof, public-sync, registry mutation, production/public readiness | excluded from this tranche |
| RESOLVED_BY_DESIGN | Prior legacy reread for P1 | resolved by consuming the closed recheck plan and C-02 rewrite plan |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| MG-C02-P1-S1 | C-02 plan section 7 | Routing pipeline gap exists | DO_NOW | Could this become dynamic registry work? | P1 remains routing-only |
| MG-C02-P1-S2 | Guard Contract phase2b test | External consumer reads snapshot `source` and `policyResult` | RESOLVED_BY_DESIGN | Could optional snapshot fields break it? | Existing fields and version must stay stable |
| MG-C02-P1-S3 | Capability registry | Capability filtering can reuse method registry | DO_NOW_WITH_BOUNDARY | Could unknown providers be silently selected for required capabilities? | Required capabilities fail closed when no matching capability record exists |

## Evidence / Verification

Dispatch verification before implementation:

| Gate | Command | Expected result |
| --- | --- | --- |
| Dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 89128582 --head HEAD --enforce` | PASS |
| Pre-dispatch autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 89128582 --head HEAD` | PASS |
| Reviewer-fast | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Diff hygiene | `git diff --check` | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex orchestrator |
| Provider or surface | Codex CLI |
| Session or invocation | dispatchBaseHead `89128582` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `Get-Content`, `rg`, `apply_patch`, dispatch gates |
| Target paths | this GC-018 and the P1 work order |
| Allowed scope source | Operator instruction on 2026-06-14 plus closed C-02 rewrite plan |
| Before status evidence | clean worktree at HEAD `89128582` |
| After status evidence | pending dispatch commit |
| Diff evidence | documentation dispatch batch only before worker implementation |
| Approval boundary | P1 routing implementation only |
| Claim boundary | no provider/live/public/registry/governance-kernel claim |
| Agent type | Codex |
| Invocation ID | `dispatchBaseHead=89128582` |
| Expected manifest | this GC-018; P1 work order status update |
| Actual changed set | this GC-018; P1 work order status update |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no protected path deleted or renamed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation authorization. Public-sync and public
catalog update are not authorized.

## Claim Boundary

This baseline authorizes a bounded P1 implementation only. It does not authorize
dynamic registry P2, unified gateway interface P3, strategy layer, EPF step
lifecycle, AI Gateway absorption, provider/API calls, live proof, public-sync,
production readiness, public readiness, cost/quality claims, raw memory release,
co-work product development, or autonomous mutation.
