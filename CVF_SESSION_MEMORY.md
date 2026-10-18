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

Startup acknowledged: current mode=`cvf_ncr_r1_pre_effect_walkthrough_handoff_ready`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=bound release then manual operator transfer of finite assisted UI assessment; role=INTERNAL_AGENT Local dispatcher/reviewer; phase=PRE_EFFECT_UI_MANUAL_HANDOFF_READY; decision owner=LOCAL; parked checkpoint=domain/provider/nonloopback/private data/production/public/deploy; no Root browser/worker start.

## Current Mode

Current mode marker: `cvf_ncr_r1_pre_effect_walkthrough_handoff_ready`
Current mode: `cvf_ncr_r1_pre_effect_walkthrough_handoff_ready`

R1 evidence disposition complete; finite assisted pre-effect UI assessment packet ready after actual bound release. Manual worker transfer only.

## Next Allowed Move

Mode: `cvf_ncr_r1_pre_effect_walkthrough_handoff_ready`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE_PRE_EFFECT_UI_ASSESSMENT; BATCH_ID=CVF-NCR-R1-PRE-EFFECT-WALKTHROUGH-20261018. Operator manually transfers docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_PRE_EFFECT_WALKTHROUGH_2026-10-18.md to selected shared-workspace worker; Root must not auto-invoke worker/app/browser. Material3 5818fb2672f74fc0719b70e24fc511b7c911ee55 includes baseline/work order/roadmap2.75 R1 evidence disposition; dedicated current6 and actual bound pre-dispatch PASS before transfer. Future worker exact2return/EP, source/tests/harness/config/registry readonly, ignored probe<=240lines/list config/capture/transcript and one existing runner only; validated Next transient restore allowed. INITIAL0/problem ncr-r1-pre-effect-user-role-walkthrough/current1/counters0,0,0,0; returnSUCCESSOR1, distinct from completed focus S5/current0, no old-chain reset/refill. One60min task, one desktop1280x900/VI/darkindigo capture W1selected/W2syntheticedit-decline/W3generic-decline/W4unbuilt-revisit,7original UI-grounded VI explanations,4checkpoint outcomes/<=8PNG8MiB; source/brief assistance declared, persona narrative frozen before technical crosscheck, no human/blind claim. Staticlist<=2 before one runner<=15min/retries0 after exact Node/Git/PATH/3033 preflight;0Build/Save/Stop/link/accept/download/copy/domain/auth-browser-write/effect,1APIRequestContext fixturecallbackPOST only; actualtraffic/pins/teardown/caps. Complete assessment may report unfavorable copy; missing execution/mandatory proof returnsBLOCKED, no source/probe fix after browser or retry. Fullgate<=2 with raw/detached final receipt. Local later material4/current6 separate. Focus Local material2f72bbf29/current6d06719b8a accepted6keyboard9required+2optionalimages/Source notes visible6/0Build-write/exactteardown; actualSUCCESSOR5/current0/counters0,0,0,0 retained. Original read/full-gate/doc limits and return/archive hashes remain in Local review/finality. Source tsc32.36s/owned2lint9.922s accepted, baseline2warnings retained. Original focuscompletionBLOCKED/S3/current4/counters0,0,0,1; repairBLOCKED/S1/current3/counters0,0,0,1/two runnerinvocations-onebrowser/117bytefirstmarker retained; component21of21/8DOM plus original12of21/3of21FAIL/INITIAL0; scriptedrefusal6 script-only; UXsourceRETURN1/counters0,0,0,1; integratedRETURN3/counters0,1,0,3; preUXbrowserRETURN1/counters0,0,0,0; parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 unchanged. R1/R2partial,R3/R4open,R5/R6deferred. Q003 agent simulation allowed/internal pilot; genuine-user researchNOT_EVALUATED not recruitment gate. R2/W05 chosenroute prelive mapping separate; actual business/provider/nonloopback/private data/production/public/deployOFF.

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
