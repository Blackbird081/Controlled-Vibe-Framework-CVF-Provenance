# CVF Post-AIF Next Value Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE_ROADMAP_AUTHORIZED_FOR_DISPATCH

docType: roadmap

Date: 2026-05-24

---

## Purpose

Coordinate the four next-value tranches that follow AIF A/B/C closure (HEAD
`cc6836bf`). These tranches fall into two tiers: Fast Lane eligible (no GC-018
required) and demand-gated (operator confirmation required before
implementation).

---

## Authorization / Decision

Operator directed on 2026-05-24: "all. create work order for codex".

- **N4 (Skill Corpus Repair):** Fast Lane eligible — pure bug fix, no runtime
  change, no governance semantic change.
- **N5 (Catalog Update):** Fast Lane eligible — documentation only, updates
  existing rows to reflect proven state.
- **N6 (AIF Phase 2 Extensions):** Demand-gated. Operator's 2026-05-24
  direction is treated as in-memory-only confirmation for AIF-C Phase 2b
  (`graph_search` activation); durable graph storage (SQLite) requires PBR-04
  lift.
- **N7 (Third Provider Expansion):** Operator authorized 2026-05-24. Provider
  confirmed: OpenAI, model `gpt-4o`, `maxRiskLevel=R2`, key `OPENAI_API_KEY`
  (present in `.env.local`). Narrow live proof required; broad stability claim
  not authorized.

---

## Owner / Source

Owner: Claude (roadmap author), Codex (implementer), operator (authorizer).

Predecessor evidence (read before any tranche):

- `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`

---

## Scope / Target / Owner Boundary

In scope:

- N4: `skill-corpus-governance.test.ts` fix — `process.cwd()` path resolution
  in vitest + re-run regeneration script if needed
- N5: `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` row
  updates for AIF-delivered surfaces (graph, memory gateway, operational index)
- N6: `memory-retrieval-policy.ts` `graph_search` activation using AIF-B
  `GraphKnowledgeService`; AIF-C Phase 2b wiring
- N7: Third provider addition (operator-nominated) with GC-018 + capability
  registry update + targeted tests

Out of scope:

- SQLite / durable graph storage (PBR-04 auto-authorized after N6 CLOSED_PASS — not before)
- Cross-session memory
- Kernel-owner replacement (D-06, requires freeze-release packet)
- Global freeze lift (D-07, rejected under binding rule)
- Public-sync push (separate operator authorization required)

---

## Non-Goals

This roadmap does not authorize:

- Any claim of full universal provider parity
- Production / hosted readiness
- Memory reinjection on live `/api/execute` route
- Broader provider stability beyond the specific nominated provider
- Database or persistence layer

---

## Work Plan

```text
N4  ──── Fast Lane; begin immediately (skill corpus test fix)
N5  ──── Fast Lane; begin immediately (catalog update)
N6  ──── Demand-gated; requires operator to name nominated provider for graph_search; AIF-B interface already exported
N7  ──── Demand-gated; requires operator to name the third provider before GC-018
```

N4 and N5 are independent and can run in parallel.
N6 depends on AIF-B `GraphKnowledgeService` (already delivered).
N7 is independent of N4/N5/N6.

---

## Acceptance Criteria

- [ ] N4: `skill-corpus-governance.test.ts` 4/4 PASS; `cvf-web` full test suite
      regression-clean
- [ ] N4: Progress Tracker updated to `CLOSED_PASS`; completion review filed
- [ ] N5: Catalog rows for graph, memory gateway, operational index updated to
      `proven (Phase 1 in-memory)` with correct evidence paths
- [ ] N5: Progress Tracker updated to `CLOSED_PASS`; completion review filed
- [ ] N6: Operator confirms `graph_search` activation scope; GC-018 filed and
      accepted; `memory-retrieval-policy.ts` `graph_search` branch active;
      LPF test suite PASS; TypeScript check PASS
- [ ] N6: Progress Tracker updated to `CLOSED_PASS`; completion review filed
- [ ] N7: Operator names third provider; GC-018 filed and accepted; provider
      capability registry updated; targeted tests PASS
- [ ] N7: Progress Tracker updated to `CLOSED_PASS`; completion review filed

---

## Verification / Evidence

After each tranche closes, the implementer must produce:

1. Completion review at `docs/reviews/CVF_N<X>_<NAME>_COMPLETION_2026-05-24.md`
2. Test suite PASS receipt (if applicable)
3. TypeScript check PASS receipt (if applicable)
4. Progress Tracker row updated in this roadmap
5. Entry updated in `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
   (if applicable)

---

## Progress Tracker

| Tranche | Name | Status | Completion review | Notes |
| --- | --- | --- | --- | --- |
| N4 | Skill Corpus Test Repair | `WORK_ORDER_READY` | — | Fast Lane; `process.cwd()` fix in vitest |
| N5 | Public Catalog AIF Update | `WORK_ORDER_READY` | — | Fast Lane; doc-only row updates |
| N6 | AIF Phase 2 graph_search Activation | `WORK_ORDER_READY` | — | Operator authorized 2026-05-24; in-memory-only; AIF-B interface ready |
| N7 | Third Provider Expansion | `WORK_ORDER_READY` | — | Operator authorized 2026-05-24: OpenAI / gpt-4o / R2 / OPENAI_API_KEY |
| PBR-04 | Graph SQLite Persist | `AUTO_AUTHORIZED_AFTER_N6` | — | Auto-starts after N6 CLOSED_PASS; no SQLite until N6 proves interface stable |

---

## Execution Order

```text
N4  ──── WORK_ORDER_READY (start immediately)
N5  ──── WORK_ORDER_READY (start immediately, parallel with N4)
N6      ──── WORK_ORDER_READY (operator authorized 2026-05-24)
PBR-04  ──── AUTO_AUTHORIZED after N6 CLOSED_PASS (no operator re-confirmation needed)
N7      ──── WORK_ORDER_READY (operator authorized 2026-05-24: OpenAI/gpt-4o/R2)
```

---

## Governance Notes

### Why N4 and N5 are Fast Lane

N4 is a pure test-path fix — `process.cwd()` in `readFileSync` resolves to the
wrong directory when vitest runs from the repo root. No runtime, provider, or
governance semantic change.

N5 is documentation only — updating existing catalog rows from `roadmap` to
`proven (Phase 1 in-memory)` with verified evidence paths. No new capability
claimed beyond what AIF delivery proved.

### Why N6 and N7 are demand-gated

N6 wires `graph_search` to live retrieval using the AIF-B `GraphKnowledgeService`
interface. This is the first live consumer of the graph engine. Scope and depth
must be confirmed before implementation.

N7 adds a new provider, which touches `providers.ts`,
`provider-router-adapter.ts`, and `PROVIDER_CAPABILITY_REGISTRY`. These are
governed surfaces requiring a fresh GC-018.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| N4 fix breaks other test infrastructure (wrong root assumption) | Run full `cvf-web` test suite after fix; confirm 2747+ pass count |
| N5 catalog rows cite paths that don't exist in public-sync | Run Test-Path verification in public-sync clone before any public-sync commit |
| N6 `graph_search` wiring causes latency regression | Benchmark before/after; gate on no regression to existing retrieval methods |
| N7 provider addition breaks router fallback logic | Targeted router tests required; existing Alibaba + DeepSeek receipts must still pass |

---

## Related Artifacts

- `docs/work_orders/CVF_WO_N4_SKILL_CORPUS_TEST_REPAIR_2026-05-24.md`
- `docs/work_orders/CVF_WO_N5_CATALOG_AIF_UPDATE_2026-05-24.md`
- `docs/work_orders/CVF_WO_N6_AIF_GRAPH_SEARCH_ACTIVATION_2026-05-24.md`
- `docs/work_orders/CVF_WO_PBR04_GRAPH_SQLITE_PERSIST_2026-05-24.md`
- `docs/work_orders/CVF_WO_N7_THIRD_PROVIDER_EXPANSION_2026-05-24.md`
- `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`

---

## Claim Boundary

This roadmap authorizes N4 and N5 immediately under Fast Lane. N6 and N7 are
`DEMAND_GATED` — they are not authorized for implementation until the operator
confirms the required scope decisions and fresh GC-018 packets are filed and
accepted for each.

This roadmap does not authorize: durable graph storage, cross-session memory,
live reinjection, kernel-owner replacement, global freeze lift, public-sync
update, or production readiness claim.
