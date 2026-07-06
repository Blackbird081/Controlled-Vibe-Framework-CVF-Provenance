# CVF Agent Work Order - MSEA R40 T1 MinerU System Chain Provider Live Proof

Memory class: governed-work-order

Status: DISPATCH_READY

Created: 2026-07-06

rawMemoryReleased: false

## Dispatch Prompt Envelope

dispatchId: MSEA-R40-T1-MINERU-SYSTEM-CHAIN-PROVIDER-LIVE-PROOF

route: WORKER_MUST_NOT_COMMIT

taskClass: Runtime / provider / live proof

role: worker

dispatchBaseHead: `4e917ebb6`

executionBaseHead: WORKER_CAPTURE_AT_START

closureBaseHead: REVIEWER_SET_AT_CLOSURE

Commit mode: WORKER_MUST_NOT_COMMIT

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_2026-07-06.md`

Current-time notes: Artifact date is 2026-07-06. The operator selected the
provider/live proof lane for the existing MinerU system-chain foundation and
confirmed DashScope-compatible API keys are available.

Do-not-misread notes: This packet authorizes one bounded live provider proof
over summary-only MinerU harness context. It does not authorize MinerU runtime
execution, private/generated output reads, production Memory/RAG route release,
file-backed persistence, retrieval, vectorization, public-sync, worker commit,
push, public claim, extraction accuracy, document truth, legal quality,
current-law correctness, not hosted readiness, and not production readiness.

Required first actions: read this work order, paired GC-018 baseline,
mandatory startup files, guard orientation, and literal gotchas. Recompute
source anchors before writing or running the live proof.

Return contract: create the focused live test and worker-return artifact, run
the deterministic MinerU test set, run the focused live test with secret-safe
key loading, record secret-safe diagnostics for any live failure before any
rerun, record final `git status --short --untracked-files=all`, and stop for
reviewer closure. Do not commit.

workerTargetPaths:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-live.alibaba.test.ts`

workerReturnPath:

- `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_WORKER_RETURN_2026-07-06.md`

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py` read as the required helper surface; packet was manually authored for R40-T1 |
| generatedProfile | work order / source-verified dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Manual source-verified authoring for MinerU system-chain provider-live proof lane |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| docOnlyNewFields | `Scaffold Provenance Block` |
| claimBoundary | Dispatch scaffold provenance only; no runtime, private-output read, production release, public-sync, worker commit, push, or public claim |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| intake summary | Operator asked to reuse existing MinerU test cases for the system chain and run a live proof with available API keys |
| scope classification | Bounded provider/live proof for existing MinerU summary-only system-chain harness |
| risk sensitivity | High: live provider proof can be misread as production release or extraction-quality proof |
| selected role route | routeMode: MULTI_AGENT_SINGLE_ROLE |
| role separation basis | Dispatcher authors GC-018/work order; worker creates live test and worker return without commit; reviewer/closer owns closure and material commit |
| escalation condition | Return to orchestrator if live proof would need private/generated output reads, MinerU runtime execution, production release, file-backed persistence, retrieval, vectorization, public-sync, or raw API key disclosure |

## Worker Autonomy / No-Question Rule

The worker may proceed without asking wording or preference questions. The
worker must repair allowed-scope checker failures directly by reading the
failing checker source and matching the literal required shape.

The worker must stop and return `BLOCKED_WITH_REASON` if a live proof cannot
be run secret-safely or if the proof would need to cross any forbidden scope.

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Dispatcher | Authored this GC-018/source-verified R40-T1 work order and paired baseline |
| Worker | Adds the focused live test, runs deterministic and live proof commands, writes worker return, and does not commit |
| Reviewer/closer | Reviews output, verifies diagnostics and gates, repairs only within scope if needed, and owns material closure commit |
| Session-sync steward | Updates session surfaces only when reviewer acceptance changes current mode or next allowed move |

## Purpose

Create and execute a bounded live provider proof that the existing MinerU
internal system-chain harness can supply summary-only context to a live
Alibaba/DashScope model without releasing raw memory, private/generated MinerU
output, or production Memory/RAG behavior.

## Authority Chain

| Authority | Role in R40-T1 |
| --- | --- |
| Operator instruction on 2026-07-06 | Selects the provider/live proof lane and confirms API keys are available |
| Paired GC-018 baseline | Authorizes bounded provider-live proof dispatch |
| R38 T4 release-gate decision | Names provider/live proof as one held authority lane requiring a fresh packet |
| R39 T1 decision matrix | Confirms provider/live proof remains held until a dedicated provider/live proof packet is accepted |
| R30 T4 decision | Prior provider/runtime proof was unreleased before this fresh packet |
| Current MinerU harness source | Provides the summary-only system-chain harness and no-runtime/no-private-output invariants |
| Existing Alibaba live test | Provides secret-safe key loading and DashScope-compatible call pattern |
| ADIF-0024 | Requires final command rerun and workspace hygiene disclosure |

## Roadmap-To-Work-Order Trace Matrix

| Driver | Work-order requirement | Disposition |
| --- | --- | --- |
| R38 selected `SYSTEM_FOUNDATION_COMPLETE_STOP` | Do not open more audit-only work | SATISFIED_BY_R40_T1_LIVE_PROOF_PACKET |
| R38 allowed exactly one held authority lane | Scope this work order to provider/live proof only | SATISFIED_BY_OPERATOR_SELECTION |
| R39 preserved provider/live proof hold pending dedicated packet | This packet releases only a bounded proof, not production behavior | SATISFIED_BY_THIS_PACKET |
| Operator requested live run with keys available | Worker may run one focused live DashScope-compatible proof secret-safely | SATISFIED_BY_THIS_PACKET |

## Operator Checkpoint

Operator checkpoint is satisfied for this packet only: the operator explicitly
asked to run live proof and stated API keys are already available.

Any production Memory/RAG route release, file-backed persistence, private
output policy release, public-sync, or use-case/legal workflow still requires
a separate fresh packet.

## Pre-flight Checks

| Check | Required worker evidence |
| --- | --- |
| Worktree before edits | `git status --short --untracked-files=all` from the provenance workspace |
| Dispatch base capture | `git rev-parse --short HEAD` at worker start |
| Source-anchor recompute | Fresh `rg -n` or equivalent source reads for each runtime/source symbol cited in this packet |
| Key availability | Secret-safe existence check for `DASHSCOPE_API_KEY` or accepted Alibaba aliases; do not print values |
| Live failure diagnostics | If the live test fails or times out, record stage, class, retryability, user action, provider/model when known, HTTP status when available, and a safe message before rerun |
| Provider-local hygiene | Inspect and disclose provider-local or IDE side-channel files; do not create, stage, or rely on them as authority |

## Write Ownership

| Surface | Owner |
| --- | --- |
| Focused live test file | Worker may create |
| R40-T1 worker return | Worker may create |
| Existing MinerU source and deterministic tests | Worker may read and run; do not edit unless the new test requires imports only in the new file |
| Session state, handoff, session memory | Not worker-owned |
| Public-sync clone or public catalog | Not worker-owned |
| Provider-local configuration or memory files | Not worker-owned; do not create, stage, or rely on them as authority |

## Required First Reads

Before writing or running live proof, read:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- active handoff named by session state
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- `docs/baselines/CVF_GC018_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_2026-07-06.md`
- this work order
- `docs/reference/CVF_MSEA_R38_T4_MINERU_TO_MEMORY_SCANLAYER_RELEASE_GATE_DECISION_2026-07-06.md`
- `docs/reference/CVF_MSEA_R39_T1_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md`
- `docs/reference/CVF_MSEA_R30_T4_MINERU_PROVIDER_RUNTIME_PROOF_BOUNDARY_DECISION_2026-07-05.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-internal-system-chain-harness.test.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/knowledge-graph-live.alibaba.test.ts`

## Mission

Add a focused live Alibaba/DashScope Vitest file that:

- loads a DashScope-compatible key using the existing secret-safe local env pattern;
- runs `runMineruInternalSystemChainHarness()` locally;
- asserts the harness result is `MINERU_INTERNAL_SYSTEM_CHAIN_HARNESS_PASS_BOUNDED`;
- builds a compact summary-only context from harness result fields and hold tokens;
- sends one live model request asking the model to echo the bounded disposition,
  held token, and no-production-release boundary;
- asserts the response contains the bounded PASS token and held token, and does
  not claim production route authorization;
- does not read private/generated MinerU output content and does not execute
  MinerU runtime.

## Allowed Scope

You may create only:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-live.alibaba.test.ts`
- `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_WORKER_RETURN_2026-07-06.md`

You may run:

- `npm run test -- tests/mineru-durable-store-invocation.test.ts tests/mineru-memory-rag-route-release.test.ts tests/mineru-python-receipt-bridge.test.ts tests/mineru-internal-system-chain-harness.test.ts tests/mineru-system-chain-route-candidate.test.ts`
- `python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`
- `npm run test -- tests/mineru-system-chain-live.alibaba.test.ts`
- worker-return and pre-implementation gates required by the current workflow

## Forbidden Scope

Do not:

- edit existing source files, existing tests, generated JSON aggregates,
  session state, active handoff, public-sync files, or provider-local files;
- print, commit, copy, or persist raw API key values;
- run MinerU runtime or read, quote, summarize, copy, import, stage, or commit
  private/generated MinerU output content;
- release production Memory/RAG, production durable-store invocation,
  file-backed persistence, retrieval, vectorization, or reinjection;
- claim extraction accuracy, document truth, legal quality, current-law
  correctness, hosted readiness, public readiness, or production readiness;
- create a public claim, public-sync batch, worker commit, or push.

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Capture execution base and worktree status | `git rev-parse --short HEAD`; `git status --short --untracked-files=all` |
| 2 | Read startup, baseline, work order, held-lane decisions, harness source, and existing live test pattern | Source Inventory in worker return |
| 3 | Recompute source anchors | fresh `rg -n` or equivalent read evidence |
| 4 | Create focused live test | target path under Learning Plane tests |
| 5 | Run deterministic MinerU tests and Python receipt tests | command output |
| 6 | Run focused live test once; if it fails, record secret-safe diagnostic before any rerun | command output and diagnostic |
| 7 | Create worker return | target path under reviews |
| 8 | Run worker-return fast gate and pre-implementation gate | command output |
| 9 | Stop without committing | final `git status --short --untracked-files=all` showing only allowed paths |

## Verification Commands

Worker must run these commands after final edits and record exact
secret-safe output summaries in the worker return:

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
npm run test -- tests/mineru-durable-store-invocation.test.ts tests/mineru-memory-rag-route-release.test.ts tests/mineru-python-receipt-bridge.test.ts tests/mineru-internal-system-chain-harness.test.ts tests/mineru-system-chain-route-candidate.test.ts
python -m pytest EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py
npm run test -- tests/mineru-system-chain-live.alibaba.test.ts
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

If the live test fails, the worker must record a secret-safe diagnostic before
any rerun and must not print raw key values.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R38 T4 allows operator selection of provider/live proof as one held authority lane through a fresh packet | `docs/reference/CVF_MSEA_R38_T4_MINERU_TO_MEMORY_SCANLAYER_RELEASE_GATE_DECISION_2026-07-06.md` | lines 60-64 | `provider/live proof` | R38 release-gate decision | VALUE_SET | ACCEPT |
| R39 T1 states provider/live proof remains held until a dedicated provider/live proof packet is accepted | `docs/reference/CVF_MSEA_R39_T1_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_MATRIX_2026-07-06.md` | lines 98 and 112-114 | `Provider/live proof` | R39-T1 decision matrix | VALUE_SET | ACCEPT |
| R30 T4 selected the prior provider/runtime proof unreleased token | `docs/reference/CVF_MSEA_R30_T4_MINERU_PROVIDER_RUNTIME_PROOF_BOUNDARY_DECISION_2026-07-05.md` | lines 34 and 40 | `R30_PROVIDER_RUNTIME_PROOF_NOT_RELEASED` | R30-T4 provider proof boundary decision | VALUE_SET | ACCEPT |
| MinerU internal system-chain harness exposes bounded PASS result and callable harness function | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | lines 32-33 and 126 | `MINERU_INTERNAL_SYSTEM_CHAIN_HARNESS_PASS_BOUNDED`; `runMineruInternalSystemChainHarness` | MinerU internal system-chain harness | EXISTS | ACCEPT |
| MinerU internal harness result explicitly records no MinerU runtime, private-output read, retrieval, vectorization, provider-live proof use, or public runtime claim | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | lines 47-54 and 151-157 | `MineruInternalSystemChainHarnessResult` | MinerU internal system-chain harness | VALUE_SET | ACCEPT |
| Existing MinerU deterministic system-chain test asserts bounded PASS and no provider-live proof use | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-internal-system-chain-harness.test.ts` | lines 14-34 | `providerLiveProofUsed` | MinerU internal system-chain harness test | RUNTIME_BEHAVIOR | ACCEPT |
| Existing Alibaba live test demonstrates secret-safe `.env.local` loading and DashScope-compatible call pattern | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/knowledge-graph-live.alibaba.test.ts` | lines 10-64 and 99-143 | `resolveAlibabaKey`; `callAlibabaWithKgrContext` | Alibaba live test pattern | EXISTS | ACCEPT |
| Learning Plane package exposes Vitest test command | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/package.json` | scripts section | `test` | package scripts | VALUE_SET | ACCEPT |

## Work-Order Fulfillment Manifest

| Required artifact | Type | Owner | Required proof literal |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-live.alibaba.test.ts` | focused live test | worker | `MINERU_INTERNAL_SYSTEM_CHAIN_HARNESS_PASS_BOUNDED` |
| `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_WORKER_RETURN_2026-07-06.md` | worker return | worker | `COMPLETE_PENDING_REVIEW` |

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must include these literal sections:

- Purpose
- Target / Source
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Decision / Disposition
- Source Inventory
- Source Verification Block
- ADIF Defect Registry Disclosure
- Checker Source Read-Ahead Block
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- External Knowledge Intake Routing
- Public Export Disposition
- Claim Boundary

It must also include `executionBaseHead`, deterministic command evidence,
live command evidence or secret-safe live diagnostic, final
`git status --short --untracked-files=all`, and an explicit no-commit
statement.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R40-T1 dispatch authoring, 2026-07-06 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `Get-Content`; `rg`; `python governance/compat/run_adif_defect_resolver.py`; `apply_patch`; governance dispatch checks |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_2026-07-06.md` |
| Allowed scope source | operator selected MinerU system-chain provider/live proof lane and confirmed API keys are available |
| Before status evidence | HEAD `4e917ebb6`; worktree clean before R40-T1 dispatch artifact authoring |
| After status evidence | R40-T1 dispatch packet pending pre-dispatch gates |
| Diff evidence | `git diff --name-status 4e917ebb6..HEAD` |
| Approval boundary | dispatch authoring only |
| Claim boundary | no live proof has been run by the dispatch packet itself |
| Agent type | dispatcher |
| Invocation ID | `msea-r40-t1-mineru-system-chain-provider-live-proof-dispatch-2026-07-06` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_2026-07-06.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_2026-07-06.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_2026-07-06.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | non-active-handoff central core; archive exception not applicable: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `MULTI_AGENT_SINGLE_ROLE` |
| rolePattern | dispatcher -> worker -> reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`4e917ebb6`; executionBaseHead=worker-captured start HEAD; closureBaseHead=reviewer-set at closure |
| changedSetScope(phase) | dispatch authoring changes only paired GC-018/work order; worker may create only live test and worker return; reviewer owns closure artifacts; session-sync steward owns session surfaces |
| traceScope(phase, actor) | dispatch trace in this work order; worker trace in worker return; reviewer trace in completion review; session-sync trace in active handoff if next move changes |
| commitOwner(phase) | dispatcher owns dispatch commit; worker must not commit; reviewer/closer owns material closure commit; session-sync steward owns session-sync commit |
| crossBatchIsolation | do not mix with production Memory/RAG release, private-output policy, persistence, public-sync, or session-sync |
| nextMoveSurfaces | reviewer/session-sync steward updates only after accepted reviewer closure decision changes current mode or next allowed move |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_COMPLETION_2026-07-06.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_MSEA_R40_T1_MINERU_SYSTEM_CHAIN_PROVIDER_LIVE_PROOF_COMPLETION_2026-07-06.md`
- this work order status and closure package if accepted

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver query:

`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

Returned defects:

- ADIF-0001
- ADIF-0002
- ADIF-0014
- ADIF-0015
- ADIF-0020
- ADIF-0021
- ADIF-0007
- ADIF-0016
- ADIF-0017
- ADIF-0024
- ADIF-0006

Disclosed defectIds:

- ADIF-0001
- ADIF-0002
- ADIF-0014
- ADIF-0015
- ADIF-0020
- ADIF-0021
- ADIF-0007
- ADIF-0016
- ADIF-0017
- ADIF-0024
- ADIF-0006

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Dispatch Prompt Envelope; Source Verification Block; ADIF Defect Registry Disclosure; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation evidence before dispatch; gates confirm packet shape after source and checker read-ahead |
| claimBoundary | checker read-ahead evidence only; no private-output read, production Memory/RAG release, retrieval, vectorization, file-backed persistence, public-sync, worker commit, push, or public claim |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | N/A with reason: R40-T1 is not absorbing external knowledge; it is dispatching a bounded provider-live proof over existing CVF-owned MinerU harness output |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | DEFERRED_EXTERNAL_ABSORPTION_NOT_IN_SCOPE |
| Claim boundary | No external knowledge is promoted to CVF authority; live response may be used only as R40-T1 provider-call evidence |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | Bounded provider-live proof invocation for MinerU system-chain summary-only context |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT until worker records live command output or secret-safe diagnostic in worker return |
| actionEvidence | ACTION_EVIDENCE_PRESENT only after worker creates the focused test and records command output |
| invocationBoundary | One focused DashScope-compatible test invocation; no universal runtime enforcement or governed-coding control claim |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, or mandatory agent-control claim |
| claimLanguage | Use "bounded provider-live proof" only after the focused command passes; do not say production-ready, public-ready, or hosted-ready |
| forbiddenExpansion | No MinerU runtime, private-output read, production Memory/RAG release, retrieval, vectorization, public-sync, worker commit, push, or public claim |

## Foundation Storage Layout Block

| Field | Value |
| --- | --- |
| storageChangeScope | N/A with reason: no docs/reference foundation file, generated aggregate, index, split, relocation, or refactor is authorized |
| durableFoundationFiles | N/A with reason: this packet creates only a work order, paired baseline, one live test, and one worker return |
| indexOrFrontDoorImpact | N/A with reason: no foundation index or front-door update is authorized in worker scope |
| rotationOrSplitPlan | N/A with reason: no touched file is a foundation file requiring rotation or split |
| claimBoundary | Foundation storage layout block is present for guard compatibility only; no durable foundation storage change is authorized |

## Worker Output Quality Controls

| Control | Requirement |
| --- | --- |
| Final rerun | Rerun deterministic and live commands after final edits |
| Static diagnostics | Disclose any Pylance, TypeScript, Vitest, pytest, or lint diagnostic observed in touched paths |
| Provider-local hygiene | Do not leave `.qwen`, IDE side-channel, or provider-local config files; disclose final status with untracked files |
| Live diagnostic | Any failed live run needs secret-safe diagnostic before rerun |
| Negative edge cases | Live test must assert no production authorization claim and no raw/private-output release claim |

## Acceptance Criteria

| ID | Criterion | Evidence |
| --- | --- | --- |
| AC1 | Focused live test exists at the allowed path | git status and file path |
| AC2 | Existing deterministic MinerU tests pass | command output |
| AC3 | Python MinerU receipt/candidate tests pass | command output |
| AC4 | Focused live Alibaba/DashScope test passes with secret-safe key loading | command output with no raw key |
| AC5 | Live response preserves bounded PASS and held-token context | test assertions |
| AC6 | Worker return records diagnostics, command evidence, and final status | worker return |
| AC7 | No forbidden production/private/public/runtime scope is crossed | worker return claim boundary and reviewer inspection |

## Evidence Requirements

| Evidence item | Required disposition |
| --- | --- |
| Execution base | Worker records `git rev-parse --short HEAD` at start |
| Deterministic MinerU tests | Worker records final pass/fail output after edits |
| Python MinerU receipt tests | Worker records final pass/fail output after edits |
| Focused live test | Worker records secret-safe pass output or a secret-safe diagnostic before any rerun |
| Source anchors | Worker recomputes anchors for harness, existing live test pattern, package script, and held-lane decisions |
| Worktree status | Worker records final `git status --short --untracked-files=all` |
| Scope boundary | Worker records no private-output read, no MinerU runtime, no production release, no public-sync, and no worker commit |

## Review Gate

Reviewer must verify that the allowed changed set is limited to the focused
live test and worker return, all command evidence is final-run evidence, no
raw API key or private/generated output content appears, the live response is
not used as production-release authority, and the worker did not commit.

## Closure Checklist

- [x] Work order includes Source Verification Block.
- [x] Work order includes ADIF Defect Registry Disclosure.
- [x] Work order includes Agent Handoff Contract Control Block.
- [x] Work order includes Reviewer Closure Conversion.
- [x] Work order includes External Knowledge Intake Routing.
- [x] Work order includes Delta Execution Claim Boundary Control Block.
- [x] Work order includes Foundation Storage Layout Block.
- [x] Work order includes Scaffold Provenance Block.
- [x] Work order includes Public Export Disposition and Claim Boundary.

## Fail Conditions

- Raw API key printed, copied, committed, or written to a new provider-local file.
- Live proof needs private/generated MinerU output content.
- Live proof runs MinerU runtime or claims extraction/document truth quality.
- Live proof claims production Memory/RAG, file-backed persistence, retrieval,
  vectorization, reinjection, public readiness, or production readiness.
- Worker edits existing source/tests outside the single allowed new test file.
- Worker commits or pushes.

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: R40-T1 is a private provenance provider-live proof packet. It does
not update public catalog content or make a public product-readiness claim.

## Claim Boundary

This work order authorizes only a bounded provider-live proof over existing
MinerU system-chain summary-only harness output. It does not authorize MinerU
runtime execution, private/generated output content reads, production
Memory/RAG route release, production durable-store invocation, file-backed
production persistence, retrieval, vectorization, public-sync, use-case/legal
workflow, extraction-truth claims, current-law claims, public readiness,
production readiness, worker commit, or push.
