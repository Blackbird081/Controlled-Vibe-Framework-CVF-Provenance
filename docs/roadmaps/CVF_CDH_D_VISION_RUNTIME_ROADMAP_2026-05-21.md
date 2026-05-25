# CVF CDH-D Vision Runtime Roadmap

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: roadmap

Date: 2026-05-21

---

## Purpose

Implement a vision runtime adapter connecting the closed `VisionContract` to
an authorized live provider lane, prove a live governed `/api/execute` call
with a vision-type payload, and enforce a negative gate rejecting vision
requests on non-vision provider lanes.

---

## Authorization

Authorized by:

- CDH-D delta rebuttal:
  `docs/reviews/archive/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- CDH delta meta-roadmap:
  `docs/roadmaps/archive/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`
- D2 vision contract closure:
  `docs/reviews/archive/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- W1 reasoning contract closure:
  `docs/reviews/archive/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md`

This roadmap requires a fresh CDH-D GC-018 before implementation begins.
Sub-surface selection: **vision runtime only**.
Reasoning runtime is out of scope for this roadmap.

---

## Why

The CDH-D rebuttal split provider-method work into three sub-surfaces:
vision contract (closed by D2), reasoning contract (closed by W1), and
vision runtime (not proved). The vision contract defines the shape of a
`VisionRequest` and `VisionCapableProvider` — but no CVF execution path
has demonstrated receiving an image input, routing it through a live
provider, and returning a governed receipt with vision output.

This gap matters because Maika's text-summary use case is proven, but a
vision-capable interaction (e.g., a governed image description task) has
no evidence chain. Closing vision runtime creates the foundation for any
future image-aware governance use case, including but not limited to Maika
photo description (which remains separately demand-gated).

---

## Scope

In scope:

- Implement a vision runtime adapter layer connecting the closed
  `VisionContract` to an authorized live provider (Alibaba `qwen-vl-plus`
  or equivalent vision-capable model lane).
- Image handling controls: image must arrive as a URL reference or base64
  blob; raw file system paths are not permitted; image content is not
  logged in plain text.
- A governed `/api/execute` call with a vision-type payload, returning
  HTTP 200, decision ALLOW, and a governance receipt.
- Receipt includes: provider lane, model, receipt id, trace id, evidence
  mode `live`, vision flag `true`.
- At least one negative gate test: a non-vision provider lane must reject
  a `VisionRequest` at the contract boundary.
- GC-018 baseline for this tranche.
- Completion review.

Out of scope:

- Reasoning runtime.
- Maika photo description (separately demand-gated).
- Bundled vision + reasoning runtime.
- Child data or child photo processing.
- New provider contract beyond what `vision-contract.ts` already defines.
- SSE streaming for vision output.
- Public-sync update (private proof only until separately authorized).

---

## Non-Goals

- Claiming CVF has universal image understanding.
- Proving vision runtime for every provider.
- Enabling image storage or persistent image references.
- Adding a new vision memory tier.

---

## Work Plan

| Step | Artifact | Owner |
| --- | --- | --- |
| D-01 | File GC-018 baseline; name vision runtime as the only sub-surface | Codex/Orchestrator |
| D-02 | Implement vision runtime adapter: wire `VisionContract` to authorized provider lane | Codex/Implementer |
| D-03 | Add image handling controls: URL/base64 only, no raw path, no plain-text log | Codex/Implementer |
| D-04 | Run live governed `/api/execute` call with vision payload; capture redacted output | Codex/Implementer |
| D-05 | Add negative gate test: non-vision provider rejects `VisionRequest` at contract boundary | Codex/Implementer |
| D-06 | File completion review with evidence trace block | Codex/Auditor |
| D-07 | Update active queue/state/handoff | Codex/Auditor |

---

## Acceptance Criteria

- [ ] GC-018 baseline filed, vision runtime named as sole sub-surface.
- [ ] Vision runtime adapter implemented connecting `VisionContract` to
      authorized provider.
- [ ] Image handling controls implemented and tested.
- [ ] Live governed `/api/execute` call: HTTP 200, decision ALLOW, receipt
      id present, `vision: true` in receipt, non-mock output, live evidence mode.
- [ ] Negative gate test PASS: non-vision provider rejects `VisionRequest`.
- [ ] Reasoning runtime not implemented or claimed.
- [ ] Maika photo description not claimed.
- [ ] Completion review filed with full evidence trace block.

---

## Verification / Evidence

All claims must be backed by:

- Redacted command/HTTP output (no raw API keys, no image content in plain text).
- Receipt id, trace id, provider lane, model in evidence trace block.
- `vision: true` flag in governance receipt.
- Negative gate test: file, test name, result.
- Image handling: confirmation that no raw file path or plain-text image
  content appears in logs or receipts.

---

## Claim Boundary

This roadmap closes only the vision runtime sub-surface of CDH-D. It does
not prove reasoning runtime, Maika photo description, child-data vision
proof, universal image understanding, or bundled provider-method parity.
Vision contract (D2) and reasoning contract (W1) remain the prior closed
evidence; this tranche adds only the live runtime proof layer for vision.
