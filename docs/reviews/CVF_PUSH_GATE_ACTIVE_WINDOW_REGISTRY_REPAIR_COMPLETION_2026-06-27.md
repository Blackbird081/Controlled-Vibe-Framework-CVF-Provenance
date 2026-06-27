# CVF Push Gate Active Window Registry Repair Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: completion_review

Date: 2026-06-27

## Purpose

Record the bounded repair required after provenance pre-push checks exposed an
over-broad duplicate rotation-guard rule in the active-window registry gate.

## Target / Source

| Target | Source / evidence |
|---|---|
| Checker | `governance/compat/check_active_window_registry.py` |
| Focused test | `governance/compat/test_check_active_window_registry.py` |
| Registry evidence | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` |
| Pre-push failure | duplicate `governance/compat/check_active_archive_hygiene.py` on binding reference active windows |
| Authorization artifact | `docs/reviews/CVF_PUSH_GATE_ACTIVE_WINDOW_REGISTRY_REPAIR_COMPLETION_2026-06-27.md` |

## Scope / Applies-To

This completion applies only to the active-window registry checker and focused
unit test repair required for provenance pre-push.

It does not mutate the active-window registry, change hook ordering, add or
remove any checker, alter CI, mutate runtime code, or change roadmap state.

## Findings / Position

The registry intentionally contains multiple `BINDING_REFERENCE_ACTIVE_WINDOW`
records that share `governance/compat/check_active_archive_hygiene.py` as their
archive-protection checker.

The prior duplicate-rotation guard check treated those binding reference
windows as if each one needed a dedicated rotation guard. That rule is correct
for dedicated log/trace rotation windows, but too broad for binding reference
active windows protected by generic archive hygiene.

The repair keeps duplicate detection for dedicated rotation windows and allows
binding reference windows to share their archive-hygiene protection surface.

## Risk / Corrective Action

Risk is bounded to active-window registry validation. Corrective action is a
checker-scope refinement plus focused regression tests covering both the
allowed binding-reference sharing case and the still-blocked duplicate
dedicated rotation-guard case.

## Verification

| Command | Result |
|---|---|
| `python -m unittest governance.compat.test_check_active_window_registry` | PASS - 5 tests |
| `python governance/compat/check_active_window_registry.py --enforce` | PASS |
| `git diff --check` | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: push-gate checker repair authorized by operator request plus pre-push machine failure, not a standalone dispatched work order | N/A | N/A with reason |
| Completion review | `docs/reviews/CVF_PUSH_GATE_ACTIVE_WINDOW_REGISTRY_REPAIR_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PUSH_GATE_ACTIVE_WINDOW_REGISTRY_REPAIR_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Checker repair | `governance/compat/check_active_window_registry.py` | shared binding-reference class excluded from dedicated rotation-guard uniqueness | PASS |
| Focused regression test | `governance/compat/test_check_active_window_registry.py` | allowed binding-reference sharing and blocked dedicated duplicate cases covered | PASS |
| Roadmap state | N/A with reason: no roadmap status is changed by this checker repair | N/A | N/A with reason |
| Registry JSON | BLOCKED with reason: no registry JSON edit is authorized or required for this checker repair | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit is authorized or required for this checker repair | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source bundle or live proof is consumed | N/A | N/A with reason |
| System loop interlock | N/A with reason: no system-loop interlock registry edit is authorized or required | N/A | N/A with reason |
| Runtime/provider/live proof | N/A with reason: local checker/test repair only | N/A | N/A with reason |
| Public-sync content mutation | N/A with reason: public-sync remote was already current | N/A | N/A with reason |
| Session continuity | N/A with reason: active handoff sync follows separately if the material commit changes HEAD | N/A | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is an internal provenance pre-push checker repair and includes
private session/push context. Public-sync content mutation is not part of this
repair.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: active-window registry checker false
positive repair only.

Protected paths:

- `governance/compat/check_active_window_registry.py`
- `governance/compat/test_check_active_window_registry.py`

Operator authorization: user requested updating local CVF to GitHub for both
provenance and public; serial provenance pre-push gates exposed an active
window registry false positive before the provenance remote could be updated.

Rollback boundary: revert this active-window registry checker repair commit
only; do not revert prior material guidance, marker repairs, front-door sync,
or session-sync commits.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-27 provenance active-window pre-push repair |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, Python, git |
| Target paths | `governance/compat/check_active_window_registry.py`; `governance/compat/test_check_active_window_registry.py`; `docs/reviews/CVF_PUSH_GATE_ACTIVE_WINDOW_REGISTRY_REPAIR_COMPLETION_2026-06-27.md` |
| Allowed scope source | operator instruction to update local CVF to GitHub and pre-push gate failure on active-window registry false positive |
| Before status evidence | HEAD `08cacacf`; provenance push blocked before remote update |
| After status evidence | focused unit test and active-window registry gate pass |
| Diff evidence | `git diff --name-status` |
| Approval boundary | push-gate checker false-positive repair only |
| Claim boundary | checker/test repair only; no registry mutation, hook semantics expansion, runtime/provider/live proof, public-sync content mutation, generated workspace state mutation, or MPI-T6 runtime |
| Agent type | single-agent push-gate repair steward |
| Invocation ID | local Codex session 2026-06-27 provenance active-window registry repair |
| Expected manifest | `docs/reviews/CVF_PUSH_GATE_ACTIVE_WINDOW_REGISTRY_REPAIR_COMPLETION_2026-06-27.md`; `governance/compat/check_active_window_registry.py`; `governance/compat/test_check_active_window_registry.py` |
| Actual changed set | `docs/reviews/CVF_PUSH_GATE_ACTIVE_WINDOW_REGISTRY_REPAIR_COMPLETION_2026-06-27.md`; `governance/compat/check_active_window_registry.py`; `governance/compat/test_check_active_window_registry.py` |
| Manifest delta | MATCH |

## Claim Boundary

This completion closes only the active-window registry checker repair needed
for local provenance pre-push self-checks. It does not claim public export,
runtime behavior, new governance behavior, or downstream roadmap readiness.
