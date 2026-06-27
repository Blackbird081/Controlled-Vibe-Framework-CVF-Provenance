# CVF Workspace Layer Full Package Absorption Foundation Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_CLOSED_PASS_BOUNDED

Date: 2026-06-27

docType: roadmap

Owner: Codex

## Purpose

Absorb the useful knowledge from the frozen
`CVF_WORKSPACE_LAYER_PRODUCTION_HANDOFF_PACKAGE` into CVF-owned foundation
artifacts without importing the raw package as authority or implementing local
runtime behavior.

## Scope / Methodology

Method: inventory every non-cache file in the package, hash the files, group
them by source class, classify absorption disposition, and bind the result to
existing CVF workspace, handoff, MCP boundary, and runtime-readiness
contracts.

## Findings / Position

Position: the package was not fully absorbed before this roadmap. Earlier work
captured a selective pilot and a useful absorption map, but no same-batch file
inventory covered all non-cache package files. This roadmap closes that gap as
bounded foundation work.

## Authorization / Decision

Operator decision on 2026-06-27: park DICE and prioritize CVF foundation
uplift. Codex is authorized to complete T0 through T4 as a single bounded
foundation batch.

Decision: complete full package absorption as governed reference work only.
Do not implement package runtime, MCP, CLI, IDE bridge, provider proof, public
sync, or generated aggregate mutation beyond GC-051 corpus registry generation
in this roadmap.

## Source Authority

| Source | Role |
|---|---|
| `governance/compat/CVF_ROOT_FOLDER_LIFECYCLE_REGISTRY.json` | frozen package lifecycle and retention policy |
| `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_EXTERNAL_PACKAGE_ABSORPTION_MAP.md` | prior selective package absorption map |
| `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | earlier pilot absorption review |
| `docs/reference/agent_workspace/README.md` | workspace front door |
| `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | Web Workspace and Local Workspace Runtime split |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | runtime-readiness boundary |
| `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | MCP implementation boundary precedent |

## Tranche Plan

| Tranche | Status | Objective | Boundary |
|---|---|---|---|
| WLFA-T0 | CLOSED_PASS_BOUNDED | Full non-cache file inventory and SHA-256 digest manifest | read-only package inspection |
| WLFA-T1 | CLOSED_PASS_BOUNDED | Absorption decision matrix by package class | no package authority promotion |
| WLFA-T2 | CLOSED_PASS_BOUNDED | CVF-owned mapping to workspace, handoff, MCP, and runtime-readiness surfaces | docs/reference only |
| WLFA-T3 | CLOSED_PASS_BOUNDED | Next-roadmap decision and parking of runtime/MCP import | no implementation authorization |
| WLFA-T4 | CLOSED_PASS_BOUNDED | Closure, gates, and session-sync handoff | material and session-sync commits separate |

## Work Plan

1. Produce a full package inventory reference with count, hash, grouping, and
   class-level disposition.
2. Author GC-018 and a source-verified work order for the bounded absorption
   batch.
3. Close T0 through T4 with a completion review and machine-readable evidence.
4. Update the workspace front door so future agents can find the full
   inventory before any runtime or MCP work.
5. Run governance gates and commit material work before separate session-sync.

## Absorption Decision Matrix

| Package class | Count | CVF disposition |
|---|---:|---|
| Root manifest and README | 2 | ABSORB_AS_REFERENCE |
| Contracts | 5 | ADAPT_TO_CVF_CONTRACTS |
| Implementation docs | 15 | ADAPT_TO_FUTURE_DESIGN |
| Integration docs | 7 | DEFER_TO_SOURCE_VERIFIED_WORK_ORDER |
| Schemas | 8 | MAP_TO_CVF_STATE_TOPOLOGY_BEFORE_USE |
| Reference implementation | 15 | KEEP_AS_NON_CANONICAL_TEST_FIXTURE |
| Runbooks | 3 | ADVISORY_ONLY |
| Scripts | 1 | ADVISORY_ONLY |
| Templates | 2 | ADAPT_AS_BOOTSTRAP_CONTEXT_ONLY |
| Tests and smoke results | 10 | NON_CANONICAL_ADVISORY |

## Design Control Gate

Any future roadmap that consumes this package for runtime, MCP, CLI, IDE
bridge, queue execution, Web UI, provider proof, or public-sync must open a
fresh GC-018 and source-verified work order. The full inventory may be cited as
reference evidence, but package files remain non-canonical unless rewritten
into CVF-governed artifacts.

## Current Runtime Freshness Verification

| Runtime surface | Verification | Disposition |
|---|---|---|
| Local Workspace Runtime | not implemented or mutated by this roadmap | ACCEPT |
| MCP runtime or adapter | not implemented or mutated by this roadmap | ACCEPT |
| Provider/live proof | not run or claimed by this roadmap | ACCEPT |
| Generated session or workspace aggregates | material batch does not mutate them | ACCEPT |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | root/folder lifecycle classification plus absorption map when retained |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_foundation_storage_layout.py` |
| Owner surface | `docs/reference/agent_workspace/` |
| Disposition | ADAPT through governed CVF reference; BLOCK runtime use until fresh GC-018 |
| Claim boundary | no raw external package authority, runtime, MCP, provider, public-sync, or readiness claim |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | T0 through T4 foundation absorption artifacts |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| actionEvidence | ACTION_EVIDENCE_PRESENT: inventory reference, work order, completion review, and gate output |
| invocationBoundary | local file inspection and governed markdown edits only |
| interceptionBoundary | N/A with reason: no runtime interception or provider route changed |
| claimLanguage | reference absorption only |
| forbiddenExpansion | no runtime, MCP, CLI, IDE bridge, provider/live, public-sync, resolver, adapter, or generated aggregate mutation beyond GC-051 corpus registry generation |
| executionBaseHead | `e83ad19e` |
| changedSetScope | roadmap, GC-018, work order, inventory reference, completion review, workspace front-door pointer |
| receiptEvidence | `CVF_RECEIPT_PRESENT`: local command output and governance gate output before commit |
| excludedRuntime | runtime, provider, MCP adapter, CLI adapter, public-sync, generated aggregate mutation beyond GC-051 corpus registry generation |
| equivalenceDisposition | N/A with reason: no runtime equivalence claim |
| boundaryDecision | package knowledge is absorbed as CVF-owned reference, not raw package authority |

## Finding-To-Governance Learning Disposition

| Learning signal | Defect class | Learning lane | Disposition | Next action |
|---|---|---|---|---|
| Frozen package had only pilot absorption coverage | DOCUMENTATION_GAP | GOVERNANCE_CONTROL_PLANE | REFERENCE_ADDED | full inventory reference added |
| Raw external package can be mistaken for CVF authority | AUTHORITY_BOUNDARY_RISK | GOVERNANCE_CONTROL_PLANE | BOUNDARY_RESTATED | future work must cite CVF-owned artifacts |

## Acceptance Criteria

- Full non-cache inventory records 68 files with SHA-256 digests.
- Every package group has an absorption disposition.
- No raw package file is promoted to CVF source of truth.
- No runtime, MCP, CLI, IDE bridge, provider/live, public-sync, resolver, or adapter mutation is included.
- Generated aggregate mutation is limited to GC-051 corpus registry generation.
- Workspace front door points to the new full inventory.
- Governance gates pass before material commit.

## Verification / Evidence

| Evidence | Required result |
|---|---|
| Inventory reference | `nonCacheFileCount=68` |
| AOT gate | manifest matches changed set |
| Machine closure gate | compliant |
| Dispatch quality gate | compliant |
| `git diff --check` | clean |

## Non-Goals

- No raw package import.
- No package instance creation.
- No certification decision.
- No runtime, MCP, CLI, or IDE bridge implementation.
- No provider/live proof.
- No public-sync or push.
- No generated aggregate mutation beyond GC-051 corpus registry generation.
- No resolver or adapter mutation.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_WLFA_T0_T4_FULL_PACKAGE_ABSORPTION_FOUNDATION_FOR_CODEX_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_WLFA_T0_T4_FULL_PACKAGE_ABSORPTION_FOUNDATION_COMPLETION_2026-06-27.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this file | `Status: ROADMAP_CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `id=workspace-layer-production-handoff-package` | PASS |
| Registry Markdown | BLOCKED with reason: no registry edit authorized | N/A | BLOCKED with reason: no registry edit authorized |
| External evidence digest | `docs/reference/agent_workspace/CVF_WORKSPACE_LAYER_FULL_PACKAGE_ABSORPTION_INVENTORY.md` | `nonCacheFileCount=68`; `packageManifestSha256=c8f475d0462b8810728a279971590641bdd9e9749923d48114208631cd6c73c9` | PASS |
| System loop interlock | N/A with reason: no interlock mutation authorized | N/A | N/A with reason |
| Session continuity | N/A with reason: session-sync follows material commit | N/A | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Receipt source | Disposition |
|---|---|---|
| Full inventory exists | inventory reference | PASS |
| Package remains non-canonical | lifecycle registry and claim boundary | PASS |
| Runtime remains parked | current runtime freshness table | PASS |
| Public export is not performed | Public Export Disposition | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation absorption. No public-sync batch is
authorized.

## Claim Boundary

This roadmap closes reference absorption only. It does not implement or prove
Local Workspace Runtime, MCP, CLI, IDE bridge, provider/live behavior,
public-sync, generated aggregate changes beyond GC-051 corpus registry
generation, resolver changes, adapter changes,
or production/public readiness.
