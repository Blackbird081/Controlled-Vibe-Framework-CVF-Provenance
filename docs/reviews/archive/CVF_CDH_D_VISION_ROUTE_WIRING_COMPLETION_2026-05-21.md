# CVF CDH-D Vision Route Wiring Completion

Memory class: FULL_RECORD

Status: CLOSED_VISION_ROUTE_WIRING_PROOF

docType: review

Date: 2026-05-21

---

## Purpose

Close the CDH-D route-wiring sub-step by proving that the governed
`/api/execute` route can carry an image-bearing request through the Alibaba
`qwen-vl-plus` vision lane and return a live governance receipt with
`vision: true`.

---

## Scope / Target / Owner Boundary

Target:

- `docs/work_orders/CVF_WO_CDH_D_VISION_ROUTE_WIRING_2026-05-21.md`

Changed implementation files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`

Owner boundary:

- minimal execute-route image transport only;
- no `vision-runtime-adapter.ts` changes;
- no `vision-contract.ts` changes;
- no `reasoning-contract.ts` changes;
- no UI, CLI, SSE streaming, package/dependency, or public-sync change.

---

## Target / Source Under Review

Authority chain:

- `docs/baselines/CVF_GC018_CDH_D_VISION_ROUTE_WIRING_2026-05-21.md`
- `docs/reviews/CVF_CDH_D_VISION_RUNTIME_COMPLETION_2026-05-21.md`
- `docs/baselines/CVF_GC018_CDH_D_VISION_RUNTIME_2026-05-21.md`
- `docs/reviews/archive/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`

---

## Scope / Methodology

Codex executed the bounded route-wiring tranche:

1. Filed GC-018 for the route-wiring sub-surface.
2. Added optional `imageUrl`, `imageBase64`, and `mimeType` fields to the web
   `ExecutionRequest` type.
3. Added optional `vision` to `GovernanceEvidenceReceipt`.
4. Updated the execute route to detect image-bearing requests, force the
   Alibaba `qwen-vl-plus` lane, call the committed vision adapter, and attach
   `vision: true` to the returned governance receipt.
5. Preserved the existing non-vision text path.
6. Ran live governed `/api/execute` proof using an operator-authorized
   Alibaba/DashScope key and a public image URL.
7. Verified route tests, TypeScript, full `cvf-web` tests, and governance
   compatibility gates.

---

## Evidence Trace Block

| Claim | Evidence | Result |
| --- | --- | --- |
| GC-018 filed | `docs/baselines/CVF_GC018_CDH_D_VISION_ROUTE_WIRING_2026-05-21.md` | PASS |
| Request type carries image fields | `ExecutionRequest` has optional `imageUrl`, `imageBase64`, `mimeType` | PASS |
| Route dispatches image requests to vision lane | `route.ts` detects image payload, selects Alibaba `qwen-vl-plus`, and calls `createAlibabaVisionRuntimeAdapter` | PASS |
| Live governed route proof | HTTP `200`, `success=true`, `decision=ALLOW`, `evidenceMode=live` | PASS |
| Receipt and trace | receipt `rcpt-env-mpfdb3kj-4d7o8r`, trace `env-mpfdb3kj-4d7o8r` | PASS |
| Provider lane | provider `alibaba`, model `qwen-vl-plus` | PASS |
| Vision receipt signal | `governanceEvidenceReceipt.vision=true` | PASS |
| Image content not echoed | receipt metadata and response metadata did not contain the public image URL or `imageBase64` field | PASS |
| Adapter unchanged | diff for `vision-runtime-adapter.ts` is empty | PASS |
| Vision contract unchanged | diff for `vision-contract.ts` is empty | PASS |
| Reasoning runtime unchanged | diff for `reasoning-contract.ts` is empty | PASS |
| Route line count | post-edit `route.ts` line count is `1001`, within the approved GC-023 exception maximum | PASS |
| Targeted route tests | `npm run test:run -- src/app/api/execute/route.test.ts` | PASS, 31 tests |
| `cvf-web` typecheck | `npm run check` | PASS |
| Full `cvf-web` tests | `npm run test:run` after stopping live-proof dev server | PASS, 217 files, 2739 tests, 2 skipped |

Note: while the live-proof server was still listening on port `3000`, the
legacy W86 PVV benchmark auto-enabled its CFG-B localhost path and surfaced
pre-existing high-risk benchmark `400` responses. After the route proof
completed and the dev server was stopped, the required `npm run test:run`
passed.

---

## Findings / Position

Position: CLOSED_VISION_ROUTE_WIRING_PROOF.

Findings:

- The governed execute route now proves image-bearing requests can reach the
  existing Alibaba vision adapter.
- The response uses the existing governance receipt shape and adds only the
  bounded `vision: true` signal.
- Image payload material is not copied into receipt metadata or audit-memory
  response metadata.
- Non-vision route behavior remains on the existing `executeAI` path.
- Route wiring required two GC-018 corrections: because `cvf-web` does not
  expose `cvf-model-gateway` as a package dependency, the route imports the
  committed adapter source by bounded relative path; because `route.ts` is at
  its approved line-count maximum, vision-specific logic was extracted to
  `vision-route-helper.ts` under the work order's pre-flight split condition.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Vision route proof overstated as Maika photo or child-data proof | Claim boundary excludes Maika and child-data/photo use |
| Image payload leaks into receipt/audit metadata | Response metadata check confirmed no image URL or base64 field in receipt/audit-memory metadata |
| Adapter or closed contracts drift | Diffs for `vision-runtime-adapter.ts`, `vision-contract.ts`, and `reasoning-contract.ts` are empty |
| PVV benchmark noise confused with route failure | Final full test run was executed after stopping the live-proof dev server |

---

## Decision / Recommendation / Disposition

Disposition: closed.

CDH-D may now be cited as closed only for the governed execute-route vision
proof recorded here: Alibaba `qwen-vl-plus`, one public-image route invocation,
live receipt, and `vision: true`.

---

## Claim Boundary

This packet closes only the CDH-D route-wiring sub-step. It does not prove
reasoning runtime, Maika photo description, child-data/photo vision handling,
universal image understanding, provider-general vision parity, bundled CDH
closure beyond the named CDH-D proof, public product readiness, or any public
capability claim.

