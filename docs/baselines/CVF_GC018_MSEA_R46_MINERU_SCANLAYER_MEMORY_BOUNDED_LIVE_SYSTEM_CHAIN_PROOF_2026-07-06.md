# CVF GC-018 Baseline - MSEA R46 MinerU ScanLayer Memory Bounded Live System Chain Proof

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

rawMemoryReleased=false

Batch ID: MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF

Dispatch base head: b35a809f0

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: reviewer/closer role

Worker target: bounded implementation worker role

## Purpose

Authorize a bounded source/test/live-proof implementation packet for the MinerU/scanlayer/memory foundation chain. The packet may add a narrow proof harness, focused deterministic tests, and one live provider test that uses operator-supplied keys secret-safely. The proof must use synthetic summary-only MinerU metadata, file-backed durable memory write/read-back, and receipt evidence. It must preserve production route hold, private-output boundary, public-sync hold, and use-case/legal hold.

## Baseline Decision

Dispatch the paired R46 work order for reviewer-owned execution. This baseline authorizes only the narrow proof lane needed to answer whether the MinerU/scanlayer/memory foundation chain is testable as an internal bounded system chain before any plane/absorb repository transition.

## Evidence / Verification

| Evidence class | Command or source | Disposition |
| --- | --- | --- |
| Clean starting point | `git rev-parse --short HEAD` returned `b35a809f0`; `git status --short --untracked-files=all` was empty before authoring | ACCEPT |
| Operator checkpoint | User explicitly requested completing the whole proposed roadmap and allowed API-key live run evidence | ACCEPT |
| R45 boundary | R45 selected bounded internal candidate, not production release | ACCEPT |
| Source verification | Source Verification Block cites current file-backed durable memory store, route candidate, existing file-backed route tests, and existing Alibaba live test pattern | ACCEPT |
| ADIF disclosure | Resolver command recorded in ADIF Defect Registry Disclosure returned no defects for the queried task class | ACCEPT |
| Claim boundary | Baseline keeps `rawMemoryReleased=false` and forbids production, public, private-output, extraction-accuracy, and use-case/legal claims | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF --title "MSEA R46 MinerU ScanLayer Memory Bounded Live System Chain Proof" --date 2026-07-06 --base b35a809f0 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch reference profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Authored R46 purpose, dependency evidence, source verification, ADIF disclosure, checker read-ahead, claim boundary, and public export disposition |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| docOnlyNewFields | MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF; R46_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_PASS |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring dispatch live proof runtime test`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring dispatch live proof runtime test" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | Packet still uses exact source verification, bounded live-run diagnostics, provider-local hygiene, no raw secret output, and no production/public/use-case overclaim |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py` |
| literalTokensReviewed | Source Verification Block; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Public Export Disposition; DISPATCH_READY; ACCEPT; EXISTS; VALUE_SET; RUNTIME_BEHAVIOR; DOC_ONLY_NEW; N/A with reason |
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
| `MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF` | This baseline and paired work order | Batch identifier for the bounded proof lane | DOC_ONLY_NEW |
| `R46_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_PASS` | Proposed source/test proof result token | New bounded proof disposition literal | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R46 roadmap path before authoring | `Test-Path docs/roadmaps/CVF_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_ROADMAP_2026-07-06.md` returned `False` before authoring | ACCEPT |
| R46 baseline path before authoring | `Test-Path docs/baselines/CVF_GC018_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_2026-07-06.md` returned `False` before authoring | ACCEPT |
| R46 work order path before authoring | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R46_MINERU_SCANLAYER_MEMORY_BOUNDED_LIVE_SYSTEM_CHAIN_PROOF_2026-07-06.md` returned `False` before authoring | ACCEPT |
| Token search before authoring | `rg -n "MSEA-R46|MSEA_R46|CVF_MSEA_R46" docs CVF_SESSION CVF_SESSION_MEMORY.md AGENT_HANDOFF_V37_2026-07-06.md EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests` returned no matches before authoring | ACCEPT |

## Claim Boundary

This baseline authorizes only a bounded internal proof harness, deterministic tests, one live Alibaba-compatible provider proof, secret-safe evidence capture, and review/session closure for the MinerU/scanlayer/memory foundation chain. It does not authorize production Memory/RAG route release, public-sync, private/generated MinerU output content reads, extraction accuracy claims, document truth claims, legal quality claims, current-law correctness claims, hosted release claims, standalone PDF application work, broad provider benchmarking, or use-case/legal workflow.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This is a private provenance dispatch baseline for bounded internal proof. No public-sync artifact, public catalog update, public remote proof, or exported public path is authorized by this baseline.
