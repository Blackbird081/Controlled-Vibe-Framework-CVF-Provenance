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
| Parent maintenance | BE-R01 accepted bounded on R1E; BE-R02 conditional cap1 controls/barrier/journey pending |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=cvf_ncr_html_r2b_be_r02_dispatched; active handoff=AGENT_HANDOFF_V63_2026-09-18.md; next allowed move=conditional R02 cap1 program1 after exact9/6 dispatch and external freeze; program2 remains behind Root PURE10 barrier; role=INTERNAL_AGENT Local orchestrator/reviewer/steward; phase=MATERIAL; decision owner=LOCAL; parked checkpoint=provider/deletion and retry remain unadmitted; no generic operator checkpoint.

## Current Mode

Current mode marker: `cvf_ncr_html_r2b_be_r02_dispatched`
Current mode: `cvf_ncr_html_r2b_be_r02_dispatched`

## Next Allowed Move

Mode: cvf_ncr_html_r2b_be_r02_dispatched

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE; BATCH_ID=CVF-NCR-HTML-B-E-R2B-RUNTIME-20261017. One fresh Local INTERNAL_AGENT LOCAL_REVIEWER ordinal2 cap1 actor ncr-be-local-20261017-r2b under docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_B_E_R2B_RUNTIME_2026-10-17.md and docs/baselines/CVF_GC018_NCR_HTML_B_E_R2B_RUNTIME_2026-10-17.md may start only after exact9 authority commit, actual-SHA exact6 continuity, bound pre-dispatch PASS on continuity HEAD and Root paired-envelope/external-pin freeze. Program1 is one actual cvf.ncrHtmlInertControls@3 SUBPROCESS matrix (9 ordered cases, 26 charged inert children, zero product effects). Root alone checks pre-frozen private PURE10 and accepted R1E; only PASS permits one original D.execute v1 cap1 journey. Program2 is not authorized by program1 success alone. Fixed runId ncr-be-local-20261017-r2b; namespace D:\CVF_NCR_RUNTIME\ncr-be-local-20261017-r2b; custody D:\CVF_NCR_RUNTIME\custody-be-r2b-20261017. Preparation 03:15Z; worker hard 04:45Z; latest launch 04:27Z; Local hard 06:15Z. Limits work900/cleanup120s, Native work/cleanup56/8, Job32, readiness engine4/web6/route2/total12, Job1/container1/web1/browserSession1, export1/evaluate1, providerStarts0/stageDeletion0, outer1080/wait1070/termination5; retry0; no separate Docker group. Worker returns exact2 after terminal and does not commit. Root closes actual result exact13 then actual-SHA6. R1E accepted bounded, S11/Q04/source18 immutable; old actors never replayed; parent gen9/SCECordinal2/counters2,0,2,0/blockers2/freeze/prior7 exclusions/LHW24 and R1/R2partial,R3/R4open,R5/R6deferred do not reset. Material anchor 1cb8f480ba626bdfe8c334cbbd07d7ad765d4e36; phase=material.

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
