# CVF GC-018 - CI1-T4 Cross-Corpus Index Model

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-02

baseHead: `15d8cec5`

## Purpose

Authorize CI1-T4 to normalize search/filter facets across the first two real
CI1 corpus packets:

- `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`
- `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`

CI1-T4 creates a reusable cross-corpus index contract before LPCI intake work
begins. The output must be machine-readable and reviewable. It is not a runtime
search index, vector database, retrieval route, or chatbot implementation.

## Source

Predecessor evidence:

- CI1 parent GC-018:
  `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md`
- CI1 roadmap:
  `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
- CI1-T2 Graphify packet:
  `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`
- CI1-T3 graph-governance packet:
  `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`
- corpus scan registry:
  `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- system loop interlock registry:
  `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
- search/filter readiness standard:
  `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`

## Decision

Proceed with a documentation/data-model tranche that creates:

- `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
- `docs/reference/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md`
- a new GC-052 interlock connection:
  `scan-packets-to-cross-corpus-index`
- a bounded completion review.

The machine-readable JSON model is the primary downstream input. The Markdown
reference explains the contract and boundaries. Neither artifact may claim
runtime indexing or semantic correctness.

## Scope / Target / Owner Boundary

CVF owns:

- common cross-corpus facet vocabulary;
- domain-extension grouping;
- query-receipt field vocabulary;
- conflict/freshness vocabulary;
- typed source-packet provenance;
- explicit downstream routing into CI1-T5, CI1-T6, and CI1-T7.

Worker owns:

- comparing the two existing CI1 packets;
- creating the JSON model and reference spec;
- adding the GC-052 interlock record;
- updating only the CI1-T4 roadmap row/status;
- creating a completion review;
- fixing allowed-scope documentation/data defects and rerunning gates.

Out of scope:

- reading new legacy source files;
- rescanning `.private_reference/legacy/`;
- modifying GC-051 corpus scan entries;
- implementing graph guards, CLI/MCP commands, vector stores, indexers,
  retrieval routes, chatbot UI/API, provider calls, or live proof;
- modifying runtime source, Python checkers, hook chains, or guard documents;
- public-sync, commit, or push by the worker.

## Expected Cross-Corpus Model Shape

The JSON model must declare:

| Field group | Required content |
| --- | --- |
| Model identity | schemaVersion, modelId, generatedAt, sourcePackets |
| Common facets | canonical fields from the search/filter readiness standard |
| Domain extensions | technical/project and legacy-absorption extension groups |
| Normalization rules | source aliases, value vocabulary, required/optional status |
| Query receipt | auditable minimum receipt fields |
| Freshness/conflict | effective, draft, amended, superseded, repealed, obsolete, stale, unknown |
| Source mappings | T2 and T3 facet-to-canonical mapping rows |
| Downstream routing | T5 sampling, T6 checker decision, T7 LPCI intake bridge |
| Claim boundary | no runtime index, semantic correctness, LPCI runtime, or production claim |

## Knowledge Absorption Blind-Spot Control Block

Standard read:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`

- Source inventory:
  - T2 packet:
    `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`
  - T3 packet:
    `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`
  - common standard:
    `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
  - registry input:
    `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
  - interlock input:
    `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`

- Prior absorption evidence resolved:
  - CI1-T2 packet represents the five-file Graphify pilot.
  - CI1-T3 packet represents the seven-file code-review-graph pilot.
  - CI1-T3 is `CLOSED_PASS_BOUNDED`.
  - CI1-T2 packet is accepted as pilot input while its completion review
    remains `COMPLETE_PENDING_REVIEW`; CI1-T4 must preserve that boundary.

- Source families skipped:
  - no new legacy folder is scanned in CI1-T4;
  - sibling corpus families remain governed by GC-051 recommendations;
  - legal/policy corpus ingestion remains LPCI-T1 work after CI1-T7.

- Owner-surface normalization:
  - common facets belong to CVF Corpus Intelligence;
  - technical/project and legacy fields remain extension groups;
  - legal/policy fields remain declared extension vocabulary for LPCI, not
    populated legal facts in CI1-T4.

- Accept/defer/reject matrix:

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Normalize T2/T3 facets | ACCEPT | CI1-T4 purpose |
| Produce machine-readable model JSON | ACCEPT | downstream loop input |
| Add GC-052 interlock record | ACCEPT | connects scan packets to index model |
| Sample semantic correctness | DEFER | CI1-T5 |
| Add structural checker | DEFER | CI1-T6 decision |
| Map LPCI intake | DEFER | CI1-T7 |
| Implement retrieval runtime | REJECT | outside CI1 scope |

- Adversarial role review:
  - Implementer: two packets are sufficient to establish the first common
    model and expose extension differences.
  - Skeptic/Auditor: two graph-adjacent packets are not enough to prove
    universal semantic coverage; the model must remain extensible.
  - Product/Operator Advocate: a typed model lets LPCI consume a stable input
    rather than reread legacy scan prose.
  - Safety/Boundary Owner: no runtime mutation, provider call, autonomous
    learning mutation, public export, or legal advice claim.

- Blind-spot verdict: CLEAR_FOR_BOUNDED_INDEX_MODEL

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| CI1-T4 roadmap row exists | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | Tranche Plan | `CI1-T4` | CI1 roadmap | ACCEPT |
| Common facet schema exists | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | Common Facet Schema | `sourcePath` | corpus search/filter standard | ACCEPT |
| Query receipt minimum exists | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | Minimum Query Receipt | `normalized query` | corpus search/filter standard | ACCEPT |
| T2 packet exists | `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` | Corpus Search And Filter Readiness | `Common facet schema` | CI1-T2 packet | ACCEPT |
| T3 packet exists | `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md` | Common Facet Schema | `sourcePath` | CI1-T3 packet | ACCEPT |
| GC-052 registry exists | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `connections` | `connections` | system loop interlock registry | ACCEPT |
| Dispatch baseHead | N/A - git command | `git rev-parse --short HEAD` | `15d8cec5` | git repository state | ACCEPT |

## System Loop Interlock Requirement

CI1-T4 must add one `ACTIVE` / `STRUCTURAL_GUARDED` GC-052 registry connection:

`scan-packets-to-cross-corpus-index`

Required routing:

```text
GC-051 registry + CI1 scan packets
  -> normalized cross-corpus facet model
  -> docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json
  -> CI1-T5 sampling and CI1-T7 LPCI intake bridge
```

This interlock proves typed artifact routing. It does not prove semantic
correctness, runtime retrieval behavior, automatic roadmap creation,
autonomous mutation, LPCI implementation, or legal answer quality.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: synchronize protected session front-door
state for the bounded CI1-T4 dispatch only. No guard checker, hook-chain, guard
document, or runtime edit is authorized.

Protected paths:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Operator authorization: operator accepted the proposed CI1-T4 continuation on
2026-06-02.

Rollback boundary: revert only the bounded CI1-T4 routing metadata if dispatch
is withdrawn. Do not revert prior CI1-T3 or GC-053 closure evidence.

## Required Evidence

```powershell
python governance/compat/check_markdown_structural_completeness.py --base 15d8cec5 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 15d8cec5 --head HEAD --enforce
python governance/compat/check_system_loop_interlock.py --base 15d8cec5 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 15d8cec5 --head HEAD
```

## Corpus Completeness And Report Integrity

CI1-T4 consumes prior scan packets; it does not enumerate or claim completion
for a new filesystem corpus.

- Corpus task class: CROSS_CORPUS_INDEX_MODEL
- Corpus root: N/A - cross-corpus derived view over the cited T2 and T3 packets
- Snapshot time: 2026-06-02
- Enumeration command: N/A - no new filesystem corpus scan; source packets
  were previously enumerated with `rg --files --hidden --no-ignore`
- Manifest artifact or inline manifest: inline source-packet ledger below
- Manifest hash: N/A - no new filesystem manifest; source packets are cited
  individually
- Declared exclusions: all new source corpus reads; CI1-T4 consumes only the
  cited prior scan packets
- Processing ledger artifact or inline ledger: inline source-packet ledger
  below
- Allowed terminal statuses: `READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE`
- Reconciliation: manifest=2; ledger_terminal=2; exclusions=0; unresolved=0
- Unresolved files: 0
- Unreadable or unsupported files: 0
- Aggregation check: PASS
- Drift check: PASS at packet-reference dispatch level
- Output traceability:
  `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
- Adversarial verification: worker comparison plus reviewer sampling
- Corpus verdict: PARTIAL

| sourcePath | processingStatus | evidencePointer |
| --- | --- | --- |
| `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` | `READ` | CI1-T2 packet |
| `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md` | `READ` | CI1-T3 packet |

Reason for PARTIAL: CI1-T4 normalizes two accepted pilot packets. It does not
claim universal corpus coverage.

## Knowledge System Reconciliation

- Knowledge task class: CROSS_CORPUS_INDEX_MODEL
- Source manifest: inline two-packet source ledger in the Corpus Completeness
  And Report Integrity block
- Source manifest hash: N/A - packet-derived model; T2 and T3 packet hashes
  remain source evidence
- Enumeration safety: source packets were previously enumerated with `rg --files --hidden --no-ignore`; CI1-T4 performs no new filesystem scan
- Intake registry or ledger: inline source-packet ledger above
- Authority assets: 2 source packets
- Derived views:
  `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
- Semantic region ledger: worker-produced JSON `sourceMappings`
- Region reconciliation: assets=2; mapped=2; deferred=0; unmapped=0
- Orphan or unmapped assets: 0
- Cross-region links: worker-produced JSON `downstreamRoutes`
- Drift check: PASS at packet-reference dispatch level
- Rebuildability check: PASS requirement - worker must prove the JSON model is
  rebuildable from the cited T2 and T3 packets and the common standard
- Retrieval boundary: no runtime retrieval index
- Adversarial verification: worker comparison plus reviewer sampling
- Knowledge-map verdict: PARTIAL

Reason for PARTIAL: model normalization is a derived view and CI1-T5 sampling
remains required.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1-T4 is a private provenance model/spec tranche. No public-sync
remote, public repository commit, public artifact path, hosted proof, or
public README claim is included.

## Claim Boundary

CI1-T4 authorizes a bounded cross-corpus facet/index contract over two pilot
packets. It does not authorize runtime indexing, vector search, retrieval
ranking, LPCI implementation, legal advice, provider use, production readiness,
hosted readiness, or public readiness.
