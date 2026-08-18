# CVF Empty Read-Budget Registry Expiry Repair

Status: ACCEPTED_REPAIR_PENDING_COMMIT

Memory class: POINTER_RECORD

docType: review

Date: 2026-08-18

## Purpose

Record the operator-authorized correction for an active-continuity migration
registry whose `entries` list is empty but whose registry-level `expiresOn`
date has passed.

## Target / Source

- `docs/reference/CVF_ACTIVE_CONTINUITY_READ_BUDGET_STANDARD_2026-08-10.md`
- `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json`
- `governance/compat/active_continuity_read_budget.py`
- `governance/compat/test_active_continuity_read_budget_expiry.py`
- operator authorization `AUTHORIZE_EMPTY_READ_BUDGET_REGISTRY_EXPIRY_REPAIR`
  issued on 2026-08-18

## Scope / Methodology

The reviewer inspected the canonical debt rule, the current registry, the
validation function, and the focused tests. The implementation changes only
expiry enforcement: schema and ISO-date validation remain unconditional;
expiry is enforced when `entries` is malformed or contains at least one row;
an exactly empty list carries no debt whose waiver can expire.

## Findings / Position

| Finding | Evidence | Position |
|---|---|---|
| The registry contains zero debt rows. | `governance/compat/CVF_ACTIVE_CONTINUITY_READ_BUDGET_MIGRATION.json` has `entries: []`. | No migration waiver exists to extend or consume. |
| The checker rejected the top-level date before applying row semantics. | `_validate_migration_top_level` previously emitted an expiry violation independently of the entries collection. | This was a machine-gate gap at the zero-row boundary. |
| Nonempty expired debt must remain blocked. | The canonical standard makes migration debt temporary and expiry-bounded. | Preserve fail-closed behavior for every nonempty registry. |

## Risk / Corrective Action

The repair does not alter the registry date and does not create a new waiver.
Regression tests cover both sides of the boundary: an expired empty registry
passes, while an expired registry carrying a valid debt row still fails.
Malformed dates, missing fields, invalid entries types, and row validation
remain governed by their existing checks.

## Decision

ACCEPTED_BOUNDED_REPAIR

The repair is accepted within the exact authorized two-code-path boundary,
subject to focused tests, the active-session checker, and repository gates.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_active_session_state.py` |
| literalTokensReviewed | `Core Guard Self-Protection Authorization`; `Protected paths`; `Operator authorization`; `Rollback boundary`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `DEFERRED_PRIVATE_ONLY`; `RULE_GAP`; `GOVERNANCE_CONTROL_PLANE`; `MACHINE_CHECK_ADDED` |
| gateRunPurpose | Confirmation of the pre-read contract and the bounded repair; gate output is not first-discovery evidence. |
| claimBoundary | Checker-level continuity repair only; no runtime, provider, live, deployment, public-sync, or broader migration-policy claim. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: change expiry enforcement only so an
expired registry-level date does not fail when `entries` is exactly an empty
list; preserve date validation and fail-closed expiry for malformed or
nonempty entries; add focused regression coverage.

Protected paths (every changed guard/control path is listed):

- `governance/compat/active_continuity_read_budget.py`
- `governance/compat/test_active_continuity_read_budget_expiry.py`

Operator authorization: `AUTHORIZE_EMPTY_READ_BUDGET_REGISTRY_EXPIRY_REPAIR`
was explicitly issued on 2026-08-18.

Rollback boundary: revert only the two protected paths above and this review
artifact. Do not modify or extend the registry-level date as rollback.

Scope boundary: no registry row is added; no canonical budget changes; no
session-mode transition; no R3 implementation; no runtime, provider/live,
deployment, public-sync, or production authorization.

## Finding-To-Governance Learning Disposition

defect class: `MACHINE_GATE_GAP`

learning lane: `GOVERNANCE_CONTROL_PLANE`

runtime/provider/cost learning lane: `N/A_WITH_REASON` - this is a local
checker-semantics repair with no runtime or provider execution.

| Finding or lesson | Disposition | Learning lane | Next action |
|---|---|---|---|
| Registry-level expiry must distinguish zero debt rows from active debt. | MACHINE_CHECK_ADDED | GOVERNANCE_CONTROL_PLANE | Keep both boundary regression tests in the active-session test suite. |

## Epistemic Process Block

| Field | Value |
|---|---|
| Mode | deterministic local source and test inspection |
| Evidence used | canonical standard, current JSON registry, checker source, focused unit tests, active-session checker output |
| Limits | no runtime, provider, network, public repository, or deployment evidence was evaluated |
| Confidence | high for the bounded zero-row checker semantics |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | empty-read-budget-expiry-repair-2026-08-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, patch application, focused unittest, active-session checker |
| Target paths | `governance/compat/active_continuity_read_budget.py`; `governance/compat/test_active_continuity_read_budget_expiry.py`; `docs/reviews/CVF_EMPTY_READ_BUDGET_REGISTRY_EXPIRY_REPAIR_2026-08-18.md` |
| Allowed scope source | operator authorization `AUTHORIZE_EMPTY_READ_BUDGET_REGISTRY_EXPIRY_REPAIR` |
| Before status evidence | clean HEAD `accd005c1786f1e5e3d1950c706ba5f117424f32` plus the separately held untracked R3 dispatch draft |
| After status evidence | two protected paths modified and this authorization/review artifact added; R3 draft remains outside this repair batch |
| Diff evidence | exact repair manifest verified by `git diff --name-status` and `git status --short` before staging |
| Approval boundary | bounded checker repair only |
| Claim boundary | local deterministic validation only; no wider readiness claim |
| Agent type | reviewer/orchestrator |
| Invocation ID | empty-read-budget-expiry-repair-2026-08-18 |
| Expected manifest | `governance/compat/active_continuity_read_budget.py`; `governance/compat/test_active_continuity_read_budget_expiry.py`; `docs/reviews/CVF_EMPTY_READ_BUDGET_REGISTRY_EXPIRY_REPAIR_2026-08-18.md` |
| Actual changed set | same three repair paths; the two held R3 draft paths are pre-existing and excluded |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | deterministic checker validation for empty versus nonempty migration debt |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE - bounded local machine-check correction |
| receiptEvidence | CVF_RECEIPT_PRESENT - focused unittest and active-session checker output |
| actionEvidence | ACTION_EVIDENCE_PRESENT - local source edit and deterministic test execution only |
| invocationBoundary | repository-local Python checks |
| interceptionBoundary | no shell, IDE, filesystem, provider, or runtime interception claim |
| claimLanguage | the empty-registry expiry defect is repaired within the tested boundary |
| forbiddenExpansion | no runtime execution, provider/live proof, deployment, public-sync, production readiness, or universal governance claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This private provenance repair is not a public catalog or public-sync batch.

## Claim Boundary

This artifact authorizes and records only the empty-registry expiry repair.
It does not change canonical read budgets, extend migration debt, authorize R3
implementation, or establish runtime, provider, live, deployment, public-sync,
production, or universal-governance readiness.
