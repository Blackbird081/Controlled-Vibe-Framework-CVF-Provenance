# CVF QBS-1 Runner And Corpus Planning Roadmap

Memory class: FULL_RECORD
Status: FINAL ROADMAP - PUBLIC PUSH COMPLETE / SCORED RUN BLOCKED
Date: 2026-05-09
GC-018:
`docs/reference/CVF_GC018_QBS1_RUNNER_CORPUS_CANDIDATE_2026-05-09.md`

---

## 0. Purpose

QBS-1 translates the accepted public QBS methodology into concrete planning
artifacts for a future runner and corpus. It does not execute a benchmark.

The track exists to make the next step reviewable:

- what tasks will be used;
- what the runner must prove;
- what scores mean;
- what artifacts must be published;
- what must be frozen before a live scored run starts.

## 1. Scope

Authorized:

- public QBS-1 planning docs under `docs/benchmark/qbs-1/`;
- public README and claim-boundary alignment;
- GitHub repo description/topics alignment if available through authenticated
  GitHub CLI;
- provenance GC-018, roadmap, and handoff update.

Not authorized:

- scored benchmark execution;
- provider-cost benchmark run;
- public QBS score;
- family-level quality claim under `POWERED_SINGLE_PROVIDER`;
- pre-registration tag for a real run.

## 2. Public Artifacts

| Artifact | Purpose |
|---|---|
| `docs/benchmark/qbs-1/README.md` | QBS-1 gate state and planning index |
| `docs/benchmark/qbs-1/corpus-candidate.md` | 48-task family/slot design |
| `docs/benchmark/qbs-1/runner-contract.md` | runner input/output/failure contract |
| `docs/benchmark/qbs-1/scoring-rubric.md` | candidate scoring rubric |
| `docs/benchmark/qbs-1/artifact-layout.md` | public/private run artifact layout |
| `docs/benchmark/qbs-1/preregistration-template.md` | tag and run declaration template |

## 3. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0 | Public methodology accepted after Claude review and Codex closure | PASS |
| G1 | GC-018 candidate authorizes planning only | PASS |
| G2 | Public QBS-1 planning packet created | PASS |
| G3 | Public README/claim boundary updated | PASS |
| G4 | Public-surface scan passes | PASS |
| G5 | Public repo pushed | PASS - `cfa44ac Publish QBS-1 runner corpus planning` |
| G6 | Handoff records public commit and blocked run boundary | PASS |

## 4. Claim Boundary

Public status after this roadmap:

`QBS1_PLANNING_READY_NO_PUBLIC_QBS_RESULT`

Allowed statements:

- QBS methodology is public.
- QBS-1 runner/corpus planning is public.
- Scored runs require a run-specific public pre-registration tag.

Not allowed:

- CVF has a public QBS score.
- QBS-1 planning docs are benchmark evidence.
- Family-level QBS claims are supported by `POWERED_SINGLE_PROVIDER`.

## 5. Next Track

The next track requires a fresh GC-018 and should be named separately, for
example:

`QBS2-CALIBRATION-RUNNER-IMPLEMENTATION`

It may implement the runner and run a calibration pilot only after it defines
the exact pre-registration, cost, provider, and artifact path boundary.

## 6. Public GitHub Alignment

Public repo:

`https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF`

Public commit:

`cfa44ac Publish QBS-1 runner corpus planning`

GitHub repo metadata updated:

- description:
  `Local-first AI governance gateway for controlled agent/provider execution, audit receipts, cost signals, and public QBS benchmark methodology.`
- topics:
  `agent-governance`, `ai-governance`, `audit-trail`, `cost-control`,
  `llm-evaluation`, `local-first`, `benchmark-methodology`

