# CVF QBS-7 Rerun Pre-Registration Roadmap

Memory class: FULL_RECORD
Status: FINAL ROADMAP - RERUN PREREGISTERED / NO SCORED RUN
Date: 2026-05-10
GC-018:
`docs/reference/CVF_GC018_QBS7_RERUN_PREREGISTRATION_CANDIDATE_2026-05-10.md`

---

## 0. Purpose

QBS-7 freezes the R2 rerun contract after QBS5 failed hard gates and QBS6
remediated bounded runtime causes. It does not execute a new powered benchmark.

## 1. Entrypoint Decision

| Scope | R2 `CFG-B` entrypoint |
|---|---|
| Non-F7 tasks | `POST /api/execute` |
| `QBS1-F7-T01` through `QBS1-F7-T06` | Intent-first front door plus clarification loop before any execute handoff |

F7 remains a `CLARIFY` expectation. The rerun does not make `/api/execute`
guess missing context for ambiguous non-coder prompts.

## 2. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | QBS5 failed/no-score evidence remains unchanged | PASS |
| G1 | Fresh GC-018 authorizes preregistration | PASS |
| G2 | R2 run ID and artifact root are frozen | PASS |
| G3 | Provider/model manifest is frozen | PASS |
| G4 | Config/entrypoint manifest records F7 front-door clarification | PASS |
| G5 | Reviewer plan records F7 adjudication rule | PASS |
| G6 | Public claim boundaries remain no-score | PASS |
| G7 | Readiness checker validates the R2 tag | PASS |

## 3. Closure

Public commit:

`361ff91 Preregister QBS rerun packet`

Public run ID:

`qbs1-powered-single-provider-20260510-alibaba-r2`

Public tag:

`qbs/preregister/qbs1-powered-single-provider-20260510-alibaba-r2`

Tag SHA:

`361ff91fb441b4fef1bdc4f9a7d78f0ed8a2a5e4`

Public packet:

- `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba-r2.md`
- `docs/benchmark/qbs-1/provider-model-manifest.qbs1-powered-single-provider-20260510-alibaba-r2.json`
- `docs/benchmark/qbs-1/config-prompt-manifest.qbs1-powered-single-provider-20260510-alibaba-r2.json`
- `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba-r2.md`
- `docs/benchmark/qbs-1/rerun-plan-qbs7.md`

Verification:

- `python scripts/check_qbs_scored_run_readiness.py --json --require-preregistration --preregistration-tag qbs/preregister/qbs1-powered-single-provider-20260510-alibaba-r2`
  PASS.
- `python scripts/check_public_surface.py` PASS.
- `git diff --check` PASS.
- targeted raw-key scan: no matches.

## 4. Claim Boundary

Allowed:

- QBS7 is a frozen R2 rerun pre-registration.
- QBS6 remediated bounded runtime gaps.
- QBS5 remains failed/no-score evidence.

Not allowed:

- CVF has a public QBS score.
- QBS7 proves L4/L5/L6.
- QBS7 is a live rerun result.
- QBS7 changes QBS5.

## 5. Next Track

`QBS8-RERUN-EXECUTION` may run the live R2 rerun only after explicit operator
authorization for live cost, credential availability, stop conditions, and
reviewer readiness.
