# GC-018: W4 Operational Benchmark Scorecard

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: baseline

Date: 2026-05-24

Roadmap: `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`

Work Order: `docs/work_orders/CVF_WO_W4_OPERATIONAL_BENCHMARK_SCORECARD_2026-05-24.md`

---

## Purpose

Authorize WC-3 Candidate 4 as W4: extend the existing Governance CLI
operational benchmark report into an operator-readable scorecard over existing
evidence logs, receipts, and diagnostics.

The immediate correction is clarity: benchmark reports that emit multiple
events per live call must surface call-level pass rate separately from
event-model metric denominators so raw event ratios cannot be misread as
execution failure.

## Scope / Target / Owner Boundary

In scope:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/operational-benchmark-suite.test.ts`
- W4 completion review, WC roadmap, session state, and handoff updates

Out of scope:

- new live provider benchmarking or broad provider soak loops;
- output-quality scoring or QBS rerun;
- provider adapter, model routing, or `/api/execute` changes;
- receipt-envelope schema changes;
- new observability dashboard/runtime;
- public-sync, hosted-readiness, production-readiness, or freeze-release claims.

Owner surface: existing Governance CLI operational benchmark suite.

## Depth Audit

Depth score: 8/10.

Rationale:

- WC-3 ranks operational benchmark scorecard as Candidate 4 because live
  receipts and diagnostics need to become user-facing reliability evidence, not
  raw event math.
- E2 already delivered `cvf.operationalBenchmark.v1`, so W4 can improve the
  report surface without opening new runtime behavior.
- The latest Claude review identified a concrete clarity defect: `5/5` live
  calls can appear as `0.5` event-model ratios when each call emits two
  benchmark events.
- The highest risk is overclaiming reliability. W4 therefore authorizes only
  local evidence-ingest scoring and table output.

## Source / Predecessor Evidence

- WC roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- WC-3 map:
  `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- WC-4 blind-spot standard:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Live-run diagnostic standard:
  `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- E2 operational benchmark closure:
  `docs/reviews/archive/CVF_E2_OPERATIONAL_BENCHMARK_SUITE_COMPLETION_2026-05-22.md`
- S3 live benchmark evidence model:
  `scripts/run_cvf_s3_governance_benchmark_probe.mjs`

## Decision / Baseline / Proposed Tranche

Decision: continue with W4 as the fourth W-series implementation tranche.

Baseline: CVF can ingest audit JSONL and release-gate JSON into an operational
benchmark report, but the report does not yet expose a first-class scorecard
with call-level result, event denominator, diagnostics, failure-class counts,
and operator guidance.

Proposed tranche:

- add `scorecard` to `cvf.operationalBenchmark.v1`;
- compute distinct call/execution counts separately from event counts;
- expose `callPassRate` and `eventModelDenominator`;
- count diagnostic classes and user actions when present;
- classify benchmark clarity posture as `clear`, `needs_context`, or
  `insufficient_evidence`;
- add table output that clearly labels call-level results and event-model
  denominators.

## Knowledge Absorption Blind-Spot Control Block

- Standard read:
  `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- Source inventory:
  - `.private_reference/legacy/CVF 16.5/abtop/` — 11 files
  - `.private_reference/legacy/CVF ADD/AI-first vs Human-first/` — 9 files
  - `.private_reference/legacy/CVF Edit/` — 10 files
  - `.private_reference/legacy/CVF ADD/REVIEW FOLDER/` — 13 files
  - active Governance CLI benchmark files and S3 probe script
- Prior absorption evidence resolved:
  - `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
  - `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md`
  - `docs/reviews/archive/CVF_E2_OPERATIONAL_BENCHMARK_SUITE_COMPLETION_2026-05-22.md`
  - `docs/work_orders/archive/CVF_WO_E2_OPERATIONAL_BENCHMARK_SUITE_2026-05-22.md`
  - `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- Detailed source files used:
  - `.private_reference/legacy/CVF 16.5/abtop/CVF_OBSERVABILITY_PLANE_FOUNDATION/README.md`
  - `.private_reference/legacy/CVF 16.5/abtop/CVF_OBSERVABILITY_PLANE_FOUNDATION/CVF_OBSERVABILITY_PLANE.md`
  - `.private_reference/legacy/CVF 16.5/abtop/CVF_OBSERVABILITY_PLANE_FOUNDATION/CVF_DASHBOARD_EVENT_STREAM.md`
  - `.private_reference/legacy/CVF 16.5/abtop/CVF_OBSERVABILITY_PLANE_FOUNDATION/CVF_AGENT_SESSION_MONITOR.md`
  - `.private_reference/legacy/CVF ADD/AI-first vs Human-first/CVF_GOVERNANCE_FRICTION_AUDIT.md`
  - `.private_reference/legacy/CVF ADD/AI-first vs Human-first/CVF_W7_EVAL_OVERCONSTRAINT_SIGNALS.md`
  - `.private_reference/legacy/CVF ADD/AI-first vs Human-first/CVF_POLICY_GATE_MINIMAL_RESPONSE.md`
  - `.private_reference/legacy/CVF ADD/AI-first vs Human-first/CVF_PATTERN_OVERCONSTRAINT_FEEDBACK.md`
  - `.private_reference/legacy/CVF Edit/CVF_EDIT_ANALYSIS.md`
  - `.private_reference/legacy/CVF Edit/CVF AUDIT LOG_md`
  - `.private_reference/legacy/CVF Edit/Failure Simulation cho CVF.md`
  - `.private_reference/legacy/CVF Edit/Review CVF_4.md`
  - `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_KNOWLEDGE_ABSORPTION_EXECUTIVE_ASSESSMENT_2026-05-06.md`
  - `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_OWNER_SURFACE_PROMOTION_MAP_2026-05-06.md`
  - `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_FINAL_ACCEPTED_VALUE_AND_REJECTION_MAP_2026-05-07.md`
  - `.private_reference/legacy/CVF ADD/REVIEW FOLDER/CVF_ADD_SOURCE_FILE_REUSE_AND_NORMALIZATION_APPENDIX_2026-05-07.md`
  - `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
  - `scripts/run_cvf_s3_governance_benchmark_probe.mjs`
- Source families skipped:
  - provider method normalization: Candidate 5, not W4.
  - runtime observability dashboard/event stream: valuable but outside a
    scorecard-only tranche.
  - new live soak evidence: rejected for W4 because existing evidence ingest
    is sufficient and avoids burning quota.
  - output-quality and hallucination scoring: still lacks a bounded event
    contract and remains deferred.
- File-level accepted value:
  - abtop: observability should be read-first, source-tagged, append-only,
    policy-aware, auditable, and never an execution authority.
  - CVF Edit audit/failure files: benchmark output must trace real execution
    steps, show failure modes, and distinguish detection from recovery.
  - AI-first vs Human-first: operational scoring must include friction and
    overconstraint signals, not only blocking success.
  - E2/S3 evidence: event-model ratios are useful but must not hide
    call-level pass/fail results.
- Owner-surface normalization:
  - scorecard -> existing Governance CLI operational benchmark report;
  - diagnostic clarity -> V3 live-run diagnostic standard vocabulary;
  - friction signals -> scorecard advisory fields only, not policy gates;
  - future dashboard -> demand-gated later observability work.
- Accept/defer/reject matrix:
  - ACCEPT_NOW: call-level pass rate, event denominator, diagnostic class/user
    action counts, benchmark clarity status, table output labels.
  - ACCEPT_AS_OWNER_MAP: abtop event-stream concepts map to future
    observability plane, not W4 runtime.
  - ACCEPT_AS_DOCTRINE: overconstraint/friction signals inform advisory
    scorecard dimensions only.
  - DEFER_DEMAND_GATED: dashboard runtime, process/session monitor, provider
    soak, public claim packaging, hallucination recovery.
  - REJECT_DIRECT: autonomous observability control, hidden live reruns,
    output-quality claims from operational receipts, and silent denominator
    ambiguity.
- Adversarial roles completed:
  - Implementer: extend the existing operational benchmark report; do not make
    a new benchmark engine.
  - Skeptic/Auditor: a scorecard over fixtures does not prove provider
    reliability; closure must state evidence-ingest only unless release gate is
    run separately.
  - Product/Operator Advocate: the operator should see `5/5 calls PASS` and
    `5/10 events` side by side, with diagnostic actions when failures exist.
  - Safety/Boundary Owner: scorecard cannot execute, approve, retry, reroute,
    mutate policy, or suppress critical diagnostics.
- Thin proof target:
  - focused CLI tests prove distinct calls and event denominators are reported
    separately, diagnostic classes are counted, and table output labels the
    difference.
- Blind-spot verdict: CLEAR

## Authorized Change

Implement W4 as a bounded Governance CLI scorecard extension:

- add scorecard types and builder logic inside the existing operational
  benchmark suite;
- preserve `cvf.operationalBenchmark.v1` schema version for backward
  compatibility by adding fields;
- keep all logic evidence-ingest only and side-effect free;
- update tests and table output;
- file completion review and update roadmap/session/handoff.

## Evidence Plan

- `npm run test -- tests/operational-benchmark-suite.test.ts`
- `npm run test -- tests/operational-benchmark-suite.test.ts tests/governance-reliability-metrics.test.ts`
- `npm run check`
- markdown/session governance guards
- release gate only if closure asserts live governance health beyond local
  evidence-ingest behavior.

## Acceptance Criteria

- [ ] Scorecard reports call-level pass rate separately from event-model
      denominator.
- [ ] Scorecard reports diagnostic class and user-action counts when present.
- [ ] Table output labels `callLevel` and `eventModel` so event ratios are not
      confused with execution pass rate.
- [ ] Scorecard includes a claim boundary and clarity status.
- [ ] Existing `cvf benchmark operational` behavior remains compatible.
- [ ] Focused Governance CLI tests PASS.
- [ ] Completion review filed and session/handoff updated.

## Claim Boundary

W4 may claim only local operational scorecard generation from existing evidence
records. It does not claim new live governance behavior, provider reliability,
output quality, hallucination recovery, autonomous observability, public
readiness, production readiness, or freeze release.
