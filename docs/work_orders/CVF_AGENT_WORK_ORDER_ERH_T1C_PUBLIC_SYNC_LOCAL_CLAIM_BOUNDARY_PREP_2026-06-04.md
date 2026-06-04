# CVF Agent Work Order - ERH-T1C Public-Sync Local Claim Boundary Prep

Memory class: POINTER_RECORD

Status: PUBLIC_SYNC_EXPORTED

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `7c7dfc52`

executionBaseHead: `7c7dfc52`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Execute the immediately available public-evaluation hardening layer from the
public-sync clone after operator instruction to handle the clean parts first.
This work order covers public-sync documentation preparation and public export
after explicit operator push authorization.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | chat instruction on 2026-06-04: handle immediate parts first | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| ERH-T1B handoff | `docs/reference/CVF_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- edit public-sync front-door documentation locally;
- add a public evaluation claim-boundary reference;
- update public catalog/index/known-limitations links and caveats;
- run public-safe documentation and public-surface gates;
- record private provenance evidence of the local public-sync preparation.

Forbidden scope:

- claim live governance proof;
- claim runtime route hardening;
- edit runtime/API behavior;
- consume provider secrets or live quota.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | bounded local public-sync documentation prep |
| Implementer | Codex | public-sync docs and manifest only |
| Reviewer | Codex self-review pending operator review | no live/runtime claim |
| Operator checkpoint | Operator | public push authorized on 2026-06-04 |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/reference/CVF_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` | public-sync wording seed |
| `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | claim calibration |
| `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | route coverage caveat |
| `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | CI caveat |
| `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | durability caveat |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git remote -v` in public-sync clone | origin is `Controlled-Vibe-Framework-CVF.git` |
| `git status --short` in public-sync clone | no unrelated dirty files |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 7c7dfc52 --head HEAD` | PASS in provenance |

## Write Ownership

| Owned surface | Mode |
| --- | --- |
| Public-sync front-door docs | local edit only |
| Public-sync public-surface manifest | local edit only |
| Private ERH T1C work order and completion packet | create/update |

Forbidden write ownership: runtime/API behavior, CI workflow hardening, provider
proof artifacts, public push.

## Execution Plan

| Step | Input | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | ERH T1B handoff | public evaluation boundary draft | missing public-sync remote |
| 2 | public front-door docs | README/GOVERNANCE/ARCHITECTURE/catalog caveats | runtime claim required |
| 3 | public limitations and manifest | L-009/L-010 and public-core handoff exception | public-surface scan fail |
| 4 | public gates | PASS evidence | public push requires operator authorization |

## Evidence Requirements

| Evidence | Path or command | Required result |
| --- | --- | --- |
| Public-sync remote | `git remote -v` | public repo remote |
| Changed-file list | `git status --short` in public-sync | docs/manifest delta only |
| Public-surface scan | `python scripts/check_public_surface.py` | PASS |
| Markdown/docs gates | public-sync markdown and docs checks | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Public-sync clone remote is public repo | canonical-command-evidence | `git remote -v` in public-sync clone | `Controlled-Vibe-Framework-CVF.git` | public-sync remote guard | ACCEPT |
| README public front door exists | canonical-public-sync-file-evidence | file exists in public-sync clone | `README.md` | public front door | ACCEPT |
| Governance public front door exists | canonical-public-sync-file-evidence | file exists in public-sync clone | `GOVERNANCE.md` | public governance summary | ACCEPT |
| Architecture public front door exists | canonical-public-sync-file-evidence | file exists in public-sync clone | `ARCHITECTURE.md` | public architecture summary | ACCEPT |
| Public catalog exists | canonical-public-sync-file-evidence | file exists in public-sync clone | `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | public product catalog | ACCEPT |
| Public limitations register exists | canonical-public-sync-file-evidence | file exists in public-sync clone | `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md` | public limitations register | ACCEPT |
| Public-surface scan exists | canonical-public-sync-file-evidence | file exists in public-sync clone | `scripts/check_public_surface.py` | public surface scanner | ACCEPT |

## New Doc-Only Fields

| Field/path | Owner surface | Disposition |
| --- | --- | --- |
| `docs/reference/CVF_PUBLIC_EVALUATION_CLAIM_BOUNDARY_2026-06-04.md` | public-sync docs reference | DOC_ONLY_NEW |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Verification | Status |
| --- | --- | --- | --- |
| Public claim calibration reaches public-facing docs | local public-sync doc delta | `git status --short` in public-sync clone | PASS |
| Route coverage overclaim is caveated publicly | public evaluation claim boundary and README/catalog caveats | public docs gate PASS | PASS |
| Static CI is not overread as live proof | public evaluation claim boundary and limitations register | public-surface scan PASS | PASS |
| Public export completed after operator push authorization | public commit `4730278fe269aec45482f9cad08f4d1e2721f53d` | PASS |

## Worker Autonomy / No-Question Rule

The worker may perform local public-sync documentation edits, rerun public
documentation gates, and publish after explicit operator push authorization.
Escalation is required for live proof, runtime/API changes, secrets/quota, or
stronger public claims.

## Evidence / Verification

Public-sync clone:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Remote guard:

```powershell
git remote -v
```

Public-safe verification:

```powershell
git diff --check
python scripts/check_public_surface.py
python governance/compat/check_markdown_structural_completeness.py --all-changed --enforce
python governance/compat/check_docs_governance_compat.py
```

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| Public evaluation boundary exists | `docs/reference/CVF_PUBLIC_EVALUATION_CLAIM_BOUNDARY_2026-06-04.md` in public-sync | PASS |
| README/catalog/governance surfaces link the boundary | public-sync changed-file list | PASS |
| Known limitations include route coverage and static CI caveats | limitations register delta | PASS |
| Public-surface scanner passes | `python scripts/check_public_surface.py` | PASS |
| Public push is operator-authorized | commit `4730278fe269aec45482f9cad08f4d1e2721f53d` pushed to public `main` | PASS |

## Review Gate

| Gate | Requirement |
| --- | --- |
| Public boundary | public docs push only; no live proof |
| Runtime boundary | changed files remain docs/manifest only |
| Export status | public docs delta is `EXPORTED`; private records remain provenance |

## Closure Checklist

| Item | Status |
| --- | --- |
| Public evaluation boundary added locally | PASS |
| Public front doors linked locally | PASS |
| Public-surface scan passed | PASS |
| Public push completed with operator authorization | PASS |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| Public remote is not `Controlled-Vibe-Framework-CVF.git` | BLOCKS_EXECUTION |
| Public docs claim live governance without live proof | BLOCKS_CLOSURE |
| Runtime/API files are changed under this work order | BLOCKS_CLOSURE |
| Public push is performed without operator push instruction | BLOCKS_CLOSURE |

## Return Conditions

Return to orchestrator if live proof, runtime/API hardening, CI workflow
hardening, or stronger public claims are requested.

## Operator Checkpoint

Public commit and push were authorized by the operator on 2026-06-04 and
completed from the public-sync clone.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| External-agent public review can overread route files and CI badges | OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | TEMPLATE_UPDATED | public evaluation boundary added locally |
| Public-surface scanner blocked public `AGENT_HANDOFF.md` without exception reason | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | manifest exception reason added for public-core pointer |

## Public Export Disposition

EXPORTED

Public-sync remote:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Public commit:

`4730278fe269aec45482f9cad08f4d1e2721f53d`

Public artifact paths:

- `README.md`
- `GOVERNANCE.md`
- `ARCHITECTURE.md`
- `docs/INDEX.md`
- `docs/reference/CVF_PUBLIC_EVALUATION_CLAIM_BOUNDARY_2026-06-04.md`
- `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md`
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- `governance/public-surface-manifest.json`

Next action: review GitHub public diff and open a separate runtime/CI hardening
work order only if stronger behavior claims are desired.

## Claim Boundary

This work order exports a public-sync documentation delta. It does not claim
live governance proof, runtime route hardening, production readiness, hosted
readiness, provider behavior, or CI workflow hardening.
