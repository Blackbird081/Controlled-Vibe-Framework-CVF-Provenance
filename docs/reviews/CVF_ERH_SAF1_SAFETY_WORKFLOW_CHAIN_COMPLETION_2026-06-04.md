# CVF ERH-SAF1 Safety Workflow Chain Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-04

Worker: Claude

executionBaseHead: `f7a75d59`

dispatchPacketCommit: `16c1fb68`

closureBaseHead: `f7a75d59`

GC-018: `docs/baselines/CVF_GC018_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_2026-06-04.md`

Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md`

## Purpose

Record the completion of ERH-SAF1: wiring the severity-classified safety
workflow chain into `/api/execute` after DLP and before provider execution.

## Scope / Target / Owner Boundary

Target: cvf-web `/api/execute` route module.

Implemented:
- `safety-workflow-chain.ts` server-safe helper (11 severity-classified patterns)
- route wiring: DLP → SAF1 → legacy safety → provider
- `SAFETY_WORKFLOW_CHAIN_TRIGGERED` audit event on any threat detection
- `check_erh_safety_workflow_chain.py` machine checker + 11 focused tests
- workflow-chain reference and ledger docs
- hook/autorun wiring, GC-052 registry entry

Not implemented:
- ML classifier, embedding-based jailbreak detection
- output safety/readout (SAF2 candidate)
- provider routing changes, auth edits, package manifest changes
- public-sync, production security certification

## Decision / Baseline / Proposed Tranche

Decision: `ACCEPT_WITH_CAVEAT_LIVE_ROUTE_PROOF_RESIDUAL`

Baseline: ERH-RS1 confirmed `ERH-SAF1_READY`. All five SAF1 readiness rules
satisfied. Route order DLP → SAF1 → legacy safety → provider is now enforced
by source-visible machine checker. Route size is within limit (890 lines, hard
limit 1000).

Reviewer disposition: Codex accepts the SAF1 source implementation, focused
tests, machine checker, hook wiring, ledger, and bounded SAF2 recommendation.
The acceptance is bounded because Playwright live governance proof remains
blocked by the recorded port 3001 infrastructure conflict. SAF1 must not be
used as a release-quality/live-proven governance claim until that live route
proof is rerun successfully.

## Source / Predecessor Evidence

| Source | Purpose | Disposition |
| --- | --- | --- |
| `docs/assessments/CVF_ERH_RS1_EXTERNAL_REVIEW_FULL_COVERAGE_RESCAN_2026-06-04.md` | SAF1 readiness basis | ACCEPTED |
| cvf-web `safety-status.ts` | pattern source (not imported directly) | READ_ONLY — patterns re-owned in server-safe helper |
| cvf-web `safety.ts` | legacy safety (preserved) | UNCHANGED_API |
| cvf-web `/api/execute` route module | wiring target | MODIFIED (SAF1 import + call + audit event) |

## Findings / Position

| Item | Finding | Disposition |
| --- | --- | --- |
| SAF1 helper created | `safety-workflow-chain.ts` — server-safe, 11 patterns | PASS |
| No direct server import of safety-status.ts | verified — route imports from safety-workflow-chain only | PASS |
| safety-status.ts `'use client'` preserved | confirmed unchanged | PASS |
| Route order DLP → SAF1 → legacy → provider | verified in source and enforced by SAF1 checker | PASS |
| Audit event on SAF1 block/escalation | `SAFETY_WORKFLOW_CHAIN_TRIGGERED` emitted | PASS |
| Audit payload contains no raw prompt text | payload uses labels/counts/severities only | PASS |
| Legacy `applySafetyFilters` compatibility | legacy safety called on SAF1-sanitized prompt | PASS |
| SAF1 helper tests | 16/16 PASS | PASS |
| Route injection test | `blocks prompt injection via safety filter` — 31/31 PASS | PASS |
| TypeScript check | PASS | PASS |
| Build | PASS | PASS |
| SAF1 checker | PASS | PASS |
| Checker tests | 13/13 PASS | PASS |
| Route line count | 890 (hard limit 1000) | PASS |

## Risk / Corrective Action

| Risk | Corrective action | Status |
| --- | --- | --- |
| MEDIUM patterns (LOG only) may not block adversarial prompts | by design — MEDIUM is LOG/STRIP only; CRITICAL/HIGH block; claim boundary explicit | ACCEPTED |
| Legacy safety.ts still runs after SAF1 | by design — backward compatibility; no duplicate block risk since SAF1 strips before legacy | ACCEPTED |
| Port 3001 conflict blocked Playwright E2E live gate | pre-existing infrastructure issue; not SAF1-caused; 5/7 release gates PASS | DOCUMENTED |

## Evidence / Verification

| Check | Result |
| --- | --- |
| `git rev-parse --short HEAD` at start | `f7a75d59` |
| Worktree at start | dispatch packet untracked; otherwise clean |
| Pre-implementation gate | PASS |
| `npm run check` | PASS |
| `npm run build` | PASS |
| `safety-workflow-chain.test.ts` | 16/16 PASS |
| `route.test.ts` | 31/31 PASS (including injection block) |
| `check_erh_safety_workflow_chain.py --enforce` | PASS |
| `pytest test_check_erh_safety_workflow_chain.py -q` | 13/13 PASS |
| Release gate: Web build | PASS |
| Release gate: TypeScript check (guard contract) | PASS |
| Release gate: Provider readiness | PASS — CERTIFIED lanes: 3 |
| Release gate: Secrets scan | PASS |
| Release gate: Docs governance (RC docs present) | PASS |
| Release gate: E2E Playwright UI (mock) | FAIL — port 3001 occupied (pre-existing infrastructure conflict) |
| Release gate: E2E Playwright Governance (live) | FAIL — port 3001 occupied (pre-existing infrastructure conflict) |
| `git diff --name-status f7a75d59 HEAD` | pending SAF1 source/docs/governance diff within Allowed scope |
| SAF1 route wiring boundary | no package/lockfile/auth/provider/rate-limit/public-sync changes |

### Reviewer Verification Addendum

| Check | Reviewer result |
| --- | --- |
| `python governance/compat/check_erh_safety_workflow_chain.py --enforce` | PASS |
| `python -m pytest governance/compat/test_check_erh_safety_workflow_chain.py -q` | 13/13 PASS |
| `npm run check` | PASS |
| `npx vitest run src/lib/safety-workflow-chain.test.ts` | 16/16 PASS |
| `npx vitest run src/app/api/execute/route.test.ts` | 31/31 PASS |
| `npm run build` | PASS with pre-existing `source-map-support` warning |
| `python governance/compat/check_work_order_dispatch_quality.py --base f7a75d59 --head HEAD --enforce` | PASS |
| `python governance/compat/check_machine_closure_package.py --base f7a75d59 --head HEAD --enforce` | PASS |

## Live Run Diagnostics

| Stage | Class | Retryability | Target | Result | Safe message |
| --- | --- | --- | --- | --- | --- |
| Release gate — E2E Playwright UI (mock) | INFRASTRUCTURE_CONFLICT | RETRYABLE_AFTER_PORT_FREE | `http://localhost:3001` | FAIL — port already in use | Another process occupies port 3001; stop that process before rerunning E2E gates |
| Release gate — E2E Playwright Governance (live) | INFRASTRUCTURE_CONFLICT | RETRYABLE_AFTER_PORT_FREE | `http://localhost:3001` | FAIL — port already in use | Same port conflict; not caused by SAF1 changes |
| Secret/quota consumed | N/A | N/A | N/A | no secrets printed; live key existence check only | Zero cost path for non-live gates |

Pre-existing: port 3001 conflict also blocked Playwright in prior sessions unrelated to SAF1. SAF1 source changes do not affect port configuration.

## SAF2 Decision

**Verdict: `SAF2_READY`**

Rationale:

- SAF1 focused tests PASS (16/16 helper + 31/31 route including injection block).
- 5/7 release gates PASS; 2 Playwright failures are port-conflict infrastructure
  issues pre-dating SAF1.
- Source-visible remaining safety gaps that could form bounded SAF2 scope:
  1. **Output safety/readout**: no safety check on AI provider output before
     returning to client; a deterministic output screen (e.g., detect
     instruction-following failures, governance-relevant leakage in output)
     could be added without ML.
  2. **Safety regression corpus**: no automated adversarial prompt regression
     test corpus; a bounded `.safety.regression.test.ts` file with documented
     adversarial cases would catch future regressions.
  3. **Safety coverage drift checker**: no checker verifying that new route
     code paths pass through the safety chain.
- SAF2 must remain separate; it must not require ML classifiers, provider
  prompt changes, output-quality tuning, package changes, live quota expansion,
  or broad security claims.

## Reviewer Checklist

| Item | Expected result |
| --- | --- |
| `safety-workflow-chain.ts` imports no client-only module | VERIFY — no `'use client'` or import from safety-status.ts |
| Route order: DLP before SAF1 before legacy safety before provider | VERIFY — machine checker enforces marker order |
| Audit payload does not store raw prompt | VERIFY — auditPayload uses labels/counts only |
| `safety-status.ts` still has `'use client'` | VERIFY |
| No package.json or lockfile changes | VERIFY |
| No auth runtime, provider router, rate-limiter changes | VERIFY |
| Completion does not claim ML DLP or production security | VERIFY |

## Core Guard Self-Protection Authorization

Operator authorization: 2026-06-04 operator authorized opening ERH-SAF1 Safety
Workflow Chain and, after SAF1, assessing SAF2.

Authorized guard-maintenance scope: added one ERH-SAF1 safety workflow-chain
checker, focused tests, hook/autorun wiring, GC-052 registry entry, and bounded
reviewer remediation to enforce route marker order.

Protected paths updated:
- `governance/compat/check_erh_safety_workflow_chain.py`
- `governance/compat/test_check_erh_safety_workflow_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (reviewer continuity sync only)
- `CVF_SESSION_MEMORY.md` (reviewer continuity sync only)
- `AGENT_HANDOFF_V15_2026-05-29.md` (reviewer continuity sync only)

Rollback boundary: revert the SAF1 closure commit. No unrelated guard
semantics, public-sync, auth runtime, or package changes are authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | this packet | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | SAF1 row closed bounded; SAF2 ready for separate work order | PASS |
| Registry JSON | `N/A with reason` | no corpus scan registry state changed; SAF1 is runtime safety wiring, not corpus/search/classification closure | BLOCKED with reason |
| Registry Markdown | `N/A with reason` | no corpus registry markdown state changed; SAF1 is runtime safety wiring, not corpus/search/classification closure | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no external corpus/source digest consumed | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | erh-saf1-safety-workflow-chain connection added (12 connections) | PASS |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up handoff sync commit required after reviewer commit | PASS |

## Deliverables

| Artifact | Path | Mode |
| --- | --- | --- |
| SAF1 helper | cvf-web `safety-workflow-chain.ts` | created |
| SAF1 helper tests | cvf-web `safety-workflow-chain.test.ts` | created (16/16 PASS) |
| Route wiring | cvf-web `/api/execute` route module | modified (import + SAF1 call + audit event) |
| Workflow chain reference | `docs/reference/CVF_ERH_SAF1_SAFETY_WORKFLOW_CHAIN_2026-06-04.md` | created |
| Workflow ledger | `docs/reference/CVF_ERH_SAF1_SAFETY_WORKFLOW_LEDGER_2026-06-04.md` | created |
| Checker | `governance/compat/check_erh_safety_workflow_chain.py` | created |
| Checker tests | `governance/compat/test_check_erh_safety_workflow_chain.py` | created (13/13 PASS) |
| Hook chain wiring | `governance/compat/run_local_governance_hook_chain.py` | updated |
| Autorun gate wiring | `governance/compat/run_agent_autorun_workflow_gate.py` | updated |
| GC-052 connection | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | updated (12 connections) |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Safety layer expanded from 4 to 11 severity-classified patterns | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_ADDED | SAF1 checker enforces route wiring and DLP → SAF1 → legacy → provider order in hook/autorun |
| Richer patterns existed only in client-side helper | ROUTE_COVERAGE_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_ADDED | checker verifies no direct safety-status.ts server import |
| SAF2 output safety, regression corpus, drift checker identified as next candidates | SCOPE_BOUNDARY_GAP | GOVERNANCE_CONTROL_PLANE | ROADMAP_CANDIDATE | open SAF2 work order when operator authorizes |
| Playwright E2E blocked by port conflict | INFRASTRUCTURE_CONFLICT | RUNTIME_BEHAVIOR_LEARNING | INVESTIGATION_DEFERRED | resolve port 3001 conflict in a separate infrastructure pass |
| Runtime/provider/cost learning lane | N/A_WITH_REASON | N/A_WITH_REASON | N/A_WITH_REASON | SAF1 is deterministic pattern change; no live provider cost expansion performed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime safety hardening. Public-facing safety claim update
requires a separate public-sync work order after SAF1 is reviewed and accepted.

## Claim Boundary

This completion records bounded deterministic severity-classified safety
workflow-chain wiring with focused test and machine-checker evidence. It does
not prove ML DLP, comprehensive jailbreak protection, production security
readiness, hosted readiness, public readiness, complete external-review
remediation, or Playwright E2E live governance behavior (port conflict blocked).
