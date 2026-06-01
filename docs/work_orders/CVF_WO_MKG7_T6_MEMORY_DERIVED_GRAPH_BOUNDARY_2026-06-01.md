# CVF Work Order - MKG7-T6 Memory Derived Graph Boundary

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-01

## Purpose

Produce a documentation-only reference packet that explicitly records the
boundary between source authority and rebuildable derived views (graph,
semantic-region, Palace, summary, cache, snapshot, retrieval indexes). The
packet makes the boundary drift-detectable so future agents cannot treat derived
graph lookups as overriding source authority.

T6 is documentation-only. No runtime/source code changes of any kind.

Success: reference document exists with explicit source-vs-derived boundary and
drift-detectability statement, markdown-structural gate PASS, public-export gate
PASS, both files pending and uncommitted.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 dispatch MKG7 T2–T7 for worker execution | ACCEPT |
| MKG7-T6 GC-018 | `docs/baselines/CVF_GC018_MKG7_T6_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md` | ACCEPT |
| MKG7 roadmap | `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | ACCEPT |
| T1 contract | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch and review pending output | no silent scope expansion |
| Worker | write boundary reference doc + completion review | no `.ts` edits, no commit |
| Reviewer | verify source-vs-derived boundary is explicit and drift-detectability stated | reject vague boundary that could authorize graph-as-source |

## Scope

Allowed scope:

- create `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md`;
- create `docs/reviews/CVF_MKG7_T6_MEMORY_DERIVED_GRAPH_BOUNDARY_COMPLETION_2026-06-01.md`;
- run listed gates.

Forbidden scope:

- any edit to any `.ts` file;
- graph persistence mutation;
- new retrieval routes;
- public-sync, push, or commit.

Risk ceiling: R0 — documentation-only.

## Required First Reads

- `docs/baselines/CVF_GC018_MKG7_T6_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md`
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` — chain produces derived context view
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` — `graph` retrieval method

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_markdown_structural_completeness.py --base 5e55714d --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base 5e55714d --head HEAD --enforce
```

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Workflow chain produces derived context view | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 49–62 | `MemoryRuntimeWorkflowResult` | workflow chain | ACCEPT |
| `graph` retrieval method exists | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | line 9 | `MemoryRetrievalMethod` | retrieval policy | ACCEPT |
| Retrieval result `rawMemoryReleased` field | LITERAL_INVARIANT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | line 48 | `rawMemoryReleased` | `MemoryRetrievalResult` | ACCEPT |
| T1 contract advisory-only boundary | EXISTS | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | Advisory-Only Execution Boundary section | `Advisory-Only` | T1 contract | ACCEPT |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Source authority stays primary | Execution Plan step 2 | boundary doc section | reviewer check | DISPATCHED |
| Derived-view drift detectable | Execution Plan step 2 | drift-detectability statement | reviewer check | DISPATCHED |
| Graph lookup cannot overrule source authority | Execution Plan step 2 | explicit prohibition | reviewer check | DISPATCHED |
| Public/runtime claims require separate proof | Execution Plan step 2 | explicit statement | reviewer check | DISPATCHED |

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously with reading files, writing docs, running gates, fixing
allowed-scope doc-format defects. Ask only for scope expansion, `.ts` edits,
live proof, secrets, push, commit, or destructive actions.

## 6D. Pending Artifact Evidence Finality

Do not commit. Record actual `git status --short`. Do not cite committed-only
or empty range as proof.

## 6G. Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md` | Yes | boundary reference document |
| `docs/reviews/CVF_MKG7_T6_MEMORY_DERIVED_GRAPH_BOUNDARY_COMPLETION_2026-06-01.md` | Yes | pending completion review |

### Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| Any `EXTENSIONS/**/*.ts` | T6 is documentation-only |

### Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| Explicit source-vs-derived boundary | boundary doc | `source authority` | Yes |
| Drift-detectability statement | boundary doc | `drift` | Yes |
| Graph-cannot-overrule statement | boundary doc | `cannot overrule` | Yes |

## 7. Write Ownership

Owned: `CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md`, completion review.
Forbidden: all `.ts` files.

## 8. Execution Plan

1. Capture `baseHead` and git status.
2. Create boundary reference document with these sections:
   - Purpose;
   - Source Authority Definition (what counts as source authority);
   - Derived Views (graph nodes, semantic-region maps, summaries, cache, snapshots — rebuildable from source);
   - Boundary Rules: source authority is primary; derived views are rebuildable; graph lookup cannot overrule source; drift between derived view and source is detectable; public or runtime claims require separate live proof;
   - Evidence Trail (cite workflow chain and retrieval policy as examples of derived-view producers);
   - Claim Boundary.
3. Run markdown-structural and public-export gates.
4. Create pending completion review.
5. Leave all files pending and uncommitted.

## Evidence Requirements

- `python governance/compat/check_markdown_structural_completeness.py --base 5e55714d --head HEAD --enforce` — PASS;
- `python governance/compat/check_public_export_disposition.py --base 5e55714d --head HEAD --enforce` — PASS;
- actual `git status --short`.

## 10. Acceptance Criteria

- [ ] Boundary doc exists with explicit source-vs-derived boundary
- [ ] Drift-detectability explicitly stated
- [ ] Statement that graph lookup cannot overrule source authority
- [ ] Statement that public/runtime claims from derived views require separate proof
- [ ] Markdown-structural gate PASS
- [ ] Public-export gate PASS
- [ ] Both files pending and uncommitted

Fail conditions:

- [ ] Any `.ts` file edited
- [ ] Boundary vague enough to authorize graph-as-source-authority
- [ ] Worker commits or asks about routine gate failures

## 11. Review Gate

Pre-implementation gate must pass before edits. Closure (by orchestrator)
requires reviewer no-blocking objection and markdown-structural + public-export
gates re-verified. A gate failure inside Allowed scope is authorization to
repair and rerun.

## 12. Closure Checklist

N/A: worker must not close or commit T6. Return pending files for orchestrator.

## 13. Return-To-Orchestrator Conditions

Return if: any `.ts` file edit required; boundary document cannot avoid
authorizing graph-as-source-authority within Allowed scope.

## Operator Checkpoint

Operator requested all MKG7 T2–T7 work orders dispatched for worker execution.
T6 is dispatch-ready; documentation-only.

## Worker Dispatch Prompt

```text
You are assigned MKG7-T6 Memory Derived Graph Boundary.

Primary work order:
docs/work_orders/CVF_WO_MKG7_T6_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md

Critical rules:
- documentation-only: do NOT edit any .ts file;
- create docs/reference/CVF_MEMORY_DERIVED_GRAPH_BOUNDARY_2026-06-01.md with
  explicit boundary: source authority is primary, derived views are rebuildable,
  graph lookup CANNOT overrule source authority, drift is detectable, public/
  runtime claims require separate proof;
- run markdown-structural and public-export gates.

Worker Autonomy Rule: repair doc-format gate failures and rerun without asking.
Pending Artifact Rule: do not commit; record actual git status.
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T6 authorizes a documentation-only boundary reference packet. No graph
persistence mutation, new retrieval routes, `.ts` edits, provider calls,
public-sync, or push.
