# CVF Document Translator Control Adaptation Roadmap

Memory class: FULL_RECORD

Status: PROPOSED_READY_FOR_FRESH_AUTHORIZATION

docType: roadmap

Date: 2026-06-13

Owner: Codex

## Authorization / Decision

Decision: `DOCUMENT_TRANSLATOR_AS_CVF_CONTROLLED_USE_CASE`.

Operator priority:

1. CVF foundation quality remains priority one.
2. The Document Translator repository is a downstream CVF use case, similar to
   Policy_Local, not a replacement for CVF foundation work.
3. Future edits should adapt the cloned repository to CVF control standards
   through a separate roadmap and fresh work orders.

Target external workspace:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator`

This roadmap authorizes planning only. It does not authorize external
repository edits, dependency installation, OCR execution, provider/API-key use,
document ingestion, public-sync, production readiness, public readiness, or
cost/quality claims.

## Purpose

Use Document Translator as a governed document-processing use-case repo to
prove that CVF can control long-document workflows with deterministic routing,
operator-visible confidence, audit logs, budget boundaries, and review gates.

The useful CVF lesson is not "document translation" as an application. The
useful foundation direction is a CVF-controlled document intelligence route
between intake and downstream knowledge/context work.

## Scope / Target / Owner Boundary

In scope:

- create a private provenance roadmap for a future Document Translator control
  adaptation lane;
- record the source snapshot of the cloned external repository;
- preserve the operator decision that CVF foundation quality is priority one;
- map the use-case lane to existing CVF extraction foundation owners;
- define the first safe tranche as audit/control only.

Out of scope:

- editing the external repository;
- creating a GC-018 baseline or work order in this batch;
- installing or running app dependencies;
- executing OCR, providers, WebSocket jobs, translation jobs, or API routes;
- copying external app code into CVF;
- mutating Policy_Local or Document Translator data;
- public-sync, production readiness, public readiness, or cost/quality claims.

Target owner surface: CVF private provenance planning under `docs/roadmaps/`.

External use-case target:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator`

## Non-Goals

This roadmap does not:

- adopt Document Translator as the CVF product front door;
- convert CVF into a document-translation app;
- prove the external repository's README performance, cost, provider, layout,
  or production claims;
- authorize translation memory, glossary, export, auth, quota, dashboard,
  provider fallback, OCR runtime, or publishing features;
- unlock Policy_Local, EC, retrieval, T12, provider proof, or public-sync;
- authorize autonomous mutation of CVF foundation or the external app.

## Source Authority

Source authority for this roadmap is limited to:

- operator instruction in this session;
- local source observations from the cloned external repository at
  `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`;
- prior governed EXA-T1 and EXA-T2 closure artifacts;
- current CVF extraction foundation source files named below.

`Thong_tin.md` is treated as an operator assessment note, not as runtime proof,
source-code proof, production-readiness proof, or cost/quality evidence.

## Source Snapshot

| Item | Observed value | Disposition |
| --- | --- | --- |
| External clone path | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator` | ACCEPT |
| Remote | `https://github.com/nclamvn/dich-tai-lieu` | ACCEPT |
| Current HEAD | `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336` | ACCEPT |
| Tracked files | `1140` by `git -c core.quotepath=false ls-files` | ACCEPT |
| External worktree | `?? Thong_tin.md` | ACCEPT_AS_OPERATOR_NOTE |
| CVF root note | `Thong_tin.md` untracked in provenance repo | ACCEPT_AS_OPERATOR_NOTE |

The external repository README and `CLAUDE.md` contain product, performance,
cost, provider, and production-readiness statements. Those are source
observations only. CVF does not adopt them as evidence without separately
authorized runtime proof.

## Authority Chain

| Authority | Path or source | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-13 chat: CVF foundation first; Document Translator is a use case | ACCEPT |
| Operator assessment note | `Thong_tin.md` | ACCEPT_AS_OPERATOR_NOTE |
| External clone | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Document_Translator` at `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336` | ACCEPT_AS_REVIEW_SOURCE |
| EXA-T1 closure | `docs/reviews/CVF_EXA_T1_DICH_TAI_LIEU_SCAN_LAYER_PATTERN_ABSORPTION_COMPLETION_2026-06-12.md` | ACCEPT_AS_PRIOR_ABSORPTION |
| EXA-T2 closure | `docs/reviews/CVF_EXA_T2_SCAN_SIGNAL_ROUTE_DECISION_CONTRACTS_COMPLETION_2026-06-12.md` | ACCEPT_AS_CURRENT_CVF_FOUNDATION |
| PolicyLocal successor model | `docs/roadmaps/CVF_POLICYLOCAL_SUCCESSOR_PILOT_ROADMAP_2026-06-12.md` | ACCEPT_AS_USE_CASE_PRECEDENT |

## Foundation-First Gate

Verdict: `PASS_BOUNDED_PROPOSED`.

This roadmap preserves CVF foundation as the priority:

- Document Translator is a use-case repo controlled by CVF, not a source of
  automatic CVF semantics.
- Existing CVF extraction foundation remains the owner for deterministic scan
  signals, route decision, extraction quality, storage boundary, and
  operator-visible scan outcome reporting.
- Any missing foundation capability must first be specified and implemented in
  CVF owner surfaces before the external app receives runtime edits that depend
  on it.
- Translation, publishing, provider fallback, OCR runtime, UI, dashboard,
  quota, and export behavior are downstream application surfaces.

## Existing CVF Foundation To Reuse

| CVF surface | Current owner | Reuse rule |
| --- | --- | --- |
| `DocumentScanSignals` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | Use as the normalized pre-route signal contract |
| `ScanRouteDecision` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_route_decision.py` | Use as the bounded route recommendation surface |
| `evaluate_extraction_quality()` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | Reuse before proposing new confidence scoring |
| `ExtractionStorageBoundary` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | Preserve raw-content and descriptor boundary discipline |
| `ScanOutcomeReport` | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/scan_outcome_report.py` | Reuse for operator-visible findings and actions |

## External Source Observations

The external repo has high-value implementation patterns:

- `core/smart_extraction/document_analyzer.py` defines document/page analysis
  dataclasses, route thresholds, scanned-page detection, academic detection,
  table/image/formula heuristics, and extraction strategy selection.
- `core/smart_extraction/extraction_router.py` routes FAST_TEXT, HYBRID,
  FULL_VISION, and OCR strategies and records text/vision/OCR page counts.
- `api/services/provider_router.py` defines provider routing modes and cold-start
  provider cost/quality defaults.
- README and `CLAUDE.md` describe a broader publishing app: translation memory,
  glossary, export, auth, quota, dashboard, WebSocket progress, and
  multi-provider fallback.

CVF disposition:

- Accept document profiling and extraction-route structure as use-case value.
- Reuse or extend CVF-owned extraction contracts before editing app runtime.
- Defer provider routing, OCR runtime, translation memory, glossary, export,
  dashboard, auth, quota, and live cost behavior to later tranches.
- Reject adopting external performance, cost, quality, or production-readiness
  claims as CVF evidence.

## Design Control Gate

Selected design:

1. Create a governed Document Translator lane separate from Policy_Local.
2. Treat Document Translator as a downstream controlled use case.
3. Start with repo custody, source map, secret-safety, and CVF control shell.
4. Route all runtime changes through fresh GC-018 baselines and source-verified
   work orders.
5. Keep CVF foundation surfaces authoritative.

Rejected design:

- direct code import into CVF foundation;
- immediate external repo runtime edits without source map and control shell;
- immediate OCR/provider execution;
- direct provider cost router adoption;
- translation/publishing capability package before document-intelligence
  foundation is stable;
- production/public readiness claims from README or external docs.

## Proposed Tranche Plan

| Tranche | Deliverable | Dependency | Status |
| --- | --- | --- | --- |
| DT-CVF-T0 | Source custody, repo inventory, secret-safety, and control-baseline audit | This roadmap plus fresh GC-018 | READY_FOR_FRESH_AUTHORIZATION |
| DT-CVF-T1 | External repo CVF control shell and contribution boundary | DT-CVF-T0 closure | HOLD_PENDING_T0 |
| DT-CVF-T2 | Document Intelligence Router contract map from app surfaces to CVF foundation | DT-CVF-T1 closure | HOLD_PENDING_T1 |
| DT-CVF-T3 | Deterministic profiler/structure metadata adapter inside use-case repo | DT-CVF-T2 closure | HOLD_PENDING_T2 |
| DT-CVF-T4 | Operator confidence, audit log, and review-gate alignment | DT-CVF-T3 closure | HOLD_PENDING_T3 |
| DT-CVF-T5 | Provider/OCR runtime gateway assessment with live-proof requirements | DT-CVF-T4 closure plus operator key/quota authorization | HOLD_PENDING_RUNTIME_AUTH |
| DT-CVF-T6 | Controlled document-translation pilot over bounded sample corpus | DT-CVF-T5 closure plus operator sample corpus | HOLD_PENDING_SAMPLE_CORPUS |

## Work Plan

1. Treat this roadmap as the intake/design artifact only.
2. If the operator authorizes DT-CVF-T0, create a fresh GC-018 baseline and
   source-verified work order.
3. In DT-CVF-T0, source-map the external clone, classify sensitive/generated
   surfaces, verify branch/remote/status, and identify first control-shell
   edit candidates.
4. Keep all runtime/provider/OCR/app edits blocked until T0 returns and Codex
   reviews the source map.
5. Open DT-CVF-T1 only after T0 closure proves the external repo custody and
   control boundaries.
6. Route later app behavior through CVF foundation owners before use-case
   runtime mutation.

## DT-CVF-T0 Scope Recommendation

First tranche should be audit/control only.

DT-CVF-T0 may:

- read the external clone;
- record remote, HEAD, branch, status, tracked-file count, and ignored/untracked
  surfaces;
- identify potential secrets or generated data directories;
- source-map smart extraction, provider routing, translation memory, glossary,
  export, auth, quota, dashboard, and WebSocket surfaces;
- compare the app against current CVF extraction foundation owners;
- produce a bounded adaptation plan and next work order.

DT-CVF-T0 must not:

- edit the external repo;
- copy app code into CVF;
- install dependencies;
- execute OCR, providers, WebSocket jobs, batch jobs, or API routes;
- read or print secret values;
- mutate `uploads/`, `outputs/`, `data/`, or any corpus records;
- claim production, public, cost, quality, or provider readiness.

## Future Control Shell Direction

If DT-CVF-T0 closes cleanly, DT-CVF-T1 should add or adapt a compact control
shell in the external repo. Candidate surfaces:

- a CVF control readme or `AGENTS.md` equivalent;
- claim-boundary rules for performance/cost/provider claims;
- secret-safety and API-key handling rules;
- operator-visible evidence requirements;
- no-raw-content-release defaults for CVF-governed runs;
- branch and commit discipline for Codex/Claude worker return.

The exact files must be source-verified in the DT-CVF-T1 work order before any
edit is dispatched.

## Relationship To Policy_Local

Policy_Local remains parked behind its own PL-S authorization chain.

Document Translator is a separate use-case lane. It should not consume or
unlock Policy_Local, EC, T12, retrieval, OCR, or legal/current-status work.

Shared foundation may be reused:

- extraction signal contracts;
- scan outcome reporting;
- metadata evidence discipline;
- operator review packets;
- memory consolidation boundaries.

Use-case-specific behavior must remain separated:

- Policy_Local: regulated-domain evidence and legal/current-status constraints.
- Document Translator: document translation/publishing workflow constraints.

## Acceptance Criteria

1. CVF foundation remains the source of document-intelligence control surfaces.
2. Document Translator edits require fresh GC-018 baselines and source-verified
   work orders.
3. External code, dependencies, OCR, providers, corpus ingestion, and API-key
   use remain blocked until a later authorized tranche.
4. README/CLAUDE performance, cost, quality, and production claims are treated
   as source observations, not CVF evidence.
5. DT-CVF-T0 starts with source custody and control audit only.
6. Policy_Local remains independent and blocked behind its own PL-S lane.

## Verification / Evidence

Observed in this roadmap authoring pass:

- `git rev-parse HEAD` in external clone returned
  `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`.
- `git remote -v` in external clone returned
  `https://github.com/nclamvn/dich-tai-lieu`.
- `git status --short` in external clone reported `?? Thong_tin.md`.
- `git -c core.quotepath=false ls-files` in external clone counted `1140`
  tracked files.
- `README.md`, `CLAUDE.md`,
  `core/smart_extraction/document_analyzer.py`,
  `core/smart_extraction/extraction_router.py`, and
  `api/services/provider_router.py` were read for planning context.

## Governed Work Lifecycle

`INTAKE -> DESIGN -> SPEC -> WORK ORDER -> BUILD -> REVIEW -> FREEZE`

- INTAKE: operator selected Document Translator as a CVF-controlled use-case
  repo after EXA absorption.
- DESIGN: this roadmap keeps CVF foundation first and the app downstream.
- SPEC: DT-CVF-T0 must create the source custody and control audit.
- WORK ORDER: each tranche requires fresh GC-018 and source verification.
- BUILD: external repo edits begin only after DT-CVF-T1 authorization.
- REVIEW: Codex reviews worker returns before commits.
- FREEZE: readiness claims require committed artifacts and applicable gates.

## Claim Boundary

This roadmap authorizes only planning for a future CVF-controlled Document
Translator use-case lane. It does not prove external app correctness, document
translation quality, OCR quality, provider quality, cost savings, layout
preservation, dashboard accuracy, quota behavior, auth security, public
readiness, production readiness, release readiness, or CVF runtime governance
behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance planning for an external use-case repository; no
public-sync batch is authorized.
