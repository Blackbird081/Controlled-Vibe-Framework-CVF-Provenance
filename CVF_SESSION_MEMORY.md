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
| Parent maintenance | Source-admission packet committed; exact worker7 is source-only; bound dispatch gate pending; effects remain parked |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_source_admission_worker_released`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=execute `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_SOURCE_ADMISSION_2026-10-16.md` only after its bound pre-dispatch gate passes; role=INTERNAL_AGENT Local dispatcher/reviewer/steward; phase=source-admission worker released, source-only and zero effects; decision owner=Local; parked checkpoint=owned B-E stage/journey, product/browser/container/provider/disposal/parent/public/deploy effects require their own current admission.

## Current Mode

Current mode marker: `cvf_ncr_html_source_admission_worker_released`
Current mode: `cvf_ncr_html_source_admission_worker_released`; previous mode marker: `cvf_ncr_html_b_e_prerequisites_qualified_source_admission_open`

## Next Allowed Move

Mode: `cvf_ncr_html_source_admission_worker_released`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE; BATCH_ID=CVF-NCR-HTML-SOURCE-ADMISSION-20261016. Material=e6de9ae45d3da60315a71d6c5219cdcea62a1437; currentAuthority=baseline=docs/baselines/CVF_GC018_NCR_HTML_SOURCE_ADMISSION_2026-10-16.md@1c33647040bc57cd32a6edb27533d7d728158b18660dbcf87a3ae0b89dfa1056; workOrder=docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_SOURCE_ADMISSION_2026-10-16.md@c7353cd7d14fd0c4675ec3edb35fb81803ee74a7ced85589347513e6d34f1b07. NEXT_TRANCHE=NCR_HTML_B_E_SOURCE_RELEASE_AND_PREREQUISITE_QUALIFICATION; entry=SOURCE_ADMISSION_WORKER_RELEASED. Bound pre-dispatch gate=PENDING_PASS for this exact work order; pre-implementation remains pending before worker edits. One internal worker owns the exact worker7 outputs (five source/test paths plus two worker evidence paths), source-only; worker test ceiling6, Local source-review ceiling3. Actual child/native/product/browser/container/network/provider/delete effects=0. Source family13 only when the new module is written; old source12/cap1/native evidence remains unchanged. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF, source generation8, SCEC2, counters2,0,2,0, blockers2, freeze and prior7 P4 exclusions; no SCEC transition or independent critical evidence. Owned B-E stage/journey, product, browser, container, provider, disposal, parent, public and deploy effects remain parked pending their own current admission. R1/R2partial,R3/R4open,R5/R6deferred; foundation active/extension NOT_APPLIED/projectOPEN; LHW24 retained.

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
