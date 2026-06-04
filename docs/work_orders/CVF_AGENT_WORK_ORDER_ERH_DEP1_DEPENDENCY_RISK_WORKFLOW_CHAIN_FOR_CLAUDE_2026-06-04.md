# CVF Agent Work Order - ERH-DEP1 Dependency Risk Workflow Chain For Claude

Memory class: FULL_RECORD

Status: DISPATCH_READY_FOR_CLAUDE

docType: work_order

Date: 2026-06-04

GC-018: `docs/baselines/CVF_GC018_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_2026-06-04.md`

dispatchBaseHead: `24915dec`

executionBaseHead: `24915dec`

closureBaseHead: `24915dec`

Assigned worker: Claude

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Implement ERH-DEP1 by converting the ERH-T4 `next-auth` beta dependency
decision into a source-backed dependency risk workflow chain.

Success means CVF can answer a public/external evaluator's dependency-risk
question without either hiding the beta dependency or prematurely migrating
auth runtime.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | Codex asked to prepare work order for Claude | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_2026-06-04.md` | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| ERH-T4 decision | `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | ACCEPT |
| ERH-PD1 drift ledger | `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_LEDGER_2026-06-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_2026-06-04.md`;
- create `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_LEDGER_2026-06-04.md`;
- create `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md`;
- create `governance/compat/check_erh_dependency_risk_workflow.py`;
- create `governance/compat/test_check_erh_dependency_risk_workflow.py`;
- update `governance/compat/run_local_governance_hook_chain.py`;
- update `governance/compat/run_agent_autorun_workflow_gate.py`;
- update `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- update `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md`;
- update this work order status/evidence only inside Claude's implementation.

Forbidden scope:

- do not edit `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`;
- do not edit `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json`;
- do not edit auth runtime files in ERH-DEP1;
- do not public-sync or push public;
- do not run live provider proof;
- do not claim hosted/production/public readiness.

Risk ceiling: R1 checker/workflow-chain implementation.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | author dispatch packet only |
| Worker | Claude | implement ERH-DEP1 within Allowed scope |
| Reviewer | Codex or operator after Claude returns | verify gates and boundary |
| Operator approval required for | package edits, auth runtime edits, public-sync, live proof, commit/push | not included |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | session front door |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active handoff and startup guards |
| `AGENT_HANDOFF_V15_2026-05-29.md` | current continuity and ERH-PD1 context |
| `docs/baselines/CVF_GC018_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_2026-06-04.md` | tranche authority |
| `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | upstream dependency decision |
| `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_LEDGER_2026-06-04.md` | public-summary boundary |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git status --short` | understand any existing worktree changes before starting |
| `rg -n '"next-auth"' EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | confirms declared and locked beta dependency |
| `npm view next-auth version dist-tags --json` | refreshed metadata snapshot |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 24915dec --head HEAD` | PASS or record blocker before implementation |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Web package declares `next-auth` beta range | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 30 | `next-auth` | cvf-web package manifest | ACCEPT |
| Lockfile root dependency keeps same beta range | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | line 21 | `next-auth` | cvf-web package lock root package | ACCEPT |
| Lockfile resolves next-auth beta package | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | lines 8641-8642 | `node_modules/next-auth` | package lock dependency entry | ACCEPT |
| NextAuth runtime entrypoint exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | lines 1-6, 113 | `NextAuth` | auth runtime module | ACCEPT |
| Session verification delegates to Auth.js runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | lines 72, 75-76 | `verifySessionCookie` | middleware auth helper | ACCEPT |
| Middleware wraps requests with auth | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/middleware.ts` | lines 11, 76 | `auth` | Next middleware | ACCEPT |
| Middleware-auth tests exist | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.test.ts` | lines 19, 22-23 | `verifySessionCookie` | middleware auth test suite | ACCEPT |
| Web CI has lint/build/test path | `.github/workflows/cvf-web-ci.yml` | lines 39, 41, 43 | `run` | web CI workflow | ACCEPT |
| Protected live gate install command exists | `.github/workflows/cvf-protected-live-release-gate.yml` | line 53 | `run` | protected live release workflow | ACCEPT |
| ERH-T4 forbids migration in decision tranche | `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | Scope / Target / Owner Boundary | `dependency migration` | ERH-T4 baseline | ACCEPT |
| ERH-PD1 defers dependency risk summary | `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_LEDGER_2026-06-04.md` | Private Evidence To Public Surface Drift Matrix | `Public status` | PD1 drift ledger | ACCEPT |

## External Metadata Snapshot

Codex observed this pre-dispatch command output:

```powershell
npm view next-auth version dist-tags --json
```

```json
{
  "version": "4.24.14",
  "dist-tags": {
    "latest": "4.24.14",
    "beta": "5.0.0-beta.31"
  }
}
```

Claude must rerun the command and record the fresh result in the DEP1 ledger.
Do not assume this snapshot is still current.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Evidence |
| --- | --- | --- |
| ERH-T4 dependency decision follow-up | dependency risk workflow chain | DEP1 reference and checker |
| PD1 public-surface boundary | public caveat remains deferred/private until separate public-sync | DEP1 ledger |
| Workflow/system, not prose-only | machine checker plus hook/autorun wiring | checker/test/gate output |
| No migration without separate authority | package manifests/lockfiles unchanged | git diff/status |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_2026-06-04.md` | create |
| `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_LEDGER_2026-06-04.md` | create |
| `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | create |
| `governance/compat/check_erh_dependency_risk_workflow.py` | create |
| `governance/compat/test_check_erh_dependency_risk_workflow.py` | create |
| `governance/compat/run_local_governance_hook_chain.py` | update |
| `governance/compat/run_agent_autorun_workflow_gate.py` | update |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | update |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | update |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md` | update status/evidence |

Forbidden paths: `package.json`, `package-lock.json`, auth runtime source,
public-sync clone, `.env*`, live/provider proof receipts.

## Execution Plan

| Step | Action | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | Rerun npm metadata and inspect package/lock | metadata snapshot in ledger | registry unavailable after diagnostic |
| 2 | Run `npm audit --json` from cvf-web | audit summary in ledger | command unavailable after diagnostic |
| 3 | Map auth touchpoints | auth touchpoint table | source path mismatch |
| 4 | Create dependency risk workflow reference | DEP1 reference | claim boundary cannot be preserved |
| 5 | Create marker-based checker and tests | checker + focused tests | package edit becomes necessary |
| 6 | Wire checker into hook/autorun and GC-052 | reusable workflow gate | core guard authorization missing |
| 7 | Run gates and create completion review | review-ready packet | gate failure outside Allowed scope |

## Dependency Risk Decision Matrix

Claude must classify the ERH-DEP1 result as exactly one:

| Decision | Meaning | Allowed next action |
| --- | --- | --- |
| `ACCEPT_WITH_CAVEAT` | current beta remains acceptable for bounded private/non-production scope | keep public caveat; no migration |
| `PUBLIC_CAVEAT_ONLY` | dependency risk needs public wording but not implementation | propose public-sync caveat only |
| `MIGRATION_REQUIRED_DEP2` | migration appears required before stronger auth/public claims | author DEP2 migration work order; do not migrate in DEP1 |
| `BLOCKED_NEEDS_OPERATOR` | evidence is insufficient or risk cannot be classified safely | return to operator with blocker |

## Evidence Requirements

| Evidence | Required result |
| --- | --- |
| Metadata snapshot | fresh `npm view next-auth version dist-tags --json` recorded |
| Audit snapshot | `npm audit --json` result summarized secret-safely |
| Auth touchpoint map | source-backed table covering `auth.ts`, middleware, middleware-auth, logout/login/session tests |
| Checker verdict | one bounded decision from the matrix |
| Focused tests | PASS |
| Package diff | no package manifest or lockfile changes |
| Public export | `DEFERRED_PRIVATE_ONLY` unless a later public-sync work order is opened |

## Review Gate

Reviewer must verify:

- no package or lockfile diff exists;
- no auth runtime source diff exists;
- dependency risk checker is wired into both hook and autorun;
- `npm audit` non-zero output, if any, is classified rather than hidden;
- completion packet does not claim production auth stability.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Source Verification Block complete | checked |
| Roadmap-to-work-order trace matrix present | checked |
| Dependency risk decision matrix resolved | one decision selected |
| Package/lockfile unchanged | checked |
| Public export disposition present | checked |
| Finding-To-Governance Learning Disposition present | checked |
| Pre-closure autorun gate run on real range | checked |

## Return Conditions

Return to orchestrator if:

- migration is required;
- package or lockfile edit is needed;
- auth runtime source edit is needed;
- public-sync edit/push is needed;
- live provider proof is requested;
- dependency risk cannot be classified from available evidence.

## Worker Autonomy / No-Question Rule

Claude should proceed autonomously for source inspection, npm metadata
refresh, `npm audit --json`, checker/reference/ledger authoring, focused tests,
hook/autorun wiring, GC-052 registration, and allowed-scope gate remediation.

Allowed-scope guard failures are mandatory remediation for Claude. Return to
orchestrator only when the repair would require package edits, auth runtime
edits, public-sync, live proof, dependency migration, destructive operations,
or a stronger public/production claim.

## Operator Checkpoint

Operator checkpoint is required before DEP2 migration, public-sync update,
public push, package edits, auth runtime edits, or any public/production
readiness claim.

## Verification Commands

Claude must run at minimum:

```powershell
npm view next-auth version dist-tags --json
npm audit --json
python governance/compat/check_erh_dependency_risk_workflow.py --enforce
python -m pytest governance/compat/test_check_erh_dependency_risk_workflow.py -q
python governance/compat/check_system_loop_interlock.py --base 24915dec --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 24915dec --head HEAD --all-changed --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 24915dec --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base 24915dec --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 24915dec --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 24915dec --head HEAD
```

Run the first two npm commands from:

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| DEP1 workflow chain exists | reference path | REQUIRED |
| DEP1 ledger exists | ledger path | REQUIRED |
| Checker exists and passes | checker command | REQUIRED |
| Focused tests pass | pytest command | REQUIRED |
| No migration performed | diff/status | REQUIRED |
| Public claim remains bounded | completion review | REQUIRED |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| Claude edits `package.json` or `package-lock.json` in DEP1 | BLOCKS_CLOSURE |
| Claude edits auth runtime in DEP1 | BLOCKS_CLOSURE |
| Claude claims production auth stability | BLOCKS_CLOSURE |
| Claude treats public caveat candidate as exported public claim | BLOCKS_CLOSURE |
| Claude hides non-zero `npm audit` output | BLOCKS_CLOSURE |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Beta dependency decision needs a repeatable risk workflow before public/auth claims | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Claude implements ERH-DEP1 checker and ledger |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order dispatches a private dependency-risk workflow chain.

Next action: Claude implements DEP1 and returns a review-ready completion
packet. Public-sync remains a separate operator-approved work order.

## Claim Boundary

This work order does not authorize dependency migration, auth runtime changes,
public-sync export, hosted readiness, production auth stability, public
readiness, or live governance proof.
