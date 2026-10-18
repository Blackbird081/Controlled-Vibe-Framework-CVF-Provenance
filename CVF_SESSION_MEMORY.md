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

Startup acknowledged: current mode=`cvf_ncr_r1_ux_profile_source_locally_disposed`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=fresh bounded component/walkthrough admission preparation only; role=INTERNAL_AGENT Local orchestrator/reviewer; phase=SOURCE_LOCAL_DISPOSITION; decision owner=LOCAL; parked checkpoint=test/app/browser/provider/network/real-data/production/public/deploy.

## Current Mode

Current mode marker: `cvf_ncr_r1_ux_profile_source_locally_disposed`
Current mode: `cvf_ncr_r1_ux_profile_source_locally_disposed`

Local source2/static acceptance with procedure limits; blocked worker terminal retained separately. No current component/walkthrough proof.

## Next Allowed Move

Mode: `cvf_ncr_r1_ux_profile_source_locally_disposed`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN_ONLY; BATCH_ID=CVF-NCR-R1-UX-PROFILE-SOURCE-20261018. Local bounded source2/static disposition at fdf2daf079c427465e57498580e9d1c4cd213a2f via docs/reviews/CVF_NCR_R1_UX_PROFILE_SOURCE_LOCAL_COMPLETION_REVIEW_2026-10-18.md; worker terminal remains BLOCKED_WITH_REASON/REQ-RETURN BLOCKED after two failed full bound gates, with original bytes archived and Root metadata-only projection. Prepare a fresh bounded component/user-role walkthrough admission on this exact revision; cite Local acceptance and blocked return separately. No test/app/browser release yet. TypeScript Root recheck PASS and scoped lint PASS0errors/2warnings; worker TSC AMBIGUOUS then FAIL retained; no product proof rerun. New UX RETURN1/counters0,0,0,1 retains original blocker in worker SCEC; Local source decision does not rewrite it or permit worker redispatch/refill. Old source RETURN3/counters0,1,0,3, browser RETURN1/counters0,0,0,0 and parent gen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 retained. Next proof targets vi/en, observed-profile/generic fallback, errors, Stop/Save/review semantics, keyboard/small-screen and non-coder refusal/pre-effect understanding. R2/W05 effect-route pre-live remains open; R1/R2partial,R3/R4open,R5/R6deferred; provider/network/real-data/production/public/deploy OFF.

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
