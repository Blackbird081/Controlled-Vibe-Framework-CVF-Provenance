# CVF GC-018 - RSE-T0 Role Switch Envelope Standard

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: baseline

dispatchBaseHead: 006986b4

Batch ID: RSE-T0

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This baseline
authorizes one bounded documentation-only standard tranche; it does not map,
enumerate, project, or classify CVF state.

## Purpose

Authorize RSE-T0, the first tranche of the Role Switch Envelope lane. RSE-T0
creates a documentation-only reference standard that defines the canonical
envelope any agent uses when changing or accepting a role inside a governed
batch, plus a companion front-door README. The standard is a role-switch local
view of the ratified Agent Handoff Contract; it does not replace that contract
and adds no runtime, checker, or helper behavior.

RSE-T0 exists because the AAF-T7B worker routed a reviewer/closer
finding-promotion decision to the operator, which the operator and reviewer
classified as an operator-question boundary gap. The standard names the envelope
fields, gives a compliant worker-to-reviewer example, and records the AAF-T7B
confusing question as a forbidden operator-question pattern.

## Operator Authorization

The operator directed on 2026-06-22 that the RSE lane proceed with a specific
role model: Codex authored the full RSE roadmap T0 through T3; Claude authors the
work orders; Codex reviews each work order; Claude executes as worker; Codex
reviews and closes. This baseline authorizes only RSE-T0 documentation. RSE-T1,
T2, and T3 remain roadmap items requiring their own fresh GC-018 and work order.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 RSE role model: Codex roadmap, Claude work order, Codex review, Claude execute, Codex close | ACCEPT |
| RSE roadmap | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | ACCEPT |
| AAF-T7B completion review | `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_COMPLETION_2026-06-22.md` | ACCEPT |
| AAF-T7B gate-trap finding | `docs/reviews/CVF_AAF_T7B_WORKER_RETURN_GATE_TRAP_FINDING_2026-06-22.md` | ACCEPT |
| Agent Handoff Contract ratification | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACCEPT |
| AHB machine-check standard | `docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Agent error-to-governance philosophy | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V21_2026-06-22.md` | ACCEPT |

Provider-specific memory is not CVF authority. This dispatch is based on
repo-local CVF-governed artifacts and the ratified Agent Handoff Contract.

## Scope / Owner Boundary

Allowed worker scope:

- create `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md`
  defining the canonical role-switch envelope fields, a compliant
  worker-to-reviewer example, and at least one forbidden operator-question
  example matching the AAF-T7B confusion pattern;
- create `docs/reference/role_switch_envelope/README.md` as a compact front door
  for the standard;
- create
  `docs/reviews/CVF_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_WORKER_RETURN_2026-06-22.md`.

Reviewer/closer scope:

- update this baseline and the paired work order status after review;
- create
  `docs/reviews/CVF_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_COMPLETION_2026-06-22.md`;
- perform session-sync if accepted.

Forbidden worker scope:

- no checker, helper, or AAF diagnostic implementation; no edit to
  `governance/compat/` files; no edit to the AAF helper source or tests;
- no change to AHB-T2 or AHB-T3 contract semantics; the standard is a local view
  only;
- no RSE-T1, T2, or T3 content; no Operator Question Boundary classification
  rules, no Worker Return Jurisdiction Block requirement, no diagnostic wiring;
- no runtime, provider, live, web, CLI/MCP adapter, workspace, queue, daemon,
  watcher, public-sync, direct interception, readiness, or universal control
  behavior or claim;
- no generated aggregate edits and no session, handoff, or front-door edits by
  the worker.

Risk ceiling: R1 bounded documentation-only reference standard plus front door.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts created:

- `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md`
- `docs/reference/role_switch_envelope/README.md`
- `docs/reviews/CVF_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_WORKER_RETURN_2026-06-22.md`

No worker commit is authorized.

## Decision / Baseline / Proposed Tranche

Baseline decision: RSE-T0 is dispatched to worker as a bounded
documentation-only standard tranche.

Proposed tranche: `RSE-T0 Role Switch Envelope Standard`.

Tranche owner split: Codex authored the roadmap; Claude authored this GC-018
baseline and the paired work order; the worker implements the standard and front
door without committing; Codex reviews and commits accepted material if gates
pass.

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
| `role switch envelope` | RSE-T0 standard vocabulary | NEW_DOC_ONLY_TERM | names the field set an agent states when changing or accepting a role |
| `operatorQuestionAllowed` | RSE-T0 envelope field | NEW_DOC_ONLY_FIELD | doc-only field naming whether a role may ask the operator in the current phase |
| `findingCaptureSurface` | RSE-T0 envelope field | NEW_DOC_ONLY_FIELD | doc-only field naming where a worker records a finding inside allowed scope |
| `outOfScopePromotionRoute` | RSE-T0 envelope field | NEW_DOC_ONLY_FIELD | doc-only field naming the route for promoting an out-of-scope finding |

These are documentation-only fields named by the RSE roadmap T0 section. No
runtime schema, checker key, or helper output field is created by RSE-T0.

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `006986b4`.
- `git status --short` was clean before RSE-T0 dispatch authoring.
- `rg` and direct reads verified the RSE roadmap T0 fields and recommended scope,
  the Agent Handoff Contract CF-01 and CF-07 fields, the AHB machine-check
  required block heading, the guard orientation role glossary, the learning
  philosophy escalation ladder, and the AAF-T7B learning-capture decision.
- Confirmed `docs/reference/role_switch_envelope/` does not yet exist, so the
  worker creates a new directory with new files only.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base 006986b4 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 006986b4 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 006986b4 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 006986b4 --head HEAD --enforce
```

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/role_switch_envelope/` (new); RSE roadmap; AHB-T2 ratification; AHB machine-check standard |
| Runtime behavior claimed | N/A_WITH_REASON: documentation-only reference standard; no product runtime, provider route, web route, CLI/MCP adapter, checker, or helper behavior |
| Helper/checker implementation claimed | N/A_WITH_REASON: RSE-T0 is documentation only; no checker or helper is added |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded documentation standard only; no provider, public-sync, runtime product behavior, checker, helper, or generated aggregate behavior is claimed |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| A worker routed a reviewer/closer finding-promotion decision to the operator | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | WRITTEN_RULE_CANDIDATE | RSE-T0 standard defines the role-switch envelope and a forbidden operator-question example | handled by this dispatch |
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
  Verification Block in this baseline.
- Manifest hash: N/A with reason: bounded direct-read dispatch, no generated
  corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows
  in this baseline.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=Authority Chain and Source Verification Block; ledger_terminal=READ for cited source rows; exclusions=full-repo sweep, generated aggregate mutation, runtime/provider/web/MCP/public-sync sweep; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: full-repo sweep, generated aggregate mutation,
  runtime/provider/web/MCP/public-sync sweep, public-sync proof, provider/live
  proof.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by dispatch.
- Drift check: N/A with reason: no generated aggregate edited by dispatch.
- Output traceability: RSE-T0 baseline maps the RSE roadmap T0 section to a
  bounded documentation-only standard work order.
- Adversarial verification: source rows distinguish the new RSE local-view
  standard from the existing ratified Agent Handoff Contract it views.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: RSE-T0 is private provenance governance-protocol work. No public-sync
repository work or public catalog claim is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | RSE-T0 Role Switch Envelope Standard dispatch |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, or provider interception claim |
| claimLanguage | documentation-only reference standard |
| forbiddenExpansion | checker or helper implementation, runtime role router, agent workspace, AHB semantics change, RSE-T1/T2/T3 content, provider/live, public-sync, queue/daemon/watcher, direct interception, readiness, and universal control remain out of scope |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | BOUNDED: creates one new reference directory `docs/reference/role_switch_envelope/` for the RSE-T0 standard and its front door. |
| New durable foundation directory | `docs/reference/role_switch_envelope/` for documentation reference only. |
| Generated aggregate impact | N/A with reason: no generated aggregate is created or edited. |
| INDEX impact | N/A with reason: this is not an INDEX artifact or INDEX storage tranche. |
| Guard owner | reviewer/closer verifies the new directory holds only the authorized RSE-T0 reference files. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: RSE-T0 creates only new
documentation reference files under `docs/reference/role_switch_envelope/` and a
new worker-return artifact under `docs/reviews/`. It modifies no protected
`governance/compat/` file, no protected guard markdown, and no session JSON, so
no Core Guard Self-Protection block listing protected paths is required for the
worker change set.

Operator authorization: the operator directed the RSE lane to proceed under the
stated role model. This baseline authorizes only RSE-T0 documentation.

Rollback boundary: revert the accepted RSE-T0 material closure commit to remove
the new role-switch envelope standard, its front door, and the worker return
together; the new directory is removed if it becomes empty.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher (Claude work-order author) |
| Provider or surface | local workspace |
| Session or invocation | RSE-T0 dispatch authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, `rg`, dispatch authoring, governance gates |
| Target paths | this GC-018 baseline and paired RSE-T0 work order |
| Allowed scope source | operator RSE role model and the RSE roadmap T0 section |
| Before status evidence | HEAD `006986b4`; clean worktree before dispatch authoring |
| After status evidence | RSE-T0 dispatch artifacts pending pre-dispatch gates |
| Diff evidence | dispatch diff plus AAF helper, dispatch-quality, and pre-dispatch autorun receipts |
| Approval boundary | dispatch authoring only; worker implementation remains no-commit; Codex reviews this work order before execution |
| Claim boundary | documentation-only standard dispatch; no runtime, provider, checker, helper, or public behavior |
| Agent type | dispatcher |
| Invocation ID | `rse-t0-role-switch-envelope-standard-dispatch-2026-06-22` |
| Expected manifest | this baseline; paired RSE-T0 work order |
| Actual changed set | this baseline and paired RSE-T0 work order |
| Manifest delta | MATCH |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | The standard names every minimum role-switch envelope field from the roadmap T0 section. |
| AC2 | The standard gives at least one compliant worker-to-reviewer role-switch example. |
| AC3 | The standard gives at least one forbidden operator-question example matching the AAF-T7B confusion pattern. |
| AC4 | The standard states RSE is documentation and reference only until a later checker tranche, and that it is a local view of the ratified Agent Handoff Contract, not a replacement. |
| AC5 | A compact front-door README points to the standard. |
| AC6 | Worker return records actual base, status, changed set, source inventory, gates, and claim boundary, and the worker commits nothing. |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this artifact | `Status: DISPATCHED_TO_WORKER` until reviewer closure | PENDING_REVIEW |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_FOR_WORKER_2026-06-22.md` | `Status: DISPATCHED_TO_WORKER` until reviewer closure | PENDING_REVIEW |
| Worker return | `docs/reviews/CVF_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_WORKER_RETURN_2026-06-22.md` | worker returns `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` | PENDING_WORKER |
| Completion or reviewer artifact | `docs/reviews/CVF_RSE_T0_ROLE_SWITCH_ENVELOPE_STANDARD_COMPLETION_2026-06-22.md` | reviewer/closer creates only if accepted | PENDING_REVIEW |
| Runtime/provider/live evidence | N/A | no runtime/provider/live behavior authorized | N/A with reason |
| Public-sync evidence | N/A | no public-sync authorized | N/A with reason |
| Session continuity | active session front-door/state/handoff | session-sync follows accepted dispatch/closure commit if needed | PENDING_SESSION_SYNC |

## Claim Boundary

RSE-T0 authorizes only a bounded documentation-only Role Switch Envelope
standard plus a front-door README and a worker return. It does not authorize any
checker, helper, or AAF diagnostic implementation, any change to AHB-T2 or AHB-T3
semantics, any RSE-T1, T2, or T3 content, runtime behavior, provider/live
behavior, CLI/MCP adapter behavior, public-sync, session-sync by the worker,
direct interception, readiness claims, speed/cost claims, or universal
governed-coding control.
