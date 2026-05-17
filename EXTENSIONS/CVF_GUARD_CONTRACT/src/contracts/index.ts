/**
 * CVF Canonical Contracts — Phase 1.P Barrel Export
 * ==================================================
 * Exports all canonical contract types and adapter maps defined in Phase 1.P.
 * Import from here, not from individual contract files.
 *
 * Authorized by: docs/baselines/CVF_GC018_PHASE_1P_POLICY_RISK_GUARD_CONVERGENCE_2026-05-18.md
 */

export type {
  PolicyDecision,
  PolicyRequestContext,
  PolicyDecisionResult,
  PolicyEvidence,
  PolicyEngine,
  PolicyEngineAdapterMeta,
} from './policy-decision.contract';

export {
  RiskLevel,
  RISK_LEVEL_ORDER,
  isMoreSevere,
  maxRiskLevel,
} from './policy-decision.contract';

export type { RiskLevel } from './policy-decision.contract';

export type {
  RiskAssessmentContext,
  RiskSignal,
  RiskAssessmentResult,
  RiskEngine,
  RiskEngineAdapterMeta,
} from './risk-engine.contract';

export {
  R_SCALE_POLICY_BINDING,
} from './risk-engine.contract';

export type { RScaleDefaultAction } from './risk-engine.contract';

export type {
  GuardEngineAdapter,
  GuardContribution,
  GuardEngineAdapterMeta,
} from './guard-engine.contract';

export {
  CANONICAL_GUARD_ENGINE,
  GUARD_ENGINE_ADAPTER_MAP,
} from './guard-engine.contract';

export { POLICY_ENGINE_ADAPTER_MAP } from './policy-engine-adapter-map';
export { RISK_ENGINE_ADAPTER_MAP } from './risk-engine-adapter-map';

export type {
  AgentFunctionRole,
  OperatorTeamRole,
  AuthRbacRole,
  GovernanceActorRole,
  RoleAxisAssignment,
  RoleAxisAdapterMeta,
} from './role-axis.contract';

export {
  CANONICAL_ROLE_SURFACES,
} from './role-axis.contract';

export { ROLE_AXIS_ADAPTER_MAP } from './role-axis-adapter-map';

export type {
  Receipt,
  GatewayReceiptPayload,
  ExecutionBridgeReceiptPayload,
  GovernanceLedgerReceiptPayload,
  ControlledMemoryReceiptPayload,
  GatewayReceipt,
  ExecutionBridgeReceipt,
  GovernanceLedgerReceipt,
  ControlledMemoryReceipt,
  ReceiptEnvelopeAdapterMeta,
} from './receipt-envelope.contract';

export {
  RECEIPT_SCHEMA_VERSION_1R,
} from './receipt-envelope.contract';

export { RECEIPT_ENVELOPE_ADAPTER_MAP } from './receipt-envelope-adapter-map';
