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

Startup acknowledged: current mode=`cvf_ncr_r2_w05_bound_source_manual_handoff_ready`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=operator manual transfer of exact36 integrated offline bound-receipt source packet after actual boundrelease; role=INTERNAL_AGENT Local dispatcher/reviewer; phase=BOUND_SOURCE_DISPATCH_READY_EFFECTS_HELD; decision owner=LOCAL; parked checkpoint=actual endpoint/key/data/storewriter/cost/business acceptance and production/public/deploy.

## Current Mode

Current mode marker: `cvf_ncr_r2_w05_bound_source_manual_handoff_ready`
Current mode: `cvf_ncr_r2_w05_bound_source_manual_handoff_ready`

One integrated exact36 source packet prepared for manual transfer after actual release; source implementation/acceptance not executed. All real effects held; production DENY.

## Next Allowed Move

Mode: `cvf_ncr_r2_w05_bound_source_manual_handoff_ready`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE_BOUND_RECEIPT_OFFLINE_SOURCE_VIA_OPERATOR_MANUAL_TRANSFER; BATCH_ID=CVF-NCR-R2-W05-BOUND-SOURCE-20261019. Operator manually transfers docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_BOUND_SOURCE_2026-10-19.md with paired docs/baselines/CVF_GC018_NCR_R2_W05_BOUND_SOURCE_2026-10-19.md after actual clean boundrelease PASS. Exact36:8existingmodifications/26newproduct-test-vector paths+returnEP;7requirements;300min,Vitest<=2x600s,pytest<=2x300s,tsc<=2x240s,changedWeblint<=2x300s,fullgate<=3x180s; worker32768files/128MiB,Pythonchildren<=24/PSACL<=12/total<=40. BC01-BC12 and crosslanguage/key-lifetime clauses freeze neweffect schema+v1codec isolation, measured pinned SQLite subclass, signed dedicated Web/engine hops, actual export/jobs/ENVI consumer, strict counters/risk/UNKNOWN and full transaction proof. Runtime defaults/productionDENY; no network/provider/browser/active-data/OSsecuritymutation/install. Exactcontrols2existinglintfingerprints only, original exits/read history preserved. Root does not invoke worker or execute product checks. NewboundeffectINITIAL0, workerSUCCESSOR1againstactualWOhash; fixtureLocalS5current0/counters0,1,0,1 frozen, no reset/refill. Local independently probes <=12min after returned proof, then acceptance/material38or39/current6. R1prelive/R2partial/R3R4open/R5R6deferred. Parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 fixed. Later actual origins/keyrefs/storewriter/data/retention/cost/acceptance groupedcheckpoint; real provider/production/public/deployOFF.

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
