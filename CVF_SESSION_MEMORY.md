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
| Parent maintenance | lasting support ledger checked; bounded qualification; product B-E open |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_body_heading_source_qualification_dispatched`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=finite current-source qualification after committed bound release; role=INTERNAL_AGENT Local orchestrator/reviewer/steward; phase=CONTINUITY; decision owner=LOCAL; parked checkpoint=old runtime grants retired, product/cap1/provider/deletion separate; no generic operator checkpoint.

## Current Mode

Current mode marker: `cvf_ncr_html_body_heading_source_qualification_dispatched`
Current mode: `cvf_ncr_html_body_heading_source_qualification_dispatched`; previous mode marker: `cvf_ncr_html_body_heading_source_accepted_bounded`

## Next Allowed Move

Mode: `cvf_ncr_html_body_heading_source_qualification_dispatched`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE; BATCH_ID=CVF-NCR-HTML-BODY-HEADING-SOURCE-QUALIFICATION-20261017. Under docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_BODY_HEADING_SOURCE_QUALIFICATION_2026-10-17.md and docs/baselines/CVF_GC018_NCR_HTML_BODY_HEADING_SOURCE_QUALIFICATION_2026-10-17.md, release INTERNAL_AGENT qualification worker only after bound pre-dispatch PASS and frozen invocation-envelope/pins external hashes. One actual cap2 control matrix9cases/26inert Python children, one Docker4 read-only group;2one-shot programs,90s/60s outer,12s Docker child,retry0; worker deadline03:40Z, Local05:10Z. Source13/adjunct5/frozen source authority unchanged; no fake/broad/native-seam rerun. Worker exact2 publishes after both programs; Local PURE independent receipt oracle then closure. Roadmap BE-S01..11 plus retained BE-S10-G checked bounded support; BE-Q04 open until actual qualification, BE-R01/R02 open. Preparation inclusive start02:10Z; hard worker03:40Z/Local05:10Z. BE-S11 checked source support and historical BE-Q01/BE-Q02/BE-Q03 accepted remain retained. No product/cap1/provider/deletion or old grant replay; gen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 and parked states retained. Ordinary details Local; no generic operator checkpoint. Qualification material dfde8b74716344b5e186840b76077971f360775a; source6 records the actual material anchor before worker release.

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
