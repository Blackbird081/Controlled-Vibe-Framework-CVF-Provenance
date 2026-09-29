# ADIF-0060 - Activation-Decision Status Gate Omission And Learning-Heading Escape

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0060
title: Activation-decision status gate omission and learning-heading escape
defectCategory: PROCESS_AND_GATE_ORDER
defectClass: PHASE_GATE_PLACEMENT_GAP
defectRole: ROOT_CAUSE
severity: HIGH
lifecycleState: ACTIVE
taskClasses: governance-checker-hardening; package-skill-productionization
roles: worker; reviewer; closer
lifecyclePhases: pre-implementation; worker-return
surfaceSelectors: ASSF activation-decision predicates (`generate_skill_control_plane_inventory.py` `_activation_decision`, `run_assf_active_resolver.py` `_decision_for`); activation-policy wrapper tests in `test_run_assf_activation_policy_resolver.py`; changed self-declared worker returns under docs/reviews/ evaluated by the Finding-To-Governance learning gate
detectionSignals: activation decision reaches ACTIVATION_READY for a runtime-eligible, truth-approved package whose registry/source `status` is not ACTIVE; inventory and resolver disagree on matrix priority/token; an activation-policy readiness fixture still uses APPROVED after the resolver status gate is repaired; a worker return's `## Findings / Position` heading carries no learning disposition; a blocked return self-declares FIRST_OCCURRENCE despite an earlier governed return with the same rootCauseClusterId
enforcementLevel: MACHINE_CHECKED
checkerBindings: governance/compat/test_skill_control_plane_inventory.py; governance/compat/test_run_assf_active_resolver.py; governance/compat/test_run_assf_activation_policy_resolver.py; governance/compat/check_finding_to_governance_learning.py; governance/compat/test_check_finding_to_governance_learning.py
promotionState: MACHINE_CHECK_ADDED
supersedes: NONE
lastVerifiedCommit: a804d4129
roadmapSeedId: NONE
```

## Purpose

Record why the same lifecycle-status conflation that R1/S06-R1 fixed in
`_drift_for_record` (ADIF-adjacent, not itself a prior ADIF entry) reappeared
one function away in `_activation_decision`/`_decision_for`, and why the
governance-learning gate did not force a human-independent catch: the
gate's finding-heading detector recognized `## Findings` and `## Known
Issues` literally, but not the standard worker-return heading
`## Findings / Position`, so only an incidental `| Finding |` table row (not
the heading itself) triggered the learning-disposition requirement on
returns that used prose instead of a table.

## Scope / Applies To

Applies prospectively to any generated activation/readiness predicate that
reads a package's lifecycle `status` field, and to any changed finding-bearing
artifact evaluated by the Finding-To-Governance learning gate. It does not
decide whether a specific implementation finding is technically correct, does
not expand a work-order path manifest, and does not authorize `ACTIVE`
promotion, P7-P10 execution, or provider/live/public/production action.

## Bad Example

`_activation_decision(runtime_eligible, truth)` returns `ACTIVATION_READY`
whenever `runtime_eligible` is true and `truth` is approved STRICT
runtime-eligible, without checking the registry entry's `status` field. A
worker creates a P6 truth packet for an `APPROVED` (not `ACTIVE`) package and
the generated inventory silently reports `ACTIVATION_READY`. Separately, a
worker return titled `## Findings / Position` with prose findings and no
`| Finding |` table passes the Finding-To-Governance learning gate with zero
violations because `_has_finding_marker` never matched the heading.

## Good Example

`_activation_decision(runtime_eligible, status, truth)` and
`run_assf_active_resolver.py`'s `_decision_for` both require `status ==
"ACTIVE"` in addition to runtime eligibility and approved truth before
returning `ACTIVATION_READY`; an `APPROVED` truth-approved package returns the
shared `DENIED_SOURCE_NOT_ACTIVE` token instead, and the SOP's new "P6/P8
Activation-Decision Matrix" states this as the canonical five-row contract
both functions must implement identically. Separately,
`FINDING_HEADING_RE` matches `## Findings / Position` directly, so a worker
return using that heading is subject to the learning-disposition requirement
regardless of whether it also happens to contain a table row. The blocked-
return guard requires a stable `rootCauseClusterId`, searches prior governed
returns for an exact match, rejects a repeated cluster labeled
`FIRST_OCCURRENCE`, and validates that a recurring return cites an existing
governed prior path carrying the same cluster ID.

## Canonical Sources

- `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`
  ("P6/P8 Activation-Decision Matrix")
- `docs/reference/agent_system_skills/CVF_ASSF_ACTIVATION_POLICY_SEMANTICS_STANDARD.md`
  ("Lifecycle Gate Precondition")
- `docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md`
- `governance/compat/generate_skill_control_plane_inventory.py`
- `governance/compat/run_assf_active_resolver.py`
- `governance/compat/check_finding_to_governance_learning.py`
- `docs/reviews/CVF_CVF_NCR_R1_S06_R1_P5_PHASE_GATE_RECONCILIATION_WORKER_RETURN_2026-09-27.md`
  (the sibling `_drift_for_record` fix this entry's defect echoes)

## Remediation

Add the `status == ACTIVE` condition to both `_activation_decision` and
`_decision_for`, returning the shared `DENIED_SOURCE_NOT_ACTIVE` token, and
prove it with a hostile APPROVED/ACTIVE regression pair in each of
`test_skill_control_plane_inventory.py` and `test_run_assf_active_resolver.py`
(including a corrected `_write_index` default so the resolver's own "ready"
fixture no longer encodes the same defect it is meant to catch). Extend
the same lifecycle oracle through the activation-policy wrapper: its ready
fixture must default to `ACTIVE`, and an explicit `APPROVED` case must remain
`SELECTED` with body read denied. Extend
`FINDING_HEADING_RE` in `check_finding_to_governance_learning.py` to match
`## Findings / Position` directly, and update
`test_check_finding_to_governance_learning.py` so the heading alone (no
table) is treated as a finding marker requiring a learning-disposition
section.

Use the same activation decision priority and tokens in both inventory and
resolver: runtime eligibility, truth presence/approval, lifecycle status, then
readiness. Add all-row hostile tests so the two surfaces cannot agree only on
the originally reported APPROVED+truth case while diverging elsewhere.

Update the worker-return scaffold and its checked-in golden fixture together;
placing recurrence fields only in the work-order template leaves return-time
authoring dependent on agent memory.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| `_activation_decision`/`_decision_for` computed activation readiness from runtime eligibility and truth alone, with no lifecycle `status` gate, letting a truth-approved `APPROVED` package be reported `ACTIVATION_READY` | `PHASE_GATE_PLACEMENT_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | add the shared `status == ACTIVE` gate to both functions, proven by a hostile APPROVED/ACTIVE regression pair in each focused test module | Handled in this correction round |
| `_has_finding_marker`'s heading regex did not recognize `## Findings / Position`, the standard worker-return findings heading, so a prose-only return under that heading could skip the learning-disposition requirement entirely | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | extend `FINDING_HEADING_RE` to match `Findings(?:\s*/\s*Position)?` and invert the prior negative-case test to a positive one | Handled in this correction round |
| Recurrence enforcement trusted self-declared `FIRST_OCCURRENCE` and accepted non-path prior evidence | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | require stable cluster IDs, exact prior-cluster lookup, existing governed prior paths, operator notice and successor freeze | Handled by Local independent review correction |
| Return scaffold omitted the recurrence fields while the template alone carried them | `SCAFFOLD_GAP` | `GOVERNANCE_CONTROL_PLANE` | `SCAFFOLD_UPDATED` | update scaffold and golden fixture atomically and retain exact-fixture tests | Handled by Local independent review correction |
| Activation-policy readiness tests retained an `APPROVED` default and therefore asserted the pre-fix readiness oracle through a downstream wrapper | `STALE_TEST_ORACLE` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | default the wrapper's ready fixture to `ACTIVE` and add an explicit `APPROVED` selected/body-read-denied regression | Handled before P7 dispatch |

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - both defects are
entirely local repository governance/control-plane behavior; no provider
call, credential, quota, runtime activation, or cost evidence is involved.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add the shared lifecycle-status gate to
the two named activation-decision functions and their focused hostile tests;
extend the finding-heading regex in the Finding-To-Governance checker and its
focused tests; preserve every other predicate, checker behavior, and
protected-path boundary.

Protected paths:

- `governance/compat/generate_skill_control_plane_inventory.py`
- `governance/compat/test_skill_control_plane_inventory.py`
- `governance/compat/run_assf_active_resolver.py`
- `governance/compat/test_run_assf_active_resolver.py`
- `governance/compat/check_finding_to_governance_learning.py`
- `governance/compat/test_check_finding_to_governance_learning.py`

Operator authorization: operator instruction to Local to treat the S07
blocked-return recurrence as a root defect, fix it before continuing, and
correct the Finding-To-Learning failure, converted into the NCR-R1/S07-R1
work order.

Rollback boundary: revert only the six protected-path edits listed above,
this ADIF entry, and the two reconciled standard sections if the hostile
tests or reviewer independent probe reject the predicate; preserve the
retained P6 truth packet, the S07 blocked return, and the S06-R1 accepted
correction as evidence.

## Machine Enforcement

`governance/compat/test_skill_control_plane_inventory.py` and
`governance/compat/test_run_assf_active_resolver.py` each assert that an
`APPROVED`, runtime-eligible, truth-approved fixture returns
`DENIED_SOURCE_NOT_ACTIVE` (not `ACTIVATION_READY`) and that an otherwise
identical `ACTIVE` fixture returns `ACTIVATION_READY`.
`governance/compat/test_run_assf_activation_policy_resolver.py` carries that
same boundary through the policy wrapper: ready cases use `ACTIVE`, while an
explicit `APPROVED` case remains `SELECTED` and cannot request a body read.
`governance/compat/test_check_finding_to_governance_learning.py` asserts that
a `## Findings / Position` heading with no learning disposition fails, and
that the same heading with a disposition section passes. It also proves a
known cluster cannot self-declare first occurrence, a non-path prior finding
is rejected, and a complete recurring cluster with an existing matching prior
path passes. The inventory/resolver tests cover the complete denial-priority
matrix, including runtime-ineligible plus missing truth.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | shared-workspace INTERNAL_AGENT root-correction worker |
| Provider or surface | private CVF workspace |
| Session or invocation | NCR-R1/S07-R1 root correction, 2026-09-27 |
| Working directory | repository root |
| Command or tool surface | governed source reads, Python checkers/generators/unittest, Node.js Web generator, read-only Git status/diff |
| Target paths | this entry; ADIF README index; six protected checker/test paths; two reconciled standards; regenerated inventory and Web projections |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R1_S07_R1_ACTIVATION_PHASE_AND_LEARNING_ESCALATION_ROOT_RECONCILIATION_2026-09-27.md` Required Root Contract items 1-11 |
| Before status evidence | S07 blocked return recorded `ACTIVATION_READY` for an `APPROVED` truth-approved package; the F2G checker's heading regex did not match `## Findings / Position` |
| After status evidence | inventory and active resolver agree on `DENIED_SOURCE_NOT_ACTIVE` for the same package; the heading regex matches `## Findings / Position` directly |
| Diff evidence | exact changed set and hostile-test pass evidence in the paired worker return |
| Approval boundary | bounded root-contract correction only; no `ACTIVE`, resolver body-read, external adapter, or provider/live/public/production action taken |
| Claim boundary | defect-record and machine-check-added claim only; no runtime/provider/live claim |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | `adif-0060-ncr-r1-s07-r1-activation-learning-root-20260927` |
| Expected manifest | this entry and ADIF README index row |
| Actual changed set | verified against the work order's exact 25-path manifest before worker return |
| Manifest delta | MATCH |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance learning. No public-sync action or
public catalog claim is authorized.

## Epistemic Process Block

### Expected Result / Prediction

Adding one shared lifecycle-status condition to both activation-decision
functions, proven by one hostile APPROVED/ACTIVE regression pair in each
focused test module, was expected to make the target package deny activation
consistently across the inventory and the live active resolver while leaving
every existing `ACTIVE` package's readiness decision unchanged. Extending the
finding-heading regex was expected to make the learning gate reject a
`## Findings / Position` return with no disposition, independent of whether
that return also happens to contain a `| Finding |` table.

### Evidence Comparison

Both hostile regression pairs fail on the pre-fix predicate shape and pass
post-fix; the live active resolver and the regenerated inventory now agree
exactly (`DENIED_SOURCE_NOT_ACTIVE`) for `cvf-engineering-test-evidence-audit`;
the pre-existing `ACTIVE`-status resolver test continues to pass unchanged
because its fixture's own default `status` was corrected from `APPROVED` to
`ACTIVE`, removing a same-defect false positive from the test suite itself.
The heading-regex test that previously asserted a `## Findings / Position`
heading alone was not a finding marker now asserts the opposite, and a
companion positive test proves a disposition section clears the requirement.

### Contradiction Or Gap Disposition

The pre-existing resolver test `test_ready_internal_agent_decision` asserted
`READY_DECISION` against a fixture whose `status` field was `APPROVED`, which
means the prior test suite encoded the same status-gate omission as a passing
assertion rather than only missing coverage. This is disclosed rather than
silently corrected: the fixture default changed from `APPROVED` to `ACTIVE`
so the existing test continues to assert genuine `ACTIVE` readiness.

### Claim Update

Both root defects are confirmed and resolved for the currently exercised
case (`cvf-engineering-test-evidence-audit`) and for the general predicate and
heading-detection shape; this does not certify every other package or
finding-bearing artifact in the repository, only the named surfaces and their
focused hostile tests.

## Claim Boundary

This entry records and guards one activation-decision lifecycle-gate omission
and one finding-heading detection gap. It does not validate every
package's activation correctness, authorize `ACTIVE` promotion or P7-P10
execution, repair the durable run store, or authorize provider/live/public/
deployment/production action.
