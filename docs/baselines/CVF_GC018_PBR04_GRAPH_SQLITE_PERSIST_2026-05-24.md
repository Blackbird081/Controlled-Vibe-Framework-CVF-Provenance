# CVF GC-018 PBR-04 - Graph SQLite Persistence

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-24

## Purpose

Authorize a SQLite-backed persistence adapter for the AIF-B symbol index after
N6 closed pass and proved the graph-search consumer interface stable.

## Source / Predecessor Evidence

- `docs/work_orders/CVF_WO_PBR04_GRAPH_SQLITE_PERSIST_2026-05-24.md`
- `docs/reviews/CVF_N6_AIF_GRAPH_SEARCH_ACTIVATION_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts`

## Decision / Baseline / Proposed Tranche

Decision: continue with optional SQLite persistence for the graph symbol index.

Baseline: AIF-B and N6 use the stable `GraphKnowledgeService` interface.

Proposed tranche: add a `GraphSQLiteStore` adapter and optional injection into
the in-memory graph service without changing callers.

## Auto-Start Verification

| Condition | Result |
| --- | --- |
| N6 closed pass evidence exists | PASS - `docs/reviews/CVF_N6_AIF_GRAPH_SEARCH_ACTIVATION_COMPLETION_2026-05-24.md` |
| N6 targeted/full LPF tests pass | PASS - targeted 25/25; full LPF 1555/1555 |
| `canReinject=false` invariant preserved | PASS - `runtime-memory-hierarchy.test.ts` pass |
| `GraphKnowledgeService` interface unchanged | PASS - no `graph-schema.ts` diff |

## Scope

In scope:

- add `better-sqlite3` and `@types/better-sqlite3`;
- create `GraphSQLiteStore`;
- wire optional persistence into `createInMemoryGraphKnowledgeService`;
- preserve `GraphKnowledgeService` interface;
- add targeted storage tests.

Out of scope:

- changing `memory-retrieval-policy.ts` after N6;
- cross-session memory for non-graph surfaces;
- live reinjection;
- migration tooling;
- public-sync, provider, route, or receipt changes.

## Legacy Spec Scan Block

| Source | Classification | Decision |
| --- | --- | --- |
| `.private_reference/legacy/CVF ADD/code-review-graph/` | runtime-owned | Adds durability to the symbol index only; scoring and authority remain deferred. |
| `.private_reference/legacy/CVF 16.5/agentmemory/` | partially absorbed | Does not change memory-tier or reinjection behavior. |

## SQLite Schema

The implementation keeps the work-order table shape and stores confidence/line
data in JSON metadata:

- `symbol_nodes(id, kind, name, filePath, startLine, endLine, metadata)`
- `symbol_edges(fromId, toId, edgeKind, metadata)`
- `index_metadata(key, value)`

## Evidence / Verification

Verification requires save/load roundtrip tests, corrupt/missing DB tests, LPF
full suite, LPF TypeScript check, and confirmation that `graph-schema.ts` is
unchanged.

## Claim Boundary

PBR-04 can claim only that the graph symbol index can be saved to and restored
from SQLite through an optional adapter. It does not claim database governance,
live memory reinjection, migration readiness, or production readiness.
