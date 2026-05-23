# CVF GC-018 AIF-B - Graph Knowledge Phase 1

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-24

## Purpose

Authorize bounded implementation of AIF-B Graph Knowledge Phase 1 inside
`EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/`. The tranche absorbs the
code-review graph specs into an in-memory AST, symbol-index, and task-query
foundation.

## Scope

In scope:

- graph schema
- TypeScript AST parser
- in-memory symbol index
- task-query mapper and blast-radius resolver
- `GraphKnowledgeService` interface export for future AIF-C consumption
- targeted unit tests and TypeScript verification

Out of scope:

- SQLite or durable graph storage
- graph scoring as a separate persisted subsystem
- mutation, approval, or denial authority
- live provider routing
- public-sync work

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`
- `docs/work_orders/CVF_WO_AIF_B_GRAPH_KNOWLEDGE_PHASE1_2026-05-23.md`
- `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
- `.private_reference/legacy/CVF ADD/code-review-graph/`

## Decision / Baseline / Proposed Tranche

Decision: proceed after the operator's 2026-05-24 instruction to complete the
roadmap and work orders. This is treated as confirmation that Phase 1 remains
in-memory-only; PBR-04 durable persistence is not lifted.

Baseline: CVF had scoped-knowledge provider boundaries but no AST graph,
dependency graph, symbol index, or blast-radius resolver implementation.

Proposed tranche: implement a local in-memory graph foundation and export an
advisory `GraphKnowledgeService` interface. Durable storage and authority-bearing
governance decisions remain excluded.

## Legacy Spec Scan Block

Legacy folder scanned:

- `.private_reference/legacy/CVF ADD/code-review-graph/`

Correction: the work order referenced `CVF_GRAPH_SCORING_SPEC.md`, but that
file does not exist in the repository source bundle. The actual implementation
scan used the files below.

| File | Status in this tranche | Reason if deferred |
| --- | --- | --- |
| `CVF_GRAPH_KNOWLEDGE_SPEC.md` | ABSORBED | Node, edge, query-result, AST ingestion, and graph-service surfaces mapped to schema/index modules. |
| `CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md` | ABSORBED | Task normalization, impacted scope, bounded expansion, and context trace mapped to task-query mapper. |
| `CVF_GRAPH_IMPLEMENTATION_PLAN.md` | ABSORBED | Phase 1 knowledge foundation implemented; later incremental/storage phases deferred. |
| `CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md` | ABSORBED | Integration exposed as read-only service interface only. |
| `CVF_GRAPH_GOVERNANCE_EXTENSION_SPEC.md` | ABSORBED | Evidence-not-authority boundary encoded in warnings and claim boundary. |
| `README.md` | METADATA_READ | Confirmed bundle contents and no parallel governance runtime. |
| `Thong_tin.md` | METADATA_READ | Metadata file read for folder context; no runtime rule required. |

## Depth Audit

| Candidate | Type | Score | Decision | Rationale |
| --- | --- | ---: | --- | --- |
| In-memory AST and symbol index | IMPLEMENTATION_FOUNDATION | 9/10 | CONTINUE | Delivers the missing graph engine foundation without PBR-04 persistence. |
| Durable SQLite graph storage | PERSISTENCE_CHANGE | 0/10 | REJECT | PBR-04 persistence lift was not granted. |
| Graph as governance approver | GOVERNANCE_SEMANTIC_CHANGE | 0/10 | REJECT | Source specs say graph is evidence, not authority. |
| Separate graph scoring subsystem | SPEC_MISSING | 2/10 | DEFER | Referenced scoring spec is absent; no standalone scoring implementation is authorized. |

## Acceptance Criteria

- GC-018 filed with complete Legacy Spec Scan Block and missing-spec correction.
- Actual code-review-graph source bundle read and classified.
- Phase 1 modules implemented under Learning Plane ownership.
- `GraphKnowledgeService` interface exported for future AIF-C consumption.
- Targeted tests and TypeScript check pass.
- Registry, roadmap tracker, session memory, active state, handoff, and work
  order are updated.
- Completion review filed.

## Evidence / Verification

Required verification:

- focused AIF-B test coverage
- Learning Plane `npm run check`
- Learning Plane full test suite
- repository governance hook chain before commit

No live provider API call is required because this tranche does not claim live
CVF governance behavior or provider execution.

## Claim Boundary

AIF-B can claim only a local in-memory graph knowledge Phase 1 foundation. It
cannot claim durable graph storage, graph scoring productization, autonomous
approval/denial authority, live route integration, or public product readiness.
