# CVF ERH External Review Hardening Roadmap

Memory class: FULL_RECORD

Status: INITIAL_PRIVATE_TRANCHES_CLOSED_PASS_BOUNDED_PUBLIC_SYNC_EXPORTED_T2C_CI1_PD1_CLOSED_PASS_BOUNDED_DEP1_ACCEPTED_BOUNDED_AUD1_CLOSED_PASS_BOUNDED_SAF1_DISPATCH_READY

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
| Work orders | ERH-T1A/T2A/T3/T2B/T4/T1B initial private tranches closed bounded; ERH-T1C exported; ERH-T2C, ERH-CI1, and ERH-PD1 closed bounded; ERH-DEP1 closed bounded; ERH-AUD1 closed bounded; ERH-SAF1 dispatch ready | private tranche outputs reviewed and closed; public-sync delta exported; runtime route workflow, CI public-evaluation workflow, and public-surface drift workflow closed bounded; dependency-risk workflow closed as `ACCEPT_WITH_CAVEAT`; dependency-audit remediation closed as `AUDIT_REDUCED_WITH_RESIDUALS`; ERH-RS1 recommended `ERH-SAF1_READY` and SAF1 is dispatched as deterministic safety workflow-chain hardening |

## Tranche Plan

| Tranche | Goal | Primary output | Status |
| --- | --- | --- | --- |
| ERH-T1A | Private public-claim calibration | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | CLOSED_PASS_BOUNDED |
| ERH-T2A | Route governance coverage ledger | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | CLOSED_PASS_BOUNDED |
| ERH-T3 | Evidence durability docs-only boundary | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | CLOSED_PASS_BOUNDED |
| ERH-T2B | CI hardening plan | `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | CLOSED_PASS_BOUNDED_SUPERSEDED_BY_ERH_CI1 |
| ERH-T4 | Dependency decision | `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | CLOSED_PASS_BOUNDED |
| ERH-T1B | Public-sync README/catalog handoff | `docs/reference/CVF_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` | CLOSED_PASS_BOUNDED_HANDOFF_PUBLIC_SYNC_EXPORTED |
| ERH-T1C | Public-sync claim-boundary export | `docs/reviews/CVF_ERH_T1C_PUBLIC_SYNC_LOCAL_CLAIM_BOUNDARY_PREP_COMPLETION_2026-06-04.md` | PUBLIC_SYNC_EXPORTED |
| ERH-T2C | Route governance proof workflow chain hardening | `docs/reviews/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_COMPLETION_2026-06-04.md` | CLOSED_PASS_BOUNDED |
| ERH-CI1 | CI public-evaluation workflow chain | `docs/reviews/CVF_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | CLOSED_PASS_BOUNDED |
| ERH-PD1 | PUBLIC_SURFACE_DRIFT_WORKFLOW | `docs/reviews/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | CLOSED_PASS_BOUNDED |
| ERH-DEP1 | Dependency risk workflow chain for `next-auth` beta posture | `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | ACCEPTED_BOUNDED |
| ERH-AUD1 | `cvf-web` dependency-audit remediation workflow | `docs/reviews/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_COMPLETION_2026-06-04.md` | CLOSED_PASS_BOUNDED |
| ERH-RS1 | External review full-coverage rescan | `docs/reviews/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_COMPLETION_2026-06-04.md` | CLOSED_PASS_BOUNDED |
| ERH-SAF1 | Safety workflow-chain hardening | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md` | DISPATCH_READY |
| ERH-SAF2 | Post-SAF1 safety follow-up decision | N/A until SAF1 completion review | HOLD_UNTIL_SAF1_PASS |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order path |
| --- | --- |
| ERH-T1A private claim calibration | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` |
| ERH-T2A route coverage ledger | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` |
| ERH-T3 evidence durability claim boundary | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` |
| ERH-T2B CI hardening plan | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` |
| ERH-T4 dependency decision | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T4_NEXT_AUTH_BETA_DECISION_2026-06-04.md` |
| ERH-T1B public-sync handoff | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` |
| ERH-T1C public-sync local claim-boundary prep | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1C_PUBLIC_SYNC_LOCAL_CLAIM_BOUNDARY_PREP_2026-06-04.md` |
| ERH-T2C route governance proof hardening | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_2026-06-04.md` |
| ERH-CI1 CI public-evaluation workflow chain | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_2026-06-04.md` |
| ERH-PD1 public-surface drift workflow chain | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md` |
| ERH-DEP1 dependency risk workflow chain | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md` |
| ERH-AUD1 dependency-audit remediation workflow | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_FOR_CLAUDE_2026-06-04.md` |
| ERH-RS1 external review full-coverage rescan | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_FOR_CLAUDE_2026-06-04.md` |
| ERH-SAF1 safety workflow-chain hardening | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md` |
| ERH-SAF2 post-SAF1 safety follow-up decision | N/A with reason: SAF2 cannot be opened until SAF1 completion review records exactly one SAF2 verdict |

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| E1 | Author fresh GC-018 and roadmap | baseline + roadmap | COMPLETE |
| E2 | Author ERH-T1A work order | T1A work order + claim packet | CLOSED_PASS_BOUNDED |
| E3 | Author ERH-T2A work order | T2A work order + route ledger | CLOSED_PASS_BOUNDED |
| E4 | Author ERH-T3 work order | T3 work order + durability packet | CLOSED_PASS_BOUNDED |
| E5 | Sequence T2B/T4/T1B after dependencies | T2B plan, T4 baseline, T1B handoff | CLOSED_PASS_BOUNDED |
| E6 | Prepare and export immediate public-sync claim-boundary delta | T1C work order and completion packet | PUBLIC_SYNC_EXPORTED |
| E7 | Implement bounded route governance proof workflow chain for five T2A missing-proof routes | registry-backed helper, five route updates, GC-052 connection, focused tests, release gate, completion packet | CLOSED_PASS_BOUNDED |
| E8 | Convert CI hardening plan into bounded public-evaluation workflow chain | checker, tests, hook/autorun wiring, GC-052 connection, completion packet | CLOSED_PASS_BOUNDED |
| E9 | Convert public/private ERH claim drift into bounded workflow chain | drift ledger, checker, tests, hook/autorun wiring, GC-052 connection, completion packet | CLOSED_PASS_BOUNDED |
| E10 | Implement dependency risk workflow chain for `next-auth` beta posture | reference, ledger, checker, tests, hook/autorun wiring, GC-052 connection, completion packet | ACCEPTED_BOUNDED |
| E11 | Close `cvf-web` dependency-audit remediation workflow | ledger, workflow chain, checker, tests, bounded package-update diff, completion packet | CLOSED_PASS_BOUNDED |
| E12 | Dispatch ERH-SAF1 deterministic safety workflow-chain hardening | fresh GC-018 and Claude work order with SAF2 decision checkpoint | DISPATCH_READY |

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
- Public-sync documentation preparation is recorded in ERH-T1C and exported to
  the public repository after explicit operator push authorization.
- ERH-T2C local runtime proof hardening is recorded as focused-test evidence
  only and exported publicly as a bounded summary, not live governance proof or
  complete route coverage.
- ERH-CI1 public-evaluation CI posture is machine-checked as
  `READY_WITH_BOUNDARIES`, not production-grade CI or public readiness.
- ERH-PD1 public-surface drift posture is machine-checked as
  `PUBLIC_SUMMARY_EXPORTED_BOUNDED`: ERH-T2C and ERH-CI1 have a bounded public
  summary at public commit `73f1da98e1a5fcc55c3124ff7c5a633193df5322`. This
  is not public readiness.
- ERH-DEP1 dependency-risk workflow-chain implementation is
  `ACCEPTED_BOUNDED` with decision `ACCEPT_WITH_CAVEAT`. It records that no
  stable v5 migration target exists and classifies the current risk as
  API-stability beta risk, not a `next-auth` CVE. It does not authorize
  `next-auth` migration, auth runtime edits, public-sync, production auth
  stability, or public readiness.
- ERH-AUD1 is closed bounded for `cvf-web` dependency-audit remediation. It
  reduced audit findings from 14 to 3, eliminated critical/high findings, and
  classified the remaining moderate residuals as major-version gated. It does
  not authorize `next-auth` migration, auth runtime edits, public-sync, full
  CVE clearance, production security readiness, or public readiness.
- ERH-RS1 is closed bounded with `COMPLETE_VERIFIED` coverage of the external
  review source: 162/162 paragraphs, 22/22 sections, 17/17 findings, and all
  five section 4.4 architectural weaknesses disposed. It recommends
  `ERH-SAF1_READY`.
- ERH-SAF1 is dispatch ready for deterministic severity-classified safety
  workflow-chain hardening. It does not authorize ML DLP, comprehensive
  jailbreak-protection claims, provider behavior changes, public-sync, hosted
  readiness, production security readiness, or public readiness.
- ERH-SAF2 remains `HOLD_UNTIL_SAF1_PASS`. It may be opened only after SAF1
  completion records exactly one SAF2 verdict: `SAF2_READY`, `SAF2_HOLD`, or
  `SAF2_NOT_NEEDED`.
- ERH initial private docs-only tranches are closed bounded in
  `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md`.
  T1A/T2A/T3/T2B/T4/T1B no longer carry review-pending status. T2B is
  superseded by ERH-CI1 for workflow-chain evidence, and T1B was consumed by
  T1C/public summary export.

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
- SAF2 is implemented before SAF1 completion evidence exists and is reviewed.
- SAF1 claims ML DLP, comprehensive jailbreak protection, hosted readiness,
  production readiness, public readiness, or public security certification.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Archived intake had absent live roadmap/work-order links | DOCUMENTATION_GAP | DOCUMENTATION_ONLY_LEARNING | RULE_CLARIFIED | use fresh paths and `PENDING_AUTHORING` |
| Public repo can be evaluated against wrong claim boundary | CLAIM_BOUNDARY_GAP | DOCUMENTATION_ONLY_LEARNING | ROADMAP_REQUIRED | ERH-T1A/T1B |
| Runtime-adjacent weaknesses need docs-first handling | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DOCS_FIRST_OPERATOR_DECISION | ERH-T3 |

## Public Export Disposition

EXPORTED

Public-sync remote:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Public-sync commit:

`73f1da98e1a5fcc55c3124ff7c5a633193df5322`

Public artifact paths:

- `README.md`
- `GOVERNANCE.md`
- `ARCHITECTURE.md`
- `docs/INDEX.md`
- `docs/reference/CVF_PUBLIC_EVALUATION_CLAIM_BOUNDARY_2026-06-04.md`
- `docs/reference/CVF_ERH_PUBLIC_SYNC_SUMMARY_2026-06-04.md`
- `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md`
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- `governance/public-surface-manifest.json`

Next action: keep DEP2 / next-major remediation separate. Open it only when the
operator authorizes auth/runtime or major-version dependency migration.
Public-sync summary for ERH-T2C and ERH-CI1 is exported bounded at public
commit `73f1da98e1a5fcc55c3124ff7c5a633193df5322`.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | six ERH initial private work orders plus ERH-AUD1 work order | initial private work orders and ERH-AUD1 no longer carry review-pending status | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` and `docs/reviews/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_COMPLETION_2026-06-04.md` | initial private closure `CLOSED_PASS_BOUNDED`; AUD1 decision `AUDIT_REDUCED_WITH_RESIDUALS` | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | roadmap status includes `INITIAL_PRIVATE_TRANCHES_CLOSED_PASS_BOUNDED`, `T2C_CI1_PD1_CLOSED_PASS_BOUNDED`, and `AUD1_CLOSED_PASS_BOUNDED`; E2-E5 and E7-E11 closed bounded or accepted bounded | PASS |
| Registry JSON | `N/A with reason` | no corpus registry state changed; AUD1 is dependency-audit closure, not corpus/search/classification closure | BLOCKED with reason |
| Registry Markdown | `N/A with reason` | no corpus registry state changed; AUD1 is dependency-audit closure, not corpus/search/classification closure | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no external corpus/source digest consumed by AUD1 | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | ERH-T2C route proof, ERH-CI1 public-evaluation, ERH-PD1 public-surface drift, and ERH-AUD1 checker connections added | PASS |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up handoff sync commit required after closure commit | PASS |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update the ERH-PD1 public-surface drift
checker snapshot and focused checker test after the bounded public-sync summary
was pushed.

Protected paths:

- `governance/compat/check_erh_public_surface_drift_workflow.py`
- `governance/compat/test_check_erh_public_surface_drift_workflow.py`

Operator authorization: operator requested the separate public-sync summary for
public GitHub, and this checker update records the resulting public commit
`73f1da98e1a5fcc55c3124ff7c5a633193df5322`.

Rollback boundary: revert this provenance status update and the public commit
`73f1da98e1a5fcc55c3124ff7c5a633193df5322` if the summary must be withdrawn.

Validation:

- `python governance/compat/check_erh_public_surface_drift_workflow.py --enforce`
- `python -m pytest governance/compat/test_check_erh_public_surface_drift_workflow.py -q`
- `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit`

## Claim Boundary

This roadmap authorizes ERH planning, closed bounded initial private tranche
records, public-sync documentation export, bounded ERH-T2C route-governance
proof workflow closure, bounded ERH-CI1 CI public-evaluation workflow closure,
bounded ERH-PD1 public-surface drift workflow closure, ERH-DEP1 dependency-risk
workflow closure, and ERH-AUD1 dependency-audit remediation closure. It does
not prove live governance behavior for every route, hosted behavior, production
readiness, production-grade CI, full CVE clearance, auth migration completion,
or public readiness.
