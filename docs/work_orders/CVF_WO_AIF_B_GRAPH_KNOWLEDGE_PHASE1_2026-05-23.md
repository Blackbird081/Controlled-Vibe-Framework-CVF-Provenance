# CVF Work Order: AIF-B Graph Knowledge Phase 1

Memory class: FULL_RECORD

Status: DEMAND_GATED_NOT_AUTHORIZED

docType: work_order

Date: 2026-05-23

Tranche: AIF-B

Roadmap: `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`

---

## Purpose

Implement Graph Knowledge Phase 1 by absorbing the `code-review-graph` spec set
(CVF ADD) into CVF. The `ScopedKnowledgeProvider` boundary exists but the AST
graph engine, dependency index, blast-radius resolver, and context builder are
not implemented.

Phase 1 scopes to an in-memory structural index (AST parsing + symbol graph +
task-to-query mapper) without requiring durable SQLite storage. Phase 2 (storage)
requires PBR-04 persistence lift and is separately gated.

---

## STOP — This work order is DEMAND_GATED

**Do not begin implementation until ALL of the following are satisfied:**

1. Operator explicitly confirms: either (a) PBR-04 persistence block is lifted,
   OR (b) Phase 1 in-memory-only scope is confirmed as acceptable without storage
2. A fresh GC-018 is filed and accepted (use GC-018 template with Legacy Spec
   Scan Block)
3. Codex has read all 5 `code-review-graph` spec files and filed the scan block
4. The GC-018 includes an explicit Phase 1 vs Phase 2 scope declaration

**When the operator authorizes this work order, update Status from
`DEMAND_GATED_NOT_AUTHORIZED` to `READY_FOR_IMPLEMENTATION` and file the
required GC-018.**

---

## Authority Chain

Operator → Claude (roadmap author) → Codex (implementer).

Authorization: DEMAND_GATED. This work order is not authorized for implementation
until the operator grants the required blocked-work overrides (see STOP section).
Parent roadmap: `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`.

---

## Agent Roles

- Operator: authorizer — must grant PBR-04 lift or in-memory scope confirmation
- Claude: GC-018 reviewer — confirms Legacy Spec Scan Block is complete
- Codex: implementer — reads all 5 code-review-graph specs before implementing

---

## Required First Reads

Before filing GC-018 (mandatory):

- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/reference/CVF_SCOPED_KNOWLEDGE_PROVIDER_BOUNDARY_DOCTRINE_2026-05-07.md`
- All 5 spec files under `.private_reference/legacy/CVF ADD/code-review-graph/`

---

## Pre-Flight Checks

Before any implementation:

1. Operator confirms PBR-04 decision or Phase 1 in-memory-only scope
2. GC-018 filed and accepted with Legacy Spec Scan Block complete
3. All 5 code-review-graph spec files read; file-by-file table in GC-018
4. GC-023 line count check for all target files in `CVF_LEARNING_PLANE_FOUNDATION`

---

## Write Ownership

Codex owns (Phase 1 only):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/ast/ast-parser.ts` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context_builder/graph/task-query-mapper.ts` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/` — targeted tests (new)
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` — code-review-graph row update
- `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md` — AIF-B row update

No provider, receipt, route, public-sync, or storage changes.

---

## Execution Plan

1. Receive operator authorization and GC-018 acceptance
2. Read all 5 code-review-graph spec files
3. Complete file-by-file absorption table in GC-018
4. Implement Module 1: `graph-schema.ts` (typed schema)
5. Implement Module 2: `ast-parser.ts` (TypeScript compiler API)
6. Implement Module 3: `symbol-index.ts` (in-memory index)
7. Implement Module 4: `task-query-mapper.ts` (task-to-query mapper)
8. Export `GraphKnowledgeService` interface for AIF-C
9. Write targeted tests for all modules
10. Run full `CVF_LEARNING_PLANE_FOUNDATION` test suite and TypeScript check
11. Update registry code-review-graph row
12. Update roadmap Progress Tracker AIF-B row
13. File completion review

---

## Evidence Requirements

- Full `CVF_LEARNING_PLANE_FOUNDATION` test suite PASS
- TypeScript check PASS
- GC-023 line count compliant for all new files
- `GraphKnowledgeService` interface exported and documented
- Legacy Spec Scan Block in GC-018 verified
- Completion review filed

---

## Owner / Source

Owner: Codex (implementer), Claude (reviewer), operator (authorizer).

Predecessor evidence (mandatory reading before GC-018):

- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
  (code-review-graph row — `boundary_absorbed_engine_missing`)
- `docs/reference/CVF_SCOPED_KNOWLEDGE_PROVIDER_BOUNDARY_DOCTRINE_2026-05-07.md`
- `docs/roadmaps/archive/CVF_ADD_E1_SCOPED_KNOWLEDGE_RUNTIME_ADOPTION_ROADMAP_2026-05-17.md`
- `.private_reference/legacy/CVF ADD/code-review-graph/` — all 5 spec files:
  - `CVF_GRAPH_KNOWLEDGE_SPEC.md`
  - `CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md`
  - `CVF_GRAPH_IMPLEMENTATION_PLAN.md`
  - `CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md`
  - `CVF_GRAPH_SCORING_SPEC.md`

---

## Scope / Target / Owner Boundary

Target surfaces (Phase 1 in-memory only):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/ast/` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/context_builder/graph/` (new)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/` — targeted tests

Target surfaces (Phase 2 — gated on PBR-04):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/storage/` (deferred)
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/scoring/` (deferred)

Out of scope for Phase 1:

- No SQLite or external storage
- No blast-radius UI surface
- No public product claim for code intelligence
- No provider, receipt, route, or public-sync change
- `graph_search` in AIF-C memory retrieval depends on this; AIF-B Phase 1 must
  expose a clean interface for AIF-C to consume

**Design doctrine (preserved from source specs, non-negotiable):**

- Graph is a **knowledge service**, NOT a runtime
- Local structural index, NOT a decision-maker
- Signal provider, NOT authorization engine
- Graph must not directly authorize any action or override governance decisions

---

## Legacy Spec Scan Block (required in GC-018)

```text
Legacy Spec Scan Block
- Registry read: docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md
- Legacy folders scanned:
  - .private_reference/legacy/CVF ADD/code-review-graph/ (all 5 files)
- Existing absorption evidence checked:
  - docs/reference/CVF_SCOPED_KNOWLEDGE_PROVIDER_BOUNDARY_DOCTRINE_2026-05-07.md
  - EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/scoped.knowledge.provider.contract.ts
  - docs/roadmaps/archive/CVF_ADD_E1_SCOPED_KNOWLEDGE_RUNTIME_ADOPTION_ROADMAP_2026-05-17.md
  - docs/reviews/CVF_LEGACY_SCOPE_ABSORPTION_AUDIT_MATRIX_2026-05-18.md
- File-by-file absorption table:
  | File | Status in this tranche | Reason if deferred |
  | CVF_GRAPH_KNOWLEDGE_SPEC.md | absorbed / partial / deferred | ... |
  | CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md | ... | ... |
  | CVF_GRAPH_IMPLEMENTATION_PLAN.md | ... | ... |
  | CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md | ... | ... |
  | CVF_GRAPH_SCORING_SPEC.md | deferred to Phase 2 | requires storage layer |
- Blindspot risk verdict: CLEAR (all 5 files explicitly covered)
```

---

## Phase 1 Deliverables (in-memory, no persistence)

### Module 1: `knowledge/graph/schema/graph-schema.ts`

Typed schema from `CVF_GRAPH_KNOWLEDGE_SPEC.md`:

- `GraphNode` — symbol, file, function, class, import
- `GraphEdge` — dependency, call, import, export
- `DependencyGraph` — nodes + edges + metadata

### Module 2: `knowledge/graph/ast/ast-parser.ts`

AST parsing layer from `CVF_GRAPH_KNOWLEDGE_SPEC.md` Phase 1:

- `parseFileToAST(filePath, source)` → AST node list
- `extractSymbols(ast)` → `GraphNode[]`
- `extractDependencies(ast)` → `GraphEdge[]`

Implementation note: use TypeScript compiler API (`ts.createSourceFile`) for
TypeScript/JavaScript parsing. Do not introduce Tree-sitter as a new dependency
without Codex confirming it is already available or operator approving the
dependency addition.

### Module 3: `knowledge/graph/index/symbol-index.ts`

In-memory symbol index from `CVF_GRAPH_KNOWLEDGE_SPEC.md`:

- `SymbolIndex` — in-memory map of file → symbols + dependencies
- `buildIndex(files)` → `SymbolIndex`
- `lookupSymbol(name)` → `GraphNode | null`
- `getDependencies(node)` → `GraphNode[]`

### Module 4: `context_builder/graph/task-query-mapper.ts`

Task-to-query mapper from `CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md`:

- `TaskQuery` — typed query: symbol names, file paths, depth
- `mapTaskToQuery(taskDescription, hints)` → `TaskQuery`
- `resolveBlastRadius(query, index)` → `GraphNode[]` (affected nodes)

### Interface for AIF-C consumption

Phase 1 must expose a clean interface that AIF-C's `graph_search` retrieval
method can consume:

```typescript
export interface GraphKnowledgeService {
  buildIndex(files: string[]): Promise<SymbolIndex>;
  query(q: TaskQuery): GraphNode[];
  getBlastRadius(node: GraphNode): GraphNode[];
}
```

This interface is the only integration surface. AIF-C imports this; it does
not directly access AST internals.

---

## GC-023 Pre-flight (required before implementation)

Before creating new directories/modules in `CVF_LEARNING_PLANE_FOUNDATION`:

1. Check current `src/index.ts` line count
2. New modules go in subdirectories, not appended to `index.ts`
3. Each new file is subject to GC-023 threshold (general_source: advisory >700, hard >1000)
4. Check exception registry for existing entries

---

## Acceptance Criteria

- [ ] Operator decision on PBR-04 / Phase 1 in-memory scope confirmed
- [ ] GC-018 filed and accepted with Legacy Spec Scan Block complete
- [ ] All 5 code-review-graph spec files read; file-by-file table in GC-018
- [ ] Design doctrine preserved: graph is knowledge service, not runtime
- [ ] `graph-schema.ts` implemented and tested
- [ ] `ast-parser.ts` implemented and tested (using TypeScript compiler API or
      approved alternative)
- [ ] `symbol-index.ts` implemented and tested
- [ ] `task-query-mapper.ts` implemented and tested
- [ ] `GraphKnowledgeService` interface exported for AIF-C consumption
- [ ] Storage layer (`knowledge/graph/storage/`) explicitly deferred and
      documented in completion review
- [ ] `CVF_LEARNING_PLANE_FOUNDATION` full test suite PASS
- [ ] TypeScript check PASS
- [ ] GC-023 line count compliant for all new files
- [ ] `CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` code-review-graph row
      updated to reflect new absorption status
- [ ] Roadmap Progress Tracker AIF-B row updated to `CLOSED_PASS`
- [ ] `CVF_SESSION_MEMORY.md` pointer added
- [ ] Handoff Latest Work section updated with HEAD SHA

---

## Review Gate

Claude reviews the completion package for:

- All 4 Phase 1 modules implemented with targeted tests
- `GraphKnowledgeService` interface exported
- Design doctrine preserved (graph is knowledge service, NOT runtime)
- `CVF_LEARNING_PLANE_FOUNDATION` full test suite PASS
- TypeScript check PASS
- GC-023 compliant for all new files
- Storage layer explicitly deferred and documented

---

## Closure Checklist

- [ ] Operator granted PBR-04 lift or in-memory scope confirmation
- [ ] GC-018 filed and accepted with Legacy Spec Scan Block
- [ ] All 5 spec files read; file-by-file table complete
- [ ] `graph-schema.ts` implemented and tested
- [ ] `ast-parser.ts` implemented and tested
- [ ] `symbol-index.ts` implemented and tested
- [ ] `task-query-mapper.ts` implemented and tested
- [ ] `GraphKnowledgeService` interface exported
- [ ] `CVF_LEARNING_PLANE_FOUNDATION` full test suite PASS
- [ ] TypeScript check PASS
- [ ] GC-023 compliant for all new files
- [ ] Registry code-review-graph row updated
- [ ] Roadmap Progress Tracker AIF-B row → `CLOSED_PASS`
- [ ] `CVF_SESSION_MEMORY.md` pointer added
- [ ] Handoff Latest Work updated with HEAD SHA
- [ ] Completion review filed

---

## Return-To-Orchestrator Conditions

Return to Claude (reviewer) when:

- All closure checklist items above are complete
- OR: a blocker is encountered (e.g., TypeScript compiler API unavailable, GC-023 threshold exceeded)

Do not return partial work. File the completion review before returning.

---

## Operator Checkpoint

Checkpoint required: operator must explicitly confirm one of: (a) PBR-04 persistence block is lifted, OR (b) Phase 1 in-memory-only scope is acceptable without SQLite storage — before implementation proceeds.

---

## Completion Review

After implementation, file at:
`docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-23.md`

Minimum sections: Purpose, Legacy Spec Scan Block (verified), Phase 1 vs Phase 2
scope declaration, Design Doctrine Preservation evidence, Deliverables Verified
(per module), `GraphKnowledgeService` interface published (for AIF-C), Acceptance
Criteria (checklist), Claim Boundary.

---

## Claim Boundary

This work order does not authorize: SQLite or durable graph storage (Phase 2),
blast-radius UI surface, public code-intelligence product claim, provider change,
receipt schema change, freeze release, or direct governance decision-making by
the graph layer. The graph is a knowledge service and signal provider only.
