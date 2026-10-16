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
| Parent maintenance | Independent cap1 matrix9/26 PASS; old failures retained; next B-E source-release/prerequisite tranche ready for Local preparation |
| Freeze posture | `governance_kernel_freeze_recommended` |
## Startup Acknowledgment

Startup acknowledged: current mode=`cvf_ncr_html_cap1_control_accepted_b_e_source_release_entry`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next=Local enters B-E source-release/prerequisite tranche and carries admitted connected work through verification/commit; role=INTERNAL_AGENT Local reviewer/steward with distinct independent probe executor; phase=cap1 control proof accepted bounded, next tranche preparation ready; decision owner=Local; parked checkpoint=B-E/product/browser/container/provider/stage/parent/public/deploy effects require current before-effect admission. No micro-stops/manual relay; old/current control/native slots closed.

## Current Mode

Current mode marker: `cvf_ncr_html_cap1_control_accepted_b_e_source_release_entry`
Current mode: `cvf_ncr_html_cap1_control_accepted_b_e_source_release_entry`; previous mode marker: `cvf_ncr_html_cap1_source_accepted_independent_matrix_held`

## Next Allowed Move

Mode: `cvf_ncr_html_cap1_control_accepted_b_e_source_release_entry`

PROGRAM_ID=CVF-NCR; NEXT_ACTION_CLASS=PLAN; BATCH_ID=CVF-NCR-HTML-CAP1-COMPLETION-LOCAL-20261016. Material=e10c2698202fb3e9de65cd878d6a10022afba4a4; proof=docs/reviews/evidence/ncr-html-cap1-completion-local-20261016.json. NEXT_TRANCHE=NCR_HTML_B_E_SOURCE_RELEASE_AND_PREREQUISITE_QUALIFICATION; entry=READY_FOR_LOCAL_PREPARATION. Local enters the next tranche: current immutable source/profile release and exact pins, scoped Docker context/daemon/cached image and Chromium identity qualification, owned synthetic stage and prospective finite B-E effect/cleanup envelope. Continue admitted preparation/implementation/verification/commit without documentary micro-stops or manual relay; current receipt alone does not release product/runtime effects. Do not rewrite/repoint old pin evidence or refill old slots. Selected failed cap1 proof now resolved: source-reviewed corrected independent oracle, fake9cases/26calls/child0 PASS and fake receipt refused, actual9cases/26 inert children PASS. Receipt SHA2569fde97a251da6a94a8df86e337819b04a43e6e683e21bf8a3c44d55e77118e3c; raw commands/terminals precede assertions, separate digest and root joins/admission PASS. Source12 and old failed proof hashes stable, production edits0; prior121/65 source tests and distinct bounded native proof consumed at original revisions, no broad/native rerun. Old failed3-child control and Local native ACK failure remain historical failures, not upgraded. Fresh current operator completion grant root1/3/reviewer2/4 programs, matrix1/2, children26/52; no new matrix retry, unused slots retired. All old/new control/native windows closed. B-E/cap1 product journey/full parent/disposal/provider/public unproved and unreleased; no executable WO. Four-field currentAuthority R5 pair historical only. Same root NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF/source generation8/SCEC2/counters2,0,2,0/two blockers/freeze; no transition or independentCriticalEvidence. Earlier preparation PARTIAL_WITH_REASON retained, current probe full model preflight before actual children; all custody retained, no cleanup deletion. Prior7 P4 blocked/excluded rows retained, normal collector only. R1/R2partial,R3/R4open,R5/R6deferred; foundation active/extension NOT_APPLIED/projectOPEN; data/custody/business/send/B2/P11/public/deploy parked; LHW24 retained.

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
