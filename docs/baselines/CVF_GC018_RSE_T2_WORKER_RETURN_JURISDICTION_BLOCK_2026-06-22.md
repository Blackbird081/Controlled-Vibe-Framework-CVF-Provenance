# CVF GC-018 - RSE-T2 Worker Return Jurisdiction Block

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

Date: 2026-06-22

docType: baseline

dispatchBaseHead: 2dd54bc5

Batch ID: RSE-T2

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This baseline
authorizes one bounded documentation-only addendum tranche; it does not map,
enumerate, project, or classify CVF state.

## Purpose

Authorize RSE-T2, the third tranche of the Role Switch Envelope lane. RSE-T2
creates a documentation-only Worker Return Jurisdiction Block addendum to the
closed RSE-T0 standard and RSE-T1 addendum. The addendum defines a structured
`## Worker Return Jurisdiction Block` with the candidate fields from the roadmap
T2 section, so a worker return carries enough routing data for a reviewer or
closer to act without asking the operator.

The addendum separates finding capture from promotion routing as distinct fields,
states that operator action is required only when an RSE-T1 `ASK_OPERATOR` class
is present, and states that no worker is granted authority to edit out-of-scope
lane memory or checkers. RSE-T2 also records a placement recommendation for the
block and defers machine enforcement to RSE-T3. RSE-T2 is documentation and
reference only; it adds no checker, helper, or runtime behavior.

## Operator Authorization

The operator directed on 2026-06-22 that RSE-T1 is closed and the next proposed
move is to open RSE-T2 Worker Return Jurisdiction Block. This proceeds under the
RSE role model: roadmap author, dispatch author, work-order reviewer, worker, and
reviewer/closer. This baseline authorizes only RSE-T2 documentation. RSE-T3
remains a roadmap item requiring its own fresh GC-018 and work order.

## Authority Chain

| Authority | Path or value | Disposition |
|---|---|---|
| Operator instruction | 2026-06-22 close RSE-T1; open RSE-T2 Worker Return Jurisdiction Block | ACCEPT |
| RSE roadmap | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | ACCEPT |
| RSE-T0 standard | `docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md` | ACCEPT |
| RSE-T1 addendum | `docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md` | ACCEPT |
| RSE-T1 completion review | `docs/reviews/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_COMPLETION_2026-06-22.md` | ACCEPT |
| AAF-T7B completion review | `docs/reviews/CVF_AAF_T7B_REVIEWER_COMPLETION_SCAFFOLD_HELPER_COMPLETION_2026-06-22.md` | ACCEPT |
| Agent Handoff Contract ratification | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | ACCEPT |
| Guard Orientation Index | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Agent error-to-governance philosophy | `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md` | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V21_2026-06-22.md` | ACCEPT |

Provider-specific memory is not CVF authority. This dispatch is based on
repo-local CVF-governed artifacts and the closed RSE-T0 and RSE-T1 documents.

## Scope / Owner Boundary

Allowed worker scope:

- create `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md`
  defining the `## Worker Return Jurisdiction Block` and its candidate fields, the
  separation of finding capture from promotion routing, the operator-action
  condition, the no-self-widening rule, and a placement recommendation, built on
  the closed RSE-T0 standard and RSE-T1 addendum;
- create
  `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_WORKER_RETURN_2026-06-22.md`.

Reviewer/closer scope:

- update
  `docs/baselines/CVF_GC018_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_2026-06-22.md`;
- update
  `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_FOR_WORKER_2026-06-22.md`;
- create
  `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_COMPLETION_2026-06-22.md`;
- perform session-sync if accepted.

Forbidden worker scope:

- no checker, helper, or AAF diagnostic implementation; no edit to
  `governance/compat/` files; no edit to dispatch-quality checker code;
- no edit to the Worker Return Packet Shape Contract enforcement code, the
  work-order template, or any existing governed artifact, including the closed
  RSE-T0 standard and RSE-T1 addendum;
- no change to AHB-T2 or AHB-T3 contract semantics; the addendum is a local view
  only;
- no RSE-T3 content; no diagnostic wiring;
- no runtime, provider, live, web, CLI/MCP adapter, workspace, queue, daemon,
  watcher, public-sync, direct interception, readiness, or universal control
  behavior or claim;
- no generated aggregate edits and no session, handoff, or front-door edits by
  the worker.

Risk ceiling: R1 bounded documentation-only reference addendum.

## Required Deliverables

The worker must return uncommitted `COMPLETE_PENDING_REVIEW` with only these
worker-owned artifacts created:

- `docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md`
- `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_WORKER_RETURN_2026-06-22.md`

No worker commit is authorized.

## Decision / Baseline / Proposed Tranche

Baseline decision: RSE-T2 is dispatched to worker as a bounded
documentation-only addendum tranche.

Proposed tranche: `RSE-T2 Worker Return Jurisdiction Block`.

Tranche owner split: the roadmap author owns the roadmap; the dispatch author
owns this GC-018 baseline and the paired work order; the worker implements the
addendum without committing; the reviewer/closer reviews and commits accepted
material if gates pass.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Roadmap T2 names the Worker Return Jurisdiction Block and its candidate fields | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | line 220 | T2 - Worker Return Jurisdiction Block | RSE roadmap T2 section | ACCEPT |
| Roadmap T2 acceptance criteria require separate capture and promotion fields and the operator-action condition | `docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md` | line 250 | Acceptance criteria for a future T2 work order | RSE roadmap T2 section | ACCEPT |
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

These are documentation-only fields named by the RSE roadmap T2 section. No
runtime schema, checker key, or helper output field is created by RSE-T2.

## Evidence / Verification

Dispatch author verification before this packet:

- `git rev-parse --short HEAD` returned `2dd54bc5`.
- `git status --short` was clean before RSE-T2 dispatch authoring.
- `rg` and direct reads verified the RSE roadmap T2 block and candidate fields,
  the closed RSE-T1 question classification and capture-versus-promotion section,
  the RSE-T0 envelope fields, the guard orientation role glossary, and the
  AAF-T7B learning-capture decision.
- Confirmed `docs/reference/role_switch_envelope/` exists with the closed RSE-T0
  and RSE-T1 files, so the worker adds one new sibling addendum without editing
  them.

Required pre-dispatch verification before dispatch commit:

```powershell
python governance/compat/run_agent_automation_assist.py --base 2dd54bc5 --head HEAD --json --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 2dd54bc5 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base 2dd54bc5 --head HEAD --enforce
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 2dd54bc5 --head HEAD --enforce
```

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `docs/reference/role_switch_envelope/` (existing RSE-T0 and RSE-T1 plus new addendum); RSE roadmap; RSE-T1 addendum |
| Runtime behavior claimed | N/A_WITH_REASON: documentation-only reference addendum; no product runtime, provider route, web route, CLI/MCP adapter, checker, or helper behavior |
| Helper/checker implementation claimed | N/A_WITH_REASON: RSE-T2 is documentation only; no checker or helper is added |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS - bounded documentation addendum only; no provider, public-sync, runtime product behavior, checker, helper, or generated aggregate behavior is claimed |

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
- Output traceability: RSE-T2 baseline maps the RSE roadmap T2 section to a
  bounded documentation-only addendum work order.
- Adversarial verification: source rows distinguish the new RSE-T2 addendum from
  the closed RSE-T0 standard and RSE-T1 addendum it builds on, and from the
  ratified Agent Handoff Contract.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: RSE-T2 is private provenance governance-protocol work. No public-sync
repository work or public catalog claim is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | RSE-T2 Worker Return Jurisdiction Block dispatch |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | documentation authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, or provider interception claim |
| claimLanguage | documentation-only reference addendum |
| forbiddenExpansion | checker or helper implementation, work-order template enforcement edit, runtime role router, agent workspace, AHB semantics change, RSE-T0 or RSE-T1 edit, RSE-T3 content, provider/live, public-sync, queue/daemon/watcher, direct interception, readiness, and universal control remain out of scope |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Storage layout change | N/A with reason: adds one new file inside the existing `docs/reference/role_switch_envelope/` directory; creates no new durable foundation directory and relocates nothing. |
| New durable foundation directory | N/A with reason: the directory already exists from RSE-T0. |
| Generated aggregate impact | N/A with reason: no generated aggregate is created or edited. |
| INDEX impact | N/A with reason: this is not an INDEX artifact or INDEX storage tranche. |
| Guard owner | reviewer/closer verifies the addendum is one new sibling file and the closed RSE-T0 and RSE-T1 files are unchanged. |

## Core Guard Self-Protection Authorization

N/A with reason: RSE-T2 creates only one new documentation reference file inside
`docs/reference/role_switch_envelope/` and a new worker-return artifact under
`docs/reviews/`. It modifies no protected `governance/compat/` file, no protected
guard markdown, and no session JSON, so no Core Guard Self-Protection block
listing protected paths is required for the worker change set.

Operator authorization: the operator directed RSE-T1 closed and RSE-T2 open under
the stated role model. This baseline authorizes only RSE-T2 documentation.

Rollback boundary: revert the accepted RSE-T2 material closure commit to remove
the new worker-return jurisdiction block addendum and the worker return together.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local workspace |
| Session or invocation | RSE-T2 dispatch authoring, 2026-06-22 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | file reads, `rg`, dispatch authoring, governance gates |
| Target paths | this GC-018 baseline and paired RSE-T2 work order |
| Allowed scope source | operator RSE role model and the RSE roadmap T2 section |
| Before status evidence | HEAD `2dd54bc5`; clean worktree before dispatch authoring |
| After status evidence | RSE-T2 dispatch artifacts pending pre-dispatch gates |
| Diff evidence | dispatch diff plus AAF helper, dispatch-quality, and pre-dispatch autorun receipts |
| Approval boundary | dispatch authoring only; worker implementation remains no-commit; the work-order reviewer reviews this work order before execution |
| Claim boundary | documentation-only addendum dispatch; no runtime, provider, checker, helper, or public behavior |
| Agent type | dispatcher |
| Invocation ID | `rse-t2-worker-return-jurisdiction-block-dispatch-2026-06-22` |
| Expected manifest | this baseline; paired RSE-T2 work order |
| Actual changed set | this baseline and paired RSE-T2 work order |
| Manifest delta | MATCH |

## Acceptance Criteria

| ID | Criterion |
|---|---|
| AC1 | The addendum defines the `## Worker Return Jurisdiction Block` with the candidate fields from the roadmap T2 section or a source-verified equivalent. |
| AC2 | Finding capture and promotion routing are separate fields in the block. |
| AC3 | The addendum states operator action is required only when an RSE-T1 `ASK_OPERATOR` class is present. |
| AC4 | The addendum states no worker is granted authority to edit out-of-scope lane memory or checkers. |
| AC5 | The addendum records a placement recommendation for the block and defers machine enforcement to RSE-T3, and states it is documentation only and builds on the closed RSE-T0 standard and RSE-T1 addendum. |
| AC6 | Worker return records actual base, status, changed set, source inventory, gates, and claim boundary, and the worker commits nothing. |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this artifact | `Status: DISPATCHED_TO_WORKER` until reviewer closure | PENDING_REVIEW |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_FOR_WORKER_2026-06-22.md` | `Status: DISPATCHED_TO_WORKER` until reviewer closure | PENDING_REVIEW |
| Worker return | `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_WORKER_RETURN_2026-06-22.md` | worker returns `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` | PENDING_WORKER |
| Completion or reviewer artifact | `docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_COMPLETION_2026-06-22.md` | reviewer/closer creates only if accepted | PENDING_REVIEW |
| Runtime/provider/live evidence | N/A | no runtime/provider/live behavior authorized | N/A with reason |
| Public-sync evidence | N/A | no public-sync authorized | N/A with reason |
| Session continuity | active session front-door/state/handoff | session-sync follows accepted dispatch/closure commit if needed | PENDING_SESSION_SYNC |

## Claim Boundary

RSE-T2 authorizes only a bounded documentation-only Worker Return Jurisdiction
Block addendum built on the closed RSE-T0 standard and RSE-T1 addendum plus a
worker return. It does not authorize any checker, helper, or AAF diagnostic
implementation, any edit to the work-order template enforcement code or any
existing governed artifact, any change to AHB-T2 or AHB-T3 semantics, any RSE-T3
content, runtime behavior, provider/live behavior, CLI/MCP adapter behavior,
public-sync, session-sync by the worker, direct interception, readiness claims,
speed/cost claims, or universal governed-coding control.
