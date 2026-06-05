# CVF Agent Work Order - LE1 Live E2E Selector Flow Diagnostic

Memory class: POINTER_RECORD

Status: DISPATCHED

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: 16ff33a9

executionBaseHead: 16ff33a9

closureBaseHead: 16ff33a9

Dispatch date: 2026-06-06

## Purpose

Execute the LE1 live E2E selector/test-flow diagnostic authorized by the matching
GC-018 baseline after MLW8-PEL1 recorded release-gate live Playwright
`locator.click` timeouts.

## 1. Mission

Identify and repair the bounded live E2E selector/test-flow failure that blocked
the MLW8-PEL1 live-governance-pass claim. Success means the release-gate live
Playwright suite has deterministic selector/test-flow behavior or, if a live
provider/browser failure remains, the failure is captured with a secret-safe
diagnostic that clearly separates test-flow failure from governance behavior.

## 2. Authority Chain

- Operator instruction: 2026-06-06 chat instruction to continue by the old
  rule.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V16_2026-06-06.md`.
- GC-018 baseline:
  `docs/baselines/CVF_GC018_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_2026-06-06.md`.
- MLW8-PEL1 completion:
  `docs/reviews/CVF_MLW8_PEL1_PROOF_EXPORT_LIVE_COMPLETION_2026-06-06.md`.
- Live diagnostic:
  `docs/evidence/CVF_MLW8_PEL1_RELEASE_GATE_DIAGNOSTIC_2026-06-06.json`.
- Release gate owner: `scripts/run_cvf_release_gate_bundle.py`.

Authority boundary:

- This work order owns test-flow diagnostics and bounded Playwright helper/spec
  hardening only.
- It does not own provider routing, `/api/execute` governance behavior, public
  export, runtime optimization, or policy changes.

## Scope / Target / Owner Boundary

Target:

- release-gate live E2E selector/test-flow reliability.

Owner boundary:

- Private provenance owns work order, E2E test helper/spec edits, evidence,
  completion review, and session sync.
- No public-sync work is authorized.

## 3. Agent Roles

- Orchestrator / dispatcher: Codex multi-role orchestrator.
- Implementer: Codex implementation role.
- Reviewer: Codex adversarial reviewer role plus machine gates.
- Operator approval required for: destructive actions, secret disclosure,
  provider routing changes, governance runtime changes, policy relaxation,
  public-sync, production deployment, or readiness claims beyond this work
  order.

## 4. Scope

Allowed scope:

- Diagnose release-gate live E2E selector/test-flow timeout evidence.
- Edit shared Playwright E2E utility and, if needed, the three release-gate live
  specs.
- Run focused live Playwright tests and the release gate bundle with
  operator-authorized local live keys.
- Save secret-safe result and diagnostic evidence.
- Update completion review, session memory, active state, and active handoff.
- `docs/baselines/CVF_GC018_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_2026-06-06.md`
- `docs/work_orders/CVF_WO_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_2026-06-06.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/governance-gate-live.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/noncoder-governance-live.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/w113-workspace-web-live-proof.spec.ts`
- `docs/evidence/CVF_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_RESULT_2026-06-06.json`
- `docs/evidence/CVF_LE1_RELEASE_GATE_RESULT_2026-06-06.json`
- `docs/evidence/CVF_LE1_RELEASE_GATE_DIAGNOSTIC_2026-06-06.json`
- `docs/reviews/CVF_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_COMPLETION_2026-06-06.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V16_2026-06-06.md`

Forbidden scope:

- Do not change provider routing behavior.
- Do not change `/api/execute` governance runtime behavior.
- Do not relax policy, DLP, approval, evidence, receipt, or audit behavior.
- Do not print, commit, copy, or public-sync raw API keys or `.env.local`.
- Do not perform public-sync.
- Do not claim public readiness, hosted readiness, production readiness,
  provider superiority, cost reduction, latency reduction, or output-quality
  improvement.

Risk ceiling: R2 bounded live E2E diagnostic/test-flow hardening.

## Write Ownership

Allowed private paths:

- `docs/baselines/CVF_GC018_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_2026-06-06.md`
- `docs/work_orders/CVF_WO_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_2026-06-06.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/governance-gate-live.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/noncoder-governance-live.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/w113-workspace-web-live-proof.spec.ts`
- `docs/evidence/CVF_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_RESULT_2026-06-06.json`
- `docs/evidence/CVF_LE1_RELEASE_GATE_RESULT_2026-06-06.json`
- `docs/evidence/CVF_LE1_RELEASE_GATE_DIAGNOSTIC_2026-06-06.json`
- `docs/reviews/CVF_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_COMPLETION_2026-06-06.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V16_2026-06-06.md`

Forbidden paths:

- `.env.local`
- secret-bearing config files
- public-sync repository files
- provider routing or governance runtime source outside listed E2E test files

## Execution Plan

1. Run pre-dispatch and pre-implementation gates.
2. Reproduce or narrow the live E2E selector/test-flow failure.
3. Implement the smallest test-flow hardening inside allowed paths.
4. Run focused live Playwright proof.
5. Run `python scripts/run_cvf_release_gate_bundle.py --json`.
6. Record result and any diagnostic.
7. Close with completion review and session sync.
8. Run pre-closure and pre-push gates.

## Evidence Requirements

Evidence must include:

- source verification table;
- focused live Playwright command/result;
- release gate command/result JSON;
- live diagnostic JSON if the live run fails, times out, or needs rerun;
- changed-file evidence and closure diff gate;
- session sync evidence.

## Acceptance Criteria

Closure requires:

- pre-dispatch and pre-implementation autorun gates pass after packet repair;
- any test-flow change stays inside the named E2E helper/spec files;
- focused live Playwright result is saved secret-safe;
- release gate result is saved secret-safe;
- live failure, timeout, or rerun condition has a diagnostic before rerun;
- completion review records changed-file evidence, claim boundary, and final
  disposition.

## Review Gate

Reviewer must reject closure if:

- the fix changes provider routing or governance runtime behavior;
- live proof failure lacks diagnostic;
- `.env.local` or raw secret values are printed/committed;
- closure claims public/hosted/production readiness without separate
  authorization;
- worktree or session state is stale.

## Closure Checklist

- [x] Dispatch source verification table included.
- [x] Roadmap-to-work-order trace matrix included.
- [x] Worker autonomy rule included.
- [x] Public/provenance boundary included.
- [x] Live/provider proof command named.
- [x] New evidence paths marked as new.

## Return Conditions

Return to orchestrator only if:

- live run exposes a secret or requires provider-side action beyond supplied
  keys;
- remediation requires provider routing, governance runtime, or policy changes;
- public-sync becomes necessary.

## Operator Checkpoint

Operator checkpoint: satisfied by 2026-06-06 instruction to continue by the old
rule after LE1 was identified as the next allowed move.

## 5. Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V16_2026-06-06.md`
- `docs/baselines/CVF_GC018_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_2026-06-06.md`
- `docs/evidence/CVF_MLW8_PEL1_RELEASE_GATE_RESULT_2026-06-06.json`
- `docs/evidence/CVF_MLW8_PEL1_RELEASE_GATE_DIAGNOSTIC_2026-06-06.json`
- `scripts/run_cvf_release_gate_bundle.py`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts`

## 6. Pre-Flight Checks

Commands to run before implementation:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 16ff33a9 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 16ff33a9 --head HEAD
```

## 6A. Source Verification Block

Runtime/source facts verified from current source or canonical contract:

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

Planned new paths clearly marked as new:

- `docs/evidence/CVF_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_RESULT_2026-06-06.json`
- `docs/evidence/CVF_LE1_RELEASE_GATE_RESULT_2026-06-06.json`
- `docs/evidence/CVF_LE1_RELEASE_GATE_DIAGNOSTIC_2026-06-06.json`
- `docs/reviews/CVF_LE1_LIVE_E2E_SELECTOR_FLOW_DIAGNOSTIC_COMPLETION_2026-06-06.md`

## 6B. Roadmap-To-Work-Order Trace Matrix

This work is derived from the active next allowed move after MLW8-PEL1.

| Requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Open separate live-E2E selector/test-flow diagnostic | Sections 1-4 | LE1 GC-018 and work order | Pre-dispatch gate | READY |
| Preserve provider/governance runtime boundary | Sections 4, Review Gate | Only E2E helper/spec paths allowed | Diff review | READY |
| Run live proof with key authorization | Sections 6, 8 | Focused live Playwright and release gate result JSON | Playwright and release gate commands | READY |
| Record diagnostic if live failure remains | Evidence Requirements | Diagnostic JSON | Live diagnostic standard | READY |
| Close without public readiness overclaim | Claim boundary and completion review | Completion review | Pre-closure gate | READY |

## 6C. Worker Autonomy / No-Question Rule

The worker proceeds without operator confirmation for non-destructive actions
inside this work order's Allowed scope.

Proceed autonomously with:

- reading and editing files named in Allowed scope;
- running focused live Playwright and release gate commands with local
  operator-supplied API keys;
- recording secret-safe result/diagnostic evidence;
- allowed-scope remediation and reruns after diagnostics are recorded.

Escalation is reserved for destructive actions, secret exposure, production
deployment, public-sync, provider routing changes, governance runtime changes,
policy relaxation, or public/hosted/production readiness claims.

## 7. Implementation Instructions

First try the smallest shared-helper hardening:

- add explicit timeout/fallback behavior around the shared login click path;
- keep login semantics unchanged for users and specs;
- preserve structural UI tests and direct API live governance tests.

Only edit individual live specs if shared-helper hardening is insufficient.

## 8. Verification Commands

Required commands:

```powershell
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx playwright test --config playwright.config.ts tests/e2e/noncoder-governance-live.spec.ts tests/e2e/governance-gate-live.spec.ts tests/e2e/w113-workspace-web-live-proof.spec.ts --reporter=json
cd ..\..\..
python scripts/run_cvf_release_gate_bundle.py --json
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 16ff33a9 --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-push --base 16ff33a9 --head HEAD
```

## Claim Boundary

LE1 may claim only selector/test-flow diagnostic outcome and bounded live E2E
evidence. It may not claim production readiness, hosted readiness, public
readiness, provider superiority, cost reduction, performance improvement,
policy relaxation, or runtime governance mutation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: LE1 is a private live E2E diagnostic tranche. No public-sync work is
authorized.
