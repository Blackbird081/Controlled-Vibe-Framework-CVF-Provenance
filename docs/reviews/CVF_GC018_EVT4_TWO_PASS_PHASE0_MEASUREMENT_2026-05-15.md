# CVF GC-018 — EVT-4 Two-Pass Quality Expansion Phase 0

**Date:** 2026-05-15  
**Status:** EXECUTED - RUNTIME IMPLEMENTATION NOT AUTHORIZED BY EVIDENCE  
**Scope:** Measure F-1a two-pass quality expansion before any runtime
implementation.

## Authorization

User accepted the F-1a direction after Claude's critique: do not patch
templates/prompts further as a closure strategy; first measure whether a
two-pass governed quality expansion can meet the EVT-4 parity rule.

## Hypothesis

The retained one-pass governed CFG-B path is consistently shorter and thinner
than the bare provider CFG-A path. If a second governed expansion pass preserves
safety while adding concrete examples, owner/role assignments, first actions,
verification signals, and acceptance checks, EVT-4 quality may reach the
registered parity rule.

## Phase 0 Only

This tranche intentionally does **not** change production runtime behavior.

Allowed work:

- Add an opt-in experimental mode to `scripts/run_evt4_output_quality_ab.js`.
- Keep one-pass behavior as the default.
- When `EVT4_TWO_PASS_EXPANSION=true`, run CFG-B as:
  - Pass 1: existing governed `/api/execute` call.
  - Pass 2: a second governed `/api/execute` call using the first output as
    `_previousOutput` and an expansion-specific intent.
- Record both pass receipts, duration, output hashes, excerpts, and usage.
- Run live EVT-4 with the experimental mode.

## Governance Risks To Measure

- **Cost/latency:** two-pass may roughly double provider calls and route time.
- **Safety drift:** pass 2 must not introduce bypass, unsafe shortcuts, or
  unsupported claims.
- **Recommendation drift:** pass 2 should preserve the first recommendation
  unless it explicitly corrects an inconsistency.
- **Overclaim risk:** this run is not runtime proof and must not be presented
  as F-1 closure unless it meets the registered rule.

## Decision Rule

Proceed to a separate F-1a runtime GC-018 only if Phase 0 shows:

- 20/20 CFG-B live final receipts.
- 20/20 CFG-B pass-1 and pass-2 receipts when two-pass is enabled.
- 0 safety failures.
- Median normalized `CFG-B - CFG-A >= -0.05`.
- Cost/latency trade-off is recorded for owner decision.

If the rule is not met, do not implement runtime two-pass.

## Implementation

`scripts/run_evt4_output_quality_ab.js` now supports opt-in Phase 0 two-pass
measurement with:

```bash
EVT4_TWO_PASS_EXPANSION=true
```

Default behavior remains one-pass. When enabled, CFG-B performs:

- Pass 1: existing governed `/api/execute`.
- Pass 2: a second governed `/api/execute` with `_previousOutput` and a
  quality-expansion intent.

The evidence records include pass-1 and pass-2 receipt presence, receipt IDs,
output hashes, excerpts, duration, and usage.

## Live Evidence

Evidence:
`docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TWO_PASS_PHASE0_EVIDENCE_2026-05-15.json`

Summary:
`docs/assessments/CVF_EVT4_OUTPUT_QUALITY_AB_TWO_PASS_PHASE0_SUMMARY_2026-05-15.md`

Result:

- Completed pairs: 20/20.
- CFG-B final receipts: 20/20.
- CFG-B expansion receipts: 20/20 pass-1 + pass-2 receipt pairs.
- Safety failures: 0.
- Median normalized delta: `-0.16`.
- CFG-B median duration: `32217` ms.
- CFG-B median output tokens: `1966`.
- Decision rule met: `false`.

## Conclusion

Two-pass quality expansion is governance-feasible in the harness: it produced
all expected receipts and did not introduce safety failures. It did **not**
close F-1. The median stayed at `-0.16`, below the registered `>= -0.05`
closure threshold.

Per the Phase 0 decision rule, do **not** implement runtime two-pass yet. The
next F-1 closure attempt should not assume that more output length is enough;
it needs a sharper task-specific evaluator or rubric that targets the exact
dimensions reviewers still mark down: immediate actionability, specificity,
and task-fit.
