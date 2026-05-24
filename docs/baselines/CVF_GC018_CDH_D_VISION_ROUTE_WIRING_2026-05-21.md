# CVF GC-018 CDH-D Vision Route Wiring

Memory class: FULL_RECORD

Status: GC018_ACCEPTED_FOR_MINIMAL_ROUTE_WIRING

docType: baseline

Date: 2026-05-21

---

## Source / Predecessor Evidence

- `docs/work_orders/CVF_WO_CDH_D_VISION_ROUTE_WIRING_2026-05-21.md`
- `docs/reviews/CVF_CDH_D_VISION_RUNTIME_COMPLETION_2026-05-21.md`
- `docs/baselines/CVF_GC018_CDH_D_VISION_RUNTIME_2026-05-21.md`
- `docs/reviews/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`

---

## Purpose / Decision / Baseline

Decision: ACCEPTED for the bounded route-wiring sub-step needed to close the
remaining CDH-D governed `/api/execute` vision receipt proof gap.

The operator confirmed API-key use for live testing on 2026-05-21. The
available key surface includes an Alibaba/DashScope-compatible key source; raw
key values must not be printed, copied into docs, or committed.

---

## Decision / Baseline / Proposed Tranche

Proposed tranche: CDH-D vision route wiring.

Accepted implementation:

- add optional image transport fields to the web execution request type;
- detect `imageUrl` or `imageBase64` in the existing execute route;
- dispatch image-bearing requests to the already-proven Alibaba
  `qwen-vl-plus` vision adapter;
- return the existing governed response shape with a `vision: true` receipt
  signal and live receipt metadata.

This tranche accepts the work order with one implementation correction: the
`cvf-web` package does not currently expose `cvf-model-gateway` as a package
dependency, so the route may import the committed adapter source by bounded
relative path inside `route.ts` rather than adding a package/dependency file
outside write ownership.

---

## Scope / Proposed Tranche

In scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- this GC-018 baseline;
- completion review and active session continuity updates.

Out of scope:

- modifying `vision-runtime-adapter.ts`;
- modifying `vision-contract.ts`;
- modifying `reasoning-contract.ts`;
- reasoning runtime;
- Maika photo description or child-data/photo processing;
- UI changes, new routes, new CLI commands, SSE streaming, dependency/package
  updates, or public-sync updates.

---

## Evidence / Required Evidence / Verification

Required verification:

- pre-flight structural gate passes;
- `route.ts` line count remains below the GC-023 hard limit;
- `cvf-web` tests and TypeScript check pass;
- live governed `/api/execute` call returns HTTP 200, `success=true`,
  `decision=ALLOW`, `evidenceMode=live`, provider `alibaba`, model
  `qwen-vl-plus`, receipt id, trace id, and `vision: true`;
- diff confirms `vision-runtime-adapter.ts`, `vision-contract.ts`, and
  `reasoning-contract.ts` are unchanged;
- no image URL or base64 payload is recorded in receipt fields or audit event
  payloads.

---

## Claim Boundary

This GC-018 authorizes only minimal execute-route wiring for the previously
proven Alibaba vision adapter. It does not prove reasoning runtime, Maika photo
description, child-data/photo vision processing, provider-general vision
parity, public product capability, or any behavior outside the live evidence
trace captured by this tranche.
