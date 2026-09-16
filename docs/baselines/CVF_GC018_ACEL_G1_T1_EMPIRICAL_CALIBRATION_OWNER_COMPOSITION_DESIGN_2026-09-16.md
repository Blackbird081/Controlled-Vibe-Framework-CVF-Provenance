# CVF GC-018 Baseline - ACEL G1 T1 Empirical Calibration Owner Composition Design

Memory class: governed-dispatch-baseline

docType: baseline

Status: AUTHORIZED_READY

Batch ID: ACEL-G1-T1-EMPIRICAL-CALIBRATION-OWNER-COMPOSITION-DESIGN

Dispatch base head: `9058a72d55fff417ca1149fdee58f2b411f68b46`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local reviewer/orchestrator

Worker target: INTERNAL_AGENT design and source-verification worker

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one bounded design pass for the missing G1 linkage:
`task class -> candidate configuration -> measured evaluation -> operating-point
decision -> regression`. The pass must adapt existing benchmark, behavioral-
evaluation, direct-calibration, and provider-readiness owners rather than create
a competing architecture.

## Operator Authorization

The operator directed Local to choose and write one work order. Local selects
G1 before G4 because comparable baseline/candidate and evaluation semantics are
prerequisites for a later incremental-value owner. The shared-workspace worker
is `INTERNAL_AGENT`; Local retains review, decision, and commit ownership.

## Target / Source

The bounded source set is the accepted ACEL T0 G1 record, current performance
benchmark contract/tests, current direct candidate-calibration contract/runner,
the accepted G3 behavioral-evaluation owner, and provider-lane readiness.
External Web research is closed advisory context only and is not a worker design
authority.

## Scope / Methodology

Produce a CVF-native owner composition and an exact later implementation
manifest. Decide identity, comparability, partition/holdout, provenance,
measurement, eligibility, decision, invalidation, and regression semantics.
Prevent circular selection, scalar-score laundering, provider-readiness
overclaim, and automatic configuration mutation.

## Proposed Tranche

One INTERNAL_AGENT creates exactly three uncommitted design/evidence artifacts.
All source, test, checker, registry, lifecycle, continuity, runtime, and provider
paths are read-only.

## Required Evidence

- exact ten-source path/hash/status ledger;
- T0-to-current freshness comparison;
- owner/consumer/dependency graph with one canonical composition owner;
- full closed-loop contract and fail-closed negative cases;
- explicit relationship to G3 evidence and future G4 measurement;
- exact successor source/test/checker manifest or a named blocker;
- zero provider, credential, network, runtime, or configuration mutation.

## Non-Goals

- no implementation, benchmark run, provider call, calibration run, or retry;
- no operating-point promotion or mutation;
- no G4 marginal-value implementation;
- no GC-026 promotion, provider certification, package lifecycle, hook, CI,
  runtime, public-sync, deployment, or production change;
- no adoption of an external advisory contract as CVF design authority;
- no automatic successor execution.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | bounded G1 owner-composition design | three uncommitted documents only | current private-CVF paths and hashes | implementation needs a separate work order | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no calibration adapter authorized | no external ingress, call, receipt, or mutation | external research already closed as advisory evidence | separate adapter authority required | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| G1 is accepted as `ADAPT` | AUTHORITY | `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md` | Findings / Position | G1 empirical execution calibration | Local T0 completion | ACCEPT |
| no closed task-class operating-point loop was proved | GAP_FACT | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_2026-09-15.md` | G1 - Empirical execution calibration | G1-C1 through G1-C3 | ACEL T0 audit | ACCEPT |
| machine ledger records the three G1 claims | EVIDENCE | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_EVIDENCE_T0_2026-09-15.json` | `claims` | G1-C1; G1-C2; G1-C3 | ACEL evidence ledger | ACCEPT |
| benchmark owner is instrumentation-only and proposal-only | CONTRACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/performance.benchmark.harness.contract.ts` | module contract and exported types | `PerformanceBenchmarkHarnessContract`; `EvidenceClass` | benchmark owner | ACCEPT |
| benchmark lifecycle is unit tested | TEST | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/performance.benchmark.harness.contract.test.ts` | benchmark test suites | init/start/record/complete/report | benchmark tests | ACCEPT |
| direct candidate evaluation is deterministic and bounded | CONTRACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts` | exported parser/rubric/evaluator | `evaluateHarderCandidate` | G2/T6A adjacent owner | ACCEPT |
| direct calibration runner is task-specific, not a general owner | IMPLEMENTATION | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-oa-t6a-candidate-calibration.ts` | runner flow | fixed task/model/result path | calibration runner | ACCEPT |
| G3 supplies admitted behavioral evidence semantics | CONTRACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts` | exported evidence and grading contracts | `gradeBehavioralEvaluation`; baseline pairing | G3 behavioral owner | ACCEPT |
| G3 is closed offline and parked | DEPENDENCY | `docs/reviews/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_COMPLETION_2026-09-16.md` | Terminal Decision | `CLOSED_PASS_BOUNDED_G3_PARKED` | Local completion | ACCEPT |
| provider readiness calibrates lane usability, not task configuration | CLAIM_BOUNDARY | `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` | Status Key and Claim Boundary | `CANARY_PASS`; `CERTIFIED` | provider readiness owner | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| five exact dispatch/output paths | all returned `False` under `Test-Path` before authoring | NO_COLLISION |
| exact batch/path tokens | `rg` over docs, state, extensions, and checker roots returned no match | NO_COLLISION |
| general operating-point owner | bounded Local G1 audit found only adjacent pieces | ADAPT_EXISTING_OWNERS |
| G4 overlap | incremental value remains a separate audit question | DEFER_G4; DO_NOT_MERGE |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch-ready status, prompt envelope fields, source-verification columns, SCEC shape, route manifest, coordination binding, return contract and no-commit evidence |
| gateRunPurpose | confirm source and packet shape before dispatch |
| claimBoundary | structural conformance does not prove the G1 design or implementation |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044 (10 returned; resolver
reported truncation). Dispatch impact: exact bounded corpus, private-CVF source
authority, checker read-ahead, no protected worker paths, exact output manifest,
no provider authority, and one complete return packet.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":"docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md"}
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design dispatch; public-sync is outside scope.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: calibration owner design only.

Target lifecycle state: unchanged.

Prior phase evidence: accepted ACEL T0 G1 disposition and accepted G3 contract.

Next forbidden skip: implementation or operating-point promotion without a separate work order.

Runtime/provider proof: N/A with reason: explicitly forbidden.

Claim boundary: package and skill lifecycle are not modified.

## Claim Boundary

This baseline authorizes exactly one documentation-only G1 owner-composition
design pass. It does not authorize implementation, provider/live execution,
configuration selection or mutation, G4 work, runtime wiring, public sync,
deployment, production, or an automatic successor.
