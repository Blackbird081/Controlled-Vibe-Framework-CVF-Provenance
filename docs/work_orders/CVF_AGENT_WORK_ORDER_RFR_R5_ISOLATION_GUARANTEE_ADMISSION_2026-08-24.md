# CVF Agent Work Order - RFR-R5 Isolation Guarantee Admission

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-08-24

Batch ID: RFR-R5

## Dispatch Prompt Envelope

```text
Role: implementation worker. The current orchestrator remains independent reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_2026-08-24.md
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: capture executionBaseHead from repository HEAD at worker start; dispatchBaseHead is 0ee6e76b6.
Current-time notes: only RFR-R5 is released; R6 and all external-effect lanes remain parked.
Do-not-misread notes: make worker-thread isolation claims truthful and fail closed; do not build a container, claim physical containment, install dependencies, use network, or edit a ninth path.
Required first actions: read required authority and sources; capture HEAD/status; verify seven hashes and exact eight-path manifest; run worker ADIF resolver.
Return contract: COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON with exact diff, tests/gates, residuals, unchanged HEAD, empty staging and zero external calls.
```

Dispatch base head: `0ee6e76b6`

dispatchBaseHead: `0ee6e76b6`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET_AFTER_WORKER_RETURN`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path: `docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_WORKER_RETURN_2026-08-24.md`

## Purpose

Close F9 boundedly by adding typed isolation requirements, truthful adapter
guarantee profiles and fail-closed admission to the existing Safety Runtime
contract and WorkerThread adapter.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "RFR-R5",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts",
    "EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts",
    "EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts",
    "EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts",
    "EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts",
    "EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts",
    "docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md",
    "docs/reviews/",
    "docs/baselines/",
    "docs/work_orders/",
    "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json",
    "CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json",
    "CVF_SESSION/ACTIVE_SESSION_STATE.json"
  ],
  "claims": ["F9 typed and tested isolation-guarantee admission"],
  "requiredProof": ["eight-dimensional matrix", "focused adapter tests", "Runtime Adapter Hub package tests", "TypeScript", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": ["R6 requires accepted R5 closure; standing roadmap authority permits dependency-ordered dispatch"],
  "forbiddenEffects": ["worker stage or commit", "dependency installation", "provider/live/network call", "credential access", "container deployment", "public write", "new subsystem"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R5 --title "Runtime Finding Remediation R5 Isolation Guarantee Admission" --date 2026-08-24 --base 0ee6e76b6 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R4 closed at 8ec399aa5 and continuity 0ee6e76b6; standing roadmap authority releases R5" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified F9 owners, hashes, exact-eight manifest, dimensional admission design and role split |
| checkerReadAheadConfirmation | applicable checker sources and routed standards read before authoring |
| docOnlyNewFields | none; worker selects bounded type names inside invariants |
| claimBoundary | dispatch provenance only; no implementation or closure claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| RFR-R4 closure | material `8ec399aa5`; continuity `0ee6e76b6` | accepted R4 required | ACCEPT |
| F9 roadmap order | runtime findings roadmap R5 row | R5 follows R4 | ACCEPT |
| operator continuation | standing autonomous dependency-ordered instruction | fresh R5 dispatch | ACCEPT |

## Required First Reads

1. `AGENTS.md`, bootstrap, front door and active handoff.
2. guard orientation and literal-format gotchas.
3. paired R5 baseline and this work order.
4. all seven pre-existing hashed sources in full.
5. applicable worker-return checker sources before return authoring.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Operator | standing roadmap authority and packet transfer |
| External worker | exact-eight implementation/proof; never stage or commit |
| Reviewer/closer | independent inspection, bounded repair, acceptance and material commit |
| Session-sync steward | continuity only after material identity |

## Authority Chain

1. Frozen doctrine and operating model remain supreme.
2. `AGENTS.md`, the runtime-findings authority, roadmap and paired R5 baseline
   govern this dispatch.
3. This work order grants only its exact-eight implementation and proof scope.
4. The worker supplies evidence; the independent reviewer alone may accept,
   repair, commit, close or escalate the result.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | close verified F9 isolation-claim mismatch |
| scope classification | SECURITY_SENSITIVE_RUNTIME_CONTRACT_IMPLEMENTATION |
| primary task class | bounded execution/isolation implementation |
| risk sensitivity | HIGH |
| selected role route | MULTI_AGENT_SINGLE_ROLE |
| orchestration requirement | external no-commit worker plus independent reviewer |
| role separation basis | worker cannot accept its own security-boundary claim change |
| escalation condition | ninth path, new runtime owner, real containment engine or external effect |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact manifest. Repair in-scope failures after
reading their source. Return `BLOCKED_WITH_REASON` only if completion needs a
ninth path, new owner/dependency, installation, container/network/credential/
live/public action, or a new critical contradiction. Never stage, commit or
push and do not ask permission for an in-scope repair.

## Pre-Flight Checks

- capture `git rev-parse HEAD` and initial `git status --short`;
- stop for overlapping pre-existing changes;
- verify all seven hashes and worker-return path absence;
- verify exact eight-path manifest;
- run ADIF resolver for implementation/worker/pre-execution.

## Scope / Target / Owner Boundary

Worker may modify or create exactly:

1. `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts`
2. `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts`
3. `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts`
4. `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts`
5. `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts`
6. `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts`
7. `docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md`
8. `docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_WORKER_RETURN_2026-08-24.md`

No ninth path, deletion or rename is authorized. Package/lock files, generated
registries, governance checkers, roadmap, session state, credentials, public
surfaces and other adapters are read-only.

## Write Ownership

Worker owns exactly eight paths. Reviewer owns any GC-051 entry required by
review findings, completion review, R5-only roadmap transition, material
commit and later continuity.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| contract has policy dimensions but no guarantee admission | TYPE_GAP | `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts` | types/defaults/execute | `SandboxConfig`; `SandboxExecutor`; `SandboxResult` | Safety Runtime | ACCEPT |
| local types mirror canonical contract | MIRROR_OWNER | `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts` | full file | sandbox mirror | Runtime Adapter Hub | ACCEPT |
| adapter invokes host child process and inherits environment | RUNTIME_GAP | `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts` | `runInWorker` | `execFileSync`; `process.env` | WorkerThreadSandboxAdapter | ACCEPT |
| adapter tests own current behavior | TEST_OWNER | `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts` | WorkerThreadSandboxAdapter suite | focused cases | Runtime Adapter Hub tests | ACCEPT |
| contract tests own validation/default behavior | TEST_OWNER | `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts` | execute/validate/default suites | SandboxIsolationContract | Safety Runtime tests | ACCEPT |
| adapter barrel owns export | EXPORT_OWNER | `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts` | export list | WorkerThreadSandboxAdapter | Runtime Adapter Hub barrel | ACCEPT |
| active reference owns package claim boundary | REFERENCE_OWNER | `docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md` | scope and packet consequences | export surface | pre-public reference | ACCEPT |
| F9 requires explicit guarantees and unsupported rejection | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | F9 and corrective action | F9 | governed review | ACCEPT |

## Source Hash Manifest

| Path | Required SHA-256 before edit |
| --- | --- |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/simulation/sandbox.isolation.contract.ts` | `a6e31345a06a28090d9b031d19f3e1ed401c39a51da257288de00debaa5caebe` |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/tests/sandbox.isolation.contract.test.ts` | `a907b31e4e5fa83024c50092debaf6d82add6b1558f31c8e1d1cba0f65b17ad4` |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/sandbox.types.ts` | `8a2cb4c009a822a070598a17b166a207b7ec318801cf0fca967e569aa1a6f3ca` |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/worker.thread.sandbox.adapter.ts` | `f450e3deb6dee7398c34d716fbab39f9ef7028d19e70cb3a47aed0708b92006d` |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/adapters/index.ts` | `d9cefbda3c08e180c2f3970c689e860bd0ab88b11d801177542d21304dfc3aee` |
| `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/tests/adapters.test.ts` | `9c0d59d0e06922ce729cdc70f3f52141edd59b642d8f7d4f427fcbce399b5e94` |
| `docs/reference/CVF_PREPUBLIC_RUNTIME_ADAPTER_HUB_EXPORT_SURFACE_2026-04-03.md` | `4f9847a8b702159faf9c62a5f520fb104651cd1dac85bfc146aff255dc03297a` |

Hash drift before edit is `BLOCKED_WITH_REASON`.

## Exact Implementation Contract

### R5-A canonical dimensional vocabulary

In the Safety Runtime owner define one exact union for `filesystem`, `network`,
`process`, `environment`, `credential`, `ipc`, `persistence`, and `host` plus
typed requirement, immutable adapter profile, admission verdict/reasons and
result evidence. Mirror the shapes exactly in Runtime Adapter Hub. The adapter
barrel must export the public types/functions needed to request and inspect
admission; the root barrel already delegates through it and needs no edit.

### R5-B fail-closed defaults and validation

Default configuration must mean `SECURITY_BOUNDARY_REQUIRED` with all eight
dimensions required. Validate exact dimension membership, uniqueness,
requirement/mode consistency, platform/profile consistency and complete
profile coverage. Any malformed or unsupported claim rejects before executor,
worker or child-process creation and returns evidence naming missing guarantees.

### R5-C explicit best-effort boundary

Permit execution on `worker_threads` only through an explicit
`BEST_EFFORT_EXPLICIT` requirement with an empty required-dimensions set.
All eight profile dimensions remain visible. Filesystem/network heuristics and
resource/time checks may remain, but evidence and docs must call them advisory
prechecks rather than physical isolation.

### R5-D environment and credential safety

Do not spread host `process.env` into worker data or child-process options.
Construct both worker and child environments only from the explicit command
environment. Do not record values, credentials or secret names in evidence.
This hardening does not authorize a broader environment/credential guarantee
unless adversarial proof establishes the exact claim.

### R5-E canonical contract admission

`SandboxIsolationContract` must evaluate the selected executor's profile before
delegation and emit auditable rejection evidence. Stub/custom test executors
must declare profiles explicitly. Existing result paths must carry evidence;
no `as` cast may fabricate a missing profile/result field.

## Dedicated Adversarial Matrix

| Case | Required result |
| --- | --- |
| default worker-thread security requirement | reject before execution; all unsupported dimensions listed |
| any one of eight dimensions required on worker thread | reject and name exact missing guarantee |
| best-effort with non-empty required dimensions | reject as inconsistent |
| best-effort explicit with empty dimensions | may execute; result says non-security boundary |
| unknown, duplicate, missing profile dimension | reject deterministically |
| config platform/profile mismatch | reject before execution |
| command omits env | child sees no inherited sentinel credential/environment value |
| command supplies bounded env | only explicitly supplied values cross |
| empty/failed/timed-out command | retains complete isolation evidence |
| policy heuristic triggers | never claims guaranteed containment |

Tests must be deterministic and local. No DNS, HTTP, provider, credential,
container or deployment call is allowed.

## Required Artifact Manifest

Exactly the eight worker-owned paths listed under Scope; no deletion or rename.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| canonical contract and test | add types, defaults, admission, evidence and negative proof |
| local mirror and worker adapter | preserve structural parity; enforce truthful admission and explicit environment |
| adapter barrel and test | export bounded surface and prove all eight dimensions |
| existing reference | narrow claims to explicit best-effort/non-security boundary |
| worker return | complete checker-safe evidence packet |

## Required Proof Manifest

- source-hash verification before edits;
- exact eight-path `git diff --name-status` and no unexpected untracked file;
- focused Safety Runtime test using only an already available repo-local
  toolchain, or exact dependency-gap evidence without installation;
- focused and full Runtime Adapter Hub tests;
- Runtime Adapter Hub TypeScript check;
- structural mirror comparison and eight-dimension reconciliation;
- `git diff --check`, file-size guard, worker-return fast gate;
- unchanged HEAD, empty staging and zero external calls.

## Required Proof Manifest Atomic Literal Discipline

Each proof row in the worker return must contain the exact command, working
directory, result/count and terminal disposition in one atomic row. Do not
split a required command from its PASS, BLOCKED or N/A-with-reason result.

## Verification Commands

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
$rfrR5ExecutionBaseHead = git rev-parse HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $rfrR5ExecutionBaseHead --head HEAD
python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json
npm test -- --run tests/adapters.test.ts
npm test
npm run typecheck
git diff --check
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --cached --name-only
git status --short --untracked-files=all
```

Run the three npm commands from
`EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB`. For the Safety Runtime focused
test, do not install anything; use a demonstrably existing local toolchain or
record `BLOCKED_COMPONENT_DEPENDENCY_GAP` with the exact attempted command.

## Execution Plan

1. Capture base/status, verify hashes/scope, read authorities/checkers, run
   pre-implementation and ADIF gates; stop on drift or overlap.
2. Implement canonical types/admission/evidence, then mirror them exactly.
3. Harden worker-thread execution and exports without adding an engine.
4. Build the adversarial matrix and update the existing reference.
5. Run all available proof after the final edit, scaffold the worker return,
   self-audit manifest/staging/HEAD, and return without commit.

## Evidence Requirements

Worker return records baseline/final counts, every dimension/profile/verdict,
proof that rejection precedes worker creation, environment-inheritance probe,
Safety Runtime dependency disposition, exact changed set, hashes, unchanged
HEAD, empty staging and zero provider/live/network/install actions.

## Acceptance Criteria

- [ ] Exactly eight isolation dimensions are typed and fully reconciled.
- [ ] Default/unsupported requirements fail before execution.
- [ ] Best-effort execution is explicit, empty-requirement and non-security.
- [ ] Host environment is not implicitly inherited.
- [ ] Exact-eight manifest and all available required gates pass.
- [ ] Worker leaves HEAD unchanged and staging empty.

Fail conditions include a ninth path, silent best-effort default, incomplete
evidence, claimed physical containment, inherited host environment, weakened
tests, dependency installation, external call, stage or commit.

## Review Gate

The reviewer independently probes every dimension, admission timing, mirror
parity, environment leakage and claim wording. Worker assertion is not
closure. Material and continuity commits remain reviewer-owned and separate.

## Closure Checklist

- [ ] reviewer-fast and semantic review pass
- [ ] exact material range is committed by reviewer/closer
- [ ] committed-range pre-closure passes
- [ ] roadmap F9 disposition is evidence-backed
- [ ] continuity is updated only after material identity
- [ ] no public/live/production claim is introduced

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_changed_corpus_registry_coverage.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification columns; dependency release; no-commit packet labels |
| gateRunPurpose | confirm R5 dispatch structure after source verification; not first discovery |
| claimBoundary | structural gates do not prove implementation, isolation or closure |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_WORKER_RETURN_2026-08-24.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Create it first with:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_WORKER_RETURN_2026-08-24.md --title "CVF RFR-R5 Isolation Guarantee Admission Worker Return"
```

Required real headings include Purpose, Scope / Methodology, Findings /
Position, Risk / Corrective Action, Decision / Disposition, Source Inventory,
Checker Source Read-Ahead Block, Agent Operation Trace Block, Delta Execution
Claim Boundary Control Block, External Knowledge Intake Routing, Rescan
Intelligence Hardening, Corpus Completeness And Report Integrity,
Finding-To-Governance Learning Disposition, Epistemic Process Block, Machine
Closure Package, Public Export Disposition and Claim Boundary. Use explicit
N/A-with-reason where applicable.

Atomic packet-shape terms required in the returned artifact: `Findings / Position`;
`Delta Execution Claim Boundary Control Block`; `executionBaseHead`;
`git status --short`; `Rescan Intelligence Hardening`; `Machine Closure Package`.
Every conditional section must be completed or state `N/A with reason`; omission
is forbidden.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_RFR_R5_ISOLATION_GUARANTEE_ADMISSION_COMPLETION_2026-08-24.md` if reviewer needs a separate decision record |
| reviewerOwnedClosurePaths | completion review; R5-only roadmap update; any required GC-051 source entry/aggregate |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | worker implements; independent reviewer/closer accepts and commits |
| phase | RFR-R5 implementation pending review |
| baseHeadFor(phase) | dispatchBaseHead=`0ee6e76b6`; executionBaseHead=worker capture; closureBaseHead=reviewer set |
| changedSetScope(phase) | exact eight worker-owned paths |
| traceScope(phase, actor) | repo-local commands, diff and result evidence only |
| commitOwner(phase) | reviewer/closer; `WORKER_MUST_NOT_COMMIT` |
| crossBatchIsolation | R6 and external-effect lanes parked |
| nextMoveSurfaces | worker return, then reviewer decision and material commit |

## Dual Agent Surface Matrix

| Surface | Disposition | Boundary |
| --- | --- | --- |
| INTERNAL_AGENT | SUPPORTED_BOUNDED | repository worker follows exact packet; no commit |
| EXTERNAL_AGENT_CLI_MCP | CONTRACT_ONLY | operator may copy packet; no claimed automatic enforcement or transport |
| adapter boundary | LOCAL_TYPES_AND_TESTS_ONLY | no provider, CLI/MCP, daemon or external runtime integration |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | YES_LOCAL_TESTED_ONLY |
| runtimeMutationAuthorized | YES_EXACT_EIGHT_PATHS |
| freshnessVerificationMode | deterministic local source/test inspection |
| reason | R5 changes local admission behavior; no provider/live assertion is made |
| requiredFutureAction | independent reviewer reruns local tests; live proof remains N/A |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: dispatcher-only correction of the current
authority hash after repairing this committed packet's pre-implementation
anchor and atomic worker-return terms. These paths are not worker-owned and do
not widen the exact-eight implementation manifest.

Protected paths:

- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Operator authorization: standing dependency-ordered roadmap continuation and
the dispatcher/reviewer obligation to repair an in-scope gate failure.

Rollback boundary: revert only this packet correction and its generated
authority-hash projections if rejected; do not revert accepted RFR-R1-R4 work.

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: no Foundation storage, registry, database or
generated aggregate owner is created or moved.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: R5 is a named-source runtime hardening task, not a
legacy absorption or corpus-completeness tranche.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | governed F9 -> existing execution/isolation owners |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` plus local source verification |
| Owner surface | Safety Runtime and Runtime Adapter Hub |
| Disposition | ADAPT bounded verified delta; no external source authority |
| Claim boundary | external question is input only; this packet and local proof govern work |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/orchestrator |
| Provider or surface | repository-local coding agent surface |
| Session or invocation | RFR-R5 dispatch authoring at `0ee6e76b6` |
| Working directory | repository root |
| Command or tool surface | read-only source inspection, hashes, local tests, ADIF resolver, patch authoring |
| Target paths | paired R5 baseline and work order |
| Allowed scope source | runtime findings roadmap plus standing operator continuation |
| Before status evidence | HEAD `0ee6e76b6`; worktree clean before dispatch authoring |
| After status evidence | paired dispatch documents pending commit |
| Diff evidence | `git diff --name-status` before dispatch commit |
| Approval boundary | fresh R5 dispatch only; worker exact-eight no-commit scope |
| Claim boundary | repo-local trace only; no hidden cross-agent or external-runtime claim |
| Agent type | dispatcher/orchestrator |
| Invocation ID | `rfr-r5-dispatch-2026-08-24` |
| Expected manifest | paired baseline/work order, then separate continuity sync |
| Actual changed set | reviewer records before commit |
| Manifest delta | must be zero at dispatch commit |
| Deletion or rename disposition | N/A with reason: none authorized |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local typed isolation admission and deterministic proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: local `SandboxResult` isolation evidence only; no external receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local deterministic test results only |
| invocationBoundary | existing Safety Runtime contract and WorkerThread adapter |
| interceptionBoundary | no IDE, shell, git, provider or filesystem interception claim |
| claimLanguage | unsupported security-boundary requirements reject before worker execution |
| forbiddenExpansion | no physical containment, container, provider/live, deployment, public or production claim |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: existing owners can express truthful dimensional
admission, but `worker_threads` cannot satisfy a default security boundary.

Evidence Comparison Requirement: worker compares actual profiles, rejection
timing, environment probe and test results against this prediction.

Contradiction Handling Requirement: any actual enforceable dimension or owner
conflict requires a Contradiction Or Gap Disposition and no overclaim.

Claim Update Requirement: worker records whether F9 was confirmed, revised,
narrowed or blocked; reviewer alone closes it.

## Return-To-Orchestrator Conditions

Return only for hash/scope contradiction, necessary ninth path/new owner,
unavailable proof that prevents honest completion, installation/external effect,
or security design contradiction. In-scope failures are repaired autonomously.

## Operator Checkpoint

No checkpoint is required inside exact R5 scope. R6 remains parked until R5 is
independently accepted and continuity releases a fresh dispatch.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private remediation dispatch; no public-sync action is authorized.

## Claim Boundary

This work order authorizes exact-eight local implementation and proof only. It
does not claim physical isolation, live/provider behavior, production security,
deployment, public export, R6 release, or permission for the worker to commit.
