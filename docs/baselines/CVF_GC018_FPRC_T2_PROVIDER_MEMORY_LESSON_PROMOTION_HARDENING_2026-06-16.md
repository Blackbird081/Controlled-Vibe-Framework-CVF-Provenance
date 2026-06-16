# GC-018 FPRC-T2 Provider Memory Lesson Promotion Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-16

Owner: Codex

rawMemoryReleased: false

## Purpose

Authorize a bounded governance hardening pass after the operator identified
that Claude recorded reusable B7/B8/B9 gate lessons in Claude-only memory and
only proposed governed escalation after being asked.

This packet closes the missing control loop: reusable lessons may not remain
only in provider-local memory, `MEMORY.md`, chat summaries, or worker-local
continuity notes.

## Operator Authorization

Operator instruction on 2026-06-16: proceed with CVF foundation hardening and
handle the findings before moving to the next roadmap.

Operator finding: Claude stated that B7/B8/B9 were written to Claude-only
memory and future same-kind work would be faster, proving those lessons were
reusable but not yet promoted into a CVF-governed artifact.

## Decision / Baseline / Proposed Tranche

Decision: execute FPRC-T2 immediately as a bounded combined-role governance
hardening tranche.

Baseline: FPRC-T1 already added the provider-memory learning escape guard, but
the PLCS-T2 worker-return loop showed the rule was still too permissive for
provider-local `MEMORY.md` and reusable-lesson `N/A_WITH_REASON` escape.

Proposed tranche: update the FPRC standard, the work-order authoring addendum,
the finding-to-governance checker, and focused checker tests. Close with a
review packet and update the FPRC roadmap.

## Scope

In scope:

- update the FPRC standard with the reusable-lesson promotion rule;
- update the work-order authoring addendum with B7/B8/B9 guidance;
- patch the finding-to-governance checker for `MEMORY.md` and reusable-lesson
  `N/A_WITH_REASON` escape;
- add focused regression tests;
- record completion evidence and update the FPRC roadmap.

Out of scope:

- runtime/source changes outside `governance/compat`;
- provider/API/live proof or credential use;
- public-sync or public catalog updates;
- historical migration of older artifacts;
- registry edit, PLCS/FPC runtime work, Model Gateway redispatch, production
  readiness, or public readiness.

## Source Authority

| Source | Role |
|---|---|
| `AGENTS.md` Provider-Specific Agent Memory Boundary | Provider-local memory is not CVF source of truth |
| `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | Existing FPRC-T1 provider-memory learning escape rule |
| `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` | Existing authoring addendum owner |
| `governance/compat/check_finding_to_governance_learning.py` | Existing machine gate owner |
| `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md` | FPRC roadmap owner |
| Operator instruction, 2026-06-16 | FPRC-T2 authorization |

## Findings

| ID | Finding | Disposition |
|---|---|---|
| B7 | Exact section-heading strings in checklist prose can confuse substring-based section extraction. | Promoted to addendum guidance |
| B8 | `NOT_APPLICABLE_WITH_REASON` can be the wrong verdict when closure-target terms appear elsewhere in a decision/dispatch artifact. | Promoted to standard/addendum guidance |
| B9 | `CLOSED_PASS_BOUNDED` in predecessor status rows can trigger closure-packaging behavior before current closure. | Promoted to addendum guidance |
| B10 | Reusable lessons captured only in Claude memory or `MEMORY.md` (`NOT_CVF_SOURCE`) remain invisible to other agents. | Promoted to standard and machine check |

## Acceptance Criteria

| ID | Criterion | Result |
|---|---|---|
| AC1 | `MEMORY.md` (`NOT_CVF_SOURCE`) is treated as provider-local memory unless CVF explicitly governs it. | PASS |
| AC2 | `N/A_WITH_REASON` no longer waives reusable provider-memory lessons. | PASS |
| AC3 | B7/B8/B9 authoring guidance is written into a CVF-governed artifact. | PASS |
| AC4 | Focused tests prove the new guard behavior. | PASS |
| AC5 | No runtime/provider/live/public/registry scope is introduced. | PASS |

## Evidence / Verification

Required evidence:

- focused pytest for `governance/compat/test_check_finding_to_governance_learning.py`;
- finding-to-governance checker self-run on the material range;
- closure autorun and steward gates after material commit;
- completion review with Core Guard Self-Protection Authorization because
  `governance/compat/*.py` files are protected guard/control files.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `MACHINE_GATE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `STANDARD_UPDATED`; `MACHINE_CHECK_ADDED`; `TEMPLATE_UPDATED` |
| Next control action | Future worker returns and work orders that claim reusable lessons in provider memory must promote them into CVF-governed artifacts or fail the checker |
| Worker blame | `N/A_WITH_REASON`: this is a control-chain gap; the operator caught that the guard was still too permissive |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.

## Claim Boundary

This GC-018 authorizes FPRC-T2 governance hardening only. It does not prove
runtime behavior, provider behavior, live governance behavior, public readiness,
production readiness, registry mutation, or historical artifact migration.
