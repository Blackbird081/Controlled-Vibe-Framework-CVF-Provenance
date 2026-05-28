# CVF Agent Intelligence Foundations Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS

docType: roadmap

Date: 2026-05-23

---

## Purpose

This roadmap coordinates the three Agent Intelligence Foundations tranches
(AIF-A, AIF-B, AIF-C) that address the remaining CVF capability gaps
surfaced by the 2026-05-23 legacy spec absorption blindspot audit and
Codex correction review.

Progress tracking is embedded in this file. Update the status table after
each tranche closes so every future agent has a single source of truth.

---

## Authorization / Decision

AIF-A is authorized immediately under Fast Lane (GC-021) — documentation only,
no GC-018 required.

AIF-B and AIF-C were originally `DEMAND_GATED`. The operator's 2026-05-24
instruction to complete the roadmap and work orders is recorded as:

- AIF-C: explicit `new_memory_tiers_beyond_lane_h_scope` override.
- AIF-B: confirmation that Phase 1 remains in-memory-only, with no PBR-04
  durable persistence lift.

This roadmap is created under the operator direction to "lên roadmap để xử lý
trước cả 3 option A, B, C luôn, tạo work order cho Codex thi công" on 2026-05-23.

---

## Owner / Source

Owner: Claude (roadmap author), Codex (implementer), operator (authorizer).

Predecessor evidence (mandatory reading before any tranche):

- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/roadmaps/archive/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`

---

## Scope / Target / Owner Boundary

In scope:

- AIF-A: `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` (new)
- AIF-B: `knowledge/graph/` foundation in `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/`
  (demand-gated; see preconditions)
- AIF-C: Memory Gateway Phase 2 in `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/`
  (demand-gated; see preconditions)

Out of scope for this roadmap:

- provider/receipt/route/public-sync changes
- freeze release, kernel-owner replacement, global lift
- durable persistence / database (PBR-04 still deferred)
- any Qwen3/hosted proof work (requires separate GC-018)

---

## Non-Goals

This roadmap does not authorize:

- SQLite or durable graph storage (Phase 2 of AIF-B; gated on PBR-04)
- Live reinjection on `/api/execute` production route
- Blast-radius UI surface
- Public code-intelligence product claim
- Cross-session memory
- Any source-code change from AIF-A
- Any durable or live-provider expansion beyond the 2026-05-24 operator unblock

---

## Work Plan

```text
AIF-A  ──── CLOSED_PASS (standalone, Fast Lane)
AIF-C  ──── CLOSED_PASS (operator override; Phase 2a local/in-memory)
AIF-B  ──── CLOSED_PASS (operator confirmed Phase 1 in-memory only)
```

Per-tranche work plan is in the individual work orders under `docs/work_orders/`.

---

## Acceptance Criteria

- [x] AIF-A: `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` created with all required rows
- [x] AIF-A: Progress Tracker updated to `CLOSED_PASS`; completion review filed
- [x] AIF-C: Operator grants `new_memory_tiers_beyond_lane_h_scope` override
- [x] AIF-C: Phase 2a modules implemented, tested, TypeScript check PASS
- [x] AIF-C: Progress Tracker updated to `CLOSED_PASS`; completion review filed
- [x] AIF-B: Operator lifts PBR-04 block or confirms in-memory-only scope
- [x] AIF-B: Phase 1 modules implemented, tested, TypeScript check PASS
- [x] AIF-B: `GraphKnowledgeService` interface exported for AIF-C consumption
- [x] AIF-B: Progress Tracker updated to `CLOSED_PASS`; completion review filed
- [x] Legacy Spec Absorption Registry updated after each tranche

---

## Verification / Evidence

After each tranche closes, the implementer must produce:

1. A completion review at `docs/reviews/CVF_AIF_<X>_<NAME>_COMPLETION_2026-05-24.md`
2. A test suite PASS receipt (if applicable)
3. A TypeScript check PASS receipt (if applicable)
4. An updated Progress Tracker row in this roadmap
5. An updated entry in `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`

---

## Progress Tracker

This table is the authoritative live status for all three tranches.
**Update this table and the per-tranche status field after each closure.**

| Tranche | Name | Status | Completion review | Notes |
| --- | --- | --- | --- | --- |
| AIF-A | Operational Reference Index | `CLOSED_PASS` | `docs/reviews/CVF_AIF_A_OPERATIONAL_REFERENCE_INDEX_COMPLETION_2026-05-24.md` | Fast Lane docs-only index created |
| AIF-B | Graph Knowledge Phase 1 | `CLOSED_PASS` | `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md` | Phase 1 in-memory only; PBR-04 persistence not lifted; missing scoring-spec reference corrected |
| AIF-C | Memory Gateway Phase 2 | `CLOSED_PASS` | `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md` | Phase 2a local policy modules; no durable/live reinjection claim |

---

## Execution Order

```text
AIF-A  ──── CLOSED_PASS
AIF-C  ──── CLOSED_PASS
AIF-B  ──── CLOSED_PASS
```

AIF-A, AIF-C, and AIF-B are closed for the bounded foundation scope. Future
durable graph storage, live memory reinjection, or graph-search activation
requires a fresh GC-018.

---

## AIF-A — Operational Reference Index

**Status:** `CLOSED_PASS`

**Work order:** `docs/work_orders/CVF_WO_AIF_A_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`

**Problem this solves:**

CVF has a file taxonomy (`docs/INDEX.md`) that answers "where to put" but not
"what exists." Agent discoverability fails because there is no "when task X →
read document Y" index. This caused the 2026-05-23 blindspot: the audit
methodology had no step that said "when scoping memory work → read agentmemory
specs."

**Deliverables:**

- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` — a single
  lookup table: task category → required reading. Covers at minimum:
  - Memory/hierarchy work → agentmemory specs + registry
  - Graph/context-builder work → code-review-graph specs + registry
  - Qwen3/hosted proof → prerequisites reference
  - Provider tranche → providers.ts + provider-router-adapter.ts + registry
  - Pain-point closure → Review CVF.md + gap audit + Codex correction
  - New GC-018 → GC-018 template + Legacy Spec Scan Block
  - Public-sync → public-sync rule (CLAUDE.md) + catalog update rule

**Governance:** Fast Lane (GC-021). Documentation only; no source code change.
No GC-018 required.

**Completion criteria:**

- Reference index file created under `docs/reference/`
- Pointer added in `CVF_SESSION_MEMORY.md` Required First Reads
- Pointer added in `ACTIVE_SESSION_STATE.json` `nextAllowedMove`
- Pointer added in handoff Latest Work section
- Progress tracker table in this roadmap updated to `CLOSED_PASS`

---

## AIF-C — Memory Gateway Phase 2

**Status:** `CLOSED_PASS`

**Work order:** `docs/work_orders/CVF_WO_AIF_C_MEMORY_GATEWAY_PHASE2_2026-05-23.md`

**Problem this solves:**

T5 (ephemeral task store) absorbed only `canReinject=false` + tier classifier
from the 10-file `agentmemory` spec set. The remaining Pain H scope —
lifecycle decay, semantic/graph retrieval, context packager, privacy filter,
reinjection protocol — is unimplemented. T-H2 was identified as demand-gated
successor in Codex commit `069957a7`.

**Source specs:**

- `.private_reference/legacy/CVF 16.5/agentmemory/` — all 10 files
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/` — existing partial absorption

**Deliverables (when authorized):**

Phase 2a (in-memory, no persistence required):

- `controlled-memory-gateway.ts` — gateway interface (entry/exit contract)
- `memory-lifecycle-policy.ts` — lifecycle decay: working → episodic → semantic
- `memory-retrieval-policy.ts` — keyword, semantic, recency, and audit-trust retrieval
- `memory-context-packager.ts` — `[MEMORY_CONTEXT]` block output format
- Targeted tests for each module

Phase 2b (requires PBR-04 if graph_search needed):

- `memory-retrieval-policy.ts` extension: `graph_search` (waits for AIF-B)

**Preconditions before GC-018:**

1. Operator granted explicit blocked-work override for
   `new_memory_tiers_beyond_lane_h_scope`
2. Legacy Spec Scan Block completed (read all 10 agentmemory files)
3. File-by-file absorption table: which files are absorbed, partial, deferred
4. No durable persistence, no public memory-readiness claim
5. GC-023 line count check on all target files before adding

**Completion criteria:**

- Phase 2a modules implemented and tested in `CVF_LEARNING_PLANE_FOUNDATION`
- All new tests PASS
- TypeScript check PASS
- Progress tracker table in this roadmap updated to `CLOSED_PASS`
- `CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` agentmemory row updated

---

## AIF-B — Graph Knowledge Phase 1

**Status:** `CLOSED_PASS`

**Work order:** `docs/work_orders/CVF_WO_AIF_B_GRAPH_KNOWLEDGE_PHASE1_2026-05-23.md`

**Problem this solves:**

`code-review-graph` specs describe a structural code intelligence layer
(AST → dependency graph → blast radius → minimal context pack) that does
not exist in CVF. The `ScopedKnowledgeProvider` boundary exists but the
engine is not implemented. T-GRAPH was identified as demand-gated successor
in Codex commit `069957a7`.

**Source specs:**

- `.private_reference/legacy/CVF ADD/code-review-graph/` — actual source bundle
  of 5 `CVF_GRAPH_*` files plus README and metadata. The stale work-order
  reference to `CVF_GRAPH_SCORING_SPEC.md` was corrected because that file does
  not exist.
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/scoped.knowledge.provider.contract.ts`
  — existing boundary

**Deliverables (when authorized):**

Phase 1 (AST foundation + in-memory graph; no SQLite required):

- `knowledge/graph/ast/` — TypeScript compiler AST parser for TypeScript/JavaScript
- `knowledge/graph/index/` — symbol index from AST output
- `knowledge/graph/schema/` — graph node/edge schema
- `context_builder/graph/task_query_mapper.ts` — task → graph query
- Targeted tests

Phase 2 (storage; requires PBR-04 persistence lift):

- `knowledge/graph/storage/` — SQLite-backed graph store
- `knowledge/graph/scoring/` — relevance scoring for context packs

**Preconditions before GC-018:**

1. Operator confirmed Phase 1 scoped to in-memory only; PBR-04 persistence is not lifted
2. Legacy Spec Scan Block completed (read actual code-review-graph bundle)
3. Explicit scope declaration: which phase and which modules
4. Design doctrine preserved: graph is a knowledge service, NOT a runtime;
   local structural index, NOT a decision-maker; signal provider, NOT
   authorization engine
5. GC-023 line count check on all target files

**Completion criteria:**

- Phase 1 modules implemented and tested
- All new tests PASS
- TypeScript check PASS
- Progress tracker table in this roadmap updated to `CLOSED_PASS`
- `CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` code-review-graph row updated

---

## Governance Notes

### Why AIF-A is Fast Lane

AIF-A is documentation only. It creates one new reference file and adds
pointers in session state. It makes no runtime, provider, receipt, or schema
change. It satisfies all seven GC-021 Fast Lane criteria.

### Why AIF-C and AIF-B are demand-gated

AIF-C touched `new_memory_tiers_beyond_lane_h_scope`; the operator explicitly
lifted this class for the bounded Phase 2a work on 2026-05-24.

AIF-B required either: (a) PBR-04 persistence lift for SQLite storage, or
(b) operator confirmation that Phase 1 in-memory-only scope is acceptable. The
operator confirmed the in-memory-only path on 2026-05-24; PBR-04 remains
closed.

### Continuous update rule

After each tranche closes:

1. Update the Progress Tracker table (Status column + Completion review column).
2. Update `CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` for the
   affected source folder.
3. Add a pointer in `CVF_SESSION_MEMORY.md`.
4. Update `ACTIVE_SESSION_STATE.json` `nextAllowedMove`.
5. Add HEAD SHA to active handoff Latest Work section.

**Do not leave the tracker stale.** Stale trackers are the documented cause of
agents "forgetting what CVF already knows."

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| AIF-A deployed but AIF-C/B trackers not updated → future agent thinks C/B are still pending | After each closure update this file immediately; commit with descriptive message |
| AIF-C scoped without reading agentmemory specs → repeats blindspot | Legacy Spec Scan Block mandatory in AIF-C GC-018 |
| AIF-B scoped with PBR-04 still blocked → dead-ends at storage layer | Confirm PBR-04 status before opening AIF-B GC-018 |
| AIF-A index becomes stale as new docs added | Add "update index" to Tranche Closure Checklist for future tranches |

---

## Related Artifacts

- `docs/work_orders/CVF_WO_AIF_A_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/work_orders/CVF_WO_AIF_C_MEMORY_GATEWAY_PHASE2_2026-05-23.md`
- `docs/work_orders/CVF_WO_AIF_B_GRAPH_KNOWLEDGE_PHASE1_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`

---

## Claim Boundary

This roadmap is closed pass for AIF-A, AIF-C Phase 2a, and AIF-B Phase 1.

This roadmap does not authorize: durable persistence, live memory reinjection,
public-sync update, provider change, receipt schema change, freeze release,
kernel-owner replacement, autonomous graph approval/denial, or broad product
readiness claims.
