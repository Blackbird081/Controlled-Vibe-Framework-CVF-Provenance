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

Startup acknowledged: current mode=`cvf_ncr_html_direct_local_source_repair_accepted_native_prerequisite_plan`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=connected material correction then final continuity/split closure; role=INTERNAL_AGENT Local implementer/reviewer/steward; phase=freshness prerequisite continuity, distinct internal probe complete; decision owner=Local; parked checkpoint=actual Windows/native/B-E/browser/product/container/provider/stage/parent/public/deploy. Local control window closed.

## Current Mode

Current mode marker: `cvf_ncr_html_direct_local_source_repair_accepted_native_prerequisite_plan`
Current mode: `cvf_ncr_html_direct_local_source_repair_accepted_native_prerequisite_plan`; previous mode marker: `cvf_ncr_html_root_semantic_r5_rejected_repair_packet_plan`

## Next Allowed Move

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-DIRECT-LOCAL-REPAIR-20261016. Committed first source disposition remains material b6b63c8329398c0b1eff4ca565ada4edcb999dde and continuity4c1bd70d19ddbb3075366a9934c1c4d827dcbb64. Next finish the connected normal-UNKNOWN fence correction material and final exact6 continuity, then split closure. The source correction has final160 Python/13 Node and distinct14 PASS; not yet committed or finally closed. Pending correction9 are hash-preserved in .cvf/runtime/ncr-html-root-local-repair-20261016/pending-correction-before-continuity/manifest.json while this precursor is committed. The prior next move named the mutable disposition as a target; the exact-target checker correctly reported AMBIGUOUS_DIRTY_TARGET. This precursor selects the actual remaining commit/closure action; no assessment is a dispatch or planning target. Restore pending bytes exactly after this commit. EXCEPTION_WITH_REASON: two material/three exact6 continuity commits, including this freshness prerequisite. No checker change or bypass. Direct Local implementation only under docs/baselines/CVF_GC018_NCR_HTML_DIRECT_LOCAL_REPAIR_2026-10-16.md; no executable work order or manual relay. Required currentAuthority pair is consumed R5 historical provenance only, never an execution grant. R5 rejection and all original failures remain. Local8/8 test programs CLOSED,52/54 inert completed; reviewer3/4,0 children. No more Local controls or profile/counter refill. After final closure Local PLAN reconciles actual Windows ABI/B-E/native/browser/product/container/cleanup prerequisites. Actual effects0 and parent/stage proof unaccepted. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF/generation6/SCEC ordinal2/counters2,0,2,0/two blockers/freeze; no new transition/critical evidence/checker. Partial preparation retained. Outside pytest cleanup policy-blocked; archives/exact paths/Local owner in current custody all-temp-retention.json; no alternate delete. Prior7 P4 exclusions preserved, first continuity collector skipped no eligible candidate. R1/R2partial,R3/R4open,R5/R6deferred; foundation active/extension NOT_APPLIED/projectOPEN; data/custody/business/send/B2/P11/public/deploy parked; LHW24 retained. No micro-confirmation for admitted Local work.

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
