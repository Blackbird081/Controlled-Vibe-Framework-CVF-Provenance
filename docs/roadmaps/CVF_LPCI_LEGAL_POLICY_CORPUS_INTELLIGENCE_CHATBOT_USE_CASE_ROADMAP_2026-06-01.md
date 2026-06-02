# CVF LPCI Legal Policy Corpus Intelligence Chatbot Product Roadmap

Memory class: FULL_RECORD

Status: PROPOSED

docType: roadmap

Date: 2026-06-01

## Purpose

Define the product direction for a real governed chatbot or retrieval app for
laws, decrees, circulars, internal company policies, notices, decisions, SOPs,
and comparable authority documents.

The goal is not to let an LLM improvise answers from a folder. The goal is to
turn a bounded corpus into classified, searchable, citeable knowledge first,
then let a model help explain, summarize, route, or abstain inside explicit
answer boundaries.

This is a product roadmap, not just a note. It preserves a real application
target for CVF after Memory/MKE/KGR stabilization. It is still not
implementation authorization, not a legal product claim, and not a
public-readiness claim.

## Authorization / Decision

Authority:

- operator direction on 2026-06-02 to preserve the legal/policy chatbot use case
  as a real product roadmap after Memory/MKE/KGR stabilization;
- active GC-047, GC-048, GC-049, and GC-050 guard chain;
- `docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`;
- `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`.

Decision: record LPCI as a future CVF product roadmap and make it a consumer of
the broader CVF corpus search/filter readiness standard, not the owner of that
generic capability.

This roadmap does not authorize runtime implementation. Any LPCI tranche must
open a fresh GC-018/work order with source verification and scoped acceptance
criteria.

## Current Dependency Chain

LPCI depends on the Memory and Knowledge work becoming stable enough that corpus
knowledge can be traced, searched, and bounded:

| Dependency | Role For LPCI | Status |
| --- | --- | --- |
| GC-047 Corpus Completeness | prove the source corpus boundary and every processed/unprocessed file | ACTIVE |
| GC-048 Knowledge Map Reconciliation | map source authority into knowledge regions without losing rebuildability | ACTIVE |
| GC-049 Core Guard Self-Protection | prevent agents from modifying guard/core surfaces outside explicit scope | ACTIVE |
| GC-050 Corpus Intelligence Classification | require ledger/evidence/disposition/answer-boundary discipline before chatbot or retrieval claims | ACTIVE |
| Corpus Search/Filter Readiness | provide generic CVF search/filter evidence before retrieval, chatbot, legacy scan, or project-intelligence claims | ACTIVE STANDARD |
| Memory Plane | retain bounded advisory/readout context without raw reinjection | CLOSED_PASS_BOUNDED |
| MKE | enforce live memory governance behavior before stronger claims | CLOSED_PASS_BOUNDED |
| KGR | retrieve knowledge graph signals with cited source boundaries | CLOSED_PASS_BOUNDED |
| CI1-T4 Cross-Corpus Index Model | normalize corpus facets into a typed downstream input | CLOSED_PASS_BOUNDED |
| CI1-T5 Classification Sampling | sample accepted/deferred/rejected/zero-result rows on the T4 model | READY_FOR_GC018 |
| CI1-T6 Checker Decision | decide whether sampling findings require a structural checker | HOLD_UNTIL_T5_CLOSED |
| CI1-T7 LPCI Intake Bridge | map the CI1 chain into LPCI-T1 product intake | HOLD_UNTIL_T6_DECIDED |

## Scope / Target / Owner Boundary

Target user:

- a user or developer who wants to bring a local corpus of laws, decrees,
  circulars, internal company policies, notices, decisions, or SOPs into a
  governed retrieval/chatbot workflow.

Owner boundary:

- CVF owns the governance, corpus discipline, retrieval boundary, citation
  receipts, and answer-class control chain;
- the user or organization owns the source corpus, legal/professional judgment,
  currentness review, and decision authority;
- an LLM provider may assist with explanation/summarization only inside the
  retrieved evidence and answer boundary.

Scope boundary:

- in scope: local/private corpus intake, manifest, classification, faceted
  search/filter, citation-first retrieval, optional API-key-backed explanation,
  and adversarial sampling;
- out of scope: legal advice, production compliance certification, public SaaS,
  multi-tenant upload, autonomous legal decisioning, and uncited direct answers.

## Product Sketch

The LPCI app should support:

- import or sync of a local legal/policy corpus;
- manifest-backed source inventory;
- document normalization and chunking with stable source IDs;
- classification into domain-specific fields;
- faceted search and filtered retrieval;
- answer generation with citations, freshness warnings, and abstention;
- optional LLM API key for explanation and summarization;
- secret-safe audit receipts for query, filters, source paths, answer class, and
  refusal/abstention reason.

The first version should be local/private by default. Public SaaS, multi-tenant
hosting, production legal advice, and automated legal decisioning remain out of
scope until separate security/legal/product reviews exist.

## CVF Corpus Search / Filter Readiness Dependency

Search/filter readiness is not owned by LPCI. It is a CVF-wide capability
defined in:

`docs/reference/CVF_CORPUS_SEARCH_FILTER_READINESS_STANDARD_2026-06-02.md`

That standard applies to legacy rescans, project folders, public docs, internal
company corpora, source-code documentation, knowledge bases, and product
corpora. LPCI is one downstream product that consumes it.

Before CVF scans legacy again, and before LPCI answers user questions, the
generic search/filter layer must make blind spots visible before a worker
writes a polished report.

| Layer | Needed improvement | Why it matters |
| --- | --- | --- |
| Corpus discovery index | record root, file path, normalized path, hash, extension, size, ignored/git-tracked state, discoveredAt, and unreadable reason | catches hidden or git-ignored folders before report review |
| Family and topic facets | assign familyId, source family, topic hints, authority/source type, and candidate owner surface | prevents folder-level summaries from hiding high-value subtopics |
| Processing ledger | distinguish read-deep, read-shallow, skipped, deferred, blocked, unsupported, duplicate, and stale snapshot | makes unfinished work explicit instead of invisible |
| Negative search evidence | record searched terms, zero-result terms, excluded folders, and why no match was accepted | avoids "not found" claims without query proof |
| Derived view trace | connect manifest rows to knowledge-map rows, classification rows, retrieval chunks, and answer receipts | lets reviewers trace a chatbot answer back to disk |
| Faceted retrieval schema | support jurisdiction, authority level, issuing body, document type, effective date, topic, audience, sensitivity, answer class, disposition, and freshness | legal/policy answers need filters before ranking |
| Conflict/freshness model | represent amended, superseded, repealed, draft, obsolete, effective, and unknown status | prevents old documents from looking authoritative |
| Query receipt | log query text, normalized query, filters applied, candidate set, excluded set, rank reasons, citations, and answer boundary | makes chatbot behavior auditable |
| Adversarial sampling | sample accepted, deferred, rejected, and zero-result rows | catches semantic and coverage errors that structural guards cannot |

## LPCI Search / Filter Domain Extension

LPCI should extend the generic CVF search/filter schema with legal/policy
fields. These fields are product-specific and must not narrow the generic CVF
standard.

| Field | Purpose |
| --- | --- |
| `documentType` | law, decree, circular, policy, notice, decision, SOP, contract, other |
| `jurisdiction` | country/state/company/org scope where applicable |
| `authorityLevel` | hierarchy or internal authority rank |
| `issuingBody` | ministry, department, company function, owner team |
| `effectiveDate` | date the rule starts applying, when known |
| `status` | effective, draft, amended, superseded, repealed, obsolete, unknown |
| `topicTags` | controlled tags from classification or reviewer |
| `knowledgeRegion` | GC-050 region such as legal policy, internal decision, procedure |
| `ownerSurface` | legal advisory, policy advisory, retrieval index, memory plane, graph |
| `processingStatus` | read-deep, read-shallow, deferred, blocked, skipped |
| `disposition` | accept, summary-only, defer, reject, blocked |
| `answerClass` | direct cited answer, summary, procedure, abstain |
| `evidencePointer` | section, line, paragraph, article, hash, or receipt |
| `sensitivity` | public, internal, confidential, restricted, unknown |
| `freshnessCheckedAt` | last check date for legal/policy currentness |

## Tranche Plan

| Tranche | Goal | Primary outputs | Status |
| --- | --- | --- | --- |
| LPCI-T0 | Hold until Memory/MKE/KGR stabilization | readiness decision after current Memory lane | HOLD |
| LPCI-T1 | Corpus Intake Prototype | local import manifest, hash inventory, unreadable/unsupported ledger | PROPOSED |
| LPCI-T2 | Domain Classification | legal/policy/internal decision classification ledger aligned with GC-050 | PROPOSED |
| LPCI-T3 | Search And Filter Index | faceted index schema, query filter contract, negative search evidence format | PROPOSED |
| LPCI-T4 | Retrieval Boundary | citation-first retrieval receipt, freshness/conflict warning, abstention rules | PROPOSED |
| LPCI-T5 | Chatbot Use Case Prototype | local UI/API with operator-provided LLM API key, citations, answer class, audit receipt | PROPOSED |
| LPCI-T6 | Adversarial Evaluation | 5-10 source-sampled checks per corpus class, false-direct-answer audit | PROPOSED |
| LPCI-T7 | Template Packaging | downstream workspace guide for users/devs to bring their own corpus | PROPOSED |

## Work Plan

| Step | Requirement | Output | Status |
| --- | --- | --- | --- |
| L0 | Wait for Memory/MKE/KGR stabilization decision | readiness note or updated roadmap dependency | HOLD |
| L1 | Define corpus intake boundary and supported file classes | LPCI-T1 GC-018 + work order | PROPOSED |
| L2 | Build manifest and discovery index before semantic classification | source inventory, hash ledger, unreadable/unsupported ledger | PROPOSED |
| L3 | Add domain classification schema and evidence discipline | classification artifact aligned to GC-050 | PROPOSED |
| L4 | Add search/filter contract before answer generation | CVF search/filter readiness block, facet schema, query receipt, negative search evidence | PROPOSED |
| L5 | Add retrieval answer boundary and citation rules | retrieval receipt, abstention rules, freshness/conflict warning | PROPOSED |
| L6 | Prototype local chatbot only after L1-L5 pass | local UI/API, optional LLM key, secret-safe receipts | PROPOSED |
| L7 | Run adversarial sampling and false-direct-answer audit | review packet with sampled evidence | PROPOSED |

## Answer Boundary

LPCI must never present itself as a lawyer, compliance officer, or final
authority. The acceptable answer modes are:

- direct answer only when source authority, currentness, jurisdiction/scope, and
  citation are present;
- summary with source when the document was read but not enough to support a
  direct answer;
- procedural guidance when the user needs next steps rather than a rule;
- abstain or escalate when authority, date, jurisdiction, source status, or
  conflict resolution is missing.

## Non-Goals

- no legal advice claim;
- no production legal/compliance certification;
- no autonomous decisioning;
- no hidden prompt-only classification;
- no answer without source citation or abstention reason;
- no public upload of private company policy corpora by default;
- no claim that structural guards prove semantic correctness.

## Future Work Orders

The first implementation work order should be LPCI-T1 only. It should build the
corpus discovery and manifest layer without chatbot UI.

LPCI dispatch lock:

- LPCI-T1 may dispatch only after CI1-T7 closes.
- LPCI-T2 may dispatch only after LPCI-T1 closes.
- LPCI-T3 may dispatch only after LPCI-T2 closes.
- LPCI-T4 may dispatch only after LPCI-T3 closes.
- LPCI-T5 may dispatch only after LPCI-T4 closes.
- LPCI-T6 may dispatch only after LPCI-T5 closes.
- LPCI-T7 may dispatch only after LPCI-T6 closes.

Search, retrieval, and chatbot behavior should not be implemented until the
source and classification layers can prove what they covered and what they left
unresolved.

## Acceptance Criteria

- Every imported corpus has manifest-backed file inventory and hash evidence.
- Every classified source signal has source path, processing status,
  knowledge region, owner surface, disposition, answer boundary, and evidence
  pointer.
- Search/filter supports at least document type, source family, authority
  level, issuing body, effective date, status, topic, sensitivity, disposition,
  and answer class.
- Query receipts record normalized query, filters, candidate set, excluded set,
  rank reasons, citations, and abstention reason when applicable.
- Legal/policy answers include currentness/freshness boundary and cite source
  evidence; uncertain authority defaults to abstain/escalate.
- Review samples include accepted, deferred, rejected, and zero-result cases.
- No implementation artifact claims legal advice, production readiness, or
  semantic correctness from structural guard pass alone.

## Verification / Evidence

Future LPCI implementation must provide:

- GC-047 corpus completeness evidence;
- GC-048 knowledge-map reconciliation evidence;
- CVF Corpus Search And Filter Readiness evidence;
- GC-050 classification evidence;
- search/filter query receipt examples;
- negative search evidence for at least one no-result or excluded-source query;
- adversarial sampling review;
- live/provider proof only if the implementation claims LLM-governed behavior
  rather than static/local retrieval structure.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap records a private product direction and dependency chain.
No public-sync remote, public repository commit, public artifact path, hosted
proof, or public README claim is included.

## Claim Boundary

This roadmap records a real future CVF product direction for legal/policy
corpus intelligence. Generic search/filter readiness belongs to the broader CVF
standard, and LPCI consumes that standard. This roadmap does not close Memory,
KGR, MKE, or legal/policy chatbot implementation work.
