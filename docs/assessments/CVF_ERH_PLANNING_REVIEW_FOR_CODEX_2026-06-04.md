# CVF ERH Planning Review For Codex Rebuttal

Memory class: FULL_RECORD

Status: DRAFT_CODEX_REBUTTAL_RECORDED

docType: planning_review

Date: 2026-06-04

baseHead: `54d4867c`

Source intake:
`docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md`

Codex response:
`docs/reviews/CVF_ERH_PLANNING_REVIEW_CODEX_RESPONSE_2026-06-04.md`

## Purpose

This document presents the proposed ERH (External Review Hardening) execution
plan for Codex review and rebuttal before a formal ERH roadmap is authored.
Codex must confirm, challenge, or refine each decision below before dispatch.

Operator decisions already locked:
- ERH-F1/F5/F7 (evidence durability, rate limit, policySnapshotId): bound claim
  in docs first; no runtime fix this batch.
- Next-lane decision (LPCI search vs legacy scan) deferred until ERH complete.

## Scope / Target / Owner Boundary

Target: ERH planning decisions before formal roadmap authoring.

Owner boundary: this file records planning questions and proposed sequencing
for Codex rebuttal. It does not authorize public-sync, runtime implementation,
live proof, or closure of ERH findings.

## Source / Predecessor Evidence

| Source | Purpose | Disposition |
| --- | --- | --- |
| `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_INTAKE_2026-06-03.md` | archived ERH findings intake | ACCEPT |
| `docs/assessments/archive/CVF_EXTERNAL_PUBLIC_REPO_REVIEW_SOURCE_2026-06-03.docx` | external public-repo review source | ACCEPT |
| `docs/reviews/CVF_ERH_PLANNING_REVIEW_CODEX_RESPONSE_2026-06-04.md` | Codex rebuttal response | RECORDED |

## Decision / Baseline / Proposed Tranche

Decision: use this file and the Codex response as planning inputs only.

Proposed baseline: formal ERH roadmap authoring must use fresh current paths,
fresh baseHead, and gate evidence. The archived 2026-06-03 intake remains
evidence, but absent roadmap/work-order links must not be treated as live
dispatch packets.

## Evidence / Verification

| Check | Result |
| --- | --- |
| `Test-Path docs/assessments/CVF_ERH_PLANNING_REVIEW_FOR_CODEX_2026-06-04.md` | PASS |
| `python governance/compat/check_corpus_scan_registry.py --base b5cf8882 --head HEAD --enforce` | PASS: 11 corpora, 0 violations |
| `python governance/compat/check_markdown_structural_completeness.py --base b5cf8882 --head HEAD --all-changed --enforce` | initially failed for this file before these GC-045 sections were added |

## Section 1 — Blocker Pre-Conditions

Before any ERH tranche can dispatch, two pre-existing autorun gate blockers must
be resolved. These are outside ERH scope but must be cleared first.

### Blocker B1 — Structural violation

File: `docs/reviews/CVF_REAL_NONCODER_USAGE_TEST_OPERATOR_SAMPLE_2026-05-25.md`

Current issue: file contains unchecked `- [ ]` checklist items (lines 67-70) and
`Status: READY_FOR_OPERATOR_REVIEW` with no reviewer pass/hold/blocked answer.
The Closure Finality Gate requires closed-equivalent artifacts not to retain
unchecked checklist items.

Operator clarification on 2026-06-04:

- CVF currently has no active public usage-sample surface.
- If a web-facing landing page later uses a usage sample, it is mock data for
  non-coder attraction/orientation only.
- Such mock usage content is not governance evidence, an operator usability
  gate, or a public GitHub assessment artifact.
- ERH is focused on public GitHub structure, README/catalog boundary, and how
  an external agent evaluates CVF from the public repository.
- Therefore this file should not be treated as an active usability gate,
  public evidence, or ERH prerequisite. If it becomes visible in a changed
  range, retire it as local scratch/out-of-scope instead of asking for PASS.

Proposed fix:
- Treat the file as retired local scratch, not a current GitHub/public evidence
  artifact.
- Do not mark it `PASS`.
- Do not add a checker suppression just to keep it active.
- If it must be kept, move/archive it with an explicit
  `RETIRED_NOT_GITHUB_PUBLIC_EVIDENCE` boundary and no public claim.

Codex question: Which option is correct per the structural checker rule? Is
Option B allowed, or must all `- [ ]` items in any governed markdown be
resolved before gate passes?

### Blocker B2 — Corpus scan registry missing fields

File: `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`

Current issue: `check_corpus_scan_registry.py` reports missing required fields
for the `GOVERNANCE_PILOT_NO_LEGAL_CORPUS` entry.

Proposed fix: add the missing required fields to that registry entry. The exact
required schema is defined in
`docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`.

Codex question: Are there other registry entries with the same missing-field
violation, or only this one? Should this be fixed as a standalone Fast Lane
patch before ERH dispatch?

## Section 2 — Proposed ERH Tranche Map

### ERH-T1 — Public Claim Calibration (Docs Only)

Scope: calibrate public README/catalog claims based on ERH findings. No runtime
changes.

Findings addressed: ERH-F10, ERH-F11, ERH-F2, ERH-F6, ERH-F8.

Proposed deliverables:
1. Public README evaluation boundary section (what CVF is/is not, current
   snapshot vs private provenance, evidence status).
2. Update catalog claim: distinguish web control-plane event store, guard-contract
   SQLite wrapper, and export signing posture clearly.
3. Carry F-1 closed-not-met statement into public docs explicitly.
4. Calibrate safety filter claim: regex/pattern-based, not ML-based DLP.
5. Benchmark live emission: do not claim until `liveEmissionWired=true`.

Authorization class: Fast Lane eligible (R0, docs only, public-sync tranche).

Codex question: Is this appropriately scoped as a single Fast Lane tranche, or
should ERH-F11 (evaluation guide) be a separate tranche because it requires more
authoring depth?

### ERH-T2 — Route Coverage And CI Hardening (Governance Evidence)

Scope: create route governance coverage ledger and plan CI hardening gates.

Findings addressed: ERH-F3, ERH-F4.

Proposed deliverables for ERH-T2a (Route Coverage Ledger):
1. Route governance coverage ledger: classify all 68 API route files as
   governed / admin-auth-informational / exempt / missing-proof.
2. Ledger format: markdown table with route path, governance status, evidence
   reference or gap disposition.
3. No checker implementation in this tranche — ledger only; checker is a
   separate CI2-style tranche after ledger stabilizes.

Proposed deliverables for ERH-T2b (CI Hardening Plan):
1. Audit current `cvf-ci.yml` gates against public production-readiness
   implication.
2. Document which gates are missing (lint, coverage threshold, dep audit,
   public-doc drift) and assign each a priority.
3. Author a CI hardening work order if operator approves scope.

Codex question: Should ERH-T2a and ERH-T2b be one tranche or two? Route ledger
is read-only analysis; CI hardening plan may involve `.github/workflows/` edits
which are higher risk.

### ERH-T3 — Evidence Durability Claim Boundary (Docs Only — No Runtime Fix)

Scope: bound the claim for evidence durability in public docs per operator
decision. No architecture change in this batch.

Findings addressed: ERH-F1 (primary), ERH-F5 (secondary), ERH-F7 (secondary).

Proposed deliverables:
1. Public docs section explicitly describing current evidence tiers:
   - Tier 1: in-memory / tmp JSON (web control-plane events, default path)
   - Tier 2: optional signing gate (`CVF_AUDIT_SIGNING_KEY`)
   - Tier 3: guard-contract SQLite wrapper (guard-contract audit storage)
2. In-memory rate limit: explicitly note local-only posture, no distributed
   guarantee.
3. `policySnapshotId`: explicitly note process-lifetime style, not a persisted
   policy version; document the gap and roadmap a future improvement.

Authorization class: Fast Lane eligible (R0, docs only).

Codex question: Is `policySnapshotId` scoped correctly as docs-only here, or is
there a minimal runtime fix (e.g., persist the active policy hash) that could be
done in the same batch without touching governed routes?

### ERH-T4 — Dependency Decision (next-auth beta)

Scope: make a governed decision on the `next-auth` beta dependency.

Finding addressed: ERH-F9.

Proposed deliverables:
1. Document the three options: accept beta for current scope, migrate to stable,
   add public caveat only.
2. Record the operator decision as a governed baseline.
3. If migrating: open a separate implementation tranche; do not do it in T4.

Authorization class: GC-018 baseline decision record, no implementation.

Codex question: Is T4 premature before T1-T3 close? Should it be held until T3
confirms production-readiness posture?

## Section 3 — Sequencing Constraints

Proposed order: B1 retirement note + B2 verification → ERH-T1 → ERH-T2a →
ERH-T2b → ERH-T3 → ERH-T4.

ERH-T2b (CI hardening work) gates on ERH-T2a (ledger), because CI hardening
claims must reference the ledger to prove route coverage improvement.

ERH-T3 can start in parallel with ERH-T2a/b if operator approves; it is
docs-only and does not depend on the ledger.

ERH-T4 should be held until T3 is closed, because the production-readiness
posture decision in T3 informs whether beta-dependency risk is acceptable
for the current scope.

## Section 4 — Open Questions For Codex

1. **Blocker B1 resolution**: confirm retired/out-of-scope disposition rather
   than PASS or suppression.
2. **Blocker B2 scope**: Only `GOVERNANCE_PILOT_NO_LEGAL_CORPUS`, or broader?
3. **ERH-T1 split**: Single Fast Lane or separate F-11 tranche?
4. **ERH-T2 split**: One tranche or two (ledger vs CI plan)?
5. **ERH-T3 policySnapshotId**: Docs-only correct, or minimal runtime fix
   allowed in same tranche?
6. **ERH-T4 timing**: Start after T3, or can it run in parallel?
7. **Dangling links in intake**: Should the ERH intake be updated now to change
   `docs/roadmaps/CVF_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-03.md` and
   `docs/work_orders/CVF_WO_EXTERNAL_REVIEW_HARDENING_FOUNDATION_2026-06-03.md`
   from dangling links to `PENDING_AUTHORING` placeholders?

## Claim Boundary

This document records a proposed plan for operator and Codex review. It does not
implement any ERH tranche, does not modify the pre-existing blockers, does not
touch public-sync, and does not claim any governance control as resolved.
