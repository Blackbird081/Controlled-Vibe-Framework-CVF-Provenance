# CVF Work Order - CI1-T5 Classification Sampling Protocol

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-02

## Purpose

Adversarially sample the committed CI1-T4 cross-corpus model and emit a
machine-readable result that CI1-T6 can use for the checker decision.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-02 sequential CI1 continuation | ACCEPT |
| CI1-T5 GC-018 | `docs/baselines/CVF_GC018_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_2026-06-02.md` | ACCEPT |
| CI1 roadmap | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | ACCEPT |
| T4 completion | `docs/reviews/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md` | ACCEPT |
| T4 JSON model | `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | ACCEPT |
| GC-051 registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ACCEPT |
| GC-052 registry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch T5 after T4 closure | no worker implementation |
| Worker | create results JSON, protocol, GC-052 row, completion review | bounded read-only sampling; no commit/push |
| Reviewer | verify sample evidence, totals, gates, and claim boundary | reject fabricated or prose-only sampling |

## Scope

Allowed scope:

- read `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- read `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`;
- read `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`;
- read
  `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`;
- read bounded sample evidence only from
  `.private_reference/legacy/CVF_Important/Knowledge Base_Graphify/`;
- read bounded sample evidence only from
  `.private_reference/legacy/CVF ADD/code-review-graph/`;
- create
  `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`;
- create
  `docs/reference/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_2026-06-02.md`;
- update
  `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- create
  `docs/reviews/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_COMPLETION_2026-06-02.md`;
- update
  `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
  CI1-T5 row/status only;
- repair allowed-scope Markdown, JSON, interlock, and dispatch-quality defects.

Forbidden scope:

- enumerating or scanning any new legacy root or sibling folder;
- editing legacy sources or `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- modifying runtime source, Python checkers, hook chains, guard docs, AGENTS,
  session front doors, active handoff, or state registry;
- implementing runtime indexing, graph guards, CLI/MCP commands, retrieval
  routes, LPCI UI/API, provider calls, or live proof;
- public-sync, commit, or push;
- claiming universal semantic coverage, legal correctness, production
  readiness, hosted readiness, or public readiness.

Risk ceiling: R1 private read-only sampling and documentation/data output.

## Required First Reads

1. `docs/baselines/CVF_GC018_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_2026-06-02.md`
2. `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
3. `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
4. `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
5. `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
6. `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`
7. `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`
8. `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`
9. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base e9f3983d --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base e9f3983d --head HEAD
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| CI1-T5 GC-018 exists | `docs/baselines/CVF_GC018_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_2026-06-02.md` | full document | `CVF_GC018_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_2026-06-02.md` | CI1-T5 baseline | ACCEPT |
| T4 model exists | `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | `downstreamRoutes` | `CI1-T5` | cross-corpus index model | ACCEPT |
| Sampling targets exist | `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | `downstreamRoutes.CI1-T5` | `samplingTargets` | cross-corpus index model | ACCEPT |
| Standard requires sampling | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | Adversarial sampling | `accepted, deferred, rejected, zero-result, high-risk, and random rows` | search/filter standard | ACCEPT |
| Template defines rows | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | 8.2 Adversarial Sample Records | `sampleId` | readiness template | ACCEPT |
| T2 packet exists | `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` | 8. Adversarial Sampling Plan | `Sample categories covered` | CI1-T2 packet | ACCEPT |
| T3 packet exists | `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md` | Adversarial Sampling Plan | `Sample Categories` | CI1-T3 packet | ACCEPT |
| Dispatch baseHead | N/A - git command | `git rev-parse --short HEAD` | `e9f3983d` | git repository state | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Sample T4 model classifications | Execution Plan | sampling JSON + protocol | reviewer evidence-pointer check | READY |
| Include accepted/deferred/rejected/zero-result rows | Sampling Rules | category totals + records | JSON parser and reviewer check | READY |
| Preserve T6 machine-readable input | System Loop Interlock Requirement | JSON + GC-052 row | GC-052 checker | READY |
| Avoid broad rescans and runtime work | Forbidden scope | bounded read-only diff | git status/diff | READY |

## Worker Autonomy / No-Question Rule

Proceed autonomously with bounded sampling, artifact creation, GC-052 routing,
gate execution, and allowed-scope repair. Ask the operator only if remediation
would expand scope, touch forbidden paths, consume secrets/quota, run live
provider proof, alter the claim boundary, or perform commit/push/public-sync.

## Pending Artifact Evidence Finality

Do not commit. Record `git status --short` in the completion review. Do not cite
committed-only or empty ranges as proof for pending files.

## Commit Mode And Base-Anchor Lifecycle

- Commit mode: WORKER_MUST_NOT_COMMIT
- `dispatchBaseHead`: `e9f3983d`
- `executionBaseHead`: capture with `git rev-parse --short HEAD` immediately
  before material edits
- `closureBaseHead`: N/A - reviewer / committer selects after review

Worker handoff boundary: return `COMPLETE_PENDING_REVIEW` with pending paths and
working-tree-aware component-gate evidence. Do not claim autorun pre-closure
PASS.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` | No - produced during execution | machine-readable T6 input |
| `docs/reference/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_2026-06-02.md` | No - produced during execution | sampling method and boundary |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | Yes - update | GC-052 typed routing record |
| `docs/reviews/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_COMPLETION_2026-06-02.md` | No - produced during execution | pending worker completion evidence |
| `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | Optional update | CI1-T5 status only |

## Write Ownership

Owned:

- `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`
- `docs/reference/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_2026-06-02.md`
- `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
- `docs/reviews/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_COMPLETION_2026-06-02.md`
- `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
  CI1-T5 row/status only

Forbidden:

- `.private_reference/legacy/` writes;
- new legacy root discovery;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` writes;
- runtime source, governance checker, hook, or guard files;
- session continuity paths;
- public-sync clone;
- any file outside the owned list above for writing.

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `.private_reference/legacy/` writes | read-only bounded source verification |
| new legacy roots or siblings | no broad rescan |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` writes | input only |
| `EXTENSIONS/` | no runtime implementation |
| `governance/compat/` | no checker maintenance |
| `governance/toolkit/` | no guard maintenance |
| public-sync clone | out of scope |

## Forbidden Filesystem State At Dispatch

| Forbidden path | State at dispatch (baseHead `e9f3983d`) | Outcome |
| --- | --- | --- |
| new `.private_reference/legacy/` roots or siblings | no discovery authorization | COMPLIANT |
| `.private_reference/legacy/` writes | read-only bounded verification only | COMPLIANT |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` writes | input only | COMPLIANT |
| `EXTENSIONS/` | no runtime implementation authorized | COMPLIANT |
| `governance/compat/` and `governance/toolkit/` | no maintenance authorization | COMPLIANT |
| public-sync clone | no public-sync work authorized | COMPLIANT |

## System Loop Interlock Requirement

Add an `ACTIVE` / `STRUCTURAL_GUARDED` connection:

`cross-corpus-index-to-classification-sampling`

```text
docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json
  -> docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json
  -> CI1-T6 checker decision
```

## Sampling Rules

- consult GC-051 registry before reading source evidence;
- do not enumerate new roots;
- sample at least ACCEPTED=3, DEFERRED=2, REJECTED=2, ZERO_RESULT=2,
  HIGH_RISK=2 when rows are available;
- use deterministic sample IDs and cite evidence pointers;
- if a category lacks enough rows, use `UNAVAILABLE_WITH_REASON`;
- record NR-04, NR-05, NR-06, and NR-07 impact for T6;
- do not convert structural PASS into semantic-certification claims.

## Execution Plan

1. Capture `executionBaseHead` and clean `git status --short`.
2. Read the GC-051 registry, T4 model, T2 packet, and T3 packet.
3. Select deterministic samples across all required categories.
4. Read only cited bounded pilot-root source evidence where needed.
5. Create the sampling JSON and protocol.
6. Add the GC-052 sampling route.
7. Create completion review with evidence trace and claim boundaries.
8. Update CI1-T5 roadmap row/status only if useful.
9. Run component gates and repair allowed-scope defects.
10. Return pending artifacts without commit or push.

## Required Component Gates

```powershell
python -m json.tool docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json
python -m json.tool docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json
python governance/compat/check_system_loop_interlock.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_corpus_intelligence_classification.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --check
git status --short
```

## Acceptance Criteria

- results JSON exists and parses;
- result cites T4 model, T2 packet, T3 packet, and GC-051 consultation;
- category totals reconcile with sample records;
- each available category meets its minimum or records
  `UNAVAILABLE_WITH_REASON`;
- each sample cites evidence and records expected versus actual behavior;
- NR-04 through NR-07 route into explicit T6 decision inputs;
- GC-052 registry contains `cross-corpus-index-to-classification-sampling`;
- no new corpus root, runtime, provider, public-sync, worker commit, or push.

## Return-To-Orchestrator Conditions

Return only if execution requires a new corpus root, scope expansion, forbidden
path edit, runtime/checker/guard maintenance, public-sync, secrets/quota,
live/provider proof, commit/push, or a claim-boundary change.

## Operator Checkpoint

Operator authorized sequential CI1 continuation after T4 closure. Worker may
sample only the two existing registered pilots. CI1-T6 remains locked until T5
reviewer closure.

## Review Gate

CI1-T5 may be returned for review only after the results JSON, protocol,
GC-052 connection, and completion review exist; working-tree-aware component
gates pass; allowed-scope defects are repaired; category totals reconcile; and
pending file status is recorded.

## Closure Checklist

- [ ] GC-051 registry consulted
- [ ] T4 model read
- [ ] deterministic category selection recorded
- [ ] results JSON created and valid
- [ ] protocol created
- [ ] GC-052 sampling route added
- [ ] completion review created with Evidence Trace Block
- [ ] NR-04 through NR-07 routed to T6 inputs
- [ ] component gates PASS
- [ ] pending paths recorded
- [ ] no forbidden path touched
- [ ] no worker commit or push

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1-T5 is private sampling evidence. No public-sync remote, public
repository commit, public artifact path, hosted proof, or public README claim
is included.

## Claim Boundary

CI1-T5 creates bounded adversarial sampling evidence and machine-readable T6
input. It does not certify semantic correctness, create a runtime index,
implement LPCI, provide legal advice, call providers, or claim production,
hosted, or public readiness.
