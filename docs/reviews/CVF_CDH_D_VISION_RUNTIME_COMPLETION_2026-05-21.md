# CVF CDH-D Vision Runtime Return Review

Memory class: FULL_RECORD

Status: RETURNED_TO_ORCHESTRATOR_ROUTE_WIRING_REQUIRED

docType: review

Date: 2026-05-21

---

## Purpose

Record partial CDH-D progress and the blocker that prevents closure under the
active work order: the vision runtime adapter and negative gate are implemented
and verified, but the required governed `/api/execute` vision receipt proof
cannot be completed without route write ownership.

---

## Scope / Target / Owner Boundary

Target:

- `docs/work_orders/CVF_WO_CDH_D_VISION_RUNTIME_2026-05-21.md`

Changed implementation files:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-runtime-adapter.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/vision-runtime-adapter.test.ts`

Owner boundary:

- vision-runtime adapter sub-surface only;
- no `vision-contract.ts` changes;
- no `reasoning-contract.ts` changes;
- no `cvf-web` route changes;
- no closure claim.

---

## Target / Source Under Review

Authority chain:

- `docs/baselines/CVF_GC018_CDH_D_VISION_RUNTIME_2026-05-21.md`
- `docs/reviews/archive/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- `docs/reviews/archive/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md`

---

## Scope / Methodology

Codex executed the bounded parts that fit the active write ownership:

1. Filed GC-018 for the CDH-D vision-runtime sub-surface.
2. Confirmed `vision-contract.ts` is read-only for this tranche.
3. Added `vision-runtime-adapter.ts` for the Alibaba `qwen-vl-plus` lane.
4. Added image handling controls: URL or base64 only, no raw file path.
5. Added a negative gate for non-vision provider/model lanes.
6. Added focused Model Gateway tests.
7. Ran adapter-level live proof with a public image URL and operator-supplied
   DashScope/Alibaba key.
8. Stopped before route wiring because `cvf-web/src/app/api/execute/route.ts`
   is outside the work order write ownership.

---

## Evidence Trace Block

| Claim | Evidence | Result |
| --- | --- | --- |
| Vision runtime adapter implemented | `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-runtime-adapter.ts` | PASS |
| Image controls implemented | tests reject raw filesystem paths and ambiguous URL/base64 inputs | PASS |
| Negative gate implemented | test rejects `deepseek/deepseek-chat` for `VisionRequest` | PASS |
| Adapter-level live provider proof | Alibaba `qwen-vl-plus` with public image URL | PASS, `done=true`, description returned |
| `vision-contract.ts` unchanged | diff review | PASS, no changes |
| `reasoning-contract.ts` unchanged | diff review | PASS, no changes |
| Focused tests | `npm test -- --run tests/vision-runtime-adapter.test.ts` in Model Gateway | PASS, 6 tests |
| TypeScript check | `npm run check` in Model Gateway | PASS |
| Governed `/api/execute` vision receipt proof | active route has no image transport/`vision: true` receipt path inside permitted write set | BLOCKED |

---

## Findings / Position

Position: RETURNED_TO_ORCHESTRATOR_ROUTE_WIRING_REQUIRED.

Findings:

- The Model Gateway adapter can call Alibaba `qwen-vl-plus` with a public image
  URL and receive a valid `VisionContract`.
- The adapter blocks non-vision provider lanes before provider dispatch.
- Local image file paths are rejected; the adapter accepts only HTTP(S) URL or
  base64 image input.
- The active `cvf-web` execute route currently sends text prompts through
  `executeAI`; it does not transport image content or emit a `vision: true`
  receipt signal.
- The CDH-D work order does not permit modifying `route.ts`, so closure would
  require a new or amended work order.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Adapter proof is overstated as governed route proof | This review explicitly does not close CDH-D |
| Vision route wiring lands outside write ownership | Stop and return to Orchestrator |
| Image data leaks into logs | Adapter avoids logging image content and rejects raw file paths |
| Reasoning runtime sneaks in | No reasoning files or runtime adapter changed |

---

## Decision / Recommendation / Disposition

Disposition: not closed.

Recommended next move:

- Issue an amended CDH-D route-wiring work order that explicitly adds write
  ownership for the minimal `cvf-web` execute-route vision transport and
  receipt field needed to prove governed `/api/execute` with `vision: true`.

---

## Claim Boundary

This packet may be cited only as partial CDH-D adapter progress plus a
route-wiring blocker. It must not be cited as closed vision runtime, governed
`/api/execute` vision proof, Maika photo description, child-data/photo proof,
reasoning runtime, public vision capability, or all-provider vision behavior.
