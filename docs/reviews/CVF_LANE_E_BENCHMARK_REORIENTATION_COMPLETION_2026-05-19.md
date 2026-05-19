# CVF Lane E Benchmark Reorientation Completion

Memory class: FULL_RECORD
Status: CLOSED - DEFINED AND OFFLINE TESTED

## Purpose

Close Lane E by adding four offline governance reliability metrics and a
`cvf benchmark governance` CLI command that computes them from a JSONL audit
log.

## Scope

Completed:

- added `governance-reliability-metrics.ts` to the governance CLI;
- added four metric functions:
  `receiptIntegrityRate`, `policyDecisionRate`,
  `stepTraceCompletionRate`, and `auditEventCaptureRate`;
- registered `cvf benchmark governance --input <path> [--format json|table]`;
- added `BenchmarkGovernanceOptions`;
- added unit tests for normal, edge, JSONL parse, and command execution paths;
- filed a baseline document in the taxonomy-compliant `docs/baselines/`.

Not completed:

- live provider benchmark run;
- hallucination recovery metric;
- cross-session continuity metric;
- QBS-1, W72, W91, or W98 benchmark changes.

## Source / Predecessor Evidence

- `docs/baselines/CVF_GC018_LANE_E_BENCHMARK_REORIENTATION_2026-05-19.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LANE_E_BENCHMARK_REORIENTATION_2026-05-19.md`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/governance-reliability-metrics.test.ts`
- `docs/baselines/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md`

## Decision / Baseline / Proposed Tranche

Decision: Lane E is closed as an offline metric computation tranche.

The implementation uses local JSONL only. It does not call a provider, mutate
existing benchmark preregistrations, or claim an operational reliability
baseline from synthetic fixtures.

## Findings

`docs/benchmark/` did not exist at the start of Lane E. The docs governance
guard rejected that folder because it is not part of the active taxonomy in
`docs/INDEX.md`, so the baseline was placed in `docs/baselines/`.

Existing JSONL files checked in this workspace are latency or PVV evidence
records, not governance audit logs with the full metric fields required by
Lane E. The baseline is therefore honestly marked
`baseline_deferred_no_real_audit_log`.

## Risk / Corrective Action

Risk: metric fixtures could be mistaken for operational data.

Corrective action: synthetic events are used only in tests. The baseline packet
records that no suitable real audit JSONL source was available.

## Evidence / Verification

Evidence trace:

- Claim: metric module exists with all four metric functions.
- Command:
  `Test-Path "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts"`
- Result: path exists.
- Key path:
  `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
- Verdict: PASS.

Evidence trace:

- Claim: baseline document exists.
- Command:
  `Test-Path "docs/baselines/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md"`
- Result: path exists.
- Key path: `docs/baselines/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md`
- Verdict: PASS.

Evidence trace:

- Claim: `benchmark governance` command is registered.
- Command:
  `rg -n "benchmark governance" EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- Result: usage and error strings include `cvf benchmark governance`.
- Key path: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- Verdict: PASS.

Verification commands:

```powershell
npm test
```

Run in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`: 5 test files passed, 59 tests
passed.

```powershell
npm run check
```

Run in `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI`: pass.

## Recommendation

The next real governance E2E runner should emit a JSONL audit log with
`receiptId`, `decision`, `enforcement.status`, `stepTraceIds`, and
`execution_requested` events so Lane E metrics can produce a non-deferred
baseline.

Public catalog update is N/A for this provenance commit. `cvf benchmark
governance` is defined and offline-tested here, but no public claim should be
made until the public-sync catalog path is verified and updated from the
public-sync clone.

## Claim Boundary

Lane E may be described as:

> Governance reliability metrics are defined and offline-tested, and the CLI
> can compute them from a JSONL audit log.

Lane E must not be described as:

> CVF has a measured operational governance reliability baseline from live
> audit traffic.
