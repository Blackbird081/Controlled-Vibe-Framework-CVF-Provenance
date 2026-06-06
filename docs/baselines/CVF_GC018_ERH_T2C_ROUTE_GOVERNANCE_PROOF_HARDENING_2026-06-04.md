# CVF GC-018 ERH-T2C Route Governance Proof Hardening

Memory class: POINTER_RECORD

Status: IMPLEMENTATION_COMPLETE_PENDING_REVIEW

docType: baseline

Date: 2026-06-04

Parent roadmap: `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md`

Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_T2C_ROUTE_GOVERNANCE_PROOF_HARDENING_2026-06-04.md`

dispatchBaseHead: `7c7dfc52`

## Purpose

Authorize the smallest runtime-source follow-up to ERH-T2A: add visible,
test-backed route governance proof workflow-chain coverage to the five web API
routes that the route ledger classified as `MISSING_ROUTE_GOVERNANCE_PROOF`.

## Source / Predecessor Evidence

| Predecessor | Evidence |
| --- | --- |
| ERH roadmap | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` records runtime route hardening as a remaining gap |
| Route coverage ledger | `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md` lists five `MISSING_ROUTE_GOVERNANCE_PROOF` routes |
| Existing session auth helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` exports `verifySessionCookie` |
| Existing service-token helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` exports `verifyServiceTokenRequest` |
| Existing route pattern | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` accepts session or service token |
| System-loop registry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` owns GC-052 connections |

## GC-018 Continuation Candidate

- Candidate ID: ERH-T2C
- Date: 2026-06-04
- Parent roadmap / wave: `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md`
- Proposed scope: shared route governance proof workflow chain plus focused wiring for five existing API routes and GC-052 interlock
- Continuation class: REALIZATION
- Active quality assessment: `docs/reference/CVF_ERH_T2A_ROUTE_GOVERNANCE_COVERAGE_LEDGER_2026-06-04.md`
- Assessment date: 2026-06-04
- Weighted total: 8.0/10
- Lowest dimension: live governance proof boundary (4.0/10)
- Quality-first decision: EXPAND_NOW
- Why expansion is still the better move now: ERH-T2A identified five concrete routes with missing visible governance proof, and existing session/service-token helpers already provide a low-risk implementation path.
- Quality protection commitments: no provider calls, no public-sync, no production-readiness claim, focused tests only, and all response proof fields stay secret-safe.
- Remediation target if not expanding: keep public docs caveat only and leave the route ledger gap open.
- Why now: public claim calibration is already exported, leaving the runtime route gap as the strongest next grounded hardening item.
- Active-path impact: LIMITED
- Risk if deferred: future external agents may continue treating route existence as either overclaimed governance proof or unexplained missing protection.
- Lateral alternative considered: YES
- Why not lateral shift: CI workflow hardening and evidence durability remain useful, but this tranche has clearer current runtime foundation.
- Real decision boundary improved: YES
- Expected enforcement class:
  - RUNTIME_GUARD
- Required evidence if approved:
  - shared workflow-chain helper source and focused helper test
  - five route updates with route governance proof in authorized and denied paths
  - focused route tests showing authorization and proof emission
  - GC-052 system-loop interlock evidence
  - release gate bundle result if live key is available

## Depth Audit

| Dimension | Score |
| --- | --- |
| Risk reduction | 2 |
| Decision value | 2 |
| Machine enforceability | 2 |
| Operational efficiency | 1 |
| Portfolio priority | 2 |
| Total | 9 |

Decision: CONTINUE

Reason: this closes a source-backed ERH route gap with bounded runtime changes
and focused tests, without touching provider/live behavior.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED_FOR_BOUNDED_IMPLEMENTATION

Baseline: ERH-T2A proves a complete route inventory and identifies exactly five
missing-proof routes. Current `cvf-web` already has session and service-token
auth helpers, so ERH-T2C should realize a shared proof workflow chain instead
of adding route-local patches.

Proposed tranche: create a shared `route-governance-proof` workflow chain,
wire it into the five T2A missing-proof routes, add GC-052 interlock evidence,
add focused tests, run release gate if live key is available, and file a
private completion packet.

## Authorization Boundary

Authorized now: YES

Next batch name: ERH-T2C Route Governance Proof Hardening

Forbidden expansion:

- no live/provider proof;
- no public-sync or public catalog upgrade;
- no CI workflow rewrite;
- no route behavior claim beyond session/service-token authorization and
  secret-safe proof metadata;
- no production readiness or hosted freshness claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline governs private provenance runtime-source hardening.
Public-sync export requires a separate operator-authorized public batch after
reviewed runtime evidence exists.

Next action: execute the T2C work order and update the private ERH roadmap with
bounded route-hardening evidence.

## Evidence / Verification

Required verification:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 7c7dfc52 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 7c7dfc52 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 7c7dfc52 --head HEAD
```

Post-implementation verification is owned by the T2C work order and completion
packet.

## Claim Boundary

This baseline authorizes bounded local route hardening and tests. It does not
prove live provider behavior, hosted behavior, production readiness, public
readiness, or complete CI hardening.
