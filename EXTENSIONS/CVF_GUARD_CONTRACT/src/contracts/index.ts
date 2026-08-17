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
  RolePermissionOutputClass,
  RolePermissionDenyRuleId,
  ReceiptOwnerAxis,
  ReceiptOwnerBoundary,
  RolePermissionProfile,
} from './role-permission.contract';

export {
  ROLE_PERMISSION_SCHEMA_VERSION,
  ROLE_PERMISSION_OUTPUT_CLASSES,
  ROLE_PERMISSION_DENY_RULES,
  ROLE_PERMISSION_PROFILES,
  getRolePermissionProfile,
  isOutputAllowedForRole,
  roleHasDenyRule,
  rolePermissionCoversAllRoles,
} from './role-permission.contract';

export type {
  OrchestratorAuthorityRole,
  WorkerLaneRole,
  OrchestratorDelegationCondition,
  OrchestratorOverreachDenyRule,
  OrchestratorDelegationProfile,
  WorkerMemoryWriteBoundary,
  WorkerLaneTicket,
} from './orchestrator.contract';

export {
  ORCHESTRATOR_CONTRACT_VERSION,
  ORCHESTRATOR_AUTHORITY_ROLES,
  WORKER_LANE_ROLES,
  ORCHESTRATOR_OVERREACH_DENY_RULES,
  ORCHESTRATOR_DELEGATION_PROFILES,
  isOrchestratorAuthorityRole,
  isWorkerLaneRole,
  orchestratorCoversAllRoles,
  canIssueWorkerLaneTicket,
  createWorkerLaneTicket,
} from './orchestrator.contract';

export type {
  MemoryContinuityTier,
  MemoryTierOwnerRole,
  MemoryPrivacyFilterId,
  WorkerRestrictedMemoryTier,
  MemoryTierOwnerPolicy,
  MemoryReinjectionPolicy,
  WorkerMemoryWriteRestrictionPolicy,
  WorkerMemoryWriteRequest,
  WorkerMemoryWriteDecision,
} from './memory-continuity.contract';

export {
  MEMORY_CONTINUITY_CONTRACT_VERSION,
  MEMORY_CONTINUITY_TIERS,
  MEMORY_TIER_OWNER_POLICIES,
  MEMORY_REINJECTION_POLICIES,
  WORKER_MEMORY_WRITE_RESTRICTIONS,
  memoryContinuityCoversAllTiers,
  isWorkerRestrictedMemoryTier,
  evaluateWorkerMemoryWrite,
} from './memory-continuity.contract';

export type {
  RuntimeWorkflowState,
  RuntimeFailureState,
  GuardEnforcementPoint,
  ToolActionClass,
  WorkflowTrigger,
  OperationalBenchmarkMetricKind,
  GuardEnforcementPointMeta,
  WorkflowTransition,
  OperationalBenchmarkExtension,
  RuntimeWorkflowEvent,
  RuntimeWorkflowDecision,
} from './runtime-workflow.contract';

export {
  RUNTIME_WORKFLOW_CONTRACT_VERSION,
  RUNTIME_FAILURE_STATES,
  GUARD_ENFORCEMENT_POINTS,
  TOOL_ACTION_CLASSES,
  WORKFLOW_TRANSITIONS,
  OPERATIONAL_BENCHMARK_EXTENSIONS,
  runtimeWorkflowCoversFailureStates,
  runtimeWorkflowCoversGuardPoints,
  toolActionClassCovers,
  evaluateRuntimeWorkflowEvent,
} from './runtime-workflow.contract';

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
  ReceiptEnvelopeInput,
  ReceiptEnvelopeReceiptRecord,
  ReceiptEnvelopeAdapterMeta,
} from './receipt-envelope.contract';

export {
  createReceiptEnvelopeReceiptRecord,
  createReceiptEnvelope,
  RECEIPT_SCHEMA_VERSION_1R,
} from './receipt-envelope.contract';

export { RECEIPT_ENVELOPE_ADAPTER_MAP } from './receipt-envelope-adapter-map';

export type {
  MemoryTierId,
  MemoryTierSpec,
  MemoryTierAdapterMeta,
} from './memory-tier.contract';

export {
  MEMORY_TIER_SPECS,
  DEFERRED_MEMORY_TIERS,
  isCanonicalTier,
  isTierImmutable,
} from './memory-tier.contract';

export { MEMORY_TIER_ADAPTER_MAP } from './memory-tier-adapter-map';

export type {
  PROVISIONAL,
  GovernedCapability,
  OutcomeWorkflow,
  OutcomeWorkflowStep,
  OutcomeDeliverable,
} from './governed-capability.contract';

export {
  OUTCOME_DELIVERABLE_CHAIN_DOC,
} from './governed-capability.contract';

export type {
  Phase2BWireupStatus,
  Phase2BWireupActor,
  Phase2BWireupClock,
  Phase2BWireupInput,
  Phase2BWireupResult,
} from './phase2b-wireup.contract';

export {
  PHASE_2B_WIREUP_VERSION,
  runPhase2BWireupFixture,
} from './phase2b-wireup.contract';

export type {
  Phase2BPrimaryRowId,
  Phase2BAdapterFamily,
  Phase2BRuntimeEvidenceMode,
  Phase2BAdapterNode,
  Phase2BAdapterEdge,
  Phase2BRuntimeCoherenceGraphInput,
  Phase2BRuntimeCoherenceGraph,
  Phase2BRuntimeCoherenceValidation,
} from './phase2b-runtime-coherence.contract';

export {
  PHASE_2B_RUNTIME_COHERENCE_SCHEMA_VERSION,
  PHASE_2B_PRIMARY_ROW_IDS,
  buildPhase2BRuntimeCoherenceGraph,
  validatePhase2BRuntimeCoherenceGraph,
  buildPhase2BAdapterInventoryChecksum,
} from './phase2b-runtime-coherence.contract';

export type {
  MetricEmissionStatus,
  OperationalMetricSchema,
} from './operational-metrics.schema';

export {
  OPERATIONAL_METRICS_SCHEMA,
  getMetricById,
  getMetricsByEmissionStatus,
  getMetricsByEmissionPhase,
} from './operational-metrics.schema';

export type {
  CadpIssueCode,
  CadpIssue,
  CadpValidationResult,
  CapabilityAdmissionDecision,
  CapabilityMutationType,
  CapabilityAdmissionAction,
  CapabilityAdmissionRecord,
  CapabilityAssignmentRecord,
  CapabilityDistributionItem,
  CapabilityDistributionManifest,
  CompatibilityEvidenceLevel,
  CompatibilityArtifactType,
  CompatibilityEvidenceRecord,
  DeterministicCadpReceiptInput,
  DeterministicCadpReceipt,
} from './capability-admission-distribution-profile.contract';

export {
  CADP_CONTRACT_VERSION,
  validateCapabilityAdmission,
  validateCapabilityAssignment,
  validateCapabilityDistribution,
  validateCompatibilityEvidence,
  createDeterministicCadpReceipt,
} from './capability-admission-distribution-profile.contract';

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
} from './cadp-external-readout-foundation.contract';

export {
  CADP_EXTERNAL_READOUT_FOUNDATION_CONTRACT_VERSION,
  CADP_EXTERNAL_READOUT_REDACTED_FIELD_NAMES,
  validateCadpExternalCallerIdentityInput,
  validateCadpExternalReadoutIngress,
  redactCadpExternalReadoutPayload,
  validateCadpExternalReadoutAllowlistedMetadata,
  evaluateCadpExternalReadoutFreshness,
  createDeterministicCadpExternalReadoutReceipt,
} from './cadp-external-readout-foundation.contract';

export type {
  CadpExternalReadoutAdapterStage,
  CadpExternalReadoutAdapterIssueCode,
  CadpExternalReadoutAdapterIssue,
  CadpExternalReadoutAdapterRequest,
  CadpExternalReadoutAdapterRejectedPayload,
  CadpExternalReadoutAdapterResponse,
} from './cadp-external-readout-adapter.contract';

export {
  CADP_EXTERNAL_READOUT_ADAPTER_CONTRACT_VERSION,
  evaluateCadpExternalReadoutAdapter,
} from './cadp-external-readout-adapter.contract';

export type {
  CapabilityOwnerBindingIssueCode,
  CapabilityOwnerBindingIssue,
  CapabilityOwnerBindingResult,
  CapabilityOwnerBindData,
  BoundArtifactType,
  CapabilityOwnerHandle,
  BoundArtifactProjection,
  CapabilityOwnerGrantProjection,
  CapabilityExecutionObservationInput,
} from './capability-owner-binding.contract';

export {
  CAPABILITY_OWNER_BINDING_CONTRACT_VERSION,
  bindCommittedCapabilityOwnerGrant,
  isBoundCapabilityOwner,
  readBoundArtifact,
  readBoundGrantIdentity,
  reconcileGrantWithObservation,
} from './capability-owner-binding.contract';

export type {
  AcquisitionOperationPhase,
  AcquisitionAction,
  AcquisitionMutationKind,
  ControlledAcquisitionOperation,
  ControlledAcquisitionMutation,
  ControlledAcquisitionPlan,
  ControlledAcquisitionApproval,
  ControlledAcquisitionIssueCode,
  ControlledAcquisitionIssue,
  ControlledAcquisitionAuthorizationResult,
  ControlledAcquisitionOperationResult,
  ControlledAcquisitionReceipt,
  ControlledAcquisitionReceiptResult,
  ControlledAcquisitionRepairInput,
  ControlledAcquisitionRepairDecision,
} from './controlled-acquisition.contract';

export type {
  CapabilityRiskLevel,
  CapabilityRouteStage,
  CapabilityReadinessState,
  CapabilityRouteCandidate,
  CapabilityCandidateSet,
  CapabilityRouteIssue,
  CapabilityRouteDecision,
  CapabilityRouteEvaluationOptions,
  CapabilityReadinessInput,
  CapabilityReadinessDecision,
} from './capability-route-readiness.contract';

export {
  CAPABILITY_ROUTE_READINESS_CONTRACT_VERSION,
  CAPABILITY_ROUTE_DECISION_VERSION,
  CAPABILITY_READINESS_DECISION_VERSION,
  evaluateCapabilityRoute,
  evaluateCapabilityReadiness,
} from './capability-route-readiness.contract';

export {
  CONTROLLED_ACQUISITION_CONTRACT_VERSION,
  CONTROLLED_ACQUISITION_PLAN_VERSION,
  CONTROLLED_ACQUISITION_APPROVAL_VERSION,
  CONTROLLED_ACQUISITION_RECEIPT_VERSION,
  computeControlledAcquisitionPlanDigest,
  evaluateControlledAcquisitionAuthorization,
  reconcileControlledAcquisitionReceipt,
  evaluateControlledAcquisitionRepair,
} from './controlled-acquisition.contract';

export type {
  CapabilityPreflightRiskLevel,
  CapabilityPreflightNetworkMode,
  CapabilityPreflightPrivilegePolicy,
  CapabilityPreflightProfile,
  CapabilityPreflightProfilePolicyInput,
  CapabilityPreflightProfilePolicyIssueCode,
  CapabilityPreflightProfilePolicyIssue,
  CapabilityPreflightProfilePolicyResult,
} from './capability-preflight-profile-policy.contract';

export {
  CAPABILITY_PREFLIGHT_PROFILE_POLICY_CONTRACT_VERSION,
  CAPABILITY_PREFLIGHT_PROFILE_POLICY_RESULT_VERSION,
  evaluateCapabilityPreflightProfilePolicy,
} from './capability-preflight-profile-policy.contract';

export type {
  CapabilityBootstrapApprovalEnvelopeClass,
  CapabilityBootstrapMutationEnvelopeEntry,
  CapabilityBootstrapApprovalEvidence,
  CapabilityBootstrapApprovalEvidenceBindingInput,
  CapabilityBootstrapApprovalEvidenceIssueCode,
  CapabilityBootstrapApprovalEvidenceIssue,
  CapabilityBootstrapApprovalEvidenceBindingResult,
} from './capability-bootstrap-approval-evidence.contract';

export {
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_CONTRACT_VERSION,
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION,
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION,
  evaluateCapabilityBootstrapApprovalEvidenceBinding,
} from './capability-bootstrap-approval-evidence.contract';

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
} from './capability-acquisition-receipt-verification.contract';

export {
  CAPABILITY_ACQUISITION_RECEIPT_VERIFICATION_CONTRACT_VERSION,
  CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION,
  CAPABILITY_ACQUISITION_RECEIPT_VERIFICATION_RESULT_VERSION,
  evaluateCapabilityAcquisitionReceiptVerification,
} from './capability-acquisition-receipt-verification.contract';

export type {
  ProjectionStalenessState,
  FindingVerificationState,
  FindingSeverity,
  PathStepKind,
  CapabilityCaseProjectionInput,
  CanonicalEvidenceInput,
  DomainFindingInput,
  DomainPathStepInput,
  DomainPathInput,
  DomainEvidenceProjectionInput,
  CaseEvidenceProjectionIssueCode,
  CaseEvidenceProjectionIssue,
  ProjectedFinding,
  ProjectedPathStep,
  ProjectedPath,
  ProjectedEvidence,
  CapabilityCaseEvidenceProjection,
} from './capability-case-evidence-projection.contract';

export {
  CAPABILITY_CASE_EVIDENCE_PROJECTION_CONTRACT_VERSION,
  CAPABILITY_CASE_PROJECTION_VERSION,
  DOMAIN_EVIDENCE_PROJECTION_VERSION,
  projectCapabilityCaseEvidence,
} from './capability-case-evidence-projection.contract';

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
} from './capability-environment-snapshot-evidence.contract';

export {
  CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_CONTRACT_VERSION,
  CAPABILITY_ENVIRONMENT_SNAPSHOT_VERSION,
  CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION,
  evaluateCapabilityEnvironmentSnapshotEvidence,
} from './capability-environment-snapshot-evidence.contract';

export type {
  CapabilityWorkspaceBootstrapProfile,
  CapabilityWorkspaceBootstrapPolicy,
  CapabilityWorkspaceBootstrapPolicyBundleInput,
  CapabilityWorkspaceBootstrapPolicyBundleIssueCode,
  CapabilityWorkspaceBootstrapPolicyBundleIssue,
  CapabilityWorkspaceBootstrapPolicyBundleResult,
} from './capability-workspace-bootstrap-policy-bundle.contract';

export {
  CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION,
  CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_RESULT_VERSION,
  evaluateCapabilityWorkspaceBootstrapPolicyBundle,
} from './capability-workspace-bootstrap-policy-bundle.contract';
