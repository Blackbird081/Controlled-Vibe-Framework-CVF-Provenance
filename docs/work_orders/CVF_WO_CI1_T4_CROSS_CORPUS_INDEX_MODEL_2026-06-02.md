# CVF Work Order - CI1-T4 Cross-Corpus Index Model

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-02

## Purpose

Normalize the first two real CI1 scan packets into a machine-readable
cross-corpus index model and a human-readable reference contract.

This work order converts scan output into a typed downstream input. It does not
scan new legacy folders and does not implement a runtime index.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-02 acceptance of CI1-T4 continuation | ACCEPT |
| CI1-T4 GC-018 | `docs/baselines/CVF_GC018_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md` | ACCEPT |
| CI1 parent GC-018 | `docs/baselines/CVF_GC018_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_2026-06-02.md` | ACCEPT |
| CI1 roadmap | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | ACCEPT |
| Search/filter standard | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | ACCEPT |
| T2 packet | `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` | ACCEPT |
| T3 packet | `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md` | ACCEPT |
| GC-051 registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | ACCEPT |
| GC-052 interlock registry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | Dispatch T4 after GC-018 exists | no worker implementation |
| Worker | Create JSON model, reference spec, GC-052 interlock row, and completion review | no new corpus scan; no runtime/checker/guard edit; no commit/push |
| Reviewer | Validate typed model, rebuildability, gates, and claim boundary | reject prose-only index output |

## Scope

Allowed scope:

- read
  `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`;
- read
  `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`;
- read `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`;
- read `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- read `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- create `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`;
- create
  `docs/reference/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md`;
- update
  `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- create
  `docs/reviews/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md`;
- update
  `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
  CI1-T4 row/status only during worker execution;
- repair allowed-scope Markdown, JSON, interlock, and dispatch-quality defects.

Reviewer-only closure coordination after worker handoff:

- update session continuity paths `CVF_SESSION_MEMORY.md`,
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and
  `AGENT_HANDOFF_V15_2026-05-29.md`;
- update
  `docs/roadmaps/CVF_LPCI_LEGAL_POLICY_CORPUS_INTELLIGENCE_CHATBOT_USE_CASE_ROADMAP_2026-06-01.md`
  dependency status only;
- close this work order, its completion review, and the CI1 roadmap after
  committed-range reviewer gates pass.

These reviewer-only paths are not worker write ownership and do not relax the
worker forbidden scope.

Forbidden scope:

- reading or scanning `.private_reference/legacy/`;
- editing `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- editing CI1-T2 or CI1-T3 source packets;
- modifying runtime TypeScript, Python checker code, hook chains, guard docs,
  AGENTS, session front doors, active handoff, or state registry;
- implementing runtime indexing, embeddings, vector databases, graph guards,
  CLI/MCP commands, retrieval routes, LPCI UI/API, provider calls, or live
  proof;
- public-sync, commit, or push;
- claiming universal semantic coverage, legal correctness, production
  readiness, hosted readiness, or public readiness.

Risk ceiling: R1 documentation and machine-readable model normalization only.

## Required First Reads

1. `docs/baselines/CVF_GC018_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md`
2. `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
3. `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`
4. `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`
5. `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`
6. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_STANDARD_2026-06-02.md`
7. `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md`
8. `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md`
9. `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
10. `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base 15d8cec5 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 15d8cec5 --head HEAD
```

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| CI1-T4 GC-018 exists | `docs/baselines/CVF_GC018_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md` | full document | `CVF_GC018_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md` | CI1-T4 baseline | ACCEPT |
| Common facet schema exists | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | Common Facet Schema | `sourcePath` | corpus search/filter standard | ACCEPT |
| Query receipt minimum exists | `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md` | Minimum Query Receipt | `normalized query` | corpus search/filter standard | ACCEPT |
| T2 packet facet schema exists | `docs/audits/CVF_CI1_T2_GRAPHIFY_READINESS_PACKET_2026-06-02.md` | Corpus Search And Filter Readiness | `Common facet schema` | CI1-T2 packet | ACCEPT |
| T3 packet facet schema exists | `docs/audits/CVF_CI1_T3_GRAPH_GOVERNANCE_CORPUS_READINESS_PACKET_2026-06-02.md` | Common Facet Schema | `sourcePath` | CI1-T3 packet | ACCEPT |
| GC-051 registry exposes source corpora | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `corpora` | `corpora` | corpus scan registry | ACCEPT |
| GC-052 registry exposes connections | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `connections` | `connections` | system loop interlock registry | ACCEPT |
| Dispatch baseHead | N/A - git command | `git rev-parse --short HEAD` | `15d8cec5` | git repository state | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Normalize facets across two packets | Execution Plan | JSON model + spec | reviewer comparison | READY |
| Preserve typed downstream input | System Loop Interlock Requirement | JSON model + GC-052 row | GC-052 checker | READY |
| Preserve extensibility for LPCI | Expected Model Content | extension groups + downstream routes | reviewer check | READY |
| Avoid premature runtime index | Forbidden scope | no runtime diffs | git status/diff | READY |
| Prepare T5/T6/T7 continuation | Expected Model Content | downstream routing block | reviewer check | READY |

## Worker Autonomy / No-Question Rule

Proceed autonomously with comparing the two packet schemas, creating the JSON
model and spec, adding the GC-052 connection, producing the completion review,
running gates, and repairing allowed-scope defects.

Allowed-scope Markdown, JSON, interlock, and dispatch-quality failures are
mandatory repairs. Escalation is permitted only when remediation would expand
scope, touch forbidden paths, consume secrets/quota, run live provider proof,
perform public-sync, commit/push, or change the claim boundary.

## Pending Artifact Evidence Finality

Do not commit. Record `git status --short` in the completion review.
Do not cite committed-only or empty ranges as proof for pending files.

## Commit Mode And Base-Anchor Lifecycle

- Commit mode: WORKER_MUST_NOT_COMMIT
- `dispatchBaseHead`: `15d8cec5`
- `executionBaseHead`: capture with `git rev-parse --short HEAD` immediately
  before material edits
- `closureBaseHead`: `4c06491e`

Worker handoff boundary: return `COMPLETE_PENDING_REVIEW` with actual pending
paths and working-tree-aware component-gate evidence. Do not claim autorun
`pre-closure` PASS.

## Work-Order Fulfillment Manifest

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | No (produced during execution) | machine-readable downstream model |
| `docs/reference/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md` | No (produced during execution) | human-readable contract and boundary |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | Yes - update | GC-052 typed routing record |
| `docs/reviews/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md` | No (produced during execution) | pending worker completion evidence |
| `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | Optional update | CI1-T4 status only |

## Write Ownership

Owned:

- `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
- `docs/reference/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md`
- `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
- `docs/reviews/CVF_CI1_T4_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md`
- `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
  CI1-T4 row/status only

Forbidden:

- `.private_reference/legacy/` reads or writes;
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`;
- runtime source, governance checker, hook, or guard files;
- `AGENTS.md`, `CVF_SESSION_MEMORY.md`, active handoff, or state registry;
- public-sync clone;
- any file outside the owned list above for writing.

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `.private_reference/legacy/` | no new scan in T4 |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | input only |
| `EXTENSIONS/` | no runtime implementation authorized |
| `governance/compat/` | no checker maintenance authorized |
| `governance/toolkit/` | no guard maintenance authorized |
| public-sync clone | out of scope |

## Forbidden Filesystem State At Dispatch

| Forbidden path | State at dispatch (baseHead `15d8cec5`) | Outcome |
| --- | --- | --- |
| `.private_reference/legacy/` | no read/write authorization | COMPLIANT |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | input only; no write authorization | COMPLIANT |
| `EXTENSIONS/` | no runtime implementation authorized | COMPLIANT |
| `governance/compat/` and `governance/toolkit/` | no maintenance authorization | COMPLIANT |
| public-sync clone | no public-sync work authorized | COMPLIANT |

## System Loop Interlock Requirement

CI1-T4 must add an `ACTIVE` / `STRUCTURAL_GUARDED` connection named:

`scan-packets-to-cross-corpus-index`

to:

`docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`

Required data flow:

```text
docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json
  + CI1-T2 packet
  + CI1-T3 packet
  -> docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json
  -> CI1-T5 sampling and CI1-T7 LPCI intake bridge
```

The interlock record must include all GC-052 required fields and cite existing
artifacts. It does not authorize autonomous mutation, runtime indexing,
retrieval behavior, automatic roadmap creation, LPCI implementation, or public
claims.

## Expected Model Content

The JSON model must contain:

- `schemaVersion`
- `modelId`
- `generatedAt`
- `sourcePackets`
- `commonFacets`
- `domainExtensionGroups`
- `normalizationRules`
- `queryReceiptFields`
- `freshnessConflictStatuses`
- `sourceMappings`
- `downstreamRoutes`
- `claimBoundary`

Required common facets:

- `sourcePath`
- `normalizedPath`
- `sourceHash`
- `sourceRoot`
- `sourceFamily`
- `documentType`
- `topicTags`
- `knowledgeRegion`
- `ownerSurface`
- `processingStatus`
- `disposition`
- `evidencePointer`
- `sensitivity`
- `freshnessStatus`
- `freshnessCheckedAt`
- `answerClass`

Required downstream routes:

- `CI1-T5`
- `CI1-T6`
- `CI1-T7`

## Execution Plan

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Record `git status --short`.
3. Read the two CI1 packets and the common search/filter standard.
4. Compare T2/T3 facets and record canonical mappings, aliases, extension
   groups, required/optional status, and unresolved gaps.
5. Create `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`.
6. Create the human-readable reference spec.
7. Add `scan-packets-to-cross-corpus-index` to the GC-052 registry.
8. Create the completion review with claim/final/verification boundaries.
9. Update the CI1-T4 roadmap row/status only if useful.
10. Run working-tree-aware component gates and fix allowed-scope failures.
11. Return pending artifacts to reviewer without commit or push.

## Required Component Gates

```powershell
python -m json.tool docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json
python -m json.tool docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json
python governance/compat/check_system_loop_interlock.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
git diff --check
git status --short
```

## Evidence Requirements

- valid JSON model with both source packet paths;
- common facet inventory and source-to-canonical mapping rows;
- domain-extension grouping with legal/policy fields kept vocabulary-only;
- query receipt and freshness/conflict vocabulary;
- GC-052 `scan-packets-to-cross-corpus-index` record;
- completion review with rebuildability statement;
- `git diff --check` result;
- `git status --short` result;
- explicit no-new-scan, no-runtime, no-provider, no-commit, and no-push
  boundary.

## Acceptance Criteria

- JSON model exists and is valid JSON.
- JSON model cites both T2 and T3 source packets.
- All common facet fields from the standard appear in the model.
- Technical/project and legacy-absorption fields remain extension groups.
- Legal/policy fields remain extension vocabulary, not fabricated populated
  values.
- Query receipt and freshness/conflict vocabulary are present.
- GC-052 registry contains `scan-packets-to-cross-corpus-index`.
- Completion review states the model is rebuildable from cited source packets.
- No new legacy source was scanned.
- No runtime, checker, hook-chain, guard, public-sync, provider, commit, or push
  action occurred.

## Review Gate

CI1-T4 may be returned for review only after the JSON model, reference spec,
GC-052 connection, and completion review exist; working-tree-aware component
gates pass; allowed-scope defects are repaired; and pending file status is
recorded.

## Handoff Prompt

Execute the work order autonomously. Do not ask whether to fix an allowed-scope
gate failure; fix it and rerun. Stop only when a repair would exceed scope,
touch forbidden paths, consume secrets/quota, require live proof, change the
claim boundary, or perform commit/push/public-sync.

Return:

- created/updated file list;
- `executionBaseHead`;
- component-gate results;
- `git status --short`;
- any unresolved gap routed to CI1-T5, CI1-T6, or CI1-T7;
- explicit statement that no commit or push was performed.

## Return-To-Orchestrator Conditions

Return only if execution requires new corpus reads, scope expansion, forbidden
path edits, runtime/checker/guard maintenance, public-sync, secrets/quota,
live/provider proof, commit/push, or a claim-boundary change.

## Operator Checkpoint

Operator accepted the CI1-T4 continuation after CI1-T3 bounded closure. Worker
may normalize the two existing packets only. LPCI runtime remains blocked until
T4 closure plus CI1-T5, CI1-T6, and CI1-T7.

## Closure Checklist

- [x] JSON model created and valid
- [x] reference spec created
- [x] GC-052 interlock row added
- [x] completion review created
- [x] both source packets cited
- [x] downstream routes T5/T6/T7 recorded
- [x] component gates PASS
- [x] pending worktree paths recorded
- [x] no forbidden path touched
- [x] no commit or push performed by worker

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: CI1-T4 is private corpus-intelligence contract work. No public-sync
remote, public repository commit, public artifact path, hosted proof, or
public README claim is included.

## Claim Boundary

CI1-T4 creates a bounded cross-corpus index-model contract over two pilot
packets. It does not create a runtime search index, embedding pipeline, vector
database, graph execution route, LPCI chatbot, legal advice capability,
provider proof, production readiness, hosted readiness, or public readiness.
