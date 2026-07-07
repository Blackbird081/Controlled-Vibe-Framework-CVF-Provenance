# CVF GC-018 - MSEA R36 T1-T3 Public Catalog Hygiene Source Packet

Memory class: governed-baseline

Status: DISPATCH_READY

Created: 2026-07-05

dispatchBaseHead: `b0ab23ae2`

rawMemoryReleased: false

## Purpose

Authorize a bounded docs-only R36 source packet that prepares public catalog
hygiene evidence after R35 identified stale capability documentation. R36
does not execute public-sync and does not edit public-facing files.

## Baseline Decision

Decision: `R36_PUBLIC_CATALOG_HYGIENE_SOURCE_PACKET_AUTHORIZED_BOUNDED`

Baseline: R35 accepted a capability snapshot and candidate ranking. The
reviewer audit selected public catalog hygiene source-packet preparation as
the next bounded initiative. Public-sync execution remains separate and held.

## Proposed Tranche

MSEA-R36 T1-T3 creates a staleness source matrix, public-safe claim boundary
plan, public-sync readiness decision matrix, and worker return.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldTool | manual scaffold from current GC-018/work-order template and R35 dispatch packet shape |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R36-T1-T3 --title "Public Catalog Hygiene Source Packet" --date 2026-07-05 --base b0ab23ae2 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| scaffoldSource | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`; R35 dispatch baseline/work-order shape |
| scaffoldReason | R36 requires a source-verified multi-tranche docs-only public catalog hygiene source packet |
| manualEditsAfterScaffold | Filled R36 authority chain, source verification, public/provenance boundary, ADIF disclosure, worker-output quality controls, handoff controls, and claim boundary |
| docOnlyNewFields | `READY_FOR_SEPARATE_PUBLIC_SYNC_PACKET`; `BLOCKED_STRAY_PROVIDER_LOCAL_FILE` |
| checkerReadAheadConfirmation | Checker sources listed in the Checker Source Read-Ahead Block were read before authoring |
| claimBoundary | Dispatch scaffold provenance only; no public-sync, provider/live, runtime, private-output, source/test, or production-readiness claim |

## Scope / Applies To

Allowed scope is limited to three new `docs/reference/` artifacts and one
`docs/reviews/` worker return. The worker must not edit source, tests,
session state, active handoff, public-sync clone files, existing capability
catalog documents, provider-local files, IDE config, or runtime files.

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator instruction | requested review/audit, next roadmap selection, and work-order creation after R35 T1-T3 worker return |
| Active state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` current mode after R35 closure session-sync |
| Active handoff | `AGENT_HANDOFF_V36_2026-07-04.md` |
| Prior closure | R35 worker return accepted at material commit `f9e2a0b33` |
| Candidate evidence | R35-T2 capability snapshot and R35-T3 ranking |
| Public boundary | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R35-T2 identifies the technical product catalog, module inventory, governance control matrix, and release readiness status as stale relative to MinerU | VALUE_SET | `docs/reference/CVF_MSEA_R35_T2_CVF_CURRENT_PRODUCT_CAPABILITY_SNAPSHOT_2026-07-05.md` | Capability-Inventory Document Currency Assessment | stale capability documents | R35-T2 snapshot | ACCEPT |
| R35-T3 identifies public catalog hygiene as low-medium risk with no direct dependency on held MinerU lanes | VALUE_SET | `docs/reference/CVF_MSEA_R35_T3_NEXT_INITIATIVE_CANDIDATE_RANKING_2026-07-05.md` | Candidate Ranking Table | Public catalog hygiene | R35-T3 ranking | ACCEPT |
| Public-facing edits must be prepared and pushed from the sibling public-sync clone, not provenance | VALUE_SET | `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | Critical Repository Boundary section | `Controlled-Vibe-Framework-CVF-public-sync` | repository boundary standard | ACCEPT |
| Public export disposition is required before public catalog claims | VALUE_SET | `docs/reference/archive/CVF_PUBLIC_EXPORT_DISPOSITION_STANDARD_2026-05-30.md` | Rule and Required Section | `DEFERRED_PRIVATE_ONLY` | public export disposition standard | ACCEPT |
| Existing catalog document has public-sync path verification rules and no current MinerU/MSEA entries | EXISTS | `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` | whole-file search and public-sync boundary notes | catalog body | technical product catalog | ACCEPT |

## Current Runtime Freshness Verification

| Search | Result |
| --- | --- |
| `Test-Path docs/reference/CVF_MSEA_R36_T1_PUBLIC_CATALOG_STALENESS_SOURCE_MATRIX_2026-07-05.md` | false before authoring |
| `Test-Path docs/reference/CVF_MSEA_R36_T2_PUBLIC_SAFE_CATALOG_UPDATE_CLAIM_BOUNDARY_PLAN_2026-07-05.md` | false before authoring |
| `Test-Path docs/reference/CVF_MSEA_R36_T3_PUBLIC_SYNC_READINESS_DECISION_MATRIX_2026-07-05.md` | false before authoring |
| `Test-Path docs/reviews/CVF_MSEA_R36_T1_T3_PUBLIC_CATALOG_HYGIENE_SOURCE_PACKET_WORKER_RETURN_2026-07-05.md` | false before authoring |

## Negative Search And Collision Discipline

| Check | Evidence |
| --- | --- |
| Search roots | `docs/reference`; `docs/reviews`; `docs/roadmaps`; `docs/baselines`; `docs/work_orders` |
| Search command or query | `Test-Path` for exact planned R36 paths; `rg -n "MinerU\|MSEA"` for catalog currency evidence |
| Collision handling | If any planned worker output path exists at worker start, worker must stop and return to orchestrator |
| Public-sync boundary handling | Worker may cite the sibling public-sync clone rule but must not enter, edit, commit, or push from that clone |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

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

Disclosure count: 10

## Acceptance Criteria

| Criterion | Evidence | Status |
| --- | --- | --- |
| T1 matrix exists and source-verifies stale catalog surfaces | T1 reference artifact | PASS_PENDING_WORKER |
| T2 plan preserves public-safe, foundation-only claim boundaries | T2 reference artifact | PASS_PENDING_WORKER |
| T3 readiness matrix records next action without executing public-sync | T3 reference artifact | PASS_PENDING_WORKER |
| Worker return records command evidence, no-commit status, and hygiene controls | worker return | PASS_PENDING_WORKER |

## Evidence / Verification

| Evidence | Result |
| --- | --- |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS_PENDING_WORKER |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` | PASS_PENDING_WORKER |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: DISPATCH_READY; Source Verification Block; ADIF Defect Registry Disclosure; Machine Closure Package; Public Export Disposition; Agent Operation Trace Block; ACCEPT |
| gateRunPurpose | confirm R36 GC-018 shape after checker source read-ahead |
| claimBoundary | baseline dispatch only; no public-sync, runtime, provider/live, private-output, source/test, or production route release |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R36 baseline is private provenance governance material only. No
public-sync remote, public commit, public README/catalog edit, or public
catalog claim is authorized by this baseline.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R36_T1_T3_PUBLIC_CATALOG_HYGIENE_SOURCE_PACKET_2026-07-05.md` | Status: DISPATCH_READY pending worker evidence | PASS |
| Roadmap state | `docs/roadmaps/CVF_MSEA_R36_PUBLIC_CATALOG_HYGIENE_SOURCE_PACKET_ROADMAP_2026-07-05.md` Status: DISPATCH_READY | roadmap top Status line to be updated by reviewer only if closed | PASS_PENDING_REVIEWER |
| Public-sync state | N/A with reason: no public-sync authorized | no public-sync surface touched | N/A with reason |
| Session continuity | session-sync steward updates front door/state/handoff after material commit | pending dedicated session-sync commit after dispatch | PASS_PENDING_SESSION_SYNC |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | R35 source-backed candidate ranking -> R36 source packet |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | R36 dispatch artifacts and worker outputs |
| Disposition | No external knowledge is required or authorized |
| Claim boundary | no external repository absorption, private/generated output content read, public-sync, provider/live proof, or route release |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R36 GC-018 authoring, 2026-07-05 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `Get-Content`; `rg`; `Test-Path`; ADIF resolver; governance gates |
| Target paths | R36 roadmap, GC-018 baseline, and work order |
| Allowed scope source | R35 closure and operator request to choose next roadmap and create work order |
| Before status evidence | HEAD `b0ab23ae2`; clean worktree before R36 dispatch authoring |
| After status evidence | R36 dispatch artifacts pending material commit |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatch authoring only |
| Claim boundary | no public-sync, runtime, provider/live, private-output, source/test, or production route release |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This GC-018 authorizes only R36 private provenance source-packet
preparation for public catalog hygiene. It does not authorize public-sync
execution, push, public README or catalog edits, production memory/RAG route
release, file-backed production persistence, retrieval, vectorization,
MinerU runtime execution, private/generated output content read,
provider/live proof, Web/UI implementation, standalone app work,
legal/use-case deep dive, extraction accuracy, document truth, legal
quality, current-law correctness, hosted readiness, production readiness,
source/test edits, worker commit, or public claim.
