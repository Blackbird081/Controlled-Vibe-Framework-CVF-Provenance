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
| Parent maintenance | Explicit source identity accepted bounded; fresh source13 controls, owned stage and B-E journey open |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_source_admission_accepted_b_e_controls_open`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=Local current-source controls/owned-stage/B-E envelope preparation; role=INTERNAL_AGENT Local reviewer/steward; phase=source identity accepted bounded, procedure partial; decision owner=Local; parked checkpoint=actual native/product/browser/container/provider/disposal/parent/public/deploy effects need current admission.

## Current Mode

Current mode marker: `cvf_ncr_html_source_admission_accepted_b_e_controls_open`
Current mode: `cvf_ncr_html_source_admission_accepted_b_e_controls_open`; previous mode marker: `cvf_ncr_html_source_admission_worker_released`

## Next Allowed Move

Mode: `cvf_ncr_html_source_admission_accepted_b_e_controls_open`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-SOURCE-ADMISSION-20261016. SOURCE_ADMISSION_ACCEPTED_BOUNDED; completedSourceOrder=docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_SOURCE_ADMISSION_2026-10-16.md; completion=docs/reviews/CVF_NCR_HTML_SOURCE_ADMISSION_COMPLETION_2026-10-16.md; frozenSourceRelease=docs/reviews/evidence/ncr-html-source-release-20261016.json@d1a591633d144bacf0c5ffa8afc019b981b2b587e8512dd3ac549a1681397fc5. Next Local prepares current source13 actual controls and owned synthetic staging/B-E before-effect envelope; no executable runtime successor yet. Explicit selector/admission and product-binding recheck implemented; worker227/227 before one Local oracle correction, affected1/1 and independent30/30 PASS; worker full gate/raw joins PASS. Local committed read is metadata only and recorded in final handoff. Family13=production7/oracles6; prior source12/control/native proofs immutable and old control bindings stale after changed bytes, not replayed/refilled. Existing tool qualification retained. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF/generation9/SCEC2/counters2,0,2,0/blockers2/freeze; no transition/independentCriticalEvidence. Prior7 P4 blocks/exclusions retained, normal collector only. Full B-E/parent/disposal unproved; actual native/product/browser/container/provider/delete0. R1/R2partial,R3/R4open,R5/R6deferred; foundation active/extension NOT_APPLIED/projectOPEN; data/custody/business/send/B2/P11/public/deploy parked; LHW24 retained.

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
