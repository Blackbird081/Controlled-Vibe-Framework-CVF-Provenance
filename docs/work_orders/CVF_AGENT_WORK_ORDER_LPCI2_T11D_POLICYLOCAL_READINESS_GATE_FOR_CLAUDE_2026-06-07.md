# CVF Agent Work Order - LPCI2-T11D PolicyLocal Readiness Gate

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

Template: `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
(post-`fce62cd3` version with Worker Pending-Return Gate section 6D)

Commit mode: `WORKER_MUST_NOT_COMMIT`

dispatchBaseHead: `fce62cd3`
executionBaseHead: `37f2a356`
closureBaseHead: `37f2a356`

Status token rule:

- `HOLD_*`, `DRAFT`, or `PROPOSED` statuses must not include the token
  `CLOSED`; use `PASS` or `SATISFIED` for prerequisite wording.

---

## Purpose

Aggregate the T11A candidate inventory, T11B source verification, and T11C
classification evidence into a single corpus-expansion readiness gate review.
The review must carry forward the T11C boundary: zero `t12Eligible=YES`
candidates. The expected verdict is `READY_WITH_CONDITIONS` because all 6
corpus candidates are `t12Eligible=CONDITIONAL` and blocked by EC-02 plus
unknown `currentStatus` and `jurisdiction` metadata. Success means: the
readiness gate review exists with a valid verdict, correct candidate summary
counts, a populated condition list, and an explicit next-allowed-move
statement that names T12 authoring as forbidden while conditions remain
unresolved. The worker returns all artifacts uncommitted for Codex review.

---

## 2. Authority Chain

- Operator instruction: 2026-06-07 - proceed to T11D Readiness Gate; cite
  the updated template with Worker Pending-Return Gate; carry T11A/B/C
  evidence forward; preserve zero `t12Eligible=YES` boundary; block T12 until
  EC-02 and status/jurisdiction metadata are satisfied.
- T11C predecessor closure:
  `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md`
  (`Status: CLOSED_PASS_BOUNDED`)
- Active handoff: `AGENT_HANDOFF_V16_2026-06-06.md` Next Allowed Move section
- GC-018: `docs/baselines/CVF_GC018_LPCI2_T11D_POLICYLOCAL_READINESS_GATE_2026-06-07.md`
- Roadmap: `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md`
  (T11-D sub-tranche, lines 265-302)
- Template hardening: `docs/reviews/CVF_WORKER_PENDING_RETURN_GATE_TEMPLATE_HARDENING_COMPLETION_2026-06-07.md`

Authority boundary:

- This work order does not authorize work outside the cited authority chain.
- If any authority artifact conflicts with this work order, stop and
  reconcile before implementation.

---

## 3. Agent Roles

- Orchestrator / dispatcher: Codex under operator direct request
- Implementer: Claude (WORKER_MUST_NOT_COMMIT)
- Reviewer / committer: Codex
- Operator approval required for: any action that would exceed Allowed scope;
  any attempt to promote a candidate to `t12Eligible=YES`; EC-02 current-law
  review initiation; T12 work order authoring; public-sync; live/provider
  proof; or any destructive or irreversible action.

---

## Write Ownership

Worker (Claude) owns authoring of both output artifacts as `WORKER_MUST_NOT_COMMIT`:

- `docs/reviews/CVF_LPCI2_T11_CORPUS_EXPANSION_READINESS_GATE_2026-06-07.md`
- `docs/reviews/CVF_LPCI2_T11D_READINESS_GATE_WORKER_RETURN_2026-06-07.md`

Reviewer (Codex) owns: review, structural remediation, commit, and session-sync
update. Operator owns: EC-02 review initiation, metadata resolution
authorization, and T12 authoring authorization.

## Evidence Requirements

The worker must confirm each of the following evidence artifacts is readable
and in the expected closed/reviewed status before authoring output artifacts:

| Artifact | Required status |
|---|---|
| `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | `REVIEWED_PASS_BOUNDED` |
| `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md` | `CLOSED_PASS_BOUNDED` |
| `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md` | `CLOSED_PASS_BOUNDED` |
| `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md` | `REVIEWED_PASS_BOUNDED` |
| T11C candidate manifest hash | `sha256:023f1276092756232949662e9be6e635d545ab22b2bd19284f11f82789c7fd1a` |

---

## Scope / Target / Owner Boundary

Allowed scope:

- Reading T11A/B/C completion and evidence artifacts listed in Section 5.
- Reading the T11C candidate manifest at the external workspace path.
- Authoring `docs/reviews/CVF_LPCI2_T11_CORPUS_EXPANSION_READINESS_GATE_2026-06-07.md`
  (new, readiness gate review).
- Authoring `docs/reviews/CVF_LPCI2_T11D_READINESS_GATE_WORKER_RETURN_2026-06-07.md`
  (new, worker return packet).
- Running `git rev-parse`, `git status`, `git diff --name-status` and all
  listed governance gates.
- Running markdown structural, finding-to-governance, machine closure package,
  and dispatch quality checks as working-tree-aware pending-artifact
  validation.
- Documentation format remediation inside Allowed scope.
- Reviewer-owned closure updates to this work order, the T11D GC-018, the T11
  roadmap, the T11D readiness review, the T11D worker return, and session
  continuity files:
  `docs/baselines/CVF_GC018_LPCI2_T11D_POLICYLOCAL_READINESS_GATE_2026-06-07.md`,
  `docs/reviews/CVF_LPCI2_T11D_READINESS_GATE_COMPLETION_2026-06-07.md`,
  `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md`,
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, and
  `AGENT_HANDOFF_V16_2026-06-06.md`.
- Reviewer-owned bounded material closure commit and session-sync commit after
  committed-range governance gates pass.

Forbidden scope:

- Corpus ingestion of any candidate document.
- Body extraction, text parsing, OCR, PDF or DOCX body reading.
- Chunking or indexing.
- Runtime search query execution against any document.
- Provider calls of any kind.
- Vector or embedding retrieval.
- Promoting any candidate from `t12Eligible=CONDITIONAL` to `t12Eligible=YES`.
- Authoring or authorizing a T12 work order.
- Mutation of existing T9/T10/T11A/T11B/T11C generated artifacts (corpus
  records, chunks, receipts, scripts, readiness reports, or the T11C
  candidate manifest).
- Public-sync, public push, or public catalog claim.
- Current-law or latest-law claim.
- Legal advice quality claim.
- Production, hosted, or public readiness claim.
- EC-02 current-law transition before 2026-07-01.
- Any worker-side commit or push.

Risk ceiling: R1

---

## 5. Required First Reads

Before filing GC-018 or editing files, read:

- `CVF_SESSION_MEMORY.md` - startup front door, current mode
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` - active mode, next allowed move
- `AGENT_HANDOFF_V16_2026-06-06.md` - T11C closure and T11D next move
- `docs/baselines/CVF_GC018_LPCI2_T11D_POLICYLOCAL_READINESS_GATE_2026-06-07.md` - T11D
  authorization and T12 gate hard invariant
- `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md`
  (T11-D section) - deliverables, scope boundary, acceptance criteria
- `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md`
  - T11C result and boundary to carry forward
- `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md`
  - per-candidate classification rows (answerClass, ec02Gate, t12Eligible)
- `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md`
  - T11B result and Unicode path-fidelity finding
- `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md`
  - T11A candidate inventory (total counts)
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
  (post-`fce62cd3`) - Worker Pending-Return Gate section 6D

---

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base fce62cd3 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base fce62cd3 --head HEAD
python governance/compat/check_work_order_dispatch_quality.py --base fce62cd3 --head HEAD --enforce
```

Expected results:

- `git rev-parse --short HEAD` returns a hash at or after `fce62cd3`.
- `git status --short` is clean before worker edits.
- `pre-dispatch` and `pre-implementation` autorun gates PASS.
- dispatch quality PASS.

If a pre-flight check fails, stop and record the failed command and result.
The worker must not continue past a failed autorun phase gate.

Mandatory Gate-Failure Remediation Protocol:

- Allowed-scope failures are mandatory remediation. Complete the remediation
  and execute the failed gate again.
- Missing `N/A with reason`, stale closure residue, source-verification
  corrections, and routine guard failures are not operator-preference
  questions.
- Escalation is reserved for remediation that would exceed Allowed scope,
  change the claim boundary, release a `HOLD_*` prerequisite, change risk
  level, open public-sync, run live/provider proof, consume secrets/quota,
  touch forbidden paths, or perform destructive/irreversible actions.

---

## 6A. Source-Fidelity Pass

Existing paths verified before dispatch:

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| T11C predecessor closure status (EXISTS) | `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md` | `Status: CLOSED_PASS_BOUNDED` | `Status` | T11C completion record | ACCEPT |
| T11C completion path (EXISTS) | `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md` | file presence | `CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md` | T11C completion record | ACCEPT |
| T11C classification report path (EXISTS) | `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md` | file presence | `CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md` | T11C classification reference | ACCEPT |
| T11C GC-018 path (EXISTS) | `docs/baselines/CVF_GC018_LPCI2_T11C_POLICYLOCAL_CLASSIFICATION_PRE_CHECK_2026-06-07.md` | file presence | `CVF_GC018_LPCI2_T11C_POLICYLOCAL_CLASSIFICATION_PRE_CHECK_2026-06-07.md` | GC-018 record | ACCEPT |
| T11B source verification completion (EXISTS) | `docs/reviews/CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md` | file presence | `CVF_LPCI2_T11B_SOURCE_VERIFICATION_COMPLETION_2026-06-07.md` | T11B completion record | ACCEPT |
| T11A inventory path (EXISTS) | `docs/reference/CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | file presence | `CVF_LPCI2_T11_CANDIDATE_INVENTORY_2026-06-07.md` | T11A inventory reference | ACCEPT |
| T11 roadmap T11-D section (EXISTS) | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | lines 265-302 | T11-D deliverables, scope, acceptance criteria | T11 roadmap | ACCEPT |
| Worker Pending-Return Gate (EXISTS) | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | section 6D post `fce62cd3` | `Worker Pending-Return Gate` section | CVF work-order template | ACCEPT |
| Template hardening completion (EXISTS) | `docs/reviews/CVF_WORKER_PENDING_RETURN_GATE_TEMPLATE_HARDENING_COMPLETION_2026-06-07.md` | file presence | `CVF_WORKER_PENDING_RETURN_GATE_TEMPLATE_HARDENING_COMPLETION_2026-06-07.md` | template hardening record | ACCEPT |
| External candidate manifest hash (VALUE_SET) | `docs/baselines/CVF_GC018_LPCI2_T11C_POLICYLOCAL_CLASSIFICATION_PRE_CHECK_2026-06-07.md`; `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md` | `sha256:023f1276092756232949662e9be6e635d545ab22b2bd19284f11f82789c7fd1a` | T11C candidate manifest hash | T11C closure | ACCEPT |
| `t12Eligible=CONDITIONAL` count = 6 (LITERAL_INVARIANT) | `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md`; `docs/reference/CVF_LPCI2_T11_CLASSIFICATION_PRE_CHECK_2026-06-07.md` | all 6 corpus candidates carry `t12Eligible=CONDITIONAL` | `t12Eligible` | T11C classification | ACCEPT |
| `t12Eligible=YES` count = 0 (LITERAL_INVARIANT) | `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md` | zero candidates carry `t12Eligible=YES` | `t12Eligible` | T11C classification | ACCEPT |
| EC-02 blocked count = 6 (LITERAL_INVARIANT) | `docs/reviews/CVF_LPCI2_T11C_CLASSIFICATION_PRE_CHECK_COMPLETION_2026-06-07.md` | all 6 carry `ec02Gate=BLOCKED_UNTIL_2026-07-01` | `ec02Gate` | T11C classification | ACCEPT |

New doc-only fields introduced by T11D:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
|---|---|---|---|---|
| `readinessVerdict` | T11D top-level corpus-expansion verdict | Yes | Yes | One of `READY`, `READY_WITH_CONDITIONS`, `NOT_READY`; doc/markdown validation only |
| `conditionList` | Named conditions for `READY_WITH_CONDITIONS` | Yes | Yes | Must name EC-02 date gate and unknown status/jurisdiction metadata; doc validation only |

---

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Produce readiness gate review with candidate summary table | Section 7 step 4a | `docs/reviews/CVF_LPCI2_T11_CORPUS_EXPANSION_READINESS_GATE_2026-06-07.md` candidate summary table | markdown structural check | PASS after delivery |
| Produce EC-02 gate summary | Section 7 step 4b | EC-02 gate summary block in readiness gate review | count verified against T11C | PASS after delivery |
| Produce overall readiness verdict | Section 7 step 4c | `readinessVerdict` field in review | one of three allowed values | PASS after delivery |
| Condition list if `READY_WITH_CONDITIONS` | Section 7 step 4d | `conditionList` in review | must name EC-02 date and unknown metadata | PASS after delivery |
| Next allowed move statement | Section 7 step 4e | next allowed move section in review | T12 named as forbidden while conditions unresolved | PASS after delivery |
| Candidate summary counts reconcile T11A/B/C | Section 6A source fidelity | count rows in candidate summary table | cross-check against T11A inventory and T11C report | PASS after delivery |
| No T12 authoring until conditions met | Section 4 Forbidden scope | next allowed move statement text | doc validation only | PASS after delivery |
| Worker Pending-Return Gate table | Section 6D | worker return packet section 6D gate table | component gate checks run and recorded | PASS after delivery |
| EC-02 boundary stated in work order | Section 4 Forbidden scope and Section 8 | explicit EC-02 text | doc validation only | PASS |
| Commit mode WORKER_MUST_NOT_COMMIT with anchors | Section 6D header | dispatchBaseHead, executionBaseHead, closureBaseHead | dispatch quality check | PASS |

---

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope.

Proceed autonomously with:

- reading all files named in Section 5;
- running `git status`, `git diff`, `git rev-parse`, and listed governance
  gates;
- documentation format remediation inside Allowed scope;
- required evidence block completion inside Allowed scope;
- repeated guard or autorun execution after allowed-scope remediation;
- authoring the two new review artifacts named in Allowed scope.

Escalation is reserved for: exceeding Allowed scope; editing legacy source
or runtime/source code; running live/provider proof; using secrets/quota;
public-sync or push; changing risk or claim boundary; releasing a `HOLD_*`
prerequisite; touching forbidden paths; performing destructive or irreversible
actions; or any attempt to promote a candidate to `t12Eligible=YES`.

If a machine gate fails inside Allowed scope, complete the remediation and
execute the gate again. Routine gate remediation is not an operator-preference
checkpoint.

### 6C.1 System Loop Interlock Routing

- Upstream loop: T11C classification pre-check output (classification report,
  updated candidate manifest).
- Downstream loop: T12 corpus ingestion work order (gated; not yet
  authorized).
- Machine-readable registry: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  `currentMode` transition from T11C closed to T11D closed after reviewer
  commits.
- Routing rule for deferred/blocked findings: any finding that a conditional
  candidate could become eligible must be routed to the operator via an
  explicit next-allowed-move statement; no autonomous eligibility upgrade.
- Claim boundary: autonomous mutation of `t12Eligible` is blocked. Only a
  separate operator-authorized evidence path after EC-02 and metadata
  resolution may upgrade eligibility.

---

## 6D. Pending Artifact Evidence Finality

Commit mode is `WORKER_MUST_NOT_COMMIT`. The worker returns two new files
pending review:

- `docs/reviews/CVF_LPCI2_T11_CORPUS_EXPANSION_READINESS_GATE_2026-06-07.md`
- `docs/reviews/CVF_LPCI2_T11D_READINESS_GATE_WORKER_RETURN_2026-06-07.md`

The worker must record actual `git status --short` output showing these files
as pending. The worker must not claim `git status --short` is clean. The
worker must not claim `pre-closure` PASS; committed-range closure is
reviewer/committer work.

### Commit Mode And Base-Anchor Lifecycle

| Anchor | Captured by | When | Used for |
|---|---|---|---|
| `dispatchBaseHead` | Codex (orchestrator) | before dispatch | audit history; `fce62cd3` |
| `executionBaseHead` | Claude (worker) | `git rev-parse --short HEAD` before edits | pending-artifact component-gate validation |
| `closureBaseHead` | Codex (reviewer/committer) | before closure commit | non-empty committed-range `pre-closure` validation |

### Worker Pending-Return Gate

`WORKER_MUST_NOT_COMMIT` is a commit-boundary rule, not a quality-gate
waiver. Before returning, the worker must run and record:

| Gate | Applies when | Command or evidence | Required pending-return result |
|---|---|---|---|
| Execution anchor | every worker run | `git rev-parse --short HEAD` before edits | `executionBaseHead=<hash>` |
| Pending worktree | every `WORKER_MUST_NOT_COMMIT` return | `git status --short` | actual pending file list showing both new review files |
| Markdown structural completeness | changed governed markdown (new review files) | `python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce` | `PASS`, or pending-return exception with explicit reason |
| Finding-To-Governance learning | any changed artifact records findings, defects, or known issues | `python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce` | `PASS`, or pending-return exception with explicit reason |
| Machine Closure Package | readiness gate review uses closed-equivalent or downstream-loop language | `python governance/compat/check_machine_closure_package.py --base <executionBaseHead> --head HEAD --enforce` | `PASS`, `N/A with reason`, or pending-return exception with explicit reason |
| Dispatch quality | this work order is a changed ready/dispatch packet | `python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce` | `PASS`, or `BLOCKED` with return action |

If a component gate reports only expected pending-return residue from
uncommitted artifacts, record the pending-return exception and the exact
reason. Do not record that result as closure PASS.

The startup acknowledgment in the worker return must mirror the active session
state and active handoff. `parked checkpoint=none` is valid only when those
front doors record no parked checkpoint.

---

## 6E. Self-Reported Gate Evidence Consistency

Before returning:

- if a required gate fails inside Allowed scope, repair and rerun;
- if the failure cannot be repaired inside Allowed scope, set status to
  `BLOCKED` and name the return action;
- do not leave a non-blocked artifact saying a required gate failed while
  asking the reviewer to rerun;
- after rerunning a gate, update the recorded result before returning.

---

## 6E.1 Machine Closure Package

The worker return packet must include the following Machine Closure Package
table. The reviewer/committer will verify and finalize it after commit.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED`; `executionBaseHead=37f2a356`; `closureBaseHead=37f2a356` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_T11D_READINESS_GATE_WORKER_RETURN_2026-06-07.md` | worker return packet reviewed by Codex; committed-range gates required before final closure claim | PASS |
| Readiness gate review | `docs/reviews/CVF_LPCI2_T11_CORPUS_EXPANSION_READINESS_GATE_2026-06-07.md` | verdict, candidate counts, EC-02 summary, condition list, next allowed move | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_T11_POLICYLOCAL_CORPUS_EXPANSION_READINESS_ROADMAP_2026-06-07.md` | T11D row updated to closed; T12 remains not authorized | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session sync updated by reviewer/committer after material closure | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V16_2026-06-06.md` | session sync updated by reviewer/committer after material closure | PASS |
| External evidence digest | T11C candidate manifest hash `sha256:023f1276092756232949662e9be6e635d545ab22b2bd19284f11f82789c7fd1a` carried forward from T11C completion | no new external artifact generated; T11C manifest hash is the evidence anchor | PASS |
| System loop interlock | no system-loop mutation authorized | T11D is aggregation only; no runtime loop changed; downstream T12 loop remains gated | PASS |
| Session continuity | `CVF_SESSION_MEMORY.md` and `AGENT_HANDOFF_V16_2026-06-06.md` | session sync updated by reviewer/committer after material closure | PASS |

---

## 7. Execution Plan

1. Run pre-flight checks (Section 6). Record `executionBaseHead`.
2. Read all files listed in Section 5.
3. Reconcile candidate counts from T11A inventory, T11B verification, and
   T11C classification report. Confirm:
   - 6 corpus candidates (T11A-CAND-001 through T11A-CAND-006)
   - 1 non-corpus record (BNDL-006)
   - 0 `t12Eligible=YES`
   - 6 `t12Eligible=CONDITIONAL`
   - 1 `t12Eligible=NO`
   - 6 `ec02Gate=BLOCKED_UNTIL_2026-07-01`
4. Author readiness gate review
   (`docs/reviews/CVF_LPCI2_T11_CORPUS_EXPANSION_READINESS_GATE_2026-06-07.md`):
   a. Candidate summary table (counts by `t12Eligible` verdict).
   b. EC-02 gate summary (count of `BLOCKED_UNTIL_2026-07-01` candidates).
   c. Overall readiness verdict (expected `READY_WITH_CONDITIONS`).
   d. Condition list naming both required blockers:
      - EC-02 freshness review required on or after 2026-07-01;
      - `currentStatus` and `jurisdiction` metadata must be resolved from
        `unknown` to known values for each candidate before re-evaluation.
   e. Next allowed move statement stating T12 work order authoring is
      forbidden while the above conditions remain unresolved.
5. Author worker return packet
   (`docs/reviews/CVF_LPCI2_T11D_READINESS_GATE_WORKER_RETURN_2026-06-07.md`)
   with: startup acknowledgment, evidence trace, candidate counts, verdict
   rationale, Worker Pending-Return Gate table, changed-file list, claim
   boundary, and Machine Closure Package.
6. Run Worker Pending-Return Gate component checks (Section 6D). Record all
   results in the worker return packet.
7. Record `git status --short` showing both new files as pending.
8. Return both artifacts uncommitted to Codex.

---

## Review Gate

Codex must verify before committing:

- Readiness gate review reviewed for bounded closure.
- Worker return packet reviewed for bounded closure.
- Candidate counts reconcile to T11C closure: 6 corpus, 0 `t12Eligible=YES`,
  6 `t12Eligible=CONDITIONAL`, 1 `t12Eligible=NO`, 6 EC-02 blocked.
- EC-02 invariant: 0 violations confirmed.
- Worker Pending-Return Gate table present and populated.
- No forbidden scope action occurred (verified via Forbidden Scope
  Confirmation table in worker return).
- All four committed-range component gates PASS after commit.

## Closure Checklist

Requirements before Codex marks this work order `CLOSED_PASS_BOUNDED`:

- Both output artifacts committed in bounded T11D closure batch.
- Markdown structural completeness gate PASS on committed range.
- Finding-to-governance learning gate PASS on committed range.
- Worker Pending-Return Gate committed-range checks PASS.
- Session continuity updated: `CVF_SESSION/ACTIVE_SESSION_STATE.json`,
  `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V16_2026-06-06.md`.
- This work order `Status` field updated to `CLOSED_PASS_BOUNDED`.

---

## 8. EC-02 And T12 Gate Hard Boundary

**This boundary is non-negotiable and not subject to worker interpretation.**

T12 corpus ingestion work order authoring may not begin while any of the
following conditions are unresolved:

1. **EC-02 freshness gate:** no corpus candidate may be promoted to
   `t12Eligible=YES` before an EC-02 freshness review on or after 2026-07-01
   with explicit operator authorization.
2. **Unknown `currentStatus`:** all 6 corpus candidates carry
   `currentStatus=unknown`. A candidate may not become `t12Eligible=YES`
   while its `currentStatus` is unknown.
3. **Unknown `jurisdiction`:** all 6 corpus candidates carry
   `jurisdiction=unknown`. A candidate may not become `t12Eligible=YES`
   while its `jurisdiction` is unknown.

The T11D readiness gate review must state these conditions explicitly. The
next allowed move must name T12 as forbidden until conditions are resolved
through a separate operator-authorized evidence path.

No worker, agent, or automated step may bypass this boundary. Operator
escalation is required before any EC-02 transition, metadata resolution, or
eligibility upgrade.

---

## 9. Stop Conditions

Stop and return `BLOCKED` with the exact failure reason if any of the
following occur:

- Pre-flight autorun gate fails and cannot be repaired inside Allowed scope.
- The T11A/B/C evidence artifacts cannot be read or candidate counts cannot
  be reconciled.
- Any step would require body extraction, ingestion, provider call, or
  promotion of a candidate to `t12Eligible=YES`.
- A required governance gate fails and cannot be repaired inside Allowed
  scope.
- Any action would exceed the Allowed scope or the EC-02 hard boundary.

Return to orchestrator when a stop condition is triggered. Record the failing
condition, the failed command output, and the current `git status --short`
before returning.

---

## 10. Acceptance Criteria (Worker-Facing)

The worker may return artifacts when all of the following are satisfied:

1. `docs/reviews/CVF_LPCI2_T11_CORPUS_EXPANSION_READINESS_GATE_2026-06-07.md`
   exists with valid verdict, candidate summary table, EC-02 gate summary,
   condition list, and next allowed move statement.
2. `docs/reviews/CVF_LPCI2_T11D_READINESS_GATE_WORKER_RETURN_2026-06-07.md`
   exists with startup acknowledgment, evidence trace, Worker Pending-Return
   Gate table (Section 6D), changed-file list, and claim boundary.
3. Candidate summary counts match T11C: 6 corpus, 1 non-corpus, 0 YES,
   6 CONDITIONAL, 1 NO, 6 EC-02 blocked.
4. Verdict is one of the three allowed values.
5. Condition list names EC-02 date gate and unknown status/jurisdiction
   metadata.
6. Next allowed move explicitly names T12 authoring as forbidden while
   conditions remain unresolved.
7. Worker Pending-Return Gate table is present with all applicable gate
   results.
8. No forbidden scope action has occurred.
9. `executionBaseHead` is captured and recorded.
10. `git status --short` shows both new files pending; no clean-status claim.

---

## Operator Checkpoint

No operator checkpoint is required for T11D aggregation (doc-only evidence
read; no runtime, provider call, or public-sync). The worker may proceed
without an additional operator confirmation step provided all pre-flight
checks pass.

If a stop condition is triggered, escalation to the operator is required
before any resumption.

## Claim Boundary

This work order claims: authority to read T11A/B/C evidence artifacts and
author the T11D readiness gate review and worker return packet, bounded by
the cited GC-018, authority chain, and Allowed scope above.

This work order does not claim: corpus ingestion readiness, T12 authorization,
EC-02 freshness review, current-law status, production readiness, public
readiness, or any action beyond the cited Allowed scope.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Policy_Local corpus candidate evidence is in scope. No
public-sync, public push, or public catalog claim is authorized.
