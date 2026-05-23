# CVF Work Order: PBR-04 Graph SQLite Persistence

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-24

Tranche: PBR-04

Roadmap: `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Add SQLite-backed persistence to `GraphKnowledgeService` so the symbol index
survives server restarts. Currently AIF-B builds the graph in RAM on each
startup — all indexed knowledge is lost on restart. PBR-04 adds a
`better-sqlite3` storage layer that serializes the `SymbolIndex` to disk and
rehydrates it on next startup.

Design constraint: persistence is a storage detail only. The `GraphKnowledgeService`
interface contract must remain unchanged — callers (`memory-retrieval-policy.ts`
and any N6 consumer) see zero API change.

---

## Authorization

Operator authorized on 2026-05-24 with the following auto-trigger condition:

> "sẽ kế tiếp nhau, nếu đủ điều kiện mà không cần chờ hỏi lại tôi"
> (will follow in sequence, proceed automatically if conditions are met without
> asking again)

**Auto-start conditions (all must be true — Codex self-checks):**

1. N6 tranche is `CLOSED_PASS` (completion review filed and committed)
2. N6 tests all PASS (LPF full suite, TypeScript check)
3. `canReinject=false` invariant still passes after N6
4. `GraphKnowledgeService` interface required no changes during N6 implementation

If any condition fails, Codex must return to operator before proceeding.

**Do not begin PBR-04 until all 4 auto-start conditions are verified.**

---

## Authority Chain

Operator (pre-authorized 2026-05-24) → Claude (roadmap author) → Codex (implementer).

Parent roadmap: `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Agent Roles

- Operator: pre-authorized; no re-confirmation needed if auto-start conditions met
- Claude: GC-018 reviewer
- Codex: implementer

---

## Required First Reads

Before filing GC-018 (mandatory):

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/schema/graph-schema.ts` — `GraphKnowledgeService` interface + `SymbolIndex` type
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts` — current in-memory `SymbolIndex` implementation
- `docs/reviews/CVF_N6_AIF_GRAPH_SEARCH_ACTIVATION_COMPLETION_2026-05-24.md` — N6 completion evidence (confirms interface stability)
- `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md` — AIF-B delivery baseline
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` — agentmemory and code-review-graph rows (Legacy Spec Scan Block required in GC-018)

---

## Pre-Flight Checks

Before implementation:

1. Verify all 4 auto-start conditions above are met
2. Confirm `better-sqlite3` is not already a dependency — check `package.json`
3. GC-023 line count check for `symbol-index.ts` before modifying
4. Confirm `GraphKnowledgeService` interface in `graph-schema.ts` has NOT changed
   since AIF-B delivery (interface must be stable before adding persistence)
5. Design the SQLite schema before writing code — review with GC-018

---

## Write Ownership

Codex owns:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/index/symbol-index.ts` — add SQLite serialization/deserialization methods
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/storage/` (new directory) — `graph-sqlite-store.ts` storage adapter
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/knowledge/graph/storage/graph-sqlite-store.test.ts` — targeted storage tests
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json` — add `better-sqlite3` dependency
- `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md` — PBR-04 row update

`GraphKnowledgeService` interface (`graph-schema.ts`) must NOT be changed.
`memory-retrieval-policy.ts` must NOT be changed (N6 already wired it correctly).
No route, provider, receipt, or public-sync change.

---

## SQLite Schema (design target)

```sql
CREATE TABLE IF NOT EXISTS symbol_nodes (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,
  name TEXT NOT NULL,
  filePath TEXT NOT NULL,
  startLine INTEGER,
  endLine INTEGER,
  metadata TEXT  -- JSON blob for extensible fields
);

CREATE TABLE IF NOT EXISTS symbol_edges (
  fromId TEXT NOT NULL,
  toId TEXT NOT NULL,
  edgeKind TEXT NOT NULL,
  PRIMARY KEY (fromId, toId, edgeKind)
);

CREATE TABLE IF NOT EXISTS index_metadata (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
-- key='builtAt' stores ISO timestamp; key='fileCount' stores count
```

Codex may adjust schema during GC-018 review — above is a design target, not
a frozen spec. Any schema deviation must be documented in the GC-018.

---

## Execution Plan

1. Verify all 4 auto-start conditions (N6 CLOSED_PASS, tests PASS, canReinject=false, interface unchanged)
2. File GC-018 with Legacy Spec Scan Block
3. Read all Required First Reads
4. Add `better-sqlite3` to `package.json`; confirm TypeScript types available (`@types/better-sqlite3`)
5. Create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/storage/graph-sqlite-store.ts`:
   - `GraphSQLiteStore` class implementing `save(index: SymbolIndex, dbPath: string): void`
   - `load(dbPath: string): SymbolIndex | null` (returns null if no DB exists yet)
6. Modify `symbol-index.ts` to accept optional `GraphSQLiteStore` — on `buildIndex()` completion, call `store.save()`; on init, attempt `store.load()` before rebuilding
7. Inject `GraphSQLiteStore` via constructor parameter (optional, defaults to no-op in-memory mode — preserves backward compatibility for tests)
8. Write targeted storage tests: save → load roundtrip, empty DB returns null, corrupt DB handled gracefully
9. Confirm `GraphKnowledgeService` interface unchanged
10. Confirm `canReinject=false` invariant still passes
11. Run full LPF test suite → PASS
12. Run TypeScript check → PASS
13. Update roadmap Progress Tracker PBR-04 row → `CLOSED_PASS`
14. File completion review
15. Commit

---

## Evidence Requirements

- `GraphSQLiteStore` save/load roundtrip tests PASS
- `GraphKnowledgeService` interface unchanged (confirmed in completion review)
- `canReinject=false` invariant still passes
- Full LPF test suite PASS
- TypeScript check PASS
- GC-023 compliant for all modified files
- Completion review with schema design documented

---

## Scope / Target / Owner Boundary

In scope:

- SQLite persistence layer for `SymbolIndex` only
- `better-sqlite3` dependency addition
- Storage adapter + targeted tests

Out of scope:

- `GraphKnowledgeService` interface change (FORBIDDEN — breaks N6 consumer)
- `memory-retrieval-policy.ts` change (N6 already completed this)
- Cross-session memory for non-graph surfaces
- Live reinjection on production route
- Migration tooling for schema changes (deferred to a future tranche)
- Public-sync, provider, or receipt changes

**Design doctrine preserved:**

- Graph is advisory evidence, NOT authorization
- Persistence adds durability only — no new query capabilities
- Interface stability is non-negotiable: `GraphKnowledgeService.query()` signature unchanged

---

## Acceptance Criteria

- [ ] All 4 auto-start conditions verified
- [ ] GC-018 filed and accepted (with Legacy Spec Scan Block)
- [ ] `better-sqlite3` added to `package.json`
- [ ] `GraphSQLiteStore` storage adapter created
- [ ] `symbol-index.ts` wired to optional persistence (backward-compatible)
- [ ] Save/load roundtrip tests PASS
- [ ] `GraphKnowledgeService` interface unchanged
- [ ] `canReinject=false` invariant preserved
- [ ] Full LPF test suite PASS
- [ ] TypeScript check PASS
- [ ] GC-023 compliant for all modified files
- [ ] Roadmap Progress Tracker PBR-04 row → `CLOSED_PASS`
- [ ] Completion review filed

---

## Review Gate

Claude reviews the completion package for:

- Interface stability confirmed (`graph-schema.ts` diff is empty)
- Storage adapter backward-compatible (optional injection, no-op default)
- `canReinject=false` confirmed
- LPF full suite PASS; TypeScript PASS; GC-023 compliant
- Bounded wording in completion review (persistence only, no new capability claims)

---

## Return-To-Orchestrator Conditions

Return to Claude when all closure checklist items are complete, or when:

- Any auto-start condition was not met (must return to operator)
- `GraphKnowledgeService` interface needed a change during N6 (schema design must be revised)
- `better-sqlite3` causes TypeScript or build conflict
- LPF test suite regression

---

## Operator Checkpoint

operator.checkpoint.waiver: PBR-04 is pre-authorized by operator on 2026-05-24
under auto-trigger condition — no re-confirmation required provided all 4
auto-start conditions in the Authorization section are verified by Codex before
implementation begins. If any auto-start condition fails, return to operator.

---

## Closure Checklist

- [ ] All 4 auto-start conditions verified (N6 CLOSED_PASS, tests PASS, canReinject=false, interface unchanged)
- [ ] GC-018 filed and accepted (with Legacy Spec Scan Block)
- [ ] Required first reads complete
- [ ] `better-sqlite3` added to `package.json`
- [ ] `GraphSQLiteStore` storage adapter created at `src/knowledge/graph/storage/graph-sqlite-store.ts`
- [ ] `symbol-index.ts` wired to optional persistence (backward-compatible injection)
- [ ] Save/load roundtrip tests PASS
- [ ] `GraphKnowledgeService` interface unchanged (confirmed by diff)
- [ ] `canReinject=false` invariant preserved
- [ ] Full LPF test suite PASS
- [ ] TypeScript check PASS
- [ ] GC-023 compliant for all modified files
- [ ] Roadmap PBR-04 row → `CLOSED_PASS`
- [ ] Completion review filed

---

## Completion Review

After implementation, file at:
`docs/reviews/CVF_PBR04_GRAPH_SQLITE_PERSIST_COMPLETION_2026-05-24.md`

Minimum sections: Purpose, Auto-Start Condition Verification (all 4), Schema
Design, Save/Load Roundtrip Evidence, Interface Stability Confirmation,
`canReinject=false` Confirmation, Claim Boundary.

---

## Claim Boundary

This work order does not authorize: `GraphKnowledgeService` interface change,
`memory-retrieval-policy.ts` change, cross-session memory for non-graph surfaces,
live reinjection, migration tooling, public-sync update, provider change, or any
governance decision delegated to the graph layer. One capability added: symbol
index survives restart.
