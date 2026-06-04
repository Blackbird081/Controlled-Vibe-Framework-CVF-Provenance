# CVF ERH External Review Hardening Roadmap

Memory class: FULL_RECORD

Status: PRIVATE_TRANCHES_COMPLETE_PUBLIC_SYNC_HOLD

docType: roadmap

Date: 2026-06-04

GC-018: `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md`

dispatchBaseHead: `b5cf8882`

## Purpose

Turn the external public-repo review into a source-backed hardening path for
the public GitHub surface. The goal is not to advertise CVF, but to make the
public repository easier for another agent to evaluate accurately: what CVF is,
what evidence exists, what is private-only, what is mock/web-facing orientation,
and what remains weak or deferred.

## Authorization / Decision

Authorized by operator instruction on 2026-06-04 and fresh GC-018:

`docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md`

Decision: author fresh ERH roadmap paths and avoid using the archived 2026-06-03
intake links as live dispatch packets.

## Scope / Target / Owner Boundary

Target: public GitHub evaluation readiness for CVF.

Owner surfaces:

- private ERH packets in this provenance repo;
- future public-sync README/catalog work from the public-sync clone;
- route governance coverage ledger;
- CI hardening plan;
- dependency risk decision record.

Boundary:

- Web landing-page mock usage samples, if later used, are non-coder orientation
  content only and not governance evidence.
- Public GitHub README/catalog content must distinguish public snapshot,
  private provenance, evidence status, claim boundaries, and known gaps.

## Scope

In scope:

- private claim-calibration packet;
- route coverage ledger for web API routes;
- docs-only evidence durability boundary;
- CI hardening plan and possible follow-up work-order proposal;
- `next-auth` beta dependency decision;
- public-sync handoff packet for README/catalog work.

Out of scope:

- public-sync execution from this workspace;
- runtime implementation;
- provider/live proof;
- production readiness;
- hosted readiness;
- output-quality parity tuning.

## Non-Goals

- do not claim CVF output-quality superiority;
- do not treat mock landing-page examples as evidence;
- do not present private provenance state as already public;
- do not convert lexical route hits into route governance proof;
- do not edit public README/catalog without a public-sync work order.

## Current State

| Surface | Evidence | State |
| --- | --- | --- |
| External review source | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx` | archived |
| Intake findings | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | archived source evidence |
| Planning review | `docs/assessments/CVF_ERH_PLANNING_REVIEW_FOR_CODEX_2026-06-04.md` | reviewed |
| Codex response | `docs/reviews/CVF_ERH_PLANNING_REVIEW_CODEX_RESPONSE_2026-06-04.md` | recorded |
| Fresh GC-018 | `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | authorized |
| Work orders | ERH-T1A/T2A/T3/T2B/T4/T1B authored | private tranche outputs prepared; public-sync execution held |

## Tranche Plan

| Tranche | Goal | Primary output | Status |
| --- | --- | --- | --- |
| ERH-T1A | Private public-claim calibration | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | COMPLETE_PENDING_REVIEW |
| ERH-T2A | Route governance coverage ledger | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | COMPLETE_PENDING_REVIEW |
| ERH-T3 | Evidence durability docs-only boundary | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | COMPLETE_PENDING_REVIEW |
| ERH-T2B | CI hardening plan | `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | COMPLETE_PENDING_REVIEW |
| ERH-T4 | Dependency decision | `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | COMPLETE_PENDING_REVIEW |
| ERH-T1B | Public-sync README/catalog update | `docs/reference/CVF_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` | HOLD_PUBLIC_SYNC_EXECUTION |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order path |
| --- | --- |
| ERH-T1A private claim calibration | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` |
| ERH-T2A route coverage ledger | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` |
| ERH-T3 evidence durability claim boundary | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` |
| ERH-T2B CI hardening plan | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` |
| ERH-T4 dependency decision | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T4_NEXT_AUTH_BETA_DECISION_2026-06-04.md` |
| ERH-T1B public-sync execution | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` |

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| E1 | Author fresh GC-018 and roadmap | baseline + roadmap | COMPLETE |
| E2 | Author ERH-T1A work order | T1A work order + claim packet | COMPLETE |
| E3 | Author ERH-T2A work order | T2A work order + route ledger | COMPLETE |
| E4 | Author ERH-T3 work order | T3 work order + durability packet | COMPLETE |
| E5 | Sequence T2B/T4/T1B after dependencies | T2B plan, T4 baseline, T1B handoff | COMPLETE_WITH_PUBLIC_SYNC_HOLD |

## Acceptance Criteria

- Fresh GC-018 exists and does not cite dangling 2026-06-03 roadmap/work-order
  paths as live dispatch packets.
- Fresh roadmap exists and marks all work orders `PENDING_AUTHORING` until
  actually created.
- Public-sync execution is isolated to a later public-sync work order.
- Mock web-facing samples are explicitly not governance evidence.
- F-1 output-quality parity remains closed-not-met.
- Runtime-adjacent issues remain docs-only unless a later fresh runtime work
  order authorizes implementation.
- Public-sync execution remains held in a separate public-sync work order and
  has not been performed from this provenance workspace.

## Verification / Evidence

Roadmap authoring verification:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base b5cf8882 --head HEAD --all-changed --enforce
python governance/compat/check_work_order_dispatch_quality.py --base b5cf8882 --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base b5cf8882 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base b5cf8882 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b5cf8882 --head HEAD
```

Live proof requirement: N/A with reason. This roadmap authoring step makes no
live governance behavior claim and performs no runtime/provider change.

## Failure Conditions

Return to orchestrator if:

- a worker treats `PENDING_AUTHORING` as a real work-order path;
- public-sync is attempted from the provenance workspace;
- landing-page mock examples are cited as governance evidence;
- route coverage is claimed without complete route ledger;
- runtime durability, rate limit, policy versioning, auth, or benchmark emission
  changes are made inside docs-only tranches;
- output-quality parity is reopened without fresh explicit operator authority.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Archived intake had absent live roadmap/work-order links | DOCUMENTATION_GAP | DOCUMENTATION_ONLY_LEARNING | RULE_CLARIFIED | use fresh paths and `PENDING_AUTHORING` |
| Public repo can be evaluated against wrong claim boundary | CLAIM_BOUNDARY_GAP | DOCUMENTATION_ONLY_LEARNING | ROADMAP_REQUIRED | ERH-T1A/T1B |
| Runtime-adjacent weaknesses need docs-first handling | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DOCS_FIRST_OPERATOR_DECISION | ERH-T3 |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap only. No public-sync remote, public commit,
or public artifact path evidence is included.

Next action: ERH-T1B must open from the public-sync clone after private claim
calibration is source-backed.

## Claim Boundary

This roadmap authorizes ERH planning and future work-order authoring. It does
not close ERH findings, implement runtime changes, prove live governance
behavior, publish public README/catalog updates, or claim production/public
readiness.
