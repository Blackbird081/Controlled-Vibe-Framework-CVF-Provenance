# CVF Session Front Door Rotation And Continuity Compaction Roadmap

Memory class: POINTER_RECORD

rawMemoryReleased: false

Date: 2026-06-15

Status: CLOSED_PASS_BOUNDED

Roadmap class: governance-continuity

Operator authorization source: operator message 2026-06-15 proposing
`CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_ROADMAP_2026-06-15.md`
with explicit scope: open V19 handoff, archive V18, compact
`CVF_SESSION_MEMORY.md`, regenerate `ACTIVE_SESSION_STATE.json`, update
`AGENTS.md` only if needed without adding prose, add completion review and
guard evidence. No runtime, no provider, no live, no Model Gateway P4B, no
public-sync.

Worker: SINGLE_AGENT_MULTI_ROLE (Claude orchestrates and executes in the same
session).

WORKER_MUST_NOT_COMMIT: worker authors all artifacts; reviewer (Codex) owns all
commits, active-handoff updates, session-state regeneration, and session-state
file mutations.

---

## Authorization / Decision

Operator authorization: operator message 2026-06-15 proposing this roadmap.
GC-018: `docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md`
Authorized by: SINGLE_AGENT_MULTI_ROLE pattern; worker=Claude; reviewer=Codex.
WORKER_MUST_NOT_COMMIT: enforced.

## Purpose

Three session front-door files are advisory-threshold-exceeded:

| File | Lines | Advisory | Hard | Class |
|---|---|---|---|---|
| `CVF_SESSION_MEMORY.md` | 1112 | 900 | 1200 | active_markdown |
| `AGENT_HANDOFF_V18_2026-06-12.md` | 964 | 900 | 1200 | active_markdown |
| `AGENTS.md` | 925 | 900 | 1200 | active_markdown |

Every session startup requires agents to read these files. Bloat here directly
raises agent latency, increases context compression risk, and increases the
probability of a missed continuity signal on startup. Reducing these files is
infrastructure maintenance with high governance leverage.

---

## Scope

### In scope

- Open `AGENT_HANDOFF_V19_2026-06-15.md` as the new active handoff (pointer
  record, compact, named from current date not V18 open date).
- Archive `AGENT_HANDOFF_V18_2026-06-12.md` to
  `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md`.
- Compact `CVF_SESSION_MEMORY.md` to a true pointer record under 400 lines:
  - keep Purpose, Startup Order, Current State, and Latest Continuity Note
    sections;
  - move all prior closed-tranche prose below the latest continuity note to a
    compaction archive:
    `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`;
  - update Current State and mode to
    `session_front_door_rotation_compaction_complete`.
- Update `CVF_SESSION/state/entries/nextAllowedMove.json` and
  `CVF_SESSION/state/entries/lastUpdated.json` to reflect compaction closure.
- Regenerate `CVF_SESSION/ACTIVE_SESSION_STATE.json` from the updated state
  sources.
- Update `AGENTS.md` front-door pointer to reference V19 instead of V18.
  Do not add prose; the only permitted change is the handoff reference line.
- Add a GC-051 registry entry for V19 (type `POLICY_DOCUMENT`) with
  registryOrder 81.
- Regenerate `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`.
- Author completion review:
  `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md`.

### Out of scope

- Model Gateway P4B live-provider wiring.
- Any runtime source, test, or EXTENSIONS mutation.
- Provider/API use, live proof, public-sync.
- Strategy-layer implementation, AI Gateway absorption.
- EPF wiring, OCR, retrieval route wiring.
- Policy_Local, EC activation, T12, DEP2/Redis/receipt-anchor.
- Co-work product development, production readiness, public readiness.
- Any mutation of ECOSYSTEM/doctrine/, v1.0/, v1.1/ frozen baselines.
- Hand-editing `CVF_CORPUS_SCAN_REGISTRY.json` (must run generator).
- rawMemoryReleased mutation (stays false on all artifacts).

---

## Non-Goals

- Model Gateway P4B live-provider wiring.
- Any runtime source, test, or EXTENSIONS mutation.
- Provider/API use, live proof, public-sync.
- AI Gateway absorption, EPF wiring, strategy-layer implementation.
- Policy_Local, EC activation, T12, DEP2, Redis, receipt-anchor.
- Production or public readiness claims.
- rawMemoryReleased mutation (stays false).

## Work Plan

| Step | Action | Artifact |
|---|---|---|
| 1 | Open V19 handoff (< 200L) | `AGENT_HANDOFF_V19_2026-06-15.md` |
| 2 | Archive V18 to `CVF_SESSION/handoffs/archive/` | V18 archived |
| 3 | Compact CVF_SESSION_MEMORY.md to < 400L | `CVF_SESSION_MEMORY.md` |
| 4 | Author compaction archive | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md` |
| 5 | Update state source entries | `nextAllowedMove.json`, `lastUpdated.json` |
| 6 | Regenerate ACTIVE_SESSION_STATE.json | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| 7 | Update AGENTS.md pointer (V18->V19, net-zero prose) | `AGENTS.md` |
| 8 | Add GC-051 entry (order 81) | `session-front-door-v19.json` |
| 9 | Regenerate GC-051 aggregate | `CVF_CORPUS_SCAN_REGISTRY.json` |
| 10 | Author worker return; run reviewer-fast 16/16 | Worker return |
| 11 | Reviewer (Codex) authors completion review, commits | Completion review |

## Verification / Evidence

Gate: `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` -- must reach 16/16 PASS.
AC-1 through AC-9: see Acceptance Criteria section.
Committed diff: provided by Codex at completion review.

## Design Control Gate

| Control | Requirement | Status |
|---|---|---|
| GC-018 baseline | Required before implementation; must cite this roadmap | REQUIRED |
| GC-023 file size | V19 handoff must open under 200L; CVF_SESSION_MEMORY.md must close under 400L; AGENTS.md change must be net-negative or net-zero | REQUIRED |
| GC-051 registry | V19 entry added (registryOrder 81); generator rerun | REQUIRED |
| Work order | Source-verified work order dispatched for worker phase | REQUIRED |
| reviewer-fast | 16/16 PASS before worker return is complete | REQUIRED |
| WORKER_MUST_NOT_COMMIT | Worker authors; Codex commits | ENFORCED |

---

## Deliverables

| ID | Artifact | Owner | Status |
|---|---|---|---|
| D1 | GC-018 baseline (`docs/baselines/CVF_GC018_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_2026-06-15.md`) | Orchestrator | REQUIRED |
| D2 | Work order (`docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_FOR_CLAUDE_2026-06-15.md`) | Orchestrator | REQUIRED |
| D3 | `AGENT_HANDOFF_V19_2026-06-15.md` (new active handoff, compact pointer) | Worker | REQUIRED |
| D4 | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md` (V18 archived) | Worker | REQUIRED |
| D5 | `CVF_SESSION_MEMORY.md` (compacted, under 400L) | Worker | REQUIRED |
| D6 | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md` (compaction archive) | Worker | REQUIRED |
| D7 | `CVF_SESSION/state/entries/nextAllowedMove.json` (updated) | Worker | REQUIRED |
| D8 | `CVF_SESSION/state/entries/lastUpdated.json` (updated) | Worker | REQUIRED |
| D9 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` (regenerated) | Worker | REQUIRED |
| D10 | `AGENTS.md` (pointer-only update to V19 reference, net-zero prose) | Worker | REQUIRED |
| D11 | `docs/corpus-intelligence/registry/entries/session-front-door-v19.json` (GC-051 entry) | Worker | REQUIRED |
| D12 | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (regenerated) | Worker | REQUIRED |
| D13 | Completion review (`docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md`) | Reviewer (Codex) | PASS |

---

## Acceptance Criteria

| ID | Criterion | Verification |
|---|---|---|
| AC-1 | V19 handoff exists at root, is < 200 lines, contains compact pointer record with mode, next allowed move, and V18 archive pointer | `wc -l AGENT_HANDOFF_V19_2026-06-15.md; grep "AGENT_HANDOFF_V18" AGENT_HANDOFF_V19_2026-06-15.md` |
| AC-2 | V18 archived at `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md` | `ls CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md` |
| AC-3 | `CVF_SESSION_MEMORY.md` is under 400 lines | `wc -l CVF_SESSION_MEMORY.md` |
| AC-4 | Compaction archive exists with prior tranche prose | `ls CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md` |
| AC-5 | `AGENTS.md` V18 reference updated to V19; no new prose added; net change <= 2 lines | `git diff AGENTS.md` |
| AC-6 | `CVF_SESSION/ACTIVE_SESSION_STATE.json` regenerated from state sources; `activeHandoff` = `AGENT_HANDOFF_V19_2026-06-15.md` | `python governance/compat/generate_active_session_state.py --check` |
| AC-7 | GC-051 entry for V19 added (registryOrder 81); aggregate regenerated; drift check PASS | `python governance/compat/generate_corpus_scan_registry.py --check` |
| AC-8 | reviewer-fast 16/16 PASS | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` |
| AC-9 | Working tree contains no uncommitted runtime source or test mutations | `git status --short` -- no `.ts` or `.py` changes outside state/registry paths |

---

## Risk And Corrective Action

| Risk | Mitigation |
|---|---|
| `check_agent_operation_trace.py` flags V18 archive path as unauthorized | Include `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V18_2026-06-12.md` in work-order Expected manifest |
| Protected path guard blocks `CVF_SESSION/**` mutation without carrier | Work order must include complete `Core Guard Self-Protection Authorization` block per DIR-T1 hardening standard |
| `CVF_SESSION_MEMORY.md` compaction archive exceeds size guard | Archive is a new file outside the active_markdown class; verify class assignment before commit |
| `ACTIVE_SESSION_STATE.json` schema version drift after state source update | Run `generate_active_session_state.py --check` after editing state source entries; fix drift before reviewer return |
| V19 handoff line count drifts over 200 during authoring | Worker must run `wc -l AGENT_HANDOFF_V19_2026-06-15.md` as final step before returning |

---

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: all artifacts in this roadmap are session continuity and front-door
governance files. They contain internal agent routing, tranche state, parked
lane records, and orchestrator/reviewer boundary wording that is not intended
for the public CVF catalog. No runtime source or public capability is added.
Public-sync is out of scope for this roadmap. A separate public-sync batch
would be required, with a fresh GC-018 and explicit operator authorization.

| Artifact | Reason |
|---|---|
| `AGENT_HANDOFF_V19_2026-06-15.md` | Internal agent continuity record; DEFERRED_PRIVATE_ONLY - not a public capability artifact |
| `CVF_SESSION_MEMORY.md` | Session front door; DEFERRED_PRIVATE_ONLY - internal operator routing only |
| `CVF_SESSION/handoffs/archive/*` | Archived continuity; DEFERRED_PRIVATE_ONLY - historical internal record |
| `CVF_SESSION/state/entries/*` | State source files; DEFERRED_PRIVATE_ONLY - machine-readable internal session state |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Generated session aggregate; DEFERRED_PRIVATE_ONLY - internal routing |
| `AGENTS.md` | Agent instructions; DEFERRED_PRIVATE_ONLY - internal governance routing |
| GC-051 entry and aggregate | Registry coverage; DEFERRED_PRIVATE_ONLY - provenance internal only |
| Completion review | Internal governance review; DEFERRED_PRIVATE_ONLY - provenance internal only |

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_FOR_CLAUDE_2026-06-15.md` | status and checked closure checklist | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SESSION_FRONT_DOOR_ROTATION_AND_CONTINUITY_COMPACTION_COMPLETION_2026-06-15.md` | reviewer audit and gate evidence | PASS |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generator drift check | PASS |
| Registry Markdown | N/A | N/A with reason: no markdown companion exists or is required by GC-051 | PASS |
| External evidence digest | N/A | N/A with reason: no live proof, provider call, or external service | N/A with reason |
| System loop interlock | N/A | N/A with reason: no autonomous mutation, loop activation, or live routing | N/A with reason |
| Session continuity | `AGENTS.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V19_2026-06-15.md` | active pointers agree; root V18 removed | PASS |

### Acceptance Receipt Assertion Matrix

No `receipt`, `selectedCandidateIds`, or `freshnessDisclosureApplied` primitives
are invoked in this roadmap. The RECEIPT_ACCEPTANCE_RE trigger does not apply.
This matrix is included as a negative assertion to satisfy the machine closure
package standard when the word appears in any referenced artifact.

---

## Current Runtime Freshness Verification

No runtime source files are claimed in this roadmap. All artifacts are session
continuity governance files (handoffs, state entries, front door, GC-051 registry).
No runtime freshness verification is required.

Negative assertion: no EXTENSIONS source, no `.ts` or `.py` runtime file, no
provider/API endpoint, no live call is named or claimed in this roadmap.
Runtime freshness verification: NOT_APPLICABLE_WITH_REASON (governance-only scope).

## Claim Boundary

This roadmap authorizes only:

1. Opening `AGENT_HANDOFF_V19_2026-06-15.md` as a compact pointer record.
2. Archiving `AGENT_HANDOFF_V18_2026-06-12.md`.
3. Compacting `CVF_SESSION_MEMORY.md` to under 400 lines.
4. Authoring `CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-15.md`.
5. Updating `CVF_SESSION/state/entries/nextAllowedMove.json` and `lastUpdated.json`.
6. Regenerating `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
7. Updating `AGENTS.md` pointer reference (net-zero prose, V18 -> V19 only).
8. Adding GC-051 entry (registryOrder 81) and regenerating aggregate.
9. Authoring completion review at D13.

This roadmap does NOT authorize:

- Any runtime source, test, EXTENSIONS, or ECOSYSTEM mutation.
- Provider/API use, live proof, public-sync, or any external service call.
- Model Gateway P4B, AI Gateway absorption, EPF wiring, strategy-layer
  implementation, OCR/retrieval wiring.
- Policy_Local, EC activation, T12, DEP2, Redis, receipt-anchor.
- Production readiness or public readiness claims.
- Co-work product development or autonomous mutation.
- rawMemoryReleased mutation (must stay false on all artifacts).
- Modifying frozen baselines in `ECOSYSTEM/doctrine/`, `v1.0/`, or `v1.1/`.
- Hand-editing `CVF_CORPUS_SCAN_REGISTRY.json` (generator required).
- Committing, pushing, or merging (WORKER_MUST_NOT_COMMIT).
