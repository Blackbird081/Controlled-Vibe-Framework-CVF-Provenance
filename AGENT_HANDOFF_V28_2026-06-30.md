# AGENT HANDOFF V28 - 2026-06-30

Status: ACTIVE HANDOFF
Memory class: active-handoff
Supersedes: `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V27_2026-06-29.md`

## Startup Acknowledgment

Startup acknowledged: current mode=`epsot_t1_provider_skill_trace_guard_closed_pending_next_skill_control_plane_decision`; active handoff=AGENT_HANDOFF_V28_2026-06-30.md; next allowed move=operator may choose a Skill Control Plane inventory/reconciliation tranche, another provider-skill governance tranche, another bounded package lifecycle promotion tranche, an explicitly scoped remaining-package batch, or a separate ACTIVE resolver/CLI-MCP adapter tranche through fresh GC-018/source-verified work order; parked checkpoint=EPSOT-T1 closed at material commit `701ebd94`; AGSK-R7 remains closed at material commit `19feb1f1`; LHW24 remains the latest closed numbered LHW wave.

## Current State

| Field | Value |
|---|---|
| Active front door | `CVF_SESSION_MEMORY.md` |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Canonical state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active review queue | `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` |
| Previous active handoff | `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V27_2026-06-29.md` |
| Remote tracking branch | `origin/codex/p1-p5-small-debt-remediation` |
| Latest material closeout | `701ebd94` EPSOT-T1 provider skill trace source-of-truth guard |
| Latest session-sync target | session sync after EPSOT-T1 material closure |
| Latest closed numbered LHW wave | `LHW24` |

## Current Mode

`epsot_t1_provider_skill_trace_guard_closed_pending_next_skill_control_plane_decision`

## Purpose

Keep the active handoff compact after V27 reached the governed file-size
near-threshold during AGSK-R7 session sync. V27 is archived as historical
continuity; V28 is the sole root active handoff and carries the current
EPSOT-T1 closure, AGSK-R7 package boundary, and next-move boundary.

## Scope / Target / Owner Boundary

Target: maintain active session continuity after EPSOT-T1 and preserve the
bounded provider-skill trace and package-loader claim boundaries.

Owner boundary: this handoff authorizes session continuity maintenance only. It
does not authorize package activation, runtime/provider/live work, public-sync
mutation, additional checker implementation, resolver mutation, provider-side
audit access, or generated aggregate mutation beyond active-session sync.

## Active Boundary

Active handoff: `AGENT_HANDOFF_V28_2026-06-30.md`.

Archived predecessor:
`CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V27_2026-06-29.md`.

Remote tracking branch: `origin/codex/p1-p5-small-debt-remediation`.

Exact remote SHA must be derived live from git when needed.

External agent memory files and provider-local memory are non-canonical
convenience only. Source facts for governed CVF work must be re-verified
against CVF-governed surfaces.

## Latest Work / Changes

Material commit `701ebd94` closed EPSOT-T1 provider skill trace
source-of-truth guard. It added:

- `docs/reference/CVF_EXTERNAL_PROVIDER_SKILL_SOURCE_OF_TRUTH_STANDARD_2026-06-30.md`
- `governance/compat/check_external_provider_skill_usage_trace.py`
- `governance/compat/test_check_external_provider_skill_usage_trace.py`
- reviewer-fast, pre-commit, and autorun catalog wiring

The guard requires changed governed artifacts that claim provider-owned
external skill output consumption to include an `External Provider Skill Usage
Trace` block with source-of-truth promotion evidence. It does not claim
provider runtime interception, provider-side audit access, live provider
behavior, package activation, resolver mutation, or adapter behavior.

Prior material commit `19feb1f1` closed AGSK-R7 runtime package batch promotion. It
promoted five additional package roots to APPROVED/PASSED/CERTIFIED/IMPLEMENTED
for explicit internal runtime-loader body reads only:
`cvf-engineering-planning-task-breakdown`,
`cvf-engineering-spec-driven-development`,
`cvf-engineering-test-driven-development`,
`cvf-engineering-debugging-error-recovery`, and
`cvf-engineering-security-hardening`.

Current audit evidence: 32 ASSF records, 24 package-root records, 6 runtime
eligible package roots, and 18 remaining package roots blocked by
`certificationState=NOT_STARTED`, `uatState=NOT_STARTED`, and
`internalAgentDisposition=CANDIDATE`.

Recent material chain:

- `701ebd94` EPSOT-T1 provider skill trace source-of-truth guard.
- `8caef205` AGSK-R6 code-review-quality pilot runtime package.
- `3a742e6e` AGSK-R5 runtime eligibility audit.
- `416eb689` AGSK-R4 runtime package loader.
- `4003289a` AGSK-R3 package roots.
- `50689173` AGSK-R2 agent-skills source mirror backfill.

## Next Allowed Move

Operator may choose a Skill Control Plane inventory/reconciliation tranche,
another provider-skill governance tranche, another bounded package lifecycle
promotion tranche, an explicitly scoped remaining-package batch, or a separate
ACTIVE resolver or CLI/MCP adapter tranche through fresh GC-018/source-verified
work order.

No provider runtime interception, provider-side audit access, automatic package
activation, resolver mutation, CLI/MCP adapter, provider/live proof,
public-sync, direct import, merge authority, commit authority, or
production-readiness claim is authorized.

## Parked Checkpoint

LHW24 remains the latest closed numbered LHW wave. Runtime/provider/live lanes,
package activation, adapter implementation, public-sync expansion, merge
automation, hook repair, policy-local runtime, and production-readiness claims
remain parked unless a recorded reopen condition is verified through a fresh
governed tranche.

## Core Guard Self-Protection Authorization - EPSOT-T1 Session Sync

Authorized guard-maintenance scope: update active session continuity after
EPSOT-T1 material commit `701ebd94`, regenerate active session state, and align
front-door, bootstrap read model, and active handoff next-move wording.

Operator authorization: session-sync is required by the mandatory startup
front-door, GC-020 in-place handoff HEAD rule, and active-session generated
aggregate discipline after the operator-approved EPSOT-T1 material tranche
closed.

Protected paths:

- `AGENT_HANDOFF_V28_2026-06-30.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/epsotT1ProviderSkillTraceGuardClosure20260630.json`

Rollback boundary: revert this session-sync commit only; do not revert material
commit `701ebd94`, AGSK-R7 material commit `19feb1f1`, AGSK-R6 material commit
`8caef205`, AGSK-R5 material commit `3a742e6e`, AGSK-R4 material commit
`416eb689`, or AGSK-R3 material commit `4003289a` unless reviewer reopens those
closures.

## GC-020 Marker - EPSOT-T1 Provider Skill Trace Guard Material Closure

Material commit `701ebd94` closed EPSOT-T1 provider skill trace
source-of-truth guard. Full material SHA:
`701ebd94c713b21669c037823372fdc148219191`

This marker satisfies the GC-020 in-place handoff HEAD rule for material commit
`701ebd94`. It does not authorize provider runtime interception, provider-side
audit access, automatic package activation, resolver mutation, CLI/MCP adapter,
provider/live proof, public-sync export, direct import, merge authority, commit
authority, or production-readiness.

## Agent Operation Trace Block - EPSOT-T1 Session Sync

| Field | Evidence |
|---|---|
| Actor | Codex session-sync steward |
| Provider or surface | Codex local workspace |
| Session or invocation | EPSOT-T1 session sync, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | active-session source edits, active-session generator, governance gates |
| Target paths | active session continuity surfaces and active V28 handoff |
| Allowed scope source | GC-020 after EPSOT-T1 material commit `701ebd94` plus generated active-session state discipline |
| Before status evidence | material commit `701ebd94` closed EPSOT-T1 |
| After status evidence | session-sync paths pending commit |
| Diff evidence | `git diff --name-status` before session-sync commit |
| Approval boundary | session continuity only; no runtime/package/resolver/provider activation |
| Claim boundary | repo-local continuity update only; no runtime/provider/public claim |
| Agent type | session-sync steward |
| Invocation ID | `epsot-t1-session-sync-2026-06-30` |
| Expected manifest | `AGENT_HANDOFF_V28_2026-06-30.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/epsotT1ProviderSkillTraceGuardClosure20260630.json` |
| Actual changed set | `AGENT_HANDOFF_V28_2026-06-30.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/epsotT1ProviderSkillTraceGuardClosure20260630.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Core Guard Self-Protection Authorization - AGSK-R7 Session Sync And Handoff Rotation

Authorized guard-maintenance scope: update active session continuity after
AGSK-R7 material commit `19feb1f1`, rotate V27 into the handoff archive because
it reached the governed file-size near-threshold, create this compact V28
active handoff, regenerate active session state, and align front-door,
bootstrap read model, AGENTS routing, and active handoff next-move wording.

Operator authorization: session-sync and handoff rotation are required by the
mandatory startup front-door, GC-020 in-place handoff HEAD rule, and governed
file-size guard after the operator-approved AGSK-R7 material tranche closed.

Protected paths:

- `AGENT_HANDOFF_V28_2026-06-30.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V27_2026-06-29.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/state/entries/agskR7RuntimePackageBatchPromotionClosure20260630.json`
- `AGENTS.md`

Rollback boundary: revert this session-sync commit only; do not revert material
commit `19feb1f1`, AGSK-R6 material commit `8caef205`, AGSK-R5 material commit
`3a742e6e`, AGSK-R4 material commit `416eb689`, or AGSK-R3 material commit
`4003289a` unless reviewer reopens those closures.

## GC-020 Marker - AGSK-R7 Runtime Package Batch Material Closure

Material commit `19feb1f1` closed AGSK-R7 runtime package batch promotion. Full
material SHA:
`19feb1f19ee6321890ea3a2773273737d32d2c68`

This marker satisfies the GC-020 in-place handoff HEAD rule for material commit
`19feb1f1`. It does not authorize automatic package activation, resolver
mutation, CLI/MCP adapter, provider/live proof, public-sync export, direct
import, merge authority, commit authority, or production-readiness.

## Agent Operation Trace Block - AGSK-R7 Session Sync And Handoff Rotation

| Field | Evidence |
|---|---|
| Actor | Codex session-sync steward |
| Provider or surface | Codex local workspace |
| Session or invocation | AGSK-R7 session sync and handoff rotation, 2026-06-30 |
| Working directory | repository root |
| Command or tool surface | active-session source edits, active-session generator, git mv, governance gates |
| Target paths | active session continuity surfaces, AGENTS routing, archived V27, and active V28 handoff |
| Allowed scope source | GC-020 after AGSK-R7 material commit `19feb1f1` plus governed file-size guard |
| Before status evidence | material commit `19feb1f1` closed AGSK-R7; V27 reached near-threshold when touched |
| After status evidence | V28 active handoff and session-sync paths pending commit |
| Diff evidence | `git diff --name-status` before session-sync commit |
| Approval boundary | session continuity and handoff rotation only; no runtime/package/resolver activation |
| Claim boundary | repo-local continuity update only; no runtime/provider/public claim |
| Agent type | session-sync steward |
| Invocation ID | `agsk-r7-session-sync-handoff-rotation-2026-06-30` |
| Expected manifest | `AGENT_HANDOFF_V28_2026-06-30.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V27_2026-06-29.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/agskR7RuntimePackageBatchPromotionClosure20260630.json`; `AGENTS.md` |
| Actual changed set | `AGENT_HANDOFF_V28_2026-06-30.md`; `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V27_2026-06-29.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/state/entries/agskR7RuntimePackageBatchPromotionClosure20260630.json`; `AGENTS.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | V27 moved to handoff archive; V28 created as sole active root handoff |

## GC-020 Marker - AGSK-R7 Session Sync Commit

Session-sync commit `7abcc4be` updated active session continuity after AGSK-R7
material commit `19feb1f1`. Full session-sync SHA:
`7abcc4bed92e453998aea27d51ddb96c50eca5ec`

At session-sync authoring time, mode is:
`agsk_r7_runtime_package_batch_promotion_closed_pending_next_runtime_decision`

At session-sync authoring time, next allowed move is: operator may select
another bounded package lifecycle promotion tranche, choose an explicitly scoped
remaining-package batch, or open a separate ACTIVE resolver or CLI/MCP adapter
tranche through fresh GC-018/source-verified work order.

This marker exists only to satisfy the GC-020 in-place handoff HEAD rule for
the session-sync commit. It does not authorize automatic package activation,
resolver mutation, CLI/MCP adapter, provider/live proof, public-sync export,
direct import, merge authority, commit authority, or production-readiness.

## GC-020 Marker - AGSK-R7 Handoff-Sync-Only Commit

This handoff-sync-only commit records parent session-sync commit `7abcc4be`.
Because the current commit SHA cannot be known before commit creation, the
active-session checker may accept the parent SHA for this dedicated handoff-only
sync commit.

This marker does not authorize automatic package activation, resolver mutation,
CLI/MCP adapter, provider/live proof, public-sync export, direct import, merge
authority, commit authority, or production-readiness.

## Claim Boundary

V28 is a compact continuity handoff and session-sync carrier. It records
EPSOT-T1 closure, AGSK-R7 package boundary, and next allowed moves only. It
does not create provider runtime interception, provider-side audit access,
runtime activation, automatic resolver behavior, external adapter behavior,
live provider proof, public export, merge authority, commit authority, or
production readiness.
