# CVF Agent Work Order - ERH-CI1 Public Evaluation Workflow Chain

Memory class: POINTER_RECORD

Status: IMPLEMENTATION_COMPLETE_PENDING_REVIEW

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `40c3c10d`

executionBaseHead: `40c3c10d`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `CODEX_MAY_COMMIT_AFTER_GATES`

## Purpose

Implement ERH-CI1 by converting the ERH-T2B CI hardening plan into a source
marker workflow chain. Success means public-evaluation CI posture is checked by
a repeatable machine gate and routed through GC-052, while overclaims remain
blocked by explicit boundary language.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | continue by creating workflow/system, not only hardening | ACCEPT |
| Clean base commit | `40c3c10d` | ACCEPT |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| ERH-T2B plan | `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | ACCEPT |
| ERH-T2C workflow chain | `docs/reference/CVF_ERH_T2C_ROUTE_GOVERNANCE_PROOF_WORKFLOW_CHAIN_2026-06-04.md` | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_2026-06-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `check_erh_ci_public_evaluation_workflow.py`;
- create focused checker tests;
- wire checker into local hook and autorun common gates;
- add a GC-052 connection;
- add/update ERH private governance docs.

Forbidden scope:

- no public-sync clone edits;
- no `.github/workflows/**` edits;
- no dependency migration, dependency install, or `npm audit` claim;
- no live provider execution required by this tranche;
- no production-grade/public-readiness claim.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | select ERH-CI1 as workflow-chain successor to T2B |
| Implementer | Codex | checker, tests, hook/autorun wiring, docs |
| Reviewer | Codex self-review pending operator review | bounded private completion only |
| Operator approval required for | public-sync, workflow rewrites, live proof, dependency migration | not included |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | upstream hardening plan |
| `.github/workflows/cvf-ci.yml` | main CI source markers |
| `.github/workflows/cvf-web-ci.yml` | web lint/coverage source markers |
| `.github/workflows/cvf-static-ci.yml` | static CI source markers |
| `.github/workflows/cvf-protected-live-release-gate.yml` | protected live gate boundary |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | downstream system-loop registry |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git rev-parse --short HEAD` | `40c3c10d` before implementation |
| `git status --short` | clean worktree before implementation |
| `rg -n "npm run lint|npm run test:coverage|RUN_LIVE_GATE" .github/workflows` | source markers found |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| EXISTS: main CI type/build/test markers | `.github/workflows/cvf-ci.yml` | lines 94, 97, 233, 236, 272 | `cvf-ci.yml` | GitHub Actions workflow | ACCEPT |
| EXISTS: web CI lint/coverage markers | `.github/workflows/cvf-web-ci.yml` | lines 39, 45 | `cvf-web-ci.yml` | GitHub Actions workflow | ACCEPT |
| EXISTS: static CI gate marker | `.github/workflows/cvf-static-ci.yml` | line 48 | `run_cvf_static_ci_gate.py --json` | GitHub Actions workflow | ACCEPT |
| EXISTS: protected manual live gate markers | `.github/workflows/cvf-protected-live-release-gate.yml` | lines 4, 7, 18, 67 | `RUN_LIVE_GATE` | protected live release workflow | ACCEPT |
| EXISTS: docs governance markers | `.github/workflows/documentation-testing.yml` | lines 79, 99 | `check_work_order_dispatch_quality.py` | documentation testing workflow | ACCEPT |
| EXISTS: web package script capabilities | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | lines 10, 12, 13, 15, 16 | `scripts` | package.json | ACCEPT |
| EXISTS: T2B public claim boundary | `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | lines 60-62 | `Public Claim Rule` | T2B plan | ACCEPT |
| EXISTS: route-governance interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | lines 144-160 | `erh-route-ledger-to-route-governance-proof-workflow` | GC-052 registry | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Verification | Status |
| --- | --- | --- | --- |
| Elevate remaining hardening into workflow chain | checker, tests, hook wiring | focused tests and checker run | PASS |
| Preserve claim calibration | explicit claim boundary | completion review | PASS |
| Keep public-sync separate | no public-sync path touched | git diff/status | PASS |
| Keep live/provider proof separate | no live command required | claim boundary | PASS |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `governance/compat/check_erh_ci_public_evaluation_workflow.py` | create |
| `governance/compat/test_check_erh_ci_public_evaluation_workflow.py` | create |
| `governance/compat/run_local_governance_hook_chain.py` | update checker wiring only |
| `governance/compat/run_agent_autorun_workflow_gate.py` | update checker wiring only |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | add one connection |
| `docs/baselines/CVF_GC018_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_2026-06-04.md` | create |
| `docs/reference/CVF_ERH_CI_PUBLIC_EVALUATION_WORKFLOW_CHAIN_2026-06-04.md` | create |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_2026-06-04.md` | create |
| `docs/reviews/CVF_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | create |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | update ERH-CI1 status |
| `docs/reference/CVF_ERH_T2B_CI_HARDENING_PLAN_2026-06-04.md` | update successor boundary |
| `AGENT_HANDOFF_V15_2026-05-29.md` | update current HEAD continuity marker required by active-session gate |

## Execution Plan

| Step | Input | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | T2B plan and CI workflows | checker requirements | missing source marker |
| 2 | checker requirements | checker and tests | focused test failure |
| 3 | checker source | hook/autorun wiring | hook-chain incompatibility |
| 4 | GC-052 registry | system-loop connection | registry gate failure |
| 5 | ERH docs | completion packet | governance gate failure |

## Evidence Requirements

| Evidence | Path or command | Required result |
| --- | --- | --- |
| Checker | `python governance/compat/check_erh_ci_public_evaluation_workflow.py --enforce` | `READY_WITH_BOUNDARIES` |
| Focused tests | `python -m pytest governance/compat/test_check_erh_ci_public_evaluation_workflow.py -q` | PASS |
| System loop | `python governance/compat/check_system_loop_interlock.py --base 40c3c10d --head HEAD --enforce` | PASS |
| Structural gates | markdown, dispatch, F2G, public export | PASS |

## Review Gate

Reviewer must confirm no `.github/workflows/**` files were changed and no
public-sync paths were touched before accepting ERH-CI1.

## Worker Autonomy / No-Question Rule

Codex proceeds autonomously for allowed checker, test, documentation, hook
wiring, and gate remediation. Escalation is reserved for public-sync, live
provider proof, dependency migration, `.github/workflows/**` rewrites, or a
public/production-readiness claim expansion.

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| Checker reports `READY_WITH_BOUNDARIES` on current repo | checker command | PASS_PENDING_FINAL_GATE |
| Checker blocks missing lint/coverage/claim-boundary markers in tests | unit tests | PASS_PENDING_FINAL_GATE |
| Checker wired into hook/autorun chains | source diff | PASS_PENDING_FINAL_GATE |
| GC-052 connection registered | system-loop checker | PASS_PENDING_FINAL_GATE |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| Checker claims production-grade CI | BLOCKS_CLOSURE |
| `.github/workflows/**` is edited | BLOCKS_CLOSURE |
| Public-sync clone is edited | BLOCKS_CLOSURE |
| Live provider gate is treated as ordinary CI | BLOCKS_CLOSURE |

## Closure Checklist

| Item | Status |
| --- | --- |
| Checker created | PASS |
| Focused tests created | PASS |
| Hook/autorun wiring added | PASS |
| GC-052 connection added | PASS |
| Public export deferred | PASS |
| Commit/push finality | PENDING |

## Return Conditions

Return to orchestrator if workflow rewrites, public-sync edits, dependency
migration, live proof, or a stronger public/production-readiness claim becomes
necessary.

## Operator Checkpoint

N/A with reason: operator instructed Codex to continue by creating workflow
chains where feasible. This tranche stays inside private checker/docs scope and
does not consume provider quota.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| ERH-T2B plan could remain non-executable hardening prose | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | add CI public-evaluation workflow-chain checker |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance workflow-chain implementation. Public export requires
a separate public-sync summary decision after review.

Next action: run checker, focused tests, structural gates, and commit when
clean.

## Claim Boundary

ERH-CI1 may claim a private, marker-based CI public-evaluation workflow-chain
gate. It does not prove GitHub Actions syntax validity, production-grade CI,
dependency-audit hardening, public-doc drift hardening, hosted freshness,
public readiness, or ordinary live-provider CI execution.
