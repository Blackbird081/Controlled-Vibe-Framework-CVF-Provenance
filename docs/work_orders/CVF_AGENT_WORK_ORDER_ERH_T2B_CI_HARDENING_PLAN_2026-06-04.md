# CVF Agent Work Order - ERH-T2B CI Hardening Plan

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED_SUPERSEDED_BY_ERH_CI1

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `b5cf8882`

executionBaseHead: `b5cf8882`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Dependency release: ERH-T2A ledger exists at
`docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md`.

## Purpose

Execute ERH-T2B by producing a CI hardening plan based on the current CI
workflow and the ERH-T2A route ledger. Success means CI gaps are prioritized
without editing workflows in this batch.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| GC-018 | `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| Dependency release | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- inspect `.github/workflows/cvf-ci.yml` and protected live gate workflow;
- create `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md`;
- propose follow-up CI work orders.

Forbidden scope:

- edit `.github/workflows/**`;
- claim CI is production-grade;
- run live provider proof or consume secrets/quota.

Risk ceiling: R0 docs-only plan.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | private ERH CI planning tranche |
| Implementer | Codex | docs-only CI plan |
| Reviewer | Codex self-review pending operator review | no workflow claim |
| Operator approval required for | workflow edits, public-sync, live proof, commit/push | not used |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | dependency release |
| `.github/workflows/cvf-ci.yml` | current CI source |
| `.github/workflows/cvf-protected-live-release-gate.yml` | live proof boundary |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `rg -n "lint|coverage|audit|public.*drift|check_" .github/workflows/cvf-ci.yml` | current gate scan |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b5cf8882 --head HEAD` | PASS |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | create/update |
| `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | create/update |

Forbidden paths: `.github/workflows/**`, runtime source, public-sync clone.

## Execution Plan

| Step | Input | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | T2A ledger | dependency release | missing T2A artifact |
| 2 | CI workflow scan | hardening plan | workflow edit required |
| 3 | governance gates | pending-review state | gate failure outside scope |

## Evidence Requirements

| Evidence | Path or command | Required at handoff |
| --- | --- | --- |
| CI plan | `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | Yes |
| Workflow scan | `rg` result over workflows | Yes |
| No workflow edit | `git diff --name-status` | Yes |

## Review Gate

| Gate | Requirement |
| --- | --- |
| Dependency release | T2A path exists |
| Workflow boundary | no `.github/workflows/**` diff |
| Pre-closure | N/A with reason: no commit in `WORKER_MUST_NOT_COMMIT` mode |

## Closure Checklist

| Item | Status |
| --- | --- |
| CI plan created | PASS |
| Protected live gate boundary preserved | PASS |
| Workflow edits avoided | PASS |
| Public export deferred | PASS |

## Return Conditions

Return to orchestrator if workflow edits, public-sync, live proof, dependency
installation, or production-grade CI claims are required.

## Operator Checkpoint

N/A with reason: docs-only CI plan remains inside autonomous private scope.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Main CI workflow exists | `.github/workflows/cvf-ci.yml` | file source | `cvf-ci.yml` | GitHub Actions workflow | ACCEPT |
| Web type check/build steps exist | `.github/workflows/cvf-ci.yml` | lines 93-97 | `npx tsc --noEmit` | `typecheck-web-ui` job | ACCEPT |
| Web test/build steps exist | `.github/workflows/cvf-ci.yml` | lines 232-236 | `test-web-ui` | `test-web-ui` job | ACCEPT |
| Protected live release gate exists | `.github/workflows/cvf-protected-live-release-gate.yml` | lines 1-70 | `run_cvf_release_gate_bundle.py --json` | protected live release workflow | ACCEPT |
| ERH-T2A route ledger exists | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | file source | `CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | route ledger | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Verification | Status |
| --- | --- | --- | --- |
| ERH-T2B CI hardening plan | `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | path exists after implementation | PASS |
| Depend on T2A | dependency release row | T2A path exists | PASS |
| No workflow edit in this tranche | forbidden scope and diff review | PASS |

## Worker Autonomy / No-Question Rule

The worker proceeds autonomously for workflow inspection, plan authoring, and
docs-only gate remediation. Escalation is reserved for workflow edits,
public-sync, live proof, provider quota, secrets, or production-readiness claim
expansion.

## Evidence / Verification

Required component gates:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base b5cf8882 --head HEAD --all-changed --enforce
python governance/compat/check_work_order_dispatch_quality.py --base b5cf8882 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base b5cf8882 --head HEAD --enforce
```

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| CI gaps are prioritized | T2B plan table | PASS |
| Protected live gate boundary is preserved | T2B plan | PASS |
| No workflow source is edited | `git diff --name-status` at review | PASS |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| T2B modifies `.github/workflows/**` | BLOCKS_CLOSURE |
| T2B implies production-grade CI without missing gates | BLOCKS_CLOSURE |
| T2B treats live gate as ordinary unprotected CI | BLOCKS_CLOSURE |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | `CLOSED_PASS_BOUNDED_SUPERSEDED_BY_ERH_CI1` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` and `docs/reviews/CVF_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | T2B docs closure plus ERH-CI1 successor | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH-T2B row `CLOSED_PASS_BOUNDED_SUPERSEDED_BY_ERH_CI1` | PASS |
| Registry JSON | `N/A with reason` | no corpus registry state changed by T2B CI-plan closure | BLOCKED with reason |
| Registry Markdown | `N/A with reason` | no corpus registry markdown state changed by T2B CI-plan closure | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no external digest consumed by T2B closure | N/A with reason |
| System loop interlock | `N/A with reason` | T2B is plan-only; successor ERH-CI1 owns GC-052 CI connection | N/A with reason |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up handoff sync commit required after closure commit | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| CI posture can imply more hardening than current workflow proves | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | propose CI hardening work order after docs plan |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance CI plan only.

Next action: public-sync can summarize CI boundary after public review.

## Claim Boundary

This work order is a CI hardening plan only. It does not edit workflows, run CI,
run live proof, or prove production readiness.
