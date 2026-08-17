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
| Current authority evidence | `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json` `currentAuthority` |
| Freeze posture | `governance_kernel_freeze_recommended` |

## Startup Acknowledgment

Startup acknowledged: current mode=`rspb_ai_t12_capability_bootstrap_closure_evidence_bundle_validation_kernel_dispatched_manual_external_worker_pending_review`; active handoff=AGENT_HANDOFF_V59_2026-08-11.md; next allowed move=operator manually transfers the committed T12 work order to one exact-five-path no-commit external worker, then this reviewer independently reviews; parked checkpoint=runtime, environment I/O, rollback/executor, acquisition/install/mutation/action authority, credentials, adapters, provider/live, push/public/deploy/production.

## Current Mode

Current mode marker: `rspb_ai_t12_capability_bootstrap_closure_evidence_bundle_validation_kernel_dispatched_manual_external_worker_pending_review`
Current mode: `rspb_ai_t12_capability_bootstrap_closure_evidence_bundle_validation_kernel_dispatched_manual_external_worker_pending_review`
Previous mode: `tpgr_t0_shadow_active_next_absorption_tranche_selection`

## Next Allowed Move

Mode: `rspb_ai_t12_capability_bootstrap_closure_evidence_bundle_validation_kernel_dispatched_manual_external_worker_pending_review`; T12 is DISPATCH_READY at `141aaf1d6`, is the first post-activation TPGR work order, and retains the full legacy gate because T0 selective execution remains forbidden.
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
T8 is independently accepted closed bounded at `3b906862b`. Roadmap, finding overlay, and conditional reopen index now agree through T5-R6; the 140-row ledger segment is byte-identical. External CADP runtime is `PARKED_DEMAND_GATED`. The repo is documented cleanly for operator selection of a different repository, but no transfer/push/public/deploy/production action occurred or is authorized. Latest closed wave: `LHW24`.
RSPB-AI-T1/T2 are accepted bounded at `d591c542a`/`44a74fa48`. T3 at `bdec9c1e7` adds the non-executing controlled-acquisition kernel. T4-R1 is independently accepted at `a2f874519`: zero-threshold ambiguity, absolute material-authority routing, malformed readiness, and ambient-key live-test activation are fail-closed. Evidence includes 19/19 focused, 65/65 boundary, 597/597 credential-cleared package tests, 14 independent probes, and zero reviewer live calls. The worker's two unintended Alibaba calls remain incident-only with no repeat-live authority. Continue only by the next local-first material-value cluster; executor/mutation remains separately governed.
Mixed-origin absorption latency/value-preservation learning is enforced at `193c91404`: reuse fresh ledgers, review by capability cluster, preserve value until contradicted, skip extra value probes unless a named decision-changing gap exists, and keep the pass bounded. RSPB-AI-T5-R1 is independently accepted and materially committed at `1b2c11c9fd1a9795cd9d5bcf17c10806e98273fb` after one disclosed repair round, 27/27 focused tests, 104/104 composed tests, 624 passed plus 5 skipped package tests, 16/16 independent probes, and pre-commit 85/85. Continue with the next highest-value local synthesis cluster from the existing ledger; do not restart value proof from zero. No adapter, file export, executor, provider/live, public, or production authority is opened.
RSPB-AI-T6 is dispatched at `4789d1442ed280c91e3dd5e6e3c8995244db19ef` after pre-dispatch 77/77 and pre-commit 85/85. The external worker may edit only the exact four-path manifest and must return `COMPLETE_PENDING_REVIEW` without staging or committing. The current orchestrator/reviewer will independently inspect the diff, reproduce tests, and run adversarial probes before any repair, acceptance, closure, or material commit. The seam remains pure and proposal-only; no storage, promotion, mutation, runtime service, provider/live, public, or production authority is opened.
RSPB-AI-T6 material plus disclosed reviewer repair is committed at `2529cc8d3d71fc40dbd838acb0cf7335e6a7c9b1` and independently accepted pending closer. Evidence: focused 60/60, bridge 3/3, direct full package PASS, TypeScript PASS, reviewer-fast 64/64, pre-commit 85/85, and zero provider/live calls. Next move is bounded closure/session synchronization only.
RSPB-AI-T6 is `CLOSED_PASS_BOUNDED`; machine closure is committed at `145d9dab27ee2faf78a9a1cf1c97e4e7ef8fee15`. Its pure seam binds accepted T5 projection evidence to a provenance-bound pending learning candidate and the existing intake bridge. Continue with the next highest-value local cluster without restarting full-corpus proof; storage, promotion, mutation, runtime service, provider/live, public, and production authority remain unopened.
RSPB-AI-T7 is `CLOSED_PASS_BOUNDED`: material and reviewer repair `63b2f7367`, completion review `25b19b3d5`, machine closure `055252ddb`. Evidence: focused 26/26, composed 57/57, package 650 plus 5 skipped, TypeScript PASS, freshness CURRENT, reviewer-fast 64/64, pre-commit 85/85, zero provider/live calls. Continue with the next highest-value local cluster without restarting full-corpus proof; all runtime/external authority remains parked.
RSPB-AI-T11 is dispatched at `8996a4e0e74856e293ee5ba36fa310b57f50a030`: seven workspace profile/bootstrap policy template hashes matched, pre-dispatch passed 77/77, and pre-commit passed 85/85. The operator manually transfers the committed work order to one external worker. Worker scope is exactly five paths, no stage/commit, with `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`; this current reviewer/orchestrator independently owns inspection, proof, bounded repair, acceptance, commit, and closure. No template loading/copying, workspace materialization, filesystem/environment read, persistence, acquisition, installation, mutation, runtime/external authority, provider/live, public, or production action is opened.
RSPB-AI-T9 is `CLOSED_PASS_BOUNDED`: material and reviewer repair `5e5aeb8a4`, completion review `d34dce4c5`, machine closure `b78651eac`. Evidence: focused 42/42, T3/T8/T9 composed 105/105, package 743 plus 5 skipped, TypeScript PASS, freshness CURRENT, reviewer-fast 64/64, pre-commit 85/85, zero provider/live calls. Continue with the next highest-value local cluster without restarting full-corpus proof; all runtime/external authority remains parked.
## Parked Checkpoints

Live retry, external T5 adapter runtime, out-of-manifest production TypeScript edits, existing-guard edits, hook/autorun/CI wiring, provider/live, credential access, quota mutation, CLI/MCP invocation, public sync, deployment, production, trusted-evidence readiness and cross-runtime determinism claims remain parked.
T4 closed as standalone static checker work with no hook wiring or production-source mutation.
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
This compact current-only pointer carries no closed-tranche narrative; historical evidence lives in the dated archives listed above.
