# CVF Work Order: Closure Packaging Preflight Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-05

dispatchBaseHead: `530728a2`

executionBaseHead: `530728a2`

closureBaseHead: `530728a2`

Commit mode: `WORKER_MAY_COMMIT`

## Purpose

Add a small machine preflight that catches recurring closure-packaging defects
before the full autorun pre-closure bundle reports them as a long finding list.

## Agent Roles

| Role | Assignment |
| --- | --- |
| Orchestrator | Codex under 2026-06-05 operator instruction |
| Worker | Codex self-execution |
| Reviewer / committer | Codex closure review and commit |

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator direction | 2026-06-05: "nâng luôn đi, trước khi qua tranche khác" after repeated pre-closure findings | ACCEPT |
| Closure quality standard | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | ACCEPT |
| Autorun workflow gate | `governance/compat/run_agent_autorun_workflow_gate.py` | ACCEPT |
| Local hook chain | `governance/compat/run_local_governance_hook_chain.py` | ACCEPT |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope preflight, test, documentation, and hook-wiring
defects directly. Escalate before runtime behavior changes, public-sync,
live/provider proof, secrets/quota use, destructive actions, or claim-boundary
expansion.

## Scope

Allowed scope:

- Add `check_closure_packaging_preflight.py`.
- Add focused unit tests for repeated closure-packaging defects.
- Wire the checker into autorun and local hook chains.
- Update the closure-quality standard with the canonical marker.
- Record bounded work order, completion review, and session continuity.
- Explicit allowed paths:
  `governance/compat/check_closure_packaging_preflight.py`,
  `governance/compat/test_check_closure_packaging_preflight.py`,
  `governance/compat/run_agent_autorun_workflow_gate.py`,
  `governance/compat/run_local_governance_hook_chain.py`,
  `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`,
  `docs/work_orders/CVF_WO_CLOSURE_PACKAGING_PREFLIGHT_HARDENING_2026-06-05.md`,
  `docs/reviews/CVF_CLOSURE_PACKAGING_PREFLIGHT_HARDENING_COMPLETION_2026-06-05.md`,
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, and
  `AGENT_HANDOFF_V15_2026-05-29.md`.

Forbidden scope:

- Runtime route behavior changes, provider calls, public-sync, live proof,
  dependency changes, package/lockfile edits, broad hook refactors, production
  readiness, public readiness, or autonomous mutation.

Risk ceiling: R2 control-plane hardening only.

## Required First Reads

| Required read | Reason | Status |
| --- | --- | --- |
| `CVF_SESSION_MEMORY.md` | active front door | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active state | READ |
| `AGENT_HANDOFF_V15_2026-05-29.md` | active handoff | READ |
| `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | closure rules | READ |
| `governance/compat/run_agent_autorun_workflow_gate.py` | autorun owner | SOURCE_VERIFIED |
| `governance/compat/run_local_governance_hook_chain.py` | local hook owner | SOURCE_VERIFIED |

## Pre-Flight Checks

| Check | Evidence | Status |
| --- | --- | --- |
| Base head captured | `530728a2` | PASS |
| Protected-file scope identified | Core Guard Self-Protection Authorization in completion review | PASS |
| Runtime scope excluded | no `EXTENSIONS/` source files in allowed paths | PASS |
| Public-sync excluded | forbidden scope and public export disposition | PASS |

## Write Ownership

| Role | Owned paths |
| --- | --- |
| Worker | `governance/compat/check_closure_packaging_preflight.py`, `governance/compat/test_check_closure_packaging_preflight.py` |
| Reviewer / committer | `governance/compat/run_agent_autorun_workflow_gate.py`, `governance/compat/run_local_governance_hook_chain.py`, docs and session continuity |
| Forbidden | `EXTENSIONS/`, dependency files, live/provider proof, public-sync |

## Execution Plan

1. Add a small structural checker for recurring closure-packaging defects.
2. Add focused tests for stale closed wording, unsafe corpus enumeration, and
   changed-file overclaim.
3. Wire the checker into autorun and local hooks.
4. Update the closure-quality standard marker.
5. Run focused and autorun gates before commit.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Autorun wrapper owns phase gate bundle | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `_common_commands` | autorun workflow gate | EXISTS | ACCEPT |
| Local hook chain owns pre-commit/pre-push checks | `governance/compat/run_local_governance_hook_chain.py` | `HOOK_CHAINS` | `HOOK_CHAINS` | local governance hook chain | EXISTS | ACCEPT |
| Core guard protected scripts require authorization | `governance/compat/check_core_guard_self_protection.py` | `PROTECTED_EXACT`, `_is_protected` | `_is_protected` | core guard self-protection gate | EXISTS | ACCEPT |
| Closure quality standard owns closure evidence discipline | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | Required Closure Markers | `Required Closure Markers` | closure quality standard | EXISTS | ACCEPT |
| Corpus enumeration must be filesystem-backed | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` | standard body | `Corpus Completeness And Report Integrity` | corpus completeness standard | EXISTS | ACCEPT |

## New Doc-Only Fields

| New field | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `Closure Packaging Preflight` | canonical standard marker for the new early gate | Yes |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | Work-order output | Evidence | Status |
| --- | --- | --- | --- |
| Promote repeated pre-closure findings into reusable control | new checker | focused tests | PASS |
| Move checks earlier than full pre-closure noise | autorun/local hook wiring | scripts updated | PASS |
| Preserve bounded claim boundary | docs and tests only | no runtime files touched | PASS |

## Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `governance/compat/check_closure_packaging_preflight.py` | true | early closure packaging checker |
| `governance/compat/test_check_closure_packaging_preflight.py` | true | focused regression tests |
| `docs/reviews/CVF_CLOSURE_PACKAGING_PREFLIGHT_HARDENING_COMPLETION_2026-06-05.md` | true | completion and authorization artifact |

## Evidence Requirements

Closure evidence must include focused unit-test PASS, preflight PASS, core-guard
PASS, dispatch-quality PASS, machine-closure PASS, corpus/report PASS, and
autorun gate PASS before final closeout.

## Acceptance Criteria

| Criterion | Required before closure |
| --- | --- |
| Preflight checker exists | YES |
| Repeated defect patterns have focused tests | YES |
| Autorun and local hook chains call the checker | YES |
| Core guard authorization covers protected files | YES |
| Runtime/public/live boundaries remain excluded | YES |

## Review Gate

Reviewer must reject closure if the checker changes runtime behavior, creates a
public claim, lacks focused tests, is not wired into autorun/local hooks, or
touches protected files without a checker-recognized authorization artifact.

## Closure Checklist

| Item | Status |
| --- | --- |
| Source verification complete | PASS |
| Focused tests pass | PASS |
| Preflight checker pass | PASS |
| Core guard authorization present | PASS |
| Public Export Disposition present | PASS |

## Return Conditions

Return to Orchestrator if the checker requires broad hook refactor, runtime
route changes, public-sync, live/provider proof, dependency edits, or a larger
closure-standard rewrite.

## Operator Checkpoint

Operator checkpoint is required before public-sync, live/provider proof,
runtime behavior changes, dependency edits, or claim-boundary expansion.

## Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/` | runtime/source behavior out of scope |
| `package.json` | dependency edits out of scope |
| `package-lock.json` | dependency edits out of scope |

## Forbidden Filesystem State At Dispatch

| Forbidden path | Actual state at dispatch | Disposition |
| --- | --- | --- |
| `EXTENSIONS/` | UNCHANGED_EXISTING_SCOPE_FORBIDDEN | directory exists but is forbidden for changes, not for existence |
| `package.json` | UNCHANGED_EXISTING_SCOPE_FORBIDDEN | file exists but is forbidden for changes |
| `package-lock.json` | UNCHANGED_EXISTING_SCOPE_FORBIDDEN | file exists but is forbidden for changes |

## Closure Diff Gate

| Requirement | Final artifact | Disposition |
| --- | --- | --- |
| Add preflight checker | `governance/compat/check_closure_packaging_preflight.py` | SATISFIED |
| Add focused tests | `governance/compat/test_check_closure_packaging_preflight.py` | SATISFIED |
| Wire autorun | `governance/compat/run_agent_autorun_workflow_gate.py` | SATISFIED |
| Wire local hooks | `governance/compat/run_local_governance_hook_chain.py` | SATISFIED |
| Update standard marker | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | SATISFIED |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | status `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_CLOSURE_PACKAGING_PREFLIGHT_HARDENING_COMPLETION_2026-06-05.md` | completion review created | PASS |
| Roadmap state | N/A | operator-authorized control-plane hardening without separate roadmap | N/A with reason |
| Registry JSON | N/A | no corpus/search registry state changed | BLOCKED with reason |
| Registry Markdown | N/A | no corpus/search registry markdown changed | BLOCKED with reason |
| External evidence digest | N/A | no external evidence consumed | N/A with reason |
| System loop interlock | N/A | local phase-gate wiring only; no downstream runtime loop added | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `AGENT_HANDOFF_V15_2026-05-29.md` | updated after closure | PASS |

## Corpus Completeness And Report Integrity

- Corpus task class: CONTROL_PLANE_HARDENING.
- Corpus root: bounded changed file set.
- Snapshot time: 2026-06-05 at base `530728a2`.
- Enumeration command: `rg --files --hidden --no-ignore governance/compat docs/reference docs/work_orders docs/reviews CVF_SESSION CVF_SESSION_MEMORY.md AGENT_HANDOFF_V15_2026-05-29.md`.
- Manifest artifact or inline manifest: Closure Diff Gate.
- Manifest hash: N/A with reason - bounded changed-file set listed inline.
- Processing ledger artifact or inline ledger: inline in completion review.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=8; ledger_terminal=8; exclusions=3; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: runtime source, package/dependency files, public-sync.
- Unreadable or unsupported files: none.
- Aggregation check: PASS.
- Drift check: PASS
- Output traceability: Source Verification Block and Closure Diff Gate.
- Adversarial verification: sampled stale dispatch wording, git enumeration,
  bare `rg --files`, overbroad diff claim, and missing core-guard authorization.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- | --- |
| Repeated pre-closure findings arrived late and noisy | PHASE_GATE_PLACEMENT_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | `check_closure_packaging_preflight.py` wired before full gates |
| Closure packets can overclaim changed files or use stale wording | RULE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | preflight validates stale status and diff-claim paths |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance control-plane hardening only; no public-sync export
or public claim is authorized.

## Claim Boundary

This work order closes only a structural closure-packaging preflight. It does
not prove runtime behavior, provider behavior, live governance behavior,
hosted readiness, production readiness, public readiness, public-sync, or
autonomous mutation.
