# CVF Corpus Scan Registry

Memory class: FULL_RECORD

Status: ACTIVE

docType: reference

Date: 2026-06-02

Last updated: 2026-06-12 (MEOR-RDA-T2 adapter source/tests)

Standard: `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`

Guard: `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`

Machine registry: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

---

## Scope / Target / Owner Boundary

Applies to: all agents and operators working on any CVF-governed project.
Owner: CVF governance control chain.
Scope: all corpora — legacy, project, policy, company docs, external sources.

## Scope / Applies To

This registry applies to every corpus scan, classification, or absorption task
in CVF and CVF-governed projects. See standard for full scope definition.

## Claim Boundary

Claims: structured index of all scanned corpora with findings and negative
search evidence. Does not claim semantic correctness of entries; production
readiness; complete coverage of all possible corpora.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: establish GC-051 Corpus Scan Registry as a
new CVF governance control. This batch adds a new checker, a new guard file,
new standard, and wires both into the autorun gate and local hook chain.
CLAUDE.md is updated to add GC-051 to Governance Controls to Know.

Protected paths:

- `CLAUDE.md`
- `governance/compat/check_corpus_scan_registry.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`

Operator authorization: operator direction on 2026-06-02 to establish a
corpus scan registry as a CVF-wide rule for all agents and projects, with a
dedicated folder, machine registry, standard, guard, and checker.

Rollback boundary: revert all files in this commit if the batch is unwound.
No runtime behavior changes — documentation, guard, checker, and wiring only.

---

## Purpose

Human-readable companion to the JSON registry. Provides a quick overview of
all corpora, their scan status, and key findings — searchable by domain keyword.
Any agent with a task touching a known corpus domain should find the relevant
prior scan here before starting new work.

---

## Quick Lookup: corpus status at-a-glance

| Corpus | Type | Status | Wave | Files | Key findings |
| --- | --- | --- | --- | --- | --- |
| `MLW-RT1 durable memory runtime proof` | RUNTIME_PROOF | SCANNED_WITH_FINDINGS | MLW-RT1 | 9 | Existing file-backed `/api/execute` durable-memory write/read continuity proved; backend migration/public readiness deferred |
| `CVF_Important/Knowledge Base_Graphify/` | LEGACY | SCANNED_WITH_FINDINGS | CI1-T2 | 5 | G-GM-* guard absent; CLI absent; KGR1 partial |
| `CVF ADD/code-review-graph/` | LEGACY | SCANNED_WITH_FINDINGS | CI1-T3 | 7 | graph governance signals deferred; command/MCP surface deferred; performance claims bounded |
| `CVF_Important/` (broad) | LEGACY | PARTIALLY_SCANNED | LHW-RESCAN-A | 230 | Inventory only; Graphify subfamily done |
| `CVF ADD/` | LEGACY | PARTIALLY_SCANNED | LHW-RESCAN-C | 167 | `code-review-graph/` is CI1-T3 candidate |
| `CVF 16.5/` | LEGACY | PARTIALLY_SCANNED | LHW-RESCAN-C | 100 | Broad routing only |
| `CVF_Restructure/` | LEGACY | PARTIALLY_SCANNED | LHW-RESCAN-C | 74 | Broad routing; Independent Review deferred |
| `CVF 17.05 + 25.05 + 28.05` | LEGACY | SCANNED | LHW-RESCAN-B | 38 | Governance decision artifacts; low priority |
| `CVF Edit/` | LEGACY | PARTIALLY_SCANNED | LHW18 | 10 | Integration SDK deferred; GC-047/050 not yet run |
| `App onboarding/` | LEGACY | NOT_STARTED | — | ? | UI design reference; low priority |
| `Policy_Local/data_input/` | POLICY_DOCUMENT | DEEP_CLASSIFIED | LPCI2-T10 | 2 | T10 foundation readiness closed; verifier/report hash-bound T9 scripts, corpus, chunks, and receipts; 76 chunks; 5/5 acceptance queries PASS; AQ-05 EC-02 freshness assertion preserved; EC-02 rescan required on or after 2026-07-01 |
| `DSCP-T1 domain-agnostic owner source surfaces` | CVF_EXTENSION | SCANNED | DSCP-T1 | 3 | Context pack, RAG convergence, and RAG pipeline type surfaces mapped for doc-only domain-agnostic schema proposal; TypeScript contracts deferred to DSCP-T2 |
| `MLW2-RT1 Context Bundle Runtime Proof` | PROJECT_SOURCE | SCANNED_WITH_FINDINGS | MLW2-RT1 | 8 | route-visible metadata-only contextBundleReadout; deterministic + Alibaba live proof; no full RAG/vector/public claim |
| `MLW3-RT1 Evidence-To-Learning Runtime Proof` | PROJECT_SOURCE | SCANNED_WITH_FINDINGS | MLW3-RT1 | 8 | route-visible metadata-only evidenceToLearningReadout; deterministic + Alibaba live proof; no truth mutation/orchestrator/public claim |
| `MLW4-MLW6 RT1 Continuity Audit Simulation Runtime Chain` | PROJECT_SOURCE | SCANNED_WITH_FINDINGS | MLW4-MLW6-RT1 | 8 | route-visible metadata-only continuity/audit/simulation readouts; deterministic + Alibaba live proof; no mutation/promotion/orchestrator/public claim |
| `External Review GAP1 extension README owner surfaces` | CVF_EXTENSION | SCANNED | ER-GAP1 | 2 | Skill Library and MCP README owner surfaces accepted only for Core KB overlap mapping; no runtime/public readiness claim |
| `CVF CPF DSCP-T10 domain profile contract source/export` | CVF_EXTENSION | SCANNED | DSCP-T10 | 2 | New deterministic domain-profile contract plus CPF export barrel; no corpus content ingested; no findings |
| `CVF CPF DSCP-T10 domain profile contract tests` | CVF_EXTENSION | SCANNED | DSCP-T10 | 1 | 17 vitest assertions covering legal_policy/company_docs/technical_project profiles; no corpus content ingested; no findings |
| `CVF CPF DSCP-T11 profile-aware pipeline harness tests` | CVF_EXTENSION | SCANNED | DSCP-T11 | 1 | 4 vitest assertions proving profile metadata/gates flow descriptor to ECO/LPF package without content release or cross-profile gate bleed |
| `CVF CPF DSCP-T11E domain profile registry source` | CVF_EXTENSION | SCANNED | DSCP-T11E | 1 | DscpDomainProfileRegistry class + factory; in-memory deterministic selection by domainFamily/languageCode/facetKey; no corpus content ingested |
| `CVF CPF DSCP-T11E domain profile registry tests` | CVF_EXTENSION | SCANNED | DSCP-T11E | 1 | 18 vitest assertions covering registration/selection/ambiguity/no-match/requiredFacetKey/select-then-apply pipeline integration |
| `CVF CPF DSCP-T11F profile selection adapter source` | CVF_EXTENSION | SCANNED | DSCP-T11F | 1 | selectAndApplyDscpDomainProfile combining registry selection + profile application in one deterministic pipeline; no corpus content ingested |
| `CVF CPF DSCP-T11F profile selection adapter tests` | CVF_EXTENSION | SCANNED | DSCP-T11F | 1 | 14 vitest assertions covering unique selection, no-match stop, ambiguous stop, blocked application stop, and profile isolation/no gate bleed |
| `CVF Extraction Foundation EX-T2 Tier 1 extractor source` | CVF_EXTENSION | SCANNED | EX-T2 | 1 | extract_docx + extract_pdf_text_layer + extract_tier1 dispatcher; MIN_CHARS_PER_PAGE=100; language-transparent; no OCR in this module |
| `CVF Extraction Foundation EX-T2 Tier 1 extractor tests` | CVF_EXTENSION | SCANNED | EX-T2 | 1 | 21 pytest assertions covering docx extraction, PDF text-layer extraction, dispatcher routing, UnsupportedFileTypeError, MIN_CHARS boundary, language_codes passthrough, and no-OCR source guard |
| `CVF Extraction Foundation EX-T2 package stubs` | CVF_EXTENSION | SCANNED | EX-T2 | 3 | Package marker stubs for EX-T2 source, src, and tests directories; no runtime behavior |
| `CVF Extraction Foundation EX-T3 through EX-T6 pipeline source` | CVF_EXTENSION | SCANNED | EX-T3-EX-T6 | 1 | Deterministic OCR adapter boundary, OCR language mapping, quality gate, chunk schema, and DSCP descriptor handoff; no OCR model download or corpus ingestion |
| `CVF Extraction Foundation EX-T3 through EX-T6 pipeline tests` | CVF_EXTENSION | SCANNED | EX-T3-EX-T6 | 1 | 10 pytest assertions covering language mapping, explicit OCR adapter requirement, confidence capture, quality flags, fixed-window chunking, and raw-content-release boundary |
| `CVF Extraction Foundation EX-T7 sentence-boundary chunking source` | CVF_EXTENSION | SCANNED | EX-T7 | 1 | Optional deterministic sentence-boundary strategy with fixed-window fallback and charStart/charEnd metadata; fixed-window default preserved |
| `CVF Extraction Foundation EX-T7 sentence-boundary chunking tests` | CVF_EXTENSION | SCANNED | EX-T7 | 1 | Focused pytest coverage for sentence grouping, long-span fallback, deterministic IDs, offset metadata, and raw-content-release boundary |
| `CVF Extraction Foundation EX-T8 authority/storage boundary source` | CVF_EXTENSION | SCANNED | EX-T8 | 1 | Extraction authority, rebuild class, raw OCR retention flag, storage boundary, boundary hash, and descriptor metadata propagation |
| `CVF Extraction Foundation EX-T8 authority/storage boundary tests` | CVF_EXTENSION | SCANNED | EX-T8 | 1 | Focused pytest coverage for authority, Tier 1/Tier 2 rebuild class, raw OCR retention default, descriptor metadata, and boundary hash determinism |
| `CVF Extraction Foundation EX-T9 scan outcome report source` | CVF_EXTENSION | SCANNED | EX-T9 | 1 | Domain-agnostic operator findings, stable actions, deterministic JSON/Markdown, and UTF-8 caller-selected output paths without raw content release |
| `CVF Extraction Foundation EX-T9 scan outcome report tests` | CVF_EXTENSION | SCANNED | EX-T9 | 1 | Focused pytest coverage for PASS, all current quality signals, generic blocking findings, deterministic rendering, raw-content non-release, and Unicode filenames |
| `CVF MEOR-T1 metadata evidence resolution contract` | PROJECT_SOURCE | SCANNED | MEOR-T1 | 2 | Domain-agnostic requirement, evidence, resolution, re-evaluation, failure-token, and cross-domain isolation semantics; specification only |
| `CVF MEOR-T2 metadata evidence normalization source` | CVF_EXTENSION | SCANNED | MEOR-T2 | 1 | Deterministic T1 matrix evaluation, failure tokens, profile ownership validation, bounded pointers, and EX-T9 finding adapter |
| `CVF MEOR-T2 metadata evidence normalization tests` | CVF_EXTENSION | SCANNED | MEOR-T2 | 1 | 30 focused pytest cases covering 21 allowed pairs, invalid records, provenance distinction, hint blocking, and report integration |
| `CVF MEOR-T3 DSCP profile requirement bridge source` | CVF_EXTENSION | SCANNED | MEOR-T3 | 3 | Optional profile-scoped declarations, evidence-basis literals, owner-map normalization, fail-closed validation, and no descriptor/gate mutation |
| `CVF MEOR-T3 DSCP profile requirement bridge tests` | CVF_EXTENSION | SCANNED | MEOR-T3 | 1 | 12 focused tests covering empty profiles, invalid declarations, owner mismatch, duplicates, evidence values, deterministic order, and non-mutation |
| `CVF MEOR-T4 cross-domain conformance fixture` | PROJECT_SOURCE | SCANNED | MEOR-T4 | 1 | Shared synthetic legal-policy and technical-project requirements plus four T1 resolution paths; no real use-case data |
| `CVF MEOR-T4 cross-domain conformance tests` | CVF_EXTENSION | SCANNED | MEOR-T4 | 2 | TypeScript and Python proof for exact sets, non-bleed, owner rejection, shared semantics, and bounded fixture content |
| `CVF MEOR-RDA-T2 regulated-domain adapter source and export surface` | CVF_EXTENSION | SCANNED | MEOR-RDA-T2 | 2 | Local deterministic helper and CPF context-barrel export generating four profile-owned regulated MEOR requirements for supportsDocumentStatus=true profiles; non-regulatory profiles receive eligible=false |
| `CVF MEOR-RDA-T2 regulated-domain adapter tests` | CVF_EXTENSION | SCANNED | MEOR-RDA-T2 | 1 | 16 focused TypeScript tests covering non-regulatory rejection, empty-ID failure, regulated eligible=true, owner scoping, evidence bases, concept keys, bridge-pass, bridge-mismatch, frozen result, and no gate activation |

---

## Finding Index

Use this index to find prior findings by domain keyword.

### Graph / Knowledge Graph

| Finding ID | Corpus | Summary | Disposition |
| --- | --- | --- | --- |
| F1-kgr1-partial | `Graphify/` | KGR1 partially absorbed data model + builder; full spec not implemented | ACCEPT_NO_ACTION |
| F2-guard-spec-absent | `Graphify/` | G-GM-01 through G-GM-08 guard IDs absent from CVF TS source | DEFER_WITH_ROADMAP |
| F3-cli-commands-absent | `Graphify/` | `cvf graph build/query/visualize/export/validate/status/purge` absent from CLI | DEFER_PHASED |
| RESCAN-C-code-review-graph | `CVF ADD/` | `code-review-graph/` subfolder (7 files) not yet deep-classified | DEFER_WITH_ROADMAP |
| F1-code-graph-value-confirmed | `code-review-graph/` | graph-backed static code intelligence confirmed as Knowledge Layer / Context Builder input | ACCEPT_NO_ACTION |
| F2-governance-signal-enforcement-deferred | `code-review-graph/` | impact, criticality, confidence, and context-inflation signals need future graph guard enforcement | DEFER_WITH_ROADMAP |
| F3-command-mcp-surface-deferred | `code-review-graph/` | command, CLI, MCP, audit, learning, and repo-registry adapters remain phased backlog | DEFER_PHASED |

### Performance Claims

| Finding ID | Corpus | Summary | Disposition |
| --- | --- | --- | --- |
| F4-performance-claim-unverified | `Graphify/` | 71.5x token reduction — author-reported, not CVF-verified | ACCEPT_WITH_BOUNDARY |
| F4-performance-claim-boundary | `code-review-graph/` | token-reduction/context-narrowing value accepted as rationale only, not CVF benchmark proof | ACCEPT_WITH_BOUNDARY |

### Integration / Adapters

| Finding ID | Corpus | Summary | Disposition |
| --- | --- | --- | --- |
| LHW18-integration-sdk | `CVF Edit/` | Integration SDK adapters not absorbed; frameworks connect INTO CVF | DEFER_DEMAND_GATED |

### PolicyLocal

| Finding ID | Corpus | Summary | Disposition |
| --- | --- | --- | --- |
| T9-F1-aq05-freshness-assertion-gap | `Policy_Local/data_input/` | Original T9 verifier marked AQ-05 PASS without asserting required freshness disclosure | ACCEPT_NO_ACTION - resolved by T9 correction |

### Memory / Learning Runtime

| Finding ID | Corpus | Summary | Disposition |
| --- | --- | --- | --- |
| MLW4-MLW6-RT1-F1-runtime-chain-proof-added | `MLW4-MLW6 RT1` | continuity, audit-feedback, and simulation/failure gates advanced from contract-only to route-visible metadata evidence | ACCEPT |
| MLW4-MLW6-RT1-F2-mutation-promotion-boundary | `MLW4-MLW6 RT1` | audit and simulation readouts remain proposal/review only; no mutation or auto-promotion authorized | ACCEPT_WITH_BOUNDARY |
| ER-GAP1-F1-extension-owner-surface | `External Review GAP1 extension README owner surfaces` | extension README files are owner surfaces for Core KB overlap mapping only; no runtime or public readiness claim | ACCEPT_WITH_BOUNDARY |

### Domain-Agnostic Scan Context Pack

| Finding ID | Corpus | Summary | Disposition |
| --- | --- | --- | --- |
| DSCP-T1-F1-governance-envelope-wrapper-needed | `DSCP-T1 domain-agnostic owner source surfaces` | ContextPackagerRequest and RAG pipeline types are reusable owner surfaces but need a governance envelope wrapper before cross-domain runtime use | DEFER_WITH_ROADMAP |

---

## Negative Search Evidence Index

Searches that confirmed absence — prevents re-doing the same negative search.

| Term | Search performed | Corpus | Result |
| --- | --- | --- | --- |
| `cvf graph` (CLI) | `rg "cvf graph" --include="*.ts"` in EXTENSIONS/ | Graphify | NOT FOUND |
| `G-GM-0` (guard IDs) | `rg "G-GM-0" --include="*.ts"` | Graphify | NOT FOUND |
| `GraphMemoryRecord` | `rg "GraphMemoryRecord"` | Graphify | NOT FOUND |
| `PreToolUse` hook | `rg "PreToolUse" --include="*.ts"` | Graphify | NOT FOUND in CVF TS source |
| `GRAPH_REPORT` | `rg "GRAPH_REPORT"` | Graphify | NOT FOUND in runtime |
| `NetworkX` / `leiden` | `rg "NetworkX\|leiden"` | Graphify | NOT FOUND |
| `direct external MCP access` | manual read of 7-file code-review-graph corpus | code-review-graph | FOUND as forbidden pattern, not allowed implementation |
| `graph service directly invoking LLMs` | manual read of 7-file code-review-graph corpus | code-review-graph | FOUND as forbidden pattern, not allowed implementation |
| full `CVF ADD/` sibling scan | CI1-T3 work-order boundary | code-review-graph | NOT SEARCHED — out of scope |
| `PolicyLocal search/chat runtime readiness` | LPCI2-T6/T7/T8 readiness gates | PolicyLocal | T9 search runtime IMPLEMENTED; local-deterministic only; no production deployment; no provider calls |
| `PolicyLocal live query negative evidence` | LPCI2-T8 completion review | PolicyLocal | PRODUCED at T9 and correction-cleaned; 5 acceptance query receipts generated; AQ-01 SUMMARY_WITH_SOURCE, AQ-02 through AQ-05 ESCALATE_OR_ABSTAIN; AQ-05 freshnessDisclosureApplied=true |
| `PolicyLocal foundation readiness` | LPCI2-T10 verifier/report | PolicyLocal | PRODUCED; hash-bound T9 external artifacts and assertion-checked AQ-01 through AQ-05; no provider, LLM, vector, corpus expansion, deployment, public-sync, current-law, or production readiness claim |

---

## Next Scan Recommendations

| Priority | Target | Reason |
| --- | --- | --- |
| HIGH | CI1-T4 Cross-Corpus Index Model | CI1 now has two real graph-adjacent packets: Graphify and code-review-graph |
| HIGH | MLW7/MLW8 or Learning Orchestrator fresh roadmap | MLW4-MLW6 RT1 now provides route-visible gate evidence, but no autonomous promotion/mutation |
| MEDIUM | Core KB pointer-ification after GAP1 overlap map | Use verified owner surfaces and split high-authority sections before editing the target document |
| MEDIUM | `CVF Edit/` — full GC-047/050 scan | Only LHW18 doc-only absorption done; no manifest or classification yet |
| MEDIUM | `CVF_Important/` remaining subfamilies | 230 files inventoried; deep classification pending per-family |
| LOW | `CVF 16.5/` + `CVF_Restructure/` deep scan | Broad routing done; deep classification when operator prioritizes |
| LOW | `App onboarding/` | UI design reference; not a knowledge absorption target |
| COMPLETE_T10 | PolicyLocal foundation readiness T10 | T10 verifier/report hash-binds T9 scripts, corpus, chunks, and receipts; all schema, hash, receipt assertion, and boundary checks PASS |
| HIGH | PolicyLocal corpus expansion readiness T11 | Inventory and source-verify candidate corpus additions before any runtime expansion; preserve EC-02 boundary until on or after 2026-07-01 |
| MEDIUM | PolicyLocal production deployment | T10 local-deterministic foundation ready; production deployment requires fresh operator-authorized work order and must not bypass EC-02/current-law review |

---

## How to Add a New Entry

1. Add to `CVF_CORPUS_SCAN_REGISTRY.json` (machine truth).
2. Add a row to the Quick Lookup table above.
3. Add any findings to the Finding Index.
4. Add any negative searches to the Negative Search Evidence Index.
5. Add a next scan recommendation row if applicable.
6. Commit both files together in the same governed batch.
