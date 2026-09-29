# CVF Agent Work Order - RFR-R4 Material Context Manifest

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-08-24

Batch ID: RFR-R4

## Dispatch Prompt Envelope

```text
Role: implementation worker. The current orchestrator remains independent reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R4_MATERIAL_CONTEXT_MANIFEST_2026-08-24.md
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: capture executionBaseHead from repository HEAD at worker start; dispatchBaseHead is deaa1b750.
Current-time notes: only RFR-R4 is released; R5-R6 and all external-effect lanes remain parked.
Do-not-misread notes: build a secret-safe local Model Gateway invocation-context manifest; no Truth runtime, provider/live, credential, deployment, public or production work.
Required first actions: read required authority and sources; capture HEAD/status; verify five hashes and exact eight-path manifest; run worker ADIF resolver.
Return contract: COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON with exact diff, tests/gates, residuals, unchanged HEAD, empty staging and zero external calls.
```

Dispatch base head: `deaa1b750`

dispatchBaseHead: `deaa1b750`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET_AFTER_WORKER_RETURN`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path: `docs/reviews/CVF_RFR_R4_MATERIAL_CONTEXT_MANIFEST_WORKER_RETURN_2026-08-24.md`

## Purpose

Implement bounded RFR-R4 closure of F5 by adding a deterministic secret-safe
material-context manifest to the existing Model Gateway execute bridge and
binding it to exact invocation evidence.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "RFR-R4",
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
    "EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/tests/material-context-manifest.test.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-execution-bridge.test.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts",
    "docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md",
    "docs/reviews/",
    "docs/baselines/",
    "docs/work_orders/"
  ],
  "claims": ["F5 secret-safe material context manifest bound to Model Gateway invocation"],
  "requiredProof": ["focused manifest tests", "bridge adversarial tests", "full Model Gateway tests", "TypeScript", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": ["R5 requires accepted R4 closure; standing roadmap authority permits dependency-ordered dispatch"],
  "forbiddenEffects": ["worker stage or commit", "provider/live call", "credential access", "Truth runtime", "deployment", "public write", "new subsystem"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, legacy disposition `RUN_FULL_LEGACY_BUNDLE`.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id RFR-R4 --title "Runtime Finding Remediation R4 Material Context Manifest" --date 2026-08-24 --base deaa1b750 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "RFR-R3 closed bounded at a18ba512f and standing roadmap authority releases R4 dispatch" --include-worker-return-skeleton --stdout` |
| generatedProfile | generic worker dispatch plus no-commit worker return |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified F5 owners, hashes, exact-eight manifest, secret-safe adversarial matrix and role split |
| checkerReadAheadConfirmation | applicable checker sources and routed standards read before authoring |
| docOnlyNewFields | none; worker selects bounded type names inside invariants |
| claimBoundary | dispatch provenance only; no implementation or closure claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| RFR-R3 closure | material `a18ba512f`; continuity `deaa1b750` | accepted R3 required | ACCEPT |
| F5 roadmap order | runtime findings roadmap R4 row | R4 follows R3 | ACCEPT |
| operator continuation | standing autonomous dependency-ordered instruction | fresh R4 dispatch | ACCEPT |

## Required First Reads

1. `AGENTS.md`, bootstrap, front door and active handoff.
2. guard orientation and literal-format gotchas.
3. paired R4 baseline and this work order.
4. all five pre-existing hashed sources in full.
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
2. `AGENTS.md`, the RFR remediation authority, and the paired R4 baseline
   govern this bounded dispatch.
3. This work order grants only its exact-eight implementation and proof scope.
4. The external worker supplies evidence; the independent reviewer alone may
   accept, repair, commit, close, or escalate the result.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | close verified F5 invocation-context provenance gap |
| scope classification | SECURITY_SENSITIVE_RUNTIME_EVIDENCE_IMPLEMENTATION |
| primary task class | bounded Model Gateway implementation |
| risk sensitivity | HIGH |
| selected role route | MULTI_AGENT_SINGLE_ROLE |
| orchestration requirement | external no-commit worker plus independent reviewer |
| role separation basis | worker cannot accept its own evidence-boundary change |
| escalation condition | ninth path, new runtime owner, external effect or raw-material retention |

## Worker Autonomy / No-Question Rule

Proceed autonomously inside the exact manifest. Repair in-scope failures after
reading their source. Return `BLOCKED_WITH_REASON` only if completion needs a
ninth path, new owner/dependency, Truth runtime, network/secrets/live/public
action, or a new independent critical contradiction. Never stage, commit or
push and do not ask permission for an in-scope repair.

## Pre-Flight Checks

- capture `git rev-parse HEAD` and initial `git status --short`;
- stop for overlapping pre-existing changes;
- verify all five hashes and three new paths are absent;
- verify exact eight-path manifest;
- run ADIF resolver for implementation/worker/pre-execution.

## Scope / Target / Owner Boundary

Worker may modify or create exactly:

1. `EXTENSIONS/CVF_MODEL_GATEWAY/src/material-context-manifest.ts`
2. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/material-context-manifest.test.ts`
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts`
4. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-execution-bridge.test.ts`
5. `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts`
6. `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
7. `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`
8. `docs/reviews/CVF_RFR_R4_MATERIAL_CONTEXT_MANIFEST_WORKER_RETURN_2026-08-24.md`

No ninth path, deletion or rename is authorized. Package/lock files, Truth
Kernel source, MCP, Web, Execution Plane, governance checkers, roadmap,
session state, credentials and public surfaces are read-only.

## Write Ownership

Worker owns exactly eight paths. Reviewer owns completion review, R4-only
roadmap transition, material commit and later continuity.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| model-visible input crosses bridge without complete manifest | RUNTIME_GAP | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | adapter invocation | `execute` | ProviderExecutionBridge | ACCEPT |
| request owns current context classes | REQUEST_OWNER | `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | execute request | `GatewayExecuteRequest` | unified gateway contract | ACCEPT |
| deterministic bridge proof owner exists | TEST_OWNER | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-execution-bridge.test.ts` | bridge suites | `makeRequest` | Model Gateway tests | ACCEPT |
| bridge exports are centralized | EXPORT_OWNER | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | bridge export block | `ProviderExecutionBridge` | barrel | ACCEPT |
| provenance vocabulary is reference-only | GOVERNANCE_REFERENCE | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | Reference-Not-Copy and Evidence Record Minimum | provenance contract | Truth Foundation reference | ACCEPT |
| F5 is accepted R4 finding | REVIEW_AUTHORITY | `docs/reviews/CVF_RUNTIME_FINDINGS_VERIFICATION_AND_REMEDIATION_AUTHORITY_2026-08-24.md` | Findings / Position | F5 | governed review | ACCEPT |

## Source Hash Manifest

| Path | Required SHA-256 before edit |
| --- | --- |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | `b678e0192726c1adf40347637c17395b2eabe25e0e4ecacb6f141ddffd1c7a3c` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/provider-execution-bridge.test.ts` | `ad930ab62fc13977162a710b23572c5df6c2ea8796d635ccec8720a4c7527d6c` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/unified-gateway-interface-contract.ts` | `97f99a936fb00f118146d319e7ded76279848ba2027f530ff13d113a0b5975b3` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | `f8d1cabe54ca05d81b82be9428e11e866cef0ca63d1cc56fe5d8ae1680da5932` |
| `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | `e496b93b02b91c394152103367a5925d026ed1ee954e6e62e6fcc2d5e4334093` |

Hash drift before edit is `BLOCKED_WITH_REASON`.

## Exact Implementation Contract

### R4-A bounded manifest owner

Create one Model Gateway-owned deterministic module. It must inventory the
current execute path's user prompt, optional system prompt, metadata and
selected invocation context without copying raw values. Do not add a generic
Truth runtime or persistence layer.

### R4-B entry minimum and completeness

Each entry resolves: context class, source reference/type, source version,
authority/provenance label, transformation method/version, invocation scope,
trace binding, sensitivity, status and deterministic content digest. Required
classes cannot silently disappear; optional absence is explicit. Unknown,
duplicate or contradictory classes reject.

### R4-C secret-safe canonicalization

Use deterministic canonicalization and a standard cryptographic digest already
available from the runtime. Reject cycles, accessors/getters, unsupported
objects, non-finite numbers, raw credential keys and unsafe depth/size. Output
must never contain prompt/system/metadata values or secret-like test tokens.

### R4-D bridge binding

Build/validate the manifest before adapter invocation and bind it to the exact
request trace, selected provider/model, adapter input and returned receipt.
Missing/mismatched/invalid manifest evidence calls adapter zero times. Success,
routing stop, pre-adapter failure and adapter throw expose truthful bounded
manifest disposition without converting a stopped call into execution proof.

### R4-E reference reconciliation

Update the Truth Foundation reference factually: vocabulary is adapted into a
Model Gateway-owned bounded runtime manifest; Truth Kernel remains unchanged
and no database/verifier/live/public/production claim follows.

## Dedicated Adversarial Matrix

Cover deterministic key order; prompt/system/metadata classes; optional
absence; empty/whitespace input; duplicate/unknown class; trace mismatch;
source/version/authority/transformation/scope omissions; raw credential keys;
secret values; cyclic/accessor/Date/Map/Set/function/symbol/bigint/non-finite
input; depth/size bounds; hash collision confusion; caller-manifest spoofing;
route deny/no-candidate; credential/health/quota/admission stop; adapter success
and throw; zero adapter calls for every invalid manifest.

## Required Artifact Manifest

All exact eight paths in Scope are required at handoff. No deletion, rename,
ninth path, staging or commit is allowed.

## Work-Order Fulfillment Manifest

| Requirement | Evidence at return |
| --- | --- |
| source/base/scope | HEAD, status, five hashes, three absent paths, exact-eight delta |
| manifest implementation | typed source, deterministic/hostile tests |
| bridge integration | adapter call-order and trace/receipt proof |
| reference reconciliation | factual bounded Truth contract update |
| no external effect | zero provider/live/network/credential/public actions |

## Required Proof Manifest

| ID | Command | Owner |
| --- | --- | --- |
| P1 | `npm test -- --run tests/material-context-manifest.test.ts tests/provider-execution-bridge.test.ts` | worker in Model Gateway |
| P2 | `npm test -- --run` | worker in Model Gateway |
| P3 | `npm run check` | worker in Model Gateway |
| P4 | `python governance/compat/generate_corpus_scan_registry.py --check` | worker at root |
| P5 | `python governance/compat/check_governed_file_size.py --enforce` | worker at root |
| P6 | `python governance/compat/run_worker_return_fast_gate.py` | worker at root |
| P7 | `git diff --check` | worker at root |
| P8 | `git diff --cached --name-only` | worker at root |
| P9 | `git rev-parse HEAD` | worker at root |
| P10 | `git status --short` | worker at root |

## Required Proof Manifest Atomic Literal Discipline

Each row is one command. Do not combine or substitute checker subsets.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_MODEL_GATEWAY
npm test -- --run tests/material-context-manifest.test.ts tests/provider-execution-bridge.test.ts
npm test -- --run
npm run check
Set-Location ../..
python governance/compat/generate_corpus_scan_registry.py --check
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --cached --name-only
git rev-parse HEAD
git status --short
```

## Execution Plan

1. Capture base/status, verify hashes/absence and complete reads.
2. Implement typed secret-safe manifest and focused adversarial tests.
3. Integrate pre-adapter build/validation and result/receipt trace binding.
4. Extend existing bridge tests and export the contract.
5. Reconcile Truth reference without runtime-authority expansion.
6. Run focused/full/type/governance proof and author truthful return.
7. Confirm empty staging and unchanged HEAD; stop for independent review.

## Evidence Requirements

Record exact before/after hashes, execution and final HEAD, exact-eight status,
empty staging, focused/full/typecheck counts, governance gates, deterministic
and hostile matrices, residuals, zero external calls and no-commit statement.

## Acceptance Criteria

- all current material context classes are complete and trace-bound;
- no raw/sensitive context appears in serialized evidence;
- canonicalization is deterministic and hostile input fails closed;
- invalid/missing/mismatched evidence calls adapter zero times;
- success/stopped/failure dispositions do not overclaim execution;
- existing Model Gateway behavior remains green;
- exact-eight manifest, unchanged HEAD and empty staging are proven.

## Review Gate

Reviewer rejects raw-material retention, caller self-attestation presented as
verified authority, partial class coverage, nondeterministic serialization,
post-adapter manifest creation, trace mismatch, assertion weakening, scope
drift, staging, worker commit or any mandatory proof failure.

## Closure Checklist

- [ ] Five hashes and three absent paths verified.
- [ ] Exact-eight manifest matched.
- [ ] Secret-safe completeness and hostile matrix passed.
- [ ] Focused/full/typecheck/governance proof passed.
- [ ] Worker-return fast gate and diff hygiene passed.
- [ ] HEAD unchanged and staging empty.
- [ ] Complete diff/evidence returned to reviewer.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_worker_experience_retrospective.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | Source Verification columns; worker-return headings/status; Agent Operation Trace labels; exact manifest; no-commit statement |
| gateRunPurpose | confirm R4 source/evidence shape before execution and prevent return-time discovery; not first discovery |
| claimBoundary | local checker/test evidence does not prove live/provider or reviewer acceptance |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_RFR_R4_MATERIAL_CONTEXT_MANIFEST_WORKER_RETURN_2026-08-24.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required real sections: Purpose; Scope / Methodology; Findings / Position; Risk
/ Corrective Action; Source Verification Block; Implementation Hash Evidence;
Test Evidence; Checker Source Read-Ahead Block; Agent Operation Trace Block;
Delta Execution Claim Boundary Control Block; Public Export Disposition;
External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus
Completeness And Report Integrity; Finding-To-Governance Learning Disposition;
Epistemic Process Block; Worker Experience Retrospective; Machine Closure
Package; Claim Boundary; git status --short; Changed Files; Command Evidence;
and No-Commit Statement.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_RFR_R4_MATERIAL_CONTEXT_MANIFEST_COMPLETION_2026-08-24.md` |
| reviewerOwnedClosurePaths | optional completion review; R4 roadmap transition; accepted exact-eight material; later continuity |
| closureOwner | current independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Agent Handoff Contract Control Block

Historical contract source, not active; archive-qualified:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

Active handoff source: `AGENT_HANDOFF_V59_2026-08-11.md`.

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | external worker then current independent reviewer/closer |
| phase | RFR-R4 implementation return |
| baseHeadFor(phase) | dispatchBaseHead=`deaa1b750`; executionBaseHead captured at start; closureBaseHead reviewer-set |
| changedSetScope(phase) | exact-eight worker manifest |
| traceScope(phase, actor) | worker reads/edits/tests/returns; reviewer inspects/probes/repairs/commits |
| commitOwner(phase) | reviewer/closer; worker forbidden |
| crossBatchIsolation | R5-R6 and every external-effect lane parked |
| nextMoveSurfaces | worker return, reviewer decision, material commit, continuity sync |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | Model Gateway request and ProviderExecutionBridge | local exact-eight evidence implementation | focused/full/type proof | repository TypeScript only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | existing RFR-R3 MCP execute adapter feeding Model Gateway | R4 changes downstream evidence only; no new ingress/live authority | hermetic/local bridge tests | existing injected executor; no transport/live call | IMPLEMENTED |

## Current Runtime Freshness Verification

| Field | Value |
| --- | --- |
| runtimeClaimPresent | YES_LOCAL_HERMETIC_ONLY |
| runtimeMutationAuthorized | YES_LOCAL_SOURCE_ONLY |
| freshnessVerificationMode | FRESH_SOURCE_HASH_AND_TEST_RECOMPUTE_REQUIRED |
| reason | R4 changes local invocation evidence, not provider/live behavior |
| requiredFutureAction | reviewer reruns local proof; live claim requires separate authority |

## Foundation Storage Layout Block

NOT_APPLICABLE_WITH_REASON: R4 creates an in-memory manifest and no durable
store, queue, database, registry family, relocation or migration.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: named-file remediation of verified F5; no corpus
absorption, coverage reassignment, source intake or foundation migration.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | verified F5 to existing Model Gateway and Truth reference owners |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | ProviderExecutionBridge and Truth Foundation reference |
| Disposition | ADAPT only locally verified F5 |
| Claim boundary | prompt is provenance input, not implementation authority |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | orchestrator/dispatcher |
| Provider or surface | private provenance repository |
| Session or invocation | `rfr-r4-dispatch-20260824` |
| Working directory | repository root |
| Command or tool surface | governed reads, source/hash inspection, Git, Vitest, TypeScript, ADIF and dispatch gates |
| Target paths | paired R4 baseline and work order |
| Allowed scope source | standing dependency-ordered roadmap authority plus accepted R3 completion review and commits `a18ba512f` / `deaa1b750` |
| Before status evidence | clean worktree at `deaa1b750` |
| After status evidence | paired R4 authority paths pending dispatch commit |
| Diff evidence | `git diff --name-status`; `git status --short`; `git diff --check` |
| Approval boundary | dispatch authority only |
| Claim boundary | no implementation, provider/live, public, deployment or push claim |
| Agent type | dispatcher |
| Invocation ID | `rfr-r4-dispatch-20260824` |
| Expected manifest | `docs/baselines/CVF_GC018_RFR_R4_MATERIAL_CONTEXT_MANIFEST_2026-08-24.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R4_MATERIAL_CONTEXT_MANIFEST_2026-08-24.md` |
| Actual changed set | `docs/baselines/CVF_GC018_RFR_R4_MATERIAL_CONTEXT_MANIFEST_2026-08-24.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_RFR_R4_MATERIAL_CONTEXT_MANIFEST_2026-08-24.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | exact local RFR-R4 no-commit dispatch |
| claimDisposition | CLAIM_REJECTED until worker proof and review |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: dispatch creates no runtime receipt |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no production source edit by dispatcher |
| invocationBoundary | local authoring/checker processes only |
| interceptionBoundary | no provider, network, public, deployment or production action |
| claimLanguage | worker-authorized local remediation, not closure |
| forbiddenExpansion | ninth path, R5-R6, live, credentials, deploy, public, push, production |

## Epistemic Process Block

### Expected Result / Prediction

F5 should close by adding one secret-safe manifest at the existing pre-adapter
bridge seam without a new Truth runtime.

### Evidence Comparison

Current sources expose all bounded owners and confirm the missing binding.

### Contradiction Or Gap Disposition

Truth vocabulary is contract-only; runtime implementation remains Model
Gateway-owned and must not self-certify broader source truth.

### Claim Update

R4 implementation is authorized but unproven pending worker return/review.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for hash drift, ninth path, incomplete class
coverage, inability to stay secret-safe/deterministic, failed proof, new
dependency/owner, or external effect. Otherwise return
`COMPLETE_PENDING_REVIEW` and stop without staging or committing.

## Operator Checkpoint

No checkpoint for in-scope local reversible implementation. Standing roadmap
authority preserves dependency sequencing and independent review. External
effects require separate authority.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance worker dispatch; public sync forbidden.

## Claim Boundary

This work order authorizes only exact-eight local RFR-R4 implementation and
proof. It does not prove F5 closure, grant worker commit authority, authorize
R5-R6, or permit provider/live, credentials, deployment, public sync or push.
