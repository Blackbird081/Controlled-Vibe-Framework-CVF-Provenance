# CVF Work Order - LPCI1-T1 Product Intake and Architecture

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

dispatchBaseHead: `0dbce418`

executionBaseHead: a155f505

closureBaseHead: a155f505

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Conduct LPCI1-T1 product intake and architecture for the Legal/Policy Corpus
Intelligence chatbot MVP. This tranche produces the architecture document,
corpus intake spec, and T1 GC-018 supplement. It does not implement any code.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| LPCI1 GC-018 | `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` | ACCEPT |
| LPCI1 MVP roadmap | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | ACCEPT |
| CI1-T7 LPCI intake bridge | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | ACCEPT |
| CI2-T4 pilot pack | `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | ACCEPT |
| CI2-T3 enforced index schema | `docs/reference/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL_SCHEMA_2026-06-02.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch; CI2-T5 closed at commit `6324fd76` | no implementation |
| Worker | produce architecture document, corpus intake spec, T1 GC-018 supplement | no runtime code |
| Reviewer | verify architecture-only scope; reject any runtime artifact | reject UI/API/vector/provider work |

## Dependency Gate

Dependency satisfied. CI2-T5 closure committed at `6324fd76`.

Release evidence:

- CI2-T5 closure review: `docs/reviews/CVF_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_COMPLETION_2026-06-02.md` — Status: CLOSED_PASS_BOUNDED at commit `6324fd76`
- CI2-T5 work order: `docs/work_orders/CVF_WO_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_2026-06-02.md` — closureBaseHead: `1ab83302`
- LPCI1 GC-018: `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` — Status: ACTIVE
- LPCI1 MVP roadmap: `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` — Status: ACTIVE

## Roadmap-To-Work-Order Trace Matrix

| LPCI1 roadmap requirement | LPCI1-T1 instruction |
| --- | --- |
| Architecture document | design corpus intake, classification, retrieval, and API/UI surface sketch |
| T1 GC-018 supplement | acknowledge NR-04/NR-05/NR-11 gaps; state hash policy |
| Corpus intake spec | state corpus prerequisites; cite CI2-T4 gaps; define per-file vs proxy hash policy |
| No runtime implementation | documentation and architecture artifacts only |

## Source Verification Block

| Claimed item | Evidence type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| NR-04 gap acknowledgment required | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 169-173 | NR-04 row | Gap Acknowledgment table | ACCEPT |
| NR-05 gap acknowledgment required | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 169-173 | NR-05 row | Gap Acknowledgment table | ACCEPT |
| NR-11 gap acknowledgment required | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 169-173 | NR-11 row | Gap Acknowledgment table | ACCEPT |
| No runtime before T1 gate | EXISTS | `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` | Implementation Gate section | `no-runtime-until-T1` | GC-018 baseline | ACCEPT |

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | CREATE | Worker |
| `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | CREATE | Worker |
| `docs/baselines/CVF_GC018_LPCI1_T1_SUPPLEMENT_2026-06-02.md` | CREATE | Worker |
| `docs/reviews/CVF_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_COMPLETION_2026-06-02.md` | CREATE | Worker |

## Allowed Scope

- create `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md`;
- create `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md`;
- create `docs/baselines/CVF_GC018_LPCI1_T1_SUPPLEMENT_2026-06-02.md`;
- create `docs/reviews/CVF_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_COMPLETION_2026-06-02.md`;
- repair allowed-scope Markdown defects only.

Forbidden scope:

- creating any UI, API route, database schema, embedding pipeline, vector
  store, or provider call;
- public-sync;
- claiming legal advice quality or production readiness;
- implementing any LPCI runtime feature.

## Required First Reads

1. `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md`
2. `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md`
3. `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` (Gap Acknowledgment section)
4. `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` (fieldPopulationReport and knownGaps)
5. `docs/reference/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL_SCHEMA_2026-06-02.md`

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| CI2-T5 closure review exists | `Test-Path docs/reviews/CVF_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_COMPLETION_2026-06-02.md` | true |
| LPCI1 GC-018 exists | `Test-Path docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` | true |
| Pilot pack valid | `python -m json.tool docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | exit 0 |

## Execution Plan

1. Read LPCI1 GC-018 baseline, roadmap, CI1-T7, and CI2-T4 pilot pack gaps.
2. Draft architecture document covering corpus intake, classification,
   retrieval/answer boundary, and API/UI surface sketch.
3. Draft corpus intake spec citing CI2-T4 knownGaps and stating hash policy.
4. Draft T1 GC-018 supplement acknowledging NR-04/NR-05/NR-11 obligations.
5. Create completion review and run governance gates.

## Execution Instructions

1. Architecture document must address:
   - corpus intake: file import, manifest, GC-051 registration path, hash policy (per-file vs manifest proxy);
   - classification: CI2 enforced field schema, NR-11 alias enforcement, legalPolicy domain extensions;
   - retrieval and answer boundary: citation-first, abstention rules, answer-class constraints;
   - API/UI surface sketch: local-first, operator-supplied LLM key, audit receipt schema.
2. Corpus intake spec must explicitly state whether per-file SHA-256 or manifest proxy hash is adopted.
3. T1 GC-018 supplement must include a gap acknowledgment table for NR-04, NR-05, and NR-11 with post-CI2 status.
4. No implementation code may be created. If any runtime artifact is needed to describe the architecture, use
   pseudocode or schema notation, not executable files.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Architecture document exists | covers intake, classification, retrieval, API/UI sketch |
| Corpus intake spec exists | states hash policy; cites CI2-T4 inherited gaps |
| T1 GC-018 supplement exists | gap acknowledgment table for NR-04/NR-05/NR-11 |
| No runtime artifact created | zero UI/API/vector/provider/embedding files |
| Completion review exists | gates documented |

## Evidence Requirements

- Architecture document cites CI1-T7 and CI2-T4 pilot pack.
- Runtime blocked scope is explicit.
- Gap acknowledgment table is present in T1 GC-018 supplement.

## Review Gate

Reviewer must verify T1 creates architecture planning artifacts only and
does not implement any runtime feature.

## Closure Checklist

| Item | Required final state |
| --- | --- |
| Architecture doc | authored |
| Corpus intake spec | authored |
| T1 GC-018 supplement | authored |
| Runtime code | zero files touched |

## Return Conditions

Return to orchestrator after architecture review closes or if an operator
checkpoint is needed (new corpus path, provider call, or public-sync request).

## Operator Checkpoint

Operator authorization is required before:

- any new legal/policy corpus path is ingested beyond the CI2-T4 pilot roots;
- any live provider key or API call is consumed;
- public-sync of any LPCI1 artifact.

Architecture and planning documents do not require a checkpoint.

## Required Gates

```powershell
python governance/compat/check_markdown_structural_completeness.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD
git diff --check
git status --short
```

## Worker Autonomy / No-Question Rule

Worker must draft architecture from CI2 evidence without asking whether to
implement runtime features. Worker must stop for: new corpus path, provider
call, public-sync request, or implementation code.

## Claim Boundary

LPCI1-T1 creates product intake and architecture planning artifacts only.
It does NOT implement LPCI, perform legal retrieval, answer legal questions,
run live proof, or claim production/public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
