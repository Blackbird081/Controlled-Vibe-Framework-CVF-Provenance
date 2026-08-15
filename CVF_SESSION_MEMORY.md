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

Startup acknowledged: current mode=`cadp_ai_t6_environment_repaired_qwen_migration_required`; active handoff=AGENT_HANDOFF_V59_2026-08-11.md; next allowed move=author fresh Qwen-Turbo deprecation migration packet; parked checkpoint=live retry, T5 implementation, CLI/MCP, public sync, deploy and production.

## Current Mode

`cadp_ai_t6_environment_repaired_qwen_migration_required`

Current mode marker: `cadp_ai_t6_environment_repaired_qwen_migration_required`
Current mode: `cadp_ai_t6_environment_repaired_qwen_migration_required`
Previous mode: `cadp_ai_t6_blocked_environment_qwen_migration_required`

## Next Allowed Move

Mode: `cadp_ai_t6_environment_repaired_qwen_migration_required`

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
v22.17.0; PowerShell and Python now resolve npm/npx 10.9.2. Do not retry live.
Author a fresh migration packet to
replace active Qwen-Turbo authority with `qwen-flash` while preserving immutable
historical receipts. T5 remains deferred. Latest closed
numbered LHW wave: `LHW24`.

## Parked Checkpoints

Live retry, T5 adapter implementation, production TypeScript edits, existing-guard
edits, hook/autorun/CI wiring, provider/live, credential access, quota mutation,
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
- For prior T2A closure narrative, read
  `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V58_2026-08-11.md`; do not
  restate it here.
- For pre-2026-08-11 front-door history, read the front-door archive above.
- For guard/task orientation, read
  `docs/reference/guard_orientation/README.md`.

## Claim Boundary

This is a compact current-only pointer record. It carries no closed-tranche
narrative; historical evidence lives in the dated archives listed above.
