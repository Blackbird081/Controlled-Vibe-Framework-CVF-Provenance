# CVF GC-018 Baseline - ACEL G2 T2 Discriminating Task Gate T2A

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-16

Batch ID: ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A

dispatchBaseHead: `253751977ee3a68f5360fec4b731d22635160bee`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local reviewer; operator owns any later live experiment.

Worker target: INTERNAL_AGENT in the shared workspace.

providerExecutionAuthority: FORBIDDEN

## Purpose

Turn the failed discrimination of the accepted direct candidate (100/100,
zero defects) into a new offline, executable task contract and independent
quality gate for a future G2-T2 fixed-versus-dynamic real-agent experiment.
This tranche produces no live candidate qualification and no topology result.

## Source / Authority Boundary

| Claim | Source | Local disposition |
|---|---|---|
| T1 direct result | `docs/reviews/CVF_ACEL_G2_T2_CALIBRATION_T1_LOCAL_DISPOSITION_2026-09-16.md` | one accepted bounded direct data point, `releaseCandidate=false`; cost-gate process deviation disclosed |
| Prior T2 design block | `docs/audits/CVF_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md` | no qualified hard task and no T1-to-MAO callable consumer |
| Existing scorer | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/harder.value.candidate.contract.ts` | read-only historical T6A contract; do not reinterpret its 100/100 result |
| Topology contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/runtime.topology.experiment.contract.ts` | pure isolated action contract only, not a composed runtime consumer |
| Existing task design owner | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G2_T2_REAL_AGENT_EXPERIMENT_DESIGN_2026-09-16.md` | next task needs independent grading, frozen task/controls and separate live authority |

## Scope / Target / Owner Boundary

The INTERNAL_AGENT may create one pure TypeScript task/scoring contract, one
focused test file with deterministic negative and positive fixtures, one
human-readable audit, and one worker return. Keep the new contract isolated:
no barrel export, MAO bridge, topology runtime hook, Model Gateway change,
provider execution grant, API key access, agent/subagent run, live test,
production routing, public sync or deployment. The existing T6A scorer,
historical and fresh receipts are read-only.

## Candidate And Gate Invariants

1. The task must model a realistic bounded CVF coordination decision with
   conflicting constraints, dependencies, failure/rollback and immutable
   authority. It must not be the July prime-number task or the just-scored
   two-engineer/48-hour plan with cosmetic difficulty added.
2. Freeze a complete prompt, expected output schema, deterministic grader,
   material-defect classes and release predicate before any future live run.
   The grader must evaluate observable output structure and semantic
   obligations, not keyword presence alone or a model's self-assessment.
3. Include a valid high-quality fixture, at least three distinct material
   failure classes, a plausible-but-wrong fixture, malformed output, missing
   evidence, authority violation and stop/rollback failure. Each fixture has
   an exact expected score/defect result and tests for deterministic replay.
4. The gate must fail closed on parse/evidence failure and distinguish
   candidate qualification from real-agent comparative value. A future
   direct-lane score <=80 or a predeclared material defect may qualify a task
   for a separately authorized T2 packet; it does not itself prove Policy B
   superiority or release a T1-to-MAO callable seam.
5. No post-hoc rubric adjustment after seeing a future provider response.
   If the task remains easy, record NOT_QUALIFIED and return to design, not
   another unbounded call.

## Evidence And Acceptance

The worker must show exact source/fixture hashes, source-to-rule traceability,
negative-test results, TypeScript result, no-provider/no-agent proof, exact
changed paths and a clear admission matrix. Local reviews task validity and
independent-grade quality; a green offline test suite proves only executable
contract behavior. The terminal output is `DESIGN_READY_FOR_LOCAL_REVIEW` or
`BLOCKED_WITH_REASON`, never `QUALIFIED_FOR_T2_LIVE`.

## Decision / Baseline / Proposed Tranche

Decision: authorize one INTERNAL_AGENT offline implementation of the task,
pure grader and negative tests. Baseline: the accepted direct candidate is
100/100 and does not release T6B; T2 composition remains blocked. Proposed
tranche: T2A exact four-path worker return followed by independent Local
review. No automatic T2B or live call follows.

## Risk / Corrective Action

The leading risk is answer-shaped overfitting: a task may be complex in prose
yet trivially satisfy its rubric. Require adversarial fixtures and explicit
separation of objective constraints from scoring implementation. A second
risk is accidental provider invocation through a test helper; prohibit
credential reads, network calls and any live runner command in this tranche.

## Negative Search And Collision Discipline

`rg --files docs/baselines docs/work_orders docs/audits docs/reviews` and
`rg -n ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A docs CVF_SESSION` found no
existing artifact for this task at dispatch base. New filenames are reserved
by the paired work order; the worker must recheck before writing.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G2-T2-DISCRIMINATING-TASK-GATE-T2A --date 2026-09-16 --base 253751977ee3a68f5360fec4b731d22635160bee --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source, worker paths, offline candidate/gate invariants and claim boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| docOnlyNewFields | candidateGate; noLiveQualification |
| claimBoundary | scaffold shape and this baseline do not prove task difficulty or runtime value |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`WORK_ORDER`, role=`DISPATCHER`, lifecyclePhase=`DISPATCH`.

Returned defects: NONE_RETURNED

Resolver result at dispatch base (`totalCandidates: 0`); resolver
command: `python governance/compat/run_adif_defect_resolver.py --task-class WORK_ORDER --role DISPATCHER --lifecycle-phase DISPATCH --max-results 8 --json`.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `providerExecutionAuthority: FORBIDDEN`; exact source paths and claim boundary |
| gateRunPurpose | confirmation of the already scoped offline packet, not discovery of source facts |
| claimBoundary | checker success cannot establish a qualified difficult task or authorize a call |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private G2-T2 candidate design, not a public catalog or public-sync
batch.

## Claim Boundary

This baseline authorizes only an offline executable task/quality-gate design
and worker evidence. It does not authorize provider use, agent execution,
comparative T2, T6B, callable seam, production, publication or deployment.
