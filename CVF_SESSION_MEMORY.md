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

Startup acknowledged: current mode=`foundation_plane_system_chain_gap_guidance_active_pending_fpc_scg_tranche_selection`; active handoff=AGENT_HANDOFF_V23_2026-06-26.md; next allowed move=open fresh GC-018/source-verified FPC system-chain gap roadmap or work order from `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md`; parked checkpoint=P0/P1 foundation system-chain gaps are highest priority and downstream runtime/use-case lanes remain parked; no registry edit, checker implementation, runtime/MCP/CLI/IDE bridge implementation, further provider/live proof, public-sync, resolver mutation, adapter mutation, package activation, certification decision, generated workspace state mutation, DICE work, MPI-T6 runtime work, or push without separate authorization.

## Current Mode

Current mode marker: `foundation_plane_system_chain_gap_guidance_active_pending_fpc_scg_tranche_selection`

Current mode: `foundation_plane_system_chain_gap_guidance_active_pending_fpc_scg_tranche_selection`

`foundation_plane_system_chain_gap_guidance_active_pending_fpc_scg_tranche_selection`

Previous mode:

`mpi_t5_current_state_reconciliation_closed_pass_bounded_pending_next_foundation_selection`

## Latest Closed Work

| Work | Commit | Disposition |
|---|---|---|
| Orchestration command catalog refactor | `10dee6e9` | CLOSED_PASS_BOUNDED |
| Orchestration session sync | `f73546c5` | CLOSED_PASS |
| Guard binding catalog-aware checker hardening | `4927687c` | CLOSED_PASS_BOUNDED |
| ASSF Web projection schema/mapping dispatch | `b233ad46` | DISPATCH_READY |
| ASSF Web projection schema/mapping decision | `a408c13e` | CLOSED_PASS_BOUNDED |
| ASSF Web projection implementation dispatch | `0ba6eaee` | DISPATCH_READY |
| ASSF Web projection implementation | `0b57a4de` | CLOSED_PASS_BOUNDED |
| ASSF external-agent readout / CLI-MCP adapter boundary | `99fabd26` | CLOSED_PASS_BOUNDED |
| Governed artifact literal-format checklist learning | `13dcb7ad` | CLOSED_PASS_BOUNDED |
| ASSF external-agent metadata readout implementation dispatch | `ce102d77` | DISPATCH_READY |
| ASSF external-agent metadata readout implementation | `1f93ea33` | CLOSED_PASS_BOUNDED |
| ASSF metadata readout guard wiring dispatch | `810f3440` | DISPATCH_READY |
| ASSF metadata readout guard wiring | `e04ed428` | CLOSED_PASS_BOUNDED |
| AAF-T7A roadmap status reconciliation | `766f81e7` | CLOSED_PASS_BOUNDED |
| GFS-PY T2 lifecycle/status validator split | `3f7cb4e8` | CLOSED_PASS_BOUNDED |
| GFS-PY T3 source-verification/token-collision split | `f8f35e3e` | CLOSED_PASS_BOUNDED |
| GFS-PY T4 orchestrator-shell reduction / roadmap closure | `78798cd0` | CLOSED_PASS_BOUNDED |
| LSC roadmap status reconciliation | `46a1f17a` | CLOSED_PASS_BOUNDED |
| RSE roadmap status reconciliation | `23d99200` | CLOSED_PASS_BOUNDED |
| Roadmap status reconciliation sweep T0-T4 | `3ccf574c` | CLOSED_PASS_BOUNDED |
| Workspace layer full package absorption WLFA-T0-T4 | `fd8b1987` | CLOSED_PASS_BOUNDED |
| Local workspace projection read model LWPRM-T0-T4 | `8be9f9b6` | CLOSED_PASS_BOUNDED |
| Workflow Value Proof WVP-T0-T4 | `00c2bc40` | CLOSED_PASS_BOUNDED |
| Evidence Readout Friction Reduction Decision EFRD-T0-T4 | `7a973124` | CLOSED_PASS_BOUNDED |
| Evidence Readout Quick Packet Template ERQP-T0-T4 | `37f2d7bd` | CLOSED_PASS_BOUNDED |
| MKG Pending Finality Reconciliation MPFR-T0-T4 | `6cd88162` | CLOSED_PASS_BOUNDED |
| MKG Owner Verification Decision MKGOV-T0-T4 | `dcdbac64` | CLOSED_PASS_BOUNDED |
| MPI-T3 External Agent Memory Read Contract | `b825a69c` | CLOSED_PASS_BOUNDED |
| MPI-T4 Current-State Reconciliation | `d85dd329` | CLOSED_PASS_BOUNDED |
| MPI-T5 Current-State Reconciliation | `ec7da05c` | CLOSED_PASS_BOUNDED |
| Foundation Plane System-Chain Gap Priority Guidance | `2fc14fde` | ACTIVE_REFERENCE |

## Next Allowed Move

Mode: `foundation_plane_system_chain_gap_guidance_active_pending_fpc_scg_tranche_selection`

Next allowed move: open a fresh GC-018/source-verified roadmap or work order to handle FPC system-chain gaps first, using `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` as the routing reference. Priority order: P0 system-loop interlock registry gap for FPC-T2-C01 through C05; P1 machine-check coverage gap for FPC-T3-C06, C02, C05, and C03; P2 downstream use-case restraint. Recommended first work order candidate: `FPC-SCG-T1 Foundation Plane System-Chain Interlock Registry Decision And Edit`. Fallback: `FPC-SCG-T0 Foundation Plane System-Chain Gap Closure Roadmap`. LHW24 remains the latest closed numbered LHW wave.

MPI-T6 runtime reopen conditions are inherited from `docs/baselines/CVF_GC018_MPI_T6_RUNTIME_CANDIDATE_DECISION_PACKET_2026-06-22.md`: an operator-stated product requirement explicitly needs the MPI lane itself to add live runtime memory read / vector-durable query / external-agent MCP-CLI read not satisfied by current MPI contract/helper or pre-existing durable/reinjection surfaces; MPI-T5 checker repeatedly flags real MPI-lane overclaim attempts caused by an actual missing MPI-lane capability rather than wording error; or an external integration partner requires the MPI lane specifically, not pre-existing memory routes, to expose live MCP-CLI memory read access. Any reopened runtime work still requires fresh operator decision, fresh GC-018, source verification, live/provider proof when governance behavior is claimed, public/provenance boundary review, and secrets/quota handling if applicable.

No registry edit, checker implementation, runtime/MCP/CLI/IDE bridge implementation, further provider/live proof, public-sync, resolver mutation, adapter mutation, package activation, certification decision, generated workspace state mutation, DICE work, MPI-T6 runtime work, Policy_Local, Document Translator, Model Gateway/Sandbox runtime expansion, or push without separate authorization.

## Parked Checkpoint

Foundation Plane System-Chain Gap Priority Guidance is active at material commit `2fc14fde`. The next tranche should prioritize P0/P1 foundation system-chain gaps before downstream runtime, provider, public-sync, use-case, or MPI-T6 runtime work. MPI-T6 remains parked unless a recorded reopen condition is verified.

## Knowledge Absorption Priority Boundary

broad external knowledge absorption remains a governed, trigger-based lane.
Current blocked work classes include runtime/provider/live expansion,
public-sync content mutation, downstream use-case work, registry mutation,
checker implementation, and MPI-T6 runtime work unless separately authorized by
fresh GC-018/source-verified work order.

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
