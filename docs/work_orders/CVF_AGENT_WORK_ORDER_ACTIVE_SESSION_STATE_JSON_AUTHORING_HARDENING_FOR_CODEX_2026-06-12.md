# CVF Agent Work Order - Active Session State JSON Authoring Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-12

Assigned agent: Codex

executionBaseHead: `005b5944`

closureBaseHead: `005b5944`

## Purpose

Execute the bounded control-plane hardening that converts
`ACTIVE_SESSION_STATE.json` from direct monolithic authoring into generated
aggregate authoring.

## Authority Chain

GC-018:

`docs/baselines/CVF_GC018_ACTIVE_SESSION_STATE_JSON_AUTHORING_HARDENING_2026-06-12.md`

Operator instruction: strengthen the CVF foundation and standardize JSON usage
before moving into the Policy_Local use case.

## Objective

Add active-session state source files, a generator, focused tests, and
aggregate drift enforcement in the active session checker.

## Agent Roles

Codex acts as orchestrator, implementer, reviewer, and closer for this small
control-plane tranche. Role separation is artifact-based: GC-018 baseline,
work order, generator/tests, checker output, and completion review are kept
distinct.

## Allowed Scope

- `CVF_SESSION/state/**`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `governance/compat/generate_active_session_state.py`
- `governance/compat/test_generate_active_session_state.py`
- `governance/compat/check_active_session_state.py`
- `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`
- `AGENTS.md`
- this work order, matching GC-018 baseline, and completion review

## Forbidden Scope

- Do not mutate external Policy_Local or cloned `dich-tai-lieu`.
- Do not change active-session semantics except stale `nextAllowedMove`
  correction to the already active PL-S1 boundary.
- Do not activate EC, retrieval, OCR, provider/API proof, corpus ingestion,
  public-sync, T12, readiness claims, memory reinjection, high-risk promotion,
  or autonomous mutation.

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`
- `governance/compat/check_active_session_state.py`
- `governance/compat/generate_corpus_scan_registry.py`

## Pre-Flight Checks

- Confirm worktree status before edits.
- Resolve active handoff and next allowed move.
- Confirm JSON parse of current aggregate.

## Write Ownership

Write ownership is limited to the paths listed in Allowed Scope. No
Policy_Local, public-sync, provider, EC, OCR, corpus ingestion, or external
repo path is owned by this work order.

## Execution Plan

1. Add active session state generator with bootstrap, generate, and check modes.
2. Bootstrap current aggregate into core and per-entry source JSON files.
3. Correct stale `nextAllowedMove` in the generated source entry.
4. Wire drift validation into `check_active_session_state.py`.
5. Add focused unit tests.
6. Add general JSON generated aggregate discipline standard and AGENTS rule.
7. Run focused checks and reviewer-fast.

## Evidence Requirements

- `python governance/compat/generate_active_session_state.py --check`
- `python governance/compat/check_active_session_state.py --enforce`
- `python -m unittest governance.compat.test_generate_active_session_state`
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Active state aggregate is startup registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | top-level object | `activeSessionFrontDoor`, `activeHandoff`, `currentMode` | active session state registry | ACCEPT |
| Active session checker validates aggregate | `governance/compat/check_active_session_state.py` | `_load_state`, `_classify` | `_classify` | active session state gate | ACCEPT |
| Existing generator pattern is available | `governance/compat/generate_corpus_scan_registry.py` | CLI parser and drift validator | `--bootstrap-from-current`, `--generate`, `--check`, `validate_aggregate_matches_sources` | generated aggregate pattern | ACCEPT |
| Active handoff contains current mode boundary | `AGENT_HANDOFF_V18_2026-06-12.md` | Current Mode / Next Allowed Move | `gc051_registry_authoring_hardening_closed_pass_bounded`, `PL-S1` | active handoff | ACCEPT |

## Acceptance Criteria

- Source files exist for current active session state.
- A generator can bootstrap, generate, and check the aggregate.
- `check_active_session_state.py --enforce` fails if the aggregate drifts from
  generated sources.
- Focused unit tests cover filename safety, ordering, entry validation, and
  drift detection.
- General JSON generated aggregate discipline is recorded for future governed
  JSON files.
- `nextAllowedMove` no longer contains stale EXA-T2 dispatch text.

## Verification Evidence

- `python governance/compat/generate_active_session_state.py --check` PASS.
- `python governance/compat/check_active_session_state.py --enforce` PASS.
- `python -m unittest governance.compat.test_generate_active_session_state`
  PASS 4/4.

## Review Gate

Reviewer-fast must pass before closure. Any allowed-scope reviewer-fast failure
must be repaired in this batch.

## Closure Checklist

- [x] Active state source files bootstrapped.
- [x] Generator added.
- [x] Checker drift validation added.
- [x] Focused unit tests added.
- [x] JSON aggregate discipline standard added.
- [x] Stale `nextAllowedMove` corrected.
- [x] Claim boundary preserved.

## Return-To-Orchestrator Conditions

Return to operator only if remediation would require Policy_Local mutation,
public-sync, provider/API use, EC activation, deletion of state entries, or
semantic changes beyond stale `nextAllowedMove` correction.

## Operator Checkpoint

Operator checkpoint satisfied by direct instruction to strengthen the CVF
foundation before applying CVF to the cloned Policy_Local use case.

## Closure Result

Status: `CLOSED_PASS_BOUNDED`.

Completion:

`docs/reviews/CVF_ACTIVE_SESSION_STATE_JSON_AUTHORING_HARDENING_COMPLETION_2026-06-12.md`

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | Status: CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ACTIVE_SESSION_STATE_JSON_AUTHORING_HARDENING_COMPLETION_2026-06-12.md` | Status: CLOSED_PASS_BOUNDED | PASS |
| Roadmap state | N/A | Direct operator-authorized small control-plane batch; no separate roadmap opened | N/A with reason |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | aggregate drift checker PASS | PASS |
| Registry Markdown | BLOCKED with reason: active-state source layout uses JSON only; no Markdown registry surface exists or is authorized | no Markdown registry update required | BLOCKED with reason |
| External evidence digest | N/A | no external corpus/provider evidence used | N/A with reason |
| System loop interlock | N/A | no new loop connection claimed | N/A with reason |
| Session continuity | active front door/handoff | sync after material commit if mode changes | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance control-plane hardening. No public-facing
catalog, README, or public-sync update is authorized in this batch.

## Claim Boundary

This work order proves active-session JSON authoring hardening only. It does
not prove semantic correctness of every historical state value, Policy_Local
readiness, public readiness, production readiness, OCR/provider behavior, or
autonomous mutation.
