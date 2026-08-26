# CVF Agent Work Order - EAFR-R10 External Store Authority And Shared Adapter Destination Policy Implementation

Memory class: governed-worker-dispatch

Status: REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED

Work order ID: EAFR-R10

Date: 2026-08-26

dispatchBaseHead: `45684c86e804b2e5a5ac8ed581c57336bc93e5c8`

executionBaseHead: worker must capture actual HEAD and require the committed packet as ancestor

closureBaseHead: `f24811243a091226eda81930e4f4fd042bf83059`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap and accepted R9 decision

Reviewer/closer: current independent orchestrator/reviewer

Worker: bounded TypeScript implementation worker role

## Dispatch Prompt Envelope

Batch ID: EAFR-R10-EXTERNAL-STORE-AUTHORITY-AND-SHARED-ADAPTER-DESTINATION-POLICY-IMPLEMENTATION.

Role: no-commit implementation worker.

Canonical packet: this committed work order and its paired GC-018 baseline.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

providerExecutionAuthority: FORBIDDEN

Current-time notes: R9 is independently accepted at material commit
`7767c728f`; continuity closes at `45684c86e`; the worktree was clean before
R10 dispatch authoring.

Do-not-misread notes: implementing an external-store contract/evaluator is
not authority to use it. Do not wire Upstash, inspect credentials, make a
network call, run a live test, edit a package manifest, or generalize the R9
interface. The destination policy has exactly three decision variants and
must be the single source of truth for both consumers.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, `DESIGN.md`, this committed packet, paired baseline, accepted R9
worker return, every pinned input, and every applicable worker-output checker.
Capture HEAD/status/staging; require clean scope, dispatch ancestry, absent
new paths, and matching hashes before editing.

Return contract: implement only the Exact Implementation Manifest, author the
worker return, run focused commands and the required fast gate, do not stage
or commit, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Worker return path: `docs/reviews/CVF_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_WORKER_RETURN_2026-08-26.md`

Conventional completion review path: `docs/reviews/CVF_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_COMPLETION_2026-08-26.md` (reviewer-owned; optional only if the reviewer records closure in the repaired worker return).

sourceAuthority: paired GC-018 baseline, accepted R9 worker return, and pinned
current source/test/package files below

## Purpose

Implement and test the accepted sibling external-store authority contract and
the one gateway-owned adapter destination policy, closing the injected-fetch
bypass without performing or enabling deliberate live-store execution.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R10 --title "External Store Authority And Shared Adapter Destination Policy Implementation" --date 2026-08-26 --base 45684c86e --commit-mode WORKER_MUST_NOT_COMMIT --dependency "EAFR-R9 accepted bounded at 7767c728f" --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | accepted R9 interface transcription, exact source/test manifest, denial-before-fetch behavior, focused package commands, and live/store exclusions |
| checkerReadAheadConfirmation | applicable dispatch and worker-return checkers read before authoring |
| docOnlyNewFields | External Store Authority Implementation; Shared Policy Implementation; Adapter And Web Integration |
| claimBoundary | dispatch authoring only |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R9 reviewer acceptance | accepted R9 worker return; `7767c728f` | RELEASED |
| sibling authority design | R9 Decision A and Reviewer Decision | ACCEPT |
| exact gateway policy owner/interface | R9 Decision B and Reviewer Decision | ACCEPT |
| R9 continuity | `45684c86e` | ACCEPT |

## Authority And Scope

Governing baseline:
`docs/baselines/CVF_GC018_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_BASELINE_2026-08-26.md`.

The worker may create/modify only the paths in the Exact Implementation
Manifest and must not stage or commit. The accepted R9 design is binding; any
required interface expansion returns blocked.

## Authority Chain

Operator EAFR authority -> accepted R9 design -> paired R10 GC-018 baseline ->
this committed no-commit work order -> worker -> independent reviewer/closer.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
| --- | --- | --- | --- | --- |
| sibling external-store authority implementation | External Store Authority Implementation | foundation contract, barrel and tests | focused foundation test/typecheck | READY |
| shared gateway policy owner | Shared Policy Implementation | new module/test and barrel export | focused gateway policy tests/typecheck | READY |
| injected-fetch bypass closure | Adapter And Web Integration | adapter plus Web guard/test edits | fail-before-fetch and Web guard tests | READY |
| preserve non-live isolation | Zero-External-Effect Boundary | worker return zero-call evidence | command review and exact manifest | READY |

## Required First Reads

Read `AGENTS.md`, `CVF_SESSION_MEMORY.md`, bootstrap read model, active
handoff, guard orientation README, governed literal gotchas, `DESIGN.md`, the
paired baseline, this work order, accepted R9 worker return, all pinned files,
and worker-output checker sources. Resolve full session state only for a
targeted missing or contradictory fact.

## Agent Roles

Operator owns scope; dispatcher owns this packet; worker implements and tests
without committing; reviewer independently inspects behavior, repairs only
authorized defects, runs closure gates, and commits accepted material.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| intake summary | operator request to continue with the accepted R9 implementation follow-on |
| scope classification | bounded exact eleven-path worker changed set |
| worker role | no-commit TypeScript implementation worker |
| reviewer role | independent orchestrator/reviewer |
| escalation condition | stop and return BLOCKED_WITH_REASON on drift, any extra path, required dependency/config change, live attempt, or interface expansion |
| risk sensitivity | P1 provider/egress boundary; live, secret, production and public-sync effects forbidden |
| external intake | none; all authority derives from CVF-governed sources |

## Pre-Flight Checks

Require clean worktree except the committed dispatch packet ancestry, empty
staging, captured HEAD, every pinned hash matching, both new source/test paths
and worker return absent, and zero provider/live/store command selection.
Hash drift, an existing target, or unrelated dirt returns blocked before edit.

## Write Ownership

Create exactly three and modify exactly eight paths as enumerated in Exact
Implementation Manifest. No other path is writable. No delete or rename.

## Pinned Input Hashes

| Path | SHA-256 |
| --- | --- |
| `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md` | `ebcc55062d7439d6bb1bc214d783304a8d7d0883a44a6aad7f4954b9653552e0` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | `75f342ce7e09815af99b3ac778b980373986bc54f39608ca3aecf4e823082c74` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/delegation.contract.test.ts` | `a74672fca32065794dfe7c03c513d045cf26e04c87f65fb138032db53785b9b9` |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.coordination.barrel.ts` | `6541375fb499facfed10f2934e36d6b526bc20ec981e485a1eda19c40c5ea270` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | `22f264e8e3a8b6cb74d74fad8ae353a6d052a0a4fa2442a7581bcd69169d53c4` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts` | `c04cb4f5391d7dd0096e45d52837be4d20fa257627ce9159d4e0735e3ea06886` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | `5ae505e2b23e2701ba4ab9673f677ea5872e2bac27a434ab18def3a528e26f22` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/alibaba-free-quota-model-ledger.ts` | `1e1a3cf72662d9235e09ddde8b7cbb6238d1100baedc1f1b23662b016d010a51` |
| `EXTENSIONS/CVF_MODEL_GATEWAY/package.json` | `e872962581b31772fbbd4a338723877abef1d2db889c763a261e5c7662cfdd61` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | `2e4f869bb6d912db9a480b0d178be62bce457991f90f485da13d13f72bc237f5` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.test.ts` | `faa2b735874836d77913c5f9d591e94dcd169b4276b5afe749c514dfe0e462bd` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | `ed166c492657ab0600af7043f17c2d11b5ca75b52109ef6f3f036bd8c0bd8868` |

Hashes are computed at dispatch base. The accepted R9 return must remain
unchanged. Mutable source hashes are pre-edit drift guards, not expected
post-edit values. Package manifests must retain these hashes post-edit.

## Exact Implementation Manifest

| Action | Path |
| --- | --- |
| CREATE | `EXTENSIONS/CVF_MODEL_GATEWAY/src/adapter-destination-policy.ts` |
| CREATE | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/adapter-destination-policy.test.ts` |
| CREATE | `docs/reviews/CVF_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_WORKER_RETURN_2026-08-26.md` |
| MODIFY | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` |
| MODIFY | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/delegation.contract.test.ts` |
| MODIFY | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.coordination.barrel.ts` |
| MODIFY | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` |
| MODIFY | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts` |
| MODIFY | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` |
| MODIFY | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` |
| MODIFY | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.test.ts` |

## External Store Authority Implementation

Implement exactly R9 Decision A in `delegation.contract.ts`: sibling
`ExternalStoreExecutionAuthority`, `ExternalStoreExecutionGrant`,
`ExternalStoreExecutionRequest`, and
`evaluateExternalStoreExecutionAuthority`. Mirror the provider evaluator's
ordered checks and reasons, substituting only `store`/`allowedStores`. Export
through the coordination barrel. Test allowed execution and every failure:
authority, authorizer/grant ID, subject/delegation, store membership,
non-positive/exhausted call budget, missing/expired/unparseable expiry.

Do not alter `ProviderExecutionGrant`, provider evaluator semantics, or
`DelegationContract`; do not create a grant issuer or runtime consumer.

## Shared Policy Implementation

Create `adapter-destination-policy.ts` with exactly:

- `AdapterDestinationDecision = { kind: "permit-non-provider" } | { kind:
  "provider"; provider: string } | { kind: "deny"; reason: string }`;
- `classifyAdapterDestination(input: string | URL):
  AdapterDestinationDecision`.

Canonicalize, do not copy, the current Web guard logic. Preserve relative URL,
loopback, `data:`, `blob:`, and `file:` behavior; recognize every current
provider endpoint using gateway-owned constants; deny malformed,
unrecognized, and external-store destinations. Export from gateway index and
cover each decision class plus malformed and unrecognized inputs.

## Adapter And Web Integration

In the gateway adapter, classify before `fetchImpl`. Throw on `deny`, and on
a provider identity mismatch against configured `providerId`, before fetch.
Permit matching provider endpoints and already-permitted non-provider inputs.
Tests must explicitly assert the injected fetch spy remains untouched for
both denial classes and replace the R8 arbitrary-endpoint residual proof with
fail-closed proof.

In the Web test guard, import the gateway classifier and remove the local
protocol/loopback/provider-host classification data. A compatibility wrapper
may normalize `Request` to URL string. Update tests to assert retained guard
semantics through the shared owner. No second permit list may remain.

## Execution Plan

1. Complete pre-flight, hashes, ancestry and absent-path checks.
2. Implement and test the foundation sibling authority contract and export.
3. Implement/export/test the gateway-owned policy.
4. Wire and test adapter denial-before-fetch, then Web shared-owner use.
5. Run all required focused commands and typechecks.
6. Author the full-gate worker return, verify exact manifest and empty staging,
   run its fast gate, and yield without commit.

## Zero-External-Effect Boundary

providerExecutionAuthority: FORBIDDEN

Do not run provider, network, live, release-gate, external-store, credential,
deployment, or public commands. Injected fetch spies must be local fakes. No
API key is needed or authorized. If a selected command unexpectedly attempts
external execution, stop, preserve secret-safe evidence, and return blocked.

## Verification Commands

From `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`:

1. `npm test -- tests/delegation.contract.test.ts`
2. `npm run check`

From `EXTENSIONS/CVF_MODEL_GATEWAY`:

1. `npm test -- tests/adapter-destination-policy.test.ts tests/openai-compatible-execute-adapter.test.ts`
2. `npm run check`

From `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`:

1. `npm run test:run -- src/test/provider-execution-guard.test.ts`
2. `npm run check`

From repository root:

1. exact `git diff --name-status` and `git status --short --untracked-files=all`
2. `python governance/compat/run_worker_return_fast_gate.py`

Use the exact package scripts declared by the pinned manifests. Do not
substitute a broader or live command. Individual checker substitution for the
worker-return fast gate is forbidden.

## Acceptance Criteria

- exact manifest only; no deletes/renames; staging empty; HEAD unchanged;
- R9 names and three-variant policy interface implemented literally;
- external-store evaluator preserves the provider evaluator's ordered
  fail-closed behavior and all focused cases pass;
- both consumers call one gateway-owned classifier;
- arbitrary/external/malformed and provider-mismatch adapter destinations
  fail before injected fetch;
- matching provider and permitted non-provider compatibility passes;
- package manifests and accepted R9 return retain pinned hashes;
- all six package commands and worker-return fast gate pass;
- zero provider calls, zero network calls, zero external-store calls, zero
  credential reads, and no release/build/public effect.

## Evidence Requirements

Worker return must include pre/post HEAD/status/staging, ancestry, pre-edit
hash recomputation, absent-new-path proof, exact diff manifest, relevant code
citations, focused test counts/output summaries, typecheck results, retained
manifest hashes, explicit fetch-not-called proof, zero-external-effect
statement, checker output, and residuals. Self-report without command evidence
is insufficient.

## Fail Conditions

Return `BLOCKED_WITH_REASON` for drift, unrelated dirt, any extra path,
required package/dependency/config change, R9 interface expansion, duplicate
permit data, live/network/provider/store attempt, inability to prove
fail-before-fetch, a failed required command, staging, or commit.

## Worker Autonomy / No-Question Rule

Resolve ordinary TypeScript details inside the exact contracts autonomously.
Do not ask the operator to widen scope. If the accepted design cannot be
implemented within the manifest, stop and return the first named blocker with
partial evidence; do not improvise a fourth decision type or live-store wire.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: implementation changes runtime source and must be freshly
proved against the committed dispatch inputs

priorVerificationArtifact: accepted R9 worker return

priorVerificationAnchor: R9 material commit `7767c728f` and pinned SHA-256 table

freshRecomputeRequired: pre-edit hashes, exact diff, focused tests, typechecks,
fetch-not-called assertions, manifest invariants, and worker-return gate

unicodePathHandling: literal repository-relative paths and UTF-8-safe tools

extractedTextAuthority: CVF-governed sources and fresh local command output only

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| sibling authority names and fields are binding | DECISION_AUTHORITY | `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md` | Decision A | ExternalStoreExecutionGrant | R9 Reviewer Decision | ACCEPT |
| exact policy path/type/function are binding | DECISION_AUTHORITY | `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md` | Decision B | classifyAdapterDestination | R9 Reviewer Decision | ACCEPT |
| provider evaluator is the ordered behavioral precedent | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | evaluator body | evaluateProviderExecutionAuthority | delegation contract | ACCEPT |
| injected adapter bypass exists before R10 | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | execute body | fetchImpl | gateway adapter | ACCEPT |
| current classifier is Web-test-local | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | classifier helpers | classifyDestination | Web test guard | ACCEPT |
| cvf-web already has gateway dependency | PACKAGE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies | cvf-model-gateway | Web manifest | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_forbidden_filesystem_state.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | first H2 prompt envelope; Source Verification; Current Runtime Freshness; Evidence Reuse scalars; exact manifest; forbidden paths/state; Agent Operation Trace labels; Delta fields; no-commit statement; Public Export token |
| gateRunPurpose | confirm as evidence that the authored dispatch and worker-return requirements match the checker contracts; not first discovery |
| claimBoundary | checker shape is not implementation evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-source-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class runtime-source-implementation --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact R10 baseline/work order/return | absent before authoring | PASS |
| new gateway source/test paths | both absent before dispatch | PASS |
| R10 token search | no prior R10 packet or implementation artifact | PASS |
| collision decision | create only the two gateway files plus worker return; modify only eight named files | PASS |

## Forbidden Path Manifest

| Path or family | Rule |
| --- | --- |
| `**/.env*` | do not read, create, or edit credential/environment files |
| all `package.json`, lockfile, tsconfig and vitest config paths | existing configuration is read-only |
| `cvf-web/src/lib/rate-limit.ts` and `cvf-web/src/lib/storage-adapter.ts` | live-store runtime wiring is a future separately governed tranche |
| `CVF_SESSION/**`, roadmaps, baselines, work orders, checkers and registries | reviewer/session owners only |
| sibling public clone, deployment and release paths | no external/public effect authority |

## Forbidden Filesystem State At Dispatch

| Forbidden path class | Actual state | Disposition |
| --- | --- | --- |
| environment and credential files | NOT_INSPECTED_WITH_REASON: access itself is forbidden and unnecessary | PASS |
| package/config manifests | PRESENT_EXEMPTED: pinned read-only inputs; modification forbidden | PASS |
| runtime external-store consumers | PRESENT_EXEMPTED: existing source, explicitly outside write ownership | PASS |
| session/governance/public/deployment families | PRESENT_EXEMPTED: existing owner surfaces, outside worker manifest | PASS |

## Pre-Existing Dirty State Exemption

N/A with reason: dispatch began from a clean worktree and the worker must also
begin clean after the committed packet; unrelated dirt is not exempted.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | foundation evaluator, gateway adapter and Web test guard | local contract/guard implementation; no live grant or traffic | focused tests and typechecks | exact eleven-path worker manifest | HARDEN_BOUNDED |
| EXTERNAL_AGENT_CLI_MCP | none | no CLI/MCP/provider authority or behavior changes | zero external-effect evidence | separately governed | DEFERRED_WITH_REASON |

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "EAFR-R10",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "LOCAL_REVERSIBLE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "NEW_AUTHORITY"
  },
  "pathFamilies": [
    "EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts",
    "EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.coordination.barrel.ts",
    "EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/delegation.contract.test.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/src/adapter-destination-policy.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/tests/adapter-destination-policy.test.ts",
    "EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts",
    "EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.test.ts",
    "docs/reviews/CVF_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_WORKER_RETURN_2026-08-26.md",
    "docs/baselines/CVF_GC018_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_BASELINE_2026-08-26.md",
    "docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_2026-08-26.md",
    "docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md"
  ],
  "claims": ["the accepted sibling authority contract and one shared gateway destination policy are implemented and locally proved without live-store wiring"],
  "requiredProof": ["pre-edit hashes", "focused tests", "typechecks", "single-owner search", "fetch-not-called assertions", "exact diff", "worker-return fast gate", "independent review"],
  "operatorCheckpoints": [],
  "forbiddenEffects": ["provider or network call", "external-store call", "credential access", "package or config edit", "duplicate permit list", "worker stage or commit", "public deploy or push"],
  "sourceEvidence": {"selectedFilesFullyRead": true, "corpusReceiptRef": null, "completenessClaimChanged": false}
}
```

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | no-commit worker plus independent reviewer |
| phase | implementation dispatch pending worker return |
| baseHeadFor(phase) | dispatchBaseHead=45684c86e; executionBaseHead=worker captures; closureBaseHead=reviewer captures |
| changedSetScope(phase) | exactly eleven worker-owned paths |
| traceScope(phase, actor) | sibling authority plus shared destination policy implementation |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | RFR, BuildAuthority, live/provider/store, public and deployment effects parked |
| nextMoveSurfaces | worker return then independent reviewer decision |

## Worker Output Checker Read-Ahead Mandate

Before authoring the worker return, read every checker source applicable to
its review-family path and conditional content. Derive headings and literal
tokens from source; do not substitute checklist prose.

## Work-Order Fulfillment Manifest

| Artifact group | Required worker action |
| --- | --- |
| foundation authority | implement sibling contract/evaluator, export, and focused tests |
| shared gateway policy | create exact module/type/function, export, and focused tests |
| consumer enforcement | wire adapter and Web guard to one classifier and prove fail-before-fetch |
| worker return | record full uncommitted evidence, exact manifest and honest residuals |

## Current Runtime Freshness Verification

| Field | Disposition |
| --- | --- |
| Runtime/source paths checked | all twelve pinned inputs plus both absent intended gateway paths |
| Current source result | MATCH: provider-only evaluator exists; gateway classifier does not; Web-test-local classifier and injected adapter bypass remain |
| Dependency result | MATCH: Web depends on gateway; no new package edge needed; manifests are read-only |
| Runtime behavior claimed | N/A_WITH_REASON: this pre-dispatch packet does not claim the worker implementation already exists |
| Provider/live proof claimed | N/A_WITH_REASON: live/provider/store execution is forbidden and not needed for this local boundary proof |
| Public-sync claimed | N/A_WITH_REASON: private provenance only |
| Freshness disposition | PASS - current source matches the accepted R9 starting condition |

## Required Artifact Manifest

| Artifact path | Required at handoff | Current disposition |
| --- | --- | --- |
| paired R10 GC-018 baseline | yes | dispatcher-authored pending commit |
| this R10 work order | yes | dispatcher-authored pending commit |
| R10 worker return path | yes | absent until worker execution |
| ten source/test implementation paths | yes | two absent and eight unchanged until worker execution |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_WORKER_RETURN_2026-08-26.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must carry the full review-family/no-commit shape, cite this work
order, report all eleven actual dirty paths, commands/results, failures and
residuals, and state `WORKER_MUST_NOT_COMMIT honored; no commit performed`.

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_COMPLETION_2026-08-26.md`; NOT_CREATED_OPTIONAL_WITH_REASON: reviewer may record decision in the repaired worker return |
| reviewerOwnedClosurePaths | worker return, optional completion review, roadmap, registry evidence and continuity |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

Reviewer must inspect implementation, independently run proportional focused
proof, confirm a single policy owner and pre-fetch denial, assess all failures,
then repair only within authorized manifest or reject/return blocked.

## Review Gate

Only the independent reviewer/closer may accept, repair, run closure gates and
commit. Worker test results are evidence inputs, not self-acceptance.

## Closure Checklist

- exact eleven-path worker manifest and no staging/commit;
- exact R9 public names and three policy variants;
- one classifier implementation, two consumers;
- ordered grant tests and fail-before-fetch tests green;
- required package typechecks green;
- zero provider/network/store/credential/public effects;
- independent reviewer-fast and proportional closure gates pass.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every acceptance criterion is met.
Otherwise return `BLOCKED_WITH_REASON` with the first blocker, partial command
evidence, exact dirty set, and no scope widening.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation Storage Layout Block | N/A with reason: R10 modifies an existing TypeScript contract and adds a gateway runtime module, not a memory foundation family or generated storage topology |
| Protected storage paths | foundation memory filenames, folder fronts, generated aggregates and indexes unchanged |
| Follow-up condition | any new stable memory foundation or generated-state path requires separate authority |

## Operator Authority Boundary

operator.checkpoint.waiver: none. API keys do not imply authority. Provider,
live, network, external-store, credential, RFR, BuildAuthority, package/config,
public sync, deployment and push remain parked.

## Core Guard Self-Protection Authorization - R10 Reviewer Repair Hashes

Authorized guard-maintenance scope: update only R10 current-authority hashes
after the reviewer corrects the dispatcher command and converts this work
order to accepted closure; regenerate session aggregates without changing the
pre-material mode.

Protected paths: `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
`CVF_SESSION/ACTIVE_SESSION_STATE.json`;
`CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`.

Operator authorization: operator assigned the current agent full
orchestrator/reviewer authority to clean worker findings and close the packet.

Rollback boundary: revert only the R10 reviewer material/continuity batches;
retain committed dispatch `ebdfdbd29` and R9 history.

Not authorized: provider/live/network/external-store calls, credentials,
live-store wiring, package/config edits, RFR, BuildAuthority, public sync,
deployment or push.

## Commit Prompt Readiness

- worker commit: forbidden;
- reviewer material commit: only after independent acceptance;
- continuity commit: separate after material commit;
- push/public sync: unauthorized.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher/orchestrator |
| Provider or surface | private local repository |
| Session or invocation | EAFR-R10 dispatch authoring, 2026-08-26 |
| Working directory | repository root |
| Command or tool surface | startup reads, source inspection, hashes, negative searches, scaffold, ADIF resolver and packet authoring |
| Target paths | R10 baseline, work order and roadmap dispatch row |
| Allowed scope source | operator continuation plus accepted R9 follow-on authority |
| Before status evidence | clean worktree at `45684c86e804b2e5a5ac8ed581c57336bc93e5c8`; staging empty |
| After status evidence | pending dispatch artifacts only; implementation paths unchanged |
| Diff evidence | exact documentation diff reviewed before gates/commit |
| Approval boundary | R10 dispatch only |
| Claim boundary | no worker implementation or external effect |
| Agent type | dispatcher |
| Invocation ID | `eafr-r10-dispatch-2026-08-26` |
| Expected manifest | R10 baseline, work order and roadmap row |
| Actual changed set | R10 baseline, R10 work order and EAFR roadmap row |
| Manifest delta | NONE |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R10 implementation dispatch authority only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: accepted R9 return, source inspection, hashes and absent-path checks |
| actionEvidence | ACTION_EVIDENCE_PRESENT: baseline/work order/roadmap dispatch artifacts only after commit |
| invocationBoundary | local documentation authoring and read-only source verification |
| interceptionBoundary | no universal runtime, CLI, MCP, provider, or network interception claim |
| forbiddenExpansion | any path/effect outside exact worker manifest, especially live-store wiring, dependencies, credentials and external execution |
| claimLanguage | committed packet will authorize bounded local implementation and fake-based tests only |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent packet request |
| Chain map route | N/A_WITH_REASON: all authority and evidence are CVF-governed local sources |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | accepted R9 return and current package sources |
| Disposition | N/A_WITH_REASON: no external knowledge intake |
| Claim boundary | no provider-local memory or external report used as authority |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: targeted named-file implementation, not an intake refresh or corpus scan.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no complete repository or all-files claim.

## Epistemic Process Block

- Epistemic Process Applicability: HIGH_EVIDENCE
- Expected Result / Prediction: the accepted sibling evaluator fits the
  existing foundation owner, while a gateway-local classifier can serve both
  consumers through the already-present Web dependency and deny before fetch.
- Evidence Comparison: current files and manifests match that prediction;
  no dependency or runtime-store wiring is required.
- Contradiction or Gap Disposition: the tempting false closure is either to
  copy Web's permit list into gateway or to treat the grant contract as live
  authority. Both are explicitly forbidden and tested as boundaries.
- Claim Update: R10 may enter no-commit worker implementation only after this
  packet is committed; live-store use remains a future separate decision.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| an injected adapter fetch bypasses the Web-only policy owner | EGRESS_AUTHORITY_GAP | GOVERNANCE_CONTROL_PLANE | IMPLEMENT_AND_TEST | centralize classifier in gateway and prove denial before fetch |
| a grant contract could be misread as runtime permission | AUTHORITY_CLAIM_GAP | GOVERNANCE_CONTROL_PLANE | BOUNDARY_ENFORCED | keep all store consumers and live execution outside R10 |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation tranche; no public-sync authority.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this work order | `REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | repaired R10 worker return | reviewer decision and two disclosed corrections | PASS |
| Roadmap state | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | R10 accepted bounded; live-store wiring unopened | PASS |
| Registry JSON | R10 GC-051 per-entry source plus generated aggregate | ten named source/test paths covered | PASS |
| Registry Markdown | N/A with reason: no Markdown registry projection exists | JSON registry is canonical | BLOCKED with reason: not applicable |
| External evidence digest | N/A with reason: no external evidence consumed | none | N/A with reason |
| System loop interlock | R8 residual to R9 design to R10 implementation | explicit dependency chain and focused proof | PASS |
| Session continuity | separate post-material synchronization | material commit required first | BLOCKED with reason: material commit pending |

## Claim Boundary

This work order authorizes only the exact eleven-path, no-commit implementation
after its dispatch commit is an ancestor. It grants no provider, network,
external-store, credential, release, build, package/config, RFR, public,
deployment, push, or production authority. Passing local tests proves only
the bounded contract and injected-boundary behaviors they exercise.
