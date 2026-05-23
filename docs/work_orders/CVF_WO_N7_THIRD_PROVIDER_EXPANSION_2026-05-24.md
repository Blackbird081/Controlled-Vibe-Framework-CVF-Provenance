# CVF Work Order: N7 Third Provider Expansion

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-24

Tranche: N7

Roadmap: `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Add a third AI provider to CVF's governed execution path. Currently CVF has
proven two providers: Alibaba (`qwen-turbo`) and DeepSeek (`deepseek-chat`).
This tranche adds a third operator-nominated provider with the same governance
coverage: capability registry entry, provider router wiring, targeted tests,
and a narrow live proof receipt.

---

## Authorization

Operator authorized on 2026-05-24 with the following confirmed parameters:

- **Provider name:** OpenAI
- **API base URL:** `https://api.openai.com/v1`
- **Model ID:** `gpt-4o`
- **Max risk level:** `R2`
- **API key env var:** `OPENAI_API_KEY` (confirmed present in `.env.local`)

**Pre-conditions before implementation:**

1. ~~Operator names provider~~ — DONE: OpenAI / gpt-4o / R2 / OPENAI_API_KEY
2. A fresh GC-018 is filed and accepted
3. Codex reads `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts`
   and `provider-router-adapter.ts` before implementing
4. Codex reads `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
   before implementing
5. ~~Operator confirms maxRiskLevel~~ — DONE: R2

---

## Authority Chain

Operator → Claude (roadmap author) → Codex (implementer).

Authorization: OPERATOR_AUTHORIZED 2026-05-24. Parent roadmap:
`docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`.

---

## Agent Roles

- Operator: authorizer — must name provider, model ID, risk ceiling, API key source
- Claude: GC-018 reviewer
- Codex: implementer

---

## Required First Reads

Before filing GC-018 (mandatory):

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts` — existing provider definitions
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts` — router logic + `maxRiskLevel` per provider
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` — `PROVIDER_CAPABILITY_REGISTRY` typed registry
- `docs/reference/CVF_QWEN3_HOSTED_PROOF_PREREQUISITES_2026-05-23.md` — if new provider is Alibaba-family (Qwen variant)
- `docs/reviews/CVF_D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF_COMPLETION_2026-05-23.md` — Alibaba R1 proof baseline

---

## Pre-Flight Checks

Before implementation:

1. Operator has named: provider name, API base URL, model ID(s), max risk level, API key env var
2. GC-018 filed and accepted
3. `providers.ts` read — understand existing structure for `ProviderConfig`
4. `provider-router-adapter.ts` read — understand `maxRiskLevel` enforcement
5. `PROVIDER_CAPABILITY_REGISTRY` read — understand `supportedMethods` schema
6. Confirm no raw API key will be committed (`rawSecretPrinted=false` invariant)
7. GC-023 line count check for `providers.ts` and `provider-router-adapter.ts` before editing

---

## Write Ownership

Codex owns:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.ts` (add new provider config)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/provider-router-adapter.ts` (add router entry + risk ceiling)
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` (add registry entry with `supportedMethods`)
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/` — targeted tests for new provider route
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/providers.test.ts` — targeted tests for new provider config
- `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md` — N7 row update

No receipt schema change, no session state change, no public-sync change.

---

## Execution Plan

1. Receive operator authorization and GC-018 acceptance
2. Read all Required First Reads
3. Add `ProviderConfig` entry in `providers.ts` for new provider
4. Add router entry in `provider-router-adapter.ts` with confirmed `maxRiskLevel`
5. Add `PROVIDER_CAPABILITY_REGISTRY` entry in `provider-capability-registry.ts`
   with `supportedMethods` (at minimum: `complete`; add `stream` or `json_mode`
   only if the provider API supports it)
6. Write targeted tests for new provider in both Model Gateway and cvf-web
7. Confirm existing Alibaba + DeepSeek tests still pass (no regression)
8. Run a narrow live proof: one governed call to `/api/execute` using the new
   provider, confirm `success=true`, `evidenceMode=live`, receipt present,
   `rawSecretPrinted=false`
9. Run full `cvf-web` test suite → regression-clean
10. Run TypeScript check → PASS
11. Update roadmap Progress Tracker N7 row → `CLOSED_PASS`
12. File completion review with live receipt
13. Commit

---

## Evidence Requirements

- New provider entry in `providers.ts`, `provider-router-adapter.ts`,
  `PROVIDER_CAPABILITY_REGISTRY` — all three surfaces
- Targeted tests PASS for new provider
- Existing Alibaba + DeepSeek tests still pass (regression check)
- Live proof: receipt with `success=true`, `evidenceMode=live`,
  `rawSecretPrinted=false`
- TypeScript check PASS
- GC-023 compliant for all modified files
- Completion review with receipt ID filed

---

## Scope / Target / Owner Boundary

In scope:

- Third provider registration on three governed surfaces
- Targeted tests
- One narrow live proof call

Out of scope:

- Broad stability claim for new provider (one proof call, not a soak)
- Universal provider parity claim
- New model families beyond the operator-nominated provider
- Receipt schema change
- Session state change
- Public-sync push

**Boundary:** This tranche proves one new provider in a narrow governed call.
It does not prove: broad stability, hosted SaaS readiness, or multiple models
on the new provider without separate GC-018.

---

## Acceptance Criteria

- [ ] Operator has named provider, model ID, risk ceiling, API key source
- [ ] GC-018 filed and accepted
- [ ] New provider in `providers.ts`
- [ ] New router entry in `provider-router-adapter.ts` with correct `maxRiskLevel`
- [ ] New registry entry in `PROVIDER_CAPABILITY_REGISTRY` with `supportedMethods`
- [ ] Targeted tests PASS
- [ ] Existing Alibaba + DeepSeek tests: no regression
- [ ] Live proof receipt: `success=true`, `evidenceMode=live`, `rawSecretPrinted=false`
- [ ] TypeScript check PASS
- [ ] GC-023 compliant for all modified files
- [ ] Roadmap Progress Tracker N7 row → `CLOSED_PASS`
- [ ] Completion review filed with live receipt ID

---

## Review Gate

Claude reviews the completion package for:

- Three governed surfaces updated
- `maxRiskLevel` correct for new provider
- `rawSecretPrinted=false` confirmed in live proof
- No regression on existing two providers
- TypeScript PASS; GC-023 compliant
- Bounded wording in completion review (one narrow proof, not broad stability)

---

## Closure Checklist

- [ ] Operator authorization received (provider named)
- [ ] GC-018 filed and accepted
- [ ] Required first reads complete
- [ ] `providers.ts` entry added
- [ ] `provider-router-adapter.ts` entry added
- [ ] `PROVIDER_CAPABILITY_REGISTRY` entry added
- [ ] Targeted tests PASS
- [ ] Existing provider tests: no regression
- [ ] Live proof: receipt with `success=true`, `rawSecretPrinted=false`
- [ ] TypeScript check PASS
- [ ] GC-023 compliant
- [ ] Roadmap N7 row → `CLOSED_PASS`
- [ ] Completion review with receipt ID filed

---

## Return-To-Orchestrator Conditions

Return to Claude when all closure checklist items are complete, or when a
blocker is encountered (e.g., provider API incompatibility, `maxRiskLevel`
conflict, test regression on existing providers).

---

## Operator Checkpoint

Checkpoint required: operator must explicitly name the third provider (provider
name, API endpoint, model ID, max risk level, API key env var name) before
implementation proceeds.

---

## Completion Review

After implementation, file at:
`docs/reviews/CVF_N7_THIRD_PROVIDER_EXPANSION_COMPLETION_2026-05-24.md`

Minimum sections: Purpose, Provider Named (operator confirmation), Three Surfaces
Updated, Live Proof Receipt, Regression Evidence, Bounded Claim, Claim Boundary.

---

## Claim Boundary

This work order does not authorize: broad provider stability claim, universal
provider parity, production/hosted readiness, receipt schema change, public-sync
update, or freeze release. One new provider proven in one narrow call.
