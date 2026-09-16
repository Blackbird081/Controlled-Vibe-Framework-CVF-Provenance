# CVF ACEL G6 T1 Impact-Derived Verification Experiment Result

Memory class: governed-experiment-result

Status: COMPLETE_PASS_BOUNDED

docType: audit

Date: 2026-09-16

Batch ID: ACEL-G6-T1-IMPACT-DERIVED-VERIFICATION-EXPERIMENT

## Purpose

Record the deterministic result of comparing a fixed verification bundle with
an impact-derived verifier subset over the same eight hermetic change cases,
seeded regressions, acceptance oracle, and Local-only authority envelope.

## Target / Source

| Artifact | Role |
|---|---|
| `docs/baselines/CVF_GC018_ACEL_G6_T1_IMPACT_DERIVED_VERIFICATION_EXPERIMENT_2026-09-16.md` | authority and acceptance criteria |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/impact.verification.experiment.contract.ts` | experiment contract and deterministic oracle |
| `docs/audits/CVF_ACEL_G6_T1_IMPACT_DERIVED_VERIFICATION_EXPERIMENT_32_RUN_RECEIPT_2026-09-16.json` | canonical result data |

## Scope / Methodology

The experiment executed eight cases under two policies with two repetitions,
for exactly 32 unique records. `FIXED_BUNDLE` selected all eight modeled
verifiers. `IMPACT_DERIVED` always retained `baseline-safety`, added verifiers
from the declared impact class, and fell back to the complete fixed bundle for
the `UNKNOWN` case. Cost and latency are deterministic experiment units, not
wall-clock production measurements.

## Result

| Measure | Fixed bundle | Impact-derived | Difference |
|---|---:|---:|---:|
| admitted runs | 16/16 | 16/16 | 0 |
| detected seeded regressions | 16 | 16 | 0 |
| missed seeded regressions | 0 | 0 | 0 |
| deterministic cost units | 480 | 172 | -308 (-64.2%) |
| deterministic latency units | 1088 | 398 | -690 (-63.4%) |

The unknown-owner fixture selected the complete fixed bundle and recorded
`UNKNOWN_IMPACT_FAIL_CLOSED`. A negative unit fixture also proved that a plan
which misses a required verifier is not admitted.

## Evidence

- canonical receipt:
  `docs/audits/CVF_ACEL_G6_T1_IMPACT_DERIVED_VERIFICATION_EXPERIMENT_32_RUN_RECEIPT_2026-09-16.json`
- receipt SHA-256:
  `7cdee0dd741b4b26af2ba78cefe71e5b7e9a3096415b89abc4cb295490774e88`
- focused tests: PASS, 15/15
- TypeScript `--noEmit`: PASS
- two runner executions: byte-identical receipt and SHA-256
- provider, network, subagent, runtime, and production wiring: none

## Findings And Decision

Within this closed synthetic corpus, impact-derived selection preserved all
seeded-regression detections while reducing deterministic modeled cost by
64.2%. This is useful positive experiment evidence for G6, but it is not a
production selection rule: the cases and mappings are authored fixtures, the
latency values are proxies, and no historical or live regression corpus was
used.

Terminal result: `PASS_BOUNDED_EXPERIMENT_SIGNAL_ONLY`.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| unknown ownership could under-select checks | fail closed to the complete fixed bundle |
| fixture circularity could overstate detection | preserve result as proposal-only and require a separate real-corpus tranche |
| cost proxy could be mistaken for elapsed time | label all values deterministic units; make no wall-clock claim |
| experiment could silently alter production | module is not production-exported and no hook, CI, checker, or autorun owner changed |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: private proposal-only experiment evidence; no public-sync authority or
public artifact was granted.

## Claim Boundary

This result establishes deterministic behavior only for the eight versioned
fixtures. It does not authorize gate removal, impact-derived production
selection, runtime integration, provider execution, deployment, or public
export.
