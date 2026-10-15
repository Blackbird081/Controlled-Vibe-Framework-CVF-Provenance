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
| Parent maintenance | Direct Local source repair accepted bounded; no manual implementation relay; actual native/B-E/parent proof held |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_direct_local_source_repair_accepted_native_prerequisite_plan`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=final split closure then Local native-proof prerequisite PLAN; role=INTERNAL_AGENT Local implementer/disposition owner/steward with distinct internal probe executor; phase=bounded direct source repair complete; decision owner=Local; parked checkpoint=actual Windows ABI/B-E/native/browser/product/container/provider/stage deletion/parent/public/deploy. Direct implementation selected; no manual relay, current Local control-program window closed.

## Current Mode

Current mode marker: `cvf_ncr_html_direct_local_source_repair_accepted_native_prerequisite_plan`
Current mode: `cvf_ncr_html_direct_local_source_repair_accepted_native_prerequisite_plan`; previous mode marker: `cvf_ncr_html_root_semantic_r5_rejected_repair_packet_plan`

## Next Allowed Move

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-DIRECT-LOCAL-REPAIR-20261016. Final source repair accepted bounded material=94f7793e17d31ca825280ea27d996a041ab48951; authorization=docs/baselines/CVF_GC018_NCR_HTML_DIRECT_LOCAL_REPAIR_2026-10-16.md; proof=docs/reviews/evidence/ncr-html-direct-local-repair-20261016.json. Operator selects direct Local implementation; prior manual relay retired. No active executable work order; schema-required currentAuthority pair is consumed R5 historical provenance only. Four R5 failures/PID cleanup race, cancellation/spawn primary errors and connected normal-UNKNOWN readiness fence corrected. Unconfirmed completion closes WORK, revokes queued work and prevents sleep/retry; confirmed nonzero may retry within budget. Final160 Python/13 Node and independent program3:14 PASS/0 FAIL. Two source-bound9-case matrices52/54 inert total,26 latest; Local8/8 programs CLOSED, reviewer3/4 and0 children. No further Local control launch in this window. First materialb6b63c83/continuity4c1bd70d1 retained; second minimal correction9 within originalsource10/documentary5. EXCEPTION_WITH_REASON: connected UNKNOWN fence found after first commit; two material/three exact6 continuity including the checker-required freshness precursor, no counter/profile refill. Preparation PARTIAL and all first failures retained, including RED3 and GREEN159/1 old private exception expectation; final current proof supersedes earlier157/12 only at source-model scope. Checked outside pytest cleanup was policy-blocked; all exact recording paths/archives/Local ownership in .cvf/runtime/ncr-html-root-local-repair-20261016/all-temp-retention.json; no alternate removal. Premature correction pre-closure failed only the unsynced handoff HEAD marker; failure retained, final continuity precedes the split rerun. A metadata-only inline script then failed PowerShell quoting before writing; file-backed correction used. Finish serial split closure then Local PLAN reconciles actual Windows ABI/B-E/native/browser/product/container/cleanup prerequisites; no automatic runtime/worker or effect release. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF/generation6/SCEC ordinal2/counters2,0,2,0/two blockers/freeze; no new transition/independentCriticalEvidence/new checker. Actual effects0, all52 inert children completed; parent custody/stage deletion unaccepted. Prior7 P4 blocks/exclusions preserved; automatic collector SKIPPED_NO_ELIGIBLE_CANDIDATE after first continuity, no manufactured observation. R1/R2partial,R3/R4open,R5/R6deferred; foundation active/extension NOT_APPLIED/projectOPEN; data/custody/business/send/B2/P11/public/deploy parked; LHW24 retained. No micro-confirmation for admitted Local work.

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
