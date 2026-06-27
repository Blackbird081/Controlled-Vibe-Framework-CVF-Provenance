# CVF Agent Work Order - REF-T0 Active Reference Path Repair

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: work_order

dispatchBaseHead: 938cfb2d

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_FOR_WORKER_2026-06-22.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: L2A-T0 is closed at `bf0c9de1`, and session continuity is
synced at `938cfb2d`. The operator approved repairing active reference path
drift before AAF-T6A. REF-T0 is reference-lifecycle repair only.

Do-not-misread notes: do not edit AGENTS, session state, active handoff,
governance/compat, runtime, provider, web, MCP, generated JSON aggregates,
public-sync, queue, daemon, watcher, wrapper/proxy, direct interception,
arbitrary command execution, or EDIT/COMMIT execution. Do not implement AAF-T6A
or AAF-T7A. Do not delete archive files.

Required first actions: read this work order, read the REF-T0 GC-018 baseline,
read the Guard Orientation Index, inspect the two archive source files, verify
the two active paths are still missing at worker start, confirm actual
`executionBaseHead`, and inspect current `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only the required
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
source inventory, scan-depth ledger, focused gate evidence, and no commit. If
blocked, return `BLOCKED_WITH_REASON` and name the exact source or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator critique about active reference files stored only in archive |
| Intake role | worker restores active reference copies and one pointer |
| Reviewer role | reviewer/closer validates path restoration and claim boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; reference lifecycle repair only |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if semantic rewrite, archive deletion, AGENTS/session edit, checker/helper/runtime/public/provider scope is required |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | REF-T0 repairs active placement of already governed reference standards; it is not a new `.private_reference/legacy` absorption scan or knowledge extraction tranche. |
| Coverage evidence used instead | AGENTS active path references, active session state pointer, archive source file existence, and active-path missing evidence. |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatcher creates packet; worker restores active reference copies and return packet; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=938cfb2d`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending REF-T0 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix REF-T0 with AAF-T6A, AAF-T7A, MPI-T3/T4, helper/checker implementation, runtime/provider/live, MCP adapter, public-sync, queue/daemon, direct-interception, or generated aggregate work |
| Before status evidence | dispatchBaseHead `938cfb2d`; clean worktree verified before REF-T0 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted active reference copies; accepted L2A pointer update; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and worker-return packet shape |
| `docs/baselines/CVF_GC018_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_2026-06-22.md` | GC-018 authorization and claim boundary |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_FOR_WORKER_2026-06-22.md` | current work order and allowed scope |
| `docs/reference/archive/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | source content for active autorun standard restoration |
| `docs/reference/archive/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | source content for active learning-philosophy restoration |
| `docs/reference/learning_to_acceleration/README.md` | pointer to update from archive to active path |

## Pre-Flight Checks

The worker must run or record these checks before returning:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_automation_assist.py --base 938cfb2d --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | worker | create active copy from archive source |
| `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | worker | create active copy from archive source |
| `docs/reference/learning_to_acceleration/README.md` | worker | update one related-surface pointer to active path |
| `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_WORKER_RETURN_2026-06-22.md` | worker | create |
| `docs/baselines/CVF_GC018_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_2026-06-22.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_FOR_WORKER_2026-06-22.md` | reviewer/closer | no worker edit |
| `AGENTS.md`, `CVF_SESSION/**`, active handoff, `governance/compat/**`, runtime routes, web, MCP, generated aggregates, public-sync, archive files | out of worker scope | forbidden |

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
semantic rewrites, deleting archive files, editing AGENTS/session/handoff,
checker/helper implementation, runtime routes, MCP/provider/live/public scope,
dependency installation, secrets/quota, destructive action, or a change to the
claim boundary.

## Purpose

Restore active reference paths for two still-binding standards currently stored
only in `docs/reference/archive/`, then update the L2A front-door pointer so
future workers can cite active paths before AAF-T6A starts.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | dispatch author role |
| Worker | active reference path repair author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 repair active/reference archive drift before AAF-T6A | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| REF-T0 GC-018 | `docs/baselines/CVF_GC018_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_2026-06-22.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Root agent instructions | `AGENTS.md` | ACCEPT |
| Archive source files | `docs/reference/archive/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`; `docs/reference/archive/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`;
- create `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`;
- update `docs/reference/learning_to_acceleration/README.md` with a compact
  active-path pointer correction;
- create `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_WORKER_RETURN_2026-06-22.md`;
- reviewer/closer closure conversion may update this work order, the GC-018
  baseline, and create
  `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_COMPLETION_2026-06-22.md`.
- reviewer/closer closure conversion may update
  `docs/baselines/CVF_GC018_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_2026-06-22.md`,
  this work order, and `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`
  only to record accepted closure and active-window protection for the two
  restored binding references.

Forbidden scope:

- no edits to `AGENTS.md`, `CVF_SESSION/**`, active handoff,
  `governance/compat/**`, archive files, archive index, runtime/provider/web,
  MCP, dependency manifests, generated aggregates, public-sync, queue, daemon,
  watcher, wrapper/proxy, direct IDE/shell/git/filesystem interception,
  arbitrary command execution, or EDIT/COMMIT execution;
- no semantic rewrite of the restored standards;
- no AAF-T6A, AAF-T7A, MPI-T3/MPI-T4, checker/helper/scaffold/patch behavior,
  provider/live proof, public-sync, readiness, speed/cost, or universal
  governed-coding-control claim.

Risk ceiling: R0/R1 documentation/reference lifecycle repair only.

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Verify active paths are missing and archive sources exist at worker start.
3. Create active copies from the archive source files, preserving content.
4. Update the L2A README related-surface pointer from archive path to active
   learning-philosophy path.
5. Create the worker-return artifact with required packet shape and
   worker-experience token.
6. Run required commands and record results.

## Worker Return Packet Shape Contract

The worker-return artifact must include these sections or exact N/A-with-reason
dispositions where listed:

| Packet item | Worker-return disposition |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| `executionBaseHead` | exact value from `git rev-parse --short HEAD` at worker start |
| `dispatchBaseHead` | `938cfb2d` |
| `git status --short` | exact output after worker changes |
| Purpose section | MUST_INCLUDE |
| Scope / Methodology section | MUST_INCLUDE |
| Findings / Position section | MUST_INCLUDE |
| Risk / Corrective Action section | MUST_INCLUDE |
| Claim Boundary section | MUST_INCLUDE |
| Agent Operation Trace Block section | MUST_INCLUDE |
| Delta Execution Claim Boundary Control Block section | MUST_INCLUDE |
| Public Export Disposition section | MUST_INCLUDE |
| External Knowledge Intake Routing section | MUST_INCLUDE |
| Rescan Intelligence Hardening section | MUST_INCLUDE |
| Corpus Completeness And Report Integrity section | MUST_INCLUDE |
| Finding-To-Governance Learning Disposition section | MUST_INCLUDE |
| Epistemic Process Block section | MUST_INCLUDE_OR_EPISTEMIC_PROCESS_NA_WITH_REASON |
| Machine Closure Package section | MUST_INCLUDE_OR_NA_WITH_REASON; worker must not mark closure |
| Worker-experience token | structured `WORKER_EXPERIENCE_RETRO` or exact asserting `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` |

The worker must not record a clean `git status --short` when the worker-return
file or other deliverables are untracked or modified.

Conditional sections that do not apply must still be present with `N/A with
reason` or `NOT_APPLICABLE_WITH_REASON` rows.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-gate, reference wording,
packet-shape, source-inventory, corpus-integrity, and text-encoding defects
without asking the operator. Ask the operator only if remediation would exceed
Allowed scope, change the claim boundary, edit AGENTS/session/handoff, delete
archive files, implement a helper or checker, touch forbidden paths, run
provider/live/public-sync work, install dependencies, consume secrets/quota, or
perform destructive actions.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AGENTS names the autorun workflow standard at active reference path | `AGENTS.md` | Mandatory Agent Autorun Workflow Control section | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | root agent instructions | ACCEPT |
| AGENTS names the agent-error learning philosophy at active reference path | `AGENTS.md` | Mandatory Agent Autorun Workflow Control section | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | root agent instructions | ACCEPT |
| Active state names the agent-error learning philosophy at active path | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `agentErrorToGovernanceLearningPhilosophy` | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | active session state registry | ACCEPT |
| Autorun archive source exists | `docs/reference/archive/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | file existence and title | `CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | archive reference source | ACCEPT |
| Learning philosophy archive source exists | `docs/reference/archive/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | file existence and title | `CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | archive reference source | ACCEPT |

## New Doc-Only Fields

| Field or term | Disposition |
|---|---|
| `Active Reference Path Repair` | New reference-lifecycle dispatch term, not a runtime field |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work-order instruction | Verification |
|---|---|---|
| Operator says important active files in archive should be restored active | create active copies from archive sources | reviewer checks changed set and file existence |
| AAF-T6A should not build on drifted active authority paths | REF-T0 precedes AAF-T6A | session next-move and closure review |
| Do not rewrite history | preserve archive files; do not delete or move them | git diff review |
| Keep scope narrow | no AGENTS/session/runtime/helper/checker edits by worker | git status and gates |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator critique about active/archive misclassification to governed reference repair |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; reviewer-fast gate |
| Owner surface | REF-T0 active reference path repair |
| Disposition | ADAPT as CVF-owned reference lifecycle repair |
| Claim boundary | operator/external critique remains input only until promoted through this governed dispatch |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | N/A with reason: REF-T0 repairs documentation/reference file placement only |
| Runtime behavior claimed | N/A_WITH_REASON |
| Helper/checker implementation claimed | N/A_WITH_REASON |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are out of scope and untouched; REF-T0 makes no provider registry absence, hardcoded-provider, provider-selection, or live-governance claim |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - no runtime, provider, helper/checker, public-sync, generated aggregate, or provider registry behavior is claimed |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | active reference files under `docs/reference/` restored from archive source |
| Storage decision | preserve archive copies and create active copies because active authority surfaces cite active paths |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | reference lifecycle repair only; no hidden state store |

## Corpus Completeness And Report Integrity

- Corpus task class: work-order dispatch source verification for bounded active reference path repair.
- Corpus root: repo-local source files named in Required First Reads and Source Verification Block.
- Snapshot time: 2026-06-22 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus targeted `rg -n` and `Test-Path` checks.
- Manifest artifact or inline manifest: Required First Reads and Source Verification Block in this work order.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=Required First Reads and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo scan, semantic rewrite, generated registry mutation, runtime/provider/web/MCP/public-sync scan; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no full `.private_reference/legacy` scan, no runtime/provider/web/MCP/public-sync corpus scan, no archive deletion.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by dispatch.
- Drift check: N/A with reason: no generated aggregate edited by dispatch.
- Output traceability: REF-T0 work order maps active/archive drift finding to worker deliverables.
- Adversarial verification: active missing/archive exists condition was checked before dispatch.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Active authority paths can drift into archive-only storage | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_UPDATED | REF-T0 restores active copies for binding references | handled by worker if complete |
| Future INDEX/lifecycle enforcement may need a checker for active path drift | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | consider a later checker after REF-T0 if the pattern recurs | deferred |
| Runtime/provider/cost applicability for this work order | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: operator critique about active files incorrectly
  living in archive.
- Predecessor intake artifact: L2A-T0 closure and current active startup
  surfaces.
- Delta ledger status: `CHANGED_DISPOSITION` because a dispatch note becomes a
  repair work order before AAF-T6A.
- Routing matrix status: `DO_NOW` for REF-T0; `DEFER` for AAF-T6A until REF-T0
  closure; `SEPARATE_RUNTIME_TRANCHE` for any checker/helper implementation.
- Semantic sampling status: sampled AGENTS, ACTIVE_SESSION_STATE, archive
  source files, and L2A README pointer.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | The two standards remain binding reference concepts. |
| CHANGED_DISPOSITION | Archive-only placement is treated as active reference drift to repair. |
| NEW_FINDING | Active-path references need filesystem-backed existence before future dispatches cite them. |
| REMOVED_OR_REJECTED | Deleting archive copies, rewriting semantics, and checker/helper implementation remain rejected. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | Restore active copies for the two binding standards and update L2A pointer. |
| RESOLVED_BY_DESIGN | Preserve archive copies as historical records; create active copies for active authority paths. |
| DEFER | AAF-T6A early diagnostic wire-in remains deferred until `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_COMPLETION_2026-06-22.md` records a reviewer disposition. |
| STRATEGIC_OPERATOR_DECISION | Operator decides once `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_COMPLETION_2026-06-22.md` exists whether to proceed to AAF-T6A immediately or inspect additional active/archive drift first. |
| SEPARATE_RUNTIME_TRANCHE | checker/helper/scaffold/patch/apply/runtime/provider/public-sync behavior. |
| OUT_OF_SCOPE | public-sync, provider/live proof, direct interception, universal control, MPI continuation during REF-T0. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| REF-T0-WO-RS1 | AGENTS autorun section | active standard paths are canonical | DO_NOW | Should worker only cite archive path? | PASS - active copy should be restored |
| REF-T0-WO-RS2 | archive source files | archived standards still exist | DO_NOW | Should archive files be moved/deleted? | PASS - preserve archive and create active copy |
| REF-T0-WO-RS3 | L2A README related surface | pointer currently uses archive path | DO_NOW | Should closed L2A be left stale? | PASS - narrow pointer update is allowed |

## Machine Closure Package

Worker return must include a Machine Closure Package section but must not mark
REF-T0 closed. Use pending-review or N/A-with-reason dispositions for closure
items the worker cannot own.

Reviewer/closer owns the final closure package in the completion review.

Reviewer/closer conversion result: worker returned `COMPLETE_PENDING_REVIEW`;
reviewer accepted the bounded active-path repair and converted REF-T0 to
`CLOSED_PASS_BOUNDED`.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_WORKER_RETURN_2026-06-22.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by reviewer/closer | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_REF_T0_ACTIVE_REFERENCE_PATH_REPAIR_COMPLETION_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Active autorun standard | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | active copy exists from archive source, plus one non-semantic gate NA line | PASS |
| Active learning philosophy | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | active copy exists from archive source, plus one non-semantic gate NA line | PASS |
| L2A pointer | `docs/reference/learning_to_acceleration/README.md` | related-surface pointer uses the active learning-philosophy path | PASS |
| Roadmap state | N/A | no roadmap status is changed by REF-T0 closure | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no registry JSON mutation; drift gate passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/registry/` | no registry source or Markdown mutation | PASS |
| External evidence digest | N/A | no external benchmark/provider/live digest created | N/A with reason |
| System loop interlock | N/A | no runtime/source interlock changed | N/A with reason |
| Session continuity | active session front-door/state/handoff | session-sync follows material closure commit | N/A with reason |
| Active window registry | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` | two restored binding active references registered as `PERMANENT_ACTIVE_WINDOW` so active/archive hygiene does not treat them as stale cleanup candidates | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Worker-return packet status | `COMPLETE_PENDING_REVIEW` | PASS |
| Active autorun standard | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` exists | PASS |
| Active learning philosophy | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` exists | PASS |
| Archive preservation | both source files under `docs/reference/archive/` remain unchanged | PASS |
| L2A pointer | related-surface pointer uses the active learning-philosophy path | PASS |
| Provider registry behavior | N/A with reason: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are untouched and not evidence for REF-T0 | N/A_WITH_REASON |
| Runtime/provider/live evidence | N/A with reason: REF-T0 creates no runtime/provider/live behavior | N/A_WITH_REASON |
| Public export evidence | N/A with reason: no public-sync authorized | N/A_WITH_REASON |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: register the two restored REF-T0 active
reference standards in `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` as
permanent active windows so the active archive hygiene gate recognizes their
binding active paths.

Protected path:

- `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`

Operator authorization: the operator directed that important active reference
files incorrectly stored under archive should be restored to active state.
REF-T0 closure applies that decision to the active-window registry without
changing active archive checker semantics.

Rollback boundary: revert the REF-T0 material closure commit to remove the two
active-window entries and restored active reference copies together.

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- source inventory and scan-depth ledger;
- changed-path list;
- active-path missing/archive-source exists verification at worker start;
- AAF helper smoke result with `--json --enforce`;
- worker-return fast gate result;
- explicit statement that archive files were preserved;
- explicit statement that no AGENTS/session/handoff/governance/compat/runtime/
  public/provider/MCP/generated path was edited;
- exact claim boundary and public export disposition.

## Review Gate

Reviewer/closer must inspect the worker-return changed set against Required
Deliverables, run reviewer-fast gates, verify no forbidden scope was touched,
and only then convert accepted material into a completion review.

## Closure Checklist

- [x] Worker returned `COMPLETE_PENDING_REVIEW`.
- [x] Changed files stay inside Required Deliverables.
- [x] Active copies exist for both restored standards.
- [x] Archive copies remain unchanged.
- [x] L2A README pointer update is narrow.
- [x] No AGENTS/session/handoff/governance/compat/runtime/public/provider path changed.
- [x] Worker-return fast gate passes.
- [x] Reviewer-owned completion review created.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all required deliverables are present,
required checks have been run or source-blocked with evidence, and changed files
remain inside Allowed scope.

Return `BLOCKED_WITH_REASON` when a required archive source is missing, a
required active-copy restoration cannot be performed inside Allowed scope, a
required gate cannot pass inside Allowed scope, or the repair would require
forbidden implementation/session/public/provider scope.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | Active autorun workflow standard copy exists under `docs/reference/` | changed set and file existence |
| AC2 | Active agent-error learning philosophy copy exists under `docs/reference/` | changed set and file existence |
| AC3 | Archive copies are preserved | git diff review |
| AC4 | L2A README uses active learning-philosophy path | diff review |
| AC5 | No forbidden paths changed | `git status --short`; diff |
| AC6 | Worker return contains required packet shape and no commit | worker-return gate |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: REF-T0 is private provenance reference-lifecycle repair work. No
public-sync repository work or public catalog claim is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | REF-T0 active reference path repair worker execution |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | governed documentation/reference lifecycle repair only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | active reference path repair only |
| forbiddenExpansion | helper/checker/scaffold implementation, patch application, wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local workspace |
| Session or invocation | REF-T0 worker execution, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, file creation, required gates |
| Target paths | worker required deliverables |
| Allowed scope source | this work order and paired GC-018 baseline |
| Before status evidence | dispatchBaseHead `938cfb2d`; clean worktree verified before REF-T0 dispatch authoring |
| After status evidence | REF-T0 worker artifacts pending no-commit return |
| Diff evidence | worker records `git status --short` and gate receipts |
| Approval boundary | worker may create/update Required Deliverables but must not commit |
| Claim boundary | reference lifecycle repair only; no helper/checker/runtime implementation |
| Agent type | worker role |
| Invocation ID | `ref-t0-active-reference-path-repair-worker-2026-06-22` |
| Expected manifest | active autorun standard; active learning philosophy; L2A README pointer; worker return |
| Actual changed set | worker records in return packet |
| Manifest delta | worker records in return packet |

## Claim Boundary

This work order authorizes only REF-T0 active reference path repair. It does
not authorize semantic standard rewrites, archive deletion, checker/helper/
scaffold implementation, patch preview/apply behavior, autorun/hook wiring,
runtime behavior, provider/live behavior, CLI/MCP adapter behavior,
public-sync, session-sync by worker, direct interception, readiness claims,
speed/cost claims, or universal governed-coding control.
