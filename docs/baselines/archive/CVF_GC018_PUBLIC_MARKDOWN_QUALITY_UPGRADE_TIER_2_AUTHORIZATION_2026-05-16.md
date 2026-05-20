# CVF GC-018 Public Markdown Quality Upgrade Tier 2 Authorization - 2026-05-16

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR TIER 2 REWRITE

## Purpose

Authorize a bounded documentation-only Tier 2 tranche to extend the public
Markdown quality upgrade beyond the Tier 1 first-impression set. This
authorization continues the public Markdown quality program approved under the
Tier 1 GC-018 packet and constrained by the Tier 2 proposal.

## Scope

Authorized work:

- copy the GC-045 enforcement stack (checker + standard + guard) into the
  public-sync workspace as the Tier 2 automation prerequisite;
- record the Tier 1 read-test status (operator-skip-approved for this tranche);
- rewrite at most 10 evidence-and-benchmark entry-point files listed in the
  Tier 2 proposal;
- preserve every numeric claim, date, and gate label verbatim during rewrite;
- record before/after measurements;
- write a Tier 2 closure note;
- push public-sync changes to `github.com/Blackbird081/Controlled-Vibe-Framework-CVF`.

## Source

Predecessor evidence:

- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_PROPOSAL_2026-05-16.md`
- `docs/baselines/CVF_GC018_PUBLIC_MARKDOWN_QUALITY_UPGRADE_AUTHORIZATION_2026-05-16.md`
- `docs/audits/CVF_PUBLIC_REPO_MARKDOWN_QUALITY_AUDIT_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_CLOSURE_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_2_PROPOSAL_2026-05-16.md`
- Public commits `edd7d70`..`1e94439` (Tier 1 bilingual diacritics amendment)

## Out Of Scope

Hard out-of-scope:

- runtime, source code, tests, provider behavior, or governance enforcement
  code changes beyond the single GC-045 checker stack copy described above;
- new external knowledge absorption (intake remains paused);
- audit-trail files including `docs/benchmark/runs/*/`, `docs/benchmark/qbs-1/r*-*`,
  preregistrations, and reviewer plans, even when they appear under
  candidate path globs;
- `docs/baselines/` except this authorization packet;
- `docs/reviews/CVF_GC018_*_AUTHORIZATION_*.md`;
- `v1.0/` and `v1.1/` frozen baselines;
- FREEZE receipts;
- `AGENT_HANDOFF*.md`;
- `.private_reference/`;
- Tier 3 work.

## Decision

Approved path:

`TIER_2_REWRITE_WITH_PUBLIC_SYNC_GC045_INSTALL`

Tier 2 is capped at 10 files. Tier 3 requires a later explicit decision.

The operator has authorized:

- proceed without intermediate stop points inside this tranche and present
  one final closure packet after completion;
- skip external Tier 1 read-test for this tranche. Closure must record the
  Tier 1 read-test status explicitly as `operator-skip-approved` so the audit
  chain remains honest.

## Acceptance Criteria

- GC-045 checker stack copied into public-sync and shown to run successfully.
- Tier 1 read-test note recorded with operator-skip status in the Tier 2
  closure packet.
- Tier 2 rewrite list locked at no more than 10 files from the candidate pool
  in the Tier 2 proposal.
- One commit per rewritten file in the public-sync workspace.
- Every rewritten file passes the GC-045 automated check.
- Every rewritten file passes the public-surface scanner.
- No claim drift: every numeric claim, date, and gate label preserved verbatim.
- Measurement records before/after word counts for three representative Tier 2
  files.
- Closure packet exists at
  `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_2_CLOSURE_2026-05-16.md`.
- Public push completed.

## Verification

Required local checks for this tranche:

```bash
git remote -v
git status -sb
git diff --check
python governance/compat/check_markdown_structural_completeness.py \
  --base origin/main --head HEAD --all-changed --enforce
python scripts/check_public_surface.py
```

## Claim Boundary

This authorization claims only that a bounded Tier 2 public Markdown quality
tranche is approved. It does not authorize runtime changes, new governance
enforcement code beyond the single GC-045 checker stack copy, new external
knowledge absorption, or Tier 3 work. It does not claim Tier 2 output is
high-quality before the closure packet records measurement.
