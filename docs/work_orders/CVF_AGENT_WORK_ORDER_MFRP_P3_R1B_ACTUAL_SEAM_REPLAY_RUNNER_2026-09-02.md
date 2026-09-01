# CVF Agent Work Order - MFRP P3-R1B Actual-Seam Replay Runner

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-02

Batch ID: MFRP-P3-R1B

Dispatch base head: `bfea86038a888e3b7715dff9df33bb4c0c5c971a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

providerExecutionAuthority: FORBIDDEN

Worker: delegated implementation worker

Reviewer/closer: independent reviewer appointed by Operator

Worker return path: `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md`

## Dispatch Prompt Envelope

Role: delegated implementation worker for MFRP-P3-R1B.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_RUNNER_2026-09-02.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: worker must capture full `git rev-parse HEAD` before edits.

Current-time notes: artifact and authority checkpoint are dated 2026-09-02.

Do-not-misread notes: this corrected packet is dispatch-ready after machine
gates; it authorizes only R1B's four paths, not P2/oracle changes,
reviewer disposition, P4 authoring/execution, provider/live/public work, or an
assertion that phase returns and receipts are the same object.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, this packet, its paired baseline, R1 redesign, committed oracle, both
P2 seam owners, and checker sources listed below; verify every pinned hash and
clean execution base before writing.

Return contract: create all four exact-manifest artifacts, run required gates,
leave changes uncommitted, and return `COMPLETE_PENDING_REVIEW` carrying one
R1B worker terminal candidate, or `BLOCKED_WITH_REASON`.

## Purpose

Implement a deterministic, local-only R1B runner that executes the committed
R1A oracle through the actual P2 receipt validator/readout seam and emits a
secret-safe result ledger for bounded independent review.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "MFRP-P3-R1B",
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
  "pathFamilies": ["governance/compat", "governance/compat/fixtures", "docs/reviews", "docs/baselines", "docs/work_orders", "docs/reference/review_cost_control", "CVF_SESSION", "CVF_SESSION_MEMORY.md", "AGENT_HANDOFF_V59_2026-08-11.md"],
  "claims": ["actual P2 seam replay can produce bounded deterministic evidence without changing P2 or the oracle"],
  "requiredProof": ["frozen input hashes", "actual owner imports and causal observations", "19/18/7 coverage reconciliation", "hostile focused tests", "deterministic secret-safe ledger", "no-commit worker return"],
  "operatorCheckpoints": ["worker return", "new authority boundary", "P2 or oracle change need", "P4 opening"],
  "forbiddenEffects": ["worker commit", "P2 mutation", "oracle mutation", "provider call", "network call", "secret read", "public sync", "deploy", "production", "automatic successor"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

Selected role route: dispatcher authors; a delegated worker implements; a
separate reviewer evaluates/commits. Roles are responsibility labels, while
SOT identities and evidence remain authoritative.

Task classification and risk sensitivity: local protected-governance Python,
test, fixture, and review evidence implementation. Risk is high enough to
require frozen owner bytes, exact-manifest isolation, no-commit execution, and
independent closure; provider/live/public/destructive scope is forbidden.

Intake summary: the Operator opened R1B authoring after R1A oracle ratification
and bounded canary-design acceptance. This packet converts that authority into
a four-path replay assignment without opening execution or P4.

Escalation condition: stop on identity mismatch, protected existing-source
write need, secret risk, coverage contradiction, or manifest expansion.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP-P3-R1B
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: INITIAL_DISPATCH
rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-p3-r1a-oracle",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 3,
  "predecessor": {
    "path": "docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md",
    "sha256": "32dabae39e0a4465b5e3a7ad4ba10e4cdf1aa7be7c20c1f6f8ba21f0ad87dee6"
  },
  "blockerDelta": {"prior": ["r1a-oracle-not-yet-ratified"], "resolved": ["r1a-oracle-not-yet-ratified"], "retained": [], "new": [], "reopened": [], "current": []},
  "resolutionEvidence": {
    "r1a-oracle-not-yet-ratified": {
      "evidenceClass": "ACCEPTED_REVIEW",
      "evidencePath": "docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md",
      "sha256": "32dabae39e0a4465b5e3a7ad4ba10e4cdf1aa7be7c20c1f6f8ba21f0ad87dee6",
      "locator": "terminalReadinessVerdict: READY_FOR_REVIEW"
    }
  },
  "counters": {"partialReadyClosures": 0, "reviewerScopeExpansions": 0, "sameClaimCorrections": 1, "nonDecreasingBlockerTransitions": 0},
  "claims": [{"claimId": "MFRP-P3-R1B-ACTUAL-SEAM-DISPATCH", "claimClass": "SCHEMA_COMPATIBILITY", "proofClass": "EXECUTABLE_BUILDER_VALIDATOR_CONTRACT_TEST", "evidenceRef": "governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json"}],
  "requiredDisposition": "READY_WITH_EXECUTABLE_PROOF",
  "successorScope": "EXECUTABLE_IMPLEMENTATION"
}
```

## Authority Chain

1. `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md`.
2. `docs/baselines/CVF_GC018_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_RUNNER_2026-09-02.md`, SHA-256 `0a4ebb9ee49a75ca31c71dc6eb4c085dac7aadb4b8685181d09a2688889da51c`.
3. This corrected work order after machine-gate confirmation and material commit.
4. The committed R1A oracle and actual P2 owner bytes.

If these sources conflict, stop. Do not infer an expanded permission.

## Agent Roles

| Role | Responsibility | Forbidden substitution |
| --- | --- | --- |
| dispatcher | authors bounded authority/evidence contract | does not implement R1B in this tranche |
| worker | implements exact four-path manifest and self-verifies | cannot accept own result or commit |
| independent reviewer/closer | bounded inspection, recomputation, disposition, commit if accepted | does not recreate worker implementation |
| Operator | opens execution and later P4 checkpoint | no implicit delegation from machine output |

## Scope / Target / Owner Boundary

Allowed implementation scope is exactly:

- `governance/compat/mfrp_actual_seam_replay.py`;
- `governance/compat/test_mfrp_actual_seam_replay.py`;
- `governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json`; and
- `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md`.

Read-only inputs include the R1 redesign, paired baseline, committed R1A
oracle, both P2 seam owners, and applicable checkers. Any other write is
forbidden.

## Required First Reads

Read the session startup surfaces required by `AGENTS.md`, guard orientation,
literal-format gotchas, this work order, paired baseline, R1 redesign, R1A
oracle/worker return, both P2 seam source files, accepted canary Revision 1,
its independent acceptance, and every checker named in the read-ahead block.

## Pre-Flight Checks

1. Capture full `executionBaseHead` and clean `git status --short`.
2. Confirm the dispatch base is an ancestor of the execution base.
3. Recompute every identity in the frozen table below.
4. Confirm all four output paths are absent and no unrelated changes exist.
5. Confirm this work order status is `DISPATCH_READY`; no separate packet
   review or operator micro-checkpoint is required.

## Task Governance Routing Manifest

| Surface | Role | Authority | Write permission | Evidence returned |
| --- | --- | --- | --- | --- |
| INTERNAL_AGENT | worker | this accepted work order | exact four paths only | code, tests, ledger, return |
| EXTERNAL_AGENT_CLI_MCP | not used | none | none | zero invocations |
| adapter boundary | local Python imports/calls only | actual P2 source owners | no provider/network adapter | call-chain observations |

The route is `MULTI_AGENT_MULTI_ROLE`; role naming does not establish truth.
The SOT plane, frozen identities, observations, and independent disposition do.

## Frozen Input Identity Manifest

| Input | Required identity |
| --- | --- |
| R1A oracle containing commit | `7f607d353bdec11e456731793f181e72abddc297` |
| R1A oracle file SHA-256 | `6aa32c3157092c974441c269d17e85aed20d5ba535479523eda5b64d23b3fbf2` |
| R1A oracle all-field JCS SHA-256 | `8d64ed3414959ca281cc47daf7067047d79776819b44df16c81dff7a6cbfa80c` |
| required-set JCS digest | `04be6dc1fa061e13af195c5490769bf88fba3309e2ddb4aa0ed24a8fd6440fca`; SHA-256 of UTF-8 RFC 8785 JCS bytes for exactly `{requiredCaseIds, requiredFamilies, requiredZeroToleranceClasses}`, with all three arrays copied unchanged from the oracle |
| P2 receipt owner SHA-256 | `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` |
| P2 readout owner SHA-256 | `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` |
| R1 redesign SHA-256 | `22a086d7742dbdaec5b887fd377890962ad34396953f48287ce865f743766011` |
| accepted canary Revision 1 SHA-256 | `65698a95dc7bb7f437fe061a81559701b91a3e611c445f5122ad8145c5f13df5` |

All identities are recomputed, never trusted from prose.

## Required Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `governance/compat/mfrp_actual_seam_replay.py` | create local deterministic actual-seam runner |
| `governance/compat/test_mfrp_actual_seam_replay.py` | create focused hostile regression suite |
| `governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json` | create schema `cvf.mfrp.actualSeamReplayResult.v1` deterministic result ledger |
| `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md` | create full-gate worker evidence return |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation path class | executable helper/test and deterministic fixture under existing `governance/compat/`, plus return under existing `docs/reviews/` |
| Storage decision | reuse existing directories; create no folder, index, registry, front door, cache, or hidden store |
| Existing aggregate impact | none; no aggregate or catalog update authorized |
| Generated state impact | one checked-in deterministic result fixture candidate only |
| Durable governance boundary | oracle and P2 remain owners; the result ledger is replay evidence, not a parallel authority |

## Work-Order Fulfillment Manifest

| Requirement | Owning section | Required worker evidence |
| --- | --- | --- |
| exact four-path scope | Required Artifact Manifest; Core Guard authorization | before/final status and manifest reconciliation |
| frozen identity | Frozen Input Identity Manifest | independently recomputed hashes |
| actual seam | Actual P2 Seam Contract | imports, causal observations, hostile tests |
| exact coverage | Coverage And Reconciliation Contract | 19/18/7 counts and no missing/extra values |
| bounded authority | Result Ledger Contract; Review Gate | worker candidate separate from reviewer disposition |
| no forbidden effects | Forbidden Actions; Claim Boundary | zero provider/network/live/cache writes and unchanged protected bytes |

## Actual P2 Seam Contract

For every admitted representable case the runner must create a valid,
deterministic `cvf.autorun.pass-receipt.v3` control through canonical P2
object/digest behavior; prove that control is accepted by the actual
`_validate_receipt_integrity`; apply the committed typed mutation in memory;
invoke that actual validator on the mutation; invoke
`build_machine_verification_readout` and `machine_readout_to_dict` on the exact
observation; and retain only normalized, secret-safe output fields.

Both actual P2 modules must be imported. The validator and readout must observe
the identical in-memory receipt object within one causal call chain. Mutation
tests must prove serialized bytes changed where the oracle requires a changed
payload. A copy/fork, static allowlist, normative-label result, monkeypatched
replacement of the owner seam, or evaluator that can be weakened without a
test failure is prohibited.

This proves receipt-local observation identity only. It does not bind a
seven-phase return object to an autorun receipt and does not convert agreement
or consistency into correctness.

## Coverage And Reconciliation Contract

The runner must require exactly 19 unique IDs, 18 families, seven
zero-tolerance classes, and 19 cases from the committed oracle. Each mutation
is consumed; each admitted representable case produces exactly one validator
and readout observation. Missing, duplicate, unknown, extra, or zero execution
fails closed.

`C07`, `C08`, and `C18` remain visible as
`NOT_REPRESENTABLE_BY_CURRENT_P2`. They never count as detected, satisfied,
passed, or machine-covered. Their presence is a limitation, not a runner
failure and not permission to change P2.

## Result Ledger Contract

The deterministic JSON ledger uses schema
`cvf.mfrp.actualSeamReplayResult.v1` and separates:

- frozen source identities and recomputation disposition;
- exact coverage reconciliation;
- per-case execution completeness and secret-safe observations;
- committed predicate evaluation;
- limitations and the three non-representable cases;
- one worker terminal candidate; and
- an explicit reviewer-owned disposition placeholder that cannot contain
  `REPLAY_PASS` or `RETURN_TO_DESIGN`.

Execution-base identity may be recorded and is part of deterministic output.
Byte-identical replay comparison is therefore scoped to repeated runs at the
same execution base and identical frozen inputs. Duration, wall-clock time,
machine-specific paths, random values, real secrets, credentials, environment
dumps, and provider data are forbidden ledger fields.

## Required Hostile Test Manifest

Tests must prove all of the following independently:

1. one-case execution cannot pass;
2. missing required family fails;
3. missing zero-tolerance class fails;
4. source locator or excerpt drift fails;
5. oracle identity drift fails;
6. unknown mutation fails;
7. normative labels cannot manufacture an observed result;
8. digest tamper reaches the actual validator;
9. fully rebound attacker case remains the disclosed structural gap;
10. no real credential or environment secret appears in ledger/readout output;
    C15's fixed non-secret test sentinel remains observable, is recorded as a
    failed `SECRET_SENTINEL_NOT_EMITTED` predicate and disclosed P2 limitation,
    and is neither suppressed nor treated as a real credential;
11. the real readout preserves required normalized observation fields;
12. zero totals fail;
13. the runner cannot emit reviewer `REPLAY_PASS` or `RETURN_TO_DESIGN`;
14. both P2 owner files are byte-identical before and after;
15. repeated runs at the same execution base and identical frozen inputs
    produce byte-identical ledger output and no receipt/cache/provider/network
    write; and
16. weakening a local predicate/evaluator causes a test failure.

## Worker Autonomy / No-Question Rule

Choose implementation structure and internal algorithm freely within these
authority, identity, evidence, output, and stop constraints. Repair allowed
scope test/checker failures directly. Return only for a source contradiction,
frozen identity mismatch, forbidden-scope need, secret risk, or missing
authority. CVF does not control the worker's detailed reasoning.

## Write Ownership

The worker owns only the four new paths in the Required Artifact Manifest and
must leave them unstaged and uncommitted. Existing oracle/P2/checker/governance
surfaces are read-only. The independent reviewer owns evidence repair needed
for closure and the material commit after acceptance; the Operator owns any
later execution or successor checkpoint.

## Execution Plan

1. Perform pre-flight and freeze input bytes.
2. Implement runner and focused tests within exact scope.
3. Execute the complete replay once, preserve the deterministic ledger, and
   distinguish runner defects from oracle/P2 limitations.
4. Run focused tests and governed gates.
5. Write worker return with exact changed-set/no-commit evidence.

If the first complete replay exposes a runner-only defect, repair the runner
within scope and record that correction in the return. Never change normative
oracle expectations or P2 to obtain a pass-shaped result.

## Acceptance Criteria

- Exact four-path changed set; no rename/deletion/stage/commit.
- All frozen identities match and are present in the ledger.
- Actual P2 imports and receipt-local identical-object evidence are inspectable.
- Coverage totals reconcile and every mutation is consumed.
- All hostile tests pass without provider/network/live access.
- Ledger is deterministic, secret-safe, and emits one allowed worker candidate.
- Worker return passes the full worker-return fast gate.
- No P4, latency/quota improvement, safety, correctness, authority, deployment,
  or production claim is made.

## Evidence Requirements

Return exact commands and outputs for identity recomputation, focused tests,
two-run ledger byte comparison, P2 before/after hashes, forbidden-write scan,
autorun pre-implementation gate, worker-return fast gate, `git status --short`,
`git diff --name-status`, cached diff, and unchanged HEAD.

## Stop Conditions

Stop with `BLOCKED_WITH_REASON` and worker candidate
`BLOCKED_EVIDENCE_INCOMPLETE` if any pinned input mismatches; output path
exists unexpectedly; changed set expands; P2/oracle modification is needed;
the actual seam cannot be invoked honestly; coverage cannot reconcile; output
may leak a real credential or environment secret; tests require
provider/network/live access; or a checker
demands a forbidden fifth path.

## Return-To-Orchestrator Conditions

Return immediately on a stop condition. Otherwise return
`COMPLETE_PENDING_REVIEW` with exactly one of
`REPLAY_EVIDENCE_COMPLETE_PASS_CANDIDATE` or
`REPLAY_EVIDENCE_COMPLETE_RETURN_TO_DESIGN_CANDIDATE`. Do not self-select
`REPLAY_PASS`, `RETURN_TO_DESIGN`, P4 readiness, or closure.

Current source evidence predicts
`REPLAY_EVIDENCE_COMPLETE_RETURN_TO_DESIGN_CANDIDATE`: C07, C08 and C18 are
not representable by current P2, while C15 is expected to record an honest
predicate miss. Producing that complete, source-faithful candidate is a
successful R1B execution outcome, not a worker failure and not a reason to
alter the oracle or suppress observations.

## Operator Checkpoint

No further pre-execution packet review or separate Operator micro-checkpoint is
required. The Operator may dispatch this committed work order. After worker
return, independent review and Operator direction are required before closure
or any P4 move.

## Review Admission Boundary

Reviewer admission is trigger-based, not step-based. The completed Claude
packet review supplied the correction set used here but does not establish a
mandatory review stage for future work orders. Routine review next occurs on
the R1B worker return. Pre-return review is allowed only for a frozen-identity
mismatch, source contradiction, manifest expansion, secret or irreversible
effect risk, or a new independent critical authority boundary. Authoring,
role handoff, machine-gate success, commit, and continuity sync do not by
themselves trigger review. The reviewer evaluates evidence and does not repeat
implementation.

## Forbidden Actions

- modify oracle, P2 owners, roadmap, design, standards, checkers, hooks,
  catalogs, registries, session state, or handoff;
- create a fifth output or Python cache;
- stage, commit, push, delete, rename, or rewrite history;
- call provider, network, live, credential, public-sync, deployment, or
  production surfaces;
- hide `UNCLASSIFIED` or non-representable cases;
- replace actual P2 behavior with a copied/local evaluator;
- make reviewer decisions or open R1B successors/P4.

## Verification Commands

```powershell
python -B governance/compat/test_mfrp_actual_seam_replay.py
python -B governance/compat/mfrp_actual_seam_replay.py --oracle governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json --output governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
git diff --name-status
git diff --cached --name-status
git rev-parse HEAD
```

Equivalent focused CLI flags may differ if documented in the return; the
observable contracts and exact paths may not.

## Evidence Reuse And Encoding Plan

| Field | Value |
| --- | --- |
| mode | RECOMPUTE_REQUIRED |
| recomputeReason | R1B must bind current committed oracle and actual P2 bytes at execution time |
| priorVerificationArtifact | `docs/reviews/CVF_MFRP_P3_R1A_R1_STATIC_ONLY_ORACLE_CORRECTION_WORKER_RETURN_2026-09-02.md` |
| priorVerificationAnchor | SHA-256 `32dabae39e0a4465b5e3a7ad4ba10e4cdf1aa7be7c20c1f6f8ba21f0ad87dee6` |
| freshRecomputeRequired | YES |
| unicodePathHandling | literal repository-relative paths and explicit UTF-8 readers; no shell-derived lossy conversion |
| claimBoundary | identity and encoding evidence only; no semantic acceptance |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| paired authoring paths | absent before authoring | CREATE_NEW |
| R1B token search | only roadmap and R1 redesign existed | NO_COLLISION |
| four worker outputs | absent before authoring | CREATE_NEW_ONLY |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R1B contract and reviewer exits | normative | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | MFRP-P3-R1B; Runtime Coverage; Reviewer | R1B | `cvf.mfrp.actualSeamReplayResult.v1` | ACCEPT |
| receipt schema and validator | source | `governance/compat/agent_autorun_machine_verification.py` | lines 17-19, 131 onward | `_validate_receipt_integrity` | `cvf.autorun.pass-receipt.v3` | ACCEPT |
| readout builder and serializer | source | `governance/compat/agent_automation_machine_verification_readout.py` | lines 63, 125 | `build_machine_verification_readout`; `machine_readout_to_dict` | P2 readout seam | ACCEPT |
| exact oracle sets and limitations | committed evidence | `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | required sets; C07/C08/C18 | `feasibilityDisposition` | R1A oracle | ACCEPT |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this is an implementation dispatch over already
ratified local authority, not legacy corpus absorption.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | preserved critique -> CVF local design revision -> independent acceptance -> bounded R1B authoring |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` plus frozen local hashes |
| Owner surface | R1 redesign and accepted canary design |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no provider fact or external critique is treated as canonical authority |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`actual-seam replay runner`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "actual-seam replay runner" --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no matching ADIF item changed this packet |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py` and split modules; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | headings Dispatch Prompt Envelope, Required Artifact Manifest, Worker Return Packet Shape Contract, Agent Operation Trace Block, Delta Execution Claim Boundary Control Block, Public Export Disposition; fields executionBaseHead, changedSetScope(phase), manifest delta; enums WORKER_MUST_NOT_COMMIT, COMPLETE_PENDING_REVIEW, DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmed exact checker-facing shape before final authoring; post-authoring gates provide confirmation evidence. |
| claimBoundary | This is read-ahead evidence for packet/output shape only; it does not prove future worker compliance. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3-R1B --title "Actual-Seam Replay Runner" --date 2026-09-02 --base bfea86038a888e3b7715dff9df33bb4c0c5c971a --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added frozen authorities, exact four-path manifest, actual-seam/coverage/ledger contracts, hostile tests, stop conditions, and reviewer boundary. |
| checkerReadAheadConfirmation | Checker sources listed above were inspected before final authoring. |
| docOnlyNewFields | R1B terminal candidate and actual-seam evidence labels remain documentation contracts until execution. |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Core Guard Self-Protection Authorization

| Field | Value |
| --- | --- |
| allowedImplementationPaths | `governance/compat/mfrp_actual_seam_replay.py`; `governance/compat/test_mfrp_actual_seam_replay.py`; `governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json` |
| allowedReviewPath | `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md` |
| forbiddenProtectedPaths | For the R1B worker: all existing checkers, hooks, catalogs, standards, P2 owners, oracle, roadmap, designs, registries, session and handoff surfaces. The dispatcher-only review-admission enforcement amendment below precedes R1B execution and is not part of the worker manifest. |
| operatorApprovalBoundary | Operator explicitly authorized completing machine enforcement first and then returning directly to R1B; no additional packet review or operator micro-checkpoint. |
| stopAndReturn | any protected-path need outside allowed new paths |

Dispatcher-only machine-enforcement protected paths:

- `governance/compat/check_review_cost_control.py`
- `governance/compat/test_check_review_cost_control.py`
- `governance/compat/review_convergence_scaffold.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher authors; delegated worker implements; independent reviewer evaluates/closes |
| phase | R1B implementation ready for Operator dispatch |
| baseHeadFor(phase) | dispatchBaseHead=bfea86038a888e3b7715dff9df33bb4c0c5c971a; executionBaseHead=worker captures full HEAD at start; closureBaseHead=reviewer sets |
| changedSetScope(phase) | worker exact four-path manifest; reviewer closure paths separately declared |
| traceScope(phase, actor) | worker records commands, outputs, identities, changed set and no-commit evidence; reviewer records bounded recomputation |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer only after acceptance |
| crossBatchIsolation | no unrelated changes admitted; stop on dirty base or manifest expansion |
| nextMoveSurfaces | worker return to reviewer; reviewer disposition to Operator; no automatic P4 move |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_COMPLETION_2026-09-02.md` optional only if worker return cannot carry repaired closure evidence |
| reviewerOwnedClosurePaths | worker return repair if needed; optional exact completion review; continuity surfaces only after accepted material commit |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing each output, read checker source for its path and content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| Python runner/test/fixture | source-protection, determinism, secret-safe output, exact-manifest and test expectations derived before writing |
| worker return under `docs/reviews/` | exact review headings, worker-return terms, trace/delta labels, public disposition, conditional N/A blocks and no-commit evidence derived before writing |

Do not spell required headings as fake heading literals before their real
section. Do not use closure language before reviewer acceptance.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; Command Evidence; No-Commit Statement.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. Use `N/A with reason` for every non-applicable block.

## Review Gate

Reviewer verifies, without rebuilding the implementation: input hashes;
actual P2 imports/call chain; receipt-local identical-object observation;
19/18/7 reconciliation; C07/C08/C18 non-detection; selected hostile tests;
deterministic ledger recomputation; exact changed set; no forbidden writes;
and worker inability to emit reviewer outcomes.

Reviewer alone selects `REPLAY_PASS`, `RETURN_TO_DESIGN`, or a blocked review
disposition. Agreement is consistency evidence, not correctness evidence.

## Closure Checklist

- Corrected dispatch-ready packet and machine gates preceded worker execution;
  no redundant packet re-review was inserted.
- Exact four-path worker manifest and unchanged P2/oracle bytes.
- All identities and totals independently recomputed.
- Worker candidate is allowed and reviewer disposition is separate.
- Review cost stayed bounded; no duplicated semantic implementation.
- Nothing staged/committed by worker.
- P4 remains closed unless Operator separately opens it after closure.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | primary dispatcher/author |
| Provider or surface | local Codex workspace; no provider call |
| Session or invocation | MFRP-P3-R1B authoring, 2026-09-02 |
| Working directory | repository root |
| Command or tool surface | read-only PowerShell/Python checks and apply_patch authoring |
| Target paths | paired baseline and work order only |
| Allowed scope source | Operator instruction opening R1B authoring, plus R1 redesign and accepted canary boundary |
| Before status evidence | clean worktree; `git status --short` was empty at clean HEAD `bfea86038a888e3b7715dff9df33bb4c0c5c971a`; both authoring paths absent |
| After status evidence | to be confirmed by authoring gates and exact two-path status |
| Diff evidence | `git diff --name-status` |
| Approval boundary | corrected authoring may be dispatched; R1B result acceptance and P4 remain reviewer/Operator checkpoints |
| Claim boundary | packet design, not R1B execution or replay result |
| Agent type | dispatcher/author |
| Invocation ID | `mfrp-p3-r1b-authoring-2026-09-02` |
| Expected manifest | paired baseline plus this work order |
| Actual changed set | paired baseline plus this work order, subject to gate confirmation |
| Manifest delta | expected NONE |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | authoring of a future bounded R1B implementation contract |
| claimDisposition | CLAIM_REJECTED: no R1B execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: authoring creates or consumes no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no replay runner action has executed under this packet |
| invocationBoundary | local authoring and static verification only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | corrected dispatch-ready work order; no execution result claimed |
| forbiddenExpansion | no provider/live/public/package/Web/MCP/model-router/P4 behavior without fresh authorization |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | NO |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | NOT_APPLICABLE_WITH_REASON |
| reason | This packet authors a local replay helper contract and makes no claim about current provider registry absence, provider capability behavior, or live runtime readiness. The existing `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and `PROVIDER_CAPABILITY_REGISTRY` are outside scope and not inspected as replay evidence. |
| requiredFutureAction | Any future provider/live/runtime claim requires a separately authorized live-proof tranche and current registry evidence. |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap/R1 requirement | Work-order control |
| --- | --- |
| actual P2 seam, not copied evaluator | Actual P2 Seam Contract and hostile tests |
| committed oracle identities | Frozen Input Identity Manifest |
| exact 19/18/7 coverage | Coverage And Reconciliation Contract |
| non-representable cases visible | C07/C08/C18 limitation rule |
| post-run ledger separates evidence from authority | Result Ledger Contract and reviewer-only outcomes |
| governance tax bounded | reviewer gate uses selective independent recomputation, not implementation replay |

## Claim Boundary

This corrected artifact is an R1B dispatch-ready work order permitting only
the exact four-path, local deterministic, no-commit worker tranche. It does not
itself execute or accept
R1B, alter P2/oracle, establish correctness/safety/latency/quota improvement,
authorize reviewer outcomes, open P4, or make runtime/provider/live/public/
deployment/production claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance work-order authoring; no public-sync
artifact, remote, commit, or catalog update is authorized.
