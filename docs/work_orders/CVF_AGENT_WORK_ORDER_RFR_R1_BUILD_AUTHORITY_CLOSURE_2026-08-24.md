# CVF Agent Work Order - RFR-R1 Build Authority Closure

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-08-24

Batch ID: RFR-R1

## Dispatch Prompt Envelope

```text
Role: implementation worker. The current Codex agent is independent orchestrator/reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R1_BUILD_AUTHORITY_CLOSURE_2026-08-24.md
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: capture executionBaseHead from committed HEAD at worker start; dispatchBaseHead is e196899548d04f88ee5bc40cfce1ddf268a29d6b.
Current-time notes: only RFR-R1 is released; R2-R6, provider/live, deployment and public sync remain parked.
Do-not-misread notes: keep five runtime phases; SPEC and WORK ORDER are typed BUILD authority evidence, not new phases or new subsystems.
Required first actions: read startup and required sources; record HEAD/status; verify exact five-path manifest; run worker ADIF resolver.
Return contract: COMPLETE_PENDING_INDEPENDENT_REVIEW or BLOCKED_WITH_REASON with exact diff, test/gate evidence, residuals, empty staging and unchanged HEAD.
```

dispatchBaseHead: `e196899548d04f88ee5bc40cfce1ddf268a29d6b`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `NOT_EXECUTED_YET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Implement the RFR-R1 mandatory BUILD authority prerequisite inside the existing
Guard Contract and return uncommitted evidence for independent review.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "RFR-R1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "NEW_INTERFACE"
  },
  "pathFamilies": [
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/",
    "EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts",
    "docs/reviews/",
    "docs/baselines/",
    "docs/roadmaps/",
    "docs/work_orders/"
  ],
  "claims": ["mutating BUILD authority prerequisite inside the canonical Guard Contract"],
  "requiredProof": ["focused hostile tests", "full Guard Contract tests", "TypeScript typecheck", "full legacy gate", "independent review"],
  "operatorCheckpoints": ["R2 remains gated on accepted R1 closure"],
  "forbiddenEffects": ["provider or live call", "credential use", "deployment", "public write", "worker commit", "new subsystem"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

completionReviewPath: `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_COMPLETION_2026-08-24.md`

reviewerOwnedClosurePaths: `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_COMPLETION_2026-08-24.md`; `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md`; applicable continuity surfaces after material commit.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Implementation | Acceptance evidence | Disposition |
|---|---|---|---|
| mutating BUILD fail-closed | mandatory `build_authority` guard | direct and shared-engine negative tests | MAPPED |
| accepted SPEC | typed status/ref | missing/rejected/empty cases | MAPPED |
| valid WORK ORDER | typed status/ref/revocation/expiry | invalid/expired/revoked cases | MAPPED |
| bounded targets | explicit work-order file scope | missing/out-of-scope cases | MAPPED |
| no owner proliferation | reuse Guard Contract/action intent | reviewer source audit | MAPPED |

## Required First Reads

1. `AGENTS.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION_MEMORY.md`
4. `AGENT_HANDOFF_V59_2026-08-11.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. `docs/baselines/CVF_GC018_RFR_R1_BUILD_AUTHORITY_CLOSURE_2026-08-24.md`
8. `docs/roadmaps/CVF_RUNTIME_FINDINGS_CLOSURE_ROADMAP_2026-08-24.md`
9. this work order and every ACCEPT source path below

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator | 2026-08-24 remediation instruction | ACCEPT |
| verified defect | runtime findings review F1 | ACCEPT |
| ordered tranche | closure roadmap R1 | ACCEPT |
| implementation boundary | paired GC-018 and exact manifest | ACCEPT |

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | authorizes bounded R1 and copies packet to worker |
| Orchestrator/dispatcher | owns packet, sequencing and scope decisions |
| External implementation worker | edits five allowed paths, tests, returns evidence, never commits |
| Reviewer/closer | independently reviews, repairs in scope, commits accepted material |
| Session-sync steward | updates continuity only after accepted material commit |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact manifest. Return `BLOCKED_WITH_REASON` if
a sixth path, engine/gateway/MCP edit, authority issuer/storage, new dependency,
live call, or phase-model change becomes necessary. Do not stage, commit, push,
or ask permission to repair an in-scope test/gate failure.

## Pre-Flight Checks

- capture `git rev-parse HEAD` as `executionBaseHead`;
- record `git status --short` and require no pre-existing overlap;
- verify both proposed new guard files and worker return are absent;
- read all five allowed production/test paths before edit;
- run the ADIF resolver for worker/pre-execution context.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | close generic mutating BUILD prerequisite gap |
| scope classification | SECURITY_SENSITIVE_RUNTIME_AUTHORITY_IMPLEMENTATION |
| primary task class | bounded Guard Contract implementation |
| risk sensitivity | HIGH |
| selected role route | MULTI_AGENT_SINGLE_ROLE |
| orchestration requirement | external no-commit worker plus current independent reviewer |
| role separation basis | worker cannot accept its own authority-boundary code |
| escalation condition | need for broader owner, sixth path, new dependency, live/public action, or phase redesign |

## Allowed Scope

Worker may modify or create exactly:

1. `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`
2. `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/build-authority.guard.ts`
3. `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/build-authority.guard.test.ts`
4. `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`
5. `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_WORKER_RETURN_2026-08-24.md`

Read-only inspection and commands elsewhere are allowed. All other edits are
forbidden, including `engine.ts`, existing tests, package metadata, Gateway,
MCP, Web, governance checkers, roadmap, completion review, session state,
handoff, deployment, public-sync clone, staging and commit history.

## Write Ownership

Worker owns the exact five paths only. Reviewer owns completion review, roadmap
transition, material commit and later continuity update.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| request context is universal input | TYPE_OWNER | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | lines 89-110 | `GuardRequestContext` | Guard Contract types | ACCEPT |
| mandatory IDs drive disable/unregister protection | RUNTIME_OWNER | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | lines 41-64 | `unregisterGuard`; `disableGuard` | Guard runtime engine | ACCEPT |
| default factory registers canonical stack | COMPOSITION_OWNER | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | lines 380-392 | `createGuardEngine` | Guard Contract package root | ACCEPT |
| mutation intent has exact token semantics | CLASSIFIER_OWNER | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/action-intent.ts` | `hasModifyIntent` | tokenized modify classification | Guard Contract guards | ACCEPT |
| existing tests prove BUILD allow without new evidence | NEGATIVE_GAP | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.test.ts` | BUILD cases | Phase/Authority positive tests | Guard Contract tests | ACCEPT |
| F1 is accepted for remediation | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | F1 row | `RUNTIME_AUTHORITY_GAP` | governed review | ACCEPT |

## Required Implementation

### Typed evidence

Add a narrow exported type on `GuardRequestContext`, named consistently with
BUILD authority. It must represent:

- non-empty accepted SPEC reference and exact `ACCEPTED` status;
- non-empty WORK ORDER reference and exact `VALID` status;
- explicit revoked flag;
- optional ISO expiry;
- explicit list of allowed repo-relative file scopes.

Do not add file reads, signatures, issuer/storage behavior or untyped metadata
parsing. Invalid scalar/array values fail closed through typed evaluation and
runtime validation.

### Mandatory guard

Create `BuildAuthorityGuard` with ID `build_authority`, deterministic priority
between phase/authority admission and downstream budget/scope guards, and stable
reason-code metadata. It applies only when `phase === 'BUILD'` and
`hasModifyIntent(context.action)` is true.

It must block missing/invalid evidence, rejected SPEC, invalid/revoked/expired
WORK ORDER, absent allowed scope, or any target outside allowed scope. Matching
uses normalized repo-relative path segment boundaries: `src/app/` may cover
`src/app/a.ts` but not `src/application/a.ts`; absolute paths and parent
traversal do not match. If target files are missing for a mutating BUILD action,
fail closed.

It must allow only its own prerequisite when evidence is valid; it never grants
execution or overrides another guard.

### Factory and package boundary

Export the type and guard through the existing root, add `build_authority` to
`MANDATORY_GUARD_IDS`, and register it in `createGuardEngine()`. Preserve the
existing registration order except for the minimum new insertion and update no
unrelated public surface.

### Dedicated tests

The new test file must cover:

- non-BUILD, read-only BUILD and phase-transition non-applicability;
- missing evidence, rejected SPEC, empty refs, invalid status;
- missing target/scope, absolute/traversal scope, and segment-prefix collision;
- revoked, expired, invalid-timestamp and exact-boundary expiry;
- valid file and directory scope cases;
- shared factory registration, mandatory disable/unregister rejection;
- a full-engine mutation with valid `ai_commit` but missing BUILD authority is
  blocked by `build_authority`;
- valid BUILD authority does not reopen a block from another mandatory guard.

Use a controlled/fake clock input only if it fits the exact manifest; otherwise
construct expiry values around the evaluation time without flaky equality.

## Execution Plan

1. capture execution base and clean overlap evidence;
2. add typed evidence and guard with the smallest API delta;
3. export/register/mark mandatory;
4. author dedicated adversarial tests;
5. run focused, full, typecheck and governance gates; repair only in scope;
6. create the full-gate worker return and leave HEAD/staging unchanged.

## Required Artifact Manifest

| Path | Owner | Required state at worker return |
|---|---|---|
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | Worker | modified, typed evidence plus mandatory ID |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/build-authority.guard.ts` | Worker | new mandatory guard |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/build-authority.guard.test.ts` | Worker | new adversarial tests |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | Worker | modified export and factory registration |
| `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_WORKER_RETURN_2026-08-24.md` | Worker | new pending review packet |

Any sixth worker-changed path is a scope violation.

## Work-Order Fulfillment Manifest

| Requirement | Fulfillment path | Proof | Owner |
|---|---|---|---|
| typed authority evidence | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | typecheck and source review | Worker |
| mandatory runtime check | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/build-authority.guard.ts` | focused negative tests | Worker |
| composition | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | shared-engine tests | Worker |
| adversarial proof | `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/build-authority.guard.test.ts` | executed test report | Worker |
| pending evidence | worker-return path | worker fast gate | Worker |
| final decision | completion-review path | independent reviewer evidence | Reviewer |

## Acceptance Criteria

- exact five-path manifest and no deletions/renames;
- all required negative and positive cases execute;
- new guard is mandatory in shared composition;
- valid evidence never grants or widens another guard's decision;
- no new dependencies, I/O, storage, issuer, approval, gateway or phase model;
- focused/full tests, typecheck, file-size and return gates pass;
- staging empty and HEAD equals `executionBaseHead`.

## Verification Commands

Run from repository root and record exact results:

```powershell
Set-Location EXTENSIONS/CVF_GUARD_CONTRACT
npx vitest run src/guards/build-authority.guard.test.ts --pool forks
npm test
npm run check
Set-Location ../..
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --stat
git status --short
git diff --cached --name-only
git rev-parse HEAD
```

No provider or release-quality live proof is required because R1 makes no live
governance claim.

## Evidence Requirements

Record test counts/exits, typecheck exit, reason-code matrix, exact five-path
diff, base/HEAD equality, empty staging, no provider call, and residual risk.
Static inspection alone is insufficient.

## Acceptance Receipt Assertion Matrix

| Assertion | Evidence | Worker disposition |
|---|---|---|
| missing authority blocks | focused missing-field cases | PENDING_EXECUTION |
| invalid lifecycle blocks | rejected/revoked/expired cases | PENDING_EXECUTION |
| scope cannot widen | traversal/absolute/prefix collision cases | PENDING_EXECUTION |
| mandatory composition | factory and disable/unregister cases | PENDING_EXECUTION |
| denial cannot reopen | full-engine conflicting-guard case | PENDING_EXECUTION |
| compatibility preserved | full suite and typecheck | PENDING_EXECUTION |

## Review Gate

Worker success is pending evidence only. Reviewer must inspect every changed
line, rerun commands, add independent adversarial probes for malformed runtime
objects and scope normalization, verify no bypass through missing targets or
phase aliases, and only then accept or return a bounded repair.

## Machine Closure Package

| Surface | Worker action | Reviewer/closer action |
|---|---|---|
| source/tests | edit exact four paths | inspect and repair only in scope |
| worker return | create pending packet | verify, never treat as independent proof |
| completion review | no edit | create accepted/rejected decision |
| roadmap | no edit | close R1 and decide whether R2 may dispatch |
| session continuity | no edit | update separately after material commit |
| public sync | forbidden | remains parked absent explicit authorization |

## Closure Checklist

- [ ] exact five-path manifest
- [ ] worker HEAD unchanged and staging empty
- [ ] focused/full/typecheck gates pass
- [ ] independent adversarial review passes
- [ ] material commit made by reviewer only
- [ ] continuity sync separated
- [ ] R2 remains undispatched until explicit closure transition

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source contradiction, need for a sixth path,
unavailable executable tests, phase-model change, new dependency, or inability
to enforce path boundaries without an unowned subsystem.

## Operator Checkpoint

No mid-worker checkpoint is needed within scope. The operator reviews the
external worker return through the current orchestrator/reviewer. R2 requires
accepted R1 closure; no separate worker may begin it early.

## Worker Return Packet Shape Contract

The worker return must include plain headings for Purpose, Target / Source,
Scope / Methodology, Findings / Position, Risk / Corrective Action, Claim
Boundary, Checker Source Read-Ahead Block, Agent Operation Trace Block, Delta
Execution Claim Boundary Control Block, and Public Export Disposition. Include
compact N/A-with-reason blocks for conditional corpus, external intake,
finding-learning, epistemic, machine-closure and storage requirements.

Self-declared worker-return artifact: yes.

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | external implementation worker followed by current independent reviewer/closer |
| phase | RFR-R1 BUILD authority closure |
| baseHeadFor(phase) | dispatchBaseHead=`e196899548d04f88ee5bc40cfce1ddf268a29d6b`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`NOT_EXECUTED_YET` |
| changedSetScope(phase) | exact five-path Required Artifact Manifest |
| traceScope(phase, actor) | reads, edits, tests, gates, diff and return evidence |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no R2-R6, gateway, MCP, provider/live, deploy, public or session mixing |
| Before status evidence | worker captures committed base and overlap status |
| nextMoveSurfaces | worker return then independent review/closure |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_RFR_R1_BUILD_AUTHORITY_CLOSURE_COMPLETION_2026-08-24.md` |
| reviewerOwnedClosurePaths | completion review, R1 roadmap transition, material commit, later continuity sync |
| closureOwner | current orchestrator/reviewer/closer |
| workerCommitPermission | FORBIDDEN |
| acceptanceRequirement | exact diff audit plus independently executed malformed-object, time, scope and monotonicity probes |

Reviewer captures a fresh `closureBaseHead`, validates the whole pending diff,
repairs only within worker/reviewer-owned paths, runs reviewer and pre-closure
gates, commits material, then performs continuity sync separately. Worker
assertions are never independent evidence.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R1 --title "Runtime Finding Remediation R1 Build Authority Closure" --date 2026-08-24 --base e196899548d04f88ee5bc40cfce1ddf268a29d6b --commit-mode WORKER_MUST_NOT_COMMIT --dependency "operator remediation authorization on 2026-08-24" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled source verification, exact runtime invariant, tests, manifest, handoff and claim boundaries |
| checkerReadAheadConfirmation | applicable checker sources read before authoring |
| docOnlyNewFields | none; runtime type is explicitly required implementation |
| claimBoundary | scaffold provenance does not prove worker execution |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | Dispatch Prompt Envelope eight fields; `WORKER_MUST_NOT_COMMIT`; Source Verification canonical columns and ACCEPT; exact manifest; handoff fields; Reviewer Closure Conversion; Public Export Disposition |
| gateRunPurpose | confirm packet literals and worker return shape before dispatch |
| claimBoundary | checker conformance does not establish R1 semantics or completion |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| proposed paths | exact `Test-Path` checks found all new R1 paths absent | ABSENT_BEFORE_AUTHORING |
| proposed symbols | `rg` found no `BuildAuthority` or `build_authority` | NO_SAME_TOKEN_COLLISION |
| adjacent owner | `action-intent.ts`, phase/authority guards and factory exist | REUSE_NOT_DUPLICATE |
| collision decision | new guard is a bounded missing invariant in the canonical owner | EXISTING_OWNER_ENRICHMENT |

## Dual Agent Surface Matrix

| Surface | Role | Interface | Authority / risk boundary | Evidence | Adapter boundary |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | current orchestrator/reviewer | private repo and local gates | dispatch/review/commit only; no worker implementation during dispatch | committed packet and independent review evidence | repository local |
| `EXTERNAL_AGENT_CLI_MCP` | implementation worker | copied canonical packet and shared workspace diff | exact five paths; no commit/push/session/public authority | worker return plus pending diff | no MCP runtime adapter invocation authorized |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class dispatch --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --max-results 50 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | none beyond canonical guards and this packet |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local Guard Contract R1 behavior only |
| claimDisposition | CLAIM_REJECTED until execution and independent review |
| receiptEvidence | N/A with reason: no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION at dispatch; worker command evidence required |
| invocationBoundary | local TypeScript tests/typecheck and repository reads |
| interceptionBoundary | shared Guard Contract evaluation only after implementation; no provider interception claim |
| claimLanguage | complete pending independent review at most |
| forbiddenExpansion | no universal deployment, provider/live, gateway, MCP, R2 or public claim |

## Epistemic Process Block

Evidence Comparison: compare every new rule against the canonical types,
action classifier, engine mandatory protection, factory and adversarial tests.

Contradiction or Gap Disposition: stop rather than invent an issuer, store,
phase or wider owner.

Claim Update: only executed worker evidence can move the tranche to pending
review; only reviewer evidence can close it.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | external question -> local owner trace -> governed review -> R1 dispatch |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Guard Contract |
| Disposition | ADAPT into existing owner; no external implementation imported |
| Claim boundary | no corpus completeness, external authority or public snapshot claim |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: RFR-R1 changes the current canonical Guard Contract
owner from locally verified findings; it does not absorb a legacy foundation,
workflow chain, source family, or legacy coverage-index row.

## Corpus Completeness And Report Integrity

- Corpus task class: BOUNDED_DISPATCH_SOURCE_VERIFICATION
- Corpus root: six named current-authority/source files in the Source Verification Block
- Snapshot time: 2026-08-24 at dispatch base `e196899548d04f88ee5bc40cfce1ddf268a29d6b`
- Enumeration command: `rg --files --hidden --no-ignore` followed by direct reads and bounded symbol searches of the six selected files
- Manifest artifact or inline manifest: six unique source files in Source Verification Block
- Manifest hash: N/A with reason: worker must reread committed selected files from execution base
- Processing ledger artifact or inline ledger: six Source Verification rows, each terminal `READ` and `ACCEPT`
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE
- Reconciliation: manifest=6; ledger_terminal=6; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: 0
- Unreadable or unsupported files: none
- Aggregation check: six unique manifest files equal six terminal rows
- Drift check: worker rereads the committed paths after capturing `executionBaseHead`
- Output traceability: each required implementation item maps to an accepted owner row
- Adversarial verification: worker and reviewer challenge missing lifecycle and scope evidence independently
- Corpus verdict: COMPLETE_VERIFIED

## Current Runtime Freshness Verification

NOT_APPLICABLE_WITH_REASON: local deterministic Guard Contract work; no model,
provider, pricing, deployment, credential or live-runtime freshness claim.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| canonicalStorageRoot | none; R1 introduces no storage |
| generatedAggregate | none |
| mutationBoundary | exact five-path manifest |
| runtimeBoundary | in-memory request evidence evaluation only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | RFR-R1 dispatch 2026-08-24 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, ADIF resolver, patch authoring, pre-dispatch gates |
| Target paths | review, roadmap, R1 baseline and work order |
| Allowed scope source | operator remediation instruction |
| Before status evidence | HEAD `e196899548d04f88ee5bc40cfce1ddf268a29d6b`; clean worktree |
| After status evidence | four new R0 dispatch artifacts pending dispatcher commit |
| Diff evidence | documentation-only R0 changed set |
| Approval boundary | R1 dispatch only |
| Claim boundary | no R1 production edit or completion claim |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `rfr-r1-dispatch-2026-08-24` |
| Expected manifest | R0 review, roadmap, baseline and work order |
| Actual changed set | same before dispatch commit |
| Manifest delta | zero expected |
| Deletion or rename disposition | N/A with reason: none authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance remediation; no public-sync authority.

## Claim Boundary

This packet authorizes only the exact R1 local implementation and verification.
It does not claim completed enforcement, live/provider behavior, deployment,
public export, closure of F1, or authority to start R2.
