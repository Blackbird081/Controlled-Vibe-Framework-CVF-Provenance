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

Startup acknowledged: current mode=`cvf_ncr_r1_goal_focus_accepted_exit_planning`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=PLAN_ONLY R1 exit criterion reconciliation then R2/W05 read-only chosen-route preparation; role=INTERNAL_AGENT Local reviewer; phase=GOAL_FOCUS_ACCEPTED_WITH_PROCEDURE_LIMITS; decision owner=LOCAL; parked checkpoint=provider/private-data/production/public/deploy.

## Current Mode

Current mode marker: `cvf_ncr_r1_goal_focus_accepted_exit_planning`
Current mode: `cvf_ncr_r1_goal_focus_accepted_exit_planning`

Finite Goal focus UI repair accepted with procedure limits; no full R1/R2 exit or effect authority.

## Next Allowed Move

Mode: `cvf_ncr_r1_goal_focus_accepted_exit_planning`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN_ONLY; BATCH_ID=CVF-NCR-R1-GOAL-FOCUS-REPAIR-20261019. R1 exit criterion reconciliation using accepted source/component/browser/pre-effect assessment/copy/Goal evidence; then R2/W05 read-only chosen-route preparation for destination/data/secretrefs/cost/permissions/retention/denials/revoke/unknown-outcome non-replay. No further Goal repair or automatic worker/app/browser/provider run. Goal focus Local review docs/reviews/CVF_NCR_R1_GOAL_FOCUS_REPAIR_LOCAL_COMPLETION_REVIEW_2026-10-19.md SHA256ce769e0c531cb056ca3db76526c75db5ceecd6466242cf99fae26f7f68978a6b ACCEPTED_TECHNICAL_BOUNDED_PROCEDURE_PARTIAL in material6 7d8c0e1c4a393511ab8b3029951f1815b76b1d5c. Final43of43 after41of43FAIL/mockprototypefix; tsc0twice/lint0exact3baselinewarnings; onebrowser7passes/12actualcriteriaalltrue/13required+2optionalPNG1848159bytes/mobileGoal3y393h58/tablet3visible/0Build-write/exactteardown/23workerpins26runnerpins/finalgate2COMPLIANT. Workerexact4unchanged; mandatoryorientationlate remains procedurepartial. WorkerS2fork kept, LocalS3actualdispatchS2/current1to0/counters0,0,0,0 governs. Root13criteria count corrected to12criteria/13images; ignored202MBbuildretained under cleanup prohibition. Rootproductruns/sourceedits0. OriginalclarityBLOCKED/S1current3/counters0,0,0,1/browserFAIL and earlierfailedgate/read/budgethistories remain in governed reviews; sourceparentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 unchanged. R1/R2partial,R3/R4open,R5/R6deferred; Q003agentsimulationallowed/humanNOT_EVALUATED not recruitmentgate. Provider/nonloopback/private-data/production/public/deployOFF. Any future implementation workorder is manually transferred to Claude by operator; Root does not invoke it.

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
