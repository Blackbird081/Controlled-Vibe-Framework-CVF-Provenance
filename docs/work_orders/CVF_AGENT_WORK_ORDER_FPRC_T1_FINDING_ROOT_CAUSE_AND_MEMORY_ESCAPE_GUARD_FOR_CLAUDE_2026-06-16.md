# CVF Agent Work Order - FPRC-T1 Finding Root Cause And Memory Escape Guard For Claude

Memory class: POINTER_RECORD

Status: DISPATCHED_TO_CLAUDE

docType: work_order

Date: 2026-06-16

Batch ID: FPRC-T1

commitMode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: aa977426

## Dispatch Prompt Envelope

Role: Claude worker.

Read first:

1. This section.
2. `docs/baselines/CVF_GC018_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_2026-06-16.md`
3. `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`
4. `governance/compat/check_finding_to_governance_learning.py`
5. `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`

Mission summary: implement FPRC-T1 before CCLV-T2 resumes. Add the governed
standard, add authoring guidance, and harden the finding-learning checker so a
reusable lesson cannot be closed only in provider-specific memory.

Do not commit. Return `COMPLETE_PENDING_REVIEW` with exact changed paths,
executionBaseHead, verification results, and claim boundary.

## 1. Mission

Implement FPRC-T1 as a bounded governance-foundation tranche. Success means CVF
has a governed root-cause grouping standard, work-order authoring guidance for
provider-memory learning escape and boundary-prose trigger discipline, and
focused checker/test coverage for provider-memory-only learning escape.

## Purpose

Give Claude a bounded no-commit implementation packet for FPRC-T1 so reusable
lessons cannot be closed only in provider-specific memory and repeated findings
can be grouped by root cause.

## Scope / Target / Owner Boundary

Target: FPRC-T1 governance standard, authoring addendum, finding-learning
checker, focused tests, completion review, and FPRC roadmap closure row.

Owner boundary: Claude owns only the files listed in Write Ownership. Codex owns
review, commit, pre-closure, session sync, and any later CCLV-T2 refresh.

## 2. Authority Chain

- Operator instruction: 2026-06-16 priority override to run FPRC-T1 before
  CCLV-T2.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Decision audit:
  `docs/reviews/CVF_FPRC_T1_PRIORITY_OVERRIDE_AND_CCLV_T2_PAUSE_AUDIT_2026-06-16.md`.
- Roadmap:
  `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`.
- GC-018:
  `docs/baselines/CVF_GC018_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_2026-06-16.md`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.

Authority boundary: this work order supersedes CCLV-T2 as the immediate worker
task. CCLV-T2 must stay paused until Codex reviews FPRC-T1.

## 3. Agent Roles

- Orchestrator / dispatcher: Codex.
- Implementer: Claude.
- Reviewer / committer: Codex.
- Operator approval required for: scope expansion, live proof, public-sync,
  legacy absorption, provider-specific memory edits, or runtime product-source
  changes outside `governance/compat`.

## 4. Scope

Allowed scope:

- Create `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`.
- Modify `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`.
- Modify `governance/compat/check_finding_to_governance_learning.py`.
- Modify `governance/compat/test_check_finding_to_governance_learning.py`.
- Create `docs/reviews/CVF_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_COMPLETION_2026-06-16.md`.
- Update `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md` only for FPRC-T1 closure evidence and FPRC-T2 release state.

Forbidden scope:

- Do not execute or modify the CCLV-T2 implementation work order.
- Do not edit provider-specific memory files such as `CLAUDE.md` or personal
  memory stores.
- Do not run live/provider/API proof.
- Do not open public-sync.
- Do not absorb or scan legacy sources.
- Do not migrate historical closed artifacts.
- Do not add broad full-repository text scanning.
- Do not commit.

Risk ceiling: R1 governance guard hardening.

## 5. Required First Reads

- `docs/baselines/CVF_GC018_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_2026-06-16.md` - authorization.
- `docs/reviews/CVF_FPRC_T1_PRIORITY_OVERRIDE_AND_CCLV_T2_PAUSE_AUDIT_2026-06-16.md` - reason CCLV-T2 is paused.
- `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md` - roadmap acceptance criteria.
- `governance/compat/check_finding_to_governance_learning.py` - existing learning trigger checker.
- `governance/compat/check_finding_to_governance_learning.py` - checker to update.
- `governance/compat/test_check_finding_to_governance_learning.py` - focused tests to extend.
- `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` - authoring addendum to update.

## 6. Pre-Flight Checks

Commands:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_active_session_state.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base aa977426 --head HEAD
```

Expected:

- executionBaseHead is current HEAD at worker start.
- Worktree contains only Codex-dispatched files or is clean before worker
  edits. If unrelated dirty files exist, record them and do not touch them.
- Active session state is compliant.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| FPRC-T1 roadmap row exists | `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md` | Tranche Plan | `FPRC-T1` | FPRC roadmap | ACCEPT |
| Finding-learning checker exists | `governance/compat/check_finding_to_governance_learning.py` | module constants and `_validate_finding_doc` | `_validate_finding_doc` | finding-to-governance checker | ACCEPT |
| Finding-learning tests exist | `governance/compat/test_check_finding_to_governance_learning.py` | test module | `test_valid_finding_doc_passes` | pytest test module | ACCEPT |
| Work-order authoring addendum exists | `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` | Purpose / Scope | `CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` | reference addendum | ACCEPT |

### New Doc-Only Fields

| Field | Purpose |
|---|---|
| `Root Cause To Propagated Findings` | Standard table for grouping one root defect and propagated findings |
| `Provider Memory Learning Escape Guard` | Rule requiring governed disposition for reusable lessons reported as stored in provider memory |
| `Boundary-Prose Trigger Discipline` | Rule preventing N/A/out-of-scope prose from becoming positive evidence-class claims |

### Current Runtime Freshness Verification

FPRC-T1 is limited to governance documentation and `governance/compat` checker
logic. Product runtime source, provider adapters, API-key usage, live proof, and
public-sync are out of scope.

Commands:

```powershell
Test-Path governance/compat/check_finding_to_governance_learning.py
Test-Path governance/compat/test_check_finding_to_governance_learning.py
Test-Path docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md
```

### Negative Search And Collision Discipline

No absence claim is used as dispatch authority. If the worker introduces any
absence claim, it must add exact search roots, exact commands, coverage, and
collision disposition before returning.

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| FPRC-AC1 root versus propagated symptom | Sections 8 and 10 | FPRC standard | Review section and tests where applicable | PASS |
| FPRC-AC2 does not replace finding-learning disposition | Sections 8 and 10 | FPRC standard and addendum | Text review | PASS |
| FPRC-AC3 initial checker limited/advisory | Sections 4, 8, 10 | checker update only for provider-memory escape | focused pytest | PASS |
| FPRC-AC4 no broad full-repository text scan | Sections 4 and 8 | checker implementation boundary | code review | PASS |
| FPRC-AC5 no runtime/provider/live/public/legacy scope | Sections 4 and 6A | completion review claim boundary | reviewer gate | PASS |

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously with allowed-scope file edits, tests, and allowed-scope
gate remediation. Do not ask the operator whether to fix a failing gate inside
Allowed scope; repair and rerun it.

Escalate only for scope expansion, claim-boundary change, live/provider proof,
public-sync, legacy absorption, secrets/quota, forbidden paths, destructive
actions, or CCLV-T2 execution.

## 6D. Intake Role Routing Decision

routeMode: MULTI_AGENT_MULTI_ROLE

Intake summary: operator prioritized FPRC-T1 before CCLV-T2 because two
reusable agent-error patterns could recur during CCLV-T2.

Scope classification: bounded governance guard hardening with protected
`governance/compat` paths.

Risk sensitivity: R1; no live proof, public-sync, secrets, provider adapters,
legacy absorption, or runtime product-source changes.

Selected role route: Claude worker implements; Codex reviewer commits.

Role separation basis: multi-agent handoff, no-commit worker return, Codex
reviewer closure.

Escalation condition: any requested work outside Allowed scope.

## 6E. Legacy Absorption Coverage Index Disposition

Disposition: NOT_APPLICABLE_WITH_REASON

Reason: FPRC-T1 hardens governance behavior from current workflow findings. It
does not absorb, scan, or classify legacy material.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update finding-to-governance checker and
focused tests for provider-memory-only learning escape.

Protected paths:

- governance/compat/check_finding_to_governance_learning.py
- governance/compat/test_check_finding_to_governance_learning.py

Operator authorization: operator explicitly prioritized FPRC-T1 before CCLV-T2
to prevent repeated agent-error patterns.

Rollback boundary: revert only FPRC-T1 implementation artifacts and the FPRC
roadmap closure update if rejected. Do not revert prior CCLV-T1/T1A closure,
CCLV-T2 dispatch, or session-sync commits.

## Reviewer Closure Conversion Block

completionReviewPath:
`docs/reviews/CVF_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_COMPLETION_2026-06-16.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_COMPLETION_2026-06-16.md`
- `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/`
- `AGENT_HANDOFF_V19_2026-06-15.md`

Reviewer closure rule: worker handoff is not closure. Codex reviews the pending
diff, commits the accepted material range, runs committed-range pre-closure,
then performs session sync if needed.

## 7. Write Ownership

Owned files:

- `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
- `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`
- `governance/compat/check_finding_to_governance_learning.py`
- `governance/compat/test_check_finding_to_governance_learning.py`
- `docs/reviews/CVF_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_COMPLETION_2026-06-16.md`
- `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`

Write mode: modify-listed/create-listed only.

## 8. Execution Plan

1. Capture `executionBaseHead`.
2. Read required sources.
3. Author the FPRC standard with:
   - root/symptom taxonomy;
   - Provider Memory Learning Escape Guard;
   - Boundary-Prose Trigger Discipline;
   - example root cause table.
4. Update the work-order authoring addendum with short rules for future
   dispatch packets and worker returns.
5. Extend `check_finding_to_governance_learning.py` so finding-bearing changed
   review/audit/log/assessment artifacts fail when they say a reusable lesson
   was stored in provider-specific memory but lack governed learning
   disposition or explicit `N/A_WITH_REASON`.
6. Add focused tests. Include a positive test using a phrase such as
   `provider_memory_only` in the test name.
7. Author completion review with Root Cause To Propagated Findings,
   Finding-To-Governance Learning Disposition, Machine Closure Package, Public
   Export Disposition, and Agent Operation Trace Block.
8. Update FPRC roadmap FPRC-T1 row only if evidence passes.
9. Run required evidence commands and return without commit.

## 8A. Design Control Carry-Forward

| Design control | Roadmap source | Work-order handling | Verdict |
|---|---|---|---|
| Scope boundary | FPRC roadmap Scope | documentation/checker only | PASS |
| Non-goals | FPRC roadmap Non-Goals | forbidden scope blocks broad suppression and historical retrofit | PASS |
| Lane split | FPRC Tranche Plan | executes T1 only | PASS |
| Dependency/source-verification plan | Source Verification Block | current files verified before dispatch | PASS |
| Claim boundary | FPRC roadmap Claim Boundary | finding grouping and learning escape only | PASS |
| Acceptance criteria | FPRC roadmap Acceptance Criteria | mapped in section 6B and 10 | PASS |
| Verification/evidence | FPRC Verification / Evidence | focused tests and reviewer-fast | PASS |
| Dispatch-readiness decision | operator priority override | GC-018 filed and CCLV-T2 paused | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 FPRC-T1 work order authoring |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, apply_patch |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_FOR_CLAUDE_2026-06-16.md` |
| Allowed scope source | operator priority override for FPRC-T1 before CCLV-T2 |
| Before status evidence | base `aa977426` |
| After status evidence | work order authored; pending dispatch commit |
| Diff evidence | `git diff --name-status`; dispatch gates |
| Approval boundary | dispatch packet only; worker must not commit |
| Claim boundary | repo-local trace only |
| Agent type | Codex |
| Invocation ID | fprc-t1-work-order-2026-06-16 |
| Expected manifest | `docs/reviews/CVF_FPRC_T1_PRIORITY_OVERRIDE_AND_CCLV_T2_PAUSE_AUDIT_2026-06-16.md`; `docs/baselines/CVF_GC018_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`; `docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md` |
| Actual changed set | docs/reviews/CVF_FPRC_T1_PRIORITY_OVERRIDE_AND_CCLV_T2_PAUSE_AUDIT_2026-06-16.md; docs/baselines/CVF_GC018_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_2026-06-16.md; docs/work_orders/CVF_AGENT_WORK_ORDER_FPRC_T1_FINDING_ROOT_CAUSE_AND_MEMORY_ESCAPE_GUARD_FOR_CLAUDE_2026-06-16.md; docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md; docs/roadmaps/CVF_CENTRAL_CORE_LOCAL_VIEW_GOVERNANCE_REFACTOR_ROADMAP_2026-06-16.md |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## 8C. Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a focused provider-memory-only learning escape
case can be detected without broad repository scanning.

Evidence Comparison Requirement: worker return compares actual checker behavior
against the prediction.

Contradiction Handling Requirement: if focused detection requires broad scans or
causes false positives, record a Contradiction Or Gap Disposition and narrow the
claim.

Claim Update Requirement: completion review records whether the claim was
confirmed, narrowed, or deferred.

## Evidence Requirements

Worker must run:

```powershell
pytest governance/compat/test_check_finding_to_governance_learning.py
python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_finding_to_governance_learning.py
git diff --check
```

Worker may run:

```powershell
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
```

Base-anchor evidence:

- dispatchBaseHead: `aa977426`
- executionBaseHead: worker must refresh at start
- closureBaseHead: N/A with reason: Codex reviewer owns closure commit
- Commit mode: `WORKER_MUST_NOT_COMMIT`
- Pending-artifact component gates: focused pytest, checker self-run,
  worker-return fast gate, diff check
- Committed-range pre-closure: N/A with reason: Codex reviewer owns after commit

## 10. Acceptance Criteria

- [ ] FPRC standard exists.
- [ ] FPRC standard includes `Root Cause To Propagated Findings`.
- [ ] FPRC standard includes `Provider Memory Learning Escape Guard`.
- [ ] FPRC standard includes `Boundary-Prose Trigger Discipline`.
- [ ] Work-order authoring addendum updated.
- [ ] Finding-learning checker updated for provider-memory-only lesson escape.
- [ ] Focused tests pass.
- [ ] Worker completion review records exact pending changed set.
- [ ] CCLV-T2 remains paused.

Fail conditions:

- [ ] Provider-specific memory is treated as CVF source authority.
- [ ] Provider-memory-only lessons can close without governed learning
  disposition or explicit `N/A_WITH_REASON`.
- [ ] Boundary-prose guidance weakens existing evidence requirements.
- [ ] Worker edits CCLV-T2 or provider-specific memory files.
- [ ] Worker commits.

## 11. Review Gate

Codex review requires:

- exact uncommitted changed set inside Write Ownership;
- focused tests PASS;
- checker self-run PASS;
- reviewer-fast PASS;
- `git diff --check` PASS;
- Codex-authored or Codex-accepted completion review;
- committed-range pre-closure PASS after Codex commits.

## 12. Closure Checklist

- [ ] Worker reported executionBaseHead and HEAD unchanged.
- [ ] Required artifacts exist.
- [ ] Required proof literals exist.
- [ ] Focused tests PASS.
- [ ] Finding-learning checker self-run PASS.
- [ ] Worker-return fast gate PASS.
- [ ] `git diff --check` PASS.
- [ ] Completion review includes Root Cause To Propagated Findings.
- [ ] Completion review includes Finding-To-Governance Learning Disposition.
- [ ] Completion review includes Machine Closure Package.
- [ ] Codex reviewed and committed accepted material range.
- [ ] Pre-closure gate PASS on committed material range.

## 13. Return-To-Orchestrator Conditions

Return without continuing if:

- any required change would exceed Allowed scope;
- focused checker behavior requires broad scanning;
- provider-specific memory must be edited to pass;
- CCLV-T2 must be changed to proceed;
- a required gate fails outside Allowed scope.

## Operator Checkpoint

No operator checkpoint is required for allowed-scope FPRC-T1 remediation.
Operator approval is required only for the escalation cases listed in section
6C.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. No public-sync batch is authorized.

## Claim Boundary

This work order authorizes FPRC-T1 governance guard hardening only. It does not
authorize runtime product behavior, provider behavior, live proof, public-sync,
production readiness, public readiness, historical migration, or CCLV-T2
execution.
