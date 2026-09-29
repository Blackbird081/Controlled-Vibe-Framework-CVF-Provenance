# CVF GC-018 Baseline - ACEL G2 T2 Candidate Qualification T0

Memory class: governed-dispatch-baseline

Status: READY_FOR_DISPATCH

Batch ID: ACEL-G2-T2-CANDIDATE-QUALIFICATION-T0

Dispatch base head: `eb88000344966c08209c155be8f70f53b501b0d8`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: Local reviewer/closer

Worker target: one INTERNAL_AGENT evidence worker

## Purpose

Determine whether the already-implemented MAO-OA-T6A harder-task contract is a
truthful candidate for a separately authorized fresh direct-lane calibration.
This tranche repairs candidate selection evidence only; it does not run an
agent, call a provider, build the T1-to-MAO seam, or execute G2-T2.

## Source / Predecessor Evidence

The predecessor is the Local-accepted G2-T2 blocked-design worker return at
material commit `f92db17c477211e5a1bb9f37e9331acc4776fd6e`, SHA-256
`e37f855587866d2007e52679a8d2fe68468388effdbe41404c15bb78266e79ea`.
It establishes `NO_QUALIFIED_HARDER_CANDIDATE` as the first blocker and keeps
the callable-seam blocker parked behind candidate qualification.

## Decision / Baseline / Proposed Tranche

Decision: open one read-only INTERNAL_AGENT qualification tranche against the
exact twelve-source corpus. Baseline: the historical T6A result stays rejected
because sanitized scorer input was absent. Proposed tranche: decide only
whether the current T6A task/evidence contract is ready for a separately
authorized fresh direct calibration.

## Target / Source

The worker must read and hash exactly these twelve current CVF-governed paths:

1. `docs/reviews/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_WORKER_RETURN_2026-09-16.md`
2. `docs/audits/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_MANIFEST_2026-09-16.json`
3. `docs/baselines/CVF_GC018_MAO_OA_T6A_HARDER_CANDIDATE_DIRECT_BASELINE_CALIBRATION_2026-07-17.md`
4. `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_OA_T6A_HARDER_CANDIDATE_DIRECT_BASELINE_CALIBRATION_2026-07-17.md`
5. `docs/reviews/CVF_MAO_OA_T6A_HARDER_CANDIDATE_DIRECT_BASELINE_CALIBRATION_COMPLETION_REVIEW_2026-07-17.md`
6. `docs/reviews/CVF_MAO_OA_T6A_WORKER_RETURN_2026-07-17.md`
7. `docs/reviews/evidence/mao-oa-t6a-direct-candidate-calibration-2026-07-17.json`
8. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts`
9. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.harder.value.candidate.contract.test.ts`
10. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts`
11. `docs/reviews/CVF_MAO_OA_T7_FINAL_ROADMAP_CLOSURE_COMPLETION_REVIEW_2026-07-17.md`
12. `docs/reviews/CVF_MAO_OA_T7_INDEPENDENT_CRITIQUE_AND_ROADMAP_CLOSURE_ASSESSMENT_2026-07-17.md`

## Admission Decision

The only allowed terminal decisions are:

- `QUALIFIED_FOR_FRESH_DIRECT_CALIBRATION_PACKET`: the task, prompt, parser,
  deterministic rubric, material-defect rules, sanitized evidence shape, and
  independent rescoring path are all reconstructable; this permits Local to
  author a later calibration packet but admits no live result.
- `BLOCKED_TASK_NOT_RECONSTRUCTABLE`: one or more required task or evidence
  elements cannot be reconstructed from current sources.
- `REJECTED_DUPLICATE_OR_EASY`: the candidate is semantically equivalent to
  the excluded prime-number task or cannot plausibly exercise review value.

The historical T6A score, zero-defect result, and release boolean remain
`NOT_ACCEPTED`. Missing sanitized scorer input may not be repaired by inference.

## Required Artifact Manifest

The worker owns exactly three uncommitted paths:

1. `docs/audits/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.json`
2. `docs/audits/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_2026-09-16.md`
3. `docs/reviews/CVF_ACEL_G2_T2_CANDIDATE_QUALIFICATION_T0_WORKER_RETURN_2026-09-16.md`

No other repository path may change.

## Evidence Requirements

- Reconcile all twelve source paths with SHA-256, byte count, and terminal status.
- Separate task qualification from historical-output qualification.
- Demonstrate that the prospective runner persists sanitized candidate content
  required for independent rescoring, without executing it.
- Compare the harder task against the excluded prime-number task on structure,
  ambiguity, rubric dimensions, material-defect detection, and revision value.
- Name every remaining blocker between candidate qualification, fresh direct
  calibration, callable-seam implementation, and the eventual A/B experiment.
- Record zero agent/provider/network/credential/runtime effects.

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_WORKER_RETURN_2026-09-16.md"
}
```

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| five proposed paths | all returned `False` before authoring | NO_COLLISION |
| exact batch token | no existing governed artifact matched before authoring | NO_COLLISION |
| related owner search | T6A contract, test, runner, receipt and Local completion exist | REUSE_CURRENT_OWNERS |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| literalTokensReviewed | dispatch readiness, exact source rows, route enums, convergence fields, no-commit return, corpus reconciliation, coordination binding and forbidden provider authority |
| gateRunPurpose | confirm dispatch shape before pre-dispatch |
| claimBoundary | checker conformance does not qualify the candidate |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G2-T2-CANDIDATE-QUALIFICATION-T0 --title "ACEL G2 T2 Candidate Qualification" --date 2026-09-16 --base eb88000344966c08209c155be8f70f53b501b0d8 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic no-commit worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact twelve-source audit, three-output manifest, terminal decision vocabulary and zero-call boundary |
| checkerReadAheadConfirmation | applicable dispatch, coordination, corpus and handoff checker sources read |
| docOnlyNewFields | taskQualification; historicalResultDisposition; calibrationReadiness; downstreamBlockers |
| claimBoundary | dispatch authoring only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033 and ADIF-0044; resolver result was
truncated at 10 of 24 candidates. Dispatch impact: exact corpus, per-source
evidence, no external authority, checker read-ahead, no protected mutation,
no provider authority, and no child timeout beyond the parent lane.

## Claim Boundary

This baseline authorizes read-only Local candidate qualification and exactly
three uncommitted evidence outputs. It does not authorize a provider call,
fresh calibration, actual-agent execution, callable-seam implementation,
runtime/source mutation, credential access, public sync, deployment, or
production behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private candidate-selection evidence; no public artifact is authorized.
