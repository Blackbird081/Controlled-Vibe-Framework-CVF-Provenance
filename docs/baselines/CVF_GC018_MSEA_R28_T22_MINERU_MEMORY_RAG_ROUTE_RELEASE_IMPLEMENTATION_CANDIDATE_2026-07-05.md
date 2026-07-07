# CVF GC-018 - MSEA-R28-T22 MinerU Memory/RAG Route Release Implementation Candidate

Memory class: POINTER_RECORD

Status: DISPATCH_READY

rawMemoryReleased: false

Date: 2026-07-05

dispatchBaseHead: 1181a46ee
executionBaseHead: 1181a46ee
closureBaseHead: REVIEWER_SET_AFTER_WORKER_RETURN
Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Authorize a bounded implementation-candidate tranche for a MinerU memory/RAG
route release helper in the Learning Plane foundation. T22 may create a focused
TypeScript helper and tests that verify explicit memory-owner authorization,
R27 five-prerequisite preservation, and R24-T4 privacy invariants before calling
the accepted T20 durable-store invocation helper in an in-process test scope.

T22 does not authorize production memory/RAG route release, file-backed
production persistence, retrieval, vectorization, MinerU runtime execution,
private/generated content reads, provider/live proof, public-sync, Web/UI,
standalone app work, legal/use-case deep dive, document-truth claims,
extraction-accuracy claims, legal-quality claims, current-law correctness
claims, workflow-chain production-readiness claims, worker commit, or push.

## Proposed Tranche

| Field | Disposition |
|---|---|
| tranche | MSEA-R28-T22 |
| worker scope | bounded Learning Plane TypeScript helper/test implementation |
| implementation class | memory/RAG route release candidate, not production route wiring |
| release boundary | in-process candidate behavior only; production route release remains held |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| T21 route decision | Material commit `6ce339437` accepted T21 worker return; session-sync commit `1181a46ee` updated the next move to T22 authoring | SATISFIED_FOR_T22_DISPATCH |
| T21 selected route | `docs/reference/CVF_MSEA_R28_T21_MINERU_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-05.md` lines 95-128 select T22 and state T22 constraints | SATISFIED_FOR_T22_DISPATCH |
| T20 bounded helper | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` lines 1-10 and 105-399 define invocation-only helper behavior | SATISFIED_FOR_T22_DISPATCH |
| R27 memory/RAG route prerequisite | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` lines 77-87 require receipt, quality, source pointer, downstream-use status, claim boundary, fresh GC-018, and memory owner work order | SATISFIED_BY_THIS_FRESH_BASELINE_AND_WORK_ORDER |
| R24-T4 privacy policy | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` lines 53-64 and 212 keep private/generated output content out of successor routing unless separately authorized | SATISFIED_FOR_PRIVACY_BOUNDARY |

## Scope

Allowed worker-owned paths:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-memory-rag-route-release.test.ts`
- `docs/reviews/CVF_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_WORKER_RETURN_2026-07-05.md`

Forbidden paths and surfaces:

- Python source/tests, including the existing Pylance-diagnostic test file;
- provider-local files such as `.qwen/settings.json` and any IDE settings;
- root package exports, public-sync clone, session state, active handoff,
  generated aggregates, private/generated MinerU output content, and any
  file-backed durable store output file.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; dispatchBaseHead; executionBaseHead; closureBaseHead; Source Verification Block; New Doc-Only Fields; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Worker Output Quality Controls; Provider-Local Stray Artifact Control; Pylance Static-Analysis Diagnostic Boundary; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition |
| gateRunPurpose | confirmation evidence before dispatch; checker execution is not first discovery |
| claimBoundary | checker read-ahead evidence only; no worker execution, MinerU runtime, private-output, provider/live, public, production memory/RAG route, source/test implementation, or production-readiness claim |

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
| manualEditsAfterScaffold | Authored T22 source verification, ADIF disclosure, worker-output quality controls, provider-local/Pylance boundaries, handoff controls, and claim boundary from current T21/T20 evidence |
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

## Worker Output Quality Controls

The worker must include a self-audit section in the worker return that records:

- exact focused commands rerun after the final source/test edit;
- `git status --short --untracked-files=all` after writing the worker return;
- no unexpected provider-local or IDE side-channel files;
- disposition for the known Python Pylance/static-analysis warning without
  editing Python source/tests;
- at least one negative test for missing memory-owner authorization;
- at least one negative test for R27 or private-output invariant failure.

## Provider-Local Stray Artifact Control

Provider-local and IDE side-channel files are not CVF source authority and are
not worker deliverables. If provider/model switching creates a local file such
as `.qwen/settings.json`, the worker must remove it before return or disclose it
as local-only and unstaged in the worker return. The worker must not commit,
stage, cite, or promote such files as evidence.

## Pylance Static-Analysis Diagnostic Boundary

| Diagnostic surface | T22 disposition |
|---|---|
| IDE may flag missing import for the Python receipt-writer test | Record as static-analysis path issue if still visible |
| Python source/test edit | Forbidden in T22 |
| New TypeScript helper/test import issue | Must be fixed inside the allowed T22 TypeScript paths |

## Acceptance Criteria

| ID | Criteria |
|---|---|
| AC1 | New T22 helper cross-checks explicit memory-owner authorization with `policyDecision`, `actorAuthorized`, `provenanceScore`, actor role, and target durable tier before invoking the T20 helper |
| AC2 | Helper preserves `outputContentRead: false`, `rawMemoryReleased: false`, `canReinject: false`, `summaryOnly: true`, and all five R27 prerequisites |
| AC3 | Helper calls `invokeMineruDurableStoreWrite` only after the T22-specific authorization gate passes |
| AC4 | Focused tests cover a successful in-process candidate route, missing authorization fail-closed behavior, R27 prerequisite failure, private-output invariant failure, and production/file-backed route non-authorization |
| AC5 | Worker return records current focused test evidence, `npm run check`, `git status --short --untracked-files=all`, provider-local no-stray evidence, Pylance/static-analysis disposition, and no-commit status |
| AC6 | T22 keeps production memory/RAG route release held by `MEMORY_RAG_ROUTE_RELEASE_NOT_PRODUCTION_AUTHORIZED_BY_T22` |

## Verification Commands

Worker must run, from `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`:

```bash
npm test -- mineru-memory-rag-route-release.test.ts
npm run check
```

Worker must also run from repository root:

```bash
git diff --name-status
git status --short --untracked-files=all
```

No MinerU runtime command, provider/live proof, private/generated content read,
public-sync command, file-backed production persistence proof, or push is
authorized.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
|---|---|
| route | MULTI_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher authors packet; worker executes under WORKER_MUST_NOT_COMMIT; reviewer/closer converts accepted return into closure and commit |
| phase | DISPATCH |
| baseHeadFor(phase) | dispatchBaseHead=`1181a46ee`; executionBaseHead=`1181a46ee`; closureBaseHead=`REVIEWER_SET_AFTER_WORKER_RETURN` |
| changedSetScope(phase) | dispatch changes only this GC-018 and paired T22 work order |
| traceScope(phase, actor) | dispatcher records source verification, ADIF disclosure, checker read-ahead, provider-local/Pylance controls, and clean-worktree evidence; worker records execution commands and changed files; reviewer records closure diff and commit steward results |
| commitOwner(phase) | dispatcher owns dispatch commit; worker owns no commit; reviewer/closer owns accepted material and session-sync commits |
| crossBatchIsolation | Before status evidence: `git rev-parse --short HEAD` returned `1181a46ee`; `git status --short --untracked-files=all` was empty before T22 authoring |
| nextMoveSurfaces | dispatcher does not update session state until dispatch commit; reviewer/closer updates session surfaces after accepted worker return |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R28_T22_MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_CANDIDATE_COMPLETION_2026-07-05.md`

reviewerOwnedClosurePaths: completion review, accepted worker-owned source/test/worker-return paths, and session-sync surfaces if T22 is accepted.

Reviewer must not convert T22 into production memory/RAG route release,
file-backed persistence, retrieval, vectorization, private-output content read,
provider/live proof, public-sync, Web/UI, app, legal/use-case, or production
workflow-chain readiness.

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
| Owner surface | dispatcher-owned T22 baseline; no external-agent source is consumed |
| Disposition | No external knowledge is required or authorized for T22 |
| Claim boundary | External routing accounting only; T22 uses governed local T21/T20/R27/R24 sources |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | T22 bounded memory/RAG route release implementation-candidate dispatch |
| claimDisposition | CLAIM_REJECTED for execution-control, interception, provider, public, production workflow-chain, and production memory/RAG route claims |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created by this dispatch baseline |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed by this dispatch baseline |
| invocationBoundary | local worker execution of allowed source/test edits only after dispatch |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | bounded dispatch authorization only |
| forbiddenExpansion | runtime enforcement, provider/live proof, public-sync, production route release, private-output reads, and workflow-chain readiness remain out of scope |

## Claim Boundary

This baseline authorizes a bounded worker tranche only. It does not claim that
the worker has executed T22, that production memory/RAG route release is live,
that any private/generated MinerU output content was read, that provider/live
governance behavior was proven, or that the workflow chain is production-ready.
