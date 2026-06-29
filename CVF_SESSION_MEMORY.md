# ACTIVE SESSION FRONT DOOR

Memory class: active-session-front-door
Status: ACTIVE
Last compacted: 2026-06-26

## Startup Order

Read these files before governed material work:

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
4. `AGENT_HANDOFF_V27_2026-06-29.md`
5. `docs/reference/guard_orientation/README.md`

For governed artifact authoring, also read:

`docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`

## Active Pointers

| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V27_2026-06-29.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Front-door archive snapshot | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-06-26.md` |

## Startup Acknowledgment

Startup acknowledged: current mode=`agsk_t7_package_candidate_expansion_work_order_dispatched_pending_worker_execution`; active handoff=AGENT_HANDOFF_V27_2026-06-29.md; next allowed move=execute AGSK-T7 as `WORKER_MUST_NOT_COMMIT` using `docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_2026-06-29.md`; parked checkpoint=AGSK second-pass blind-spot audit found under-converted package-candidate inventory; AGSK-T7 dispatch material commit `9ee75a5e`; AGSK-T5 closed at material commit `a00f7cf5`; AGSK-T6 checker/runtime lanes remain value-parked behind fresh governed authorization; LHW24 remains the latest closed numbered LHW wave.

## Current Mode

Current mode marker: `agsk_t7_package_candidate_expansion_work_order_dispatched_pending_worker_execution`

Current mode: `agsk_t7_package_candidate_expansion_work_order_dispatched_pending_worker_execution`

`agsk_t7_package_candidate_expansion_work_order_dispatched_pending_worker_execution`

Previous mode:

`everos_absorption_lane_closed_pending_next_external_absorption_target`

## Latest Closed Work

| Work | Commit | Disposition |
|---|---|---|
| AGSK-T7 package-candidate expansion work order dispatch | `9ee75a5e` | DISPATCH_READY; worker must not commit; create metadata-only CANDIDATE registry entries from source-backed AGSK capability concepts and regenerate generated skill index |
| EverOS memory-foundation absorption lane closeout | `37771016` | CLOSED_PASS_BOUNDED; T3 plan `ed10ced8`, T4 checker `cac4947e`, T5 decision `CLOSE_EVEROS_ABSORPTION_LANE_NO_NEXT_TRANCHE`; 20 focused memory-access claim tests pass |
| CGE-R1 CodeGraph full reabsorption closeout | `2f106dea` | CLOSED_PASS_BOUNDED; 89 files dispositioned; 33 ADAPTED, 54 REJECTED, 2 NO_NEW_VALUE, 0 unresolved; GC-051 registry coverage added |
| CGE-R1 CodeGraph full reabsorption work order dispatch | `0041218b` | DISPATCH_READY; worker must not commit; full manifest/ledger/EAC/EAVC owner-surface conversion required |
| AGSK-T5 first external absorption package candidate | `a00f7cf5` | CLOSED_PASS_BOUNDED |
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
| FPC-SCG-T8 Foundation System-Chain Acceptance Ledger Provenance Carrier Reconciliation | `e278c039` | CLOSED_PASS_BOUNDED |
| FPC-DSD-T1 Foundation Downstream Post-Public-Export Lane Selection Decision | `24726307` | CLOSED_PASS_BOUNDED; decision `HOLD_DOWNSTREAM_IMPLEMENTATION` |
| FPC-PRG-T0 Parked Reopen Gate Systemization Roadmap | `8d4ed2f4` | CLOSED_PASS_BOUNDED; decision `SYSTEMIZE_PARKED_REOPEN_GATE_BEFORE_DOWNSTREAM_IMPLEMENTATION` |
| FPC-PRG-T1 Parked Reopen Condition Source Inventory | `ca60e1fd` | CLOSED_PASS_BOUNDED; decision `INVENTORY_REOPEN_CONDITIONS_BEFORE_CHECKER_IMPLEMENTATION` |
| FPC-PRG-T2 Parked Reopen Gate Checker | `ec7e4057` | CLOSED_PASS_BOUNDED; decision `CHECKER_EXISTS_BEFORE_GATE_WIRING` |
| FPC-PRG-T3 Parked Reopen Gate Wiring | `f74f0b7a` | CLOSED_PASS_BOUNDED; decision `CHECKER_WIRED_INTO_LOCAL_GATES` |
| FPC-PRG-T4 Parked Reopen Fixture Coverage | `aa0d1276` | CLOSED_PASS_BOUNDED; decision `FOCUSED_FIXTURE_COVERAGE_COMPLETE` |
| FPC-PRG-T5 Final Session/Front-Door Sync | `d749823c` | CLOSED_PASS; final sync for PRG-T1-T5 chain |
| FPC-FMS-T2 Current Registry Evidence Reconciliation | `9c6f43de` | ROADMAP_READY_FOR_OPERATOR_NEXT_LANE_DECISION; decision `HOLD_FOUNDATION_MAINTENANCE_NO_CURRENT_SOURCE_BACKED_GAP` |
| Truth Foundation / TKG-T0-T5 external absorption lane | `6ce94464` | CLOSED_PASS_BOUNDED; checker wired at `79f26845`; decision `CLOSE_TKG_ABSORPTION_LANE_NO_NEXT_TRANCHE` |
| Agent Engineering Control / AECG-T0 external absorption roadmap | `edee01a0` | ROADMAP_READY_FOR_AECG_T1_SOURCE_VERIFIED_TRIAGE |
| Agent Engineering Control / AECG-T1-T3 absorption closeout | `7701abb8` | CLOSED_PASS_BOUNDED; decision `CLOSE_AECG_ABSORPTION_LANE_NO_CHECKER_NOW` |
| Provider Intelligence / PINT-T0 external absorption roadmap | `658bc76d` | ROADMAP_READY_FOR_PINT_T1_SOURCE_VERIFIED_RECONCILIATION |
| Provider Intelligence / PINT-T1 source-verified reconciliation | `3a729e83` | CLOSED_PASS_BOUNDED; decision `AUTHOR_PINT_T2_PROVIDER_INTELLIGENCE_CLAIM_BOUNDARY_AND_RECEIPT_ADVISORY_REFERENCE` |
| Provider Intelligence / PINT-T1-T3 absorption closeout | `c21cd0e9` | CLOSED_PASS_BOUNDED; decision `CLOSE_PINT_ABSORPTION_LANE_NO_CHECKER_NOW` |
| MinerU Structured Extraction / MSEA-T0 external absorption roadmap | `3776d5db` | ROADMAP_READY_FOR_MSEA_T1_SOURCE_VERIFIED_RECONCILIATION |
| MinerU Structured Extraction / MSEA-T1-T3 absorption closeout | `38f236bc` | CLOSED_PASS_BOUNDED; decision `CLOSE_MSEA_ABSORPTION_LANE_NO_CHECKER_NOW` |
| Agent Skills Governance / AGSG-T0 external absorption roadmap | `b7b31f4e` | CLOSED_PASS_BOUNDED by AGSG-T1-T3 closeout |
| Agent Skills Governance / AGSG-T1-T3 absorption closeout | `66eb39ac` | CLOSED_PASS_BOUNDED; decision `CLOSE_AGSG_ABSORPTION_LANE_NO_CHECKER_NOW` |
| AGSG-BSH-T1 blind-spot presence checker | `328de12b` | CLOSED_PASS_BOUNDED; ADIF-0014 machine-checked |
| ADIF-0015 declared-route-vs-execution-behavior record | `a8f45aa7` | ACTIVE_ADIF_RECORD |
| EAC-T1 external absorption core guard | `80a87e45` | CLOSED_PASS_BOUNDED; external repo/folder absorption now requires machine-checked manifest/ledger core |
| AGSK absorption pack reabsorption review | `4d08aa64` | CLOSED_PASS_BOUNDED; 29-file pack sweep under EAC core |
| EAVC-T1 external absorption value conversion guard | `4f0ef2c9` | CLOSED_PASS_BOUNDED; external absorption now requires machine-checked doctrine/package/runtime/checker value conversion matrix; AGSK addendum applied |
| AGSK package-candidate triage roadmap | `d8b14a2e` | ACTIVE_TRIAGE; opens AGSK-T4 before AGSK-T5 |
| AGSK-T4 riskTriggers work order dispatch | `11590704` | DISPATCH_READY; worker must not commit; AGSK-T5 remains blocked until T4 closes |
| AGSK-T4 riskTriggers contract patch | `2a84036a` | CLOSED_PASS_BOUNDED; AGSK-T5 package-candidate registry instance is next |
| AGSK-T5 first external-absorption package candidate dispatch | `1cc52d7a` | DISPATCH_READY; worker must not commit; candidate metadata only |
| AGSK-T5 first external-absorption package candidate | `a00f7cf5` | CLOSED_PASS_BOUNDED; first AGSK-derived ASSF registry candidate added |

## Next Allowed Move

Mode: `agsk_t7_package_candidate_expansion_work_order_dispatched_pending_worker_execution`

Next allowed move: execute AGSK-T7 as `WORKER_MUST_NOT_COMMIT` using
`docs/work_orders/CVF_AGENT_WORK_ORDER_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_2026-06-29.md`.
The worker must create metadata-only `CANDIDATE` ASSF registry entries for
source-backed AGSK capability concepts, regenerate
`docs/reference/agent_system_skills/generated/skill-index.json` through the
existing generator, create
`docs/reviews/CVF_AGSK_T7_PACKAGE_CANDIDATE_EXPANSION_FROM_SOURCE_PACK_WORKER_RETURN_2026-06-29.md`,
and return without committing. AGSK-T7 dispatch material commit is `9ee75a5e`.
LHW24 remains the latest closed numbered LHW wave.

No package root, `SKILL.md`, checker implementation, resolver mutation, runtime
activation, provider/live proof, public-sync, session-sync, package activation,
lifecycle promotion, external CLI/MCP adapter, direct pack checker import, or
production-readiness claim is authorized.

MPI-T6 runtime reopen conditions are inherited from `docs/baselines/CVF_GC018_MPI_T6_RUNTIME_CANDIDATE_DECISION_PACKET_2026-06-22.md`: an operator-stated product requirement explicitly needs the MPI lane itself to add live runtime memory read / vector-durable query / external-agent MCP-CLI read not satisfied by current MPI contract/helper or pre-existing durable/reinjection surfaces; MPI-T5 checker repeatedly flags real MPI-lane overclaim attempts caused by an actual missing MPI-lane capability rather than wording error; or an external integration partner requires the MPI lane specifically, not pre-existing memory routes, to expose live MCP-CLI memory read access. Any reopened runtime work still requires fresh operator decision, fresh GC-018, source verification, live/provider proof when governance behavior is claimed, public/provenance boundary review, and secrets/quota handling if applicable.

No runtime/MCP/CLI/IDE bridge implementation, further provider/live proof, resolver mutation, adapter mutation, package activation, certification decision, generated workspace state mutation beyond session sync, DICE runtime expansion, MPI-T6 runtime work, Policy_Local, Document Translator, Model Gateway/Sandbox runtime expansion, push from provenance workspace, P0 registry reopen, C06 checker reopen, C02 checker reopen, C05 checker reopen, T5 manifest reopen, T6 checker reopen, T7 reopen, or downstream implementation without separate authorization and regression/reopen evidence. Live/API keys may be used only in a future authorized live-proof tranche; FPC-PRG-T2 did not use live keys because it made no runtime/provider governance claim.

## Parked Checkpoint

FPC-SCG-T1 closed the P0 system-loop interlock registry visibility gap at material commit `75fcad20`. FPC-SCG-T2 through FPC-SCG-T7, FPC-DSD-T0, and FPC-UAP-T0 through FPC-UAP-T2 are closed bounded at current provenance carrier `be253923`. FPC-SCG-T8 closed the acceptance-ledger provenance carrier reconciliation at material commit `e278c039`. FPC-DSD-T1 closed the post-public-export downstream hold decision at material commit `24726307`. FPC-PRG-T0 closed parked reopen gate systemization at material commit `8d4ed2f4`; FPC-PRG-T1 closed parked reopen condition source inventory at material commit `ca60e1fd`; FPC-PRG-T2 closed parked reopen gate checker at material commit `ec7e4057`; FPC-PRG-T3 closed gate wiring at material commit `f74f0b7a`; FPC-PRG-T4 closed fixture coverage at material commit `aa0d1276`; FPC-FMS-T2 added current registry reconciliation at material commit `9c6f43de` and holds foundation maintenance because no current source-backed P0/P1 gap remains. TKG-T0 through TKG-T5 closed the Agent Governance Toolkit / Truth Kernel absorption lane at material commit `6ce94464`; TKG-T4 wired the truth foundation claim guard at `79f26845`. AECG-T1 through T3 closed the CodeGraph and Agent Engineering Control absorption roadmap at material commit `7701abb8`; no AECG checker is implemented now. PINT-T1 through T3 closed Provider Intelligence absorption at material commit `c21cd0e9`; no PINT checker is implemented now. MSEA-T1 through T3 closed MinerU Structured Extraction absorption at material commit `38f236bc`; no MSEA checker is implemented now. AGSG-T1 through T3 closed Agent Skills Governance absorption at material commit `66eb39ac`; AGSG-BSH-T1 closed the scope-triggered blind-spot presence checker at material commit `328de12b`; EAVC-T1 closed value conversion guard at material commit `4f0ef2c9` and applied it to AGSK. Runtime-provider-live lanes, package activation, adapter implementation, public-sync expansion, MPI-T6 runtime work, merge automation, hook repair, CodeGraph runtime/MCP/watcher/daemon, direct AEC package import, OpenRouter dependency, MCP production routing, benchmark/cost/latency measurement, automatic model selection, provider-intelligence checker implementation, MinerU runtime/install/model-download/OCR/provider-live/VLM-hybrid/RAG-index/checker implementation, extraction accuracy, document-truth, Agent Skills plugin/command/persona/hook/runtime import, ASSF package instance mutation, CLI/MCP adapter, automatic skill invocation, and production-readiness claims remain parked unless a recorded reopen condition is verified through a fresh governed tranche.

## Knowledge Absorption Priority Boundary

Broad external knowledge absorption remains a governed, trigger-based lane.
AGSG-T1 through T3 closed the Agent Skills Governance absorption roadmap, and
EAVC-T1 now requires every external absorption to classify doctrine,
package, runtime, checker, reject-direct-import, and no-package/runtime value.
EverOS memory-foundation absorption is closed through T5 with no immediate next
EverOS tranche. The next governed move is AGSK-T7 package-candidate expansion,
because the AGSK second pass found package-candidate inventory value that should
be converted before moving to a different external repo. The exact markers
`broad external knowledge absorption` and `blocked work classes` remain active
for compatibility gates. Current blocked work classes include
runtime/provider/live expansion, public-sync content mutation,
downstream use-case work, registry mutation, checker implementation, merge
automation, hook repair, CodeGraph runtime/MCP/watcher/daemon, direct AEC
package import, OpenRouter dependency, MCP production routing, benchmark
campaign, cost/latency measurement, automatic model selection, MinerU runtime
install, model download, OCR/provider-live/VLM-hybrid execution, RAG index
write, document-truth claim, extraction accuracy claim, Agent Skills plugin
or command import, persona orchestration, hook install, checker implementation,
ASSF package instance mutation, automatic skill invocation, production-readiness
claim, and MPI-T6 runtime work unless separately authorized by fresh
GC-018/source-verified work order.

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
