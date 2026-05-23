# CVF Agent Intelligence Foundations Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE_ROADMAP_AIF_A_AUTHORIZED_FOR_DISPATCH

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

AIF-B and AIF-C are `DEMAND_GATED`. Neither may begin implementation until the
operator grants the required blocked-work overrides listed in their respective
work orders.

This roadmap is created under the operator direction to "lên roadmap để xử lý
trước cả 3 option A, B, C luôn, tạo work order cho Codex thi công" on 2026-05-23.

---

## Owner / Source

Owner: Claude (roadmap author), Codex (implementer), operator (authorizer).

Predecessor evidence (mandatory reading before any tranche):

- `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md`
- `docs/reviews/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_CODEX_REVIEW_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `docs/roadmaps/CVF_REVIEW_CVF_PAIN_POINT_DELIVERY_GAP_ROADMAP_V2_2026-05-22.md`

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
- Any implementation from AIF-B or AIF-C without operator unblock

---

## Work Plan

```text
AIF-A  ──── (standalone, Fast Lane, start immediately)
AIF-C  ──── (demand-gated; can run after operator lifts memory block)
AIF-B  ──── (demand-gated; requires PBR-04 persistence lift or in-memory confirmation)
```

Per-tranche work plan is in the individual work orders under `docs/work_orders/`.

---

## Acceptance Criteria

- [ ] AIF-A: `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` created with all required rows
- [ ] AIF-A: Progress Tracker updated to `CLOSED_PASS`; completion review filed
- [ ] AIF-C: Operator grants `new_memory_tiers_beyond_lane_h_scope` override
- [ ] AIF-C: Phase 2a modules implemented, tested, TypeScript check PASS
- [ ] AIF-C: Progress Tracker updated to `CLOSED_PASS`; completion review filed
- [ ] AIF-B: Operator lifts PBR-04 block or confirms in-memory-only scope
- [ ] AIF-B: Phase 1 modules implemented, tested, TypeScript check PASS
- [ ] AIF-B: `GraphKnowledgeService` interface exported for AIF-C consumption
- [ ] AIF-B: Progress Tracker updated to `CLOSED_PASS`; completion review filed
- [ ] Legacy Spec Absorption Registry updated after each tranche

---

## Verification / Evidence

After each tranche closes, the implementer must produce:

1. A completion review at `docs/reviews/CVF_AIF_<X>_<NAME>_COMPLETION_2026-05-23.md`
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
| AIF-A | Operational Reference Index | `WORK_ORDER_READY` | — | Fast Lane eligible; no GC-018 required |
| AIF-B | Graph Knowledge Phase 1 | `DEMAND_GATED` | — | Blocked by PBR-04 (persistence); requires operator lift |
| AIF-C | Memory Gateway Phase 2 | `DEMAND_GATED` | — | Blocked by `new_memory_tiers_beyond_lane_h_scope`; requires operator override |

---

## Execution Order

```text
AIF-A  ──── (standalone, Fast Lane, start immediately)
AIF-C  ──── (demand-gated; can run after operator lifts memory block)
AIF-B  ──── (demand-gated; requires PBR-04 persistence lift; can follow AIF-C)
```

AIF-A does not block AIF-B or AIF-C. AIF-C does not require AIF-B. AIF-B's
`graph_search` retrieval method is enhanced by AIF-C but can proceed
independently once PBR-04 is lifted.

---

## AIF-A — Operational Reference Index

**Status:** `WORK_ORDER_READY`

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

**Status:** `DEMAND_GATED`

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
- `memory-retrieval-policy.ts` — keyword + semantic retrieval (recency optional)
- `memory-context-packager.ts` — `[MEMORY_CONTEXT]` block output format
- Targeted tests for each module

Phase 2b (requires PBR-04 if graph_search needed):

- `memory-retrieval-policy.ts` extension: `graph_search` (waits for AIF-B)

**Preconditions before GC-018:**

1. Operator grants explicit blocked-work override for
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

**Status:** `DEMAND_GATED`

**Work order:** `docs/work_orders/CVF_WO_AIF_B_GRAPH_KNOWLEDGE_PHASE1_2026-05-23.md`

**Problem this solves:**

`code-review-graph` specs describe a structural code intelligence layer
(AST → dependency graph → blast radius → minimal context pack) that does
not exist in CVF. The `ScopedKnowledgeProvider` boundary exists but the
engine is not implemented. T-GRAPH was identified as demand-gated successor
in Codex commit `069957a7`.

**Source specs:**

- `.private_reference/legacy/CVF ADD/code-review-graph/` — all 5 spec files
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/scoped.knowledge.provider.contract.ts`
  — existing boundary

**Deliverables (when authorized):**

Phase 1 (AST foundation + in-memory graph; no SQLite required):

- `knowledge/graph/ast/` — Tree-sitter AST parser for TypeScript/JavaScript
- `knowledge/graph/index/` — symbol index from AST output
- `knowledge/graph/schema/` — graph node/edge schema
- `context_builder/graph/task_query_mapper.ts` — task → graph query
- Targeted tests

Phase 2 (storage; requires PBR-04 persistence lift):

- `knowledge/graph/storage/` — SQLite-backed graph store
- `knowledge/graph/scoring/` — relevance scoring for context packs

**Preconditions before GC-018:**

1. Operator lifts PBR-04 persistence block (or Phase 1 scoped to in-memory only)
2. Legacy Spec Scan Block completed (read all 5 code-review-graph files)
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

AIF-C touches `new_memory_tiers_beyond_lane_h_scope` — a currently blocked
work class. Operator must explicitly lift this class for AIF-C.

AIF-B requires either: (a) PBR-04 persistence lift for SQLite storage, or
(b) operator confirmation that Phase 1 in-memory-only scope is acceptable.
No path exists without one of these two decisions.

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

This roadmap authorizes AIF-A immediately under Fast Lane. AIF-B and AIF-C
are `DEMAND_GATED` — they are not authorized for implementation until the
operator grants the required blocked-work overrides and a fresh GC-018 is
filed and accepted for each.

This roadmap does not authorize: runtime memory expansion, graph engine
implementation, durable persistence, public-sync update, provider change,
receipt schema change, freeze release, or kernel-owner replacement.
