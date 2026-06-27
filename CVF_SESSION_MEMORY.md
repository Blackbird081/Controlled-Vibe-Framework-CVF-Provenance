# ACTIVE SESSION FRONT DOOR

Memory class: active-session-front-door
Status: ACTIVE
Last compacted: 2026-06-26

## Startup Order

Read these files before governed material work:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V24_2026-06-27.md`
5. `docs/reference/guard_orientation/README.md`

For governed artifact authoring, also read:

`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

## Active Pointers

| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V24_2026-06-27.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Front-door archive snapshot | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-26.md` |

## Startup Acknowledgment

Startup acknowledged: current mode=`fpc_uap_t2_public_export_closed_pass_bounded_pending_hold_or_fresh_governed_next_tranche`; active handoff=AGENT_HANDOFF_V24_2026-06-27.md; next allowed move=hold, or open a fresh GC-018/source-verified next tranche only after operator selection; parked checkpoint=P0 registry visibility, FPC-T3-C06 raw-memory invariant coverage, FPC-T3-C02 DICE machine-candidate coverage, FPC-T3-C05 worker-return fast-gate coverage, FPC-T3-C03 expected-chain manifest source verification/checker extension, FPC-SCG-T0 roadmap refresh, FPC-SCG-T7 acceptance ledger/reopen gate, FPC-DSD-T0 downstream lane selection, FPC-UAP-T0 public-boundary roadmap, FPC-UAP-T1 public surface inventory, and FPC-UAP-T2 public export are closed bounded through material commit `be253923`; public repo current for UAP comprehension at `04d88109317c780ceb2062a257c0e863e2379276`; runtime/provider-live lanes and MPI-T6 runtime remain parked unless a recorded reopen condition is verified through a fresh governed tranche.

## Current Mode

Current mode marker: `fpc_uap_t2_public_export_closed_pass_bounded_pending_hold_or_fresh_governed_next_tranche`

Current mode: `fpc_uap_t2_public_export_closed_pass_bounded_pending_hold_or_fresh_governed_next_tranche`

`fpc_uap_t2_public_export_closed_pass_bounded_pending_hold_or_fresh_governed_next_tranche`

Previous mode:

`fpc_uap_t1_public_surface_inventory_closed_pass_bounded_pending_fpc_uap_t2_public_export_or_hold`

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
| FPC-SCG-T1 System-Chain Interlock Registry Decision And Edit | `75fcad20` | CLOSED_PASS_BOUNDED |
| FPC-SCG-T2 Raw Memory Release Invariant Autorun Coverage | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-SCG-T3 DICE Machine-Candidate Checker | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-SCG-T4 Worker-Return Fast-Gate Epistemic Fixture | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-SCG-T5 Interlock Expected-Chain Manifest Source Verification | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-SCG-T6 Interlock Expected-Chain Checker Extension | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-SCG-T0 Foundation System-Chain Gap Closure Roadmap Refresh | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-SCG-T7 Foundation System-Chain Acceptance Ledger And Downstream Reopen Gate | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-DSD-T0 Foundation Downstream Lane Selection Decision | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-UAP-T0 Use-Case Adapter Public Boundary And Dev-Facing Comprehension Roadmap | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-UAP-T1 Use-Case Adapter Public Comprehension Surface Inventory And Boundary | `be253923` | CLOSED_PASS_BOUNDED |
| FPC-UAP-T2 Use-Case Adapter Public Export README Catalog Snapshot Refresh | `be253923` | CLOSED_PASS_BOUNDED; public `04d88109317c780ceb2062a257c0e863e2379276` |

## Next Allowed Move

Mode: `fpc_uap_t2_public_export_closed_pass_bounded_pending_hold_or_fresh_governed_next_tranche`

Next allowed move: hold, or open a fresh GC-018/source-verified next tranche only after operator selection. FPC-UAP-T2 is closed bounded at provenance material commit `be253923`; public-sync commit `04d88109317c780ceb2062a257c0e863e2379276` updated `README.md`, `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`, and `docs/evidence/public-current-state-snapshot-2026-06-27.md`. Recommended posture is to return to foundation-plane system-chain priorities or a new governed downstream-selection decision, not runtime/provider/live/MPI-T6/package activation by default. P0/C06/C02/C05/T5/T6/T0/T7, FPC-DSD-T0, FPC-UAP-T0, FPC-UAP-T1, and FPC-UAP-T2 remain closed bounded unless recorded evidence regresses. LHW24 remains the latest closed numbered LHW wave.

MPI-T6 runtime reopen conditions are inherited from `docs/baselines/CVF_GC018_MPI_T6_RUNTIME_CANDIDATE_DECISION_PACKET_2026-06-22.md`: an operator-stated product requirement explicitly needs the MPI lane itself to add live runtime memory read / vector-durable query / external-agent MCP-CLI read not satisfied by current MPI contract/helper or pre-existing durable/reinjection surfaces; MPI-T5 checker repeatedly flags real MPI-lane overclaim attempts caused by an actual missing MPI-lane capability rather than wording error; or an external integration partner requires the MPI lane specifically, not pre-existing memory routes, to expose live MCP-CLI memory read access. Any reopened runtime work still requires fresh operator decision, fresh GC-018, source verification, live/provider proof when governance behavior is claimed, public/provenance boundary review, and secrets/quota handling if applicable.

No runtime/MCP/CLI/IDE bridge implementation, further provider/live proof, resolver mutation, adapter mutation, package activation, certification decision, generated workspace state mutation beyond session sync, DICE runtime expansion, MPI-T6 runtime work, Policy_Local, Document Translator, Model Gateway/Sandbox runtime expansion, push from provenance workspace, P0 registry reopen, C06 checker reopen, C02 checker reopen, C05 checker reopen, T5 manifest reopen, T6 checker reopen, T7 reopen, or downstream implementation without separate authorization and regression/reopen evidence. Live/API keys may be used only in a future authorized live-proof tranche; FPC-UAP-T2 did not use live keys because it made no runtime/provider governance claim.

## Parked Checkpoint

FPC-SCG-T1 closed the P0 system-loop interlock registry visibility gap at material commit `75fcad20`. FPC-SCG-T2 closed FPC-T3-C06 raw-memory-release invariant autorun coverage at material commit `be253923`. FPC-SCG-T3 closed FPC-T3-C02 DICE machine-candidate coverage at material commit `be253923`. FPC-SCG-T4 closed FPC-T3-C05 worker-return fast-gate epistemic fixture coverage at material commit `be253923`. FPC-SCG-T5 closed FPC-T3-C03 expected-chain manifest source verification at material commit `be253923`. FPC-SCG-T6 closed FPC-T3-C03 expected-chain checker extension at material commit `be253923`. FPC-SCG-T0 closed the foundation system-chain roadmap refresh at material commit `be253923`. FPC-SCG-T7 closed the acceptance ledger and downstream reopen gate at material commit `be253923`. FPC-DSD-T0 selected `use-case-adapter-public` as the next valuable downstream lane at material commit `be253923`. FPC-UAP-T0 closed the public/provenance boundary and dev-facing comprehension roadmap at material commit `be253923`. FPC-UAP-T1 closed the public comprehension surface inventory and boundary decision at material commit `be253923`. FPC-UAP-T2 closed the bounded public README/catalog/snapshot export at provenance material commit `be253923` and public-sync commit `04d88109317c780ceb2062a257c0e863e2379276`. Runtime-provider-live lanes, package activation, and MPI-T6 runtime work remain parked unless a recorded reopen condition is verified through a fresh governed tranche.

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
