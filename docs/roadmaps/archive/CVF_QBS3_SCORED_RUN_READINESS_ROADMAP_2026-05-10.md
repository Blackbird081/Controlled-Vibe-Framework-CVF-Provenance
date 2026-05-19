# CVF QBS-3 Scored Run Readiness Roadmap

Memory class: FULL_RECORD
Status: FINAL ROADMAP - READINESS PACKET COMPLETE / SCORED RUN BLOCKED
Date: 2026-05-10
GC-018:
`docs/reference/CVF_GC018_QBS3_SCORED_RUN_READINESS_CANDIDATE_2026-05-10.md`

---

## 0. Purpose

QBS-3 prepares QBS-1 for a future scored benchmark without running one. It
turns the accepted methodology and calibration proof into a machine-checkable
readiness packet.

This is a bridge between QBS-2 calibration and a future scored run. It is
structural evidence, not quality evidence.

## 1. Scope

Authorized:

- expand the prose corpus candidate into a public machine-readable 48-task
  corpus for aggregate-only `POWERED_SINGLE_PROVIDER`;
- add scored-run readiness documentation;
- add a readiness checker that validates corpus shape, required public files,
  secret-scan patterns, and optional pre-registration tag existence;
- update public benchmark index and runner contract;
- update public-surface manifest for the new checker;
- record provenance GC-018, roadmap, and handoff.

Not authorized:

- scored QBS benchmark execution;
- public QBS score;
- powered L4/L5/L6 claim;
- family-level quality claim;
- provider parity claim;
- new live provider evidence run.

## 2. Public Artifacts

| Artifact | Purpose |
|---|---|
| `docs/benchmark/qbs-1/powered-single-provider-corpus-v1.json` | 48-task aggregate-only powered corpus packet |
| `docs/benchmark/qbs-1/scored-run-readiness.md` | readiness gate and blocked-run boundary |
| `scripts/check_qbs_scored_run_readiness.py` | machine validation of readiness packet |
| `docs/benchmark/qbs-1/README.md` | QBS-1 status/index update |
| `docs/benchmark/README.md` | benchmark status update |
| `docs/benchmark/qbs-1/runner-contract.md` | readiness checker command boundary |
| `governance/public-surface-manifest.json` | public-surface allowlist update |

## 3. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | QBS-2 calibration pilot complete | PASS |
| G1 | Fresh GC-018 authorizes readiness only | PASS |
| G2 | 48-task corpus JSON exists | PASS |
| G3 | Corpus validates 8 families x 6 tasks | PASS |
| G4 | Negative controls validate as 6 tasks | PASS |
| G5 | Readiness checker implemented | PASS |
| G6 | Readiness checker passes without pre-registration | PASS with expected blocked-run warning |
| G7 | Public-surface scan passes | PASS |
| G8 | Whitespace check passes | PASS |
| G9 | Scored benchmark remains blocked | PASS |

## 4. Validation

Command:

```bash
python scripts/check_qbs_scored_run_readiness.py --json
```

Observed result:

- status: `PASS`
- public status: `QBS3_SCORED_RUN_READINESS_PACKET_READY_NO_SCORED_RUN`
- task count: 48
- run class: `POWERED_SINGLE_PROVIDER`
- claim scope: `aggregate_only`
- warning: no pre-registration tag supplied; scored execution remains blocked

Additional checks:

- `git diff --check`: PASS
- `python scripts/check_public_surface.py`: PASS

## 5. Claim Boundary

Public status after this roadmap:

`QBS3_SCORED_RUN_READINESS_PACKET_READY_NO_PUBLIC_QBS_SCORE`

Allowed statements:

- CVF has a public QBS methodology.
- CVF has QBS-1 planning and calibration artifacts.
- CVF has a public scored-run readiness packet for aggregate-only
  `POWERED_SINGLE_PROVIDER` planning.
- Scored runs require a run-specific public pre-registration tag and separate
  authorization.

Not allowed:

- CVF has a public QBS score.
- QBS3 is powered benchmark evidence.
- QBS3 proves L4/L5/L6.
- QBS3 proves provider parity.
- QBS3 supports family-level quality claims.

## 6. Next Track

The next track requires a fresh GC-018 and should be named separately, for
example:

`QBS4-SCORED-RUN-PREREGISTRATION`

Candidate scope:

- choose first scored run class: dry scored run vs `POWERED_SINGLE_PROVIDER`;
- choose provider/model lane;
- create provider/model manifest;
- create reviewer plan and blinded packet schema;
- create exact artifact path;
- create public `qbs/preregister/<run-id>` tag;
- run readiness checker with `--require-preregistration`;
- only then consider live scored execution under a separate operator approval.
