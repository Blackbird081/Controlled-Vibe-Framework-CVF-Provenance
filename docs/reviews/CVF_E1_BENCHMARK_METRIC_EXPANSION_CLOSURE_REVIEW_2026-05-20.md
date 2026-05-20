# CVF E1 Benchmark Metric Expansion Closure Review

Memory class: FULL_RECORD

Status: CLOSED

docType: review

Reviewer: Codex

Date: 2026-05-20

---

## Purpose

Close Residual E1 by recording the offline benchmark metric expansion.

---

## Target

- Work order: `docs/work_orders/CVF_WO_RESIDUAL_E1_BENCHMARK_METRIC_EXPANSION_2026-05-20.md`
- Baseline: `docs/baselines/CVF_GC018_E1_BENCHMARK_METRIC_EXPANSION_2026-05-20.md`
- Code: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
- Tests: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/governance-reliability-metrics.test.ts`

---

## Scope / Methodology

Verified schema-first metric expansion and CLI benchmark formatter behavior.

---

## Findings

- Added typed `operator_correction` and `rollback` event shapes.
- Added `humanCorrectionRate`, `longHorizonStabilityRate`, and
  `rollbackSuccessRate`.
- Extended `GovernanceReliabilityReport` from 9 to 12 fields.
- Updated table and JSON benchmark output handling; `null` rates render as
  `n/a` in table/text output.
- Hallucination recovery remains explicitly rejected.
- Benchmark remains offline only.

Verification snapshot:

- `npm test` in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`: PASS, 97 tests.
- `npm run check` in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`: PASS.
- Local governance hook chain: pre-commit PASS, 11/11.
- Local governance hook chain: pre-push PASS, 43/43.

---

## Risk / Corrective Action

Rollback success returns `null` when there are no rollback events. This avoids
misrepresenting absent rollback data as a failed rollback lane.

---

## Decision / Disposition

Disposition: CLOSED_FOR_OFFLINE_BENCHMARK_METRIC_CONTRACT.

Problem E moves from PARTIAL to CLOSED for the current offline operational
benchmark contract. Future hallucination-recovery work requires a separate
LLM-judged evaluation charter.

---

## Claim Boundary

This review claims only offline benchmark expansion. It does not claim live
provider behavior, release readiness, or hallucination-recovery capability.
