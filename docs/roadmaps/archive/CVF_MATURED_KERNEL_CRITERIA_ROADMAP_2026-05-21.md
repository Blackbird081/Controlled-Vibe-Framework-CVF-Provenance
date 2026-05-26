# CVF Matured Kernel Criteria Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_MATURED_KERNEL_CRITERIA_FILED

docType: roadmap

Date: 2026-05-21

---

## Purpose

Define a bounded strategic roadmap for turning
`freezePosture: governance_kernel_freeze_recommended` into an explicit
maturity model.

This roadmap answers the long-horizon question: when should CVF keep a
governance-kernel surface frozen, when may it be considered mature enough for a
one-surface release packet, and when should the freeze be treated as
effectively permanent?

It does not lift the freeze.

---

## Authority Chain

- Active state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- HN2.b owner map:
  `docs/reference/archive/CVF_GOVERNANCE_KERNEL_OWNER_MAP_2026-05-20.md`
- HN2.c freeze-release rule:
  `governance/toolkit/05_OPERATION/CVF_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE.md`
- HN2.c roadmap:
  `docs/roadmaps/archive/CVF_HN2C_GOVERNANCE_KERNEL_FREEZE_RELEASE_RULE_ROADMAP_2026-05-20.md`
- Post-Phase 2.B publicization readiness completion:
  `docs/reviews/CVF_POST_PHASE_2B_PUBLICIZATION_READINESS_COMPLETION_2026-05-21.md`
- Operator decision: 2026-05-21 approval to proceed with a matured-kernel
  criteria packet.

---

## Authorization / Decision

Decision: proceed with a documentation-only criteria tranche.

The operator accepted the recommendation to define matured-kernel criteria now
while avoiding any actual freeze lift. The resulting artifact may guide future
HN2.c one-surface release packets, but it cannot replace HN2.c conditions or
operator approval.

---

## Scope

In scope:

- Define `matured kernel` as a governance state, not a runtime claim.
- Define allowed posture labels for future review language.
- Define per-surface maturity criteria.
- Define permanent-freeze criteria.
- Define release-candidate criteria that feed HN2.c one-surface release
  packets.
- Record why global freeze lift remains prohibited.
- Sync active session state, review queue, and handoff.

Out of scope:

- Changing `freezePosture` in active state.
- Releasing any of the 12 kernel surfaces.
- Updating the HN2.b owner map.
- Replacing a kernel owner.
- Adding new kernel surfaces, roles, engines, memory tiers, receipt envelopes,
  provider semantics, or doctrine.
- Creating a mechanical guard.
- Public-sync or public-facing claim updates.

---

## Non-Goals

- Do not interpret maturity as production readiness.
- Do not interpret maturity as permission to bypass GC-018, rebuttal, or
  operator approval.
- Do not claim CVF has a globally matured kernel.
- Do not convert a surface from frozen to released in this tranche.
- Do not add a new machine-readable schema field to active state.

---

## Current Baseline

The current baseline is:

- `freezePosture` remains `governance_kernel_freeze_recommended`.
- HN2.b locked 12 governance-kernel surfaces and their owner classifications.
- HN2.c made global lift prohibited and one-surface release conditional.
- Phase 2.B closed adapter/receipt coverage and bounded runtime coherence, but
  those closures do not prove a mature kernel or authorize freeze release.

Current gap:

HN2.c defines the release process. It does not define a maturity scale that
helps future reviewers decide whether a release request is premature,
surface-specific, or should be permanently rejected.

---

## Roadmap Slices

### MKC-01 - Maturity Vocabulary

Define the posture labels future artifacts may use:

- `frozen_recommended`
- `maturity_candidate`
- `surface_release_candidate`
- `surface_released`
- `permanent_freeze_recommended`

Acceptance:

- Labels are defined as review vocabulary only.
- Labels do not alter active-state schema.
- `surface_released` is explicitly unreachable without HN2.c release.

### MKC-02 - Per-Surface Maturity Criteria

Define criteria across ownership, evidence, drift control, runtime behavior,
operator demand, review history, and public-claim safety.

Acceptance:

- Criteria are surface-specific and cite the HN2.b owner map.
- Criteria distinguish "stable enough to keep frozen" from "ready to request
  release".
- Runtime evidence is required only when a future release claim touches runtime
  behavior.

### MKC-03 - Permanent-Freeze Criteria

Define when a surface should remain frozen indefinitely.

Acceptance:

- Permanent freeze is framed as a recommendation, not an irreversible schema
  mutation.
- Doctrine supremacy and global-lift prohibition remain intact.

### MKC-04 - Release-Candidate Bridge

Define how maturity criteria feed a future one-surface HN2.c release packet.

Acceptance:

- HN2.c five release conditions remain mandatory.
- Maturity evidence can support, but cannot replace, evidence of harm,
  replacement design, different-role rebuttal, and operator approval.

### MKC-05 - Criteria Reference Filing

File a reference artifact that future work orders can cite.

Acceptance:

- Reference doc has `docType: reference`.
- Reference doc states no freeze is lifted.
- Completion review records the final boundary.

---

## Evidence Requirements

Required static evidence:

- HN2.b owner map reviewed for the 12 surfaces.
- HN2.c freeze-release rule reviewed for release conditions and global-lift
  prohibition.
- Criteria reference file created.
- Completion review filed.
- Active session state and review queue synced.
- Docs governance, markdown structural completeness, active-session, and local
  governance checks pass.

Live provider proof is not required because this tranche makes no runtime
governance behavior claim.

---

## Decision / Recommendation / Disposition

Disposition: close this roadmap as a criteria-only governance infrastructure
tranche.

Recommendation:

- Use the matured-kernel criteria before any future kernel-owner replacement or
  one-surface release request.
- Continue rejecting global freeze lift unless a later doctrine-level roadmap
  explicitly supersedes HN2.c with operator authorization.

---

## Work Plan

1. File GC-018 for matured-kernel criteria.
2. File work order with operator checkpoint and no-lift boundary.
3. Create `docs/reference/CVF_MATURED_KERNEL_CRITERIA_2026-05-21.md`.
4. File completion review.
5. Sync active state, review queue, and handoff.
6. Run governance checks.
7. Commit and push provenance changes.

---

## Acceptance Criteria

- Matured-kernel criteria reference exists and is cited by completion.
- No surface is released.
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` keeps
  `freezePosture: governance_kernel_freeze_recommended`.
- Global lift remains prohibited.
- Future release path still requires HN2.c one-surface release packet.
- Governance checks pass before commit.

---

## Claim Boundary

This roadmap defines criteria only. It does not prove CVF has a matured
kernel, does not release any kernel surface, does not update owner maps, does
not change doctrine, does not implement a guard, and does not create a
public-facing product or runtime claim.
