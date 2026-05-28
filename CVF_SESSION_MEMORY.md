# CVF Session Memory Front Door

Memory class: POINTER_RECORD

Status: ACTIVE SESSION FRONT DOOR

Last updated: 2026-05-28

Current mode marker: `agent_autorun_workflow_control_enforced`
Freeze posture marker: `governance_kernel_freeze_recommended`

---

## Purpose

This file is the compact startup front door for new or resumed CVF agents.
It intentionally points to canonical state instead of carrying long history.

Previous long front-door snapshot:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_PRE_ROTATION_ARCHIVE_2026-05-28.md`

## Startup Order

1. Read this file.
2. Resolve machine-readable state:
   `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. Resolve review queue:
   `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
4. Resolve active handoff from the state registry:
   `AGENT_HANDOFF_V14_2026-05-27.md`
5. Read mandatory startup guards listed in the state registry.

## Current State

Current mode: `agent_autorun_workflow_control_enforced`.

Active handoff:

`AGENT_HANDOFF_V14_2026-05-27.md`

Active state registry:

`CVF_SESSION/ACTIVE_SESSION_STATE.json`

Active review queue:

`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`

Pain-point closure direction:

`docs/reviews/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md`

## Active Rule Additions

Work-order dispatch quality is machine-enforced by:

`governance/compat/check_work_order_dispatch_quality.py`

Governed file-size maintainability now requires proactive rotation/splitting
instead of last-minute text compression when active governed files approach
hard thresholds.

This applies to broad external knowledge absorption records, session front
doors, handoffs, reviews, work orders, and other blocked work classes that
would become hard to test or review if oversized.

Canonical size guard:

`governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md`

Agent autorun workflow control is mandatory for governed work phases. Agents
must pass the phase wrapper before dispatch, implementation, closure, or push:

`governance/compat/run_agent_autorun_workflow_gate.py`

Canonical autorun standard:

`docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`

Autorun gates are now range-aware. Governed closure must use a captured
`baseHead` and a non-empty committed range; `--base HEAD --head HEAD` is not
valid closure evidence for changed artifacts. Source Verification false
invariants require literal source proof or runtime-path proof.

## Next Allowed Move

LHW6 is present in HEAD as `CLOSED_PASS_BOUNDED` and any follow-on wave must be
reviewed through the autorun `pre-dispatch`, `pre-implementation`, and
`pre-closure` gates before it can be trusted as closed.

Future connector waves require fresh GC-018, roadmap, source-verified work
orders, roadmap-to-work-order trace matrix, dispatch-quality gate, closure
quality gate, and governed file-size maintainability planning.

Parked checkpoints:

- VI5-T4/T5 hosted Netlify freshness and operator external-agent retest
- Delta production hardening for MCP/client memory direction

## Claim Boundary

This front door is a pointer record only. It does not prove runtime behavior,
provider behavior, hosted freshness, public readiness, production readiness, or
automatic loading by external agents.
