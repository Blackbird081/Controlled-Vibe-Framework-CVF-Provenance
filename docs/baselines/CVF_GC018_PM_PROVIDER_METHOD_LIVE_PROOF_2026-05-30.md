# CVF GC-018 — PM Provider Method Live Proof Roadmap

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-30

---

## Purpose

Authorize the PM Provider Method Live Proof Roadmap: three bounded live proof
tranches for provider method capabilities beyond the current `chat` baseline.

Current certified live proof: `chat` method on Alibaba/qwen-turbo and
DeepSeek/deepseek-chat (confirmed by Delta D1 receipt `rcpt-env-mpql0ujo-4gawwj`
and WCE W3 receipt `rcpt-env-mpqlrk1z-xhs73v`).

---

## Source / Predecessor Evidence

- W5 provider method normalization: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/provider-method-fallback-normalization.ts`
- D2 capability registry: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/provider-capability-registry.ts`
- Current certified receipts: `rcpt-env-mpql0ujo-4gawwj` (Alibaba/chat) and `rcpt-env-mpqlrk1z-xhs73v` (DeepSeek/chat)

## Decision / Baseline

Decision: proceed with PM-1 (Alibaba streaming) as WORK_ORDER_READY. PM-2
(DeepSeek json_mode) and PM-3 (Alibaba vision) are DEMAND_GATED pending PM-1
CLOSED_PASS. Each PM tranche requires one bounded live receipt per method.

Proposed tranche order: PM-1 stream → PM-2 json_mode → PM-3 vision.

## Evidence / Verification

Before closure of each PM tranche:
- Live receipt with `evidenceMode: live` for the specific method
- `rawSecretPrinted: false` confirmed
- Provider and method cited explicitly in completion review

## Authorization Basis

- Operator authorization: operator direction 2026-05-30
- W5 provider method normalization: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/provider-method-fallback-normalization.ts`
- D2 provider capability registry: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/provider-capability-registry.ts`
- API keys available: Alibaba/DeepSeek/OpenAI (operator confirmed 2026-05-29)
- Risk: R1/R2 per method

---

## Scope — Three Phases

### PM-1 (WORK_ORDER_READY) — Streaming Proof
Live proof that Alibaba stream adapter works: SSE stream from `chat` endpoint
with Alibaba qwen-turbo. Additive — does not change route.ts behavior.
Risk: R1.

### PM-2 (DEMAND_GATED after PM-1) — JSON Mode Proof
Live proof for DeepSeek `json_mode` method: structured JSON output from
deepseek-chat. Risk: R1/R2.

### PM-3 (DEMAND_GATED after PM-2) — Vision Proof
Live proof for Alibaba qwen-vl-plus vision method: image input + text output.
Risk: R2.

---

## Claim Boundary

PM proves individual provider method capabilities with live receipts.
Does not claim: universal provider parity, production stability of any provider,
streaming SSE delivery to end users, or hosted readiness.
