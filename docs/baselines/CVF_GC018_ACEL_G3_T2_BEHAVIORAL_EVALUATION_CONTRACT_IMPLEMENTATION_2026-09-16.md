# CVF GC-018 Baseline - ACEL G3 T2 Behavioral Evaluation Contract Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-G3-T2-BEHAVIORAL-EVALUATION-CONTRACT-IMPLEMENTATION

Dispatch base head: `01a854f7b7ed80c35ab77ba02c7ffd273ae61658`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator.

Reviewer owner: Local reviewer/orchestrator.

Worker target: INTERNAL_AGENT implementation worker.

## Purpose

Authorize one offline implementation tranche for the accepted G3 behavioral-
evaluation design. The worker implements the normative contract, pure
TypeScript grader and tests, plus a read-only Python evidence checker and its
focused tests; Local alone reviews, repairs, closes, and commits.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| G3 T1 design completion | `docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md`, SHA-256 `175598c620caf4e106d4dd3b1a68522cc39a6412186109bb64f092d53b765148`, terminal `CLOSED_PASS_BOUNDED_DESIGN_READY` | exact accepted predecessor and clean continuity head | RELEASED |
| G3 T1 design manifest | `docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json`, SHA-256 `0af2a46edec9e31b879812c0beabead5582e00944db9cf616a904141d640c93e` | four declared successor paths and no blocker | RELEASED |

The fifth implementation path,
`governance/compat/test_check_assf_behavioral_evaluation_evidence.py`, is the
focused test companion required to make the declared Python checker
independently closeable. It does not expand the behavioral owner, add wiring,
or mutate a package or lifecycle state.

## Scope Baseline

Worker-owned paths are exactly:

1. `docs/reference/agent_system_skills/CVF_ASSF_BEHAVIORAL_EVALUATION_CONTRACT.md`
2. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/assf.behavioral.evaluation.contract.ts`
3. `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/assf.behavioral.evaluation.contract.test.ts`
4. `governance/compat/check_assf_behavioral_evaluation_evidence.py`
5. `governance/compat/test_check_assf_behavioral_evaluation_evidence.py`
6. `docs/audits/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_2026-09-16.md`
7. `docs/reviews/CVF_ACEL_G3_T2_BEHAVIORAL_EVALUATION_CONTRACT_IMPLEMENTATION_WORKER_RETURN_2026-09-16.md`

Allowed behavior is pure, deterministic local parsing, validation, grading,
and read-only evidence checking. Fixtures are synthetic. No real skill,
provider, agent, credential, network, runtime, or production action occurs.

## Acceptance Baseline

- one normative owner; existing ASSF lifecycle and package schemas are reused;
- runner and grader are separately invokable and share no mutable state;
- outcome and process/tool-order assertions are both mandatory;
- deterministic evidence requires one pass; stochastic evidence requires three
  consecutive passes;
- WITH/WITHOUT fixture inputs must be byte-identical;
- mock/replay evidence has provenance and expiry and never implies live proof;
- source-hash change invalidates prior evidence;
- malformed or unknown input fails closed;
- grader/checker never writes `certificationState: CERTIFIED`;
- all six accepted negative classes have focused regression tests;
- TypeScript and Python focused tests plus TypeScript typecheck pass.

## Baseline Decision

Release the exact seven-path, no-commit offline implementation tranche to one
INTERNAL_AGENT. Local retains review, repair, closure, commit, and every later
expansion decision.

## Evidence / Verification

Dependency hashes, source authority, initial path-absence checks, the ADIF
resolver result, scaffold provenance, and pre-dispatch gates are the dispatch
evidence. Worker implementation claims require the focused commands in the
paired work order and do not inherit PASS from this baseline.

## Forbidden Expansion

Do not edit package entries, generated skill index, lifecycle state, barrel
exports, package scripts, hooks, CI, autorun catalogs, release bundle, provider
matrix, session state, public-sync surfaces, runtime wiring, or deployment.
Do not run provider/live calls or real-skill evaluation. Do not commit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| implementation is released by accepted design | DEPENDENCY | `docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md` | Terminal Decision | `CLOSED_PASS_BOUNDED_DESIGN_READY` | Local completion review | ACCEPT |
| four successor paths are approved | MANIFEST | `docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_MANIFEST_2026-09-16.json` | `successorManifest.paths` | four exact paths | G3 T1 machine design | ACCEPT |
| lifecycle remains state authority | AUTHORITY | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | Certification And UAT State Model | `certificationState`; `uatState` | ASSF lifecycle contract | ACCEPT |
| package schema remains field authority | SCHEMA | `docs/reference/agent_system_skills/CVF_ASSF_PACKAGE_CONTRACT.md` | Compact Machine Source Schema | `acceptanceEvidence`; `evidenceRequirements` | ASSF package contract | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| seven worker paths | all returned `False` under `Test-Path` before authoring | NO_COLLISION |
| generic behavioral checker/test tokens | no current exact-path owner | NEW_BOUNDED_OWNER |
| adjacent ASSF admission checker | current checker and tests inspected | REUSE_PATTERN_DO_NOT_DUPLICATE_OWNER |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G3-T2-BEHAVIORAL-EVALUATION-CONTRACT-IMPLEMENTATION --title "ACEL G3 T2 Behavioral Evaluation Contract Implementation" --date 2026-09-16 --base 01a854f7b7ed80c35ab77ba02c7ffd273ae61658 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --scec-problem-key acel-g3-behavioral-evaluation-owner-composition --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/reviews/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_COMPLETION_2026-09-16.md --scec-predecessor-sha256 175598c620caf4e106d4dd3b1a68522cc39a6412186109bb64f092d53b765148 --scec-required-disposition READY_WITH_EXECUTABLE_PROOF --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | generic no-commit worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact dependency, seven-path closeable manifest, acceptance, gates, and forbidden boundary |
| checkerReadAheadConfirmation | dispatch, convergence, routing, closeability, trace, provider-authority, handoff, and Delta checker families |
| docOnlyNewFields | none |
| claimBoundary | dispatch authorization only; no implementation result |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | baseline decision/evidence headings, ADIF query shape, package-skill control, closure section, and ready status |
| gateRunPurpose | confirm baseline shape and evidence before dispatch |
| claimBoundary | structural compliance only; no implementation proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0007, ADIF-0016,
ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049 and
ADIF-0006.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: offline behavioral evidence contract implementation only.

Target lifecycle state: unchanged; no package or skill state mutation.

Prior phase evidence: accepted G3 T1 design completion and manifest.

Next forbidden skip: activation, UAT state change, certification, runtime, or
provider proof without a separate accepted work order.

Runtime/provider proof: N/A with reason: explicitly forbidden.

Claim boundary: package/skill references are schema inputs, not lifecycle
promotion authority.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired work order | `DISPATCH_READY` is the required pre-execution state | PASS |
| Completion or reviewer artifact | Local-owned future completion | N/A with reason: implementation has not run | N/A with reason |
| Roadmap state | active ACEL continuity | G3 T2 is operator-selected and intentionally open | PASS |
| Registry JSON | `docs/corpus-intelligence/registry/entries/acel-g3-t1-behavioral-evaluation-owner-composition-design.json` | GC-051 already covers the declared successor paths; mutation forbidden | PASS |
| Registry Markdown | `docs/audits/CVF_ACEL_G3_T1_BEHAVIORAL_EVALUATION_OWNER_COMPOSITION_DESIGN_2026-09-16.md` | accepted human design and successor manifest | PASS |
| External evidence digest | N/A with reason: no external evidence | zero external inputs | N/A with reason |
| System loop interlock | no runtime consumer | runtime forbidden | N/A with reason |
| Session continuity | active handoff/front doors | N/A with reason: Local projects dispatch commit after these gates | N/A with reason |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | NO_NEW_RUNTIME_CLAIM |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | clean HEAD, accepted predecessor hashes, exact path checks, and current source inspection |
| reason | implementation paths were checked at dispatch; runtime remains outside scope |
| requiredFutureAction | separate Local review before any integration or execution |

## Claim Boundary

This baseline releases only the seven-path offline implementation tranche. It
does not claim implementation success, behavioral quality of any real skill,
certification, live/provider evidence, runtime readiness, or public export.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private offline implementation dispatch; no public-sync authority.
