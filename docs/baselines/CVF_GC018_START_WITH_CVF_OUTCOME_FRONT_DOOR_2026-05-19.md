# GC-018 Authorization — START_WITH_CVF.md: Outcome Front Door

Memory class: SUMMARY_RECORD

Status: AUTHORIZED — 2026-05-19

## Purpose

Authorize a bounded public-sync documentation tranche that introduces an
outcome-first `START_WITH_CVF.md` front door without adding new capability
claims or changing the internal provenance repository.

## Source / Predecessor Evidence

- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
  line 379–383: recommends `docs/START_WITH_CVF.md` or updated README
  section leading with outcome capability before governance architecture;
  deferred from assessment baseline; requires separate GC-018
- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
  line 571: risk row — "Public-sync surface continues to understate CVF
  capability — Deferred: START_WITH_CVF.md or README outcome section —
  requires separate GC-018"
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (public-
  sync) — R1 section "What CVF Can Do Today" contains 5 proven outcomes;
  these are the canonical source for `START_WITH_CVF.md` content

## Decision / Baseline / Proposed Tranche

**What is authorized:**

Create `docs/START_WITH_CVF.md` in the **public-sync repo only**
(`Controlled-Vibe-Framework-CVF-public-sync/docs/START_WITH_CVF.md`).
This file answers "What can I do with CVF today?" in outcome-first
language before governance architecture.

**Format:**
- 3–4 concrete outcomes drawn from the R1 catalog section (verified
  evidence paths already in public-sync)
- Brief "How to start" pointer (3 steps max) pointing to existing
  public docs
- Architecture depth deferred to `ARCHITECTURE.md` and the catalog

**What is NOT authorized:**
- Adding new capability claims not already in the R1 catalog
- Creating `START_WITH_CVF.md` in the governance repo (internal repo;
  this file belongs in public-sync only)
- Modifying `README.md` in this tranche (separate GC-018 if needed)
- Adding new evidence packets (no new proofs in this tranche)

**Risk: R0** — documentation only; no code, no runtime, no new claims.

**Implementer:** Claude (coordinating agent, not Codex — documentation
work per session rule: "Phần này giao cho bạn xử lý, không bàn giao
codex, tránh lệch thông tin").

**Write ownership:**
```
Controlled-Vibe-Framework-CVF-public-sync/docs/START_WITH_CVF.md  (NEW)
```

**Forbidden:**
```
README.md                    (separate tranche)
docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md  (do not modify)
governance repo (internal)   (no START_WITH_CVF.md here)
```

## Evidence / Verification

Pre-write verification (run from public-sync clone):

```powershell
Test-Path "docs/START_WITH_CVF.md"   # must be False before writing
Test-Path "docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md"  # True
Test-Path "docs/evidence/phase-e-governed-execution-chain.md"  # True
```

Post-write verification:

```powershell
Test-Path "docs/START_WITH_CVF.md"   # True after write
(Get-Content "docs/START_WITH_CVF.md").Count  # must be < 200 lines (GC-023)
```

## Acceptance Criteria

- [ ] `docs/START_WITH_CVF.md` exists in public-sync repo
- [ ] File is under 200 lines
- [ ] Leads with 3–4 concrete outcomes, each with a verified evidence
      link that resolves in the public-sync clone
- [ ] No new capability claims beyond the R1 catalog section
- [ ] No references to internal governance paths, W-series names, or
      GC numbers
- [ ] Links to `ARCHITECTURE.md` or catalog for architecture depth
- [ ] Passes `Test-Path` verification on every linked file from public-sync root

## Tranche Closure Checklist

- [ ] GC-018 filed and self-referenced
- [ ] `START_WITH_CVF.md` created in public-sync
- [ ] All acceptance criteria PASS
- [ ] `Test-Path` on all internal links — verified from public-sync clone
- [ ] No internal governance artifacts in the file content
- [ ] GC-020 handoff updated with new HEAD SHA

## Claim Boundary

This authorization covers public-sync documentation only. It does not authorize
new runtime behavior, new evidence claims, provenance-repo publication, or
README changes.
