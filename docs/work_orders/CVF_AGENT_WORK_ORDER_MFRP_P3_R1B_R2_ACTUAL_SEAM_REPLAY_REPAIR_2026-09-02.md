# CVF Agent Work Order - MFRP-P3-R1B-R2 Actual-Seam Replay Repair

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-02

Batch ID: MFRP-P3-R1B-R2

Dispatch base head: `5cf4d663b7b0f25e2faff24c12d1a0d8b363df05`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: bounded local R1B-R2 replay-repair worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_2026-09-02.md`.

Paired baseline: `docs/baselines/CVF_GC018_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_2026-09-02.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: R1A-R2 is ratified at `e15cf55d8`; R1B-R2 repair
authoring is operator-authorized. The first R1B replay remains rejected
evidence. P4 is closed.

Do-not-misread notes: repair and rerun the existing helper; do not change P2,
the oracle, the old worker return, review admission, or P4. Machine completion
is evidence, not reviewer acceptance or safety truth.

Required first actions: complete startup acknowledgement; capture clean HEAD;
read this packet/baseline, guard orientation, literal gotchas, R1 redesign,
accepted oracle/return, rejected R1B adjudication, existing runner/test/ledger,
P2 owners and checker sources; recompute every frozen hash; run
pre-implementation; then touch only four paths.

Return contract: leave all changes uncommitted and return
`COMPLETE_PENDING_REVIEW` with one replay evidence candidate, or
`BLOCKED_WITH_REASON`. Do not emit reviewer acceptance or P4 readiness.

Worker: bounded local implementation worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md`

successorTrancheOpened: NO

## Purpose

Repair the existing R1B runner so it executes the ratified oracle's source
bindings, rejects real cited-source drift before seam calls, and emits the
complete per-case digest/classification evidence required by the R1 design.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

The dispatcher fixes authority, the worker implements the exact repair, and a
reviewer evaluates returned evidence without recreating the implementation.
SOT identities, actual P2 observations and deterministic ledger evidence, not
role/provider names, control trust.

Intake summary: operator authorized R1B repair after R1A-R2 acceptance to meet
the still-closed P4 prerequisite.

Risk sensitivity: protected local governance code and false-confidence risk;
P2, provider/live/public/production and destructive effects are forbidden.

Scope classification: bounded protected-governance local implementation and
deterministic evidence repair; no runtime route or external effect.

Escalation condition: stop for identity contradiction, P2/oracle change need,
secret risk, fifth repository path or unexplained zero-tolerance divergence.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP-P3-R1B-R2
reviewRoundCount: 1
priorFindingSetDigest: a042f80260042b7f71675edc57a8fb4e33ad5a1c70963c87a471d2123d85df5c
dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS
newIndependentCriticalEvidence: R1B_RV_1_SOURCE_BINDING_R1B_RV_2_ORACLE_CORRECTION_R1B_RV_3_LEDGER_COMPLETENESS
regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: ONE_CONSOLIDATED_REWORK
rootCauseClusterId: mfrp-p3-r1b-replay-evidence
reworkGeneration: 1
consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

The adjudicated findings and corrected oracle are already independently
reviewed. No further pre-execution review is admitted; routine review resumes
once at worker return.

## Worker Autonomy / No-Question Rule

Resolve routine in-scope implementation, test, ledger and gate defects from
the fixed contracts. Ask no preference questions. Stop only for a real
authority/source contradiction or forbidden-scope need.

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-p3-r1b-r2-repair",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["source-binding-not-executed", "cited-source-drift-not-tested", "ledger-digest-classification-incomplete"],
    "reopened": [],
    "current": ["source-binding-not-executed", "cited-source-drift-not-tested", "ledger-digest-classification-incomplete"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "MFRP-P3-R1B-R2-DISPATCH",
    "claimClass": "SCHEMA_COMPATIBILITY",
    "proofClass": "EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST",
    "evidenceRef": "docs/baselines/CVF_GC018_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_2026-09-02.md"
  }],
  "requiredDisposition": "READY_WITH_EXECUTABLE_PROOF",
  "successorScope": "EXECUTABLE_IMPLEMENTATION"
}
```

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator repair instruction | operator message dated 2026-09-02 | ACCEPT |
| actual-seam/ledger design | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | ACCEPT |
| rejected replay findings | `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md` | ACCEPT |
| ratified corrected oracle | `docs/reviews/CVF_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_WORKER_RETURN_2026-09-02.md` | ACCEPT |
| accepted canary boundary | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` | ACCEPT |

## Agent Roles

- Operator: owns authorization and later P4 checkpoint.
- Dispatcher: owns this exact repair contract.
- Worker: edits four paths and returns evidence without commit.
- Reviewer/closer: bounded challenge, disposition and accepted commit.
- Session-sync steward: continuity only after material disposition.

## Scope / Target / Owner Boundary

Allowed writes are exactly the four paths in Required Artifact Manifest.
Read-only inputs include the oracle, its sources, P2 owners, redesign, P4
design, prior R1B evidence, current baseline/work order and checkers.

Forbidden writes include P2 owners, oracle, prior R1B return, standards,
checkers, hooks, catalogs, registries, session state and P4.

## Required First Reads

1. Startup surfaces required by `AGENTS.md`.
2. Guard orientation and governed literal gotchas.
3. Paired R1B-R2 baseline and this work order.
4. R1 redesign; R1A-R2 accepted return/oracle; first R1B adjudication.
5. Existing runner, tests and ledger in full.
6. Both P2 seam owners and applicable checker sources.
7. Accepted P4 design for dependency boundary only.

## Pre-Flight Checks

- Capture clean `executionBaseHead`; confirm dispatch base ancestry.
- Confirm exact current starting hashes below.
- Confirm the new worker-return path is absent.
- Confirm oracle and P2 files are unchanged at pinned identities.
- Run pre-implementation gate against captured execution base.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "MFRP-P3-R1B-R2",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["governance/compat", "governance/compat/fixtures", "docs/reviews", "docs/baselines", "docs/work_orders"],
  "claims": ["bounded actual-seam repair evidence only"],
  "requiredProof": [
    "accepted oracle and P2 identities",
    "seven-source and nineteen-excerpt execution",
    "genuine cited-source drift rejection before seam calls",
    "same-object actual P2 observations",
    "per-case same-domain digests and classification",
    "exact 19/18/7 deterministic ledger and four-path no-commit return"
  ],
  "operatorCheckpoints": ["P2 or oracle change", "fifth path", "P4 opening", "external effect"],
  "forbiddenEffects": ["P2 or oracle mutation", "worker commit", "provider network live public deploy production", "automatic P4 opening"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named source set",
    "completenessClaimChanged": false
  }
}
```

Expected route: `P3_ELEVATED`; shadow route only. Full legacy gates remain.

## Frozen Input Identity Manifest

| Input | Required identity |
|---|---|
| oracle containing commit | `e15cf55d8060a44056f44dd819b399ae3aec1fb0` |
| oracle raw SHA-256 | `c6a8006265ff1968760101e380c779e2a031c870aa7ff3c6d0296df94dbebd43` |
| oracle all-field JCS | `5a6751a7b6cda0291792a476799594dde63bdfa7e13997b8a093f3cecfd8e97d` |
| required-set three-key JCS | `04be6dc1fa061e13af195c5490769bf88fba3309e2ddb4aa0ed24a8fd6440fca` |
| P2 receipt owner | `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` |
| P2 readout owner | `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` |
| R1 redesign | `22a086d7742dbdaec5b887fd377890962ad34396953f48287ce865f743766011` |
| accepted P4 design | `65698a95dc7bb7f437fe061a81559701b91a3e611c445f5122ad8145c5f13df5` |
| R1A-R2 accepted return | `516f35f754e47a24e163f6bced33a9c0cae4c1f78826fd028511de5de0d240c8` |

## Starting Artifact Identity Manifest

| Artifact | Starting SHA-256 |
|---|---|
| `governance/compat/mfrp_actual_seam_replay.py` | `f348483d813dc670da7f15e792f89c57f812074659cc4ebb88e84bce53e78e38` |
| `governance/compat/test_mfrp_actual_seam_replay.py` | `fd5074b63fceb85740cb92db64a59da9159e210cfc9ee29510178fc1c4757ecf` |
| `governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json` | `f293738e675ad2edb075f2900f409d985baf2c64f0707ab8d8995ff94022df0a` |
| rejected R1B return, read-only | `a042f80260042b7f71675edc57a8fb4e33ad5a1c70963c87a471d2123d85df5c` |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | existing compat helper/test/result fixture plus new review return |
| Storage decision | reuse existing directories; no folder, index, registry, cache or hidden store |
| Existing aggregate impact | none |
| Generated state impact | deterministic result fixture only |
| Durable governance boundary | oracle and P2 remain owners; ledger is evidence, not parallel authority |

## Required Artifact Manifest

| Path | Action | Owner |
|---|---|---|
| `governance/compat/mfrp_actual_seam_replay.py` | MODIFY | worker |
| `governance/compat/test_mfrp_actual_seam_replay.py` | MODIFY | worker |
| `governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json` | MODIFY | worker |
| `docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_WORKER_RETURN_2026-09-02.md` | CREATE | worker |

No fifth path, rename or deletion.

## Write Ownership

| Path class | Worker | Reviewer |
|---|---|---|
| runner/test/ledger | implement and self-verify | inspect/rerun/challenge |
| worker return | author candidate | adjudicate/repair allowed return-only defects |
| P2/oracle/P4 | no write | no write in this tranche |

## Work-Order Fulfillment Manifest

| Requirement | Proof |
|---|---|
| frozen identity | recomputed oracle/P2/design/starting hashes |
| source binding | 7 source hashes and 19 range/digest checks before replay |
| hostile causality | cited-source byte drift fails with zero seam calls |
| actual P2 seam | validator and readout see identical receipt object |
| ledger completeness | per-case base/mutated digests, classification and booleans |
| exact coverage | 19/18/7 and representability reconciliation |
| bounded authority | four paths, no commit/provider/P4 effect |

## Actual Source-Binding Execution Contract

Runner must validate source bindings before case replay:

1. recompute all seven `sourceManifest.path` raw hashes;
2. require each case `sourceId` and path equal its manifest row;
3. reject UTF-8 BOM and any recipe other than
   `UTF8_NO_BOM_LF_NORMALIZED_LINE_RANGE_V1`;
4. normalize CRLF/lone CR to LF, use one-based inclusive line range, require
   `includeTrailingLf: false`, and reject invalid/empty/out-of-bounds ranges;
5. require the exact locator occur exactly once inside the selected range;
6. recompute and compare `sourceExcerptSha256`;
7. fail before any call to `_validate_receipt_integrity` or readout owner.

The implementation may expose an internal test-only source-root parameter;
the production CLI must always bind to repository root and must not accept an
override that could substitute clean historical bytes.

## Genuine Cited-Source Drift Hostile Test

Use a temporary directory outside the repository. Copy the required historical
source tree or supply the internal validator with a temporary test root,
change at least one byte inside one cited source, leave oracle/sourceManifest
pins unchanged, and assert:

- validation fails on source hash or excerpt binding;
- seam-call counters remain zero;
- no oracle expected identity is patched;
- repository source bytes remain unchanged.

Also retain unknown source ID, wrong path, missing locator, invalid range,
excerpt drift and oracle hash negative tests.

## Actual P2 Seam Contract

For every representable case, build a canonical valid v3 receipt using actual
P2 owners; prove the base control validates; apply the committed mutation in
memory; prove non-control serialized bytes changed; pass the identical mutated
receipt object to actual validator and readout call chain; store only normalized
secret-safe observations; evaluate the committed predicate. Do not copy/fork,
monkeypatch away, or weaken the production evaluator.

## Receipt Digest And Classification Contract

`baseReceiptDigest` and `mutatedReceiptDigest` are SHA-256 of RFC 8785 JCS bytes
over the complete in-memory receipt payload, excluding no field. They use the
same helper and byte domain. Non-control representable mutations require
inequality; `NO_MUTATION` requires equality.

Each case records `classification`, `falseNegative`, and `falsePositive`:

- valid `NO_MUTATION` control -> `TRUE_NEGATIVE`, both booleans false;
- rejected/missed `NO_MUTATION` control -> `FALSE_POSITIVE`, falsePositive true;
- representable mutation with predicate satisfied -> `TRUE_POSITIVE`, both false;
- representable mutation with predicate missed -> `FALSE_NEGATIVE`, falseNegative true;
- unrepresentable -> `NOT_REPRESENTABLE_BY_CURRENT_P2`, booleans null and
  exclusion from safety denominator.

Unknown or inconsistent classification fails the run. C15 must remain visible
as `FALSE_NEGATIVE` if the sentinel appears. C07/C08/C18 remain unrepresentable
unless actual unchanged P2 fields prove otherwise; the worker cannot redefine
the oracle to improve metrics.

## Result Ledger Contract

Preserve schema `cvf.mfrp.actualSeamReplayResult.v1` unless an additive schema
version is required and fully documented. Per-case records include oracle ID,
oracle identity, source-binding status, base/mutated digests, mutation proof,
validator/readout observation, required/observed predicate, classification,
booleans and limitation. Aggregates separate execution completeness from
safety candidate, reconcile classification counts, exact failed/missing IDs,
per-class numerator/denominator, excluded unrepresentable cases and claim
boundary.

`executionCompleteness: COMPLETE` may coexist with
`safetyCandidate: RETURN_TO_DESIGN_CANDIDATE`. No reviewer token may be emitted.

## Required Hostile Regression Matrix

- one-case corpus, missing family and missing zero-tolerance class fail;
- oracle raw/JCS/required-set identity drift fails;
- actual cited-source byte drift fails before seam call;
- unknown source ID, wrong path, missing/duplicate locator, invalid range,
  excerpt digest drift and BOM fail;
- unknown/unused mutation and no serialized-byte change fail;
- expected-label mutation cannot manufacture observation;
- actual P2 digest tamper reaches and is rejected by validator;
- same-object evidence fails if validator/readout payload identity diverges;
- classification weakening/always-pass evaluator is caught;
- base/mutated digest and classification inconsistency fails;
- C15 sentinel remains visible as a miss; secret-safe scan passes;
- repeated same-base runs are byte-identical and write no cache/provider data.

## Execution Plan

1. Freeze identities and run pre-implementation.
2. Add fail-closed source-binding validation before replay.
3. Add same-domain receipt digests and classification reconciliation.
4. Add/repair hostile tests, including real cited-source drift.
5. Regenerate deterministic ledger from actual P2 seams.
6. Run focused tests twice and compare ledger bytes.
7. Author full worker return, run wrapper gate, reconcile four paths, stop.

## Acceptance Criteria

- Exact four-path changed set and clean starting base.
- Every frozen/starting identity matches before edit.
- Source binding 7/19 PASS before replay; hostile drift rejects with zero calls.
- Both actual P2 seams and identical-object causal evidence are exercised.
- All 19 records carry consistent digest/classification fields.
- 19/18/7, classifications and denominators reconcile exactly.
- Actual misses and unrepresentable cases remain visible.
- Focused suite and two-run deterministic ledger pass.
- Required gates pass; P2/oracle hashes unchanged.
- Zero provider/live/network calls, staging and commit.

## Evidence Requirements

Record execution base, identity hashes, exact changed set, call order,
source-binding totals, hostile source-drift zero-call proof, per-class ledger
totals, every failed predicate, deterministic output hashes, focused/gate
results, unchanged P2/oracle hashes, provider count zero and no-commit status.

## Stop Conditions

Stop on any frozen identity mismatch, need for P2/oracle edit, inability to
validate source binding before seam calls, fifth path, unknown predicate,
classification inconsistency, secret exposure, hidden actual miss, external
call need or non-deterministic ledger.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with complete evidence and a worker
candidate of `REPLAY_EVIDENCE_COMPLETE_ACCEPTANCE_CANDIDATE` or
`REPLAY_EVIDENCE_COMPLETE_RETURN_TO_DESIGN_CANDIDATE`. Otherwise return
`BLOCKED_WITH_REASON`. Never return reviewer acceptance or P4 opening.

## Operator Checkpoint

No further operator input or pre-execution reviewer is required for exact
four-path execution. Routine review occurs at worker return. P2/oracle change,
manifest expansion, P4 execution or external effect requires a new checkpoint.

## Forbidden Actions

Do not modify P2, oracle, old R1B return, standards, checkers, hooks, catalogs,
registries, session or P4; do not create a fifth path; do not weaken evaluator,
hide C15/C07/C08/C18, stage/commit, call provider/network/live, read secrets,
public-sync, deploy, produce or self-accept.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short
git diff --cached --name-status
python -B governance/compat/test_mfrp_actual_seam_replay.py
python -B governance/compat/mfrp_actual_seam_replay.py --help
python governance/compat/run_worker_return_fast_gate.py
```

Use the runner CLI defined by its help to regenerate the exact ledger with the
captured execution base. Run it twice and compare bytes/hashes.

## Evidence Reuse And Encoding Plan

| Evidence | Mode | Encoding |
|---|---|---|
| accepted oracle/P2/design | RECOMPUTE_REQUIRED | raw SHA-256 plus RFC 8785 JCS where specified |
| starting runner/test/ledger | RECOMPUTE_REQUIRED | raw SHA-256 |
| first R1B findings | REUSE_PRIOR_VERIFICATION | committed UTF-8 reviewer evidence |
| repaired outputs | REVIEWER_RECOMPUTE_ONLY | UTF-8 Python/JSON/Markdown |

Provider-specific memory is `NOT_CVF_SOURCE`; no source-verification or
authority row cites it.

## Negative Search And Collision Discipline

The new baseline/work order/worker-return names were absent before authoring.
The three existing implementation artifacts are the explicit repair targets;
the old R1B worker return is immutable evidence, not a collision.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| source/ledger contract | governed design | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | Source And Locator Binding; Result Ledger Contract; Mandatory Hostile Tests | R1B replay | R1 redesign | ACCEPT |
| repair findings | adjudicated evidence | `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md` | Independent Reviewer Adjudication | R1B-RV-1 through R1B-RV-3 | reviewer disposition | ACCEPT |
| accepted source-bound oracle | accepted evidence | `docs/reviews/CVF_MFRP_P3_R1A_R2_ORACLE_SOURCE_BINDING_CORRECTION_WORKER_RETURN_2026-09-02.md` | Independent Reviewer Adjudication | `ORACLE_RATIFIED_BOUNDED` | R1A-R2 oracle | ACCEPT |
| actual validator owner | executable source | `governance/compat/agent_autorun_machine_verification.py` | receipt object/digest/validator symbols | `_validate_receipt_integrity` | P2 receipt owner | ACCEPT |
| actual readout owner | executable source | `governance/compat/agent_automation_machine_verification_readout.py` | builder/serializer symbols | `build_machine_verification_readout`; `machine_readout_to_dict` | P2 readout owner | ACCEPT |
| P4 opening remains conditional | accepted design | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md` | Dependency And Opening Rule | accepted R1B prerequisite | P4 design | ACCEPT |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: bounded repair over fixed named artifacts; no
legacy corpus absorption or complete-scan claim.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | prior critique/review evidence -> CVF adjudication -> local repair contract |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R1 redesign, accepted R1A-R2 oracle and this work order |
| Disposition | NO_NEW_ABSORPTION |
| Claim boundary | local repair only; external statement is not runtime truth |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`actual seam replay repair`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

Disclosed defectIds: NONE

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch/no-commit fields, review admission, Source Verification columns, protected paths, full worker-return profile |
| gateRunPurpose | confirm the already-authored packet and collect pre-dispatch evidence |
| claimBoundary | gate PASS proves shape, not replay correctness, acceptance or P4 readiness |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3-R1B-R2 --title "Actual-Seam Replay Repair" --date 2026-09-02 --base 5cf4d663b7b0f25e2faff24c12d1a0d8b363df05 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id mfrp-p3-r1b-replay-evidence --prior-finding-set-digest a042f80260042b7f71675edc57a8fb4e33ad5a1c70963c87a471d2123d85df5c --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence R1B_RV_1_R1B_RV_2_R1B_RV_3 --scec-problem-key mfrp-p3-r1b-r2-repair --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | protected-governance-path internal no-commit rework |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact repair findings, frozen identities, four paths, hostile source drift, digest/classification and P4 boundary |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | baseReceiptDigest, mutatedReceiptDigest, classification, falseNegative, falsePositive |
| claimBoundary | provenance only; no replay outcome predeclared |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify the exact existing R1B
runner/test/result fixture and create the named R1B-R2 return. No P2, oracle,
checker, hook, standard, catalog, registry or session surface may change.

Protected paths:

- `governance/compat/mfrp_actual_seam_replay.py`
- `governance/compat/test_mfrp_actual_seam_replay.py`
- `governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json`

Operator authorization: explicit 2026-09-02 R1B repair after accepted R1A-R2.

Rollback boundary: restore three existing artifacts to Starting Artifact
Identity Manifest and remove only the new uncommitted worker return.

## Commit Mode And Base-Anchor Lifecycle

dispatchBaseHead: `5cf4d663b7b0f25e2faff24c12d1a0d8b363df05`

executionBaseHead: worker captures clean descendant at start.

closureBaseHead: reviewer captures after accepted material commit.

Worker commit is forbidden; reviewer/closer owns material and continuity.

## Single-Agent Multi-Role Control Block

Route is MULTI_AGENT_MULTI_ROLE. If one runtime performs multiple named roles,
authority still does not transfer.

| Control | Binding |
|---|---|
| role separation ledger | operator authorizes; dispatcher scopes; worker repairs; reviewer evaluates/commits |
| self-review boundary | worker checks are not independent acceptance |
| escalation conditions | P2/oracle need, fifth path, secret risk or unexplained divergence |
| gate sequence | pre-dispatch -> pre-implementation -> focused suite -> worker-return gate -> reviewer/closure |

## Dual Agent Surface Matrix

| Surface | Status | Authority boundary |
|---|---|---|
| INTERNAL_AGENT | AUTHORIZED | exact four-path local no-commit worker |
| EXTERNAL_AGENT_CLI_MCP | FORBIDDEN | zero external invocation/quota |
| adapter boundary | NOT_APPLICABLE_WITH_REASON | actual local P2 imports only; no adapter |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator -> dispatcher -> bounded no-commit repair worker -> reviewer/closer |
| phase | R1B-R2 replay repair pending worker evidence |
| baseHeadFor(phase) | dispatchBaseHead=`5cf4d663b7b0f25e2faff24c12d1a0d8b363df05`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exactly three modified compat artifacts plus one new return |
| traceScope(phase, actor) | identities, source bindings, seam calls, digests/classifications, tests, gates and no-commit evidence |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no P2, oracle, old return, checker, standard, session or P4 change; clean worktree required at start |
| Before status evidence | clean worktree at captured execution base; `git status --short` empty |
| nextMoveSurfaces | reviewer adjudicates R1B-R2; P4 remains separately conditional |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MFRP_P3_R1B_R2_ACTUAL_SEAM_REPLAY_REPAIR_COMPLETION_2026-09-02.md`

reviewerOwnedClosurePaths: exact four worker outputs, conventional completion
review when needed, and separate post-material continuity surfaces.

closureOwner: reviewer/closer.

workerCommitPermission: FORBIDDEN.

Reviewer recomputes identities, reruns focused suite/ledger, drifts one actual
source byte through the test root, challenges one classification and one
owner-observed field, then accepts or returns. Reviewer does not rewrite the
runner. Acceptance still does not automatically run P4.

## Worker Output Checker Read-Ahead Mandate

Read all return-shape checkers before writing the return. Use the wrapper gate;
individual checker substitution is forbidden.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Return must include full required headings, exact work-order binding, execution
base, changed files, command evidence, Core Guard authorization, checker
read-ahead, operation trace, Delta boundary, convergence proof, conditional
controls, public disposition, no-commit status and claim boundary.

## Review Gate

Routine review occurs once at worker return. Reviewer checks machine evidence
and bounded hostile probes, not every implementation step. No P4 review/run is
part of this gate.

## Closure Checklist

- [ ] clean base and exact four paths;
- [ ] frozen/starting hashes match;
- [ ] 7/19 source binding and cited-source drift zero-call test pass;
- [ ] actual P2 same-object call chain passes;
- [ ] all case digests/classifications reconcile;
- [ ] 19/18/7, misses and unrepresentable exclusions remain visible;
- [ ] deterministic ledger/focused/worker-return gates pass;
- [ ] P2/oracle unchanged; zero provider calls; no worker commit;
- [ ] `successorTrancheOpened: NO` exact.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/author |
| Provider or surface | local private provenance repository |
| Session or invocation | MFRP-P3-R1B-R2 dispatch authoring |
| Working directory | repository root |
| Command or tool surface | source reads, hashes, apply_patch and governance gates |
| Target paths | paired R1B-R2 baseline and work order |
| Allowed scope source | operator repair instruction and accepted R1A-R2 identity |
| Before status evidence | clean worktree at `5cf4d663b7b0f25e2faff24c12d1a0d8b363df05`; `git status --short` empty |
| After status evidence | exactly two untracked dispatch artifacts |
| Diff evidence | status and unstaged/staged name-status |
| Approval boundary | dispatch authoring only; no worker execution/result |
| Claim boundary | no R1B-R2 result, P4 or external effect |
| Agent type | dispatcher/author |
| Invocation ID | `mfrp-p3-r1b-r2-dispatch-authoring-2026-09-02` |
| Expected manifest | paired R1B-R2 baseline and work order |
| Actual changed set | paired R1B-R2 baseline and work order |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | R1B-R2 dispatch authority only |
| claimDisposition | CLAIM_REJECTED: no replay result, acceptance or P4 readiness claimed |
| receiptEvidence | N/A with reason: dispatch authoring constructs no receipt |
| actionEvidence | N/A with reason: worker repair has not executed |
| invocationBoundary | local authoring and gates only |
| interceptionBoundary | no runtime route or lifecycle activation |
| claimLanguage | dispatch-ready bounded repair |
| forbiddenExpansion | no P2/oracle, P4, provider/live/public/deploy/production effect |

## Claim Boundary

This work order authorizes exactly one no-commit four-path R1B-R2 repair. It
does not accept replay results, modify P2/oracle, open/run P4, change route
authority, or claim safety, latency, quota, provider/live, public, deployment
or production improvement.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair dispatch; public sync is forbidden.
