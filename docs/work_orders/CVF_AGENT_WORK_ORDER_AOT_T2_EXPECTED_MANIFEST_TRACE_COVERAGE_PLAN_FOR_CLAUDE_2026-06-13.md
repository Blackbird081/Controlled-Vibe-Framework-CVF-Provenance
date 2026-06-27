# CVF Agent Work Order - AOT-T2 Expected Manifest Trace Coverage Plan For Claude

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-13

Owner: Codex

Worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_FOR_CLAUDE_2026-06-13.md`
- `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`
- `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

## Purpose

Dispatch a bounded Claude worker packet for AOT-T2 coverage planning. The
purpose is to define the next implementation-ready manifest and trace coverage
requirements before any checker, test, hook, runtime, provider, or OS-control
work is opened.

## Mission

Create a planning-only AOT-T2 coverage plan that defines the next useful
hardening step for CVF agent/provider supervision: expected-manifest and
co-work trace coverage. The output must explain what later implementation
should check, what evidence it should require, and what remains out of scope.

Claude must not implement the checker, tests, hooks, runtime, provider calls,
session sync, public-sync, OS audit tooling, endpoint monitoring, or external
application changes.

## Authority Chain

- Operator instruction: chat request on 2026-06-13: "next roadmap? tao work
  order cho claude".
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Decision authority: AOT-T1 closure and active next-allowed move.
- GC-018: `docs/baselines/CVF_GC018_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`.
- Canonical standard: `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`.
- Current checker: `governance/compat/check_agent_operation_trace.py`.
- Active handoff: `AGENT_HANDOFF_V18_2026-06-12.md`.

Authority boundary:

- This work order authorizes Claude to create only the two deliverables listed
  in Write Ownership.
- Codex owns review, allowed reviewer repairs, commit, and session sync.
- Any conflict between this work order and a canonical standard must return to
  Codex before implementation continues.

## Agent Roles

- Orchestrator / dispatcher: Codex.
- Implementer: Claude.
- Reviewer / committer: Codex.
- Escalation required for: scope expansion, checker/test/hook/runtime
  edits, OS audit or endpoint monitoring, public-sync, provider/API/live-proof,
  external app inspection or mutation, or any commit by Claude.

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_FOR_CLAUDE_2026-06-13.md`
- `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`
- `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

Reviewer conversion boundary: Claude worker return is not closure. Codex must
review the worker artifacts, add any reviewer-owned completion packet, commit
the accepted diff, run committed-range pre-closure, and perform session sync
before any closed-equivalent status is claimed.

## Scope

Allowed scope:

- read the source authority files listed in this work order;
- create `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`;
- create `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md`;
- Codex reviewer may update `docs/baselines/CVF_GC018_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`
  from dispatched status to closed status;
- Codex reviewer may create
  `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md`;
- Codex reviewer closure conversion may update this work order status, update
  the paired GC-018 status, add the completion review, apply reviewer-owned
  repairs inside the two worker artifacts, commit the accepted closure diff,
  and perform a separate session-sync commit after material closure;
- rank later implementation candidates for expected-manifest and trace coverage;
- identify collision risks and negative-search evidence;
- preserve the boundary that CVF supervises co-work agents by repo-local trace
  evidence and does not develop provider co-work platforms.

Forbidden scope:

- no changes to `governance/compat/`;
- no changes to `CVF_SESSION/`, `CVF_SESSION_MEMORY.md`, or
  `AGENT_HANDOFF*.md`;
- no changes to `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`;
- no changes to `AGENTS.md`, `CLAUDE.md`, or provider-local memory files;
- no runtime, source, test, hook, CI, public-sync, provider, browser, OS audit,
  endpoint-monitoring, file-watcher, destructive-broker, external
  Document_Translator, or Policy_Local work;
- no commit.

Risk ceiling:

- R1 documentation and planning only.

## Required First Reads

Before editing deliverables, Claude must read:

- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` - canonical AOT boundary and required trace block.
- `governance/compat/check_agent_operation_trace.py` - current checker behavior and protected prefixes.
- `governance/compat/test_check_agent_operation_trace.py` - current regression coverage.
- `governance/compat/run_local_governance_hook_chain.py` - current hook placement.
- `governance/compat/run_agent_autorun_workflow_gate.py` - current autorun placement.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` - active next allowed move and current mode.
- `docs/baselines/CVF_GC018_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` - dispatch baseline and boundaries.

## Pre-Flight Checks

Claude must capture and record these checks before writing deliverables:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md
Test-Path docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base ce369ab6 --head HEAD
```

Expected results:

- base HEAD is at or after `ce369ab6`;
- the two deliverable paths are absent before Claude writes them;
- pre-implementation gate passes or Claude records a blocking return.

If a pre-flight check fails, Claude must stop and return the failed command and
result to Codex. Claude must not continue past a failed autorun phase gate.

## Source-Fidelity Pass

Existing paths verified by Codex before dispatch:

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS current mode | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` | line 62 | `currentMode` | active session state source | ACCEPT |
| EXISTS AOT-T2 next allowed move | `CVF_SESSION/state/entries/agentOperationTraceFoundationClosure20260613.json` | line 28 | `nextAllowedMove` | active session state entry | ACCEPT |
| EXISTS AOT standard repo-local purpose | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 17 | repo-local evidence | AOT standard | ACCEPT |
| EXISTS co-work platform non-goal | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 20 | `codex_cowork` / `claude_cowork` | AOT standard | ACCEPT |
| EXISTS required trace block | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 64 | `Agent Operation Trace Block` | AOT standard | ACCEPT |
| EXISTS protected repo-local integrity surface | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 86 | protected repo-local integrity surface | AOT standard | ACCEPT |
| EXISTS checker path | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 105 | `governance/compat/check_agent_operation_trace.py` | AOT standard | ACCEPT |
| EXISTS claim boundary | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 123 | claim boundary | AOT standard | ACCEPT |
| EXISTS checker trace marker | `governance/compat/check_agent_operation_trace.py` | line 24 | `TRACE_MARKER` | checker module | ACCEPT |
| EXISTS checker required labels | `governance/compat/check_agent_operation_trace.py` | line 27 | `TRACE_REQUIRED_LABELS` | checker module | ACCEPT |
| EXISTS checker trace artifact prefixes | `governance/compat/check_agent_operation_trace.py` | line 42 | `TRACE_ARTIFACT_PREFIXES` | checker module | ACCEPT |
| EXISTS checker review triggers | `governance/compat/check_agent_operation_trace.py` | line 47 | `TRACE_REVIEW_TRIGGERS` | checker module | ACCEPT |
| EXISTS checker protected prefixes | `governance/compat/check_agent_operation_trace.py` | line 58 | `PROTECTED_REPO_PREFIXES` | checker module | ACCEPT |
| EXISTS protected delete or rename detector | `governance/compat/check_agent_operation_trace.py` | line 160 | `protected_delete_or_rename_paths` | checker module | ACCEPT |
| EXISTS trace violation evaluator | `governance/compat/check_agent_operation_trace.py` | line 170 | `find_trace_violations` | checker module | ACCEPT |
| EXISTS work-order missing-trace regression | `governance/compat/test_check_agent_operation_trace.py` | line 38 | `test_changed_work_order_without_trace_is_violation` | unittest module | ACCEPT |
| EXISTS complete-trace regression | `governance/compat/test_check_agent_operation_trace.py` | line 46 | `test_changed_work_order_with_complete_trace_passes` | unittest module | ACCEPT |
| EXISTS worker-trigger regression | `governance/compat/test_check_agent_operation_trace.py` | line 52 | `test_completion_review_with_worker_trigger_requires_trace` | unittest module | ACCEPT |
| EXISTS protected-delete regression | `governance/compat/test_check_agent_operation_trace.py` | line 70 | `test_protected_delete_requires_delete_or_rename_disposition` | unittest module | ACCEPT |
| EXISTS protected-delete disposition regression | `governance/compat/test_check_agent_operation_trace.py` | line 82 | `test_protected_delete_with_disposition_passes` | unittest module | ACCEPT |
| EXISTS local hook AOT gate placement | `governance/compat/run_local_governance_hook_chain.py` | line 50 | `agent operation trace integrity` | local hook chain | ACCEPT |
| EXISTS autorun AOT gate placement | `governance/compat/run_agent_autorun_workflow_gate.py` | line 79 | `agent operation trace integrity` | autorun gate | ACCEPT |

New doc-only planned paths:

| Planned path | Status | Owner |
|---|---|---|
| `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` | DOC_ONLY_NEW | Claude drafts; Codex reviews |
| `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md` | DOC_ONLY_NEW | Claude drafts; Codex reviews |

## Negative Search And Collision Discipline

- `expected-manifest` is an AOT-T2 planning label from active next-allowed
  state, not an existing runtime field.
- Exact search command used before dispatch:
  `rg -n "expected-manifest" .`
- Exact search roots covered by that command: repository root `.`, including
  source, tests, docs, JSON, scripts, active session state, and private
  reference paths visible to ripgrep.
- Collision result: same-token occurrences exist in older corpus-manifest
  drift-check scripts/docs and in FPC-T3 protected-path design notes. Those
  occurrences are non-authoritative for AOT-T2 runtime/schema behavior.
- Claude must not present expected-manifest as an implemented runtime schema,
  checker field, or provider platform feature.
- Same-token collisions, if found during worker search, must be recorded in the
  coverage plan with `ACCEPT`, `DEFER`, or `REJECT` disposition.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake item | AOT-T2 expected-manifest trace coverage plan |
| Scope classification | bounded documentation-only planning packet; changed paths limited to two Claude-owned docs |
| Risk sensitivity | R1 governance-control planning only |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Selected role route | Claude worker drafts; Codex reviewer/committer closes |
| routeMode | MULTI_AGENT_MULTI_ROLE |
| Routed role | Claude as worker |
| Reviewer | Codex |
| Commit authority | Codex only |
| Runtime/source authority | NONE |
| Live/provider authority | NONE |
| Public-sync authority | NONE |
| Escalation condition | Stop and return to Codex for scope expansion, forbidden paths, live/provider proof, public-sync, OS audit, endpoint monitoring, or commit request |
| Disposition | DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT |

## Single-Agent Multi-Role Control Block

| Field | Decision |
|---|---|
| Single agent owns implementation and review | NO |
| Role separation ledger | Claude owns worker drafting only; Codex owns review, commit, completion, and session sync |
| Self-review boundary | Independent review is not claimed from Claude; Claude must not close its own work |
| Gate sequence | pre-dispatch by Codex, pre-implementation by Claude, worker-return fast gate by Claude when possible, reviewer-fast and pre-closure by Codex |
| Escalation conditions | Stop for forbidden paths, claim-boundary changes, public-sync, live/provider work, OS audit, endpoint monitoring, destructive action, or commit request |
| Worker | Claude |
| Reviewer / committer | Codex |
| Human escalation checkpoint | Scope expansion only |
| Collusion boundary | Codex must review real diff and gates before any commit |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: dispatch this AOT-T2 documentation-only
work order and perform Codex-owned session-sync after dispatch. Claude is not
authorized to edit protected guard/session files.

Protected paths:

- `docs/baselines/CVF_GC018_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_FOR_CLAUDE_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/aotT2ExpectedManifestTraceCoveragePlanDispatch20260613.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

Operator authorization: the operator asked Codex to choose the next roadmap and
create a Claude work order after AOT-T1 closure.

Rollback boundary: revert only this AOT-T2 dispatch and session sync if
rejected. Do not revert AOT-T1 material commit `41977f58`, AOT-T1 session sync
`f4aebdb8`, or AOT-T1 authorization repair `ce369ab6`.

## Write Ownership

Owned files:

- `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`
- `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md`

Forbidden paths:

- `governance/compat/**`
- `CVF_SESSION/**`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF*.md`
- `AGENTS.md`
- `CLAUDE.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `.github/**`
- `EXTENSIONS/**`
- public-sync clone
- external Document Translator repo
- external Policy_Local repo

Write mode:

- create-only for the two owned files.

Any file outside ownership requires return to Codex.

## Execution Plan

1. Read all required first-read files.
2. Run pre-flight checks and record results in the worker return.
3. Create the AOT-T2 coverage plan with these required sections:
   - Purpose;
   - Source Authority;
   - Current AOT-T1 Capability Map;
   - Expected Manifest Design Boundary;
   - Co-Work Trace Coverage Matrix;
   - Protected Path And Delete/Rename Coverage;
   - Negative Search And Collision Discipline;
   - Candidate Ranking;
   - Recommended First Implementation Tranche;
   - Claim Boundary;
   - Public Export Disposition.
4. Create the worker-return packet with:
   - deliverables list;
   - file-change list;
   - Worker Pending-Return Gate table;
   - Agent Operation Trace Block;
   - Negative Search And Collision Discipline;
   - Return-To-Orchestrator Conditions;
   - Claim Boundary.
5. Run the worker-return fast gate if possible:

```powershell
python governance/compat/run_worker_return_fast_gate.py
```

If the fast gate fails only because final commit/session closure is Codex-owned,
record a pending-finality result with the failing command. Other allowed-scope
failures must be repaired before return.

## Design Control Carry-Forward

| Design control | Source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | AOT standard and active next allowed move | Planning-only coverage; no checker/runtime edits | PASS |
| Non-goals | AOT standard claim boundary | OS audit, endpoint monitoring, provider features, and public-sync forbidden | PASS |
| Lane split | AOT-T1 closure state | Executes AOT-T2 planning only | PASS |
| Dependency/source-verification plan | Source-Fidelity Pass in this work order | Exact current paths and symbols verified before dispatch | PASS |
| Claim boundary | AOT standard Claim Boundary | Repo-local trace only; no OS/user attribution | PASS |
| Acceptance criteria | This work order | Observable deliverables and worker return evidence | PASS |
| Verification/evidence | This work order | Pre-flight, worker-return fast gate, Codex reviewer gates | PASS |
| Dispatch-readiness decision | GC-018 and this work order | Ready for Claude under WORKER_MUST_NOT_COMMIT | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex CLI |
| Session or invocation | dispatch range starts at `ce369ab6`; material dispatch commit `e69ea3ca`; closure base `9581a2e3` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`, `Test-Path`, `apply_patch`, governance gates |
| Target paths | GC-018, this work order, planned Claude deliverables |
| Allowed scope source | Operator request on 2026-06-13, active state nextAllowedMove, AOT-T1 closure |
| Before status evidence | `git status --short` clean before dispatch authoring |
| After status evidence | To be recorded by Codex after dispatch commit |
| Diff evidence | `git diff --name-status` before commit; committed range after Codex commit |
| Approval boundary | Operator asked Codex to choose next roadmap and create Claude work order |
| Claim boundary | Repo-local trace only; no OS/user attribution, endpoint telemetry, provider-internal logs, or physical-machine identity |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Evidence Requirements

Required worker evidence:

- pre-flight command results;
- exact changed files;
- complete Agent Operation Trace Block in both deliverables;
- coverage plan section checklist;
- negative search and collision results;
- worker-return fast gate result or explicit pending-finality explanation.

Base-anchor evidence:

- `dispatchBaseHead`: `ce369ab6`
- `executionBaseHead`: worker must record actual HEAD before edits
- `closureBaseHead`: `9581a2e3` - Codex reviewer owns closure
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Worker-return fast gate: required when possible
- Committed-range pre-closure: Codex-owned after review and commit

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Coverage plan exists | `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` |
| Worker return exists | `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md` |
| Current AOT-T1 behavior mapped | Source-backed map of standard, checker, tests, and hook placement |
| Expected-manifest design bounded | Clear doc-only design boundary; no runtime/schema/checker claim |
| Co-work trace coverage included | Matrix for current repo-local supervision of co-work agent work |
| Next implementation tranche recommended | Ranked candidate list with first tranche and deferred items |
| Forbidden scope preserved | No modified files outside Write Ownership |
| Worker return complete | Worker Pending-Return Gate and Agent Operation Trace Block present |

Fail conditions:

| Fail condition | Return action |
|---|---|
| Claude edits forbidden paths | Stop and return to Codex |
| Claude commits | Stop; Codex must inspect and correct repository state |
| Coverage plan claims OS/user attribution or endpoint telemetry | Stop and correct claim boundary |
| Coverage plan presents expected-manifest as existing runtime field | Stop and correct source-fidelity defect |
| Worker-return fast gate fails for allowed-scope reasons | Repair and rerun before return |
| Source facts are unverified or invented | Return to Codex with a source blocker disposition |

## Review Gate

Implementation may proceed only after this dispatch work order and GC-018 are
committed by Codex and the dispatch gates pass.

Closure may proceed only after Codex reviews Claude's uncommitted worker return,
runs reviewer-fast or worker-return fast gate, applies allowed repairs if
needed, commits reviewed deliverables, and runs committed-range pre-closure.

Claude must return without committing.

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within the
Allowed scope and Write Ownership must be repaired and rerun by Claude before
return. Routine allowed-scope fixes are mandatory, including missing
`N/A with reason`, missing trace rows, formatting required by a gate, or
source-verification wording.

Claude must stop and return to Codex only when repair would exceed Allowed
scope, change the claim boundary, require forbidden paths, open public-sync, run
live/provider proof, consume secrets/quota, configure OS audit or endpoint
monitoring, perform destructive action, or require a commit.

## Worker Pending-Return Gate

| Gate | Expected result |
|---|---|
| Required first reads completed | PASS |
| Pre-flight base HEAD recorded | PASS |
| Pre-flight status recorded | PASS |
| Coverage plan created | PASS |
| Worker return created | PASS |
| Source Authority section present | PASS |
| Current AOT-T1 Capability Map present | PASS |
| Expected Manifest Design Boundary present | PASS |
| Co-Work Trace Coverage Matrix present | PASS |
| Negative Search And Collision Discipline present | PASS |
| Candidate Ranking present | PASS |
| Agent Operation Trace Block complete | PASS |
| Forbidden paths untouched | PASS |
| Worker-return fast gate recorded | PASS or pending-finality explanation with reason |

## Closure Checklist

| Closure item | Owner | Required disposition |
|---|---|---|
| Claude deliverables reviewed | Codex | Required before commit |
| Worker-return fast gate result recorded | Claude | PASS or justified pending-finality result |
| Reviewer-fast gate run | Codex | Required before material commit |
| Committed-range pre-closure run | Codex | Required after material commit |
| Completion review filed | Codex | Required for closure |
| Session state/front door/handoff sync | Codex | Required if mode or next allowed move changes |
| Public catalog disposition | Codex | Not applicable unless public-sync is separately authorized |

## Operator Checkpoint

Operator checkpoint is required only if Claude or Codex needs to expand beyond
documentation-only AOT-T2 planning, touch forbidden paths, run provider/live
proof, open public-sync, inspect or mutate external applications, configure
OS/endpoint monitoring, or change the claim boundary.

## Return-To-Orchestrator Conditions

Return to Codex without continuing if:

- any required source file is missing;
- pre-flight gate fails outside allowed-scope repair;
- planned deliverable paths already exist with unrelated content;
- a required source fact cannot be verified;
- implementation would require checker/test/hook/runtime/session/public-sync or
  external app edits;
- Claude cannot preserve `WORKER_MUST_NOT_COMMIT`.

## Claim Boundary

This work order dispatches documentation-only AOT-T2 coverage planning. It does
not authorize checker implementation, runtime behavior, provider behavior,
OS-level identity proof, endpoint telemetry, public readiness, production
readiness, live governance proof, public-sync, or autonomous mutation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| GC-018 status | `docs/baselines/CVF_GC018_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED`; `closureBaseHead: 9581a2e3` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason | AOT-T2 is a next-allowed-move planning tranche, not a parent-roadmap status conversion | N/A with reason |
| Coverage plan | `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md` | C01-C04 ranking and Agent Operation Trace Block present | PASS |
| Worker return | `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_WORKER_RETURN_2026-06-13.md` | worker disposition and gate evidence present | PASS |
| Registry JSON | BLOCKED with reason | no governed runtime/source/test owner surface changed; registry mutation not authorized by AOT-T2 planning closure | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no corpus registry Markdown owner change was authorized by AOT-T2 planning closure | BLOCKED with reason |
| System loop interlock | N/A with reason | AOT-T2 is trace planning only and did not change the system-loop interlock registry | N/A with reason |
| External evidence digest | N/A with reason | no external source tree, provider/API/live proof, OS audit, or retained external artifact was used | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V18_2026-06-12.md` | separate session-sync commit after material closure | PASS |
| Public export | this file and closure artifacts | `DEFERRED_PRIVATE_ONLY` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control dispatch. Public-sync is not
authorized.

rawMemoryReleased=false
