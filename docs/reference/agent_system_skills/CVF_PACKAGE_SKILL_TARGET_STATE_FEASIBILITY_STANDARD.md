# CVF Package Skill Target-State Feasibility Standard

Memory class: FULL_RECORD

Status: ACTIVE_STANDARD

Date: 2026-09-28

docType: reference

EPISTEMIC_PROCESS_NA_WITH_REASON: normative dispatch-admission standard; it
defines required declarations and machine rejection behavior rather than
making an empirical outcome claim.

## Purpose

Prevent a package-productionization work order from reaching a worker when its
declared target lifecycle, truth state, activation decision, external adapter
posture, dependent projections, or blocker routing contradict canonical owner
rules.

## Scope

This standard applies to every new or changed work order containing
`## Package Skill Productionization Control Block`. It is enforced against the
explicit active work order at both pre-dispatch and pre-implementation.

## Owner Surface

The package productionization SOP owns phase semantics. Certified admission,
the productionization pipeline, inventory generator, active resolver and
CLI/MCP projection own the predicates that must agree with the declared target.
The autorun workflow owns early placement.

## Required Contract

Applicable work orders must contain exactly one
`## Package Skill Target-State Feasibility Contract` JSON object using
`cvf.packageSkillTargetStateFeasibility.v1`. It must declare:

- package identity and exact P3-P10 phase;
- complete target lifecycle/UAT/certification/internal/external/truth state;
- whether external use is actually claimed;
- expected internal activation and external read/output decisions;
- all canonical predicate sources read before dispatch;
- source mutation families used to infer generated dependent paths;
- blocker routing to Local with `BLOCKED_WITH_REASON` and no operator question.

## Phase And Decision Matrix

| Phase | Source status | Internal activation decision |
|---|---|---|
| P3 | `CANDIDATE` | `DENIED_NOT_RUNTIME_ELIGIBLE` |
| P4 | `PROPOSED` | `DENIED_NOT_RUNTIME_ELIGIBLE` |
| P5 | `APPROVED` | `DENIED_MISSING_TRUTH_PACKET` |
| P6-P7 | `APPROVED` | `DENIED_SOURCE_NOT_ACTIVE` |
| P8-P10 | `ACTIVE` | `ACTIVATION_READY` |

P5 and later require UAT `PASSED`, certification `CERTIFIED`, and internal
disposition `IMPLEMENTED`. P6 and later require approved `STRICT` truth.
External `IMPLEMENTED` is valid only when external use is claimed and concrete
adapter contract/evidence are declared. Internal-only `ACTIVE` may retain
`DEFERRED_WITH_REASON`; this never grants external body read or output use.

## Dependency Inference

The gate derives mandatory generated paths from declared mutation families:

- `REGISTRY_ENTRY`: generated skill index, inventory, Web skill index and Web
  control-plane projection;
- `PACKAGE_SOURCE`: inventory;
- `TRUTH_PACKET`: generated truth index, inventory and both Web projections;
- `USE_PROOF_RECEIPT`: no generated projection by itself.

Every inferred path must already appear in the work order before dispatch.
Workers must not discover a missing aggregate after implementation starts.

## Blocker Routing

Technical contradictions belong to Local. The contract must declare
`technicalDecisionOwner=LOCAL`, `workerTerminalReturn=BLOCKED_WITH_REASON`, and
`operatorQuestionAllowed=false`. Operator escalation remains appropriate only
for a genuine effect, expense, data, publication, or scope choice outside the
technical decision already delegated to Local.

## Machine Enforcement

```powershell
python governance/compat/check_package_skill_target_state_feasibility.py --active-work-order <path> --enforce
```

The autorun gate invokes this command immediately after dispatch-release
binding at pre-dispatch and pre-implementation. A structural gate PASS is not
a substitute for this semantic feasibility result.

## Risk / Corrective Action

The gate validates declared target semantics; it does not execute the target
state or prove implementation success. A newly discovered predicate must be
added to the standard, checker and hostile tests before a dependent work order
is released.

## Claim Boundary

This standard and checker authorize no lifecycle mutation, body read, package
execution, external adapter, provider/live call, public sync, deployment or
production action.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private CVF control-plane dispatch admission.
