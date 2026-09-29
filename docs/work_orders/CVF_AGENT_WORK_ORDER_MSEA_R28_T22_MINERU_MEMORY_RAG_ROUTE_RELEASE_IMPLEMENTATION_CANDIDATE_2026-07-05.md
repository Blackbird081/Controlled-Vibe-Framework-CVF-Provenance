# CVF Agent Work Order - MSEA-R28-T22 MinerU Memory/RAG Route Release Implementation Candidate

Memory class: POINTER_RECORD

Status: DISPATCH_READY

rawMemoryReleased: false

Date: 2026-07-05

Role: Worker
Canonical packet: `docs/baselines/CVF_GC018_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_2026-07-05.md`
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: 1181a46ee
executionBaseHead: 1181a46ee
closureBaseHead: REVIEWER_SET_AFTER_WORKER_RETURN
Return contract: `COMPLETE_PENDING_REVIEW` with uncommitted worker-owned files, or `BLOCKED` with reason.

## Dispatch Prompt Envelope

Role: Worker.
Canonical packet: `docs/baselines/CVF_GC018_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_2026-07-05.md`
Commit mode: WORKER_MUST_NOT_COMMIT
executionBaseHead: 1181a46ee
Current-time notes: T22 is bounded to source/test implementation candidate work; no live provider, private-output, public-sync, production route, or push is authorized.
Do-not-misread notes: T22 may implement an in-process candidate helper and tests only; it must not claim production memory/RAG route release.
Required first actions: read the canonical packet, T21 matrix, T21 worker return, T20 helper, durable store, runtime hierarchy, T18 adapter source, R27 ledger, R24-T4 policy, and ADIF-0024 before editing.
Return contract: COMPLETE_PENDING_REVIEW with uncommitted worker-owned files and current command evidence, or BLOCKED with reason.

Execute T22 as a bounded implementation-candidate tranche. Create a focused
TypeScript helper and tests that release only a test-scoped MinerU memory/RAG
route candidate after explicit memory-owner authorization, R27 prerequisite
verification, and R24-T4 privacy invariant checks. Use the T20 durable-store
invocation helper rather than bypassing it.

Do not commit. Do not push. Do not edit files outside allowed scope.

## Purpose

Implement and test the bounded T22 memory/RAG route release candidate helper
without releasing production memory/RAG routing or expanding beyond the
authorized Learning Plane source/test scope.

## Authority Chain

| Authority | Disposition |
|---|---|
| Operator request | Author a fresh work order after T21 worker execution and review chain |
| T21 decision matrix | Selects T22 implementation candidate and names memory-owner authorization constraints |
| T20 helper | Provides accepted durable-store invocation helper for bounded reuse |
| R27 ledger | Requires receipt, quality, source pointer, downstream-use status, claim boundary, fresh GC-018, and memory owner work order |
| R24-T4 policy | Preserves private/generated output boundary |

## Agent Roles

| Role | Responsibility |
|---|---|
| dispatcher | authored this T22 packet and pre-dispatch evidence |
| worker | implements allowed T22 helper/test paths and writes worker return |
| reviewer/closer | reviews worker return, repairs allowed-scope defects if needed, commits accepted material, and updates session-sync surfaces |

## Required First Reads

Read these before editing:

1. `docs/baselines/CVF_GC018_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_2026-07-05.md`
2. `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md`
3. `docs/reviews/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-05.md`
4. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts`
5. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts`
6. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts`
7. `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`
8. `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md`
9. `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md`
10. `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0024.md`

## Scope

Allowed edits:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-memory-rag-route-release.test.ts`
- `docs/reviews/CVF_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_WORKER_RETURN_2026-07-05.md`

Forbidden edits and actions:

- no Python source/test edits, including Pylance workaround edits;
- no `.qwen`, `.vscode`, IDE, provider-local, or user configuration artifacts;
- no root package export/barrel edits unless the worker blocks and requests a
  fresh dispatch amendment;
- no MinerU runtime execution, private/generated content read, Candidate Group
  A import, provider/live proof, public-sync, Web/UI, standalone app,
  legal/use-case deep dive, retrieval/vectorization, file-backed production
  persistence, production route wiring, commit, or push.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| routeMode | MULTI_AGENT_SINGLE_ROLE |
| intake summary | Operator requested the next governed T22 work order after T21 selected the memory/RAG route release implementation candidate |
| dispatcher | dispatch author created this T22 packet |
| worker | executes only the allowed source/test/worker-return paths |
| reviewerCloser | reviews `COMPLETE_PENDING_REVIEW`, repairs allowed-scope defects if needed, commits accepted material, and updates session-sync surfaces |
| workerCommitMode | WORKER_MUST_NOT_COMMIT |
| externalAgentSurface | N/A with reason: no CLI/MCP external-agent adapter, provider-local state, or public-sync surface is authorized |
| escalation | BLOCKED only if required source facts contradict, allowed paths are insufficient, or forbidden actions become necessary |

## Worker Autonomy / No-Question Rule

The worker must use reasonable implementation judgment inside allowed scope and
must not stop for preference questions. The worker may return `BLOCKED` only
when the work cannot be completed without forbidden files, forbidden runtime
execution, missing source authority, or a contradiction in the verified T21/T20
chain.

## Pre-Flight Checks

Before editing, worker must confirm:

- `git rev-parse --short HEAD` matches `executionBaseHead` or record drift;
- allowed paths are still available;
- no provider-local or IDE side-channel file is needed for implementation;
- no private/generated MinerU output content is required.

## Write Ownership

Worker owns uncommitted changes only in the allowed T22 source, test, and worker
return paths. Reviewer/closer owns closure review, commit, and session-sync
surfaces after acceptance.

## Execution Plan

1. Read required sources.
2. Implement the T22 helper in the allowed TypeScript source path.
3. Add focused Vitest coverage in the allowed TypeScript test path.
4. Run required verification commands after the final material edit.
5. Write the worker return with current evidence and no-commit status.

## Evidence Requirements

Evidence must include current command results for the focused Vitest command,
`npm run check`, `git diff --name-status`, and
`git status --short --untracked-files=all`, plus a worker-output hygiene
self-audit covering provider-local files and static-analysis disposition.

## Implementation Requirements

Create a T22 helper that:

- introduces `MineruMemoryOwnerAuthorization`, `MineruMemoryRagRouteReleaseInput`,
  `MineruMemoryRagRouteReleaseResult`, and
  `releaseMineruMemoryRagRouteCandidate` or equivalent local names;
- accepts a `DurableMemoryStore`, a T20-compatible adapter payload, and a
  memory-owner authorization object;
- requires authorization `policyDecision` to match `"allow"`;
- requires authorization `actorAuthorized` to be `true`;
- requires authorization `provenanceScore` to be at least `0.7`;
- requires authorization actor role and target durable tier to match the T20
  adapter payload;
- verifies all five R27 prerequisite booleans before invoking T20 helper;
- preserves `outputContentRead: false`, `rawMemoryReleased: false`,
  `canReinject: false`, and `summaryOnly: true`;
- invokes `invokeMineruDurableStoreWrite` only after T22 authorization and
  invariant checks pass;
- returns a bounded success disposition such as
  `MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTED_BOUNDED_CANDIDATE` only for
  in-process candidate behavior;
- returns or carries `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22`
  so production route release remains held.

## Test Requirements

Create focused Vitest coverage for:

- successful bounded in-process route release through the T20 helper;
- missing memory-owner authorization fail-closed behavior;
- authorization mismatch against adapter payload fail-closed behavior;
- low provenance fail-closed behavior;
- at least one R27 prerequisite fail-closed case;
- private-output invariant fail-closed case using a fixture that flips one
  privacy boolean away from its source-verified allowed value;
- confirmation that no file-backed production persistence, retrieval,
  vectorization, private-output content read, or reinjection behavior is
  introduced.

## Verification Commands

Run from `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION` after the final material
source/test edit:

```bash
npm test -- mineru-memory-rag-route-release.test.ts
npm run check
```

Run from repository root after the worker return is created:

```bash
python governance/compat/run_worker_return_fast_gate.py --base 1181a46ee --head HEAD
git diff --name-status
git status --short --untracked-files=all
```

Record command, working directory, exit status, and a concise result in the
worker return.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must include:

- Purpose;
- Target / Source;
- Scope / Methodology;
- Findings / Position;
- Risk / Corrective Action;
- Claim Boundary;
- Checker Source Read-Ahead Block;
- Agent Operation Trace Block;
- Delta Execution Claim Boundary Control Block;
- Public Export Disposition;
- executionBaseHead;
- git status evidence after worker return creation;
- Worker Output Quality Controls;
- Provider-Local Stray Artifact Control;
- Pylance Static-Analysis Diagnostic Boundary.

## Worker Output Quality Controls

The worker return must state:

- focused tests and `npm run check` were rerun after the final source/test edit;
- every required command was copied exactly from this work order;
- `git status --short --untracked-files=all` was run after creating the worker
  return;
- no unexpected provider-local or IDE side-channel files remain;
- any `.qwen/settings.json` or equivalent provider-local file created during
  provider/model switching was removed or disclosed as local-only and unstaged;
- the existing Python Pylance/static-analysis warning is either still an
  out-of-scope IDE path issue or unaffected by T22;
- negative tests cover memory-owner authorization and a risky invariant.

## Provider-Local Stray Artifact Control

Provider-local files are not allowed worker deliverables. Do not create,
modify, stage, commit, or cite `.qwen/settings.json`, `.vscode/settings.json`,
IDE settings, provider memory, or model-provider local config as source
authority. If such a file appears during execution, remove it before return or
disclose it as local-only and unstaged.

## Pylance Static-Analysis Diagnostic Boundary

The existing IDE warning on the Python receipt-writer test is outside T22
allowed edit scope. Do not edit Python source/tests, `pyrightconfig.json`, or
IDE configuration to silence it. Fix only TypeScript import/type diagnostics
inside the allowed T22 TypeScript files.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; dispatchBaseHead; executionBaseHead; closureBaseHead; Worker Return Packet Shape Contract; contractProfile: WORKER_RETURN_FULL_GATE_V1; requiredGate; run_worker_return_fast_gate.py; individualCheckerSubstitution: FORBIDDEN; workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED; Source Verification Block; New Doc-Only Fields; Work-Order Fulfillment Manifest; Worker Output Quality Controls; Provider-Local Stray Artifact Control; Pylance Static-Analysis Diagnostic Boundary; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition |
| gateRunPurpose | confirmation evidence before dispatch; checker execution is not first discovery |
| claimBoundary | checker read-ahead evidence only; no worker execution, MinerU runtime, private-output, provider/live, public, production memory/RAG route, or production-readiness claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024

Disclosure count: 10 returned defects from the resolver output are listed.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| T21 selected T22 as the future memory/RAG route implementation candidate and preserved the T21 no-release hold token | `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md` | lines 95-128 and 135-151 | `T22_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE`; `MEMORY_RAG_ROUTE_RELEASE_NOT_AUTHORIZED_BY_T21_DECISION_ONLY` | T21 selected decision disposition | VALUE_SET | ACCEPT |
| T21 requires T22 to provide explicit memory-owner authorization fields and R27 prerequisite verification | `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md` | lines 117-128 | `policyDecision`; `actorAuthorized`; `provenanceScore`; `outputContentRead`; `rawMemoryReleased` | T21 next recommended move | VALUE_SET | ACCEPT |
| T20 helper is invocation-only and does not authorize memory/RAG route release or production file-backed storage | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 1-10 | `invokeMineruDurableStoreWrite` | MinerU durable-store invocation helper | RUNTIME_BEHAVIOR | ACCEPT |
| T20 helper input mirrors the T18 adapter payload keys needed by T22 | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 37-60 | `MineruDurableStoreInvocationInput` | TypeScript interface | EXISTS | ACCEPT |
| T20 helper fail-closes on private-output and R27 prerequisite violations before store invocation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 111-261 | `outputContentRead`; `rawMemoryReleased`; `canReinject`; `summaryOnly`; `r27ReceiptPrerequisite`; `r27QualityPrerequisite`; `r27SourcePointerPrerequisite`; `r27DownstreamUsePrerequisite`; `r27ClaimBoundaryPrerequisite` | `invokeMineruDurableStoreWrite` | RUNTIME_BEHAVIOR | ACCEPT |
| T20 helper maps validated adapter fields into `DurableMemoryWriteInput` and captures a durable-store receipt | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 365-399 | `DurableMemoryWriteInput`; `durableStoreReceipt` | `invokeMineruDurableStoreWrite` | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store write input contains the policy, actor, and provenance fields T22 must cross-check | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-64 | `DurableMemoryWriteInput`; `policyDecision`; `actorAuthorized`; `provenanceScore` | Durable memory store interface | EXISTS | ACCEPT |
| Durable store denies writes unless policy allows and actor is authorized | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-212 | `write`; `durable_memory_policy_denied` | `BaseDurableMemoryStore.write` | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store rejects low provenance, raw payload, secrets, empty fields, and blocked lifecycle states before recording memory | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 248-276 | `low_provenance_score`; `raw_memory_payload_rejected`; `privacy_filtered` | `BaseDurableMemoryStore.write` | RUNTIME_BEHAVIOR | ACCEPT |
| Durable store receipt preserves summary-only, no-reinjection, and no-raw-memory-release invariants | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35-49 and 148-176 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | `DurableMemoryReceipt`; `makeReceipt` | LITERAL_INVARIANT | ACCEPT |
| Runtime memory hierarchy allows durable writes only for specified actor roles and denies injection or reinjection | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 171-205 and 245-286 | `evaluateRuntimeMemoryAction`; `RuntimeMemoryActorRole` | runtime memory hierarchy | RUNTIME_BEHAVIOR | ACCEPT |
| T18 adapter candidate carries policy, actor, provenance, R27, summary-only, no-reinjection, no-raw-release, no-output-read, and memory-write false fields | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 198-228 and 928-953 | `MineruDurableMemoryWriteAdapterCandidate`; `mineru_durable_memory_write_adapter_candidate_payload` | T18 adapter payload | EXISTS | ACCEPT |
| T18 adapter builder fail-closes on policy, actor, provenance, actor-role/tier, R27, private-output, and preauthorized-memory gaps | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 779-917 | `build_mineru_durable_memory_write_adapter_candidate` | T18 adapter builder | RUNTIME_BEHAVIOR | ACCEPT |
| R27 requires receipt, quality, source pointer, downstream-use status, and claim boundary before memory-safe candidate release, plus a fresh GC-018 and memory owner work order before memory write authorization | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 77-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | Scan-to-memory intake route matrix | VALUE_SET | ACCEPT |
| R24-T4 requires output-content-read false and keeps private generated output content out of successor routing | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 53-64 and 212 | `outputContentRead`; `privateOutputDisposition`; `PRIVATE_GENERATED_OUTPUT` | private-output policy | VALUE_SET | ACCEPT |
| ADIF-0024 requires current command evidence, git status with untracked files, provider-local or IDE cleanup/disclosure, static-analysis disposition, and negative edge-case tests for risky source/test tranches | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0024.md` | lines 64-85 and 111-119 | `Worker Output Quality Controls` | ADIF entry | VALUE_SET | ACCEPT |
| The Python test Pylance warning is a static-analysis path issue involving `sys.path.insert` and import placement; T22 does not authorize Python path edits | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 1-13 | `sys.path.insert`; `from mineru_metadata_receipt_writer import` | Python focused test | EXISTS | ACCEPT |

## New Doc-Only Fields

| New field or token | Purpose | Disposition |
|---|---|---|
| `MINERU_MEMORY_RAG_ROUTE_RELEASE_VERSION` | proposed T22 helper version constant | DOC_ONLY_NEW |
| `MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTED_BOUNDED_CANDIDATE` | proposed bounded candidate success disposition | DOC_ONLY_NEW |
| `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22` | proposed hold token proving no production route release | DOC_ONLY_NEW |
| `MineruMemoryRagRouteReleaseInput` | proposed T22 helper input type | DOC_ONLY_NEW |
| `MineruMemoryOwnerAuthorization` | proposed explicit authorization type for T22 | DOC_ONLY_NEW |
| `MineruMemoryRagRouteReleaseResult` | proposed T22 helper result type | DOC_ONLY_NEW |
| `releaseMineruMemoryRagRouteCandidate` | proposed helper function | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Checked item | Evidence | Disposition |
|---|---|---|
| Planned T22 source path | `Test-Path` returned `False` before authoring | ABSENT_BEFORE_DISPATCH |
| Planned T22 test path | `Test-Path` returned `False` before authoring | ABSENT_BEFORE_DISPATCH |
| Planned T22 GC-018 path | `Test-Path` returned `False` before authoring | ABSENT_BEFORE_DISPATCH |
| Planned T22 work-order path | `Test-Path` returned `False` before authoring | ABSENT_BEFORE_DISPATCH |
| Planned T22 worker-return path | `Test-Path` returned `False` before authoring | ABSENT_BEFORE_DISPATCH |

## Evidence Reuse And Encoding Plan

| Field | Value |
|---|---|
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | N/A with reason: T22 implementation candidate requires fresh source/test verification |
| priorVerificationAnchor | N/A with reason: T22 starts from dispatchBaseHead `1181a46ee` |
| freshRecomputeRequired | true |
| unicodePathHandling | ASCII-only new artifact names; preserve existing repository paths exactly when cited |
| extractedTextAuthority | N/A with reason: no OCR, PDF extraction, private generated output, or document-truth evidence is authorized |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T22 --title "MinerU Memory RAG Route Release Implementation Candidate" --date 2026-07-05 --base 1181a46ee --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Authored T22 envelope fields, authority chain, roles, pre-flight checks, source verification, ADIF disclosure, worker-output quality controls, provider-local/Pylance boundaries, handoff controls, and claim boundary from current T21/T20 evidence |
| docOnlyNewFields | `MINERU_MEMORY_RAG_ROUTE_RELEASE_VERSION`; `MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTED_BOUNDED_CANDIDATE`; `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22` |
| checkerReadAheadConfirmation | Checker sources listed in the Checker Source Read-Ahead Block were read before authoring |
| claimBoundary | Dispatch scaffold provenance only; no provider/live/public/Web/MCP/model-router/runtime behavior claim |

## Work-Order Fulfillment Manifest

| Planned worker output | Required path or surface | Required disposition |
|---|---|---|
| T22 helper implementation | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | create or block with reason |
| T22 focused tests | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-memory-rag-route-release.test.ts` | create or block with reason |
| Worker return | `docs/reviews/CVF_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_WORKER_RETURN_2026-07-05.md` | COMPLETE_PENDING_REVIEW or BLOCKED |

## Required Proof Manifest Atomic Literal Discipline

Future proof rows in the worker return must be command-backed and current after
the last material edit. T22 must not treat planned source/test paths as proof
until the worker has created or explicitly blocked them.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local repository authoring through shell and apply_patch |
| Session or invocation | MSEA-R28-T22 work-order authoring, 2026-07-05 |
| Working directory | repository root |
| Command or tool surface | `rg`; `Get-Content`; `Test-Path`; ADIF resolver; apply_patch |
| Target paths | this work order; paired GC-018 baseline |
| Allowed scope source | operator requested next work order after T21 worker execution and review chain |
| Before status evidence | worktree clean before T22 authoring; `git rev-parse --short HEAD` returned `1181a46ee`; `git status --short --untracked-files=all` was empty |
| After status evidence | to be produced by dispatch author gates before dispatch commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no worker execution, runtime, provider/live, private-output, public, production memory/RAG route, or production-readiness claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r28-t22-memory-rag-route-release-implementation-candidate-dispatch-2026-07-05` |
| Expected manifest | paired GC-018 baseline and this work order |
| Actual changed set | paired GC-018 baseline and this work order before material commit |
| Manifest delta | MATCH |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker executes under WORKER_MUST_NOT_COMMIT; reviewer/closer converts accepted return into closure and commit |
| phase | DISPATCH |
| baseHeadFor(phase) | dispatchBaseHead=`1181a46ee`; executionBaseHead=`1181a46ee`; closureBaseHead=`REVIEWER_SET_AFTER_WORKER_RETURN` |
| changedSetScope(phase) | dispatch changes only this work order and paired T22 GC-018 |
| traceScope(phase, actor) | dispatcher records source verification, ADIF disclosure, checker read-ahead, provider-local/Pylance controls, and clean-worktree evidence; worker records execution commands and changed files; reviewer records closure diff and commit steward results |
| commitOwner(phase) | dispatcher owns dispatch commit; worker owns no commit; reviewer/closer owns accepted material and session-sync commits |
| crossBatchIsolation | Before status evidence: `git rev-parse --short HEAD` returned `1181a46ee`; `git status --short --untracked-files=all` was empty before T22 authoring |
| nextMoveSurfaces | dispatcher updates session surfaces only after dispatch commit; reviewer/closer updates closure surfaces after accepted worker return |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_COMPLETION_2026-07-05.md`

reviewerOwnedClosurePaths: completion review, accepted worker-owned source/test/worker-return paths, and session-sync surfaces if T22 is accepted.

Reviewer must not convert T22 into production memory/RAG route release,
file-backed persistence, retrieval, vectorization, private-output content read,
provider/live proof, public-sync, Web/UI, app, legal/use-case, or production
workflow-chain readiness.

## Review Gate

Reviewer must reject or repair within scope if focused tests are stale, command
evidence is missing, provider-local files remain undisclosed, Python files were
edited, production route claims appear, or T22 bypasses the accepted T20 helper.

## Closure Checklist

- T22 helper and tests are limited to allowed paths.
- Required verification commands are current after final edit.
- Worker return satisfies worker-return fast gate.
- Production memory/RAG route release remains held.
- Provider-local and Pylance/static-analysis boundaries are dispositioned.

## Return-To-Orchestrator Conditions

Return to orchestrator if implementation requires forbidden paths, private
content, provider/live proof, file-backed production persistence, root export
edits, public-sync, or a source fact contradicts the T21/T20 chain.

## Operator Checkpoint

operator.checkpoint.waiver: No additional checkpoint is required for the bounded
T22 helper/test tranche unless a Return-To-Orchestrator condition is hit.

## Acceptance Criteria

| ID | Criteria |
|---|---|
| AC1 | Worker creates the T22 helper and focused tests only inside allowed TypeScript paths |
| AC2 | T22 helper enforces explicit memory-owner authorization before invoking T20 helper |
| AC3 | T22 helper preserves R27 five-prerequisite, R24-T4 privacy, no-reinjection, and no-raw-memory-release invariants |
| AC4 | Tests include successful in-process candidate behavior and negative tests for authorization, provenance, R27, and private-output invariant failures |
| AC5 | Worker return records exact command evidence rerun after final edit, git status with untracked files, no provider-local stray artifacts, Pylance/static-analysis boundary, and no-commit status |
| AC6 | Worker return preserves `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22` and makes no production route claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T22 dispatch is private provenance work and does not update the
public-sync clone.

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NO_EXTERNAL_INTAKE_LOCAL_GOVERNED_ARTIFACTS_ONLY |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | dispatcher-owned T22 work order; no external-agent source is consumed |
| Disposition | No external knowledge is required or authorized for T22 |
| Claim boundary | External routing accounting only; T22 uses governed local T21/T20/R27/R24 sources |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | T22 bounded memory/RAG route release implementation-candidate work order |
| claimDisposition | CLAIM_REJECTED for execution-control, interception, provider, public, production workflow-chain, and production memory/RAG route claims |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created by this work order |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed by this work order |
| invocationBoundary | local worker execution of allowed source/test edits only after dispatch |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | bounded dispatch authorization only |
| forbiddenExpansion | runtime enforcement, provider/live proof, public-sync, production route release, private-output reads, and workflow-chain readiness remain out of scope |

## Claim Boundary

This work order authorizes bounded worker execution only. It does not prove
worker completion, production memory/RAG route release, private-output content
handling, provider/live behavior, public readiness, or workflow-chain
production readiness.
