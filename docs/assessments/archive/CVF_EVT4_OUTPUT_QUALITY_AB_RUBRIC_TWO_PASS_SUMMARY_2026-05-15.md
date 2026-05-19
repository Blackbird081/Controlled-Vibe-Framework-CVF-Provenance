# CVF EVT-4 Output Quality A/B Summary

**Completed:** 20/20
**Reviewer modes:** openai:gpt-4o
**Median normalized delta (CFG-B - CFG-A):** -0.16000000000000003
**Decision rule met:** false
**CFG-B live receipts:** 20
**CFG-B expansion receipts:** 20
**Safety failures:** 0
**Two-pass expansion:** true
**CFG-B median duration ms:** 29255
**CFG-B median output tokens:** 1960

| Task | Title | Status | CFG-A | CFG-B | Delta/Error |
| --- | --- | --- | --- | --- | --- |
| EVT4-01 | Onboarding checklist | OK | 1.00 | 0.84 | -0.16 |
| EVT4-02 | Launch options memo | OK | 1.00 | 0.84 | -0.16 |
| EVT4-03 | Feature priority | OK | 1.00 | 0.84 | -0.16 |
| EVT4-04 | Persona synthesis | OK | 0.96 | 0.84 | -0.12 |
| EVT4-05 | Pricing tiers | OK | 0.92 | 0.68 | -0.24 |
| EVT4-06 | Competitor review | OK | 1.00 | 0.84 | -0.16 |
| EVT4-07 | Builder handoff | OK | 1.00 | 0.84 | -0.16 |
| EVT4-08 | Ops plan | OK | 0.92 | 0.84 | -0.08 |
| EVT4-09 | MVP scope | OK | 1.00 | 0.84 | -0.16 |
| EVT4-10 | Research notes | OK | 1.00 | 0.84 | -0.16 |
| EVT4-11 | Pilot pricing | OK | 1.00 | 0.84 | -0.16 |
| EVT4-12 | SOP draft | OK | 1.00 | 0.84 | -0.16 |
| EVT4-13 | Channel choice | OK | 1.00 | 0.84 | -0.16 |
| EVT4-14 | Backlog triage | OK | 1.00 | 0.84 | -0.16 |
| EVT4-15 | Differentiation | OK | 0.92 | 0.72 | -0.20 |
| EVT4-16 | FAQ plan | OK | 0.92 | 0.84 | -0.08 |
| EVT4-17 | B2B persona | OK | 0.96 | 0.80 | -0.16 |
| EVT4-18 | Freemium decision | OK | 1.00 | 0.84 | -0.16 |
| EVT4-19 | Retention plan | OK | 1.00 | 0.84 | -0.16 |
| EVT4-20 | Acceptance criteria | OK | 1.00 | 0.84 | -0.16 |

Bounded claim only: this evidence applies to the frozen EVT-4 R0/R1 corpus and the reviewer mode above.

## Interpretation

This run tested the repaired family rubrics together with the experimental
two-pass quality expansion path. It preserved live governance proof:
20/20 final receipts, 20/20 expansion receipt pairs, and 0 safety failures.

It still did not close F-1. Median `CFG-B - CFG-A` remained `-0.16`, below the
registered `>= -0.05` rule, with CFG-B median duration `29255` ms and median
output tokens `1960`.

Do not implement runtime two-pass from this evidence. Output shaping has likely
hit the current benchmark ceiling.
