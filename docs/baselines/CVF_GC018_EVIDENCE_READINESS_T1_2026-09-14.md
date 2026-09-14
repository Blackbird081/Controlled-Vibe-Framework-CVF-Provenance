# CVF GC-018 Baseline - Evidence Readiness Foundation
Memory class: governed-dispatch-baseline
docType: baseline
Status: APPROVED_FOR_EXECUTION
Date: 2026-09-14
Batch ID: EVIDENCE-READINESS-T1
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: 7a4501c5a20430c1283d02949537d0fc1b2d06a1

## Purpose
Authorize the operator-prioritized evidence-readiness foundation before more R4
finding repair. Extend the existing return checker; do not add a hook process.

## Decision / Baseline
APPROVED_FOR_EXECUTION after pre-dispatch passes. Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_EVIDENCE_READINESS_T1_2026-09-14.md`.
Exact worker paths, acceptance matrix, migration and latency budgets are binding.
R4 stays parked and its two untracked files remain byte-identical.

## Scope / Target / Owner Boundary
Nine worker paths from paired work order. Local owns acceptance, commit and
continuity. No mirror acquisition, upstream code execution, project runtime,
provider, public-sync, deployment or R4 editing.

## Source Verification Block
| Fact | Source file | Verified section | Disposition |
| --- | --- | --- | --- |
| Existing structural checker | governance/compat/check_worker_return_quality_gate.py | diagnose and run | ACCEPT |
| Existing gate calls checker | governance/compat/run_worker_return_fast_gate.py | build_commands | ACCEPT |
| Canonical shape owner | docs/reference/work_order_authoring/CVF_WORKER_RETURN_QUALITY_GATE_STANDARD.md | Required Worker-Return Shape | ACCEPT |

## Acceptance Criteria
All rows in paired acceptance table, automatic integration proof, bounded source
resolution and measured latency. Worker returns pending review without commits.
Tests cannot claim actual reading, perfect discovery or semantic correctness.

## Evidence / Verification
Focused negative/positive and existing integration tests, paired baseline timings,
complete return gate, and immutable parked-input hashes. Use synthetic fixtures;
never execute upstream or mutate original R4 evidence.

## Checker Source Read-Ahead Block
| Field | Evidence |
| --- | --- |
| applicableCheckersRead | governance/compat/check_worker_return_quality_gate.py; governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_gate_to_role_closeability.py |
| literalTokensReviewed | pending return and required shape; automatic call sites; exact ownership |
| gateRunPurpose | Confirm dispatch evidence and structure |
| claimBoundary | No implementation acceptance |

## ADIF Defect Registry Disclosure
Resolver query: taskClass=`governance-machine-hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class governance-machine-hardening --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`.
Returned defects: NONE_RETURNED; items=[], totalCandidates=0, truncated=false.

## Agent Operation Trace Block
| Field | Evidence |
| --- | --- |
| Actor | Local dispatcher |
| Surface | local workspace |
| Operation | source inspection, scoped packet and continuity |
| Target paths | this baseline and paired work order |
| Allowed scope | operator priority change and foundation authorization |
| Claim boundary | Dispatch only |

## Claim Boundary
This is governance implementation authority only. Program remains open; R4 repair
parked. No implementation has been accepted by creating this baseline.

## Public Export Disposition
DEFERRED_PRIVATE_ONLY
Private provenance packet; no public artifact or sync scope.
