# CVF GC-018 Public Markdown Quality Upgrade Tier 3 Authorization - 2026-05-16

Memory class: SUMMARY_RECORD

Status: AUTHORIZED FOR TIER 3 REWRITE

## Purpose

Authorize a bounded documentation-only Tier 3 tranche to extend the public
Markdown quality upgrade to benchmark planning, methodology adjuncts, and
miscellaneous public reference files that the Tier 2 closure left out of
scope but that a post-Tier-2 audit identified as in-scope failures.

## Scope

Authorized work:

- rewrite at most 13 in-scope public Markdown files in the Tier 3 candidate
  list below;
- preserve every numeric claim, date, gate label, and policy ID verbatim;
- run the GC-045 checker with `--no-bootstrap --all-changed --enforce` on
  each commit;
- one commit per Tier 3 file in the public-sync workspace;
- record before/after word counts for three representative Tier 3 files;
- write a Tier 3 closure note;
- push public-sync changes to
  `github.com/Blackbird081/Controlled-Vibe-Framework-CVF`.

## Source

Predecessor evidence:

- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_PROPOSAL_2026-05-16.md`
- `docs/baselines/CVF_GC018_PUBLIC_MARKDOWN_QUALITY_UPGRADE_AUTHORIZATION_2026-05-16.md`
- `docs/audits/CVF_PUBLIC_REPO_MARKDOWN_QUALITY_AUDIT_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_CLOSURE_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_2_PROPOSAL_2026-05-16.md`
- `docs/baselines/CVF_GC018_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_2_AUTHORIZATION_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_2_CLOSURE_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_AMENDMENT_2026-05-16.md`

## Out Of Scope

Hard out-of-scope:

- runtime, source code, tests, provider behavior, or governance enforcement
  code changes;
- new external knowledge absorption (intake remains paused);
- `docs/baselines/` except this authorization packet;
- `docs/reviews/CVF_GC018_*_AUTHORIZATION_*.md`;
- `docs/reviews/CVF_GC018_TRACK_*` (EA track review records — audit chain);
- `v1.0/` and `v1.1/` frozen baselines;
- FREEZE receipts;
- `AGENT_HANDOFF*.md`;
- `.private_reference/`;
- QBS-N record files (qbs6, qbs7, qbs10, qbs12, qbs14-22, qbs33-40) — these
  are audit-trail-adjacent records of method-level remediation steps and are
  deferred to a possible Tier 4 if ever justified;
- preregistration files under `docs/benchmark/qbs-1/preregistrations/`;
- run records under `docs/benchmark/runs/`;
- reviewer plan files (`reviewer-plan.*`);
- `docs/EXPORT_MANIFEST.md` — has an active GC-023 size violation and
  requires a separate fix path, not a GC-045 rewrite.

## Decision

Approved path:

`TIER_3_REWRITE_BOUNDED_PUBLIC_BENCHMARK_AND_REFERENCE`

Tier 3 is capped at 13 files. Tier 4 requires a later explicit decision
based on Tier 3 outcome and any fresh user feedback.

Operator authorizes Codex to proceed without intermediate stop points and to
present one final closure packet after completion.

## Candidate List

| # | Path | Class |
| --: | --- | --- |
| 1 | `docs/benchmark/quality-benchmark-suite-claim-ladder.md` | benchmark methodology adjunct |
| 2 | `docs/benchmark/quality-benchmark-suite-standards-alignment.md` | benchmark methodology adjunct |
| 3 | `docs/benchmark/dlp/dlp-quality-baseline.md` | benchmark adjunct (DLP) |
| 4 | `docs/benchmark/governance-tax/governance-tax-fitness-function.md` | benchmark adjunct (governance-tax) |
| 5 | `docs/benchmark/qbs-1/corpus-candidate.md` | QBS-1 planning core |
| 6 | `docs/benchmark/qbs-1/runner-contract.md` | QBS-1 planning core |
| 7 | `docs/benchmark/qbs-1/scoring-rubric.md` | QBS-1 planning core |
| 8 | `docs/benchmark/qbs-1/artifact-layout.md` | QBS-1 planning core |
| 9 | `docs/benchmark/qbs-1/preregistration-template.md` | QBS-1 planning core |
| 10 | `docs/benchmark/qbs-1/scored-run-readiness.md` | QBS-1 planning core |
| 11 | `docs/benchmark/qbs-1/provider-routing-policy.md` | QBS-1 planning core |
| 12 | `docs/guides/CVF_DEMO_SCRIPT_2026-04-21.md` | guide (demo) |
| 13 | `docs/evidence/renewed-repo-release-gate-proof.md` | evidence (release-gate proof) |

## Acceptance Criteria

- Tier 3 rewrite list locked at the 13 files above.
- One commit per rewritten file in the public-sync workspace.
- Every rewritten file passes the GC-045 automated check
  (`--no-bootstrap --all-changed --enforce`).
- No claim drift: every numeric value, date, gate label, policy ID, and
  evidence anchor preserved verbatim.
- Measurement records before/after word counts for three representative
  Tier 3 files.
- Closure packet exists at
  `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_3_CLOSURE_2026-05-16.md`.
- Public push completed.

## Verification

Required local checks for this tranche:

```bash
git remote -v
git status -sb
git diff --check
python governance/compat/check_markdown_structural_completeness.py \
  --base origin/main --head HEAD --no-bootstrap --all-changed --enforce
```

## Claim Boundary

This authorization claims only that a bounded Tier 3 public Markdown quality
tranche over 13 specific files is approved. It does not authorize runtime
changes, new governance enforcement code, new external knowledge absorption,
or Tier 4 work. It does not claim Tier 3 output is high-quality before the
closure packet records measurement.
