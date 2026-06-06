# CVF GC-018 ERH-PD1 Public Surface Drift Workflow Chain Baseline

Memory class: FULL_RECORD

Status: IMPLEMENTATION_AUTHORIZED

docType: baseline

Date: 2026-06-04

baseHead: `bc6ce0fa`

## Purpose

Authorize a bounded ERH-PD1 tranche that converts public-surface claim drift
after ERH-T1C/T2C/CI1 into a repeatable workflow chain and machine gate.

## Scope / Target / Owner Boundary

Allowed scope:

- create a public-surface drift ledger for ERH private evidence versus public
  artifacts;
- create a public-surface drift workflow-chain reference;
- add a marker-based public-surface drift checker and focused tests;
- wire the checker into local hook and agent autorun chains;
- add one GC-052 system-loop connection;
- update the ERH roadmap and active handoff.

Forbidden scope:

- no public-sync clone edits in this tranche;
- no public push;
- no runtime or provider behavior changes;
- no dependency migration or audit-hardening claim;
- no hosted, production, or public-readiness claim;
- no ordinary live-provider CI claim.

Risk ceiling: R1 governance/checker workflow-chain implementation.

## Source / Predecessor Evidence

| Source | Purpose | Disposition |
| --- | --- | --- |
| `docs/reviews/CVF_ERH_T1C_PUBLIC_SYNC_LOCAL_CLAIM_BOUNDARY_PREP_COMPLETION_2026-06-04.md` | prior public-sync export evidence | ACCEPT |
| `docs/reviews/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_COMPLETION_2026-06-04.md` | private route governance workflow evidence | ACCEPT |
| `docs/reviews/CVF_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | private CI public-evaluation workflow evidence | ACCEPT |
| `docs/reference/CVF_ERH_T1B_PUBLIC_SYNC_HANDOFF_2026-06-04.md` | public-sync boundary | ACCEPT |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH tranche registry | ACCEPT |
| `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync` | observed clean public-sync clone | ACCEPT_AS_SNAPSHOT_INPUT |

## Decision

Proceed. The public repository already has a claim-boundary export from ERH-T1C,
while ERH-T2C and ERH-CI1 add private evidence that should not be silently
overclaimed or silently ignored. PD1 records that drift explicitly and makes the
next public-sync decision auditable.

## Acceptance Criteria

| Criterion | Evidence |
| --- | --- |
| Drift ledger exists | `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_LEDGER_2026-06-04.md` |
| Workflow-chain reference exists | `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_WORKFLOW_CHAIN_2026-06-04.md` |
| Checker exists | `governance/compat/check_erh_public_surface_drift_workflow.py` |
| Checker has focused tests | `governance/compat/test_check_erh_public_surface_drift_workflow.py` |
| Hook/autorun wiring exists | `run_local_governance_hook_chain.py`; `run_agent_autorun_workflow_gate.py` |
| System-loop connection exists | `erh-public-surface-drift-workflow-chain` |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: ERH-PD1 may add one new governance checker,
one focused checker test, and wire that checker into existing local hook and
agent autorun chains so public-surface drift becomes a reusable workflow gate.

Protected paths:

- `governance/compat/check_erh_public_surface_drift_workflow.py`
- `governance/compat/test_check_erh_public_surface_drift_workflow.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: the operator approved ERH-PD1 after Codex recommended
public-surface drift and claim sync as the next tranche. This authorization is
bounded to the four protected paths above and the ERH-PD1 documentation
artifacts in this batch.

Rollback boundary: if the checker or hook wiring blocks unrelated work, revert
only the four protected-path changes plus the ERH-PD1 docs/GC-052 connection in
this tranche. Do not revert earlier ERH-T1C/T2C/CI1 commits or unrelated user
work.

## Evidence / Verification

Verification commands:

```powershell
python governance/compat/check_erh_public_surface_drift_workflow.py --enforce
python -m pytest governance/compat/test_check_erh_public_surface_drift_workflow.py -q
python governance/compat/check_system_loop_interlock.py --base bc6ce0fa --head HEAD --enforce
```

Live proof requirement: N/A with reason. ERH-PD1 checks public documentation
claim drift and export posture only. It does not assert runtime or provider
governance behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance workflow-chain implementation. It prepares
the next public-sync decision but does not itself export public content.

Next action: after review, decide whether to open a public-sync summary update
for T2C/CI1 public caveats.

## Claim Boundary

This baseline authorizes bounded drift workflow-chain implementation only. It
does not prove live governance behavior, hosted freshness, production readiness,
public readiness, dependency-audit hardening, or public-sync publication.
