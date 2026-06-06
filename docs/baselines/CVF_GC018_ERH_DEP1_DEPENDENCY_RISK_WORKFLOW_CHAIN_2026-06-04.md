# CVF GC-018 ERH-DEP1 Dependency Risk Workflow Chain Baseline

Memory class: FULL_RECORD

Status: DISPATCH_AUTHORIZED_FOR_CLAUDE

docType: baseline

Date: 2026-06-04

baseHead: `24915dec`

Assigned worker: Claude

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize a bounded ERH-DEP1 tranche for Claude to convert the ERH-T4
`next-auth` beta dependency decision into a dependency risk workflow chain.

The goal is not to migrate dependencies immediately. The goal is to make
dependency risk visible, source-backed, testable, and public-claim bounded
before any future auth migration or production-auth claim.

## Scope / Target / Owner Boundary

Allowed scope:

- create an ERH-DEP1 dependency risk workflow-chain reference;
- create an ERH-DEP1 dependency risk ledger;
- create a marker-based dependency risk workflow checker and focused tests;
- wire the checker into local hook and agent autorun chains;
- add one GC-052 system-loop connection;
- update ERH roadmap and completion review for ERH-DEP1;
- run local dependency metadata/audit commands and record secret-safe output.

Forbidden scope:

- no `next-auth` migration in ERH-DEP1;
- no package manifest or lockfile edits unless Claude returns to operator with
  a DEP2 migration work order first;
- no auth runtime behavior changes;
- no public-sync clone edits or public push;
- no hosted, production, enterprise-auth, stable-dependency, or public-readiness
  claim;
- no live provider proof.

Risk ceiling: R1 governance/checker workflow-chain implementation.

## Source / Predecessor Evidence

| Source | Purpose | Disposition |
| --- | --- | --- |
| `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | upstream dependency decision | ACCEPT |
| `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_LEDGER_2026-06-04.md` | public-surface drift boundary | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependency declaration source | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | resolved dependency source | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | NextAuth runtime entrypoint source | ACCEPT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | session verification source | ACCEPT |
| `.github/workflows/cvf-web-ci.yml` | current web CI source | ACCEPT |

## External Metadata Snapshot

Captured on 2026-06-04 from:

```powershell
npm view next-auth version dist-tags --json
```

Observed result:

```json
{
  "version": "4.24.14",
  "dist-tags": {
    "latest": "4.24.14",
    "beta": "5.0.0-beta.31"
  }
}
```

Claude must rerun this command before implementation and treat any changed
metadata as a refreshed input, not as a blocker by itself.

## Decision

Proceed to Claude dispatch. ERH-T4 accepted `next-auth` beta for current bounded
scope, but the public/external evaluation path now needs a repeatable dependency
risk workflow chain. ERH-DEP1 must answer:

- what version is declared and locked;
- what upstream metadata currently says;
- whether audit/CI surfaces cover dependency risk;
- which auth touchpoints would need regression evidence before any migration;
- whether the correct next action is `ACCEPT_WITH_CAVEAT`, `MIGRATION_REQUIRED`,
  or `PUBLIC_CAVEAT_ONLY`.

## Acceptance Criteria

| Criterion | Evidence |
| --- | --- |
| Dependency risk workflow reference exists | `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_2026-06-04.md` |
| Dependency risk ledger exists | `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_LEDGER_2026-06-04.md` |
| Checker exists | `governance/compat/check_erh_dependency_risk_workflow.py` |
| Checker has focused tests | `governance/compat/test_check_erh_dependency_risk_workflow.py` |
| Hook/autorun wiring exists | `run_local_governance_hook_chain.py`; `run_agent_autorun_workflow_gate.py` |
| System-loop connection exists | `erh-dependency-risk-workflow-chain` |
| No migration occurs | `package.json` and `package-lock.json` unchanged |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: ERH-DEP1 may add one new governance checker,
one focused checker test, and wire that checker into existing local hook and
agent autorun chains so dependency risk posture becomes a reusable workflow
gate.

Protected paths:

- `governance/compat/check_erh_dependency_risk_workflow.py`
- `governance/compat/test_check_erh_dependency_risk_workflow.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: the operator asked Codex to prepare the next work order
so Claude can perform the worker implementation. This authorization is bounded
to the four protected paths above and ERH-DEP1 documentation artifacts.

Rollback boundary: if the checker or hook wiring blocks unrelated work, revert
only the four protected-path changes plus the ERH-DEP1 docs/GC-052 connection in
that tranche. Do not revert ERH-T1C/T2C/CI1/PD1 commits or unrelated user work.

## Evidence / Verification

Minimum commands for Claude:

```powershell
npm view next-auth version dist-tags --json
npm audit --json
python governance/compat/check_erh_dependency_risk_workflow.py --enforce
python -m pytest governance/compat/test_check_erh_dependency_risk_workflow.py -q
python governance/compat/check_system_loop_interlock.py --base 24915dec --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 24915dec --head HEAD
```

Run `npm audit --json` from
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`. If `npm audit` exits non-zero,
Claude must record the JSON summary and classify the result instead of
blind-rerunning or hiding it.

Live proof requirement: N/A with reason. ERH-DEP1 checks dependency risk and
auth touchpoint evidence only. It does not assert runtime/provider governance
behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline authorizes a private provenance dependency-risk workflow
chain. It does not publish public documentation.

Next action: Claude implements ERH-DEP1 in this private repo, then returns a
review-ready completion packet. A separate public-sync work order is required
before any public caveat update.

## Claim Boundary

This baseline authorizes dependency risk workflow-chain implementation only. It
does not prove auth security, hosted freshness, production readiness, public
readiness, dependency migration completion, or live governance behavior.
