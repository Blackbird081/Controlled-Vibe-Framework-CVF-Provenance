Memory class: FULL_RECORD
# CVF Public GitHub Renewal - Operator Visibility Decision

Date: 2026-05-09
Status: OPERATOR DECISION RECORDED LOCALLY

## Decision

The repository `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git`
is the private provenance archive for CVF.

It should be made private. Access should be provided only when an auditor,
partner, maintainer, or deep-review user needs to inspect historical evidence,
raw development records, agent handoffs, rebuttals, or other provenance-only
material.

From this decision onward, the only GitHub repository intended to provide CVF
information to external/public users is:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`

## Operating Rule

- Do not push public-facing CVF content to the provenance repository.
- Do not use the provenance repository as the public product front door.
- Push public-facing architecture, contributor attribution, setup, governance,
  provider, cost, and evidence-summary changes to
  `Controlled-Vibe-Framework-CVF.git`.
- Keep the provenance repository available for private audit and deep continuity
  review only.

## Boundary

This local decision record does not rename repositories, change GitHub
visibility, export history, or create a release. It records the operator's
visibility decision for future local work.
