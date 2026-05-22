# CVF GC-018 E2 Operational Benchmark Suite

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_E2_OPERATIONAL_BENCHMARK_SUITE

Date: 2026-05-22

## Source or Predecessor Evidence

- `.private_reference/legacy/CVF 17.05/Review CVF.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- `docs/reviews/CVF_D2_PROVIDER_CAPABILITY_MATRIX_COMPLETION_2026-05-22.md`
- `docs/baselines/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md`

## Purpose / Decision / Baseline

Authorize E2, the operational benchmark suite phase after D2.

Decision: proceed with a bounded Governance CLI benchmark suite that computes
governance reliability metrics from audit JSONL and release-gate JSON evidence,
separating live, offline, fixture, and unknown evidence modes.

## Decision / Baseline / Proposed Tranche

Baseline: Lane E already added offline metric helpers and
`cvf benchmark governance --input <audit.jsonl>`.

Gap: the existing metric path is not yet a first-class operational benchmark
suite. It lacks a stable report envelope, evidence-mode breakdown, release-gate
JSON ingestion, retry/human-correction count metrics, and an explicit
hallucination-recovery boundary.

Proposed tranche: add `cvf.operationalBenchmark.v1` report generation and a
new `cvf benchmark operational` command while preserving existing benchmark
commands.

## Scope / Proposed Tranche

In scope:

- add operational benchmark schema and report envelope;
- compute Review-CVF operational metrics: task completion rate, retry count,
  policy violation rate, human correction count, cross-session continuity,
  long-horizon stability, receipt integrity, deterministic consistency, and
  rollback success;
- ingest audit JSONL and release-gate JSON-style evidence;
- separate live, offline, fixture, and unknown evidence modes;
- record hallucination recovery as deferred with replacement metrics;
- add tests for schema, ingestion, report formatting, and CLI command path.

Out of scope:

- new policy/risk guard semantics;
- live provider benchmarking;
- output-quality scoring or QBS rerun;
- provider stability claims;
- route changes;
- receipt-envelope changes;
- public-sync, hosted readiness, Maika proof, or freeze release.

## Blocked-Work Override

Blocked-work override: not required.

Reason: E2 computes benchmark reports from existing evidence records and adds
no new policy/risk guard semantics.

## Evidence / Required Evidence / Verification

Required evidence:

- focused operational benchmark suite tests pass;
- existing governance reliability metric tests pass;
- full Governance CLI test suite passes;
- Governance CLI TypeScript check passes;
- local governance hook chain passes before final commit.

Live provider proof:

- Not required for this phase because E2 implements an offline/evidence-ingest
  benchmark suite and does not claim new live governance behavior.

## Claim Boundary / Approval Gate

E2 closes the operational benchmark foundation only. It does not claim broad
reliability, live provider stability, output quality, or hallucination
recovery unless future evidence runs meet those separate gates.
