# CVF Agent Work Order - AAF-T1 Agent Automation Assist Foundation

Memory class: FULL_RECORD

Status: DISPATCH_READY

Date: 2026-06-20

docType: work_order

dispatchBaseHead: 21521829

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Implementer/worker (Claude). Codex is reviewer/closer.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_FOR_CLAUDE_2026-06-20.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: AAF-T1 is an automation-assist foundation tranche. It exists
because noncoder operators and external agents connected through CLI/MCP need
machine help to navigate CVF review, dispatch, closure, and session-sync without
manual latency loops.

Do-not-misread notes: do not open runtime execution, MCP wiring, provider/live
proof, public-sync, wrapper/proxy enforcement, direct IDE/shell/git/filesystem
interception, arbitrary command execution, queue/daemon, watcher, or background
service. The helper must remain read-only and advisory.

Required first actions: read this work order, read the AAF-T1 GC-018 baseline,
read the source files named in the Source Verification Block, confirm actual
`executionBaseHead`, and inspect current `git status --short` before editing.

Return contract: return `COMPLETE_PENDING_REVIEW` with exactly the three
uncommitted artifacts named in Required Deliverables, actual `executionBaseHead`,
actual `git status --short`, focused test result, worker-return fast gate result,
and no commit. If blocked, return `BLOCKED_WITH_REASON` and name the exact source
or gate that blocked the work.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two agents, one role each: Claude implements helper/tests/worker-return; Codex reviews/closes |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=21521829`; `executionBaseHead` confirmed by Claude; `closureBaseHead` set by Codex before closure commit |
| changedSetScope(phase) | worker creates only the three required artifacts; Codex owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one Claude worker-return trace covers the pending helper, test, and worker-return artifact; one Codex trace covers review/closure if accepted |
| commitOwner(phase) | Claude commits nothing (`WORKER_MUST_NOT_COMMIT`); Codex owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix AAF-T1 with CGE-T3 absorption, runtime, public-sync, provider/live, MCP, or direct-interception work |
| Before status evidence | clean worktree at dispatch base `21521829`, except recurring Windows global git-ignore permission warning |
| nextMoveSurfaces | Codex updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | Codex is the designated reviewer and closer |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_COMPLETION_2026-06-20.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_COMPLETION_2026-06-20.md`
- session front-door/state/handoff paths only if Codex changes current mode or
  next allowed move after accepting the worker return.

Claude must not create the completion review and must not mark the work closed.

## Purpose

Implement a deterministic read-only helper that reduces CVF workflow latency for
noncoder operators and external agents by classifying the current batch, pointing
to the correct steward lane, listing missing worker-return packet-shape blocks,
and printing exact next commands.

## Agent Roles

| Role | Owner |
|---|---|
| Dispatcher | Codex |
| Worker | Claude |
| Reviewer | Codex |
| Closer | Codex |
| Session-sync steward | Codex after review, only if next-move surfaces change |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 automation foundation approval | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T1 GC-018 | `docs/baselines/CVF_GC018_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_2026-06-20.md` | ACCEPT |
| Worker-return packet-shape hardening completion | `docs/reviews/CVF_WORKER_RETURN_PACKET_SHAPE_CONTRACT_GUARD_HARDENING_COMPLETION_2026-06-20.md` | ACCEPT |
| Commit steward protocol | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | ACCEPT |
| Work order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |
| External knowledge chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `governance/compat/run_agent_automation_assist.py`;
- create `governance/compat/test_run_agent_automation_assist.py`;
- create the worker-return artifact named in Required Deliverables;
- reuse existing helper functions or invoke existing read-only checkers through
  safe subprocess command construction;
- implement local path classification, mode recommendation, missing-block
  diagnostics, exact-command suggestions, and JSON output;
- run focused tests and worker-return fast gate.

Forbidden scope:

- no edits outside the three Required Deliverables;
- no edits under `EXTENSIONS/**`, product runtime, web UI, MCP packages,
  `.github/**`, public-sync, dependency manifests, or root lifecycle registries;
- no provider/live proof, benchmark, public push, secret read, dependency
  install, CodeGraph install/init, watcher/daemon, queue, or background service;
- no automatic mutation by the helper: no writing, staging, committing, pushing,
  deleting, moving, shelling into arbitrary user commands, or direct
  IDE/shell/git/filesystem interception;
- no readiness, production, public release, universal governed-coding control,
  or universal latency-reduction claim.

Risk ceiling: R1 governance tooling, read-only assistance.

## Required First Reads

Claude must read these before editing:

- `docs/baselines/CVF_GC018_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_2026-06-20.md`
- `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`
- `governance/compat/run_agent_commit_steward_preflight.py`
- `governance/compat/build_session_sync_pack.py`
- `governance/compat/run_worker_return_fast_gate.py`
- `governance/compat/run_dispatch_packet_author_fast_gate.py`
- `governance/compat/check_work_order_dispatch_quality.py`

## Pre-Flight Checks

Before implementation, Claude must run or record:

```powershell
git rev-parse --short HEAD
git status --short
```

If the worktree contains unrelated dirty paths, Claude must preserve them and
avoid editing outside the three Required Deliverables.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `governance/compat/run_agent_automation_assist.py` | Claude | create only |
| `governance/compat/test_run_agent_automation_assist.py` | Claude | create only |
| `docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_WORKER_RETURN_2026-06-20.md` | Claude | create only |
| Any other path | Not Claude | forbidden unless Codex issues a revised work order |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one read-only automation-assist helper
and one focused test under `governance/compat/` for AAF-T1 only.

Protected paths:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator explicitly approved raising CVF automation
and issuing this AAF-T1 work order to Claude on 2026-06-20.

Rollback boundary: if AAF-T1 is rejected, remove only the new helper, new test,
and AAF-T1 worker-return/reviewer artifacts. Do not revert prior guard hardening
commit `640f27a1` or session-sync commit `21521829`.

Scope boundary: this authorization does not extend to existing guard behavior,
active session files, root handoff files, runtime/product source, public-sync,
provider/live proof, or direct-interception tooling.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator-originated CVF automation-foundation request |
| Route | `MULTI_AGENT_SINGLE_ROLE` |
| risk sensitivity | R1; read-only local governance helper, no provider/live/public/runtime scope |
| selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Worker role | Claude implements helper/tests/worker-return only |
| Reviewer role | Codex reviews, commits, closes, and session-syncs if accepted |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | satisfied for dispatch; fresh checkpoint required for scope expansion |
| escalation condition | scope expansion, forbidden paths, provider/live, public-sync, secrets/quota, dependency install, destructive actions, or claim-boundary change |

## Worker Autonomy / No-Question Rule

Claude must repair and rerun gate failures inside Allowed scope. Claude must
stop and return `BLOCKED_WITH_REASON` only for scope expansion, forbidden paths,
live/provider proof, public-sync, secret/quota consumption, dependency install,
destructive actions, or claim-boundary changes.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | `governance/compat/` helper and focused test |
| Storage decision | add one narrow helper file and one matching test file |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | helper is read-only advisory automation; no hidden state store |

## Required Deliverables

Claude must create exactly these new uncommitted artifacts:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`
- `docs/reviews/CVF_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_WORKER_RETURN_2026-06-20.md`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Commit steward supports phase-specific modes including dispatch, reviewer-return, closure, session-sync, and handoff-sync | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | lines 48-67 | `run_agent_commit_steward_preflight.py --mode <mode>` | commit steward protocol | ACCEPT |
| Commit steward exposes session and handoff path prefixes for classification | `governance/compat/run_agent_commit_steward_preflight.py` | lines 18-31 | `SESSION_PREFIXES`; `HANDOFF_PREFIXES` | commit steward path classifier | ACCEPT |
| Commit steward maps modes to autorun or focused commands | `governance/compat/run_agent_commit_steward_preflight.py` | lines 195-268 | `_mode_commands` | commit steward command planner | ACCEPT |
| Session-sync pack helper is read-only and imports steward/state logic instead of duplicating it | `governance/compat/build_session_sync_pack.py` | lines 3-12, 46-52 | `build_path_plan`; `validate_aggregate_matches_sources` | session-sync pack helper | ACCEPT |
| Session-sync pack helper supports author-entry skeleton output | `governance/compat/build_session_sync_pack.py` | lines 209-250 | `--author-entry`; `--state-key` | session-sync pack CLI | ACCEPT |
| Worker-return fast gate runs focused pytest targets, corpus registry drift, reviewer-fast, and diff hygiene | `governance/compat/run_worker_return_fast_gate.py` | lines 30-52, 78-100 | `build_commands`; `--pytest-target` | worker-return fast gate | ACCEPT |
| Dispatch packet author fast gate runs five packet-authoring checks | `governance/compat/run_dispatch_packet_author_fast_gate.py` | lines 3-32, 44-91 | `GATE_COMMANDS` | dispatch packet author fast gate | ACCEPT |
| Work order template requires no-commit worker returns to use worker-return fast gate and record actual pending status | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | lines 877-919 | `WORKER_MUST_NOT_COMMIT`; `run_worker_return_fast_gate.py` | work order template review gate | ACCEPT |
| Dispatch-quality checker enforces Worker Return Packet Shape Contract for no-commit dispatches | `governance/compat/check_work_order_dispatch_quality.py` | lines 51, 159-177, 777-805, 2345 | `WORKER_RETURN_PACKET_SHAPE_CONTRACT_MARKER`; `_validate_worker_return_packet_shape_contract` | work order dispatch-quality gate | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | input router to governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` and `governance/compat/run_agent_commit_steward_preflight.py` |
| Owner surface | `governance/compat/run_agent_automation_assist.py` after implementation |
| Disposition | ADAPT as CVF-owned governance helper |
| Claim boundary | existing CVF helpers and standards remain source authority; no third-party repo code or claims are absorbed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T1 read-only governance automation helper work order only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local user invokes the helper manually |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | automation-assist helper, not execution-control enforcement |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, readiness, and universal control remain parked |

## New Helper Surface Declaration

| New item | File | Type | Boundary |
|---|---|---|---|
| `run_agent_automation_assist.py` | `governance/compat/run_agent_automation_assist.py` | new read-only CLI helper | advisory automation only |
| `test_run_agent_automation_assist.py` | `governance/compat/test_run_agent_automation_assist.py` | new focused tests | no runtime/provider/public effects |

## Roadmap-To-Work-Order Trace Matrix

| Need | Source | AAF-T1 instruction |
|---|---|---|
| Reduce noncoder/external-agent latency | operator 2026-06-20 instruction | implement one read-only automation assist helper |
| Preserve guard coverage | commit steward protocol lines 35-46 | recommend existing gates instead of bypassing them |
| Make worker-return shape machine-visible | worker-return packet-shape hardening completion | diagnose missing shape blocks and require worker return to use the new shape |
| Keep automation bounded | AAF-T1 GC-018 Scope / Owner Boundary | no mutation, provider/live, public-sync, or direct interception |

## Required Helper Contract

The helper must accept:

```powershell
python governance/compat/run_agent_automation_assist.py --base <baseHead> --head HEAD
python governance/compat/run_agent_automation_assist.py --base <baseHead> --head HEAD --mode auto
python governance/compat/run_agent_automation_assist.py --base <baseHead> --head HEAD --json
python governance/compat/run_agent_automation_assist.py --base <baseHead> --head HEAD --enforce
```

Allowed `--mode` values:

- `auto`
- `dispatch`
- `implementation`
- `reviewer-return`
- `closure`
- `session-sync`
- `handoff-sync`

Required output:

- changed path summary;
- recommended steward lane;
- exact next command;
- missing worker-return packet-shape contract diagnostics for changed
  `WORKER_MUST_NOT_COMMIT` work orders;
- session-sync helper hint when only session/handoff paths changed;
- JSON object with equivalent fields when `--json` is used.

`--enforce` must exit non-zero only for local helper-detectable defects such as
missing Worker Return Packet Shape Contract in a changed no-commit work order,
unsupported mode, invalid range, or inability to inspect the changed set. It must
not execute provider/live checks or mutate files.

## Execution Plan

1. Re-read Required First Reads and confirm `executionBaseHead`.
2. Implement `run_agent_automation_assist.py` as a read-only helper.
3. Reuse existing steward path-planning logic where practical.
4. Add focused unit tests for path classification, mode recommendation,
   no-commit work-order diagnostics, JSON output, and enforce failure.
5. Create the worker-return artifact with the Worker Return Packet Shape
   Contract.
6. Run the required evidence commands and return uncommitted
   `COMPLETE_PENDING_REVIEW`.

## Worker Return Packet Shape Contract

Claude's worker-return artifact must include these always-required sections or
terms:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- actual `executionBaseHead`
- actual `git status --short`

Claude's worker-return artifact must include or explicitly mark `N/A with reason`
or `NOT_APPLICABLE_WITH_REASON` for these conditional gate sections:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Because this dispatch is itself testing the new guard, omission of this contract
or any required term is a blocking worker-return defect.

## Evidence Requirements

Claude must run and record:

```powershell
python -m unittest governance.compat.test_run_agent_automation_assist
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_automation_assist.py
git status --short
```

Claude may also run the helper against the current changed set and record safe
output, but must not run provider/live, dependency install, public-sync, or any
destructive command.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | New helper is read-only and contains no file write/stage/commit/push/delete behavior. |
| AC2 | Helper classifies changed paths and recommends a steward lane or mode-specific command. |
| AC3 | Helper reports missing Worker Return Packet Shape Contract for changed `WORKER_MUST_NOT_COMMIT` work orders. |
| AC4 | Helper emits JSON and human-readable output. |
| AC5 | Focused tests cover auto mode, session-sync path classification, no-commit work-order missing contract, JSON output, and enforce failure behavior. |
| AC6 | Worker return uses the Worker Return Packet Shape Contract and records actual pending status. |

## Mandatory Gate-Failure Remediation Protocol

If a focused test, worker-return fast gate, or local helper diagnostic fails
inside Allowed scope, Claude must repair and rerun.

Block only if repair would exceed Allowed scope, alter claim boundary, touch
forbidden paths, require live/provider proof, require public-sync, consume
secrets/quota, install dependencies, or perform destructive/irreversible action.

## Review Gate

Worker handoff may proceed only after:

- all three Required Deliverables exist;
- focused unittest passed or failure is source-backed and marked
  `BLOCKED_WITH_REASON`;
- worker-return fast gate passed or failure is outside Allowed scope and marked
  `BLOCKED_WITH_REASON`;
- actual `git status --short` is recorded;
- no commit was made by Claude.

For `WORKER_MUST_NOT_COMMIT`, worker handoff is not closure. Codex must review
the pending diff, decide acceptance, commit accepted material, and run the
committed-range `pre-closure` gate before any closed-equivalent claim.

## Return-To-Orchestrator Conditions

Return to orchestrator as `BLOCKED_WITH_REASON` if:

- any Required First Read is missing;
- the helper cannot stay read-only;
- focused tests require changing forbidden paths;
- a gate failure requires provider/live proof, public-sync, dependency install,
  destructive action, or claim-boundary expansion;
- `WORKER_MUST_NOT_COMMIT` cannot be preserved.

## Closure Checklist

- [ ] Required deliverables exist and no extra worker-owned files were created.
- [ ] Source Verification Block remains source-backed.
- [ ] Focused unittest result recorded.
- [ ] Worker-return fast gate result recorded.
- [ ] Worker Return Packet Shape Contract satisfied in the worker-return packet.
- [ ] Codex reviewer ran committed-range `pre-closure` after accepted material
  commit.
- [ ] Session-sync performed only if mode or next allowed move changed.

## Return Conditions

Return `COMPLETE_PENDING_REVIEW` only if the helper, tests, and worker-return
artifact are present, uncommitted, inside Allowed scope, and supported by command
evidence.

Return `BLOCKED_WITH_REASON` if any required source is missing, the helper cannot
be implemented without forbidden mutation behavior, a gate fails outside Allowed
scope, or the worker cannot preserve `WORKER_MUST_NOT_COMMIT`.

## Claim Boundary

AAF-T1 authorizes only a read-only local automation-assist helper and tests. It
does not authorize runtime/product behavior, provider/live proof, public-sync,
MCP execution, wrapper/proxy enforcement, direct interception, arbitrary command
execution, queue/daemon behavior, background services, readiness, production, or
universal governed-coding-control claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance governance tooling. Public export, if any,
requires a separate public-sync authorization.

## Operator Checkpoint

Operator checkpoint for dispatch is satisfied by the 2026-06-20 instruction to
proceed with CVF automation foundation and issue this work order to Claude.
Fresh operator approval is required before any scope expansion into runtime,
MCP, provider/live, public-sync, automatic mutation, direct interception, or
release/readiness claims.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | Codex local workspace |
| Session or invocation | AAF-T1 dispatch packet authoring, 2026-06-20 |
| Working directory | repository root |
| Command or tool surface | apply_patch; rg; PowerShell reads; dispatch gates |
| Target paths | AAF-T1 GC-018 baseline and work order |
| Allowed scope source | operator 2026-06-20 automation-foundation instruction |
| Before status evidence | clean worktree at dispatch base `21521829`; `git status --short` clean except recurring Windows global git-ignore permission warning |
| After status evidence | AAF-T1 baseline and work order added as dispatch-ready packet |
| Diff evidence | `git diff --name-status` over `21521829..HEAD` before dispatch commit |
| Approval boundary | dispatch packet only; Claude remains `WORKER_MUST_NOT_COMMIT` |
| Claim boundary | no runtime/provider/public/direct-interception/readiness claim |
| Agent type | single-agent dispatch author |
| Invocation ID | `aaf-t1-agent-automation-assist-dispatch-codex-2026-06-20` |
| Expected manifest | `docs/baselines/CVF_GC018_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_FOR_CLAUDE_2026-06-20.md` |
| Actual changed set | `docs/baselines/CVF_GC018_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T1_AGENT_AUTOMATION_ASSIST_FOUNDATION_FOR_CLAUDE_2026-06-20.md` |
| Manifest delta | MATCH |
