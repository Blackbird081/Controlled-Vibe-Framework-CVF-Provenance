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
| Parent maintenance | B-E source-only adjunct pair committed; bound implementation release and fake proofs next |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_b_e_adjunct_source_released`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=bound source-only adjunct implementation release and fake proofs; role=INTERNAL_AGENT Local dispatcher/reviewer/steward; phase=source-only dispatch, bound gate required before worker; decision owner=Local; parked checkpoint=actual B-E/Native/product/browser/container/provider/disposal/parent/public/deploy require separate current effect admission; no extra operator checkpoint for this source-only package.

## Current Mode

Current mode marker: `cvf_ncr_html_b_e_adjunct_source_released`
Current mode: `cvf_ncr_html_b_e_adjunct_source_released`; previous mode marker: `cvf_ncr_html_b_e_effect_design_accepted_source_packet_open`

## Next Allowed Move

Mode: `cvf_ncr_html_b_e_adjunct_source_released`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=EXECUTE; BATCH_ID=CVF-NCR-HTML-B-E-ADJUNCT-SOURCE-20261016. WORK_ORDER=docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md; baseline=docs/baselines/CVF_GC018_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md. Committed pair and exact6 continuity require current bound pre-dispatch PASS before worker starts; worker captures clean actual HEAD and bound pre-implementation before ignored scaffold/source/tests. INTERNAL_AGENT source-only worker exact7: five new adjunct source/test files below350 lines each plus return/proof. Locked APIs/counter56work8cleanup/identity/browser/helper/admission schemas and fixed root expectations; worker6 fake programs/root2 independent90s each, all preparation from06:54Z worker deadline09:54Z/root10:54Z; no budget reset. Full worker return gate and byte freeze, then distinct Local probes, accepted source-only release, atomic18 closure and handoff-only SHA sync. No actual runtime admission/pins/namespace/Job/Native children/browser/container/listener/provider/credentials/delete. Source13/production7/oracles6/gen9/original release/source authority and prior controls immutable; old5 programs/52 starts closed, no replay/refill. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF/SCEC2/counters2,0,2,0/blockers2/freeze; no transition/independentCriticalEvidence. Prior7 P4 exclusions retained, normal collector only; R1/R2partial,R3/R4open,R5/R6deferred, foundation active/extension NOT_APPLIED/projectOPEN; parked effects/LHW24 retained. Pre-edit authority amendment fixes counter-lock persistence and worker-before-Local probe order; renewed bound dispatch required, slots0 and deadlines unchanged.

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
