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
| Parent maintenance | S14 source accepted; BE-Q05 conditional qualification dispatched; product/runtime pending; parent unchanged |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_login_readiness_qualification_dispatched`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=bounded Q05 worker after actual hash-bound release; role=INTERNAL_AGENT Local dispatcher/reviewer; phase=MATERIAL; decision owner=LOCAL; parked checkpoint=product/runtime/provider/native utilities/real-data/deletion/public/deploy.

## Current Mode

Current mode marker: `cvf_ncr_html_login_readiness_qualification_dispatched`
Current mode: `cvf_ncr_html_login_readiness_qualification_dispatched`; previous mode marker: `cvf_ncr_html_login_readiness_source_phase_accepted_bounded`

## Next Allowed Move

Mode: `cvf_ncr_html_login_readiness_qualification_dispatched`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE; BATCH_ID=CVF-NCR-HTML-LOGIN-READINESS-QUALIFICATION-20261017. Under `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_LOGIN_READINESS_QUALIFICATION_2026-10-17.md` and `docs/baselines/CVF_GC018_NCR_HTML_LOGIN_READINESS_QUALIFICATION_2026-10-17.md`, release INTERNAL_AGENT exact2 qualification worker only after committed normal9/6, bound pre-dispatch/pre-implementation PASS, fresh frozen pins/envelope and separate cap2/Docker admission. One cap2 inert9case/26 Python-child matrix<=90s; exactly4 local read-only Docker queries<=12s each/60s group; no automatic retry, original outcomes retained. Program root `.cvf/runtime/ncr-login-readiness-qualification-20261017/preparation`; Root private PURE10 after frozen exact2, no case-child/native/Docker rerun. Separate qualification phase06:59Z, workerhard08:00Z, Localhard08:15Z; cumulative04:00Z history/S14 old07:00Z retained, no old budget reset. S14source release/authority/source18 unchanged; canonical standalone identity proof reused, driver retains immediate admission precondition. BE-Q05 pending; R02/S12 spent; parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 and R1/R2partial,R3/R4open,R5/R6deferred unchanged. Reviewer proactively records necessary bounded repair/recheck with contradiction/gain/cost and first outcomes; no per-tranche confirmation or silent effect expansion. Product/browser/native utilities/HTTP/provider/real-data/deletion/public/deploy remain parked. Dispatch base fc9b7545806c3b979251a1c238339cc3bac2c353.

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
