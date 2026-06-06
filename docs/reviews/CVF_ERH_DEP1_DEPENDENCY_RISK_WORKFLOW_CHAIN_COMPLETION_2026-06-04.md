# CVF ERH-DEP1 Dependency Risk Workflow Chain Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-04

Worker: Claude

dispatchBaseHead: `24915dec`

executionBaseHead: `24915dec`

closureBaseHead: `6d10b379`

Reviewer disposition: ACCEPT_WITH_CAVEAT

GC-018: `docs/baselines/CVF_GC018_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_2026-06-04.md`

Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md`

## Purpose

Record the completion of the ERH-DEP1 dependency risk workflow chain implemented
by Claude and accepted by Codex/operator with caveat.

## Scope / Target / Owner Boundary

Target: `next-auth` beta dependency risk workflow chain for `cvf-web`.

Boundary: this completion records Claude's implementation. It does not claim
dependency migration, auth runtime security, hosted readiness, production
readiness, or public-sync export.

## Source / Predecessor Evidence

| Source | Purpose | Disposition |
| --- | --- | --- |
| `docs/baselines/CVF_ERH_T4_NEXT_AUTH_BETA_DECISION_BASELINE_2026-06-04.md` | upstream dependency decision | ACCEPTED |
| `docs/reference/CVF_ERH_PD1_PUBLIC_SURFACE_DRIFT_LEDGER_2026-06-04.md` | public-surface drift boundary | ACCEPTED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` line 30 | declared `^5.0.0-beta.30` range | VERIFIED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` line 8641 | resolves to `5.0.0-beta.31` | VERIFIED |
| `npm view next-auth version dist-tags --json` fresh run 2026-06-04 | latest stable=4.24.14; beta=5.0.0-beta.31; no stable v5 exists | RECORDED |
| `npm audit --json` fresh run 2026-06-04 | 14 vulnerabilities (3 critical/7 high/4 moderate); 0 from next-auth itself | CLASSIFIED |

## Decision / Baseline / Proposed Tranche

Decision: `ACCEPT_WITH_CAVEAT`

Rationale:

- No stable v5 available; downgrade to v4 would be API-incompatible.
- Current scope is private/prototype, not hosted production.
- Beta dependency must be disclosed in public docs (deferred to ERH-T1B).
- DEP2 migration work order must be opened when stable v5 ships or
  production auth claim is made.

## Findings / Position

| Item | Finding | Disposition |
| --- | --- | --- |
| next-auth declared version | `^5.0.0-beta.30` resolves to `5.0.0-beta.31`; no stable v5 exists upstream | ACCEPT_WITH_CAVEAT |
| Audit CVE exposure | 14 vulns total; 0 from next-auth itself; all toolchain/framework scope | CLASSIFIED_OUT_OF_SCOPE_FOR_DEP1 |
| Auth touchpoints | 4 touchpoints (`auth.ts`, `middleware.ts`, `middleware-auth.ts`, tests) identified | DOCUMENTED |
| Checker gate | `check_erh_dependency_risk_workflow.py` created, 12/12 tests pass, wired into hook and autorun | PASS |
| Package/lockfile diff | No changes — migration not performed | CLEAN |
| GC-052 connection | `erh-dependency-risk-workflow-chain` added (10 connections total) | WIRED |

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| `next` framework high/moderate vulns gated on semver-major upgrade | Open separate `next` upgrade work order; not in ERH-DEP1 scope |
| Critical dev-toolchain vulns (`vitest`, `@vitest/coverage-v8`, `jspdf`) | Fix in separate toolchain upgrade pass; not auth-security risk |
| Public caveat for next-auth beta not yet exported | Handled in ERH-T1B public-sync work order per PD1 drift ledger |
| Migration required when stable v5 ships | Open DEP2 work order at that time; checker will alert if beta marker removed without DEP2 |

## Evidence / Verification

| Check | Result |
| --- | --- |
| `npm view next-auth version dist-tags --json` | PASS — fresh result recorded in ledger; beta=5.0.0-beta.31; no stable v5 |
| `npm audit --json` | CLASSIFIED — 14 vulnerabilities, 0 from next-auth itself; all toolchain/framework scope |
| `python -m pytest governance/compat/test_check_erh_dependency_risk_workflow.py -q` | 12/12 PASS |
| `python governance/compat/check_erh_dependency_risk_workflow.py --enforce` | PASS |
| `python governance/compat/check_system_loop_interlock.py --base 24915dec --head HEAD --enforce` | PASS — 10 connections, 0 violations |
| `python governance/compat/check_markdown_structural_completeness.py --base 24915dec --head HEAD --all-changed --enforce` | PASS |
| `python governance/compat/check_work_order_dispatch_quality.py --base 24915dec --head HEAD --enforce` | PASS |
| `python governance/compat/check_public_export_disposition.py --base 24915dec --head HEAD --enforce` | PASS |
| `python governance/compat/check_finding_to_governance_learning.py --base 24915dec --head HEAD --enforce` | PASS |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 6d10b379 --head HEAD` | EXPECTED FAIL before commit — uncommitted worktree; all content gates passed after core-guard authorization |
| Package diff | CLEAN — no package.json or package-lock.json changes |
| Auth runtime diff | CLEAN — no auth runtime source changes |

## Deliverables

| Artifact | Path | Mode |
| --- | --- | --- |
| Dependency risk workflow chain | `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_2026-06-04.md` | created |
| Dependency risk ledger | `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_LEDGER_2026-06-04.md` | created |
| Checker | `governance/compat/check_erh_dependency_risk_workflow.py` | created |
| Focused tests | `governance/compat/test_check_erh_dependency_risk_workflow.py` | created (12/12 PASS) |
| Hook chain wiring | `governance/compat/run_local_governance_hook_chain.py` | updated |
| Autorun gate wiring | `governance/compat/run_agent_autorun_workflow_gate.py` | updated |
| GC-052 connection | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | updated (10 connections) |
| Roadmap DEP1 status update | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | updated |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: ERH-DEP1 adds one bounded dependency-risk
checker and wires it into the existing local hook and autorun gate chains.

Protected paths:

- `governance/compat/check_erh_dependency_risk_workflow.py`
- `governance/compat/test_check_erh_dependency_risk_workflow.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`

Operator authorization: ERH-DEP1 was dispatched by Codex for Claude from
`docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md`.

Rollback boundary: revert the four protected-path changes above and remove the
matching ERH-DEP1 reference/ledger/review artifacts if the checker is rejected.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_FOR_CLAUDE_2026-06-04.md` | `Status: CLOSED_PASS_BOUNDED`; worker honored `WORKER_MUST_NOT_COMMIT` | PASS - work order closed after reviewer acceptance |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | `Status: CLOSED_PASS_BOUNDED`; `Reviewer disposition: ACCEPT_WITH_CAVEAT` | PASS - accepted with caveat |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH-DEP1 row updated to `ACCEPTED_BOUNDED` | PASS - roadmap aligned |
| Registry JSON | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | connection id `erh-dependency-risk-workflow-chain` | PASS - GC-052 connection registered |
| Registry Markdown | `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_2026-06-04.md` | `Decision: ACCEPT_WITH_CAVEAT`; checker marker in ledger | PASS - reference and ledger aligned |
| External evidence digest | `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_LEDGER_2026-06-04.md` | npm metadata and audit snapshot recorded | PASS - external dependency metadata summarized |
| System loop interlock | `governance/compat/check_system_loop_interlock.py --base 6d10b379 --head HEAD --enforce` | 0 violations | PASS - interlock gate passed |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | handoff remains active; update after commit if active-session gate requires sync | N/A with reason - closure batch did not change session front door before commit |

## Reviewer Checklist

| Item | Expected result |
| --- | --- |
| No package.json diff | VERIFY |
| No package-lock.json diff | VERIFY |
| No auth runtime diff | VERIFY |
| Checker wired in both hook and autorun | VERIFY |
| npm audit result classified, not hidden | VERIFY — 14 vulns classified in ledger |
| Completion does not claim production auth stability | VERIFY |
| pre-closure gate passes after commit | VERIFY after operator commit |

## Audit Note: npm audit 14 Vulnerabilities

All 14 vulnerabilities are in dev/build toolchain or the `next` framework
(not `next-auth` directly). The 2 high/moderate items gated on `next` semver-major
require a separate `next` upgrade work order — they are not in ERH-DEP1 scope.
`next-auth` itself does not appear in the audit vulnerability list; its risk is
API-stability (beta API can change), not a published CVE.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Beta auth dependency needs repeatable risk workflow before public/auth claims | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | ERH-DEP1 checker and ledger now active in hook/autorun |
| 14 npm audit vulnerabilities in toolchain/framework scope | DEPENDENCY_AUDIT_GAP | GOVERNANCE_CONTROL_PLANE | ROADMAP_REQUIRED | Separate `next` upgrade work order for gated high/moderate items; separate test-runner fix for critical dev items |
| Runtime/provider learning lane | N/A_WITH_REASON | N/A_WITH_REASON | N/A_WITH_REASON | ERH-DEP1 is a dependency-risk governance workflow; no runtime provider execution or live proof was performed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance completion record. Public caveat for next-auth beta
is deferred to the ERH-T1B public-sync work order per PD1 drift ledger status
`PRIVATE_ONLY_DEFERRED`.

Next action: operator commits this batch; reviewer verifies; public caveat
handled in ERH-T1B (separate public-sync work order).

## Claim Boundary

This completion records Claude's implementation of the ERH-DEP1 dependency risk
workflow chain. It does not prove auth security, hosted freshness, production
readiness, stable dependency posture, dependency migration completion, live
governance behavior, or public readiness.
