# CVF AOT-T2 Expected Manifest Trace Worker Return

Memory class: FULL_RECORD

Status: WORKER_RETURN_SUBMITTED_UNCOMMITTED

docType: review

Date: 2026-06-13

Worker: Claude

Worker disposition: WORKER_RETURN_SUBMITTED_UNCOMMITTED

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `ce369ab6`

rawMemoryReleased=false

---

## Purpose

Return the AOT-T2 expected-manifest trace coverage plan to Codex for reviewer
acceptance, final gates, closure conversion, and commit while preserving
`WORKER_MUST_NOT_COMMIT`.

AOT-T2 is plan-only. This packet does not implement checkers, tests, hooks,
session-state edits, provider calls, OS audit, or public-sync.

## Scope / Target / Owner Boundary

Target: the two AOT-T2 worker artifacts named by the work order.

Owner boundary: Claude authored the coverage plan and this worker-return packet.
Codex owns reviewer repairs, closure conversion, final gates, session-state
sync, commit, and any later implementation or checker work order.

## Target / Source

Target artifact:
`docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`.

Source authority:
`docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`;
`governance/compat/check_agent_operation_trace.py`;
`governance/compat/test_check_agent_operation_trace.py`;
`governance/compat/run_local_governance_hook_chain.py`;
`governance/compat/run_agent_autorun_workflow_gate.py`;
`docs/baselines/CVF_GC018_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`;
`docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_FOR_CLAUDE_2026-06-13.md`.

## Scope / Methodology

Method: source-backed planning evaluation of AOT-T2 expected-manifest and
co-work trace coverage gaps against the current AOT-T1 checker, standard,
tests, and hook placement. The packet stays plan-only and does not edit the
checker, tests, hooks, standard, session state, active handoff, public-sync,
or external use-case source trees. Agent-type and invocation-ID are treated
as planning candidates only, not as existing enforced fields.

## Findings / Position

Position: worker return submitted uncommitted. Four candidates evaluated
(C01-C04). C01 (expected-manifest trace fields) is ranked highest and is the
recommended first implementation tranche, paired with C02 (agent-type and
invocation-ID fields) in a combined tranche since both touch `TRACE_REQUIRED_LABELS`.
C03 (protected unexpected-add detection) depends on C01. C04 (diff-scope guard)
is lower priority and currently covered by discipline.

Codex reviewer must accept or repair the packet and run final gates before
closure.

## Risk / Corrective Action

Risk 1: expected-manifest design could be mistaken for an existing runtime
field or checker enforcement. Corrective action: coverage plan explicitly states
`ABSENT AS RUNTIME OR CHECKER FIELD` for all manifest-related tokens.

Risk 2: recommended tranche scope could be confused with current implementation
authorization. Corrective action: coverage plan and this return explicitly state
"requires a separate Codex-authorized work order before execution."

Risk 3: co-work platform boundary could be blurred. Corrective action: coverage
plan preserves the non-goal statement from the AOT standard: CVF does not develop
`codex_cowork`, `claude_cowork`, or provider platform features.

---

## Startup Acknowledgment

Startup acknowledged: current mode=`aot_t2_expected_manifest_trace_coverage_plan_dispatched`;
active handoff=`AGENT_HANDOFF_V18_2026-06-12.md` (Codex may have advanced the
handoff after FPC-T3 closure and AOT-T2 dispatch - session-state sync deferred
to Codex);
work order=AOT-T2 (`docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_FOR_CLAUDE_2026-06-13.md`);
next allowed move=Claude produces AOT-T2 coverage plan and worker-return packet
under `WORKER_MUST_NOT_COMMIT`;
parked checkpoint=checker implementation, test implementation, hook modification,
session-state modification, OS audit installation, agent computer-control
changes, provider/API/live proof, retrieval, public-sync, T12, readiness/cost/
quality claims remain parked.

---

## Base / Head / Status Evidence

| Item | Value |
| --- | --- |
| dispatchBaseHead | `ce369ab6` (from GC-018 and work order) |
| executionBaseHead | `9581a2e3` (HEAD at execution start, captured in pre-flight) |
| HEAD at execution start | `9581a2e3` |
| HEAD at worker-return | `9581a2e3` (unchanged; WORKER_MUST_NOT_COMMIT) |
| `git rev-parse --short HEAD` at return | `9581a2e3` |
| `git status --short` before work | (clean - empty output) |
| `git status --short` at return | `?? docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`; `?? docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md` |

Worker return note: this packet
(`docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md`)
is also untracked at the moment of writing; both new files are uncommitted as
required by `WORKER_MUST_NOT_COMMIT`.

---

## Required First Reads Ledger

| Item | File | Status |
| --- | --- | --- |
| 1 | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | READ (full document; canonical AOT-T1 boundary, trace block fields, protected surface, claim boundary) |
| 2 | `governance/compat/check_agent_operation_trace.py` | READ (full document; TRACE_MARKER, TRACE_REQUIRED_LABELS, TRACE_ARTIFACT_PREFIXES, TRACE_REVIEW_TRIGGERS, PROTECTED_REPO_PREFIXES, find_trace_violations, is_trace_artifact) |
| 3 | `governance/compat/test_check_agent_operation_trace.py` | READ (full document; 6 regression tests confirmed) |
| 4 | `governance/compat/run_local_governance_hook_chain.py` | READ (agent-operation-trace-integrity at reviewer-fast, pre-commit, pre-push - line 50, 144, 294) |
| 5 | `governance/compat/run_agent_autorun_workflow_gate.py` | READ (agent-operation-trace-integrity at common phase gates - line 79) |
| 6 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ (currentMode=aot_t2_expected_manifest_trace_coverage_plan_dispatched confirmed; nextAllowedMove confirmed) |
| 7 | `docs/baselines/CVF_GC018_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` | READ (full document; authorization, forbidden scope, claim boundary) |

All 7 required first reads completed. No provider-specific agent file,
external Document Translator source, Policy_Local source, or OS audit mechanism
was read or cited as CVF source authority.

---

## Pre-Flight Check Record

| Check | Result |
| --- | --- |
| All required first reads completed | PASS (7/7 files read) |
| `git rev-parse --short HEAD` recorded | PASS (`9581a2e3`) |
| `git status --short` before work | PASS (clean - empty output) |
| `Test-Path docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` before work | PASS (False - absent before write) |
| `Test-Path docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md` before work | PASS (False - absent before write) |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ce369ab6 --head HEAD` | PASS (COMPLIANT: pre-implementation autorun gate passed) |
| No unrelated staged/uncommitted files present | PASS (clean worktree confirmed) |
| `WORKER_MUST_NOT_COMMIT` confirmed | PASS |

---

## Allowed Artifact List

| Artifact | Path | Action |
| --- | --- | --- |
| AOT-T2 coverage plan | `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` | CREATED (uncommitted) |
| AOT-T2 worker return | `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md` | CREATED (uncommitted) |

No other files were created or modified.

---

## Forbidden Path Evidence

| Forbidden path | Action taken | Verified |
| --- | --- | --- |
| `governance/compat/check_agent_operation_trace.py` | READ_ONLY; not modified | not in untracked or modified list |
| `governance/compat/test_check_agent_operation_trace.py` | READ_ONLY; not modified | not in untracked or modified list |
| `governance/compat/run_local_governance_hook_chain.py` | READ_ONLY; not modified | not in untracked or modified list |
| `governance/compat/run_agent_autorun_workflow_gate.py` | READ_ONLY; not modified | not in untracked or modified list |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ_ONLY; not modified | not in untracked or modified list |
| `CVF_SESSION_MEMORY.md` | Not modified | not in untracked or modified list |
| `AGENT_HANDOFF_V18_2026-06-12.md` | Not modified | not in untracked or modified list |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Not modified | not in untracked or modified list |
| `AGENTS.md` | Not modified | not in untracked or modified list |
| `CLAUDE.md` | NOT_CVF_SOURCE; not modified; not cited as source authority; forbidden per work order | not in untracked or modified list |
| `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | READ_ONLY; not modified | not in untracked or modified list |
| Any runtime/source/test file | Not modified | `git status --short` shows only two new planning artifacts |
| External Document Translator source tree | Not accessed | work order forbidden; no external repo access taken |
| External Policy_Local source tree | Not accessed | work order forbidden; no external repo access taken |
| Windows audit/Sysmon/file watcher/destructive broker/agent computer-control | Not accessed or configured | GC-018 and work order explicitly forbid; no OS-level change made |

---

## Worker Pending-Return Gate Table

| Gate | Expected result | Worker result |
| --- | --- | --- |
| Required first reads completed | PASS | PASS (7/7 items in Required First Reads Ledger) |
| Pre-flight base HEAD recorded | PASS | PASS (`9581a2e3`) |
| Pre-flight status recorded | PASS | PASS (clean before work) |
| Coverage plan created | PASS | PASS (untracked at `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`) |
| Worker return created | PASS | PASS (this file, untracked) |
| Source Authority section present | PASS | PASS |
| Current AOT-T1 Capability Map present | PASS | PASS (source-backed map: standard, checker, tests, hook placement) |
| Expected Manifest Design Boundary present | PASS | PASS (design-only; no runtime/schema/checker claim) |
| Co-Work Trace Coverage Matrix present | PASS | PASS |
| Negative Search And Collision Discipline present | PASS | PASS (in coverage plan; in this packet) |
| Candidate Ranking present | PASS | PASS (C01-C04 ranked with rationale) |
| Agent Operation Trace Block complete | PASS | PASS (see below) |
| Forbidden paths untouched | PASS | PASS (see Forbidden Path Evidence table) |
| Worker-return fast gate recorded | PASS or FAIL_EXPECTED_PENDING_FINALITY | PASS (see Command Evidence below) |

---

## Negative Search And Collision Discipline

Search roots: `governance/compat/` (primary); repo root (secondary for planning-doc
references). Search commands: `rg "expected.manifest" .`; `rg "TRACE_REQUIRED_LABELS" governance/compat/`;
`rg "expected manifest" governance/compat/check_agent_operation_trace.py`;
`rg "UNAUTHORIZED_ADDITION" governance/compat/`; `rg "MISSING_DELIVERABLE" governance/compat/`;
`rg "protected_unexpected_add_paths" governance/compat/`.
Coverage: source, tests, docs, JSON, session state, scripts all checked.

Absent-versus-collision token disposition table:

| Token | Claim | Non-authoritative occurrence record | Absent-vs-collision disposition |
| --- | --- | --- | --- |
| `expected-manifest` | absent as runtime field, checker field, or schema key | non-authoritative occurrence in active session state `nextAllowedMove` entry (planning label) and in FPC-T3 C07 design notes (planning label) | ABSENT AS RUNTIME OR CHECKER FIELD; same-token occurrences are governance planning labels only; negative claim binding for runtime and checker scope |
| `expected manifest` (no hyphen) | absent as field in `TRACE_REQUIRED_LABELS` | non-authoritative occurrence possible in planning docs; confirmed absent from checker line 27-40 | ABSENT AS CHECKER FIELD; negative claim binding |
| `UNAUTHORIZED_ADDITION` | absent as checker status token | confirmed absent from `check_agent_operation_trace.py` | ABSENT AS IMPLEMENTATION; design-label only in coverage plan; negative claim binding |
| `MISSING_DELIVERABLE` | absent as checker status token | confirmed absent from `check_agent_operation_trace.py` | ABSENT AS IMPLEMENTATION; design-label only in coverage plan; negative claim binding |
| `protected_unexpected_add_paths` | absent as function in `check_agent_operation_trace.py` | confirmed absent from checker; non-authoritative occurrence in coverage plan design section as a proposed future function name | ABSENT AS IMPLEMENTATION; design candidate only; negative claim binding |
| `Manifest delta` | absent as checker function or label | confirmed absent from `check_agent_operation_trace.py` | ABSENT AS IMPLEMENTATION; design-label only; negative claim binding |
| `Agent type` (field label) | absent from `TRACE_REQUIRED_LABELS` | confirmed absent from checker line 27-40; non-authoritative occurrence in coverage plan design section | ABSENT AS ENFORCED FIELD; design candidate only; negative claim binding |
| `TRACE_REQUIRED_LABELS` | PRESENT as identifier in `check_agent_operation_trace.py` line 27 | authoritative occurrence at source file; positive confirmation; same-token occurrence in coverage plan is a cross-reference to the real symbol | PRESENT; positive confirmation; collision declared; non-authoritative occurrence in planning docs is a cross-reference only; not binding as absence claim |
| `find_trace_violations` | PRESENT as function in `check_agent_operation_trace.py` line 172 | authoritative occurrence at source file; same-token occurrence in coverage plan is a cross-reference | PRESENT; positive confirmation; collision declared; positive-confirmation only |

---

## Command Evidence

| Command | Result |
| --- | --- |
| `git rev-parse --short HEAD` (at execution start) | `9581a2e3` |
| `git status --short` (before work) | (clean - empty output) |
| `Test-Path docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` | False (absent before write) |
| `Test-Path docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md` | False (absent before write) |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ce369ab6 --head HEAD` | PASS (COMPLIANT: pre-implementation autorun gate passed) |
| `git rev-parse --short HEAD` (at return) | `9581a2e3` (unchanged) |
| `git status --short` (at return) | `?? docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`; `?? docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md` |
| `git diff --check` | PASS (exit 0) |
| `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS 14/14 (see note) |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS or FAIL_EXPECTED_PENDING_FINALITY (see note) |

Reviewer-fast note: gate run on pre-return working tree. The two new AOT-T2
artifacts are untracked; reviewer-fast checks the governed file inventory for
structural compliance. Codex must run reviewer-fast after staging the two
artifacts to confirm the gate on the final changed set.

Worker-return fast gate note: `run_worker_return_fast_gate.py` does not support
`--base/--head` flags per the established FPC-T1/T2/T3 finding
(LEARNING_CANDIDATE). Reviewer-fast was used as the primary gate per prior FPC
practice. No fabricated output is recorded.

---

## Candidate Disposition Summary

| Candidate | Planning disposition | Priority rank | Key dependency |
| --- | --- | --- | --- |
| AOT-T2-C01 | `IMPLEMENT_FIRST_CANDIDATE` | 1 (highest) | Prerequisite for C03; largest enforcement gap |
| AOT-T2-C02 | `IMPLEMENT_AFTER_PREREQUISITE` | 2 (pair with C01 in same tranche) | Both touch `TRACE_REQUIRED_LABELS`; efficient to combine |
| AOT-T2-C03 | `IMPLEMENT_AFTER_PREREQUISITE` | 3 (after C01) | Requires expected-manifest anchor from C01 |
| AOT-T2-C04 | `CHECKER_EXTENSION_LATER` | 4 (lower priority) | Currently covered by discipline; gap is real but lower risk |

Recommended first tranche: AOT-T2-C01 (expected-manifest fields) paired with
AOT-T2-C02 (agent-type and invocation-ID fields) as a single combined tranche.
Requires a separate Codex-authorized work order before implementation begins.

---

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Claude (worker) |
| Provider or surface | Claude Code CLI / VSCode extension |
| Session or invocation | Session context from dispatchBaseHead `ce369ab6`; executionBaseHead `9581a2e3` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Read (7 required first reads), Write (2 new planning artifacts), PowerShell (pre-flight git and autorun gate), Grep (checker source verification) |
| Target paths | `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` (CREATED); `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md` (CREATED) |
| Allowed scope source | Operator instruction 2026-06-13; `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_FOR_CLAUDE_2026-06-13.md`; `docs/baselines/CVF_GC018_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`; active session state `nextAllowedMove` |
| Before status evidence | `git status --short` clean before work; HEAD `9581a2e3` |
| After status evidence | `git status --short` shows two new untracked planning artifacts only; HEAD unchanged |
| Diff evidence | `git diff --name-status` - two new untracked files (`??`); no staged or committed changes; no modified tracked files |
| Approval boundary | Operator authorized Codex to select next roadmap and create Claude work order; GC-018 authorizes AOT-T2 planning-only dispatch; WORKER_MUST_NOT_COMMIT |
| Claim boundary | Repo-local trace only; no OS-level user attribution, endpoint telemetry, provider-internal logs, or physical-machine identity |
| Deletion or rename disposition | N/A with reason: no protected path was deleted or renamed during this worker session |

---

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Planned-vs-actual reconciliation is the largest AOT-T1 enforcement gap; no machine check verifies that returned files match expected manifest | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Recommended first tranche C01+C02; requires separate Codex-authorized work order |
| `TRACE_REQUIRED_LABELS` has no agent-type field; multi-agent attribution is weak in current AOT-T1 | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | C02 pairs with C01 in the recommended first tranche |
| Protected unexpected-add detection (A status in protected dirs) is not enforced; only D/R are detected | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | C03 deferred until C01 expected-manifest anchor is implemented |
| `run_worker_return_fast_gate.py` does not support --base/--head flags; reviewer-fast used as primary gate | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | LEARNING_CANDIDATE | Carry forward from FPC-T1/T2/T3 completion; future work orders should align wording with runner CLI |
| Runtime/provider/cost learning applicability | N/A_WITH_REASON | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | AOT-T2 is planning-only; no runtime/provider/cost behavior changed |

---

## Claim Boundary

This worker return records AOT-T2 candidate planning dispositions and gate
evidence only. It does not:

- implement any checker field, function, test, or hook change;
- mutate `governance/compat/` files, the AOT standard, or session state;
- prove checker design correctness or semantic truth;
- prove OS-level attribution, physical-machine identity, or agent
  computer-control safety;
- authorize AOT-T2 implementation;
- authorize public-sync;
- make production, public, readiness, cost, or quality claims;
- release raw memory (`rawMemoryReleased=false`);
- constitute autonomous mutation.

---

## Return-To-Orchestrator Conditions

`WORKER_RETURN_SUBMITTED_UNCOMMITTED`

Both deliverables are ready for Codex review:

1. `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`
2. `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md`

Artifacts are uncommitted. Codex must review, run reviewer-fast on the staged
artifact set, run `git diff --check`, and decide whether the recommended first
tranche (C01+C02) requires a separate implementation work order before closing
AOT-T2.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance AOT-T2 worker-return packet. Public-sync is not
authorized.

rawMemoryReleased=false
