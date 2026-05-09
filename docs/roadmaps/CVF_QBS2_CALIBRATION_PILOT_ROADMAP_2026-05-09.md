# CVF QBS-2 Calibration Pilot Roadmap

Memory class: FULL_RECORD
Status: FINAL ROADMAP - PUBLIC PUSH COMPLETE / SCORED RUN BLOCKED
Date: 2026-05-09
GC-018:
`docs/reference/CVF_GC018_QBS2_CALIBRATION_PILOT_CANDIDATE_2026-05-09.md`

---

## 0. Purpose

QBS-2 proves that the QBS runner concept can execute a small calibration pilot
across live provider lanes and publish curated artifacts without claiming a
benchmark score.

This is a bridge between methodology/planning and a future scored benchmark.
It is intentionally directional and operational, not statistical.

## 1. Scope

Authorized:

- implement a public calibration runner;
- use Alibaba/DashScope, DeepSeek, and OpenAI local ignored API keys;
- run the three QBS configuration paths:
  - `CFG-A0`: direct model baseline;
  - `CFG-A1`: neutral-control baseline;
  - `CFG-B`: governed CVF path;
- publish curated calibration artifacts under `docs/benchmark/runs/`;
- update public README, benchmark status, and claim-boundary language;
- record provenance GC-018, roadmap, and handoff.

Not authorized:

- scored QBS benchmark execution;
- powered L4/L5/L6 claim;
- family-level quality claim;
- provider parity claim;
- public QBS score.

## 2. Public Implementation And Evidence

Public runner:

- `scripts/run_qbs_calibration_pilot.py`

Public pre-registration tags:

- initial: `qbs/preregister/qbs1-calibration-20260509-three-provider`
- r2: `qbs/preregister/qbs1-calibration-20260509-three-provider-r2`
- r3: `qbs/preregister/qbs1-calibration-20260509-three-provider-r3`
- r4: `qbs/preregister/qbs1-calibration-20260509-three-provider-r4`
- final successful tag:
  `qbs/preregister/qbs1-calibration-20260509-three-provider-r5`

Public artifacts:

- `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/README.md`
- `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/aggregate-results.json`
- `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/run-manifest.json`
- `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/corpus-manifest.json`
- `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/config-prompt-manifest.json`
- `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/hard-gate-results.json`
- `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/claim-statement.md`
- `docs/benchmark/runs/qbs1-calibration-20260509-three-provider/limitations.md`

## 3. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | QBS public methodology accepted | PASS |
| G1 | QBS-1 planning packet public | PASS |
| G2 | Calibration GC-018 boundary recorded | PASS |
| G3 | Public runner implemented | PASS |
| G4 | Final public pre-registration tag exists | PASS - r5 |
| G5 | Alibaba/DashScope lane executes | PASS |
| G6 | DeepSeek lane executes | PASS |
| G7 | OpenAI lane executes | PASS |
| G8 | Governed `CFG-B` receipt completeness checked | PASS |
| G9 | Secret scan clean | PASS |
| G10 | Mock fallback not detected | PASS |
| G11 | Public docs and claim boundaries aligned | PASS |
| G12 | Public repo pushed | PASS - `4a405cf Publish QBS-1 calibration pilot results` |

## 4. Calibration Result

Run ID:

`qbs1-calibration-20260509-three-provider`

Command shape:

```bash
python scripts/run_qbs_calibration_pilot.py --preregistration-tag qbs/preregister/qbs1-calibration-20260509-three-provider-r5 --env-file <local ignored env file>
```

Result:

- overall status: `PASS`
- run class: `CALIBRATION_PILOT`
- public status: `CALIBRATION_DIRECTIONAL_NO_QBS_SCORE`
- providers: Alibaba/DashScope, DeepSeek, OpenAI
- tasks: 3
- configs: 3
- configuration executions: 27/27 usable
- hard gates:
  - all configs ok: true
  - governed receipt completeness: true
  - secret scan clean: true
  - mock fallback detected: false

## 5. Claim Boundary

Public status after this roadmap:

`QBS1_CALIBRATION_PILOT_PASS_NO_PUBLIC_QBS_SCORE`

Allowed statements:

- CVF has a public QBS methodology.
- CVF has public QBS-1 runner/corpus planning.
- CVF has a QBS-1 calibration pilot that executed direct, neutral-control, and
  governed paths across Alibaba/DashScope, DeepSeek, and OpenAI.
- The pilot produced curated artifacts and live governed receipts without
  publishing secrets.

Not allowed:

- CVF has a public QBS score.
- The calibration pilot is a powered benchmark.
- The calibration pilot proves L4/L5/L6 claim levels.
- The calibration pilot proves provider parity.
- The calibration pilot proves family-level quality claims.

## 6. Next Track

The next track should remain benchmark-focused and should require a fresh
GC-018 before implementation. Recommended scope:

`QBS3-SCORED-RUN-READINESS`

Candidate work:

- expand the corpus toward the public QBS-1 design;
- finalize reviewer workflow and blinding mechanics;
- define score computation and artifact validation tooling;
- decide whether to run a small unpowered scored dry run or move directly to a
  powered single-provider scored run;
- freeze a new run-specific `qbs/preregister/<run-id>` tag before execution.

## 7. Public GitHub Alignment

Public repo:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF`

Public implementation commits:

- `c8577df Add QBS calibration pilot runner`
- `a1a5161 Fix QBS calibration runner npm launch on Windows`
- `c3fbda2 Align QBS calibration CFG-B phase authority`
- `354e7e2 Harden QBS calibration runner timeout handling`
- `97fa934 Make QBS calibration server readiness robust`

Public artifact commit:

- `4a405cf Publish QBS-1 calibration pilot results`

