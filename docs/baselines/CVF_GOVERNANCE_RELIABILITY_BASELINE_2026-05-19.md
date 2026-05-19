# CVF Governance Reliability Baseline

Memory class: SUMMARY_RECORD
Status: BASELINE_DEFERRED_NO_REAL_AUDIT_LOG

## Purpose

Record the first Lane E governance reliability metric baseline posture without
presenting synthetic unit-test data as operational evidence.

## Scope

This baseline covers the four offline metrics implemented by Lane E:

- `receiptIntegrityRate`
- `policyDecisionRate`
- `stepTraceCompletionRate`
- `auditEventCaptureRate`

It does not cover live provider benchmarking, QBS output-quality scoring,
hallucination recovery, or cross-session continuity.

## Source / Predecessor Evidence

- `docs/baselines/CVF_GC018_LANE_E_BENCHMARK_REORIENTATION_2026-05-19.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
- Existing JSONL files checked:
  `docs/assessments/CVF_EVT2_LIVE_LATENCY_MEASUREMENT_2026-05-14.jsonl` and
  `docs/baselines/pvv_phase_a_pilot_evidence.jsonl`

## Baseline

Baseline result: `baseline_deferred_no_real_audit_log`.

Reason: existing JSONL files in this workspace are live latency or PVV evidence
records, not governance audit JSONL logs with the required event fields:
`receiptId`, `decision === "captured"`, `enforcement.status`,
`stepTraceIds`, and execution request events. Synthetic fixtures were used only
for unit tests.

Placement note: the work order originally requested `docs/benchmark/`, but the
active docs taxonomy in `docs/INDEX.md` does not allow a `benchmark` folder.
This baseline therefore lives in `docs/baselines/`.

## Evidence / Verification

The CLI command shape is:

```powershell
cvf benchmark governance --input <audit.jsonl> [--format json|table]
```

When a real governance audit JSONL source is produced, rerun the command and
replace this deferred baseline with measured values in a new dated baseline
document.

## Claim Boundary

Lane E defines and tests the metric computation path. It does not yet provide
an operational reliability baseline because no suitable real audit JSONL source
was available in the workspace.
