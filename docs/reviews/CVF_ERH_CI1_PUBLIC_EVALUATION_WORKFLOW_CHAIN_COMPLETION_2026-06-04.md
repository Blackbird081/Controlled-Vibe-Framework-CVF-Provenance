# CVF ERH-CI1 Public Evaluation Workflow Chain Completion

Memory class: FULL_RECORD

Status: IMPLEMENTATION_COMPLETE_PENDING_REVIEW

docType: completion_review

Date: 2026-06-04

Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_2026-06-04.md`

GC-018: `docs/baselines/CVF_GC018_ERH_CI1_PUBLIC_EVALUATION_WORKFLOW_CHAIN_2026-06-04.md`

dispatchBaseHead: `40c3c10d`

executionBaseHead: `40c3c10d`

## Purpose

Record ERH-CI1 completion evidence. This tranche upgrades ERH-T2B from a
docs-only CI hardening plan into a marker-based public-evaluation workflow
chain with a machine checker, focused tests, hook/autorun wiring, and GC-052
system-loop routing.

## Scope / Target / Owner Boundary

Owned outputs:

- ERH-CI1 checker and focused checker tests;
- local hook and autorun wiring;
- ERH-CI workflow-chain reference packet;
- ERH-CI1 GC-018, work order, completion review, roadmap update;
- one GC-052 connection.

Boundary:

- no public-sync clone edit;
- no workflow-source rewrite;
- no dependency migration;
- no live/provider proof required;
- no production, hosted, public-readiness, or ordinary live-provider CI claim.

## Target / Source

Target: ERH-T2B CI hardening plan successor workflow chain.

Source authority:

- ERH-T2B CI hardening plan;
- current GitHub Actions workflow files;
- cvf-web package script declarations;
- ERH-T2C route-governance workflow chain;
- GC-052 system-loop registry.

## Implementation Summary

| Item | Result |
| --- | --- |
| Chain version | `cvf.erhCiPublicEvaluationWorkflow.ci1.v1` |
| Machine checker | added ERH CI public-evaluation workflow-chain checker |
| Focused tests | added three checker tests |
| Hook chain | wired checker into local pre-commit and pre-push |
| Autorun chain | wired checker into common autorun gates |
| System loop | added `erh-ci-plan-to-public-evaluation-workflow-chain` |
| Verdict | `READY_WITH_BOUNDARIES` |

## Findings / Position

Position: IMPLEMENTATION_COMPLETE_PENDING_REVIEW.

Findings:

| Finding | Position |
| --- | --- |
| T2B plan was useful but advisory-only | ACCEPT |
| Current repo has enough CI source markers for a bounded workflow chain | ACCEPT |
| Web lint/coverage exists in a dedicated web workflow, so evaluating only `cvf-ci.yml` is incomplete | ACCEPT |
| Protected live gate remains manual and must not be called ordinary CI | ACCEPT_WITH_BOUNDARY |

## Evidence Trace Block

| Evidence item | Artifact or command | Result |
| --- | --- | --- |
| Checker source | `governance/compat/check_erh_ci_public_evaluation_workflow.py` | created |
| Focused tests | `python -m pytest governance/compat/test_check_erh_ci_public_evaluation_workflow.py -q` | PASS, 3 tests |
| Chain check | `python governance/compat/check_erh_ci_public_evaluation_workflow.py --enforce` | PASS, `READY_WITH_BOUNDARIES` |
| System-loop check | `python governance/compat/check_system_loop_interlock.py --base 40c3c10d --head HEAD --enforce` | PASS |
| Worktree finality | `git status --short` | pending commit |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Evidence | Status |
| --- | --- | --- | --- |
| Continue ERH by workflow/system, not only hardening | checker plus GC-052 connection | checker/source diff | PASS |
| Preserve public claim calibration | bounded verdict and claim boundary | reference and completion packet | PASS |
| Keep public-sync separate | no public-sync files touched | diff/status | PASS |
| Avoid live/provider overclaim | protected live gate remains manual-only | checker boundary | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| ERH-T2B CI hardening plan could remain advisory prose | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | ERH-CI1 checker and hook/autorun wiring |
| T2B plan initially looked mostly at `cvf-ci.yml` and missed broader CI surfaces | DOCUMENTATION_GAP | GOVERNANCE_CONTROL_PLANE | RULE_CLARIFIED | checker evaluates multiple CI workflow surfaces |
| ERH-CI1 does not run provider/live proof or change runtime behavior | N/A | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | no runtime/provider/cost learning action; protected live gate boundary only |

## Risk / Corrective Action

| Risk | Corrective action | Status |
| --- | --- | --- |
| Overclaiming source markers as production-grade CI | checker verdict is `READY_WITH_BOUNDARIES` | PASS |
| Treating protected live gate as ordinary CI | checker requires `RUN_LIVE_GATE` marker and boundary text | PASS |
| T2B plan remaining prose-only | checker wired into hook and autorun chains | PASS |
| Public-sync drift | public export remains deferred | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance workflow-chain implementation has not been exported
to the public-sync repository.

Next action: after review/commit, decide whether a separate public-sync summary
should narrow the public CI caveat.

## Claim Boundary

ERH-CI1 may claim private machine-check evidence that public-evaluation CI
posture is now represented as a bounded workflow chain. It does not claim
GitHub Actions syntax validity, production-grade CI, dependency-audit
hardening, public-doc drift hardening, hosted freshness, public readiness, or
ordinary live-provider CI execution.
