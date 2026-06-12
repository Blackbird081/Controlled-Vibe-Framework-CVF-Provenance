# CVF GC-018 - GC-051 Registry Authoring Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-12

Owner: Codex

## Purpose

Authorize a bounded GC-051 control-plane hardening batch that makes registry
updates safer for future agents.

## Authority Chain

Operator direction: "Dong y, nang nen CVF truoc di" after EXA-T2 review exposed
that the monolithic GC-051 registry JSON is easy for workers to edit
incorrectly.

Governance standards:

- `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`
- `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`
- `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`

## Objective

Reduce GC-051 registry authoring risk by making
`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` a generated aggregate
from reviewable per-entry source files.

## Decision / Baseline / Proposed Tranche

Decision: close this as a single bounded control-plane hardening tranche.

Baseline: before this batch, agents edited the GC-051 aggregate JSON directly.

Proposed tranche: add per-entry source files, generator, checker drift
validation, focused tests, and updated authoring instructions.

## Bounded Scope

Allowed:

- add per-entry source directory under `docs/corpus-intelligence/registry/`;
- add generator and focused unit tests;
- harden `check_corpus_scan_registry.py` with aggregate drift validation;
- update GC-051 standard, guard, human companion, and startup front-door rule.

Forbidden:

- change corpus registry semantics;
- delete or reclassify existing entries;
- mutate Policy_Local;
- run OCR/provider/API proof;
- change EC activation, retrieval, corpus ingestion, public-sync, readiness
  claims, memory reinjection, high-risk promotion, or autonomous mutation.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Current GC-051 aggregate exists | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | top-level object | `corpora` | GC-051 registry schema | ACCEPT |
| Current GC-051 checker exists | `governance/compat/check_corpus_scan_registry.py` | module constants and `main()` | `REGISTRY_PATH`, `_validate_entry`, `main` | GC-051 machine guard | ACCEPT |
| Current GC-051 standard exists | `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md` | Registry Location / Mandatory Agent Rules | `CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 standard | ACCEPT |
| Current GC-051 guard exists | `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md` | Machine Check / Enforcement Surface | `check_corpus_scan_registry.py` | GC-051 guard | ACCEPT |

## Closure Summary

This GC-018 closes in the same batch because the operator authorized Codex to
self-execute the foundation hardening. Completion evidence is recorded in:

`docs/reviews/CVF_GC051_REGISTRY_AUTHORING_HARDENING_COMPLETION_2026-06-12.md`

## Evidence / Verification

Required closure evidence:

- generator check PASS;
- GC-051 checker PASS;
- focused unit tests PASS;
- reviewer-fast PASS before closure.

## Claim Boundary

This proves authoring/control-plane hardening for GC-051 registry updates. It
does not prove semantic correctness of registry entries, full corpus coverage,
Policy_Local readiness, public readiness, production readiness, OCR/provider
behavior, or autonomous mutation.
