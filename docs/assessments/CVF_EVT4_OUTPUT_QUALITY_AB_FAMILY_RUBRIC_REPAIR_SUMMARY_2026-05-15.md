# CVF EVT-4 Output Quality A/B Summary

**Completed:** 20/20
**Reviewer modes:** openai:gpt-4o
**Median normalized delta (CFG-B - CFG-A):** -0.16000000000000003
**Decision rule met:** false
**CFG-B live receipts:** 20
**CFG-B expansion receipts:** 0
**Safety failures:** 0
**Two-pass expansion:** false
**CFG-B median duration ms:** 13772
**CFG-B median output tokens:** 894

| Task | Title | Status | CFG-A | CFG-B | Delta/Error |
| --- | --- | --- | --- | --- | --- |
| EVT4-01 | Onboarding checklist | OK | 1.00 | 0.84 | -0.16 |
| EVT4-02 | Launch options memo | OK | 1.00 | 0.84 | -0.16 |
| EVT4-03 | Feature priority | OK | 1.00 | 0.84 | -0.16 |
| EVT4-04 | Persona synthesis | OK | 0.96 | 0.80 | -0.16 |
| EVT4-05 | Pricing tiers | OK | 1.00 | 0.84 | -0.16 |
| EVT4-06 | Competitor review | OK | 1.00 | 0.84 | -0.16 |
| EVT4-07 | Builder handoff | OK | 1.00 | 0.84 | -0.16 |
| EVT4-08 | Ops plan | OK | 1.00 | 0.84 | -0.16 |
| EVT4-09 | MVP scope | OK | 1.00 | 0.84 | -0.16 |
| EVT4-10 | Research notes | OK | 1.00 | 0.84 | -0.16 |
| EVT4-11 | Pilot pricing | OK | 0.96 | 0.80 | -0.16 |
| EVT4-12 | SOP draft | OK | 1.00 | 0.84 | -0.16 |
| EVT4-13 | Channel choice | OK | 1.00 | 0.84 | -0.16 |
| EVT4-14 | Backlog triage | OK | 1.00 | 0.84 | -0.16 |
| EVT4-15 | Differentiation | OK | 0.96 | 0.80 | -0.16 |
| EVT4-16 | FAQ plan | OK | 0.92 | 0.84 | -0.08 |
| EVT4-17 | B2B persona | OK | 1.00 | 0.84 | -0.16 |
| EVT4-18 | Freemium decision | OK | 1.00 | 0.84 | -0.16 |
| EVT4-19 | Retention plan | OK | 1.00 | 0.84 | -0.16 |
| EVT4-20 | Acceptance criteria | OK | 1.00 | 0.84 | -0.16 |

Bounded claim only: this evidence applies to the frozen EVT-4 R0/R1 corpus and the reviewer mode above.

## Interpretation

This run tested targeted family-rubric repair for
`feature_prioritization`, `user_persona`, `operator_plan`, and
`competitor_review`. The repair removed the worst outliers from the previous
one-pass family split, but it did not meet F-1 parity. Median `CFG-B - CFG-A`
remained `-0.16`, below the registered `>= -0.05` rule.

This evidence supports keeping the family-rubric improvements as a better
bounded template posture, but it does not close F-1.
