# CVF Autorun Exact-Manifest Range Shape Guard Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-15

## Purpose

Promote a repeated reviewer/committer error into a machine guard: full
pre-closure ranges must not mix Agent Operation Trace exact-manifest artifacts
with protected session or handoff sync paths.

## Target / Source

Target:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`

Source: operator finding on 2026-06-15 that Codex repeatedly ran or attempted
invalid combined ranges and that the pattern must be controlled by guard
placement instead of agent memory.

## Scope / Methodology

Scope is limited to the autorun workflow wrapper and focused tests. The change
reuses the existing commit steward path-shape classifier so an invalid combined
range fails before the full pre-closure or pre-push bundle runs.

## Findings / Position

Finding: agents, including Codex, can repeatedly run a full closure range that
includes material artifacts plus handoff/session-sync commits. That range is
semantically invalid when a changed artifact carries an exact Agent Operation
Trace manifest, because the protected sync file is observed by git but is not
part of the material manifest.

Position: this is a governance-control-plane learning issue, not a worker-only
mistake. The earliest practical control point is the autorun wrapper itself.

## Risk / Corrective Action

Risk: without early range-shape rejection, agents waste time running a full
bundle and may normalize a bad evidence habit.

Corrective action: add a range-shape preflight to `pre-closure` and `pre-push`.
If the range mixes exact-manifest artifacts with protected session/handoff
paths, fail immediately and instruct split ranges: material range first, then
closure/session range.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: operator identified repeated Codex range
selection failures and requested control so the pattern does not recur. This
batch hardens the autorun workflow wrapper to reject the invalid range shape
early.

Protected paths:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`

Operator authorization: operator request on 2026-06-15 that repeated
full-range exact-manifest/session-sync violations be controlled rather than
handled by memory.

Rollback boundary: revert only this guard hardening batch. Do not revert Model
Gateway C-02 P4C material, closure, or session-sync commits.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Full pre-closure range can mix exact-manifest artifacts with handoff/session sync and fail late | PHASE_GATE_PLACEMENT_GAP; MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED; N/A_WITH_REASON runtime/provider/cost learning not applicable because this is local guard placement | Autorun wrapper now fails the invalid range shape before the full bundle runs |

## Epistemic Process Block

## Expected Result / Prediction

Prediction: an invalid combined range will fail immediately in the autorun
wrapper, while split material-only and closure-only ranges remain allowed.

## Evidence Comparison

Evidence comparison: focused tests cover both the blocked mixed range and the
allowed split material range.

## Contradiction Or Gap Disposition

Contradiction or gap disposition: this does not weaken Agent Operation Trace,
active session, handoff, or closure gates. It only moves a known failure earlier.

## Claim Update

Claim update: prediction is bounded to local range-shape classification. No
runtime/provider behavior, public readiness, or production readiness is claimed.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | Codex CLI |
| Session or invocation | Autorun exact-manifest range-shape guard hardening from HEAD `6150fc0e` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | Edit autorun wrapper; add focused tests; add this completion/auth review |
| Target paths | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/test_run_agent_autorun_workflow_gate.py`; `docs/reviews/CVF_AUTORUN_EXACT_MANIFEST_RANGE_SHAPE_GUARD_HARDENING_2026-06-15.md` |
| Allowed scope source | Operator request 2026-06-15: control repeated exact-manifest/session-sync full-range violations |
| Before status evidence | HEAD `6150fc0e`; worktree clean before this batch |
| After status evidence | `git status --short` shows exactly the three target paths before commit |
| Diff evidence | focused pytest, steward preflight, reviewer-fast, and `git diff --check` before commit |
| Approval boundary | Governance-control hardening only |
| Claim boundary | Local guard behavior only; no runtime/provider/live/public behavior claim |
| Agent type | Single agent acting as reviewer and governance-control maintainer |
| Invocation ID | autorun-range-shape-hardening-2026-06-15 |
| Expected manifest | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/test_run_agent_autorun_workflow_gate.py`; `docs/reviews/CVF_AUTORUN_EXACT_MANIFEST_RANGE_SHAPE_GUARD_HARDENING_2026-06-15.md` |
| Actual changed set | `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/test_run_agent_autorun_workflow_gate.py`; `docs/reviews/CVF_AUTORUN_EXACT_MANIFEST_RANGE_SHAPE_GUARD_HARDENING_2026-06-15.md` |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance governance-control hardening. No public-sync
batch is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | N/A with reason: direct operator-authorized guard hardening | This completion review records the operator source and scope | N/A with reason: no separate work order was created for this small control-plane repair |
| Completion or reviewer artifact | `docs/reviews/CVF_AUTORUN_EXACT_MANIFEST_RANGE_SHAPE_GUARD_HARDENING_2026-06-15.md` | This artifact | PASS |
| Roadmap state | N/A with reason: direct guard repair, not roadmap-derived | No roadmap path cited as owner | N/A with reason: no roadmap state changes |
| Registry JSON | No registry JSON owner changed | `git status --short` changed set excludes registry JSON | PASS |
| Registry Markdown | No registry Markdown owner changed | `git status --short` changed set excludes registry Markdown | PASS |
| External evidence digest | N/A with reason: no external evidence used | Repo-local tests and guard output only | N/A with reason: no external artifact |
| System loop interlock | N/A with reason: no system-loop interlock surface changed | Guard wrapper only | N/A with reason: no interlock row required |
| Session continuity | N/A with reason: no session mode or next allowed move changed | Session files unchanged | N/A with reason: no session sync needed |

## Claim Boundary

This review records a bounded control-plane hardening only. It does not change
Model Gateway behavior, provider routing, live proof, public-sync, production
readiness, or co-work product development.
