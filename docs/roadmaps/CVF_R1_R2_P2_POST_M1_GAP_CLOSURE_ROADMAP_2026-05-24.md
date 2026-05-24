# CVF R1/R2/P2 Post-M1 Gap Closure Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

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

Decision: R2 and R3 are closed after fresh authority, implementation, live
proof, and public-safe onboarding verification. R3 supersedes the original P2
label to avoid mixing the gated roadmap row with the operator-authorized
execution tranche.

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
| R2 | `/api/execute` durable memory route wiring | Fresh GC-018 | CLOSED_PASS | `docs/work_orders/CVF_WO_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_2026-05-24.md` |
| P2 | Non-coder Step 0 API-key setup | Public/onboarding claim gate | SUPERSEDED_BY_R3 | `docs/work_orders/CVF_WO_P2_NONCODER_STEP0_API_KEY_SETUP_2026-05-24.md` |
| R3 | Non-coder Step 0 API-key setup | Fresh GC-018 and public-sync verification | CLOSED_PASS | `docs/work_orders/CVF_WO_R3_NONCODER_STEP0_API_KEY_SETUP_2026-05-24.md` |

---

## Work Plan

Execution order:

1. R1 closed first as a localized resilience bug in the store delivered by M1.
2. R2 closed after fresh GC-018 authorized route-level behavior change to
   `/api/execute`, with unit and live-provider proof.
3. R3 closed after fresh GC-018 authorized public-safe Step 0 setup docs,
   public-sync update, and secret-hygiene verification.

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
- [x] R2: `/api/execute` reads bounded durable memories through the existing
      policy gate, emits durable-memory receipt evidence, and never releases
      raw memory into provider prompts.
- [x] R2: live governance proof proves one web-route cross-session memory
      benefit with `canReinject=false` preserved.
- [x] R3: Step 0 provider-key setup guide exists in non-coder language.
- [x] R3: public-safe guide/catalog paths are updated from public-sync if a
      public claim is changed.

---

## Verification / Evidence

R1 evidence:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/durable-memory-store.test.ts`
- `docs/reviews/CVF_R1_DURABLE_MEMORY_STORE_RESILIENCE_COMPLETION_2026-05-24.md`

R2 evidence:

- GC-018 baseline:
  `docs/baselines/CVF_GC018_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_2026-05-24.md`
- Route unit tests:
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.durable-memory.test.ts`
- Targeted live route proof:
  `node scripts/run_cvf_r2_durable_memory_route_live_probe.mjs` -> PASS,
  receipt `rcpt-env-mpjdj5rc-p1g9go`, trace `env-mpjdj5rc-p1g9go`,
  provider `alibaba`, model `qwen-turbo`, memory id `r2-skill-safe`,
  `rawMemoryReleased=false`, `canReinject=false`.
- Mandatory release gate:
  `python scripts/run_cvf_release_gate_bundle.py --json` -> PASS, 7/7.
- Completion review:
  `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_COMPLETION_2026-05-24.md`

R3 evidence:

- GC-018 baseline:
  `docs/baselines/CVF_GC018_R3_NONCODER_STEP0_API_KEY_SETUP_2026-05-24.md`
- Private Step 0 guide:
  `docs/guides/CVF_NON_CODER_STEP0_API_KEY_SETUP_2026-05-24.md`
- Public-sync Step 0 guide and catalog update committed at public-sync commit
  `1160f1b9`.
- Public-sync remote verified as
  `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`.
- Secret-hygiene scan PASS for the updated public-safe docs.
- Completion review:
  `docs/reviews/CVF_R3_NONCODER_STEP0_API_KEY_SETUP_COMPLETION_2026-05-24.md`

---

## Claim Boundary

After R1/R2/R3, CVF may claim: the M1 file-backed durable store is resilient to
corrupt JSON; `/api/execute` can perform an explicit, policy-gated,
summary-only durable skill/long-term memory read with receipt evidence; and a
public-safe Step 0 provider-key setup guide exists for small-team/non-coder
operators.

Still not claimed: autonomous memory reinjection, `canReinject=true`, graph
approval authority, universal provider stability, automated provider account
procurement, hosted secret-vault operations, enterprise SaaS/GA readiness, or
broad production availability.
