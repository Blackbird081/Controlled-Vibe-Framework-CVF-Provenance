# CVF Session Read-First Router

Memory class: POINTER_RECORD

Status: ACTIVE READ-FIRST ROUTER

## Rule

Read `CVF_SESSION_MEMORY.md` first.

Then resolve:

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`

Only after that should an agent decide which versioned handoff, review packet,
roadmap, or guard to load.

## Purpose

Provide a minimal read-first router so agents, future `cvf-cli`, and future
`cvf-mcp-server` do not start by guessing between root handoffs or scattered
review packets.

## Owner And Source

Owner: CVF governance/session-continuity surface.

Source truth:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Scope Boundary

In scope:

- startup routing order
- layer separation between memory, handoff, review packets, and guards

Out of scope:

- authorizing new work
- replacing the active state registry
- replacing GC-020 or GC-025 controls

## Protocol Requirements

1. Start at `CVF_SESSION_MEMORY.md`.
2. Resolve `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
3. Resolve `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` before any ambiguous
   roadmap/review request.
4. Resolve the post-pain-point hardening roadmap before any new CVF hardening
   request.
5. Resolve the pain-point closure evidence before any A-H pain-point status
   request.
6. Load `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`.
7. Continue only through the current active state.

## Non-Substitution Rule

- `CVF_SESSION_MEMORY.md` is the front door.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` is the machine-readable pointer set.
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` is the machine-readable review intake
  queue for ambiguous roadmap/review requests.
- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`
  is the current steering source for post-pain-point CVF hardening.
- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`
  is closure evidence for Review-CVF A-H pain-point status.
- Root `AGENT_HANDOFF*.md` files are transition records.
- Review packets remain evidence and reasoning records.
- Governance guards remain rules.

Do not use any one of these layers as a substitute for the others.

## Enforcement And Verification

Machine check:

- `python governance/compat/check_active_session_state.py --enforce`

## Boundaries And Non-Goals

- This file is a router, not an evidence packet.
- This file is not the complete session memory state.
- This file does not make any root handoff current by filename alone.

## Related Artifacts

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `docs/roadmaps/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`
- `docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`
- `CVF_SESSION/REQUIRED_STARTUP_GUARDS.md`
- `docs/reference/CVF_SESSION_GOVERNANCE_BOOTSTRAP.md`

## Claim Boundary

This artifact only defines the read-first order for session startup.
