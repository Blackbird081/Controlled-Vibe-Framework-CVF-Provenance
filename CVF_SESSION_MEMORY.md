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
| Parent maintenance | Reviewer adjudication complete; runtime acceptance remains blocked and grant spent. First material dbb07364863ea627c22b07fd23b62a574b10aea0/continuity e4497e82cafe81b302d30aa5cbaa2331f6397a35 passed normal91/91, but automatic P4 committed-range generation failed RIPA on root-selected invalid reviewer Status. That unsafe automatic result is retained, never promoted. Existing canonical Recurring Blocked-Return Escalation governs blocked worker returns; explicit completion_review negative adjudication is not a new worker return. The narrow existing checker correction retains generic finding validation, actual/ambiguous worker enforcement and original FIRST_OCCURRENCE worker bytes. Worker focused tests and distinct root five-case metadata probe passed; no runtime/provider/native effect or worker repair/replay. Final first-result combined material range has15 paths (original13 plus checker2), following actual-SHA continuity6. Root corrective metadata helper first stopped on a Windows default-codepage read after partial documentary writes; exact preimages restored, UTF-8 explicit, no tests/effects replayed. Worker encoding inspection followed its initial patch and is recorded as partial preparation. BE-S10-G tracks this prerequisite; BE-S10 passive observer source work remains pending separate authority. Corrective normal hook attempt90/91 passed, active continuity failed because root move omitted explicit LHW24; existing marker restored, no new rule/checker or effect rerun.; fresh grant exhausted, BE-R02 remains open |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_r1c_be_r01_blocked_spent`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=Local PLAN named actual-result diagnostic only; no automatic source/effect grant only; role=INTERNAL_AGENT Local reviewer/closer/steward; phase=CONTINUITY; decision owner=LOCAL; parked checkpoint=cap1/any runtime retry/provider/deletion separately unadmitted; no generic operator checkpoint.

## Current Mode

Current mode marker: `cvf_ncr_html_r1c_be_r01_blocked_spent`
Current mode: `cvf_ncr_html_r1c_be_r01_blocked_spent`; previous mode marker: `cvf_ncr_html_r1c_be_r01_dispatched`

## Next Allowed Move

Mode: `cvf_ncr_html_r1c_be_r01_blocked_spent`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-B-E-R1C-RUNTIME-20261017. Reviewer adjudication complete; runtime acceptance remains blocked and grant spent. First material dbb07364863ea627c22b07fd23b62a574b10aea0/continuity e4497e82cafe81b302d30aa5cbaa2331f6397a35 passed normal91/91, but automatic P4 committed-range generation failed RIPA on root-selected invalid reviewer Status. That unsafe automatic result is retained, never promoted. Existing canonical Recurring Blocked-Return Escalation governs blocked worker returns; explicit completion_review negative adjudication is not a new worker return. The narrow existing checker correction retains generic finding validation, actual/ambiguous worker enforcement and original FIRST_OCCURRENCE worker bytes. Worker focused tests and distinct root five-case metadata probe passed; no runtime/provider/native effect or worker repair/replay. Final first-result combined material range has15 paths (original13 plus checker2), following actual-SHA continuity6. Root corrective metadata helper first stopped on a Windows default-codepage read after partial documentary writes; exact preimages restored, UTF-8 explicit, no tests/effects replayed. Worker encoding inspection followed its initial patch and is recorded as partial preparation. BE-S10-G tracks this prerequisite; BE-S10 passive observer source work remains pending separate authority. Next Local may adopt separately governed passive request observer source correction using the actual saved diagnostic and real delayed IncomingMessage-to-Request RED/GREEN proof; no runtime/provider/retry/cap1/deletion grant. Corrective material 187996f311383a63ce1fe13451f7f1bba9700177 committed; actual-SHA continuity6 and final combined15/6 split finality pending. gen9/SCECordinal2/counters2,0,2,0/blockers2/freeze/prior7 exclusions/LHW24 and R1/R2partial,R3/R4open,R5/R6deferred unchanged; old1spent/2retired never replayed.

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
