# CVF Public Markdown Quality Upgrade Tier 1 Amendment - 2026-05-16

Memory class: FULL_RECORD

Status: TIER 1 AMENDMENT CLOSED - PUBLIC PUSH PENDING

## Purpose

Record a faithful amendment to the Tier 1 closure packet
(`CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_CLOSURE_2026-05-16.md`) after a
post-Tier-2 audit found that Tier 1 had reached GC-045 common-elements
compliance only, not full artifact-type template compliance. Seven Tier 1
files have now been amended to satisfy the full automated template, and this
amendment records the discrepancy honestly so the audit chain reflects what
actually happened.

## Scope

Documentation-only amendment to Tier 1 closure semantics. No claim drift, no
runtime change, no new external knowledge intake, no Tier 3 work.

## Target

Tier 1 closure record:

`docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_CLOSURE_2026-05-16.md`

Original Tier 1 closure stated:

> Tier 1 GC-045 compliance: 15 of 15 satisfied (rubric)
> Verification used the GC-045 rubric from the provenance checker.

That claim was true under a **manual common-elements rubric** (title, Memory
class, Status, Purpose, Scope, Claim Boundary). It was not verified against
the **full automated template check** in `check_markdown_structural_completeness.py`,
which classifies each file into an artifact type (spec / baseline / handoff /
review / policy / contract / roadmap / adr / guard) and requires additional
type-specific sections.

## Findings

After Tier 2 installed the GC-045 checker stack into public-sync, a post-Tier-2
audit ran the automated check across the whole public Markdown surface. Result
for Tier 1 files:

| File | Classifier | Automated check before amendment |
| --- | --- | --- |
| `README.md` | spec | FAIL — missing 4 spec sections |
| `docs/guides/minimum-useful-cvf.md` | spec | FAIL — missing 4 spec sections |
| `docs/guides/local-first-deployment-baseline.md` | baseline | FAIL — missing 3 baseline sections |
| `docs/evidence/claim-boundaries.md` | baseline | FAIL — missing 3 baseline sections |
| `docs/evidence/current-cvf-quality-status.md` | baseline | FAIL — missing 2 baseline sections |
| `docs/evidence/README.md` | handoff (misfire) → baseline after rephrase | FAIL — missing handoff/baseline sections |
| `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md` | spec | FAIL — missing 4 spec sections |

Eight remaining Tier 1 files passed the automated check unchanged.

The classifier false-positive on `docs/evidence/README.md` was caused by
keyword scanning in the first 8 lines: the original body mentioned
*"handoffs"* and *"rebuttals"* in passing, which triggered handoff and review
classification. The amendment rephrased that line to neutral text and the
file then classified as baseline, which is the right artifact type for an
evidence index.

## Risk

- **Claim drift in Tier 1 closure.** The closure stated 15/15 GC-045 PASS,
  which was true for the rubric used but not for the full template. This
  amendment makes the discrepancy explicit so the audit chain remains honest.
- **Classifier false positives.** The keyword-based classifier can mis-route
  files when their body text mentions other artifact types. Mitigation:
  authors should keep the first 8 lines focused on the file's own purpose,
  not on what the file is *not*. A future GC-045 improvement could move
  artifact-type hinting to frontmatter.
- **Word-count direction.** The seven amendment files all grew (added 16–35
  lines each). This is consistent with the Tier 2 finding that structural
  metadata enrichment is the right metric for baseline and spec files, not
  word-count reduction.

## Corrective Action

Seven public-sync commits, one per amended file:

| Commit | File |
| --- | --- |
| `3e329a1` | `README.md` |
| `911a487` | `docs/guides/minimum-useful-cvf.md` |
| `d40cc7d` | `docs/guides/local-first-deployment-baseline.md` |
| `08bdbdc` | `docs/evidence/claim-boundaries.md` |
| `bfdadfa` | `docs/evidence/current-cvf-quality-status.md` |
| `baff761` | `docs/evidence/README.md` |
| `5ed436a` | `docs/reference/CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md` |

Every amended file passes `check_markdown_structural_completeness.py --no-bootstrap --all-changed --enforce` after the amendment.

## Decision

Tier 1 closure is preserved as-is for audit chain continuity. This amendment
file supersedes the Tier 1 "15 of 15 satisfied rubric" line for any future reader.
The current public state is:

- Tier 1 files: 15 of 15 satisfied full GC-045 automated template (after amendment).
- Tier 2 files: 10 of 10 satisfied full GC-045 automated template.
- No claim drift on numeric values, dates, or gate labels in any amendment file.

## Verification

For each amendment commit:

```bash
cd <public-sync-workspace>
python governance/compat/check_markdown_structural_completeness.py \
  --base HEAD --head HEAD --no-bootstrap --all-changed --enforce
```

Re-running across the full Tier 1 set after amendment:

| Check | Result |
| --- | --- |
| Tier 1 files automated GC-045 PASS | 15/15 |
| Tier 1 amendment commits in public-sync | 7 |
| No claim drift on numeric/date/gate labels | confirmed |

## Recommendation

Close the Tier 1 amendment at the seven files above. Do not retroactively
edit the original Tier 1 closure file beyond this amendment record. Treat
this discrepancy as a known process lesson: any future "rubric PASS" claim
should be verified against the automated checker rather than against a
manual common-elements rubric, when the automated checker is available.

## Related Artifacts

- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_PROPOSAL_2026-05-16.md`
- `docs/baselines/CVF_GC018_PUBLIC_MARKDOWN_QUALITY_UPGRADE_AUTHORIZATION_2026-05-16.md`
- `docs/audits/CVF_PUBLIC_REPO_MARKDOWN_QUALITY_AUDIT_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_1_CLOSURE_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_2_PROPOSAL_2026-05-16.md`
- `docs/baselines/CVF_GC018_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_2_AUTHORIZATION_2026-05-16.md`
- `docs/reviews/CVF_PUBLIC_MARKDOWN_QUALITY_UPGRADE_TIER_2_CLOSURE_2026-05-16.md`

## Claim Boundary

This amendment claims only that seven Tier 1 files have been re-amended to
satisfy the full automated GC-045 template, and that the original Tier 1
closure "15 of 15 satisfied rubric" line is now superseded by automated 15 of 15 satisfied.
It does not claim every public Markdown file is GC-045 compliant, does not
claim Tier 1 read-time improvement was externally verified, does not
authorize Tier 3, and does not claim runtime governance or output-quality
changes.
