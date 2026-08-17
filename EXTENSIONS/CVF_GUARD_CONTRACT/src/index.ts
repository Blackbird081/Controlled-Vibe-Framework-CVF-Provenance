/**
 * CVF Guard Contract — Barrel Export
 * ===================================
 * SINGLE SOURCE OF TRUTH — import everything from here.
 *
 * Usage:
 *   import { GuardRuntimeEngine, createGuardEngine, type GuardRequestContext } from 'cvf-guard-contract';
 *
 * @module cvf-guard-contract
 */

// Types
export * from './types';

// Engine
export { GuardRuntimeEngine } from './engine';

// Runtime helpers
export {
  classifyHandoffTransition,
  requiresFormalHandoff,
  createHandoffCheckpoint,
  resolveHandoffCheckpoint,
} from './runtime/agent-handoff';

// Mandatory gateway (T1 runtime composition)
export type { GatewayConfig, GatewayResult } from './runtime/mandatory-gateway';
export {
  MandatoryGateway,
  createMandatoryGateway,
  DEFAULT_GATEWAY_CONFIG,
} from './runtime/mandatory-gateway';

// Multi-agent coordination (W6-T2)
export {
  AgentCoordinationBus,
  createCoordinationBus,
  buildCoordinationMessage,
} from './runtime/agent-coordination';

// Guards
export { PhaseGateGuard, PHASE_ROLE_MATRIX, PHASE_DESCRIPTIONS } from './guards/phase-gate.guard';
export { RiskGateGuard, RISK_DESCRIPTIONS } from './guards/risk-gate.guard';
export { AuthorityGateGuard, AUTHORITY_MATRIX, RESTRICTED_ACTIONS } from './guards/authority-gate.guard';
export { AiCommitGuard } from './guards/ai-commit.guard';
export { MutationBudgetGuard, DEFAULT_MUTATION_BUDGETS, ESCALATION_THRESHOLD } from './guards/mutation-budget.guard';
export { FileScopeGuard, PROTECTED_PATHS as FILE_SCOPE_PROTECTED_PATHS, READ_ONLY_ROLES, BUILDER_CLASS_ROLES } from './guards/file-scope.guard';
export { ScopeGuard, PROTECTED_PATHS, CVF_ROOT_INDICATORS } from './guards/scope.guard';
export { AuditTrailGuard } from './guards/audit-trail.guard';

// Phase D role-permission contract
export type {
  RolePermissionOutputClass,
  RolePermissionDenyRuleId,
  ReceiptOwnerAxis,
  ReceiptOwnerBoundary,
  RolePermissionProfile,
} from './contracts/role-permission.contract';

export {
  ROLE_PERMISSION_SCHEMA_VERSION,
  ROLE_PERMISSION_OUTPUT_CLASSES,
  ROLE_PERMISSION_DENY_RULES,
  ROLE_PERMISSION_PROFILES,
  getRolePermissionProfile,
  isOutputAllowedForRole,
  roleHasDenyRule,
  rolePermissionCoversAllRoles,
} from './contracts/role-permission.contract';

// Phase E workflow binding contract
export type {
  WorkflowBindingStatus,
  WorkflowStepDecision,
  WorkflowStepTraceSource,
  WorkflowStepRole,
  WorkflowStep,
  WorkflowBinding,
  WorkflowStepExecutionTrace,
  WorkflowBindingValidationResult,
} from './contracts/workflow-binding.contract';

export {
  WORKFLOW_BINDING_CONTRACT_VERSION,
  validateWorkflowBinding,
  getActiveWorkflowSteps,
} from './contracts/workflow-binding.contract';

// CADP T2A deliberate root authority API. It accepts only a committed grant
// path; caller-authored grant objects are not part of the input surface.
export type { CapabilityOwnerHandle, CapabilityOwnerBindingResult } from './contracts/capability-owner-binding.contract';
export { bindCommittedCapabilityOwnerGrant } from './contracts/capability-owner-binding.contract';

export type {
  ControlledAcquisitionPlan,
  ControlledAcquisitionApproval,
  ControlledAcquisitionReceipt,
  ControlledAcquisitionAuthorizationResult,
  ControlledAcquisitionReceiptResult,
  ControlledAcquisitionRepairInput,
  ControlledAcquisitionRepairDecision,
} from './contracts/controlled-acquisition.contract';
export {
  CONTROLLED_ACQUISITION_CONTRACT_VERSION,
  computeControlledAcquisitionPlanDigest,
  evaluateControlledAcquisitionAuthorization,
  reconcileControlledAcquisitionReceipt,
  evaluateControlledAcquisitionRepair,
} from './contracts/controlled-acquisition.contract';

export type {
  CapabilityRouteCandidate,
  CapabilityCandidateSet,
  CapabilityRouteIssue,
  CapabilityRouteDecision,
  CapabilityRouteEvaluationOptions,
  CapabilityReadinessInput,
  CapabilityReadinessDecision,
  CapabilityRouteStage,
  CapabilityReadinessState,
} from './contracts/capability-route-readiness.contract';
export {
  CAPABILITY_ROUTE_READINESS_CONTRACT_VERSION,
  evaluateCapabilityRoute,
  evaluateCapabilityReadiness,
} from './contracts/capability-route-readiness.contract';

// RSPB-AI-T8 capability bootstrap approval evidence binding kernel (pure,
// contract-only; no approval issuance, replay storage/consumption, executor,
// or I/O authority).
export type {
  CapabilityBootstrapApprovalEnvelopeClass,
  CapabilityBootstrapMutationEnvelopeEntry,
  CapabilityBootstrapApprovalEvidence,
  CapabilityBootstrapApprovalEvidenceBindingInput,
  CapabilityBootstrapApprovalEvidenceIssueCode,
  CapabilityBootstrapApprovalEvidenceIssue,
  CapabilityBootstrapApprovalEvidenceBindingResult,
} from './contracts/capability-bootstrap-approval-evidence.contract';
export {
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_CONTRACT_VERSION,
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION,
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION,
  evaluateCapabilityBootstrapApprovalEvidenceBinding,
} from './contracts/capability-bootstrap-approval-evidence.contract';

// RSPB-AI-T9 capability acquisition receipt verification and repair-stop
// kernel (pure, contract-only; no receipt persistence, evidence collection,
// rollback/repair execution, executor, or I/O authority).
export type {
  CapabilityAcquisitionReceiptOperationStatus,
  CapabilityAcquisitionReceiptRollbackStatus,
  CapabilityAcquisitionReceiptVerificationStatus,
  CapabilityAcquisitionReceiptOperationResult,
  CapabilityAcquisitionReceiptMutation,
  CapabilityAcquisitionReceiptArtifact,
  CapabilityAcquisitionReceiptVerification,
  CapabilityAcquisitionReceipt,
  CapabilityAcquisitionReceiptVerificationInput,
  CapabilityAcquisitionReceiptVerificationIssueCode,
  CapabilityAcquisitionReceiptVerificationIssue,
  CapabilityAcquisitionReceiptVerificationResult,
} from './contracts/capability-acquisition-receipt-verification.contract';
export {
  CAPABILITY_ACQUISITION_RECEIPT_VERIFICATION_CONTRACT_VERSION,
  CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION,
  CAPABILITY_ACQUISITION_RECEIPT_VERIFICATION_RESULT_VERSION,
  evaluateCapabilityAcquisitionReceiptVerification,
} from './contracts/capability-acquisition-receipt-verification.contract';

// RSPB-AI-T7 capability preflight profile policy selection kernel
// (pure, contract-only; no profile loading, environment observation,
// acquisition, network, or execution authority).
export type {
  CapabilityPreflightRiskLevel,
  CapabilityPreflightNetworkMode,
  CapabilityPreflightPrivilegePolicy,
  CapabilityPreflightProfile,
  CapabilityPreflightProfilePolicyInput,
  CapabilityPreflightProfilePolicyIssueCode,
  CapabilityPreflightProfilePolicyIssue,
  CapabilityPreflightProfilePolicyResult,
} from './contracts/capability-preflight-profile-policy.contract';
export {
  CAPABILITY_PREFLIGHT_PROFILE_POLICY_CONTRACT_VERSION,
  CAPABILITY_PREFLIGHT_PROFILE_POLICY_RESULT_VERSION,
  evaluateCapabilityPreflightProfilePolicy,
} from './contracts/capability-preflight-profile-policy.contract';

// CADP T5-R1 external-readout authority foundation (pure, contract-only).
export type {
  CadpExternalReadoutIssueCode,
  CadpExternalReadoutIssue,
  CadpExternalReadoutValidationResult,
  CadpExternalReadoutAllowlistedMetadata,
  CadpExternalCallerIdentityInput,
  CadpExternalReadoutIngressRequest,
  CadpExternalReadoutFreshnessInput,
  CadpExternalReadoutFreshnessDisposition,
  CadpExternalReadoutFreshnessResult,
  CadpExternalReadoutReceiptInput,
  CadpExternalReadoutReceipt,
} from './contracts/cadp-external-readout-foundation.contract';
export {
  CADP_EXTERNAL_READOUT_FOUNDATION_CONTRACT_VERSION,
  CADP_EXTERNAL_READOUT_REDACTED_FIELD_NAMES,
  validateCadpExternalCallerIdentityInput,
  validateCadpExternalReadoutIngress,
  redactCadpExternalReadoutPayload,
  validateCadpExternalReadoutAllowlistedMetadata,
  evaluateCadpExternalReadoutFreshness,
  createDeterministicCadpExternalReadoutReceipt,
} from './contracts/cadp-external-readout-foundation.contract';

// CADP T5-R2 transport-neutral external-readout adapter (pure, contract-only;
// no MCP/CLI/HTTP registration, no authentication implementation, no external
// invocation authority).
export type {
  CadpExternalReadoutAdapterStage,
  CadpExternalReadoutAdapterIssueCode,
  CadpExternalReadoutAdapterIssue,
  CadpExternalReadoutAdapterRequest,
  CadpExternalReadoutAdapterRejectedPayload,
  CadpExternalReadoutAdapterResponse,
} from './contracts/cadp-external-readout-adapter.contract';
export {
  CADP_EXTERNAL_READOUT_ADAPTER_CONTRACT_VERSION,
  evaluateCadpExternalReadoutAdapter,
} from './contracts/cadp-external-readout-adapter.contract';

// RSPB-AI-T10 environment-snapshot evidence validation (pure, in-memory,
// evidence-only; no observation, persistence, refresh, or action authority).
export type {
  CapabilityDependencyKind,
  CapabilityDependencyAvailability,
  CapabilityDependencyVerificationLevel,
  CapabilityNetworkMode,
  CapabilitySandboxStatus,
  CapabilityCredentialBindingStatus,
  CapabilitySnapshotVerificationStatus,
  CapabilityEnvironmentSnapshotPackage,
  CapabilityEnvironmentSnapshotDependency,
  CapabilityEnvironmentSnapshot,
  CapabilityEnvironmentSnapshotReadinessPolicyEvidence,
  CapabilityEnvironmentSnapshotEvidenceInput,
  CapabilityEnvironmentSnapshotEvidenceIssueCode,
  CapabilityEnvironmentSnapshotEvidenceIssue,
  CapabilityEnvironmentSnapshotEvidenceStatus,
  CapabilityEnvironmentSnapshotEvidenceResult,
} from './contracts/capability-environment-snapshot-evidence.contract';
export {
  CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_CONTRACT_VERSION,
  CAPABILITY_ENVIRONMENT_SNAPSHOT_VERSION,
  CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION,
  evaluateCapabilityEnvironmentSnapshotEvidence,
} from './contracts/capability-environment-snapshot-evidence.contract';

// RSPB-AI-T11 capability workspace profile / bootstrap policy bundle
// validation kernel (pure, in-memory; no loading, materialization,
// persistence, install, acquisition, network, execution, or action authority).
export type {
  CapabilityWorkspaceBootstrapProfile,
  CapabilityWorkspaceBootstrapPolicy,
  CapabilityWorkspaceBootstrapPolicyBundleInput,
  CapabilityWorkspaceBootstrapPolicyBundleIssueCode,
  CapabilityWorkspaceBootstrapPolicyBundleIssue,
  CapabilityWorkspaceBootstrapPolicyBundleResult,
} from './contracts/capability-workspace-bootstrap-policy-bundle.contract';
export {
  CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION,
  CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_RESULT_VERSION,
  evaluateCapabilityWorkspaceBootstrapPolicyBundle,
} from './contracts/capability-workspace-bootstrap-policy-bundle.contract';

// RSPB-AI-T12 capability bootstrap closure evidence bundle validation kernel
// (pure, in-memory composition of the current T9/T10/T11 evaluators only; no
// loading, rollback, execution, mutation, provider/live, public, or
// deployment authority).
export type {
  CapabilityBootstrapClosureEvidenceBundleInput,
  CapabilityBootstrapClosureEvidenceBundleIssueCode,
  CapabilityBootstrapClosureEvidenceBundleIssue,
  CapabilityBootstrapClosureEvidenceBundleStatus,
  CapabilityBootstrapClosureEvidenceBundleResult,
} from './contracts/capability-bootstrap-closure-evidence-bundle.contract';
export {
  CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_CONTRACT_VERSION,
  CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_RESULT_VERSION,
  evaluateCapabilityBootstrapClosureEvidenceBundle,
} from './contracts/capability-bootstrap-closure-evidence-bundle.contract';

// RSPB-AI-T13 ASSF package metadata to capability-preflight candidate binding
// kernel (pure, in-memory; no registry/index read, package activation,
// loading, instruction-body read, execution, mutation, external adapter,
// provider/live, public, or deployment authority). authorityStatus is the
// literal CANDIDATE_ONLY on every path.
export type {
  AssfPackageLifecycleStatus,
  AssfPackageRiskLevel,
  AssfCliMcpDisposition,
  AssfCandidateApprovalState,
  AssfCandidateUatState,
  AssfCandidateCertificationState,
  AssfPackageMetadata,
  AssfCapabilityPreflightCandidateBindingInput,
  AssfCapabilityPreflightCandidateBindingIssueCode,
  AssfCapabilityPreflightCandidateBindingIssue,
  AssfCapabilityPreflightCandidateBindingStatus,
  AssfCapabilityPreflightCandidateBindingResult,
} from './contracts/assf-capability-preflight-candidate-binding.contract';
export {
  ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_CONTRACT_VERSION,
  ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_RESULT_VERSION,
  evaluateAssfCapabilityPreflightCandidateBinding,
} from './contracts/assf-capability-preflight-candidate-binding.contract';

// Phase E receipt binding contract
export type {
  ReceiptBindingDisposition,
  StepReceiptEmissionSource,
  StepReceiptObligation,
  StepReceiptEmission,
  StepReceiptBindingResult,
} from './contracts/receipt-binding.contract';

export {
  RECEIPT_BINDING_CONTRACT_VERSION,
  FULL_ROLE_ACTION_MATRIX_DEFERRED_REASON,
  buildSelectedFlowReceiptObligations,
  emitStepReceipt,
  bindStepReceipts,
} from './contracts/receipt-binding.contract';

// Factory
import type { GuardRuntimeConfig } from './types';
import { GuardRuntimeEngine } from './engine';
import { PhaseGateGuard } from './guards/phase-gate.guard';
import { RiskGateGuard } from './guards/risk-gate.guard';
import { AuthorityGateGuard } from './guards/authority-gate.guard';
import { AiCommitGuard } from './guards/ai-commit.guard';
import { MutationBudgetGuard } from './guards/mutation-budget.guard';
import { FileScopeGuard } from './guards/file-scope.guard';
import { ScopeGuard } from './guards/scope.guard';
import { AuditTrailGuard } from './guards/audit-trail.guard';

/**
 * Creates a GuardRuntimeEngine pre-loaded with the hardened default guard stack.
 * Ready to use — just call engine.evaluate(context).
 *
 * This factory is the RECOMMENDED way to create an engine.
 * Both Web UI and MCP Server should use this.
 */
export function createGuardEngine(
  config?: Partial<GuardRuntimeConfig>,
): GuardRuntimeEngine {
  const engine = new GuardRuntimeEngine(config);
  engine.registerGuard(new AiCommitGuard());
  engine.registerGuard(new PhaseGateGuard());
  engine.registerGuard(new RiskGateGuard());
  engine.registerGuard(new AuthorityGateGuard());
  engine.registerGuard(new MutationBudgetGuard());
  engine.registerGuard(new FileScopeGuard());
  engine.registerGuard(new ScopeGuard());
  engine.registerGuard(new AuditTrailGuard());
  return engine;
}
