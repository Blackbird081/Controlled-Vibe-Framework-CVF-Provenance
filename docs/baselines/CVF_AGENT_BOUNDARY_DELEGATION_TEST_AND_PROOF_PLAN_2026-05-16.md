<!-- Memory class: SUMMARY_RECORD -->

# CVF Agent Boundary Delegation Test And Proof Plan - 2026-05-16

Status: ACTIVE TEST PLAN.

## Purpose

Define the verification bar for making Agent Boundary / Delegation knowledge
live inside CVF.

## Scope

Owner surface:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`

Implemented target:

- `AgentGovernedSessionContract`

## Source

This plan derives from the Claude Kit registry, permission, handoff, risk,
audit receipt, and orchestration source files.

## Decision

Use deterministic local tests because the implemented surface is a Control Plane
contract and does not execute a live external agent.

Live proof is required only for a future tranche that claims live external-agent
execution enforcement.

## Test Plan

Required local tests:

- registered agent with valid permission and risk is allowed;
- unregistered agent is denied;
- capability self-extension is denied;
- denied paths and tools are detected;
- high risk requires approval;
- approved high-risk action is allowed with constraints;
- structured handoff with audit reference is valid;
- vague handoff is rejected;
- high-risk handoff stops unless policy state requires approval;
- execution receipt includes agent, policy, file/tool, validation, handoff, and
  output evidence.

## Proof Plan

Required proof commands:

```bash
cd EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION
npm run check
npx vitest run tests/agent.governed.session.contract.test.ts --config vitest.config.ts
```

Repository-level proof before push:

```bash
python governance/compat/run_local_governance_hook_chain.py --hook pre-push
```

## Evidence

Expected evidence:

- typecheck pass;
- focused vitest pass;
- governance markdown/file-size checks pass;
- full pre-push chain pass before provenance push.

## Claim Boundary

Passing this plan proves deterministic local Control Plane contract behavior. It
does not prove live multi-agent execution.
