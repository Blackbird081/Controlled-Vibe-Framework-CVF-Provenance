# CVF N6 AIF graph_search Activation Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS

Date: 2026-05-24

## Purpose

Close N6 after activating `graph_search` in the local Memory Retrieval Policy
using the AIF-B `GraphKnowledgeService` interface.

## Target / Source

Targets:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-policy.test.ts`

Source: `docs/work_orders/CVF_WO_N6_AIF_GRAPH_SEARCH_ACTIVATION_2026-05-24.md`.

## Scope / Target / Owner Boundary

In scope: local advisory `graph_search` activation and targeted tests.

Out of scope: durable graph storage, live reinjection, route/provider/receipt
changes, public-sync, or graph authority.

## Scope / Methodology

Read the AIF-B/AIF-C surfaces, confirmed the delivered interface, injected the
graph service through policy options, and mapped graph nodes to summary-only
retrieval candidates.

## Findings / Position

Position: N6 is closed pass. The older work-order `query(TaskQuery)` wording was
superseded by the actual `queryImpact()` interface, which was sufficient.

## Risk / Corrective Action

Risk: graph results could be mistaken for authorization. Corrective action:
graph candidates are advisory summaries only, unauthorized actors are denied
before graph use, and `rawMemoryReleased=false` remains fixed.

## Decision / Recommendation / Disposition

Disposition: CLOSED_PASS.

## GC-018 Reference

`docs/baselines/CVF_GC018_N6_AIF_GRAPH_SEARCH_ACTIVATION_2026-05-24.md`

## Interface Injection Evidence

`evaluateRetrievalRequest()` now accepts optional
`MemoryRetrievalPolicyOptions.graphKnowledgeService`. When the service is
present, `graph_search` calls `queryImpact()` and maps `resolvedNodes` into
summary-only `MemoryRetrievalCandidate` records. When absent, the branch returns
a deterministic deferred status.

The delivered AIF-B interface is `queryImpact(...) : GraphQueryResult`, not the
older work-order wording `query(TaskQuery): GraphNode[]`; no interface change
was required.

## Design Doctrine Preservation

Graph results are advisory evidence only:

- `rawMemoryReleased=false` is preserved;
- generated candidates are summaries, not raw memory;
- graph output is never used as an authorization decision;
- unauthorized actors are denied before graph service use.

## Test Evidence

- Targeted LPF run:
  `npm test -- --run tests/memory-retrieval-policy.test.ts tests/controlled-memory-gateway.test.ts tests/symbol-index.test.ts tests/knowledge/graph/storage/graph-sqlite-store.test.ts tests/runtime-memory-hierarchy.test.ts`
  - PASS: 5 files / 25 tests.
- Full LPF:
  `npm test`
  - PASS: 59 files / 1555 tests.
- LPF TypeScript:
  `npm run check`
  - PASS.

## canReinject=false Confirmation

`tests/runtime-memory-hierarchy.test.ts` passed in the targeted and full LPF
runs. N6 did not change memory tier rules.

## GC-023

`memory-retrieval-policy.ts` is 202 lines.

## Claim Boundary

N6 proves only local in-memory advisory `graph_search` activation. It does not
prove durable graph storage, live route reinjection, graph scoring,
authorization by graph, public-sync readiness, hosted readiness, or production
readiness.
