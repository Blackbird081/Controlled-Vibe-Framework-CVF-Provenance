# CVF GC-018 Lane E Benchmark Reorientation

Memory class: SUMMARY_RECORD
Status: AUTHORIZED

## Purpose

Authorize Lane E to add offline governance reliability metrics to the
governance CLI and publish the first honest baseline posture for the metric
set.

## Scope

In scope:

- add
  `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`;
- define `receiptIntegrityRate`, `policyDecisionRate`,
  `stepTraceCompletionRate`, and `auditEventCaptureRate`;
- add `cvf benchmark governance --input <path>` with optional
  `--format json|table`;
- add `BenchmarkGovernanceOptions` in CLI types;
- add unit tests for metric formulas, edge cases, and command behavior;
- create `docs/baselines/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md`.

Out of scope:

- live provider benchmark execution;
- QBS-1, W72, W91, or W98 benchmark rebuilds;
- hallucination recovery or cross-session continuity metrics;
- public claims that governance reliability has been live-benchmarked.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_E_BENCHMARK_REORIENTATION_2026-05-19.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/types.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`

## Source-Fidelity Pass

Pre-flight source checks found no existing `benchmark governance` command and
no existing `receiptIntegrityRate` implementation in the CLI package.

The work order requested `docs/benchmark/`, but the active docs taxonomy in
`docs/INDEX.md` does not allow a `benchmark` folder. Existing JSONL evidence
under `docs/assessments/` and `docs/baselines/` is live/provider or PVV
evidence, not a governance audit JSONL log with the full metric shape. Lane E
therefore must not present synthetic fixture data as the first operational
baseline. If no real audit JSONL with the required fields is available, the
baseline document must live in `docs/baselines/` and say
`baseline_deferred_no_real_audit_log`.

## Decision / Baseline / Proposed Tranche

Decision: implement Lane E as an offline CLI computation tranche.

Metric formulas:

- `receiptIntegrityRate(events)`: count events with non-empty `receiptId` and
  `decision === "captured"` over total events.
- `policyDecisionRate(events)`: count events with non-empty
  `enforcement.status` and status not equal to `"error"` over total events.
- `stepTraceCompletionRate(events)`: count events with a non-empty
  `stepTraceIds` array over total events.
- `auditEventCaptureRate(events)`: count unique execution IDs with at least one
  audit event over the total execution request count found in the log.

Exact CLI subcommand:

```powershell
cvf benchmark governance --input <path> [--format json|table]
```

Risk ceiling: R0, because this reads local JSONL and performs deterministic
offline computation only.

## Rule

Lane E may claim:

> The CLI defines and offline-tests four governance reliability metrics and can
> compute them from a JSONL audit log.

Lane E must not claim:

> A live provider benchmark was run or a production governance reliability
> baseline exists when no real audit JSONL source was available.

## Evidence / Verification

Required commands:

```powershell
npm test
npm run check
```

Run in:

```text
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI
```

Repository guard:

```powershell
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

## Tranche Closure Checklist

- Metric module exists with all four functions.
- `cvf benchmark governance --input <path>` is registered.
- Tests prove normal and edge cases.
- Baseline document uses a real audit JSONL source or explicitly defers.
- No QBS or historical benchmark files are modified.
- No live provider call is made.
- Current governance hook chain passes without bypassing hooks.

## Claim Boundary

This authorization covers only offline metric definition and CLI computation.
Operational governance-reliability baselining remains deferred until a real
audit JSONL source exists.
