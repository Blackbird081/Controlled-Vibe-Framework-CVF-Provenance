# CVF GC-018 Baseline - MSEA R43 T2 MinerU Actor Role Persistence Authority Wiring Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION

Dispatch base head: 0d408e163

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: reviewer/closer role

Worker target: delegated worker role, not a provider-specific agent identity

## Purpose

Authorize a narrow implementation packet for the accepted R43-T1 Option B design: wire a purpose-built actor-role authority field into the MinerU system-chain route candidate's file-backed persistence decision path. This baseline records the operator-approved allowlist `OPERATOR`, `GOVERNOR` as CVF route authority policy for this path. It does not authorize CVF to control or interfere with an agent's internal operation; it authorizes only boundary control, fail-closed behavior, receipt/evidence expectations, and traceability for later responsibility review.

## Decision Baseline

| Field | Value |
| --- | --- |
| Selected tranche | MSEA-R43-T2 Option B implementation packet |
| Source decision | R43-T1 accepted worker return and decision matrix selected actor-role authority wiring design |
| Approved allowlist | `OPERATOR`, `GOVERNOR` |
| Baseline disposition | DISPATCH_READY for a no-commit source/test worker |
| Claim boundary | Route-boundary authority and traceability only; no agent-internal intervention or production release claim. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION --title "MSEA R43 T2 MinerU Actor Role Persistence Authority Wiring Implementation" --date 2026-07-06 --base 0d408e163 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled R43-T2 mission, operator allowlist policy, source verification, scope, gates, and claim boundary. |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py` |
| docOnlyNewFields | `operatorApprovedFileBackedPersistenceActorRoles`; `agentOperationInterventionBoundary` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

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
- ADIF-0006

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` |
| Returned defect count | 11 |
| Returned defects | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Disclosed defectIds | ADIF-0001; ADIF-0002; ADIF-0014; ADIF-0015; ADIF-0020; ADIF-0021; ADIF-0007; ADIF-0016; ADIF-0017; ADIF-0024; ADIF-0006 |
| Dispatch impact | Packet uses source verification, checker read-ahead, exact commit mode, explicit worker scope, and no provider-local authority. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | ADIF disclosure query line; Source Verification Block table labels; Negative Search And Collision Discipline; Agent Handoff Contract Control Block; Reviewer Closure Conversion; WORKER_MUST_NOT_COMMIT; DISPATCH_READY |
| gateRunPurpose | Confirm dispatch packet shape and evidence after authoring; not first discovery. |
| claimBoundary | Read-ahead covers dispatch artifact shape only; it does not prove implementation behavior, runtime execution, live provider behavior, public-sync, or production readiness. |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| R43-T1 selected Option B for actor-role authority wiring design. | `docs/reference/CVF_MSEA_R43_T1_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_DESIGN_MATRIX_2026-07-06.md` | Accepted design disposition section | `R43_T1_ACTOR_ROLE_WIRING_DESIGN_READY_FOR_IMPLEMENTATION_PACKET` | R43-T1 decision matrix | ACCEPT |
| Route authority currently has `fileBackedPersistenceRequested`. | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | line 40 | `fileBackedPersistenceRequested` | `MineruSystemChainRouteAuthority` | ACCEPT |
| Route builder currently rejects file-backed persistence requests. | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/mineru-system-chain-route-candidate.ts` | lines 105-109 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | `buildMineruSystemChainRouteCandidate` | ACCEPT |
| Runtime memory actor role vocabulary includes `OPERATOR` and `GOVERNOR`. | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12-22 | `RuntimeMemoryActorRole` | `RuntimeMemoryActorRole` | ACCEPT |
| Existing system-chain route candidate tests cover the current file-backed fail-closed path. | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/mineru-system-chain-route-candidate.test.ts` | lines 161-174 | `FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED` | `buildMineruSystemChainRouteCandidate` tests | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Baseline path existence | `Test-Path docs/baselines/CVF_GC018_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md` returned `False` before authoring. | PASS |
| Work order path existence | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R43_T2_MINERU_ACTOR_ROLE_PERSISTENCE_AUTHORITY_WIRING_IMPLEMENTATION_2026-07-06.md` returned `False` before authoring. | PASS |
| Token collision search | `rg -n "MSEA-R43-T2|MSEA_R43_T2|CVF_MSEA_R43_T2" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION CVF_SESSION_MEMORY.md AGENT_HANDOFF_V37_2026-07-06.md` returned only next-move/session references before authoring. | PASS |
| Collision decision | No existing R43-T2 baseline, work order, review, or reference artifact exists; current packet may claim the R43-T2 dispatch identifiers. | PASS |

## Operator Authority Recording

operatorApprovedFileBackedPersistenceActorRoles: `OPERATOR`, `GOVERNOR`

agentOperationInterventionBoundary: CVF does not intervene in or direct an agent's internal operation. CVF controls only the route boundary where file-backed persistence is requested, records actor-role authority evidence, and requires fail-closed behavior plus traceable proof so later review can attribute which actor role requested or authorized the route.

Authority note: the allowlist is operator-approved dispatch policy recorded by this packet, not a pre-existing runtime source fact.

## Evidence / Verification

| Evidence item | Command or source | Result |
| --- | --- | --- |
| Startup base head | `git rev-parse --short HEAD` | `0d408e163` |
| Initial worktree | `git status --short --untracked-files=all` | clean before authoring |
| ADIF disclosure | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 20 --json` | 11 defects disclosed |
| Dispatch quality gate | `python governance/compat/check_work_order_dispatch_quality.py --base 0d408e163 --head HEAD --enforce` | PASS after allowed-scope packet repair |
| Handoff boundary gate | `python governance/compat/check_agent_handoff_boundary.py --base 0d408e163 --head HEAD --enforce` | PASS after allowed-scope packet repair |

## Claim Boundary

This baseline authorizes only a narrow R43-T2 implementation work order. It does not itself edit source or tests, run MinerU, read private/generated output, invoke file-backed persistence, widen persistence mode, release production durable-store or Memory/RAG routes, add retrieval or vectorization, run provider/live proof, public-sync, worker commit, push, or make public or production-readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch packet only; no public-sync scope is authorized.
