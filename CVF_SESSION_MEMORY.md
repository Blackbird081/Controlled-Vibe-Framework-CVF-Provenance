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

Startup acknowledged: current mode=`assf_web_projection_schema_mapping_decision_closed_pass_bounded_pending_web_projection_implementation_work_order`; active handoff=AGENT_HANDOFF_V23_2026-06-26.md; next allowed move=open ASSF Web projection implementation GC-018 and source-verified work order; parked checkpoint=no direct Web runtime/source mutation, adapter, public-sync, push, package instance, certification decision, generated-index mutation, resolver mutation, or package execution without a new work order.

## Current Mode

Current mode marker: `assf_web_projection_schema_mapping_decision_closed_pass_bounded_pending_web_projection_implementation_work_order`

Current mode: `assf_web_projection_schema_mapping_decision_closed_pass_bounded_pending_web_projection_implementation_work_order`

`assf_web_projection_schema_mapping_decision_closed_pass_bounded_pending_web_projection_implementation_work_order`

Previous mode:

`assf_web_projection_schema_mapping_decision_dispatched_pending_execution`

## Latest Closed Work

| Work | Commit | Disposition |
|---|---|---|
| Orchestration command catalog refactor | `10dee6e9` | CLOSED_PASS_BOUNDED |
| Orchestration session sync | `f73546c5` | CLOSED_PASS |
| Guard binding catalog-aware checker hardening | `4927687c` | CLOSED_PASS_BOUNDED |
| ASSF Web projection schema/mapping dispatch | `b233ad46` | DISPATCH_READY |
| ASSF Web projection schema/mapping decision | `a408c13e` | CLOSED_PASS_BOUNDED |

## Next Allowed Move

Mode: `assf_web_projection_schema_mapping_decision_closed_pass_bounded_pending_web_projection_implementation_work_order`

Next allowed move: open a fresh GC-018 baseline and source-verified work order for Web projection implementation, using `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_2026-06-26.md` and `docs/reviews/CVF_ASSF_WEB_PROJECTION_SCHEMA_MAPPING_DECISION_COMPLETION_2026-06-26.md` as decision evidence. LHW24 remains the latest closed numbered LHW wave.

No direct Web runtime/source mutation, package instance creation, certification decision, lifecycle mutation, registry-source mutation, generated-index mutation, resolver source mutation, CLI/MCP adapter behavior, provider/live proof, public-sync, push, activation, package instruction execution, package integration, or implementation without a new work order is authorized by this front door.

## Parked Checkpoint

ASSF Web projection decision-first tranche is closed. Implementation remains parked until a fresh GC-018 baseline and source-verified work order are opened.

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
