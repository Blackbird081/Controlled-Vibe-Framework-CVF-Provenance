# ADIF-0013 - Upstream Push Debt Range Backlog

Memory class: POINTER_RECORD

Status: ACTIVE

EPISTEMIC_PROCESS_NA_WITH_REASON: ADIF registry entry; canonical sources and
trace evidence are recorded, but this entry does not perform a separate
evidence-comparison process.

```text
defectId: ADIF-0013
title: Upstream push debt range backlog
defectCategory: STATE_CONTINUITY
defectClass: RULE_GAP
defectRole: NOT_APPLICABLE_WITH_REASON: general reviewer/closer and session-sync steward sequencing pattern
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Push-readiness preview; Closure; Session-sync
roles: reviewer; closer; session-sync steward
lifecyclePhases: pre-closure; pre-push
surfaceSelectors: governed branch with upstream tracking branch and local commits ahead of upstream
detectionSignals: preview discloses ahead count as WARN above the advisory threshold; actual missing authorization, unreconciled remote commits or stale continuity requires targeted repair; commit count alone is not a defect
enforcementLevel: MACHINE_CHECKED
checkerBindings: governance/compat/run_agent_push_readiness_preview.py
promotionState: MACHINE_CHECK_ADDED
supersedes: NONE
lastVerifiedCommit: 42ffa4f6
roadmapSeedId: NONE
```

## Purpose

Record the failure pattern where an agent completes multiple governed tranches
locally but defers upstream push until the branch contains a long unpushed
stack. Once material commits, protected session-sync commits, handoff rotation,
and guard authorization artifacts accumulate in one unpublished range, the
pre-push path becomes hard to repair because each sub-range can require a
different authorization or commit shape.

Operator revision, 2026-10-11: a large unpublished stack is not itself a defect.
The actionable defect is an actual missing scope authorization, stale continuity
or malformed per-tranche range discovered at sync. Ahead count is machine-reported
advisory context, not a prohibition on continuing local work. The historical
June control was overly broad and is superseded by this current remediation.

## Scope / Applies To

Applies to governed CVF branches with an upstream tracking branch when an
agent is acting as reviewer, closer, or session-sync steward. Does not apply
to intentionally untracked scratch branches where `--skip-upstream` is used
and the reason is recorded in the closure packet.

## Bad Example

Accumulate local tranches and later assert push readiness without reconciling
actual scope/continuity, or force a push/stop new work solely because ahead > 2.
Commit count cannot establish either safety or a violation.

## Good Example

Keep material and continuity commits separate within each admitted tranche.
Continue local work until the operator-selected sync checkpoint. Then disclose
upstream..HEAD and ahead/behind, verify real authorizations and continuity, run
canonical push checks and push only with the existing effect authorization.
An ahead-count WARN alone needs no exception or worker interruption.

## Canonical Sources

- `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`:
  upstream push-debt rule and required preview command
- `governance/compat/run_agent_push_readiness_preview.py`:
  `DEFAULT_UPSTREAM_AHEAD_WARNING` and `_upstream_status`
- `docs/reference/guard_orientation/README.md`:
  Push-readiness preview task-class row and common failure pattern
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`:
  material/session-sync commit separation discipline

## Remediation

Run preview at planned sync checkpoints, before push or for a named range issue.
An ahead-only WARN does not fail --enforce and permits admitted local continuation.
Hold dependent push for missing/unreadable upstream or unreconciled remote commits;
repair concrete authorization/continuity/shape failures under their owners.
The historical 2-commit stop rule is withdrawn, not replaced by a larger hard cap.

## Historical Agent Operation Trace Block - 2026-06-27

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | provenance push debt standardization, 2026-06-27 |
| Working directory | repository root |
| Command or tool surface | git status, git rev-list upstream readout, apply_patch, focused pytest |
| Target paths | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0013.md`; `docs/reference/agent_defect_intelligence/entries/README.md` |
| Allowed scope source | operator instruction to standardize the provenance push-debt lesson so other agents cannot repeat it |
| Before status evidence | branch was 27 commits ahead of `origin/codex/p1-p5-small-debt-remediation`; push-readiness preview showed upstream `behind_ahead=0 27` |
| After status evidence | ADIF entry added and preview helper updated to machine-fail upstream push debt over the default limit |
| Diff evidence | new-file creation plus README row in this commit |
| Approval boundary | ADIF entry and push-debt prevention guidance only |
| Claim boundary | records and machine-binds one sequencing defect pattern; does not push, rewrite history, or authorize public-sync |
| Agent type | reviewer/closer |
| Invocation ID | cvf-adif-0013-upstream-push-debt-2026-06-27 |
| Expected manifest | this entry, plus README table row |
| Actual changed set | this entry, plus README table row |
| Manifest delta | MATCH |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local Codex maintainer |
| Provider or surface | private shared workspace |
| Session or invocation | operator count-policy revision, 2026-10-11 |
| Working directory | repository root |
| Command or tool surface | source read, apply_patch, focused pytest and maintenance gates |
| Target paths | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0013.md`; `docs/baselines/CVF_GC018_PUSH_BACKLOG_ADVISORY_2026-10-11.md` |
| Allowed scope source | direct operator request and that GC-018 authorization |
| Before status evidence | clean HEAD 3700b4ee949af6a216b2f74b652fc027f7a72ba3, ahead 2 / behind 0 |
| After status evidence | ahead-only WARN is nonblocking; 17 focused tests passed |
| Diff evidence | exact named-owner policy/helper/test and active-window binding changes; historical trace retained above |
| Approval boundary | authorized local maintenance, no push grant |
| Claim boundary | static policy checks; no worker/provider/live/public proof |
| Agent type | INTERNAL_AGENT maintainer |
| Invocation ID | cvf-push-backlog-advisory-20261011 |
| Expected manifest | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0013.md`; `docs/baselines/CVF_GC018_PUSH_BACKLOG_ADVISORY_2026-10-11.md` |
| Actual changed set | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json`; `governance/compat/run_agent_push_readiness_preview.py`; `governance/compat/test_run_agent_push_readiness_preview.py`; `docs/reference/CVF_AGENT_PUSH_READINESS_PREVIEW_STANDARD_2026-06-27.md`; `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`; `docs/reference/guard_orientation/README.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0013.md`; `docs/baselines/CVF_GC018_PUSH_BACKLOG_ADVISORY_2026-10-11.md` |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance ADIF entry. No public-sync claim.

## Claim Boundary

This entry records one observed sequencing defect pattern and its confirmed
checker binding. It does not modify git history, push any branch, authorize
runtime/provider/live work, or replace the canonical pre-push autorun gate.
