# CVF GC-018 LPCI1 Legal Policy Corpus Intelligence Product MVP Baseline

Memory class: FULL_RECORD

Status: ACTIVE

docType: baseline

Date: 2026-06-03

executionBaseHead: `c0ebfd9c`

## Purpose

Authorize LPCI1 as a governed CVF product roadmap unit. This baseline
establishes the product scope, corpus prerequisites, claim boundary, gap
acknowledgment obligations, and forbidden-scope rules for the first LPCI
product implementation wave.

LPCI1 is the Legal/Policy Corpus Intelligence chatbot MVP. It turns a
bounded corpus of laws, decrees, circulars, internal company policies,
notices, decisions, and SOPs into classified, searchable, citeable knowledge
and lets a model explain or summarize inside explicit answer boundaries.

This baseline is a planning authorization only. It does NOT authorize
runtime implementation, provider calls, or live product deployment. Each
implementation tranche must open a fresh work order with source verification
and scoped acceptance criteria.

## Scope / Applies To

Applies to:

- all LPCI1 implementation tranches (LPCI1-T1 through LPCI1-T7);
- any CVF worker or agent that adds routes, components, API endpoints, vector
  DB schemas, corpus ingest pipelines, or retrieval logic for LPCI;
- any roadmap or work order that claims LPCI product authority.

Owner surface: CVF governance layer; LPCI1 product tranche owners.

Out of scope:

- legal advice, production compliance certification, public SaaS, multi-tenant
  upload, autonomous legal decisioning;
- features beyond what is listed in the MVP tranche plan and product sketch.

---

## Source

This baseline is authorized by the following predecessor evidence. All items
must exist at the dispatch-base commit before LPCI1-T1 may be executed.

| Predecessor | Path | Status at dispatch |
| --- | --- | --- |
| CI2 GC-018 | `docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md` | CLOSED_PASS_BOUNDED |
| CI2-T4 pilot pack | `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | CLOSED_PASS_BOUNDED |
| CI2-T4 closure review | `docs/reviews/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_COMPLETION_2026-06-02.md` | CLOSED_PASS_BOUNDED |
| CI1-T7 LPCI intake bridge | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | ACTIVE |
| LPCI use-case roadmap | `docs/roadmaps/CVF_LPCI_LEGAL_POLICY_CORPUS_INTELLIGENCE_CHATBOT_USE_CASE_ROADMAP_2026-06-01.md` | ACTIVE |

---

## Authority Chain

| Authority | Artifact |
| --- | --- |
| CI2 GC-018 | `docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md` |
| CI2 roadmap | `docs/roadmaps/CVF_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_ROADMAP_2026-06-02.md` |
| CI2-T4 closure | `docs/reviews/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_COMPLETION_2026-06-02.md` |
| CI2-T4 pilot pack | `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` |
| CI1-T7 LPCI intake bridge | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` |
| LPCI use-case roadmap | `docs/roadmaps/CVF_LPCI_LEGAL_POLICY_CORPUS_INTELLIGENCE_CHATBOT_USE_CASE_ROADMAP_2026-06-01.md` |
| CI2-T3 enforced index model | `docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json` |
| CI2-T5 work order | `docs/work_orders/CVF_WO_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_2026-06-02.md` |

---

## Decision

LPCI1 is authorized as a governed CVF product roadmap unit with the following
binding decisions:

1. **Product authorized**: The LPCI legal/policy corpus intelligence chatbot
   MVP is authorized for roadmap authoring, architecture intake, and staged
   implementation planning.

2. **No runtime until T1 passes**: No UI, API routes, vector DB schema,
   embedding pipeline, or provider invocation may be created before
   LPCI1-T1 product intake and architecture work order closes with an
   authorized architecture document.

3. **Corpus prerequisites required**: Any LPCI corpus scan requires a prior
   GC-051 registration. Classification must satisfy GC-047, GC-048, and GC-050.

4. **CI2 standards adopted**: LPCI inherits NR-04, NR-05, and NR-11
   enforcement from CI2. Per-file sourceHash or manifest proxy must be
   structurally enforced for all LPCI corpus packets.

5. **Gap acknowledgment binding**: All three T6 gaps listed in the CI1-T7
   LPCI intake bridge (NR-04, NR-05, NR-11) are post-CI2 satisfied and must
   be cited by LPCI1-T1 GC-018 before implementation begins.

---

## Evidence

Evidence required before any LPCI1 implementation tranche begins:

| Evidence type | Artifact | Required state |
| --- | --- | --- |
| CI2-T5 closure | `docs/reviews/CVF_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_COMPLETION_2026-06-02.md` | CLOSED_PASS_BOUNDED |
| LPCI1 GC-018 (this baseline) | `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` | ACTIVE |
| LPCI1 MVP roadmap | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | ACTIVE |
| CI2-T4 pilot pack | `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | valid JSON, CLOSED_PASS_BOUNDED |
| GC-051 registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | target corpus must be registered before any ingest tranche |

---

## Corpus Prerequisites

Before any LPCI corpus ingest or retrieval implementation tranche begins, the
following corpus prerequisites must be satisfied:

| Prerequisite | Standard | Status |
| --- | --- | --- |
| Corpus GC-051 registration | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | REQUIRED PER CORPUS |
| Corpus completeness check (GC-047) | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | REQUIRED PER CORPUS |
| Knowledge-map reconciliation (GC-048) | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` | REQUIRED PER CORPUS |
| Corpus classification (GC-050) | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | REQUIRED PER CORPUS |
| NR-04 sourceHash enforcement | `docs/reference/CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md` | SATISFIED_BY_CI2_T1_T2 |
| NR-05 normalizedPath enforcement | `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md` | SATISFIED_BY_CSA1_CI2_T2 |
| NR-11 dispositionAlias enforcement | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | SATISFIED_BY_CSA1_CI2_T2 |

For the governance pilot corpus (`GOVERNANCE_PILOT_NO_LEGAL_CORPUS`) that
proved field population shape:

- CI2-T4 pilot pack at `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json`
  is the schema proof for LPCI1-T1 intake. It does NOT serve as a production
  corpus. A real legal/policy corpus must be separately registered and classified.

---

## Gap Acknowledgment (inherited from CI1-T7)

Per `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` lines
165-173, LPCI1-T1 must acknowledge the following gaps in its own GC-018:

| gapId | CI2 resolution | LPCI obligation |
| --- | --- | --- |
| NR-04 sourceHash | Standard: `CVF_CORPUS_SOURCE_HASH_STANDARD_2026-06-02.md`; checker: `check_corpus_packet_source_hash.py` (CI2-T2) | LPCI1-T1 GC-018 must cite the NR-04 standard and state whether LPCI ingest requires per-file hash or accepts documented manifest proxy |
| NR-05 normalizedPath | Standard: `CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md`; checker: `check_corpus_packet_normalized_path.py` (CI2-T2) | LPCI1-T1 GC-018 must cite the NR-05 algorithm standard and confirm the same normalizedPath algorithm is adopted |
| NR-11 dispositionAlias | Classification standard (CSA1/CI2-T2); checker: `check_corpus_packet_disposition_canonical.py` | LPCI1-T1 GC-018 must cite the classification standard and confirm consumption of `rawDisposition` plus `dispositionAlias: ACCEPT_DEFERRED` for DEFER/ACCEPT_SUMMARY_ONLY rows |

---

## Product Boundary

| Boundary | Rule |
| --- | --- |
| Corpus ownership | User/operator owns the source corpus, legal judgment, and currentness review |
| CVF role | CVF owns governance, corpus discipline, retrieval boundary, citation receipts, and answer-class control |
| LLM provider role | May assist with explanation and summarization inside retrieved evidence and answer boundary only |
| Legal advice | OUT OF SCOPE — LPCI never claims legal advice quality |
| Production compliance certification | OUT OF SCOPE |
| Public SaaS / multi-tenant hosting | OUT OF SCOPE until separate security/legal/product reviews exist |

---

## Alternatives

| Alternative | Reason not chosen |
| --- | --- |
| Continue with governance pilot corpus only (no legal corpus) | Insufficient for the product goal; a real legal corpus intake is needed for LPCI value delivery |
| Skip GC-051 registration for LPCI corpus | Rejected — GC-051 is a mandatory gate before any corpus expansion |
| Implement LPCI runtime before T1 architecture review | Rejected — no-runtime-until-T1 gate is binding per this baseline |
| Use a generic LLM search without CVF corpus discipline | Rejected — violates CVF governance model; no cited-evidence boundary |

---

## Consequences

| Consequence | Effect |
| --- | --- |
| LPCI1 product roadmap is now an active CVF commitment | Future work orders for LPCI tranches are authorized by this GC-018 |
| Any LPCI runtime tranche must open a separate work order | CI2-T5 creates planning artifacts only; T1 is the first authorized implementation tranche |
| Legal/policy corpus must be registered before classification | Prevents un-governed corpus intake that bypasses GC-047/GC-050 |
| LPCI inherits CI1 and CI2 claim boundaries | No chatbot answer may exceed answer-class authorization set in T4 model |

---

## Implementation Gate (no-runtime-until-T1)

No LPCI runtime artifact (route, component, vector DB schema, embedding
pipeline, API endpoint, browser test, or provider call) may be created
until LPCI1-T1 closes with:

- an authorized architecture document;
- a GC-051-registered target corpus (or explicit GOVERNANCE_PILOT_NO_LEGAL_CORPUS
  acknowledgment for architecture-only tranches);
- a signed GC-018 (this baseline plus T1-level supplement).

---

## Claim Boundary

This baseline authorizes product roadmap planning and architecture intake only.

It does NOT claim:

- runtime legal retrieval behavior;
- legal answer correctness or production readiness;
- chatbot accuracy, precision, or completeness for any legal domain;
- embedding quality or vector index correctness;
- public or hosted readiness;
- multi-tenant or SaaS capability.

---

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` — no LPCI1-specific GC-018 baseline existed prior
to this tranche

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_ADDED` — LPCI1 GC-018 establishes product boundary, gap
acknowledgment obligations, corpus prerequisites, and no-runtime-until-T1 gate

Next control action: `CLOSED` — baseline authored; LPCI1-T1 work order is
the next authorized dispatch

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: this baseline is a governance planning artifact only; no provider
calls, runtime behavior changes, or cost events.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: baseline references private corpus pilot data and internal governance
chain details not suitable for the public CVF repository until a public-facing
architecture document is separately authored.

Public-sync boundary: no artifacts from this batch are queued for public-sync.
Next public-sync action: none required.
