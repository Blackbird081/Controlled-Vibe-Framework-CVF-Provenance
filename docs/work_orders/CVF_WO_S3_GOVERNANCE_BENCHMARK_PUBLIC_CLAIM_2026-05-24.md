# CVF Work Order: S3 — Governance Benchmark Public Claim

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-24

Tranche: S3

Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Run the existing E2 governance benchmark suite against the live hosted
`/api/execute` target, record at least 3 live metric values, and publish a
bounded `governance benchmark` capability row in the public technical catalog.

This closes the gap between E2's defined-but-unrun metrics and a public-facing
evidence claim.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_2026-05-24.md`
- Roadmap: `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`
- E2 deliverables:
  - `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
  - `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
- Public catalog: `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
  (public-sync)
- Public catalog rule: `CLAUDE.md` — "Public Catalog Update Rule (GC-024)"

---

## Scope / Target / Owner Boundary

Target surfaces:

- E2 benchmark types and metric definitions (read-only — do not modify).
- New probe script: `scripts/run_cvf_s3_governance_benchmark_probe.mjs`
- Evidence: `docs/reviews/CVF_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_EVIDENCE_2026-05-24.json`
- Public catalog (public-sync clone):
  `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- Setup guide link: `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`
  (public-safe reference for catalog evidence path)

Out of scope:

- Modifying E2 source files.
- Adding new metric types.
- Claiming enterprise benchmark certification.
- Any route, memory, or kernel surface modification.
- Publishing private review content to public-sync.

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Read E2 sources fully; design minimal probe that exercises live path for 3+ metrics. |
| Implementer | Write probe script; run against live hosted target. |
| QA | Verify live receipt; confirm metrics have real values; confirm no raw key in output. |
| Governance Reviewer | Confirm claim is bounded; public evidence path is public-safe; Test-Path PASS. |
| Release Manager | Update public catalog; verify Test-Path; file completion review; commit. |

---

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
  — ALL content. Must read before designing probe.
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
  — ALL content. Must read before designing probe.
- `docs/reviews/CVF_R2_EXECUTE_ROUTE_DURABLE_MEMORY_WIRING_COMPLETION_2026-05-24.md`
  (live proof pattern to reference for probe design)
- `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`
  (public-safe artifact to use as catalog evidence pointer)
- `CLAUDE.md` — "Public Catalog Update Rule (GC-024)" section.
- `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Write Ownership

- `scripts/run_cvf_s3_governance_benchmark_probe.mjs` (new script)
- `docs/reviews/CVF_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_EVIDENCE_2026-05-24.json`
- Public catalog (public-sync clone):
  `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- `docs/reviews/CVF_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_COMPLETION_2026-05-24.md`
- `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md` — update S3
  row to `CLOSED_PASS`.

---

## Pre-Flight Checks

- Confirm hosted target is reachable:
  `https://vibcode.netlify.app/api/execute`.
- Confirm live provider key available (Alibaba preferred). Do not print.
- Confirm public-sync clone is accessible for catalog update.
- Confirm public-sync remote is
  `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`
  before any write.

---

## Allowed / Forbidden Scope

Allowed:

- Read E2 `OperationalBenchmarkReport` and `GovernanceReliabilityMetrics`
  types to design probe metrics.
- Write probe script that fires ≥3 governed `/api/execute` calls, records
  receipts, and computes `taskCompletionRate`, `policyViolationRate`, and
  `receiptIntegrityRate` from live evidence.
- Additional metrics if live data supports them.
- File private evidence JSON.
- Add bounded `governance benchmark` row to public catalog.
- Evidence path in catalog: public-safe guide or evidence artifact (no private
  review, no raw receipt, no service-token header).
- Run Test-Path from public-sync clone on every modified path.
- Commit governance repo first, then public-sync update separately.

Forbidden:

- Modifying `operational-benchmark-suite.ts` or `governance-reliability-metrics.ts`.
- Publishing `docs/reviews/`, `docs/baselines/`, or `docs/roadmaps/` to
  public-sync.
- Claiming metric values not backed by live run evidence.
- Printing raw API keys, service tokens, or signed headers.
- Claiming enterprise benchmark certification or SLA-level guarantees.

---

## Metric Definitions (from E2 — read source for full context)

Minimum required (from `OperationalBenchmarkReport`):

- `taskCompletionRate`: fraction of executions that returned `success=true`.
- `policyViolationRate`: fraction of executions where policy was bypassed or
  receipt was absent.
- `receiptIntegrityRate`: fraction of executions where
  `governanceEvidenceReceipt` was present and valid.

Probe design: run N executions (minimum 5 recommended), collect receipts,
compute the three rates from live results.

---

## Execution Plan

1. Read required first reads. Note E2 metric types fully.
2. Design probe: N live executions, collect receipts, compute rates.
3. Write `run_cvf_s3_governance_benchmark_probe.mjs`.
4. Run probe against `https://vibcode.netlify.app/api/execute` with live
   Alibaba key. `rawSecretPrinted=false` enforced.
5. Record evidence JSON with: probe run timestamp, N, receipts summary,
   metric values, and `rawSecretPrinted=false` confirmation.
6. Update public catalog in public-sync clone:
   a. Add `governance benchmark` row with metric values and evidence path.
   b. Evidence path: `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`
      or a new public-safe benchmark summary artifact — not private reviews.
   c. Run Test-Path on every modified path from public-sync clone.
7. File completion review with bounded claim language.
8. Commit governance repo artifacts.
9. Commit public-sync update separately.

---

## Evidence Requirements

- Probe script run log with ≥5 live receipts.
- Metric values: `taskCompletionRate`, `policyViolationRate`,
  `receiptIntegrityRate` with real numbers from live run.
- Evidence JSON filed.
- Public catalog diff with bounded row and Test-Path PASS.
- `rawSecretPrinted=false` confirmed for all probe calls.
- Completion review filed with exact metric values.

---

## Acceptance Criteria

- [ ] E2 sources read (cite `OperationalBenchmarkReport` field names in review).
- [ ] Probe script produces ≥3 live metric values from live run.
- [ ] Evidence JSON filed.
- [ ] Public catalog row added with bounded claim and public-safe evidence path.
- [ ] Test-Path PASS from public-sync clone for all modified paths.
- [ ] No raw key or private review path in any public artifact.
- [ ] Completion review filed with exact metric values.
- [ ] No modification to E2 source files.

---

## Review Gate

The completion review must confirm:

- E2 sources were read and cited.
- Metric values come from live run evidence (cite probe receipts).
- Public catalog evidence path is public-safe (no private review reference).
- Test-Path verified from public-sync clone before commit.
- No raw API key or signed header in any public artifact.
- Claim language is bounded to exact measured values only.

---

## Operator Checkpoint

Operator authorized S3 on 2026-05-24. Public-sync remote must be verified
before catalog update.

Codex must self-execute and return the final result after tranche completion.

---

## Closure Checklist

- [ ] E2 sources read.
- [ ] Probe script written and run.
- [ ] Live metric values recorded.
- [ ] Evidence JSON filed.
- [ ] Public catalog updated.
- [ ] Test-Path PASS from public-sync.
- [ ] Completion review filed and committed.
- [ ] No raw key in any artifact.

---

## Return-To-Orchestrator Conditions

Return blocked if: hosted target unreachable, all probe calls fail, metric
computation produces no valid values, Test-Path fails on public catalog, or
public-sync remote cannot be verified.

---

## Tasks

| Task | Status | Output |
| --- | --- | --- |
| Read E2 sources | DONE | Types and metric definitions noted. |
| Design + write probe | DONE | `scripts/run_cvf_s3_governance_benchmark_probe.mjs` |
| Run probe (≥5 live calls) | DONE | ≥3 metric values from live run. |
| Evidence JSON | DONE | Filed. |
| Public catalog update | DONE | Row added, Test-Path PASS. |
| Completion review | DONE | Filed with exact metric values. |

---

## Claim Boundary

S3 claims a bounded governance benchmark with live metric evidence for at
least 3 of 9 E2 metrics against the live hosted target. It does not claim
perfect metrics, SLA-level availability, enterprise production readiness, or
universal benchmark coverage. Claim language must state exact measured values
(e.g., `taskCompletionRate=1.0 from 5 live calls`) — not "high quality" or
"production-grade".
