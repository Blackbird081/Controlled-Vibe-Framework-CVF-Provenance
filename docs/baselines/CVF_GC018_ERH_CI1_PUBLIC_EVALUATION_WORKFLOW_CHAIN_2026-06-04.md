# CVF GC-018 ERH-CI1 Public Evaluation Workflow Chain Baseline

Memory class: FULL_RECORD

Status: IMPLEMENTATION_AUTHORIZED

docType: baseline

Date: 2026-06-04

baseHead: `40c3c10d`

## Purpose

Authorize a bounded ERH-CI1 tranche that converts the ERH-T2B CI hardening plan
from a docs-only queue into a repeatable public-evaluation workflow chain.

## Scope / Target / Owner Boundary

Allowed scope:

- add a marker-based CI public-evaluation workflow-chain checker;
- add focused checker tests;
- wire the checker into agent autorun and local hook chains;
- add one GC-052 system-loop connection;
- add private workflow-chain reference, work order, and completion packet;
- update the ERH roadmap and T2B plan status/boundary.

Forbidden scope:

- no public-sync clone edits;
- no `.github/workflows/**` rewrites;
- no dependency installation or dependency migration;
- no hosted, production, or public-readiness claim;
- no ordinary live-provider CI claim.

Risk ceiling: R1 governance/checker workflow-chain implementation.

## Source / Predecessor Evidence

| Source | Purpose | Disposition |
| --- | --- | --- |
| `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | upstream CI hardening plan | ACCEPT |
| `docs/reference/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_WORKFLOW_CHAIN_2026-06-04.md` | route-governance workflow predecessor | ACCEPT |
| `.github/workflows/cvf-ci.yml` | main type/build/test CI markers | ACCEPT |
| `.github/workflows/cvf-web-ci.yml` | web lint/coverage CI markers | ACCEPT |
| `.github/workflows/cvf-static-ci.yml` | static governance CI marker | ACCEPT |
| `.github/workflows/cvf-protected-live-release-gate.yml` | protected manual live gate marker | ACCEPT |

## Decision

Proceed. The current repository has enough foundation to elevate CI posture from
plan-only hardening into a bounded workflow chain because source-visible
workflow lanes already exist for main type/build/test, web lint/coverage,
static governance gate, documentation governance, protected manual live release
gate, and ERH-T2C route-governance workflow traceability.

## Acceptance Criteria

| Criterion | Evidence |
| --- | --- |
| Checker exists | `governance/compat/check_erh_ci_public_evaluation_workflow.py` |
| Checker has focused tests | `governance/compat/test_check_erh_ci_public_evaluation_workflow.py` |
| Hook/autorun wiring exists | `run_local_governance_hook_chain.py`; `run_agent_autorun_workflow_gate.py` |
| System-loop connection exists | `erh-ci-plan-to-public-evaluation-workflow-chain` |
| Public claim remains bounded | completion review and chain reference |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: ERH-CI1 may add one new governance checker,
one focused checker test, and wire that checker into existing local hook and
agent autorun chains so the CI public-evaluation workflow chain is reusable.

Protected paths:

- `governance/compat/check_erh_ci_public_evaluation_workflow.py`
- `governance/compat/test_check_erh_ci_public_evaluation_workflow.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: the operator instructed Codex to continue by elevating
remaining ERH hardening into workflow/system chains where feasible. This
authorization is bounded to the four protected paths above and does not permit
other guard/control changes.

Rollback boundary: if the checker or hook wiring blocks unrelated work, revert
only the four protected-path changes plus the ERH-CI1 docs/GC-052 connection in
this tranche. Do not revert earlier ERH-T1C/T2C commits or unrelated user work.

## Evidence / Verification

Verification commands:

```powershell
python governance/compat/check_erh_ci_public_evaluation_workflow.py --enforce
python -m pytest governance/compat/test_check_erh_ci_public_evaluation_workflow.py -q
python governance/compat/check_system_loop_interlock.py --base 40c3c10d --head HEAD --enforce
```

Live proof requirement: N/A with reason. ERH-CI1 checks source-visible CI
workflow posture and protected live-gate presence only; it does not assert live
governance behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance governance workflow-chain implementation.

Next action: after review/commit, decide whether the public repo needs a small
CI boundary summary. Do not export the private checker details as a public
production-readiness claim.

## Claim Boundary

This baseline authorizes a private machine-check workflow chain only. It does
not prove GitHub Actions syntax validity, production-grade CI, dependency-audit
hardening, public-doc drift hardening, hosted freshness, public readiness, or
ordinary live-provider CI execution.
