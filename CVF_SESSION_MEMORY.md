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

Startup acknowledged: current mode=`cvf_ncr_r2_w05_offline_source_manual_handoff_ready`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=bound release then operator manual transfer of integrated offline source/verification packet; role=INTERNAL_AGENT Local dispatcher/reviewer; phase=OFFLINE_SOURCE_PACKET_READY; decision owner=LOCAL; parked checkpoint=real endpoint/provider/data/store/production/public/deploy effects.

## Current Mode

Current mode marker: `cvf_ncr_r2_w05_offline_source_manual_handoff_ready`
Current mode: `cvf_ncr_r2_w05_offline_source_manual_handoff_ready`

Integrated offline source packet prepared for operator manual transfer after actual bound release; Root has not invoked worker or created/run product tests.

## Next Allowed Move

Mode: `cvf_ncr_r2_w05_offline_source_manual_handoff_ready`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=MANUAL_TRANSFER_OFFLINE_SOURCE_PACKET; BATCH_ID=CVF-NCR-R2-W05-OFFLINE-SOURCE-20261019. Operator manually transfers docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_OFFLINE_SOURCE_2026-10-19.md including proposed focused offline verification scope after actual clean boundrelease PASS; Root does not invoke worker or create/run producttests. One INTERNAL_AGENT180min/exact13:contract/store/injectedproof/profile/branch/actualPOST/hook plus returnEP; Vitest<=4,tsc<=2,targetedESLint<=2,requiredGate<=3; no install/app/browser/network/provider/active-data/runtime/public/deploy. Seven-field body/two selectors, ownergetJob/requesthash beforeBuild;getVersion onlyafterSave; separateINJECTED_SYNTHETIC_RECEIPT notJOB_EFFECTS. Fixedkey excludesjobId; immutabletarget/config,0sendexactreuse or409referenceonly/no oldreceipt-newHTML; declared-unattestedfixtureidentity; reconcileBpresence cannot releaseUNKNOWN. Disabled/invalid/profilemissing selectorsdeny/no fallback.256monotonicreservations-owner/16KiBrecords/noexpiry/noGC;R1/REVIEW. Local independentprobe pending afterworker. New implementationINITIAL0/docplan/INTEGRATED_ROOT_CONTRACT distinctfrom closed AuditS1/current0/counters0,0,0,1/docNO_SUCCESSOR; all prior source/Goal/Clarity/runtimecounters frozen. R1prelive/R2partial,R3R4open,R5R6deferred; M14-M16deferred. Parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 unchanged. Endpoint/auth/store/attestation/cost/businessacceptance remains held for dependent real effects.

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
