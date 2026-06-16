# CVF Next-Move Freshness Checker Foundation Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-16

Owner / closer: Codex

rawMemoryReleased: false

## Purpose

Close the bounded governance-checker repair authorized after RSF-T3: future
active next-move surfaces should fail local/autorun gates when they dispatch or
open work already closed in active session state.

## Scope / Methodology

Scope: local governance checker, tests, hook-chain wiring, autorun wiring,
steward wiring, and governed closure packets.

Methodology:

- inspect current session next-move surfaces and C-02 P2 closure state;
- implement deterministic read-only checker logic;
- add synthetic stale/safe focused tests;
- run current-state checker and governance gates;
- close with material/session split.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Work order authorized this checker | `docs/work_orders/CVF_AGENT_WORK_ORDER_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_FOR_CODEX_2026-06-16.md` | `## Scope` | `check_next_move_freshness.py` | work order | ACCEPT |
| Standard defines current next-move surfaces | `docs/reference/CVF_NEXT_MOVE_FRESHNESS_CHECKER_STANDARD_2026-06-16.md` | `## Current Surfaces` | `nextAllowedMove` | reference standard | ACCEPT |
| Checker implements current-surface scan | `governance/compat/check_next_move_freshness.py` | module constants and `collect_next_move_surfaces` | `collect_next_move_surfaces` | next-move freshness checker | ACCEPT |
| Focused tests cover stale closed-target dispatch | `governance/compat/test_check_next_move_freshness.py` | test methods | `test_rejects_active_state_dispatch_to_closed_target` | unittest suite | ACCEPT |
| Hook chain runner exposes reviewer-fast checks | `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS` | `REVIEWER_FAST_CHECKS` | local governance hook chain | ACCEPT |
| Autorun common gates include checker | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `next-move freshness` | autorun workflow gate | ACCEPT |
| Steward session-sync lane includes checker | `governance/compat/run_agent_commit_steward_preflight.py` | `mode == "session-sync"` | `next-move freshness` | commit steward preflight | ACCEPT |

## Implementation Summary

Added `governance/compat/check_next_move_freshness.py`, a read-only checker
that:

- discovers closed targets from active session state records with
  `CLOSED_PASS` or `CLOSED_PASS_BOUNDED`;
- scans current next-move surfaces only;
- rejects stale dispatch/open/worker-action wording for closed labels;
- allows blocked or closure-context mentions;
- splits long next-move prose into sentence fragments to avoid safe text
  masking stale action text later in the same value.

Added focused tests for active state, front door, handoff section, startup
acknowledgment, advisory mode, missing section enforcement, allowed blocked
context, soft-wrapped negation, and long-line masking.

Wired the checker into reviewer-fast, pre-commit, pre-push, autorun common
phase gates, and steward `session-sync` preflight.

## Findings / Position

| ID | Finding | Evidence | Disposition |
|---|---|---|---|
| NMF-F1 | Existing structural session checks do not prove next-move semantic freshness. | RSF-T3 machine-check candidate and current checker addition | CLOSED_BY_MACHINE_CHECK |
| NMF-F2 | Current session surfaces are now compliant. | `check_next_move_freshness.py --enforce` returns zero violations | PASS |
| NMF-F3 | Synthetic stale active-state/front-door/handoff/startup text is rejected. | focused unittest suite PASS 9/9 | PASS |

## Risk / Corrective Action

| Risk | Corrective action | Disposition |
|---|---|---|
| Long `nextAllowedMove` prose could mask a later stale sentence | checker splits sentence fragments before evaluating safe context | CONTROLLED |
| Historical nested state entries could create false positives | checker scans current next-move surfaces only | CONTROLLED |
| Guard wiring could be too late for worker returns | checker added to reviewer-fast and autorun common gates | CONTROLLED |

## Verification

| Command | Result |
|---|---|
| `python -m unittest governance.compat.test_check_next_move_freshness -v` | PASS 9/9 |
| `python governance/compat/check_next_move_freshness.py --enforce` | PASS on current active state, front door, and handoff |
| `python governance/compat/check_markdown_structural_completeness.py --base 7a89cccc --head HEAD --enforce` | PASS |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS; reviewer-fast 19/19 PASS |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 7a89cccc --head HEAD --enforce` | PASS |

Post-material-commit required gate:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 7a89cccc --head HEAD`

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work order section | Final artifact or evidence | Disposition |
|---|---|---|---|
| RSF-T3 machine-check candidate | Purpose and Scope | checker, tests, hook/autorun/steward wiring | PASS |
| Operator asked to process this error first | Dispatch Prompt Envelope | bounded material batch on base `7a89cccc` | PASS |
| No Model Gateway redispatch/P3 opening | Scope and Claim Boundary | no Model Gateway source changed | PASS |
| No session mutation in material commit | Scope | session files excluded from manifest | PASS |

## Closure Diff Gate

| Surface | Requirement | Reviewer result |
|---|---|---|
| Checker | read-only, current surfaces only | PASS |
| Tests | cover stale and safe cases | PASS |
| Gate wiring | early enough for worker-return, commit, push, autorun, and session-sync | PASS |
| Documentation | work order, GC-018, standard, completion present | PASS |
| Scope | no runtime/provider/live/public/session material mutation | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_FOR_CODEX_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason | direct operator-authorized bounded foundation guard; no dedicated roadmap opened | N/A with reason |
| Registry JSON | BLOCKED with reason | no corpus registry mutation authorized or needed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no corpus registry mutation authorized or needed | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source, provider, OCR, live-proof, or public-sync artifact | N/A with reason |
| System loop interlock | N/A with reason | no system loop interlock registry mutation | N/A with reason |
| Session continuity | N/A with reason | material commit excludes session-sync; continuity sync is a separate lane | N/A with reason |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `MACHINE_GATE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_ADDED` |
| Next control action | Checker added and wired into reviewer-fast, pre-commit, pre-push, autorun common gates, and steward `session-sync` |
| Worker blame | `N/A_WITH_REASON`: the defect was a control-plane freshness gap left after RSF-T3, not a worker-only error |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE.

Expected Result / Prediction: current session surfaces are compliant after
RSF-T3 pointer remediation, while synthetic stale next-move text should fail.

Evidence Comparison: current-state checker run passes with zero violations.
Focused tests prove stale active-state, front-door, handoff, and startup
acknowledgment text fail in enforce mode.

Contradiction Or Gap Disposition: prediction confirmed.

Claim Update: CVF now has a bounded machine gate for current next-move
freshness; it is not a broad historical roadmap reconciliation engine.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 next-move freshness checker foundation |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | apply_patch, unittest, checker CLI, local governance gates |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_COMPLETION_2026-06-16.md`; `governance/compat/check_next_move_freshness.py`; `governance/compat/test_check_next_move_freshness.py` |
| Allowed scope source | operator instruction, work order, GC-018 |
| Before status evidence | `executionBaseHead=7a89cccc`; clean worktree before edits |
| After status evidence | pending material commit |
| Diff evidence | `git diff --name-status` on `7a89cccc..HEAD` after material commit |
| Approval boundary | bounded governance-checker hardening only |
| Claim boundary | no runtime/provider/live/public/session material mutation or Model Gateway authorization |
| Agent type | Codex single-agent multi-role |
| Invocation ID | `next-move-freshness-checker-foundation-2026-06-16` |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_COMPLETION_2026-06-16.md`; `governance/compat/check_next_move_freshness.py`; `governance/compat/test_check_next_move_freshness.py` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_COMPLETION_2026-06-16.md`; `governance/compat/check_next_move_freshness.py`; `governance/compat/test_check_next_move_freshness.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance guard hardening. No public-sync batch is
authorized.

## Claim Boundary

Allowed claim: CVF has a read-only next-move freshness checker wired into
local and autorun gates. It catches current next-move surfaces that dispatch or
open already closed work.

Forbidden claims:

- broad historical roadmap reconciliation is complete;
- runtime governance behavior changed;
- provider routing or live governance behavior was proven;
- Model Gateway C-02 P2/P3 work is authorized;
- public readiness, production readiness, public export, or public catalog
  update occurred.
