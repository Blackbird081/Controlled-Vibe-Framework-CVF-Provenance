# CVF Agent Work Order - AAF-T6A Early Diagnostic Wire-in

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: work_order

dispatchBaseHead: d11e0522

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_FOR_WORKER_2026-06-22.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: REF-T0 closed at material commit `8e024b2f` and session
continuity is synced at `d11e0522`. AAF-T6A is the next authorized learning
tranche. MPI work remains paused until this learning lane checkpoint is handled.

Do-not-misread notes: do not implement full AAF-T6 Guard Orientation
Read-Receipt Gate. Do not implement AAF-T7A acceleration helper. Do not build a
scaffold generator, patch preview/apply helper, runtime Learning Plane mutation,
provider/live proof, CLI/MCP adapter behavior, public-sync, queue, daemon,
watcher, wrapper/proxy, direct IDE/shell/git/filesystem interception, arbitrary
command execution, EDIT/COMMIT execution, durable store, readiness, cost/speed,
or universal governed-coding-control claim.

Required first actions: read this work order, read the AAF-T6A GC-018 baseline,
read the Guard Orientation Index, inspect the existing AAF helper and autorun
gate insertion point, confirm actual `executionBaseHead`, and inspect current
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
| Intake source | operator critique that late B19-B22 style defects need proactive helper reminders |
| Intake role | worker wires existing AAF helper into pre-implementation autorun and tests it |
| Reviewer role | reviewer/closer validates helper placement, focused tests, and claim boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; guard wiring only |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation would require full read-receipt, AAF-T7A, scaffold, patch/apply, provider/live, public-sync, runtime/product, CLI/MCP adapter, arbitrary command, or forbidden path scope |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | AAF-T6A wires existing repo-local AAF helper diagnostics into autorun. It is not a `.private_reference/legacy` scan or memory-plane absorption tranche. |
| Coverage evidence used instead | autorun standard, learning philosophy, existing helper CLI, and existing autorun gate source verification. |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatcher creates packet; worker wires guard helper and return packet; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=d11e0522`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending AAF-T6A artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix AAF-T6A with AAF-T7A, MPI-T3/T4, full AAF-T6 read-receipt, scaffold/patch/apply, runtime/provider/live, MCP adapter, public-sync, queue/daemon, direct-interception, generated aggregate, or memory-plane work |
| Before status evidence | dispatchBaseHead `d11e0522`; clean worktree verified before AAF-T6A dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted autorun gate source/test changes; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and worker-return packet shape |
| `docs/baselines/CVF_GC018_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_2026-06-22.md` | GC-018 authorization and claim boundary |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_FOR_WORKER_2026-06-22.md` | current work order and allowed scope |
| `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | pre-implementation phase authority |
| `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | earliest-applicable-gate learning authority |
| `governance/compat/run_agent_automation_assist.py` | existing read-only helper CLI and defect output |
| `governance/compat/run_agent_autorun_workflow_gate.py` | autorun command list and pre-implementation insertion point |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | focused test module to extend |

## Pre-Flight Checks

The worker must run or record these checks before returning. For commands that
use `<executionBaseHead>`, replace it with the exact value returned by
`git rev-parse --short HEAD` at worker start.

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_run_agent_autorun_workflow_gate
python -m unittest governance.compat.test_run_agent_automation_assist
python governance/compat/run_agent_automation_assist.py --base <executionBaseHead> --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_autorun_workflow_gate.py
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `governance/compat/run_agent_autorun_workflow_gate.py` | worker | update pre-implementation command list to invoke existing AAF helper read-only |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | worker | update focused tests for helper command inclusion and failure propagation |
| `governance/compat/test_run_agent_automation_assist.py` | worker | optional, only if needed for a focused helper contract fixture |
| `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_WORKER_RETURN_2026-06-22.md` | worker | create |
| `docs/baselines/CVF_GC018_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_2026-06-22.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_FOR_WORKER_2026-06-22.md` | reviewer/closer | no worker edit |
| `AGENTS.md`, `CVF_SESSION/**`, active handoff, runtime routes, web, MCP, provider registry, generated aggregates, public-sync, queue/daemon/watcher, wrapper/proxy, scaffold/patch/apply files | out of worker scope | forbidden |

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
full read-receipt proof, AAF-T7A acceleration, scaffold/patch/apply behavior,
runtime/product behavior, generated aggregate edits, AGENTS/session/handoff
edits, provider/live/public-sync scope, dependency installation, secrets/quota,
destructive action, or a change to the claim boundary.

## Purpose

Wire the existing read-only AAF helper into the `pre-implementation` autorun
phase so known helper-detectable worker-return and packet-shape defects are
surfaced before a worker writes material files.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | dispatch author role |
| Worker | guard wiring and focused test author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 create AAF-T6A Early Diagnostic Wire-in work order | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T6A GC-018 | `docs/baselines/CVF_GC018_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_2026-06-22.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Autorun workflow standard | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | ACCEPT |
| Agent-error learning philosophy | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | ACCEPT |
| Existing AAF helper | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| Existing autorun gate | `governance/compat/run_agent_autorun_workflow_gate.py` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- update `governance/compat/run_agent_autorun_workflow_gate.py` so
  `phase == "pre-implementation"` invokes:
  `python governance/compat/run_agent_automation_assist.py --base <base> --head <head> --json --enforce`;
- update `governance/compat/test_run_agent_autorun_workflow_gate.py` with
  focused tests proving placement and failure propagation;
- update `governance/compat/test_run_agent_automation_assist.py` only if
  needed for a focused fixture or helper-contract assertion;
- create
  `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_WORKER_RETURN_2026-06-22.md`.
- reviewer/closer closure conversion may update
  `docs/baselines/CVF_GC018_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_2026-06-22.md`,
  this work order, and create
  `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_COMPLETION_2026-06-22.md`
  after accepting the worker return.

Forbidden scope:

- no full AAF-T6 Guard Orientation Read-Receipt Gate;
- no AAF-T7A reviewer/closer acceleration helper;
- no ledger store, source directory, generator, drift checker, durable store,
  runtime Learning Plane mutation, provider/live proof, CLI/MCP adapter
  behavior, public-sync, wrapper/proxy enforcement, direct IDE/shell/git/
  filesystem interception, arbitrary command execution, EDIT/COMMIT execution,
  queue, daemon, watcher, readiness, full-hook equivalence, cost optimization
  claim, or universal governed-coding-control claim;
- no scaffold template generator, patch preview/apply, helper mutation,
  route schema edits, runtime/product behavior, dependency installation, or
  generated aggregate edits.

Risk ceiling: R0/R1 guard wiring and focused tests only.

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Inspect existing helper CLI and autorun `pre-implementation` insertion
   branch.
3. Add the existing helper command to the pre-implementation autorun command
   list with `--json --enforce`.
4. Add focused tests proving command placement and failure propagation through
   the existing gate result aggregation.
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
| `dispatchBaseHead` | `d11e0522` |
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

Within Allowed scope, the worker must repair machine-gate, source-inventory,
packet-shape, test, corpus-integrity, and text-encoding defects without asking
the operator. Ask the operator only if remediation would exceed Allowed scope,
change the claim boundary, edit AGENTS/session/handoff, implement full
read-receipt/scaffold/patch/apply/runtime/provider/public behavior, touch
forbidden paths, install dependencies, consume secrets/quota, or perform
destructive actions.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Pre-implementation is the autorun phase before file edits | `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md` | lines 62, 145-148, 210 | `pre-implementation` | autorun workflow standard | ACCEPT |
| Late machine checks should move into earliest applicable autorun phase | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | line 78 | earliest applicable autorun phase gate | learning philosophy | ACCEPT |
| Existing autorun gate builds phase command list in `_run_phase` | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 578-619 | `_run_phase` | autorun gate runner | ACCEPT |
| Existing autorun gate has focused tests | `governance/compat/test_run_agent_autorun_workflow_gate.py` | file exists; test module | `test_range_shape_preflight_blocks_exact_manifest_session_mix` | unittest module | ACCEPT |
| Existing AAF helper supports JSON and enforce mode | `governance/compat/run_agent_automation_assist.py` | lines 839-877 | `--json`; `--enforce`; `report.defects` | AAF helper CLI | ACCEPT |
| Existing AAF helper emits defects and signal readout | `governance/compat/run_agent_automation_assist.py` | lines 491-532, 710-776 | `defects`; `signalReadout` | AAF helper report | ACCEPT |

## New Doc-Only Fields

| Field or term | Disposition |
|---|---|
| `Early Diagnostic Wire-in` | New AAF dispatch term, not a runtime/product field |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work-order instruction | Verification |
|---|---|---|
| Operator wants helper reminders before worker errors reach reviewer | wire existing AAF helper into pre-implementation autorun | focused autorun test and gate command output |
| CVF learning philosophy says late checks move to earliest applicable phase | use `pre-implementation` phase only | source verification and test |
| Keep claim narrow | forbid full AAF-T6, AAF-T7A, scaffold, patch/apply, runtime/provider/public scope | worker-return claim boundary and reviewer diff |
| Worker must not commit | `WORKER_MUST_NOT_COMMIT` route | git status and reviewer closure conversion |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator critique about late worker-return defects to governed early diagnostic wire-in |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; reviewer-fast gate |
| Owner surface | AAF-T6A Early Diagnostic Wire-in |
| Disposition | ADAPT as CVF-owned pre-implementation diagnostic wiring |
| Claim boundary | operator/external critique remains input only until promoted through this governed dispatch |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_automation_assist.py`; focused tests |
| Runtime behavior claimed | N/A_WITH_REASON: governance compatibility helper/gate invocation only; no product runtime, provider route, web route, CLI/MCP adapter, or Learning Plane mutation |
| Helper/checker implementation claimed | BOUNDED: invoke existing read-only helper from pre-implementation autorun and add focused tests |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are out of scope and untouched; AAF-T6A makes no provider registry absence, hardcoded-provider, provider-selection, or live-governance claim |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded governance helper/gate wiring only; no provider, public-sync, runtime product behavior, or generated aggregate behavior is claimed |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | governance compatibility helper/gate source and tests |
| Storage decision | reuse existing helper and autorun gate; no new source directory or store |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | read-only helper invocation only; no hidden state store |

## Corpus Completeness And Report Integrity

- Corpus task class: work-order dispatch source verification for bounded
  autorun helper wire-in.
- Corpus root: repo-local source files named in Required First Reads and Source
  Verification Block.
- Snapshot time: 2026-06-22 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus targeted
  `rg -n` checks.
- Manifest artifact or inline manifest: Required First Reads and Source
  Verification Block in this work order.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE.
- Reconciliation: manifest=Required First Reads and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo scan, generated registry mutation, runtime/provider/web/MCP/public-sync corpus scan; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no full `.private_reference/legacy` scan, no runtime/
  provider/web/MCP/public-sync corpus scan, no generated aggregate edit.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by dispatch.
- Drift check: N/A with reason: no generated aggregate edited by dispatch.
- Output traceability: AAF-T6A work order maps operator finding to worker
  deliverables.
- Adversarial verification: source lines identify existing helper CLI and
  autorun insertion point.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Repeated worker-return packet defects can be caught only late when AAF helper is optional | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_PROMOTED | Wire existing helper into pre-implementation autorun | handled by worker if complete |
| Agents need repeated-error acceleration, not only blocking gates | ACCELERATION_GAP | LEARNING_TO_ACCELERATION | SEPARATE_TRANCHE | AAF-T7A acceleration helper remains next after AAF-T6A | deferred |
| Full read-receipt proof would require a larger gate | CONTROL_PROOF_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | full AAF-T6 read-receipt gate remains parked unless separately authorized | deferred |
| Runtime/provider/cost applicability for this work order | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: operator critique and Claude report about B19-B22
  late defects and optional AAF diagnostics.
- Predecessor intake artifact: L2A-T0 closure, REF-T0 closure, existing AAF
  helper source, autorun standard, and learning philosophy.
- Delta ledger status: `CHANGED_DISPOSITION` because optional helper guidance
  becomes mandatory pre-implementation diagnostic wiring.
- Routing matrix status: `DO_NOW` for AAF-T6A; `DEFER` for AAF-T7A and full
  AAF-T6 read-receipt gate; `SEPARATE_RUNTIME_TRANCHE` for any provider,
  runtime, CLI/MCP, scaffold, patch, queue, watcher, or public-sync behavior.
- Semantic sampling status: sampled autorun phase standard, learning philosophy,
  existing helper CLI, and autorun gate insertion point.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | AAF helper remains read-only and local-diagnostic only. |
| CHANGED_DISPOSITION | Helper moves from opt-in command to pre-implementation autorun command. |
| NEW_FINDING | Focused autorun tests should prove the helper command appears only in pre-implementation common commands. |
| REMOVED_OR_REJECTED | Read-receipt proof, scaffold generation, patch/apply, runtime/provider/public behavior, and AAF-T7A acceleration are rejected from AAF-T6A. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | Wire read-only AAF helper into pre-implementation autorun and test command presence/failure propagation. |
| RESOLVED_BY_DESIGN | Existing helper already emits JSON, defects, and signal readout; AAF-T6A reuses it. |
| DEFER | AAF-T7A reviewer/closer acceleration helper and full AAF-T6 read-receipt gate. |
| STRATEGIC_OPERATOR_DECISION | Operator decides once AAF-T6A is closed whether AAF-T7A or MPI continuation comes next. |
| SEPARATE_RUNTIME_TRANCHE | runtime/product behavior, provider/live proof, CLI/MCP adapter behavior, scaffold generator, patch apply, queue/daemon/watcher, public-sync. |
| OUT_OF_SCOPE | direct interception, universal governed-coding control, speed/cost claims, durable memory store, Learning Plane runtime mutation. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T6A-WO-RS1 | Autorun standard `pre-implementation` | Worker runs this gate before material edits | DO_NOW | Should helper stay optional? | PASS - pre-implementation is earliest applicable phase |
| AAF-T6A-WO-RS2 | Learning philosophy | Late machine check should move earlier | DO_NOW | Should this wait for full read-receipt? | PASS - bounded helper wire-in is separable |
| AAF-T6A-WO-RS3 | AAF helper CLI | `--json --enforce` already exists | RESOLVED_BY_DESIGN | Should worker build a new helper? | PASS - reuse existing helper |
| AAF-T6A-WO-RS4 | Autorun gate `_run_phase` | phase-specific command insertion exists | DO_NOW | Should helper run in every phase? | PASS - work order limits it to pre-implementation |

## Machine Closure Package

Worker return must include a Machine Closure Package section but must not mark
AAF-T6A closed. Use pending-review or N/A-with-reason dispositions for closure
items the worker cannot own.

Reviewer/closer owns the final closure package in the completion review.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_WORKER_RETURN_2026-06-22.md` | `Status: COMPLETE_PENDING_REVIEW`; accepted by reviewer/closer | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AAF_T6A_EARLY_DIAGNOSTIC_WIRE_IN_COMPLETION_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Autorun gate source | `governance/compat/run_agent_autorun_workflow_gate.py` | helper command appears in pre-implementation branch; reviewer added package-import fallback | PASS |
| Focused tests | `governance/compat/test_run_agent_autorun_workflow_gate.py` | pytest focused tests pass 19/19; unittest import check succeeds | PASS |
| Runtime/provider/live evidence | N/A | no runtime/provider/live behavior authorized | N/A with reason |
| Public-sync evidence | N/A | no public-sync authorized | N/A with reason |
| Roadmap state | N/A | no roadmap status is changed by AAF-T6A closure | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | no registry JSON mutation; drift gate passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/registry/` | no registry source or Markdown mutation | PASS |
| External evidence digest | N/A | no external benchmark/provider/live digest created | N/A with reason |
| System loop interlock | N/A | no runtime/source interlock changed | N/A with reason |
| Session continuity | active session front-door/state/handoff | session-sync follows accepted material closure commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Worker-return packet status | `COMPLETE_PENDING_REVIEW` | PASS |
| Pre-implementation helper command | `run_agent_automation_assist.py --json --enforce` appears in `_pre_implementation_commands` | PASS |
| Helper mutation behavior | no helper mutation or apply/write/provider/live flag added | PASS |
| Focused test evidence | pytest focused tests pass 19/19; unittest import command succeeds | PASS |
| Public export evidence | N/A with reason: no public-sync authorized | N/A_WITH_REASON |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify the autorun workflow gate and its
focused tests to run the existing AAF read-only helper in the
`pre-implementation` phase.

Protected paths:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`
- optional:
  `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator directed proactive helper reminders at
the start of worker execution to reduce repeated late defects. AAF-T6A applies
that decision to the existing autorun pre-implementation phase.

Rollback boundary: revert the accepted AAF-T6A material closure commit to
remove the helper command insertion and focused tests together.

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
- explicit statement that the helper remains read-only and advisory until
  defects cause existing gate failure;
- explicit statement that no full read-receipt, AAF-T7A, scaffold, patch/apply,
  runtime, provider/live, public-sync, CLI/MCP adapter, generated aggregate, or
  session/handoff path was edited;
- exact claim boundary and public export disposition.

## Review Gate

Reviewer/closer must inspect the worker-return changed set against Required
Deliverables, run reviewer-fast gates, verify no forbidden scope was touched,
and only then convert accepted material into a completion review.

## Closure Checklist

- [x] Worker returned `COMPLETE_PENDING_REVIEW`.
- [x] Changed files stay inside Required Deliverables.
- [x] Pre-implementation autorun invokes the AAF helper with `--json --enforce`.
- [x] Focused tests cover helper placement and failure propagation.
- [x] Existing helper remains read-only; no helper mutation behavior is added.
- [x] No full AAF-T6, AAF-T7A, scaffold, patch/apply, runtime/provider/live,
  public-sync, CLI/MCP adapter, generated aggregate, or session/handoff path changed.
- [x] Worker-return fast gate passes.
- [x] Reviewer-owned completion review created.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all required deliverables are present,
required checks have been run or source-blocked with evidence, and changed files
remain inside Allowed scope.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, or the repair would require forbidden
read-receipt/scaffold/patch/runtime/provider/public/session scope.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | `pre-implementation` autorun runs `governance/compat/run_agent_automation_assist.py --base <base> --head <head> --json --enforce` | source diff and focused test |
| AC2 | Helper command is not introduced as an all-phase command | focused test |
| AC3 | Helper command failure contributes to pre-implementation gate failure | focused test or existing aggregation proof |
| AC4 | Existing AAF helper remains read-only and does not mutate files or run provider/live/arbitrary commands | diff review and worker return |
| AC5 | No forbidden paths changed | `git status --short`; diff |
| AC6 | Worker return contains required packet shape and no commit | worker-return gate |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T6A is private provenance governance-helper wiring. No public-sync
repository work or public catalog claim is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T6A early diagnostic wire-in worker execution |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | governed autorun helper invocation only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | early diagnostic wire-in only |
| forbiddenExpansion | helper mutation, read-receipt proof, scaffold generation, patch application, wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, speed/cost, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local workspace |
| Session or invocation | AAF-T6A worker execution, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, focused source/test edits, required gates |
| Target paths | worker required deliverables |
| Allowed scope source | this work order and paired GC-018 baseline |
| Before status evidence | dispatchBaseHead `d11e0522`; clean worktree verified before AAF-T6A dispatch authoring |
| After status evidence | AAF-T6A worker artifacts pending no-commit return |
| Diff evidence | worker records `git status --short` and gate receipts |
| Approval boundary | worker may update Required Deliverables but must not commit |
| Claim boundary | early diagnostic wire-in only; no read-receipt/scaffold/runtime/provider/public behavior |
| Agent type | worker role |
| Invocation ID | `aaf-t6a-early-diagnostic-wire-in-worker-2026-06-22` |
| Expected manifest | autorun gate source; focused tests; worker return |
| Actual changed set | worker records in return packet |
| Manifest delta | worker records in return packet |

## Claim Boundary

This work order authorizes only AAF-T6A early diagnostic wire-in of the existing
read-only AAF helper into `pre-implementation` autorun plus focused tests. It
does not authorize full AAF-T6 read-receipt proof, AAF-T7A acceleration,
scaffold generation, patch preview/apply behavior, helper mutation, runtime
behavior, provider/live behavior, CLI/MCP adapter behavior, public-sync,
session-sync by worker, direct interception, readiness claims, speed/cost
claims, or universal governed-coding control.
