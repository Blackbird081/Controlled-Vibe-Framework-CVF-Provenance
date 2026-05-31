# CVF Agent Work Order - LHW23 Routing and Registry Intelligence

Memory class: FULL_RECORD

Status: HOLD_UNTIL_LHW22_PASS

docType: work_order

Date: 2026-05-31

## Purpose

Prepare, but do not dispatch, the LHW23 documentation-only advisory connector
wave for model registry service, multi-factor routing policy, and execution
strategy model.

This order remains on HOLD until LHW22 has machine-backed PASS closure evidence
and Orchestrator refreshes or re-authorizes the LHW23 source baseline.

## Scope / Target / Owner Boundary

Target wave: LHW23 documentation-only advisory connectors.

Allowed scope after hold is released:

- Create `docs/baselines/CVF_GC018_LHW23_ROUTING_REGISTRY_INTELLIGENCE_2026-05-31.md`.
- Create `docs/reference/CVF_LHW23_T1_MODEL_REGISTRY_SERVICE_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`.
- Create `docs/reference/CVF_LHW23_T2_MULTIFACTOR_ROUTING_POLICY_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`.
- Create `docs/reference/CVF_LHW23_T3_EXECUTION_STRATEGY_MODEL_ADVISORY_CONNECTOR_SPEC_2026-05-31.md`.
- Create `docs/reviews/CVF_LHW23_T1_MODEL_REGISTRY_SERVICE_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`.
- Create `docs/reviews/CVF_LHW23_T2_MULTIFACTOR_ROUTING_POLICY_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`.
- Create `docs/reviews/CVF_LHW23_T3_EXECUTION_STRATEGY_MODEL_ADVISORY_CONNECTOR_COMPLETION_2026-05-31.md`.

Forbidden scope:

- Do not dispatch this order while LHW22 is unresolved.
- Do not edit `EXTENSIONS/`, route files, `resolveProviderForRole`, provider
  registry source, routing policy source, execution facade source, or runtime
  receipt types.
- Do not run live provider calls or claim governance behavior.
- Do not edit or push public-sync.
- Do not execute LHW22 or LHW24 from this order.

## Authority Chain

| Authority | Path / basis | Disposition |
|---|---|---|
| Parent roadmap | `docs/roadmaps/CVF_LHW22_LHW23_LHW24_AGENT_INTELLIGENCE_ROADMAP_2026-05-31.md` | ACCEPT |
| Required predecessor | LHW22 wave closure evidence | HOLD |
| Full-scan audit | `docs/audits/CVF_IMPORTANT_FULL_FILE_SCAN_BLINDSPOT_RECORD_2026-05-31.md` | ACCEPT |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
|---|---|---|
| Orchestrator | Release hold only after LHW22 PASS evidence exists | No premature dispatch |
| Implementer | Author docs after hold release | No runtime edits |
| Reviewer | Verify current runtime owner paths before closure | No stale basename-only claims |

## Required First Reads

- `docs/roadmaps/CVF_LHW22_LHW23_LHW24_AGENT_INTELLIGENCE_ROADMAP_2026-05-31.md`
- `docs/audits/CVF_IMPORTANT_FULL_FILE_SCAN_BLINDSPOT_RECORD_2026-05-31.md`
- `.private_reference/legacy/CVF_Important/ADDING_MODEL_ROUTER/CVF_MODEL_REGISTRY_SERVICE.md`
- `.private_reference/legacy/CVF_Important/ADDING_MODEL_ROUTER/CVF_ROUTING_POLICY_ENGINE.md`
- `.private_reference/legacy/CVF_Important/ADDING_MODEL GATEWAY/CVF_EXECUTION_STRATEGY_MODEL.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- `EXTENSIONS/CVF_PLANE_FACADES/src/execution.facade.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts`
- `governance/compat/check_work_order_dispatch_quality.py`

## Pre-Flight Checks

Do not run implementation checks until the HOLD is released. When released,
capture a non-empty base and run:

```bash
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base <baseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <baseHead> --head HEAD
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS model registry source concept | `.private_reference/legacy/CVF_Important/ADDING_MODEL_ROUTER/CVF_MODEL_REGISTRY_SERVICE.md` | Model router source file | `Model Registry` | Future advisory map to model gateway registry surface | ACCEPT |
| EXISTS multi-factor routing source concept | `.private_reference/legacy/CVF_Important/ADDING_MODEL_ROUTER/CVF_ROUTING_POLICY_ENGINE.md` | Routing policy source file | `Routing Policy` | Future advisory map to routing policy owner surface | ACCEPT |
| EXISTS execution strategy source concept | `.private_reference/legacy/CVF_Important/ADDING_MODEL GATEWAY/CVF_EXECUTION_STRATEGY_MODEL.md` | Execution strategy source file | `Execution Strategy` | Future advisory map to execution facade/orchestrator surfaces | ACCEPT |
| EXISTS current provider registry surface | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | Runtime source file | `ProviderRegistry` | `ProviderRegistry` | ACCEPT |
| EXISTS current provider capability registry surface | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | Runtime source file | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry module | ACCEPT |
| EXISTS current routing policy surface | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | Runtime source file | `RoutingPolicyEngine` | `RoutingPolicyEngine` | ACCEPT |
| EXISTS current role provider resolver | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | Runtime source file | `resolveProviderForRole` | `resolveProviderForRole` | ACCEPT |
| EXISTS current execution facade surface | `EXTENSIONS/CVF_PLANE_FACADES/src/execution.facade.ts` | Runtime source file | `executeGovernedTask` | execution facade | ACCEPT |
| EXISTS current web orchestrator surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | Runtime source file | `runPipelineChain` | pipeline-chain orchestrator | ACCEPT |

## Current Runtime Freshness Verification

LHW23 must not claim that CVF has no provider registry or that routing is only
hardcoded strings. Current source shows provider and capability registry
surfaces already exist. The remaining advisory gap is narrower: normalize a
single capability-aware model registry and route-decision contract across the
current provider registry, capability registry, routing policy, role resolver,
execution facade, and web orchestration surfaces.

| Runtime surface | Current source checked | Freshness disposition |
|---|---|---|
| Provider registry | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` | EXISTS; do not describe as absent |
| Provider capability registry | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | EXISTS; advisory work must map to it |
| Routing policy engine | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | EXISTS as partial owner surface |
| Role resolver | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | EXISTS; cite this path for `resolveProviderForRole` |
| Execution facade | `EXTENSIONS/CVF_PLANE_FACADES/src/execution.facade.ts` | EXISTS; future strategy mapping only |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Release / closure evidence required |
|---|---|---|
| LHW23 waits for LHW22 | Keep status `HOLD_UNTIL_LHW22_PASS` | LHW22 PASS evidence before dispatch |
| T1 model registry service advisory | Author T1 only after fresh LHW23 GC-018 | Spec/review paths and current registry mapping |
| T2 multi-factor routing policy advisory | Author T2 only after runtime freshness check | Spec/review paths and route owner mapping |
| T3 execution strategy model advisory | Author T3 only after runtime freshness check | Spec/review paths and facade/orchestrator mapping |
| No stale provider absence claims | Cite current provider registry surfaces | Source table and freshness table |

## Write Ownership

While on HOLD, this file is planning material only. After hold release, write
ownership is limited to the LHW23 GC-018 baseline, the LHW23 spec/review files
listed above, this work order, the parent roadmap, and closure continuity files.

## Execution Plan

1. Stop if LHW22 PASS evidence is not present.
2. Create a fresh LHW23 GC-018 baseline with current runtime source paths.
3. Author T1/T2/T3 specs as documentation-only advisory connectors.
4. Author completion reviews with closure diff and machine evidence.
5. Keep all runtime changes out of scope.

## Evidence Requirements

- LHW22 PASS closure reference.
- Fresh LHW23 GC-018 baseline.
- `git diff --name-status <baseHead> HEAD`.
- Work-order dispatch quality guard on a non-empty range.
- Autorun pre-dispatch, pre-implementation, and pre-closure gates.
- Public export disposition guard.
- Explicit `N/A with reason` for live proof and public-sync.

## Acceptance Criteria

| Criterion | Required disposition |
|---|---|
| LHW22 predecessor evidence exists before dispatch | PASS |
| Fresh LHW23 GC-018 exists before specs | PASS |
| Current registry/routing owner paths are cited | PASS |
| Specs do not claim missing provider registry surfaces | PASS |
| No runtime, route, public-sync, or live-provider work occurs | PASS |

## Review Gate

The reviewer must reject any LHW23 completion that uses stale provider absence
language, cites `resolveProviderForRole` without the current `execute.client.ts`
path, or converts advisory routing concepts into runtime claims.

## Closure Checklist

| Item | Resolution |
|---|---|
| LHW22 PASS prerequisite verified | HOLD |
| Fresh LHW23 GC-018 created | HOLD |
| Source Verification Block refreshed | HOLD |
| Runtime freshness table refreshed | HOLD |
| Closure Diff Gate completed | HOLD |

## Return-To-Orchestrator Conditions

Return this order if LHW22 evidence is missing, fresh LHW23 GC-018 cannot be
created, current runtime paths differ from this draft, provider registry claims
become stale, or implementation requires code/public/live changes.

## Operator Checkpoint

PENDING_AFTER_LHW22_PASS. This order is not ready for worker execution until
Orchestrator releases the hold.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Private planning packet only. No public-sync artifact or public catalog claim is
authorized.

## Claim Boundary

This work order is a held documentation plan. It does not authorize runtime
routing changes, provider selection changes, model registry mutation, live
proof, public release, or LHW24 execution.
