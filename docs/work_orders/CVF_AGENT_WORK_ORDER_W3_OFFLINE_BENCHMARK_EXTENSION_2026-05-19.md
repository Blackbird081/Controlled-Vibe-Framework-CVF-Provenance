# CVF Agent Work Order — W3: Offline 9-Metric Benchmark Extension

Memory class: SUMMARY_RECORD

Status: OPEN

GC-018 required: No — hardening of existing `benchmark` command, R0 scope (same as C2).

## Purpose

Extend `governance-reliability-metrics.ts` from 4 metrics to 9 and add a
`cvf benchmark run` subcommand to `command.registry.ts` that reads any JSONL
audit log via `--input <path>` and outputs a 9-metric governance reliability
report. Tests use in-memory fixture JSONL strings — no live audit JSONL is
required, and no live proof is claimed.

Closes: Review CVF Problem E (offline benchmark extension — per-slice).

## Authority Chain

`docs/roadmaps/CVF_PHASE3_REVIEW_CLOSURE_ROADMAP_V2_2026-05-19.md` — W3 section.
No GC-018 required. Worker may begin immediately after reading this work order
and completing the source-fidelity pre-flight below.

## Agent Roles

- **Orchestrator** — dispatches this work order; accepts completion packet.
- **Worker** — implements all tasks in `CVF_ECO_v2.2_GOVERNANCE_CLI` only; runs
  pre-flight before any code; files completion review upon closure.

## Scope

**Allowed scope:**

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
  — MODIFY (extend from 4 to 9 metrics; ≤ 180 lines after changes)
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/governance-reliability-metrics.test.ts`
  — MODIFY (add 5 new tests; ≤ 220 lines after changes)
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
  — MODIFY (add `benchmark run` subcommand wiring only)

**Forbidden scope:**

- Any live HTTP call, AI provider call, or file system read beyond `--input` flag
- Any new metric that requires external data sources
- Public-sync repo edits
- Any file outside `CVF_ECO_v2.2_GOVERNANCE_CLI/`

## Write Ownership

Worker owns: `governance-reliability-metrics.ts` (extend), `governance-reliability-metrics.test.ts` (extend), `command.registry.ts` (add `benchmark run` branch only). No other files.

## Required First Reads

1. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
   — full file (94 lines, 4 existing metrics)
2. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/governance-reliability-metrics.test.ts`
   — full test file (current test count and structure)
3. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
   — lines 125–160 (existing `benchmark` command registration)
4. This work order — done criteria and metric specifications

## Source-Fidelity Pre-Flight (Worker must verify before writing)

```text
1. Confirm governance-reliability-metrics.ts is 94 lines (4 metrics)
2. Confirm GovernanceReliabilityReport has exactly 4 fields
3. Confirm parseAuditJsonl() and computeGovernanceReliabilityReport() exist
4. Confirm benchmark command registered at ~line 135 of command.registry.ts
5. Confirm NO 'benchmark run' subcommand exists in command.registry.ts
6. Confirm npm test currently passes (record test count as baseline)
```

## Execution Plan

Task 1 (5 new metric functions) → Task 2 (extend interface + report function) →
Task 3 (5 new tests) → Task 4 (benchmark run subcommand) in sequence.

### Task 1 — 5 New Metric Functions

Add to `governance-reliability-metrics.ts` after the existing 4 functions.
All functions follow the same `ratio()` helper pattern already in the file.

**`taskCompletionRate`** — ratio of events where `decision === 'allow'` over total:

```typescript
export function taskCompletionRate(events: AuditEvent[]): MetricResult {
  return ratio(
    events.filter((e) => e.decision === 'allow').length,
    events.length,
  );
}
```

**`retryRecoveryRate`** — ratio of events where `enforcement.status === 'retry'`
or `enforcement.status === 'recovered'` over events with any enforcement status:

```typescript
export function retryRecoveryRate(events: AuditEvent[]): MetricResult {
  const withStatus = events.filter((e) => Boolean(e.enforcement?.status));
  const recovered = withStatus.filter((e) =>
    e.enforcement?.status === 'retry' || e.enforcement?.status === 'recovered'
  );
  return ratio(recovered.length, withStatus.length);
}
```

**`policyViolationRate`** — ratio of events where `enforcement.status === 'deny'`
or `enforcement.status === 'blocked'` over total:

```typescript
export function policyViolationRate(events: AuditEvent[]): MetricResult {
  return ratio(
    events.filter((e) =>
      e.enforcement?.status === 'deny' || e.enforcement?.status === 'blocked'
    ).length,
    events.length,
  );
}
```

**`crossSessionContinuityRate`** — ratio of distinct `runId` values that appear
in more than one event (cross-session continuity) over total distinct `runId`
values. Uses the existing `executionKey()` helper indirectly:

```typescript
export function crossSessionContinuityRate(events: AuditEvent[]): MetricResult {
  const runGroups = new Map<string, number>();
  events.forEach((e) => {
    const key = nonEmptyString(e.runId);
    if (key) runGroups.set(key, (runGroups.get(key) ?? 0) + 1);
  });
  const total = runGroups.size;
  const crossSession = [...runGroups.values()].filter((count) => count > 1).length;
  return ratio(crossSession, total);
}
```

**`deterministicConsistencyRate`** — ratio of `executionId` values that have
exactly 1 audit event (no duplicate execution IDs, indicating deterministic
dispatch) over total distinct `executionId` values:

```typescript
export function deterministicConsistencyRate(events: AuditEvent[]): MetricResult {
  const execGroups = new Map<string, number>();
  events.forEach((e) => {
    const key = nonEmptyString(e.executionId);
    if (key) execGroups.set(key, (execGroups.get(key) ?? 0) + 1);
  });
  const total = execGroups.size;
  const deterministic = [...execGroups.values()].filter((count) => count === 1).length;
  return ratio(deterministic, total);
}
```

Note: `nonEmptyString` is already defined in the file — do not redefine.

### Task 2 — Extend Interface and Report Function

Extend `GovernanceReliabilityReport`:

```typescript
export interface GovernanceReliabilityReport {
  receiptIntegrityRate: MetricResult;
  policyDecisionRate: MetricResult;
  stepTraceCompletionRate: MetricResult;
  auditEventCaptureRate: MetricResult;
  taskCompletionRate: MetricResult;
  retryRecoveryRate: MetricResult;
  policyViolationRate: MetricResult;
  crossSessionContinuityRate: MetricResult;
  deterministicConsistencyRate: MetricResult;
}
```

Extend `computeGovernanceReliabilityReport()` to include all 9 metrics:

```typescript
export function computeGovernanceReliabilityReport(events: AuditEvent[]): GovernanceReliabilityReport {
  return {
    receiptIntegrityRate: receiptIntegrityRate(events),
    policyDecisionRate: policyDecisionRate(events),
    stepTraceCompletionRate: stepTraceCompletionRate(events),
    auditEventCaptureRate: auditEventCaptureRate(events),
    taskCompletionRate: taskCompletionRate(events),
    retryRecoveryRate: retryRecoveryRate(events),
    policyViolationRate: policyViolationRate(events),
    crossSessionContinuityRate: crossSessionContinuityRate(events),
    deterministicConsistencyRate: deterministicConsistencyRate(events),
  };
}
```

`governance-reliability-metrics.ts` must be ≤ 180 lines after all additions.

### Task 3 — 5 New Tests

Add to existing test file (≤ 220 lines total after additions). Use same fixture
pattern already in the file (in-memory JSONL strings). Each test is independent.

```typescript
it('taskCompletionRate: counts allow decisions', () => {
  const events: AuditEvent[] = [
    { decision: 'allow' }, { decision: 'allow' }, { decision: 'deny' },
  ];
  const result = taskCompletionRate(events);
  expect(result.count).toBe(2);
  expect(result.total).toBe(3);
  expect(result.rate).toBeCloseTo(2 / 3);
});

it('retryRecoveryRate: counts retry/recovered enforcement', () => {
  const events: AuditEvent[] = [
    { enforcement: { status: 'retry' } },
    { enforcement: { status: 'recovered' } },
    { enforcement: { status: 'deny' } },
  ];
  const result = retryRecoveryRate(events);
  expect(result.count).toBe(2);
  expect(result.total).toBe(3);
});

it('policyViolationRate: counts deny/blocked enforcement', () => {
  const events: AuditEvent[] = [
    { enforcement: { status: 'deny' } },
    { enforcement: { status: 'blocked' } },
    { enforcement: { status: 'allow' } },
  ];
  const result = policyViolationRate(events);
  expect(result.count).toBe(2);
  expect(result.total).toBe(3);
});

it('crossSessionContinuityRate: counts runIds appearing more than once', () => {
  const events: AuditEvent[] = [
    { runId: 'run-1' }, { runId: 'run-1' }, { runId: 'run-2' },
  ];
  const result = crossSessionContinuityRate(events);
  expect(result.count).toBe(1); // run-1 appears twice
  expect(result.total).toBe(2); // 2 distinct runIds
});

it('deterministicConsistencyRate: counts executionIds with exactly 1 event', () => {
  const events: AuditEvent[] = [
    { executionId: 'exec-1' }, { executionId: 'exec-1' }, { executionId: 'exec-2' },
  ];
  const result = deterministicConsistencyRate(events);
  expect(result.count).toBe(1); // exec-2 is deterministic
  expect(result.total).toBe(2); // 2 distinct executionIds
});
```

### Task 4 — `benchmark run` Subcommand

In `command.registry.ts`, modify the existing `benchmark` command registration
to add `run` subcommand handling. The simplest correct approach:

Check if `args.positional[0] === 'run'` inside the existing `benchmarkCommand()`
private method. If `run` subcommand detected, read from `--input`, parse JSONL,
run `computeGovernanceReliabilityReport`, format and print all 9 metrics.

The output format:

```text
CVF Governance Reliability Report
==================================
receiptIntegrityRate:        0.95 (19/20)
policyDecisionRate:          1.00 (20/20)
stepTraceCompletionRate:     0.90 (18/20)
auditEventCaptureRate:       1.00 (20/20)
taskCompletionRate:          0.85 (17/20)
retryRecoveryRate:           0.50  (5/10)
policyViolationRate:         0.10  (2/20)
crossSessionContinuityRate:  0.30  (3/10)
deterministicConsistencyRate: 1.00 (20/20)
```

Usage: `cvf benchmark run --input <path.jsonl> [--format json|table]`

With `--format json`, output the `GovernanceReliabilityReport` as JSON to stdout.

Do NOT add a new top-level command. Wire inside the existing `benchmarkCommand()`
private method, branching on `args.positional[0]`.

## Acceptance Criteria

- [ ] 5 new metric functions exported: `taskCompletionRate`, `retryRecoveryRate`, `policyViolationRate`, `crossSessionContinuityRate`, `deterministicConsistencyRate`
- [ ] `GovernanceReliabilityReport` interface has all 9 fields
- [ ] `computeGovernanceReliabilityReport()` returns all 9 metrics
- [ ] `governance-reliability-metrics.ts` ≤ 180 lines
- [ ] 5 new tests added, all PASS; test file ≤ 220 lines
- [ ] `cvf benchmark run --input <path>` subcommand wired in existing `benchmarkCommand()` — no new top-level command added
- [ ] `npm test` PASS (all existing + 5 new — show count before and after)
- [ ] `npm run check` PASS

## Evidence Requirements

Completion review must include:

1. `npm test` output — PASS; test count before vs. after (show +5)
2. `npm run check` output — PASS
3. `wc -l governance-reliability-metrics.ts` ≤ 180
4. Sample `cvf benchmark run` stdout showing all 9 metric lines (use a fixture JSONL inline string in the review)
5. Confirmation: no live HTTP call, no AI SDK import added to any file

## Review Gate

Orchestrator reviews completion packet. No closure without:

- 5 new metric functions exported and all 9 in `GovernanceReliabilityReport`
- `governance-reliability-metrics.ts` ≤ 180 lines confirmed
- `npm test` PASS (count before and after shown)
- `npm run check` PASS
- Sample `cvf benchmark run` output showing all 9 metrics

## Closure Checklist

- [ ] GC-018 not required — confirmed R0 scope (hardening of existing benchmark command)
- [ ] 5 new metric functions added: `taskCompletionRate`, `retryRecoveryRate`, `policyViolationRate`, `crossSessionContinuityRate`, `deterministicConsistencyRate`
- [ ] `GovernanceReliabilityReport` has 9 fields
- [ ] `computeGovernanceReliabilityReport()` returns all 9 metrics
- [ ] `governance-reliability-metrics.ts` ≤ 180 lines
- [ ] 5 new tests added, all PASS; test file ≤ 220 lines
- [ ] `cvf benchmark run --input <path>` subcommand wired (no new top-level command)
- [ ] `npm test` PASS
- [ ] `npm run check` PASS
- [ ] Completion review filed in CVF `docs/reviews/`
- [ ] GC-020 handoff HEAD SHA updated after commit

## Return-To-Orchestrator Conditions

Return immediately if:

- `governance-reliability-metrics.ts` would exceed 180 lines after additions — report and stop
- Test file would exceed 220 lines — split into a new test file instead; report
- `npm test` baseline fails before changes (pre-existing failure must be reported)
- `npm run check` fails after additions (type error from interface extension)
- `benchmarkCommand()` is not a private method (source has changed) — report and stop

## Target Repo

`Controlled-Vibe-Framework-CVF` (governance/provenance repo).
`EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/` only.

## Claim Boundary

W3 covers offline 9-metric benchmark extension and `cvf benchmark run` subcommand.
It does not add live audit log integration, real JSONL data from `docs/evidence/`,
new CLI top-level commands, or any provider/route/memory surface changes. Live proof
is not claimed.
