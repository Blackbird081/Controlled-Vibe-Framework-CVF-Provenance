# CVF GC-018 - CI1-T5 Classification Sampling Protocol

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-02

baseHead: `e9f3983d`

## Purpose

Authorize CI1-T5 to adversarially sample the committed CI1-T4 cross-corpus
index model and emit a machine-readable sampling result for CI1-T6.

CI1-T5 checks classification discipline and claim boundaries over the first two
pilot packets. It is not a broad legacy rescan, runtime index, retrieval route,
graph guard implementation, LPCI implementation, or semantic-certification
claim.

## Source

- CI1 roadmap:
  `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
- T4 completion:
  `docs/reviews/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md`
- T4 model:
  `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
- T2 packet:
  `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`
- T3 packet:
  `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`
- readiness template:
  `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`
- search/filter standard:
  `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
- GC-052 registry:
  `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`

## Decision

Proceed with a bounded documentation/data tranche that creates:

- `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`
- `docs/reference/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_2026-06-02.md`
- GC-052 route `cross-corpus-index-to-classification-sampling`
- a bounded completion review.

The sampling JSON is the primary downstream input for CI1-T6. Markdown explains
the method, evidence, failures, and claim boundary.

## Scope / Target / Owner Boundary

Worker may:

- read the committed T4 model and T2/T3 packet evidence;
- consult the GC-051 registry before source verification;
- read only the two registered pilot roots for bounded source cross-checks:
  `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/` and
  `.private_reference/legacy/CVF ADD/code-review-graph/`;
- create the sampling JSON, protocol, and completion review;
- add the bounded GC-052 sampling route;
- update only the CI1-T5 roadmap row/status;
- repair allowed-scope documentation, JSON, interlock, and dispatch-quality
  defects.

Worker must not:

- enumerate or scan any new legacy root or sibling folder;
- edit legacy sources, runtime source, checker code, hook chains, guard docs,
  session front doors, active handoff, or state registry;
- implement graph guards, CLI/MCP commands, retrieval runtime, LPCI UI/API,
  provider calls, live proof, public-sync, commit, or push;
- claim universal semantic correctness, legal correctness, production
  readiness, hosted readiness, or public readiness.

Risk ceiling: R1 read-only sampling and private documentation/data output.

## Sampling Contract

The result JSON must include:

| Field | Requirement |
| --- | --- |
| Identity | schemaVersion, resultId, generatedAt, sourceModelPath |
| Source evidence | T2 packet, T3 packet, GC-051 registry consultation |
| Selection method | deterministic category selection and bounded source cross-check rule |
| Category summary | required, available, sampled, pass, fail, unavailable-with-reason |
| Sample records | sampleId, category, sourcePath/query, expectedBehavior, actualBehavior, evidencePointer, verdict, notes |
| Normalization gaps | NR-04, NR-05, NR-06, NR-07 and observed impact |
| T6 inputs | structural-check candidates, documentation-only gaps, non-candidates |
| Claim boundary | no runtime, semantic-certification, LPCI, provider, or public claim |

Required categories:

| Category | Minimum |
| --- | --- |
| ACCEPTED | 3 |
| DEFERRED | 2 |
| REJECTED | 2 |
| ZERO_RESULT | 2 |
| HIGH_RISK | 2 |

If a category has fewer available rows, the result must record
`UNAVAILABLE_WITH_REASON`; it must not fabricate rows.

## Knowledge Absorption Blind-Spot Control Block

- Prior evidence resolved: T4 model, T2 packet, T3 packet, and GC-051 registry.
- New source discovery: forbidden. Only bounded source cross-check reads inside
  the two registered pilot roots are allowed.
- Owner-surface normalization: T5 tests T4 classifications and claim
  boundaries; it does not create runtime owner surfaces.
- Deferred signals: NR-04 through NR-07 must be routed into T6 decision input.
- Adversarial roles:
  - Implementer checks reproducible sampling records.
  - Skeptic challenges overclaim and zero-result evidence.
  - Product advocate verifies T6 receives machine-readable output.
  - Safety owner blocks new scans, runtime implementation, and public claims.
- Blind-spot verdict: CLEAR_FOR_BOUNDED_CLASSIFICATION_SAMPLING

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| CI1-T5 roadmap row exists | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | Tranche Plan | `CI1-T5` | CI1 roadmap | ACCEPT |
| T4 model exists | `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | `downstreamRoutes` | `CI1-T5` | cross-corpus index model | ACCEPT |
| T4 names sampling targets | `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | `downstreamRoutes.CI1-T5` | `samplingTargets` | cross-corpus index model | ACCEPT |
| Standard requires adversarial categories | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | Adversarial sampling | `accepted, deferred, rejected, zero-result, high-risk, and random rows` | search/filter standard | ACCEPT |
| Template defines sample ledger | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | 8. Adversarial Sampling Plan | `Adversarial Sample Records` | readiness packet template | ACCEPT |
| T2 packet has samples | `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` | 8. Adversarial Sampling Plan | `Sample categories covered` | CI1-T2 packet | ACCEPT |
| T3 packet has samples | `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md` | Adversarial Sampling Plan | `Sample Categories` | CI1-T3 packet | ACCEPT |
| GC-052 registry exists | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `connections` | `connections` | system loop interlock registry | ACCEPT |
| Dispatch baseHead | N/A - git command | `git rev-parse --short HEAD` | `e9f3983d` | git repository state | ACCEPT |

## System Loop Interlock Requirement

Add one `ACTIVE` / `STRUCTURAL_GUARDED` GC-052 connection:

`cross-corpus-index-to-classification-sampling`

Required route:

```text
docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json
  -> bounded adversarial samples with evidence pointers
  -> docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json
  -> CI1-T6 checker decision
```

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: synchronize protected session front-door
state for bounded CI1-T5 dispatch only. No guard checker, hook-chain, guard
document, runtime, or public-sync edit is authorized.

Protected paths:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Operator authorization: operator authorized sequential CI1 continuation after
CI1-T4 completion on 2026-06-02.

Rollback boundary: revert only the bounded CI1-T5 dispatch routing metadata if
dispatch is withdrawn. Do not revert prior CI1-T4 closure evidence.

## Required Evidence / Verification

```powershell
python governance/compat/check_markdown_structural_completeness.py --base e9f3983d --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base e9f3983d --head HEAD --enforce
python governance/compat/check_system_loop_interlock.py --base e9f3983d --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base e9f3983d --head HEAD
git diff --check
git status --short
```

## Corpus Completeness And Report Integrity

CI1-T5 consumes registered prior packets and performs bounded source
cross-checks. It does not claim a new corpus enumeration.

- Corpus task class: ADVERSARIAL_CLASSIFICATION_SAMPLING
- Corpus root: two registered pilot packet artifacts plus bounded cited reads
  inside their registered roots only
- Snapshot time: 2026-06-02
- Enumeration command:
  `rg --files --hidden --no-ignore ".private_reference/legacy/CVF_Important/Knowledge Base_Graphify" ".private_reference/legacy/CVF ADD/code-review-graph"`
  for bounded source cross-checks after GC-051 registry consultation
- Manifest artifact or inline manifest: inline two-packet ledger below
- Manifest hash: N/A - packet-derived sampling input; T2 hash `a88e3412` and
  T3 hash `d921f708` remain source evidence
- Declared exclusions: every legacy root and sibling folder outside the two
  registered pilots
- Processing ledger artifact or inline ledger: inline two-packet ledger below
- Allowed terminal statuses: `READ | SKIPPED_WITH_REASON | DEFERRED |
  BLOCKED_UNREADABLE`
- Reconciliation: manifest=2; ledger_terminal=2; exclusions=0; unresolved=0
- Unresolved files: 0
- Unreadable or unsupported files: 0
- Aggregation check: PASS at packet-reference dispatch level
- Drift check: worker records registry consultation and source-pointer checks
- Output traceability:
  `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`
- Adversarial verification: worker sampling plus reviewer evidence-pointer
  verification
- Corpus verdict: PARTIAL

| sourcePath | processingStatus | evidencePointer |
| --- | --- | --- |
| `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` | `READ` | T2 packet sampling and classification ledgers |
| `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md` | `READ` | T3 packet sampling and classification ledgers |

Reason for PARTIAL: bounded sampling checks two pilot packets only.

## Knowledge System Reconciliation

- Knowledge task class: ADVERSARIAL_CLASSIFICATION_SAMPLING
- Source manifest: inline two-packet source ledger in the Corpus Completeness
  And Report Integrity block
- Source manifest hash: N/A - packet-derived sampling; T2 and T3 packet hashes
  remain source evidence
- Enumeration safety:
  `rg --files --hidden --no-ignore ".private_reference/legacy/CVF_Important/Knowledge Base_Graphify" ".private_reference/legacy/CVF ADD/code-review-graph"`
  is bounded to the two registered pilots; T5 performs no broad filesystem
  discovery
- Intake registry or ledger:
  `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- Authority assets: 2 source packets plus bounded cited source reads
- Derived views: input `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`;
  output
  `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`
- Semantic region ledger: worker-produced JSON sample records grouped by
  category
- Region reconciliation: assets=2; mapped=2; deferred=0; unmapped=0 at
  packet-reference dispatch level
- Orphan or unmapped assets: 0 at packet-reference dispatch level
- Cross-region links: T4 downstream route into T5 and T5 route into T6 checker
  decision
- Drift check: PASS at packet-reference dispatch level
- Rebuildability check: PASS requirement - results rebuild from cited sample
  records
- Retrieval boundary: no runtime retrieval or ranking
- Adversarial verification: worker source-pointer sampling plus reviewer
  category-total recomputation
- Knowledge-map verdict: PARTIAL

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1-T5 is private sampling evidence. No public-sync remote, public
repository commit, public artifact path, hosted proof, or public README claim
is included.

## Claim Boundary

CI1-T5 authorizes bounded adversarial sampling and machine-readable T6 input.
It does not authorize broad rescans, runtime indexing, graph execution, LPCI
implementation, legal advice, provider use, production readiness, hosted
readiness, or public readiness.
