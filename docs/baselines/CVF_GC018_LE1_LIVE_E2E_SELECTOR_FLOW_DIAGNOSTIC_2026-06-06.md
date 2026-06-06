# CVF GC-018 - LE1 Live E2E Selector Flow Diagnostic

Memory class: POINTER_RECORD

Status: BASELINE_ACCEPTED

Date: 2026-06-06

## Purpose

Authorize a bounded diagnostic tranche for the live Playwright governance E2E
failure recorded during MLW8-PEL1 closure. The tranche may inspect and harden
selector/test-flow reliability for the release-gate live E2E suite, then rerun
secret-safe live proof. It does not authorize provider routing changes,
governance runtime behavior changes, policy relaxation, public readiness, hosted
readiness, production readiness, cost/performance claims, or autonomous
mutation.

## Scope / Target / Owner Boundary

Target:

- live E2E selector/test-flow diagnostic for release-gate Playwright live suite;
- secret-safe diagnostic evidence and closure packet;
- session continuity update after bounded closure.

Owner boundary:

- Private provenance owns this GC-018, work order, live E2E test-flow helper
  changes, evidence, completion review, and session sync.
- Public-sync is not authorized by this baseline.
- Runtime provider routing and governance behavior are out of scope.

## 2. Authority Chain

- Operator instruction: 2026-06-06 chat instruction to continue by the old
  rule, after MLW8-PEL1 next allowed move identified the separate live-E2E
  selector/test-flow diagnostic GC-018/work order.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V16_2026-06-06.md`.
- MLW8-PEL1 completion:
  `docs/reviews/CVF_MLW8_PEL1_PROOF_EXPORT_LIVE_COMPLETION_2026-06-06.md`.
- MLW8-PEL1 live diagnostic:
  `docs/evidence/CVF_MLW8_PEL1_RELEASE_GATE_DIAGNOSTIC_2026-06-06.json`.
- Release gate owner: `scripts/run_cvf_release_gate_bundle.py`.

## Source / Predecessor Evidence

Predecessor evidence is the MLW8-PEL1 release gate result and diagnostic named
above. The only admitted failure class for this baseline is the live Playwright
selector/test-flow `locator.click` timeout recorded in those artifacts.

## 3. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| RUNTIME_BEHAVIOR - release gate runs three live E2E specs | `scripts/run_cvf_release_gate_bundle.py` | Lines 230-236 | `check_e2e` | Release gate bundle | ACCEPT |
| RUNTIME_BEHAVIOR - release gate reruns failed live E2E once | `scripts/run_cvf_release_gate_bundle.py` | Lines 255-271 | `retry_code` | Release gate bundle | ACCEPT |
| EXISTS - shared live E2E login helper exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts` | Lines 26-41 | `loginAs` | Playwright E2E utility | ACCEPT |
| EXISTS - shared Alibaba storage seed exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts` | Lines 73-89 | `seedStorageWithAlibaba` | Playwright E2E utility | ACCEPT |
| EXISTS - shared live governed execution helper exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts` | Lines 119-169 | `postLiveGovernedExecution` | Playwright E2E utility | ACCEPT |
| EXISTS - governance live spec uses shared login and live execution helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/governance-gate-live.spec.ts` | Lines 2, 15-17, 28-30, 39-41 | `login` | Playwright live governance spec | ACCEPT |
| EXISTS - noncoder live spec uses shared login and live execution helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/noncoder-governance-live.spec.ts` | Lines 2, 27-52 | `login` | Playwright noncoder live spec | ACCEPT |
| EXISTS - W113 live proof spec uses shared login and live execution helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/w113-workspace-web-live-proof.spec.ts` | Lines 2, 8-10 | `login` | Playwright W113 live proof spec | ACCEPT |
| EXISTS - MLW8-PEL1 result recorded live E2E locator click timeout | `docs/evidence/CVF_MLW8_PEL1_RELEASE_GATE_RESULT_2026-06-06.json` | Lines 44-55 | `E2E Playwright Governance (live)` | Release gate evidence JSON | ACCEPT |
| EXISTS - MLW8-PEL1 diagnostic classified locator timeout | `docs/evidence/CVF_MLW8_PEL1_RELEASE_GATE_DIAGNOSTIC_2026-06-06.json` | Lines 6-15, 24 | `live_playwright_locator_timeout` | Live run diagnostic JSON | ACCEPT |

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

Proposed tranche:

- `LE1` live E2E selector/test-flow diagnostic and bounded repair.

Allowed diagnostic changes:

- add explicit per-action timeout/fallback behavior to shared Playwright
  selector/test-flow helpers;
- update the three release-gate live specs only if the shared helper fix is
  insufficient;
- rerun focused live Playwright evidence and the release-gate bundle;
- record any live failure with a secret-safe diagnostic before rerun.

Forbidden changes:

- provider routing behavior;
- `/api/execute` governance runtime behavior;
- policy, DLP, approval, evidence, or receipt weakening;
- public-sync;
- public, hosted, production, provider-quality, cost, or performance readiness
  claims;
- memory reinjection, high-risk promotion implementation, Learning Orchestrator
  runtime behavior, or autonomous mutation.

## Evidence / Verification

Required verification:

- pre-dispatch and pre-implementation autorun gates;
- focused Playwright live diagnostic run for the release-gate specs;
- `python scripts/run_cvf_release_gate_bundle.py --json`;
- secret-safe diagnostic JSON if any live run fails, times out, or requires
  rerun;
- pre-closure and pre-push autorun gates.

## Risk Ceiling

Risk ceiling: R2 bounded live E2E diagnostic and test-flow hardening.

## Claim Boundary

This baseline may close a live E2E selector/test-flow issue and may record live
proof evidence. It does not by itself authorize public readiness, hosted
readiness, production readiness, provider superiority, cost reduction,
performance improvement, policy relaxation, or runtime governance changes.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this baseline is private diagnostic authorization only. Public-safe
export is not in scope for LE1.
