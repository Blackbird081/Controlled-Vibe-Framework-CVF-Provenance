# CVF AAF Worker Experience Findings And T5 Proposal Codex Rebuttal

Memory class: FULL_RECORD

Status: RETURN_TO_WORKER_FOR_REBUTTAL

docType: review_context

Date: 2026-06-20

From: Codex reviewer/closer role

To: worker role for critique before any GC-018/work order

External absorption review: REQUIRED

EPISTEMIC_PROCESS_NA_WITH_REASON: rebuttal and roadmap classification packet -
it evaluates a returned advisory finding packet and makes no closure, runtime,
provider, public-sync, or readiness claim.

## Purpose

Review
`docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_FOR_CODEX_2026-06-20.md`
and decide whether the operator finding is a real CVF governance blind spot:
CVF absorbs agent errors into governance learning, but does not proactively
capture worker first-hand execution friction when the worker still passes gates.

This packet is a rebuttal and classification draft only. It does not dispatch
AAF-T5, edit checkers, change the worker-return packet shape, or mutate session
state.

## Executive Position

ACCEPT the core finding.

The blind spot is real and distinct from the AAF-T5 read-receipt proposal.
Current CVF learning mechanisms are strong when a defect is caught by a guard
or closure review. They are weaker when a worker completes successfully but
encounters avoidable friction, ambiguity, late surprise, or repeated manual
search. That signal is high value because it identifies the next preventable
failure before it becomes a hard error for a future worker or noncoder operator.

However, REVISE the implementation direction. Do not make AAF-T5 only a Guard
Orientation Read-Receipt Gate. The worker-experience finding is broader and
more foundational. A read receipt is one downstream control. Worker experience
capture is the intake channel that should decide which controls deserve to be
promoted.

## Main Rebuttal

### 1. The Proposal Correctly Identifies A New Learning Lane

CVF already has `Finding-To-Governance Learning Disposition`, but that section
is mostly activated by explicit findings, defects, gate failures, or reviewer
repairs. It does not reliably ask a successful worker:

- what was slow;
- what was ambiguous;
- what trap almost fired;
- what helper/checker/index update would have prevented the friction;
- what should be promoted to a rule, standard, helper diagnostic, or phase gate.

That missing signal is not just comfort feedback. It is governance telemetry
from the actual actor executing the process.

### 2. A Purely Optional Retrospective Is Too Weak

The returned packet proposes an optional, lightweight Worker Experience
Retrospective block. Optional is useful as a starter, but it does not close the
blind spot. If the block can be omitted without an explicit reason, future
workers will omit it exactly when tired, rushed, or uncertain.

Recommended revision:

- Require a worker-experience token for `WORKER_MUST_NOT_COMMIT` worker-return
  packets.
- Permit an explicit no-friction escape hatch.
- Keep the payload short and enum-driven.

Suggested token shape:

```text
WORKER_EXPERIENCE_RETRO:
frictionLevel: NONE|LOW|MEDIUM|HIGH|BLOCKING
frictionType: GATE_SURPRISE|SCOPE_AMBIGUITY|SOURCE_DISCOVERY|WORKTREE_CONTAMINATION|HELPER_GAP|LATENCY|OTHER
observedStep: short text
preventiveControlCandidate: NONE|INDEX_UPDATE|HELPER_DIAGNOSTIC|CHECKER|WORK_ORDER_TEMPLATE|STANDARD_UPDATE|DEFER
```

Allowed no-friction form:

```text
WORKER_EXPERIENCE_RETRO_NA_WITH_REASON: no notable friction beyond normal gates
```

This keeps the burden small while making the absence of signal explicit.

### 3. Do Not Overload AAF-T5 With Read Receipt And Experience Capture

The read-receipt gate and worker-experience capture solve different problems:

| Problem | Control |
|---|---|
| Worker may not read the guard orientation index before authoring | Guard Orientation Read-Receipt Gate |
| Worker may pass but still experience avoidable friction | Worker Experience Retrospective Capture |

If both are shipped in one tranche, the scope will blur:

- one control checks pre-authoring orientation;
- one control captures post-execution learning;
- one wants strict validation;
- one needs short advisory classification.

Recommended tranche split:

| Tranche | Recommended focus | Disposition |
|---|---|---|
| AAF-T5 | Worker Experience Retrospective Capture Foundation | DO_NOW if operator approves |
| AAF-T6 | Guard Orientation Read-Receipt Gate | NEXT_AFTER_T5 |
| AAF-T7 | Helper/index drift hardening from U-findings | DEFER_UNTIL_T5_T6_CLOSE |

### 4. The Worker Experience Block Must Not Become Ritual Prose

The risk is that CVF adds another large mandatory section and increases the
very friction it is trying to reduce.

Mitigation:

- use fixed tokens and enums;
- limit free text to one short `observedStep`;
- do not require long narrative;
- collect signal first, promote only recurring or high-value items later;
- make helper output summarize the retrospective classification.

The goal is not "more paperwork". The goal is a small, machine-visible sensor
for worker friction.

### 5. The Returned U/F Findings Are Mostly Valid But Should Be Routed

| ID | Codex disposition | Reason |
|---|---|---|
| U3 | ACCEPT_AS_AAF_T7_HELPER_CANDIDATE | A clean-status false claim can be caught earlier by helper diagnostics, but should be implemented with fixtures and current checker evidence. |
| U2 | ACCEPT_AS_INDEX_QUALITY_UPDATE | Mapping task-class failures to catching checkers would reduce search time. Best paired with read-receipt/index work. |
| U4 | ACCEPT_AS_SMALL_DRIFT_TEST_CANDIDATE | Helper mode vocabulary appears narrower than commit steward mode vocabulary; confirm whether `push` exclusion is intentional before changing code. |
| U1 | ACCEPT_AS_AAF_T6_RULE_CANDIDATE | New worker task classes should update the guard orientation index in the same governed batch. |
| F1 | ACCEPT | A receipt must cite a real task class, not only exist. |
| F2 | ACCEPT | Fixed machine tokens are better than free-text headings. |
| F3 | ACCEPT_WITH_SCOPE_REFINEMENT | Eligibility must be narrow and avoid forcing reviewer/session-sync/reference-only files to carry worker receipts. |
| F4 | ACCEPT | Stable task-class keys are safer than line numbers. |
| F5 | ACCEPT_CRITICAL | Worktree-mode contamination is real; gate must bind to the self-declared worker-return artifact, not every changed file. |
| F6 | ACCEPT | Missing receipt should fail in helper before reviewer-fast when possible. |
| F7 | ACCEPT_WITH_CLAIM_BOUNDARY | A receipt proves artifact-level declaration, not comprehension. State this limit explicitly. |

## Proposed Revised Roadmap

### AAF-T5 - Worker Experience Retrospective Capture Foundation

Goal: create a lightweight, machine-visible worker-experience capture channel
for `WORKER_MUST_NOT_COMMIT` returns.

Recommended deliverables:

- reference standard defining `WORKER_EXPERIENCE_RETRO` and
  `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON`;
- update worker-return packet shape contract for future work orders;
- helper diagnostic for missing/malformed retrospective token on eligible
  worker-return packets;
- focused tests for token presence, NA reason, enum validation, and non-worker
  exemption;
- completion review classifying the operator finding as governance learning.

Claim boundary:

- no runtime behavior;
- no provider/live proof;
- no public-sync;
- no automatic quality scoring;
- no claim that worker friction is fully measured;
- no universal governed-coding-control claim.

### AAF-T6 - Guard Orientation Read-Receipt Gate

Goal: make guard orientation read receipts mandatory for eligible worker-return
packets.

Recommended deliverables:

- fixed `GUARD_ORIENTATION_READ_RECEIPT:` token;
- fixed `GUARD_ORIENTATION_NA_WITH_REASON:` token;
- checker/helper logic validating task-class key against
  `docs/reference/guard_orientation/README.md`;
- at least one named failure-to-avoid or guard row reference from the selected
  task class;
- contamination-safe eligibility based on the self-declared worker-return
  artifact;
- focused tests for valid receipt, missing receipt, invalid task class,
  reference-only exemption, reviewer completion exemption, and multi-batch
  worktree contamination.

### AAF-T7 - Helper And Index Friction Hardening

Goal: absorb the concrete U-findings after the new experience channel and read
receipt gate are stable.

Candidate items:

- U3 helper diagnostic for clean-status false claims;
- U2 task-class failure to checker mapping in the Guard Orientation Index;
- U4 helper/steward mode vocabulary drift test or documented exclusion;
- U1 rule that new worker task classes update the Guard Orientation Index.

## Required Absorption Table

| External item ID | External claim summary | Source basis | CVF verification surface | CVF disposition | Owner artifact | Next action | Claim boundary |
|---|---|---|---|---|---|---|---|
| WE-1 | CVF lacks proactive worker-experience learning capture when workers pass gates | worker returned advisory output plus current worker-return/learning artifacts | `docs/reviews/CVF_AAF_WORKER_EXPERIENCE_FINDINGS_AND_T5_PROPOSAL_FOR_CODEX_2026-06-20.md`; AAF-T1 through AAF-T4 completion packets; `governance/compat/check_finding_to_governance_learning.py` | GOVERNANCE_LEARNING_REQUIRED | proposed AAF-T5 GC-018/work order | Accept as next foundation candidate pending operator approval | advisory classification only; no checker or runtime change |
| WE-2 | Guard Orientation Read Receipt should not be the whole AAF-T5 | inference from scope separation and AAF-T4 closure finding | AAF-T4 worker return and completion review | GOVERNED_FINDING_CANDIDATE | proposed AAF-T5/T6 roadmap | Split worker-experience capture from read-receipt gate | does not dispatch either tranche |
| WE-3 | Worktree contamination can false-fire broad worker-return checks | worker returned advisory output | worker-return fast gate behavior and AOT local-view design constraints | GOVERNED_FINDING_CANDIDATE | AAF-T6 checker design | Require self-declared worker-return targeting | no current checker change |
| WE-4 | Helper/steward mode vocabulary may drift | source-backed helper/steward comparison | `governance/compat/run_agent_automation_assist.py`; `governance/compat/run_agent_commit_steward_preflight.py` | GOVERNED_FINDING_CANDIDATE | AAF-T7 helper/index hardening | Verify whether `push` exclusion is intentional before implementation | no helper change in this packet |

## Epistemic Process Block

### Expected Result / Prediction

Prediction: first-hand worker-experience capture will expose high-value
governance friction that ordinary pass/fail gates do not record.

### Evidence Comparison

The returned advisory packet contains concrete examples from AAF-T1, CGE-T1,
and AAF-T4. Current CVF artifacts contain finding-to-governance learning
sections, but those sections are usually tied to defects, guard failures, or
reviewer repairs, not successful-worker friction.

### Contradiction Or Gap Disposition

No contradiction with existing learning philosophy was found. The gap is an
intake gap: CVF needs a small channel for worker friction before deciding
whether to promote the signal to standard, helper, checker, or phase gate.

### Claim Update

Updated belief: AAF-T5 should prioritize worker-experience retrospective
capture. Guard-orientation read receipts remain valuable but should become a
separate AAF-T6 gate or a clearly separated T5B only if the operator insists on
one tranche.

## Risk / Corrective Action

Risk: adding a mandatory retrospective block can increase ritual paperwork.

Corrective action: use fixed tokens, enum values, short text, and an explicit
NA-with-reason escape hatch. Enforce presence and shape, not long narrative.

Risk: worker-experience claims can become subjective complaints.

Corrective action: route them through Finding-To-Governance Learning
Disposition. Only recurring, source-backed, or high-value items become
standards/checkers. Everything else stays advisory or is rejected with reason.

## Return Questions For Worker Rebuttal

1. Should AAF-T5 be renamed to Worker Experience Retrospective Capture
   Foundation, leaving read receipt for AAF-T6?
2. Is the proposed enum set sufficient, or does it miss a friction class seen
   during AAF-T1/CGE-T1/AAF-T4?
3. Should `WORKER_EXPERIENCE_RETRO_NA_WITH_REASON` be accepted for every
   eligible worker-return, or only when the worker also confirms no helper/gate
   surprise occurred?
4. For U4, is `push` intentionally excluded from AAF helper mode, or is it
   silent drift that should be tested?
5. For F5, what is the minimal reliable marker for "this is the self-declared
   worker-return artifact" without scanning unrelated changed files?

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance advisory rebuttal for worker critique. No
public-sync remote, public commit, public artifact path, or public claim is
authorized.

## Claim Boundary

This packet is a rebuttal and classification draft only. It does not dispatch
AAF-T5, create a GC-018, edit runtime/source/checkers, alter helper behavior,
open provider/live proof, perform public-sync, or claim readiness, cost
optimization, universal speed, or universal governed-coding control.

## Target / Source

Target: the initial worker-experience proposal and the AAF-T5/T6/T7 split.

Source: advisory proposal, current AAF helper behavior, local governance
learning rules, and reviewer classification.

## Scope / Target / Owner Boundary

Scope: rebuttal and classification input only.

Owner boundary: Codex owns this rebuttal; implementation requires a fresh
GC-018 and work order. This packet does not edit closed artifacts or implement
code.

## Scope / Methodology

Methodology: compare the proposal with CVF learning-loop gaps, worker-return
packet shape, helper latency, and tranche boundaries.

## Findings / Position

Position: AAF-T5 should become worker-experience capture first; read receipt
belongs in AAF-T6; helper/index drift belongs in AAF-T7.

## Finding-To-Governance Learning Disposition

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - this rebuttal changes
classification only and does not change runtime, provider, live, cost,
token-budget, or public-sync behavior.

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Worker pass can hide useful friction | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | AAF-T5 dispatch should create capture checker | handled by classification |
| Read receipt and experience capture are separate controls | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | split AAF-T5/T6 | handled by classification |
| Helper/index drift exists but should not be mixed into T5 | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | defer to AAF-T7 | deferred |
| Runtime/provider/cost applicability | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost behavior changed or claimed | handled |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | rebuttal/classification input only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | local advisory text only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | worker-experience tranche split only |
| forbiddenExpansion | runtime/provider/live/public-sync/direct interception, queue/daemon, readiness, and universal control remain parked |

## Agent Operation Trace Block

| Field | Value |
|---|---|
| Actor | Codex reviewer role |
| Provider or surface | local workspace |
| Session or invocation | Codex advisory rebuttal |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | local review and file authoring |
| Target paths | this rebuttal packet |
| Allowed scope source | operator request for Codex rebuttal |
| Before status evidence | advisory proposal existed uncommitted |
| After status evidence | rebuttal response left uncommitted for classification |
| Diff evidence | checked by later dispatch gates |
| Approval boundary | advisory only; no implementation |
| Claim boundary | no runtime/provider/live/public-sync/direct-interception claim |
| Agent type | reviewer |
| Invocation ID | local-session-2026-06-20-aaf-worker-experience-rebuttal |
| Expected manifest | this rebuttal packet |
| Actual changed set | this rebuttal packet plus later dispatch normalization |
| Manifest delta | later Codex dispatch normalization added structural gate sections |
