# CVF GC-018 - CI1-T3 Graph Governance Corpus Deep Scan

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-02

baseHead: `13c91de8`

## Purpose

Authorize CI1-T3 as the second bounded CI1 corpus execution. The target corpus is
the graph governance source family at:

`.private_reference/legacy/CVF ADD/code-review-graph/`

Filesystem enumeration shows 7 in-scope files. CI1-T3 applies the CI1 readiness
packet workflow to this folder and must route any findings into GC-051 Corpus
Scan Registry and the GC-052 scan-loop-to-learning-loop interlock.

## Source

Predecessor evidence:

- CI1 parent GC-018:
  `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md`
- CI1-T1 readiness template:
  `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`
- CI1-T2 Graphify scan completion:
  `docs/reviews/CVF_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_COMPLETION_2026-06-02.md`
- CI1-T2 finding packet:
  `docs/corpus-intelligence/findings/legacy-cvf-important-graphify.md`
- Graphify guard enforcement parking roadmap:
  `docs/roadmaps/CVF_GRAPHIFY_GUARD_ENFORCEMENT_ROADMAP_2026-06-02.md`
- GC-051 corpus scan registry:
  `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- GC-052 interlock registry:
  `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`

## Decision

Proceed with CI1-T3 on `CVF ADD/code-review-graph/`.

Rationale:

- the folder is small enough for a deep scan;
- it is directly related to CI1-T2 Finding F2, graph guard/governance
  enforcement;
- it provides a second graph-adjacent corpus before CVF designs a cross-corpus
  index model;
- it tests whether GC-051 findings and GC-052 interlock routing are usable by a
  worker, not just by the orchestrator.

The previous CI1-T3 label "Cross-Corpus Index Model" is intentionally deferred
until at least two real CI1 scan packets exist.

## Scope / Target / Owner Boundary

Corpus target: `.private_reference/legacy/CVF ADD/code-review-graph/`

Known files at dispatch:

| File | Status |
| --- | --- |
| `CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md` | IN_SCOPE |
| `CVF_GRAPH_GOVERNANCE_EXTENSION_SPEC.md` | IN_SCOPE |
| `CVF_GRAPH_IMPLEMENTATION_PLAN.md` | IN_SCOPE |
| `CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md` | IN_SCOPE |
| `CVF_GRAPH_KNOWLEDGE_SPEC.md` | IN_SCOPE |
| `README.md` | IN_SCOPE |
| `Thong_tin.md` | IN_SCOPE |

Total in-scope files: 7

CVF owns:

- corpus evidence discipline;
- readiness packet, classification ledger, and completion review;
- scan finding normalization into GC-051;
- learning disposition routing via GC-052 when findings exist.

Worker owns:

- reading all 7 files;
- producing the filled packet and completion review;
- updating the scan registry and finding packet if findings exist;
- running required gates and repairing allowed-scope defects.

Out of scope:

- files outside `CVF ADD/code-review-graph/`;
- implementing graph runtime, CLI commands, vector stores, indexers, or
  chatbot/product behavior;
- modifying governance checkers, hook chains, guard docs, or runtime source;
- public-sync, push, or commit;
- semantic correctness, production readiness, hosted readiness, or public
  readiness claims.

## Claim Boundary

CI1-T3 claims only a bounded corpus-intelligence deep scan of the 7-file graph
governance family. It does not claim graph guard enforcement, graph CLI
implementation, runtime retrieval quality, LPCI implementation, production
readiness, hosted readiness, or public readiness.

## Risk Register

| Risk | Control |
| --- | --- |
| Worker scans too broadly | Work order forbids files outside `code-review-graph/` |
| Worker treats legacy spec as current runtime fact | Source Verification must distinguish legacy proposal from current CVF source |
| Findings remain trapped in prose | GC-051 registry update and finding packet required when findings exist |
| Learning loop remains disconnected | GC-052 routing evidence required for deferred or blocked findings |
| Worker implements graph guard/CLI prematurely | runtime/checker/source edits forbidden |

## Knowledge Absorption Blind-Spot Control Block

Standard read:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-06-01.md`

- Source inventory:
  - Root: `.private_reference/legacy/CVF ADD/code-review-graph/`
  - Shell command run:
    `rg --files --hidden --no-ignore ".private_reference/legacy/CVF ADD/code-review-graph"`
  - Shell output:

    ```text
    .private_reference/legacy/CVF ADD/code-review-graph\Thong_tin.md
    .private_reference/legacy/CVF ADD/code-review-graph\CVF_GRAPH_IMPLEMENTATION_PLAN.md
    .private_reference/legacy/CVF ADD/code-review-graph\README.md
    .private_reference/legacy/CVF ADD/code-review-graph\CVF_GRAPH_GOVERNANCE_EXTENSION_SPEC.md
    .private_reference/legacy/CVF ADD/code-review-graph\CVF_GRAPH_KNOWLEDGE_SPEC.md
    .private_reference/legacy/CVF ADD/code-review-graph\CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md
    .private_reference/legacy/CVF ADD/code-review-graph\CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md
    ```

  - Total file count: 7
  - Sorted-list manifest hash: `d921f708e3b321343fae43060a7fb447a166a7eba6584f23de151422e663f51a`

- Prior absorption evidence resolved:
  - LHW-RESCAN-C broad scan:
    `docs/reviews/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md`
  - CI1-T2 Graphify scan:
    `docs/reviews/CVF_CI1_T2_GRAPHIFY_LEGACY_RESCAN_PILOT_COMPLETION_2026-06-02.md`
  - CI1-T2 Finding F2:
    `docs/corpus-intelligence/findings/legacy-cvf-important-graphify.md#f2--guard-spec-g-gm-01-through-g-gm-08-absent-from-cvf-runtime`

- Source families skipped:
  - other `CVF ADD/` folders are out of scope and require separate CI1
    tranches;
  - `CVF 16.5/tolaria/` is a future candidate and is not part of CI1-T3.

- Owner-surface normalization:
  - graph governance concepts map to KGR/Graphify governance planning surfaces;
  - machine-check or guard enforcement candidates must be routed through
    GC-051/F2G, not implemented inside CI1-T3;
  - CLI candidates must be routed to the graph CLI backlog, not implemented in
    CI1-T3.

- Accept/defer/reject matrix at GC-018 level:

| Candidate | Disposition | Reason |
| --- | --- | --- |
| Deep-read all 7 files | ACCEPT | CI1-T3 target scope |
| Normalize graph governance findings | ACCEPT | feeds CI1-T2 F2 follow-up |
| Implement graph guard enforcement | DEFER | separate GC/work order required |
| Implement graph CLI commands | DEFER | separate graph CLI roadmap required |
| Scan full `CVF ADD/` root | REJECT | too broad for this tranche |

- Adversarial role review:
  - Implementer: the 7-file corpus is small and directly useful.
  - Skeptic/Auditor: legacy graph governance docs may propose capabilities CVF
    should not implement yet; Source Verification and claim boundary mitigate.
  - Product/Operator Advocate: this scan improves corpus intelligence for
    future legal/policy and project-corpus search because it exercises
    cross-corpus facet normalization on a second real corpus.
  - Safety/Boundary Owner: no runtime mutation, no autonomous learning mutation,
    no public export.

- Gate 7 completeness cross-check:

| File/folder | In source inventory? | Disposition | Reason |
| --- | --- | --- | --- |
| `CVF_GRAPH_CONTEXT_RESOLUTION_SPEC.md` | YES | READ by worker | In scope |
| `CVF_GRAPH_GOVERNANCE_EXTENSION_SPEC.md` | YES | READ by worker | In scope |
| `CVF_GRAPH_IMPLEMENTATION_PLAN.md` | YES | READ by worker | In scope |
| `CVF_GRAPH_INTEGRATION_SURFACE_SPEC.md` | YES | READ by worker | In scope |
| `CVF_GRAPH_KNOWLEDGE_SPEC.md` | YES | READ by worker | In scope |
| `README.md` | YES | READ by worker | In scope |
| `Thong_tin.md` | YES | READ by worker | In scope |
| Other `CVF ADD/` folders | NO | SKIPPED | Separate tranche |

- Blind-spot verdict: CLEAR

Rationale: all 7 files are filesystem-confirmed, prior broad scan evidence is
resolved, out-of-scope folders are explicitly rejected for this tranche, and all
findings must route into GC-051/GC-052 rather than remaining prose-only.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| CI1-T1 readiness template exists | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | full document | `CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | CI1 packet template | ACCEPT |
| GC-051 registry exists | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `corpora` | `corpora` | corpus scan registry | ACCEPT |
| GC-052 interlock exists | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `scan-loop-to-learning-loop` | `scan-loop-to-learning-loop` | system loop interlock registry | ACCEPT |
| Target folder has 7 files | N/A - filesystem enumeration | `rg --files --hidden --no-ignore` output | `.private_reference/legacy/CVF ADD/code-review-graph/` | filesystem source corpus | ACCEPT |
| Dispatch baseHead | N/A - git command | `git rev-parse --short HEAD` | `13c91de8` | git repository state | ACCEPT |

## Required Evidence

```powershell
python governance/compat/check_corpus_completeness_report_integrity.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_corpus_to_knowledge_map_reconciliation.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_corpus_scan_registry.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_system_loop_interlock.py --base 13c91de8 --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 13c91de8 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 13c91de8 --head HEAD
```

## Current Runtime Freshness Verification

CI1-T3 is a documentation-only corpus scan dispatch. It does not claim that
current CVF runtime source lacks or implements any graph guard, graph CLI, graph
index, vector store, retrieval route, or chatbot behavior.

Runtime/source claims in this GC-018 are scope-boundary statements only:

- `runtimeExecutionAuthorized: false` for CI1-T3;
- no runtime TypeScript, Python checker, hook-chain, or guard-doc edit is
  authorized by this GC-018;
- any legacy concept that appears implementation-worthy must be routed into
  GC-051/F2G evidence and a later GC/work order before source modification.

## Corpus Completeness And Report Integrity

This GC-018 is a dispatch authorization document. The worker performs the deep
read and produces the filled packet.

- Corpus task class: GC018_DISPATCH_AUTHORIZATION
- Corpus root: `.private_reference/legacy/CVF ADD/code-review-graph/`
- Snapshot time: 2026-06-02
- Enumeration command: `rg --files --hidden --no-ignore ".private_reference/legacy/CVF ADD/code-review-graph"`
- Manifest artifact or inline manifest: inline shell output above
- Manifest hash: `d921f708e3b321343fae43060a7fb447a166a7eba6584f23de151422e663f51a`
- Processing ledger artifact or inline ledger: worker-produced packet
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=7 ledger_terminal=0 exclusions=0 unresolved=7
- Unresolved files: 7 (worker resolves all to READ in packet)
- Declared exclusions: other `CVF ADD/` folders
- Unreadable or unsupported files: none known
- Aggregation check: PASS at dispatch inventory level
- Drift check: PASS at dispatch inventory level
- Output traceability: `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`
- Adversarial verification: worker-produced packet
- Corpus verdict: PARTIAL

Reason for PARTIAL: this is authorization plus inventory, not the worker's
completed corpus read.

## Knowledge System Reconciliation

- Knowledge task class: GC018_DISPATCH_AUTHORIZATION
- Source manifest: inline shell output above
- Source manifest hash: `d921f708e3b321343fae43060a7fb447a166a7eba6584f23de151422e663f51a`
- Enumeration safety: `rg --files --hidden --no-ignore`
- Intake registry or ledger: worker-produced packet
- Authority assets: 7
- Derived views: none at GC-018 level
- Semantic region ledger: worker-produced packet
- Region reconciliation: assets=7; mapped=0; deferred=7; unmapped=0
- Orphan or unmapped assets: 0
- Cross-region links: worker-produced packet
- Drift check: PASS at dispatch inventory level
- Rebuildability check: N/A - no derived view produced by GC-018
- Retrieval boundary: no retrieval claims at GC-018 level
- Adversarial verification: worker-produced packet
- Knowledge-map verdict: PARTIAL

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1-T3 reads private legacy corpus under `.private_reference/legacy/`.
No public-sync remote, public repository commit, public artifact path, hosted
proof, or public README claim is included.
