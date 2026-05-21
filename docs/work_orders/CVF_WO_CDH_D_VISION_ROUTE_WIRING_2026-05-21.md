# Work Order — CDH-D Vision Route Wiring

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-21

---

## Purpose

Wire the existing `vision-runtime-adapter.ts` into the `cvf-web` execute route
so that a request carrying `imageUrl` or `imageBase64` is dispatched to the
Alibaba `qwen-vl-plus` lane and the returned receipt carries `vision: true`.
This closes the remaining blocker from the CDH-D adapter return review.

---

## Authority Chain

- CDH-D adapter return review:
  `docs/reviews/CVF_CDH_D_VISION_RUNTIME_COMPLETION_2026-05-21.md`
- CDH-D original work order (partially closed):
  `docs/work_orders/CVF_WO_CDH_D_VISION_RUNTIME_2026-05-21.md`
- CDH-D adapter GC-018:
  `docs/baselines/CVF_GC018_CDH_D_VISION_RUNTIME_2026-05-21.md`
- CDH-D delta rebuttal:
  `docs/reviews/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- D2 vision contract closure:
  `docs/reviews/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- GC-018 to be filed:
  `docs/baselines/CVF_GC018_CDH_D_VISION_ROUTE_WIRING_2026-05-21.md`

---

## Agent Roles

- Orchestrator: Codex files GC-018 and confirms write ownership before
  touching route.ts.
- Reviewer: Codex confirms adapter return review boundary and that no
  reasoning runtime or new provider contract is introduced.
- Implementer: Codex adds minimal route-level vision dispatch and receipt
  field; runs live governed call.
- Auditor: Codex verifies evidence trace block and closes the packet.

---

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  — minimal additions only: read `imageUrl`/`imageBase64`/`mimeType` from
  request body; dispatch to `createAlibabaVisionRuntimeAdapter` when image
  field is present; add `vision: true` to the governance receipt response.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
  — add optional `imageUrl`, `imageBase64`, `mimeType` fields to
  `ExecutionRequest` if not already present.
- Live governed `/api/execute` call with vision-type payload; capture redacted
  output including receipt id, trace id, provider, model, decision, and
  `vision: true` flag.
- `docs/baselines/CVF_GC018_CDH_D_VISION_ROUTE_WIRING_2026-05-21.md`
- `docs/reviews/CVF_CDH_D_VISION_ROUTE_WIRING_COMPLETION_2026-05-21.md`
- Active queue/state/handoff updates.

Out of scope:

- Reasoning runtime.
- Maika photo description (separately demand-gated).
- Child data or child photo processing.
- Modifying `vision-contract.ts` (closed by D2).
- Modifying `reasoning-contract.ts`.
- Modifying `vision-runtime-adapter.ts` (already closed).
- SSE streaming for vision output.
- New provider contract shapes.
- New route, new endpoint, or new CLI command.
- UI changes or frontend components.
- Public-sync update.

---

## Required First Reads

- `docs/reviews/CVF_CDH_D_VISION_RUNTIME_COMPLETION_2026-05-21.md`
- `docs/baselines/CVF_GC018_CDH_D_VISION_RUNTIME_2026-05-21.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-runtime-adapter.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`

---

## Pre-Flight Checks

- Confirm `vision-runtime-adapter.ts` is already committed and its exports
  are available (do not re-implement).
- Confirm `vision-contract.ts` will not be modified.
- Confirm `route.ts` current line count; if adding lines would breach GC-023
  hard limit, split by extracting a `vision-route-helper.ts` instead.
- Confirm `ExecutionRequest` in `types.ts` does not already have conflicting
  `imageUrl`/`imageBase64` fields.
- Confirm authorized vision-capable provider key (Alibaba `qwen-vl-plus`)
  is present without printing raw value.
- Run `python governance/compat/check_markdown_structural_completeness.py
  --base HEAD --head HEAD --enforce` — must be COMPLIANT before staging.

---

## Write Ownership

Permitted writes:

| File | Change |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | Minimal vision dispatch: read image fields, call vision adapter, add `vision: true` to receipt response |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | Add optional `imageUrl`, `imageBase64`, `mimeType` to `ExecutionRequest` if absent |
| `docs/baselines/CVF_GC018_CDH_D_VISION_ROUTE_WIRING_2026-05-21.md` | New GC-018 baseline |
| `docs/reviews/CVF_CDH_D_VISION_ROUTE_WIRING_COMPLETION_2026-05-21.md` | Completion review |
| `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` | Update cdh-d-delta and cdh-d-vision-runtime status |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Update nextAllowedMove |
| `AGENT_HANDOFF_V10_2026-05-19.md` | GC-020 sync |

No other files may be modified. `vision-runtime-adapter.ts`,
`vision-contract.ts`, and `reasoning-contract.ts` are read-only for this
work order.

---

## Execution Plan

1. File `CVF_GC018_CDH_D_VISION_ROUTE_WIRING_2026-05-21.md` (R-01).
2. Add optional `imageUrl`, `imageBase64`, `mimeType` to `ExecutionRequest`
   in `types.ts` if not already present (R-02).
3. In `route.ts`, after request body parsing: if `imageUrl` or `imageBase64`
   is present, validate and dispatch to `createAlibabaVisionRuntimeAdapter`;
   obtain `VisionContract`; build the governance receipt with `vision: true`
   and `provider: "alibaba"`, `model: "qwen-vl-plus"` (R-03).
4. Image content must not appear in logs, audit events, or receipt fields;
   only the `vision: true` flag and contract metadata are recorded (R-04).
5. Run live governed `/api/execute` call with a vision-type payload (public
   image URL); capture redacted output including receipt id, trace id,
   provider, model, decision, and `vision: true` (R-05).
6. Run `npm run test:run` and `npm run check` in `cvf-web` (R-06).
7. File `CVF_CDH_D_VISION_ROUTE_WIRING_COMPLETION_2026-05-21.md` with
   evidence trace block (R-07).
8. Update active queue/state/handoff (R-08).
9. Run governance checks (R-09):
   `python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce`
   `python governance/compat/check_governed_file_size.py --enforce`

---

## Evidence Requirements

| Claim | Required evidence |
| --- | --- |
| Live vision invocation via route | HTTP 200, `success=true`, decision ALLOW, receipt id, trace id, `vision: true` in response, non-mock, `evidenceMode: live` |
| Authorized provider lane | Provider `alibaba`, model `qwen-vl-plus` in evidence trace block |
| Image content not logged | Confirmation that no image URL payload or base64 content appears in audit events or receipt fields |
| `vision-runtime-adapter.ts` unchanged | Diff shows 0 lines changed in that file |
| `vision-contract.ts` unchanged | Diff shows 0 lines changed in that file |
| Reasoning runtime not added | No reasoning runtime adapter or reasoning live proof in diff |
| `route.ts` line count | Pre-flight and post-edit line counts both within GC-023 limit or split documented |
| `cvf-web` tests PASS | `npm run test:run` output |

---

## Acceptance Criteria

- [ ] GC-018 filed for route wiring tranche.
- [ ] `ExecutionRequest` has optional `imageUrl`/`imageBase64`/`mimeType`.
- [ ] Route dispatches vision request to adapter when image field present.
- [ ] Live `/api/execute` call: HTTP 200, ALLOW, receipt id, `vision: true`,
      non-mock, live evidence mode.
- [ ] Image content not in logs or receipts.
- [ ] `vision-runtime-adapter.ts` unchanged.
- [ ] `vision-contract.ts` unchanged.
- [ ] Reasoning runtime not added or claimed.
- [ ] Maika photo description not claimed.
- [ ] GC-023 line counts within limits.
- [ ] `cvf-web` tests and typecheck PASS.
- [ ] Governance checks exit 0.
- [ ] Completion review filed.
- [ ] Active queue `cdh-d-delta` status updated to CLOSED.

---

## Review Gate

Close only after R-09 governance checks exit 0, `cvf-web` test suite PASS,
and the evidence trace block has real receipt id, trace id, provider, model,
decision, and `vision: true` — no placeholder values.

---

## Closure Checklist

- [ ] GC-018 filed.
- [ ] `ExecutionRequest` type updated.
- [ ] Route vision dispatch implemented.
- [ ] Image content log-isolation confirmed.
- [ ] Live invocation run and output captured.
- [ ] `cvf-web` tests and typecheck PASS.
- [ ] Completion review filed.
- [ ] Queue/state/handoff updated.
- [ ] Governance checks PASS.

---

## Return-To-Orchestrator Conditions

Return to Orchestrator (do not close) if:

- Authorized vision-capable provider key is not available.
- Live invocation returns non-200 or mock fallback.
- Adding route wiring requires modifying `vision-contract.ts` or
  `vision-runtime-adapter.ts`.
- `route.ts` line count would breach GC-023 hard limit and no split
  strategy is clear.
- Any governance check exits non-zero.

---

## Operator Checkpoint

Checkpoint required: operator must confirm that a vision-capable provider
key (Alibaba `qwen-vl-plus` or equivalent) is available and accessible
before Codex proceeds to step R-05 (live invocation). If no vision-capable
key is available, Codex must stop at R-04 and return to Orchestrator.

---

## Claim Boundary

This work order closes only the route-wiring sub-step of CDH-D. It does not
prove reasoning runtime, Maika photo description, child-data vision proof,
universal image understanding, bundled provider-method parity, or any public
product capability beyond what the evidence trace block records. The adapter
layer was already proven in the CDH-D adapter return review; this tranche
adds only the governed execute-route proof layer.
