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
| Parent maintenance | Fresh S14-source R1F cap2 plus R2C cap1 synthetic mechanical pair accepted bounded; R2C paired actor spent; gen9/SCECordinal2/counters2,0,2,0/blockers2/freeze/prior7/LHW24; R1/R2partial,R3/R4open,R5/R6deferred unchanged; no automatic successor |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_r2_w05_binding_repair_accepted_offline`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=Local consolidated R2/W05 activation design only after accepted offline binding repair; role=INTERNAL_AGENT Local reviewer/closer; phase=OFFLINE_SOURCE_ACCEPTED_EFFECTS_HELD; decision owner=LOCAL; parked checkpoint=actual destination/auth/store/data/provider/cost/business acceptance and production/public/deploy.

## Current Mode

Current mode marker: `cvf_ncr_r2_w05_binding_repair_accepted_offline`
Current mode: `cvf_ncr_r2_w05_binding_repair_accepted_offline`

Finite binding repair accepted offline with procedure limits; next Local design/admission consolidation only. Production export denies; real effects remain OFF.

## Next Allowed Move

Mode: `cvf_ncr_r2_w05_binding_repair_accepted_offline`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=CONSOLIDATE_R2_W05_ACTIVATION_DESIGN_ONLY; BATCH_ID=CVF-NCR-R2-W05-BINDING-REPAIR-20261019. Binding repair material12 7c0aa69c386884bd3d9193528b1ec32bae615c58 accepted bounded with procedure limits; Local review docs/reviews/CVF_NCR_R2_W05_BINDING_REPAIR_LOCAL_COMPLETION_REVIEW_2026-10-19.md and EP docs/reviews/evidence/ncr-r2-w05-binding-repair-local-20261019.json. Worker199of199/tsc0/changed7lint0; distinctLocal10of10PASS on actual production TS/freshsynthetic roots, no network. Production export intentionally DENY under locked R04; legacy explicitnonproductiononly. Internal start/admission, consume/envelope, outcome/opaquehandle changes require no route.ts or operation-branch.ts edit. Panel4baseline and hook1warning exceptions retained, panel/whole11lint not rerun; originalblockedsource/probe4of8FAIL/read/ADIF/scratch history not cured. WorkerS4current0/counters0,1,0,0; LocalS5current0/counters0,1,0,1, samechain/noINITIALreset/noautomaticworker. Next Local reconciles remaining endpoint/auth/store attestation, exactrequest mapping, effect/cost/Stop/UNKNOWN and acceptance gaps into one integrated design/admission packet; no implementation or activation grant. Real destination/data/writer/provider/cost/businessacceptance and production/public/deploy remain parked. R1prelive/R2partial/R3R4open/R5R6deferred. Parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 frozen. All real network/provider/active-data/production/public/deployOFF.

## Parked Checkpoints

NCR-R0 limited pilot selection is retained; real-data writer/custody, business acceptance and effect-specific cost decisions remain action-specific checkpoints. U1 code import/runtime use, out-of-manifest TypeScript edits, unrelated existing-guard edits, hook/autorun/CI wiring, provider/live, credential access, quota mutation, CLI/MCP invocation, public sync, deployment, production, trusted-evidence readiness and cross-runtime determinism claims remain parked.
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
