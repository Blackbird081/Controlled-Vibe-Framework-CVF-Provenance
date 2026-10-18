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

Startup acknowledged: current mode=`cvf_ncr_r1_ux_focused_verify_manual_handoff_ready`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=actual bound release then manual operator worker transfer; role=INTERNAL_AGENT Local reviewer/dispatcher; phase=MANUAL_VERIFY_HANDOFF_READY; decision owner=LOCAL; parked checkpoint=domain/provider/nonloopback/private data/production/public/deploy; no Root worker/browser start.

## Current Mode

Current mode marker: `cvf_ncr_r1_ux_focused_verify_manual_handoff_ready`
Current mode: `cvf_ncr_r1_ux_focused_verify_manual_handoff_ready`

Corrected verification-only pair ready for manual transfer after bound release; no Root worker/browser.

## Next Allowed Move

Mode: `cvf_ncr_r1_ux_focused_verify_manual_handoff_ready`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE_FOCUSED_UI_VERIFY; BATCH_ID=CVF-NCR-R1-UX-FOCUSED-VERIFY-20261018. Operator manually transfers docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_UX_FOCUSED_VERIFY_2026-10-18.md to Claude in same checkout. Pair2 8768d1f2d4a5af7e3e53edaedb18bb4944080c89 after dedicated current6 and actual bound pre-dispatch PASS; then full scoped reads/clean actual HEAD/pins/pre-implementation. Worker exact2 new return/EP only; source/spec/config/runner/registry readonly, runner validated transient restore only. SUCCESSOR4/current1/counters0,0,0,0 derives from actual3/current4 and accepted static/contract evidence; returnSUCCESSOR5, no INITIAL/reset. Reuse Local final-byte tsc/strict owned2lint only when pins/config/tool/dependency identities match; preserve2baseline hookwarnings. One60min task, one copied final pinned spec/static list<=1, one runner<=15min/retries0 after exact node/Git/PATH/3033 preflight,6mobile/tablet theme keyboard passes/9inspected required PNG<=12/16MiB,0Build/domain/auth-browser-write/effect attempts, callback-only fixture auth and owned teardown. No source/spec repair or runner retry; incomplete proof returns BLOCKED. Root later material4/current6 separate. Original focused worker BLOCKED/SUCCESSOR3/current4/counters0,0,0,1, partial mandatory reads, helper syntax failure before tool launch, useLang errors and both path-ineligible full gates retained byte-for-byte; zero runner/browser/run root/keyboard/images. Original full6 lint FAIL with2readonly baseline warnings; final source/spec Local tscPASS32.36s and strict owned2 lintPASS9.922s. Source focus leaf/spec accepted bounded; original return54835b71d949c376ee1a9cfe881889f0bdba8f23e5f862ef5717ce0d91cea462, EP443d2e67c5403b82ac1d511a2515d44f9a84346ac46e43088fd949cccaec5dd3. Mandatory registry3 correction adds existing lint config only; first normal hookGC051 failure retained. Prior repair BLOCKED/SUCCESSOR1/counters0,0,0,1/current3/two runner invocations-onebrowser/required-read omissions/failed gates retained; source36rows/6completekeyboard accepted at61ac95d1f, continuity3085c195b. Prior browser INITIAL0; component BLOCKED/INITIAL0/12of21 and3of21FAILs, Local21of21/8DOM; UX sourceRETURN1/counters0,0,0,1; integratedRETURN3/counters0,1,0,3; preUXbrowserRETURN1/counters0,0,0,0; parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 retained. R1/R2partial,R3/R4open,R5/R6deferred; sidebar/R2/W05/human-business acceptance remain separate; domain/provider/nonloopback/private data/production/public/deploy OFF.

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
