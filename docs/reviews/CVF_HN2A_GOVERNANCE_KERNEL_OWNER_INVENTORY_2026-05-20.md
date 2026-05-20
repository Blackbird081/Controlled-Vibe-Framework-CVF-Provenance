# CVF HN2.a Governance Kernel Owner Inventory

Memory class: FULL_RECORD

Status: INVENTORY_FILED

docType: review

Reviewer: Codex (Orchestrator-author)

Date: 2026-05-20

---

## Purpose

Record a static observation inventory of the 12 governance-kernel surfaces named
by HN2.a. The inventory exists so later HN2.b and HN2.c work can classify owners
and codify freeze-release rules without mixing observation with policy.

## Scope / Target / Owner Boundary

Scope is limited to the 12 surfaces named in
`docs/work_orders/CVF_WO_HN2A_GOVERNANCE_KERNEL_OWNER_INVENTORY_2026-05-20.md`.
This file records current owner candidates, legacy aliases, terms, ambiguity,
and evidence paths. It does not modify guards, runtime, policy, provider,
registry, doctrine, or public-sync surfaces.

## Source / Target

Sources read:

- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`
- `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`
- `governance/toolkit/05_OPERATION/`
- `ECOSYSTEM/doctrine/`
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
- `docs/CVF_ARCHITECTURE_DECISIONS.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/*/execution.policy.json`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/`
- `docs/reference/CVF_AGENT_ROLE_CATALOG.md`

Target artifact: this inventory file.

## Scope / Methodology

Method: read only. I listed the required directories, read the named documents
and contracts, and mapped each fixed surface to a current owner candidate where
one was directly observable. Terms and aliases are literal observations from
the read set. No classification column, policy verdict, or downstream owner-map
claim is included.

## Findings / Position

All 12 required surfaces are observable in existing CVF artifacts. Several
surfaces have strong current owner candidates in `CVF_GUARD_CONTRACT`, the
governed web execute path, the model gateway, and the agent role catalog.
Ambiguity remains where the source material names a full system chain while the
current repository has several local contracts that each carry part of that
chain.

## Per-Surface Inventory Table

| surfaceName | currentCanonicalOwnerCandidate | legacyAliasesObserved | termsObserved | ambiguityNote | evidencePaths |
| --- | --- | --- | --- | --- | --- |
| Authority model | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts` | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`, `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`, `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | authority hierarchy, Orchestrator, delegatingRole, worker lane, approval checkpoint | Current code has an orchestrator contract and control matrix, while legacy packets describe a broader role-boundary chain. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`, `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` |
| Role model | `docs/reference/CVF_AGENT_ROLE_CATALOG.md` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`, `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/role-permission.contract.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts` | CVFRole, role templates, allowed_outputs, permission_model, execution authority labels | Catalog roles and runtime pack authority labels coexist with explicit separation. | `docs/reference/CVF_AGENT_ROLE_CATALOG.md`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-role-resolver.ts` |
| Policy decision surface | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/policy-decision.contract.ts` | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/documentation/execution.policy.json`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/strategy_analysis/execution.policy.json` | PolicyDecision, allow, deny, escalate, defer, guardPolicyRef, requiredRole | Contract-level policy decisions and pack-local policy JSON are separate observable surfaces. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/policy-decision.contract.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json` |
| Risk model | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/risk-engine.contract.ts` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`, `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`, `docs/CVF_ARCHITECTURE_DECISIONS.md` | R0, R1, R2, R3, RiskEngine, RiskSignal, R_SCALE_POLICY_BINDING | R-scale appears in several places, with the risk-engine contract carrying the clearest current contract. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/risk-engine.contract.ts`, `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` |
| Guard model | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | `governance/toolkit/05_OPERATION/CVF_GUARD_REGISTRY_GUARD.md`, `governance/toolkit/05_OPERATION/CVF_GUARD_AUTHORING_STANDARD_GUARD.md`, `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | GuardRuntimeEngine, Guard, GuardDecision, runtime guard, CI repo gate | Runtime guard engine and repository guard standards both carry guard terminology. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts`, `governance/toolkit/05_OPERATION/CVF_GUARD_AUTHORING_STANDARD_GUARD.md` |
| Execution lifecycle | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`, `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`, `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md` | INTAKE, DESIGN, BUILD, REVIEW, FREEZE, RuntimeWorkflowState, workflow state | Phase vocabulary and runtime workflow metadata overlap but are directly traceable. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/runtime-workflow.contract.ts`, `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` |
| Delegation / handoff | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts` | `docs/reference/CVF_ADR_AGENT_HANDOFF_CONTRACT_RELATIONSHIP_2026-05-17.md`, `docs/reference/CVF_ADR_DELEGATION_CONTRACT_AND_CPF_RELATIONSHIP_2026-05-17.md`, `AGENT_HANDOFF_V10_2026-05-19.md` | delegation, handoff, WorkerLaneTicket, delegationReceiptId, transition | Handoff continuity and orchestrator delegation are adjacent but not a single file surface. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/orchestrator.contract.ts`, `AGENT_HANDOFF_V10_2026-05-19.md` |
| Receipt envelope | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts` | GovernanceEvidenceReceipt, GatewayReceipt, evidence receipt, receiptId, envelopeId | Multiple receipt shapes exist for different lanes, with the guard contract carrying the shared evidence receipt type. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/web-governance-envelope.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` |
| Memory tier model | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts` | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_SYSTEM_RECONVERGENCE_STOP_DECISION_2026-05-17.md`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts` | working, task, skill, organizational, long-term, audit, receipt, reinjection | The classifier is explicit that it is contract-only and not runtime reinjection wiring. | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts` |
| Capability surface | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/skill-registry.ts` | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/full-skill-registry.ts`, `docs/reference/CVF_GOVERNED_CAPABILITY_INTAKE_DOCTRINE_2026-05-07.md`, `docs/reference/CVF_GOVERNED_CAPABILITY_INTAKE_AND_BOUNDARY_FIRST_GOVERNANCE_DOCTRINE_2026-05-17.md` | skill, capability, governed capability, outcome workflow, certification | Skill registry and governed capability doctrine use adjacent capability vocabulary. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/skill-registry.ts`, `docs/reference/CVF_GOVERNED_CAPABILITY_INTAKE_DOCTRINE_2026-05-07.md` |
| Provider execution semantics | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/tool-call-contract.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/json-mode-contract.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/reasoning-contract.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts` | provider output, stream, tool call, json mode, reasoning, vision, gateway receipt | Provider method contracts are split by method surface under one model-gateway package. | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts`, `EXTENSIONS/CVF_MODEL_GATEWAY/src/gateway-receipt.ts` |
| Vocabulary aliases | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | `.private_reference/legacy/CVF 17.05/REVIEW FOLDER/CVF_17_05_GOVERNANCE_KERNEL_FREEZE_CODEX_RECOMMENDATION_2026-05-17.md`, `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md`, `docs/reference/CVF_AGENT_ROLE_CATALOG.md` | LegacyCVFPhaseAlias, DISCOVERY, canonical runtime vocabulary, aliases, term drift | Alias handling is explicit for phases, while broader kernel vocabulary is distributed across docs. | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts`, `ECOSYSTEM/doctrine/CVF_DOCTRINE_RULES.md`, `docs/reference/CVF_AGENT_ROLE_CATALOG.md` |

## Risk / Corrective Action

Downstream HN2.b inherits these risks if it skips classification discipline:

- Term drift can continue where runtime labels, catalog role templates, and
  legacy ORCHESTRATOR language use adjacent names.
- Receipt envelope work can overclaim if it treats web, gateway, audit-memory,
  and guard-contract receipts as one interchangeable runtime object.
- Provider semantics can over-bundle if method-specific contracts are treated as
  a unified runtime-provider claim.
- Memory work can blur capture and reinjection if the classifier contract is
  treated as persistence or prompt-injection wiring.

Corrective action belongs to HN2.b/HN2.c, not this inventory.

## Decision / Disposition

INVENTORY_ONLY. This file records observed owner candidates and evidence paths.
It does not classify ownership, write policy, file GC-018, or authorize runtime
work.

## Claim Boundary

This review is private provenance inventory. It makes no public claim, changes
no runtime behavior, and does not reopen any Review-CVF A-H pain point.
