# GC-018 — Catalog as First-Class Governed Artifact

Memory class: FULL_RECORD
Status: AUTHORIZED

## Purpose

Authorize and bound the work to elevate the public technical catalog
from a static orientation document to a first-class governed artifact
that accurately reflects CVF's current capability state to external
readers.

## Why This Is Needed

An external review written 2026-05-17 contained 3 factual errors about
CVF (CLI, benchmark, Skill/Provider/Memory foundations). Root cause
analysis confirmed the errors were not the reviewer's fault — CVF
delivered real capabilities but did not surface them in the public
catalog. Any future reviewer will make the same errors until the catalog
is fixed.

Reference: `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
Section: "Catalog Gap Remediation"

## Authorized Scope

Three catalog enrichments (R1/R2/R3) plus one enforcement addition (R4
already done in CLAUDE.md). All changes apply to the public-sync repo
only — no governance internals, no private process detail, no W-series
tranche names, no GC-018 packet references.

### R1 — Current Outcomes section

Add a "What CVF Can Do Today" section near the top of the catalog.
Format: 4–5 concrete outcomes, each one sentence + one verified
evidence path. Purpose: answer "what can CVF help me accomplish right
now?" for the first-time reader.

Public Filter Gate applied:
- No implementation detail (how it works internally)
- No W-series tranche names or commit SHAs
- No internal GC-018 or review packet references
- Every evidence path must exist in public-sync and pass Test-Path

### R2 — Extension Inventory table

Add a "Key Extensions" table listing 6–8 most important EXTENSIONS
modules. Columns: Extension name | What it does | Status. Purpose:
prevent "build from zero" misdiagnosis by showing the existing
foundation in plain language.

Public Filter Gate applied:
- Extension name and plain-language description only
- No internal test counts, line counts, or W-series attribution
- No roadmap state or private gap ledger references
- Status values: `active` | `proven` | `in development` only

### R3 — Delivery Narrative anchor

Add a short paragraph stating CVF's maturity level in public terms.
Purpose: prevent reviewers from assuming CVF is early-stage.

Public Filter Gate applied:
- Version number + GA date + high-level tranche count only
- No W-series tranche breakdown, no internal commit references
- No operator notes or internal decision log content

## Out of Scope

- Any change to governance internals (`docs/reviews/`, `docs/baselines/`,
  `AGENT_HANDOFF*.md`) — these stay internal only
- Any new public claim not backed by a verified evidence path
- Any over-claim beyond current `proven` status
- Any Codex involvement — this tranche is Claude-only to avoid
  information leakage into internal agent prompts

## Public Filter Gate (binding for all edits in this tranche)

Before adding any content to the public catalog, pass 3 questions:

1. If a competitor reads this, does CVF lose any advantage? If YES → cut.
2. Can an external reader understand CVF's value without knowing our
   internal process? If NO → rephrase to outcome, not process.
3. Does every linked path exist in the public-sync clone and pass
   Test-Path? If NO → do not link it.

## Scope / Target / Owner Boundary

In scope:

- Enriching the public technical catalog with R1/R2/R3 sections
- Adding a pre-commit advisory checker (GC-024) to the hook chain
- Adding a mandatory Tranche Closure Checklist to the GC-018 template

Out of scope:

- Any runtime implementation changes
- Any change to public claims beyond what is already evidenced
- Any promotion of internal governance artifacts to the public repo
- Lifting `system_reconvergence_stop` or changing GA posture

Owner: Claude (reviewer + implementer for this tranche; no Codex
involvement to prevent information leakage into agent prompts).

## Source / Predecessor Evidence

- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
  — root cause analysis and Catalog Gap Remediation section
- `CLAUDE.md` — GC-024 candidate binding rule (already added, commit `c7e32d75`)
- `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md` (public-sync)
  — target artifact for R1/R2/R3 enrichment

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED — doc-only changes to public-sync catalog and
provenance governance files. Zero active-path risk. Public Filter Gate
applied to every sentence added to public-facing content.

Baseline: public catalog before this tranche has "What CVF Is",
capability table, and claim boundary — but no outcomes section, no
extension inventory, and no delivery narrative. Any reader who opens
it cannot answer "what can CVF do for me today?"

Proposed tranche: CATALOG-R1R2R3-2026-05-18 — all three enrichments
plus pre-commit advisory and GC-018 closure template update in one batch.

## Acceptance Criteria

- [ ] R1: "What CVF Can Do Today" section present with 4–5 outcomes,
      each with verified public evidence path
- [ ] R2: "Key Extensions" table present with 6–8 rows, plain-language
      descriptions, no internal detail
- [ ] R3: Delivery narrative paragraph present, version + date + scale
      only
- [ ] All new paths pass Test-Path in public-sync clone before commit
- [ ] No internal governance paths, W-series names, or GC numbers in
      public-facing text
- [ ] GC-018 closure template updated with mandatory catalog checklist item
- [ ] Pre-commit advisory checker added to hook chain

## GC-018 Continuation Candidate

```text
GC-018 Continuation Candidate
- Candidate ID: GC-018-CATALOG-2026-05-18
- Date: 2026-05-18
- Parent roadmap / wave: CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md
- Proposed scope: Elevate public technical catalog to first-class governed
  artifact with Current Outcomes, Extension Inventory, Delivery Narrative,
  and enforcement (pre-commit advisory + GC-018 closure checklist)
- Continuation class: PACKAGING_ONLY
- Active quality assessment: docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md
- Assessment date: 2026-05-18
- Weighted total: 8.0/10
- Lowest dimension: Machine enforceability (1/2 — advisory only, not hard block)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: The catalog gap directly
  causes external misassessment of CVF's capability. Every day without
  R1/R2/R3, any new reviewer repeats the 3 factual errors. Risk of
  inaction exceeds risk of catalog update.
- Quality protection commitments: Public Filter Gate applied to every
  sentence; no internal process detail; Test-Path verification on all
  paths before commit; Claude-only (no Codex) to prevent info leakage
- Why now: Root cause analysis complete; filter rules defined; no
  implementation risk (doc-only changes to public-sync)
- Active-path impact: NONE
- Risk if deferred: Continued external misassessment of CVF capability
- Lateral alternative considered: YES — considered updating README only;
  rejected because catalog is the structured artifact with claim boundary
- Why not lateral shift: README is entry point, not the governed
  capability catalog; both will eventually need updating
- Real decision boundary improved: YES — external reviewers will have
  accurate capability picture
- Expected enforcement class: CI_REPO_GATE (advisory) + APPROVAL_CHECKPOINT
  (GC-018 closure checklist)
- Required evidence if approved:
  - Updated catalog with R1/R2/R3 sections, Test-Path 15+ PASS
  - GC-018 closure template with catalog checklist item
  - Pre-commit advisory script added to hook chain

Depth Audit
- Risk reduction: 2
- Decision value: 2
- Machine enforceability: 1
- Operational efficiency: 2
- Portfolio priority: 2
- Total: 9
- Decision: CONTINUE
- Reason: High decision value (prevents repeated external misassessment),
  zero active-path risk, doc-only changes, filter gate protects security

Authorization Boundary
- Authorized now: YES
- Next batch name: CATALOG-R1R2R3-2026-05-18
- If NO, reopen trigger: N/A
```

## Evidence / Verification

Test-Path verification run in public-sync clone on 2026-05-19 before commit.
All 15 paths referenced by new catalog sections pass:

```text
PASS  ARCHITECTURE.md
PASS  docs/benchmark
PASS  docs/evidence/latest-release-gate.md
PASS  docs/evidence/web-governance-path.md
PASS  docs/evidence/phase-e-governed-execution-chain.md
PASS  docs/evidence/current-cvf-quality-status.md
PASS  docs/evidence/cvf-16-5-runtime-absorption.md
PASS  docs/evidence/provider-lanes.md
PASS  docs/reference/CVF_MODULE_INVENTORY.md
PASS  scripts/run_cvf_release_gate_bundle.py
PASS  governance/toolkit/03_CONTROL/CVF_AGENT_REGISTRY.md
PASS  governance/toolkit/05_OPERATION/CVF_AGENT_HANDOFF_GUARD.md
PASS  governance/toolkit/05_OPERATION/CVF_MEMORY_GOVERNANCE_GUARD.md
PASS  docs/reference/archive/CVF_PUBLIC_NONCODER_VALUE_STATEMENT_2026-04-17.md
PASS  docs/reference/CVF_PUBLIC_STRUCTURE_OVERVIEW.md
```

Result: 15/15 PASS. No broken links introduced.

## Claim Boundary

This GC-018 authorizes catalog documentation changes only. It does not
authorize:

- Any runtime implementation
- Any change to public claims beyond what is already evidenced
- Any promotion of internal governance artifacts to the public repo
- Any change to GA_LOCAL_FIRST_APPROVED posture
- Any lifting of system_reconvergence_stop
