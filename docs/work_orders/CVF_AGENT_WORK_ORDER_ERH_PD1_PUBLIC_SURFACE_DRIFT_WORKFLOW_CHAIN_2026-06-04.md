# CVF Agent Work Order - ERH-PD1 Public Surface Drift Workflow Chain

Memory class: FULL_RECORD

Status: IMPLEMENTATION_COMPLETE_PENDING_REVIEW

docType: work_order

Date: 2026-06-04

GC-018: `docs/baselines/CVF_GC018_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md`

dispatchBaseHead: `bc6ce0fa`

## Purpose

Implement ERH-PD1 by converting post-T1C public claim drift into a bounded
workflow chain. Success means a future agent can inspect one ledger and one
machine gate to see which ERH private evidence is public, deferred, or a public
summary update candidate.

## Scope / Target / Owner Boundary

Allowed scope:

- create PD1 drift ledger, workflow reference, work order, and completion
  review;
- add and test `check_erh_public_surface_drift_workflow.py`;
- wire the checker into local hook and autorun chains;
- add a GC-052 connection;
- update ERH roadmap and active handoff.
- `governance/compat/check_erh_public_surface_drift_workflow.py`
- `governance/compat/test_check_erh_public_surface_drift_workflow.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `docs/baselines/CVF_GC018_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md`
- `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md`
- `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_LEDGER_2026-06-04.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md`
- `docs/reviews/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md`
- `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md`
- `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
- `AGENT_HANDOFF_V15_2026-05-29.md`

Forbidden scope:

- no public-sync clone edits;
- no public push;
- no runtime/provider route changes;
- no dependency migration;
- no live proof;
- no public/production/hosted readiness claim.

## Authority Chain

| Authority | Artifact or source | Disposition |
| --- | --- | --- |
| Operator approval | chat instruction approving PD1 | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md` | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | select PD1 after operator approval |
| Worker | Codex | implement checker/docs/interlock only |
| Reviewer | Codex self-review pending operator review | bounded private closure |
| Operator approval required for | public-sync edit/push, live proof, dependency migration | not included |

## Required First Reads

| Artifact | Purpose |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | startup front door |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active handoff and guard registry |
| `AGENT_HANDOFF_V15_2026-05-29.md` | current session continuity |
| `docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` | public export boundary |
| `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | closure quality requirements |

## Pre-Flight Checks

| Check | Evidence | Result |
| --- | --- | --- |
| Base captured | `git rev-parse --short HEAD` | `bc6ce0fa` |
| Worktree clean before PD1 | `git status --short` | PASS |
| Public-sync remote verified | `git -C ..\Controlled-Vibe-Framework-CVF-public-sync remote -v` | public repo remote |
| Public-sync worktree clean | `git -C ..\Controlled-Vibe-Framework-CVF-public-sync status --short` | PASS |

## Source Packet

| Source | Role |
| --- | --- |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH parent roadmap |
| `docs/reference/CVF_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` | public-sync boundary |
| `docs/reviews/CVF_ERH_T1C_PUBLIC_SYNC_LOCAL_CLAIM_BOUNDARY_PREP_COMPLETION_2026-06-04.md` | exported public baseline |
| `docs/reviews/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_COMPLETION_2026-06-04.md` | private route proof workflow evidence |
| `docs/reviews/CVF_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | private CI workflow evidence |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| ERH roadmap exists | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | Tranche Plan | `ERH-CI1` | ERH roadmap | ACCEPT |
| T1C public export evidence exists | `docs/reviews/CVF_ERH_T1C_PUBLIC_SYNC_LOCAL_CLAIM_BOUNDARY_PREP_COMPLETION_2026-06-04.md` | Public Export Disposition | `Public commit` | T1C completion review | ACCEPT |
| T2C private evidence exists | `docs/reviews/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_COMPLETION_2026-06-04.md` | Claim Boundary | `focused-test evidence` | T2C completion review | ACCEPT |
| CI1 private evidence exists | `docs/reviews/CVF_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | Claim Boundary | `verdict` | CI1 completion review | ACCEPT |
| Public-sync remote exists | `docs/reviews/CVF_ERH_T1C_PUBLIC_SYNC_LOCAL_CLAIM_BOUNDARY_PREP_COMPLETION_2026-06-04.md` | Public Export Disposition | `Public-sync remote` | T1C completion review | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Evidence |
| --- | --- | --- |
| Continue ERH as workflow/system | PD1 checker and GC-052 connection | checker + registry |
| Keep public-sync separate | ledger marks future public-sync action only | no public-sync files touched |
| Prevent public overclaim | status vocabulary and claim boundary | ledger/reference |
| Preserve public export evidence | snapshot remote/commit/artifact list | ledger |

## Write Ownership

| Path | Action |
| --- | --- |
| `governance/compat/check_erh_public_surface_drift_workflow.py` | create |
| `governance/compat/test_check_erh_public_surface_drift_workflow.py` | create |
| `governance/compat/run_local_governance_hook_chain.py` | update |
| `governance/compat/run_agent_autorun_workflow_gate.py` | update |
| `docs/baselines/CVF_GC018_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md` | create |
| `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md` | create |
| `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_LEDGER_2026-06-04.md` | create |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md` | create/update |
| `docs/reviews/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | create |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | update |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | update |
| `AGENT_HANDOFF_V15_2026-05-29.md` | update |

Forbidden paths: public-sync clone, runtime source, `.github/workflows/**`,
dependency manifests.

## Execution Plan

1. Create PD1 ledger and reference.
2. Implement marker-based checker and focused tests.
3. Wire checker into hook and autorun chains.
4. Add GC-052 connection.
5. Update roadmap and completion review.
6. Run focused checks and governance gates.
7. Commit private provenance batch only.

## Evidence Requirements

| Evidence | Required result |
| --- | --- |
| PD1 checker | `DRIFT_BOUNDED_WITH_UPDATE_CANDIDATES` |
| Focused tests | PASS |
| GC-052 checker | PASS |
| Public export gate | PASS |
| Worktree finality | clean after commit |

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Checker verdict | `DRIFT_BOUNDED_WITH_UPDATE_CANDIDATES` |
| Focused tests | PASS |
| Public-sync boundary | no public-sync files touched |
| Live proof boundary | N/A with reason |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` |

## Verification Commands

```powershell
python governance/compat/check_erh_public_surface_drift_workflow.py --enforce
python -m pytest governance/compat/test_check_erh_public_surface_drift_workflow.py -q
python governance/compat/check_system_loop_interlock.py --base bc6ce0fa --head HEAD --enforce
```

## Failure Conditions

Return to orchestrator if public-sync edits, workflow rewrites, dependency
migration, live proof, runtime changes, or a stronger public/production claim
becomes necessary.

## Review Gate

Reviewer must confirm the PD1 checker passes, public-sync remains untouched,
and the completion packet preserves the no-live-proof and no-public-readiness
claim boundary.

## Closure Checklist

| Item | Disposition |
| --- | --- |
| Roadmap-to-work-order trace exists | checked |
| Source Verification Block has no guessed runtime fields | checked |
| Public Export Disposition exists | checked |
| Finding-To-Governance Learning Disposition exists | checked |
| Live proof is N/A with reason | checked |
| Public-sync edit is N/A with reason | checked |

## Operator Checkpoint

No operator checkpoint is required for PD1 private implementation. Operator
approval is required before any later public-sync edit, public push, live proof,
runtime change, or dependency migration.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Public-surface drift can accumulate after private ERH workflow chains | PUBLIC_SURFACE_DRIFT_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | PD1 checker and ledger |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: work order governs private provenance implementation only.

Next action: separate public-sync work order if the operator approves public
summary updates.

## Claim Boundary

ERH-PD1 may claim a private drift workflow chain and update-candidate ledger.
It does not claim public-sync export, public readiness, production readiness,
hosted freshness, live governance behavior, or dependency hardening.
