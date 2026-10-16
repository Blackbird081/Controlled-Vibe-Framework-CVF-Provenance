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
| Parent maintenance | spent BE-R01 closed; BE-S10 source-only correction in progress, product outcomes open |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_passive_request_observer_source_dispatched`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=conditional exact6 PASSIVE_REQUEST_OBSERVER_SOURCE worker after committed bound source release/preimplementation; role=INTERNAL_AGENT Local dispatcher/reviewer/steward; phase=CONTINUITY; decision owner=LOCAL; parked checkpoint=all browser runtime/cap1/provider/deletion/retry effects unadmitted; no generic operator checkpoint.

## Current Mode

Current mode marker: `cvf_ncr_html_passive_request_observer_source_dispatched`
Current mode: `cvf_ncr_html_passive_request_observer_source_dispatched`; previous mode marker: `cvf_ncr_html_r1c_be_r01_blocked_spent`

## Next Allowed Move

Mode: `cvf_ncr_html_passive_request_observer_source_dispatched`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE; BATCH_ID=CVF-NCR-HTML-PASSIVE-REQUEST-OBSERVER-SOURCE-20261017. Under docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_PASSIVE_REQUEST_OBSERVER_SOURCE_2026-10-17.md and docs/baselines/CVF_GC018_NCR_HTML_PASSIVE_REQUEST_OBSERVER_SOURCE_2026-10-17.md, conditionally release one INTERNAL_AGENT exact6 source worker after committed dispatch/current authority/actual-SHA continuity, bound pre-dispatch and worker preimplementation PASS. Correct eager evaluate-POST IncomingMessage consumption using passive observation in existing journey owner/tests; preserve prior main-entry/GET/malformed fixes; exact source_release AUTHORITY and effect-driver test assertion only. Worker Node budget exactly2 direct CJS RED/GREEN starts with real delayed IncomingMessage-to-Request regression, no legacy Windows test collection; root separate independent1 Node probe, budgets/physical pins/custody exactly W. Inclusive prep 2026-10-16T18:42:00Z, worker hard90min deadline 2026-10-16T20:12:00Z, Local180min 2026-10-16T21:42:00Z; no reset. BE-S10 unchecked IN_PROGRESS_SOURCE_ONLY; BE-R01 spent failed/open and BE-R02 open/unadmitted. Prior result material 187996f311383a63ce1fe13451f7f1bba9700177/continuity fcdc86057d5e9df72a1b17115193e7e7e691bd7b actual13/6 split PASS consumed, no rerun. Source18 before-image frozen; accepted main-entry source B/W/releases/qualification/failed worker2/CP/LP unchanged. Worker leaves F release constants; Local accepted new-source identity/release/F binding is a later distinct closure, not old release repin. No browser/runtime/cap1/provider/deletion/retry; changed source requires separate future qualification. gen9/SCECordinal2/counters2,0,2,0/blockers2/freeze/prior7 exclusions/LHW24 and R1/R2partial,R3/R4open,R5/R6deferred unchanged; old1spent/2retired and r1b/r1c spent blocked retained. Current continuity anchor 1437e2725d99ab66bd0984e0fa96b5e9075f18e9; ordinary technical details Local, no generic documentary operator checkpoint.

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
