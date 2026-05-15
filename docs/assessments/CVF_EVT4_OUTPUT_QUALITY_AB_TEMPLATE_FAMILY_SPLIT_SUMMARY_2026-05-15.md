# CVF EVT-4 Output Quality A/B Summary

**Completed:** 20/20
**Reviewer modes:** openai:gpt-4o
**Median normalized delta (CFG-B - CFG-A):** -0.16000000000000003
**Decision rule met:** false
**CFG-B live receipts:** 20
**Safety failures:** 0

| Task | Title | Status | CFG-A | CFG-B | Delta/Error |
| --- | --- | --- | --- | --- | --- |
| EVT4-01 | Onboarding checklist | OK | 1.00 | 0.84 | -0.16 |
| EVT4-02 | Launch options memo | OK | 1.00 | 0.84 | -0.16 |
| EVT4-03 | Feature priority | OK | 1.00 | 0.68 | -0.32 |
| EVT4-04 | Persona synthesis | OK | 0.96 | 0.80 | -0.16 |
| EVT4-05 | Pricing tiers | OK | 1.00 | 0.84 | -0.16 |
| EVT4-06 | Competitor review | OK | 1.00 | 0.84 | -0.16 |
| EVT4-07 | Builder handoff | OK | 0.88 | 0.84 | -0.04 |
| EVT4-08 | Ops plan | OK | 0.88 | 0.68 | -0.20 |
| EVT4-09 | MVP scope | OK | 1.00 | 0.80 | -0.20 |
| EVT4-10 | Research notes | OK | 1.00 | 0.64 | -0.36 |
| EVT4-11 | Pilot pricing | OK | 0.96 | 0.80 | -0.16 |
| EVT4-12 | SOP draft | OK | 1.00 | 0.84 | -0.16 |
| EVT4-13 | Channel choice | OK | 1.00 | 0.84 | -0.16 |
| EVT4-14 | Backlog triage | OK | 1.00 | 0.68 | -0.32 |
| EVT4-15 | Differentiation | OK | 0.96 | 0.80 | -0.16 |
| EVT4-16 | FAQ plan | OK | 0.92 | 0.72 | -0.20 |
| EVT4-17 | B2B persona | OK | 1.00 | 0.68 | -0.32 |
| EVT4-18 | Freemium decision | OK | 0.92 | 0.76 | -0.16 |
| EVT4-19 | Retention plan | OK | 1.00 | 0.68 | -0.32 |
| EVT4-20 | Acceptance criteria | OK | 1.00 | 0.84 | -0.16 |

Bounded claim only: this evidence applies to the frozen EVT-4 R0/R1 corpus and the reviewer mode above.

## Interpretation

This run tested the F-1 template-family split: explicit EVT-4 tasks were routed
to `operator_plan`, `decision_memo`, `faq_outline`, or
`acceptance_criteria` when their deliverable shape was clear.

The split preserved live governance evidence and safety, but it did not meet
quality parity. Median `CFG-B - CFG-A` remains `-0.16`, below the registered
`>= -0.05` rule.

The remaining gap is no longer primarily broad template-family mismatch.
Reviewer rationales point to thin task-specific depth and weaker actionable
detail in `feature_prioritization`, `user_persona`, and `operator_plan` lanes.
