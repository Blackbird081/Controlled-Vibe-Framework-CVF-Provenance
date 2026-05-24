# CVF GC-018 D1 Provider Method Contract Residual

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-20

---

## Purpose

Authorize the residual decision for `retry`, `cost`, and `risk` provider method
asks.

---

## Source or Predecessor Evidence

- `docs/work_orders/CVF_WO_RESIDUAL_D1_PROVIDER_METHOD_CONTRACT_2026-05-20.md`
- `docs/reviews/archive/CVF_W1_PROVIDER_CONTRACT_COMPLETION_2026-05-19.md`
- `docs/reviews/archive/CVF_LANE_D_PROVIDER_METHOD_PARITY_COMPLETION_2026-05-19.md`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/fallback-policy.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-policy.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`

---

## Decision / Baseline

Decision: EXPLICIT_REJECTION for all three residual methods.

| Method | Outcome | Existing owning surface |
| --- | --- | --- |
| `retry()` | EXPLICIT_REJECTION | `fallback-policy.ts` and `provider-output-contract.ts` own retry/fallback classification |
| `cost()` | EXPLICIT_REJECTION | `quota-ledger.ts`, `routing-policy.ts`, and CLI `quickRiskScore(... amount)` own quota/cost-adjacent policy |
| `risk()` | EXPLICIT_REJECTION | `gateway-policy.ts`, `provider-registry.ts`, and CLI `quickRiskScore` own risk classification |

Adding standalone method contract files would duplicate policy/routing surfaces
and could imply blocked provider execution semantics.

---

## Scope or Proposed Tranche

Authorized:

- Record per-method explicit rejection.
- File closure review.

Forbidden:

- New `retry-contract.ts`, `cost-contract.ts`, or `risk-contract.ts` in this
  tranche.
- Changes to `llm.adapter.interface.ts`.
- Provider execution semantics.

---

## Evidence / Required Evidence / Verification

Required verification:

- `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY`
- `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`
- `git diff` confirms `llm.adapter.interface.ts` unchanged.

---

## Claim Boundary

This baseline closes only the residual method-placement question. It does not
add provider methods, adapter semantics, or runtime routing behavior.
