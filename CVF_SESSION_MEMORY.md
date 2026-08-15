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
3. `AGENT_HANDOFF_V59_2026-08-11.md`
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
| Active handoff | `AGENT_HANDOFF_V59_2026-08-11.md` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Pain-point closure direction | `docs/reviews/archive/CVF_REVIEW_CVF_PAIN_POINT_CLOSURE_DIRECTION_CODEX_2026-05-20.md` |
| Historical handoffs | `CVF_SESSION/handoffs/archive/` |
| Prior handoff (archive-qualified) | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V58_2026-08-11.md` |
| Latest front-door archive | `CVF_SESSION/handoffs/archive/CVF_SESSION_MEMORY_COMPACTION_ARCHIVE_2026-08-11.md` |
| Current authority (baseline/work order + hashes) | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` `currentAuthority` |
| Freeze posture | `governance_kernel_freeze_recommended` |

## Startup Acknowledgment

Startup acknowledged: current mode=`cadp_ai_t5_r6_read_only_authorization_consumer_value_decision_dispatched_worker_must_not_commit`; active handoff=AGENT_HANDOFF_V59_2026-08-11.md; next allowed move=execute the bounded R6 value/cost decision; parked checkpoint=route/registry/runtime mutation, live/provider/public/deploy/production work.

## Current Mode

`cadp_ai_t5_r6_read_only_authorization_consumer_value_decision_dispatched_worker_must_not_commit`
Current mode marker: `cadp_ai_t5_r6_read_only_authorization_consumer_value_decision_dispatched_worker_must_not_commit`
Current mode: `cadp_ai_t5_r6_read_only_authorization_consumer_value_decision_dispatched_worker_must_not_commit`
Previous mode: `cadp_ai_t5_r5_authentication_composition_implementation_accepted_bounded_route_registration_deferred`

## Next Allowed Move

Mode: `cadp_ai_t5_r6_read_only_authorization_consumer_value_decision_dispatched_worker_must_not_commit`
CADP-AI-T2A-R1 authority reconciliation is independently accepted
`CLOSED_PASS_BOUNDED` and materially committed at `944bfe852`. Grant v1
remains fail-closed; additive v2 is consumable from the reviewed current HEAD.
Completion review:
`docs/reviews/CVF_CADP_AI_T2A_AUTHORITY_RECONCILIATION_COMPLETION_2026-08-13.md`.
CADP-AI-T3A is independently accepted `CLOSED_PASS_BOUNDED` at `f1dc9a6f7`.
CADP-AI-T3B is independently accepted `CLOSED_PASS_BOUNDED` at `9a4920c92`.
CADP-AI-T4 is independently accepted at `7dfee6e4d`. CADP-AI-T5D is accepted
bounded and deferred at `ef84a1f6a`. CADP-AI-T7 selected hermetic scope is
accepted at `a49cebd8a`. T6 blocked evidence is accepted at `25c0b2217`: npm/
npx were absent, the local negative gate did not run, and zero provider calls
or quota were consumed. NVM4W was repaired by activating complete Node
v22.17.0. QTDM-01 is independently closed bounded at `9f57a431b`: active
surfaces target `qwen-flash`, historical live receipts do not transfer, and
fresh live revalidation remains required. Operator quota evidence committed at
`256fa5485` selects `qwen3.7-flash` (snapshot `qwen3.7-flash-2026-07-15`),
expiry `2026-10-22`. R1 blocked evidence is reviewer-accepted at `e85a1fa17`.
R2 is independently accepted `REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED` at
`2599ff10e`: exact `qwen3.7-flash`, one real SOT3 call, HTTP 200, strict
admission PASS, and historical receipt unchanged. The original bundle FAIL is
retained and excludes full release readiness. No repeat-live authority carries
forward. Model Gateway TS-next compatibility is fixed at `766c86d17`. T5-R1
authority foundation is independently accepted bounded at `7d96fa115` after
reviewer canonical-receipt repair, 121/121 focused regressions, and operator
disposition of the disclosed two-call reviewer test incident. The calls are not
T5 evidence and grant no repeat-live authority. T5-R2 is independently
accepted bounded at `ad76d7433` after reviewer repair of candidate-metadata
composition and deterministic malformed-input receipts. TypeScript, 69/69
focused tests, CADP drift 5/0, reviewer-fast 63/63, and pre-commit 84/84
passed. T5-R2A checker hardening is independently accepted bounded at `4f359cd2d`;
contract-source uniqueness remains fail-closed and T5-R1/T5-R2 now have independent
shared-root export proof. Tests passed 45/45, CADP drift 5/0, reviewer-fast 63/63,
and pre-commit 84/84. T5-R3 is independently accepted bounded as a decision-only
closure at `6ae59fa88`: `authorizeRouteGovernanceProof` is selected only as the
authentication-composition owner, not as CADP authorization or durable-receipt owner. T5-R4 contract hardening is independently accepted bounded at `af2f425d8`
with operator-selected Option A, `CADP_FAIL_CLOSED_ON_INVALID_TOKEN`. T5-R5 implementation is independently accepted bounded at `6284e5bd1` after reviewer repair of the Auth.js fail-closed invocation and test-count evidence.
TypeScript, 34/34 focused tests, CADP drift 5/0, reviewer-fast 63/63, and pre-commit 84/84 passed. No CADP route or registry row was added.
R6 is dispatched at `5110ea55d` as a documentation-only value/cost decision. The worker may write only the named decision and worker-return files and must not commit. Proceed to a later bounded system-chain packet only if all mandatory gates pass and the sensitivity-tested value margin is at least 12; otherwise stop or report a missing prerequisite. No route, registry row, runtime mutation, provider/live/network, credentials, public/deploy/production work is authorized. Latest closed wave: `LHW24`.

## Parked Checkpoints

Live retry, external T5 adapter runtime, out-of-manifest production TypeScript edits, existing-guard edits, hook/autorun/CI wiring, provider/live, credential access, quota mutation,
CLI/MCP invocation, public sync,
deployment, production, trusted-evidence readiness and cross-runtime
determinism claims remain parked. T4 closed as standalone static checker work
with no hook wiring or production-source mutation.
Prior unrelated checkpoints remain historical.

The `broad external knowledge absorption` lane remains outside the current
release. It is included in the `blocked work classes` unless the operator opens
a fresh, source-verified governed tranche.

## Targeted Lookup Rules

- For complete canonical state, read `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- For prior T2A closure narrative, read `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V58_2026-08-11.md`; do not restate it here.
- For pre-2026-08-11 front-door history, read the front-door archive above.
- For guard/task orientation, read `docs/reference/guard_orientation/README.md`.

## Claim Boundary
This is a compact current-only pointer record. It carries no closed-tranche
narrative; historical evidence lives in the dated archives listed above.
