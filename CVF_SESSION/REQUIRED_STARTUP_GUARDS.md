# CVF Required Startup Guards

Memory class: POINTER_RECORD

Status: ACTIVE STARTUP GUARD ROUTER

## Purpose

This file lists the guard set that a new or resumed agent must route through
before material governed work in the current reconvergence session.

## Owner And Source

Owner: CVF governance/session-continuity surface.

Source truth:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- GC-020, GC-022, GC-025, and GC-032 guard surfaces

## Scope Boundary

In scope:

- startup guard routing
- required acknowledgment for new/resumed agents
- current stop-boundary reminder

Out of scope:

- changing guard semantics
- replacing the canonical guard documents
- implementing runtime orchestration

## Required Guard Surfaces

| Guard or surface | Purpose |
|---|---|
| `CVF_SESSION_MEMORY.md` | Single front door for active session state. |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable active handoff, first-read, blocked-class, and next-move registry. |
| `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` | Machine-readable review intake queue for ambiguous roadmap/review requests. |
| `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md` | Current steering source for post-pain-point CVF hardening. |
| `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` | Closure evidence for Review-CVF A-H pain-point status. |
| `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md` | Session-start governance routing. |
| `governance/toolkit/05_OPERATION/CVF_SESSION_GOVERNANCE_BOOTSTRAP_GUARD.md` | GC-025 bootstrap rule. |
| `governance/toolkit/05_OPERATION/CVF_AGENT_HANDOFF_TRANSITION_GUARD.md` | GC-020 transition classification before writing or trusting handoffs. |
| `governance/toolkit/05_OPERATION/CVF_AGENT_HANDOFF_GUARD.md` | GC-020 handoff content and continuity requirements. |
| `governance/toolkit/05_OPERATION/CVF_MEMORY_GOVERNANCE_GUARD.md` | GC-022 durable memory, evidence, and continuity boundary. |
| `governance/toolkit/05_OPERATION/CVF_GOVERNED_ARTIFACT_AUTHORING_GUARD.md` | GC-032 governed artifact authoring and source-truth rules. |
| `governance/toolkit/05_OPERATION/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_GUARD.md` | GC-047 manifest, terminal-ledger, reconciliation, and honest-verdict rules for bounded corpus tasks. |
| `governance/toolkit/05_OPERATION/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_GUARD.md` | GC-048 authority/derived-view, semantic-region, orphan, drift, rebuildability, and retrieval-boundary rules for corpus-derived knowledge maps. |

## Protocol Requirements

1. Resolve the active state registry before choosing guard depth.
2. Load the guards listed here only as triggered by task class and current mode.
3. Preserve the active state registry boundary until superseded.
4. Record or internally confirm the required acknowledgment before material
   governed work.

## Required Acknowledgment

Before material governed work, state or internally confirm:

- active session mode
- active handoff path
- post-pain-point hardening roadmap
- required first-read packet set
- blocked work classes
- next allowed move

## Current Stop Boundary

The current mode is
`gc048_knowledge_system_foundation_closed_pass_bounded`.

GC-048 Knowledge System foundation is closed. `LHW-RESCAN-A` may open only
with a fresh GC-018 packet, GC-047 corpus evidence, and GC-048 reconciliation
evidence. New runtime contracts and public claims of coherent governed
capability runtime remain blocked unless separately authorized.

## Enforcement And Verification

Machine check:

- `python governance/compat/check_active_session_state.py --enforce`

## Related Artifacts

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`
- `CVF_SESSION/READ_FIRST.md`
- `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md`

## Claim Boundary

This artifact routes startup guard loading for the current reconvergence
session. It does not replace or supersede any guard it lists.
