# CVF Work Order - CI2-T3 Enforced Cross-Corpus Index Model

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-02

dispatchBaseHead: `73079521`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: NOT_EXECUTED_YET

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Create an enforced cross-corpus index schema/model that consumes CI2-T1/T2
controls and becomes the stable machine-readable input for product readiness
packets and future LPCI ingestion design.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| CI2 GC-018 | `docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md` | ACCEPT |
| CI2 roadmap | `docs/roadmaps/CVF_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_ROADMAP_2026-06-02.md` | ACCEPT |
| CI2-T2 checker closure | `docs/reviews/CVF_CI2_T2_PACKET_NORMALIZATION_CHECKERS_COMPLETION_2026-06-02.md` | ACCEPT |
| CI1-T7 | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch after T2 closure | no runtime work |
| Worker | create JSON model/schema docs | no checker/runtime changes |
| Reviewer | verify model validity and mapping | reject old-model overwrite |

## Dependency Gate

CI2-T3 must not begin until CI2-T2 closes with checker tests and hook/autorun
integration evidence.

## Roadmap-To-Work-Order Trace Matrix

| CI2 roadmap requirement | CI2-T3 instruction |
| --- | --- |
| Normalize enforced index output | create schema/model v2 |
| Feed product-readiness pilot | define fields T4 must populate |
| Prevent prose-only scan results | require machine-readable JSON model |

## Source Verification Block

| Claimed item | Evidence type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| CI1-T4 already created a cross-corpus index model | EXISTS | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | lines 92 and 113 | `CI1-T4` | CI1 tranche plan | ACCEPT |
| LPCI-T1 must consume T4 model fields | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 69-80 | `CVF_CROSS_CORPUS_INDEX_MODEL.json` | Corpus Input Contract | ACCEPT |
| LPCI inherits T4/T5/T6 boundaries | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 106-143 | `Claim Boundary Inheritance` | CI1-T7 intake bridge | ACCEPT |
| Required common fields include normalizedPath and sourceHash | EXISTS | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | Common Facet Schema | `normalizedPath`, `sourceHash` | readiness packet template | ACCEPT |
| Readiness packet identity rule requires docs/audits path, READINESS_PACKET filename marker, and docType audit for new packets | EXISTS | `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md` | Packet Identity Rule | `docType` | readiness packet template | ACCEPT |
| CI2-T2 implemented packet normalization checkers | EXISTS | `docs/reviews/CVF_CI2_T2_PACKET_NORMALIZATION_CHECKERS_COMPLETION_2026-06-02.md` | Methodology and Findings | `check_corpus_packet_source_hash.py`, `check_corpus_packet_normalized_path.py`, `check_corpus_packet_disposition_canonical.py` | CI2-T2 completion review | ACCEPT |

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json` | CREATE | Worker |
| `docs/reference/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL_SCHEMA_2026-06-02.md` | CREATE | Worker |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | UPDATE IF REQUIRED | Worker |
| `docs/reviews/CVF_CI2_T3_ENFORCED_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md` | CREATE | Worker |

## Allowed Scope

- create `docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json`;
- create `docs/reference/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL_SCHEMA_2026-06-02.md`;
- update `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` only to add a CI2 connection from packet checkers to enforced index model, if registry structure supports it;
- create `docs/reviews/CVF_CI2_T3_ENFORCED_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md`;
- repair allowed-scope JSON/Markdown defects.

Forbidden scope:

- modifying the CI1 T4 model in place unless a compatibility note is required;
- checker implementation;
- LPCI implementation;
- new corpus scan;
- public-sync.

## Required First Reads

1. CI2-T2 completion review:
   `docs/reviews/CVF_CI2_T2_PACKET_NORMALIZATION_CHECKERS_COMPLETION_2026-06-02.md`
2. `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
3. `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`
4. `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`
5. `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| Capture fresh execution base | `git rev-parse --short HEAD` | record as `executionBaseHead`; do not reuse dispatchBaseHead |
| T2 completion exists | `Test-Path docs/reviews/CVF_CI2_T2_PACKET_NORMALIZATION_CHECKERS_COMPLETION_2026-06-02.md` | true |
| CI1 model valid | `python -m json.tool docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | exit 0 |

## Execution Plan

1. Read T2 outputs and CI1 index model.
2. Create CI2 enforced JSON model.
3. Create schema/reference explanation.
4. Run JSON and governance gates.

## Execution Instructions

1. Create a JSON model that includes required facets for `sourcePath`,
   `normalizedPath`, `sourceHash`, `sourceHashAlgorithm`, `disposition`,
   `rawDisposition`, `dispositionAlias`, `answerClass`, `evidencePointer`,
   and domain extensions for legal/policy corpora.
2. Record which fields are structural-required, optional, derived, or
   domain-extension.
3. Bind each enforced field to its originating standard/checker.
4. Add a schema reference document explaining how T4/CI1 maps into CI2 model
   without changing historical CI1 artifacts.
5. Record product-readiness boundary: model is not a runtime index or vector
   database.
6. Do not create a filled readiness packet in CI2-T3. If a future packet is
   needed, it must follow the template identity rule: `docs/audits/`,
   `READINESS_PACKET` filename marker, and `docType: audit`.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| JSON model valid | `python -m json.tool` PASS |
| Schema doc exists | field glossary and enforcement source map |
| T4 compatibility | maps CI1 model to CI2 without overwriting history |
| T4 input for T4 pilot | T4 work order can consume model directly |
| Claim boundary | no runtime/vector/product claim |

## Evidence Requirements

- JSON validation output.
- Field-to-standard/checker map.
- Compatibility note explaining that CI1 historical model is not overwritten.

## Review Gate

Reviewer must verify the CI2 model is additive, machine-readable, and does not
claim runtime retrieval behavior.

## Closure Checklist

| Item | Required final state |
| --- | --- |
| Enforced JSON model | valid |
| Schema reference | authored |
| T2 mapping | cited |
| Runtime boundary | explicit |

## Return Conditions

Return to orchestrator after model/schema/gates complete or if T2 closure is
missing.

## Operator Checkpoint

No additional operator checkpoint is required for schema/model authoring.

## Required Gates

```powershell
python -m json.tool docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json
python governance/compat/check_system_loop_interlock.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
# Reviewer/committer only, after approved commit:
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <closureBaseHead> --head HEAD
git diff --check
git status --short
```

## Worker Autonomy / No-Question Rule

Worker must fix JSON/schema/Markdown defects inside allowed scope. Worker must
stop for runtime, vector DB, LPCI UI/API, new scan, or public-sync requests.
Worker must not ask whether to fix allowed-scope JSON/schema/Markdown/gate
defects; repair them and rerun the gate. Worker must not commit or push.

## Claim Boundary

CI2-T3 produces an enforced index model artifact only. It does not build or
populate a runtime retrieval index and does not prove query behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
