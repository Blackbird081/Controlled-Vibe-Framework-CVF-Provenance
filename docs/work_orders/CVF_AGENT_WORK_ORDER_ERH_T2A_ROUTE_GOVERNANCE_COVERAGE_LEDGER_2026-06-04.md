# CVF Agent Work Order - ERH-T2A Route Governance Coverage Ledger

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `b5cf8882`

executionBaseHead: `b5cf8882`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Execute ERH-T2A by producing a filesystem-backed route governance coverage
ledger for the web API route corpus. Success means every current
`src/app/api/**/route.ts` file is listed with method, auth/governance evidence,
and a bounded disposition.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator authorization | 2026-06-04 autonomous ERH tranche instruction | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| T1A calibration | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- enumerate `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/**/route.ts`;
- create `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md`;
- classify evidence as lexical/source-surface proof only.

Forbidden scope:

- edit runtime routes, tests, CI workflows, or public-sync files;
- claim semantic governance enforcement for a route without source-specific
  evidence;
- run live/provider proof.

Risk ceiling: R0 docs-only inventory.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | private ERH route-ledger tranche |
| Implementer | Codex | filesystem-backed docs inventory |
| Reviewer | Codex self-review pending operator review | no runtime route claim |
| Operator approval required for | runtime route edits, public-sync, live proof, commit/push | not used |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | authority |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | tranche scope |
| `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | claim boundary |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git rev-parse --short HEAD` | capture base anchor |
| `Get-ChildItem -LiteralPath 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api' -Recurse -Filter route.ts` | route list |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b5cf8882 --head HEAD` | PASS |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | create/update |
| `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | create/update |

Forbidden paths: runtime route files, tests, public-sync clone, workflows.

## Execution Plan

| Step | Input | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | route filesystem enumeration | route list | unreadable route |
| 2 | shallow lexical/auth scan | route ledger | count mismatch |
| 3 | corpus and governance gates | pending-review packet | gate failure outside scope |

## Evidence Requirements

| Evidence | Path or command | Required at handoff |
| --- | --- | --- |
| Route count | route enumeration command | Yes |
| Route ledger | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | Yes |
| Corpus blocks | completeness and classification sections | Yes |

## Review Gate

| Gate | Requirement |
| --- | --- |
| Completeness | 68 route rows and zero unresolved files |
| Claim boundary | lexical hit is not semantic proof |
| Pre-closure | N/A with reason: no commit in `WORKER_MUST_NOT_COMMIT` mode |

## Closure Checklist

| Item | Status |
| --- | --- |
| All routes listed | PASS |
| Gap summary included | PASS |
| Runtime edits avoided | PASS |
| Public export deferred | PASS |

## Return Conditions

Return to orchestrator if route files cannot be read, runtime proof is required,
public-sync is requested, or semantic enforcement must be claimed.

## Operator Checkpoint

N/A with reason: operator authorized autonomous private tranche execution; T2A
does not cross public-sync, live proof, runtime edit, or commit/push boundary.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Web API route root exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api` | filesystem enumeration | `src/app/api` | Next.js API route tree | ACCEPT |
| Route file count is 68 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api` | `Get-ChildItem -Recurse -Filter route.ts` | `route.ts` | route inventory command | ACCEPT |
| Session auth helper appears in route corpus | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/evaluate/route.ts` | line 2 | `verifySessionCookie` | route auth import | ACCEPT |
| Governance envelope appears in approval route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/route.ts` | source search | `buildGovernanceEnvelope` | approval route governance evidence | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Verification | Status |
| --- | --- | --- | --- |
| ERH-T2A route governance coverage ledger | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | 68 route rows | PASS |
| Do not treat lexical hits as coverage proof | ledger boundary and dispositions | explicit claim boundary | PASS |
| Feed ERH-T2B CI plan | gap summary table | T2B dependency release | PASS |

## Worker Autonomy / No-Question Rule

The worker proceeds autonomously for route enumeration, table generation,
documentation remediation, and gate reruns inside this docs-only scope.
Escalation is reserved for runtime route edits, CI workflow edits, public-sync,
live/provider proof, or claim-boundary expansion.

## Evidence / Verification

Required component gates:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base b5cf8882 --head HEAD --all-changed --enforce
python governance/compat/check_finding_to_governance_learning.py --base b5cf8882 --head HEAD --enforce
python governance/compat/check_corpus_completeness_report_integrity.py --base b5cf8882 --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base b5cf8882 --head HEAD --enforce
```

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| All 68 route files are listed | route ledger table | PASS |
| Missing-proof routes are not hidden | gap summary | PASS |
| No runtime edit is made | `git diff --name-status` at review | PASS |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| Route count self-reported without filesystem command | BLOCKS_CLOSURE |
| Lexical hit converted into semantic route governance proof | BLOCKS_CLOSURE |
| Runtime route files edited in T2A | BLOCKS_CLOSURE |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` | initial private tranche closure | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH-T2A row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `N/A with reason` | no corpus registry state changed by T2A route-ledger closure | BLOCKED with reason |
| Registry Markdown | `N/A with reason` | no corpus registry markdown state changed by T2A route-ledger closure | BLOCKED with reason |
| External evidence digest | `N/A with reason` | route corpus is local source inventory, not external corpus digest | N/A with reason |
| System loop interlock | `N/A with reason` | T2A is source inventory; successor ERH-T2C owns GC-052 route proof | N/A with reason |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up handoff sync commit required after closure commit | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Public route coverage lacked a complete ledger | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | consider CI checker after ledger stabilizes |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance route ledger only. Public export requires ERH-T1B.

Next action: cite this ledger in the public-sync README/catalog handoff.

## Claim Boundary

This work order produces a source-backed inventory and gap ledger only. It does
not prove live route behavior, production coverage, or runtime enforcement.
