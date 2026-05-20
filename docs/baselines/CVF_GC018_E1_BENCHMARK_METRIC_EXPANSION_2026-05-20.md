# CVF GC-018 E1 Benchmark Metric Expansion

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-20

---

## Purpose

Authorize the offline governance benchmark metric expansion from 9 to 12
metrics.

---

## Source or Predecessor Evidence

- `docs/work_orders/CVF_WO_RESIDUAL_E1_BENCHMARK_METRIC_EXPANSION_2026-05-20.md`
- `docs/reviews/CVF_LANE_E_BENCHMARK_REORIENTATION_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`

---

## Decision / Baseline

Decision: CONTRACT_CLOSURE for computable offline metrics.

Authorized metrics:

| Metric | Data dependency | Boundary |
| --- | --- | --- |
| `humanCorrectionRate` | `operator_correction` events keyed by `executionId` | Offline JSONL only |
| `longHorizonStabilityRate` | timestamps grouped by `executionId`, plus violation and rollback events | Offline JSONL only |
| `rollbackSuccessRate` | `rollback` events with `success: boolean` | Returns `null` when no rollback exists |

Rejected metric:

- `hallucination_recovery`: rejected because it requires LLM-judged
  classification outside the offline benchmark contract.

---

## Scope or Proposed Tranche

Authorized:

- Extend the typed audit event schema in
  `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`.
- Add the three metric functions.
- Extend JSON and table formatters.
- Add unit tests.

Forbidden:

- Live benchmark mode.
- Provider API calls.
- Hallucination-recovery scoring.

---

## Evidence / Required Evidence / Verification

Required verification:

- `npm test` in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`
- `npm run check` in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`

Both commands are offline and require no API keys.

---

## Claim Boundary

This baseline authorizes offline metric expansion only. It does not claim live
governance proof, hallucination recovery, or release readiness.
