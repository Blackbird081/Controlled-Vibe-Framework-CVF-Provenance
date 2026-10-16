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
| Parent maintenance | Adjunct source accepted bounded; Local actual B-E readiness/prerequisite assessment next |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_b_e_adjunct_source_accepted_readiness_open`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=Local actual B-E technical readiness/prerequisite assessment under existing design; role=INTERNAL_AGENT Local closure/session-sync steward; phase=source-only adjunct accepted/procedure partial, effects held; decision owner=Local root; parked checkpoint=concrete runtime readiness/effect admission required, no extra generic operator checkpoint for routine technical choices; Local3 spent and original10:54Z deadline retained.

## Current Mode

Current mode marker: `cvf_ncr_html_b_e_adjunct_source_accepted_readiness_open`
Current mode: `cvf_ncr_html_b_e_adjunct_source_accepted_readiness_open`; previous mode marker: `cvf_ncr_html_b_e_python_oracle_recovery_local_allowance_admitted`

## Next Allowed Move

Mode: `cvf_ncr_html_b_e_adjunct_source_accepted_readiness_open`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=ASSESS; BATCH_ID=CVF-NCR-HTML-B-E-PYTHON-ORACLE-RECOVERY-20261016. ACCEPTED_SOURCE_ONLY_PROCEDURE_PARTIAL: frozen adjunct5/worker7 accepted with actual root Python45 predicates including20 typed/message refusals, prior valid LocalJS18 and worker35/30/full gate reused. Source-only release issued; no runtime release or AI-governance proof. Next Local assesses actual B-E technical readiness/prerequisites under existing docs/assessments/CVF_NCR_HTML_B_E_EFFECT_DRIVER_LOCAL_DESIGN_2026-10-16.md, preparing concrete before-effect authority/identity/custody/budgets as needed. Routine technical choices proceed under existing Local delegation; no generic operator documentary checkpoint. Actual Native/Job/product/browser/container/provider/disposal/public/deploy effects held until concrete readiness/effect admission. Local3/3 spent, original failed Python/JS18/old ledger retained, no retry/refill/worker or JS rerun. Original root deadline10:54Z elapsed after valid09:33Z proof; terminal docs only11:13Z-11:43Z under Local decision, procedure PARTIAL and no proof or timer reset. Source13/gen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7 P4 exclusions unchanged; no transition/new independentCriticalEvidence. R1/R2partial,R3/R4open,R5/R6deferred; parked effects/LHW24 retained.

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
