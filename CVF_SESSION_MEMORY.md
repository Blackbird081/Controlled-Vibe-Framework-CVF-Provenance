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
| Parent maintenance | BE-S11 source support accepted bounded; BE-R01/R02 open |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_body_heading_source_accepted_bounded`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=PLAN separately governed changed-source qualification and fresh cap2 admission; role=INTERNAL_AGENT Local reviewer/closer/steward; phase=CONTINUITY; decision owner=LOCAL; parked checkpoint=old grant retry/cap1/provider/deletion; no generic operator checkpoint.

## Current Mode

Current mode marker: `cvf_ncr_html_body_heading_source_accepted_bounded`
Current mode: `cvf_ncr_html_body_heading_source_accepted_bounded`; previous mode marker: `cvf_ncr_html_body_heading_source_dispatched`

## Next Allowed Move

Mode: `cvf_ncr_html_body_heading_source_accepted_bounded`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-BODY-HEADING-SOURCE-20261017. BE-S11 source support accepted bounded from actual-renderer DOM regression and pre-assertion custody source proof/current SOURCE_IDENTITY_ONLY release and distinct Local one-Node probe; consume docs/reviews/CVF_NCR_HTML_BODY_HEADING_SOURCE_COMPLETION_2026-10-17.md and docs/reviews/evidence/ncr-html-body-heading-source-local-20261017.json. Next Local plans separately governed separately admitted changed-source qualification/control and fresh cap2 runtime authority; prior controls9/26 are not current-source proof. BE-R01/BE-R02 open; no automatic actual effect. Parent generation9/SCECordinal2/counters2,0,2,0/two blockers/freeze/prior7/LHW24 unchanged. BE-R01 failed/unchecked; BE-R02 cap1 open; no prior actor replay. Actual result material 7efeb836d9bbe319fceb11d7c6a6c3bbc73feb4d committed; exact6 actual-SHA continuity prepared; clean split closure pending. Finality evidence front door: .cvf/runtime/ncr-body-heading-source-20261017/final-result.json; on resume consume its actual clean19/6 split PASS if present, rather than repeat committed closure. The pending phrase is the pre-commit continuity projection.

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
