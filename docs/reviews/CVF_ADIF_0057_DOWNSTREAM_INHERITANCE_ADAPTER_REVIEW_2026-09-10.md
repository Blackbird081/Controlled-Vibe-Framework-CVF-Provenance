# CVF ADIF-0057 Downstream Inheritance Adapter Review

Memory class: FULL_RECORD

Status: ACCEPTED_MACHINE_REVIEWED

Date: 2026-09-10

## Purpose

Close the propagation gap discovered while refreshing the operator-local
`shift-operations-workspace`: the Core checker was bound to Core repository
hooks but could not evaluate an explicitly named downstream Git worktree.

## Target / Source

- Canonical machine standard:
  `docs/reference/CVF_GATE_TO_ROLE_CLOSEABILITY_MACHINE_STANDARD.md`
- Existing checker:
  `governance/compat/check_gate_to_role_closeability.py`
- Operator instruction: continue the agreed downstream inheritance refresh
  after ADIF-0057 machine enforcement was completed in Core.

## Scope / Methodology

Add an explicit `--repo-root` adapter to the existing checker, cover it with a
temporary downstream-repository regression test, and include the standard,
checker, and ADIF record in the operator-local workspace overlay. No checker
semantics, mandatory gate set, agent reasoning, product code, provider call,
runtime interception, public sync, push, or deployment behavior is changed.

## Findings / Position

The previous Core implementation correctly enforced configured Core hook
paths. A rule-pack consumer could receive its prose and source pin but had no
supported way to direct the checker at the consumer repository. Therefore a
pin refresh alone could not substantiate downstream machine-enforcement.

## Risk / Corrective Action

Risk is bounded to repository selection. The default remains the checker's own
repository. Downstream use must explicitly name a Git worktree; invalid roots
fail before evaluation. Rollback removes only the adapter, its focused test,
the three overlay catalog rows, and this review record.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add the bounded downstream worktree
adapter and operator-local projection needed to apply the already-authorized
ADIF-0057 machine control to `shift-operations-workspace`.

Protected paths:

- `governance/compat/check_gate_to_role_closeability.py`
- `governance/compat/test_check_gate_to_role_closeability.py`

Operator authorization: on 2026-09-10 the operator explicitly approved the
inheritance refresh after asking whether the project had received the completed
CVF Core upgrade.

Rollback boundary: revert only this downstream adapter batch; preserve the
accepted ADIF-0057 machine semantics and all unrelated CVF history.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `Authorized guard-maintenance scope`; `Protected paths`; `Operator authorization`; `Rollback boundary` |
| gateRunPurpose | Confirmation evidence after source read-ahead; not first discovery of required fields. |
| claimBoundary | Local static repository enforcement only; no live provider or universal interception claim. |

## Claim Boundary

This batch enables a cooperating operator-local project gate to apply the Core
checker to its own Git worktree. It does not auto-install hooks, intercept
out-of-band tools, prove agent comprehension, or authorize product/runtime,
provider/live, public-sync, push, or deployment effects.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the operator-local provenance adapter is being validated in the private
Core and downstream project before any separately authorized public export.

## Epistemic Process Block

### Expected Result / Prediction

The unchanged default invocation should inspect Core, while `--repo-root`
should inspect changed files in a distinct Git worktree.

### Evidence Comparison

Focused tests exercise the downstream worktree path; Core self-protection and
catalog parsing are run against the exact changed set.

Verification evidence: 22 focused checker/hook tests passed; the 68-check
reviewer-fast governance chain passed; core guard self-protection reported zero
violations; the overlay catalog parsed as valid JSON.

### Contradiction Or Gap Disposition

The contradiction between `rule-pack refreshed` and `downstream checker
enforced` is resolved by treating propagation and invocation as separate gates.

### Claim Update

Downstream enforcement may be claimed only after the project invokes the
materialized checker with its own root and that invocation passes.
