# CVF External Extraction Pattern Absorption Roadmap

Memory class: FULL_RECORD

Status: EXA_T1_DISPATCHED

docType: roadmap

Date: 2026-06-12

Owner: Codex

## Authorization / Decision

Decision: `EXTERNAL_EXTRACTION_PATTERN_ABSORPTION_BEFORE_POLICYLOCAL_USE_CASE`.

Operator identified `nclamvn/dich-tai-lieu` as a candidate external source for
CVF scan-layer learning. This roadmap absorbs reusable extraction-pattern
knowledge into CVF governance before opening Policy_Local use-case execution.

External source anchor:

- Repository: `https://github.com/nclamvn/dich-tai-lieu`
- Observed commit: `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`
- Local review clone: outside the CVF repo, temporary only

## Purpose

Evaluate external document extraction patterns that can improve CVF scan-layer
foundation without copying application code, importing dependencies, or
claiming third-party production behavior.

The target learning is generic:

- extraction strategy routing;
- page/document analysis signals;
- extraction quality scoring;
- retry or escalation recommendations;
- language/script-aware OCR routing.

## Scope / Target / Owner Boundary

In scope:

- source-map the pinned external repository areas relevant to extraction;
- classify each observed pattern as `ACCEPT`, `DEFER`, or `REJECT`;
- translate accepted ideas into CVF-owned scan-layer contract candidates;
- preserve CVF claim boundaries and operator-visible reporting.

Out of scope:

- copying third-party code into CVF;
- installing OCR, PyMuPDF, PaddleOCR, MathPix, or provider dependencies;
- running provider/API-key calls;
- mutating Policy_Local;
- corpus ingestion, retrieval, EC activation, or T12 unlock;
- public-sync, production readiness, public readiness, or performance claims.

## Non-Goals

This roadmap does not:

- evaluate `dich-tai-lieu` as a product;
- verify its README production, cost, speed, or accuracy claims;
- migrate its translation, publishing, glossary, or UI surfaces;
- add a provider fallback path to CVF;
- authorize automatic Vision/OCR execution.

## Authority Chain

| Authority | Path or source | Disposition |
| --- | --- | --- |
| Operator direction | 2026-06-12 chat direction | ACCEPT |
| RDA foundation closure | `docs/reviews/CVF_MEOR_RDA_T4_FOUNDATION_CLOSURE_AND_POLICYLOCAL_SUCCESSOR_COMPLETION_2026-06-12.md` | ACCEPT |
| Policy_Local successor roadmap | `docs/roadmaps/CVF_POLICYLOCAL_SUCCESSOR_PILOT_ROADMAP_2026-06-12.md` | ACCEPT_AS_DOWNSTREAM |
| External repo | `https://github.com/nclamvn/dich-tai-lieu` at `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336` | ACCEPT_AS_REVIEW_SOURCE |

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

1. Absorb patterns before Policy_Local execution.
2. Treat external code as source evidence only, not implementation to copy.
3. Keep accepted value in CVF-owned contracts and reports.
4. Separate deterministic local scan signals from provider-assisted extraction.
5. Require operator-visible escalation for low-quality extraction.

Rejected design:

- direct code import;
- dependency installation;
- provider fallback by default;
- external production claim adoption;
- Policy_Local mutation during absorption.

## Work Plan

1. Dispatch EXA-T1 to Claude as `WORKER_MUST_NOT_COMMIT`.
2. Require a pinned external-repo source map and corpus completeness block.
3. Require pattern disposition for extraction router, document analysis,
   extraction quality score, feedback loop, and OCR language support.
4. Require CVF contract candidate recommendations.
5. Return uncommitted artifacts for Codex review before any closure.

## Tranche Plan

| Tranche | Deliverable | Dependency | Status |
| --- | --- | --- | --- |
| EXA-T1 | External extraction pattern source map and absorption decision | RDA-T4 closure `dba15ca7` | DISPATCHED |
| EXA-T2 | CVF scan strategy decision contract, if EXA-T1 accepts patterns | EXA-T1 closure | HOLD_PENDING_EXA_T1 |
| PL-S1 | Policy_Local evidence-resolution pilot | EXA-T1 closure plus fresh authorization | HOLD_PENDING_EXA_T1 |

## Dispatch Boundary

EXA-T1 may only read the pinned external repository and create governed
analysis artifacts under `docs/reference/` and `docs/reviews/`.

EXA-T1 must not:

- alter CVF runtime/source code;
- alter external Policy_Local files;
- install or run OCR/provider dependencies;
- import third-party code;
- call provider APIs or use keys;
- claim performance, accuracy, production, public, or Policy_Local readiness.

## Acceptance Criteria

1. External repository source facts are pinned to commit
   `92c5aeb3b4886b6d5a14ea4682dc5e4e1bc1a336`.
2. Every accepted pattern cites source file and line or section evidence.
3. Each pattern receives `ACCEPT`, `DEFER`, or `REJECT`.
4. Accepted patterns are restated as CVF-owned scan-layer candidates.
5. Provider-assisted or dependency-heavy patterns are deferred or bounded.
6. No code import, dependency install, provider call, or Policy_Local mutation
   occurs.

## Verification / Evidence

Required EXA-T1 evidence:

- `git rev-parse HEAD` from the external clone;
- `git remote -v` for the external clone;
- file inventory for the bounded source set;
- source-verification table;
- blind-spot control block;
- pattern disposition matrix;
- claim boundary and public export disposition.

## Governed Work Lifecycle

`INTAKE -> DESIGN -> SPEC -> WORK ORDER -> BUILD -> REVIEW -> FREEZE`

- INTAKE: operator identifies external repo as scan-layer learning candidate.
- DESIGN: this roadmap limits the work to pattern absorption.
- SPEC: EXA-T1 defines source map and disposition criteria.
- WORK ORDER: Claude receives a source-verified no-commit packet.
- BUILD: worker creates analysis artifacts only.
- REVIEW: Codex reviews before any closure.
- FREEZE: accepted patterns can open EXA-T2 only after closure.

## Claim Boundary

This roadmap authorizes only external pattern absorption for CVF scan-layer
foundation. It does not prove third-party product quality, extraction accuracy,
OCR readiness, provider behavior, Policy_Local readiness, EC activation,
retrieval quality, production readiness, public readiness, or autonomous
mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private external-source absorption planning; no public-sync authorized.
