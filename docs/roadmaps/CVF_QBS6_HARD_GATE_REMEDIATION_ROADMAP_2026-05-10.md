# CVF QBS-6 Hard-Gate Remediation And Rerun Planning Roadmap

Memory class: FULL_RECORD
Status: FINAL ROADMAP - REMEDIATION COMPLETE / RERUN BLOCKED
Date: 2026-05-10
GC-018:
`docs/reference/CVF_GC018_QBS6_HARD_GATE_REMEDIATION_CANDIDATE_2026-05-10.md`

---

## 0. Purpose

QBS-6 remediates bounded hard-gate failures exposed by the failed QBS5
execution and prepares a future rerun plan. It does not execute a new scored
benchmark.

## 1. Failure Classification

| Failure | Classification | QBS6 action |
|---|---|---|
| Safety-filter block returned no receipt | Runtime evidence bug | Fix receipt emission |
| R2 sensitive/access-boundary tasks were allowed | Runtime policy gap | Escalate to `NEEDS_APPROVAL` |
| Ambiguous non-coder tasks were allowed instead of clarified | Benchmark entrypoint mismatch | Plan rerun-path change; no quick runtime patch |

## 2. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | QBS5 failed/no-score evidence published | PASS |
| G1 | Fresh GC-018 authorizes remediation | PASS |
| G2 | Safety-filter receipt fix | PASS |
| G3 | R2 sensitive approval escalation fix | PASS |
| G4 | Targeted tests pass | PASS |
| G5 | Public remediation/rerun plan published | PASS |
| G6 | No new scored rerun or score claim | PASS |

## 3. Closure

Public commit:

`4e37e86 Remediate QBS hard-gate failures`

Delivered:

- safety-filter receipt completeness fix;
- declared-risk enforcement fix;
- R2 sensitive/access-boundary approval escalation;
- targeted unit/route coverage;
- public QBS6 remediation note.

Verification:

- `npm run test:run -- src/lib/enforcement.qbs-hard-gates.test.ts src/app/api/execute/route.qbs-hard-gates.test.ts`
  PASS, 5/5.
- live remediation smoke PASS across allow, safety block receipt, R2 sensitive
  approval, and R2 external-scope approval cases.
- `npm run build` PASS.
- `python scripts/check_public_surface.py` PASS.
- `git diff --check` PASS.
- targeted raw-key scan: no matches.

## 4. Claim Boundary

Allowed:

- QBS5 failed hard gates.
- QBS6 remediates bounded runtime gaps and plans a rerun.

Not allowed:

- CVF has a QBS score.
- QBS6 proves L4/L5/L6.
- QBS6 changes the QBS5 failed result.

## 5. Next Track

After QBS6, a future track may create a new pre-registration tag for a rerun
only after the F7 ambiguous-request entrypoint is resolved.
