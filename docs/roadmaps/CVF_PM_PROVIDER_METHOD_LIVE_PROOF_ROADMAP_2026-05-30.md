# CVF PM Provider Method Live Proof Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE

docType: roadmap

Date: 2026-05-30

---

## Authorization / Decision

Authorized by operator direction 2026-05-30. Extends CVF's certified provider
method evidence beyond the current `chat` baseline.

Fresh GC-018:
`docs/baselines/CVF_GC018_PM_PROVIDER_METHOD_LIVE_PROOF_2026-05-30.md`

Dispatch status:
PM-1 WORK_ORDER_READY.
PM-2 DEMAND_GATED (PM-1 must close first).
PM-3 DEMAND_GATED (PM-2 must close first).

## Current Certified Baseline

| Provider | Model | Method | Evidence |
| --- | --- | --- | --- |
| Alibaba | qwen-turbo | `chat` | `rcpt-env-mpql0ujo-4gawwj` (D1 live proof) |
| DeepSeek | deepseek-chat | `chat` | `rcpt-env-mpqlrk1z-xhs73v` (W3 live proof) |

Gaps:
- Alibaba stream adapter: W5 implemented `stream()` adapter; never live-proven
- DeepSeek `json_mode`: W5 implemented `json_mode()` adapter; never live-proven
- Alibaba vision (`qwen-vl-plus`): capability registry has entry; never live-proven

## Purpose

W5 delivered provider method normalization contracts. D2 delivered a capability
registry. Both have adapters and types but no live receipts for non-`chat`
methods. PM closes those gaps one method at a time, each with a bounded live
receipt.

---

## PM-1 — Alibaba Streaming Method Live Proof

**Risk:** R1 — additive live call, existing adapter.

**Gap:** `provider-method-fallback-normalization.ts` has `stream()` adapter for
Alibaba. W5 tests use mocks. No live SSE stream receipt exists.

**Deliverables:**
1. Live proof script or test: call Alibaba qwen-turbo with `stream: true`
2. Live receipt with `evidenceMode: live`, provider `alibaba`, method `stream`
3. Fast Lane audit + completion review documenting receipt and boundary

**Boundary:** SSE stream receipt only — not end-user delivery, not route change,
not public-sync.

**Contract version:** `cvf.providerMethodLiveProof.pm1.streaming.v1`

---

## PM-2 — DeepSeek JSON Mode Live Proof

**Risk:** R1/R2 — structured output constraint.

**Status:** DEMAND_GATED (PM-1 CLOSED_PASS required).

**Gap:** `provider-method-fallback-normalization.ts` has `json_mode()` adapter
for DeepSeek. No live `json_mode` receipt exists.

**Deliverables:**
1. Live proof: call DeepSeek deepseek-chat with `response_format: { type: "json_object" }`
2. Live receipt with method `json_mode`
3. Verify JSON-shaped output; capture structured evidence

**Contract version:** `cvf.providerMethodLiveProof.pm2.json_mode.v1`

---

## PM-3 — Alibaba Vision Method Live Proof

**Risk:** R2 — multi-modal input.

**Status:** DEMAND_GATED (PM-2 CLOSED_PASS required).

**Gap:** `provider-capability-registry.ts` lists `qwen-vl-plus` with `vision`
method. No live vision receipt exists.

**Deliverables:**
1. Live proof: call Alibaba qwen-vl-plus with image input
2. Live receipt with method `vision`, provider `alibaba`, model `qwen-vl-plus`
3. Verify image description output; confirm no raw key in output

**Contract version:** `cvf.providerMethodLiveProof.pm3.vision.v1`

---

## Scope

Target: bounded live HTTP call per PM tranche to the local `/api/execute` route
or direct provider API. No route code change, no public-sync without explicit
authorization, no new provider lane certification without a separate GC-018.

Owner: CVF execution surface; API keys stay operator-owned.

## Verification

For each PM tranche before closure:
- Live receipt ID present (`rcpt-env-*`)
- `evidenceMode: live` confirmed
- `rawSecretPrinted: false` confirmed
- Provider, model, and method cited in completion review

## Non-Goals

- Universal provider parity claim
- Production stability of any streaming or vision method
- Route-level streaming SSE delivery to end users
- New provider lane certification
- Public-sync repo changes without explicit authorization

## Work Plan

| Tranche | Method | Provider | Gate |
| --- | --- | --- | --- |
| PM-1 | stream | Alibaba/qwen-turbo | None — open |
| PM-2 | json_mode | DeepSeek/deepseek-chat | DEMAND_GATED (PM-1 closed) |
| PM-3 | vision | Alibaba/qwen-vl-plus | DEMAND_GATED (PM-2 closed) |

## Acceptance Criteria

- [ ] PM-1: live stream receipt from Alibaba qwen-turbo; `evidenceMode: live`; `rawSecretPrinted: false`
- [ ] PM-2: live json_mode receipt from DeepSeek; structured JSON output confirmed
- [ ] PM-3: live vision receipt from Alibaba qwen-vl-plus; image description confirmed

## Claim Boundary

PM proves individual provider method capabilities. Does not claim production
stability, universal provider parity, end-user SSE delivery, or hosted readiness.
