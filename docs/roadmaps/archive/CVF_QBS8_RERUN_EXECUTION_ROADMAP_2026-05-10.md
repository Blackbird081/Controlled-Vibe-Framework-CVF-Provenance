# CVF QBS-8 Rerun Execution Roadmap

Memory class: FULL_RECORD
Status: FINAL ROADMAP - EXECUTION COMPLETE / REVIEW PENDING / NO QBS SCORE
Date: 2026-05-10
GC-018:
`docs/reference/CVF_GC018_QBS8_RERUN_EXECUTION_CANDIDATE_2026-05-10.md`

---

## 0. Purpose

QBS-8 executes the live powered single-provider rerun after QBS5 failed,
QBS6 remediated bounded runtime gaps, and QBS7 froze the F7 front-door
entrypoint decision.

## 1. Run-Set Progression

| Run-set | Status | Reason |
|---|---|---|
| R2 | Preregistered/no-score | F7 front-door behavior needed implementation hardening before live run |
| R3 | Preregistered/diagnostic | Exposed runner suffix and R3 block-enforcement gaps; no public execution artifact published |
| R4 | Executed/review-pending | Final hard-gate-passing live execution artifact |

## 2. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | Fresh operator authorization for live benchmark measurement | PASS |
| G1 | Public repo remote confirmed before push | PASS |
| G2 | R4 preregistration tag exists before execution | PASS |
| G3 | Runner supports R4 F7 front-door clarification path | PASS |
| G4 | R3 prohibited prompts block instead of approval-only escalation | PASS |
| G5 | 48 tasks x 3 repeats x 3 configs complete | PASS |
| G6 | `CFG-B` receipts complete | PASS |
| G7 | `CFG-B` expected decisions match | PASS |
| G8 | Secret scan clean and no mock fallback | PASS |
| G9 | Public artifacts published no-score/reviewer-pending | PASS |

## 3. Closure

Public artifact:

`docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba-r4/`

Public status:

`EXECUTION_COMPLETE_REVIEW_PENDING_NO_QBS_SCORE`

Hard-gate result:

- 432 configuration executions completed.
- All direct baseline transports OK.
- All `CFG-B` receipts present.
- All `CFG-B` expected decisions matched.
- F7 front-door clarification evidence complete.
- Severe unsafe false negatives: 0.
- Negative-control false blocks: 0.

## 4. Claim Boundary

Allowed:

- QBS8 R4 is hard-gate-passing `POWERED_SINGLE_PROVIDER` execution evidence for
  Alibaba/DashScope `qwen-turbo`.

Not allowed:

- public QBS score;
- L4/L5/L6 claim;
- family-level claim;
- provider parity claim;
- reviewer-scored quality claim.

## 5. Next Track

`QBS9-REVIEWER-SCORING-AND-AGREEMENT` may prepare blinded reviewer packets,
run reviewer scoring, compute agreement, adjudicate hard-gate disputes if any,
and only then determine whether an aggregate claim level is allowed.
