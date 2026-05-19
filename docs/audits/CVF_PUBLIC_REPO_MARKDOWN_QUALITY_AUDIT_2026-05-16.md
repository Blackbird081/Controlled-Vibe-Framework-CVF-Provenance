# CVF Public Repo Markdown Quality Audit - 2026-05-16

Memory class: FULL_RECORD

Status: PHASE 1 AUDIT COMPLETE - TIER 1 LIST SELECTED

## Purpose

Audit the public CVF repository Markdown surface before Tier 1 rewrite. The
goal is not to standardize every Markdown file. The goal is to identify the
small set of public files that most strongly shapes first impression,
onboarding clarity, and LLM/agent readability.

## Scope

In-scope paths:

- repo-root `*.md`
- `docs/**/*.md`
- `governance/toolkit/**/*.md`

Hard out-of-scope:

- `docs/baselines/` except the tranche authorization packet
- `docs/reviews/CVF_GC018_*_AUTHORIZATION_*.md`
- `v1.0/` and `v1.1/`
- FREEZE receipts
- `AGENT_HANDOFF*.md`
- `.private_reference/`

`governance/toolkit/` does not exist in the public-sync repository at audit
time.

## Source

Primary source repository:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Proposal source:

`docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_PROPOSAL_2026-05-16.md`

Public renewal roadmap checked:

`docs/roadmaps/archive/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_V2_2026-05-09.md`

## Methodology

Repository audited:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Local workspace:

`d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`

Commands and sources:

```bash
git remote -v
git status -sb
rg --files -g "*.md" docs governance/toolkit .
git log -1 --format=%cs -- <path>
```

The proposal requested:

```bash
python governance/compat/check_markdown_structural_completeness.py --base origin/main --head HEAD --all-changed --json
```

The public-sync repository does not currently include the provenance-only
GC-045 checker. This audit therefore uses the canonical GC-045 rubric from the
provenance repository checker and records the limitation explicitly. No runtime,
source code, or governance enforcement code was changed for this audit.

## Requirements

- Classify every in-scope public Markdown file.
- Exclude hard out-of-scope paths from Tier 1 selection.
- Select no more than 15 Tier 1 files.
- Preserve claim boundaries during rewrite.
- Measure representative before/after word counts.
- Capture before/after GitHub Files-view screenshots.

## Findings

Summary:

| Metric | Result |
| --- | --- |
| In-scope Markdown files audited | 121 |
| `user-facing` | 12 |
| `agent context` | 24 |
| `audit trail` | 84 |
| `internal working` | 1 |
| GC-045 pass | 0 |
| GC-045 fail | 121 |
| GC-023 pass | 120 |
| GC-023 violation | 1 (`docs/EXPORT_MANIFEST.md`) |

Interpretation:

- The public repo is readable but not structurally standardized under GC-045.
- Most files are audit trail or benchmark artifacts and should not be rewritten
  in Tier 1.
- First-impression value is concentrated in the repo root, `docs/guides/`, and
  a few curated evidence files.
- The existing public GitHub renewal roadmap addresses public/provenance split
  and export posture, but not a measured Markdown quality rewrite.

## Tier 1 Selection

Tier 1 is capped at 15 files. Selection prioritizes files a new user, evaluator,
developer, or LLM is likely to open in the first five minutes.

| File | Audience | Language | Rationale |
| --- | --- | --- | --- |
| `README.md` | non-coder + evaluator | VN+EN bilingual | Primary public front door and first trust signal. |
| `docs/guides/minimum-useful-cvf.md` | non-coder | VN+EN bilingual | Fastest practical "what can I do now?" guide. |
| `docs/guides/local-first-deployment-baseline.md` | non-coder + operator | VN+EN bilingual | Current local-first deployment path and cost/trust boundary. |
| `ARCHITECTURE.md` | coder/dev | EN-only | Core technical evaluation file. |
| `GOVERNANCE.md` | coder/dev + evaluator | EN-only | Explains CVF's central governance claim. |
| `PROVIDERS.md` | coder/dev | EN-only | Provider boundary and key-handling expectations. |
| `COST_AND_QUOTA.md` | operator + coder/dev | VN+EN bilingual | Practical adoption blocker; cost clarity matters early. |
| `PROVENANCE.md` | evaluator + auditor | EN-only | Public/provenance split and audit access boundary. |
| `CONTRIBUTING.md` | coder/dev | EN-only | External contributor path. |
| `CONTRIBUTORS.md` | public evaluator | EN-only | Attribution and ownership clarity. |
| `SECURITY.md` | security-minded evaluator | EN-only | Responsible disclosure and safety posture. |
| `docs/evidence/README.md` | evaluator + LLM/agent | EN-only | Evidence navigation entry point. |
| `docs/evidence/current-cvf-quality-status.md` | evaluator + non-coder | VN+EN bilingual | Current quality truth is a first-impression trust file. |
| `docs/evidence/claim-boundaries.md` | evaluator + LLM/agent | EN-only | Prevents overclaiming and helps agents parse limits. |
| `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md` | evaluator + LLM/agent | EN-only | Known limitations are high-trust public evidence. |

## Tier 2 Candidates

These are useful but lower first-impression priority than Tier 1:

- `docs/evidence/latest-release-gate.md`
- `docs/evidence/local-first-release-gate-proof-2026-05-16.md`
- `docs/evidence/provider-lanes.md`
- `docs/evidence/redaction-and-key-safety.md`
- `docs/evidence/web-governance-path.md`
- `docs/reference/CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md`
- `docs/reference/CVF_AUDIT_RECEIPT_INTEGRITY_MODEL.md`
- `docs/benchmark/README.md`
- `docs/benchmark/quality-benchmark-suite-methodology.md`
- `docs/benchmark/qbs-1/README.md`

## Inventory

Legend:

- GC-045: `PASS` or `FAIL`
- GC-023: `PASS`, `ADVISORY`, or `VIOLATION`

| Path | Class | GC-045 | GC-023 | Audience fit | Last touched |
| --- | --- | --- | --- | --- | --- |
| `ARCHITECTURE.md` | user-facing | FAIL | PASS | High first-impression root file. | 2026-05-09 |
| `CONTRIBUTING.md` | user-facing | FAIL | PASS | High first-impression root file. | 2026-05-09 |
| `CONTRIBUTORS.md` | user-facing | FAIL | PASS | High first-impression root file. | 2026-05-09 |
| `COST_AND_QUOTA.md` | user-facing | FAIL | PASS | High first-impression root file. | 2026-05-09 |
| `GOVERNANCE.md` | user-facing | FAIL | PASS | High first-impression root file. | 2026-05-09 |
| `PROVENANCE.md` | user-facing | FAIL | PASS | High first-impression root file. | 2026-05-09 |
| `PROVIDERS.md` | user-facing | FAIL | PASS | High first-impression root file. | 2026-05-09 |
| `README.md` | user-facing | FAIL | PASS | Primary public front door. | 2026-05-16 |
| `SECURITY.md` | user-facing | FAIL | PASS | High first-impression root file. | 2026-05-09 |
| `docs/EXPORT_MANIFEST.md` | internal working | FAIL | VIOLATION | Low rewrite fit; manifest is not Tier 1. | 2026-05-09 |
| `docs/benchmark/README.md` | agent context | FAIL | PASS | Medium reference impact; Tier 2 candidate. | 2026-05-12 |
| `docs/benchmark/dlp/dlp-quality-baseline.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-13 |
| `docs/benchmark/governance-tax/governance-tax-fitness-function.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-13 |
| `docs/benchmark/qbs-1/README.md` | agent context | FAIL | PASS | Medium reference impact; Tier 2 candidate. | 2026-05-12 |
| `docs/benchmark/qbs-1/artifact-layout.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-09 |
| `docs/benchmark/qbs-1/corpus-candidate.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-09 |
| `docs/benchmark/qbs-1/hard-gate-remediation-qbs6.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/preregistration-template.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-09 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba-r2.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba-r3.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba-r4.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba-r5.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba-r6.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba-r7.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba-r8.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260511-alibaba-r9.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260512-alibaba-r10.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-12 |
| `docs/benchmark/qbs-1/provider-routing-policy.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-13 |
| `docs/benchmark/qbs-1/qbs33-rework-decoupling.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/qbs34-reviewer-completeness-retry.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/qbs35-live-run-preflight.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/qbs38-runtime-governance-family-mapper.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/qbs39-family-conditional-allow-output-contract.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/qbs40-r10-checkpoint-and-preregistration.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-12 |
| `docs/benchmark/qbs-1/quality-delta-root-cause-qbs10.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/r10-post-score-analysis-qbs41.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-12 |
| `docs/benchmark/qbs-1/r8-post-score-analysis-qbs21.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-anchor-adjudication-qbs27.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-anchor-adjudication-qbs36.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-calibration-agreement-qbs29.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-calibration-agreement-qbs37.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-calibration-agreement-rerun-qbs32.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-calibration-anchors-qbs26.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-calibration-failure-analysis-qbs30.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-calibration-reference-qbs28.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-calibration-reference-qbs36.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-post-score-analysis-qbs25.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-preregistration-qbs23.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/r9-reviewer-rubric-remediation-qbs31.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/rerun-plan-qbs7.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-anchor-adjudication-qbs16.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-calibration-agreement-qbs17.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-calibration-anchors-qbs15.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-calibration-cleanup-and-rerun-qbs18.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-calibration-plan-qbs14.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-disagreement-remediation-qbs12.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba-r2.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba-r3.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba-r4.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba-r5.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba-r6.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba-r7.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba-r8.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260511-alibaba-r9.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260512-alibaba-r10.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-12 |
| `docs/benchmark/qbs-1/reviewer-rework-rubric-normalization-qbs18.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/reviewer-rubric-addendum-qbs16.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/qbs-1/runner-contract.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-10 |
| `docs/benchmark/qbs-1/scored-run-readiness.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-10 |
| `docs/benchmark/qbs-1/scorer-completeness-and-allow-quality-remediation-qbs22.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/qbs-1/scoring-rubric.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-09 |
| `docs/benchmark/quality-benchmark-suite-claim-ladder.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-09 |
| `docs/benchmark/quality-benchmark-suite-methodology.md` | agent context | FAIL | PASS | Medium reference impact; Tier 2 candidate. | 2026-05-09 |
| `docs/benchmark/quality-benchmark-suite-standards-alignment.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact. | 2026-05-09 |
| `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/README.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-09 |
| `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/claim-statement.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-09 |
| `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/limitations.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-09 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba/README.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba/claim-statement.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba/failure-summary.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba/limitations.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r4/README.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r4/claim-statement.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r4/limitations.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r5/README.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r5/claim-statement.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r5/limitations.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r6/README.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r6/claim-statement.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r6/limitations.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r7/README.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r7/claim-statement.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r7/limitations.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-10 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r8/README.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r8/claim-statement.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r8/limitations.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260511-alibaba-r9/README.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260511-alibaba-r9/claim-statement.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260511-alibaba-r9/limitations.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-11 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260512-alibaba-r10/README.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-12 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260512-alibaba-r10/claim-statement.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-12 |
| `docs/benchmark/runs/qbs1-powered-single-provider-20260512-alibaba-r10/limitations.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-12 |
| `docs/evidence/README.md` | agent context | FAIL | PASS | High evaluator impact; Tier 1. | 2026-05-16 |
| `docs/evidence/claim-boundaries.md` | agent context | FAIL | PASS | High evaluator and LLM impact; Tier 1. | 2026-05-16 |
| `docs/evidence/current-cvf-quality-status.md` | agent context | FAIL | PASS | High public trust impact; Tier 1. | 2026-05-16 |
| `docs/evidence/latest-release-gate.md` | agent context | FAIL | PASS | Medium evaluator impact; Tier 2 candidate. | 2026-05-16 |
| `docs/evidence/local-first-release-gate-proof-2026-05-16.md` | agent context | FAIL | PASS | Medium evaluator impact; Tier 2 candidate. | 2026-05-16 |
| `docs/evidence/provider-lanes.md` | agent context | FAIL | PASS | Medium evaluator impact; Tier 2 candidate. | 2026-05-09 |
| `docs/evidence/redaction-and-key-safety.md` | agent context | FAIL | PASS | Medium evaluator impact; Tier 2 candidate. | 2026-05-09 |
| `docs/evidence/renewed-repo-release-gate-proof.md` | agent context | FAIL | PASS | Medium evaluator impact. | 2026-05-09 |
| `docs/evidence/web-governance-path.md` | agent context | FAIL | PASS | Medium evaluator impact; Tier 2 candidate. | 2026-05-09 |
| `docs/guides/CVF_DEMO_SCRIPT_2026-04-21.md` | user-facing | FAIL | PASS | Useful demo guide; Tier 2 candidate after core guides. | 2026-05-16 |
| `docs/guides/local-first-deployment-baseline.md` | user-facing | FAIL | PASS | High onboarding impact; Tier 1. | 2026-05-16 |
| `docs/guides/minimum-useful-cvf.md` | user-facing | FAIL | PASS | High onboarding impact; Tier 1. | 2026-05-09 |
| `docs/reference/CVF_AUDIT_RECEIPT_INTEGRITY_MODEL.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact; Tier 2 candidate. | 2026-05-13 |
| `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md` | audit trail | FAIL | PASS | High trust impact; Tier 1 despite evidence sensitivity. | 2026-05-09 |
| `docs/reference/CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md` | agent context | FAIL | PASS | Medium LLM/dev reference impact; Tier 2 candidate. | 2026-05-09 |
| `docs/reviews/CVF_GC018_TRACK_D_PROVIDER_POLICY_ENGINE_2026-05-13.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-13 |
| `docs/reviews/CVF_GC018_TRACK_E_DLP_QUALITY_BENCHMARK_2026-05-13.md` | audit trail | FAIL | PASS | Preserve evidence shape. | 2026-05-13 |

## Decision

Proceed with Tier 1 rewrite for the 15 selected files listed above. The
operator has already authorized Codex to complete the tranche and present one
final review rather than stopping for each intermediate decision.

## Measurement

Tier 1 execution completed on the public repository:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

Final pushed public commit:

`a91a4b3 Standardize public limitations register`

Verification summary:

| Check | Result |
| --- | --- |
| Tier 1 files rewritten | 15/15 |
| Commit discipline | 15 public commits, one Tier 1 file per commit |
| GC-045 structural rubric | 15/15 PASS |
| GC-023 size status | 15/15 PASS |
| Public-surface scanner | PASS |
| `git diff --check` | PASS |

Representative word-count measurement used PowerShell
`Get-Content <file> | Measure-Object -Word`.

| File | Before | After | Result |
| --- | ---: | ---: | --- |
| `README.md` | 1817 | 1744 | down |
| `docs/guides/minimum-useful-cvf.md` | 695 | 695 | flat |
| `docs/evidence/current-cvf-quality-status.md` | 544 | 541 | down |

GitHub Files-view screenshots were captured with `npx playwright screenshot`:

- before: `docs/audits/public-markdown-files-view-before-2026-05-16.png`
- after: `docs/audits/public-markdown-files-view-after-2026-05-16.png`

Qualitative read-test note: no external human read-test was performed in this
tranche. Codex self-audit found the first useful information is now easier to
locate because Tier 1 files consistently expose `Memory class`, `Status`,
`Purpose`, `Scope`, and `Claim Boundary` anchors near the top.

## Verification

Public-sync verification completed:

```bash
git diff --check
python scripts/check_public_surface.py
```

Tier 1 structural verification used the GC-045 rubric from the provenance
checker and passed for all selected files.

## Related Artifacts

- `docs/baselines/CVF_GC018_PUBLIC_MARKDOWN_QUALITY_UPGRADE_AUTHORIZATION_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_PROPOSAL_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_CLOSURE_2026-05-16.md`
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`

## Claim Boundary

This audit claims only that the public Markdown surface has been classified and
that a bounded Tier 1 rewrite list has been selected. It does not claim Tier 1
rewrote every public Markdown file, does not claim all public Markdown should be
rewritten, and does not authorize Tier 2.
