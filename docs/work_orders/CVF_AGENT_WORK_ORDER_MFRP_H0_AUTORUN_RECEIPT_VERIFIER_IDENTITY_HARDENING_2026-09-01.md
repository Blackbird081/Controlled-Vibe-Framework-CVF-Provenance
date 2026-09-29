# CVF Agent Work Order - MFRP-H0 Autorun Receipt Verifier Identity Hardening

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: MFRP-H0

Dispatch base head: `4def03d7aa7665cdc80ee56ab3ce702f3a2787e0`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker return path: `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_WORKER_RETURN_2026-09-01.md`

successorTrancheOpened: NO

## Dispatch Prompt Envelope

Role: internal governance implementation worker for MFRP-H0. The
orchestrator/reviewer remains closure owner.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_2026-09-01.md`.

Paired baseline: `docs/baselines/CVF_GC018_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_2026-09-01.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: packet authored on 2026-09-01 from clean committed base
`4def03d7aa7665cdc80ee56ab3ce702f3a2787e0`; H0 is the only open MFRP
implementation lane.

Do-not-misread notes: harden receipt reuse only. Do not change command
semantics, any checker verdict, command catalog, hook, standard, ADIF, session,
P1/P2, provider/live or public surface. A cache miss runs the full bundle; it
is not a gate failure and is not review advice.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired packet, current runner/catalog/focused tests, the MFRP roadmap
and reconciliation, Core Guard checker and worker-output checker sources; then
capture HEAD/status/hashes and run pre-implementation.

Return contract: modify exactly two protected Python paths, create exactly one
worker return, run every named test/gate, leave all changes uncommitted, and
return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Repair the shipped autorun PASS-receipt reuse boundary so a receipt can be
reused only when its repository-controlled verifier inputs and Python
interpreter identity exactly match the inputs that produced the PASS.

## Semantic Convergence Outcome

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "mfrp-autorun-receipt-verifier-identity",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [], "resolved": [], "retained": [],
    "new": ["autorun-pass-receipt-does-not-bind-verifier-input-identity"],
    "reopened": [],
    "current": ["autorun-pass-receipt-does-not-bind-verifier-input-identity"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0, "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0, "nonDecreasingBlockerTransitions": 0
  },
  "claims": [{
    "claimId": "MFRP-H0-DISPATCH-SEED",
    "claimClass": "DOCUMENTATION_ONLY",
    "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
    "evidenceRef": "docs/baselines/CVF_GC018_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_2026-09-01.md"
  }],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

The worker return uses ordinal 1 and this work order's exact raw SHA-256 as
its predecessor. Successful implementation resolves the named blocker and
selects `READY_WITH_EXECUTABLE_PROOF` with `EXECUTABLE_IMPLEMENTATION`; a
failed hostile matrix retains it and selects `STOP_REASSESS_ARCHITECTURE` with
receipt reuse disabled.
`successorTrancheOpened: NO` remains invariant.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: MFRP-H0
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

## Scope / Target / Owner Boundary

In scope: existing receipt schema/context/load/write/reuse code, a conservative
repository-controlled verifier snapshot, interpreter identity, focused hostile
tests and one implementation return.

Authorized worker paths:

1. `governance/compat/run_agent_autorun_workflow_gate.py`
2. `governance/compat/test_run_agent_autorun_workflow_gate.py`
3. `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_WORKER_RETURN_2026-09-01.md`

No other path may change. Temporary test content must use test-owned temporary
directories and be removed automatically.

## Write Ownership

Worker owns only the three authorized paths and must not commit. Reviewer owns
semantic acceptance, bounded correction if needed, material commit and later
continuity sync. Agent/provider/role labels do not grant trust; evidence and
the accepted SOT chain do.

## Authority Chain

1. Active CVF governance and autorun standards.
2. Paired H0 baseline, raw SHA-256
   `29cb00bf693b7a0428501ea7a422e2b0ee19d33e35a5741e51becec26efee640`.
3. Revised MFRP roadmap and CVF external-finding reconciliation.
4. This exact work order.
5. Worker output is non-authoritative until independent evidence review.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | Authorized machine-first foundation upgrade and retains scope-expansion checkpoints. |
| Dispatcher | Fixes the defect boundary, exact paths, digest profile, hostile matrix and rollback. |
| Worker | Implements only the authorized receipt/test changes and returns evidence without commit. |
| Reviewer/closer | Evaluates the diff/evidence, independently recomputes selected probes, and owns acceptance/commits. |

## Dual Agent Surface Matrix

| Surface | Disposition | Evidence boundary |
|---|---|---|
| INTERNAL_AGENT | AUTHORIZED_ONCE | One bounded no-commit H0 implementation pass. |
| EXTERNAL_AGENT_CLI_MCP | FORBIDDEN | Claude critique is accepted historical input only; no new invocation. |
| Adapter boundary | DOCUMENTATION_ONLY_NO_RUNTIME_ADAPTER | Repository file handoff only. |

## Required First Reads

1. current startup bootstrap, memory and active handoff;
2. guard orientation README and governed literal gotchas;
3. paired H0 baseline and this work order;
4. revised MFRP roadmap and CVF reconciliation;
5. `governance/compat/run_agent_autorun_workflow_gate.py` in full;
6. `governance/compat/agent_autorun_command_catalog.py` in full;
7. `governance/compat/test_run_agent_autorun_workflow_gate.py` in full;
8. Core Guard, work-order and worker-return checker sources named below.

## Pre-Flight Checks

Capture full `executionBaseHead`, `git status --short --untracked-files=all`,
and SHA-256 for baseline and work order. Require a clean worktree and a HEAD
equal to the committed dispatch packet head. Run:

`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD`

Stop on an unexpected path or authority contradiction. No credential, network,
provider, package install or live release proof applies.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "MFRP-H0",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "ENRICHES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["governance/compat", "docs/baselines", "docs/work_orders", "docs/reviews"],
  "claims": ["autorun receipt verifier identity invalidation"],
  "requiredProof": ["fixed vector", "cache hit", "cross-batch drift", "shared-input drift", "interpreter drift", "fail-closed miss", "independent review"],
  "operatorCheckpoints": ["scope expansion", "command-semantic change", "new standard", "provider/live/public action"],
  "forbiddenEffects": ["checker verdict change", "command catalog change", "hook change", "provider execution", "public sync", "worker commit"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Intake Role Routing Decision

routeMode: MULTI_AGENT_MULTI_ROLE

intakeSummary: repository-owned local governance receipt hardening

scopeClassification: PROTECTED_GOVERNANCE_IMPLEMENTATION

riskSensitivity: HIGH_LOCAL_CONTROL_PLANE

roleSeparationBasis: worker authors the bounded implementation evidence;
reviewer evaluates that returned evidence and independently probes bypasses.
The route token names dispatch choreography only and is never a trust source.

escalationCondition: any required fourth path, command/verdict change, incomplete
identity treated as a hit, non-deterministic vector, provider/live need or
public effect returns to the orchestrator without self-expansion.

## Execution Plan

1. Capture dispatch identity and run pre-implementation.
2. Add the v2 receipt and verifier-identity profile without changing command execution.
3. Build a deterministic current-state snapshot from Git-tracked files and all
   untracked non-ignored regular files; require every command file to be a member.
4. Bind the enumerated Python interpreter identity.
5. Make all identity construction uncertainty a cache miss/full run.
6. Add fixed-vector, exact-hit and hostile-drift regressions.
7. Run focused and governed gates and write the no-commit worker return.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| H0 precedes P1 | System Loop Interlock Routing | `successorTrancheOpened: NO` | reviewer checks no P1/P2 path changed | N/A with reason: ordering constraint, not a worker output |
| bind conservative dependency closure | Conservative Verifier-Input Snapshot | `verifierIdentityDigest` | hostile tracked/untracked/shared/config drift tests | N/A with reason: pending worker proof |
| bind interpreter identity | Interpreter Identity | six exact interpreter values | hostile interpreter drift tests | N/A with reason: pending worker proof |
| versioned fail-closed migration | Receipt Migration | `cvf.autorun.pass-receipt.v2` | v1/partial/malformed receipt tests | N/A with reason: pending worker proof |
| use fixed canonical hash discipline without TruthReceipt label reuse | Canonical Preimage Profile | `cvf.autorun.verifierIdentity.v1` and published vector | independent SHA-256 recomputation | N/A with reason: pending worker proof |
| unknown dependencies are misses | Fail-Closed Reuse Semantics | full-bundle fallback and no receipt from incomplete identity | unreadable/unstable input tests | N/A with reason: pending worker proof |
| hostile same-batch/cross-batch/shared/config/interpreter cases | Mandatory Hostile Tests | expected/observed case ledger | focused pytest plus reviewer probes | N/A with reason: pending worker proof |
| rollback disables reuse and preserves full execution | Rollback boundary and acceptance criteria | `DISABLE_REUSE_AND_STOP` | no-reuse/full-bundle control | N/A with reason: pending worker proof |

## Text Encoding Exception

The single Greek alpha code point in the published canonicalization test vector
is intentional and required to prove UTF-8 Unicode preservation rather than
ASCII escaping. All repository paths and prose outside that literal vector use
the normal encoding discipline.

## Implementation Requirements

### Receipt Migration

- Set the only reusable schema to `cvf.autorun.pass-receipt.v2`.
- Treat v1, unknown schema, absent field, malformed value and partial v2 as a
  deterministic miss. Never mutate or upgrade an old receipt in place.
- Preserve `--reuse-valid-receipt` as opt-in. Without the flag, execute the
  full bundle even if a valid v2 receipt exists.
- Record `verifierIdentityProfile` and `verifierIdentityDigest` in both context
  and written receipt; exact comparison is mandatory.

### Conservative Verifier-Input Snapshot

- Membership includes every path returned by `git ls-files -z` and
  `git ls-files --others --exclude-standard -z` at evaluation time. Duplicate
  paths collapse to one record. Every repository-relative file named directly
  in the selected command argv must resolve inside the repository and be a
  member; ignored or missing command inputs make reuse unavailable.
- Normalize separators to `/`, reject absolute/out-of-repository traversal,
  sort paths lexicographically and hash the current bytes with SHA-256.
- A tracked missing path receives an explicit stable missing marker in the
  preimage; unsafe, non-regular or unreadable inputs make reuse unavailable.
- Detect read instability by comparing stable file identity/size/mtime before
  and after the byte read or by an equivalently stronger local mechanism. A
  changed-during-read input makes reuse unavailable.
- Do not hash unbounded process environment, credentials, raw command output,
  `.git`, `.cvf/runtime`, Git-ignored files/secrets or provider state.
- This H0 snapshot intentionally over-invalidates on any tracked repository
  byte drift. Narrowing it requires a later proof-backed tranche; the worker
  may not substitute a self-declared direct-script list.

### Interpreter Identity

Bind exactly:

- `sys.implementation.name`;
- `sys.implementation.cache_tag` or an explicit empty string;
- `major.minor.micro.releaselevel.serial` from `sys.version_info`;
- resolved `sys.executable` path normalized with `/`;
- SHA-256 of the interpreter executable bytes.

An absent, unsafe or unreadable executable identity makes reuse unavailable.
No ambient environment variable or installed-package inventory is added.

### Canonical Preimage Profile

Profile name: `cvf.autorun.verifierIdentity.v1`.

Digest: lowercase SHA-256 of UTF-8 RFC 8785 JCS for a restricted I-JSON domain
containing only objects, arrays and Unicode strings. Object keys are sorted,
arrays retain their contract order, paths are sorted before serialization,
and no insignificant whitespace or ASCII-only escaping is allowed. Reject any
unexpected value type rather than silently canonicalizing it. Do not use
`cvf.sotThreeLayer.receiptHash.v1`; that label belongs to TruthReceipt.

Published independent vector preimage:

```json
{"digestAlgorithm":"sha256","files":[{"path":"governance/compat/check_α.py","sha256":"0000000000000000000000000000000000000000000000000000000000000000"}],"interpreter":{"cacheTag":"cpython-313","executablePath":"C:/Python313/python.exe","executableSha256":"1111111111111111111111111111111111111111111111111111111111111111","implementation":"cpython","version":"3.13.7.final.0"},"profile":"cvf.autorun.verifierIdentity.v1"}
```

Expected UTF-8 SHA-256:
`37730e62eac9a4f900b100c4734aee20311d596fd6426cebea7f6ae8d1a63575`.
The test must contain this literal preimage/digest and must not derive the
expected value with the production canonicalizer.

### Fail-Closed Reuse Semantics

- Identity-complete exact match permits reuse; no weaker fallback exists.
- Identity mismatch/unavailability prints one secret-safe reason and runs the
  complete selected phase bundle.
- Compute a complete identity before fresh execution and again after all
  commands PASS. Write v2 only when both complete digests are equal. A failed
  recomputation or mid-bundle drift reports PASS without a reusable receipt.
- Reused PASS remains only execution evidence for the named mechanical gates.
  Output must not say review, rerun or semantic judgment is unnecessary.
- Preserve command ordering, parallel/serial behavior, phase ranges, closure
  finality and all existing exit codes.

## Mandatory Hostile Tests

Required test IDs or equivalently explicit test names:

- `V2_EXACT_STATE_REUSE_HIT_NO_EXECUTION`
- `V1_SCHEMA_FORCES_FULL_RUN`
- `DIRECT_CHECKER_BODY_DRIFT_SAME_ARGV_MISS`
- `CROSS_BATCH_TRACKED_VERIFIER_DRIFT_OUTSIDE_PATH_PLAN_MISS`
- `SHARED_IMPORTED_MODULE_DRIFT_MISS`
- `TRACKED_CONFIG_REGISTRY_FIXTURE_STANDARD_DRIFT_MISS`
- `UNTRACKED_NONIGNORED_SHARED_INPUT_DRIFT_MISS`
- `RUNNER_OR_CATALOG_DRIFT_MISS`
- `INTERPRETER_IMPLEMENTATION_VERSION_TAG_PATH_OR_BYTES_DRIFT_MISS`
- `UNREADABLE_OR_UNSTABLE_INPUT_MISS_NO_REUSABLE_RECEIPT`
- `MID_BUNDLE_INPUT_DRIFT_PASS_BUT_NO_REUSABLE_RECEIPT`
- `PATH_ORDER_CANONICALIZATION_STABLE`
- `UNICODE_JCS_FIXED_VECTOR_MATCH`
- `NO_REUSE_FLAG_ALWAYS_EXECUTES`
- `REUSE_DISABLED_FULL_BUNDLE_PASS_CONTROL`
- `MALFORMED_OR_PARTIAL_V2_FAILS_CLOSED`
- `SECRET_SAFE_MISS_REASON_NO_FILE_CONTENT_OR_ENV_VALUE`

Tests may inject Git/file/interpreter providers to stay deterministic. They
must prove both miss reason and full-bundle execution; checking digest
inequality alone is insufficient.

## Evidence Requirements

- Exact before/after receipt field matrix.
- Snapshot membership and exclusion rationale.
- Literal canonical vector and independent recomputation.
- Expected/observed ledger for all hostile test IDs.
- Proof that an exact hit executes zero commands.
- Proof that every miss executes the full phase commands.
- Proof that incomplete identity cannot write a reusable v2 receipt.
- Proof that a pre/post identity mismatch cannot write a reusable v2 receipt.
- Focused suite, direct runner smoke check, worker-return gate, diff hygiene,
  full execution base/final HEAD and no-commit status.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Existing receipt schema is v1 | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | constants | `RECEIPT_SCHEMA` | autorun runner | ACCEPT |
| Existing command identity is name plus argv | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | `_command_manifest_hash` | manifest payload | receipt context | ACCEPT |
| Existing path fingerprint is current path-plan scoped | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | `_worktree_fingerprint` | `build_path_plan` | receipt context | ACCEPT |
| Receipt validity checks schema/status and expected fields | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | `_load_valid_receipt` | expected loop | receipt validator | ACCEPT |
| Runner imports catalog and commit-steward helper | executable source | `governance/compat/run_agent_autorun_workflow_gate.py` | imports | `agent_autorun_command_catalog`; `run_agent_commit_steward_preflight` | autorun composition | ACCEPT |
| Catalog supplies all selected commands | executable source | `governance/compat/agent_autorun_command_catalog.py` | command factories and tuples | `_common_commands`; `_pre_implementation_commands`; `PRE_PUSH_COMMANDS` | command catalog | ACCEPT |
| Focused suite lacks the named hostile identity cases | regression source | `governance/compat/test_run_agent_autorun_workflow_gate.py` | receipt/fingerprint tests | existing receipt tests | autorun test owner | ACCEPT |
| H0 is required before P1 | governed decision | `docs/roadmaps/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_ROADMAP_2026-09-01.md` | tranche map | MFRP-H0 | MFRP roadmap | ACCEPT |
| Direct script hashes are insufficient | governed reconciliation | `docs/reviews/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_EXTERNAL_FINDING_ABSORPTION_AND_CVF_RECONCILIATION_2026-09-01.md` | H0 Bounded Design Requirement | conservative closure | CVF reconciliation | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION_PLUS_FRESH_EXECUTABLE_PROOF

priorVerificationArtifact: `docs/reviews/CVF_GCLH_MACHINE_FIRST_REVIEW_PREFLIGHT_EXTERNAL_FINDING_ABSORPTION_AND_CVF_RECONCILIATION_2026-09-01.md`

priorVerificationAnchor: `2b501582df905da37b6a97865f844401a8ee38c9`

freshRecomputeRequired: all implementation hashes, fixed vector, hostile cases,
focused suite, exact diff/status and reviewer probes

unicodePathHandling: UTF-8 JCS, slash-normalized repository paths, no
replacement decoding

extractedTextAuthority: direct source and observed execution control; critique
and prior reconciliation establish scope only

## Negative Search And Collision Discipline

- The paired baseline, work order and worker return paths were absent at
  authoring start.
- Search roots and tokens are recorded in the paired baseline.
- Existing MFRP-H0 mentions are roadmap/reconciliation/continuity planning
  pointers, not a competing execution packet.
- Disposition: `ABSENT_H0_IMPLEMENTATION_AND_OUTPUT_CONFIRMED`.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: H0 consumes a governed CVF reconciliation and
current repository source; it does not reopen or inventory legacy material.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent returned output |
| Chain map route | external critique -> atomic source verification -> CVF reconciliation -> revised roadmap -> H0 packet |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired H0 baseline/work order and existing autorun receipt owner |
| Disposition | ADAPT_VERIFIED_FINDING; no raw external authority and no new external invocation |
| Claim boundary | H0 implementation is controlled by CVF sources and fresh local proof. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`autorun receipt verifier identity hardening`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "autorun receipt verifier identity hardening" --role dispatcher --lifecycle-phase dispatch --json`
- Returned defects: `NONE_RETURNED`
- Disclosed defectIds: `NONE`
- Dispatch impact: no new ADIF edit; apply the accepted MFRP defect owner and
  fail-closed evidence posture.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Commit mode: WORKER_MUST_NOT_COMMIT`; prompt labels; Source Verification columns; SCEC and review-control fields; protected-path authorization labels; trace and delta-boundary fields; `successorTrancheOpened: NO` |
| gateRunPurpose | Confirm source-read packet shape and protected authorization after authoring. |
| claimBoundary | Dispatch structure only; no H0 executable result is claimed. |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-H0 --title "Autorun Receipt Verifier Identity Hardening" --date 2026-09-01 --base 4def03d7a --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --scec-problem-key mfrp-autorun-receipt-verifier-identity --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope EXECUTABLE_IMPLEMENTATION --stdout` |
| generatedProfile | protected governance path, internal no-commit implementation |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added exact source findings, snapshot/interpreter/JCS contract, hostile matrix, exact scope and rollback. |
| checkerReadAheadConfirmation | COMPLETE |
| docOnlyNewFields | verifier identity profile, file membership, interpreter identity and hostile test IDs |
| claimBoundary | Dispatch provenance only. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update only optional autorun receipt reuse
identity and its focused regression suite. Underlying command selection,
execution and checker semantics must remain unchanged.

Protected paths:

- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`

Operator authorization: the operator approved machine-first CVF learning and
said to continue after the H0-first revised roadmap and reconciliation were
accepted.

Rollback boundary: disable optional reuse and always execute the full bundle.
No protected-path change is accepted if full execution no longer works or if
any incomplete identity can become a cache hit.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | operator -> dispatcher -> bounded worker -> independent reviewer/closer |
| phase | protected local implementation pending reviewer closure |
| baseHeadFor(phase) | dispatchBaseHead=`4def03d7aa7665cdc80ee56ab3ce702f3a2787e0`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exactly two Python modifications and one worker return |
| traceScope(phase, actor) | worker records identity fields, cases, commands, hashes, diff and no-commit evidence |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no unrelated edit, staging, receipt migration or successor work |
| nextMoveSurfaces | material closure first; continuity in a separate commit after acceptance |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MFRP_H0_AUTORUN_RECEIPT_VERIFIER_IDENTITY_HARDENING_COMPLETION_2026-09-01.md`

reviewerOwnedClosurePaths: the two Python changes and worker return; a separate
completion artifact is optional when the worker return contains an explicit
Independent Reviewer Correction and final disposition.

Reviewer checks the exact work-order digest and manifest, reads the source diff,
recomputes the literal JCS vector with an independent snippet, reruns the
focused suite and independently exercises exact-hit, cross-batch tracked drift,
shared/config input drift and interpreter drift. Reviewer does not recreate
the implementation. Any fourth-path need or semantic command change blocks.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections include Purpose, Target / Source, Scope / Methodology,
Findings / Position, Risk / Corrective Action, Decision / Disposition,
External Knowledge Intake Routing, Rescan Intelligence Hardening, Corpus
Completeness And Report Integrity, Finding-To-Governance Learning Disposition,
Epistemic Process Block, Checker Source Read-Ahead Block, Agent Operation Trace
Block, Delta Execution Claim Boundary Control Block, Public Export Disposition,
Changed Files, git status --short, Worker Experience Retrospective and
No-Commit Statement. Non-applicable conditional sections require a reason.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: only a complete exact v2 verifier/interpreter
identity reuses PASS; every named drift or uncertainty executes the full bundle.

Evidence Comparison Requirement: compare expected/observed reuse, execution
count, miss reason, receipt-write status and digest for every hostile case.

Contradiction Or Gap Disposition: any hit on drift/uncertainty, any failure to
run the full bundle after a miss, or any mismatched fixed vector selects
`DISABLE_REUSE_AND_STOP`.

Claim Update Requirement: the worker selects `COMPLETE_PENDING_REVIEW` only
with the full matrix; reviewer selects `H0_CLOSED_PASS_BOUNDED` or
`DISABLE_REUSE_AND_STOP` from independent evidence.

## System Loop Interlock Routing

The loop stops at H0 reviewer closure. P1, P2 and all phase-return/readout work
remain closed regardless of H0 result until a later continuity-authorized
operator move. `successorTrancheOpened: NO` throughout.

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: H0 changes one ignored local JSON receipt format
and no durable product store, generated aggregate, provider store or public
storage layout.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher/orchestrator |
| Provider or surface | local private provenance workspace |
| Session or invocation | MFRP-H0 dispatch authoring, 2026-09-01 |
| Working directory | repository root |
| Command or tool surface | governed source reads, scaffold helper, apply_patch, local guards, git |
| Target paths | paired MFRP-H0 baseline and work order |
| Allowed scope source | operator-approved machine-first CVF roadmap and current H0 work-order checkpoint |
| Before status evidence | HEAD `4def03d7aa7665cdc80ee56ab3ce702f3a2787e0`; worktree clean; packet paths absent |
| After status evidence | paired dispatch packet only; implementation paths unchanged |
| Diff evidence | exact two-path dispatcher manifest |
| Approval boundary | H0 dispatch only; no verifier implementation in authoring batch |
| Claim boundary | source-verified authorization, not executable repair evidence |
| Agent type | dispatcher/orchestrator |
| Invocation ID | `mfrp-h0-dispatch-2026-09-01` |
| Expected manifest | paired H0 baseline and work order |
| Actual changed set | paired H0 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local optional PASS-receipt reuse identity hardening |
| claimDisposition | CLAIM_REJECTED: dispatch packet does not claim H0 is implemented or effective |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no H0 v2 receipt exists yet |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: only baseline/work-order authoring occurs in this batch |
| invocationBoundary | one internal no-commit worker pass followed by independent review |
| interceptionBoundary | no provider, IDE, shell, filesystem watcher or agent-reasoning interception claim |
| claimLanguage | future proof is limited to deterministic local cache invalidation and fallback execution |
| forbiddenExpansion | semantic truth, reviewer replacement, command/verdict changes, P1/P2, provider/live, public/deploy/production |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python -m pytest governance/compat/test_run_agent_autorun_workflow_gate.py -q
python governance/compat/run_dispatch_packet_author_fast_gate.py --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_core_guard_self_protection.py --base <executionBaseHead> --head HEAD
python governance/compat/check_semantic_convergence_control.py --base <executionBaseHead> --head HEAD
git diff --check
git diff --name-status
git status --short --untracked-files=all
```

The reviewer additionally runs pre-commit and split-range pre-closure after the
material commit. Do not run the live release bundle; H0 makes no provider claim.

## Acceptance Criteria

- [ ] Exactly three authorized uncommitted paths; no rename/deletion.
- [ ] v2 is the only reusable schema; v1/partial/unknown receipts miss.
- [ ] Snapshot contains all Git-tracked and untracked non-ignored current bytes;
      every direct command file is a safe member.
- [ ] Interpreter identity has all six enumerated values.
- [ ] Fixed Unicode JCS vector equals the literal expected SHA-256.
- [ ] Exact state hits and executes zero commands.
- [ ] Every hostile drift/uncertainty misses and executes the full bundle.
- [ ] Incomplete identity writes no reusable v2 receipt.
- [ ] Mid-bundle pre/post identity drift writes no reusable v2 receipt.
- [ ] No-reuse and rollback controls preserve full bundle execution.
- [ ] No command catalog, checker verdict, hook, standard, ADIF or session edit.
- [ ] Focused tests, author/worker gates, diff hygiene and no-commit evidence pass.
- [ ] Ordinal-1 SCEC successor uses exact work-order digest and no successor.

## Review Gate

Machine checks establish identity mechanics and regression shape, not semantic
truth. Reviewer evaluates the returned evidence graph and independently
recomputes selected probes without repeating the worker's implementation.
Reviewer rejects closure if the solution depends on a self-declared incomplete
dependency list, if the fixed vector is self-derived, or if any miss can skip
full execution.

## Operator Checkpoint

No checkpoint is needed inside the exact three-path H0 scope. Stop for any
fourth path, command/verdict change, new owner/standard, provider/live/public
effect or proposed opening of P1/P2.

## Closure Checklist

- exact manifest, base/head and no-commit evidence;
- source diff and fixed-vector independent recomputation;
- complete hostile matrix with execution-count evidence;
- focused/author/worker/core-guard/SCEC gates and diff hygiene;
- reviewer disposition `H0_CLOSED_PASS_BOUNDED` or `DISABLE_REUSE_AND_STOP`;
- separate material and continuity commits;
- Public catalog N/A: private foundation repair adds no public capability;
- P1/P2 and all product/provider/public effects remain parked.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only after the exact matrix and gates pass.
Return `BLOCKED_WITH_REASON` for source contradiction, forbidden-path need,
incomplete deterministic identity, fixed-vector mismatch or scope expansion.
Do not open a successor.

## Worker Autonomy / No-Question Rule

Worker may choose function decomposition and test injection seams within the
fixed profile, membership, identity, fail-closed semantics, path manifest and
effect boundaries. It must repair allowed-scope test/gate defects directly and
must not expose chain-of-thought.

## Claim Boundary

This work order authorizes one local optional-receipt cache hardening and its
focused proof. It does not claim checker semantic correctness, review
completion, seven-phase truth, runtime/provider behavior, public readiness,
deployment, production or authority from an agent/role label.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF governance-foundation hardening.
