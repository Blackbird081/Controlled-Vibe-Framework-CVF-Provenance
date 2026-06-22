# CVF Agent Work Order - RSE-T0 Role Switch Envelope Standard

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: work_order

dispatchBaseHead: 006986b4

Commit mode: `WORKER_MUST_NOT_COMMIT`

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This work order
authorizes one bounded documentation-only standard tranche; it does not map,
enumerate, project, or classify CVF state.

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_FOR_WORKER_2026-06-22.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: Codex authored the RSE roadmap T0 through T3 (`6608be51`).
Claude authored this work order and the paired GC-018 baseline. Per the operator
role model, Codex reviews this work order before any worker execution, then the
worker executes, then Codex reviews and closes. RSE-T0 is documentation only.

Do-not-misread notes: implement only the RSE-T0 documentation standard and its
front door. Do not implement any checker, helper, or AAF diagnostic; do not edit
`governance/compat/` files or AAF helper source or tests; do not change AHB-T2 or
AHB-T3 contract semantics; do not author RSE-T1, T2, or T3 content; do not add
runtime, provider/live, public-sync, CLI/MCP adapter, workspace, queue, daemon,
watcher, direct interception, readiness, or universal control behavior or claim.

Required first actions: read this work order, read the RSE-T0 GC-018 baseline,
read the RSE roadmap T0 section, read the Agent Handoff Contract ratification,
read the AHB machine-check standard, read the Guard Orientation Index role
glossary, read the AAF-T7B completion review learning-capture decision, confirm
actual `executionBaseHead`, and inspect current `git status --short`.

Return contract: return `COMPLETE_PENDING_REVIEW` with only the required
uncommitted artifacts, actual `executionBaseHead`, actual `git status --short`,
source inventory, scan-depth ledger, gate evidence, and no commit. If blocked,
return `BLOCKED_WITH_REASON` and name the exact source or gate.

The worker-return artifact must include either the structured
`WORKER_EXPERIENCE_RETRO` block or the exact asserting
`WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` line.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator instruction to proceed with the RSE lane under the stated role model |
| Intake role | worker creates the RSE-T0 documentation standard and front door |
| Reviewer role | reviewer/closer validates field coverage, examples, claim boundary, and AHB local-view alignment |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; bounded documentation standard only |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | Codex roadmap, Claude work order, Codex work-order review, worker execution, Codex review and closure |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation would require any checker or helper code, AHB semantics change, RSE-T1/T2/T3 content, runtime/provider/live, public-sync, session/handoff edits, or forbidden path scope |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | Codex authored roadmap; Claude authored work order and GC-018; Codex reviews the work order; worker creates the RSE-T0 standard and front door; reviewer/closer reviews and commits if accepted |
| phase | DISPATCH_AUTHORING; WORK_ORDER_REVIEW; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=006986b4`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending RSE-T0 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix RSE-T0 with RSE-T1/T2/T3, AAF, MPI, runtime/provider/live, MCP adapter, public-sync, queue/daemon, direct-interception, generated aggregate, or memory-plane work |
| Before status evidence | dispatchBaseHead `006986b4`; clean worktree verified before RSE-T0 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted standard and front-door files; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map, role glossary, and worker-return packet shape |
| `docs/baselines/CVF_GC018_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_2026-06-22.md` | GC-018 authorization and claim boundary |
| `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | roadmap T0 fields, examples, and acceptance criteria |
| `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | canonical role-switch fields the envelope views |
| `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | required Agent Handoff Contract Control Block heading |
| `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_COMPLETION_2026-06-22.md` | the AAF-T7B confusion pattern to encode as a forbidden operator-question example |

## Pre-Flight Checks

The worker must run or record these checks before returning. For commands that
use `<executionBaseHead>`, replace it with the exact value returned by
`git rev-parse --short HEAD` at worker start.

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_automation_assist.py --base <executionBaseHead> --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_automation_assist.py
```

The worker-return artifact must record command results or a
`BLOCKED_WITH_REASON` if a required command cannot run. RSE-T0 adds no Python
file, so the fast-gate pytest target is the existing AAF helper test module used
only as the fast-gate routing target, not as a new test surface.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-gate, source-inventory,
packet-shape, or documentation-structure defects and rerun the required checks
without asking the operator. Ask the operator only if remediation would exceed
Allowed scope, change the claim boundary, require checker/helper/runtime/provider/
public/session scope, require AHB semantics change, require RSE-T1/T2/T3 content,
touch forbidden paths, consume secrets/quota, require a destructive action, or
contradict this work order. Worker-to-reviewer questions are routed to the
reviewer/closer in the worker return, not escalated to the operator.

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
- gate evidence
- `WORKER_EXPERIENCE_RETRO` block or
  `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`

If any listed section is not applicable, include the section with `N/A with reason` or `NOT_APPLICABLE_WITH_REASON` and a short reason instead of omitting it.

## Execution Plan

1. Read required sources and record `executionBaseHead`.
2. Create the new directory `docs/reference/role_switch_envelope/` with the
   standard file and a compact front-door README.
3. In the standard, define every minimum role-switch envelope field from the
   roadmap T0 section, with a one-line meaning for each.
4. Add at least one compliant worker-to-reviewer role-switch example and at
   least one forbidden operator-question example matching the AAF-T7B confusion
   pattern.
5. State explicitly that RSE is documentation and reference only until a later
   checker tranche, and that the standard is a local view of the ratified Agent
   Handoff Contract, not a replacement.
6. Run required checks and create the worker-return artifact without committing.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md` | worker | create the RSE-T0 documentation standard |
| `docs/reference/role_switch_envelope/README.md` | worker | create a compact front door |
| `docs/reviews/CVF_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_WORKER_RETURN_2026-06-22.md` | worker | create |
| `docs/baselines/CVF_GC018_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_2026-06-22.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_FOR_WORKER_2026-06-22.md` | reviewer/closer | no worker edit |
| `governance/compat/**`, AAF helper source/tests, AHB contract files, `AGENTS.md`, `CVF_SESSION/**`, active handoff, runtime routes, web, MCP, provider registry, generated aggregates, public-sync, queue/daemon/watcher, RSE-T1/T2/T3 files | out of worker scope | forbidden |

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
checker or helper implementation, AHB semantics change, RSE-T1/T2/T3 content,
runtime/product behavior, generated aggregate edits, AGENTS/session/handoff
edits, provider/live/public-sync scope, dependency installation, secrets/quota,
destructive action, or a change to the claim boundary.

## Purpose

Create the RSE-T0 Role Switch Envelope standard: a documentation-only reference
that defines the canonical envelope any agent uses when changing or accepting a
role inside a governed batch, plus a compact front door. The standard is a
role-switch local view of the ratified Agent Handoff Contract and encodes the
AAF-T7B operator-question confusion as a forbidden pattern.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Roadmap author | Codex roadmap role |
| Dispatcher | Claude work-order author role |
| Work-order reviewer | Codex reviews this work order before execution |
| Worker | RSE-T0 standard and front-door author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 RSE role model and lane proceed direction | ACCEPT |
| RSE-T0 GC-018 | `docs/baselines/CVF_GC018_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_2026-06-22.md` | ACCEPT |
| RSE roadmap | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | ACCEPT |
| Agent Handoff Contract ratification | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACCEPT |
| AHB machine-check standard | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| AAF-T7B completion review | `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_COMPLETION_2026-06-22.md` | ACCEPT |
| Agent error-to-governance philosophy | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md`
  with all minimum envelope fields, a compliant worker-to-reviewer example, a
  forbidden operator-question example, and an explicit documentation-only and
  AHB-local-view boundary;
- create `docs/reference/role_switch_envelope/README.md` as a compact front door;
- create
  `docs/reviews/CVF_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_WORKER_RETURN_2026-06-22.md`;
- reviewer/closer closure conversion may update this work order, paired
  GC-018, and create the completion review after accepting the worker return.

Forbidden scope:

- no checker, helper, or AAF diagnostic implementation and no edit to
  `governance/compat/` files or AAF helper source or tests;
- no change to AHB-T2 or AHB-T3 contract semantics;
- no RSE-T1, T2, or T3 content;
- no staging, commit, push, closure decision, provider/live call, or arbitrary
  command execution;
- no runtime, web, CLI/MCP adapter, workspace, queue, daemon, watcher,
  public-sync, wrapper/proxy enforcement, direct IDE/shell/git/filesystem
  interception, readiness, cost optimization claim, speed/productivity claim
  without proof, or universal governed-coding-control claim;
- no route schema edits, runtime/product behavior, dependency installation, or
  generated aggregate edits.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Roadmap names the minimum role-switch envelope fields for T0 | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | line 160 | Minimum envelope fields | RSE roadmap T0 section | ACCEPT |
| Roadmap recommends the RSE-T0 allowed scope paths | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | line 303 | Recommended Initial Allowed Scope | RSE roadmap | ACCEPT |
| Agent Handoff Contract defines canonical role-switch fields the envelope views | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | line 102 | CF-01 | Agent Handoff Contract field set | ACCEPT |
| Agent Handoff Contract defines commitOwner per phase | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | line 235 | CF-07 | Agent Handoff Contract field set | ACCEPT |
| AHB machine-check standard names the required Agent Handoff Contract Control Block heading | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | line 39 | Agent Handoff Contract Control Block | AHB local-view standard | ACCEPT |
| Guard Orientation Index defines the canonical role glossary | `docs/reference/guard_orientation/README.md` | line 56 | Role Glossary | guard orientation index | ACCEPT |
| Learning philosophy requires agent boundary defects to become governance improvements | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | line 69 | Escalation Ladder | governance learning philosophy | ACCEPT |
| AAF-T7B closure records that finding capture is required but worker scope cannot self-widen | `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_COMPLETION_2026-06-22.md` | line 109 | Learning Capture Decision | AAF-T7B completion review | ACCEPT |

## New Standard Terms

| Proposed term | Owner in RSE-T0 | Runtime status | Reason |
|---|---|---|---|
| `CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md` | RSE-T0 reference standard | NEW_DOC_ONLY_REFERENCE | the canonical role-switch envelope standard, documentation only |
| `operatorQuestionAllowed` | RSE-T0 envelope field | NEW_DOC_ONLY_FIELD | doc-only field naming whether a role may ask the operator in the current phase |
| `findingCaptureSurface` | RSE-T0 envelope field | NEW_DOC_ONLY_FIELD | doc-only field naming where a worker records a finding inside allowed scope |
| `outOfScopePromotionRoute` | RSE-T0 envelope field | NEW_DOC_ONLY_FIELD | doc-only field naming the route for promoting an out-of-scope finding |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap item | Source | Work-order coverage | Evidence requirement |
|---|---|---|---|
| RSE-T0 envelope fields | roadmap line 160 | standard names all fields | source diff and worker return |
| RSE-T0 compliant example | roadmap line 185 | standard includes a worker-to-reviewer example | source diff |
| RSE-T0 forbidden operator-question example | roadmap line 186 | standard encodes the AAF-T7B pattern | source diff |
| RSE-T0 documentation-only boundary | roadmap line 188 | standard states doc-only and AHB local view | claim boundary |
| RSE-T1/T2/T3 | roadmap lines 192, 220, 259 | excluded from this tranche | claim boundary and no T1/T2/T3 content |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | local governed role-boundary protocol route, not external authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; pre-dispatch autorun |
| Owner surface | RSE-T0 Role Switch Envelope Standard |
| Disposition | ADAPT as a CVF-owned documentation standard with bounded scope |
| Claim boundary | operator critique remains input only until implemented and closed through this governed work order |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/role_switch_envelope/` (new); RSE roadmap; AHB-T2 ratification; AHB machine-check standard |
| Runtime behavior claimed | N/A_WITH_REASON: documentation-only reference standard; no product runtime, provider route, web route, CLI/MCP adapter, checker, or helper behavior |
| Helper/checker implementation claimed | N/A_WITH_REASON: RSE-T0 is documentation only; no checker or helper is added |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded documentation standard only; no provider, public-sync, runtime product behavior, checker, helper, or generated aggregate behavior is claimed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | RSE-T0 Role Switch Envelope Standard |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, or provider interception claim |
| claimLanguage | documentation-only reference standard |
| forbiddenExpansion | checker or helper implementation, runtime role router, agent workspace, AHB semantics change, RSE-T1/T2/T3 content, provider/live, public-sync, queue/daemon/watcher, direct interception, readiness, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| A worker routed a reviewer/closer finding-promotion decision to the operator | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | WRITTEN_RULE_CANDIDATE | RSE-T0 standard defines the envelope and a forbidden operator-question example | handled by this dispatch |
| Operator-question boundary needs machine enforcement eventually | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | RSE-T3 may add diagnostics after T0 through T2 | deferred |
| Worker Return Jurisdiction Block is not yet a packet requirement | RULE_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | RSE-T2 defines the jurisdiction block | deferred |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime, provider, or cost behavior changed or claimed | handled |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded
  documentation-only standard tranche.
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
- Output traceability: RSE-T0 work order maps the RSE roadmap T0 section to
  worker deliverables and required gates.
- Adversarial verification: source rows distinguish the new RSE local-view
  standard from the existing ratified Agent Handoff Contract it views.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Core Guard Self-Protection Authorization

N/A with reason: RSE-T0 creates only new documentation reference files under
`docs/reference/role_switch_envelope/` and a new worker-return artifact under
`docs/reviews/`. It modifies no protected `governance/compat/` file, no protected
guard markdown, and no session JSON, so no Core Guard Self-Protection block
listing protected paths is required for the worker change set.

Operator authorization: the operator directed the RSE lane to proceed under the
stated role model. This work order authorizes only RSE-T0 documentation.

Rollback boundary: revert the accepted RSE-T0 material closure commit to remove
the new standard, its front door, and the worker return together.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | BOUNDED: creates one new reference directory `docs/reference/role_switch_envelope/` for the RSE-T0 standard and front door. |
| New durable foundation directory | `docs/reference/role_switch_envelope/` for documentation reference only. |
| Generated aggregate impact | N/A with reason: no generated aggregate is created or edited. |
| INDEX impact | N/A with reason: this is not an INDEX artifact or INDEX storage tranche. |
| Guard owner | reviewer/closer verifies the new directory holds only the authorized RSE-T0 reference files. |

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- source inventory and scan-depth ledger;
- changed-path list;
- AAF helper smoke result with `--json --enforce`;
- pre-implementation autorun gate result;
- worker-return fast gate result;
- explicit statement that the standard names every minimum envelope field;
- explicit statement that the standard includes a compliant worker-to-reviewer
  example and a forbidden operator-question example matching the AAF-T7B pattern;
- explicit statement that the standard is documentation-only and an AHB local
  view, not a replacement;
- explicit statement that no checker, helper, AAF diagnostic, AHB semantics,
  RSE-T1/T2/T3 content, runtime, provider/live, public-sync, generated aggregate,
  or session/handoff path was edited;
- exact claim boundary and public export disposition.

## Review Gate

Reviewer/closer must inspect the worker-return changed set against Required
Deliverables, run reviewer-fast gates, verify no forbidden scope was touched,
verify the standard covers all envelope fields and required examples, verify the
documentation-only and AHB-local-view boundary, and only then convert accepted
material into a completion review.

## Closure Checklist

- [ ] Worker returned `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.
- [ ] Changed files stay inside Required Deliverables.
- [ ] Standard names every minimum role-switch envelope field.
- [ ] Standard includes a compliant worker-to-reviewer example.
- [ ] Standard includes a forbidden operator-question example matching the AAF-T7B pattern.
- [ ] Standard states documentation-only and AHB local-view boundary.
- [ ] Front-door README points to the standard.
- [ ] Worker performed no checker, helper, AHB semantics, RSE-T1/T2/T3, staging, commit, push, provider/live call, or closure decision.
- [ ] Worker-return fast gate passes or records `BLOCKED_WITH_REASON`.
- [ ] Reviewer-owned completion review created if accepted.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all required deliverables are present,
required checks have been run or source-blocked with evidence, and changed files
remain inside Allowed scope.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, or the repair would require forbidden
checker/helper/AHB-semantics/RSE-T1-T2-T3/runtime/provider/public/session scope.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | The standard names every minimum role-switch envelope field from the roadmap T0 section | source diff and worker return |
| AC2 | The standard includes a compliant worker-to-reviewer role-switch example | source diff |
| AC3 | The standard includes a forbidden operator-question example matching the AAF-T7B confusion pattern | source diff |
| AC4 | The standard states RSE is documentation and reference only and an AHB local view, not a replacement | claim boundary and source diff |
| AC5 | A compact front-door README points to the standard | source diff |
| AC6 | No forbidden paths changed and the worker commits nothing | `git status --short`; worker-return gate |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: RSE-T0 is private provenance governance-protocol work. No public-sync
repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local workspace |
| Session or invocation | RSE-T0 worker execution, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, documentation authoring, required gates |
| Target paths | worker required deliverables |
| Allowed scope source | this work order and paired GC-018 baseline |
| Before status evidence | dispatchBaseHead `006986b4`; clean worktree verified before RSE-T0 dispatch authoring |
| After status evidence | RSE-T0 worker artifacts pending no-commit return |
| Diff evidence | worker records `git status --short` and gate receipts |
| Approval boundary | worker may create Required Deliverables but must not commit |
| Claim boundary | documentation-only standard; no checker, helper, runtime, provider, or public behavior |
| Agent type | worker role |
| Invocation ID | `rse-t0-role-switch-envelope-standard-worker-2026-06-22` |
| Expected manifest | standard; front door; worker return |
| Actual changed set | worker records in return packet |
| Manifest delta | worker records in return packet |

## Claim Boundary

This work order authorizes only the RSE-T0 documentation-only Role Switch
Envelope standard plus a front-door README and a worker return. It does not
authorize any checker, helper, or AAF diagnostic implementation, any change to
AHB-T2 or AHB-T3 semantics, any RSE-T1, T2, or T3 content, runtime behavior,
provider/live behavior, CLI/MCP adapter behavior, public-sync, session-sync by
the worker, direct interception, readiness claims, speed/cost claims, or
universal governed-coding control.
