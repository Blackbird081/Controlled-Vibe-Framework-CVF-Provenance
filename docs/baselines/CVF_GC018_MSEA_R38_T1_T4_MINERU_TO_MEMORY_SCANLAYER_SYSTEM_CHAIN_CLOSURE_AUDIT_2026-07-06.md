# CVF GC-018 - MSEA R38 T1-T4 MinerU To Memory ScanLayer System Chain Closure Audit

Memory class: governed-baseline

Status: DISPATCH_READY

Created: 2026-07-06

rawMemoryReleased: false

## Purpose

This GC-018 baseline authorizes a docs-only, source-verified R38 T1-T4
audit and release-boundary decision packet for the current MinerU output,
memory, and scan-layer chain.

The packet answers the operator's current product question: whether the
MinerU-to-memory/scanlayer work is already a coherent CVF system, and if
not, exactly which small release or proof tranche remains valuable.

## Baseline Decision

R38 T1-T4 is approved for dispatch as a private provenance audit and
decision packet only.

The worker may create four reference artifacts and one worker-return
artifact. The worker must not edit source, tests, runtime wiring,
private/generated output, public-sync files, session state, active handoff,
or provider-local files.

## Operator Question Boundary

| Question | R38 treatment |
| --- | --- |
| Has MinerU output been connected to memory and scanlayer as a CVF system? | Answer from current source and closed artifacts only, with a status taxonomy of released, foundation-only, held, or blocked |
| What remains after the latest public catalog sync? | Classify remaining gaps and name the smallest next valuable tranche |
| Should CVF go into a use-case/legal workflow now? | No. Use-case/legal/extraction-truth/current-law lanes remain out of scope unless a later operator-selected roadmap opens them |
| Should R38 run MinerU, providers, or durable production memory writes? | No. This is docs-only audit and decision work |

## T1-T4 Output Plan

| Tranche | Required output | Required decision |
| --- | --- | --- |
| T1 | Current chain map | Map receipt writer, scan-layer surfaces, durable-store invocation candidate, memory/RAG route candidate, system-chain route candidate, harness, and bridge boundaries |
| T2 | Gap classification | Separate implemented internal links, tested fixture links, held production links, missing release authority, and no-value/use-case lanes |
| T3 | Minimal E2E harness decision | Decide whether a narrow next proof should run, and if so, define only the minimal proof surface without executing it |
| T4 | Release gate decision | Recommend stop, narrow proof, or separate production authority packet, with exact held boundaries and next-move text |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Python MinerU receipt writer defines the metadata receipt object and durable memory write adapter candidate builder | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 96, 198, and 779 | `build_mineru_durable_memory_write_adapter_candidate` | MinerU receipt writer | EXISTS | ACCEPT |
| Scan-layer route decision source defines document scan signals and route decision function | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | lines 40 and 71 | `decide_scan_route` | scan route decision module | EXISTS | ACCEPT |
| Scan outcome report source defines report output and file writer | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | lines 43 and 274 | `write_scan_outcome_report_files` | scan outcome report module | EXISTS | ACCEPT |
| Durable-store invocation source exposes an implemented bounded invocation function and a no-memory-write authorization token | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-durable-store-invocation.ts` | lines 27, 30, 37, and 105 | `invokeMineruDurableStoreWrite` | durable-store invocation candidate | EXISTS | ACCEPT |
| Memory/RAG route release source exposes a bounded candidate function and not-production-authorized token | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-memory-rag-route-release.ts` | lines 30, 33, and 93 | `releaseMineruMemoryRagRouteCandidate` | memory/RAG route release candidate | EXISTS | ACCEPT |
| System-chain route candidate source restricts persistence mode to in-process-only and keeps production route not released | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 25, 28, 34, and 78 | `buildMineruSystemChainRouteCandidate` | system-chain route candidate | VALUE_SET | ACCEPT |
| Internal system-chain harness source defines a bounded pass token and records Python receipt bridge not wired by R33 | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-internal-system-chain-harness.ts` | lines 32, 38, and 126 | `runMineruInternalSystemChainHarness` | internal system-chain harness | VALUE_SET | ACCEPT |
| Python receipt bridge source defines fixture-only proof and a not-production-wired hold token | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-python-receipt-bridge.ts` | lines 25, 28, and 188 | `mapMineruPythonReceiptFixtureToDurableStoreInvocationInput` | Python receipt bridge | VALUE_SET | ACCEPT |
| R33 closed the internal system-chain readiness audit bounded and kept the Python receipt bridge separate | `docs/reviews/CVF_MSEA_R33_T5_MINERU_INTERNAL_SYSTEM_CHAIN_COMPLETION_2026-07-05.md` | lines 45-52 and 230 | `R33_INTERNAL_SYSTEM_CHAIN_HARNESS_PASS_BOUNDED_PUBLIC_SAFE_SNAPSHOT_READY` | R33 completion review | VALUE_SET | ACCEPT |
| R34-T2 selected stopping the foundation lane until an operator names a priority, and kept production memory/RAG and file-backed persistence held | `docs/reference/CVF_MSEA_R34_T2_MINERU_FOUNDATION_LANE_STOP_OR_NARROW_RELEASE_DECISION_MATRIX_2026-07-05.md` | lines 47, 55-56, and 219 | `MINERU_FOUNDATION_PLANE_STOP_HERE_PENDING_OPERATOR_NEW_INITIATIVE` | R34-T2 decision matrix | VALUE_SET | ACCEPT |
| R35-T2 classified the MinerU chain as foundation-only and not production-usable | `docs/reference/CVF_MSEA_R35_T2_CVF_CURRENT_PRODUCT_CAPABILITY_SNAPSHOT_2026-07-05.md` | lines 61-63, 73-74, and 212-215 | foundation-only MinerU chain | R35-T2 capability snapshot | VALUE_SET | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver query:

`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json`

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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; ADIF Defect Registry Disclosure; Checker Source Read-Ahead Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirm R38 GC-018 dispatch baseline shape before work-order authoring |
| claimBoundary | checker read-ahead evidence only; no runtime, provider/live, public-sync, private-output, source/test, memory write, or production route release |

## Evidence / Verification

| Evidence item | Disposition |
| --- | --- |
| Source anchors | Source Verification Block cites current source and governed closure artifacts |
| ADIF disclosure | Resolver query and returned defectIds are recorded in this baseline |
| Checker read-ahead | Checker Source Read-Ahead Block names applicable checker sources read before authoring |
| Dispatch gate | Pre-dispatch autorun must pass before this packet is committed or handed to a worker |
| Runtime boundary | No runtime, provider/live, public-sync, private-output, source/test, memory write, or production route release evidence is claimed |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind gc018-baseline --batch-id MSEA-R38-T1-T4 --title "MinerU To Memory ScanLayer System Chain Closure Audit" --date 2026-07-06 --base aeaadccf9 --stdout` |
| generatedProfile | gc018-baseline docs-only dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Manual authoring used to fill source verification, ADIF disclosure, checker read-ahead, evidence/verification, and claim boundary |
| checkerReadAheadConfirmation | Checker sources listed in Checker Source Read-Ahead Block were read before authoring |
| docOnlyNewFields | R38 T1-T4 output and decision tokens are listed in the paired work order |
| claimBoundary | Dispatch scaffold provenance only; no runtime, provider/live, public-sync, private-output, source/test, memory write, or production route release |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: R38 T1-T4 is private provenance audit and decision work. It does
not update public catalog content and does not make a public runtime or
product-readiness claim.

## Claim Boundary

This baseline authorizes only R38 T1-T4 dispatch for docs-only audit and
decision artifacts. It does not authorize source/test edits, MinerU runtime
execution, private/generated content reads, memory/RAG writes, file-backed
production persistence, provider/live proof, public-sync, use-case/legal
workflow, extraction-truth claims, current-law claims, production readiness,
worker commit, or push.
