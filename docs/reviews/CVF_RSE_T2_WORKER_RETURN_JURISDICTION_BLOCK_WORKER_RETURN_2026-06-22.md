# CVF RSE-T2 Worker Return Jurisdiction Block - Worker Return

Memory class: FULL_RECORD

docType: review

Status: COMPLETE_PENDING_REVIEW

Date: 2026-06-22

dispatchBaseHead: 2dd54bc5

executionBaseHead: 45247ab0

Index classification: GOVERNED_DOC (not an INDEX_ARTIFACT). This worker return
records one bounded documentation tranche; it does not map, enumerate, project,
or classify CVF state.

## Status

COMPLETE_PENDING_REVIEW. The worker created the RSE-T2 documentation-only Worker
Return Jurisdiction Block addendum inside Allowed scope and committed nothing.
Reviewer/closer owns review, gates, and any commit.

## Target / Source

| Item | Value |
|---|---|
| Work order | docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_FOR_WORKER_2026-06-22.md |
| GC-018 baseline | docs/baselines/CVF_GC018_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_2026-06-22.md |
| Roadmap | docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md (T2 section) |
| RSE-T1 addendum | docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md |
| RSE-T0 standard | docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md |

## Purpose

Create the RSE-T2 Worker Return Jurisdiction Block addendum: a documentation-only
reference defining a structured worker-return block that carries routing data, so
a reviewer or closer can act without asking the operator. It keeps finding
capture and promotion routing as separate fields, ties operator action to an
RSE-T1 ASK_OPERATOR class, forbids self-widening, and records a placement
recommendation while deferring machine enforcement to RSE-T3.

## Scope / Methodology

Allowed-scope changes only, following the RSE roadmap T2 section and the closed
RSE-T0 and RSE-T1 documents:

1. Read the work order, GC-018 baseline, RSE roadmap T2 section, the closed RSE-T1
   addendum and RSE-T0 standard, the Guard Orientation role glossary, and the
   AAF-T7B completion review.
2. Recorded actual executionBaseHead with `git rev-parse --short HEAD`.
3. Created the addendum file inside the existing
   `docs/reference/role_switch_envelope/` directory, leaving the closed RSE-T0
   and RSE-T1 files unchanged.
4. Defined the `## Worker Return Jurisdiction Block` with the eleven candidate
   fields from the roadmap T2 section, each with a one-line meaning.
5. Kept finding capture and promotion routing as separate fields and tied
   `operatorActionRequired` to an RSE-T1 ASK_OPERATOR class.
6. Stated that no worker is granted authority to edit out-of-scope lane memory or
   checkers by filling in the block.
7. Recorded a placement recommendation across the four candidate surfaces and
   deferred machine enforcement to RSE-T3.
8. Stated the documentation-only and Agent Handoff Contract local-view boundary.
9. Ran the required checks and authored this worker return without committing.

## Findings / Position

- The addendum defines the Worker Return Jurisdiction Block with all eleven
  candidate fields: findingRecorded, findingSurface, allowedScopeRepairPerformed,
  outOfScopePromotionCandidate, promotionTargetType, promotionTargetPath,
  reviewerActionRequested, operatorActionRequired, operatorActionReason,
  blockedReason, claimBoundary.
- Capture fields and promotion fields are distinct; the addendum states the
  worker does not perform promotion and routes it instead.
- `operatorActionRequired` is true only when an RSE-T1 ASK_OPERATOR class is
  present; otherwise the request goes to the reviewer or closer.
- The addendum states no worker may edit an out-of-scope promotion target by
  filling in the block.
- The addendum records a placement recommendation across the four candidate
  surfaces and defers machine enforcement to RSE-T3.
- The closed RSE-T0 standard, the closed RSE-T1 addendum, and the front door are
  unchanged.
- No checker, helper, work-order template enforcement, AHB semantics, RSE-T3
  content, runtime, provider, public-sync, or session path was touched.
- Position: deliverables satisfy the Acceptance Criteria; ready for reviewer
  review and closure conversion.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Block could be read as enforced today | Mitigated: documentation-only boundary and placement recommendation defer enforcement to RSE-T3 |
| Capture and promotion could be conflated again | Mitigated: distinct field groups and an explicit separation section |
| Worker could read the block as authorizing out-of-scope edits | Mitigated: an explicit no-self-widening section |
| Addendum could drift from RSE-T0 or RSE-T1 | Mitigated: fields and classes are cited from RSE-T0 and RSE-T1; those files are unchanged |
| Block placement could be misread as decided | Mitigated: recommendation is explicitly non-binding and routed to RSE-T3 |

## Claim Boundary

This worker return covers only the RSE-T2 documentation-only Worker Return
Jurisdiction Block addendum. It does not claim any checker, helper, or diagnostic
implementation, any edit to the Worker Return Packet Shape Contract enforcement
or the work-order template, any edit to the closed RSE-T0 standard or RSE-T1
addendum or any existing governed artifact, any change to Agent Handoff Contract
semantics, any RSE-T3 content, runtime behavior, provider or live behavior,
CLI/MCP adapter behavior, public-sync, session-sync by the worker, direct
interception, readiness, speed or cost outcomes, or universal governed-coding
control.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker role |
| Provider or surface | local workspace |
| Session or invocation | RSE-T2 worker execution, 2026-06-22 |
| Working directory | D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF |
| Command or tool surface | file reads, documentation authoring, required gates |
| Target paths | the addendum and this worker return |
| Allowed scope source | RSE-T2 work order and paired GC-018 baseline |
| Before status evidence | executionBaseHead 45247ab0; clean worktree before worker edits |
| After status evidence | one new reference file and this new worker return, uncommitted |
| Diff evidence | `git status --short` recorded below; gates recorded below |
| Approval boundary | worker created Required Deliverables only and committed nothing |
| Claim boundary | documentation-only addendum; no checker, helper, runtime, provider, or public behavior |
| Agent type | worker role |
| Invocation ID | rse-t2-worker-return-jurisdiction-block-worker-2026-06-22 |
| Expected manifest | addendum; this worker return |
| Actual changed set | docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md; this worker return |
| Manifest delta | MATCH |

## Worker Return Jurisdiction Block

This return dogfoods the block it defines.

- findingRecorded: yes
- findingSurface: this worker return, WORKER_EXPERIENCE_RETRO and Findings sections
- allowedScopeRepairPerformed: no repair needed; the addendum passed gates on the first run
- outOfScopePromotionCandidate: no
- promotionTargetType: none
- promotionTargetPath: none
- reviewerActionRequested: review and decide closure acceptance for the RSE-T2 addendum
- operatorActionRequired: no
- operatorActionReason: none
- blockedReason: none
- claimBoundary: documentation-only worker return; no out-of-scope edit performed; the block fields here are illustrative and not machine-enforced

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

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: RSE-T2 is private provenance governance-protocol work. No public-sync
repository work or public catalog claim is authorized.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | local governed role-boundary protocol route, not external authority |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | RSE-T2 Worker Return Jurisdiction Block addendum |
| Disposition | ADAPT as a CVF-owned documentation addendum with bounded scope |
| Claim boundary | operator critique remains input only until implemented and closed through this governed work order |

## Rescan Intelligence Hardening

- Original source artifact: RSE roadmap T2 section and the AAF-T7B
  operator-question confusion pattern.
- Predecessor intake artifact: the closed RSE-T0 standard, the closed RSE-T1
  addendum, the AAF-T7B completion review, and the Guard Orientation role glossary.
- Delta ledger status: `NEW_FINDING` because the roadmap T2 block fields become an
  implemented documentation addendum.
- Routing matrix status: `DO_NOW` for the T2 addendum; `DEFER` for the placement
  decision; `OUT_OF_SCOPE` for RSE-T3 diagnostics, checker/helper, work-order
  template enforcement, runtime, provider, public-sync.
- Semantic sampling status: sampled the roadmap T2 field list, the closed RSE-T1
  question classes, and the RSE-T0 envelope fields.
- Rescan intelligence verdict: COMPLETE_WITH_DELTA_ROUTING_SAMPLE

### Original-Intake Delta Ledger

| Delta category | Evidence |
|---|---|
| UNCHANGED_FROM_INTAKE | The closed RSE-T0 standard, the closed RSE-T1 addendum, and the ratified Agent Handoff Contract remain unchanged; the addendum builds on them, it does not edit them. |
| CHANGED_DISPOSITION | The roadmap T2 candidate field list becomes an implemented documentation block with meanings and a worked example. |
| NEW_FINDING | A structured Worker Return Jurisdiction Block plus a placement recommendation are recorded as a reference addendum. |
| REMOVED_OR_REJECTED | Checker/helper implementation, work-order template enforcement edits, RSE-T0 or RSE-T1 edits, AHB semantics change, and RSE-T3 content are rejected from this tranche. |

### Follow-Up Routing Matrix

| Routing lane | Disposition |
|---|---|
| DO_NOW | Create the RSE-T2 addendum with the block, its fields, the separation rule, and the placement recommendation. |
| RESOLVED_BY_DESIGN | The addendum reuses the RSE-T1 question classes and RSE-T0 envelope fields rather than redefining them. |
| DEFER | The block placement decision and machine enforcement to RSE-T3. |
| STRATEGIC_OPERATOR_DECISION | Operator decides whether to open RSE-T3 next or resume another lane after T2 closure. |
| SEPARATE_RUNTIME_TRANCHE | RSE-T3 diagnostics, any checker or helper, work-order template enforcement, runtime, provider, public-sync. |
| OUT_OF_SCOPE | Runtime role router, agent workspace, AHB semantics change, direct interception, universal governed-coding control. |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
|---|---|---|---|---|---|
| RSE-T2-WR-RS1 | roadmap T2 candidate fields | the addendum defines all eleven fields | DO_NOW | Did any field get dropped or renamed? | PASS - all eleven field names are present in the block table |
| RSE-T2-WR-RS2 | roadmap T2 acceptance criteria | capture and promotion are separate fields | DO_NOW | Are they merged anywhere? | PASS - distinct field groups plus an explicit separation section |
| RSE-T2-WR-RS3 | RSE-T1 ASK_OPERATOR class | operator action is the exception | DO_NOW | Could the block default to operator action? | PASS - operatorActionRequired is true only for an ASK_OPERATOR class |
| RSE-T2-WR-RS4 | roadmap T2 placement options | the placement is a recommendation, not a decision | DEFER | Did the addendum change a placement surface? | PASS - no surface was edited; enforcement deferred to RSE-T3 |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded implementation of one documentation-only addendum
  tranche.
- Corpus root: repo-local files named in Target / Source and the work order
  Source Verification Block.
- Snapshot time: 2026-06-22 worker execution.
- Enumeration command: filesystem-backed direct file reads of named sources plus
  `rg --files --hidden --no-ignore` for targeted confirmation.
- Manifest artifact or inline manifest: Target / Source table in this return.
- Manifest hash: N/A with reason: bounded direct-read implementation, no
  generated corpus manifest.
- Processing ledger artifact or inline ledger: Scope / Methodology steps and the
  Source Inventory And Scan-Depth Ledger below.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=Target / Source plus Source Inventory ledger; ledger_terminal=READ for cited source rows; exclusions=full-repo sweep, generated aggregate mutation, runtime/provider/web/MCP/public-sync surfaces; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: full-repo sweep, generated aggregate mutation, runtime,
  provider, web, MCP, public-sync, and live-proof surfaces.
- Unreadable or unsupported files: 0.
- Aggregation check: N/A with reason: no aggregate generated by this work.
- Drift check: N/A with reason: no generated aggregate edited by this work.
- Output traceability: each Acceptance Criterion maps to an addendum section named
  in the Findings section.
- Adversarial verification: the Semantic Sampling table distinguishes the new
  addendum from the closed RSE-T0 standard and RSE-T1 addendum it builds on.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Source Inventory And Scan-Depth Ledger

| Source | Scan depth | Terminal status |
|---|---|---|
| docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_FOR_WORKER_2026-06-22.md | full read | READ |
| docs/baselines/CVF_GC018_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_2026-06-22.md | full read | READ |
| docs/roadmaps/CVF_RSE_ROLE_SWITCH_ENVELOPE_PROTOCOL_ROADMAP_2026-06-22.md | targeted read at T2 section | READ |
| docs/reference/role_switch_envelope/CVF_RSE_T1_OPERATOR_QUESTION_BOUNDARY_ADDENDUM.md | targeted read at question classes and capture-versus-promotion | READ |
| docs/reference/role_switch_envelope/CVF_ROLE_SWITCH_ENVELOPE_STANDARD.md | targeted read at envelope fields | READ |
| docs/reference/guard_orientation/README.md | targeted read at role glossary | READ |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker returns lacked structured routing data so reviewer needs to infer jurisdiction | RULE_GAP | GOVERNANCE_CONTROL_PLANE | WRITTEN_RULE_CANDIDATE | RSE-T2 defines the Worker Return Jurisdiction Block fields | handled |
| Block placement and machine enforcement need a decision | RULE_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | RSE-T2 records a placement recommendation; RSE-T3 may enforce it | deferred |
| Operator-question boundary needs machine enforcement eventually | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | SEPARATE_TRANCHE | RSE-T3 may add diagnostics after T2 | deferred |
| Runtime, provider, or cost applicability for this work | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime, provider, or cost behavior changed or claimed | handled |

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: this is a bounded deterministic documentation
implementation following a roadmap field list, not an estimation, forecast, or
probabilistic judgment task; no epistemic confidence calibration applies.

## Machine Closure Package

| Closure item | Required artifact or path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_FOR_WORKER_2026-06-22.md | reviewer/closer converts status after acceptance | PENDING_REVIEW |
| Worker return | this artifact | worker returns COMPLETE_PENDING_REVIEW | COMPLETE_PENDING_REVIEW |
| Completion or reviewer artifact | reviewer/closer creates the RSE-T2 completion review after accepting this return | reviewer/closer owns creation | PENDING_REVIEW |
| Session continuity | active session front-door, state, and handoff | session-sync follows accepted closure commit if the next move changes | PASS |
| System loop interlock | N/A with reason: this documentation addendum introduces no system-loop interlock surface | no interlock change | N/A with reason |
| Runtime, provider, or live evidence | N/A with reason: no runtime, provider, or live behavior authorized | none | N/A with reason |
| Public-sync evidence | N/A with reason: no public-sync authorized | none | N/A with reason |

## Evidence

executionBaseHead: 45247ab0

git status --short:

```
?? docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md
?? docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_WORKER_RETURN_2026-06-22.md
```

Changed-path list:

- docs/reference/role_switch_envelope/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_ADDENDUM.md (new)
- docs/reviews/CVF_RSE_T2_WORKER_RETURN_JURISDICTION_BLOCK_WORKER_RETURN_2026-06-22.md (new)

AAF helper self-smoke: `python governance/compat/run_agent_automation_assist.py
--base 45247ab0 --head HEAD --json --enforce` returned exit 0 with no defects.

Pre-implementation autorun gate:
`python governance/compat/run_agent_autorun_workflow_gate.py --phase
pre-implementation --base 45247ab0 --head HEAD` returned COMPLIANT (exit 0).

Worker-return fast gate:
`python governance/compat/run_worker_return_fast_gate.py --pytest-target
governance/compat/test_run_agent_automation_assist.py` result recorded in the
Gate Evidence section below.

Explicit boundary statements:
- The addendum defines the Worker Return Jurisdiction Block and all eleven
  candidate fields.
- Capture and promotion are separate fields and operator action is tied to an
  RSE-T1 ASK_OPERATOR class.
- No worker is granted authority to edit out-of-scope lane memory or checkers; a
  placement recommendation defers machine enforcement to RSE-T3.
- The addendum is documentation-only, builds on the closed RSE-T0 standard and
  RSE-T1 addendum, and is an Agent Handoff Contract local view.
- No checker, helper, AAF diagnostic, work-order template enforcement, RSE-T0 or
  RSE-T1 edit, AHB semantics, RSE-T3 content, runtime, provider or live,
  public-sync, generated aggregate, or session or handoff path was edited.

## Gate Evidence

| Gate | Command | Result |
|---|---|---|
| AAF helper self-smoke | `run_agent_automation_assist.py --base 45247ab0 --head HEAD --json --enforce` | PASS (exit 0, no defects) |
| Pre-implementation autorun gate | `run_agent_autorun_workflow_gate.py --phase pre-implementation --base 45247ab0 --head HEAD` | PASS (COMPLIANT, exit 0) |
| Worker-return fast gate | `run_worker_return_fast_gate.py --pytest-target governance/compat/test_run_agent_automation_assist.py` | PASS (COMPLIANT, exit 0) |

## WORKER_EXPERIENCE_RETRO

| Field | Note |
|---|---|
| What went smoothly | the closed RSE-T0 and RSE-T1 documents gave exact field and class sources; the addendum passed pre-implementation on the first run |
| Friction | none material; the work stayed inside the bounded documentation scope |
| Reusable lesson | a tranche that defines a worker-return block can dogfood it by including the block in its own worker return, which both validates the field set and demonstrates correct routing |
| Next-time action | continue the sibling-addendum pattern for RSE-T3, citing RSE-T0, RSE-T1, and RSE-T2 as closed sources, and treat any machine-enforcement work as the explicit RSE-T3 scope |

## Review Gate Handoff

Reviewer/closer must inspect the changed set against Required Deliverables, run
reviewer-fast gates, verify no forbidden scope was touched, verify the addendum
defines the block and all eleven fields, keeps capture and promotion separate,
ties operator action to an ASK_OPERATOR class, forbids self-widening, records a
placement recommendation, verifies the documentation-only and Agent Handoff
Contract local-view boundary, verifies the closed RSE-T0 and RSE-T1 files are
unchanged, and only then convert accepted material into the RSE-T2 completion
review. The worker committed nothing.
