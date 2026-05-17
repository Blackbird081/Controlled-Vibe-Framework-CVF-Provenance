# CVF 17.05 Stabilization Drift Inventory

Date: 2026-05-17

Memory class: FULL_RECORD

Status: PHASE 1.0 DRIFT INVENTORY ARTIFACT. Produced by
`scripts/run_cvf_17_05_drift_inventory.py`.

This file does not authorize implementation, does not modify runtime code,
does not change public claims, and does not change release gates.

Authorized by:
`.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_REVIEW_CVF_FINAL_CONVERGED_REMEDIATION_ROADMAP_2026-05-17.md`

Generated: 2026-05-17T16:46:28Z

## Purpose

Produce a reproducible, machine-generated inventory of drift surfaces identified
in the 17.05 Review CVF absorption review chain (Problems A, G, H) before any
runtime code is changed. This inventory is the Phase 1.0 gating artifact that
must exist before Phases 1.P, 1.I, 1.R, and 1.M may open.

## Target

Source: `Review CVF.md` Problems A (internal coherence), G (execution identity
drift), H (memory hierarchy). Repo surfaces searched: `EXTENSIONS/`, `governance/`,
`tools/`, `docs/`. Concern groups: PolicyEngine, RiskEngine/RiskScorer,
GuardEngine, AgentRole/ActorRole/CVFRole, Receipt/Ledger/AuditLog, Memory/MemoryHome.

## Scope

Surfaces inventoried: PolicyEngine, RiskEngine/RiskScorer, GuardEngine,
AgentRole/ActorRole/CVFRole, Receipt/Ledger/AuditLog, Memory/MemoryHome.

## Disposition Taxonomy

| Disposition | Meaning |
|---|---|
| `canonical_contract` | authoritative contract home for this concern |
| `adapter` | domain-specific behavior emitting/consuming canonical contract |
| `legacy_reference` | historical/sample/template module retained as reference |
| `deprecate_candidate` | obsolete path, only after consumer analysis proves it |

## Summary

Total distinct surface files found: **94**

| Concern | Files found | Query |
|---|---:|---|
| PolicyEngine | 13 | `class .*PolicyEngine\|RoutingPolicyEngine\|PolicyDecisionEngine\|BasePolicyEngin...` |
| RiskEngine / RiskScorer | 26 | `class.*RiskScorer\|class.*RiskEngine\|class.*RiskPropagation\|export class.*Risk...` |
| GuardEngine | 7 | `class.*GuardEngine\|class.*GuardRuntime\|class.*ContaminationGuard...` |
| AgentRole / ActorRole / CVFRole | 20 | `enum\s+\w*Role\b\|type\s+\w*Role\s*=\|AgentRole\|CVFRole\|ActorRole\|OperatorRol...` |
| Receipt / Ledger / AuditLog | 27 | `interface.*Receipt\|class.*Receipt\|type.*Receipt\s*=\|GatewayReceipt\|SkillAudi...` |
| Memory / MemoryHome | 1 | `MemoryHome\|MemoryStore\|WorkingMemory\|SkillMemory\|TaskMemory\|working_memory\...` |

## Acceptance Gate

Per Phase 1.0 acceptance criteria:

- [x] Inventory file exists
- [x] Script exists and records exact queries used
- [x] Script is deterministic (same tree -> same output)
- [x] No runtime code modified
- [ ] Every listed surface receives a proposed disposition (see per-concern tables below — requires manual verification of heuristic entries)
- [ ] Phases 1.P / 1.I / 1.R / 1.M remain blocked until manual verification of this inventory is complete

## PolicyEngine

Policy decision engine implementations across extensions and governance

**Exact query used:**

```
rg --no-heading -n "class .*PolicyEngine|RoutingPolicyEngine|PolicyDecisionEngine|BasePolicyEngine|class PolicyEngine" EXTENSIONS governance tools docs
```

**Hit count:** 0 matching lines → 13 distinct files

| File path | Domain | Proposed disposition | Notes |
|---|---|---|---|
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | CVF_MODEL_GATEWAY | `adapter` | Gateway domain — likely adapter over canonical contract |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | CVF_MODEL_GATEWAY | `adapter` | Gateway routing policy — domain adapter over canonical contract once defined |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/model-gateway-runtime.integration.test.ts` | CVF_MODEL_GATEWAY | `legacy_reference` | Test fixture — not a production surface |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/routing-policy.test.ts` | CVF_MODEL_GATEWAY | `legacy_reference` | Test fixture — not a production surface |
| `EXTENSIONS/CVF_STARTER_TEMPLATE_REFERENCE/src/cvf/policy-engine.service.ts` | CVF_STARTER_TEMPLATE_REFERENCE | `legacy_reference` | Starter template reference — illustrative, not production policy authority |
| `EXTENSIONS/CVF_v1.2.1_EXTERNAL_INTEGRATION/certification/certification.state.machine.ts` | CVF_v1.2.1_EXTERNAL_INTEGRATION | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_v1.2.1_EXTERNAL_INTEGRATION/policies/policy.decision.engine.ts` | CVF_v1.2.1_EXTERNAL_INTEGRATION | `adapter` | External integration policy adapter — domain-specific; not the canonical home |
| `EXTENSIONS/CVF_v1.2.1_EXTERNAL_INTEGRATION/tests/v1.2.1.pipeline.test.ts` | CVF_v1.2.1_EXTERNAL_INTEGRATION | `legacy_reference` | Test fixture — not a production surface |
| `EXTENSIONS/CVF_v1.2.1_EXTERNAL_INTEGRATION/tests/v1.2.1.test.ts` | CVF_v1.2.1_EXTERNAL_INTEGRATION | `legacy_reference` | Test fixture — not a production surface |
| `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/server.py` | CVF_v1.6.1_GOVERNANCE_ENGINE | `canonical_contract` | Primary domain engine — heuristic canonical candidate |
| `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core/policy_engine.py` | CVF_v1.6.1_GOVERNANCE_ENGINE | `canonical_contract` | Python governance core — primary policy authority for Python governance path |
| `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core_orchestrator.py` | CVF_v1.6.1_GOVERNANCE_ENGINE | `canonical_contract` | Primary domain engine — heuristic canonical candidate |
| `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/main.py` | CVF_v1.6.1_GOVERNANCE_ENGINE | `canonical_contract` | Primary domain engine — heuristic canonical candidate |

## RiskEngine / RiskScorer

Risk scoring and risk propagation engine implementations

**Exact query used:**

```
rg --no-heading -n "class.*RiskScorer|class.*RiskEngine|class.*RiskPropagation|export class.*Risk" EXTENSIONS governance tools docs
```

**Hit count:** 0 matching lines → 26 distinct files

| File path | Domain | Proposed disposition | Notes |
|---|---|---|---|
| `EXTENSIONS/CVF_ECO_v1.2_LLM_RISK_ENGINE/src/risk.aggregator.ts` | CVF_ECO_v1.2_LLM_RISK_ENGINE | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v1.2_LLM_RISK_ENGINE/src/risk.scorer.ts` | CVF_ECO_v1.2_LLM_RISK_ENGINE | `canonical_contract` | LLM risk engine — primary risk scorer for the ECO risk domain |
| `EXTENSIONS/CVF_ECO_v2.0_AGENT_GUARD_SDK/src/risk.module.ts` | CVF_ECO_v2.0_AGENT_GUARD_SDK | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/node_modules/cvf-guard-contract/src/guards/risk-gate.guard.ts` | CVF_ECO_v2.5_MCP_SERVER | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/risk-gate.guard.ts` | CVF_ECO_v2.5_MCP_SERVER | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/guards/risk-gate.guard.ts` | CVF_GUARD_CONTRACT | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_PLANE_FACADES/node_modules/cvf-guard-contract/src/guards/risk-gate.guard.ts` | CVF_PLANE_FACADES | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_STARTER_TEMPLATE_REFERENCE/src/core/error.types.ts` | CVF_STARTER_TEMPLATE_REFERENCE | `legacy_reference` | Template or reference module — heuristic classification |
| `EXTENSIONS/CVF_STARTER_TEMPLATE_REFERENCE/src/cvf/risk-classifier.service.ts` | CVF_STARTER_TEMPLATE_REFERENCE | `legacy_reference` | Template or reference module — heuristic classification |
| `EXTENSIONS/CVF_STARTER_TEMPLATE_REFERENCE/src/cvf/risk-escalation.service.ts` | CVF_STARTER_TEMPLATE_REFERENCE | `legacy_reference` | Template or reference module — heuristic classification |
| `EXTENSIONS/CVF_TOOLKIT_REFERENCE/02_TOOLKIT_CORE/errors.ts` | CVF_TOOLKIT_REFERENCE | `legacy_reference` | Template or reference module — heuristic classification |
| `EXTENSIONS/CVF_TOOLKIT_REFERENCE/04_EXTENSION_LAYER/_extension.template/domain.risk.profile.template.ts` | CVF_TOOLKIT_REFERENCE | `legacy_reference` | Template or reference module — heuristic classification |
| `EXTENSIONS/CVF_TOOLKIT_REFERENCE/04_EXTENSION_LAYER/financial.extension/financial.risk.profile.ts` | CVF_TOOLKIT_REFERENCE | `legacy_reference` | Template or reference module — heuristic classification |
| `EXTENSIONS/CVF_TOOLKIT_REFERENCE/dist/04_EXTENSION_LAYER/financial.extension/financial.risk.profile.d.ts` | CVF_TOOLKIT_REFERENCE | `legacy_reference` | Template or reference module — heuristic classification |
| `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/guards/risk.gate.guard.ts` | CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_v1.2.1_EXTERNAL_INTEGRATION/governance_hooks/risk.scoring.hook.ts` | CVF_v1.2.1_EXTERNAL_INTEGRATION | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE/skill_system/governance/risk.scorer.ts` | CVF_v1.2.2_SKILL_GOVERNANCE_ENGINE | `adapter` | Skill governance domain risk scorer — adapter consuming risk engine output |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/cvf-guard-contract/src/guards/risk-gate.guard.ts` | CVF_v1.6_AGENT_PLATFORM | `adapter` | Web platform memory surfaces — UI-layer adapters, not canonical memory home |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/internal_ledger/risk_evolution.ts` | CVF_v1.7.1_SAFETY_RUNTIME | `canonical_contract` | Safety runtime domain — GuardEngine canonical home for safety path |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_detector.ts` | CVF_v1.7.1_SAFETY_RUNTIME | `canonical_contract` | Safety runtime domain — GuardEngine canonical home for safety path |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_propagation_engine.ts` | CVF_v1.7.1_SAFETY_RUNTIME | `adapter` | Risk propagation within contamination guard kernel — bounded domain adapter |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/03_contamination_guard/risk_scorer.ts` | CVF_v1.7.1_SAFETY_RUNTIME | `adapter` | Contamination guard kernel adapter — domain-specific risk scorer |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/kernel-architecture/kernel/04_refusal_router/refusal.risk.ts` | CVF_v1.7.1_SAFETY_RUNTIME | `canonical_contract` | Safety runtime domain — GuardEngine canonical home for safety path |
| `EXTENSIONS/CVF_v1.7.1_SAFETY_RUNTIME/policy/risk.engine.ts` | CVF_v1.7.1_SAFETY_RUNTIME | `canonical_contract` | Safety runtime risk engine — canonical for the safety runtime domain |
| `EXTENSIONS/CVF_v1.8_SAFETY_HARDENING/core/risk/risk.lock.ts` | CVF_v1.8_SAFETY_HARDENING | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_v1.8_SAFETY_HARDENING/core/risk/risk.scorer.ts` | CVF_v1.8_SAFETY_HARDENING | `adapter` | Safety hardening domain risk scorer — inherits from safety runtime domain |

## GuardEngine

Guard and contamination guard engine implementations

**Exact query used:**

```
rg --no-heading -n "class.*GuardEngine|class.*GuardRuntime|class.*ContaminationGuard" EXTENSIONS governance tools docs
```

**Hit count:** 0 matching lines → 7 distinct files

| File path | Domain | Proposed disposition | Notes |
|---|---|---|---|
| `EXTENSIONS/CVF_ECO_v1.3_DOMAIN_GUARDS/src/guard.engine.ts` | CVF_ECO_v1.3_DOMAIN_GUARDS | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/dist/guards/engine.d.ts` | CVF_ECO_v2.5_MCP_SERVER | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/node_modules/cvf-guard-contract/src/engine.ts` | CVF_ECO_v2.5_MCP_SERVER | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` | CVF_ECO_v2.5_MCP_SERVER | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | CVF_GUARD_CONTRACT | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_PLANE_FACADES/node_modules/cvf-guard-contract/src/engine.ts` | CVF_PLANE_FACADES | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/cvf-guard-contract/src/engine.ts` | CVF_v1.6_AGENT_PLATFORM | `adapter` | Web platform memory surfaces — UI-layer adapters, not canonical memory home |

## AgentRole / ActorRole / CVFRole

Role type definitions across the repo — enum, type alias, or class

**Exact query used:**

```
rg --no-heading -n "enum\s+\w*Role\b|type\s+\w*Role\s*=|AgentRole|CVFRole|ActorRole|OperatorRole" EXTENSIONS governance tools docs
```

**Hit count:** 0 matching lines → 20 distinct files

| File path | Domain | Proposed disposition | Notes |
|---|---|---|---|
| `EXTENSIONS/CVF_AGENT_DEFINITION/node_modules/typescript/lib/lib.dom.d.ts` | CVF_AGENT_DEFINITION | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_AGENT_DEFINITION/src/index.ts` | CVF_AGENT_DEFINITION | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_AGENT_LEDGER/node_modules/typescript/lib/lib.dom.d.ts` | CVF_AGENT_LEDGER | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/node_modules/typescript/lib/lib.dom.d.ts` | CVF_CONTROL_PLANE_FOUNDATION | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.definition.boundary.contract.ts` | CVF_CONTROL_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/continuity.checkpoint.contract.ts` | CVF_CONTROL_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.continuation.barrel.ts` | CVF_CONTROL_PLANE_FOUNDATION | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.coordination.barrel.ts` | CVF_CONTROL_PLANE_FOUNDATION | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.design.boardroom.barrel.ts` | CVF_CONTROL_PLANE_FOUNDATION | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/design.contract.ts` | CVF_CONTROL_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/orchestration.contract.ts` | CVF_CONTROL_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/helpers/cpf.batch.contract.fixtures.ts` | CVF_CONTROL_PLANE_FOUNDATION | `legacy_reference` | Test fixture — not a production surface |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/index.test.ts` | CVF_CONTROL_PLANE_FOUNDATION | `legacy_reference` | Test fixture — not a production surface |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/orchestration.batch.contract.test.ts` | CVF_CONTROL_PLANE_FOUNDATION | `legacy_reference` | Test fixture — not a production surface |
| `EXTENSIONS/CVF_ECO_v1.0_INTENT_VALIDATION/node_modules/typescript/lib/lib.dom.d.ts` | CVF_ECO_v1.0_INTENT_VALIDATION | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v1.1_NL_POLICY/node_modules/typescript/lib/lib.dom.d.ts` | CVF_ECO_v1.1_NL_POLICY | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v1.2_LLM_RISK_ENGINE/node_modules/typescript/lib/lib.dom.d.ts` | CVF_ECO_v1.2_LLM_RISK_ENGINE | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v1.3_DOMAIN_GUARDS/node_modules/typescript/lib/lib.dom.d.ts` | CVF_ECO_v1.3_DOMAIN_GUARDS | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v1.4_RAG_PIPELINE/node_modules/typescript/lib/lib.dom.d.ts` | CVF_ECO_v1.4_RAG_PIPELINE | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_ECO_v2.0_AGENT_GUARD_SDK/node_modules/typescript/lib/lib.dom.d.ts` | CVF_ECO_v2.0_AGENT_GUARD_SDK | `adapter` | Eco/external/hardening module — domain adapter heuristic |

## Receipt / Ledger / AuditLog

Receipt, audit ledger, and evidence envelope type/class definitions

**Exact query used:**

```
rg --no-heading -n "interface.*Receipt|class.*Receipt|type.*Receipt\s*=|GatewayReceipt|SkillAuditReceipt|GovernanceLedger|AuditLogEntry" EXTENSIONS governance tools docs
```

**Hit count:** 0 matching lines → 27 distinct files

| File path | Domain | Proposed disposition | Notes |
|---|---|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/agent.governed.session.contract.ts` | CVF_CONTROL_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/consumer.contract.ts` | CVF_CONTROL_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/design.consumer.contract.ts` | CVF_CONTROL_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/gateway.consumer.contract.ts` | CVF_CONTROL_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/knowledge.vault.intake.types.ts` | CVF_CONTROL_PLANE_FOUNDATION | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/packaging.contract.ts` | CVF_CONTROL_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/node_modules/cvf-guard-contract/src/types.ts` | CVF_ECO_v2.5_MCP_SERVER | `adapter` | Eco/external/hardening module — domain adapter heuristic |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.bridge.consumer.batch.contract.ts` | CVF_EXECUTION_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.bridge.consumer.contract.ts` | CVF_EXECUTION_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.observer.contract.ts` | CVF_EXECUTION_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.pipeline.contract.ts` | CVF_EXECUTION_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.business.adapter.contract.ts` | CVF_EXECUTION_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/tool.call.trace.contract.ts` | CVF_EXECUTION_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | CVF_GUARD_CONTRACT | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract.ts` | CVF_LEARNING_PLANE_FOUNDATION | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` | CVF_MODEL_GATEWAY | `adapter` | Gateway domain — likely adapter over canonical contract |
| `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | CVF_MODEL_GATEWAY | `adapter` | Gateway domain — likely adapter over canonical contract |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/gateway-receipt.test.ts` | CVF_MODEL_GATEWAY | `legacy_reference` | Test fixture — not a production surface |
| `EXTENSIONS/CVF_MODEL_GATEWAY/tests/model-gateway-runtime.integration.test.ts` | CVF_MODEL_GATEWAY | `legacy_reference` | Test fixture — not a production surface |
| `EXTENSIONS/CVF_PLANE_FACADES/node_modules/cvf-control-plane-foundation/src/agent.governed.session.contract.ts` | CVF_PLANE_FACADES | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_PLANE_FACADES/node_modules/cvf-control-plane-foundation/src/consumer.contract.ts` | CVF_PLANE_FACADES | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_PLANE_FACADES/node_modules/cvf-control-plane-foundation/src/design.consumer.contract.ts` | CVF_PLANE_FACADES | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_PLANE_FACADES/node_modules/cvf-control-plane-foundation/src/gateway.consumer.contract.ts` | CVF_PLANE_FACADES | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_PLANE_FACADES/node_modules/cvf-control-plane-foundation/src/knowledge.vault.intake.types.ts` | CVF_PLANE_FACADES | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_PLANE_FACADES/node_modules/cvf-control-plane-foundation/src/packaging.contract.ts` | CVF_PLANE_FACADES | `canonical_contract` | Base contract or interface — heuristic; verify before migration |
| `EXTENSIONS/CVF_PLANE_FACADES/node_modules/cvf-guard-contract/src/types.ts` | CVF_PLANE_FACADES | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |
| `EXTENSIONS/CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL/governance/guard_runtime/wiring/extension.bridge.ts` | CVF_v1.1.1_PHASE_GOVERNANCE_PROTOCOL | `adapter` | Unclassified — requires manual review in Phase 1.P/1.I/1.R/1.M |

## Memory / MemoryHome

Memory store, working memory, skill memory, and continuity homes

**Exact query used:**

```
rg --no-heading -n "MemoryHome|MemoryStore|WorkingMemory|SkillMemory|TaskMemory|working_memory|task_memory|skill_memory" EXTENSIONS governance tools docs
```

**Hit count:** 0 matching lines → 1 distinct files

| File path | Domain | Proposed disposition | Notes |
|---|---|---|---|
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/node_modules/express-rate-limit/dist/index.d.ts` | CVF_ECO_v2.5_MCP_SERVER | `adapter` | Eco/external/hardening module — domain adapter heuristic |

## Findings

Total distinct surface files found: **94** across 6 concern groups.

Key findings:

- PolicyEngine: 5+ distinct implementations span gateway, external integration,
  starter template, and Python governance domains with no canonical contract home.
- RiskEngine/RiskScorer: 7+ distinct implementations span ECO risk engine, skill
  governance, safety runtime, and safety hardening domains.
- GuardEngine: 3 distinct implementations include a class-name collision risk between
  domain adapters and the safety runtime canonical surface.
- AgentRole/CVFRole/ActorRole: 10+ role type definitions in incompatible taxonomies
  across guard, web governance, multi-agent, enterprise, and safety domains.
- Receipt/Ledger: 27 distinct surfaces with no canonical Receipt<TPayload> envelope.
- Memory/MemoryHome: 1 surface found for canonical memory-tier vocabulary — the
  working_memory/task_memory/skill_memory tier model has no active implementation.

All dispositions in the per-concern tables are heuristic proposals requiring manual
verification before Phases 1.P/1.I/1.R/1.M may proceed.

## Phase Gate

Phases 1.P, 1.I, 1.R, and 1.M are BLOCKED until:

1. This inventory is manually reviewed and heuristic dispositions are confirmed.
2. Each `adapter` entry is verified to have an identified canonical contract home.
3. Each `deprecate_candidate` entry has a consumer analysis proving the path is obsolete.
4. A separate GC-018 is filed for each sub-phase (1.P, 1.I, 1.R, 1.M).

Phase 2.A contract sketch may begin after this inventory is accepted.

## Raw Evidence

The raw grep output for each concern is not included here for brevity.
Re-run `scripts/run_cvf_17_05_drift_inventory.py` to regenerate with current working tree.

## Claim Boundary

This inventory:

- does not authorize implementation of any Phase 1 sub-phase
- does not modify runtime code
- does not change public claims or release gates
- does not promote any private review source into CVF canon
- does not claim live governance proof
- does not reopen F-1 output-quality parity work
- proposed dispositions are heuristic only — manual verification required
- `deprecate_candidate` disposition must not be acted on without separate consumer analysis
