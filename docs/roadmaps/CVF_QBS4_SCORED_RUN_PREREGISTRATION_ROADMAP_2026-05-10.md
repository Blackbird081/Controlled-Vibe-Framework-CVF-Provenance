# CVF QBS-4 Scored Run Pre-Registration Roadmap

Memory class: FULL_RECORD
Status: FINAL ROADMAP - PRE-REGISTRATION COMPLETE / SCORED RUN BLOCKED
Date: 2026-05-10
GC-018:
`docs/reference/CVF_GC018_QBS4_SCORED_RUN_PREREGISTRATION_CANDIDATE_2026-05-10.md`

---

## 0. Purpose

QBS-4 freezes the first planned QBS scored-run input set. It does not execute
the scored benchmark.

The track exists to prevent post-hoc benchmark changes before a future live
scored run.

## 1. Scope

Authorized:

- choose the first scored run class and provider/model lane;
- publish a run-specific pre-registration packet;
- publish provider/model, config prompt, and reviewer plan artifacts;
- create and push a public `qbs/preregister/<run-id>` tag;
- run the scored-run readiness checker with tag verification;
- update public benchmark and claim-boundary docs;
- record provenance GC-018, roadmap, and handoff.

Not authorized:

- scored QBS benchmark execution;
- public QBS score;
- powered L4/L5/L6 claim;
- family-level quality claim;
- provider parity claim;
- new live provider evidence execution.

## 2. Public Artifacts

Run ID:

`qbs1-powered-single-provider-20260510-alibaba`

Public artifacts:

- `docs/benchmark/qbs-1/preregistrations/qbs1-powered-single-provider-20260510-alibaba.md`
- `docs/benchmark/qbs-1/provider-model-manifest.qbs1-powered-single-provider-20260510-alibaba.json`
- `docs/benchmark/qbs-1/config-prompt-manifest.qbs1-powered-single-provider-20260510-alibaba.json`
- `docs/benchmark/qbs-1/reviewer-plan.qbs1-powered-single-provider-20260510-alibaba.md`
- `scripts/check_qbs_scored_run_readiness.py`
- `README.md`
- `docs/benchmark/README.md`
- `docs/benchmark/qbs-1/README.md`
- `docs/evidence/claim-boundaries.md`

Public tag:

`qbs/preregister/qbs1-powered-single-provider-20260510-alibaba`

Tag SHA:

`3f574fd5e5843b577a1e7ec78bfcce7f10fd1053`

## 3. Frozen Run Declaration

| Field | Value |
|---|---|
| run class | `POWERED_SINGLE_PROVIDER` |
| provider | Alibaba/DashScope |
| model | `qwen-turbo` |
| corpus version | `qbs1-powered-single-provider-corpus-v1-2026-05-10` |
| task count | 48 |
| configs | `CFG-A0`, `CFG-A1`, `CFG-B` |
| repeat count | 3 |
| planned configuration executions | 432 |
| artifact root | `docs/benchmark/runs/qbs1-powered-single-provider-20260510-alibaba/` |
| allowed claim target | L4 aggregate only |
| family-level claims | blocked |

## 4. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | QBS3 readiness packet complete | PASS |
| G1 | Fresh GC-018 authorizes pre-registration only | PASS |
| G2 | Run-specific pre-registration packet exists | PASS |
| G3 | Provider/model manifest exists | PASS |
| G4 | Config prompt manifest exists | PASS |
| G5 | Reviewer plan exists | PASS |
| G6 | Public pre-registration tag exists | PASS |
| G7 | Readiness checker passes with `--require-preregistration` | PASS |
| G8 | Public-surface scan passes | PASS |
| G9 | Whitespace check passes | PASS |
| G10 | Scored benchmark remains blocked | PASS |

## 5. Validation

Command:

```bash
python scripts/check_qbs_scored_run_readiness.py --json --require-preregistration --preregistration-tag qbs/preregister/qbs1-powered-single-provider-20260510-alibaba
```

Observed result:

- status: `PASS`
- public status: `QBS4_SCORED_RUN_PREREGISTERED_NO_SCORED_RUN`
- task count: 48
- run class: `POWERED_SINGLE_PROVIDER`
- claim scope: `aggregate_only`
- pre-registration tag SHA:
  `3f574fd5e5843b577a1e7ec78bfcce7f10fd1053`
- warnings: none

Additional checks:

- `git diff --check`: PASS
- `python scripts/check_public_surface.py`: PASS
- targeted raw-secret scan: no matches

## 6. Claim Boundary

Public status after this roadmap:

`QBS4_SCORED_RUN_PREREGISTERED_NO_PUBLIC_QBS_SCORE`

Allowed statements:

- CVF has a public QBS methodology.
- CVF has QBS-1 planning, calibration, scored-run readiness, and a first
  scored-run pre-registration packet.
- The first planned aggregate-only `POWERED_SINGLE_PROVIDER` run is
  pre-registered for Alibaba/DashScope `qwen-turbo`.

Not allowed:

- CVF has a public QBS score.
- QBS4 is powered benchmark evidence.
- QBS4 proves L4/L5/L6.
- QBS4 proves provider parity.
- QBS4 supports family-level quality claims.

## 7. Next Track

The next track requires a fresh GC-018 and should be named separately, for
example:

`QBS5-SCORED-RUN-EXECUTION`

Candidate prerequisites:

- operator explicitly authorizes live scored execution;
- live budget, quota, stop conditions, and provider credentials are confirmed;
- reviewer availability is confirmed;
- raw/private artifact retention path is confirmed outside the public repo;
- scored execution runner is implemented or extended from calibration runner;
- no scored evidence is claimed until artifacts and review are complete.
