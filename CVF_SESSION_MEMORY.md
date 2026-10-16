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
| Parent maintenance | qualification accepted; one fresh conditional BE-R01 grant, product acceptance open |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_fresh_be_r01_dispatched`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=one new conditional fresh cap2 BE-R01 after committed bound release/external freeze/worker preimplementation; role=INTERNAL_AGENT Local orchestrator/reviewer/steward; phase=CONTINUITY; decision owner=LOCAL; parked checkpoint=old grants/cap1/provider/deletion and unrelated effects, no generic operator checkpoint.

## Current Mode

Current mode marker: `cvf_ncr_html_fresh_be_r01_dispatched`
Current mode: `cvf_ncr_html_fresh_be_r01_dispatched`; previous mode marker: `cvf_ncr_html_windows_qualification_accepted_bounded`

## Next Allowed Move

Mode: `cvf_ncr_html_fresh_be_r01_dispatched`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE; BATCH_ID=CVF-NCR-HTML-B-E-FRESH-RUNTIME-20261016. Root selected new one-actor fresh BE-R01 under docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_B_E_FRESH_RUNTIME_2026-10-16.md and docs/baselines/CVF_GC018_NCR_HTML_B_E_FRESH_RUNTIME_2026-10-16.md. Execute only after committed pair/currentAuthority, actual-material source6 continuity, bound pre-dispatch PASS, frozen external admission/pins/inputs/independent envelope digest and worker pre-implementation PASS. One default D.execute ordinal1/IMPLEMENTATION_WORKER/cap2/runId=ncr-be-fresh-worker-20261016-r1b, namespace D:/CVF_NCR_RUNTIME/ncr-be-fresh-worker-20261016-r1b, custody D:/CVF_NCR_RUNTIME/custody-be-fresh-20261016-b. Prep16:42Z; worker deadline18:12Z/latest launch17:54Z, Local19:42Z; work900s/cleanup120s,56work+8cleanup controlled roots,outer1080s,retry0/provider0/stageDeletion0. Refusal/ambiguous start spends new slot; no old replay/cap1/provider/deletion. Source18/accepted Windows source B/W/release immutable. Qualification cap2 actual9/26+Docker4+Local PURE10 accepted; qualification split13/6 PASS consumed from prior final-result, no rerun. BE-Q01 checked bounded; BE-R01 in-progress conditional grant remains unchecked, BE-R02 open; support8 retained. Metadata file-only preparation16:43:31Z starts0/source-tools/namespace absence/input spec join is preparation, recheck before consume. Root external freeze occurs after bound gate; pure closed-schema metadata validation adds no runtime slot. gen9/SCECordinal2/counters2,0,2,0/blockers2/freeze/prior7 exclusions/LHW24 and R1/R2partial,R3/R4open,R5/R6deferred unchanged; old1spent/2retired never replayed. Current continuity anchor d99f0d89d03228c487feb8e8a3980bab444018f7; no fresh runtime outcome claimed. Ordinary technical detail Local, no generic operator checkpoint.

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
