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

Startup acknowledged: current mode=`cvf_ncr_r1_ux_focused_verify_locally_accepted`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=R1 exit/readability evidence disposition and bounded missing-proof planning only; role=INTERNAL_AGENT Local reviewer/closer; phase=FOCUSED_UI_ACCEPTED_LOCAL; decision owner=LOCAL; parked checkpoint=domain/provider/nonloopback/private data/production/public/deploy; manual worker transfer retained.

## Current Mode

Current mode marker: `cvf_ncr_r1_ux_focused_verify_locally_accepted`
Current mode: `cvf_ncr_r1_ux_focused_verify_locally_accepted`

Finite focused UI proof accepted bounded; next evidence disposition/planning only, no automatic worker/browser.

## Next Allowed Move

Mode: `cvf_ncr_r1_ux_focused_verify_locally_accepted`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN_ONLY; BATCH_ID=CVF-NCR-R1-UX-FOCUSED-VERIFY-20261018. Focused verification accepted bounded at 2f72bbf2941547cb92414b0ff2d849d79e65ee4c via docs/reviews/CVF_NCR_R1_UX_FOCUSED_VERIFY_LOCAL_COMPLETION_REVIEW_2026-10-18.md SHA256 5fd0b3e1cc4e87c9aab7a9417d56ac0bc295f47424e780774266eab2835d5659. Actual run-Qnaj9B/293.046s:6of6mobile/tablet3theme keyboard passes, all8criteria true, full Source notes visibility6,9required+2optionalimages/623799bytes,0Build/domain/browser-auth writes/effects,1fixturecallbackPOST and exact owned teardown;26pins stable, static tscPASS32.36s/strict owned2lintPASS9.922s reused,2baselinewarnings retained. Worker COMPLETE_PENDING_REVIEW/SUCCESSOR5/current0/counters0,0,0,0 retained; original return c050007b1466879c9086e3a3fb4fd10939100319268e228913efec86b3865206 archived, final documentary correction dce6ca3b000801440ba8bd2780acc50b17cbc512fc8966d00774b40db930ddc2, EP e7e24e703d8775197e19a0527008ad78a116588d1662c1fb8074cf0350aed0f3 unchanged. Knowledge/epistemic/probe applicability clarified; original full-gate/read order self-reported, not independent proof. Local sampled3existingPNG/hash-verified11; captured intake exact2 canonicalledger0issues, reviewer-return PASS after recorded Root active-envelope/enum correction; no product/browser replay. Next finite roadmap move: R1 exit/copy-effect explanation evidence disposition using existing component8DOM/scripted6refusals/current actual UI evidence; identify only genuinely missing agent-simulated novice interactions and prepare bounded contract if needed, no repeated focus campaign. Q003 permits agent simulation in internal pilot; genuine-user research NOT_EVALUATED, no recruitment prerequisite for R0-R3. R2/W05 selected-route pre-live destination/data/cost/admission/unknown-outcome read-only mapping remains separate; no effect grant. Future worker instructions go to operator for manual Claude transfer; Root must not auto-invoke worker/app/browser. Original focused completion BLOCKED/SUCCESSOR3/current4/counters0,0,0,1/partialreads/useLang/full6lintFAIL/path-ineligiblegates retained; contract correction SUCCESSOR4/current1 at8768d1f2d/17d8a099b. Prior repair BLOCKED/SUCCESSOR1/current3/counters0,0,0,1/two runner invocations-onebrowser/first117byte marker retained; source36rows/6keyboard accepted61ac95d1f/3085c195b. Prior browser INITIAL0; component BLOCKED/INITIAL0/12of21 and3of21FAILs/Local21of21with8DOM; UXsourceRETURN1/counters0,0,0,1; integratedRETURN3/counters0,1,0,3; preUXbrowserRETURN1/counters0,0,0,0; parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 retained. R1/R2partial,R3/R4open,R5/R6deferred; sidebarUXQ01 separate; actual business acceptance/provider/nonloopback/private data/production/public/deploy OFF.

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
