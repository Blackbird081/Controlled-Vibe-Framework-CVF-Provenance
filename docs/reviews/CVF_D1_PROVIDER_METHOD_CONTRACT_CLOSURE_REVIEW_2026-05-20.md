# CVF D1 Provider Method Contract Closure Review

Memory class: FULL_RECORD

Status: CLOSED

docType: review

Reviewer: Codex

Date: 2026-05-20

---

## Purpose

Close Residual D1 by recording where `retry`, `cost`, and `risk` belong.

---

## Target

- Work order: `docs/work_orders/CVF_WO_RESIDUAL_D1_PROVIDER_METHOD_CONTRACT_2026-05-20.md`
- Baseline: `docs/baselines/CVF_GC018_D1_PROVIDER_METHOD_CONTRACT_RESIDUAL_2026-05-20.md`

---

## Scope / Methodology

Reviewed model-gateway provider contracts, routing/fallback/quota policy, and
CLI risk scoring surfaces.

---

## Findings

- `retry()` is already represented by fallback and provider-output retryability
  semantics.
- `cost()` is policy/routing owned through quota and amount-aware risk scoring.
- `risk()` is policy/routing owned through gateway policy, provider risk class,
  and CLI risk scoring.
- No new contract files were created.
- `llm.adapter.interface.ts` was not changed.

Verification snapshot:

- `npm test` in `EXTENSIONS/CVF_MODEL_GATEWAY`: PASS, 59 tests.
- `npm run check` in `EXTENSIONS/CVF_MODEL_GATEWAY`: PASS.
- Local governance hook chain: pre-commit PASS, 11/11.
- Local governance hook chain: pre-push PASS, 43/43.

---

## Risk / Corrective Action

Future method-contract work must distinguish method-call capability from
policy/routing ownership before adding files.

---

## Decision / Disposition

Disposition: CLOSED_BY_METHOD_PLACEMENT_REJECTION.

---

## Claim Boundary

This review closes only D1's residual method contract decision. It does not
claim new provider execution semantics or adapter interface changes.
