# CVF Agent Work Order - AAF-T7A Reviewer/Closer Acceleration Helper (L0 Read-Only)

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: work_order

dispatchBaseHead: 68d5044a

Commit mode: `WORKER_MUST_NOT_COMMIT`

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This work order
authorizes one bounded helper tranche; it does not map, enumerate, project, or
classify CVF state.

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_FOR_WORKER_2026-06-22.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: AAF-T6A is closed by the Codex reviewer/closer. AAF-T7A
roadmap continuity is synced at `68d5044a`. AAF-T7A.1 is the next authorized
acceleration tranche at the L0 read-only level. MPI work remains paused until
this acceleration lane checkpoint is handled.

Do-not-misread notes: do not implement L1 scaffold generation, L2 patch
preview, or L3 apply mode. Do not let the helper mutate files, create/edit/
stage/commit/push, run arbitrary commands, call provider/live APIs, or make
closure decisions. Do not implement full AAF-T6 read-receipt gate, CLI/MCP
adapter behavior, public-sync, queue, daemon, watcher, wrapper/proxy, direct
IDE/shell/git/filesystem interception, durable store, readiness, cost/speed, or
universal governed-coding-control claim.

Required first actions: read this work order, read the AAF-T7A.1 GC-018
baseline, read the AAF-T7A roadmap, read the L2A classification standard, read
the Guard Orientation Index, inspect the existing AAF helper report/mode/readout
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
| Intake source | operator critique that reviewer/closer conversion steps repeat and cost time |
| Intake role | worker adds an L0 read-only reviewer readout to the existing AAF helper and tests it |
| Reviewer role | reviewer/closer validates readout placement, read-only behavior, focused tests, and claim boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; read-only helper readout only |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | worker return to reviewer/closer closure conversion |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation would require L1 scaffold, L2 patch preview, L3 apply, helper mutation, closure decision, provider/live, public-sync, runtime/product, CLI/MCP adapter, arbitrary command, or forbidden path scope |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
|---|---|
| Coverage index requirement | NOT_APPLICABLE_WITH_REASON |
| Reason | AAF-T7A.1 adds a read-only readout to the existing repo-local AAF helper. It is not a `.private_reference/legacy` scan or memory-plane absorption tranche. |
| Coverage evidence used instead | L2A standard, AAF-T7A roadmap, existing helper report/mode/readout, and helper tests source verification. |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatcher creates packet; worker adds read-only readout and return packet; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=68d5044a`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending AAF-T7A.1 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix AAF-T7A.1 with later AAF-T7A L1/L2/L3 tranches, MPI-T3/T4, full AAF-T6 read-receipt, scaffold/patch/apply, runtime/provider/live, MCP adapter, public-sync, queue/daemon, direct-interception, generated aggregate, or memory-plane work |
| Before status evidence | dispatchBaseHead `68d5044a`; clean worktree verified before AAF-T7A.1 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted helper source/test changes; optional README pointer; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map and worker-return packet shape |
| `docs/baselines/CVF_GC018_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_2026-06-22.md` | GC-018 authorization and claim boundary |
| `docs/roadmaps/CVF_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_ROADMAP_2026-06-22.md` | roadmap posture and L0-first recommendation |
| `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | L0 safety level and ACCELERATOR_CANDIDATE authority |
| `governance/compat/run_agent_automation_assist.py` | existing report builder, mode resolution, and read-only signalReadout pattern |
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

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `governance/compat/run_agent_automation_assist.py` | worker | add L0 read-only `reviewerReadout` to the report for reviewer-return shape |
| `governance/compat/test_run_agent_automation_assist.py` | worker | add focused tests for read-only/bounded/reviewer-return-only behavior |
| `docs/reference/learning_to_acceleration/README.md` | worker | optional pointer to the new readout only |
| `docs/reviews/CVF_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_WORKER_RETURN_2026-06-22.md` | worker | create |
| `docs/baselines/CVF_GC018_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_2026-06-22.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_FOR_WORKER_2026-06-22.md` | reviewer/closer | no worker edit |
| `AGENTS.md`, `CVF_SESSION/**`, active handoff, runtime routes, web, MCP, provider registry, generated aggregates, public-sync, queue/daemon/watcher, wrapper/proxy, scaffold/patch/apply files | out of worker scope | forbidden |

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
L1 scaffold, L2 patch preview, L3 apply, helper mutation, closure decision,
runtime/product behavior, generated aggregate edits, AGENTS/session/handoff
edits, provider/live/public-sync scope, dependency installation, secrets/quota,
destructive action, or a change to the claim boundary.

## Purpose

Add an L0 read-only reviewer/closer acceleration readout to the existing AAF
helper so the mechanical conversion steps that repeat across closures are
surfaced as advisory text and JSON for a reviewer/closer, without changing
anything on disk and without making any closure decision.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Dispatcher | dispatch author role |
| Worker | read-only helper readout and focused test author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 proceed AAF-T7A at L0; dispatch authoring now; worker execution only through this work order | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T7A.1 GC-018 | `docs/baselines/CVF_GC018_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_2026-06-22.md` | ACCEPT |
| AAF-T7A roadmap | `docs/roadmaps/CVF_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_ROADMAP_2026-06-22.md` | ACCEPT |
| L2A classification standard | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Existing AAF helper | `governance/compat/run_agent_automation_assist.py` | ACCEPT |
| Existing AAF helper tests | `governance/compat/test_run_agent_automation_assist.py` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- update `governance/compat/run_agent_automation_assist.py` to add a bounded
  read-only `reviewerReadout` list to the report, populated only when the
  changed range resolves to a reviewer-return shape, derived only from existing
  report diagnostics and L2A vocabulary;
- update `governance/compat/test_run_agent_automation_assist.py` with focused
  tests proving read-only behavior, bounded output shape, and reviewer-return-
  only presence;
- optionally update `docs/reference/learning_to_acceleration/README.md` for a
  pointer to the new readout only;
- create
  `docs/reviews/CVF_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_WORKER_RETURN_2026-06-22.md`.

Forbidden scope:

- no L1 scaffold generation, no L2 patch preview, no L3 apply mode;
- no helper filesystem mutation, file create/edit/stage/commit/push, closure
  decision, provider/live call, or arbitrary command;
- no full AAF-T6 Guard Orientation Read-Receipt Gate;
- no ledger store, source directory, generator, drift checker, durable store,
  runtime Learning Plane mutation, provider/live proof, CLI/MCP adapter
  behavior, public-sync, wrapper/proxy enforcement, direct IDE/shell/git/
  filesystem interception, arbitrary command execution, EDIT/COMMIT execution,
  queue, daemon, watcher, readiness, full-hook equivalence, cost optimization
  claim, speed/productivity claim without proof, or universal
  governed-coding-control claim;
- no route schema edits, runtime/product behavior, dependency installation, or
  generated aggregate edits.

Risk ceiling: R0/R1 read-only helper readout and focused tests only.

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Inspect the existing `build_report`, mode resolution, and `signalReadout`
   read-only pattern.
3. Add a bounded read-only `reviewerReadout` list to `AssistReport` and
   `to_dict`, populated only for reviewer-return shape from existing
   diagnostics and L2A vocabulary.
4. Add focused tests proving read-only behavior, bounded output shape, and
   reviewer-return-only presence.
5. Optionally add a README pointer to the new readout.
6. Create the worker-return artifact with required packet shape and
   worker-experience token.
7. Run required commands and record results.

## Worker Return Packet Shape Contract

The worker-return artifact must include these sections or exact N/A-with-reason
dispositions where listed:

| Packet item | Worker-return disposition |
|---|---|
| Status | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| executionBaseHead | exact value from `git rev-parse --short HEAD` at worker start |
| dispatchBaseHead | `68d5044a` |
| git status --short | exact output after worker changes |
| Purpose | MUST_INCLUDE |
| Scope / Methodology | MUST_INCLUDE |
| Findings / Position | MUST_INCLUDE |
| Risk / Corrective Action | MUST_INCLUDE |
| Claim Boundary | MUST_INCLUDE |
| Agent Operation Trace Block | MUST_INCLUDE |
| Delta Execution Claim Boundary Control Block | MUST_INCLUDE |
| Public Export Disposition | MUST_INCLUDE |
| External Knowledge Intake Routing | MUST_INCLUDE |
| Rescan Intelligence Hardening | MUST_INCLUDE |
| Corpus Completeness And Report Integrity | MUST_INCLUDE |
| Finding-To-Governance Learning Disposition | MUST_INCLUDE |
| Epistemic Process Block | MUST_INCLUDE_OR_EPISTEMIC_PROCESS_NA_WITH_REASON |
| Machine Closure Package | MUST_INCLUDE_OR_NA_WITH_REASON; worker must not mark closure |
| Worker-experience token | structured `WORKER_EXPERIENCE_RETRO` or exact asserting `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` |

The worker must not record a clean `git status --short` when the worker-return
file or other deliverables are untracked or modified.

Conditional sections that do not apply must still be present with `N/A with
reason` or `NOT_APPLICABLE_WITH_REASON` rows.

The worker-return Machine Closure Package must not backtick a not-yet-created
completion-review path as an authority artifact; describe it as reviewer-created
after acceptance instead.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-gate, source-inventory,
packet-shape, test, corpus-integrity, and text-encoding defects without asking
the operator. Ask the operator only if remediation would exceed Allowed scope,
change the claim boundary, edit AGENTS/session/handoff, implement L1/L2/L3
behavior, make the helper mutate files or close work, touch forbidden paths,
install dependencies, consume secrets/quota, or perform destructive actions.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| L2A classifies repeated reviewer labor reducible by a read-only helper as an accelerator candidate | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | line 85 | ACCELERATOR_CANDIDATE | L2A classification standard | ACCEPT |
| L2A safety level L0 is read-only suggestion that changes nothing | `docs/reference/learning_to_acceleration/CVF_L2A_T0_LEARNING_TO_ACCELERATION_CLASSIFICATION_STANDARD.md` | lines 96, 104 | L0 read-only suggestion | L2A Acceleration Safety Levels | ACCEPT |
| AAF helper exposes JSON enforce CLI entrypoint | `governance/compat/run_agent_automation_assist.py` | lines 839-880 | main | AAF helper CLI | ACCEPT |
| AAF helper builds a report from the changed range | `governance/compat/run_agent_automation_assist.py` | line 667 | build_report | AAF helper report builder | ACCEPT |
| AAF helper report serializes to a JSON dict | `governance/compat/run_agent_automation_assist.py` | lines 479-499 | AssistReport.to_dict | AAF helper report dataclass | ACCEPT |
| AAF helper resolves a reviewer-return mode for worker-return changed sets | `governance/compat/run_agent_automation_assist.py` | lines 400, 437 | reviewer-return | AAF helper mode resolution | ACCEPT |
| AAF helper already emits a bounded read-only signalReadout list | `governance/compat/run_agent_automation_assist.py` | line 532 | signalReadout | AAF helper report | ACCEPT |
| AAF helper has focused report and CLI tests | `governance/compat/test_run_agent_automation_assist.py` | lines 258, 317 | BuildReportTests; CliOutputTests | AAF helper test module | ACCEPT |
| AAF helper has focused signal-readout tests | `governance/compat/test_run_agent_automation_assist.py` | line 625 | SignalReadoutTests | AAF helper test module | ACCEPT |
| Worker-return fast gate routes a focused pytest target before reviewer-fast | `governance/compat/run_worker_return_fast_gate.py` | lines 30-47 | build_commands | worker-return fast gate | ACCEPT |

## New Doc-Only Fields

| Field or term | Disposition |
|---|---|
| `reviewerReadout` | New AAF helper read-only output field; not a runtime/product field |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work-order instruction | Verification |
|---|---|---|
| Roadmap recommends L0 read-only first implementation | add read-only reviewerReadout only | focused test and helper smoke output |
| L2A classifies reviewer labor as ACCELERATOR_CANDIDATE | tie readout to existing diagnostics and L2A vocabulary | source verification and test |
| Roadmap forbids L1/L2/L3 in this tranche | forbid scaffold, patch preview, apply, helper mutation | worker-return claim boundary and reviewer diff |
| Worker must not commit | `WORKER_MUST_NOT_COMMIT` route | git status and reviewer closure conversion |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | operator critique about repeated reviewer/closer conversion cost to a governed L0 readout |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; reviewer-fast gate |
| Owner surface | AAF-T7A.1 Reviewer/Closer Acceleration Helper |
| Disposition | ADAPT as CVF-owned L0 read-only reviewer readout |
| Claim boundary | operator/external critique remains input only until promoted through this governed dispatch |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/run_agent_automation_assist.py`; `governance/compat/test_run_agent_automation_assist.py` |
| Runtime behavior claimed | N/A_WITH_REASON: governance compatibility helper readout only; no product runtime, provider route, web route, CLI/MCP adapter, or Learning Plane mutation |
| Helper/checker implementation claimed | BOUNDED: add an L0 read-only reviewer readout list and focused tests |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are out of scope and untouched; AAF-T7A.1 makes no provider registry absence, hardcoded-provider, provider-selection, or live-governance claim |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded read-only helper readout only; no provider, public-sync, runtime product behavior, or generated aggregate behavior is claimed |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | governance compatibility helper source and tests |
| Storage decision | reuse the existing helper report; no new source directory or store |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | read-only helper readout only; no hidden state store |

## Corpus Completeness And Report Integrity

- Corpus task class: work-order dispatch source verification for a bounded L0
  read-only helper readout.
- Corpus root: repo-local source files named in Required First Reads and Source
  Verification Block.
- Snapshot time: 2026-06-22 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus targeted
  `rg`/`grep` checks.
- Manifest artifact or inline manifest: Required First Reads and Source
  Verification Block in this work order.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=Required First Reads and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo scan and generated registry mutation and runtime/provider/web/MCP/public-sync corpus scan; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: no full `.private_reference/legacy` scan, no runtime/provider/web/MCP/public-sync corpus scan, no generated aggregate edit.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by dispatch.
- Drift check: N/A with reason: no generated aggregate edited by dispatch.
- Output traceability: AAF-T7A.1 work order maps the roadmap deferral to worker
  deliverables.
- Adversarial verification: source lines identify the existing helper readout
  pattern, reviewer-return mode, and L2A L0 safety level.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Reviewer/closer conversion steps repeat mechanically across closures | ACCELERATION_GAP | LEARNING_TO_ACCELERATION | ACCELERATOR_CANDIDATE | Add L0 read-only reviewer readout to existing helper | handled by worker if complete |
| L1 scaffold or L2 patch preview would reduce more labor but carries higher risk | ACCELERATION_GAP | LEARNING_TO_ACCELERATION | SEPARATE_TRANCHE | L1/L2 only by a future work order with postcondition checks | deferred |
| L3 apply mode could close work without human review | CONTROL_PROOF_GAP | GOVERNANCE_CONTROL_PLANE | OUT_OF_SCOPE | L3 apply mode remains out of scope | deferred |
| Runtime/provider/cost applicability for this work order | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Rescan Intelligence Hardening

- Original source artifact: AAF-T7A roadmap and AAF-T6A completion review
  deferral of reviewer/closer repetitive text edits.
- Predecessor intake artifact: L2A-T0 classification standard, L2A front door,
  AAF-T6A closure, existing AAF helper source and tests.
- Delta ledger status: `NEW_FINDING` because the roadmap deferral becomes a
  bounded L0 read-only readout implementation tranche.
- Routing matrix status: `DO_NOW` for the L0 readout; `DEFER` for L1 scaffold
  and L2 patch preview; `OUT_OF_SCOPE` for L3 apply, runtime, provider, CLI/MCP,
  public-sync.
- Semantic sampling status: sampled L2A safety levels, ACCELERATOR_CANDIDATE
  classification, existing helper report/mode/readout, and helper test classes.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | AAF helper remains read-only and local-diagnostic only. |
| CHANGED_DISPOSITION | Roadmap deferral of reviewer/closer acceleration becomes a dispatched L0 readout tranche. |
| NEW_FINDING | A reviewer-return-shape readout can advise closure conversion steps from existing diagnostics. |
| REMOVED_OR_REJECTED | L1 scaffold, L2 patch preview, L3 apply, helper mutation, runtime/provider/public behavior are rejected from AAF-T7A.1. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | Add an L0 read-only reviewerReadout to the existing helper report and test read-only/bounded behavior. |
| RESOLVED_BY_DESIGN | Existing helper already emits a read-only signalReadout; reviewerReadout reuses the same read-only pattern. |
| DEFER | L1 scaffold generation and L2 patch preview for closure conversion. |
| STRATEGIC_OPERATOR_DECISION | Operator decides after AAF-T7A.1 whether to authorize L1/L2 or resume MPI. |
| SEPARATE_RUNTIME_TRANCHE | runtime/product behavior, provider/live proof, CLI/MCP adapter behavior, scaffold generator, patch apply, queue/daemon/watcher, public-sync. |
| OUT_OF_SCOPE | L3 apply mode, direct interception, universal governed-coding control, speed/cost claims, durable memory store, Learning Plane runtime mutation. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T7A-WO-RS1 | L2A Acceleration Safety Levels | L0 changes nothing on disk | DO_NOW | Could the readout silently write a file? | PASS - readout is print/JSON only, tests assert no mutation |
| AAF-T7A-WO-RS2 | L2A ACCELERATOR_CANDIDATE | reviewer labor is an accelerator candidate | DO_NOW | Should this be L1 scaffold first? | PASS - roadmap recommends L0 first |
| AAF-T7A-WO-RS3 | AAF helper signalReadout | read-only readout pattern already exists | RESOLVED_BY_DESIGN | Should worker build a new helper? | PASS - reuse existing report pattern |
| AAF-T7A-WO-RS4 | AAF helper reviewer-return mode | readout should target reviewer-return shape | DO_NOW | Should it print for every mode? | PASS - work order limits readout to reviewer-return shape |

## Machine Closure Package

Worker return must include a Machine Closure Package section but must not mark
AAF-T7A.1 closed. Use pending-review or N/A-with-reason dispositions for closure
items the worker cannot own.

Reviewer/closer owns the final closure package in the completion review.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: DISPATCHED_TO_WORKER` now; reviewer updates after return | PENDING_REVIEWER |
| GC-018 status | `docs/baselines/CVF_GC018_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_2026-06-22.md` | `Status: DISPATCHED_TO_WORKER` now; reviewer updates after return | PENDING_REVIEWER |
| Worker return | `docs/reviews/CVF_AAF_T7A_REVIEWER_CLOSER_ACCELERATION_HELPER_WORKER_RETURN_2026-06-22.md` | expected `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` | PENDING_WORKER |
| Completion or reviewer artifact | reviewer creates the AAF-T7A.1 completion review after accepting the return | reviewer-owned if accepted | PENDING_REVIEWER |
| Helper source | `governance/compat/run_agent_automation_assist.py` | reviewerReadout appears only for reviewer-return shape; read-only | PENDING_WORKER |
| Focused tests | `governance/compat/test_run_agent_automation_assist.py` | unit tests pass | PENDING_WORKER |
| Runtime/provider/live evidence | N/A | no runtime/provider/live behavior authorized | N/A with reason |
| Public-sync evidence | N/A | no public-sync authorized | N/A with reason |
| Session continuity | active session front-door/state/handoff | session-sync follows accepted dispatch/closure commits | PENDING_REVIEWER |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add an L0 read-only reviewer/closer
acceleration readout to the existing AAF helper and add focused tests, without
changing the helper to mutate files or make closure decisions.

Protected paths:

- `governance/compat/run_agent_automation_assist.py`
- `governance/compat/test_run_agent_automation_assist.py`

Operator authorization: the operator directed AAF-T7A to proceed at L0 to reduce
repeated reviewer/closer conversion cost while preserving human review and CVF
source authority.

Rollback boundary: revert the accepted AAF-T7A.1 material closure commit to
remove the reviewer readout and focused tests together.

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
- explicit statement that the helper remains read-only and makes no closure
  decision or filesystem mutation;
- explicit statement that no L1 scaffold, L2 patch preview, L3 apply, helper
  mutation, runtime, provider/live, public-sync, CLI/MCP adapter, generated
  aggregate, or session/handoff path was edited;
- exact claim boundary and public export disposition.

## Review Gate

Reviewer/closer must inspect the worker-return changed set against Required
Deliverables, run reviewer-fast gates, verify no forbidden scope was touched,
verify the helper remains read-only, and only then convert accepted material
into a completion review.

## Closure Checklist

- [ ] Worker returned `COMPLETE_PENDING_REVIEW`.
- [ ] Changed files stay inside Required Deliverables.
- [ ] `reviewerReadout` appears only for reviewer-return shape.
- [ ] Focused tests cover read-only behavior, bounded shape, and reviewer-return-only presence.
- [ ] Helper makes no filesystem mutation or closure decision.
- [ ] No L1/L2/L3, full AAF-T6, runtime/provider/live, public-sync, CLI/MCP adapter, generated aggregate, or session/handoff path changed.
- [ ] Worker-return fast gate passes.
- [ ] Reviewer-owned completion review created.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all required deliverables are present,
required checks have been run or source-blocked with evidence, and changed files
remain inside Allowed scope.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, or the repair would require forbidden
L1/L2/L3/helper-mutation/runtime/provider/public/session scope.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | The helper emits a bounded `reviewerReadout` only for reviewer-return shape | source diff and focused test |
| AC2 | `reviewerReadout` items derive only from existing diagnostics and L2A vocabulary | source diff and focused test |
| AC3 | The helper performs no filesystem mutation, closure decision, provider/live call, or arbitrary command | diff review and focused test |
| AC4 | Focused tests prove read-only, bounded, reviewer-return-only behavior | focused test |
| AC5 | No forbidden paths changed | `git status --short`; diff |
| AC6 | Worker return contains required packet shape and no commit | worker-return gate |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T7A.1 is private provenance governance-helper work. No public-sync
repository work or public catalog claim is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T7A.1 L0 read-only reviewer readout worker execution |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | read-only helper report invocation only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | L0 read-only reviewer/closer acceleration readout only |
| forbiddenExpansion | L1 scaffold, L2 patch preview, L3 apply, helper mutation, file generation, wrapper/proxy enforcement, arbitrary-command execution, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, cost/speed claim, and universal control remain out of scope |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local workspace |
| Session or invocation | AAF-T7A.1 worker execution, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, focused source/test edits, required gates |
| Target paths | worker required deliverables |
| Allowed scope source | this work order and paired GC-018 baseline |
| Before status evidence | dispatchBaseHead `68d5044a`; clean worktree verified before AAF-T7A.1 dispatch authoring |
| After status evidence | AAF-T7A.1 worker artifacts pending no-commit return |
| Diff evidence | worker records `git status --short` and gate receipts |
| Approval boundary | worker may update Required Deliverables but must not commit |
| Claim boundary | L0 read-only reviewer readout only; no L1/L2/L3, runtime, provider, or public behavior |
| Agent type | worker role |
| Invocation ID | `aaf-t7a-reviewer-closer-acceleration-worker-2026-06-22` |
| Expected manifest | helper source; focused tests; optional README pointer; worker return |
| Actual changed set | worker records in return packet |
| Manifest delta | worker records in return packet |

## Claim Boundary

This work order authorizes only AAF-T7A.1 L0 read-only reviewer/closer
acceleration readout added to the existing AAF helper plus focused tests. It
does not authorize L1 scaffold generation, L2 patch preview, L3 apply mode,
helper file mutation, closure decisions by the helper, full AAF-T6 read-receipt
proof, runtime behavior, provider/live behavior, CLI/MCP adapter behavior,
public-sync, session-sync by worker, direct interception, readiness claims,
speed/cost claims, or universal governed-coding control.
