# CVF Agent Work Order - ERH-T3 Evidence Durability Boundary

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-04

dispatchBaseHead: `b5cf8882`

executionBaseHead: `b5cf8882`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Execute ERH-T3 by creating a docs-only evidence durability boundary packet.
Success means public-facing claims can distinguish tmp JSON web evidence,
optional CSV signing, guard-contract SQLite audit storage, in-memory rate
limits, process-lifetime policy snapshot IDs, pattern safety filters, and
non-wired benchmark live emission.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator decision | ERH planning review says evidence durability/rate limit/policySnapshotId are docs-first this batch | ACCEPT |
| GC-018 | `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | ACCEPT |
| Roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ACCEPT |
| T1A calibration | `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | ACCEPT |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md`;
- cite current source facts for durability, signing, rate limit, policy snapshot,
  safety filter, and benchmark emission boundaries.

Forbidden scope:

- edit runtime storage, signing, rate-limit, safety, policy, benchmark, provider,
  or CI source;
- assert production durability, distributed rate limiting, persisted policy
  versioning, ML DLP, hash-chain signing, or live benchmark emission.

Risk ceiling: R0 docs-only.

## Agent Roles

| Role | Assignee | Boundary |
| --- | --- | --- |
| Orchestrator / dispatcher | Codex | private ERH durability tranche |
| Implementer | Codex | docs-only boundary packet |
| Reviewer | Codex self-review pending operator review | no runtime durability claim |
| Operator approval required for | runtime edits, public-sync, live proof, commit/push | not used |

## Required First Reads

| Path | Why it matters |
| --- | --- |
| `docs/baselines/CVF_GC018_ERH_EXTERNAL_REVIEW_HARDENING_2026-06-04.md` | authority |
| `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | tranche scope |
| `docs/reference/CVF_ERH_T1A_PUBLIC_CLAIM_CALIBRATION_2026-06-04.md` | public claim boundary |

## Pre-Flight Checks

| Command | Required result |
| --- | --- |
| `git rev-parse --short HEAD` | capture base anchor |
| `rg -n "CVF_CONTROL_PLANE_EVENTS_PATH|CVF_AUDIT_SIGNING_KEY|buckets|PII_PATTERNS|generatePolicySnapshotId|liveEmissionWired"` | source facts found |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b5cf8882 --head HEAD` | PASS |

## Write Ownership

| Owned path | Mode |
| --- | --- |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | create/update |
| `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | create/update |

Forbidden paths: runtime source, tests, public-sync clone, workflows.

## Execution Plan

| Step | Input | Output | Stop condition |
| --- | --- | --- | --- |
| 1 | source facts | verification table | missing source symbol |
| 2 | operator docs-first decision | durability boundary packet | runtime fix required |
| 3 | governance gates | pending-review state | gate failure outside scope |

## Evidence Requirements

| Evidence | Path or command | Required at handoff |
| --- | --- | --- |
| Source verification | source line citations | Yes |
| Boundary packet | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | Yes |
| Public export boundary | `DEFERRED_PRIVATE_ONLY` | Yes |

## Review Gate

| Gate | Requirement |
| --- | --- |
| Runtime edit check | no runtime/source files touched |
| Claim check | no durable-by-default or live-emission claim |
| Pre-closure | N/A with reason: no commit in `WORKER_MUST_NOT_COMMIT` mode |

## Closure Checklist

| Item | Status |
| --- | --- |
| Durability tiers documented | PASS |
| Runtime candidates deferred | PASS |
| T4 dependency boundary supplied | PASS |
| Public export deferred | PASS |

## Return Conditions

Return to orchestrator if runtime implementation, live proof, public-sync, or a
stronger durability claim is required.

## Operator Checkpoint

N/A with reason: docs-only boundary remains inside autonomous private scope.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Web control-plane store defaults to tmp JSON | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 86-89 | `CVF_CONTROL_PLANE_EVENTS_PATH` | `getStorePath` | ACCEPT |
| CSV export signing is key-gated | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/control-plane-events.ts` | lines 347-354 | `CVF_AUDIT_SIGNING_KEY` | `exportAuditEventsToCsv` | ACCEPT |
| Guard-contract SQLite audit wrapper exists | `EXTENSIONS/CVF_GUARD_CONTRACT/src/audit/sqlite-db.ts` | lines 50-65 | `AuditDatabase` | SQLite audit storage | ACCEPT |
| Rate limiter uses in-memory maps | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/rate-limit.ts` | lines 6-7 | `buckets` | `getRateLimiter` | ACCEPT |
| Safety filter uses regex pattern arrays | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety.ts` | lines 1-35 | `PII_PATTERNS` | `applySafetyFilters` | ACCEPT |
| Policy snapshot id is process-lifetime style | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts` | lines 39-50 | `generatePolicySnapshotId` | web governance envelope | ACCEPT |
| Benchmark live emission is false in contract | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | lines 85-90 and 206-226 | `liveEmissionWired` | `OperationalBenchmarkExtension` | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Verification | Status |
| --- | --- | --- | --- |
| ERH-T3 evidence durability claim boundary | `docs/reference/CVF_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | path exists after implementation | PASS |
| No runtime fix in this tranche | forbidden scope and diff review | PASS |
| Inform T4 dependency decision | production posture boundary table | PASS |

## Worker Autonomy / No-Question Rule

The worker proceeds autonomously for documentation output and gate remediation
inside this docs-only scope. Escalation is reserved for runtime edits,
distributed storage/rate-limit implementation, live/provider proof, public-sync,
or changing the docs-only claim boundary.

## Evidence / Verification

Required component gates:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base b5cf8882 --head HEAD --all-changed --enforce
python governance/compat/check_finding_to_governance_learning.py --base b5cf8882 --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base b5cf8882 --head HEAD --enforce
```

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| Durability tiers are documented | T3 output tier table | PASS |
| Rate-limit and policySnapshotId are bounded | T3 output boundary table | PASS |
| Runtime implementation is deferred | T3 claim boundary | PASS |

## Fail Conditions

| Condition | Disposition |
| --- | --- |
| T3 claims durable signed web evidence by default | BLOCKS_CLOSURE |
| T3 changes runtime/source files | BLOCKS_CLOSURE |
| T3 claims live benchmark emission while source says false | BLOCKS_CLOSURE |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T3_EVIDENCE_DURABILITY_BOUNDARY_2026-06-04.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_INITIAL_PRIVATE_TRANCHES_COMPLETION_2026-06-04.md` | initial private tranche closure | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH-T3 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `N/A with reason` | no corpus registry state changed by T3 durability-boundary closure | BLOCKED with reason |
| Registry Markdown | `N/A with reason` | no corpus registry markdown state changed by T3 durability-boundary closure | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no external digest consumed by T3 closure | N/A with reason |
| System loop interlock | `N/A with reason` | T3 is docs-only boundary; no new workflow-chain connection | N/A with reason |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up handoff sync commit required after closure commit | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Runtime-adjacent durability gaps need claim boundary before public claim | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | open separate runtime roadmap only after docs boundary |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance docs-only durability packet.

Next action: ERH-T1B may export summarized caveats after public-sync review.

## Claim Boundary

This work order closes only the private docs boundary for ERH-T3. It does not
implement durability hardening, live proof, production readiness, or public docs.
