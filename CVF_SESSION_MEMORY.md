# ACTIVE SESSION FRONT DOOR

Memory class: active-session-front-door
Status: ACTIVE
Last compacted: 2026-06-26

## Startup Order

Read these files before governed material work:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V23_2026-06-26.md`
5. `docs/reference/guard_orientation/README.md`

For governed artifact authoring, also read:

`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

## Active Pointers

| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V23_2026-06-26.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Front-door archive snapshot | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-26.md` |

## Startup Acknowledgment

Startup acknowledged: current mode=`assf_web_projection_implementation_dispatched_pending_execution`; active handoff=AGENT_HANDOFF_V23_2026-06-26.md; next allowed move=execute ASSF Web projection implementation work order as no-commit worker; parked checkpoint=no ASSF registry/generated-index source mutation, resolver mutation, adapter, public-sync, push, package instance, certification decision, lifecycle mutation, provider/live proof, activation, package execution, package integration, or session-sync inside material implementation.

## Current Mode

Current mode marker: `assf_web_projection_implementation_dispatched_pending_execution`

Current mode: `assf_web_projection_implementation_dispatched_pending_execution`

`assf_web_projection_implementation_dispatched_pending_execution`

Previous mode:

`assf_web_projection_schema_mapping_decision_closed_pass_bounded_pending_web_projection_implementation_work_order`

## Latest Closed Work

| Work | Commit | Disposition |
|---|---|---|
| Orchestration command catalog refactor | `10dee6e9` | CLOSED_PASS_BOUNDED |
| Orchestration session sync | `f73546c5` | CLOSED_PASS |
| Guard binding catalog-aware checker hardening | `4927687c` | CLOSED_PASS_BOUNDED |
| ASSF Web projection schema/mapping dispatch | `b233ad46` | DISPATCH_READY |
| ASSF Web projection schema/mapping decision | `a408c13e` | CLOSED_PASS_BOUNDED |
| ASSF Web projection implementation dispatch | `0ba6eaee` | DISPATCH_READY |

## Next Allowed Move

Mode: `assf_web_projection_implementation_dispatched_pending_execution`

Next allowed move: execute `docs/work_orders/CVF_AGENT_WORK_ORDER_ASSF_WEB_PROJECTION_IMPLEMENTATION_FOR_CODEX_2026-06-26.md` as Codex no-commit worker, record actual worker-start `executionBaseHead`, implement only within Write Ownership, create `docs/reviews/CVF_ASSF_WEB_PROJECTION_IMPLEMENTATION_WORKER_RETURN_2026-06-26.md`, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` for reviewer closure. LHW24 remains the latest closed numbered LHW wave.

No ASSF registry-source mutation, ASSF generated-index source mutation, resolver mutation, package instance creation, certification decision, lifecycle mutation, CLI/MCP adapter behavior, provider/live proof, public-sync, push, activation, package instruction execution, package integration, or session-sync inside the material implementation range is authorized by this front door.

## Parked Checkpoint

ASSF Web projection implementation work order is dispatched. Certification, adapter, provider/live, package execution, public-sync, and session-sync remain parked outside the material implementation range.

## Continuity Markers

| Field | Value |
|---|---|
| Freeze posture | `governance_kernel_freeze_recommended` |
| Pain-point closure direction | `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` |
| Latest closed LHW wave | `LHW24` |

## Maintainability Note

This front door is intentionally compact. Long continuity history was archived to:

`CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-26.md`

Do not append long status history here. Update compact pointers, generated session state sources, and the active handoff instead.

## Claim Boundary

This file is a startup pointer surface only. Complete canonical state lives in `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
