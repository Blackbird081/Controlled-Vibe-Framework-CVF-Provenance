# CVF Agent Work Order - RSE-T2 Worker Return Jurisdiction Block

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-22

docType: work_order

dispatchBaseHead: 2dd54bc5

Commit mode: `WORKER_MUST_NOT_COMMIT`

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This work order
authorizes one bounded documentation-only addendum tranche; it does not map,
enumerate, project, or classify CVF state.

## Dispatch Prompt Envelope

Role: Worker. Reviewer/closer is a separate role after worker return.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_FOR_WORKER_2026-06-22.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: record with `git rev-parse --short HEAD` at worker start.

Current-time notes: RSE-T1 is closed (`50679d36`, sync `2dd54bc5`). The roadmap
author completed the RSE roadmap T0 through T3, and the dispatch author prepared
this work order and the paired GC-018 baseline. Per the operator role model, the
work-order reviewer accepts the packet before execution; the worker then returns
uncommitted work for the reviewer/closer. RSE-T2 is documentation only.

Do-not-misread notes: implement only the RSE-T2 documentation addendum. Do not
implement any checker, helper, or AAF diagnostic; do not edit `governance/compat/`
files, dispatch-quality checker code, or the work-order template enforcement
code; do not edit the closed RSE-T0 standard, the closed RSE-T1 addendum, or any
existing governed artifact; do not change AHB-T2 or AHB-T3 contract semantics; do
not author RSE-T3 content; do not add runtime, provider/live, public-sync,
CLI/MCP adapter, workspace, queue, daemon, watcher, direct interception,
readiness, or universal control behavior or claim.

Required first actions: read this work order, read the RSE-T2 GC-018 baseline,
read the RSE roadmap T2 section, read the closed RSE-T1 addendum and the closed
RSE-T0 standard, read the Guard Orientation Index role glossary, read the AAF-T7B
completion review learning capture decision, confirm actual `executionBaseHead`,
and inspect current `git status --short`.

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
| Intake source | operator instruction to close RSE-T1 and open RSE-T2 Worker Return Jurisdiction Block |
| Intake role | worker creates the RSE-T2 documentation addendum |
| Reviewer role | reviewer/closer validates block-field coverage, the capture-versus-promotion separation, the placement recommendation, and claim boundary |
| Routing decision | `WORKER_MUST_NOT_COMMIT`; bounded documentation addendum only |
| Public route | `DEFERRED_PRIVATE_ONLY`; no public-sync |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | roadmap author, dispatch author, work-order reviewer, worker, reviewer/closer |
| escalation condition | stop and return `BLOCKED_WITH_REASON` if implementation would require any checker or helper code, edit to the work-order template enforcement, edit to the closed RSE-T0 or RSE-T1 documents, AHB semantics change, RSE-T3 content, runtime/provider/live, public-sync, session/handoff edits, or forbidden path scope |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | roadmap author -> dispatch author -> work-order reviewer -> worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING; WORK_ORDER_REVIEW; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=2dd54bc5`; `executionBaseHead` recorded by worker; `closureBaseHead` set by reviewer before closure commit |
| changedSetScope(phase) | worker changes only Required Deliverables; reviewer/closer owns status/closure/session-sync if accepted |
| traceScope(phase, actor) | one worker-return trace covers pending RSE-T2 artifacts; one reviewer trace covers review/closure |
| commitOwner(phase) | worker commits nothing (`WORKER_MUST_NOT_COMMIT`); reviewer/closer owns any material/closure/session-sync commit |
| crossBatchIsolation | do not mix RSE-T2 with RSE-T0 or RSE-T1 edits, RSE-T3, AAF, MPI, runtime/provider/live, MCP adapter, public-sync, queue/daemon, direct-interception, generated aggregate, or memory-plane work |
| Before status evidence | dispatchBaseHead `2dd54bc5`; clean worktree verified before RSE-T2 dispatch authoring |
| nextMoveSurfaces | reviewer/closer updates next-move surfaces only after review if mode or next allowed move changes |
| Closer designation | reviewer/closer role is the designated closer |

## Reviewer Closure Conversion

| Field | Disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_COMPLETION_2026-06-22.md` |
| reviewerOwnedClosurePaths | this work order; GC-018 baseline; accepted addendum file; worker-return artifact; reviewer-owned completion review; optional session-sync surfaces if accepted |
| workerReturnStatus | `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| closer | reviewer/closer role |

## Required First Reads

| Source | Reason |
|---|---|
| `docs/reference/guard_orientation/README.md` | task-first guard map, role glossary, and worker-return packet shape |
| `docs/baselines/CVF_GC018_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_2026-06-22.md` | GC-018 authorization and claim boundary |
| `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | roadmap T2 block fields and acceptance criteria |
| `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | the closed RSE-T1 question classes the block routes against |
| `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md` | the closed RSE-T0 envelope fields the block reuses |
| `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_COMPLETION_2026-06-22.md` | the AAF-T7B confusion pattern the block prevents |

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
`BLOCKED_WITH_REASON` if a required command cannot run. RSE-T2 adds no Python
file, so the fast-gate pytest target is the existing AAF helper test module used
only as the fast-gate routing target, not as a new test surface.

## Worker Autonomy / No-Question Rule

Within Allowed scope, the worker must repair machine-gate, source-inventory,
packet-shape, or documentation-structure defects and rerun the required checks
without asking the operator. Ask the operator only if remediation would exceed
Allowed scope, change the claim boundary, require checker/helper/runtime/provider/
public/session scope, require AHB semantics change, require an edit to the
work-order template enforcement or the closed RSE-T0 or RSE-T1 documents, require
RSE-T3 content, touch forbidden paths, consume secrets/quota, require a
destructive action, or contradict this work order. Worker-to-reviewer questions
are routed to the reviewer/closer in the worker return, not escalated to the
operator. This rule and the deliverable itself are instances of the RSE boundary
the addendum documents.

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
2. Create the addendum file inside the existing
   `docs/reference/role_switch_envelope/` directory.
3. Define the `## Worker Return Jurisdiction Block` with the candidate fields from
   the roadmap T2 section, each with a one-line meaning.
4. Keep finding capture and promotion routing as separate fields, and state that
   operator action is required only when an RSE-T1 `ASK_OPERATOR` class is
   present.
5. State that no worker is granted authority to edit out-of-scope lane memory or
   checkers.
6. Record a placement recommendation (work-order template, Worker Return Packet
   Shape Contract, AAF helper diagnostics, or a future checker) and defer machine
   enforcement to RSE-T3.
7. State the documentation-only boundary and the build on the closed RSE-T0
   standard and RSE-T1 addendum.
8. Run required checks and create the worker-return artifact without committing.

## Write Ownership

| Path | Owner during worker execution | Disposition |
|---|---|---|
| `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | worker | create the RSE-T2 documentation addendum |
| `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_WORKER_RETURN_2026-06-22.md` | worker | create |
| `docs/baselines/CVF_GC018_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_2026-06-22.md` | reviewer/closer | no worker edit |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_FOR_WORKER_2026-06-22.md` | reviewer/closer | no worker edit |
| `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md`, `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md`, `docs/reference/role_switch_envelope/README.md` | not worker-editable | forbidden: closed RSE-T0 and RSE-T1 artifacts |
| `governance/compat/**`, dispatch-quality checker, work-order template enforcement, AHB contract files, `AGENTS.md`, `CVF_SESSION/**`, active handoff, runtime routes, web, MCP, provider registry, generated aggregates, public-sync, queue/daemon/watcher, RSE-T3 files | out of worker scope | forbidden |

## Operator Checkpoint

No operator checkpoint is required for routine allowed-scope remediation inside
this work order. Operator checkpoint is required only if execution would require
checker or helper implementation, an edit to the work-order template enforcement
or the closed RSE-T0 or RSE-T1 documents, AHB semantics change, RSE-T3 content,
runtime/product behavior, generated aggregate edits, AGENTS/session/handoff
edits, provider/live/public-sync scope, dependency installation, secrets/quota,
destructive action, or a change to the claim boundary.

## Purpose

Create the RSE-T2 Worker Return Jurisdiction Block addendum: a documentation-only
reference that defines a structured worker-return block carrying routing data, so
a reviewer or closer can act without asking the operator. It keeps finding
capture and promotion routing as separate fields, records a placement
recommendation, and defers machine enforcement to RSE-T3. It builds on the closed
RSE-T0 standard and RSE-T1 addendum and is a local view of the Agent Handoff
Contract.

## Agent Roles

| Role | Owner |
|---|---|
| Operator | project authority and scope approval |
| Roadmap author | roadmap author role |
| Dispatcher | dispatch author role |
| Work-order reviewer | work-order reviewer role before execution |
| Worker | RSE-T2 addendum author role |
| Reviewer | review role after worker return |
| Closer | closer role after acceptance |
| Session-sync steward | session-sync steward role if session-sync is required |

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 close RSE-T1; open RSE-T2 Worker Return Jurisdiction Block | ACCEPT |
| RSE-T2 GC-018 | `docs/baselines/CVF_GC018_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_2026-06-22.md` | ACCEPT |
| RSE roadmap | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | ACCEPT |
| RSE-T1 addendum | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | ACCEPT |
| RSE-T0 standard | `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md` | ACCEPT |
| Agent Handoff Contract ratification | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| AAF-T7B completion review | `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_COMPLETION_2026-06-22.md` | ACCEPT |
| Agent error-to-governance philosophy | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md`
  with the `## Worker Return Jurisdiction Block` and candidate fields, separate
  capture and promotion fields, the operator-action condition, the
  no-self-widening rule, a placement recommendation, and an explicit
  documentation-only and AHB-local-view boundary;
- create
  `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_WORKER_RETURN_2026-06-22.md`;
- reviewer/closer closure conversion may update
  `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_FOR_WORKER_2026-06-22.md`;
- reviewer/closer closure conversion may update
  `docs/baselines/CVF_GC018_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_2026-06-22.md`;
- reviewer/closer closure conversion may create
  `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_COMPLETION_2026-06-22.md`
  after accepting the worker return.

Forbidden scope:

- no checker, helper, or AAF diagnostic implementation and no edit to
  `governance/compat/` files, dispatch-quality checker code, or work-order
  template enforcement code;
- no edit to the closed RSE-T0 standard, the closed RSE-T1 addendum, the front
  door, or any existing governed artifact;
- no change to AHB-T2 or AHB-T3 contract semantics;
- no RSE-T3 content;
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
| Roadmap T2 names the Worker Return Jurisdiction Block and its candidate fields | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | line 220 | T2 - Worker Return Jurisdiction Block | RSE roadmap T2 section | ACCEPT |
| Roadmap T2 acceptance criteria require separate capture and promotion fields and the operator-action condition | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | line 250 | RSE-T2 acceptance criteria | RSE roadmap T2 section | ACCEPT |
| RSE-T1 addendum defines the four question classes the block routes against | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | line 48 | Question Classification | RSE-T1 addendum | ACCEPT |
| RSE-T1 addendum separates finding capture from promotion routing | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | line 74 | Finding Capture And Promotion Are Separate | RSE-T1 addendum | ACCEPT |
| RSE-T0 standard defines the findingCaptureSurface envelope field | `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md` | line 98 | findingCaptureSurface | RSE-T0 envelope field set | ACCEPT |
| RSE-T0 standard defines the outOfScopePromotionRoute envelope field | `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md` | line 99 | outOfScopePromotionRoute | RSE-T0 envelope field set | ACCEPT |
| Guard Orientation Index defines the canonical role glossary | `docs/reference/guard_orientation/README.md` | line 56 | Role Glossary | guard orientation index | ACCEPT |
| AAF-T7B closure records the operator-question confusion pattern the block prevents | `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_COMPLETION_2026-06-22.md` | line 109 | Learning Capture Decision | AAF-T7B completion review | ACCEPT |

## New Standard Terms

| Proposed term | Owner in RSE-T2 | Runtime status | Reason |
|---|---|---|---|
| `CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md` | RSE-T2 reference addendum | NEW_DOC_ONLY_REFERENCE | the worker-return jurisdiction block addendum, documentation only |
| `Worker Return Jurisdiction Block` | RSE-T2 documentation block | NEW_DOC_ONLY_BLOCK | doc-only worker-return section name carrying routing data |
| `findingRecorded` | RSE-T2 block field | NEW_DOC_ONLY_FIELD | doc-only field stating whether a finding was captured |
| `outOfScopePromotionCandidate` | RSE-T2 block field | NEW_DOC_ONLY_FIELD | doc-only field naming a finding that may need promotion |
| `operatorActionRequired` | RSE-T2 block field | NEW_DOC_ONLY_FIELD | doc-only field stating whether an operator-owned class is present |

## Roadmap-to-Work-Order Trace Matrix

| Roadmap item | Source | Work-order coverage | Evidence requirement |
|---|---|---|---|
| RSE-T2 Worker Return Jurisdiction Block and fields | roadmap line 220 | addendum defines the block and candidate fields | source diff and worker return |
| RSE-T2 separate capture and promotion fields | roadmap line 250 | addendum keeps them as distinct fields | source diff |
| RSE-T2 operator-action condition | roadmap line 250 | addendum ties operatorActionRequired to an ASK_OPERATOR class | source diff |
| RSE-T2 no-self-widening rule | roadmap line 250 | addendum states no worker edits out-of-scope artifacts | source diff |
| RSE-T3 | roadmap line 259 | excluded from this tranche | claim boundary and no T3 content |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | local governed role-boundary protocol route, not external authority |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; pre-dispatch autorun |
| Owner surface | RSE-T2 Worker Return Jurisdiction Block addendum |
| Disposition | ADAPT as a CVF-owned documentation addendum with bounded scope |
| Claim boundary | operator critique remains input only until implemented and closed through this governed work order |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/role_switch_envelope/` (existing RSE-T0 and RSE-T1 plus new addendum); RSE roadmap; RSE-T1 addendum |
| Runtime behavior claimed | N/A_WITH_REASON: documentation-only reference addendum; no product runtime, provider route, web route, CLI/MCP adapter, checker, or helper behavior |
| Helper/checker implementation claimed | N/A_WITH_REASON: RSE-T2 is documentation only; no checker or helper is added |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded documentation addendum only; no provider, public-sync, runtime product behavior, checker, helper, or generated aggregate behavior is claimed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | RSE-T2 Worker Return Jurisdiction Block addendum |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, or provider interception claim |
| claimLanguage | documentation-only reference addendum |
| forbiddenExpansion | checker or helper implementation, work-order template enforcement edit, runtime role router, agent workspace, AHB semantics change, RSE-T0 or RSE-T1 edit, RSE-T3 content, provider/live, public-sync, queue/daemon/watcher, direct interception, readiness, and universal control remain out of scope |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker returns lacked structured routing data so reviewer needs to infer jurisdiction | RULE_GAP | GOVERNANCE_CONTROL_PLANE | WRITTEN_RULE_CANDIDATE | RSE-T2 defines the Worker Return Jurisdiction Block fields | handled by this dispatch |
| Block placement and machine enforcement need a decision | RULE_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | RSE-T2 records a placement recommendation; RSE-T3 may enforce it | deferred |
| Operator-question boundary needs machine enforcement eventually | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | RSE-T3 may add diagnostics after T2 | deferred |
| Runtime/provider/cost applicability for this dispatch | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime, provider, or cost behavior changed or claimed | handled |

## Corpus Completeness And Report Integrity

- Corpus task class: dispatch source verification for a bounded
  documentation-only addendum tranche.
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
- Output traceability: RSE-T2 work order maps the RSE roadmap T2 section to
  worker deliverables and required gates.
- Adversarial verification: source rows distinguish the new RSE-T2 addendum from
  the closed RSE-T0 standard and RSE-T1 addendum it builds on, and from the
  ratified Agent Handoff Contract.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Core Guard Self-Protection Authorization

N/A with reason: RSE-T2 creates only one new documentation reference file inside
`docs/reference/role_switch_envelope/` and a new worker-return artifact under
`docs/reviews/`. It modifies no protected `governance/compat/` file, no protected
guard markdown, and no session JSON, so no Core Guard Self-Protection block
listing protected paths is required for the worker change set.

Operator authorization: the operator directed RSE-T1 closed and RSE-T2 open under
the stated role model. This work order authorizes only RSE-T2 documentation.

Rollback boundary: revert the accepted RSE-T2 material closure commit to remove
the new addendum and the worker return together.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | N/A with reason: adds one new file inside the existing `docs/reference/role_switch_envelope/` directory; creates no new durable foundation directory and relocates nothing. |
| New durable foundation directory | N/A with reason: the directory already exists from RSE-T0. |
| Generated aggregate impact | N/A with reason: no generated aggregate is created or edited. |
| INDEX impact | N/A with reason: this is not an INDEX artifact or INDEX storage tranche. |
| Guard owner | reviewer/closer verifies the addendum is one new sibling file and the closed RSE-T0 and RSE-T1 files are unchanged. |

## Evidence Requirements

The worker-return artifact must record:

- actual `executionBaseHead`;
- actual `git status --short`;
- source inventory and scan-depth ledger;
- changed-path list;
- AAF helper smoke result with `--json --enforce`;
- pre-implementation autorun gate result;
- worker-return fast gate result;
- explicit statement that the addendum defines the Worker Return Jurisdiction
  Block and its candidate fields;
- explicit statement that capture and promotion are separate fields and that
  operator action is tied to an RSE-T1 ASK_OPERATOR class;
- explicit statement that no worker is granted authority to edit out-of-scope
  lane memory or checkers, and that a placement recommendation defers machine
  enforcement to RSE-T3;
- explicit statement that the addendum is documentation-only, builds on the
  closed RSE-T0 standard and RSE-T1 addendum, and is an AHB local view;
- explicit statement that no checker, helper, AAF diagnostic, work-order template
  enforcement, RSE-T0 or RSE-T1 edit, AHB semantics, RSE-T3 content, runtime,
  provider/live, public-sync, generated aggregate, or session/handoff path was
  edited;
- exact claim boundary and public export disposition.

## Review Gate

Reviewer/closer must inspect the worker-return changed set against Required
Deliverables, run reviewer-fast gates, verify no forbidden scope was touched,
verify the addendum defines the block and its fields, keeps capture and promotion
separate, states the operator-action condition and the no-self-widening rule,
records a placement recommendation, verifies the documentation-only and
AHB-local-view boundary, verifies the closed RSE-T0 and RSE-T1 files are
unchanged, and only then convert accepted material into a completion review.

## Closure Checklist

- [x] Worker returned `COMPLETE_PENDING_REVIEW`.
- [x] Changed files stay inside Required Deliverables.
- [x] Addendum defines the Worker Return Jurisdiction Block and candidate fields.
- [x] Capture and promotion are separate fields.
- [x] Operator action is tied to an RSE-T1 ASK_OPERATOR class.
- [x] Addendum states no worker edits out-of-scope lane memory or checkers.
- [x] Addendum records a placement recommendation and defers enforcement to RSE-T3.
- [x] Addendum states documentation-only and AHB local-view boundary.
- [x] Closed RSE-T0 standard, RSE-T1 addendum, and front door are unchanged.
- [x] Worker performed no checker, helper, template enforcement edit, RSE-T0 or RSE-T1 edit, AHB semantics, RSE-T3, staging, commit, push, provider/live call, or closure decision.
- [x] Worker-return fast gate passes.
- [x] Reviewer-owned completion review created.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all required deliverables are present,
required checks have been run or source-blocked with evidence, and changed files
remain inside Allowed scope.

Return `BLOCKED_WITH_REASON` when a required source is missing, a required gate
cannot pass inside Allowed scope, or the repair would require forbidden
checker/helper/template-enforcement/RSE-T0-or-RSE-T1-edit/AHB-semantics/RSE-T3/runtime/provider/public/session
scope.

## Acceptance Criteria

| ID | Requirement | Evidence |
|---|---|---|
| AC1 | The addendum defines the Worker Return Jurisdiction Block with the candidate fields or a source-verified equivalent | source diff and worker return |
| AC2 | Finding capture and promotion routing are separate fields | source diff |
| AC3 | The addendum states operator action is required only when an RSE-T1 ASK_OPERATOR class is present | source diff |
| AC4 | The addendum states no worker is granted authority to edit out-of-scope lane memory or checkers | source diff |
| AC5 | The addendum records a placement recommendation, defers enforcement to RSE-T3, and states documentation-only plus AHB local-view boundary built on RSE-T0 and RSE-T1 | claim boundary and source diff |
| AC6 | No forbidden paths changed, the closed RSE-T0 and RSE-T1 files are unchanged, and the worker commits nothing | `git status --short`; worker-return gate |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED`; checklist checked | PASS |
| Worker return | `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_WORKER_RETURN_2026-06-22.md` | `Status: COMPLETE_PENDING_REVIEW` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_COMPLETION_2026-06-22.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | roadmap remains `ROADMAP_READY_FOR_WORK_ORDER_AUTHORING`; T2 closed by completion review | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | aggregate drift check passes; no mutation required | PASS |
| Registry Markdown | `docs/reference/role_switch_envelope/README.md` | active RSE reference front door remains present and unchanged | PASS |
| External evidence digest | N/A | no external evidence digest created or consumed | N/A with reason |
| System loop interlock | N/A | no interlock surface changed | N/A with reason |
| Runtime/provider/live evidence | N/A | no runtime/provider/live behavior | N/A with reason |
| Public-sync evidence | N/A | no public-sync authorized | N/A with reason |
| Session continuity | active session front-door, state, and handoff | separate session-sync follows material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Receipt/query acceptance evidence | N/A with reason: RSE-T2 creates no receipt/query acceptance surface | PASS |
| Runtime receipt value | N/A with reason: no runtime execution or provider call | PASS |
| Delta receipt value | N/A with reason: no Delta execution-control claim | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: RSE-T2 is private provenance governance-protocol work. No public-sync
repository work or public catalog claim is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local workspace |
| Session or invocation | RSE-T2 worker execution, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, documentation authoring, required gates |
| Target paths | worker required deliverables |
| Allowed scope source | this work order and paired GC-018 baseline |
| Before status evidence | dispatchBaseHead `2dd54bc5`; clean worktree verified before RSE-T2 dispatch authoring |
| After status evidence | RSE-T2 worker artifacts pending no-commit return |
| Diff evidence | worker records `git status --short` and gate receipts |
| Approval boundary | worker may create Required Deliverables but must not commit |
| Claim boundary | documentation-only addendum; no checker, helper, runtime, provider, or public behavior |
| Agent type | worker role |
| Invocation ID | `rse-t2-worker-return-jurisdiction-block-worker-2026-06-22` |
| Expected manifest | addendum; worker return |
| Actual changed set | worker records in return packet |
| Manifest delta | worker records in return packet |

## Claim Boundary

This work order authorizes only the RSE-T2 documentation-only Worker Return
Jurisdiction Block addendum built on the closed RSE-T0 standard and RSE-T1
addendum plus a worker return. It does not authorize any checker, helper, or AAF
diagnostic implementation, any edit to the work-order template enforcement code,
the closed RSE-T0 standard, the closed RSE-T1 addendum, or any existing governed
artifact, any change to AHB-T2 or AHB-T3 semantics, any RSE-T3 content, runtime
behavior, provider/live behavior, CLI/MCP adapter behavior, public-sync,
session-sync by the worker, direct interception, readiness claims, speed/cost
claims, or universal governed-coding control.
