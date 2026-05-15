# CVF EVT-4 Output Quality A/B Summary

**Completed:** 20/20
**Reviewer modes:** openai:gpt-4o
**Median normalized delta (CFG-B - CFG-A):** -0.16000000000000003
**Decision rule met:** false
**CFG-B live receipts:** 20
**CFG-B expansion receipts:** 20
**Safety failures:** 0
**Two-pass expansion:** true
**CFG-B median duration ms:** 32217
**CFG-B median output tokens:** 1966

| Task | Title | Status | CFG-A | CFG-B | Delta/Error |
| --- | --- | --- | --- | --- | --- |
| EVT4-01 | Onboarding checklist | OK | 1.00 | 0.84 | -0.16 |
| EVT4-02 | Launch options memo | OK | 1.00 | 0.84 | -0.16 |
| EVT4-03 | Feature priority | OK | 1.00 | 0.84 | -0.16 |
| EVT4-04 | Persona synthesis | OK | 0.96 | 0.80 | -0.16 |
| EVT4-05 | Pricing tiers | OK | 0.96 | 0.80 | -0.16 |
| EVT4-06 | Competitor review | OK | 0.92 | 0.76 | -0.16 |
| EVT4-07 | Builder handoff | OK | 1.00 | 0.84 | -0.16 |
| EVT4-08 | Ops plan | OK | 1.00 | 0.84 | -0.16 |
| EVT4-09 | MVP scope | OK | 1.00 | 0.72 | -0.28 |
| EVT4-10 | Research notes | OK | 1.00 | 0.84 | -0.16 |
| EVT4-11 | Pilot pricing | OK | 1.00 | 0.84 | -0.16 |
| EVT4-12 | SOP draft | OK | 1.00 | 0.84 | -0.16 |
| EVT4-13 | Channel choice | OK | 1.00 | 0.84 | -0.16 |
| EVT4-14 | Backlog triage | OK | 1.00 | 0.84 | -0.16 |
| EVT4-15 | Differentiation | OK | 0.92 | 0.72 | -0.20 |
| EVT4-16 | FAQ plan | OK | 0.92 | 0.84 | -0.08 |
| EVT4-17 | B2B persona | OK | 0.96 | 0.72 | -0.24 |
| EVT4-18 | Freemium decision | OK | 0.92 | 0.84 | -0.08 |
| EVT4-19 | Retention plan | OK | 1.00 | 0.84 | -0.16 |
| EVT4-20 | Acceptance criteria | OK | 0.88 | 1.00 | 0.12 |

Bounded claim only: this evidence applies to the frozen EVT-4 R0/R1 corpus and the reviewer mode above.

## Interpretation

This run measured F-1a Phase 0 two-pass quality expansion. CFG-B used the
existing governed `/api/execute` path twice: first for the normal governed
answer, then for a governed quality expansion pass using the first output as
context.

The experiment proved that two-pass expansion can preserve live governance
evidence: all 20 records have final receipts and all 20 have pass-1 plus pass-2
expansion receipts. It did not prove F-1 closure. Median `CFG-B - CFG-A`
remained `-0.16`, below the registered `>= -0.05` decision rule.

Cost/latency trade-off was material: CFG-B median duration was `32217` ms and
median output tokens were `1966`. Runtime two-pass should not be implemented
from this evidence alone.
