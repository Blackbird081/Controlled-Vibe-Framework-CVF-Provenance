# CVF Agent Work Order - AAF-T7B Reviewer Completion Scaffold Helper (L1)

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: work_order

dispatchBaseHead: bf3d4acf

Commit mode: `WORKER_MUST_NOT_COMMIT`

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This work order
authorizes one bounded helper tranche; it does not map, enumerate, project, or
classify CVF state.

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_FOR_WORKER_2026-06-22.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: AAF-T7A.1 L0 reviewer readout is closed by Codex
reviewer/closer at material commit `5fc456a4` and session-sync commit
`bf3d4acf`. AAF-T7B is the next bounded AAF-T7 tranche at the L1 scaffold
level. L2 patch preview remains separate after this tranche. L3 apply remains
out of scope.

Do-not-misread notes: implement only L1 reviewer-completion scaffold output and
explicit one-file scaffold write. Do not implement L2 patch preview, L3 apply,
patch application, edit of existing governed markdown by helper, staging,
commit, push, arbitrary command execution, provider/live calls, runtime
Learning Plane mutation, CLI/MCP adapter behavior, public-sync, queue, daemon,
watcher, wrapper/proxy, direct IDE/shell/git/filesystem interception, readiness,
cost/speed claim, or universal governed-coding-control claim.

Required first actions: read this work order, read the AAF-T7B GC-018
baseline, read the AAF-T7A roadmap, read the L2A classification standard, read
the Guard Orientation Index, inspect the existing AAF helper CLI/report/readout
and helper tests, confirm actual `executionBaseHead`, and inspect current
`git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only the required
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
source inventory, scan-depth ledger, focused test evidence, gate evidence, and
no commit. If blocked, return `BLOCKED_WITH_REASON` and name the exact source
or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator instruction to continue AAF-T7 remaining parts after AAF-T7A.1 closure |
| Intake role | worker adds L1 reviewer-completion scaffold helper mode and focused tests |
| Reviewer role | reviewer/closer validates scaffold boundaries, path restrictions, focused tests, and claim boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; bounded scaffold helper only |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation would require L2 patch preview, L3 apply, editing existing governed docs by helper, staging, commit, provider/live, public-sync, runtime/product, CLI/MCP adapter, arbitrary command, session/handoff edits, or forbidden path scope |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatcher creates packet; worker adds L1 scaffold helper and return packet; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=bf3d4acf`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending AAF-T7B artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix AAF-T7B with L2 patch preview, L3 apply, MPI, full AAF-T6 read-receipt, runtime/provider/live, MCP adapter, public-sync, queue/daemon, direct-interception, generated aggregate, or memory-plane work |
| Before status evidence | dispatchBaseHead `bf3d4acf`; clean worktree verified before AAF-T7B dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted helper source/test changes; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and worker-return packet shape |
| `docs/baselines/CVF_GC018_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_2026-06-22.md` | GC-018 authorization and claim boundary |
| `docs/roadmaps/CVF_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_ROADMAP_2026-06-22.md` | roadmap posture and remaining AAF-T7 acceleration sequence |
| `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | L1/L2/L3 safety-level authority |
| `governance/compat/run_agent_automation_assist.py` | existing helper CLI, report, readout, and output path to extend |
| `governance/compat/test_run_agent_automation_assist.py` | focused test module to extend |
| `governance/compat/run_worker_return_fast_gate.py` | focused pytest target routing for the fast gate |

## Pre-Flight Checks

The worker must run or record these checks before returning. For commands that
use `<executionBaseHead>`, replace it with the exact value returned by
`git rev-parse --short HEAD` at worker start.

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_run_agent_automation_assist
python governance/compat/run_agent_automation_assist.py --base <executionBaseHead> --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_automation_assist.py
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-gate, source-inventory,
packet-shape, focused-test, or scaffold-boundary defects and rerun the required
checks without asking the operator. Ask the operator only if remediation would
exceed Allowed scope, change the claim boundary, require L2/L3/runtime/provider/
public/session scope, touch forbidden paths, consume secrets/quota, require a
destructive action, or contradict this work order.

## Worker Return Packet Shape Contract

The worker-return artifact must include these sections so reviewer-fast can
diagnose issues before closure:

- `Status`
- `Purpose`
- `Scope / Methodology`
- `Findings / Position`
- `Risk / Corrective Action`
- `Claim Boundary`
- `Agent Operation Trace Block`
- `Delta Execution Claim Boundary Control Block`
- `Public Export Disposition`
- `External Knowledge Intake Routing`
- `Rescan Intelligence Hardening`
- `Corpus Completeness And Report Integrity`
- `Finding-To-Governance Learning Disposition`
- `Epistemic Process Block`
- `Machine Closure Package`
- actual `executionBaseHead`
- actual `git status --short`
- changed-path list
- focused test and gate evidence
- `WORKER_EXPERIENCE_RETRO` block or
  `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`

If any listed section is not applicable, include the section with `N/A with reason` or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it.

## Execution Plan

1. Read required sources and record `executionBaseHead`.
2. Extend the existing AAF helper with explicit scaffold emit/write options.
3. Keep default helper behavior unchanged when no scaffold flag is passed.
4. Restrict scaffold writes to one new markdown file under `docs/reviews/` and
   refuse overwrite.
5. Add focused tests for scaffold output, explicit invocation, path restriction,
   no-overwrite behavior, and no L2/L3/apply/commit behavior.
6. Run required checks and create the worker-return artifact without committing.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `governance/compat/run_agent_automation_assist.py` | worker | add explicit L1 scaffold emit/write mode with bounded path and overwrite checks |
| `governance/compat/test_run_agent_automation_assist.py` | worker | add focused tests for scaffold content, explicit invocation, path restriction, no-overwrite behavior, and no patch/apply/commit behavior |
| `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_WORKER_RETURN_2026-06-22.md` | worker | create |
| `docs/baselines/CVF_GC018_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_2026-06-22.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_FOR_WORKER_2026-06-22.md` | reviewer/closer | no worker edit |
| `AGENTS.md`, `CVF_SESSION/**`, active handoff, runtime routes, web, MCP, provider registry, generated aggregates, public-sync, queue/daemon/watcher, wrapper/proxy, L2 patch preview, L3 apply files | out of worker scope | forbidden |

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
L2 patch preview, L3 apply, editing existing governed docs by helper,
runtime/product behavior, generated aggregate edits, AGENTS/session/handoff
edits, provider/live/public-sync scope, dependency installation, secrets/quota,
destructive action, or a change to the claim boundary.

## Purpose

Add an explicit L1 reviewer-completion scaffold helper mode to the existing AAF
helper so a reviewer/closer can generate a skeleton completion review with the
required governance headings present before manual review and completion.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | dispatch author role |
| Worker | scaffold helper and focused test author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 continue AAF-T7 remaining parts and finish the lane in order | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T7B GC-018 | `docs/baselines/CVF_GC018_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_2026-06-22.md` | ACCEPT |
| AAF-T7A.1 completion review | `docs/reviews/CVF_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_COMPLETION_2026-06-22.md` | ACCEPT |
| AAF-T7A roadmap | `docs/roadmaps/CVF_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_ROADMAP_2026-06-22.md` | ACCEPT |
| L2A classification standard | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Existing AAF helper | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| Existing AAF helper tests | `governance/compat/test_run_agent_automation_assist.py` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- update `governance/compat/run_agent_automation_assist.py` to add explicit
  L1 scaffold emit/write behavior:
  - emit scaffold text only when `--emit-reviewer-completion-scaffold` or
    `--write-reviewer-completion-scaffold <path>` is provided;
  - write exactly one new markdown file only under `docs/reviews/`;
  - refuse overwrite and return nonzero on invalid scaffold paths;
  - do not stage, commit, apply, or edit existing files;
- update `governance/compat/test_run_agent_automation_assist.py` with focused
  tests for the behavior above;
- create
  `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_WORKER_RETURN_2026-06-22.md`;
- reviewer/closer closure conversion may update this work order, paired
  GC-018, and create the completion review after accepting the worker return.

Forbidden scope:

- no L2 patch preview and no L3 apply mode;
- no helper edit to existing governed markdown, no patch apply, no staging, no
  commit, no push, no closure decision, no provider/live call, and no arbitrary
  command execution;
- no full AAF-T6 Guard Orientation Read-Receipt Gate;
- no ledger store, source directory, generator, drift checker, durable store,
  runtime Learning Plane mutation, CLI/MCP adapter behavior, public-sync,
  wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception,
  queue, daemon, watcher, readiness, full-hook equivalence, cost optimization
  claim, speed/productivity claim without proof, or universal
  governed-coding-control claim;
- no route schema edits, runtime/product behavior, dependency installation, or
  generated aggregate edits.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| L2A safety level L1 writes a skeleton file or section with required structure and empty fields | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | line 105 | L1 scaffold generation | L2A Acceleration Safety Levels | ACCEPT |
| L2A safety level L2 is patch preview only and does not apply | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | line 106 | L2 patch preview | L2A Acceleration Safety Levels | ACCEPT |
| L2A safety level L3 is future allowlisted apply with postcondition checker | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | line 107 | L3 allowlisted apply with postcondition checker | L2A Acceleration Safety Levels | ACCEPT |
| AAF helper exposes an argparse CLI entrypoint | `governance/compat/run_agent_automation_assist.py` | lines 943-957 | main | AAF helper CLI | ACCEPT |
| AAF helper report serializes reviewer readout in JSON | `governance/compat/run_agent_automation_assist.py` | lines 496, 564 | AssistReport; reviewerReadout | AAF helper report dataclass | ACCEPT |
| AAF helper builds reviewer readout from existing diagnostics | `governance/compat/run_agent_automation_assist.py` | lines 702-748 | _build_reviewer_readout | AAF helper readout builder | ACCEPT |
| AAF helper has focused reviewer readout tests | `governance/compat/test_run_agent_automation_assist.py` | lines 831-945 | ReviewerReadoutTests | AAF helper test module | ACCEPT |
| AAF-T7A.1 work order deferred L1 and L2 to a later tranche | `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_FOR_WORKER_2026-06-22.md` | lines 385, 419 | DEFER | Follow-Up Routing Matrix | ACCEPT |

## New Helper Terms

| Proposed term | Owner in AAF-T7B | Runtime status | Reason |
|---|---|---|---|
| `reviewerCompletionScaffold` | AAF-T7B helper output | NEW_HELPER_OUTPUT_FIELD | names the generated completion-review skeleton text in JSON/human output |
| `--emit-reviewer-completion-scaffold` | AAF-T7B helper CLI flag | NEW_HELPER_CLI_FLAG | prints scaffold text without writing a file |
| `--write-reviewer-completion-scaffold` | AAF-T7B helper CLI flag | NEW_HELPER_CLI_FLAG | writes one new scaffold file under `docs/reviews/` and refuses overwrite |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap item | Source | Work-order coverage | Evidence requirement |
|---|---|---|---|
| AAF-T7A.1 closed L0 readout | `5fc456a4`; `bf3d4acf` | prerequisite satisfied | commit evidence and completion review |
| Remaining AAF-T7 safe acceleration level | L2A line 105 | AAF-T7B implements L1 scaffold only | focused tests and worker return |
| L2 patch preview | L2A line 106 | excluded from this tranche | claim boundary and no L2 code |
| L3 apply | L2A line 107 | forbidden | claim boundary and no apply mode |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | local governed learning-to-acceleration route, not external authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; pre-dispatch autorun |
| Owner surface | AAF-T7B Reviewer Completion Scaffold Helper |
| Disposition | ADAPT as CVF-owned L1 scaffold helper with bounded path checks |
| Claim boundary | operator critique remains input only until implemented and closed through this governed work order |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/run_agent_automation_assist.py`; `governance/compat/test_run_agent_automation_assist.py` |
| Runtime behavior claimed | N/A_WITH_REASON: governance compatibility helper only; no product runtime, provider route, web route, CLI/MCP adapter, or Learning Plane mutation |
| Helper/checker implementation claimed | BOUNDED: add explicit L1 scaffold output/write mode and focused tests |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded helper scaffold only; no provider, public-sync, runtime product behavior, or generated aggregate behavior is claimed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T7B L1 reviewer-completion scaffold helper |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | explicit helper scaffold invocation only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | L1 scaffold helper only |
| forbiddenExpansion | L2 patch preview, L3 apply, wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, cost/speed claim, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Reviewer completion packets repeat the same required headings and evidence blocks | ACCELERATION_GAP | LEARNING_TO_ACCELERATION | ACCELERATOR_CANDIDATE | Add L1 scaffold helper with bounded path and overwrite checks | handled by this dispatch |
| Patch preview could automate repeated status wording changes | ACCELERATION_GAP | LEARNING_TO_ACCELERATION | SEPARATE_TRANCHE | keep L2 for a later work order after L1 closes | deferred |
| Apply mode could mutate governed files without review | CONTROL_PROOF_GAP | GOVERNANCE_CONTROL_PLANE | OUT_OF_SCOPE | L3 remains forbidden | deferred |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded L1 scaffold
  helper tranche.
- Corpus root: repo-local files named in Authority Chain and Source
  Verification Block.
- Snapshot time: 2026-06-22 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus targeted `rg`.
- Manifest artifact or inline manifest: Authority Chain and Source
  Verification Block in this work order.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows
  in this work order.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=Authority Chain and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo scan, generated aggregate mutation, runtime/provider/web/MCP/public-sync scan; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: full-repo scan, generated aggregate mutation,
  runtime/provider/web/MCP/public-sync scan, public-sync proof, provider/live
  proof.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by dispatch.
- Drift check: N/A with reason: no generated aggregate edited by dispatch.
- Output traceability: AAF-T7B work order maps the AAF-T7A.1 L1/L2 deferral to
  worker deliverables and required gates.
- Adversarial verification: source rows distinguish L1 scaffold from L2 patch
  preview and L3 apply.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add an explicit L1 reviewer-completion
scaffold mode to the existing AAF helper and add focused tests for bounded file
creation, without adding patch apply, closure decision, staging, commit, push,
provider/live, or runtime behavior.

Protected paths:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator directed the AAF-T7 lane to continue and
finish the remaining parts after the closed AAF-T7A.1 L0 readout. This work
order authorizes only the next safe level, L1 scaffold generation.

Rollback boundary: revert the accepted AAF-T7B material closure commit to
remove the scaffold helper and focused tests together.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | N/A with reason: this work order does not create, split, relocate, or refactor durable governance foundation storage. |
| New durable foundation directory | N/A with reason |
| Generated aggregate impact | N/A with reason: no generated aggregate is edited. |
| INDEX impact | N/A with reason: this is not an INDEX artifact or storage-layout tranche. |
| Guard owner | reviewer/closer verifies no durable storage layout mutation during closure. |

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- source inventory and scan-depth ledger;
- changed-path list;
- focused unit test results;
- AAF helper smoke result with `--json --enforce`;
- pre-implementation autorun gate result;
- worker-return fast gate result;
- explicit statement that the helper writes only one new scaffold file when an
  explicit scaffold-write flag is used;
- explicit statement that the helper refuses overwrite and paths outside
  `docs/reviews/`;
- explicit statement that no L2 patch preview, L3 apply, runtime,
  provider/live, public-sync, CLI/MCP adapter, generated aggregate, or
  session/handoff path was edited;
- exact claim boundary and public export disposition.

## Review Gate

Reviewer/closer must inspect the worker-return changed set against Required
Deliverables, run reviewer-fast gates, verify no forbidden scope was touched,
verify scaffold writes are explicit and bounded, and only then convert accepted
material into a completion review.

## Closure Checklist

- [ ] Worker returned `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
- [ ] Changed files stay inside Required Deliverables.
- [ ] Scaffold output requires an explicit scaffold flag.
- [ ] Scaffold write creates only one new markdown file under `docs/reviews/`.
- [ ] Existing file overwrite and out-of-scope paths are refused.
- [ ] Helper performs no L2 patch preview, L3 apply, staging, commit, push, provider/live call, or closure decision.
- [ ] Worker-return fast gate passes or records `BLOCKED_WITH_REASON`.
- [ ] Reviewer-owned completion review created if accepted.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all required deliverables are present,
required checks have been run or source-blocked with evidence, and changed files
remain inside Allowed scope.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, or the repair would require forbidden
L2/L3/runtime/provider/public/session scope.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | The helper emits scaffold text only for explicit scaffold invocation | source diff and focused test |
| AC2 | The helper writes one new scaffold file only under `docs/reviews/` | source diff and focused test |
| AC3 | The helper refuses overwrite and paths outside `docs/reviews/` | focused test |
| AC4 | The helper performs no L2 patch preview, L3 apply, staging, commit, provider/live call, or arbitrary command | diff review and focused test |
| AC5 | No forbidden paths changed | `git status --short`; diff |
| AC6 | Worker return contains required packet shape and no commit | worker-return gate |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T7B is private provenance governance-helper work. No public-sync
repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local workspace |
| Session or invocation | AAF-T7B worker execution, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, focused source/test edits, required gates |
| Target paths | worker required deliverables |
| Allowed scope source | this work order and paired GC-018 baseline |
| Before status evidence | dispatchBaseHead `bf3d4acf`; clean worktree verified before AAF-T7B dispatch authoring |
| After status evidence | AAF-T7B worker artifacts pending no-commit return |
| Diff evidence | worker records `git status --short` and gate receipts |
| Approval boundary | worker may update Required Deliverables but must not commit |
| Claim boundary | L1 scaffold helper only; no L2/L3, runtime, provider, or public behavior |
| Agent type | worker role |
| Invocation ID | `aaf-t7b-reviewer-completion-scaffold-worker-2026-06-22` |
| Expected manifest | helper source; focused tests; worker return |
| Actual changed set | worker records in return packet |
| Manifest delta | worker records in return packet |

## Claim Boundary

This work order authorizes only AAF-T7B L1 reviewer-completion scaffold helper
behavior added to the existing AAF helper plus focused tests. It does not
authorize L2 patch preview, L3 apply mode, helper edits to existing governed
artifacts, closure decisions by the helper, full AAF-T6 read-receipt proof,
runtime behavior, provider/live behavior, CLI/MCP adapter behavior, public-sync,
session-sync by worker, direct interception, readiness claims, speed/cost
claims, or universal governed-coding control.
