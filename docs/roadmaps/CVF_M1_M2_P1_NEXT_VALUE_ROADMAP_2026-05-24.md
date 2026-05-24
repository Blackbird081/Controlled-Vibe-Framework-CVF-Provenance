# CVF M1/M2/P1 Next-Value Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE

docType: roadmap

Date: 2026-05-24

---

## Scope / Target / Owner Boundary

Scope: three implementation tranches targeting governed memory and production
readiness surfaces.

Target: private provenance documentation, LPF memory surfaces, and web UI
onboarding path.

Owner: Codex (implementation); Claude (dispatch and quality assessment).

---

## Authorization / Decision

Operator authorized on 2026-05-24:

- M2 (D-06 memory tier unfreeze): AUTHORIZED — surface is memory tier model
  (`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`).
- M1 (durable/cross-session memory): AUTHORIZED, conditional on M2 CLOSED_PASS.
- P1 (production readiness, small team/non-coder): AUTHORIZED, runs in parallel
  with M2/M1.

Authority chain baselines:

- M2: `docs/baselines/CVF_GC018_M2_D06_MEMORY_TIER_FREEZE_RELEASE_2026-05-24.md`
- M1: `docs/baselines/CVF_GC018_M1_DURABLE_CROSS_SESSION_MEMORY_2026-05-24.md`
- P1: `docs/baselines/CVF_GC018_P1_PRODUCTION_READINESS_SMALL_TEAM_2026-05-24.md`

---

## Purpose

After C2-C5 closure the next highest-value surface is durable memory for the
small-team/non-coder audience. D-06 (M2) unblocks M1 by releasing the memory
tier contract from the kernel freeze. P1 runs in parallel to prove the
production path for CVF's declared addressable audience.

---

## Scope

| Tranche | Title | Depends On | Status | Work Order |
| --- | --- | --- | --- | --- |
| M2 | D-06 memory tier model freeze release | — | WORK_ORDER_READY | `docs/work_orders/CVF_WO_M2_D06_MEMORY_TIER_FREEZE_RELEASE_2026-05-24.md` |
| M1 | Durable/cross-session memory | M2 CLOSED_PASS | DEMAND_GATED | `docs/work_orders/CVF_WO_M1_DURABLE_CROSS_SESSION_MEMORY_2026-05-24.md` |
| P1 | Production readiness for small team/non-coder | — | WORK_ORDER_READY | `docs/work_orders/CVF_WO_P1_PRODUCTION_READINESS_SMALL_TEAM_2026-05-24.md` |

---

## Non-Goals

The following are explicitly out of scope for this roadmap:

- D-07 global freeze lift — permanently rejected under binding rule.
- Autonomous memory reinjection.
- Graph approval authority.
- Universal provider stability.
- Full hosted SaaS/GA or enterprise production readiness.
- Maika proof.
- Broad kernel unfreeze beyond the single M2 surface.
- Public-sync update (deferred to after P1 CLOSED_PASS per public catalog rule).

---

## Work Plan

Execution order:

1. M2 and P1 begin immediately in parallel.
2. M1 begins only after M2 is `CLOSED_PASS`. Codex must self-check M2 status.

M2 deliverables:

- Formal freeze-release packet for `memory-tier-classifier.contract.ts`.
- Owner map entry updated with `freeze_released: true`.
- TypeScript check PASS.
- Completion review filed.

M1 deliverables (after M2 CLOSED_PASS):

- Durable store interface for skill-tier and long-term-tier.
- Cross-session read/write path with receipt evidence.
- `canReinject=false` invariant preserved.
- Summary-only reinjection proven through AIF C2 gate.
- Release gate PASS.
- Completion review filed.

P1 deliverables:

- Onboarding journey assessment and top-3 friction point closure.
- Minimum setup doc for non-coder persona.
- End-to-end proof: non-coder persona → template → governed `/api/execute` →
  live receipt.
- Public catalog row updated with bounded claim and verified evidence path.
- Completion review filed.

---

## Acceptance Criteria

- [ ] M2: freeze-release packet filed, owner map updated, TypeScript PASS,
      completion review filed.
- [ ] M1: durable store for skill/long-term tiers, cross-session receipts,
      `canReinject=false` test PASS, release gate PASS, completion review filed.
- [ ] P1: non-coder onboarding doc, friction points closed, live proof receipt,
      public catalog updated, completion review filed.
- [ ] M1 must not start before M2 CLOSED_PASS is confirmed.
- [ ] No raw secret in any committed artifact across all tranches.

---

## Verification / Evidence

Required evidence per tranche:

M2:

- `docs/reviews/CVF_M2_D06_MEMORY_TIER_FREEZE_RELEASE_COMPLETION_2026-05-24.md`
- Owner map diff showing `freeze_released: true`.

M1:

- `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- Cross-session write receipt and read receipt.
- `canReinject=false` binding test result.
- Release gate PASS evidence.

P1:

- `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`
- Live proof receipt: HTTP 200, `success=true`, `evidenceMode=live`,
  `rawSecretPrinted=false`.
- Public catalog updated row with Test-Path PASS from public-sync clone.

---

## Claim Boundary

Allowed after all three tranches CLOSED_PASS:

- Durable memory for skill-tier and long-term-tier under policy gate.
- Cross-session memory read/write with receipt evidence.
- One kernel surface unfrozen (memory tier model only).
- Production readiness for non-coder/small team persona with proven path.

Still not allowed after this roadmap closes:

- Global freeze lift (D-07) — PERMANENTLY REJECTED.
- Autonomous memory reinjection.
- Graph approval authority.
- Universal provider stability.
- Full hosted SaaS/GA production readiness.
- Maika proof.
- Broad kernel unfreeze.

---

## Progress Tracker

| Tranche | Status | Completion Review |
| --- | --- | --- |
| M2 | WORK_ORDER_READY | — |
| M1 | DEMAND_GATED | — |
| P1 | WORK_ORDER_READY | — |
