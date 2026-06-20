# CVF AAF Worker Experience Findings And T5 Proposal For Codex

Memory class: FULL_RECORD

Status: RETURNED_ADVISORY_FOR_CODEX_CLASSIFICATION

docType: review_context

Date: 2026-06-20

From: Claude, acting as a worker reporting first-hand execution experience

To: Codex (owner of classification, GC-018, and any resulting work order)

EPISTEMIC_PROCESS_NA_WITH_REASON: advisory finding/proposal packet - it reports
worker experience and improvement proposals; it makes no closure claim and
updates no source-of-truth state.

## Purpose

Record findings discovered while executing AAF-T1, CGE-T1, and AAF-T4 as a
worker, and propose improvements to the closed AAF T1-T3 surfaces and to the
proposed AAF-T5 read-receipt gate. Also raise one process blind-spot: agents
do not currently capture their own first-hand execution experience as governed
learning input.

This packet is advisory. Codex must classify it through
`docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`
before opening any work order, editing source, or changing session state.

## Scope / Methodology

All findings below are grounded in observed behavior during this session, not
speculation. Each cites the artifact or commit that demonstrates it. T1-T3 are
already `CLOSED_PASS_BOUNDED`; this packet does not edit them. Any accepted fix
needs a fresh GC-018 and work order, or inclusion in AAF-T5.

Evidence base:

- AAF-T1 automation assist foundation closed at `3b26e23a`.
- AAF-T2 early gap diagnostics closed at `904eb09a`.
- AAF-T3 guard orientation index closed at `45fd5468`.
- CGE-T1 triage closed at `1db59198`.
- AAF-T4 delegation envelope closed at `518d4131`.

## Findings / Position

T1-T3 are usable and broadly complete; Codex already added the mirror-vocabulary
drift tests this packet would otherwise request. The items below are remaining
improvements, ranked, plus a process blind-spot that is larger than any single
tranche.

## T1-T3 Improvement Findings

### U3 - Helper does not catch a "clean git status" false claim early (high value)

Evidence: at AAF-T4 the helper smoke
`run_agent_automation_assist.py --base f209d973 --head HEAD --json --enforce`
returned `defects: []`, yet the worker-return fast gate then failed on
`check_work_order_dispatch_quality` for recording git status as clean while the
worker-return file was untracked. The guard orientation index lists this exact
failure, but the early helper does not detect it. Result: the worker learned the
defect late instead of early.

Proposal: add a helper diagnostic that flags a worker-return claiming a clean
status while the changed set is non-empty. This closes the gap between what the
index warns about and what the early helper actually catches.

### U2 - Task Class Guard Map failures do not name the catching checker (medium)

Evidence: the index Task Class Guard Map worker row lists failures such as the
git-status-clean case but does not name which checker catches each, while the
separate Common Failure Patterns table does include a checker column. During
AAF-T4 the worker had to search the repo to find which checker fired.

Proposal: add a checker reference to each Task Class Guard Map failure, or
cross-link each to the Common Failure Patterns row, so a worker can map a
failure to its gate without searching.

### U4 - Helper mode list drifted from the commit steward (low-medium)

Evidence: the commit steward
`run_agent_commit_steward_preflight.py` supports a `push` mode (lines 200, 273,
317), but the helper `ALLOWED_MODES` omits `push`. The mirror-vocabulary drift
tests do not cover the mode list, so this drift is silent.

Proposal: add a drift test asserting the helper mode set matches the steward
mode set, or document deliberately why `push` is excluded from the helper.

### U1 - New task classes are not required to update the index (process, route to T5)

Evidence: AAF-T4 had to add a project-delegation row to the index Task Class
Guard Map because no row existed; the index did not cover that task class when
T3 closed. There is no rule binding a tranche that introduces a new task class
to update the index in the same batch.

Proposal: make this a standard rule (best placed in AAF-T5): any tranche that
introduces a new worker task class must add its index row in the same changed
set.

## AAF-T5 Read-Receipt Gate Proposal Findings

These refine the proposed Guard Orientation Read-Receipt gate so it adds real
value and resists both false-fire and empty-label gaming.

### F1 - Verify the receipt names a real task class, not just that a receipt exists

A receipt block that merely exists can be empty or wrong, the same failure shape
as a control block that is present but meaningless. The checker should confirm
the receipt cites a task class that actually appears in the index Task Class
Guard Map, plus at least one matching "common failure to avoid" the worker
commits to.

### F2 - Use a fixed machine token, not a free-text heading

Use a stable token such as `GUARD_ORIENTATION_READ_RECEIPT:` with a paired
exemption token `GUARD_ORIENTATION_NA_WITH_REASON:`, mirroring the existing
epistemic-process token style. A free-text heading both false-fires on documents
that merely mention the index and is easy to fake.

### F3 - Define when a receipt is not required

Require the receipt only when worker-execution vocabulary appears as a standalone
value, reusing the narrow eligibility logic already in
`check_agent_operation_trace.py` (`REFERENCE_WORKER_TRIGGERS`). Memory updates,
reviewer completion reviews, and pure reference edits must not be forced to carry
a receipt.

### F4 - Anchor the receipt to a stable key, not a line number

The index is a living document; AAF-T4 added a row to it. A receipt that cites a
line number or long row title will break on the next index edit. Cite the task
class name. Add a drift test so that if the index task-class set changes, the
receipt checker is flagged for update.

### F5 - Survive worktree mode and multi-batch contamination

Per CLAUDE.md lines 128-130 and AGENTS.md lines 399-401, reviewer-fast runs in
`HEAD --head HEAD` worktree mode and scans every changed file on disk, including
co-present batches from another worker. Throughout this session that forced
repeated separation of "my file" from "another batch's file". The receipt gate
must require a receipt only on the artifact the packet self-declares as its own
worker-return, not on every changed file present.

### F6 - Fail early in the helper, not only at reviewer-fast

The AAF-T2 corpus diagnostic caught a real defect at the helper smoke step
before the fast gate during AAF-T4. A missing-receipt diagnostic belongs in the
same early helper path first, then wired into the worker-return fast gate and
reviewer-fast, following the rule then machine-check then earliest-phase-gate
progression.

### F7 - Accept that a receipt proves a claim, not comprehension

A machine cannot confirm a worker actually understood the index. To raise real
value, require the receipt to quote a specific applicable item from the index
(for example one named failure-to-avoid for the chosen task class), which forces
the worker to open the index to obtain that string rather than paste an empty
token. State this limit plainly in the standard.

## Process Blind-Spot: No Worker-Experience Retrospective Capture

Position: CVF systematically absorbs agent errors into governance learning, but
has no mechanism to capture worker first-hand execution experience when no error
blocks closure. Both Claude and Codex are the real workers; their lived friction
is a high-quality, non-fabricated improvement source that is currently lost after
each tranche.

Evidence from this session: the most valuable improvements above (U3, F5, F6)
came from friction that did not by itself block closure - the worker still
passed, but only after avoidable rework. None of that experience would have been
recorded under current process; it survives only because the operator asked.

Why it matters: this is the same philosophy already in CLAUDE.md (agent error to
governance learning), extended to the case where there is friction without a hard
error. A worker who just executed a tranche knows exactly which steps were
slow, ambiguous, or trap-prone. That signal is real and repeatable across agents.

Proposed direction (for Codex to scope, not yet authorized):

- Add an optional, lightweight Worker Experience Retrospective block to the
  worker-return packet shape: what was slow, what was ambiguous, what trap fired,
  what would have prevented it. Keep it advisory and short so it does not become
  ritual.
- On rule or guard upgrades, require a one-line retrospective note from the
  worker or reviewer who exercised the new rule first, captured in the closure
  or session-sync surface.
- Route accepted retrospective items through the existing finding-to-governance
  learning lane so they become rules, machine checks, or phase gates over time.

Boundary: this is a learning-capture proposal only. It does not claim runtime
behavior, does not change any checker, and must itself avoid becoming a
heavyweight mandatory block that adds the very friction it aims to reduce.

## Risk / Corrective Action

Risk level: R1 advisory finding and proposal only.

Corrective action: Codex classifies each item, decides which belong in AAF-T5
versus a separate small tranche versus a standard update, and opens a fresh
GC-018 and work order for any code or guard change. T1-T3 remain closed and must
not be edited outside a governed batch.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | External-agent returned output to external finding absorption workflow to atomic finding classification to CVF disposition to future AAF-T5 or small tranche only if Codex accepts |
| Owner surface | AAF helper, guard orientation index, worker-return packet shape standard |
| Disposition | RETURNED_ADVISORY_FOR_CODEX_CLASSIFICATION |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py` |
| Claim boundary | advisory finding/proposal only; no runtime, checker change, public-sync, provider/live, readiness, or universal governed-coding-control claim |

## Claim Boundary

This packet records worker-experience findings and improvement proposals only.
It does not edit closed T1-T3 artifacts, change any checker, authorize
implementation, prove runtime behavior, or claim readiness or universal control.
Canonical standards, work orders, machine checkers, and current session state
still control.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker-experience findings for Codex classification.
No public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Target / Source

Target: AAF worker-experience finding and proposed follow-up routing.

Source: operator-identified latency/friction observations, current AAF helper
behavior, and source-checked local governance surfaces named in this packet.

## Finding-To-Governance Learning Disposition

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - this advisory proposes
governance-helper follow-up only and does not change runtime, provider, live,
cost, token-budget, or public-sync behavior.

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker pass can hide useful friction | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Codex classification and AAF-T5 dispatch | handled by classification |
| Helper can miss early gap diagnostics | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | PHASE_GATE_PLACEMENT_GAP | route helper hardening to AAF-T7 where applicable | deferred |
| Provider-memory-only learning is not sufficient | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | promote to CVF-governed AAF-T5 packet | handled by classification |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | advisory proposal only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | local advisory text only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | worker-experience finding proposal only |
| forbiddenExpansion | runtime/provider/live/public-sync/direct interception, queue/daemon, readiness, and universal control remain parked |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: advisory proposal only | no work order is closed by this packet | N/A with reason |
| Completion or reviewer artifact | Future AAF-T5 completion review | not part of this packet | N/A with reason |
| Roadmap state | N/A with reason: advisory proposal only | Codex classification owns routing | N/A with reason |
| Registry JSON | BLOCKED with reason: no JSON registry edit authorized for advisory proposal | no path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no Markdown registry edit authorized for advisory proposal | no path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence digest created | no path changed | N/A with reason |
| System loop interlock | N/A with reason: no system loop interlock changed | no path changed | N/A with reason |
| Session continuity | N/A with reason: advisory proposal only | no session path changed | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Advisory-only status | `RETURNED_ADVISORY_FOR_CODEX_CLASSIFICATION` | PASS |
| No implementation closure | no checker/helper/runtime change in this packet | PASS |
| Codex classification required | AAF-T5 classification packet owns final routing | PASS |

## Agent Operation Trace Block

| Field | Value |
|---|---|
| Actor | advisory proposal author role |
| Provider or surface | local advisory surface |
| Session or invocation | worker-experience proposal return |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | advisory authoring and source review |
| Target paths | this advisory proposal packet |
| Allowed scope source | operator worker-experience finding |
| Before status evidence | AAF-T4 closure had recommended a read-receipt follow-up |
| After status evidence | advisory proposal left uncommitted for Codex classification |
| Diff evidence | checked by later dispatch gates |
| Approval boundary | advisory only; no implementation |
| Claim boundary | no runtime/provider/live/public-sync/direct-interception claim |
| Agent type | advisory author |
| Invocation ID | local-session-2026-06-20-aaf-worker-experience-proposal |
| Expected manifest | this advisory proposal packet |
| Actual changed set | this advisory proposal packet plus later dispatch normalization |
| Manifest delta | later Codex dispatch normalization added structural gate sections |
