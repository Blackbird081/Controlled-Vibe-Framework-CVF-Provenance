# CVF LPCI2 PolicyLocal Corpus Intelligence Evidence Roadmap

Memory class: FULL_RECORD

Status: T5_DISPATCH_READY

docType: roadmap

Date: 2026-06-03

executionBaseHead: `3ff90651`

## Purpose

Use PolicyLocal as a local-first evidence lane to prove CVF Corpus Intelligence
discipline on real user-supplied legal/policy files. PolicyLocal remains a
future application target, but this roadmap is not a commitment to build the
production chatbot now.

This roadmap starts after LPCI1-T1 through LPCI1-T7 are
`CLOSED_PASS_BOUNDED`. It is not a continuation of worker dispatch; it is a
self-executed Corpus Intelligence control path until the operator reopens
external worker delegation.

## Scope / Applies To

Applies to: PolicyLocal local workspace adoption, bounded pilot corpus intake,
Corpus Intelligence classification proof, and any later UI/API implementation
for the legal/policy chatbot use case.

Owner surface: CVF governance layer; Corpus Intelligence foundation; LPCI
product surface; PolicyLocal local workspace.

## Strategic Boundary

PolicyLocal is currently a test use case for proving CVF Corpus Intelligence as
a reusable foundation capability. It must not be treated as a production
chatbot build lane while legacy Memory/Knowledge absorption remains incomplete
or while local corpus records are only hash-only, partially extracted, or
classification-unverified.

The correct near-term output is machine-readable corpus evidence: sourceHash,
normalizedPath, extracted text boundary, legal/policy domain fields,
classification ledger, response boundary, and sampling evidence. The app/runtime
layer remains deferred until that evidence is strong enough to support LLM
retrieval without overclaiming.

## Authority Chain

| Authority | Path | Disposition |
| --- | --- | --- |
| Operator instruction | chat instruction on 2026-06-03 to let Codex hold multiple roles and finish without external worker handoff | ACCEPT |
| LPCI1 MVP roadmap | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | ACCEPT |
| LPCI1-T7 template packaging spec | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` | ACCEPT |
| PolicyLocal frontend handoff | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CLAUDE_BUILD_HANDOFF.md` | ACCEPT as external workspace input |
| Codex PolicyLocal addendum | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_SPEC_REVIEW_2026-06-02.md` | ACCEPT as external workspace input |

## Roadmap

| Tranche | Goal | Output | Status |
| --- | --- | --- | --- |
| LPCI2-T1 | PolicyLocal build control packet | repo reference packet plus workspace copy tying Claude spec to LPCI1 rules | CLOSED_PASS_BOUNDED |
| LPCI2-T2 | Product scaffold readiness decision | review Claude-built local prototype and decide scaffold readiness | CLOSED_PASS_BOUNDED |
| LPCI2-T2A | Prototype schema cleanup | fix T2 answer-class, citation, receipt, and local validation blockers in the Policy_Local prototype | CLOSED_PASS_BOUNDED |
| LPCI2-T3 | Production-corpus pilot planning | define first real corpus, GC-051 registration, legal/policy domain fields, and sampling plan | CLOSED_PASS_BOUNDED |
| LPCI2-T4S | Data input smoke test | rename local folder to `data_input`, hash two DOCX files, and record hash-only boundary | CLOSED_PASS_BOUNDED |
| LPCI2-T4 | Corpus Intelligence import/classification evidence | extract DOCX text locally, populate legal/policy fields, and run GC-047/GC-050 without search/chat | CLOSED_PASS_BOUNDED |
| LPCI2-T5 | Deep classification evidence | full-body effectiveDate scan, GC-048 knowledge-map reconciliation, adversarial sampling | DISPATCH_READY |

## Work Plan

| Step | Action | Output | Status |
| --- | --- | --- | --- |
| W1 | Create PolicyLocal build-control packet | repo reference plus external workspace copy | CLOSED_PASS_BOUNDED |
| W2 | Decide scaffold readiness | prototype accepted as visual reference with schema blockers before runtime scaffold | CLOSED_PASS_BOUNDED |
| W2A | Clean prototype schema blockers | canonical answer classes, citation minimum, receipt boundary, and validator added | CLOSED_PASS_BOUNDED |
| W3 | Plan production-corpus pilot | GC-051 drop-zone registration plus T3 pilot plan | CLOSED_PASS_BOUNDED |
| W4S | Smoke-test data input | two DOCX files hashed with no text extraction claim | CLOSED_PASS_BOUNDED |
| W4 | Import and classify local corpus | DOCX extraction and legal/policy classification evidence | CLOSED_PASS_BOUNDED |
| W5 | Deep classification and knowledge-map reconciliation | full-body effectiveDate scan, GC-048, adversarial sampling | DISPATCH_READY |

## Decision

LPCI2-T1 created the build-control packet. LPCI2-T2 reviewed the new local
PolicyLocal prototype files and accepted them as visual/product reference only.
LPCI2-T2A repaired the concrete schema blockers in the local `Policy_Local`
prototype while preserving the no-runtime/no-chatbot boundary. LPCI2-T3
registered the pilot corpus drop-zone and defined the import, domain,
search, and sampling gates required before real chat runtime. LPCI2-T4S renamed
the local-first corpus folder to `data_input` and proved two DOCX files can be
enumerated, normalized, and hashed, while keeping text extraction and answer
runtime blocked. LPCI2-T4 is CLOSED_PASS_BOUNDED at commit `212d6adf`. LPCI2-T5 is DISPATCH_READY
as deep-classification evidence: full-body effectiveDate scan, GC-048
knowledge-map reconciliation, and adversarial sampling. Search/chat/runtime
remains blocked until T5 closes and a separate readiness gate work order passes.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| LPCI1 inheritance preserved | packet cites T1-T7 specs and answer-boundary rules |
| PolicyLocal handoff constrained | Claude frontend spec is accepted only with CVF addendum gates |
| External workspace copy present | packet saved under `CVF-Workspace\PolicyLocal` |
| Runtime boundary preserved | no app code, API route, DB file, provider call, answer runtime, or public-sync |
| Next move clear | T2/T3/T4 dependency order recorded |
| Prototype readiness classified | T2 review separates visual acceptance from runtime blockers |
| Prototype schema cleaned | T2A adds canonical answer-class constants, citation fields, receipt boundary fields, and validator |
| Production corpus pilot planned | T3 registers a GC-051 drop-zone and defines import/sampling release gates |
| Data input smoke-tested | T4S proves hash-only local file detection and records DOCX extraction as deferred |
| Product deferral explicit | T4 is evidence-only and T5 remains blocked by T4 evidence plus memory/legacy readiness |

## Verification Evidence

| Evidence | Path |
| --- | --- |
| Work order | `docs/work_orders/CVF_WO_LPCI2_T1_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |
| Repo build-control packet | `docs/reference/CVF_LPCI2_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |
| Completion review | `docs/reviews/CVF_LPCI2_T1_POLICYLOCAL_BUILD_CONTROL_PACKET_COMPLETION_2026-06-03.md` |
| Session sync authorization | `docs/reviews/CVF_LPCI2_T1_SESSION_SYNC_AUTH_2026-06-03.md` |
| Workspace copy | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CVF_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` |
| T2 work order | `docs/work_orders/CVF_WO_LPCI2_T2_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_2026-06-03.md` |
| T2 readiness review | `docs/reviews/CVF_LPCI2_T2_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_REVIEW_2026-06-03.md` |
| T2 session sync authorization | `docs/reviews/CVF_LPCI2_T2_SESSION_SYNC_AUTH_2026-06-03.md` |
| T2 workspace review copy | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_FRONTEND_PROTOTYPE_READINESS_REVIEW_2026-06-03.md` |
| T2A work order | `docs/work_orders/CVF_WO_LPCI2_T2A_POLICYLOCAL_PROTOTYPE_SCHEMA_CLEANUP_2026-06-03.md` |
| T2A completion review | `docs/reviews/CVF_LPCI2_T2A_POLICYLOCAL_PROTOTYPE_SCHEMA_CLEANUP_COMPLETION_2026-06-03.md` |
| T2A session sync authorization | `docs/reviews/CVF_LPCI2_T2A_SESSION_SYNC_AUTH_2026-06-03.md` |
| T2A workspace completion note | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_SCHEMA_CLEANUP_COMPLETION_2026-06-03.md` |
| T3 work order | `docs/work_orders/CVF_WO_LPCI2_T3_PRODUCTION_CORPUS_PILOT_PLANNING_2026-06-03.md` |
| T3 pilot plan | `docs/reference/CVF_LPCI2_T3_POLICYLOCAL_PRODUCTION_CORPUS_PILOT_PLAN_2026-06-03.md` |
| T3 completion review | `docs/reviews/CVF_LPCI2_T3_POLICYLOCAL_PRODUCTION_CORPUS_PILOT_PLANNING_COMPLETION_2026-06-03.md` |
| T3 session sync authorization | `docs/reviews/CVF_LPCI2_T3_SESSION_SYNC_AUTH_2026-06-03.md` |
| T3 GC-051 registry entry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` entry `policylocal-production-corpus-dropzone` |
| T4S work order | `docs/work_orders/CVF_WO_LPCI2_T4S_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_2026-06-04.md` |
| T4S completion review | `docs/reviews/CVF_LPCI2_T4S_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_COMPLETION_2026-06-04.md` |
| T4S session sync authorization | `docs/reviews/CVF_LPCI2_T4S_SESSION_SYNC_AUTH_2026-06-04.md` |
| T4S workspace completion note | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\CODEX_POLICYLOCAL_DATA_INPUT_SMOKE_TEST_COMPLETION_2026-06-04.md` |
| T4S local manifest | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-data-input-manifest.json` |
| T4 work order | `docs/work_orders/CVF_WO_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_2026-06-04.md` |
| T4 completion review | `docs/reviews/CVF_LPCI2_T4_CORPUS_INTELLIGENCE_IMPORT_CLASSIFICATION_EVIDENCE_COMPLETION_2026-06-04.md` |
| T5 work order | `docs/work_orders/CVF_WO_LPCI2_T5_POLICYLOCAL_DEEP_CLASSIFICATION_2026-06-04.md` |

## Non-Goals

- Build the PolicyLocal app.
- Turn the pilot local corpus into a production product corpus.
- Run provider calls or live legal answer tests.
- Claim legal advice, current law status, production readiness, or public
  release readiness.
- Push or sync artifacts to the public CVF repository.
- Treat PolicyLocal as more important than finishing Memory/Knowledge legacy
  absorption.

## Claim Boundary

This roadmap claims that LPCI2-T1 created a reusable build control packet,
LPCI2-T2 reviewed the local frontend prototype as visual/product reference,
LPCI2-T2A cleaned the concrete prototype schema blockers with local validation,
LPCI2-T3 registered the production-corpus drop-zone plus pilot release gates,
and LPCI2-T4S smoke-tested two local DOCX files through hash-only intake.

LPCI2-T4 claims DOCX text extraction (READ_SHALLOW), conservative legal/policy
classification (answerClass=SUMMARY_WITH_SOURCE), and GC-051 registry update.
LPCI2-T5 is dispatch-authorized for deep classification, GC-048, and adversarial
sampling evidence.

It does not claim runtime implementation, chatbot product readiness, production
corpus readiness, legal answer correctness, hosted readiness, or public export.

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` - after LPCI1 closure, PolicyLocal had a strong
frontend handoff but no single product build control packet that made LPCI
rules mandatory for implementation.

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `TEMPLATE_UPDATED` - LPCI2-T2A adds a local prototype validator and
records that future PolicyLocal scaffold work must include schema fixture
validation before chat runtime is accepted.

Next control action: `DISPATCH_READY` for T5 deep classification. T5 must not
start search, chat runtime, or product implementation. Readiness gate is a
separate work order after T5 closes.

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: LPCI2-T1 is documentation and productization control only.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this roadmap references a private local workspace path and internal
LPCI governance chain. A sanitized public-facing guide may be prepared later as
a separate public-sync batch.
