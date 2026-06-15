# CVF Session Continuity Authoring And Mode-Consistency Foundation Roadmap

Memory class: FULL_RECORD

rawMemoryReleased: false

Date: 2026-06-16

Status: ROADMAP_READY_FOR_GC018

Owner: Codex orchestrator

Worker target: Codex

## Purpose

Session-sync is the single largest recurring governance cost in CVF: 59 of the
last 120 commits (49 percent) are session-sync or handoff-sync commits, each
touching 5-7 protected session/handoff files by hand. Two foundation gaps make
this worse than it needs to be:

1. No checker verifies that the session mode marker agrees across its three
   surfaces (front door, active handoff, `ACTIVE_SESSION_STATE_CORE.json`).
   This gap is not theoretical: a real `currentMode` drift was introduced and
   passed all 16 reviewer-fast checks plus pre-commit plus the session-sync
   steward, and was only caught by a manual audit. It was repaired in commit
   `7df9679d`.

2. Session-sync content is authored entirely by hand. The existing
   `build_session_sync_pack.py` reports the protected-path manifest and drift
   (read-only), but the agent still hand-writes every state entry, the
   `nextAllowedMove` update, and the mode marker in three places.

This roadmap closes both gaps as bounded, read-only/authoring governance
foundation that lowers latency for every agent regardless of model.

## Audit Position

Audit of `governance/compat/check_active_session_state.py` line 366 shows the
checker only validates that `currentMode` is a non-empty string. It never
compares `currentMode` against the `Current mode marker:` line in the front
door or the `## Current Mode` value in the active handoff. The three surfaces
can therefore diverge silently.

Audit of `governance/compat/` shows `generate_active_session_state.py`
(regenerates the aggregate from entries) and `build_session_sync_pack.py`
(manifest + drift, read-only) are the only session-state helpers. Neither
authors new state-entry content, the `nextAllowedMove` update, or the
three-surface mode marker block.

## Authorization / Decision

Decision: proceed to GC-018 and Codex work order. Operator approved both parts
(mode-consistency checker + session-sync authoring helper) as the next CVF
foundation tranche after the session-sync pack builder closure.

## Scope

Two tranches, each bounded governance tooling:

- T1: mode-consistency checker that fails when the mode marker disagrees across
  the front door, active handoff, and `ACTIVE_SESSION_STATE_CORE.json`; wired
  into reviewer-fast and the session-sync steward.
- T2: session-sync authoring helper (new mode in `build_session_sync_pack.py`
  or a sibling read-only tool) that emits a paste-ready skeleton state entry
  with the next `stateOrder` and correct schema, a `nextAllowedMove` update
  template, and the three-surface mode marker block.

## Non-Goals

- Auto-writing session files, handoff mutations, or staged changes;
- changing `generate_active_session_state.py` aggregate behavior;
- live provider, runtime, or public-sync changes;
- co-work product development;
- production or public readiness claims.

## Design Boundary

T1 is a read-only validator. T2 is a read-only generator. Neither writes,
stages, or commits any file. All session-file writes remain the agent's
responsibility after reviewing generated content.

T1 must read the canonical marker locations only:

- front door `CVF_SESSION_MEMORY.md`: `Current mode marker:` and
  `Current mode:` lines;
- active handoff: `## Current Mode` value and the startup acknowledgment
  `current mode=` field;
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`: `currentMode`.

The active handoff path is resolved from `ACTIVE_SESSION_STATE.json`
`activeHandoff`, not hardcoded.

## Design Control Gate

T1 must not duplicate the active-session-state structural checks already in
`check_active_session_state.py`; it adds only the cross-surface marker
agreement check. T2 must not duplicate `build_path_plan` or
`validate_aggregate_matches_sources`; it reuses the existing imports from the
session-sync pack builder.

## Recommended Tranche

T1: Mode-Consistency Checker Foundation.

Codex should:

- author `governance/compat/check_session_mode_consistency.py` that compares
  the mode marker across the three canonical surfaces and exits non-zero on
  disagreement;
- add focused tests `governance/compat/test_check_session_mode_consistency.py`;
- wire the checker into `run_local_governance_hook_chain.py` reviewer-fast and
  into the session-sync lane of `run_agent_commit_steward_preflight.py`;
- author a completion review.

T2: Session-Sync Authoring Helper.

Codex should:

- add a `--author-entry` (or equivalent) read-only mode that prints a skeleton
  state entry with the next `stateOrder`, the `nextAllowedMove` update text,
  and the three-surface mode marker block;
- add focused tests;
- author a completion review.

T2 dispatch is held until T1 closes, because T1 defines the canonical marker
locations that T2 must emit.

## Work Plan

| Step | Work | Owner |
|---|---|---|
| 1 | Author T1 checker and tests | Codex |
| 2 | Wire T1 into reviewer-fast and session-sync steward | Codex |
| 3 | Close T1 with completion review | Codex |
| 4 | Author T2 helper mode and tests | Codex |
| 5 | Close T2 with completion review | Codex |

## Value Rationale

This improves CVF core for all agents. T1 closes a proven gate gap that let a
real mode drift pass every check. T2 attacks the 49 percent session-sync
commit overhead by giving every agent correct, schema-valid session-sync
content to paste instead of hand-authoring it. Both keep canonical authority
in governed files and machine gates, and neither depends on Claude, Codex, or
any single worker model.

## Scope Guard

Allowed:

- `governance/compat/check_session_mode_consistency.py` (new, read-only);
- `governance/compat/test_check_session_mode_consistency.py` (new);
- `governance/compat/run_local_governance_hook_chain.py` (additive wiring of
  the new checker only);
- `governance/compat/run_agent_commit_steward_preflight.py` (additive wiring
  into the session-sync lane only);
- `governance/compat/build_session_sync_pack.py` (T2: additive read-only mode);
- `governance/compat/test_build_session_sync_pack.py` (T2: additive tests);
- completion reviews.

Forbidden:

- auto-writing session files, handoff mutations, or staged changes;
- aggregate-generation behavior change;
- live API calls;
- co-work product or platform development;
- public-sync;
- production or public readiness claims.

## Acceptance Criteria

T1 is complete when the checker fails on a mode marker that disagrees across
the three surfaces, passes when they agree, is wired into reviewer-fast and the
session-sync steward, and has focused tests. T2 is complete when the authoring
helper prints a schema-valid skeleton state entry with the next `stateOrder`, a
`nextAllowedMove` update template, and the three-surface marker block, with
focused tests, and remains read-only.

## Verification / Evidence

Required evidence: focused checker/helper tests, reviewer-fast output, session-
sync steward output, diff hygiene, and completion reviews with Agent Operation
Trace Blocks.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 foundation roadmap audit after session-sync pack builder closure |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, governance gates |
| Target paths | roadmap only |
| Allowed scope source | operator approved mode-consistency + session-sync authoring foundation roadmap |
| Before status evidence | session-sync pack builder closed `a5e91d4b`; mode drift fixed `7df9679d`; HEAD `7df9679d` |
| After status evidence | roadmap ready for GC-018 |
| Diff evidence | roadmap authoring session 2026-06-16 |
| Approval boundary | roadmap authoring only; no source mutation |
| Claim boundary | no runtime/provider/public/production claim |
| Agent type | Codex orchestrator |
| Invocation ID | `session-continuity-authoring-mode-consistency-roadmap-2026-06-16` |
| Expected manifest | `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md` |
| Actual changed set | `docs/roadmaps/CVF_SESSION_CONTINUITY_AUTHORING_AND_MODE_CONSISTENCY_FOUNDATION_ROADMAP_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation planning. No public-sync batch is
authorized.

## Claim Boundary

This roadmap selects a governance/control-plane tooling tranche. It does not
prove implementation, runtime behavior, provider behavior, live governance
behavior, public readiness, production readiness, or co-work product
capability.
