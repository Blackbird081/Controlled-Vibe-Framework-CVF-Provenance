# ACTIVE SESSION FRONT DOOR
Memory class: active-session-front-door
Status: ACTIVE
Last compacted: 2026-08-11
## Startup Order
Read progressively, stopping once current facts are resolved; the full
history/state aggregate is a targeted lookup, not a default startup step:
1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` (compact current
   facts: current mode, active handoff, next allowed move)
2. this front door
3. `AGENT_HANDOFF_V63_2026-09-18.md`
4. only the current-authority paths those two surfaces name for the task
5. `CVF_SESSION/ACTIVE_SESSION_STATE.json` only as a targeted lookup, when a
   current fact above is missing, contradictory, or the task explicitly
   requires historical evidence
Canonical read-budget standard:
`docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`.
Machine guard: `governance/compat/check_active_session_state.py`.
Read `DESIGN.md` only when touching Web, UI, or dashboard work. Read
`docs/reference/guard_orientation/README.md` before authoring a governed
artifact.
## Active Pointers
| Field | Path |
|---|---|
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V63_2026-09-18.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Pain-point closure direction | `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Prior handoff (archive-qualified) | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V62_2026-09-17.md` |
| Latest front-door archive | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-08-11.md` |
| Current authority evidence | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` `currentAuthority` |
| Parent maintenance | B-E tool identities qualified; documentary candidate frozen; executable source admission/stage/journey open |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_b_e_prerequisites_qualified_source_admission_open`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=Local source-admission implementation preparation and connected scoped execution; role=INTERNAL_AGENT Local orchestrator/reviewer/steward; phase=B-E prerequisites qualified bounded, executable source release open; decision owner=Local; parked checkpoint=owned stage/product/browser/container/provider/disposal/parent/public/deploy effects need current before-effect admission. Current operator permits needed Alibaba tests; no API call in this qualification. No micro-stops/manual relay; old and qualification windows closed.

## Current Mode

Current mode marker: `cvf_ncr_html_b_e_prerequisites_qualified_source_admission_open`
Current mode: `cvf_ncr_html_b_e_prerequisites_qualified_source_admission_open`; previous mode marker: `cvf_ncr_html_cap1_control_accepted_b_e_source_release_entry`

## Next Allowed Move

Mode: `cvf_ncr_html_b_e_prerequisites_qualified_source_admission_open`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-B-E-QUALIFICATION-LOCAL-20261016. Material=db619cf48555ea1740973ed96cac0e72eafc35f7; proof=docs/reviews/evidence/ncr-html-b-e-qualification-local-20261016.json. NEXT_TRANCHE=NCR_HTML_B_E_SOURCE_RELEASE_AND_PREREQUISITE_QUALIFICATION; entry=PREREQUISITES_QUALIFIED_SOURCE_ADMISSION_OPEN. Next Local prepares/implements an explicit immutable current source release selector and admission in existing owners under locked design; focused missing/stale/foreign/current fences, then fresh controls bound to any changed production/oracle bytes before product. Candidate-v2 documentary only, RUNTIME_SOURCE_ADMISSION_NOT_RELEASED; no executable WO. Old pins missing2/stale3 helpers remain immutable. Docker desktop-linux/local named pipe and daemon linux/amd64, exact cached a0725d62 image platform, Chromium1208 file hash qualified; raw joins PASS. Initial image-name filter PARTIAL retained; separately admitted exact inspect PASS. Programs2/read-only utilities6, all windows/unused slots closed; source12/old cap1/native/proof stable, no broad/control/native rerun or slot refill. Accepted cap1 receipt9fde97a251da6a94a8df86e337819b04a43e6e683e21bf8a3c44d55e77118e3c remains prior unchanged source12 only. Current first authority/candidate preimages retained; final metadata candidate versioned. Old failed3-child and Local native ACK failures retained. No owned stage/product/browser/container/provider/disposal/public/deploy effect or B-E/parent proof. Continue connected admitted work without micro-stops/manual relay; owned stage and finite B-E effect/cleanup envelope still precede effects. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF/generation8/SCEC2/counters2,0,2,0/blockers2/freeze; no transition/independentCriticalEvidence. R5 authority pair historical only; prior7 P4 blocks/exclusions retained, collector normal only. R1/R2partial,R3/R4open,R5/R6deferred; foundation active/extension NOT_APPLIED/projectOPEN; data/custody/business/send/B2/P11/public/deploy parked; LHW24 retained.

## Parked Checkpoints

NCR-R0 limited pilot selection is retained; real-data writer/custody, business acceptance and effect-specific cost decisions remain action-specific checkpoints. U1 code import/runtime use, out-of-manifest production TypeScript edits, unrelated existing-guard edits, hook/autorun/CI wiring, provider/live, credential access, quota mutation, CLI/MCP invocation, public sync, deployment, production, trusted-evidence readiness and cross-runtime determinism claims remain parked.
T4 closed as standalone static checker work with no hook wiring or production-source mutation.
Prior unrelated checkpoints remain historical.

The `broad external knowledge absorption` lane remains outside the current release; blocked work classes remain G1-G6 continuation, G7 implementation/experiment work, Party B/C, credential handling, Group 4 source/T3E, provider/runtime/deployment, and any new absorption tranche without fresh operator authority.

External absorption preparation closed at `b4fb661bb`, path correction `100d6bd8b`: public `main` is `132371c3`; protocol-1.3 packet `D:\UNG DUNG AI\EXTERNAL_AGENT_READ` is live-refreshed with 5/5 hashes matching. Each new repo still needs its own immutable pin, license evidence, and new task capsule.

## Targeted Lookup Rules

- For complete canonical state, read `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- For prior T2A closure narrative, read `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V58_2026-08-11.md`; do not restate it here.
- For pre-2026-08-11 front-door history, read the front-door archive above.
- For guard/task orientation, read `docs/reference/guard_orientation/README.md`.

## Claim Boundary
This compact current-only pointer carries no closed-tranche narrative; historical evidence lives in the dated archives listed above.

## Dispatch Eligibility Learning Discovery
Read `docs/reviews/learnings/README.md` before fresh-context/blind-review dispatch. T1H blocked1 retained; generic pre-transfer rule added at 8c0904c53; machine binding candidate only. R1 authority and parked lanes unchanged.
