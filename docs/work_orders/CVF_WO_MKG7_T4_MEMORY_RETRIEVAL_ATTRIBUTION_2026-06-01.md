# CVF Work Order - MKG7-T4 Memory Retrieval Attribution

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-01

## Purpose

Add an attribution layer over the existing retrieval result
(`MemoryRetrievalResult` @ `memory-retrieval-policy.ts:40`) that answers:
authority source, freshness, rank reason, exclusion reason, staleness status,
and raw-content boundary — without releasing raw candidate `content`. T4 is
additive; `memory-retrieval-policy.ts` must not be modified.

Success: new attribution helper exists, attribution fields populated from
existing result, raw `content` absent, `rawMemoryReleased=false` preserved,
LPF TypeScript check PASS, file-size guard PASS, pending and uncommitted.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 dispatch MKG7 T2–T7 for worker execution | ACCEPT |
| MKG7-T4 GC-018 | `docs/baselines/CVF_GC018_MKG7_T4_MEMORY_RETRIEVAL_ATTRIBUTION_2026-06-01.md` | ACCEPT |
| MKG7 roadmap | `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | ACCEPT |
| T1 contract | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch and review pending output | no silent scope expansion |
| Worker | implement attribution helper + tests | no retrieval-engine edits, no commit |
| Reviewer | verify raw `content` absent, attribution fields present, existing retrieval unmodified | reject if `content` leaks |

## Scope

Allowed scope:

- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-attribution.ts`;
- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-attribution.test.ts`;
- optionally extend `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts` export;
- create `docs/reviews/CVF_MKG7_T4_MEMORY_RETRIEVAL_ATTRIBUTION_COMPLETION_2026-06-01.md`.

Forbidden scope:

- any edit to `memory-retrieval-policy.ts`;
- any edit to `index.ts`;
- raw candidate `content` in output;
- route changes, provider calls, live proof, persistence mutation;
- public-sync, push, or commit.

Risk ceiling: R1 — additive attribution helper.

## Required First Reads

- `docs/baselines/CVF_GC018_MKG7_T4_MEMORY_RETRIEVAL_ATTRIBUTION_2026-06-01.md`
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` — existing result shape

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5e55714d --head HEAD
python governance/compat/check_governed_file_size.py --enforce
```

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `MemoryRetrievalResult` shape | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 40–48 | `MemoryRetrievalResult` | retrieval policy | ACCEPT |
| `selected` array (attribution source) | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | line 45 | `selected` | `MemoryRetrievalResult` | ACCEPT |
| `excluded` array (exclusion reasons) | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | line 46 | `excluded` | `MemoryRetrievalResult` | ACCEPT |
| `rawMemoryReleased` on result | LITERAL_INVARIANT | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | line 48 | `rawMemoryReleased` | `MemoryRetrievalResult` | ACCEPT |
| `content` field on candidate (must be stripped) | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | line 19 | `content` | `MemoryRetrievalCandidate` | ACCEPT |
| Existing exclusion reasons | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 167–180 | `out_of_scope` | retrieval evaluator | ACCEPT |
| `auditTrust` field (rank basis) | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | line 22 | `auditTrust` | `MemoryRetrievalCandidate` | ACCEPT |
| `createdAt` field (freshness basis) | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | line 21 | `createdAt` | `MemoryRetrievalCandidate` | ACCEPT |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Source/freshness/rank/exclusion attribution | Execution Plan step 2 | attribution fields in output | focused test | DISPATCHED |
| No raw `content` release | Forbidden scope + Proof Manifest | `content` absent from output | sentinel test | DISPATCHED |
| `rawMemoryReleased=false` preserved | Source Verification Block | attribution output field | focused test | DISPATCHED |
| Deterministic and testable without provider calls | Execution Plan | pure function | LPF `npm run check` | DISPATCHED |

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously. Ask only for scope expansion, forbidden-path edits, live
proof, secrets, push, commit, or destructive actions.

## 6D. Pending Artifact Evidence Finality

Do not commit. Record actual `git status --short`. Do not cite committed-only
or empty range as proof for pending files.

## 6G. Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-attribution.ts` | Yes | attribution helper |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-attribution.test.ts` | Yes | focused tests |
| `docs/reviews/CVF_MKG7_T4_MEMORY_RETRIEVAL_ATTRIBUTION_COMPLETION_2026-06-01.md` | Yes | pending completion review |

### Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | existing retrieval engine — must not be modified |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` | must not expand root barrel |

### Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| Raw content absent from attribution output | test file | `content` | Yes (assert absent) |
| `rawMemoryReleased=false` in attribution | test file | `rawMemoryReleased` | Yes |
| Attribution fields populated | test file | `rankReason` | Yes |

## 7. Write Ownership

Owned: `memory-retrieval-attribution.ts`, test file, optionally `memory-runtime.ts` export, completion review.
Forbidden: `memory-retrieval-policy.ts`, `index.ts`.

## 8. Execution Plan

1. Capture `baseHead` and git status. Run pre-flight gate.
2. Create `memory-retrieval-attribution.ts` with:
   - `MemoryRetrievalAttribution` type: `{ sourceId, scope, freshness, rankReason, exclusionReason?, isStale, rawContentBoundary, rawMemoryReleased: false }`;
   - `buildRetrievalAttribution(result: MemoryRetrievalResult): MemoryRetrievalAttribution[]` — maps selected/excluded arrays from existing result; strips `content`; derives `freshness` from `createdAt`, `rankReason` from `auditTrust`, `exclusionReason` from excluded array.
3. Create focused tests: attribution fields populated, `content` absent, `rawMemoryReleased=false`, deterministic output.
4. Run `npm run check` from LPF. Run file-size guard.
5. Create pending completion review.
6. Leave all files pending and uncommitted.

## Evidence Requirements

- `npm run check` from LPF — PASS;
- file-size guard PASS;
- `git diff --name-status` — no edits to forbidden paths;
- actual `git status --short`.

## 10. Acceptance Criteria

- [ ] `memory-retrieval-attribution.ts` exists with attribution type and builder
- [ ] Attribution output contains `sourceId`, `freshness`, `rankReason`, `exclusionReason`, `rawMemoryReleased:false`
- [ ] Raw candidate `content` absent from attribution output
- [ ] `memory-retrieval-policy.ts` unmodified
- [ ] LPF `npm run check` PASS
- [ ] File-size guard PASS

Fail conditions:

- [ ] Raw candidate `content` present in attribution output
- [ ] Any edit to `memory-retrieval-policy.ts`
- [ ] Worker commits or asks whether to fix an allowed-scope failure

## 11. Review Gate

Pre-implementation autorun gate must pass before edits. Closure (by
orchestrator) requires reviewer no-blocking objection and `pre-closure` gate.
A gate failure inside Allowed scope is authorization to repair and rerun.

## 12. Closure Checklist

N/A: worker must not close or commit T4. Return pending files for orchestrator.

## 13. Return-To-Orchestrator Conditions

Return if: pre-flight fails outside the work order's scope; a forbidden-path
edit would be required; raw candidate `content` cannot be excluded from
attribution output within the work order's scope.

## Operator Checkpoint

This tranche was authorized and dispatched by the operator on 2026-06-01 as
part of the MKG7 full-wave dispatch. T4 is ready to execute; T1 contract
is the primary authority source.

## Worker Dispatch Prompt

```text
You are assigned MKG7-T4 Memory Retrieval Attribution.

Primary work order:
docs/work_orders/CVF_WO_MKG7_T4_MEMORY_RETRIEVAL_ATTRIBUTION_2026-06-01.md

Critical rules:
- create memory-retrieval-attribution.ts that wraps existing MemoryRetrievalResult;
- output attribution fields: sourceId, freshness (from createdAt), rankReason
  (from auditTrust), exclusionReason (from excluded array), rawMemoryReleased:false;
- do NOT include raw candidate content field in output — strip it;
- do NOT modify memory-retrieval-policy.ts;
- run LPF npm run check and file-size guard.

Worker Autonomy Rule: repair allowed-scope failures and rerun without asking.
Pending Artifact Rule: do not commit; record actual git status.
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T4 authorizes an additive attribution helper only. No retrieval-engine edits,
raw content release, route changes, provider calls, persistence mutation,
public-sync, or push.
