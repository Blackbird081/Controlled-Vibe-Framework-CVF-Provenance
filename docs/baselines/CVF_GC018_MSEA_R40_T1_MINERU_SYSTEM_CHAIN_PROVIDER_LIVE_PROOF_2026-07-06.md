# CVF GC-018 - MSEA R40 T1 MinerU System Chain Provider Live Proof

Memory class: governed-baseline

Status: DISPATCH_READY

Created: 2026-07-06

rawMemoryReleased: false

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py` read as the required helper surface; packet was manually authored for R40-T1 |
| generatedProfile | GC-018 baseline / source-verified dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Manual source-verified authoring for MinerU system-chain provider-live proof lane |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| docOnlyNewFields | `Scaffold Provenance Block` |
| claimBoundary | Dispatch scaffold provenance only; no runtime, private-output read, production release, public-sync, push, or public claim |

## Purpose

Authorize one bounded provider-live proof packet for the existing MinerU
system-chain foundation. The proof may use the accepted in-process MinerU
system-chain harness output as summary-only context in a live Alibaba/DashScope
call, then assert that the response preserves the bounded PASS token and the
production-not-released boundary.

This baseline does not authorize MinerU runtime execution, private/generated
MinerU output reads, production Memory/RAG route release, file-backed
production persistence, retrieval, vectorization, public-sync, push, or public
claim.

## Baseline Decision

R40-T1 is approved for dispatch as a private provenance provider-live proof
packet only.

The worker may add one focused live test file under the Learning Plane package
and one worker-return artifact, run the existing deterministic MinerU tests,
run the new live test with operator-provided DashScope-compatible key loaded
secret-safely, and stop for reviewer closure. The worker must not commit.

## Operator Lane Selection Boundary

| Question | R40-T1 treatment |
| --- | --- |
| Which held R38 authority lane is selected now? | Provider/live proof for the existing MinerU system-chain foundation |
| Does this packet release production Memory/RAG? | No |
| Does this packet run MinerU runtime or read private/generated output? | No |
| Does this packet prove extraction accuracy, document truth, or legal workflow readiness? | No |

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

Dispatch impact: the packet source-verifies the held live-proof lane,
prevents provider-local authority promotion, requires secret-safe key loading,
and keeps final worker-return command evidence current.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Public Export Disposition; Claim Boundary; Agent Handoff Contract Control Block |
| gateRunPurpose | confirmation evidence before dispatch; gates confirm packet shape after source and checker read-ahead |
| claimBoundary | checker read-ahead evidence only; no runtime, public-sync, private-output read, production Memory/RAG release, retrieval, vectorization, file-backed persistence, worker commit, push, or public claim |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R39_T1_MINERU_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_AUTHORITY_DECISION_COMPLETION_2026-07-06.md`

priorVerificationAnchor: `R39_T1_AUTHORITY_DECISION_COMPLETE_HELD_PENDING_AUTHORITY_GAPS`

freshRecomputeRequired: yes - worker must recompute all source anchors before writing R40-T1 worker return.

unicodePathHandling: use literal repo-relative paths and UTF-8-safe readers; do not normalize filenames broadly.

extractedTextAuthority: current source, deterministic harness output, and live provider response only; private/generated MinerU output content is not authority for this packet.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact path collision | `Test-Path` for the R40-T1 baseline, work order, live test, and worker return returned `False` before authoring | PASS |
| Token search for R40-T1 paths | `rg -n "MSEA-R40-T1|CVF_MSEA_R40_T1|R40_T1" docs EXTENSIONS CVF_SESSION` returned no existing R40-T1 governed artifact before authoring | PASS |
| Collision decision | No existing R40-T1 governed artifact was found | PASS |

## Evidence / Verification

| Evidence item | Disposition |
| --- | --- |
| Source anchors | Source Verification Block cites current source and governed closure artifacts |
| ADIF disclosure | Resolver query and returned defectIds are recorded in this baseline |
| Checker read-ahead | Checker Source Read-Ahead Block names applicable checker sources read before authoring |
| Dispatch gate | Pre-dispatch autorun must pass before this packet is committed or handed to worker |
| Runtime boundary | Live call is allowed only through the planned focused test; MinerU runtime, private-output read, production release, file-backed persistence, retrieval, vectorization, public-sync, push, and public claim remain forbidden |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: R40-T1 is a private provenance live-proof packet. It does not update
public catalog content and does not make a public runtime or product-readiness
claim.

## Claim Boundary

This baseline authorizes only R40-T1 dispatch for a bounded provider-live
proof over existing MinerU system-chain summary-only harness output. It does
not authorize MinerU runtime execution, private/generated output content
reads, production Memory/RAG route release, production durable-store
invocation, file-backed production persistence, retrieval, vectorization,
public-sync, use-case/legal workflow, extraction-truth claims, current-law
claims, public readiness, production readiness, worker commit, or push.
