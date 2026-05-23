# CVF Work Order: N5 Public Catalog AIF Update

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-24

Tranche: N5

Roadmap: `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Update `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` to reflect
the three new surfaces delivered by AIF A/B/C (HEAD `f9e2f82d`). The catalog
currently shows "Graph/code-intelligence context: roadmap" — this is stale.
AIF-B delivered Phase 1 in-memory graph (schema, AST parser, symbol index,
task-query mapper, `GraphKnowledgeService` interface). AIF-C delivered Memory
Gateway Phase 2a (lifecycle decay, retrieval policy, context packager, gateway
interface). AIF-A delivered the Operational Reference Index.

---

## Authority Chain

Operator → Claude (roadmap author) → Codex (implementer).

Authorization: Fast Lane (GC-021). Documentation only — updating existing rows
to reflect proven delivered state. No new capability claimed, no runtime change.

---

## Agent Roles

- Codex: implementer — updates catalog rows; runs Test-Path verification
- Claude: reviewer — confirms all paths verified, no overclaim
- Operator: pre-authorized under Fast Lane

---

## Required First Reads

Before implementing:

- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` — current state
- `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md` — AIF-B evidence
- `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md` — AIF-C evidence
- `docs/reviews/CVF_AIF_A_OPERATIONAL_REFERENCE_INDEX_COMPLETION_2026-05-24.md` — AIF-A evidence
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` — AIF-A deliverable

---

## Pre-Flight Checks

1. Confirm `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` exists
2. Check GC-023 line count before editing — do not exceed threshold
3. Verify all new evidence paths exist in the governance repo with `Test-Path`
4. Do NOT run Test-Path in governance repo for paths that will be public-sync targets — note those separately for a future public-sync commit

---

## Write Ownership

Codex owns:

- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (row updates only)

No other files may be modified. Public-sync copy is out of scope for this work order.

---

## Execution Plan

1. Read the full catalog file
2. Identify and update these rows:

   **Row to update:** `Graph/code-intelligence context | roadmap | ...`
   → Change to: `Graph/code-intelligence context (Phase 1) | proven — Phase 1 in-memory AST foundation | evidence: AIF-B completion review + LPF test suite 1550/1550 PASS`
   Evidence path: `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md`

   **Row to add or update:** Memory gateway / lifecycle / retrieval
   → `Memory Gateway Phase 2a | proven — in-memory lifecycle decay + retrieval policy + context packager; canReinject=false preserved | evidence: AIF-C completion review`
   Evidence path: `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md`

   **Row to add:** Operational Reference Index
   → `Operational Reference Index | proven — agent discoverability lookup table deployed | evidence: AIF-A completion review`
   Evidence path: `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`

3. Verify all cited paths exist with Test-Path in governance repo
4. Add a dated update note at the bottom of the catalog file (one line)
5. Check GC-023 — if adding rows would exceed threshold, keep additions minimal (one sentence per new row)
6. Update roadmap Progress Tracker N5 row → `CLOSED_PASS`
7. File completion review
8. Commit

---

## Evidence Requirements

- All cited paths pass Test-Path in governance repo
- GC-023 compliant for modified catalog file
- No overclaim: all new rows bounded to "Phase 1 in-memory" and "bounded proof"
- Completion review filed

---

## Scope / Target / Owner Boundary

In scope:

- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` row updates (3 rows)

Out of scope:

- Public-sync copy of the catalog — separate work order required
- Any new section additions (requires fresh GC-018 per catalog update rule)
- Any provider, receipt, runtime, or source code change
- Claiming Phase 2 capabilities (durable storage, live reinjection, graph_search) not yet delivered

**Boundary:** All new rows must be bounded to "Phase 1 in-memory" and must
not claim: durable persistence, cross-session memory, live reinjection,
`graph_search` activation (deferred to N6), or broad provider stability.

---

## Acceptance Criteria

- [ ] `Graph/code-intelligence context` row updated from `roadmap` to `proven (Phase 1 in-memory)`
- [ ] Memory Gateway Phase 2a row added/updated with bounded wording
- [ ] Operational Reference Index row added with evidence path
- [ ] All cited paths pass Test-Path in governance repo
- [ ] GC-023 compliant for modified catalog file
- [ ] No overclaim beyond delivered Phase 1 state
- [ ] Roadmap Progress Tracker N5 row → `CLOSED_PASS`
- [ ] Completion review filed

---

## Review Gate

Claude reviews the completion package for:

- Correct row updates — no overclaim, bounded language only
- All paths verified (Test-Path PASS for each)
- GC-023 compliant
- Public-sync copy explicitly deferred and noted

---

## Closure Checklist

- [ ] Read current catalog
- [ ] 3 row updates applied with bounded wording
- [ ] All cited paths Test-Path PASS in governance repo
- [ ] GC-023 compliant
- [ ] No overclaim
- [ ] Roadmap N5 row → `CLOSED_PASS`
- [ ] Completion review filed

---

## Return-To-Orchestrator Conditions

Return to Claude when:

- All closure checklist items above are complete
- OR: a blocker is encountered (e.g., GC-023 threshold exceeded, path not found)

---

## Operator Checkpoint

operator.checkpoint.waiver: N5 is documentation-only Fast Lane work — updating
existing catalog rows to reflect proven delivered state. Pre-authorized under
operator directive on 2026-05-24.

---

## Completion Review

After implementation, file at:
`docs/reviews/CVF_N5_CATALOG_AIF_UPDATE_COMPLETION_2026-05-24.md`

Minimum sections: Purpose, Rows Updated (each with Test-Path result), Bounded
Wording Verification, Claim Boundary.

---

## Claim Boundary

This work order authorizes only catalog row updates for AIF-delivered surfaces.
It does not authorize: public-sync push, new catalog sections, Phase 2
capability claims, durable storage claims, live reinjection claims, or
`graph_search` activation claims.
