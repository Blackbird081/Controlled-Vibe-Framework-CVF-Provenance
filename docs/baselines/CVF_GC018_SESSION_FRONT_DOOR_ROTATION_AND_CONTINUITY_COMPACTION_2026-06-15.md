# GC-018 Continuation Governance Baseline

Memory class: POINTER_RECORD

rawMemoryReleased: false

Baseline ID: GC018-SESSION-FRONT-DOOR-ROTATION-COMPACTION-2026-06-15

Date: 2026-06-15

Status: AUTHORIZED

Authorized by: operator message 2026-06-15 proposing session front door rotation
and continuity compaction roadmap.

## Purpose

Baseline authorizing Session Front Door Rotation And Continuity Compaction:
open V19 handoff, archive V18, compact CVF_SESSION_MEMORY.md, update state
sources, regenerate ACTIVE_SESSION_STATE.json, update AGENTS.md pointer, add
GC-051 entry, and regenerate corpus scan registry.

## Scope / Target / Owner Boundary

Target: session continuity files only. No runtime, no EXTENSIONS, no live proof.
Owner: Claude (worker) authors artifacts; Codex (reviewer) commits.

## Source / Predecessor Evidence

Prior active handoff: `AGENT_HANDOFF_V18_2026-06-12.md` (current, 964L, advisory-exceeded).
Prior CVF_SESSION_MEMORY.md: 1112L (advisory-exceeded).
Prior AGENTS.md: 925L (advisory-exceeded).
All three files exceed advisory threshold 900 for class `active_markdown`.
File size guard evidence: `python governance/compat/check_governed_file_size.py --json`.

## Decision / Baseline / Proposed Tranche

Decision: authorize Session Front Door Rotation And Continuity Compaction.
Tranche scope: V19 handoff + V18 archive + CVF_SESSION_MEMORY.md compaction +
state source updates + ACTIVE_SESSION_STATE.json regeneration + AGENTS.md
pointer update + GC-051 entry (order 81) + aggregate regeneration.
No subsequent tranches authorized in this baseline.

## Evidence / Verification

Planning authority: `docs/roadmaps/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_ROADMAP_2026-06-15.md`

Prior active handoff: `AGENT_HANDOFF_V18_2026-06-12.md`

Current HEAD at baseline: `c7d3d955`

Worker assignment: SINGLE_AGENT_MULTI_ROLE (Claude orchestrates and implements;
Codex reviews and commits).

WORKER_MUST_NOT_COMMIT: enforced.

---

## Authorized Scope

1. Open `AGENT_HANDOFF_V19_2026-06-15.md` as new active compact handoff
   (pointer record, target < 200 lines).
2. Archive `AGENT_HANDOFF_V18_2026-06-12.md` to
   `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`.
3. Compact `CVF_SESSION_MEMORY.md` to under 400 lines; move prior closed-tranche
   prose to `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`.
4. Update `CVF_SESSION/state/entries/nextAllowedMove.json` and `lastUpdated.json`.
5. Regenerate `CVF_SESSION/ACTIVE_SESSION_STATE.json` via
   `governance/compat/generate_active_session_state.py`.
6. Update `AGENTS.md` handoff reference from V18 to V19 only; no prose added.
7. Add GC-051 entry `docs/corpus-intelligence/registry/entries/session-front-door-v19.json`
   (registryOrder 81); regenerate `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`.
8. Author completion review at
   `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md`
   (reviewer Codex).

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Claude (worker) may author the new V19
handoff, archive V18, compact CVF_SESSION_MEMORY.md, update state source
entries, and update the AGENTS.md pointer. Codex (reviewer) may regenerate
ACTIVE_SESSION_STATE.json, regenerate the GC-051 aggregate, commit all changes,
and author the completion review.

Protected paths (worker must include in work-order Expected manifest):

- `AGENT_HANDOFF_V19_2026-06-15.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/lastUpdated.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENTS.md`
- `docs/corpus-intelligence/registry/entries/session-front-door-v19.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md`

Rollback boundary: if session-sync gates fail, revert only this compaction batch.
Do not revert Model Gateway C-02 P3/P4A material closure commit `5d46bc62`,
commit steward hardening commit `a31f32a9`, latency hardening commits
`83fbb6a4`/`c7d3d955`, or any prior closed tranche.

Operator authorization: explicit. Scope locked to continuity compaction only.

## Not Authorized

- Runtime source, test, or EXTENSIONS mutation.
- Provider/API use, live proof, public-sync.
- Model Gateway P4B, AI Gateway absorption, EPF wiring, strategy-layer.
- Policy_Local, EC activation, T12, DEP2, Redis, receipt-anchor.
- Production readiness or public readiness claims.
- rawMemoryReleased mutation (stays false on all artifacts).
- Committing, pushing, or merging (WORKER_MUST_NOT_COMMIT).

Verification: reviewer-fast 16/16 PASS after worker phase completion.
Closure evidence: committed diff, git status, gate output in completion review.

## Claim Boundary

This baseline authorizes only the compaction scope listed above. It does not
authorize runtime source changes, live proof, public-sync, provider use, or any
other governed tranche not named here.
