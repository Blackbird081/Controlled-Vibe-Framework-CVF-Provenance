<!-- Memory class: SUMMARY_RECORD -->

# CVF Agent Boundary Delegation Source Adoption Matrix - 2026-05-16

Status: ACTIVE SOURCE MATRIX.

## Purpose

Map the Claude Kit source files to the CVF runtime behavior adopted in this
tranche.

## Scope

Owner surface:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`

Implemented contract:

- `src/agent.governed.session.contract.ts`

Focused tests:

- `tests/agent.governed.session.contract.test.ts`

## Source

Source folder:

- `.private_reference/legacy/CVF 16.5/Claude Kit/`

## Decision

Adopt the agent-boundary subset as CVF-owned Control Plane behavior, not as a
Claude Kit runtime dependency.

## Adoption Matrix

| Source file | Adopted pattern | CVF owner behavior | Status |
|---|---|---|---|
| `CVF_AGENT_REGISTRY_SPEC.md` | agents must be registered before execution | action evaluation requires an `AgentDefinitionRecord` | adopted |
| `CVF_AGENT_PERMISSION_PROFILE.md` | minimum necessary permission | file/tool/command/receipt profile checks | adopted |
| `CVF_AGENT_HANDOFF_CONTRACT.md` | structured handoff required | handoff validator rejects missing summary/action/audit/state | adopted |
| `CVF_AGENT_RISK_POLICY.md` | risk belongs to action | risk threshold and critical approval behavior | adopted |
| `CVF_AGENT_AUDIT_RECEIPT.md` | no receipt, no valid execution | deterministic agent execution audit receipt | adopted |
| `CVF_AGENT_ORCHESTRATION_RULES.md` | one orchestrator, bounded workers | high-risk handoff stop and no free-form handoff boundary | adopted |
| `CVF_AGENT_ROLE_CATALOG.md` | role templates only | deferred to future catalog expansion; existing roles remain bounded | deferred |
| `CVF_AGENT_ADAPTER_BOUNDARY.md` | external agents pass through adapter | deferred to future live adapter integration | deferred |

## Evidence

Runtime evidence target:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/agent.governed.session.contract.test.ts`

## Verification

The matrix is valid only when:

- adopted rows map to tested owner behavior;
- deferred rows are explicit;
- no source file is silently copied as runtime authority.

## Claim Boundary

This matrix records a bounded agent-governance subset. It does not claim full
Claude Kit adoption.
