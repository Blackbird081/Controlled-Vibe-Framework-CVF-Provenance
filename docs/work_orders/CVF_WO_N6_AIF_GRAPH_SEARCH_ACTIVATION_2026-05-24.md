# CVF Work Order: N6 AIF graph_search Activation (Phase 2b)

Memory class: FULL_RECORD

Status: DEMAND_GATED_NOT_AUTHORIZED

docType: work_order

Date: 2026-05-24

Tranche: N6

Roadmap: `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Activate `graph_search` in `memory-retrieval-policy.ts` by wiring it to the
`GraphKnowledgeService` interface delivered by AIF-B. This is AIF-C Phase 2b
— currently `graph_search` returns a `DEFERRED` stub. Phase 2b makes it a live
retrieval path using the in-memory AST/symbol index.

---

## STOP — This work order is DEMAND_GATED

**Do not begin implementation until ALL of the following are satisfied:**

1. Operator explicitly confirms scope: in-memory-only `graph_search` activation
   (no SQLite, no durable storage) is acceptable
2. A fresh GC-018 is filed and accepted
3. Codex confirms `GraphKnowledgeService.query()` contract is sufficient for
   `graph_search` retrieval needs (read AIF-B completion review and
   `graph-schema.ts` interface before filing GC-018)
4. GC-023 line count check for `memory-retrieval-policy.ts` before adding code

**When the operator authorizes this work order, update Status from
`DEMAND_GATED_NOT_AUTHORIZED` to `READY_FOR_IMPLEMENTATION` and file the
required GC-018.**

---

## Authority Chain

Operator → Claude (roadmap author) → Codex (implementer).

Authorization: DEMAND_GATED. Parent roadmap:
`docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`.

---

## Agent Roles

- Operator: authorizer — must confirm in-memory-only scope
- Claude: GC-018 reviewer
- Codex: implementer

---

## Required First Reads

Before filing GC-018 (mandatory):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` — current stub at `graph_search` branch
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` — `GraphKnowledgeService` interface
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts` — `SymbolIndex` contract
- `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md` — AIF-B delivery evidence
- `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md` — AIF-C Phase 2a delivery evidence
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` — agentmemory and code-review-graph rows

---

## Pre-Flight Checks

Before implementation:

1. Operator confirms in-memory-only scope
2. GC-018 filed and accepted
3. `GraphKnowledgeService` interface read; confirm `query(TaskQuery): GraphNode[]` is sufficient
4. GC-023 line count check: `memory-retrieval-policy.ts` is currently 122 lines; threshold advisory at 700, hard at 1000 — safe to add
5. Confirm `canReinject=false` invariant still passes before touching any memory code

---

## Write Ownership

Codex owns:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` (activate `graph_search` branch)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-policy.test.ts` (add `graph_search` tests)
- `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md` — N6 row update

No provider, receipt, route, public-sync, or durable persistence changes.

---

## Execution Plan

1. Receive operator authorization and GC-018 acceptance
2. Read all Required First Reads
3. Understand `GraphKnowledgeService.query(TaskQuery): GraphNode[]` contract
4. In `memory-retrieval-policy.ts`: replace `graph_search` DEFERRED stub with
   call to `GraphKnowledgeService.query()` — translate `MemoryRetrievalRequest`
   query into a `TaskQuery`, call `query()`, translate `GraphNode[]` results
   into `MemoryRetrievalResult`
5. Inject `GraphKnowledgeService` via constructor/parameter (do not hardcode
   a concrete implementation — keep the interface boundary clean)
6. Add targeted tests for `graph_search` path in `memory-retrieval-policy.test.ts`
7. Confirm `canReinject=false` invariant still passes
8. Run full `CVF_LEARNING_PLANE_FOUNDATION` test suite → PASS
9. Run TypeScript check → PASS
10. Update roadmap Progress Tracker N6 row → `CLOSED_PASS`
11. File completion review
12. Commit

---

## Evidence Requirements

- `memory-retrieval-policy.ts` `graph_search` branch is active (not DEFERRED stub)
- New tests for `graph_search` path PASS
- `canReinject=false` invariant still passes
- Full LPF test suite PASS
- TypeScript check PASS
- GC-023 compliant

---

## Scope / Target / Owner Boundary

In scope (Phase 2b only):

- `memory-retrieval-policy.ts` `graph_search` activation
- Targeted new tests

Out of scope:

- SQLite or durable graph storage (Phase 2 of AIF-B — PBR-04 still deferred)
- Cross-session memory
- Live reinjection on production route
- `GraphKnowledgeService` implementation changes (AIF-B delivered; do not modify)
- Public-sync, provider, or receipt changes

**Design doctrine preserved:**

- Graph is advisory evidence, NOT authorization
- `graph_search` returns candidate nodes for context enrichment only
- No governance decision may be delegated to the graph layer

---

## Acceptance Criteria

- [ ] Operator confirms in-memory-only scope
- [ ] GC-018 filed and accepted
- [ ] `memory-retrieval-policy.ts` `graph_search` branch active (not DEFERRED stub)
- [ ] `GraphKnowledgeService` injected via interface (not hardcoded)
- [ ] Targeted `graph_search` tests PASS
- [ ] `canReinject=false` invariant still passes
- [ ] Full LPF test suite PASS
- [ ] TypeScript check PASS
- [ ] GC-023 compliant for modified files
- [ ] Roadmap Progress Tracker N6 row → `CLOSED_PASS`
- [ ] Completion review filed

---

## Review Gate

Claude reviews the completion package for:

- `graph_search` branch active and wired to `GraphKnowledgeService.query()`
- Interface injection (not hardcoded concrete implementation)
- Design doctrine preserved (graph is advisory only)
- `canReinject=false` invariant confirmed
- LPF test suite PASS; TypeScript PASS; GC-023 compliant

---

## Closure Checklist

- [ ] Operator authorization received
- [ ] GC-018 filed and accepted
- [ ] Required first reads complete
- [ ] `graph_search` branch active
- [ ] Interface injection pattern used
- [ ] Tests PASS
- [ ] `canReinject=false` preserved
- [ ] LPF full suite PASS
- [ ] TypeScript check PASS
- [ ] GC-023 compliant
- [ ] Roadmap N6 row → `CLOSED_PASS`
- [ ] Completion review filed

---

## Return-To-Orchestrator Conditions

Return to Claude when all closure checklist items are complete, or when a
blocker is encountered (e.g., `GraphKnowledgeService` interface insufficient,
`canReinject=false` regression).

---

## Operator Checkpoint

Checkpoint required: operator must explicitly confirm that in-memory-only
`graph_search` activation (no SQLite, no durable storage) is the intended scope
before implementation proceeds.

---

## Completion Review

After implementation, file at:
`docs/reviews/CVF_N6_AIF_GRAPH_SEARCH_ACTIVATION_COMPLETION_2026-05-24.md`

Minimum sections: Purpose, GC-018 reference, Interface Injection evidence,
Design Doctrine Preservation, Test Evidence, `canReinject=false` confirmation,
Claim Boundary.

---

## Claim Boundary

This work order does not authorize: durable graph storage, cross-session memory,
live reinjection on production route, SQLite, public-sync update, provider
change, or any governance decision delegated to the graph layer.
