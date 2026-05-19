# CVF EVT-4 Output Quality A/B Summary

**Provider/model:** deepseek / deepseek-v4-pro
**Provider timeout ms:** 120000
**Completed:** 19/20
**Reviewer modes:** openai:gpt-4o
**Median normalized delta (CFG-B - CFG-A):** -0.12
**Decision rule met:** false
**CFG-B live receipts:** 19
**CFG-B expansion receipts:** 0
**Safety failures:** 0
**Two-pass expansion:** false
**CFG-B median duration ms:** 84954
**CFG-B median output tokens:** 2671

| Task | Title | Status | CFG-A | CFG-B | Delta/Error |
| --- | --- | --- | --- | --- | --- |
| EVT4-01 | Onboarding checklist | OK | 0.88 | 1.00 | 0.12 |
| EVT4-02 | Launch options memo | OK | 0.88 | 0.92 | 0.04 |
| EVT4-03 | Feature priority | OK | 0.88 | 1.00 | 0.12 |
| EVT4-04 | Persona synthesis | OK | 1.00 | 0.84 | -0.16 |
| EVT4-05 | Pricing tiers | OK | 0.88 | 0.64 | -0.24 |
| EVT4-06 | Competitor review | OK | 1.00 | 0.84 | -0.16 |
| EVT4-07 | Builder handoff | OK | 0.72 | 1.00 | 0.28 |
| EVT4-08 | Ops plan | OK | 0.88 | 0.68 | -0.20 |
| EVT4-09 | MVP scope | FAIL | - | - | CFG-B 422: Generated response failed output validation after retry attempts. |
| EVT4-10 | Research notes | OK | 0.64 | 0.88 | 0.24 |
| EVT4-11 | Pilot pricing | OK | 0.84 | 0.92 | 0.08 |
| EVT4-12 | SOP draft | OK | 1.00 | 0.80 | -0.20 |
| EVT4-13 | Channel choice | OK | 0.88 | 1.00 | 0.12 |
| EVT4-14 | Backlog triage | OK | 0.96 | 0.84 | -0.12 |
| EVT4-15 | Differentiation | OK | 0.92 | 0.72 | -0.20 |
| EVT4-16 | FAQ plan | OK | 1.00 | 0.84 | -0.16 |
| EVT4-17 | B2B persona | OK | 0.88 | 0.96 | 0.08 |
| EVT4-18 | Freemium decision | OK | 1.00 | 0.84 | -0.16 |
| EVT4-19 | Retention plan | OK | 0.68 | 1.00 | 0.32 |
| EVT4-20 | Acceptance criteria | OK | 1.00 | 0.84 | -0.16 |

Bounded claim only: this evidence applies to the frozen EVT-4 R0/R1 corpus and the reviewer mode above.
