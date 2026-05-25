# Work Order — CDH-D Vision Runtime

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-21

---

## Purpose

Implement a vision runtime adapter connecting the closed `VisionContract`
to an authorized live provider lane, prove a live governed `/api/execute`
call with a vision-type payload, and enforce a negative gate that rejects
vision requests on non-vision provider lanes.

---

## Authority Chain

- CDH-D delta rebuttal:
  `docs/reviews/archive/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- CDH-D roadmap:
  `docs/roadmaps/CVF_CDH_D_VISION_RUNTIME_ROADMAP_2026-05-21.md`
- D2 vision contract closure:
  `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- W1 reasoning contract closure:
  `docs/reviews/archive/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md`
- GC-018 to be filed:
  `docs/baselines/CVF_GC018_CDH_D_VISION_RUNTIME_2026-05-21.md`

---

## Agent Roles

- Orchestrator: Codex files GC-018, names vision runtime as the sole
  sub-surface, confirms provider lane before proceeding.
- Reviewer: Codex reviews the D rebuttal sub-surface split boundary before
  implementation.
- Implementer: Codex implements adapter, image controls, and live proof.
- Auditor: Codex verifies evidence trace block and closes the packet.

---

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts` (read only; do
  not modify the closed contract shape).
- New vision runtime adapter file under `EXTENSIONS/CVF_MODEL_GATEWAY/src/`
  or the appropriate provider lane.
- Image handling controls: URL or base64 input only; no raw file system
  path; no plain-text image content in logs or receipts.
- Live governed `/api/execute` call with vision-type payload.
- Negative gate test: non-vision provider rejects `VisionRequest` at
  contract boundary.
- `docs/baselines/CVF_GC018_CDH_D_VISION_RUNTIME_2026-05-21.md`
- `docs/reviews/CVF_CDH_D_VISION_RUNTIME_COMPLETION_2026-05-21.md`
- Active queue/state/handoff updates.

Out of scope:

- Reasoning runtime.
- Maika photo description (separately demand-gated).
- Child data or child photo processing.
- Modifying `vision-contract.ts` (already closed by D2).
- Modifying `reasoning-contract.ts`.
- SSE streaming for vision output.
- New provider contract shapes.
- Public-sync update.

---

## Required First Reads

- `docs/reviews/archive/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` (current exports)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Pre-Flight Checks

- Confirm `vision-contract.ts` is closed and its shape will not be
  modified by this work order.
- Confirm `reasoning-contract.ts` will not be modified.
- Confirm authorized vision-capable provider lane and model (e.g.,
  Alibaba `qwen-vl-plus`) key is present without printing raw value.
- Confirm no vision runtime adapter file already exists that would
  conflict with this work order.
- Check GC-023 line count for any existing files to be modified.
- Run `python governance/compat/check_markdown_structural_completeness.py
  --base HEAD --head HEAD --enforce` — must be COMPLIANT before staging.

---

## Write Ownership

Permitted writes:

| File | Change |
| --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-runtime-adapter.ts` (new) | Vision runtime adapter |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | Export vision runtime adapter |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/vision-runtime-adapter.test.ts` (new) | Negative gate test + adapter unit tests |
| `docs/baselines/CVF_GC018_CDH_D_VISION_RUNTIME_2026-05-21.md` | New GC-018 baseline |
| `docs/reviews/CVF_CDH_D_VISION_RUNTIME_COMPLETION_2026-05-21.md` | Completion review |
| `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` | Update cdh-d-delta status |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Update nextAllowedMove |
| `AGENT_HANDOFF_V10_2026-05-19.md` | GC-020 sync |

No other files may be modified. `vision-contract.ts` and
`reasoning-contract.ts` are read-only for this work order.

---

## Execution Plan

1. File `CVF_GC018_CDH_D_VISION_RUNTIME_2026-05-21.md`; name vision
   runtime as the sole sub-surface (D-01).
2. Implement vision runtime adapter connecting `VisionContract` to
   authorized provider lane (D-02).
3. Implement image handling controls: URL/base64 only, no raw file path,
   no plain-text image content in logs (D-03).
4. Run live governed `/api/execute` call with vision-type payload; capture
   redacted output including receipt id, trace id, provider, model,
   decision, and `vision: true` flag (D-04).
5. Add negative gate test: non-vision provider must reject `VisionRequest`
   at contract boundary with a clear error (D-05).
6. Run test suite for `CVF_MODEL_GATEWAY` extension (D-06).
7. File `CVF_CDH_D_VISION_RUNTIME_COMPLETION_2026-05-21.md` with evidence
   trace block (D-07).
8. Update active queue/state/handoff (D-08).
9. Run governance checks (D-09):
   `python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce`
   `python governance/compat/check_governed_file_size.py --enforce`
   `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY/`

---

## Evidence Requirements

| Claim | Required evidence |
| --- | --- |
| Live vision invocation | HTTP 200, `success=true`, decision ALLOW, receipt id, trace id, `vision: true` in receipt, non-mock, `evidenceMode: live` |
| Authorized provider lane | Provider name and model in evidence trace block |
| Image handling controls | Confirmation no raw path or plain-text image content in logs/receipts |
| Negative gate PASS | Test file, test name, PASS, error message from non-vision provider |
| `vision-contract.ts` unchanged | Diff shows 0 lines changed in that file |
| Reasoning runtime not added | No reasoning runtime adapter or reasoning live proof in diff |
| GC-023 compliance | Pre-flight and post-edit line counts within limits |

---

## Acceptance Criteria

- [ ] GC-018 baseline filed, vision runtime named as sole sub-surface.
- [ ] Vision runtime adapter implemented.
- [ ] Image handling controls implemented and verified.
- [ ] Live `/api/execute` call: HTTP 200, ALLOW, receipt id, `vision: true`,
      non-mock, live evidence mode.
- [ ] Negative gate test PASS.
- [ ] `vision-contract.ts` unchanged.
- [ ] Reasoning runtime not added or claimed.
- [ ] Maika photo description not claimed.
- [ ] GC-023 line counts within limits.
- [ ] Governance checks exit 0.
- [ ] Completion review filed.
- [ ] Active queue `cdh-d-delta` status updated.

---

## Review Gate

Close only after D-09 governance checks exit 0, the negative gate test
PASS, and the evidence trace block has real receipt id, trace id, provider,
model, and `vision: true` — no placeholder values.

---

## Closure Checklist

- [ ] GC-018 filed.
- [ ] Vision runtime adapter implemented.
- [ ] Image handling controls implemented.
- [ ] Live invocation run and output captured.
- [ ] Negative gate test PASS.
- [ ] Model Gateway `npm run check` PASS.
- [ ] Completion review filed.
- [ ] Queue/state/handoff updated.
- [ ] Governance checks PASS.

---

## Return-To-Orchestrator Conditions

Return to Orchestrator (do not close) if:

- Authorized vision-capable provider key is not available.
- Live invocation returns non-200 or mock fallback.
- Live output contains a raw API key that cannot be redacted.
- Implementing the adapter requires modifying `vision-contract.ts`.
- Implementing the adapter requires adding reasoning runtime.
- Any governance check exits non-zero.

---

## Operator Checkpoint

Checkpoint required: operator must confirm that a vision-capable provider
key (e.g., Alibaba `qwen-vl-plus` or equivalent) is available and
accessible before Codex proceeds to step D-04 (live invocation). If no
vision-capable key is available, Codex must stop at D-03 and return to
Orchestrator — the live proof step cannot be substituted with a mock call.

---

## Claim Boundary

This work order closes only the vision runtime sub-surface of CDH-D. It
does not prove reasoning runtime, Maika photo description, child-data vision
proof, universal image understanding, bundled provider-method parity, or any
public product capability beyond what the evidence trace block records.
