# CVF GC-018 - AOT-T2-C01-C02 Manifest Trace Implementation

Memory class: POINTER_RECORD

Status: DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT

docType: gc018_baseline

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `6ca6a748`

rawMemoryReleased=false

## Purpose

Authorize a bounded Claude implementation work order for the highest-value
AOT-T2 follow-up: expected-manifest trace enforcement, agent-type /
invocation-ID trace labels, and narrow worker-authored `docs/reference/`
trace eligibility.

This tranche converts the AOT-T2 planning finding into a machine-check update
without asking CVF to develop `codex_cowork`, `claude_cowork`, provider
platform features, operating-system audit tooling, endpoint monitoring, or
agent computer-control surfaces.

## Scope / Target / Owner Boundary

Target owner surfaces:

- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`;
- `governance/compat/check_agent_operation_trace.py`;
- `governance/compat/test_check_agent_operation_trace.py`;
- `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_WORKER_RETURN_2026-06-13.md`.

Allowed implementation:

- add required trace labels for `Agent type`, `Invocation ID`,
  `Expected manifest`, `Actual changed set`, and `Manifest delta`;
- implement manifest set comparison against the actual repo-local changed set;
- require trace blocks for worker-authored `docs/reference/` deliverables only
  when worker/execution triggers are present;
- update the AOT standard to document the new labels and claim boundary;
- add deterministic regression tests.

Forbidden scope:

- no hook-chain wiring changes unless the existing checker invocation cannot
  cover the new behavior;
- no session-state or handoff mutation by Claude;
- no runtime/product source mutation outside the checker/test/standard owner
  surfaces;
- no public-sync;
- no external Document Translator or Policy_Local inspection or mutation;
- no OS audit, Sysmon, endpoint monitoring, file watcher service, destructive
  broker, or agent computer-control permission change;
- no provider/API/live-proof work;
- no commit.

## Decision / Baseline / Proposed Tranche

Decision: dispatch AOT-T2-C01+C02 implementation to Claude under
`WORKER_MUST_NOT_COMMIT`.

Proposed tranche:

`AOT-T2-C01+C02 - Manifest Trace And Co-Work Attribution Enforcement`

Required worker return:

- `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_WORKER_RETURN_2026-06-13.md`

Planned Codex completion review:

- `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_COMPLETION_2026-06-13.md`

## Source Authority

| Source | Authority use | Disposition |
| --- | --- | --- |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Current mode and next allowed move authorize fresh AOT-T2-C01+C02 work order. | ACCEPT |
| `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` | Planning matrix and recommended C01+C02 tranche. | ACCEPT |
| `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md` | Codex closure finding that coverage plan lacked trace block and C01+C02 is next. | ACCEPT |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Canonical AOT-T1 standard and claim boundary. | ACCEPT |
| `governance/compat/check_agent_operation_trace.py` | Current checker behavior and implementation owner surface. | ACCEPT |
| `governance/compat/test_check_agent_operation_trace.py` | Current deterministic regression owner surface. | ACCEPT |

## Evidence / Verification

Codex pre-dispatch evidence:

- `git rev-parse --short HEAD` -> `6ca6a748`;
- pre-authoring workspace status check returned no output;
- pending dispatch `git status --short` includes:
  - `?? docs/baselines/CVF_GC018_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_2026-06-13.md`;
  - `?? docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_FOR_CLAUDE_2026-06-13.md`;
- planned GC-018 and work-order paths did not exist before this dispatch;
- current checker has `TRACE_ARTIFACT_PREFIXES` at line 42 and does not include
  `docs/reference/` as a trace artifact prefix;
- current checker has `TRACE_REQUIRED_LABELS` at line 27 and does not include
  `Agent type`, `Invocation ID`, `Expected manifest`, `Actual changed set`, or
  `Manifest delta`;
- current protected surface includes `docs/reference/` in
  `PROTECTED_REPO_PREFIXES` at line 58;
- AOT-T2 completion records the coverage-plan missing trace-block repair at
  lines 85 and 101.

## Claim Boundary

This GC-018 authorizes a repo-local checker/standard/test implementation only.
It does not prove or authorize OS-level attribution, endpoint telemetry,
physical machine identity, provider-internal logs, runtime behavior,
production readiness, public readiness, public-sync, live governance proof, or
autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control implementation dispatch.
Public-sync is not authorized by this tranche.

rawMemoryReleased=false
