# CVF GC-018 N6 - AIF graph_search Activation

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-24

## Purpose

Authorize the bounded AIF-C Phase 2b activation of `graph_search` in
`memory-retrieval-policy.ts` using the AIF-B in-memory `GraphKnowledgeService`
surface.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`
- `docs/work_orders/CVF_WO_N6_AIF_GRAPH_SEARCH_ACTIVATION_2026-05-24.md`
- `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md`

## Decision / Baseline / Proposed Tranche

Decision: continue with in-memory-only advisory `graph_search` activation.

Baseline: AIF-C Phase 2a has local retrieval policy; AIF-B has an in-memory
graph service.

Proposed tranche: inject `GraphKnowledgeService` into the retrieval policy and
map graph nodes to summary-only retrieval candidates.

## Scope

In scope:

- activate `graph_search` for local advisory retrieval;
- inject `GraphKnowledgeService` through an interface parameter;
- preserve `rawMemoryReleased=false`;
- preserve `canReinject=false` runtime-memory invariant;
- add targeted Learning Plane tests.

Out of scope:

- durable graph storage;
- live `/api/execute` reinjection;
- provider, route, receipt, or public-sync change;
- delegating governance decisions to graph results.

## Legacy Spec Scan Block

| Source | Classification | Decision |
| --- | --- | --- |
| `.private_reference/legacy/CVF 16.5/agentmemory/` | partially absorbed | Retrieval policy concepts are absorbed only for local policy evaluation. Durable/live/cross-session memory remains out of scope. |
| `.private_reference/legacy/CVF ADD/code-review-graph/` | runtime-owned Phase 1 | AIF-B graph service is used as advisory context only. No scoring or authority expansion. |

## Interface Finding

The work order mentioned `GraphKnowledgeService.query(TaskQuery): GraphNode[]`,
but the delivered AIF-B interface is `queryImpact(...) : GraphQueryResult`.
That contract is sufficient because `resolvedNodes` provides the candidate node
set required by `graph_search`; no schema/interface change is needed.

## Acceptance Criteria

N6 passes only if targeted graph-search tests pass, full LPF tests pass,
TypeScript passes, `GraphKnowledgeService` interface remains unchanged, and
`canReinject=false` tests still pass.

## Evidence / Verification

Verification requires targeted LPF tests, full LPF tests, LPF TypeScript check,
and review evidence that graph output remains advisory only.

## Claim Boundary

N6 can claim only bounded in-memory `graph_search` activation for advisory
retrieval. It does not claim durable persistence, live reinjection, graph
authority, public readiness, or production readiness.
