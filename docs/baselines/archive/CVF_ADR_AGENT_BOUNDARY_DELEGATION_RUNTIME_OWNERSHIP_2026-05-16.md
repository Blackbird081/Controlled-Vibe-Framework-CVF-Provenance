<!-- Memory class: SUMMARY_RECORD -->

# CVF ADR Agent Boundary Delegation Runtime Ownership - 2026-05-16

Status: ACCEPTED.

## Purpose

Record the ownership decision for adopting Claude Kit agent-boundary knowledge
into CVF as executable Control Plane behavior.

## Scope

This ADR covers the first bounded Agent Boundary / Delegation tranche inside:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`

## Context

Claude Kit provides useful patterns for agent catalogs, role templates,
permission profiles, handoff contracts, risk policy, audit receipts, and
orchestration rules.

CVF must not absorb this as "more autonomous agents." CVF's product value is
that agents remain bounded workers under a control plane.

## Decision

Implement a CVF-owned `AgentGovernedSessionContract` in the Control Plane.

The contract owns:

- registered-agent action evaluation;
- capability self-extension denial;
- permission profile checks for files, tools, commands, and receipts;
- risk-based approval decisions;
- structured handoff validation;
- high-risk handoff approval stop;
- deterministic audit receipt generation.

## Alternatives

Alternative 1: copy Claude Kit markdown files into CVF extension folders.

Rejected because copied docs are not living runtime behavior.

Alternative 2: introduce a Claude Kit agent runtime dependency.

Rejected because CVF should govern external agents through adapters, not become
dependent on an external agent catalog.

Alternative 3: expand existing `AgentDefinitionBoundaryContract`.

Rejected for this tranche because the existing contract owns registration and
capability scope. Session permission, handoff, and receipt behavior is clearer
as a separate contract.

## Consequences

Positive:

- agent execution can be evaluated before it mutates state;
- handoff can be rejected when it lacks structured state or audit reference;
- high-risk handoff state stops for approval;
- future orchestrator/runtime tranches can consume the same decision and receipt
  objects.

Costs:

- no live agent runner is wired in this tranche;
- existing orchestration surfaces are not yet rewired to call this contract.

## Verification

Verification must include:

- Control Plane package typecheck;
- focused vitest coverage for the governed session contract;
- governance markdown and file-size checks before commit;
- full pre-push chain before provenance push.

## Claim Boundary

This ADR claims runtime ownership of the agent-boundary/session primitive only.
It does not claim live multi-agent execution enforcement across every CVF path.
