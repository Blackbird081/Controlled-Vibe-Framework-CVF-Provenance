# CVF Agent Work Order - AAF-T4 Project Role And Provider Delegation Envelope

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-20

docType: work_order

dispatchBaseHead: f209d973

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_FOR_WORKER_2026-06-20.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: confirm with `git rev-parse --short HEAD` at worker start.

Current-time notes: AAF-T3 is closed at `45fd5468` with session-sync
`f209d973`. AAF-T4 creates the missing private project role/provider delegation
envelope behind the public multi-agent/provider routing guide. The public guide
is context only; CVF-governed repo surfaces are the authority.

Do-not-misread notes: do not open automated provider selection, runtime
provider routing, provider/API calls, live proof, secrets/quota use, public-sync,
runtime/source/test implementation, MCP execution, wrapper/proxy enforcement,
direct IDE/shell/git/filesystem interception, arbitrary command execution,
EDIT/COMMIT execution, queue/daemon, watcher, readiness, full-hook equivalence,
or universal governed-coding-control claims. This is a documentation/reference
tranche only.

Role-neutrality note: normative instructions in AAF-T4 artifacts must name
roles and project configuration duties, not a specific agent/provider/model as
the required worker.

Required first actions: read this work order, read the AAF-T4 GC-018 baseline,
read the source files named in the Source Verification Block, confirm actual
`executionBaseHead`, and inspect current `git status --short` before editing.

Return contract: return `COMPLETE_PENDING_REVIEW` with exactly the four
uncommitted artifacts named in Required Deliverables, actual
`executionBaseHead`, actual `git status --short`, focused review evidence,
worker-return fast gate result, and no commit. If blocked, return
`BLOCKED_WITH_REASON` and name the exact source or gate that blocked the work.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | two roles across phases: dispatch author creates packet; worker creates delegation-envelope artifacts; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=f209d973`; `executionBaseHead` confirmed by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only the four Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending envelope artifacts; one reviewer trace covers review/closure if accepted |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix AAF-T4 with CGE-T3, ACE-R1, runtime/provider/live, MCP, public-sync, automated provider selection, or direct-interception work |
| Before status evidence | clean worktree at dispatch base `f209d973`, except recurring Windows global git-ignore permission warning |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_COMPLETION_2026-06-20.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_COMPLETION_2026-06-20.md`
- this work order status/checklist/closure package if accepted;
- session front-door/state/handoff paths only if reviewer/closer changes
  current mode or next allowed move after accepting the worker return.

The closure packet is reviewer-owned. The execution role must not mark the work
closed.

## Purpose

Create a stable private Project Role And Provider Delegation Envelope so an
operator can approve project role assignment, delegation scope, provider-lane
selection boundaries, cost/quota ceilings, evidence logs, and reapproval
triggers before agents begin governed project work.

The envelope must help a noncoder operator and external agents understand who is
allowed to do what, which provider-lane selection is merely configured by the
operator, and when reapproval is required.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority, provider-lane approval, cost/quota ceiling |
| Dispatcher | dispatch author role |
| Worker | worker role |
| Reviewer | reviewer role |
| Closer | closer role |
| Session-sync steward | session-sync steward role when session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-20 AAF-T4 selection after AAF-T3 closure | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | ACCEPT |
| AAF-T4 GC-018 | `docs/baselines/CVF_GC018_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_2026-06-20.md` | ACCEPT |
| AAF-T3 completion | `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Agent role assignment matrix | `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` | ACCEPT |
| Delegation/subagent boundary standard | `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md` | ACCEPT |
| C-02 provider-routing boundary plan and closure | `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md`; `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md` | ACCEPT |
| Public guide context | public-sync `docs/guides/CVF_MULTI_AGENT_PROVIDER_ROUTING.md` named by active next move | CONTEXT_ONLY_NOT_CVF_SOURCE |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/project_role_provider_delegation/README.md`;
- update `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`;
- update `docs/reference/guard_orientation/README.md`;
- create `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_WORKER_RETURN_2026-06-20.md`;
- reviewer/closer closure conversion may create
  `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_COMPLETION_2026-06-20.md`
  and update this work order status/checklist/closure package;
- keep all normative role/provider wording role-neutral and project-configurable.

Forbidden scope:

- no edits outside the four Required Deliverables;
- no edits under `EXTENSIONS/**`, product runtime, web UI, MCP packages,
  `.github/**`, public-sync, dependency manifests, generated session state,
  active handoff, or session memory;
- no provider/model addition, concrete provider binding, automated provider
  selection, runtime provider routing, provider/API call, live proof, secrets/
  quota use, dependency install, CodeGraph install/init, watcher/daemon, queue,
  background service, or CVF Web action execution;
- no automatic mutation by the envelope;
- no direct IDE/shell/git/filesystem interception claim;
- no readiness, production, public release, universal speed, universal
  governed-coding control, or full-hook equivalence claim.

Risk ceiling: R1 governance documentation and reference.

## Required First Reads

The worker must read these before editing:

- `docs/baselines/CVF_GC018_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_2026-06-20.md`
- `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md`
- `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md`
- `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md`
- `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md`
- `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`

## Pre-Flight Checks

Before implementation, the worker must run or record:

```powershell
git rev-parse --short HEAD
git status --short
```

If the worktree contains unrelated dirty paths, the worker must preserve them
and avoid editing outside the four Required Deliverables.

## Write Ownership

| Path | Owner | Disposition |
|---|---|---|
| `docs/reference/project_role_provider_delegation/README.md` | worker | create within AAF-T4 scope |
| `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | worker | modify only to route project delegation lookup |
| `docs/reference/guard_orientation/README.md` | worker | modify only to point project delegation tasks to the new envelope |
| `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_WORKER_RETURN_2026-06-20.md` | worker | create only |
| Any other path | Not worker-owned | forbidden unless a revised work order authorizes it |

## Core Guard Self-Protection Authorization

N/A with reason: the worker-owned AAF-T4 changed set does not authorize changes
to protected root/session/handoff/checker paths. Reviewer/closer session-sync,
if needed after closure, must carry its own authorization block.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator-originated AAF-T4 delegation-envelope request |
| Route | `MULTI_AGENT_SINGLE_ROLE` |
| risk sensitivity | R1; documentation-only project delegation reference |
| selected role route | `MULTI_AGENT_SINGLE_ROLE` |
| Worker role | worker creates reference envelope and routing updates only |
| Reviewer role | reviewer/closer reviews, commits, closes, and session-syncs if accepted |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | satisfied for dispatch; fresh checkpoint required for scope expansion |
| escalation condition | scope expansion, forbidden paths, provider/live, public-sync, secrets/quota, dependency install, destructive actions, automated provider selection, runtime implementation, or claim-boundary change |

## Worker Autonomy / No-Question Rule

The worker must repair and rerun gate failures inside Allowed scope. The worker
must stop and return `BLOCKED_WITH_REASON` only for scope expansion, forbidden
paths, live/provider proof, public-sync, secret/quota consumption, dependency
install, destructive actions, runtime implementation, automated provider
selection, or claim-boundary changes.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | new stable reference folder under `docs/reference/project_role_provider_delegation/` plus existing routing/reference surfaces |
| Storage decision | create `README.md` as stable private front door; do not create runtime config or generated state |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | envelope remains documentation/reference only; no hidden state store |

## Required Deliverables

The worker must leave exactly these uncommitted artifact changes:

- `docs/reference/project_role_provider_delegation/README.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_WORKER_RETURN_2026-06-20.md`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active next move authorizes AAF-T4 and lists substrate fields | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | line 2706 | `nextAllowedMove` | active session state registry | ACCEPT |
| AAF-T3 completion names AAF-T4 as follow-up and blocks runtime/provider expansion | `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md` | lines 126-127, 150, 158-159 | AAF-T4 follow-up rows | AAF-T3 completion review | ACCEPT |
| Guard Orientation Index requires role-neutral wording | `docs/reference/guard_orientation/README.md` | lines 37-54 | `## Role-Neutrality Rule` | guard orientation index | ACCEPT |
| Guard Orientation Index defines startup and live-proof boundaries | `docs/reference/guard_orientation/README.md` | lines 73, 81 | startup row; runtime/provider/live proof row | guard orientation index | ACCEPT |
| Agent role matrix requires role ownership before implementation | `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` | lines 58-88 | `Core Assignment Rule`; `Role Assignment Flow` | role assignment matrix | ACCEPT |
| Agent role matrix keeps runtime role enforcement out of scope | `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` | lines 111, 155, 202 | runtime enforcement boundary | role assignment matrix | ACCEPT |
| Delegation standard states delegation is bounded execution, not authority transfer | `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md` | lines 61-72 | `Core Principle`; `Rule` | delegation boundary standard | ACCEPT |
| Delegation standard requires a mandatory delegation packet | `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md` | lines 139-160 | `### Mandatory Delegation Packet` | delegation boundary standard | ACCEPT |
| Delegation standard defines tool and memory boundaries | `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md` | lines 176, 197 | `### Tool Boundary`; `### Memory Boundary` | delegation boundary standard | ACCEPT |
| Delegation standard requires review gate before close | `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md` | line 308 | `## Review Gate` | delegation boundary standard | ACCEPT |
| C-02 provider-routing plan is planning-only and not runtime implementation | `docs/reference/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_PLAN_2026-06-14.md` | lines 39, 518, 530, 578 | planning-only claim boundary | provider-routing boundary plan | ACCEPT |
| C-02 closure preserves planning-only claim boundary | `docs/reviews/CVF_MODEL_GATEWAY_C02_PROVIDER_ROUTING_BOUNDARY_REWRITE_COMPLETION_2026-06-14.md` | lines 61, 83, 146 | planning-only closure | provider-routing closure review | ACCEPT |

## Current Repository Presence Check

| Checked item | Command/evidence | Disposition |
|---|---|---|
| Public guide path in provenance workspace | `Test-Path docs/guides/CVF_MULTI_AGENT_PROVIDER_ROUTING.md` returned `False` during dispatch authoring | CONTEXT_ONLY_NOT_CVF_SOURCE |

## New Doc-Only Artifact Fields

| Proposed item | Disposition |
|---|---|
| `docs/reference/project_role_provider_delegation/README.md` | DOC_ONLY_NEW front door for project role/provider delegation envelope |
| `Operator Approval Envelope` | DOC_ONLY_NEW section requiring operator-approved project profile before role/provider delegation |
| `Role And Delegation Map` | DOC_ONLY_NEW table mapping project roles, responsibilities, allowed tools, forbidden tools, outputs, and reviewer gate |
| `Provider Lane Selection Boundary` | DOC_ONLY_NEW section separating operator configuration from automated provider selection |
| `Cost And Quota Ceiling` | DOC_ONLY_NEW section for configured ceilings, not measured cost optimization |
| `Evidence Log` | DOC_ONLY_NEW section listing required local evidence fields |
| `Reapproval Triggers` | DOC_ONLY_NEW section naming changes that require operator reapproval |

## Required Envelope Contract

The new `docs/reference/project_role_provider_delegation/README.md` must include:

- `## Purpose`
- `## When To Use`
- `## Operator Approval Envelope`
- `## Role And Delegation Map`
- `## Provider Lane Selection Boundary`
- `## Cost And Quota Ceiling`
- `## Evidence Log`
- `## Reapproval Triggers`
- `## Non-Goals`
- `## Claim Boundary`
- `## Related Surfaces`

Minimum envelope fields:

- project identifier or N/A with reason;
- operator approval timestamp or placeholder for project start;
- role lanes and responsibilities;
- allowed and forbidden tools per role;
- provider-lane selection basis as operator configuration only;
- cost/quota ceiling and stop condition;
- evidence log fields for role, provider lane, invocation surface, changed
  files, proof basis, review gate, and reapproval status;
- reapproval triggers for scope expansion, provider/model change, cost/quota
  change, live/provider proof, public-sync, runtime/source implementation,
  direct interception, queue/daemon, or readiness claim.

The envelope must explicitly say it is not an automated provider selector and
does not claim provider quality, cost optimization, or runtime routing behavior.

## Provider Version / Model Name Discipline

The worker must avoid hard-coding current model/provider names as normative CVF
requirements. If examples are necessary, label them as project configuration
examples and avoid making them source authority. Provider/model versions,
prices, quotas, availability, and capabilities are temporal and require
operator-approved refresh for a specific project.

## Acceptance Criteria

| ID | Criterion | Evidence required |
|---|---|---|
| AC1 | Stable project delegation front door exists | `docs/reference/project_role_provider_delegation/README.md` |
| AC2 | Envelope contains all required sections and minimum fields | worker-return checklist and reviewer scan |
| AC3 | Operational reference index routes project role/provider delegation lookup to the new front door | diff evidence |
| AC4 | Guard Orientation Index points project delegation tasks to the new envelope | diff evidence |
| AC5 | Public guide context remains context-only, not CVF source authority | envelope claim boundary and worker-return evidence |
| AC6 | Worker changed only the four Required Deliverables | `git status --short` and trace manifest |
| AC7 | No runtime/provider/public/automated-selection scope is introduced | worker-return claim boundary and reviewer inspection |

## Execution Plan

1. Confirm `executionBaseHead` and current `git status --short`.
2. Read all Required First Reads and preserve unrelated dirty paths.
3. Create the stable private project delegation envelope at
   `docs/reference/project_role_provider_delegation/README.md`.
4. Update the operational reference index and Guard Orientation Index only
   enough to route role/provider delegation setup to the new envelope.
5. Create the worker-return packet using role-neutral language.
6. Run the Test / Gate Requirements and repair allowed-scope failures.
7. Return `COMPLETE_PENDING_REVIEW` with no commit.

## Test / Gate Requirements

The worker must run:

```powershell
python governance/compat/run_agent_automation_assist.py --base f209d973 --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
```

If a gate fails inside Allowed scope, the worker must fix the packet and rerun.
Do not ask the operator for allowed-scope repairs.

## Evidence Requirements

The worker return must record:

- actual `executionBaseHead`;
- actual `git status --short` at start and return;
- helper smoke command and result;
- worker-return fast gate command and result;
- exact changed paths;
- role-neutrality and provider-version discipline self-check result;
- explicit N/A-with-reason rows for automated provider selection, runtime,
  provider/live, public-sync, cost optimization, readiness, and direct
  interception.

## Review Gate

Reviewer/closer must run, at minimum:

```powershell
python governance/compat/run_agent_automation_assist.py --base <closureBaseHead> --head HEAD --json --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <closureBaseHead> --head HEAD --enforce
```

Reviewer/closer may repair only AAF-T4 allowed-scope defects before committing.
Any scope expansion returns to the operator.

## Closure Checklist

- [x] Worker changed only the four Required Deliverables.
- [x] Delegation envelope is role-neutral and project-configurable.
- [x] Operational reference index points to the envelope.
- [x] Guard Orientation Index points project delegation tasks to the envelope.
- [x] Worker-return packet includes required shape sections.
- [x] Public Export Disposition is resolved.
- [x] Automated provider selection, runtime/provider/live/public-sync/cost
  optimization/readiness claims are N/A with reason.
- [x] Reviewer/closer owns completion review and session-sync.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all Required Deliverables are present,
helper smoke passes, worker-return fast gate passes, role-neutrality and
provider-version discipline self-checks pass, and no forbidden scope was
touched.

Return `BLOCKED_WITH_REASON` only when blocked by missing source authority,
forbidden path requirements, dependency install need, provider/live proof,
public-sync, destructive action, secret/quota access, runtime implementation,
automated provider selection, or claim-boundary change.

## Operator Checkpoint

No operator checkpoint is required for allowed-scope repairs. A fresh operator
checkpoint is required before opening automated provider selection,
runtime/source/test implementation, CLI/MCP integration, watcher/daemon
behavior, provider/live proof, public-sync, direct interception,
full-hook-equivalence claims, universal-control claims, or broad CGE-T3
absorption.

## Commit Prompt Readiness

This section exists only because the dispatch packet includes commit-prompt
language in the worker-return contract and review gate. It does not authorize
the worker to commit.

- Diff scope: PASS - dispatch authoring changes are limited to the AAF-T4
  GC-018 baseline and this work order.
- Tests: PASS - dispatch authoring gates are required before the dispatch
  author commits this packet; worker must run AAF-T4 gate requirements before
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
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py`; guard orientation index |
| Owner surface | `docs/reference/project_role_provider_delegation/README.md` |
| Disposition | ADAPT as CVF-owned private delegation reference |
| Claim boundary | public guide context is not CVF source authority; CVF-owned standards and state control |

## Rescan Intelligence Hardening

- Original source artifact: operator AAF-T4 selection and AAF-T3 closure
  follow-up candidate.
- Predecessor intake artifact:
  `docs/reviews/CVF_AAF_T3_GUARD_ORIENTATION_INDEX_COMPLETION_2026-06-20.md`.
- Delta ledger status: `CHANGED_DISPOSITION` because AAF-T4 promotes project
  role/provider delegation from follow-up candidate into dispatch-ready
  reference work.
- Routing matrix status:
  - `DO_NOW`: create private project role/provider delegation envelope.
  - `RESOLVED_BY_DESIGN`: keep provider examples configurable and
    non-canonical.
  - `SEPARATE_RUNTIME_TRANCHE`: automated provider selection, runtime routing,
    provider calls, queue/daemon, direct interception.
  - `OUT_OF_SCOPE`: public-sync, production readiness, universal control.
- Semantic sampling status: `PARTIAL_TARGETED`, limited to AAF-T3 follow-up,
  delegation standards, and provider-routing planning boundary.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Disposition |
|---|---|
| UNCHANGED_FROM_INTAKE | Public guide remains context; CVF source authority remains private governed surfaces. |
| CHANGED_DISPOSITION | AAF-T4 delegation envelope becomes dispatch-ready documentation/reference work. |
| NEW_FINDING | Project provider-lane approval needs explicit cost/quota and reapproval fields before external-agent use. |
| REMOVED_OR_REJECTED | Automated provider selection, runtime routing, provider/live, public-sync, direct-interception scope remains rejected. |

### Follow-Up Routing Matrix

| Lane | Disposition |
|---|---|
| DO_NOW | Create project delegation envelope and route it from reference surfaces. |
| RESOLVED_BY_DESIGN | Keep provider/model examples as project configuration, not CVF source authority. |
| SEPARATE_RUNTIME_TRANCHE | Automated provider selection, runtime routing, CLI/MCP integration, watcher/daemon, provider/live, direct interception. |
| STRATEGIC_OPERATOR_DECISION | Broad CGE-T3 absorption and ACE-R1 remain parked. |
| DEFER | Public-sync summary or public-facing provider-routing guide refresh. |
| OUT_OF_SCOPE | Production readiness, public release readiness, universal governed-coding-control claim. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| AAF-T4-RS1 | Active next move | AAF-T4 creates private substrate | DO_NOW | Could this be mistaken for runtime routing? | PASS_DOC_ONLY_REQUIRED |
| AAF-T4-RS2 | Delegation standard | delegation is bounded execution, not authority transfer | DO_NOW | Could a role delegate authority to a provider/worker? | PASS_AUTHORITY_BOUNDARY_REQUIRED |
| AAF-T4-RS3 | C-02 plan | provider routing remains planning-only | OUT_OF_SCOPE runtime | Could the envelope implement provider selection? | PASS_RUNTIME_REJECTED |

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - this is a work order authoring packet,
  not a corpus inventory, folder-tree scan, or extraction report.
- Corpus root: N/A with reason - no corpus root was authorized or enumerated.
- Snapshot time: 2026-06-20 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads and `rg -n` source
  lookups over named AAF-T4 authority files.
- Manifest artifact or inline manifest: Source Verification Block and Required
  First Reads.
- Manifest hash: N/A with reason - no generated corpus manifest artifact was
  produced.
- Processing ledger artifact or inline ledger: inline in Source Verification
  Block and Test / Gate Requirements.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=inline; ledger_terminal=inline; exclusions=no-corpus-inventory-scope; unresolved=0
- Unresolved files: 0
- Declared exclusions: full corpus inventory, folder-tree scan, extraction
  report, runtime/provider proof, public-sync.
- Unreadable or unsupported files: none.
- Aggregation check: N/A with reason - no corpus aggregate was produced.
- Drift check: N/A with reason - no corpus aggregate was produced.
- Output traceability: work order source verification rows cite source files
  and line anchors.
- Adversarial verification: claim rejects any full-corpus, complete-inventory,
  automated provider selection, runtime, or public readiness assertion.
- Corpus verdict: PARTIAL

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| Public multi-agent/provider routing language needs a private governed delegation substrate before project use | RULE_GAP | GOVERNANCE_CONTROL_PLANE | STANDARD_ADDED | Worker creates AAF-T4 project delegation envelope reference. |
| Runtime/provider/cost behavior is mentioned but not changed | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | AAF-T4 records configuration boundaries only; no provider/live/cost behavior changes. |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: Current CVF sources will show role assignment and
delegation standards plus provider-routing planning boundaries, but no compact
project-level envelope that combines operator approval, role delegation,
provider-lane selection boundary, cost/quota ceiling, evidence log, and
reapproval triggers.

Evidence Comparison Requirement: worker return compares the created envelope
against AAF-T3 follow-up rows, role/delegation standards, and C-02
planning-only boundaries.

Contradiction Handling Requirement: if current source already contains an
equivalent active envelope, worker returns `BLOCKED_WITH_REASON` instead of
duplicating it.

Claim Update Requirement: worker return records whether AAF-T4 confirms,
narrows, or rejects the dispatch prediction.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_FOR_WORKER_2026-06-20.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Worker return | `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_WORKER_RETURN_2026-06-20.md` | worker return present and accepted by reviewer/closer | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_COMPLETION_2026-06-20.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Delegation envelope | `docs/reference/project_role_provider_delegation/README.md` | `Status: ACTIVE_REFERENCE`; `docType: reference` | PASS |
| Reference routing | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`; `docs/reference/guard_orientation/README.md` | bounded routing rows present | PASS |
| Roadmap state | AAF-T4 closure state | `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | N/A with reason: no JSON registry required or changed | no generated JSON registry touched | PASS |
| Registry Markdown | N/A with reason: no Markdown registry required; operational reference and guard orientation rows added | routing rows added instead | PASS |
| External evidence digest | N/A with reason: no external evidence digest created | documentation/reference closure only | N/A with reason |
| System loop interlock | N/A with reason: no system loop interlock changed | no runtime/source interlock mutation | N/A with reason |
| Session continuity | active session front-door/state/handoff after material commit | material closure only; active session-sync follows this commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Runtime receipt evidence | N/A with reason: AAF-T4 creates no runtime receipt | N/A_WITH_REASON |
| Query acceptance evidence | N/A with reason: AAF-T4 performs no query acceptance | N/A_WITH_REASON |
| Worker-return acceptance | worker return present and accepted by reviewer/closer | PASS |
| Closure claim | `CLOSED_PASS_BOUNDED` documentation/reference closure only | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | AAF-T4 project delegation documentation work order only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | cooperating local operator/roles read the envelope manually |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | delegation envelope, not execution-control enforcement |
| forbiddenExpansion | wrapper/proxy enforcement, direct interception, arbitrary commands, EDIT/COMMIT execution, automated provider selection, runtime provider routing, provider/live, public-sync, queue/daemon, watcher, readiness, full-hook equivalence, and universal control remain parked |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author role |
| Provider or surface | local workspace |
| Session or invocation | AAF-T4 dispatch authoring, 2026-06-20 |
| Working directory | repository root |
| Command or tool surface | file reads, `rg -n`, `apply_patch`, governance gates |
| Target paths | AAF-T4 GC-018 baseline and this work order |
| Allowed scope source | operator AAF-T4 approval and active next-move state |
| Before status evidence | HEAD `f209d973`; clean worktree except recurring Windows global git-ignore warning |
| After status evidence | AAF-T4 dispatch packet ready for pre-dispatch gates |
| Diff evidence | exact dispatch diff and dispatch-quality gate |
| Approval boundary | dispatch authoring only; no implementation by dispatch author in this packet |
| Claim boundary | no runtime mutation, provider/live, public-sync, direct interception, automated provider selection, or universal enforcement claim |
| Agent type | single-role dispatch author |
| Invocation ID | `aaf-t4-dispatch-authoring-2026-06-20` |
| Expected manifest | `docs/baselines/CVF_GC018_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_FOR_WORKER_2026-06-20.md` |
| Actual changed set | `docs/baselines/CVF_GC018_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_2026-06-20.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AAF_T4_PROJECT_ROLE_PROVIDER_DELEGATION_ENVELOPE_FOR_WORKER_2026-06-20.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: AAF-T4 is private provenance governance-reference work. Public export
requires separate public-sync authorization and a bounded public-facing summary
if the operator requests it later.

## Claim Boundary

This work order authorizes only a private project role/provider delegation
envelope and discoverability updates. It does not authorize automated provider
selection, runtime provider routing, provider/live proof, MCP execution,
public-sync, direct interception, automatic mutation, full-hook equivalence
claims, cost optimization claims, production readiness, public release
readiness, universal speed, or universal governed-coding-control claims.
