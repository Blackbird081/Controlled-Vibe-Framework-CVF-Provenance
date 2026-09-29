# CVF Agent Work Order - MSEA R46 MinerU ScanLayer Memory Bounded Live System Chain Proof

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

rawMemoryReleased=false

Batch ID: MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF

Dispatch base head: b35a809f0

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: bounded implementation worker role

Reviewer/closer: reviewer/closer role

Worker return path: `docs/reviews/CVF_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_WORKER_RETURN_2026-07-06.md`

## Dispatch Prompt Envelope

Role: bounded implementation worker for MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_2026-07-06.md`

Paired GC-018 baseline: `docs/baselines/CVF_GC018_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_2026-07-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: artifact date is 2026-07-06; dispatch base head is `b35a809f0`.

Do-not-misread notes: this packet authorizes a bounded proof of the CVF MinerU summary-only foundation chain. It does not authorize production Memory/RAG release, use-case/legal workflow, private/generated MinerU output content reads, extraction accuracy claims, document truth claims, public-sync, broad live-provider benchmarking, or standalone application work.

Required first actions: read required startup files, guard orientation, literal gotchas, this packet, paired GC-018 baseline, current source/test files named in the Source Verification Block, and checker source listed in the Checker Source Read-Ahead Block before writing runtime or review artifacts.

Return contract: implement only the allowed source/test/evidence changes, run deterministic and live proof commands with secret-safe diagnostics, create the worker return artifact, run required gates, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Create and prove a bounded live system-chain path for MinerU summary-only metadata into file-backed durable memory and read-back through the governed memory interface, then use a live Alibaba-compatible provider call to verify the resulting proof packet without exposing secrets or raw private output.

## Authority Chain

| Authority source | Role in this dispatch |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Current front-door continuity and R45 stop/reopen context |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical active mode, active handoff, and session state |
| `AGENT_HANDOFF_V37_2026-07-06.md` | Active handoff named by the state registry |
| `docs/reference/guard_orientation/README.md` | Guard routing for dispatch and worker execution |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format guardrails |
| `docs/roadmaps/CVF_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_ROADMAP_2026-07-06.md` | Roadmap objective and claim boundary |
| `docs/baselines/CVF_GC018_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_2026-07-06.md` | Paired GC-018 authorization baseline |
| Current source files named in Source Verification Block | Runtime/source evidence for allowed implementation surface |

## Agent Roles

| Role | Responsibility | Commit authority |
| --- | --- | --- |
| Dispatcher | Author roadmap, GC-018 baseline, and work order | May commit dispatch artifacts if gates pass |
| Worker | Implement bounded proof harness, tests, evidence artifact, and worker return | WORKER_MUST_NOT_COMMIT |
| Reviewer/closer | Review evidence, run closure gates, decide acceptance, and own material/session-sync commits | Reviewer-owned |
| Operator | Owns any future production, public, use-case, or broad live-run release decision | N/A |

## Dependency Release Evidence

| Dependency | Required evidence | Refreshed evidence | Disposition |
| --- | --- | --- | --- |
| R45 stop decision | Bounded internal candidate may reopen only by explicit operator authorization | Operator requested completing the proposed bounded live system-chain roadmap and allowed API-key live evidence | SATISFIED |
| File-backed persistence implementation | Existing route candidate must already support file-backed write behavior with route-local actor role | Current route source and tests include file-backed persistence mode, OPERATOR/GOVERNOR actor role behavior, and production route false invariant | SATISFIED |
| Live provider proof boundary | Live proof must use operator key secret-safely and must not print raw keys | Existing live Alibaba test pattern loads env aliases and local env file without printing raw key values | SATISFIED |
| Use-case/legal hold | Proof must stay foundation-chain only | Roadmap and this work order forbid use-case/legal workflow and domain-specific correctness claims | SATISFIED |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF --title "MSEA R46 MinerU ScanLayer Memory Bounded Live System Chain Proof" --date 2026-07-06 --base b35a809f0 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch reference profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Authored R46 purpose, dependency evidence, source verification, ADIF disclosure, handoff control, allowed scope, fulfillment manifest, verification commands, claim boundary, and public export disposition |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| docOnlyNewFields | MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF; R46_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_PASS |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly by reading the failing checker source and matching the literal required shape. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, live-provider diagnostic blocker, or missing authority that makes completion impossible.

## Required First Reads

| Required read | Purpose |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | Session front door |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | Compact state read |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Canonical current mode and handoff routing |
| `AGENT_HANDOFF_V37_2026-07-06.md` | Current governed continuity |
| `docs/reference/guard_orientation/README.md` | Guard orientation |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | Literal-format failure prevention |
| this work order and paired GC-018 baseline | Dispatch authority |
| source and test files listed in Source Verification Block | Runtime/source authority |
| checker files listed in Checker Source Read-Ahead Block | Output-shape authority |

## Pre-Flight Checks

| Check | Required worker evidence |
| --- | --- |
| Execution base | Record `git rev-parse --short HEAD` before implementation |
| Clean worktree | Record `git status --short --untracked-files=all` before implementation |
| Required reads | List startup, guard, dispatch, source, test, and checker files actually read |
| Scope confirmation | Confirm only Work-Order Fulfillment Manifest paths are changed |
| Provider-local hygiene | Confirm no provider-local stray files or IDE config changes were created |

## Write Ownership

| Field | Value |
| --- | --- |
| commitMode | WORKER_MUST_NOT_COMMIT |
| workerWrites | Allowed Scope paths only |
| reviewerWrites | Material acceptance commit and session-sync surfaces during reviewer closure |
| forbiddenWrites | Public-sync, private/generated output, provider-local config, unrelated source/tests |

## Execution Plan

1. Capture execution base and clean worktree evidence.
2. Add bounded proof source harness.
3. Add deterministic and live provider tests.
4. Add corpus registry entries and regenerate corpus registry if required.
5. Run package check, deterministic test, live test, and pre-implementation gate.
6. Create worker return with evidence, diagnostics, changed files, and claim boundary.

## Evidence Requirements

Evidence must include deterministic test output, live proof output or diagnostic, evidence JSON path, package check output, corpus registry generation result, pre-implementation gate result, worker-return gate result if run, no-secret statement, provider-local hygiene statement, and final git status.

## Review Gate

Reviewer/closer must verify manifest match, inspect evidence JSON for secret safety, run required closure gates, and reject any production/public/use-case/private-output overclaim.

## Closure Checklist

| Item | Required closure state |
| --- | --- |
| Dispatch artifacts | Checked, gated, and committed or included in material closure |
| Source/test/evidence artifacts | Checked against Allowed Scope |
| Live proof | PASS or blocked by recorded diagnostic |
| Public export disposition | DEFERRED_PRIVATE_ONLY |
| Session continuity | Updated during material acceptance |

## Return Conditions

Return `COMPLETE_PENDING_REVIEW` when implementation, tests, live proof or diagnostic, worker return, and required gates are complete with no worker commit. Return `BLOCKED_WITH_REASON` when completion would require forbidden scope or live proof fails with a non-retryable diagnostic.

## Operator Checkpoint

Future production release, public-sync, hosted release, private-output read, use-case/legal workflow, or broad provider benchmark requires a fresh operator decision in a later tranche.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap objective | Required implementation | R46 handling |
| --- | --- | --- |
| Synthetic MinerU summary-only write | Add a source harness that builds a summary-only route input and uses file-backed durable memory | Allowed source path includes a new bounded proof harness |
| File-backed persistence and read-back | Reopen the same file-backed durable memory path and read via durable store API | Deterministic test must assert write receipt, read receipt, record count, and summary hash evidence |
| Live provider proof | Use Alibaba-compatible live call with safe evidence artifact | Live test must load keys secret-safely, persist only hashes/booleans/tokens, and capture diagnostic on failure |
| Stop boundary preservation | Keep production/public/use-case/private-output claims closed | Acceptance requires `productionRouteAuthorized=false`, `rawMemoryReleased=false`, `privateOutputContentRead=false`, and `canReinject=false` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring dispatch live proof runtime test`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring dispatch live proof runtime test" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | Worker must still use source verification, exact allowed scope, live-run diagnostics, provider-local hygiene, and no-overclaim evidence |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Source Verification Block; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; DISPATCH_READY; ACCEPT; EXISTS; VALUE_SET; RUNTIME_BEHAVIOR; DOC_ONLY_NEW; N/A with reason |
| gateRunPurpose | Confirmation after source-read authoring; gate runs are evidence and not first discovery for packet shape |
| claimBoundary | Read-ahead covers dispatch artifact shape only; it does not prove implementation behavior, live provider behavior, or production readiness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| File-backed durable memory store constructor exists | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 105 | `createFileBackedDurableMemoryStore` | Durable memory store | ACCEPT |
| Durable memory store exposes write and read operations | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 90-91 | `write`; `read` | `DurableMemoryStore` | ACCEPT |
| Durable memory store implements write behavior | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 195 | `write` | `DurableMemoryStore` | ACCEPT |
| Durable memory store implements read behavior | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | line 308 | `read` | `DurableMemoryStore` | ACCEPT |
| Route candidate supports file-backed persistence mode | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 46 | `MineruSystemChainPersistenceMode` | MinerU system-chain route candidate | ACCEPT |
| Route authority exposes route-local actor role for file-backed persistence | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 60 | `fileBackedPersistenceActorRole` | `MineruSystemChainRouteAuthority` | ACCEPT |
| Route candidate keeps production route unauthorized | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 74, 89, 200, and 212 | `productionRouteAuthorized` | MinerU system-chain route candidate result | ACCEPT |
| Route candidate rejects retrieval and private output content reads | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 168 and 182 | `retrievalRequested`; `privateOutputContentRead` | `buildMineruSystemChainRouteCandidate` | ACCEPT |
| Focused tests already prove file-backed route behavior with OPERATOR and GOVERNOR actor roles | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | lines 401-447 | `fileBackedPersistenceActorRole` | MinerU system-chain route candidate tests | ACCEPT |
| Existing MinerU live test loads operator keys from safe env aliases and local env file | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-live.alibaba.test.ts` | lines 10-55 | `loadLocalEnv`; `DASHSCOPE_API_KEY` | MinerU Alibaba live test | ACCEPT |
| Existing MinerU live test uses Alibaba DashScope compatible endpoint and `qwen-turbo` | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-live.alibaba.test.ts` | lines 10-11 | `ENDPOINT`; `MODEL` | MinerU Alibaba live test | ACCEPT |

## New Doc-Only Fields

| Field | Owner artifact | Purpose | Runtime/source status |
| --- | --- | --- | --- |
| `MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF` | This work order and paired baseline | Batch identifier for the bounded proof lane | DOC_ONLY_NEW |
| `R46_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_PASS` | Proposed source/test proof result token | New bounded proof disposition literal | DOC_ONLY_NEW |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | Dispatcher authors packet; implementation worker executes; reviewer/closer reviews and commits if accepted |
| phase | dispatch |
| baseHeadFor(phase) | dispatchBaseHead=b35a809f0; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | Worker may edit only paths listed in Work-Order Fulfillment Manifest |
| traceScope(phase, actor) | Worker return must record commands, cwd, changed files, deterministic test results, live proof result or diagnostic, gate results, pending status, and manifest match |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | Before status evidence must be clean worktree or disclose only owned pending paths; unrelated provider-local or IDE files must be removed or disclosed as blockers; before status evidence: `git status --short` (empty) and `git status --short --untracked-files=all` (empty) before R46 dispatch authoring |
| nextMoveSurfaces | Reviewer/closer owns session state, front door, active handoff, and next-move sync after acceptance |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_COMPLETION_2026-07-06.md` |
| reviewerOwnedClosurePaths | Worker return, allowed source/test/evidence paths, corpus registry entries if required, active session state source fragments, generated active session state, active handoff, and session memory front door |
| closureOwner | reviewer/closer role |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| routeMode | SINGLE_AGENT_SINGLE_ROLE |
| intakeSummary | Operator requested completion of the bounded live system-chain roadmap following the R45 stop decision |
| scopeClassification | Bounded foundation-chain source/test/live proof |
| riskSensitivity | Medium governance risk because live provider keys and persistence evidence are involved |
| selectedRoleRoute | routeMode SINGLE_AGENT_SINGLE_ROLE; implementation worker executes and reviewer/closer owns closure |
| roleSeparationBasis | Worker must not commit; reviewer/closer owns closure decision and session-sync |
| dispatcherRole | dispatcher role |
| workerRole | bounded implementation worker role |
| reviewerRole | reviewer/closer role |
| authorityCheckpoint | SATISFIED: operator explicitly authorized bounded live proof and API-key use for evidence |
| escalationCondition | Stop and return BLOCKED if completion needs private output, production release, public-sync, use-case/legal workflow, raw secret exposure, or broad provider benchmarking |
| claimBoundary | Role routing only; no production/public/use-case/provider-readiness claim |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: R46 uses CVF-governed artifacts and runtime source, not external knowledge absorption |
| Matching local-view guard | N/A with reason: no external knowledge intake event occurred |
| Owner surface | This work order and paired GC-018 baseline |
| Disposition | NOT_APPLICABLE_WITH_REASON: no external source is promoted to CVF authority |
| Claim boundary | Routing evidence only; no outside-source absorption is authorized |

## Agent Operation Trace Block

| Field | Value |
| --- | --- |
| Actor | dispatcher role |
| Provider or surface | local repository tool surface |
| Session or invocation | R46 dispatch authoring |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `apply_patch`; `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b35a809f0 --head HEAD` |
| Target paths | This work order, paired GC-018 baseline, paired roadmap |
| Allowed scope source | Operator authorization plus paired roadmap |
| Before status evidence | clean worktree; `git status --short` (empty) and `git status --short --untracked-files=all` (empty) before R46 dispatch authoring |
| After status evidence | To be refreshed by worker and reviewer during implementation closure |
| Diff evidence | `git diff --name-status` to be refreshed by worker and reviewer |
| Approval boundary | Operator authorized bounded live proof; production/public/use-case remains forbidden |
| Claim boundary | Dispatch trace only; no runtime/live behavior claim |
| Agent type | local implementation worker and reviewer/closer role separation |
| Invocation ID | R46_DISPATCH_AUTHORING |
| Expected manifest | Work-Order Fulfillment Manifest paths only |
| Actual changed set | To be refreshed by worker and reviewer |
| Manifest delta | To be refreshed by worker and reviewer |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | Bounded internal MinerU summary-only system-chain proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT through durable memory write/read receipts and safe evidence JSON |
| actionEvidence | ACTION_EVIDENCE_PRESENT through focused deterministic and live proof commands |
| invocationBoundary | One local test invocation and one Alibaba-compatible provider proof invocation |
| interceptionBoundary | N/A with reason: R46 does not claim direct interception or universal agent execution control |
| claimLanguage | Passing R46 proves bounded internal chain behavior only |
| forbiddenExpansion | No production/public/use-case/private-output/extraction-accuracy expansion |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| durableFoundationFilesCreated | N/A with reason: no durable governance foundation file split or relocation is authorized |
| runtimeStorageTouched | Test-only temporary file-backed durable memory path and evidence JSON only |
| indexOrRegistryTouched | Corpus scan registry entries may be added for new extension source/test paths |
| storageBoundary | No production memory database, private output store, public-sync store, or provider-local store is authorized |

## Allowed Scope

The worker may edit only:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-bounded-live-system-chain-proof.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-bounded-live-system-chain-proof.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-bounded-live-system-chain-proof.alibaba.test.ts`
- `docs/reviews/evidence/CVF_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_2026-07-06.json`
- `docs/reviews/CVF_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_WORKER_RETURN_2026-07-06.md`
- `docs/corpus-intelligence/registry/entries/msea-r46-mineru-bounded-live-system-chain-proof-source.json`
- `docs/corpus-intelligence/registry/entries/msea-r46-mineru-bounded-live-system-chain-proof-tests.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

Implementation requirements:

- Use synthetic summary-only MinerU metadata.
- Use file-backed durable memory for write and read-back proof.
- Re-open or re-create the file-backed store from the same path before read-back.
- Preserve `productionRouteAuthorized=false`.
- Preserve `rawMemoryReleased=false` and `canReinject=false` receipt boundaries.
- Keep `privateOutputContentRead=false`, retrieval off, and vectorization off.
- Persist only secret-safe evidence: hashes, booleans, model name, endpoint host, route tokens, receipt decisions, and diagnostic class if failure occurs.
- If the live provider call fails, record a secret-safe diagnostic before any rerun.

## Forbidden Scope

The worker must not:

- run broad MinerU OCR/model extraction or read private/generated MinerU output content;
- claim extraction accuracy, document truth, legal quality, current-law correctness, public readiness, hosted readiness, or production Memory/RAG readiness;
- add public-sync artifacts, push to public repository, or update public catalog;
- add use-case/legal workflow logic;
- print or commit raw API keys, provider secrets, raw private output, or `.env.local` contents;
- create provider-local stray files such as `.qwen/settings.json`;
- modify unrelated source, tests, Web/UI, dashboard, session state, handoff, or public-sync files outside reviewer closure sync.

## Work-Order Fulfillment Manifest

| Artifact | Required action | Disposition requirement |
| --- | --- | --- |
| New bounded proof source | Add file-backed write/read-back harness with bounded proof result | Required |
| Deterministic test | Prove write receipt, read receipt, record count, summary hash, and no production/private-output boundary | Required |
| Live Alibaba-compatible test | Prove provider call consumes secret-safe proof packet and evidence artifact is written | Required unless secret-safe diagnostic records provider/key/service blocker |
| Evidence JSON | Persist only safe hashes/booleans/tokens/model/endpoint/diagnostic data | Required |
| Corpus registry entries | Register new extension source/test paths if GC-051 path-literal discipline requires it | Required |
| Worker return | Record changed files, commands, gate results, live proof evidence, and claim boundary | Required |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Before writing the worker return, read checker source for the review path family and conditional content class. The worker return must include Purpose, Target / Source, Scope / Methodology, Findings / Position, Risk / Corrective Action, Decision / Disposition, External Knowledge Intake Routing, Epistemic Process Block, Agent Operation Trace Block, Delta Execution Claim Boundary Control Block, Public Export Disposition, verification commands, changed files, provider-local hygiene, no-secret statement, and git status.

## Verification Commands

Required commands:

- `git rev-parse --short HEAD`
- `git status --short --untracked-files=all`
- `npm run check` from `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`
- `npx vitest run tests/mineru-bounded-live-system-chain-proof.test.ts` from `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`
- `npx vitest run tests/mineru-bounded-live-system-chain-proof.alibaba.test.ts` from `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`, with `CVF_MSEA_R46_EVIDENCE_PATH` set to the evidence JSON path
- `python governance/compat/generate_corpus_scan_registry.py`
- `python governance/compat/run_worker_return_fast_gate.py`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b35a809f0 --head HEAD`

## Acceptance Criteria

| Criterion | Evidence |
| --- | --- |
| Deterministic proof passes | Focused Vitest command passes |
| Live provider proof passes or has secret-safe blocker diagnostic | Live Vitest command passes and writes evidence JSON, or worker return records diagnostic class and no rerun loop |
| File-backed memory was used | Evidence JSON records `fileBackedPersistenceUsed=true` and read-back record count greater than zero |
| Production boundary held | Evidence JSON and tests record `productionRouteAuthorized=false` |
| Private-output boundary held | Evidence JSON and tests record `privateOutputContentRead=false` |
| Receipt boundaries held | Evidence JSON and tests record `rawMemoryReleased=false` and `canReinject=false` |
| Secret hygiene held | Worker return records no raw key output, no `.env.local` copy, and no provider-local stray files |

## Claim Boundary

R46 may close only as a bounded internal system-chain proof. A passing R46 proves that the current CVF MinerU summary-only foundation chain can write a synthetic record to file-backed durable memory, read it back through the governed memory interface, and present a secret-safe proof packet to a live provider. It does not prove production Memory/RAG readiness, public release readiness, extraction accuracy, document truth, legal/current-law correctness, or use-case workflow readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance work order for bounded internal proof. No public-sync artifact, public catalog update, public remote proof, or exported public path is authorized by this work order.
