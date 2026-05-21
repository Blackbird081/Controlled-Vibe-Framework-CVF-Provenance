# CVF GC-018 CDH-D Vision Runtime

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_WITH_ROUTE_PROOF_GATE

docType: baseline

Date: 2026-05-21

---

## Source / Predecessor Evidence

- `docs/reviews/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/roadmaps/CVF_CDH_D_VISION_RUNTIME_ROADMAP_2026-05-21.md`
- `docs/work_orders/CVF_WO_CDH_D_VISION_RUNTIME_2026-05-21.md`
- `docs/reviews/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md`

---

## Purpose / Decision / Baseline

Decision: ACCEPTED for the bounded vision-runtime adapter sub-surface, with
closure gated on a live governed `/api/execute` proof that carries a vision
receipt signal.

The operator authorized API-key use for testing on 2026-05-21. This baseline
does not authorize reasoning runtime, Maika photo description, child-data/photo
processing, or changes to the closed vision/reasoning contract shapes.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: CDH-D vision runtime.

Accepted implementation:

- add a provider-specific vision runtime adapter under `CVF_MODEL_GATEWAY`;
- enforce URL/base64-only image input controls;
- reject non-vision provider lanes at the contract boundary;
- run adapter-level live proof on an authorized vision-capable provider lane.

Closure gate:

- a later live governed `/api/execute` proof must show HTTP 200,
  `success=true`, `decision=ALLOW`, `evidenceMode=live`, provider/model, receipt
  id, trace id, and a `vision: true` or equivalent receipt signal.

---

## Scope / Proposed Tranche

In scope:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-runtime-adapter.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/vision-runtime-adapter.test.ts`
- completion/return review and continuity sync.

Out of scope:

- modifying `vision-contract.ts`;
- modifying `reasoning-contract.ts`;
- adding reasoning runtime;
- changing `cvf-web` route behavior unless a later work order explicitly adds
  route write ownership;
- Maika photo description;
- child data/photo processing;
- public-sync update.

---

## Evidence / Required Evidence / Verification

Required verification:

- focused Model Gateway vision-runtime tests;
- Model Gateway TypeScript check;
- adapter-level live provider proof if key is available;
- diff confirms `vision-contract.ts` and `reasoning-contract.ts` unchanged;
- closure must not be claimed until the governed `/api/execute` vision receipt
  gate is met.

---

## Claim Boundary

This GC-018 authorizes only the bounded vision-runtime adapter sub-surface and
associated tests. It does not authorize route wiring, reasoning runtime, Maika
photo/child-data claims, provider-general vision claims, public-sync updates, or
closure without a governed `/api/execute` vision receipt proof.
