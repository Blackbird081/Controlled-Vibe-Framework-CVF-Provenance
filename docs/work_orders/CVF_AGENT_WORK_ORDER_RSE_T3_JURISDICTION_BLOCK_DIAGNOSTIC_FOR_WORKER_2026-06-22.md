# CVF Agent Work Order - RSE-T3 Jurisdiction Block Diagnostic

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: work_order

dispatchBaseHead: 31faa6bc

Commit mode: `WORKER_MUST_NOT_COMMIT`

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This work order
authorizes one bounded read-only diagnostic tranche; it does not map, enumerate,
project, or classify CVF state.

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_FOR_WORKER_2026-06-22.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: RSE-T2 is closed (`6ab1eaf6`, sync `31faa6bc`). The roadmap
author completed the RSE roadmap T0 through T3, and the dispatch author prepared
this work order and the paired GC-018 baseline. Per the operator role model, the
work-order reviewer accepts the packet before execution; the worker then returns
uncommitted work for the reviewer/closer. RSE-T3 is a read-only diagnostic, one
diagnostic in the first slice.

Do-not-misread notes: implement only one read-only advisory diagnostic in the AAF
helper plus focused tests. Do not add closure-blocking enforcement, a new
exit-nonzero defect class, or any change to existing enforce-mode behavior. Do
not edit other `governance/compat/` checkers, the autorun gate wiring, the
dispatch-quality checker, the work-order template, or the closed RSE-T0, RSE-T1,
or RSE-T2 documents. Do not implement the remaining four roadmap T3 candidate
diagnostics. Do not add provider/live, public-sync, CLI/MCP adapter, workspace,
queue, daemon, watcher, direct interception, L3 apply, arbitrary command,
readiness, or universal control behavior or claim.

Required first actions: read this work order, read the RSE-T3 GC-018 baseline,
read the RSE roadmap T3 section, read the closed RSE-T2 addendum, read the L2A
classification standard, read the Guard Orientation Index, inspect the existing
AAF helper readout dataclass, builder, report assembly, and readout test class,
confirm actual `executionBaseHead`, and inspect current `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only the required
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
source inventory, scan-depth ledger, focused test evidence, gate evidence, and no
commit. If blocked, return `BLOCKED_WITH_REASON` and name the exact source or
gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator instruction to open RSE-T3 as a read-only AAF-helper diagnostic, bounded first slice of one diagnostic |
| Intake role | worker adds one read-only diagnostic and focused tests |
| Reviewer role | reviewer/closer validates read-only property, no enforcement, focused tests, and claim boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; bounded read-only diagnostic only |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | roadmap author, dispatch author, work-order reviewer, worker, reviewer/closer |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation would require closure-blocking enforcement, a new exit-nonzero defect, edits to other checkers or autorun wiring or the work-order template, edits to the closed RSE-T0 or RSE-T1 or RSE-T2 documents, the remaining T3 candidates, runtime/provider/live, public-sync, session/handoff edits, or forbidden path scope |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | roadmap author -> dispatch author -> work-order reviewer -> worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; WORK_ORDER_REVIEW; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=31faa6bc`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending RSE-T3 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix RSE-T3 with RSE-T0 or RSE-T1 or RSE-T2 edits, the remaining T3 candidates, AAF, MPI, runtime/provider/live, MCP adapter, public-sync, queue/daemon, direct-interception, generated aggregate, or memory-plane work |
| Before status evidence | dispatchBaseHead `31faa6bc`; clean worktree verified before RSE-T3 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted helper source and test changes; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and worker-return packet shape |
| `docs/baselines/CVF_GC018_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_2026-06-22.md` | GC-018 authorization and claim boundary |
| `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | roadmap T3 candidate diagnostics and acceptance criteria |
| `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | the jurisdiction block the diagnostic detects |
| `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | L0 read-only safety level authority |
| `governance/compat/run_agent_automation_assist.py` | existing readout dataclass, builder, report assembly to mirror |
| `governance/compat/test_run_agent_automation_assist.py` | focused readout test class to mirror |

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
packet-shape, focused-test, or diagnostic-boundary defects and rerun the required
checks without asking the operator. Ask the operator only if remediation would
exceed Allowed scope, change the claim boundary, require closure-blocking
enforcement, require edits to other checkers or autorun wiring or the work-order
template or the closed RSE documents, require the remaining T3 candidates,
require runtime/provider/public/session scope, touch forbidden paths, consume
secrets/quota, require a destructive action, or contradict this work order.
Worker-to-reviewer questions are routed to the reviewer/closer in the worker
return, not escalated to the operator.

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
- `Core Guard Self-Protection Authorization`
- `Machine Closure Package`
- actual `executionBaseHead`
- actual `git status --short`
- changed-path list
- focused test and gate evidence
- `WORKER_EXPERIENCE_RETRO` block or
  `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`

If any listed section is not applicable, include the section with `N/A with reason` or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it. The `Core Guard Self-Protection Authorization` section is required and must list both protected helper paths, because this changeset touches protected `governance/compat/` files.

## Execution Plan

1. Read required sources and record `executionBaseHead`.
2. Add a frozen advisory item dataclass mirroring `ReviewerReadoutItem`, a new
   field on `AssistReport` and key in `to_dict`, and a `_build_*` function that
   returns an empty tuple unless the changed range resolves to the worker-return
   shape and a changed worker-return has finding or gate-trap language without a
   `## Worker Return Jurisdiction Block`.
3. Add a human-output block for the new readout and serialize it in JSON.
4. Keep the diagnostic read-only: no closure decision, no new defect, no
   exit-nonzero change, no file write.
5. Add focused tests: positive case, negative case (block present),
   negative case (no finding or gate-trap language), read-only property by
   patching `builtins.open` to fail on any write mode, and the no-defect
   property.
6. Run required checks and create the worker-return artifact without committing.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `governance/compat/run_agent_automation_assist.py` | worker | add one read-only advisory diagnostic mirroring the existing readout pattern |
| `governance/compat/test_run_agent_automation_assist.py` | worker | add focused tests for the diagnostic |
| `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_WORKER_RETURN_2026-06-22.md` | worker | create |
| `docs/baselines/CVF_GC018_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_2026-06-22.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_FOR_WORKER_2026-06-22.md` | reviewer/closer | no worker edit |
| other `governance/compat/` checkers, autorun gate wiring, dispatch-quality checker, work-order template, closed RSE-T0/T1/T2 docs, `AGENTS.md`, `CVF_SESSION/**`, active handoff, runtime routes, web, MCP, provider registry, generated aggregates, public-sync, queue/daemon/watcher | out of worker scope | forbidden |

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
closure-blocking enforcement, edits to other checkers or autorun wiring or the
work-order template or the closed RSE documents, the remaining T3 candidates,
runtime/product behavior, generated aggregate edits, AGENTS/session/handoff
edits, provider/live/public-sync scope, dependency installation, secrets/quota,
destructive action, or a change to the claim boundary.

## Purpose

Add one bounded read-only diagnostic to the existing AAF helper that flags a
changed worker-return artifact which contains finding or gate-trap language but
lacks a `## Worker Return Jurisdiction Block`, so the omission surfaces early as
advisory output without blocking closure.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Roadmap author | roadmap author role |
| Dispatcher | dispatch author role |
| Work-order reviewer | work-order reviewer role before execution |
| Worker | diagnostic and focused test author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 open RSE-T3 read-only AAF-helper diagnostic, bounded first slice of one diagnostic | ACCEPT |
| RSE-T3 GC-018 | `docs/baselines/CVF_GC018_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_2026-06-22.md` | ACCEPT |
| RSE roadmap | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | ACCEPT |
| RSE-T2 addendum | `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | ACCEPT |
| L2A classification standard | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | ACCEPT |
| Existing AAF helper | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| Existing AAF helper tests | `governance/compat/test_run_agent_automation_assist.py` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- update `governance/compat/run_agent_automation_assist.py` to add one read-only
  advisory diagnostic flagging a changed worker-return with finding or gate-trap
  language but no `## Worker Return Jurisdiction Block`, populated only for the
  worker-return shape and derived from changed-file text already read;
- update `governance/compat/test_run_agent_automation_assist.py` with focused
  tests for the positive case, the two negative cases, the read-only property,
  and the no-defect property;
- create
  `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_WORKER_RETURN_2026-06-22.md`;
- reviewer/closer closure conversion may update
  `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_FOR_WORKER_2026-06-22.md`;
- reviewer/closer closure conversion may update
  `docs/baselines/CVF_GC018_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_2026-06-22.md`;
- reviewer/closer closure conversion may create
  `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_COMPLETION_2026-06-22.md`
  after accepting the worker return.

Forbidden scope:

- no closure-blocking enforcement, no new exit-nonzero defect class, and no
  change to existing enforce-mode defect behavior;
- no edit to other `governance/compat/` checkers, the autorun gate wiring, the
  dispatch-quality checker, or the work-order template;
- no edit to the closed RSE-T0 standard, RSE-T1 addendum, or RSE-T2 addendum;
- no implementation of the remaining four roadmap T3 candidate diagnostics;
- no staging, commit, push, closure decision, provider/live call, L3 apply, or
  arbitrary command execution;
- no runtime, web, CLI/MCP adapter, workspace, queue, daemon, watcher,
  public-sync, wrapper/proxy enforcement, direct interception, readiness, cost or
  speed claim, or universal governed-coding-control claim;
- no route schema edits, runtime/product behavior, dependency installation, or
  generated aggregate edits.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Roadmap T3 names the jurisdiction-block-missing diagnostic as a candidate | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | line 259 | T3 - Early Diagnostic / Checker Wire-In | RSE roadmap T3 section | ACCEPT |
| RSE-T2 addendum defines the Worker Return Jurisdiction Block the diagnostic detects | `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | line 51 | The Worker Return Jurisdiction Block | RSE-T2 addendum | ACCEPT |
| AAF helper has a read-only advisory readout item dataclass to mirror | `governance/compat/run_agent_automation_assist.py` | line 487 | ReviewerReadoutItem | AAF helper readout item | ACCEPT |
| AAF helper builds a read-only readout only for the reviewer-return shape | `governance/compat/run_agent_automation_assist.py` | line 708 | _build_reviewer_readout | AAF helper readout builder | ACCEPT |
| AAF helper assembles the report in build_report | `governance/compat/run_agent_automation_assist.py` | line 867 | build_report | AAF helper report assembly | ACCEPT |
| AAF helper reads changed-file text without a runtime call | `governance/compat/run_agent_automation_assist.py` | line 197 | _read_changed_text | AAF helper changed-text reader | ACCEPT |
| AAF helper has a focused readout test class to mirror | `governance/compat/test_run_agent_automation_assist.py` | line 830 | ReviewerReadoutTests | AAF helper test module | ACCEPT |
| L2A safety level L0 is a read-only suggestion that changes nothing | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | line 104 | L0 read-only suggestion | L2A Acceleration Safety Levels | ACCEPT |

## New Helper Terms

| Proposed term | Owner in RSE-T3 | Runtime status | Reason |
|---|---|---|---|
| `jurisdictionReadout` | RSE-T3 helper output | NEW_HELPER_OUTPUT_FIELD | names the read-only advisory list flagging worker-returns missing a jurisdiction block |
| `JurisdictionReadoutItem` | RSE-T3 helper dataclass | NEW_HELPER_DATACLASS | a frozen advisory item with text fields only, mirroring ReviewerReadoutItem |

The worker may use a source-verified equivalent name if it mirrors the existing
read-only readout pattern. No checker key, exit code, or enforce-mode defect is
created by RSE-T3.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap item | Source | Work-order coverage | Evidence requirement |
|---|---|---|---|
| T3 jurisdiction-block-missing diagnostic | roadmap line 259 | implemented as a read-only readout | focused tests and worker return |
| T3 read-only acceptance criterion | roadmap line 277 | diagnostic edits no file and makes no closure decision | read-only focused test |
| remaining four T3 candidates | roadmap line 259 | excluded from this slice | claim boundary and no code for them |
| machine enforcement | roadmap line 277 | excluded; advisory only | claim boundary |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | local governed role-boundary protocol route, not external authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; pre-dispatch autorun |
| Owner surface | RSE-T3 Jurisdiction Block Diagnostic |
| Disposition | ADAPT as a CVF-owned read-only diagnostic with bounded scope |
| Claim boundary | operator critique remains input only until implemented and closed through this governed work order |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/run_agent_automation_assist.py`; `governance/compat/test_run_agent_automation_assist.py` |
| Runtime behavior claimed | N/A_WITH_REASON: governance compatibility helper only; no product runtime, provider route, web route, CLI/MCP adapter, or Learning Plane mutation |
| Helper/checker implementation claimed | BOUNDED: add one read-only advisory readout diagnostic and focused tests |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded read-only helper diagnostic only; no provider, public-sync, runtime product behavior, enforcement, or generated aggregate behavior is claimed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | RSE-T3 read-only jurisdiction block diagnostic |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | explicit helper invocation only; advisory readout output |
| interceptionBoundary | no IDE, shell, git, filesystem, or provider interception claim |
| claimLanguage | read-only advisory diagnostic only |
| forbiddenExpansion | closure-blocking enforcement, new exit-nonzero defect, other checker edits, autorun wiring change, remaining T3 candidates, L3 apply, provider/live, public-sync, queue/daemon/watcher, direct interception, readiness, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker returns with findings can omit the jurisdiction block, leaving routing implicit | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | RSE-T3 adds a read-only diagnostic flagging the omission | handled by this dispatch |
| The remaining four roadmap T3 diagnostics are not yet implemented | RULE_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | a later RSE-T3 slice may add them with fresh authorization | deferred |
| Closure-blocking enforcement of the jurisdiction block | CONTROL_PROOF_GAP | GOVERNANCE_CONTROL_PLANE | OUT_OF_SCOPE | enforcement remains out of scope; advisory only | deferred |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime, provider, or cost behavior changed or claimed | handled |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded read-only
  diagnostic tranche.
- Corpus root: repo-local files named in Authority Chain and Source
  Verification Block.
- Snapshot time: 2026-06-22 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus `rg --files --hidden --no-ignore` for targeted confirmation.
- Manifest artifact or inline manifest: Authority Chain and Source
  Verification Block in this work order.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows
  in this work order.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=Authority Chain and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo sweep, generated aggregate mutation, runtime/provider/web/MCP/public-sync sweep; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: full-repo sweep, generated aggregate mutation,
  runtime/provider/web/MCP/public-sync sweep, public-sync proof, provider/live
  proof.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by dispatch.
- Drift check: N/A with reason: no generated aggregate edited by dispatch.
- Output traceability: RSE-T3 work order maps one roadmap T3 candidate diagnostic
  to worker deliverables and required gates.
- Adversarial verification: source rows distinguish the read-only diagnostic from
  closure-blocking enforcement and from the deferred candidates.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one read-only advisory diagnostic to the
existing AAF helper and add focused tests for it, without adding any
closure-blocking enforcement, new exit-nonzero defect class, patch apply, closure
decision, staging, commit, push, provider or live, or runtime behavior.

Protected paths:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator directed RSE-T2 closed and chose to open
RSE-T3 as a read-only AAF-helper diagnostic with a bounded first slice of one
diagnostic. This work order authorizes only that scope.

Rollback boundary: revert the accepted RSE-T3 material closure commit to remove
the read-only diagnostic and its focused tests together.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | N/A with reason: extends two existing helper files; creates no new durable foundation directory and relocates nothing. |
| New durable foundation directory | N/A with reason |
| Generated aggregate impact | N/A with reason: no generated aggregate is created or edited. |
| INDEX impact | N/A with reason: this is not an INDEX artifact or INDEX storage tranche. |
| Guard owner | reviewer/closer verifies the diagnostic is read-only and the changed set stays within the two helper files plus the worker return. |

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
- explicit statement that the diagnostic emits an advisory item for a
  block-missing worker-return and none when the block is present or no finding or
  gate-trap language exists;
- explicit statement that the diagnostic makes no closure decision, writes no
  file, adds no exit-nonzero defect, and changes no existing enforce-mode
  behavior;
- a `Core Guard Self-Protection Authorization` block listing both protected
  helper paths;
- explicit statement that no other checker, autorun wiring, work-order template,
  closed RSE document, remaining T3 candidate, runtime, provider/live,
  public-sync, generated aggregate, or session/handoff path was edited;
- exact claim boundary and public export disposition.

## Review Gate

Reviewer/closer must inspect the worker-return changed set against Required
Deliverables, run reviewer-fast gates, verify no forbidden scope was touched,
verify the diagnostic is read-only and advisory with no enforcement, verify the
focused tests cover the positive and negative cases and the read-only property,
verify the Core Guard Self-Protection block lists both protected paths, and only
then convert accepted material into a completion review.

## Closure Checklist

- [x] Worker returned `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
- [x] Changed files stay inside Required Deliverables.
- [x] The diagnostic emits an advisory item for a block-missing worker-return.
- [x] The diagnostic emits nothing when the block is present or no finding or gate-trap language exists.
- [x] The diagnostic makes no closure decision, writes no file, and adds no exit-nonzero defect.
- [x] Focused tests cover positive, negative, read-only, and no-defect cases.
- [x] The worker return carries a Core Guard Self-Protection block listing both protected paths.
- [x] No other checker, autorun wiring, work-order template, or closed RSE document changed.
- [x] Worker-return fast gate passes or records `BLOCKED_WITH_REASON`.
- [x] Reviewer-owned completion review created if accepted.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all required deliverables are present,
required checks have been run or source-blocked with evidence, and changed files
remain inside Allowed scope.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, or the repair would require forbidden
enforcement, other-checker, autorun-wiring, closed-RSE-edit, remaining-T3,
runtime, provider, public, or session scope.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | The helper emits a read-only advisory item when a changed worker-return contains finding or gate-trap language but lacks a `## Worker Return Jurisdiction Block` | source diff and focused test |
| AC2 | The helper emits no such item when the block is present or no finding or gate-trap language exists | focused tests |
| AC3 | The diagnostic makes no closure decision, writes no file, adds no exit-nonzero defect, and changes no existing enforce-mode behavior | diff review and focused test |
| AC4 | Focused tests cover positive, negative, read-only, and no-defect cases | test results |
| AC5 | The worker return carries a Core Guard Self-Protection block listing both protected paths and no forbidden paths changed | `git status --short`; diff; worker return |
| AC6 | Worker return contains required packet shape and no commit | worker-return gate |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: RSE-T3 is private provenance governance-helper work. No public-sync
repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local workspace |
| Session or invocation | RSE-T3 worker execution, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, focused source and test edits, required gates |
| Target paths | worker required deliverables |
| Allowed scope source | this work order and paired GC-018 baseline |
| Before status evidence | dispatchBaseHead `31faa6bc`; clean worktree verified before RSE-T3 dispatch authoring |
| After status evidence | RSE-T3 worker artifacts pending no-commit return |
| Diff evidence | worker records `git status --short` and gate receipts |
| Approval boundary | worker may update Required Deliverables but must not commit |
| Claim boundary | read-only diagnostic only; no enforcement, runtime, provider, or public behavior |
| Agent type | worker role |
| Invocation ID | `rse-t3-jurisdiction-block-diagnostic-worker-2026-06-22` |
| Expected manifest | helper source; focused tests; worker return |
| Actual changed set | worker records in return packet |
| Manifest delta | worker records in return packet |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED`; checklist checked | PASS |
| Worker return | `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_WORKER_RETURN_2026-06-22.md` | `Status: COMPLETE_PENDING_REVIEW` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_RSE_T3_JURISDICTION_BLOCK_DIAGNOSTIC_COMPLETION_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | roadmap remains `ROADMAP_READY_FOR_WORK_ORDER_AUTHORING`; T3 closed by completion review | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | aggregate drift check passes; no mutation required | PASS |
| Registry Markdown | `docs/reference/role_switch_envelope/README.md` | active RSE reference front door remains present and unchanged | PASS |
| External evidence digest | N/A | no external evidence digest created or consumed | N/A with reason |
| System loop interlock | N/A | no system-loop interlock surface changed | N/A with reason |
| Runtime/provider/live evidence | N/A | no runtime/provider/live behavior | N/A with reason |
| Public-sync evidence | N/A | no public-sync authorized | N/A with reason |
| Session continuity | active session front-door, state, and handoff | separate session-sync follows material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Receipt/query acceptance evidence | N/A with reason: no receipt/query surface | PASS |
| Runtime receipt value | N/A with reason: no runtime execution | PASS |
| Delta receipt value | N/A with reason: no Delta execution claim | PASS |

## Claim Boundary

This work order authorizes only one bounded RSE-T3 read-only advisory diagnostic
added to the existing AAF helper plus focused tests. It does not authorize
closure-blocking enforcement, a new exit-nonzero defect class, any change to
existing enforce-mode behavior, edits to other checkers or the autorun wiring or
the work-order template, edits to the closed RSE-T0, RSE-T1, or RSE-T2 documents,
the remaining roadmap T3 candidate diagnostics, L3 apply, runtime behavior,
provider/live behavior, CLI/MCP adapter behavior, public-sync, session-sync by
the worker, direct interception, readiness claims, speed/cost claims, or
universal governed-coding control.
