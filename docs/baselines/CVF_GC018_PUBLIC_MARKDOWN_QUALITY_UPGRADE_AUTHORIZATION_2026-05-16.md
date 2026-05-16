# CVF GC-018 Public Markdown Quality Upgrade Authorization - 2026-05-16

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR PHASE 1 AUDIT AND TIER 1 REWRITE

## Purpose

Authorize a bounded documentation-only tranche to improve the public CVF
Markdown surface for first-impression quality, audience fit, and GC-045
structural completeness.

This authorization also marks new external knowledge intake as paused for this
tranche. CVF will focus on standardizing the existing public Markdown surface
before absorbing additional external knowledge.

## Scope

Authorized work:

- verify whether the public GitHub renewal roadmap already covers Markdown
  quality;
- create a Phase 1 audit of public Markdown files in `docs/`,
  `governance/toolkit/`, and the repo root;
- classify each in-scope Markdown file by audience and document role;
- select up to 15 Tier 1 files for first-impression rewrite;
- rewrite locked Tier 1 files only;
- preserve original claim boundaries and current evidence claims;
- record before/after measurements and a closure note.

The public GitHub renewal roadmap V2 covers repository split, public/provenance
surface control, and export posture. It mentions several public-front-door
documents, but it does not provide a dedicated Markdown quality audit,
GC-045-based compliance baseline, Tier 1 rewrite list, or measurement plan.
This tranche is therefore justified as a bounded companion tranche rather than
a duplicate of the renewal roadmap.

## Source

Predecessor evidence:

- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_PROPOSAL_2026-05-16.md`
- `docs/roadmaps/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_V2_2026-05-09.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`
- `governance/toolkit/05_OPERATION/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_GUARD.md`

## Out Of Scope

Hard out-of-scope:

- runtime, source code, tests, provider behavior, or governance enforcement code
  changes;
- new external knowledge absorption;
- `docs/baselines/` except this authorization packet;
- `docs/reviews/CVF_GC018_*_AUTHORIZATION_*.md`;
- `v1.0/` and `v1.1/` frozen baselines;
- FREEZE receipts;
- `AGENT_HANDOFF*.md`;
- `.private_reference/`;
- bulk rewrite of every Markdown file.

## Decision

Approved path:

`PHASE_1_AUDIT_PLUS_TIER_1_REWRITE_ONLY`

Tier 1 is capped at 15 files. Tier 2 requires a later explicit decision based
on Tier 1 measurement.

The operator has authorized Codex to proceed without intermediate stop points
inside this tranche and to present one final review packet after completion.
Codex must still preserve the GC-018 boundaries in this file and must not
expand scope silently.

## Acceptance Criteria

- Phase 1 audit exists at
  `docs/audits/CVF_PUBLIC_REPO_MARKDOWN_QUALITY_AUDIT_2026-05-16.md`.
- The audit classifies every in-scope Markdown file into `user-facing`,
  `agent context`, `audit trail`, or `internal working`.
- The audit records GC-045 status, GC-023 size status, audience fit, and
  last-touched date for each in-scope file.
- Tier 1 list contains no more than 15 files and excludes hard out-of-scope
  paths.
- Each Tier 1 rewrite is committed separately.
- Each rewritten Tier 1 file satisfies GC-045 structural completeness.
- GC-023 size status remains pass or explicitly documented if inherited.
- Measurement records before/after word counts for three representative Tier 1
  files.
- Closure note recommends either bounded Tier 2 or stop-at-Tier-1.

## Verification

Required local checks for this tranche:

```bash
git remote -v
git status -sb
git diff --check
```

Where the public repository does not include the provenance-only GC-045 checker,
the audit may use the canonical GC-045 standard from the provenance repository
as the baseline rubric and record that limitation explicitly.

## Claim Boundary

This authorization claims only that a bounded public Markdown quality tranche is
approved. It does not claim current public Markdown quality is high. It does not
authorize runtime changes, new governance enforcement code, new external
knowledge intake, or Tier 2 work.
