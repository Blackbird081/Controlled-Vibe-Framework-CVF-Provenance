# CVF Agent Work Order — Lane E: Benchmark Reorientation

Memory class: POINTER_RECORD

Status: OPEN — awaiting Codex GC-018 filing before implementation begins.
Prerequisite: Lane D must be closed before Lane E begins.

## Purpose

Dispatch Codex to implement Lane E (Benchmark Reorientation) as defined in
`docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`.

Lane E adds 4 governance reliability metric definitions to the CLI and a
`cvf benchmark governance` subcommand that reads an audit JSONL log and
computes them. It does not rebuild existing QBS-1 or W-series benchmarks.

## Source

- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md` — lane E spec
- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` —
  Problem E: benchmark measures output quality, not governance reliability
- `AGENT_HANDOFF_V9_2026-05-18.md` — active session posture
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — current mode

## 1. Mission

Define 4 governance reliability metrics and a CLI command to compute them
from an existing audit JSONL log. Record the first baseline run.

Success means: `cvf benchmark governance --input <audit.jsonl>` outputs the
4 metric rates, a baseline document is filed, and unit tests pass.

## 2. Authority Chain

- Operator instruction: 2026-05-19 — implement Lane D/E/F/G in sequence
- Roadmap: `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`
- Decision pack: `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff: `AGENT_HANDOFF_V9_2026-05-18.md`
- Prerequisite: Lane D completion packet filed and reviewed

## 3. Agent Roles

- Orchestrator / dispatcher: operator and coordinating agent (Claude)
- Implementer: Codex
- Reviewer: Claude
- Operator approval required for: live provider benchmark run, hallucination
  recovery metric (demand-gated), QBS-1 changes

## 4. Required First Reads

Before filing GC-018:

1. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` — how
   existing commands are registered; `cvf benchmark governance` follows same pattern
2. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/types.ts` — existing type definitions
3. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` — audit
   event structure emitted by executions (Lane C output)
4. `docs/benchmark/` — list existing benchmark files; do not overwrite any
5. `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` — line
   limits before touching any governed file

Anti-duplication grep:

```powershell
rg -n "benchmark|governance.*metric|receiptIntegrity" EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/
ls docs/benchmark/
```

## 5. Pre-Flight Checks

```powershell
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_docs_governance_compat.py
Test-Path "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts"
ls docs/benchmark/
git status --short
```

## 6. GC-018 Requirements

Before implementation, file:

```
docs/baselines/CVF_GC018_LANE_E_BENCHMARK_REORIENTATION_2026-05-19.md
```

The GC-018 must record:

- exact file name for metric definitions (`governance-reliability-metrics.ts`)
- exact 4 metric names and their computation formulas
- exact CLI subcommand: `cvf benchmark governance --input <path>`
- baseline document path in `docs/benchmark/`
- R0 risk statement (offline computation only)
- explicit no-live-provider-call boundary
- acceptance criteria
- Tranche Closure Checklist

## 7. Write Ownership

Allowed scope:

```
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts  (NEW)
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts                 (MODIFY — add benchmark subcommand)
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/types.ts                            (MODIFY — BenchmarkOptions type)
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/governance-reliability-metrics.test.ts (NEW)
docs/benchmark/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md               (NEW)
docs/baselines/CVF_GC018_LANE_E_BENCHMARK_REORIENTATION_2026-05-19.md          (NEW)
docs/reviews/CVF_LANE_E_BENCHMARK_REORIENTATION_COMPLETION_2026-05-19.md       (NEW)
```

Forbidden scope:

```
docs/benchmark/qbs-preregistrations/   (existing — do not modify)
docs/benchmark/CVF_GOVERNANCE_TAX_*    (existing — do not modify)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/    (no web changes in this lane)
```

## 8. Execution Plan

1. Read existing benchmark files and CLI command registry.
   Grep for existing metric or benchmark command implementations.
   Stop if `cvf benchmark governance` already exists.

2. Define `governance-reliability-metrics.ts` with 4 metric functions:
   - `receiptIntegrityRate(events)`: % of events where `receiptId` is non-null
     and `decision === 'captured'`
   - `policyDecisionRate(events)`: % of events where `enforcement.status` is
     non-null and not `'error'`
   - `stepTraceCompletionRate(events)`: % of events where `stepTraceIds` array
     is non-empty
   - `auditEventCaptureRate(events)`: % of executions where at least one audit
     event was emitted (total events / total execution requests in log)
   Each function takes `AuditEvent[]` and returns a `{ rate: number, count: number, total: number }`.

3. Add `cvf benchmark governance` subcommand to `command.registry.ts`:
   - flag: `--input <path>` (path to JSONL audit log)
   - flag: `--format json|table` (default: table)
   - reads JSONL line by line, parses, calls all 4 metric functions, outputs result

4. Add `BenchmarkGovernanceOptions` type to `types.ts`.

5. Create a sample audit JSONL fixture for tests (10–20 synthetic events
   with known receipt/step/policy values).

6. Write unit tests in `governance-reliability-metrics.test.ts`:
   - test each metric on the fixture
   - test edge: empty log → all rates 0
   - test edge: all receipts null → receiptIntegrityRate = 0

7. Run `cvf benchmark governance` against the best available real audit JSONL
   or release-gate evidence log to get the baseline. Synthetic fixtures are
   allowed for unit tests only. If no real audit log exists, the baseline
   document must say `baseline_deferred_no_real_audit_log` instead of presenting
   synthetic data as an operational baseline.

8. File `docs/benchmark/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md`
   recording: metric definitions, computation date, input source, result values.

9. File GC-018 baseline. File completion packet. Update GC-020.

## 9. Evidence Requirements

```powershell
Test-Path "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts"
Test-Path "docs/benchmark/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md"
rg -n "benchmark governance" EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts
npm test (CVF_ECO_v2.2_GOVERNANCE_CLI) — all pass including new tests
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

Evidence Trace Block required for each claim in completion packet.

## 10. Acceptance Criteria

- [ ] `governance-reliability-metrics.ts` exists with 4 metric functions
- [ ] `cvf benchmark governance --input <path>` command registered and functional
- [ ] All 4 metrics return `{ rate, count, total }` shape
- [ ] Unit tests pass for all 4 metrics including edge cases
- [ ] Baseline document filed in `docs/benchmark/` using a real audit/log source,
      or explicitly marked `baseline_deferred_no_real_audit_log`
- [ ] No existing QBS-1, W72/W91/W98 benchmark files modified
- [ ] No live provider call made
- [ ] GC-023 line limits respected
- [ ] Current governance pre-commit hook chain passes without bypassing hooks

## 11. Review Gate

Reviewer: Claude.

Reviewer checks:
- Metric formulas are correct against the audit event shape
- Baseline document cites the input source honestly; synthetic fixtures may
  prove unit behavior but must not be presented as the first operational baseline
- No existing benchmark files overwritten
- All acceptance criteria evidenced

## 12. Closure Checklist

- [ ] GC-018 filed and referenced
- [ ] All acceptance criteria PASS
- [ ] Evidence Trace Block present
- [ ] Current governance hook chain passes without bypassing hooks
- [ ] GC-020 handoff updated
- [ ] Public catalog: consider adding `cvf benchmark governance` to catalog
      capability table with `defined, offline-tested` status — verify path in
      public-sync before committing
- [ ] Reviewer disposition: NO_BLOCKING_FINDING or operator waiver

## 13. Return-To-Orchestrator Conditions

Stop and escalate if:

- `cvf benchmark governance` already exists in CLI — report, do not duplicate
- Existing benchmark files would be overwritten
- Live provider call is required to produce baseline data — use synthetic fixture instead
- Any governed file would exceed GC-023 line limit

## Claim Boundary

Lane E closes with: 4 governance reliability metrics defined, CLI subcommand
functional, baseline recorded — `defined, offline-tested`

Not claimed: live-run benchmark against production, hallucination recovery
metric, cross-session continuity metric (demand-gated for Lane E+1).
