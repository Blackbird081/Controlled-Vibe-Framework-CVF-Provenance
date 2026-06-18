# CVF Session Continuity Rotation Guard Hardening Roadmap - 2026-06-15

Memory class: ROADMAP_PACKET

Status: ROADMAP_CLOSED_PASS_BOUNDED

## Purpose

Harden the session-continuity guard so future handoff rotations cannot leave a
superseded root `AGENT_HANDOFF*.md` file behind. The current worker return
showed the governance pattern clearly: the guard detects duplicate ACTIVE
handoffs and ARCHIVED root handoffs, but a root handoff marked SUPERSEDED can
survive until a reviewer performs a manual cleanup step.

## Foundation Value

This is CVF core control-plane work. It does not add a product use case, model
gateway feature, provider integration, or legacy absorption wave. It reduces
operator latency by moving a repeated reviewer cleanup risk into the earliest
machine-checkable phase.

## Authorization / Decision

Decision: proceed with a focused guard-hardening tranche before returning to
Model Gateway P4B. This is the highest-value foundation move because it applies
to every future orchestrator/worker/reviewer session rotation, regardless of
provider.

## Scope

In scope:

- Update `governance/compat/check_active_session_state.py` so any root
  `AGENT_HANDOFF*.md` other than the active handoff is a violation, regardless
  of status text.
- Preserve the existing exact-one-ACTIVE check and active registry mismatch
  check.
- Add focused tests in `governance/compat/test_check_active_session_state.py`
  for a root SUPERSEDED handoff and a root non-active handoff with unexpected
  status wording.
- Keep the remediation message operator-friendly: archive or delete the stale
  root handoff and keep archive-qualified references under
  `CVF_SESSION/handoffs/archive/`.

Out of scope:

- Runtime source outside `governance/compat/check_active_session_state.py`.
- Provider/API/live proof.
- Public-sync.
- Legacy absorption.
- Changes to Model Gateway routing behavior.
- Broad handoff format redesign.

## Non-Goals

- No product use-case implementation.
- No Model Gateway runtime behavior.
- No provider/model/live proof.
- No public-sync.
- No legacy scan or absorption.
- No rewrite of the active-session state schema.

## Design Control Gate

The implementation must preserve the existing active handoff registry model and
only tighten root handoff stale-file detection. The worker must not mutate
session state or handoff files while implementing the guard; tests must use
temporary fixtures.

## Source Findings

| Finding | Evidence | Disposition |
|---|---|---|
| Root handoff discovery already exists | `governance/compat/check_active_session_state.py` lines 272-273 `_root_handoff_paths()` | ACCEPT |
| Status parsing already exists | `governance/compat/check_active_session_state.py` lines 290-296 `_handoff_status()` | ACCEPT |
| Exact-one-ACTIVE logic exists | `governance/compat/check_active_session_state.py` lines 507-516 | ACCEPT |
| Current stale-root check only covers `Status: ARCHIVED` | `governance/compat/check_active_session_state.py` lines 517-526 | ACCEPT |
| Existing tests cover archived root stale files | `governance/compat/test_check_active_session_state.py` lines 238-250 | ACCEPT |

## Deliverables

| ID | Deliverable | Owner | Status |
|---|---|---|---|
| D1 | GC-018 baseline for this guard hardening | Codex | READY |
| D2 | Claude work order | Codex | READY |
| D3 | Guard implementation | Claude | CLOSED_PASS_BOUNDED |
| D4 | Focused unit tests | Claude | CLOSED_PASS_BOUNDED |
| D5 | Worker return with gate evidence | Claude | REQUIRED_AFTER_IMPLEMENTATION |
| D6 | Completion review and commit | Codex | REQUIRED_AFTER_WORKER_RETURN |

## Work Plan

| Step | Action | Owner |
|---|---|---|
| 1 | Verify source lines and test fixture pattern | Claude |
| 2 | Update stale root handoff detection | Claude |
| 3 | Add focused SUPERSEDED and unexpected-status tests | Claude |
| 4 | Run focused tests and fast return gate | Claude |
| 5 | Author worker return without commit | Claude |
| 6 | Review and commit | Codex |

## Acceptance Criteria

| ID | Criterion | Verification |
|---|---|---|
| AC-1 | A root `AGENT_HANDOFF*.md` that is not the registry active handoff fails even when status is `Status: SUPERSEDED` | Focused test |
| AC-2 | A root `AGENT_HANDOFF*.md` that is not the registry active handoff fails even when status is neither ACTIVE nor ARCHIVED | Focused test |
| AC-3 | Existing duplicate ACTIVE and ARCHIVED-root checks remain covered | Existing tests still pass |
| AC-4 | `python governance/compat/test_check_active_session_state.py` or the repo's pytest target for that file passes | Worker evidence |
| AC-5 | `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_active_session_state.py` passes, or the local equivalent is recorded with reason if the target invocation differs | Worker evidence |
| AC-6 | No runtime/provider/public-sync paths changed | `git diff --name-status` evidence |

## Verification / Evidence

Required evidence includes focused pytest output, fast return gate output,
changed file set, no-commit evidence, and an Agent Operation Trace Block in the
worker return.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: this roadmap changes internal provenance governance guards only. It is
not a public CVF product claim or runtime capability. No public-sync batch is
authorized.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this roadmap hardens an existing session continuity
machine guard. It does not absorb, reopen, or scope legacy knowledge.

## Finding-To-Governance Learning Disposition

| Finding | Learning lane | Escalation state | Next control action |
|---|---|---|---|
| Reviewer had to manually delete a root SUPERSEDED V18 handoff after compaction | Governance/control-plane learning | MACHINE_CHECK_CANDIDATE | Update `check_active_session_state.py` and focused tests so stale non-active root handoffs fail automatically |

## Claim Boundary

This roadmap authorizes only a focused guard and test hardening pass. It does
not authorize Model Gateway P4B, live-provider wiring, provider/model addition,
public-sync, legacy absorption, or broader session architecture redesign.

## GFC-T3 Closure Note (2026-06-18)

This roadmap is closed bounded per GFC-T3 Roadmap State Hygiene Remediation
(work order `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md`).
Closure evidence: `docs/reviews/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_COMPLETION_2026-06-15.md`
(status `REVIEW_PASS_BOUNDED`; session memory records this tranche as `CLOSED_PASS_BOUNDED`).
Status line updated from `ROADMAP_READY` to `ROADMAP_CLOSED_PASS_BOUNDED` by GFC-T3 worker.

## Current Runtime Freshness Verification

NOT_APPLICABLE_WITH_REASON: this roadmap's GFC-T3 closure note adds governance metadata only; no runtime source symbols were modified or introduced.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_FOR_CLAUDE_2026-06-18.md` | GFC-T3 work order authorizes this status-line change; GC-018 baseline approves scope | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GFC_T3_ROADMAP_STATE_HYGIENE_REMEDIATION_PACKET_2026-06-18.md` | worker packet Status: COMPLETE_PENDING_REVIEW; this row marked REMEDIATED | PASS |
| Roadmap state | `docs/roadmaps/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_ROADMAP_2026-06-15.md` | `Status: ROADMAP_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | governance-doc-only tranche | no GC-051 registry mutation authorized or required | BLOCKED with reason: governance-doc-only status remediation |
| Registry Markdown | governance-doc-only tranche | no registry markdown update authorized or required | BLOCKED with reason: governance-doc-only status remediation |
| External evidence digest | all evidence is repo-local and git-tracked | no external artifacts or digests needed | N/A with reason |
| System loop interlock | no runtime system loop required | no API interlock needed for governance status remediation | N/A with reason |
| Session continuity | session mode unchanged | no session state file modification authorized for GFC-T3 worker | N/A with reason |
| Tranche completion review | `docs/reviews/CVF_SESSION_CONTINUITY_ROTATION_GUARD_HARDENING_COMPLETION_2026-06-15.md` | `Status: REVIEW_PASS_BOUNDED`; session memory records `CLOSED_PASS_BOUNDED` | PASS |
| Public-sync | N/A with reason: private provenance, `DEFERRED_PRIVATE_ONLY` | N/A | N/A with reason |
