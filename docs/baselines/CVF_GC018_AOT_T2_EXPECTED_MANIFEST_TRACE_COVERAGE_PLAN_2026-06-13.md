# CVF GC-018 - AOT-T2 Expected Manifest Trace Coverage Plan

Memory class: POINTER_RECORD

Status: DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT

docType: gc018_baseline

Date: 2026-06-13

Owner: Codex

rawMemoryReleased=false

## Purpose

Authorize a bounded Claude work order for the next Agent Operation Trace
hardening step: design the AOT-T2 expected-manifest and co-work trace coverage
plan.

This tranche is selected because it directly extends the closed Agent Operation
Trace foundation without asking CVF to develop `codex_cowork`,
`claude_cowork`, provider platform features, operating-system audit tooling, or
endpoint monitoring.

## Scope / Target / Owner Boundary

Target: create a planning-only coverage artifact that defines how CVF should
strengthen repo-local operation trace evidence for co-work agent execution.

Allowed scope:

- inspect the existing AOT standard, checker, tests, hook wiring, active state,
  and AOT-T1 completion artifacts;
- create a reference coverage plan under `docs/reference/`;
- create a worker-return packet under `docs/reviews/`;
- recommend later implementation candidates without editing runtime, checker,
  hook, session, public-sync, provider, or external app files.

Forbidden scope:

- no checker implementation;
- no test implementation;
- no hook or autorun modification;
- no session-state or handoff modification by Claude;
- no OS audit, Sysmon, endpoint monitoring, file watcher service, destructive
  broker, or agent computer-control permission change;
- no provider/API/live-proof work;
- no public-sync;
- no external Document Translator or Policy_Local inspection or mutation.

## Decision / Baseline / Proposed Tranche

Decision: dispatch AOT-T2 as a planning and coverage tranche for Claude under
`WORKER_MUST_NOT_COMMIT`.

Proposed tranche:

`AOT-T2 - Expected Manifest Trace Coverage Plan`

Required worker deliverables:

- `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`
- `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md`

## Source Authority

| Source | Authority use | Disposition |
|---|---|---|
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Active current mode and next allowed move include AOT-T2 deeper expected-manifest/trace hardening. | ACCEPT |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | Canonical AOT-T1 standard and claim boundary. | ACCEPT |
| `governance/compat/check_agent_operation_trace.py` | Current checker behavior, protected surface, trace labels, and enforcement limits. | ACCEPT |
| `governance/compat/test_check_agent_operation_trace.py` | Current regression coverage. | ACCEPT |
| `governance/compat/run_local_governance_hook_chain.py` | Current hook placement evidence. | ACCEPT |
| `governance/compat/run_agent_autorun_workflow_gate.py` | Current autorun placement evidence. | ACCEPT |

## Evidence / Verification

Source-fidelity evidence captured by Codex before dispatch:

- `git rev-parse --short HEAD` -> `ce369ab6`;
- `Test-Path` confirmed the two planned Claude deliverables did not already
  exist before dispatch;
- `rg -n "Agent Operation Trace Block|Protected Repo-Local Integrity Surface|Machine checker|Claim Boundary|codex_cowork|repo-local" docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`;
- `rg -n "TRACE_MARKER|TRACE_REQUIRED_LABELS|PROTECTED_REPO_PREFIXES|protected_delete_or_rename_paths|find_trace_violations|TRACE_REVIEW_TRIGGERS|TRACE_ARTIFACT_PREFIXES" governance/compat/check_agent_operation_trace.py`;
- `rg -n "test_changed_work_order|test_completion_review|test_protected_delete" governance/compat/test_check_agent_operation_trace.py`;
- `rg -n "agent operation trace integrity|check_agent_operation_trace" governance/compat/run_local_governance_hook_chain.py governance/compat/run_agent_autorun_workflow_gate.py`;
- `python governance/compat/check_active_session_state.py --enforce` PASS before dispatch.

## Claim Boundary

This GC-018 authorizes planning-only AOT-T2 coverage work. It does not prove or
authorize checker implementation, runtime behavior, provider behavior,
OS-level attribution, endpoint telemetry, physical machine identity, public
readiness, production readiness, live governance proof, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control planning packet. Public-sync is
not authorized by this dispatch.

rawMemoryReleased=false
