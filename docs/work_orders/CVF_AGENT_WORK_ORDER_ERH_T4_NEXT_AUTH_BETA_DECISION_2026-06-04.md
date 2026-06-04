# CVF Agent Work Order - ERH-T4 Next-Auth Beta Decision

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `b5cf8882`

executionBaseHead: `b5cf8882`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Dependency release: ERH-T3 boundary exists at
`docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md`.

## Purpose

Execute ERH-T4 by recording a governed decision baseline for the current
`next-auth` beta dependency. Success means public claims have a clear caveat and
any migration is routed to a separate implementation tranche.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| GC-018 | `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| T3 dependency | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- inspect `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`;
- create `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md`.

Forbidden scope:

- modify package manifests, lockfiles, auth runtime, or public-sync files;
- claim hosted/production readiness from this decision.

Risk ceiling: R0 decision record.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | private ERH dependency decision |
| Implementer | Codex | decision baseline only |
| Reviewer | Codex self-review pending operator review | no package migration |
| Operator approval required for | package edits, auth runtime edits, public-sync, commit/push | not used |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | dependency release |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | current dependency source |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | tranche scope |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `rg -n '"next-auth"' EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | beta dependency line |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b5cf8882 --head HEAD` | PASS |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T4_NEXT_AUTH_BETA_DECISION_2026-06-04.md` | create/update |
| `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | create/update |

Forbidden paths: package manifests, lockfiles, auth runtime, public-sync clone.

## Execution Plan

| Step | Input | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | T3 boundary | dependency release | missing T3 artifact |
| 2 | package manifest | beta decision baseline | package edit required |
| 3 | governance gates | pending-review state | gate failure outside scope |

## Evidence Requirements

| Evidence | Path or command | Required at handoff |
| --- | --- | --- |
| Dependency source | `package.json` line 30 | Yes |
| Decision baseline | `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | Yes |
| No package edit | `git diff --name-status` | Yes |

## Review Gate

| Gate | Requirement |
| --- | --- |
| Dependency release | T3 path exists |
| Package boundary | no package or lockfile diff |
| Pre-closure | N/A with reason: no commit in `WORKER_MUST_NOT_COMMIT` mode |

## Closure Checklist

| Item | Status |
| --- | --- |
| Decision baseline created | PASS |
| Migration deferred | PASS |
| Public caveat captured | PASS |
| Public export deferred | PASS |

## Return Conditions

Return to orchestrator if dependency migration, package edit, auth runtime edit,
public-sync, or production auth claim is required.

## Operator Checkpoint

N/A with reason: decision baseline remains inside autonomous private scope.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Web package manifest exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | file source | `package.json` | cvf-web package manifest | ACCEPT |
| `next-auth` beta dependency is declared | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | line 30 | `next-auth` | dependency manifest | ACCEPT |
| T3 says current posture is not production-readiness proof | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | Decision / Baseline / Proposed Tranche | `Baseline for ERH-T4` | T3 boundary | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Verification | Status |
| --- | --- | --- | --- |
| ERH-T4 dependency decision | `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | path exists after implementation | PASS |
| Hold until T3 | dependency release row | T3 path exists | PASS |
| No migration in T4 | forbidden scope and diff review | PASS |

## Worker Autonomy / No-Question Rule

The worker proceeds autonomously for decision-record authoring and docs-only gate
remediation. Escalation is reserved for package changes, auth runtime edits,
public-sync, live proof, or production-readiness claim expansion.

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
| Dependency decision baseline exists | T4 baseline path | PASS |
| Migration is not performed in T4 | claim boundary | PASS |
| Public caveat is explicit | T4 baseline | PASS |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| T4 edits `package.json` or lockfiles | BLOCKS_CLOSURE |
| T4 claims production auth stability | BLOCKS_CLOSURE |
| T4 hides beta caveat from public-sync | BLOCKS_CLOSURE |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T4_NEXT_AUTH_BETA_DECISION_2026-06-04.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` and `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | T4 docs closure plus DEP1 successor decision | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH-T4 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `N/A with reason` | no corpus registry state changed by T4 dependency decision closure | BLOCKED with reason |
| Registry Markdown | `N/A with reason` | no corpus registry markdown state changed by T4 dependency decision closure | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no external digest consumed by T4 closure | N/A with reason |
| System loop interlock | `N/A with reason` | T4 is decision-only; successor DEP/AUD workflow chains own dependency checks | N/A with reason |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up handoff sync commit required after closure commit | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Beta dependency risk needed explicit decision | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | separate migration/stability work order before production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision baseline only.

Next action: ERH-T1B may export a short dependency caveat.

## Claim Boundary

This work order records a dependency decision only. It does not migrate auth,
prove production readiness, or publish public docs.
