# CVF Corpus Intelligence Classification Standard

Memory class: FULL_RECORD

Status: canonical corpus intelligence classification standard

docType: reference

Date: 2026-06-01

## Purpose

Define the discipline for turning an arbitrary document corpus into classified
knowledge that a chatbot, LLM assistant, retrieval app, or internal advisory
surface may use without collapsing source evidence into vague prose.

This standard sits after GC-047 corpus completeness and GC-048 knowledge-map
reconciliation. GC-047 proves what files exist and were processed. GC-048 proves
how corpus assets map into knowledge regions. GC-050 requires each classified
knowledge signal to carry source path, processing depth, owner surface,
disposition, evidence, and answer boundary.

Search/filter readiness is broader than classification and is defined in
`docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`.
Use that standard whenever a corpus must become searchable, filterable, or
queryable across projects, including but not limited to legal/policy chatbot
work.

## Scope / Applies To

Apply this standard whenever an agent classifies a document set for downstream
question answering, retrieval, legal/policy lookup, internal notice lookup,
company decision search, operational SOP search, or domain-specific chatbot use.

It applies to:

- law, decree, circular, regulation, contract, policy, SOP, notice, decision,
  guideline, and internal company announcement corpora;
- arbitrary folder scans where output is intended to become queryable
  knowledge;
- corpus-derived ledgers that assign owner surfaces, answer classes, or
  actionability.

## Three-Layer Model

Layer 1 is this standard. It defines schema, vocabulary, pipeline, and claim
boundary.

Layer 2 is the structural checker
`governance/compat/check_corpus_intelligence_classification.py`. It checks
classification discipline only: required sections, ledger columns, accepted
evidence pointers, legal/policy domain fields, and response-boundary answer
classes.

Layer 3 is review or adversarial sampling. Semantic correctness must be checked
by source review, random sampling, or multi-agent adversarial review. The
machine checker does not prove the agent understood the corpus correctly.

## Vocabulary

Processing statuses:

- `READ_DEEP`
- `READ_SHALLOW`
- `SKIPPED_WITH_REASON`
- `DEFERRED`
- `BLOCKED_UNREADABLE`

Knowledge regions:

- `LEGAL_POLICY`
- `INTERNAL_DECISION`
- `PROCEDURE`
- `TECHNICAL`
- `GOVERNANCE`
- `RUNTIME`
- `PRODUCT`
- `REFERENCE`
- `OTHER`

Owner surfaces:

- `LEGAL_ADVISORY`
- `POLICY_ADVISORY`
- `MEMORY_PLANE`
- `KNOWLEDGE_GRAPH`
- `RETRIEVAL_INDEX`
- `WORKFLOW`
- `RUNTIME_ROUTE`
- `PUBLIC_DOCS`
- `PRIVATE_PROVENANCE`
- `OTHER`

Dispositions:

- `ACCEPT`
- `ACCEPT_SUMMARY_ONLY`
- `DEFER`
- `REJECT`
- `BLOCKED_SOURCE_NOT_FOUND`
- `BLOCKED_UNREADABLE`

Answer classes:

- `DIRECT_CITED_ANSWER`
- `SUMMARY_WITH_SOURCE`
- `PROCEDURAL_GUIDANCE`
- `ESCALATE_OR_ABSTAIN`

## Pipeline

1. Establish corpus boundary with GC-047.
2. Reconcile source authority and derived views with GC-048.
3. Build or cite CVF corpus search/filter readiness when the work claims
   retrieval, chatbot, project-intelligence, legacy-rescan, or "not found"
   behavior.
4. Classify every accepted or deferred source signal into a ledger row.
5. Assign processing depth and evidence pointer.
6. Assign knowledge region and owner surface.
7. Assign disposition and answer class.
8. Add legal/policy domain fields when the corpus can affect legal, policy,
   compliance, employment, procurement, finance, or regulatory answers.
9. Run structural checker.
10. Run adversarial sampling before semantic correctness is claimed.

## Required Evidence Block

```text
## Corpus Intelligence Classification

- Classification task class: LEGAL_POLICY_QA | INTERNAL_DECISION_QA |
  COMPANY_NOTICE_QA | TECHNICAL_QA | GOVERNANCE_QA | MIXED_CORPUS | OTHER
- Source corpus evidence: <GC-047 manifest/report path or N/A with reason>
- Knowledge map evidence: <GC-048 reconciliation path or N/A with reason>
- Classification ledger: <inline table or artifact path>
- Legal/policy corpus: YES | NO
- Domain fields: <jurisdiction, authorityLevel, effectiveDate, sourceAuthority,
  answerBoundary or N/A with reason>
- Response Boundary: DIRECT_CITED_ANSWER, SUMMARY_WITH_SOURCE,
  PROCEDURAL_GUIDANCE, ESCALATE_OR_ABSTAIN
- Adversarial sampling plan: <5-10 random/source-risk samples or N/A with reason>
- Classification verdict: CLASSIFIED_STRUCTURAL_PASS |
  CLASSIFIED_WITH_DECLARED_GAPS | PARTIAL | BLOCKED

### Corpus Intelligence Classification Ledger

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | evidencePointer | answerClass | domainFields |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <path> | READ_DEEP | LEGAL_POLICY | LEGAL_ADVISORY | ACCEPT | <source section/line/hash> | DIRECT_CITED_ANSWER | jurisdiction=...; authorityLevel=...; effectiveDate=...; sourceAuthority=... |
```

## Legal / Policy Domain Fields

If `Legal/policy corpus: YES`, accepted or summary-only rows must include
domain fields sufficient to stop the assistant from inventing authority:

- `jurisdiction`
- `authorityLevel`
- `effectiveDate`
- `sourceAuthority`
- `answerBoundary`

When these fields are unknown, the disposition must remain `DEFER` or
`BLOCKED_*`, or the answer class must be `ESCALATE_OR_ABSTAIN`.

## READ_SHALLOW Boundary

`READ_SHALLOW` can support triage, routing, or summary-only classification. It
must not support a direct runtime, legal, policy, compliance, or operational
answer claim. Any row classified from shallow reading must use
`SUMMARY_WITH_SOURCE`, `PROCEDURAL_GUIDANCE`, or `ESCALATE_OR_ABSTAIN`, not
`DIRECT_CITED_ANSWER`.

## Enforcement / Verification

```powershell
python governance/compat/check_corpus_intelligence_classification.py --base <baseHead> --head HEAD --enforce
```

Machine checks validate classification structure. They do not prove semantic
correctness, legal correctness, runtime correctness, or retrieval quality.

## Relationship To GC-047 And GC-048

GC-047 is corpus evidence discipline.

GC-048 is corpus-to-knowledge-map reconciliation.

GC-050 is corpus intelligence classification discipline.

## Claim Boundary

This standard makes corpus classification explicit and reviewable. It does not
provide legal advice, replace professional review, certify semantic
correctness, or authorize autonomous runtime behavior.
