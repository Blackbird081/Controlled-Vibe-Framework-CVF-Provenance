# CVF GC-018 - Active Session State JSON Authoring Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-12

Owner: Codex

## Purpose

Authorize a bounded control-plane hardening batch for
`CVF_SESSION/ACTIVE_SESSION_STATE.json` after GC-051 showed that large
agent-edited JSON aggregates are easy to break or stale.

## Authority Chain

Operator direction: proceed with strengthening `ACTIVE_SESSION_STATE.json` and
standardize JSON usage before moving into the Policy_Local use case.

Governance standards:

- `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md`
- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`

## Objective

Make `CVF_SESSION/ACTIVE_SESSION_STATE.json` a generated aggregate from a
compact core source and per-entry state sources, then enforce aggregate drift
in the active session checker.

## Decision / Baseline / Proposed Tranche

Decision: close this as a single bounded CVF foundation hardening tranche.

Baseline: before this batch, active session state was a monolithic JSON file
edited directly by agents. Syntax was checked, but source/aggregate drift and
review blast radius were not controlled.

Proposed tranche: add source files under `CVF_SESSION/state/`, a deterministic
generator, focused tests, active-session drift validation, and a general JSON
generated aggregate discipline standard.

## Bounded Scope

Allowed:

- add `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`;
- add per-entry source JSON files under `CVF_SESSION/state/entries/`;
- add `governance/compat/generate_active_session_state.py`;
- add focused unit tests;
- wire drift validation into `check_active_session_state.py`;
- update `AGENTS.md` and add a general JSON generated aggregate standard;
- correct the stale `nextAllowedMove` source entry to match the active
  front-door/handoff PL-S1 boundary.

Forbidden:

- do not change active session semantics beyond correcting stale
  `nextAllowedMove`;
- do not mutate Policy_Local or the external cloned `dich-tai-lieu` repo;
- do not activate EC, retrieval, OCR, provider/API proof, corpus ingestion,
  public-sync, T12, readiness claims, memory reinjection, high-risk promotion,
  or autonomous mutation.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Active session aggregate exists | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | top-level object | `activeHandoff`, `currentMode`, `nextAllowedMove` | active session state registry | ACCEPT |
| Active session checker exists | `governance/compat/check_active_session_state.py` | module constants and `_classify` | `STATE_PATH`, `_load_state`, `_classify` | active session state gate | ACCEPT |
| Front-door state route exists | `CVF_SESSION_MEMORY.md` | Startup Order / Current State | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | session memory front door | ACCEPT |
| Active handoff route exists | `AGENT_HANDOFF_V18_2026-06-12.md` | Startup Acknowledgment / Current Mode | `gc051_registry_authoring_hardening_closed_pass_bounded` | active handoff | ACCEPT |

## JSON Layout Disposition

`GENERATED_SOURCE_LAYOUT_ADDED`

Source layout:

- core source: `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`;
- per-entry sources: `CVF_SESSION/state/entries/*.json`;
- aggregate: `CVF_SESSION/ACTIVE_SESSION_STATE.json`;
- generator: `governance/compat/generate_active_session_state.py`.

## Closure Summary

Completion evidence is recorded in:

`docs/reviews/CVF_ACTIVE_SESSION_STATE_JSON_AUTHORING_HARDENING_COMPLETION_2026-06-12.md`

## Evidence / Verification

Required closure evidence:

- active-state generator check PASS;
- active session checker PASS;
- focused unit tests PASS;
- reviewer-fast PASS before closure.

## Claim Boundary

This proves active-state JSON authoring and drift-control hardening only. It
does not prove semantic correctness of historical state values, runtime
behavior, provider behavior, Policy_Local readiness, public readiness,
production readiness, or autonomous mutation.
