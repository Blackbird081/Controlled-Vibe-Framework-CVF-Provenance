# CVF R1/R2/P2 Post-M1 Gap Closure Roadmap

Memory class: SUMMARY_RECORD

Status: PARTIAL_PASS_R2_P2_GATED

docType: roadmap

Date: 2026-05-24

---

## Purpose

Translate the post-M1/P1 audit into a bounded follow-on roadmap. The audit
found one immediate implementation defect, one route-level value gap, and one
non-coder onboarding gap.

---

## Authorization / Decision

Decision: R1 is authorized as a fast-lane corrective bugfix because it is
localized to the M1 durable store and does not change route behavior or public
claims.

Decision: R2 and P2 are registered as next work orders but remain
`DEMAND_GATED`. R2 needs a fresh GC-018 before `/api/execute` behavior changes.
P2 needs a public/onboarding gate before any public self-onboarding claim is
updated.

---

## Scope / Target / Owner Boundary

Target surfaces:

- LPF durable memory store resilience.
- Web `/api/execute` route durable-memory wiring.
- Non-coder Step 0 provider-key setup documentation.

Owner: CVF memory, web execution route, and public onboarding surfaces.

Boundary: this roadmap does not authorize autonomous memory reinjection, graph
approval authority, universal provider stability, enterprise SaaS readiness,
or broad production availability claims.

---

## Source / Review Input

Claude audit input, 2026-05-24:

- R1: `FileBackedDurableMemoryStore.list()` needs safe JSON parsing and better
  receipt ids.
- R2: M1 durable memory store is not wired into `/api/execute`, so web UI
  non-coder journeys do not yet benefit from cross-session memory.
- P2: P1 guide assumes an operator has already configured provider keys; Step 0
  onboarding remains incomplete for a non-coder/small-team install.

---

## Scope

| Tranche | Title | Depends On | Status | Work Order |
| --- | --- | --- | --- | --- |
| R1 | Durable memory store resilience | M1 CLOSED_PASS | CLOSED_PASS | `docs/work_orders/CVF_WO_R1_DURABLE_MEMORY_STORE_RESILIENCE_2026-05-24.md` |
| R2 | `/api/execute` durable memory route wiring | Fresh GC-018 | DEMAND_GATED | `docs/work_orders/CVF_WO_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_2026-05-24.md` |
| P2 | Non-coder Step 0 API-key setup | Public/onboarding claim gate | DEMAND_GATED | `docs/work_orders/CVF_WO_P2_NONCODER_STEP0_API_KEY_SETUP_2026-05-24.md` |

---

## Work Plan

Execution order:

1. R1 is fast-lane because it is a localized resilience bug in the store
   delivered by M1.
2. R2 must not begin until a fresh GC-018 authorizes route-level behavior
   change to `/api/execute`.
3. P2 must not be claimed closed until a public-safe setup guide and any
   public-sync update are complete and verified for secret hygiene.

---

## Non-Goals

- Autonomous memory reinjection.
- `canReinject=true`.
- Graph approval authority.
- Universal provider stability.
- Enterprise SaaS or hosted GA readiness.
- Public runtime availability expansion.
- Raw-memory prompt release.

---

## Acceptance Criteria

- [x] R1: corrupt file-backed durable memory JSON does not throw.
- [x] R1: repeated durable-memory operations produce unique receipt ids.
- [ ] R2: `/api/execute` reads bounded durable memories through the existing
      policy gate, emits durable-memory receipt evidence, and never releases
      raw memory into provider prompts.
- [ ] R2: live governance proof proves one web-route cross-session memory
      benefit with `canReinject=false` preserved.
- [ ] P2: Step 0 provider-key setup guide exists in non-coder language.
- [ ] P2: public-safe guide/catalog paths are updated from public-sync if a
      public claim is changed.

---

## Verification / Evidence

R1 evidence:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/durable-memory-store.test.ts`
- `docs/reviews/CVF_R1_DURABLE_MEMORY_STORE_RESILIENCE_COMPLETION_2026-05-24.md`

R2 required future evidence:

- GC-018 baseline.
- Route unit tests for durable-memory read/receipt.
- Targeted `/api/execute` live proof using an approved provider key.
- Release gate if governance behavior is claimed.

P2 required future evidence:

- Step 0 setup guide.
- Secret hygiene scan.
- Public-sync Test-Path verification if public catalog/guide is updated.

---

## Claim Boundary

After R1 only, CVF may claim improved resilience of the M1 file-backed durable
store. It may not claim live web UI cross-session memory benefit, public
operator self-onboarding, or hosted production readiness until R2/P2 are closed
with their required evidence.
