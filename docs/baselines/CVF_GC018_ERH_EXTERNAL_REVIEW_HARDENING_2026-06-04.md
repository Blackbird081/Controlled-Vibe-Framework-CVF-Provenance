# CVF GC-018 - ERH External Review Hardening

Memory class: FULL_RECORD

Status: AUTHORIZED_DISPATCH_PACKET_WITH_PRIVATE_TRANCHE_OUTPUTS

docType: gc018_baseline

Date: 2026-06-04

dispatchBaseHead: `b5cf8882`

## Purpose

Authorize the External Review Hardening roadmap as a bounded private
provenance planning and documentation-hardening lane. ERH exists because an
external agent review of the public GitHub repository identified useful
public-surface gaps: claim boundaries, README/catalog structure, evidence
durability wording, route coverage proof, CI posture, and dependency-risk
decisioning.

## Scope / Target / Owner Boundary

Target: public GitHub evaluation readiness for CVF, as seen by external agents
reading `Blackbird081/Controlled-Vibe-Framework-CVF.git`.

Owner surfaces:

- private ERH planning artifacts in this provenance repository;
- future public-sync README/catalog work orders;
- route coverage and CI hardening evidence packets;
- explicit claim boundaries for mock landing-page content versus governance
  evidence.

Out of scope:

- public-sync execution from this provenance workspace;
- runtime fixes for audit durability, rate limiting, policy versioning, auth, or
  benchmark emission;
- live-provider proof unless a later implementation tranche asserts governance
  behavior;
- output-quality parity reopening or F-1 tuning.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-04: "claude đã đồng ý: Codex author ERH roadmap chính thức với fresh GC-018 + fresh paths" | ACCEPT |
| Planning review | `docs/assessments/CVF_ERH_PLANNING_REVIEW_FOR_CODEX_2026-06-04.md` | ACCEPT |
| Codex response | `docs/reviews/CVF_ERH_PLANNING_REVIEW_CODEX_RESPONSE_2026-06-04.md` | ACCEPT |
| Archived intake | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | ACCEPT_AS_SOURCE_EVIDENCE |
| External source artifact | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx` | ACCEPT_AS_REFERENCE |

## Source / Predecessor Evidence

| Predecessor | Evidence | ERH dependency |
| --- | --- | --- |
| External public-repo review | archived `.docx` source | seed findings only |
| Archived ERH intake | source-verified findings ledger | predecessor evidence, not live roadmap |
| Codex planning response | seven planning decisions | tranche split and B1/B2 disposition |
| F-1 closure | `docs/reviews/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md` | prevents output-quality parity overclaim |
| Public export standard | `docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` | public-sync boundary |

## Decision / Baseline / Proposed Tranche

Decision: authorize ERH as a fresh four-part roadmap with no dangling
2026-06-03 work-order links.

Baseline:

- ERH is about public GitHub structure and external-agent evaluation accuracy.
- Landing-page samples, if any, are mock orientation content for non-coders and
  not governance evidence.
- Runtime-adjacent findings are documentation/claim-boundary work in this
  roadmap unless a later fresh GC-018 authorizes implementation.
- Public README/catalog changes require a separate public-sync work order.

## Authorized Sequence

| Tranche | Work order | Goal | Dependency |
| --- | --- | --- | --- |
| ERH-T1A | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | private public-claim calibration packet | this GC-018 |
| ERH-T2A | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | route governance coverage ledger | this GC-018 |
| ERH-T3 | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | evidence durability claim-boundary packet | this GC-018 |
| ERH-T2B | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | CI hardening plan and optional workflow work-order proposal | ERH-T2A |
| ERH-T4 | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T4_NEXT_AUTH_BETA_DECISION_2026-06-04.md` | `next-auth` beta dependency decision record | ERH-T3 |
| ERH-T1B | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` | public-sync handoff; public execution still held | ERH-T1A, ERH-T2A, ERH-T3 |

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| ERH planning review exists | EXISTS | `docs/assessments/CVF_ERH_PLANNING_REVIEW_FOR_CODEX_2026-06-04.md` | file source | `CVF_ERH_PLANNING_REVIEW_FOR_CODEX_2026-06-04.md` | ERH planning review | ACCEPT |
| Codex response exists | EXISTS | `docs/reviews/CVF_ERH_PLANNING_REVIEW_CODEX_RESPONSE_2026-06-04.md` | file source | `CVF_ERH_PLANNING_REVIEW_CODEX_RESPONSE_2026-06-04.md` | ERH review response | ACCEPT |
| Archived intake exists | EXISTS | `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | file source | `CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | ERH archived intake | ACCEPT |
| Public-sync boundary standard exists | EXISTS | `docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` | file source | `Public Export Disposition` | public export standard | ACCEPT |

## Evidence / Verification

Required dispatch verification:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base b5cf8882 --head HEAD --all-changed --enforce
python governance/compat/check_work_order_dispatch_quality.py --base b5cf8882 --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base b5cf8882 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base b5cf8882 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b5cf8882 --head HEAD
```

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Public repo review can misread CVF without README/catalog claim boundaries | CLAIM_BOUNDARY_GAP | DOCUMENTATION_ONLY_LEARNING | ROADMAP_REQUIRED | ERH-T1A/T1B |
| Route governance coverage lacks complete public-facing evidence ledger | EVIDENCE_GAP | GOVERNANCE_CONTROL_PLANE | ROADMAP_REQUIRED | ERH-T2A |
| Runtime-adjacent evidence durability findings need claim boundary before runtime work | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DOCS_FIRST_OPERATOR_DECISION | ERH-T3 |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this GC-018 is private provenance authorization. It includes no
public-sync remote, public repository commit, or public artifact path evidence.

Next action: ERH-T1B must be a separate public-sync work order.

## Claim Boundary

This GC-018 authorizes ERH planning and documentation hardening only. It does
not implement runtime fixes, prove production readiness, run live governance
proof, publish public README/catalog changes, or reopen F-1 output-quality
parity work.
