# CVF Agent Work Order - ERH-T1A Public Claim Calibration

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `b5cf8882`

executionBaseHead: `b5cf8882`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Execute ERH-T1A from the official ERH roadmap by creating a private public-claim
calibration packet for future public README/catalog work. Success means another
agent can see which CVF public claims are allowed, bounded, deferred, or blocked
before any public-sync work starts.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator authorization | 2026-06-04 autonomous ERH tranche instruction | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V15_2026-05-29.md` | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| Planning response | `docs/reviews/CVF_ERH_PLANNING_REVIEW_CODEX_RESPONSE_2026-06-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md`;
- record private claim boundaries for future public GitHub README/catalog work;
- preserve public/provenance separation.

Forbidden scope:

- edit `README.md`, public-sync clone files, runtime source, workflow source, or
  provider/live proof scripts;
- claim output-quality parity, production readiness, public publication, or live
  governance proof.

Risk ceiling: R0 docs-only.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex acting under operator instruction | private ERH tranche only |
| Implementer | Codex | docs-only output |
| Reviewer | Codex self-review pending operator review | no public-sync or runtime claim |
| Human escalation boundary | public-sync, live proof, runtime edits, commit/push | not used in this tranche |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | authority |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | tranche scope |
| `docs/reviews/CVF_ERH_PLANNING_REVIEW_CODEX_RESPONSE_2026-06-04.md` | planning decisions |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git rev-parse --short HEAD` | capture base anchor |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b5cf8882 --head HEAD` | PASS before material edits |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | create/update |
| `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | create/update |

Forbidden paths: runtime source, public-sync clone, `.github/workflows/**`.

## Execution Plan

| Step | Input | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | GC-018 and roadmap | work order | missing authority |
| 2 | planning response and source facts | claim calibration packet | unverified source fact |
| 3 | governance gates | final pending-review state | gate failure outside scope |

## Evidence Requirements

| Evidence | Path or command | Required at handoff |
| --- | --- | --- |
| Output packet | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | Yes |
| Gate evidence | structural, public export, F2G gates | Yes |
| Diff boundary | `git diff --name-status` | Yes |

## Review Gate

| Gate | Requirement |
| --- | --- |
| Pre-implementation | PASS before material edits |
| Component gates | PASS before handoff |
| Pre-closure | N/A with reason: no commit in `WORKER_MUST_NOT_COMMIT` mode |

## Closure Checklist

| Item | Status |
| --- | --- |
| Acceptance criteria resolved | PASS |
| Commit mode recorded | PASS |
| Public/provenance boundary preserved | PASS |
| Public catalog action | N/A with reason: ERH-T1B only |

## Return Conditions

Return to orchestrator if public-sync, live proof, runtime edit, missing source,
or claim-boundary expansion is required.

## Operator Checkpoint

N/A with reason: operator authorized autonomous private tranche execution; no
checkpoint is needed unless the task crosses into public-sync, live proof,
runtime edits, or commit/push.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Public export disposition standard exists | `docs/reference/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` | file source | `Public Export Disposition` | public export standard | ACCEPT |
| F-1 closure artifact exists | `docs/reviews/archive/CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md` | file source | `CVF_F1_OUTPUT_QUALITY_PARITY_CLOSURE_NOT_MET_2026-05-15.md` | F-1 closure | ACCEPT |
| Benchmark live emission field exists | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | lines 85-90 | `liveEmissionWired` | `OperationalBenchmarkExtension` | ACCEPT |
| Safety filter pattern source exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts` | lines 1-35 | `PII_PATTERNS` | `applySafetyFilters` | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Verification | Status |
| --- | --- | --- | --- |
| ERH-T1A private claim calibration | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | path exists after implementation | PASS |
| Public-sync isolated to later work order | Public Export Disposition in output | `DEFERRED_PRIVATE_ONLY` | PASS |
| Mock usage samples not governance evidence | claim table row | direct text boundary | PASS |
| F-1 remains closed-not-met | claim table row | F-1 artifact cited | PASS |

## Worker Autonomy / No-Question Rule

The worker proceeds autonomously for documentation creation, source-fact checks,
allowed-scope gate handling, and repeated verification. Escalation is reserved
for public-sync, live/provider proof, runtime edits, workflow edits, destructive
actions, secrets/quota use, or claim-boundary expansion.

## Evidence / Verification

Required component gates:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b5cf8882 --head HEAD
python governance/compat/check_markdown_structural_completeness.py --base b5cf8882 --head HEAD --all-changed --enforce
python governance/compat/check_public_export_disposition.py --base b5cf8882 --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base b5cf8882 --head HEAD --enforce
```

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| Claim calibration packet exists | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | PASS |
| Public README/catalog work remains future public-sync | output claim boundary | PASS |
| No runtime or public README change is claimed | `git diff --name-status` at review | PASS |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| Public-sync performed from provenance workspace | BLOCKS_CLOSURE |
| Mock landing-page examples treated as governance evidence | BLOCKS_CLOSURE |
| Output-quality parity reopened | BLOCKS_CLOSURE |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` | initial private tranche closure | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH-T1A row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `N/A with reason` | no corpus registry state changed by T1A docs-only closure | BLOCKED with reason |
| Registry Markdown | `N/A with reason` | no corpus registry markdown state changed by T1A docs-only closure | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no new external digest consumed by T1A closure | N/A with reason |
| System loop interlock | `N/A with reason` | T1A is docs-only claim calibration | N/A with reason |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up handoff sync commit required after closure commit | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Public claims can be overread without calibration | OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | TEMPLATE_UPDATED | export calibration packet before public-sync |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this work order and output are private provenance artifacts only.

Next action: ERH-T1B public-sync handoff must execute from the public-sync clone.

## Claim Boundary

This work order completes private T1A documentation output only. It does not
publish public README/catalog changes, prove governance behavior, or close any
runtime hardening gap.
