# CVF Agent Work Order - AAF-T3 Guard Orientation Index

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-20

docType: work_order

dispatchBaseHead: ab3854d9

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T3_GUARD_ORIENTATION_INDEX_FOR_WORKER_2026-06-20.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: AAF-T3 is a bounded follow-up to AAF-T2. AAF-T2 moved one
late corpus-gate failure class into early helper diagnostics. AAF-T3 moves an
even earlier prevention layer into documentation: a task-first Guard Orientation
Index that tells a new or resumed agent which rules to read before writing.

Do-not-misread notes: do not open checker implementation, hook wiring, autorun
phase changes, runtime execution, MCP wiring, provider/live proof, public-sync,
wrapper/proxy enforcement, direct IDE/shell/git/filesystem interception,
arbitrary command execution, queue/daemon, watcher, background service, or
universal control. This is a documentation/orientation tranche only.

Role-neutrality note: normative instructions in AAF-T3 artifacts must name
roles and required work, not a specific agent/provider/model. Use terms such as
operator, dispatcher, worker, reviewer, closer, and session-sync steward.

Required first actions: read this work order, read the AAF-T3 GC-018 baseline,
read the source files named in the Source Verification Block, confirm actual
`executionBaseHead`, and inspect current `git status --short` before editing.

Return contract: return `COMPLETE_PENDING_REVIEW` with exactly the five
uncommitted artifacts named in Required Deliverables, actual `executionBaseHead`,
actual `git status --short`, focused review evidence, worker-return fast gate
result, and no commit. If blocked, return `BLOCKED_WITH_REASON` and name the
exact source or gate that blocked the work.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatch author creates packet; worker creates orientation artifacts; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=ab3854d9`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only the five Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending orientation artifacts; one reviewer trace covers review/closure if accepted |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix AAF-T3 with CGE-T3 absorption, runtime, public-sync, provider/live, MCP, checker implementation, or direct-interception work |
| Before status evidence | clean worktree at dispatch base `ab3854d9`, except recurring Windows global git-ignore permission warning |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md`
- session front-door/state/handoff paths only if reviewer/closer changes current
  mode or next allowed move after accepting the worker return.

The closure packet is reviewer-owned. The execution role must not mark the work
closed.

## Purpose

Create a stable, task-first Guard Orientation Index so future local or external
agents can read role/task-class guard guidance before authoring governed CVF
artifacts. The index should reduce avoidable late gate failures without
claiming enforcement or replacing canonical guards.

## Agent Roles

| Role | Owner |
|---|---|
| Dispatcher | dispatch author role |
| Worker | worker role |
| Reviewer | reviewer role |
| Closer | closer role |
| Session-sync steward | session-sync steward role when session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 AAF-T3 approval and role-neutrality constraint | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T3 GC-018 | `docs/baselines/CVF_GC018_AAF_T3_GUARD_ORIENTATION_INDEX_2026-06-20.md` | ACCEPT |
| AAF-T2 closure | `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_COMPLETION_2026-06-20.md` | ACCEPT |
| Operational reference index | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | ACCEPT |
| Startup guard router | `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md` | ACCEPT |
| Root agent instructions | `AGENTS.md` | ACCEPT |
| Guard registry guard | `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md` | ACCEPT |
| Agent handoff boundary standard | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/guard_orientation/README.md`;
- update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`;
- update `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`;
- update `AGENTS.md`;
- create `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_WORKER_RETURN_2026-06-20.md`;
- reviewer/closer closure conversion may create
  `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md`
  and update this work order status/checklist/closure package;
- keep all normative role and return-contract language role-neutral.

Forbidden scope:

- worker role: no edits outside the five Required Deliverables;
- no edits under `EXTENSIONS/**`, product runtime, web UI, MCP packages,
  `.github/**`, public-sync, dependency manifests, generated session state,
  active handoff, or session memory;
- no checker implementation, hook wiring, autorun phase change, provider/live
  proof, benchmark, public push, secret read, dependency install, CodeGraph
  install/init, watcher/daemon, queue, or background service;
- no automatic mutation by the index;
- no direct IDE/shell/git/filesystem interception claim;
- no readiness, production, public release, universal speed, universal
  governed-coding control, or full-hook equivalence claim.

Risk ceiling: R1 governance documentation and orientation.

## Required First Reads

The worker must read these before editing:

- `docs/baselines/CVF_GC018_AAF_T3_GUARD_ORIENTATION_INDEX_2026-06-20.md`
- `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_COMPLETION_2026-06-20.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `AGENTS.md`
- `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md`
- `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md`
- `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`

## Pre-Flight Checks

Before implementation, the worker must run or record:

```powershell
git rev-parse --short HEAD
git status --short
```

If the worktree contains unrelated dirty paths, the worker must preserve them
and avoid editing outside the five Required Deliverables.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/guard_orientation/README.md` | worker | create within AAF-T3 scope |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | worker | modify only to route guard-orientation lookup |
| `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md` | worker | modify only to list the orientation index as startup orientation |
| `AGENTS.md` | worker | modify only to add a short role-neutral orientation-read instruction |
| `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_WORKER_RETURN_2026-06-20.md` | worker | create only |
| Any other path | Not worker-owned | forbidden unless a revised work order authorizes it |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create a role-neutral guard orientation
front door and update only the allowed routing/startup surfaces that make it
discoverable before governed work.

Protected paths:

- `AGENTS.md`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`

Operator authorization: the operator explicitly approved AAF-T3 on 2026-06-20
and required role-neutral language that does not name a specific agent/provider/
model in normative instructions.

Rollback boundary: if AAF-T3 is rejected, revert only the five Required
Deliverables. Do not revert AAF-T2 closure commit `904eb09a` or closure
continuity commit `ab3854d9`.

Scope boundary: this authorization does not extend to checker behavior,
session-state generated aggregates, active handoff files, runtime/product
source, public-sync, provider/live proof, MCP execution, or direct-interception
tooling.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator-originated AAF-T3 orientation-index request |
| Route | `MULTI_AGENT_SINGLE_ROLE` |
| risk sensitivity | R1; documentation-only guard orientation |
| selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Worker role | worker creates orientation/index/routing artifacts only |
| Reviewer role | reviewer/closer reviews, commits, closes, and session-syncs if accepted |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | satisfied for dispatch; fresh checkpoint required for scope expansion |
| escalation condition | scope expansion, forbidden paths, provider/live, public-sync, secrets/quota, dependency install, destructive actions, checker implementation, or claim-boundary change |

## Worker Autonomy / No-Question Rule

The worker must repair and rerun gate failures inside Allowed scope. The worker
must stop and return `BLOCKED_WITH_REASON` only for scope expansion, forbidden
paths, live/provider proof, public-sync, secret/quota consumption, dependency
install, destructive actions, checker implementation, or claim-boundary changes.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | new stable reference folder under `docs/reference/guard_orientation/` plus existing routing/startup surfaces |
| Storage decision | create `README.md` as stable front door; do not create dated reference file for the index body |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | orientation index remains documentation/routing only; no hidden state store |

## Required Deliverables

The worker must leave exactly these uncommitted artifact changes:

- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `AGENTS.md`
- `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_WORKER_RETURN_2026-06-20.md`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Operational reference index is an existing routing reference | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | line 9 | `## Purpose` | operational reference front door | ACCEPT |
| Operational reference index has lookup table for task triggers | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | line 34 | `## Lookup Table` | operational reference front door | ACCEPT |
| Startup/resume already routes through session memory, active state, and handoff | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | line 48 | `Starting or resuming a session` | operational reference lookup row | ACCEPT |
| Work-order authoring already routes through template, choreography, source verification, and canonical contracts | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | line 50 | `Authoring or dispatching a work order` | operational reference lookup row | ACCEPT |
| External-agent review and external package absorption already have a routing row | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | line 54 | `Preparing external-agent review context or absorbing external MCP/workspace ideas` | operational reference lookup row | ACCEPT |
| Operational reference index has maintenance and claim-boundary sections | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | lines 58, 65 | `## Maintenance Rule`; `## Claim Boundary` | operational reference front door | ACCEPT |
| Startup guard router lists startup guard surfaces | `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md` | lines 36, 40-41, 50-51 | `## Required Guard Surfaces` | startup guard router | ACCEPT |
| Startup guard router has protocol requirements and claim boundary | `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md` | lines 54, 99 | `## Protocol Requirements`; `## Claim Boundary` | startup guard router | ACCEPT |
| Guard registry guard requires discoverability in README and core knowledge base when guard files change | `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md` | lines 14, 18-26 | `## Rule` | guard registry guard | ACCEPT |
| Root instructions require startup acknowledgment before material governed work | `AGENTS.md` | line 30 | `## Mandatory Startup Acknowledgment` | root agent instructions | ACCEPT |
| Root instructions require source verification for work orders | `AGENTS.md` | line 236 | `## Mandatory Work Order Source Verification` | root agent instructions | ACCEPT |
| Root instructions define autorun phase gate command | `AGENTS.md` | line 533 | `run_agent_autorun_workflow_gate.py --phase pre-dispatch` | root agent instructions | ACCEPT |
| Root instructions define reviewer fast preflight and commit steward command | `AGENTS.md` | lines 542, 585 | reviewer fast preflight; commit steward preflight | root agent instructions | ACCEPT |
| Root instructions require allowed-scope gate remediation | `AGENTS.md` | line 567 | Allowed-scope gate remediation | root agent instructions | ACCEPT |
| Handoff boundary standard requires Agent Handoff Contract Control Block and reviewer closure conversion | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | lines 35-69 | `## Required Work Order Block`; `## Commit Mode Rules` | agent handoff local view | ACCEPT |
| AAF-T2 completion recommends Guard Orientation Index as follow-up candidate | `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_COMPLETION_2026-06-20.md` | line 82 | Guard Orientation Index follow-up | AAF-T2 completion review | ACCEPT |
| AAF-T2 helper emits structured corpus diagnostics | `governance/compat/run_agent_automation_assist.py` | line 493 | `corpusDiagnostics` | AAF helper JSON report | ACCEPT |

## New Doc-Only Artifact Fields

| Proposed item | Disposition |
|---|---|
| `docs/reference/guard_orientation/README.md` | DOC_ONLY_NEW front door for role-neutral task-first guard orientation |
| `Task Class Guard Map` | DOC_ONLY_NEW table inside the orientation index |
| `Role-Neutrality Rule` | DOC_ONLY_NEW orientation rule derived from operator instruction |
| `Fast command or gate` | DOC_ONLY_NEW row field pointing to existing commands, not a new command |

## Required Orientation Index Contract

The new `docs/reference/guard_orientation/README.md` must be concise enough to
read before work, but specific enough to prevent common late gate failures.

Minimum required sections:

- `## Purpose`
- `## Read This First`
- `## Role-Neutrality Rule`
- `## Role Glossary`
- `## Task Class Guard Map`
- `## Common Failure Patterns`
- `## Claim Boundary`
- `## Related Surfaces`

The `Task Class Guard Map` table must include rows for at least:

- startup/resume;
- work-order authoring/dispatch;
- worker execution under `WORKER_MUST_NOT_COMMIT`;
- reviewer-return review;
- closure;
- session-sync;
- external knowledge absorption;
- public-sync;
- runtime/provider/live proof;
- guard/checker maintenance.

Each row must include:

- task class;
- active role;
- read first;
- required blocks or outputs;
- common failure to avoid;
- fast command or gate;
- boundary.

The index must state that it is an orientation layer only. Canonical standards,
work orders, checkers, and current state still control.

## Role-Neutrality Contract

Normative instructions in all AAF-T3 artifacts must use role names and work
ownership, not a specific agent/provider/model. The worker return must preserve
this style. Historical artifact titles may be cited only as file paths; do not
turn historical provider names into current authority.

Allowed role terms include:

- operator
- dispatcher
- dispatch author
- worker
- reviewer
- closer
- reviewer/closer
- session-sync steward
- external reviewer

Forbidden normative pattern examples:

- naming a specific agent/provider/model as the required worker;
- saying a provider-specific memory file is CVF source authority;
- binding future work to one provider surface when the route is role-based.

## Acceptance Criteria

| ID | Criterion | Evidence required |
|---|---|---|
| AC1 | Stable guard orientation front door exists | `docs/reference/guard_orientation/README.md` |
| AC2 | Orientation index is task-first and role-neutral | reviewer scan and worker-return evidence |
| AC3 | Operational reference index routes guard-orientation lookup to the new front door | diff evidence |
| AC4 | Startup guard router lists the orientation index as startup orientation | diff evidence |
| AC5 | Root instructions require reading the orientation index before material governed work | diff evidence |
| AC6 | Worker changed only the five Required Deliverables | `git status --short` and trace manifest |
| AC7 | No checker/runtime/provider/public scope is introduced | worker-return claim boundary and reviewer inspection |

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Read all Required First Reads and preserve unrelated dirty paths.
3. Create the stable guard orientation front door at
   `docs/reference/guard_orientation/README.md`.
4. Update the operational reference index, startup guard router, and root agent
   instructions only enough to route agents to the orientation index.
5. Create the worker-return packet using role-neutral language.
6. Run the Test / Gate Requirements and repair allowed-scope failures.
7. Return `COMPLETE_PENDING_REVIEW` with no commit.

## Test / Gate Requirements

The worker must run:

```powershell
python governance/compat/run_agent_automation_assist.py --base ab3854d9 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
```

If the helper smoke command fails only because it correctly detects the
in-progress worker-return packet defect, the worker must fix the packet inside
Allowed scope and rerun. Do not ask the operator for allowed-scope repairs.

## Evidence Requirements

The worker return must record:

- actual `executionBaseHead`;
- actual `git status --short` at start and return;
- helper smoke command and result;
- worker-return fast gate command and result;
- exact changed paths;
- role-neutrality self-check result;
- explicit N/A-with-reason rows for checker/runtime/provider/live/public/cost
  scope.

## Review Gate

Reviewer/closer must run, at minimum:

```powershell
python governance/compat/run_agent_automation_assist.py --base <closureBaseHead> --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBaseHead> --head HEAD --enforce
```

Reviewer/closer may repair only AAF-T3 allowed-scope defects before committing.
Any scope expansion returns to the operator.

## Closure Checklist

- [x] Worker changed only the five Required Deliverables.
- [x] Orientation index is role-neutral and task-first.
- [x] Operational reference index points to the orientation index.
- [x] Startup guard router points to the orientation index.
- [x] Root instructions include a short orientation-read instruction.
- [x] Worker-return packet includes required shape sections.
- [x] Public Export Disposition is resolved.
- [x] Runtime/provider/live/public-sync/checker claims are N/A with reason.
- [x] Reviewer/closer owns completion review and session-sync.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all Required Deliverables are present,
helper smoke passes, worker-return fast gate passes, role-neutrality self-check
passes, and no forbidden scope was touched.

Return `BLOCKED_WITH_REASON` only when blocked by missing source authority,
forbidden path requirements, dependency install need, provider/live proof,
public-sync, destructive action, secret/quota access, checker implementation,
or claim-boundary change.

## Operator Checkpoint

No operator checkpoint is required for allowed-scope repairs. A fresh operator
checkpoint is required before opening checker implementation, AAF helper
integration of orientation rows, CLI/MCP integration, watcher/daemon behavior,
runtime/provider/live proof, public-sync, direct interception, full-hook
equivalence claims, universal control claims, or broad CGE-T3 absorption.

## Commit Prompt Readiness

This section exists only because the dispatch packet includes commit-prompt
language in the worker-return contract and review gate. It does not authorize
the worker to commit.

- Diff scope: PASS - dispatch authoring changes are limited to the AAF-T3
  GC-018 baseline and this work order.
- Tests: PASS - dispatch authoring gates are required before the dispatch
  author commits this packet; worker must run AAF-T3 gate requirements before
  returning.
- Gates: PASS - dispatch-quality and pre-dispatch gates are required before
  the dispatch author commits this packet.
- Untracked unrelated: NONE - dispatch author observed no unrelated dirty paths
  except the recurring Windows global git-ignore permission warning.
- Forbidden touched paths: NONE - no implementation/runtime/public/checker
  paths are touched by dispatch authoring.

## Worker Return Packet Shape Contract

Worker return must include these always-required sections:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- executionBaseHead
- git status --short

Worker return must include or explicitly mark `N/A with reason` for these
conditional gate sections:

- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Return vocabulary:

- success: `COMPLETE_PENDING_REVIEW`
- blocked: `BLOCKED_WITH_REASON`
- no commit: `WORKER_MUST_NOT_COMMIT`

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | governed work-order/source-verification/autorun lane |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py`; startup guard router |
| Owner surface | `docs/reference/guard_orientation/README.md` |
| Disposition | ADAPT as CVF-owned orientation reference |
| Claim boundary | existing CVF helpers, standards, and checkers remain source authority; the index is a navigation layer |

## Rescan Intelligence Hardening

- Original source artifact: operator AAF-T3 selection and AAF-T2 closure
  follow-up candidate.
- Predecessor intake artifact:
  `docs/reviews/CVF_AAF_T2_AGENT_AUTOMATION_ASSIST_EARLY_GAP_DIAGNOSTICS_COMPLETION_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because AAF-T3 promotes guard
  orientation from chat-level recommendation into a governed reference index.
- Routing matrix status:
  - `DO_NOW`: create role-neutral task-first guard orientation index.
  - `RESOLVED_BY_DESIGN`: keep index as documentation/routing only.
  - `SEPARATE_RUNTIME_TRANCHE`: checker implementation, CLI/MCP integration,
    watcher/daemon, provider/live, direct interception.
  - `OUT_OF_SCOPE`: public-sync, production readiness, universal control.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to the AAF-T2 closure
  follow-up and operator role-neutrality constraint.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | AAF helper remains read-only, local, and advisory. |
| CHANGED_DISPOSITION | Guard orientation moves from operator recommendation to dispatch-ready documentation tranche. |
| NEW_FINDING | Normative role instructions should avoid naming a specific agent/provider/model. |
| REMOVED_OR_REJECTED | Checker implementation, runtime, MCP, watcher, provider/live, public-sync, direct-interception scope remains rejected. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | Create orientation index and route it from startup/reference surfaces. |
| RESOLVED_BY_DESIGN | Keep orientation role-neutral and task-first. |
| SEPARATE_RUNTIME_TRANCHE | Checker implementation, helper integration, CLI/MCP integration, watcher/daemon, provider/live, direct interception. |
| STRATEGIC_OPERATOR_DECISION | Broad CGE-T3 absorption after AAF-T3 is declined or closed. |
| DEFER | Public-sync summary or public-facing guard orientation page. |
| OUT_OF_SCOPE | Production readiness, universal governed-coding-control claim. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T3-RS1 | Role-Neutrality Contract | use role names, not provider/model names | DO_NOW | Could future single-agent or multi-agent routes stale the wording? | PASS_ROLE_NEUTRAL_REQUIRED |
| AAF-T3-RS2 | Required Orientation Index Contract | task-first guard map | DO_NOW | Could this become another long reference that agents skip? | PASS_CONCISE_TABLE_REQUIRED |
| AAF-T3-RS3 | Scope / Target / Owner Boundary | documentation only | OUT_OF_SCOPE runtime | Could the index imply checker enforcement or runtime control? | PASS_BOUNDARY_EXPLICIT |

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this is a work order authoring packet, not a corpus inventory, folder-tree scan, or extraction report.
- Corpus root: N/A with reason - no corpus root was authorized or enumerated.
- Snapshot time: 2026-06-20 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads and `rg -n` source lookups over named AAF-T3 authority files.
- Manifest artifact or inline manifest: Source Verification Block and Required First Reads.
- Manifest hash: N/A with reason - no generated corpus manifest artifact was produced.
- Processing ledger artifact or inline ledger: inline in Source Verification Block and Test / Gate Requirements.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=no-corpus-inventory-scope; unresolved=0
- Unresolved files: 0
- Declared exclusions: full corpus inventory, folder-tree scan, extraction report, runtime/provider proof, public-sync.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregate was produced.
- Drift check: N/A with reason - no corpus aggregate was produced.
- Output traceability: work order source verification rows cite source files and line anchors.
- Adversarial verification: claim rejects any full-corpus, complete-inventory, checker-enforcement, runtime, or public readiness assertion.
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

- Defect class: `ORIENTATION_GAP`
- Learning lane: `GOVERNANCE_CONTROL_PLANE`
- Disposition: `PROMOTED_TO_GOVERNED_ORIENTATION_INDEX`
- Next action: worker creates AAF-T3 orientation index; reviewer/closer reviews
  whether a future tranche should integrate orientation rows into the helper.
- Runtime/provider/cost learning lane: `N/A_WITH_REASON` - no runtime or
  provider behavior is involved.

| Finding or lesson | Disposition | Reason |
|---|---|---|
| Agents can write governed artifacts before reading the relevant guard family | GOVERNANCE_LEARNING_PROMOTED | Create a task-first guard orientation index. |
| Naming a specific provider/agent in normative role text creates stale routing and checker friction | GOVERNANCE_LEARNING_PROMOTED | Enforce role-neutral wording in AAF-T3 artifacts. |

## Epistemic Process Block

| Field | Disposition |
|---|---|
| Source basis | current repository files named in Source Verification Block |
| Inference boundary | AAF-T3 value is inferred from observed guard-latency/friction, not from public or production usage |
| Uncertainty | index discoverability may still depend on agents reading startup instructions |
| Falsification path | worker return, reviewer scan, helper smoke, worker-return fast gate |
| Claim status | bounded dispatch-ready work order |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T3_GUARD_ORIENTATION_INDEX_FOR_WORKER_2026-06-20.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_WORKER_RETURN_2026-06-20.md` | worker return present and accepted by reviewer/closer | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | AAF-T3 closure state | `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no JSON registry required or changed | no generated JSON registry touched | PASS |
| Registry Markdown | N/A with reason: no Markdown registry required; operational reference index row added | operational reference index row added instead | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | documentation/reference closure only | N/A with reason |
| System loop interlock | N/A with reason: no system loop interlock changed | no runtime/source interlock mutation | N/A with reason |
| Session continuity | active session front-door/state/handoff after material commit | material closure only; active session-sync follows this commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: AAF-T3 creates no runtime receipt | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: AAF-T3 performs no query acceptance | N/A_WITH_REASON |
| Worker-return acceptance | worker return present and accepted by reviewer/closer | PASS |
| Closure claim | `CLOSED_PASS_BOUNDED` documentation/reference closure only | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T3 guard-orientation documentation work order only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local user/agent reads the index manually |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | orientation index, not execution-control enforcement |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain parked |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | local workspace |
| Session or invocation | AAF-T3 dispatch authoring, 2026-06-20 |
| Working directory | repository root |
| Command or tool surface | file reads, `rg -n`, `apply_patch`, governance gates |
| Target paths | AAF-T3 GC-018 baseline and this work order |
| Allowed scope source | operator AAF-T3 approval and AAF-T2 closure follow-up |
| Before status evidence | HEAD `ab3854d9`; clean worktree except recurring Windows global git-ignore warning |
| After status evidence | AAF-T3 dispatch packet ready for pre-dispatch gates |
| Diff evidence | exact dispatch diff and dispatch-quality gate |
| Approval boundary | dispatch authoring only; no implementation by dispatch author in this packet |
| Claim boundary | no runtime mutation, provider/live, public-sync, direct interception, checker implementation, or universal enforcement claim |
| Agent type | single-role dispatch author |
| Invocation ID | `aaf-t3-dispatch-authoring-2026-06-20` |
| Expected manifest | `docs/baselines/CVF_GC018_AAF_T3_GUARD_ORIENTATION_INDEX_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T3_GUARD_ORIENTATION_INDEX_FOR_WORKER_2026-06-20.md` |
| Actual changed set | `docs/baselines/CVF_GC018_AAF_T3_GUARD_ORIENTATION_INDEX_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T3_GUARD_ORIENTATION_INDEX_FOR_WORKER_2026-06-20.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T3 is private provenance governance orientation work. Public export
requires separate public-sync authorization and a bounded public-facing summary
if the operator requests it later.

## Claim Boundary

This work order authorizes only a role-neutral, task-first guard orientation
index and discoverability updates. It does not authorize checker implementation,
runtime execution, provider/live proof, MCP execution, public-sync, direct
interception, automatic mutation, full-hook equivalence claims, production
readiness, public release readiness, universal speed, or universal
governed-coding-control claims.
