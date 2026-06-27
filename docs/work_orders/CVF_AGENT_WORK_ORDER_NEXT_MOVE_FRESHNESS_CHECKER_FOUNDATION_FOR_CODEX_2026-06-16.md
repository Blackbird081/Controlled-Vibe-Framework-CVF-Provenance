# CVF Agent Work Order - Next-Move Freshness Checker Foundation For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-16

Owner / Orchestrator: Codex

Implementer: Codex

Reviewer / closer: Codex

commitMode: WORKER_MAY_COMMIT

executionBaseHead: 7a89cccc

riskCeiling: R1_GOVERNANCE_CHECKER_HARDENING

rawMemoryReleased: false

completionReviewPath:
`docs/reviews/CVF_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_COMPLETION_2026-06-16.md`

## Dispatch Prompt Envelope

```text
Role: Codex is orchestrator, implementer, reviewer, and commit steward for a bounded governance-checker foundation batch.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_FOR_CODEX_2026-06-16.md.
Commit mode: WORKER_MAY_COMMIT with material/session split.
Base: executionBaseHead 7a89cccc.
Current-time notes: operator authorized fixing the RSF-T3 machine-check gap before opening other roadmap work.
Do-not-misread notes: do not redispatch Model Gateway C-02 P2; do not open Model Gateway P3; do not run provider/API/live/public-sync; do not mutate session files in the material commit.
Required first actions: read CVF_SESSION_MEMORY.md, CVF_SESSION/ACTIVE_SESSION_STATE.json, AGENT_HANDOFF_V19_2026-06-15.md, RSF-T3 completion, C-02 P2 state entry, existing session-mode checker, hook chain, autorun gate, and steward preflight.
Return contract: committed material range with focused tests, checker current-state run, reviewer-fast/pre-closure evidence, then separate session-sync.
```

## Purpose

Implement the machine-check candidate left by RSF-T3: active next-move text
must not point a future agent back at work already closed in active session
state.

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | scope selection and packet authoring |
| Implementer | Codex | bounded checker, tests, and gate wiring |
| Reviewer / closer | Codex | gates, closure review, material commit |
| Operator | Human | scope expansion, public-sync, live/provider, runtime product work |

## Authority Chain

- Operator instruction on 2026-06-16: "xu ly loi nay truoc".
- RSF-T3 completion:
  `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md`.
- Active state registry: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active session front door: `CVF_SESSION_MEMORY.md`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.
- GC-018:
  `docs/baselines/CVF_GC018_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_2026-06-16.md`.

## Intake Role Routing Decision

routeMode: SINGLE_AGENT_MULTI_ROLE

Intake summary: RSF-T3 proved a stale non-CI2 next-move sample and left the
semantic freshness check as a machine-check candidate. The operator authorized
fixing that machine gap before any other roadmap work.

Scope classification: R1 governance checker hardening.

Risk sensitivity: protected `governance/compat` paths and governed artifacts;
no provider, credential, live, public-sync, runtime product source, or session
mutation in material commit.

Selected role route: Codex implements and reviews in one bounded material
batch because the operator directly authorized a narrow control-plane repair.

Escalation condition: any request to mutate runtime product source, run live or
provider proof, open public-sync, alter Model Gateway scope, or update session
continuity before material commit.

## Required First Reads

| File | Required use |
|---|---|
| `CVF_SESSION_MEMORY.md` | current front-door next-move surface |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active state aggregate and active handoff |
| `CVF_SESSION/state/entries/nextAllowedMove.json` | source nextAllowedMove entry |
| `AGENT_HANDOFF_V19_2026-06-15.md` | active handoff next-move and startup acknowledgment |
| `CVF_SESSION/state/entries/modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615.json` | closed C-02 P2 source evidence |
| `governance/compat/check_session_mode_consistency.py` | read-only session-surface checker pattern |
| `governance/compat/run_local_governance_hook_chain.py` | reviewer-fast/pre-commit/pre-push wiring point |
| `governance/compat/run_agent_autorun_workflow_gate.py` | autorun common wiring point |
| `governance/compat/run_agent_commit_steward_preflight.py` | session-sync steward wiring point |

## Pre-Flight Checks

Commands:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_session_mode_consistency.py --enforce
```

Expected: base head is `7a89cccc`, worktree is clean before edits, and
structural session gates pass before the semantic freshness checker is added.

## Single-Agent Multi-Role Control Block

| Control | Disposition |
|---|---|
| Role separation reason | Bounded guard implementation is small and source-local; operator directly authorized immediate repair |
| Self-review duty | Codex must run focused tests, checker current-state run, reviewer-fast, steward/autorun gates, and committed-range closure gates |
| Commit split | Material commit first; session-sync commit second if continuity changes |
| Stop condition | Any out-of-scope runtime/provider/public/session mutation stops material work |

## Scope

Allowed paths:

- `docs/baselines/CVF_GC018_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_2026-06-16.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_FOR_CODEX_2026-06-16.md`
- `docs/reference/CVF_NEXT_MOVE_FRESHNESS_CHECKER_STANDARD_2026-06-16.md`
- `docs/reviews/CVF_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_COMPLETION_2026-06-16.md`
- `governance/compat/check_next_move_freshness.py`
- `governance/compat/test_check_next_move_freshness.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_agent_commit_steward_preflight.py`

Forbidden paths and work:

- `CVF_SESSION/**`, `CVF_SESSION_MEMORY.md`, and `AGENT_HANDOFF_V19_2026-06-15.md`
  in the material commit;
- runtime product source outside `governance/compat`;
- provider/API calls, credentials, network proof, live proof, public-sync;
- Model Gateway C-02 P2 redispatch or Model Gateway P3 authorization;
- broad legacy scan, historical migration, public readiness, production
  readiness, or co-work product development.

## Write Ownership

Codex may write only the paths listed in Allowed paths for the material commit.
Session front door, active state, and active handoff updates are reserved for a
separate session-sync commit after material closure.

## Execution Plan

1. Add `check_next_move_freshness.py`.
2. Add focused unit tests for stale and safe current next-move cases.
3. Wire the checker into reviewer-fast, pre-commit, pre-push, autorun common
   gates, and steward `session-sync`.
4. Add GC-018, standard, work order, and completion review.
5. Run focused tests and required local governance gates.
6. Commit material changes, then run material-range pre-closure.

## Evidence Requirements

Evidence must include:

- focused unit-test output;
- current-state checker output;
- core guard self-protection output;
- dispatch-quality, trace, machine-closure, public-export, and
  finding-learning outputs;
- reviewer-fast and steward/autorun outputs;
- `git diff --name-status` or committed range evidence.

## Acceptance Criteria

| ID | Acceptance criterion | Evidence |
|---|---|---|
| NMF-AC1 | stale closed-target active `nextAllowedMove` fails | focused test |
| NMF-AC2 | stale front-door next move fails | focused test |
| NMF-AC3 | stale handoff next move and startup acknowledgment fail | focused tests |
| NMF-AC4 | safe blocked/closed wording passes, including soft-wrapped negation | focused tests and current-state run |
| NMF-AC5 | checker is wired into early gates | runner diffs and gates |

## Review Gate

Closure requires focused tests, current-state checker run, reviewer-fast, and
material-range pre-closure to pass or record a bounded session-sync-only
exception if the material commit needs later continuity sync.

## Closure Checklist

- [x] GC-018 authorization exists.
- [x] Work order includes dispatch prompt envelope.
- [x] Checker and tests are implemented.
- [x] Gate wiring is additive.
- [x] Machine closure package is present.
- [x] Public export disposition is present.
- [x] Runtime/provider/live/public/session material mutation is excluded.

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after tests and local gates pass for the
material scope. Return `BLOCKED` if closure requires runtime, provider,
public-sync, Model Gateway, or session mutation inside the material commit.

## Operator Checkpoint

No operator checkpoint remains inside this bounded material scope. Operator
authorization is required for the next roadmap, public-sync, live/provider
proof, runtime product mutation, Model Gateway P3, or any session-sync beyond
recording this closure.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Active next-move source is top-level `nextAllowedMove` | `CVF_SESSION/state/entries/nextAllowedMove.json` | JSON `stateKey` and `value` | `nextAllowedMove` | active session state entry | ACCEPT |
| Generated active session state carries `nextAllowedMove` | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | top-level key | `nextAllowedMove` | generated active state aggregate | ACCEPT |
| C-02 P2 state entry is closed bounded | `CVF_SESSION/state/entries/modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615.json` | JSON `value.status` | `modelGatewayC02P2DynamicModelRegistryBoundaryDispatch20260615` | active session state entry | ACCEPT |
| Front door has current Next Allowed Move section | `CVF_SESSION_MEMORY.md` | `## Next Allowed Move` | `Next Allowed Move` | active session front door | ACCEPT |
| Active handoff has current Next Allowed Move section | `AGENT_HANDOFF_V19_2026-06-15.md` | `## Next Allowed Move` | `Next Allowed Move` | active handoff | ACCEPT |
| Existing session-mode checker resolves active handoff from active state | `governance/compat/check_session_mode_consistency.py` | `resolve_active_handoff` | `activeHandoff` | session mode checker | ACCEPT |
| Reviewer-fast hook is the early worker-return gate | `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS` | `REVIEWER_FAST_CHECKS` | local governance hook chain | ACCEPT |
| Autorun common gate function exists | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `_common_commands` | autorun workflow gate | ACCEPT |
| Steward session-sync lane includes generated state and session checks | `governance/compat/run_agent_commit_steward_preflight.py` | `mode == "session-sync"` | `session-sync` | commit steward preflight | ACCEPT |

## Required Artifact Manifest

| Path | Role |
|---|---|
| `docs/baselines/CVF_GC018_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_2026-06-16.md` | GC-018 authorization |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_FOR_CODEX_2026-06-16.md` | work order |
| `docs/reference/CVF_NEXT_MOVE_FRESHNESS_CHECKER_STANDARD_2026-06-16.md` | reference standard |
| `docs/reviews/CVF_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_COMPLETION_2026-06-16.md` | completion review |
| `governance/compat/check_next_move_freshness.py` | checker |
| `governance/compat/test_check_next_move_freshness.py` | focused tests |
| `governance/compat/run_local_governance_hook_chain.py` | local hook wiring |
| `governance/compat/run_agent_autorun_workflow_gate.py` | autorun wiring |
| `governance/compat/run_agent_commit_steward_preflight.py` | steward wiring |

## Work-Order Fulfillment Manifest

| Deliverable | Path | Final disposition |
|---|---|---|
| GC-018 authorization | `docs/baselines/CVF_GC018_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_2026-06-16.md` | PASS |
| Work order | this file | PASS |
| Standard | `docs/reference/CVF_NEXT_MOVE_FRESHNESS_CHECKER_STANDARD_2026-06-16.md` | PASS |
| Completion review | `docs/reviews/CVF_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_COMPLETION_2026-06-16.md` | PASS |
| Checker | `governance/compat/check_next_move_freshness.py` | PASS |
| Focused tests | `governance/compat/test_check_next_move_freshness.py` | PASS |
| Hook chain wiring | `governance/compat/run_local_governance_hook_chain.py` | PASS |
| Autorun wiring | `governance/compat/run_agent_autorun_workflow_gate.py` | PASS |
| Steward wiring | `governance/compat/run_agent_commit_steward_preflight.py` | PASS |

## Commit Mode And Base-Anchor Lifecycle

| Field | Value |
|---|---|
| executionBaseHead | `7a89cccc` |
| material closure base | `7a89cccc` |
| material commit mode | `WORKER_MAY_COMMIT` |
| session-sync plan | separate commit after material closure if next allowed move changes |
| invalid evidence shape | identical base and head refs are not closure evidence |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and wire a read-only next-move
freshness checker so existing local and autorun gates reject stale active
next-move text that targets closed work.

Protected paths:

- `governance/compat/check_next_move_freshness.py`
- `governance/compat/test_check_next_move_freshness.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_agent_commit_steward_preflight.py`

Operator authorization: 2026-06-16 operator instruction to process this error
before the next roadmap.

Rollback boundary: revert only the next-move freshness checker batch if
rejected; do not revert RSF-T3, C-02 P2, or prior session-sync commits.

## Negative Search And Collision Discipline

No absence claim is used as authority. The checker rejects positive stale
action wording against known closed labels and does not depend on a repository
wide negative search.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

Prior evidence from RSF-T3 is used only to select the defect class. This batch
recomputes current evidence from active session state, front door, active
handoff, focused tests, and guard runs. Authored text remains ASCII.

## Required Proof Manifest Atomic Literal Discipline

Required proof commands:

```powershell
python -m unittest governance.compat.test_check_next_move_freshness -v
python governance/compat/check_next_move_freshness.py --enforce
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 7a89cccc --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 7a89cccc --head HEAD
```

Each command result must be recorded in the completion review before closure.

## Legacy Absorption Coverage Index Disposition

Disposition: NOT_APPLICABLE_WITH_REASON

Reason: this work hardens current session next-move governance and does not
absorb, scan, classify, or re-open legacy material.

## Export Surface Decision

Public export surface: DEFERRED_PRIVATE_ONLY.

Reason: private provenance governance guard hardening. No public-sync batch is
authorized by this work order.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap or candidate source | Requirement | Work order output | Disposition |
|---|---|---|---|
| RSF-T3 machine-check candidate | implement bounded next-move freshness checker | checker, tests, standard, gate wiring | PASS |
| Operator instruction | process this error first | immediate bounded guard batch | PASS |
| Current active session state | no C-02 P2 redispatch from stale text | checker rejects closed-target action wording | PASS |

## Closure Diff Gate

| Surface | Required closure result | Final result |
|---|---|---|
| Checker | read-only, current surfaces only | PASS |
| Tests | stale active state, front door, handoff, startup, long-line masking | PASS |
| Hook chain | reviewer-fast, pre-commit, pre-push wiring | PASS |
| Autorun/steward | common phase gate and session-sync lane wiring | PASS |
| Scope | no runtime/provider/public/session material mutation | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason | direct operator-authorized bounded foundation guard; no dedicated roadmap opened | N/A with reason |
| Registry JSON | BLOCKED with reason | no corpus registry mutation authorized or needed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no corpus registry mutation authorized or needed | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source, provider, OCR, live-proof, or public-sync artifact | N/A with reason |
| System loop interlock | N/A with reason | no system loop interlock registry mutation | N/A with reason |
| Session continuity | N/A with reason | material commit excludes session-sync; continuity sync is a separate lane | N/A with reason |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 next-move freshness checker foundation |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | apply_patch, unittest, checker CLI, local governance gates |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_NEXT_MOVE_FRESHNESS_CHECKER_FOUNDATION_COMPLETION_2026-06-16.md`; `governance/compat/check_next_move_freshness.py`; `governance/compat/test_check_next_move_freshness.py` |
| Allowed scope source | operator instruction, this work order, GC-018 |
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

This work order closes a read-only next-move freshness checker and gate wiring.
It does not claim runtime governance behavior, provider behavior, public
readiness, production readiness, Model Gateway implementation readiness, or
public export.
