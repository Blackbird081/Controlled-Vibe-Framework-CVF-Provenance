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
| Parent maintenance | Cap1/source fences corrected; independent matrix failed oracle after3 children; preserve failure and prepare connected fresh admission without micro-stops |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_cap1_source_accepted_independent_matrix_held`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=Local correct independent oracle vocabulary/preflight and consolidate fresh complete-matrix/B-E admission, then carry admitted work through commit; role=INTERNAL_AGENT Local implementer/reviewer/steward with distinct control reviewer; phase=source accepted bounded, independent actual matrix FAIL_ORACLE/incomplete; decision owner=Local; parked checkpoint=actual B-E/product/browser/container/provider/stage/parent/public/deploy. No micro-stops/manual relay; old control/native windows closed.

## Current Mode

Current mode marker: `cvf_ncr_html_cap1_source_accepted_independent_matrix_held`
Current mode: `cvf_ncr_html_cap1_source_accepted_independent_matrix_held`; previous mode marker: `cvf_ncr_html_native_binding_accepted_independent_cap1_admission_plan`

## Next Allowed Move

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-CAP1-ADMISSION-LOCAL-20261016. Source material=c379cb3c06219c483b5102a067f8de619ae2646a; proof=docs/reviews/evidence/ncr-html-cap1-admission-local-20261016.json. Local next prepares the corrected independent control oracle against actual protocol vocabulary and a fresh complete-matrix admission, joined with current B-E source/profile/tool requirements. Continue admitted preparation/implementation/verification/commit without per-documentary-step operator stops or manual relay. Current source12, six production/six oracles: exact int cap1 LOCAL_REVIEWER versus cap2 IMPLEMENTATION_WORKER; mandatory every current helper pin and comparison of all supplied source hashes before Git. Prior claim old pins necessarily rejected lifecycle drift was unsupported because helpers were excluded; corrected now, old46-pin manifest lacks two current oracles and refuses before Git. No old pin/proof rewrite or runtime release. Root RED33FAIL/32PASS then65PASS; connected121PASS/1deselected. Distinct one-shot actual inert attempt FAIL_ORACLE after3 reaped children: probe literal UNKNOWN differs from NOT_ACCEPTED_UNKNOWN; first-case terminal and receipt never saved. Preserve failure, no fabricated completion or accepted independent matrix. Root3/5 and reviewer1/2 programs, matrix1/1, children3/26, all remaining slots retired; no refill/replay. Prior native one-shot windows remain closed. Six tool paths and two dependencies present only, Docker daemon/image/Chromium/full staged source/B-E actual cleanup and journeys still unproved. Source acceptance bounded; no executable WO and no B-E/cap1 product/parent/disposal/provider/public release. CurrentAuthority four-field R5 pair historical only. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF, dependent source generation8, SCEC2/counters2,0,2,0/two blockers/freeze; no transition or independentCriticalEvidence. Procedure PARTIAL_WITH_REASON; original failures/raw custody retained, no cleanup/deletion attempted. Prior7 P4 blocked/excluded rows retained, normal collector only. R1/R2partial,R3/R4open,R5/R6deferred; foundation active/extension NOT_APPLIED/projectOPEN; data/custody/business/send/B2/P11/public/deploy parked; LHW24 retained.

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
