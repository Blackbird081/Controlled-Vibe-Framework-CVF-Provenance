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

Startup acknowledged: current mode=`cvf_ncr_r1_ux_focused_claude_handoff_ready`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=actual bound release then manual operator worker transfer; role=INTERNAL_AGENT Local dispatcher/reviewer; phase=MANUAL_FOCUSED_UI_HANDOFF_READY; decision owner=LOCAL; parked checkpoint=domain/provider/nonloopback/private data/production/public/deploy; no Root worker/browser start.

## Current Mode

Current mode marker: `cvf_ncr_r1_ux_focused_claude_handoff_ready`
Current mode: `cvf_ncr_r1_ux_focused_claude_handoff_ready`

Focused same-chain source/spec/quality packet for manual worker transfer. Actual bound release follows dedicated current6. No Root product change/check/browser/worker during preparation.

## Next Allowed Move

Mode: `cvf_ncr_r1_ux_focused_claude_handoff_ready`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE_FOCUSED_UI_COMPLETION; BATCH_ID=CVF-NCR-R1-UX-FOCUSED-COMPLETION-20261018. Operator transfers docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_FOCUSED_COMPLETION_2026-10-18.md to Claude in same checkout; Root must not auto-invoke worker/app/browser. Pair2 e9f618973cecdd2d1ab11650fac738a753bfd03b; after dedicated current6 and actual bound pre-dispatch PASS, capture clean release/full required reads/preimages and bound pre-implementation. Worker exact4=ArtifactExportPanel Source notes focus leaf/existing focused spec/return2; source4/harness/config/registry read-only, existing runner validated Next transient restore only. Same problem ncr-r1-existing-owner-ux-findings-repair SUCCESSOR2/current2/counters0,0,0,0: accepted-review proof resolves original source implementation only, not mobile/tablet/lint. Return must be SUCCESSOR3, no INITIAL/reset. One60min task, tsc/lint1each<=120s completed exit0 BEFORE browser; smaller typed focused spec under unchanged rules, no suppression or blind timeout extension. Static list<=2, ONE fresh runner<=15min/retries0 after exact PATH/git HEAD/port preflight;6mobile/tablet theme keyboard passes,9required inspected images<=12/16MiB;0Build/effect/write attempts, callback-only fixture auth and owned teardown/pins. Reuse prior36rows/desktop/validation at recorded revisions. After browser no source/spec edits; incomplete proof returns BLOCKED. Root later material6/current6 separate. Original repair worker BLOCKED/SUCCESSOR1/counters0,0,0,1/current3, required-read omissions, two runner invocations/one browser and failed gates retained. Root accepted source/36rows/6completekeyboard at61ac95d1f, continuity3085c195b/split10+6 PASS; one encoding comment, tscPASS62.922s, lint300timeout/debug45 spec traversal stall, no lint verdict. Prior browser INITIAL0, component BLOCKED/INITIAL0 and12/21,3/21 FAILs; UX source RETURN1/counters0,0,0,1; integrated RETURN3/counters0,1,0,3; pre-UX browser RETURN1/counters0,0,0,0; parent gen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 retained. R1/R2partial,R3/R4open,R5/R6deferred; off-canvas sidebar and R2/W05/human acceptance remain separate; provider/private data/production/public/deploy OFF. Release metadata correction: first pre-dispatch failed DR-05 because material marker omitted exact batch id; marker now names CVF-NCR-R1-UX-FOCUSED-COMPLETION-20261018. No work-order/source/effect change; consume the actual new bound receipt before transfer.

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
