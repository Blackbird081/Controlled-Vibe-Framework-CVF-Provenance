# CVF Agent Work Order - ERH-AUD1 CVF Web Dependency Audit Remediation For Claude

Memory class: FULL_RECORD

Status: DISPATCH_READY_FOR_CLAUDE

docType: work_order

Date: 2026-06-04

GC-018: `docs/baselines/CVF_GC018_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_2026-06-04.md`

dispatchBaseHead: `28f76620`

executionBaseHead: `28f76620`

closureBaseHead: `28f76620`

Assigned worker: Claude

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Implement ERH-AUD1 by reducing or fully classifying the current
`cvf-web` npm audit findings with bounded dependency updates and machine
evidence.

Success means CVF has a repeatable dependency-audit remediation workflow for
the public/external review gap without confusing it with `next-auth` beta
migration or production security readiness.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | Codex asked to create a Claude work order after ERH-DEP1 closure | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_2026-06-04.md` | ACCEPT |
| ERH-DEP1 completion | `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | ACCEPT |
| ERH-DEP1 ledger | `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_LEDGER_2026-06-04.md` | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- run `npm audit --json` from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`;
- run package metadata checks for direct vulnerable packages;
- update `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`;
- update `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json`;
- create `docs/reference/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_LEDGER_2026-06-04.md`;
- create `docs/reference/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_WORKFLOW_CHAIN_2026-06-04.md`;
- create `docs/reviews/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_COMPLETION_2026-06-04.md`;
- create `governance/compat/check_erh_cvf_web_dependency_audit_workflow.py`;
- create `governance/compat/test_check_erh_cvf_web_dependency_audit_workflow.py`;
- update `governance/compat/run_local_governance_hook_chain.py`;
- update `governance/compat/run_agent_autorun_workflow_gate.py`;
- update `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only if GC-051 requires coverage for newly cited source paths;
- update `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md`;
- update this work order status/evidence only inside Claude's implementation.

Forbidden scope:

- do not edit auth runtime source files;
- do not migrate or remove `next-auth`;
- do not edit public-sync clone;
- do not run live provider proof;
- do not claim production, hosted, public, or full security readiness;
- do not perform a broad `npm update` or destructive dependency reset;
- do not hide non-zero audit output.

Risk ceiling: R2 package-lock and dependency update workflow. Escalate before
any semver-major framework migration, auth behavior change, or runtime rewrite.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | author dispatch packet only |
| Worker | Claude | implement ERH-AUD1 within Allowed scope |
| Reviewer | Codex or operator after Claude returns | verify dependency diff, gates, and claim boundary |
| Operator approval required for | semver-major framework migration, auth runtime edit, public-sync, live proof, commit/push | not included |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | session front door |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active handoff and startup guards |
| `AGENT_HANDOFF_V15_2026-05-29.md` | current continuity and ERH state |
| `docs/baselines/CVF_GC018_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_2026-06-04.md` | tranche authority |
| `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | dependency-risk predecessor |
| `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_LEDGER_2026-06-04.md` | audit snapshot and next-auth boundary |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git status --short` | understand existing worktree before starting |
| `npm audit --json` from `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` | fresh audit snapshot recorded, even when non-zero |
| `npm view next version --json` | current `next` metadata recorded |
| `npm view jspdf version --json` | current `jspdf` metadata recorded |
| `npm view vitest version --json` | current `vitest` metadata recorded |
| `npm view @vitest/coverage-v8 version --json` | current coverage package metadata recorded |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 28f76620 --head HEAD` | PASS or record blocker before implementation |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Web package scripts include build/test/check | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | lines 5-16 | `scripts` | cvf-web package manifest | ACCEPT |
| Direct `jspdf` dependency exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 27 | `jspdf` | cvf-web package manifest | ACCEPT |
| Direct `next` dependency exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 29 | `next` | cvf-web package manifest | ACCEPT |
| Direct `next-auth` beta dependency remains separate from AUD1 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 30 | `next-auth` | cvf-web package manifest | ACCEPT |
| Direct `@vitest/coverage-v8` dependency exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 49 | `@vitest/coverage-v8` | cvf-web package manifest | ACCEPT |
| Direct `vitest` dependency exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 55 | `vitest` | cvf-web package manifest | ACCEPT |
| Lockfile root mirrors direct audit-target dependencies | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | lines 18, 20, 21, 40, 46 | root package dependencies | npm lock root package | ACCEPT |
| Installed `next` lock entry exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | line 8588 | `node_modules/next` | npm lock dependency entry | ACCEPT |
| Installed `jspdf` lock entry exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | line 7101 | `node_modules/jspdf` | npm lock dependency entry | ACCEPT |
| Installed `vitest` lock entry exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | line 11158 | `node_modules/vitest` | npm lock dependency entry | ACCEPT |
| ERH-DEP1 distinguishes next-auth beta from audit CVE remediation | `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | Audit Note | `next-auth` | ERH-DEP1 completion review | ACCEPT |

## Initial Audit Snapshot

Codex ran `npm audit --json` from `cvf-web` at base `28f76620`. The command
exited non-zero with:

| Severity | Count |
| --- | --- |
| critical | 3 |
| high | 7 |
| moderate | 4 |
| total | 14 |

Direct vulnerable packages in that snapshot:

- `next` direct, installed `16.1.6`, fix available `16.2.7`,
  `isSemVerMajor=false`;
- `jspdf` direct, affected range `<=4.2.0`, fix available;
- `vitest` direct, affected range `<4.1.0`, fix available;
- `@vitest/coverage-v8` direct, affected via `vitest`, fix available.

Claude must treat this as a starting snapshot, not final truth. Rerun audit and
metadata before changing files.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap / predecessor requirement | Work order output | Evidence |
| --- | --- | --- |
| ERH-DEP1 separated `next-auth` beta from audit vulnerabilities | AUD1 keeps `next-auth` out of remediation unless separate DEP2 opens | audit ledger and package diff |
| ERH roadmap next action called for `next` / toolchain audit work | bounded dependency audit remediation | package diff, tests, checker |
| Workflow/system, not prose-only | audit ledger plus checker/hook/autorun wiring | checker/test/gate output |
| Public claim remains bounded | private completion only | Public Export Disposition |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | update only for bounded dependency remediation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | update only through npm install/audit fix |
| `docs/reference/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_LEDGER_2026-06-04.md` | create |
| `docs/reference/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_WORKFLOW_CHAIN_2026-06-04.md` | create |
| `docs/reviews/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_COMPLETION_2026-06-04.md` | create |
| `governance/compat/check_erh_cvf_web_dependency_audit_workflow.py` | create |
| `governance/compat/test_check_erh_cvf_web_dependency_audit_workflow.py` | create |
| `governance/compat/run_local_governance_hook_chain.py` | update |
| `governance/compat/run_agent_autorun_workflow_gate.py` | update |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | update |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | bounded GC-051 remediation only if required |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | update |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_FOR_CLAUDE_2026-06-04.md` | update status/evidence |

Forbidden paths include auth runtime files, public-sync clone, `.env*`, live
provider receipts, and unrelated source/frontend refactors.

## Execution Plan

| Step | Action | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | Refresh npm audit and package metadata | before snapshot in ledger | npm registry unavailable after diagnostic |
| 2 | Classify direct vs transitive vulnerabilities | audit matrix | classification cannot identify owner package |
| 3 | Apply bounded non-semver-major dependency remediation | package/lock diff | semver-major or auth/runtime migration required |
| 4 | Re-run audit | after snapshot | unresolved findings need classification |
| 5 | Run web verification | test/type/build evidence | dependency break exceeds allowed scope |
| 6 | Create workflow reference, ledger, checker, tests | reusable audit workflow | checker cannot be bounded |
| 7 | Wire checker into hook/autorun and GC-052 | system workflow chain | core guard authorization missing |
| 8 | Create completion review | review-ready packet | claim boundary cannot be preserved |

## Remediation Decision Matrix

Claude must classify the final result as exactly one:

| Decision | Meaning | Allowed next action |
| --- | --- | --- |
| `AUDIT_CLEAN_PASS` | `npm audit --json` returns zero vulnerabilities after bounded remediation | close with clean evidence |
| `AUDIT_REDUCED_WITH_RESIDUALS` | vulnerabilities reduced, residuals classified with owner/fix boundary | close bounded and propose next work order |
| `AUDIT_BLOCKED_MAJOR_OR_RUNTIME` | fix requires semver-major, auth runtime change, or broad migration | stop and propose follow-up work order |
| `AUDIT_BLOCKED_REGISTRY_OR_TESTS` | registry/test/build failure prevents safe closure | return blocker with diagnostic |

## Evidence Requirements

| Evidence | Required result |
| --- | --- |
| Before audit snapshot | fresh `npm audit --json` summarized |
| Package metadata | `npm view` outputs summarized for direct audit targets |
| Dependency diff | package/lock diff explained by direct remediation |
| After audit snapshot | zero vulnerabilities or residual matrix |
| Verification | `npm run check`, `npm run test:run`, and `npm run build` attempted and recorded |
| Checker verdict | one bounded decision from the matrix |
| Focused checker tests | PASS |
| Public export | `DEFERRED_PRIVATE_ONLY` unless a later public-sync work order opens |

## Review Gate

Reviewer must verify:

- `next-auth` was not migrated or removed;
- auth runtime files were not changed;
- every package/lockfile change maps to an audit finding or safe peer alignment;
- `npm audit` output is not hidden;
- tests/build failures, if any, are classified with owner and next action;
- completion does not claim production security or public readiness.

## Closure Checklist

| Item | Required disposition |
| --- | --- |
| Source Verification Block complete | checked |
| Roadmap-to-work-order trace matrix present | checked |
| Audit decision matrix resolved | one decision selected |
| Package/lockfile diff scoped | checked |
| Auth runtime unchanged | checked |
| Public export disposition present | checked |
| Finding-To-Governance Learning Disposition present | checked |
| Pre-closure autorun gate run on real committed range | checked by reviewer after operator commit |

## Return Conditions

Return to orchestrator if:

- a semver-major framework migration is required;
- `next-auth` migration becomes necessary;
- auth runtime source edit is needed;
- package changes trigger broad app behavior changes;
- public-sync edit/push is needed;
- live/provider proof is requested;
- audit residuals cannot be safely classified.

## Worker Autonomy / No-Question Rule

Claude should proceed autonomously for audit refresh, metadata refresh,
bounded package remediation, ledger/reference/checker authoring, focused tests,
hook/autorun wiring, GC-052 registration, and allowed-scope gate remediation.

Allowed-scope guard failures are mandatory remediation for Claude. Return to
orchestrator only when the repair would require semver-major migration, auth
runtime edits, public-sync, live proof, destructive operations, or stronger
public/production/security claims.

## Operator Checkpoint

Operator checkpoint is required before semver-major framework migration,
`next-auth` migration, auth runtime edits, public-sync update, public push,
live/provider proof, or any production/public security-readiness claim.

## Verification Commands

Claude must run at minimum from:

`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`

```powershell
npm audit --json
npm view next version --json
npm view jspdf version --json
npm view vitest version --json
npm view @vitest/coverage-v8 version --json
npm run check
npm run test:run
npm run build
```

Claude must then run from repo root:

```powershell
python governance/compat/check_erh_cvf_web_dependency_audit_workflow.py --enforce
python -m pytest governance/compat/test_check_erh_cvf_web_dependency_audit_workflow.py -q
python governance/compat/check_system_loop_interlock.py --base 28f76620 --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 28f76620 --head HEAD --all-changed --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 28f76620 --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base 28f76620 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base 28f76620 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 28f76620 --head HEAD
```

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| Audit before/after recorded | ledger | REQUIRED |
| Bounded dependency diff produced or blocker classified | package diff / review | REQUIRED |
| `next-auth` unchanged | diff/status | REQUIRED |
| Auth runtime unchanged | diff/status | REQUIRED |
| Checker exists and passes | checker command | REQUIRED |
| Focused tests pass | pytest command | REQUIRED |
| Public claim remains bounded | completion review | REQUIRED |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| Claude edits auth runtime in AUD1 | BLOCKS_CLOSURE |
| Claude migrates or removes `next-auth` in AUD1 | BLOCKS_CLOSURE |
| Claude performs broad dependency refresh unrelated to audit | BLOCKS_CLOSURE |
| Claude hides non-zero `npm audit` output | BLOCKS_CLOSURE |
| Claude claims production security readiness | BLOCKS_CLOSURE |
| Claude treats private remediation as public export | BLOCKS_CLOSURE |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| ERH-DEP1 found 14 npm audit vulnerabilities outside `next-auth` beta risk | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Claude implements ERH-AUD1 audit remediation checker and ledger |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order dispatches private dependency-audit remediation work in
the provenance repository. Public catalog or README changes require a separate
public-sync work order.

Next action: Claude implements AUD1 and returns a review-ready completion
packet under `WORKER_MUST_NOT_COMMIT`.

## Claim Boundary

This work order does not authorize production security claims, public
readiness, hosted readiness, `next-auth` migration, auth runtime changes,
public-sync export, or live governance proof.
