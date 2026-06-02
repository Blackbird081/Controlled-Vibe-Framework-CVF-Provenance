# CVF Work Order - CI2-T1 Source Hash Standard

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-02

dispatchBaseHead: `65a0620f`

executionBaseHead: `65a0620f`

closureBaseHead: NOT_EXECUTED_YET

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Author the missing NR-04 per-file source hash standard so future corpus packets
can prove file-level drift resistance before retrieval, chatbot, or product
intake claims.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| CI2 GC-018 | `docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md` | ACCEPT |
| CI2 roadmap | `docs/roadmaps/CVF_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_ROADMAP_2026-06-02.md` | ACCEPT |
| CI1-T6 | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch CI2-T1 and review output | no runtime work |
| Worker | author standard, update template, create completion review | no checker code |
| Reviewer | verify NR-04 standard and gates | reject scope bleed |

## Roadmap-To-Work-Order Trace Matrix

| CI2 roadmap requirement | CI2-T1 instruction |
| --- | --- |
| Close NR-04 written standard | create source hash standard |
| Prepare T2 checker implementation | define exact fields and exception rule |
| Preserve LPCI boundary | no runtime, chatbot, or product implementation |

## Source Verification Block

| Claimed item | Evidence type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| NR-04 requires per-file sourceHash or manifest proxy exception | DOC_ONLY_NEW | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | line 75 and Stub 1 lines 111-119 | `NR-04` | CI1-T6 Decision Table / Checker Spec Stubs | ACCEPT |
| Readiness template already names `sourceHash` as a common facet | EXISTS | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | lines 233-234 | `sourceHash` | Common Facet Schema | ACCEPT |
| LPCI inherits NR-04 as an ingestion-integrity obligation | DOC_ONLY_NEW | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 150-156 and 183 | `NR-04` | Gap Acknowledgment / Governance Gate Requirements | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Boundary |
| --- | --- | --- |
| `sourceHashAlgorithm` | records hash algorithm used for per-file hashes | doc/schema only |
| `manifestHashProxy` | explicit packet-level exception when per-file hashes are unavailable | doc/schema only |
| `manifestProxyException` | human-readable trade-off statement for manifest proxy use | doc/schema only |

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` | CREATE | Worker |
| `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | UPDATE | Worker |
| `docs/reviews/CVF_CI2_T1_SOURCE_HASH_STANDARD_COMPLETION_2026-06-02.md` | CREATE | Worker |

## Allowed Scope

- create `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md`;
- update `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` only to add the NR-04 source-hash rule, manifest proxy exception, and source-hash fields;
- create `docs/reviews/CVF_CI2_T1_SOURCE_HASH_STANDARD_COMPLETION_2026-06-02.md`;
- repair allowed-scope Markdown defects.

Forbidden scope:

- checker implementation;
- `governance/compat/`, hook chains, runtime code, tests, LPCI product files,
  provider calls, new corpus scans, public-sync.

## Required First Reads

1. `docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md`
2. `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md`
3. `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`
4. `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| Source template exists | `Test-Path docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | true |
| CI1-T6 exists | `Test-Path docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | true |

## Execution Plan

1. Read required sources.
2. Author NR-04 source hash standard.
3. Update readiness template with source hash and proxy exception rules.
4. Create completion review and run gates.

## Execution Instructions

1. Author the NR-04 standard with canonical algorithm, field requirements,
   manifest proxy exception, and reviewer verification rule.
2. Update the readiness packet template so future packets require per-row
   `sourceHash` or explicit `manifestHashProxy` plus exception.
3. State that `sourceHash` is a source-file content hash, not a manifest hash,
   path hash, semantic hash, or runtime proof.
4. Create the completion review with gate output and claim boundary.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| NR-04 standard exists | new reference doc with canonical sourceHash rule |
| Template updated | future packets know how to fill `sourceHash` or proxy exception |
| T2 unblocked | standard names checker-ready requirements |
| No code touched | no governance/runtime/test files modified |
| Closure evidence | gates and clean worktree evidence recorded |

## Evidence Requirements

- Source standard cites NR-04 decision and checker stub.
- Template update shows exact fields worker must fill.
- Completion review records `git diff --name-status`, gates, and claim boundary.

## Review Gate

Reviewer must verify that CI2-T1 touches only allowed docs and does not
implement checker/runtime/product code.

## Closure Checklist

| Item | Required final state |
| --- | --- |
| NR-04 standard | authored |
| Template update | authored |
| Completion review | authored |
| Gates | PASS |

## Return Conditions

Return to orchestrator when all acceptance criteria are satisfied. If a cited
source fact is missing, mark the work order blocked with source evidence and do
not begin implementation. Allowed-scope gate failures must be resolved before
return.

## Operator Checkpoint

No additional operator checkpoint is required for CI2-T1. Operator input is
required only for forbidden-scope expansion.

## Worker Autonomy / No-Question Rule

Worker must produce passing allowed-scope Markdown and gate results directly.
Worker must stop only for forbidden-scope requests, runtime implementation
requests, new corpus scan requests, or missing source facts.

## Required Gates

```powershell
python governance/compat/check_markdown_structural_completeness.py --base 65a0620f --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 65a0620f --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 65a0620f --head HEAD
git diff --check
git status --short
```

## Claim Boundary

CI2-T1 is documentation-only. It does not implement a checker, mutate runtime,
scan a corpus, authorize LPCI implementation, or claim production/public
readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
