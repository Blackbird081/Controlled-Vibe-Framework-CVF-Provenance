# CVF Agent Work Order - GC010 SCR R2 T1G Pending Agent Execution Canonical Approval Hash Fail-Closed Reissue Non-Production Implementation

Memory class: governed-worker-dispatch
docType: work_order
Status: DISPATCH_READY
Batch ID: GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION
Dispatch base head: 6801859bd
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
closureBaseHead: REVIEWER_TO_SET
providerExecutionAuthority: FORBIDDEN
Commit mode: WORKER_MUST_NOT_COMMIT
Worker: delegated worker
Reviewer/closer: orchestrator/reviewer
Worker return path: `docs/reviews/CVF_GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-08-31.md`

## Dispatch Prompt Envelope

Role: delegated worker for GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION_2026-08-31.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: Dispatch authored 2026-08-31 from clean base `6801859bd`; worker must capture its own full execution base.

Do-not-misread notes: T1F selected a bounded contract, not production release. This packet permits exactly four implementation/test paths plus one worker return; it does not permit route-source, store, pending-core, SQLite-source, package/export, provider/live, distributed or production changes.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, the paired GC-018 baseline, and all checker source listed in the Checker Source Read-Ahead Block before writing any artifact.

Return contract: create the worker return artifact, run required gates, leave changes uncommitted (if WORKER_MUST_NOT_COMMIT), and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Implement and prove the T1F-selected canonical approval-request hashing and
fail-closed legacy reissue contract. Repair only the exact four approved
source/test paths, remove the T1E JSON round-trip mask, preserve all parked
boundaries, and return the five-path worker diff uncommitted for independent
review.

## Authority Chain

- T1E blocked material: `d367ea1c7`.
- T1F accepted decision: `52a84fecf` over dispatch `648063886`.
- T1F closure continuity and current dispatch base: `6801859bd`.
- Frozen prerequisite terminal:
  `CANONICAL_APPROVAL_REQUEST_HASH_FAIL_CLOSED_REISSUE_READY_FOR_BOUNDED_IMPLEMENTATION`.
- Operator continuation on 2026-08-31 authorizes this T1G dispatch; it does not
  authorize automatic T1H or production integration.

## Agent Roles

| Role | Owner | Permission |
| --- | --- | --- |
| Operator | operator | T1G continuation and any future scope expansion |
| Dispatcher | orchestrator | author and commit baseline/work order only |
| Worker | one internal delegated worker | exact four implementation/test paths plus worker return; no commit |
| Reviewer/closer | orchestrator/reviewer | independent diff/test review, bounded repair, material closure and separate continuity |

## Intake Role Routing Decision

- Intake summary: implement the accepted local canonical approval hash correction.
- Scope classification: BOUNDED_INTERNAL_NON_PRODUCTION_IMPLEMENTATION.
- Risk sensitivity: elevated because approval identity gates resume authority and persisted state.
- Selected role route: routeMode=MULTI_AGENT_MULTI_ROLE.
- Role separation basis: dispatcher freezes contract; one worker implements without commit; independent reviewer reproduces and closes.
- Escalation condition: source contradiction, forbidden path need, dual-read/migration requirement, external effect, or proof unavailable within scope.
- Canonical route mode: MULTI_AGENT_MULTI_ROLE.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION --title "GC010 SCR R2 T1G Pending Agent Execution Canonical Approval Hash Fail-Closed Reissue Non-Production Implementation" --date 2026-08-31 --base 6801859bd --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added T1F authority, exact owner/schema/hash contract, five-path worker changed set, focused proof matrix, dual-surface controls and stop boundaries. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| docOnlyNewFields | No new machine contract fields; descriptive approval projection and legacy proof rows only. |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |


## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION
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


## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T1F accepted decision material `52a84fecf` | Completion review selects approval-binding owner, exact projection/hash contract, fail-closed legacy policy and four-file future manifest | Preserve exact contract; stop and reopen Family D for any mixed-version continuity requirement | SATISFIED |

Author reminder: do not move this packet to DISPATCH_READY/DISPATCHED until every dependency row carries source-backed evidence.

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`bounded implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "bounded implementation" --role worker --lifecycle-phase pre-implementation` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE |
| Dispatch impact | No ADIF-specific amendment; canonical no-commit and independent-review controls remain mandatory. |

Author reminder: run the resolver command above for real before dispatch; list every defectId it actually returns.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status; repo-root source paths and real symbols; review convergence fields; handoff fields; worker-return profile; trace and delta rows; public disposition |
| gateRunPurpose | Confirm packet shape and evidence before pre-dispatch; gates are confirmation, not first discovery. |
| claimBoundary | Read-ahead covers governed artifact shape, not product correctness or runtime behavior. |

Author reminder: read every applicable checker source before writing the first governed line, then fill this block as confirmation evidence.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current builder emits optional own undefined and hashes insertion-sensitive JSON | source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | lines 21-43, 71-98 | `normalizeOptionalString`; `sortStringRecord`; `buildApprovalRequestSnapshot`; `computeApprovalRequestHash` | approval identity/hash owner | ACCEPT |
| Execute route recomputes hash and returns 409 on missing/mismatch | source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 177-237 | `approvalRequestHash`; mismatch response | execute approval resume boundary | ACCEPT |
| Pending claim fails closed on snapshot hash mismatch | source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | canonical projection lines 149-169; claim validation lines 879-883 | `canonicalizeJsonValue`; `claimPendingExecution` | T1A pending core | ACCEPT |
| Raw builder blocker is currently masked by JSON stringify/parse | test evidence | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.test.ts` | lines 266-286 | `buildApprovalRequestSnapshot`; blocker regression | T1E local harness proof | ACCEPT |
| Selected implementation, legacy and rollback contract | accepted decision | `docs/assessments/CVF_GC010_SCR_R2_T1F_PENDING_AGENT_EXECUTION_APPROVAL_SNAPSHOT_DURABLE_COMPATIBILITY_CORRECTION_DECISION_2026-08-31.md` | lines 100-203 | Family A selection and four-path manifest | T1F decision | ACCEPT |
| Independent decision closure | accepted review | `docs/reviews/CVF_GC010_SCR_R2_T1F_PENDING_AGENT_EXECUTION_APPROVAL_SNAPSHOT_DURABLE_COMPATIBILITY_CORRECTION_DECISION_COMPLETION_2026-08-31.md` | Findings / Position; Risk / Corrective Action; Decision / Recommendation / Disposition | closed-pass terminal and exact manifest | T1F reviewer | ACCEPT |

Author reminder: every claimed item needs a real source file and line/section; do not leave placeholder rows in the dispatched artifact.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| New binding test and worker-return path existence | `Test-Path -LiteralPath <exact-path>` returned `False` for each before dispatch | ABSENT_CONFIRMED |
| T1G token search before packet authoring | `rg -n "GC010-SCR-R2-T1G|CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION" docs CVF_SESSION -g '*.md' -g '*.json'`; only current next-move authority existed | EXPECTED_AUTHORITY_ONLY |
| Existing owner and regression paths | Exact three existing paths intentionally collide with T1F-approved edit manifest; new binding test does not collide. | PROCEED_BOUNDED |

Author reminder: run the searches for real before dispatch; do not leave placeholder rows.

## Required First Reads

1. Startup bootstrap, `CVF_SESSION_MEMORY.md`, and active handoff.
2. Guard orientation and governed literal-format gotchas.
3. Paired T1G baseline and this work order.
4. T1F assessment, worker return and completion review.
5. Every source/test path in Source Verification and the exact four-path edit
   manifest.
6. Applicable checker source before writing the worker return.

## Pre-Flight Checks

- Capture full `git rev-parse HEAD` as `executionBaseHead` and actual
  `git status --short --untracked-files=all`.
- Require a clean tree and absent new binding-test/worker-return paths.
- Run pre-implementation from the captured base before product edits.
- Reverify source symbols and exact changed-set ownership.
- Stop for dirty overlap, missing source, contract contradiction, forbidden
  path need, or a requirement for mixed-version/dual-read continuity.

## Scope

In scope: exact approval snapshot projection and hash correction; one new
binding test; existing route and harness regression edits; deterministic
offline focused tests, unchanged adjacent regressions, TypeScript and local
governance evidence.

Out of scope: approval route/store source; execute route source; pending core;
SQLite store/composition; local harness source; package/barrel/export;
registration/script/workflow/config; record rewrite or migration; hash version
field or dual-read; provider/audit/MAO/execution plane; live/network/browser/
credentials; public sync; deployment; distributed or production behavior.

## Write Ownership

Worker may change exactly four implementation/test paths plus one worker return:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.test.ts`
5. `docs/reviews/CVF_GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-08-31.md`

No deletion, rename, staging or commit is allowed.

## Canonical Approval Projection And Hash Contract

Recognized root projection keys are exactly:

`actorAuthMode`, `actorId`, `actorOrgId`, `actorTeamId`, `cvfPhase`,
`cvfRiskLevel`, `inputs`, `intent`, `knowledgeCollectionId`, `model`,
`provider`, `templateId`, `templateName`.

- `templateId`, `templateName` and `intent` remain required normalized strings.
- Root and nested `inputs` keys use ordinal UTF-16 comparison with `<`/`>`;
  `localeCompare` is forbidden.
- Builder omits every optional field normalized to `undefined`; defined
  schema-nullable values retain explicit `null`.
- Hash input must be a plain exact recognized shape. Reject unknown own keys,
  own `undefined`, symbol keys or values, accessors, non-plain objects and
  type-invalid values.
- Project once, compact-serialize once with `JSON.stringify`, encode UTF-8,
  and compute lowercase hexadecimal SHA-256.
- Semantically identical insertion-order variants must hash identically.

## Legacy, Forward And Rollback Contract

- Missing hash retains the existing 409 reissue receipt.
- A manually seeded legacy order-sensitive hash for the same semantic request
  returns the existing mismatch 409 and invokes no provider.
- No old-hash fallback, dual acceptance, silent rewrite or migration occurs.
- An old CREATED pending row that fails recomputation becomes `STALE` with
  `STALE_APPROVAL_SNAPSHOT_HASH_MISMATCH`; a non-CREATED row receives no new
  grant or execution authority.
- Forward and rollback posture is fail-closed reissue. If uninterrupted
  mixed-version availability, bidirectional continuity or record migration is
  required, stop T1G and reopen a separate Family D decision.

## Required Focused Test Matrix

| Case | Required observable proof |
| --- | --- |
| Builder omission | raw builder output has no own property whose value is `undefined`; explicit schema-nullable `null` is retained |
| Ordinal projection | root and `inputs` key order use ordinal comparison and do not depend on locale |
| Deterministic hash | insertion-order variants of the same recognized data have the same digest |
| Hash boundary rejection | unknown keys, own undefined, symbols, accessors, non-plain objects and invalid types throw/fail closed |
| Legacy digest | old order-sensitive digest differs and is never accepted as current |
| Execute exact match | canonical current request resumes without 409 |
| Execute legacy/missing | existing 409 reissue/mismatch receipts; provider invocation count exactly zero |
| Raw harness lifecycle | remove JSON parse/stringify mask; raw builder reaches versions 0/1/2/3 and durable reopened terminal equality |
| Old pending row | CREATED mismatch becomes named STALE reason; non-CREATED receives no new grant |
| Unchanged regressions | approval/store, T1A pending core and T1C SQLite suites plus TypeScript pass |

## Execution Plan

1. Capture clean execution base, run pre-implementation, and verify all sources.
2. Implement the exact projection/validation/hash boundary in approval-binding.
3. Add the new focused binding test and update only the two approved regression tests.
4. Run focused suites and TypeScript; repair only inside the four edit paths.
5. Scaffold and complete the worker return, run return gates, and stop uncommitted.

Each step stops immediately if completion needs any forbidden path or effect.

## Acceptance Criteria

- Exact five-path worker changed set and no staged/committed worker changes.
- Canonical projection/hash and all fail-closed legacy rules pass focused proof.
- Raw harness test proves lifecycle versions 0/1/2/3 and durable reopen without
  the prior JSON round-trip mask.
- Unchanged adjacent regressions and `npx tsc --noEmit` pass.
- No package/export, route-source, provider/live or production behavior changes.
- External/provider/network/browser/credential invocation counts are zero.
- Worker returns exactly `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Fail conditions: source contradiction; forbidden changed path; dual-read or
migration need; provider/live call; test failure not repairable within scope;
dirty overlap; staging or commit.

## Dual Agent Surface Matrix

| Surface | Dispatch | Authority / boundary |
| --- | --- | --- |
| `INTERNAL_AGENT` | SELECTED | One internal worker implements and returns uncommitted evidence. |
| `EXTERNAL_AGENT_CLI_MCP` | NOT_USED | No external CLI/MCP/provider invocation is authorized. |
| Adapter boundary | NOT_APPLICABLE_WITH_REASON | T1G edits local approval/test surfaces only and creates no adapter. |

## Evidence Reuse And Encoding Plan

priorEvidenceReuse: T1F decision facts and T1E blocker are reused only at their exact committed paths and are reverified against current source.

freshEvidenceRequired: execution HEAD/status, source symbols, focused tests, TypeScript, exact diff, worker-return gates and zero-call receipt.

encodingDisposition: preserve UTF-8 repository text; SHA-256 preimage encoding is explicitly UTF-8.

claimBoundary: prior receipts do not substitute for fresh T1G implementation proof.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | local source verification only; no external intake admitted |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired T1G baseline/work order and T1F accepted review |
| Disposition | NO_EXTERNAL_INTAKE_THIS_TRANCHE |
| Claim boundary | sub-agent audit is reviewer input, not external source authority |

## Epistemic Process Block

Epistemic Process Applicability: EVIDENCE_LIGHT

Expected Result / Prediction: the T1F-selected projection removes own
undefined and ordering drift while preserving fail-closed legacy receipts.

Evidence Comparison Requirement: worker return compares focused and durable
results to that prediction.

Contradiction Handling Requirement: any mixed-version or owner contradiction
requires a Contradiction Or Gap Disposition and `BLOCKED_WITH_REASON`.

Claim Update Requirement: worker return records confirmed, narrowed, revised
or invalidated status without opening a successor tranche.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> one implementation worker -> independent reviewer/closer -> session-sync steward |
| phase | implementation pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=6801859bd; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | worker exact four implementation/test paths plus one worker return; reviewer may repair only those material paths |
| traceScope(phase, actor) | worker records execution base, commands, exact diff/status and zero external calls; reviewer records independent reproduction and closure range |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | No unrelated dirty path may be absorbed; stop for overlap. |
| nextMoveSurfaces | Reviewer/closer updates active handoff and generated session state only in a separate continuity commit. |


## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION_COMPLETION_2026-08-31.md` (optional; prefer repairing evidence in the worker return per gotcha 30) |
| reviewerOwnedClosurePaths | optional named completion review plus bounded repairs inside the worker five-path manifest; continuity is separate |
| closureOwner | orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |


## Worker Output Checker Read-Ahead Mandate

Before writing each worker-owned output artifact, read checker source for that file's docType, path family, and conditional content class.

| Output artifact | Required read-ahead result |
| --- | --- |
| worker return under `docs/reviews/` | derive exact review headings, worker-return quality terms, trace labels, delta boundary labels, corpus/value/rescan tokens, and no-commit evidence shape before writing |
| companion reference under `docs/reference/` | derive exact reference headings such as Scope / Applies To, Target / Source, source verification, corpus/value/rescan, trace, and claim-boundary labels before writing |

Literal-shape reminders: do not list required headings as backticked `## ...` strings before the real section; write source-not-found disposition spelling instead of the exact blocked enum in literalTokensReviewed; avoid `after ... closure` wording unless a dependency-release row cites the accepted artifact path and commit.

## Planned Artifact Manifest

| Artifact | Required worker action |
| --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | implement exact projection, validation and canonical hash |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.test.ts` | create focused contract and adversarial tests |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts` | add exact-match plus missing/legacy 409 zero-provider regressions |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.test.ts` | remove JSON round-trip mask; prove raw lifecycle/durable/legacy behavior |
| `docs/reviews/CVF_GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-08-31.md` | record checker-safe uncommitted return and exact receipts |

## Required Artifact Manifest

| Required artifact | Owner | Dispatch state |
| --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | worker/reviewer | EXISTING_EDIT_REQUIRED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.test.ts` | worker/reviewer | NEW_PLANNED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts` | worker/reviewer | EXISTING_EDIT_REQUIRED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.test.ts` | worker/reviewer | EXISTING_EDIT_REQUIRED |
| `docs/reviews/CVF_GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-08-31.md` | worker | NEW_PLANNED |


## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "GC010-SCR-R2-T1G",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["docs/baselines/", "docs/work_orders/", "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/", "docs/reviews/"],
  "claims": ["canonical approval-request hash compatibility correction"],
  "requiredProof": ["exact projection tests", "legacy 409 zero-provider proof", "durable versions 0/1/2/3 reopen", "TypeScript and unchanged regressions"],
  "operatorCheckpoints": ["independent review before T1E acceptance or successor dispatch"],
  "forbiddenEffects": ["dual-read migration", "package export", "provider/live", "public/deploy/production"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": "N/A with reason: bounded named committed files only",
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, `P3_ELEVATED`, selective execution false,
`RUN_FULL_LEGACY_BUNDLE`.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-08-31.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Claim Boundary; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package.

Use `N/A with reason` for every non-applicable conditional block.

The review artifact must include actual headings satisfying all five review
families: Purpose; Target / Source; Scope / Methodology; Findings / Position;
Risk / Corrective Action; Decision / Recommendation / Disposition. It must
also include Responds-to, worker self-declaration, Changed Files, actual
`git status --short --untracked-files=all`, and No-Commit Declaration.

Shape-list rule: when listing required worker-output sections, write section names without the `##` prefix. Reserve actual heading syntax for real sections so structural checkers do not treat this checklist as the artifact section body.


## Verification Commands

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/app/api/approvals/approval-binding.test.ts src/app/api/approvals/approvals.c4.test.ts src/app/api/approvals/store.test.ts src/app/api/execute/route.test.ts src/lib/server/pending-agent-execution-local-harness.test.ts src/lib/pending-agent-execution.test.ts src/lib/pending-agent-execution-sqlite-store.test.ts
npx tsc --noEmit
Set-Location ../../..
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_worker_return_quality_gate.py --enforce
git diff --check
git diff --name-status
git status --short --untracked-files=all
```

Do not run the release gate, live/provider tests, broad network-dependent tests,
browser automation, package installation, or commands that read credentials.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatch author / orchestrator |
| Provider or surface | internal orchestrator surface |
| Session or invocation | GC010_SCR_R2_T1G_PENDING_AGENT_EXECUTION_CANONICAL_APPROVAL_HASH_FAIL_CLOSED_REISSUE_NON_PRODUCTION_IMPLEMENTATION GC010 SCR R2 T1G Pending Agent Execution Canonical Approval Hash Fail-Closed Reissue Non-Production Implementation, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | read-only source inspection, scaffold helper, patch editing, ADIF resolver and governance gates |
| Target paths | paired T1G baseline and work order |
| Allowed scope source | operator continuation on 2026-08-31, T1F accepted material `52a84fecf`, active next-move authority |
| Before status evidence | clean worktree at HEAD `6801859bd` before packet authoring |
| After status evidence | exactly paired T1G baseline/work order pending before dispatch commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | Dispatch authoring only; worker implementation begins only from committed packet and captured execution base. |
| Claim boundary | Repo-local trace; no OS identity, hidden-memory transfer, provider or runtime claim. |
| Agent type | INTERNAL_AGENT dispatcher |
| Invocation ID | `gc010_scr_r2_t1g_pending_agent_execution_canonical_approval_hash_fail_closed_reissue_non_production_implementation-2026-08-31` |
| Expected manifest | paired T1G baseline and work order |
| Actual changed set | paired T1G baseline and work order at dispatch review |
| Manifest delta | NONE_EXPECTED |


## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | bounded local approval-binding and regression-test implementation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: committed T1F decision plus future focused test/worker-return receipts |
| actionEvidence | ACTION_EVIDENCE_PRESENT: exact diff, command output and no-commit status required |
| invocationBoundary | local file editing and deterministic offline tests only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized unless replaced with real evidence. |
| claimLanguage | T1G may correct and test canonical approval identity locally; it does not release a production consumer. |
| forbiddenExpansion | No route source/store/pending/SQLite source, migration, dual-read, package/export, provider/live, public, distributed, deployment or production expansion. |


## Work-Order Fulfillment Manifest

| Requirement | Evidence owner | State at dispatch |
| --- | --- | --- |
| Canonical exact projection and hash boundary | binding source plus new focused test | PLANNED |
| Exact-match and legacy/missing 409 behavior | execute-route regressions | PLANNED |
| Raw builder lifecycle versions 0/1/2/3 and reopen | harness regression | PLANNED |
| Unchanged approval/pending/SQLite and TypeScript | command receipts | PLANNED |
| Exact five-path diff, zero external calls, no commit | worker return | PLANNED |

## Evidence Requirements

Worker return records initial/final full HEAD and actual status; exact changed
files; source-verification deltas; focused per-file test counts; TypeScript;
legacy 409 provider-call count; raw lifecycle/reopen assertions; diff hygiene;
worker-return gates; zero provider/network/browser/credential calls; and the
no-commit declaration. Historical T1F receipts are authority, not substitute
proof.

## Commit Prompt Readiness

Commit owner: reviewer/closer only.

Worker commit permission: FORBIDDEN.

Expected worker changed paths: exact four implementation/test paths plus one
worker return listed in Write Ownership.

Forbidden touched paths: NONE_EXPECTED.

The reviewer must inspect and reproduce evidence before any material commit;
mode/next-move continuity must be a later separate commit.

## Review Gate

Implementation begins only after committed T1G dispatch and a passing
pre-implementation gate. Worker handoff is never closure. Reviewer must inspect
the complete dependency class once, reproduce focused tests and TypeScript,
verify exact manifest/legacy/zero-call boundaries, run reviewer-return gates,
and either accept bounded, repair inside allowed paths, or return one
consolidated blocker set.

## Closure Checklist

- [ ] Exact four implementation/test paths plus one worker return only.
- [ ] Canonical projection, rejection and deterministic hash tests pass.
- [ ] Current resume and legacy/missing fail-closed route tests pass with zero provider call.
- [ ] Raw harness versions 0/1/2/3, terminal identity and durable reopen pass.
- [ ] Adjacent unchanged regressions and TypeScript pass.
- [ ] Worker-return gates, diff hygiene, actual status and no-commit evidence pass.
- [ ] Independent reviewer accepts and commits material before separate session sync.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` without expanding scope for dirty overlap, missing
source, owner/contract contradiction, required forbidden path, dual-read or
migration need, provider/live requirement, or proof unavailable after
allowed-scope repair. Otherwise return `COMPLETE_PENDING_REVIEW` and stop.

## Stop Conditions

Stop immediately after the uncommitted worker return. Do not stage, commit,
update continuity, accept T1E, open package/route/provider/production work, or
author a successor tranche.

## Legacy Absorption Coverage Index Disposition

| Field | Value |
| --- | --- |
| coverageIndexApplicability | NOT_APPLICABLE_WITH_REASON |
| reason | T1G implements a current local TypeScript contract and absorbs no legacy corpus or external artifact. |
| coverageIndexPath | N/A with reason: no legacy absorption packet exists. |
| claimBoundary | T1E legacy-hash compatibility is product regression scope, not knowledge-corpus absorption. |

## Finding-To-Governance Learning Disposition

NOT_APPLICABLE_WITH_REASON: T1G implements the accepted T1F correction; any
new recurring defect class discovered by reviewer is separately routed and
does not widen this worker scope.

## Operator Checkpoint

After the worker return, stop for independent review. T1E acceptance, package
export, route/provider/audit integration, production consumer, distributed
safety, public sync, deployment and any successor tranche require reviewer
closure plus fresh operator continuation.

## Claim Boundary

This work order authorizes only the exact four implementation/test paths plus
one worker return for a non-production canonical approval hash correction. It
does not itself accept T1E, release a package export or caller, alter
route/provider/audit behavior, migrate records, support distributed safety, or
authorize public, deployment, live or production claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch and bounded non-production implementation;
no public-sync artifact or export authority is included.
