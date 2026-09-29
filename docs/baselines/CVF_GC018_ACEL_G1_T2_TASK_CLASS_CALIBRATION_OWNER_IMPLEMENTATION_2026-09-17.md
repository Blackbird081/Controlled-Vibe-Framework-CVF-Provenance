# CVF GC-018 Baseline - ACEL G1 T2 Task-Class Calibration Owner Implementation

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: ACEL-G1-T2-TASK-CLASS-CALIBRATION-OWNER-IMPLEMENTATION

Dispatch base head: `899f162dece18abf42980cb82dab671626d6672e`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local reviewer/orchestrator

Worker target: shared-workspace `INTERNAL_AGENT`

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one bounded, pure offline implementation of the accepted G1
task-class calibration decision-layer design. Implement its five-path
successor manifest, add an implementation audit and full worker return, and
leave every output uncommitted for Local review. This is contract execution
on synthetic evidence, not empirical calibration or configuration selection.

## Operator Authorization

The operator asked Local to continue after the G1 and G4 design closures.
V61 permits Local to select one separately governed bounded ACEL delta.
Local selects G1 T2 because G4's future comparable marginal-value evidence
would benefit from G1's candidate/evidence identity and decision semantics.
The G1 and G4 audit questions remain independent. A shared-workspace worker
is `INTERNAL_AGENT` regardless of provider.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| G1 T1 completion | `docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md`, SHA-256 `4c8a4978ba9da86af8fe45276dbe7f875bc442e296fcd600f8b834e0d95e4644`, `CLOSED_PASS_BOUNDED` | accepted design, implementation separate | RELEASED |
| G1 T1 machine manifest | `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`, SHA-256 `c8c1f6899e50513141e69113b8ac9faf37669b1fcd785bc2df3b88d8e894505b` | exact five successor paths, zero blocker | RELEASED |
| current continuity | `AGENT_HANDOFF_V61_2026-09-16.md` and compact bootstrap | Local may select one bounded delta | RELEASED_FOR_G1_T2_ONLY |

## Scope Baseline

Worker may create exactly the seven paths listed in the paired work order:
five design-manifest implementation outputs, one implementation audit, and
one full worker return. The TypeScript decision layer is pure and does not
invoke a provider, execute a benchmark, mutate an operating configuration, or
write a regression record to a live store. The Python checker only reads
explicit evidence files and returns a verdict.

## Acceptance Baseline

- Bind task class, candidate configuration hash, fixture/trace/result hashes,
  and producer receipt before any candidate decision.
- Preserve SEARCH versus HELD_OUT membership and reject contamination.
- Enforce exclusive precedence: incomparable, insufficient evidence,
  ineligible, then eligible/preference.
- Use G3 admission/grading evidence without making G3 attest candidate identity.
- Keep raw `PROPOSAL_ONLY` benchmark evidence exploratory; no preferred point
  or RegressionBinding without a separately admissible preference basis.
- Treat provider readiness as eligibility only, never ranking evidence.
- Emit regression binding only for one admissibly preferred candidate;
  invalidation marks it stale, never rolls back or mutates configuration.
- Cover all declared negative cases with focused TypeScript and Python tests;
  parse/typecheck and required return gates must pass.

## Baseline Decision

Release the exact seven-path offline implementation tranche to one
`INTERNAL_AGENT` under `WORKER_MUST_NOT_COMMIT`. Local retains review,
closure, commits and all later expansion decisions.

## Proposed Tranche

The worker creates five accepted successor paths and two evidence paths.
The predecessor design remains read-only and G4 remains independently parked.

## Evidence / Verification

Dispatch evidence is the clean base, exact predecessor hashes, path-absence
checks and pre-dispatch gate. Worker evidence must be produced under the
paired work order; this baseline does not inherit a test PASS.

## Forbidden Expansion

No provider/live call, real empirical value experiment, G4 implementation,
configuration mutation, Core change, runtime/dispatcher wiring, package or
skill lifecycle edit, benchmark promotion, GC-026 tracker mutation, hook/CI,
public sync, deployment, production claim, stage, or worker commit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| design accepted for separate implementation | DEPENDENCY | `docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md` | Decision / Recommendation / Disposition | `DESIGN_READY_FOR_SEPARATE_IMPLEMENTATION_WORK_ORDER` | Local completion review | ACCEPT |
| five planned paths and decision semantics | MANIFEST | `docs/audits/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` | `successorManifest`, `candidateEvidenceBinding`, `classificationPrecedence` | G1 T1 machine design | G1 design | ACCEPT |
| G3 grading and fixture admission exist | CONTRACT | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts` | `gradeBehavioralEvaluation`, `admitFixtureSet` | G3 owner | G3 pure contract | ACCEPT |
| benchmark evidence remains proposal-only | CONTRACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/performance.benchmark.harness.contract.ts` | `EvidenceClass` | `PROPOSAL_ONLY` | benchmark harness | ACCEPT |

## Negative Search And Collision Discipline

All seven exact worker paths and both dispatch paths returned `False` under
`Test-Path` at clean base `899f162dece18abf42980cb82dab671626d6672e`.
Do not convert the absent exact paths into a repository-wide absence claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | baseline status, Source Verification Block, checker read-ahead, no-commit scope |
| gateRunPurpose | dispatch structure confirmation only |
| claimBoundary | no implementation result or empirical proof |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | predecessor and current source SHA-256, synthetic tests only |
| reason | offline pure owner implementation |
| requiredFutureAction | separate authority for real calibration or runtime use |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T2-TASK-CLASS-CALIBRATION-OWNER-IMPLEMENTATION --title "ACEL G1 T2 Task-Class Calibration Owner Implementation" --date 2026-09-17 --base 899f162dece18abf42980cb82dab671626d6672e --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-17.md --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key acel-g1-empirical-calibration-owner-composition --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T1_EMPIRICAL_CALIBRATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md --scec-predecessor-sha256 72a672175a43503d514187d0928667e676b7f4af159e45447a8afdde0ea0c1ea --scec-required-disposition READY_WITH_EXECUTABLE_PROOF --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | manual governed dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | exact G1 dependency, scope and seven-path implementation |
| checkerReadAheadConfirmation | dispatch and structural controls |
| docOnlyNewFields | none |
| claimBoundary | scaffold provenance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`. Returned ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044; count 10, truncated from 24 candidates.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired G1 T2 work order | `DISPATCH_READY` | PASS |
| Completion or reviewer artifact | future Local completion review | worker has not returned | BLOCKED with reason: pre-execution |
| Roadmap state | V61 active continuity | G1 T2 selected, other deltas parked | PASS |
| Registry JSON | G1 T1 design manifest | five successor paths | PASS |
| Registry Markdown | G1 T1 human design | accepted by Local review | PASS |
| External evidence digest | N/A with reason: no new external input | advisory phase closed | N/A with reason |
| System loop interlock | no runtime consumer | pure offline scope | N/A with reason: runtime forbidden |
| Session continuity | active handoff/state | post-dispatch sync required | BLOCKED with reason: follows dispatch material commit |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| predecessor | accepted G1 design with five exact paths | hashes and path-absence verified at dispatch | PASS |
| pure offline implementation | seven worker outputs, focused tests and gates | pending worker return | BLOCKED with reason: pre-execution |
| external effects | zero | none in dispatch | PASS |

## Claim Boundary

This baseline releases only a seven-path offline implementation worker task.
It does not prove a measured operating point, authorize provider execution,
open G4, or grant any runtime or public-export permission.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
