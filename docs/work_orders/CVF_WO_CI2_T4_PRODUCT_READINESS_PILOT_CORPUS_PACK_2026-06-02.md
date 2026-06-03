# CVF Work Order - CI2-T4 Product Readiness Pilot Corpus Pack

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-02

dispatchBaseHead: `e983bac4`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: NOT_EXECUTED_YET

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Build a bounded pilot corpus pack that proves the CI2 enforced index fields can
be populated and reviewed before LPCI product roadmap authoring.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| CI2 GC-018 | `docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md` | ACCEPT |
| CI2 roadmap | `docs/roadmaps/CVF_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_ROADMAP_2026-06-02.md` | ACCEPT |
| CI2-T3 model | T3 enforced index model after closure | REQUIRED |
| CI1-T7 | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch after T3 closure | no new corpus unless supplied |
| Worker | build pilot pack from existing CI1 evidence or supplied corpus | no invented source data |
| Reviewer | verify evidence and gap honesty | reject runtime/product claims |

## Dependency Gate

CI2-T4 may begin because CI2-T3 closed with a valid enforced index model and
schema document at commit `e983bac4`.

Prerequisite evidence:

- `docs/reviews/CVF_CI2_T3_ENFORCED_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md`
- `docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json`
- `docs/reference/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL_SCHEMA_2026-06-02.md`

## Roadmap-To-Work-Order Trace Matrix

| CI2 roadmap requirement | CI2-T4 instruction |
| --- | --- |
| Prove product-readiness packet shape | create pilot pack |
| Avoid blind rescan | use existing CI1 packets unless operator supplies a bounded corpus |
| Feed LPCI roadmap | produce a product intake readiness summary |

## Source Verification Block

| Claimed item | Evidence type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| CI1-T7 identifies primary inputs for LPCI | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 69-80 | `Primary Inputs` | Corpus Input Contract | ACCEPT |
| New corpora require GC-051 registration | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 92-99 and 177-182 | `GC-051` | Input Consumption Rules / Governance Gate Requirements | ACCEPT |
| CI1-T5 sampling verdict has gaps, not full semantic proof | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 124-133 | `T5` | Claim Boundary Inheritance | ACCEPT |

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | CREATE | Worker |
| `docs/reference/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_2026-06-02.md` | CREATE | Worker |
| `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | UPDATE IF NEW CORPUS SUPPLIED | Worker |
| `docs/reviews/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_COMPLETION_2026-06-02.md` | CREATE | Worker |

## Allowed Scope

- create `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json`;
- create `docs/reference/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_2026-06-02.md`;
- create `docs/reviews/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_COMPLETION_2026-06-02.md`;
- update `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only if the worker is explicitly given a new bounded corpus by the operator;
- repair allowed-scope JSON/Markdown defects.

Forbidden scope:

- scanning a new corpus without explicit operator-supplied corpus path;
- inventing legal/policy source documents;
- implementing LPCI runtime or frontend;
- provider calls/live proof;
- public-sync.

## Required First Reads

1. CI2-T3 enforced index model and schema.
2. `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`
3. `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`
4. Existing CI1 T2/T3 readiness packets.

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| T3 model exists | `Test-Path docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json` | true |
| T3 model valid | `python -m json.tool docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json` | exit 0 |

## Execution Plan

1. Read T3 model and CI1 evidence.
2. Choose existing CI1 pilot input unless dispatch supplies a corpus path.
3. Create pilot JSON and explanatory reference doc.
4. Run JSON and governance gates.

## Execution Instructions

1. If no operator-provided corpus path is included in the dispatch message, use
   the existing CI1 T2/T3 packets as the pilot input and label the pack
   `GOVERNANCE_PILOT_NO_LEGAL_CORPUS`.
2. Populate the enforced CI2 fields from available CI1 data and declare any
   field that remains unpopulated with a bounded reason.
3. Include product-readiness sections for ingestion, search/filter, answer
   boundary, evidence trace, and known gaps.
4. Record whether the pack is sufficient for LPCI roadmap authoring. It does
   not need to be sufficient for runtime implementation.
5. Create a completion review with gates and gap disposition.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Pilot JSON valid | `python -m json.tool` PASS |
| Pilot reference doc exists | explains field population and gaps |
| No invented corpus | legal/policy data absent unless operator supplied |
| T5 gap inheritance | pack preserves claim boundaries |
| T5 input readiness | T5 can cite the pilot pack for roadmap proposal |

## Evidence Requirements

- Pilot pack names every input artifact.
- Unfilled enforced fields have explicit gap reasons.
- Completion review records whether corpus is governance-pilot or operator
  supplied.

## Review Gate

Reviewer must verify the pilot pack does not invent corpus content and that it
is sufficient for roadmap authoring only.

## Closure Checklist

| Item | Required final state |
| --- | --- |
| Pilot JSON | valid |
| Pilot reference | authored |
| Input evidence | cited |
| Claim boundary | explicit |

## Return Conditions

Return to orchestrator after pilot pack and gates complete or if a supplied
corpus lacks registration authority.

## Operator Checkpoint

No operator checkpoint is required when using existing CI1 evidence. Operator
authorization is required for any new corpus path.

## Required Gates

```powershell
python -m json.tool docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json
python governance/compat/check_corpus_scan_registry.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD
git diff --check
git status --short
```

## Worker Autonomy / No-Question Rule

Worker must use the existing CI1 evidence pack when no new corpus is supplied,
instead of asking whether to invent or search for legal data. Worker must stop
for new corpus ambiguity, runtime implementation, live calls, or public-sync.

## Claim Boundary

CI2-T4 proves product-readiness packet shape only. It does not prove legal
answer correctness, runtime retrieval, chatbot behavior, or production/public
readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
