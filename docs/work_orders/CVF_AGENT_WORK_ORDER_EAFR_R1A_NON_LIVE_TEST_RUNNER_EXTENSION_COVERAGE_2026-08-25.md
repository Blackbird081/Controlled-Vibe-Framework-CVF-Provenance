# CVF Agent Work Order - CVF EAFR-R1A Non-Live Test Runner Extension Coverage

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: EAFR-R1A-NON-LIVE-TEST-RUNNER-EXTENSION-COVERAGE

Dispatch base head: bb49266fd

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: delegated worker

Reviewer/closer: independent orchestrator/reviewer/closer

Worker return path: `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_WORKER_RETURN_2026-08-25.md`

## Dispatch Prompt Envelope

Role: delegated worker for EAFR-R1A-NON-LIVE-TEST-RUNNER-EXTENSION-COVERAGE.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_2026-08-25.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-08-25; dispatch parent is accepted-material commit `bb49266fd09bea5c2252520d838526d5d8f13086`.

Do-not-misread notes: this is a deterministic package-script repair. It does not authorize `test:live`, a provider call, credential access, network use or re-running the incident test.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the worker return artifact, run required gates, leave changes uncommitted (if WORKER_MUST_NOT_COMMIT), and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Make all three cvf-web test scripts extension-complete: non-live run and coverage
must exclude both tracked live-test extensions, while the explicit live runner
must include both. Add a static regression proving this boundary without
executing live tests or resolving provider credentials.

## Allowed Scope

Allowed paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/package-test-script-boundary.test.ts`
- `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_WORKER_RETURN_2026-08-25.md`

Allowed actions: update only the three npm script strings, add one deterministic
static test, run the commands below and write the worker return. The worker must
not edit any live test, route, provider adapter, environment file, credential,
Vitest configuration, dependency manifest field outside `scripts`, R1 source,
governance checker or session surface.

## Implementation Requirements

1. `test:run` must exclude both `src/**/*.live.test.ts` and
   `src/**/*.live.test.tsx`.
2. `test:coverage` must exclude the same two patterns.
3. `test:live` must explicitly include both patterns and retain
   `--fileParallelism=false`.
4. The new static test must parse `package.json`, assert all three exact script
   properties, enumerate the current tracked live-test suffixes without
   importing or executing those files, and prove the observed extension set is
   exactly `ts` and `tsx`.
5. Do not invoke `test:live`; do not load `.env.local`; do not inspect whether a
   key exists; do not call provider/network surfaces.
6. Preserve all other package fields and scripts byte-semantically.

## Acceptance Criteria

- [ ] all three script-boundary requirements are asserted by the focused test;
- [ ] the focused static test passes with provider environment variables
  cleared for the command process;
- [ ] Vitest static list with both excludes contains zero path matching
  `.live.test.ts` or `.live.test.tsx`;
- [ ] package JSON parses and only the `scripts.test:run`,
  `scripts.test:coverage`, and `scripts.test:live` values change;
- [ ] exact three-path manifest, empty staging and no commit;
- [ ] worker-return fast gate passes;
- [ ] zero live/provider/network call or credential read occurs.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R1A",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": [
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/package-test-script-boundary.test.ts",
    "docs/reviews/",
    "docs/baselines/CVF_GC018_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_2026-08-25.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_2026-08-25.md",
    "AGENT_HANDOFF_V59_2026-08-11.md",
    "CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json",
    "CVF_SESSION/ACTIVE_SESSION_STATE.json",
    "CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json",
    "CVF_SESSION/state/entries/nextAllowedMove.json",
    "CVF_SESSION_MEMORY.md"
  ],
  "claims": ["non-live scripts exclude every currently tracked live-test TypeScript extension"],
  "requiredProof": ["static package-script regression", "non-executing Vitest file list", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["worker stage or commit", "live test execution", "provider/network call", "credential access", "route or adapter edit", "deployment", "public write"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R1A-NON-LIVE-TEST-RUNNER-EXTENSION-COVERAGE --title "CVF EAFR-R1A Non-Live Test Runner Extension Coverage" --date 2026-08-25 --base bb49266fd --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders; added exact manifest, source/hash authority, deterministic acceptance and no-live commands |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| docOnlyNewFields | `trackedLiveTestExtensions`; `incidentEvidenceDisposition`; `repeatLiveAuthority` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |


## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| EAFR-R1 accepted material blocked by live-test activation incident at bb49266fd | committed completion review at `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md` | accepted R1 material and mandatory R1A route exist at committed HEAD | RELEASED_FOR_R1A_ONLY |

Author reminder: do not move this packet to DISPATCH_READY/DISPATCHED until every dependency row carries source-backed evidence.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-execution`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-execution --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF constraint beyond the governing packet |

Author reminder: run the resolver command above for real before dispatch; list every defectId it actually returns.

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | external finding -> governed CVF source verification -> bounded first-party repair |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; pre-dispatch autorun |
| Owner surface | EAFR-R1 completion review and this EAFR-R1A work order |
| Disposition | ADAPT as a CVF-owned deterministic package-script boundary repair |
| Claim boundary | external-agent material is input only; the committed R1 review and repository-local package/test inventory provide the authority and evidence for this dispatch |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; executionBaseHead; Source Verification columns; Worker Return Packet Shape Contract; Agent Operation Trace Block |
| gateRunPurpose | confirm final work-order shape before pre-dispatch, not discover requirements |
| claimBoundary | checker read-ahead proves packet conformance only; it does not prove test selection or zero external effect |

Author reminder: read every applicable checker source before writing the first governed line, then fill this block as confirmation evidence.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| current package script boundary is extension-incomplete | PACKAGE_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts block | `scripts` | npm package scripts | ACCEPT |
| current tracked live-test extension set contains TS and TSX | TEST_SOURCE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.gc009-live-t5-mandatory-gateway.alibaba.live.test.tsx` | file identity and live-call ceiling | `ALIBABA_API_KEY` | Vitest live acceptance file | ACCEPT |
| R1 closure is blocked pending this repair | REVIEW_SOURCE | `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md` | final position and Machine Closure Package | `R1-F8` | EAFR reviewer decision | ACCEPT |

Author reminder: every claimed item needs a real source file and line/section; do not leave placeholder rows in the dispatched artifact.

## Authority Chain

1. `ECOSYSTEM/doctrine/` frozen governance.
2. Root `AGENTS.md` and active CVF standards.
3. `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`.
4. `docs/reviews/CVF_EAFR_R1_AIF_REINJECTION_PROVENANCE_FAIL_CLOSED_COMPLETION_2026-08-25.md` at commit `bb49266fd`.
5. Paired R1A baseline and this work order.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| operator | standing roadmap authority; no routine checkpoint required |
| orchestrator/dispatcher | owns packet, scope and dependency release |
| worker | implements exact three-path manifest; no stage or commit |
| reviewer/closer | independently verifies and decides R1/R1A reconciliation |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | correct a package test-selection boundary exposed during R1 review |
| scope classification | BOUNDED_TEST_INFRASTRUCTURE_SAFETY_REPAIR |
| primary task class | implementation |
| risk sensitivity | HIGH because the defect can consume provider quota |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| orchestration requirement | one no-commit worker plus independent reviewer/closer |
| role separation basis | worker cannot accept its own external-effect boundary repair |
| escalation condition | live activation, credential read, wider script/config need, source contradiction or forbidden edit |

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`, `CVF_SESSION_MEMORY.md` and the active handoff.
- `docs/reference/guard_orientation/README.md` and the literal-format gotchas standard.
- EAFR roadmap, paired R1A baseline, this work order and the R1 blocked completion review.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` in full.
- the named live TSX file only as read-only source; do not import or execute it.
- worker-return checker sources required by the Worker Output Checker Read-Ahead Mandate.

## Pre-Flight Checks

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
Get-FileHash -Algorithm SHA256 -LiteralPath 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json'
$eafrR1aExecutionBase = git rev-parse HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $eafrR1aExecutionBase --head HEAD
```

Stop before editing if the worktree is not clean, the package hash is not
`60358c01e39d962ce64a78bdad5eddd6a6690057f461d2c71a0355d1fa465ed1`,
or current script/live-extension facts contradict the paired baseline.

## Write Ownership

Write ownership is exactly the three paths in Allowed Scope. The worker may
read other named authority/source files but must not edit, stage or commit
anything outside that manifest.

## Execution Plan

1. Capture the clean execution base and verify the package hash.
2. Read package scripts and enumerate live-test suffixes without importing tests.
3. Update only the three named script values.
4. Add the static regression test and run focused proof with provider variables cleared for the process.
5. Run the non-executing static list, inspect exact diff/status, create the worker return and run its full fast gate.

## Evidence Requirements

- before/after package SHA-256 and semantic diff limited to three scripts;
- tracked live-test count and exact extension set;
- focused test count and command cwd;
- static-list proof with zero live-test path;
- secret-safe statement that no environment file/key was read and no provider/network call occurred;
- exact three-path status, empty staging and unchanged worker HEAD.

## Current Runtime Freshness Verification

Current source inspection at dispatch found 34 tracked live-test files: 33 end
in `.live.test.ts` and one ends in `.live.test.tsx`. `package.json` currently
excludes/includes only the TS pattern. Worker must repeat suffix enumeration
without executing tests and return `BLOCKED_WITH_REASON` on contradiction.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| exclude TS and TSX from non-live runner | Implementation Requirements | `package.json` and static test | focused Vitest plus static file list | implementation pending |
| align coverage and explicit live runner | Implementation Requirements | three script values | static assertions | implementation pending |
| zero external effect | Claim Boundary | worker return incident statement | reviewer source/command audit | required |
| independent R1/R1A reconciliation | Review Gate | completion review | reviewer-return preflight | required |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: this is a first-party package test-runner boundary
repair, not legacy absorption, corpus intake or owner-map reassessment.

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: the tranche creates no durable governance
foundation, registry, index, split, relocation or storage layout. The only new
implementation file is one package-local static test.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for "CVF EAFR-R1A Non-Live Test Runner Extension Coverage" artifacts | both dispatch paths absent before scaffold creation | PASS |
| Token search for "CVF EAFR-R1A Non-Live Test Runner Extension Coverage" (2026-08-25) | `rg -n "EAFR-R1A-NON-LIVE-TEST-RUNNER-EXTENSION-COVERAGE" docs CVF_SESSION`; post-authoring results are limited to this paired packet | PASS |
| Collision decision | fresh R1A suffix and exact file paths | PROCEED |

Author reminder: run the searches for real before dispatch; do not leave placeholder rows.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | delegated no-commit worker followed by independent reviewer/closer |
| phase | R1A implementation pending |
| baseHeadFor(phase) | dispatchBaseHead=bb49266fd; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exact package.json, one new static test and one worker return |
| traceScope(phase, actor) | worker records deterministic commands and zero-external-effect evidence; reviewer independently verifies |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | R1 source/test remain committed and read-only; R2-R6, RFR, provider/live, public and deployment remain parked |
| nextMoveSurfaces | named R1A worker return, then reviewer reconciliation of R1 and R1A |


## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_COMPLETION_2026-08-25.md` |
| reviewerOwnedClosurePaths | R1A work order/baseline, worker return, completion review, EAFR roadmap and continuity surfaces |
| closureOwner | independent orchestrator/reviewer/closer |
| workerCommitPermission | FORBIDDEN |


## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews/` | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference under `docs/reference/` | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings as backticked `## ...` strings before the real section; write source-not-found disposition spelling instead of the exact blocked enum in literalTokensReviewed; avoid `after ... closure` wording unless a dependency-release row cites the accepted artifact path and commit.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | edit only the three named test script values |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/package-test-script-boundary.test.ts` | create deterministic static regression |
| `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_WORKER_RETURN_2026-08-25.md` | create full no-commit worker return |


## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R1A_NON_LIVE_TEST_RUNNER_EXTENSION_COVERAGE_WORKER_RETURN_2026-08-25.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Shape-list rule: when listing required worker-output sections, write section names without the `##` prefix. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.


## Verification Commands

```powershell
`$eafrR1aExecutionBase = git rev-parse HEAD`
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $eafrR1aExecutionBase --head HEAD
Push-Location 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web'
$env:ALIBABA_API_KEY=$null; $env:DASHSCOPE_API_KEY=$null; $env:CVF_BENCHMARK_ALIBABA_KEY=$null; $env:CVF_ALIBABA_API_KEY=$null
npm run test:run -- src/lib/package-test-script-boundary.test.ts
$listed = & .\node_modules\.bin\vitest.cmd list --filesOnly --staticParse --exclude "src/**/*.live.test.ts" --exclude "src/**/*.live.test.tsx"
if ($listed | Select-String -Pattern '\.live\.test\.tsx?$') { throw 'Live test present in non-live static list' }
Pop-Location
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short --untracked-files=all
```

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatch author / orchestrator |
| Provider or surface | private local repository |
| Session or invocation | EAFR-R1A-NON-LIVE-TEST-RUNNER-EXTENSION-COVERAGE CVF EAFR-R1A Non-Live Test Runner Extension Coverage, 2026-08-25 |
| Working directory | repository root |
| Command or tool surface | source enumeration, hashing, scaffold authoring and dispatch gates |
| Target paths | paired R1A baseline/work order |
| Allowed scope source | operator standing EAFR orchestration authority and committed R1 blocked review |
| Before status evidence | clean worktree at HEAD `bb49266fd09bea5c2252520d838526d5d8f13086` before dispatch authoring |
| After status evidence | paired dispatch docs only, pending dispatcher commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | deterministic R1A package-script repair dispatch only |
| Claim boundary | no implementation, live/provider/network, credential, public, deploy or production claim |
| Agent type | orchestrator/dispatch author |
| Invocation ID | `eafr-r1a-non-live-test-runner-extension-coverage-2026-08-25` |
| Expected manifest | paired R1A baseline and work order |
| Actual changed set | paired R1A baseline and work order |
| Manifest delta | NONE |


## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | dispatch authority and deterministic future test-script proof only |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, or mandatory-wrapper behavior is claimed unless replaced with real evidence. |
| receiptEvidence | N/A with reason: dispatch has no execution receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: implementation remains worker-pending |
| invocationBoundary | local authoring and static source verification only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized unless replaced with real evidence. |
| claimLanguage | no package behavior claim until worker evidence and independent review |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior without a fresh source-verified authorization. |


## Review Gate

Worker return is not closure. Reviewer must inspect script semantics, confirm
the static list cannot select a live test, independently run focused proof,
verify zero external effect, then decide whether R1 and R1A can close together.

## Closure Checklist

- [ ] exact three-path worker manifest and empty staging;
- [ ] all Acceptance Criteria satisfied;
- [ ] no live/provider/network/key/environment-file action;
- [ ] reviewer-return preflight passes;
- [ ] reviewer owns material commit and any continuity conversion.

## Operator Checkpoint

operator.checkpoint.waiver: standing operator delegation covers routine
deterministic R1A work and independent closure. It does not waive external
effect, scope expansion, secret access, public, deploy or destructive bounds.

## Claim Boundary

This work order authorizes only the exact three-path worker manifest and
deterministic commands above. It forbids `test:live`, live-test import or
execution, provider/network calls, API-key inspection/use, environment-file
reads, route/provider changes, dependency installation, build, deployment,
public sync, push and worker commit. Return only `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance repair dispatch; no public-sync action is authorized.
