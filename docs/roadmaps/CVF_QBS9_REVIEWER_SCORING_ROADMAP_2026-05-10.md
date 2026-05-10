# CVF QBS-9 Reviewer Scoring And Agreement Roadmap

Memory class: FULL_RECORD
Status: FINAL ROADMAP - REVIEWER SCORED / NO PUBLIC QBS CLAIM
Date: 2026-05-10
GC-018:
`docs/reference/CVF_GC018_QBS9_REVIEWER_SCORING_CANDIDATE_2026-05-10.md`

---

## 0. Purpose

QBS-9 converts the hard-gate-passing QBS8 execution into a reviewer-scored
benchmark result, while preserving claim discipline.

## 1. Key Decision

R4 could not be legitimately scored for output quality because the public
artifact retained previews and hashes, not full redacted reviewer outputs. QBS9
therefore created R5 with a redacted reviewer output bundle.

## 2. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | R5 preregistration tag exists before execution | PASS |
| G1 | R5 includes full redacted reviewer output bundle | PASS |
| G2 | R5 hard gates pass after resume | PASS |
| G3 | Two model-assisted reviewers score blinded outputs | PASS |
| G4 | Reviewer agreement threshold passes | PASS |
| G5 | L4 quality uplift threshold evaluated | PASS |
| G6 | Public claim boundary reflects measured result | PASS |

## 3. Result

Agreement passed:

- kappa: `0.7138606707187487`
- Spearman rho: `0.7864500452029551`

L4 did not pass:

- median normalized quality delta `CFG-B` vs `CFG-A1`: `-0.25`
- bootstrap 95% CI: `[-0.3125, -0.25]`

Public status:

`QBS9_REVIEWER_SCORED_NO_PUBLIC_QBS_CLAIM`

## 4. Claim Boundary

Allowed:

- QBS9 may be cited as model-assisted reviewer scoring with agreement passed
  and no public QBS claim.

Not allowed:

- CVF has a public QBS quality score.
- CVF achieved L4/L5/L6 on QBS-1.
- family-level performance is proven.
- provider parity is proven.

## 5. Next Track

`QBS10-QUALITY-DELTA-ROOT-CAUSE-AND-IMPROVEMENT` should analyze why `CFG-B`
underperformed `CFG-A1` and propose bounded improvements before any new scored
claim attempt.
