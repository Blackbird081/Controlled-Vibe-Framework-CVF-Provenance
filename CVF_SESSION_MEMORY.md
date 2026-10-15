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
| Parent maintenance | Source/native binding corrected; independent actual Windows proof accepted bounded; Local failed ACK preserved; continue admitted steps through commit without micro-stops |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_native_binding_accepted_independent_cap1_admission_plan`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=Local consolidate cap1/source-admission plus B-E prerequisites and carry admitted steps through verification/commit; role=INTERNAL_AGENT Local implementer/reviewer/steward with distinct native probe executor; phase=source and independent native accepted bounded, Local failed ACK retained; decision owner=Local; parked checkpoint=actual B-E/product/browser/container/provider/stage/parent/public/deploy. No documentary micro-stops or manual relay; native slots spent.

## Current Mode

Current mode marker: `cvf_ncr_html_native_binding_accepted_independent_cap1_admission_plan`
Current mode: `cvf_ncr_html_native_binding_accepted_independent_cap1_admission_plan`; previous mode marker: `cvf_ncr_html_native_prerequisites_complete_source_contract_plan`

## Next Allowed Move

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-NATIVE-BINDING-LOCAL-20261016. Source/native material=cbf22efeba80f53fad754016a1be6268342e97f9; proof=docs/reviews/evidence/ncr-html-native-binding-local-20261016.json. Local next consolidates independent cap1 control/source-admission and B-E synthetic owned-profile prerequisites into one finite direct envelope, then continues admitted preparation/implementation/verification/commit without phase-by-phase operator stops. Keep real authority/effect checkpoints explicit; no manual implementation relay, new checker, broad hardening or old-slot refill. Current source11: lifecycle343 plus new focused test_win32258, other nine original code bytes retained. Snapshot/wait/enumeration/prior-count/post-open-thread-owner/primary+close contracts corrected. Final selected50 PASS/93deselected; old160/13/14 remains predecessor evidence, no whole suite replay. Distinct one-shot actual Windows64 Job/one-benign-child proof PASS: independent ABI/policy/identity, nonce ACK, retained-handle stop, signaled exit/empty members, all closes and exact2239-byte terminal/separate ACK. Local own native program remains FAIL_NATIVE: froze protocol before terminal ACK, FROZEN correctly refused write; no terminal bytes saved, no recovery/replay/upgrade. Procedure/preparation PARTIAL_WITH_REASON. Root5/6 and reviewer1/2 programs; native1/1 and child1/1 each,2 actual benign children total. Both native windows closed, no repeat slot. Product effects0; B-E/cap1/full parent/disposal unproved, old runtime source pins intentionally refuse changed lifecycle. New baseline consumed for this bounded outcome; no executable work order. Schema-required currentAuthority R5 pair is historical provenance only. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF, actual dependent source generation7; SCEC2/counters2,0,2,0/two blockers/freeze unchanged, no transition or independentCriticalEvidence. All failed source/native attempts and four exact fresh legacy-caller fixture relocations preserved in current custody; no historical data touched or outside-temp deletion attempted. Prior7 P4 blocked rows/exclusions preserved, use normal collector only, no manual rerun/promotion. R1/R2partial,R3/R4open,R5/R6deferred; foundation active/extension NOT_APPLIED/projectOPEN; data/custody/business/send/B2/P11/public/deploy parked; LHW24 retained.

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
