import type {
  CapabilityReadinessDecision,
  CapabilityReadinessState,
  CapabilityRouteDecision,
  CapabilityRouteStage,
} from './capability-route-readiness.contract';
import type { CapabilityBootstrapApprovalEvidenceBindingResult } from './capability-bootstrap-approval-evidence.contract';
import type {
  CapabilityEnvironmentSnapshotEvidenceResult,
  CapabilityEnvironmentSnapshotEvidenceStatus,
} from './capability-environment-snapshot-evidence.contract';
import type {
  CapabilityCaseEvidenceProjection,
  FindingVerificationState,
  PathStepKind,
  ProjectionStalenessState,
} from './capability-case-evidence-projection.contract';

export const CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_CONTRACT_VERSION =
  'cvf.capabilityPreflightAdvisoryProjection.v1' as const;
export const CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_RESULT_VERSION =
  'cvf.capabilityPreflightAdvisoryProjectionResult.v1' as const;

export interface CapabilityPreflightAdvisoryProjectionInput {
  readonly schemaVersion: typeof CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_CONTRACT_VERSION;
  readonly route: CapabilityRouteDecision;
  readonly readiness: CapabilityReadinessDecision;
  readonly environment: CapabilityEnvironmentSnapshotEvidenceResult;
  readonly approval: CapabilityBootstrapApprovalEvidenceBindingResult | null;
  readonly caseEvidence: CapabilityCaseEvidenceProjection | null;
  readonly now: string;
}

export type CapabilityPreflightAdvisoryProjectionIssueCode =
  | 'MALFORMED_INPUT' | 'UNKNOWN_KEY' | 'INVALID_FIELD' | 'UNSAFE_STRING'
  | 'RAW_SECRET_DETECTED' | 'UNBOUNDED_COLLECTION' | 'SPARSE_ARRAY' | 'DUPLICATE_VALUE'
  | 'ROUTE_READINESS_BINDING_MISMATCH' | 'READINESS_ENVIRONMENT_BINDING_MISMATCH'
  | 'ENVIRONMENT_EVIDENCE_REJECTED' | 'APPROVAL_BINDING_CONTRADICTION'
  | 'CASE_EVIDENCE_BINDING_CONTRADICTION' | 'STALE_EVIDENCE_TIME';

export interface CapabilityPreflightAdvisoryProjectionIssue {
  readonly code: CapabilityPreflightAdvisoryProjectionIssueCode;
  readonly path: string;
  readonly message: string;
}

export type CapabilityPreflightAdvisoryProjectionStatus =
  | 'ADVISORY_PROJECTION_READY' | 'ADVISORY_PROJECTION_REJECTED' | 'ADVISORY_PROJECTION_BLOCKED';

export interface CapabilityAdvisoryRouteView {
  readonly routeDecisionId: string;
  readonly stage: CapabilityRouteStage;
  readonly primary: Readonly<{ capabilityId: string; packageId: string; packageVersion: string }> | null;
  readonly supporting: readonly string[];
  readonly rejected: readonly Readonly<{ capabilityId: string; reasonCodes: readonly string[] }>[];
  readonly confidence: number;
  readonly ambiguityReasons: readonly string[];
}

export interface CapabilityAdvisoryReadinessView {
  readonly readinessDecisionId: string;
  readonly snapshotId: string;
  readonly state: CapabilityReadinessState;
  readonly missingDependencies: readonly string[];
  readonly blockingReasons: readonly string[];
  readonly evidenceRefs: readonly string[];
  readonly environmentStatus: CapabilityEnvironmentSnapshotEvidenceStatus;
  readonly requiredDependencies: readonly string[];
  readonly availableDependencies: readonly string[];
  readonly environmentBlockingReasons: readonly string[];
}

export type CapabilityAdvisoryApprovalPresence = 'PRESENT_VALIDATED' | 'PRESENT_REJECTED' | 'ABSENT';

export interface CapabilityAdvisoryApprovalBoundaryView {
  readonly presence: CapabilityAdvisoryApprovalPresence;
  readonly planId: string | null;
  readonly planDigest: string | null;
  readonly approvalId: string | null;
}

export interface CapabilityAdvisoryFindingView {
  readonly findingId: string;
  readonly claim: string;
  readonly verificationState: FindingVerificationState;
  readonly evidenceRefs: readonly string[];
}

export interface CapabilityAdvisoryPathStepView {
  readonly kind: PathStepKind;
  readonly description: string;
  readonly evidenceRef: string | null;
}

export interface CapabilityAdvisoryPathView {
  readonly pathId: string;
  readonly steps: readonly CapabilityAdvisoryPathStepView[];
}

export type CapabilityAdvisoryEvidencePresence = 'PRESENT' | 'ABSENT';

export interface CapabilityAdvisoryEvidenceView {
  readonly presence: CapabilityAdvisoryEvidencePresence;
  readonly staleness: ProjectionStalenessState | null;
  readonly findings: readonly CapabilityAdvisoryFindingView[];
  readonly paths: readonly CapabilityAdvisoryPathView[];
}

export interface CapabilityPreflightAdvisoryProjectionResult {
  readonly schemaVersion: typeof CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_RESULT_VERSION;
  readonly status: CapabilityPreflightAdvisoryProjectionStatus;
  readonly route: CapabilityAdvisoryRouteView | null;
  readonly readiness: CapabilityAdvisoryReadinessView | null;
  readonly approvalBoundary: CapabilityAdvisoryApprovalBoundaryView | null;
  readonly evidence: CapabilityAdvisoryEvidenceView | null;
  readonly nextSafeAction: string;
  readonly blocked: boolean;
  readonly issues: readonly CapabilityPreflightAdvisoryProjectionIssue[];
  readonly evaluatedAt: string;
  readonly approvalAuthorityGranted: false;
  readonly taskAuthorityGranted: false;
  readonly activationAuthorityGranted: false;
  readonly executionAuthorityGranted: false;
  readonly mutationAuthorityGranted: false;
  readonly actionInvocationAuthorized: false;
}
