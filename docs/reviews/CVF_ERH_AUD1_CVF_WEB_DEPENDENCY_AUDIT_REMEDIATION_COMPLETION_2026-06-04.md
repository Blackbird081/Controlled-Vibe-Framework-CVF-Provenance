# CVF ERH-AUD1 CVF-Web Dependency Audit Remediation Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-04

Worker: Claude

dispatchPacketCommit: `358611bb`

executionBaseHead: `af0f0220`

closureBaseHead: `af0f0220`

GC-018: `docs/baselines/CVF_GC018_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_2026-06-04.md`

Work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_FOR_CLAUDE_2026-06-04.md`

Authored work-order base: `28f76620`; committed dispatch packet:
`358611bb`; operator handoff sync before Claude artifact intake: `af0f0220`.

## Purpose

Record the completion of the ERH-AUD1 `cvf-web` dependency audit remediation
implemented by Claude. This review provides the evidence packet for Codex or
operator review before the batch is committed.

## Scope / Target / Owner Boundary

Target: `cvf-web` npm audit remediation — bounded non-semver-major updates only.

Boundary: no `next-auth` migration, no auth runtime changes, no semver-major
framework migration, no public-sync export, no production security claims.

## Source / Predecessor Evidence

| Source | Purpose | Disposition |
| --- | --- | --- |
| `docs/reviews/CVF_ERH_DEP1_DEPENDENCY_RISK_WORKFLOW_CHAIN_COMPLETION_2026-06-04.md` | DEP1 predecessor — 14 vulns classified | ACCEPTED |
| `docs/reference/CVF_ERH_DEP1_DEPENDENCY_RISK_LEDGER_2026-06-04.md` | before audit snapshot | ACCEPTED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependency manifest | MODIFIED |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | lock file | REGENERATED |

## Decision / Baseline / Proposed Tranche

**Decision: `AUDIT_REDUCED_WITH_RESIDUALS`**

Rationale:

- Critical reduced 3 → 0; High reduced 7 → 0; Moderate 4 → 3.
- 3 residuals are semver-major gated (`next@9`, `next-auth@3`, `postcss` via next).
- All bounded non-semver-major fixes applied; verification PASS.

## Findings / Position

| Item | Finding | Disposition |
| --- | --- | --- |
| Before audit | 14 vulnerabilities (3 critical / 7 high / 4 moderate) | DOCUMENTED |
| After audit | 3 vulnerabilities (0 critical / 0 high / 3 moderate) | DOCUMENTED |
| Residuals | `next` + `postcss` + `next-auth` all gated on semver-major | CLASSIFIED_BLOCKED_MAJOR |
| `next-auth` unchanged | still `^5.0.0-beta.30` | CONFIRMED |
| Auth runtime unchanged | `src/auth.ts`, `middleware.ts`, `middleware-auth.ts` untouched | CONFIRMED |
| TypeScript check | PASS after `.next` cache clear | PASS |
| Build | PASS | PASS |
| Tests | 3020/3021 PASS; 1 live test pre-existing fail | PASS_WITH_PRE_EXISTING_LIVE_FAIL |

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| 3 residual moderate vulns gated on `next` semver-major | Separate `next` major upgrade work order requires operator decision on app compatibility |
| `next-auth` residual moderate via `next` dep | Blocked by ERH-DEP1 scope; follows `next` major decision |
| `route.dlp.live.test.ts` live test failure | Pre-existing issue, not caused by AUD1 dep updates; separate investigation needed |
| Public claim could overclaim security hardening | Completion explicitly deferred as `DEFERRED_PRIVATE_ONLY`; no production security claim made |

## Evidence / Verification

| Check | Result |
| --- | --- |
| Before audit: `npm audit --json` | 14 vulns (3c/7h/4m) — recorded |
| After audit: `npm audit --json` | 3 vulns (0c/0h/3m) — recorded |
| `npm run check` (tsc --noEmit) | PASS |
| `npm run build` | PASS |
| `npm run test:run` | 3020/3021 PASS; 1 pre-existing live fail |
| `python -m pytest governance/compat/test_check_erh_cvf_web_dependency_audit_workflow.py -q` | 13/13 PASS |
| `python governance/compat/check_erh_cvf_web_dependency_audit_workflow.py --enforce` | PASS |
| `python governance/compat/check_system_loop_interlock.py --base af0f0220 --head HEAD --enforce` | PASS — 11 connections |
| `next-auth` diff | CLEAN — `^5.0.0-beta.30` unchanged |
| Auth runtime diff | CLEAN — no auth source changes |
| Codex review rerun: `npm audit --json` | expected non-zero; confirms 3 moderate residuals, 0 critical, 0 high |
| Codex review rerun: `npm run build` | PASS with pre-existing `source-map-support` warning |
| Codex review rerun: `npm run check` | PASS after fresh build regenerated `.next/types` |

## Codex Reviewer Closeout

Disposition: `CLOSED_PASS_BOUNDED`.

Reviewer corrections applied before commit:

- corrected `next 16.1.6` to `16.2.7` classification from patch/same
  major.minor to minor/same-major;
- removed an over-strong residual exploitability phrase and kept the claim to
  audit-regression boundary;
- refreshed closure anchors to the committed AUD1 dispatch packet and the
  operator handoff sync head.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one bounded ERH-AUD1 dependency-audit
workflow checker, focused checker tests, and hook/autorun wiring so future
dependency-audit remediation does not remain prose-only.

Protected paths:

- `governance/compat/check_erh_cvf_web_dependency_audit_workflow.py`
- `governance/compat/test_check_erh_cvf_web_dependency_audit_workflow.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: ERH-AUD1 work order explicitly allowed the checker,
focused tests, and hook/autorun wiring for this bounded workflow-chain tranche;
the operator returned Claude's AUD1 packet for Codex/operator commit review.

Rollback boundary: revert the ERH-AUD1 closure commit and follow-up handoff sync
commit. No unrelated guard semantics, protected-file rename/delete, public-sync,
auth runtime, or `next-auth` migration is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_FOR_CLAUDE_2026-06-04.md` | `CLOSED_PASS_BOUNDED`; acceptance rows PASS; closure anchors refreshed | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_COMPLETION_2026-06-04.md` | final disposition, changed files, verification, claim boundary, and self-protection authorization | PASS |
| Roadmap state | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | ERH-AUD1 row and E11 row `CLOSED_PASS_BOUNDED`; next action moved to separate DEP2/next-major decision | PASS |
| Registry JSON | `N/A with reason` | no corpus scan registry state changed; AUD1 is dependency-audit closure, not corpus/search/classification closure | BLOCKED with reason |
| Registry Markdown | `N/A with reason` | no corpus scan registry state changed; AUD1 is dependency-audit closure, not corpus/search/classification closure | BLOCKED with reason |
| External evidence digest | `N/A with reason` | no external corpus/source digest consumed; npm audit output summarized in this packet | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | ERH-AUD1 checker connection added and verified | PASS |
| Session continuity | `AGENT_HANDOFF_V15_2026-05-29.md` | follow-up handoff sync commit required after closure commit | PASS |

## Deliverables

| Artifact | Path | Mode |
| --- | --- | --- |
| `package.json` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | updated (5 bumps) |
| `package-lock.json` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | regenerated |
| Workflow chain reference | `docs/reference/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_WORKFLOW_CHAIN_2026-06-04.md` | created |
| Remediation ledger | `docs/reference/CVF_ERH_AUD1_CVF_WEB_DEPENDENCY_AUDIT_REMEDIATION_LEDGER_2026-06-04.md` | created |
| Checker | `governance/compat/check_erh_cvf_web_dependency_audit_workflow.py` | created |
| Focused tests | `governance/compat/test_check_erh_cvf_web_dependency_audit_workflow.py` | created (13/13 PASS) |
| Hook chain wiring | `governance/compat/run_local_governance_hook_chain.py` | updated |
| Autorun gate wiring | `governance/compat/run_agent_autorun_workflow_gate.py` | updated |
| GC-052 connection | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | updated (11 connections) |
| Roadmap AUD1 status | `docs/roadmaps/CVF_ERH_EXTERNAL_REVIEW_HARDENING_ROADMAP_2026-06-04.md` | updated |

## Reviewer Checklist

| Item | Expected result |
| --- | --- |
| `next-auth` unchanged | VERIFY — `^5.0.0-beta.30` in package.json |
| Auth runtime files unchanged | VERIFY — no diff on auth.ts/middleware |
| Residual 3 vulns classified (not hidden) | VERIFY — ledger documents all 3 |
| `npm audit` output classified, not hidden | VERIFY |
| pre-existing live test documented | VERIFY — `route.dlp.live.test.ts` |
| Completion does not claim production security | VERIFY |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| 14 npm audit vulns reduced to 3 via bounded remediation | DEPENDENCY_AUDIT_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | ERH-AUD1 checker and ledger active in hook/autorun |
| 3 residual moderate vulns require semver-major `next` decision | DEPENDENCY_MIGRATION_GATE | GOVERNANCE_CONTROL_PLANE | ROADMAP_REQUIRED | Open separate next-major-upgrade work order if operator approves |
| Pre-existing DLP live test failure unrelated to deps | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | INVESTIGATION_DEFERRED | Separate investigation; not blocking AUD1 closure |
| Runtime/provider learning lane | N/A_WITH_REASON | N/A_WITH_REASON | N/A_WITH_REASON | AUD1 is dependency governance; no live provider execution performed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance audit remediation. Public security/dependency posture
requires a separate public-sync work order.

## Claim Boundary

This completion records bounded npm audit remediation. It does not prove
production security hardening, full CVE clearance, hosted freshness, public
security readiness, or complete dependency coverage.
