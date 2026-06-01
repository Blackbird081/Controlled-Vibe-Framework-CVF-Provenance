# CVF MKG1 Memory Knowledge Graph Owner-Surface Review Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-01

## Purpose

Turn the RESCAN-C Memory/Knowledge/Graph finding into a bounded owner-surface
review that another agent can execute without mistaking Legacy graph or Memory
concepts for runtime authority.

## Authorization / Decision

Decision: dispatch one documentation-only source-analysis worker tranche.

Authority:

- `docs/baselines/CVF_GC018_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_2026-06-01.md`
- `docs/audits/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_DISPATCH_AUDIT_2026-06-01.md`
- RESCAN-C completion and synthesis packets
- GC-047 and GC-048 standards

## Why This Tranche

RESCAN-C closed file visibility for the three partial Legacy roots and routed
Memory/Knowledge/Graph as the highest-value next candidate. Current CVF already
has knowledge-store, graph-boundary, memory-continuity, memory-sync, and
learning-intake surfaces. MKG1 must reconcile source value into those owners
instead of creating a parallel `agentmemory`, `tolaria`, `cortex-hub`, or
`code-review-graph` owner.

## Scope

In scope:

- `47` RESCAN-C Memory/Knowledge/Graph authority assets;
- current CVF owner-surface comparison;
- accept/defer/reject matrix;
- future candidate ledger;
- documentation-only completion packet;
- continuity sync.

Out of scope:

- runtime Memory implementation;
- graph retrieval execution;
- Memory reinjection;
- skill mutation;
- route/provider/database changes;
- public-sync;
- live/provider proof;
- hosted, production, or public readiness claims.

## Non-Goals

- no runtime Memory adoption;
- no graph retrieval execution;
- no reinjection enablement;
- no skill mutation or autonomous learning mutation;
- no public catalog claim;
- no claim that RESCAN-C broad routing equals complete semantic absorption.

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| M1 | Rebuild source set from RESCAN-C manifest | `47`-asset source ledger | READY |
| M2 | Read all five source families | file-level owner-surface notes | READY |
| M3 | Compare against current owner surfaces | owner-surface matrix | READY |
| M4 | Disposition every asset | accept/defer/reject matrix | READY |
| M5 | Separate future candidates | gap ledger with GC-018 routing | READY |
| M6 | Close with evidence | completion review and continuity sync | READY |

## Owner-Surface Lanes

| Lane | Current owner candidate | Boundary question |
| --- | --- | --- |
| Knowledge store | `knowledgeStore`, `InProcessKnowledgeStore`, `FileBackedKnowledgeStore` | Does the source value belong to CRUD/ingest/persistence or remain advisory? |
| Graph boundary | `graphContextResolverBoundaryAdvisoryType` | Does the source value change boundary vocabulary without runtime graph execution? |
| Memory continuity | `memoryContinuityLevelAdvisoryType` | Does the source value clarify L0/L1/L2/L3 boundaries without reinjection? |
| Memory sync | LHW24-T2 Memory Sync Protocol | Does the source value improve sync vocabulary while preserving autonomous mutation false? |
| Learning intake | `LearningSignalIntakeRecord` | Does the source value become a learning signal, not a mutation? |
| Graphify data model | `CVF_GRAPH_MEMORY_DATA_MODEL.md` | Does the source value map to node/edge/record vocabulary as doc-only reference? |

## Verification / Evidence

Required commands:

```powershell
python scripts/build_legacy_rescan_c_manifest.py --check-only --expected-manifest-hash ae7fe05e016b7079a81002de60de1e1209112de59c8bee793e15e11557cae0ff
python governance/compat/check_corpus_completeness_report_integrity.py --base ec03e762 --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base ec03e762 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base ec03e762 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base ec03e762 --head HEAD
```

## Acceptance Criteria

| Criterion | Required result |
| --- | --- |
| Source set | `47` RESCAN-C assets reconciled |
| Source family coverage | five families read and dispositioned |
| Owner-surface mapping | every accepted item maps to a current owner |
| Rejections | source-native parallel owners rejected as authority |
| Runtime boundary | no runtime Memory, graph, route, provider, or mutation claim |
| Future candidates | gap ledger routes only through fresh GC-018 |
| GC-047 | honest corpus block |
| GC-048 | honest knowledge-map block |

## Failure Conditions

Return to Orchestrator if:

- any of the `47` source assets cannot be read or dispositioned;
- a proposed accepted item lacks current owner-surface mapping;
- runtime implementation becomes necessary;
- public-sync, live provider proof, secrets, paid quota, or destructive action
  becomes necessary;
- a source-native Legacy module is treated as a new CVF owner.

## Roadmap-To-Work-Order Trace

Execution packet:

`docs/work_orders/CVF_WO_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_2026-06-01.md`

Completion packet:

`docs/reviews/CVF_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_COMPLETION_2026-06-01.md`

Closure result: `CLOSED_PASS_BOUNDED` with `47/47` file-level corpus ledger,
`26` doc-only owner-surface mappings, and `21` deferred runtime or
implementation candidates routed to MKG2.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Memory/Knowledge/Graph review only. No public-sync
remote, public repository commit, or public artifact path is included.

## Claim Boundary

This roadmap dispatches source review and owner-surface mapping only. It does
not authorize runtime realization, graph retrieval, Memory reinjection, skill
mutation, public claims, hosted readiness, production readiness, or autonomous
mutation.
