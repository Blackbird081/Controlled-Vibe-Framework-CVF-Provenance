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
| Parent maintenance | R1F accepted; R2C conditional fresh cap1 dispatch, actual outcome pending; parent unchanged |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=cvf_ncr_html_be_r2c_runtime_dispatched; active handoff=AGENT_HANDOFF_V63_2026-09-18.md; next allowed move=conditional R2C paired cap1 after committed bound release; role=INTERNAL_AGENT Local dispatcher/reviewer; phase=CONTINUITY; decision owner=LOCAL; parked checkpoint=provider/real-data/deletion/public/deploy.

## Current Mode

Current mode marker: cvf_ncr_html_be_r2c_runtime_dispatched
Current mode: cvf_ncr_html_be_r2c_runtime_dispatched; previous mode marker: cvf_ncr_html_r1f_current_source_cap2_accepted_bounded

## Next Allowed Move

Mode: cvf_ncr_html_be_r2c_runtime_dispatched

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE; BATCH_ID=CVF-NCR-HTML-B-E-R2C-RUNTIME-20261018. Under docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_B_E_R2C_RUNTIME_2026-10-18.md and docs/baselines/CVF_GC018_NCR_HTML_B_E_R2C_RUNTIME_2026-10-18.md, release eligible distinct /root/r2c_execute only after committed exact9/6, bound pre-dispatch PASS, reviewed initial external pins/control envelope and clean source. One fresh ordinal2 LOCAL_REVIEWER cap1 runId ncr-be-local-20261018-r2c, exactly two programs under one authority: program1 actual9/26 then Root independent PURE10 barrier/stage2 freeze before one original D.execute v1 program2. No stage2 after failed/ambiguous program1, retry0, provider0, stageDeletion0; work900/cleanup120, starts56/8, readiness4/6/2. Preparation 2026-10-18T00:50:14.167024+00:00, latest launch 2026-10-18T02:12:00+00:00, worker hard 2026-10-18T02:30:00+00:00, Local hard 2026-10-18T03:00:00+00:00; old R2B clocks/custody/grants spent. R1F material862957c7930d79ba01b7241f0ccf6caf29a8b8df/continuityd08f88760761738efe588572e97f1b294bef5a5f accepted bounded; source18/Q05 proof reused, new cap1 control must be actual. Worker exact2/no commit; Root separate PURE11 and exact13/6 closure after actual terminal. Parentgen9/SCECordinal2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 unchanged, never successor3. R1/R2partial,R3/R4open,R5/R6deferred; provider/real-data/deletion/public/deploy parked. Actual R2C material anchor ab6d7ea5d73fd590f6417a4ddf17f110a1aca370.

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
