# CVF Agent Work Order - AOT-T2-C01-C02 Manifest Trace Implementation For Claude

Memory class: POINTER_RECORD

Status: DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT

docType: work_order

Date: 2026-06-13

Owner: Codex

Worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `6ca6a748`

executionBaseHead: `6ca6a748`

closureBaseHead: `6ca6a748`

rawMemoryReleased=false

completionReviewPath:
`docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/baselines/CVF_GC018_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_FOR_CLAUDE_2026-06-13.md`
- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- `governance/compat/check_agent_operation_trace.py`
- `governance/compat/test_check_agent_operation_trace.py`
- `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

## Purpose

Dispatch a bounded Claude implementation packet for AOT-T2-C01+C02. The
purpose is to convert the AOT-T2 planning findings into a deterministic
repo-local guard: expected-manifest trace enforcement, co-work attribution
fields, and narrow trace eligibility for worker-authored `docs/reference/`
deliverables.

## Mission

Implement and test the AOT checker/standard update that prevents the exact
reviewer repair found in AOT-T2 planning: a worker-authored reference coverage
plan lacked an `Agent Operation Trace Block` and the machine gate did not fail.

Claude must implement the guard in the existing AOT checker and test surface,
update the standard, create the worker-return packet, and return without
committing.

## Authority Chain

- Operator instruction on 2026-06-13: "Dua vao luon, tiep tuc tao work order
  cho claude".
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- AOT-T2 closure:
  `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md`.
- AOT-T2 coverage plan:
  `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`.
- GC-018:
  `docs/baselines/CVF_GC018_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_2026-06-13.md`.
- Current standard:
  `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`.
- Current checker:
  `governance/compat/check_agent_operation_trace.py`.
- Current tests:
  `governance/compat/test_check_agent_operation_trace.py`.
- Active handoff: `AGENT_HANDOFF_V18_2026-06-12.md`.

Authority boundary:

- This work order authorizes only the files listed in Write Ownership.
- Codex owns review, allowed reviewer repairs, commit, completion review,
  committed-range pre-closure, and session sync.
- Any conflict between this work order and a canonical standard returns to
  Codex before implementation continues.

## Agent Roles

- Orchestrator / dispatcher: Codex.
- Implementer: Claude.
- Reviewer / committer: Codex.
- Escalation required for: scope expansion, hook-chain mutation, runtime
  mutation, OS audit or endpoint monitoring, public-sync, provider/API/live
  proof, external app inspection or mutation, or any commit by Claude.

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_COMPLETION_2026-06-13.md`

reviewerOwnedClosurePaths:

- `docs/baselines/CVF_GC018_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_FOR_CLAUDE_2026-06-13.md`
- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- `governance/compat/check_agent_operation_trace.py`
- `governance/compat/test_check_agent_operation_trace.py`
- `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_WORKER_RETURN_2026-06-13.md`
- `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

Reviewer conversion boundary: Claude worker return is not closure. Codex must
review the worker artifacts, add completion evidence, commit accepted changes,
run committed-range pre-closure, and perform session sync before claiming
closure.

## Scope

Allowed scope:

- update `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`;
- update `governance/compat/check_agent_operation_trace.py`;
- update `governance/compat/test_check_agent_operation_trace.py`;
- create `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_WORKER_RETURN_2026-06-13.md`;
- implement AOT-T2-C01 expected-manifest trace labels and manifest-delta
  enforcement;
- implement AOT-T2-C02 `Agent type` and `Invocation ID` labels;
- implement narrow worker-authored `docs/reference/` trace eligibility so a
  reference deliverable with worker/execution triggers must include a complete
  trace block;
- keep all claims repo-local.

Forbidden scope:

- no changes to hook-chain wiring unless existing checker invocation cannot
  cover the behavior;
- no changes to `CVF_SESSION/`, `CVF_SESSION_MEMORY.md`, or
  `AGENT_HANDOFF*.md`;
- no changes to `AGENTS.md`, `CLAUDE.md`, or provider-local memory files;
- no runtime/product source mutation outside the checker/test/standard owner
  surfaces;
- no public-sync;
- no provider/API/live-proof work;
- no OS audit, Sysmon, endpoint monitoring, file watcher service, destructive
  broker, or agent computer-control permission changes;
- no external Document Translator or Policy_Local inspection or mutation;
- no commit.

Risk ceiling:

- R2 bounded governance-control implementation.

## Required First Reads

Before editing, Claude must read:

- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`;
- `governance/compat/check_agent_operation_trace.py`;
- `governance/compat/test_check_agent_operation_trace.py`;
- `docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md`;
- `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md`;
- `docs/baselines/CVF_GC018_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_2026-06-13.md`;
- this work order;
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`.

## Pre-Flight Checks

Claude must capture and record these checks before implementation:

```powershell
git rev-parse --short HEAD
git status --short
Test-Path docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_WORKER_RETURN_2026-06-13.md
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 6ca6a748 --head HEAD
python -m unittest governance.compat.test_check_agent_operation_trace
```

Expected results:

- HEAD is at or after `6ca6a748`;
- the worker-return path is absent before Claude writes it;
- pre-implementation gate passes;
- current focused AOT tests pass before edits.

If a pre-flight check fails, Claude must stop and return the failed command and
result to Codex unless the fix is inside allowed scope and explicitly part of
this work order.

## Source-Fidelity Pass

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS current AOT trace marker | `governance/compat/check_agent_operation_trace.py` | line 24 | `TRACE_MARKER` | checker module | ACCEPT |
| EXISTS current required labels | `governance/compat/check_agent_operation_trace.py` | line 27 | `TRACE_REQUIRED_LABELS` | checker module | ACCEPT |
| EXISTS trace artifact prefixes exclude reference docs | `governance/compat/check_agent_operation_trace.py` | line 42 | `TRACE_ARTIFACT_PREFIXES` | checker module | ACCEPT |
| EXISTS worker/review triggers | `governance/compat/check_agent_operation_trace.py` | line 47 | `TRACE_REVIEW_TRIGGERS` | checker module | ACCEPT |
| EXISTS protected reference surface | `governance/compat/check_agent_operation_trace.py` | line 58 | `PROTECTED_REPO_PREFIXES` | checker module | ACCEPT |
| EXISTS trace artifact classifier | `governance/compat/check_agent_operation_trace.py` | line 134 | `is_trace_artifact` | checker module | ACCEPT |
| EXISTS missing-label evaluator | `governance/compat/check_agent_operation_trace.py` | line 145 | `missing_trace_labels` | checker module | ACCEPT |
| EXISTS trace violation evaluator | `governance/compat/check_agent_operation_trace.py` | line 170 | `find_trace_violations` | checker module | ACCEPT |
| EXISTS current AOT tests | `governance/compat/test_check_agent_operation_trace.py` | lines 38, 47, 53, 65, 71, 83 | `AgentOperationTraceTests` | unittest module | ACCEPT |
| EXISTS AOT standard required block | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 64 | `Required Agent Operation Trace Block` | AOT standard | ACCEPT |
| EXISTS AOT standard protected reference surface | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 95 | `docs/reference/` | AOT standard | ACCEPT |
| EXISTS checker expansion allowance | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | line 101 | checker may expand | AOT standard | ACCEPT |
| EXISTS coverage-plan missing-trace finding | `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md` | lines 85, 101 | coverage plan lacked trace block | AOT-T2 completion | ACCEPT |
| EXISTS accepted C01+C02 next tranche | `docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md` | lines 108, 109, 238 | AOT-T2-C01+C02 | AOT-T2 completion | ACCEPT |

New fields to implement:

| Planned item | Current disposition | Implementation owner |
| --- | --- | --- |
| `Agent type` | DOC_ONLY_PLANNED in AOT-T2 coverage plan; absent from checker labels | Claude |
| `Invocation ID` | DOC_ONLY_PLANNED in AOT-T2 coverage plan; absent as dedicated checker label | Claude |
| `Expected manifest` | DOC_ONLY_PLANNED in AOT-T2 coverage plan; absent from checker labels | Claude |
| `Actual changed set` | DOC_ONLY_PLANNED in AOT-T2 coverage plan; absent from checker labels | Claude |
| `Manifest delta` | DOC_ONLY_PLANNED in AOT-T2 coverage plan; absent from checker labels | Claude |
| worker-authored `docs/reference/` trace eligibility | MACHINE_CHECK_CANDIDATE from AOT-T2 reviewer repair | Claude |

## Negative Search And Collision Discipline

Exact pre-dispatch search command:

```powershell
rg -n "Agent type|Invocation ID|Expected manifest|Actual changed set|Manifest delta|UNAUTHORIZED_ADDITION|MISSING_DELIVERABLE|docs/reference/" governance/compat/check_agent_operation_trace.py governance/compat/test_check_agent_operation_trace.py docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md docs/reference/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_2026-06-13.md docs/reviews/CVF_AOT_T2_EXPECTED_MANIFEST_TRACE_COVERAGE_PLAN_COMPLETION_2026-06-13.md
```

Collision result:

- new manifest and attribution labels exist in AOT-T2 planning/completion docs
  as planning labels only;
- `docs/reference/` exists in protected-path lists, but not in current
  `TRACE_ARTIFACT_PREFIXES`;
- none of the new labels is currently enforced by `TRACE_REQUIRED_LABELS`;
- `UNAUTHORIZED_ADDITION` and `MISSING_DELIVERABLE` are planning tokens only.

Claude must preserve the distinction between planning-token occurrences and
implemented checker behavior in the worker return.

## Implementation Requirements

### AOT-T2-C01 Manifest Trace Fields

Add these required labels to `TRACE_REQUIRED_LABELS`:

- `Agent type`;
- `Invocation ID`;
- `Expected manifest`;
- `Actual changed set`;
- `Manifest delta`.

Manifest enforcement requirements:

- parse `Expected manifest` and `Actual changed set` values from the trace
  table when present;
- support semicolon, comma, newline, and backtick-wrapped path values where
  practical;
- compare the parsed expected manifest to the actual changed file set observed
  by `get_changed_paths`;
- `Manifest delta` must be `MATCH` when the expected manifest equals the
  changed file set;
- missing expected paths must trigger a violation containing
  `MISSING_DELIVERABLE`;
- unexpected changed paths must trigger a violation containing
  `UNAUTHORIZED_ADDITION`;
- `N/A with reason` is allowed only when all manifest fields clearly state an
  N/A reason and the task is not a worker-return or work-order governed
  execution packet.

### AOT-T2-C02 Co-Work Attribution Fields

`Agent type` must accept at least:

- `Codex`;
- `Claude`;
- `operator`;
- `OTHER: <description>`.

`Invocation ID` may be a session id, commit range, provider invocation label,
or `N/A with reason`. This is repo-local attribution only and must not claim
OS-level user identity or provider-internal logs.

### Worker-Authored Reference Trace Eligibility

Implement narrow `docs/reference/` trace eligibility:

- do not require trace blocks for every `docs/reference/*.md` file;
- require trace blocks for changed reference deliverables when worker or
  execution triggers are present, including `Worker:`,
  `WORKER_MUST_NOT_COMMIT`, `WORKER_RETURN_SUBMITTED_UNCOMMITTED`,
  `COMPLETE_PENDING_REVIEW`, or similar existing AOT trigger vocabulary;
- add a regression proving a worker-authored reference coverage plan without
  trace is a violation;
- add a regression proving a normal standard/reference file without worker
  triggers is not forced to include a trace block.

### Standard Update

Update the AOT standard to document:

- the five new required labels;
- manifest-delta accepted values and repo-local claim boundary;
- worker-authored reference deliverable trace eligibility;
- non-goals: no OS/user attribution, endpoint telemetry, provider-internal
  logging, physical-machine identity, public readiness, or production
  readiness.

## Execution Plan

Claude must execute in this order:

1. Confirm required first reads and pre-flight checks.
2. Update the focused checker and tests to enforce the new trace labels,
   manifest comparison, and narrow worker-authored reference eligibility.
3. Update the AOT standard to match implemented behavior and claim boundary.
4. Run focused tests and worker-return gates.
5. Create the worker-return packet with command output, changed paths, and
   `WORKER_MUST_NOT_COMMIT` confirmation.
6. Return to Codex with uncommitted changes only.

## Required Regression Tests

Claude must add focused tests for at least:

- existing work-order trace tests still pass after the new labels are added;
- changed worker-authored `docs/reference/` coverage plan without trace fails;
- changed non-worker standard/reference doc remains ignored;
- complete trace with new labels passes;
- manifest `MATCH` passes;
- missing expected deliverable fails with `MISSING_DELIVERABLE`;
- unexpected actual changed file fails with `UNAUTHORIZED_ADDITION`;
- N/A-with-reason manifest fields pass only for low-risk non-worker trace
  artifacts.

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| Intake item | AOT-T2-C01+C02 manifest trace implementation |
| Scope classification | bounded governance-control checker/test/standard implementation |
| Risk sensitivity | R2 checker behavior, deterministic tests required |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Selected role route | Claude worker implements; Codex reviewer/committer closes |
| routeMode | MULTI_AGENT_MULTI_ROLE |
| Routed role | Claude as worker |
| Reviewer | Codex |
| Commit authority | Codex only |
| Runtime/source authority | checker/test/standard only |
| Live/provider authority | NONE |
| Public-sync authority | NONE |
| Escalation condition | Stop for hook wiring, runtime expansion, public-sync, live/provider proof, OS audit, endpoint monitoring, external app access, destructive action, or commit request |
| Disposition | DISPATCHED_UNDER_WORKER_MUST_NOT_COMMIT |

## Single-Agent Multi-Role Control Block

| Field | Decision |
| --- | --- |
| Single agent owns implementation and review | NO |
| Role separation ledger | Claude owns implementation and worker return; Codex owns review, commit, completion, and session sync |
| Self-review boundary | Claude may run tests but may not close its own work |
| Gate sequence | pre-dispatch by Codex, pre-implementation by Claude, focused tests and worker-return fast gate by Claude, reviewer-fast/pre-closure by Codex |
| Escalation conditions | Stop for forbidden paths, hook mutation, public-sync, live/provider work, OS audit, endpoint monitoring, destructive action, or commit request |
| Worker | Claude |
| Reviewer / committer | Codex |
| Human escalation checkpoint | Scope expansion only |
| Collusion boundary | Codex must review real diff and gates before any commit |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: implement AOT-T2-C01+C02 in the existing
agent operation trace checker, its focused tests, and its canonical standard;
create the worker return; then allow Codex-owned closure/session sync.

Protected paths:

- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- `governance/compat/check_agent_operation_trace.py`
- `governance/compat/test_check_agent_operation_trace.py`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

Operator authorization: the operator instructed Codex to include the
worker-authored reference trace gap immediately and continue by creating a
Claude work order.

Rollback boundary: revert only this AOT-T2-C01+C02 implementation tranche and
its session sync if rejected. Do not revert AOT-T2 planning closure commit
`688bd97e`, session-sync commits `7891408c` and `6ca6a748`, or earlier AOT-T1
material history.

## Write Ownership

Claude-owned files:

- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- `governance/compat/check_agent_operation_trace.py`
- `governance/compat/test_check_agent_operation_trace.py`
- `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_WORKER_RETURN_2026-06-13.md`

Codex-owned closure files:

- `docs/reviews/CVF_AOT_T2_C01_C02_MANIFEST_TRACE_IMPLEMENTATION_COMPLETION_2026-06-13.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V18_2026-06-12.md`

Forbidden paths:

- `.github/**`;
- `EXTENSIONS/**`;
- `CVF_SESSION/**` by Claude;
- public-sync clone;
- external Document Translator repo;
- external Policy_Local repo;
- provider-local memory files.

## Verification Requirements

Claude must run and record:

```powershell
python -m unittest governance.compat.test_check_agent_operation_trace
python governance/compat/check_agent_operation_trace.py --base 6ca6a748 --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short
```

If `run_worker_return_fast_gate.py` hits Windows console encoding output
issues, rerun with:

```powershell
$env:PYTHONIOENCODING='utf-8'; python governance/compat/run_worker_return_fast_gate.py
```

## Evidence Requirements

Claude's worker return must include:

- pre-flight HEAD, status, and worker-return path existence result;
- focused unittest command and result;
- AOT checker command and result;
- worker-return fast gate command and result;
- `git diff --check` result;
- `git status --short` after implementation;
- changed file list;
- explicit confirmation that Claude did not commit;
- explicit claim boundary preserving repo-local trace enforcement only.

## Acceptance Criteria

| Criterion | Required evidence |
| --- | --- |
| New labels enforced | `TRACE_REQUIRED_LABELS` includes the five new labels and missing-label tests cover them |
| Manifest comparison works | tests cover `MATCH`, `MISSING_DELIVERABLE`, and `UNAUTHORIZED_ADDITION` |
| Reference deliverable gap closed | test proves worker-authored `docs/reference/` deliverable without trace fails |
| False positive controlled | test proves ordinary non-worker reference standard remains ignored |
| Standard updated | AOT standard documents labels, manifest delta, reference eligibility, and claim boundary |
| Existing behavior preserved | prior work-order/review/delete-rename tests still pass |
| Worker remains no-commit | HEAD unchanged by Claude; only allowed files changed/untracked |

Fail conditions:

| Fail condition | Return action |
| --- | --- |
| Claude edits forbidden paths | Stop and return to Codex |
| Claude commits | Stop; Codex must inspect repository state |
| Checker claims OS/user attribution or endpoint telemetry | Stop and correct claim boundary |
| New reference eligibility forces every `docs/reference/` file to carry trace | Stop and narrow the rule |
| Manifest parser blocks legitimate N/A-with-reason non-worker cases | Stop and narrow the rule |
| Focused tests fail | Repair inside allowed scope and rerun |

## Review Gate

Implementation may proceed only after this GC-018 and work order are committed
by Codex and dispatch gates pass.

Closure may proceed only after Codex reviews Claude's uncommitted worker return,
runs reviewer-fast/focused tests, applies allowed reviewer repairs if needed,
commits accepted changes, runs committed-range pre-closure, and performs
session sync.

Claude must return without committing.

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure within the
Allowed scope and Write Ownership must be repaired and rerun by Claude before
return. Routine allowed-scope fixes are mandatory.

Claude must stop and return to Codex only when repair would exceed Allowed
scope, change the claim boundary, require forbidden paths, open public-sync,
run live/provider proof, consume secrets/quota, configure OS audit or endpoint
monitoring, perform destructive action, or require a commit.

## Worker Pending-Return Gate

| Gate | Expected result |
| --- | --- |
| Required first reads completed | PASS |
| Pre-flight base HEAD recorded | PASS |
| Pre-flight status recorded | PASS |
| Standard updated | PASS |
| Checker updated | PASS |
| Focused tests updated | PASS |
| Worker return created | PASS |
| New labels enforced | PASS |
| Reference deliverable trace gap closed | PASS |
| False-positive reference standard test present | PASS |
| Focused unittest run recorded | PASS |
| Worker-return fast gate recorded | PASS |
| Agent Operation Trace Block complete | PASS |
| Forbidden paths untouched | PASS |

## Closure Checklist

| Closure item | Owner | Required disposition |
| --- | --- | --- |
| Claude implementation reviewed | Codex | Required before commit |
| Focused tests rerun | Codex | Required before material commit |
| Reviewer-fast gate run | Codex | Required before material commit |
| Completion review filed | Codex | Required for closure |
| Committed-range pre-closure run | Codex | Required after material commit |
| Session state/front door/handoff sync | Codex | Required if mode or next allowed move changes |
| Public catalog disposition | Codex | N/A unless public-sync is separately authorized |

## Operator Checkpoint

Operator checkpoint is required only if Claude or Codex needs to expand beyond
the checker/test/standard implementation, mutate hooks, touch runtime/product
source, run provider/live proof, open public-sync, inspect or mutate external
applications, configure OS/endpoint monitoring, or change the claim boundary.

## Return-To-Orchestrator Conditions

Return to Codex without continuing if:

- any required source file is missing;
- source facts conflict with this work order;
- a safe manifest parser cannot be implemented inside allowed scope;
- hook-chain changes become necessary;
- implementation would require forbidden paths;
- Claude cannot preserve `WORKER_MUST_NOT_COMMIT`.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex CLI |
| Session or invocation | dispatch base `6ca6a748` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `rg`, `Get-Content`, `Test-Path`, `apply_patch`, governance gates |
| Target paths | AOT-T2-C01+C02 GC-018, this work order, planned checker/test/standard surfaces, planned worker return |
| Allowed scope source | Operator instruction on 2026-06-13, active state nextAllowedMove, AOT-T2 completion |
| Before status evidence | `git status --short` clean before dispatch authoring |
| After status evidence | To be recorded by Codex after dispatch commit |
| Diff evidence | `git diff --name-status` before commit; committed range after Codex commit |
| Approval boundary | Operator asked to include the guard tightening now and create Claude work order |
| Claim boundary | Repo-local trace enforcement only; no OS/user attribution, endpoint telemetry, provider-internal logs, physical-machine identity, public readiness, or production readiness |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized by dispatch |

## Claim Boundary

This work order authorizes bounded repo-local checker/standard/test work only.
It does not authorize runtime behavior, provider behavior, OS-level identity
proof, endpoint telemetry, public readiness, production readiness, live
governance proof, public-sync, raw memory release, or autonomous mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control implementation dispatch.
Public-sync is not authorized.

rawMemoryReleased=false
