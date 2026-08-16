/**
 * Capability case and domain-evidence projection kernel.
 *
 * Pure projection only. Combines canonical route/readiness and optional
 * controlled-acquisition evidence into deterministic, traceable, secret-safe
 * data. A projection is never authority: it cannot mutate, approve, or
 * strengthen the source artifacts it describes.
 */

import { createHash } from 'node:crypto';
import { isProxy } from 'node:util/types';
import {
  CAPABILITY_READINESS_DECISION_VERSION,
  CAPABILITY_ROUTE_DECISION_VERSION,
  type CapabilityRouteDecision,
  type CapabilityReadinessDecision,
} from './capability-route-readiness.contract';
import {
  CONTROLLED_ACQUISITION_CONTRACT_VERSION,
  type ControlledAcquisitionAuthorizationResult,
  type ControlledAcquisitionReceiptResult,
} from './controlled-acquisition.contract';

export const CAPABILITY_CASE_EVIDENCE_PROJECTION_CONTRACT_VERSION = 'cvf.capabilityCaseEvidenceProjection.v1' as const;
export const CAPABILITY_CASE_PROJECTION_VERSION = 'cvf.capabilityCaseProjection.v1' as const;
export const DOMAIN_EVIDENCE_PROJECTION_VERSION = 'cvf.domainEvidenceProjection.v1' as const;

export type ProjectionStalenessState = 'CURRENT' | 'STALE' | 'INVALID';
export type FindingVerificationState = 'VERIFIED' | 'UNVERIFIED' | 'INCOMPLETE' | 'BLOCKED';
export type FindingSeverity = 'INFO' | 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
export type PathStepKind = 'DEMONSTRATED' | 'INFERRED';

export interface CapabilityCaseProjectionInput {
  readonly caseId: string;
  readonly requestId: string;
  readonly workspaceId: string;
  readonly workOrderId?: string | null;
  readonly route: CapabilityRouteDecision;
  readonly readiness: CapabilityReadinessDecision;
  readonly acquisitionAuthorization?: ControlledAcquisitionAuthorizationResult | null;
  readonly acquisitionAuthorizationRef?: string | null;
  readonly acquisitionReceipt?: ControlledAcquisitionReceiptResult | null;
  readonly acquisitionReceiptRef?: string | null;
  readonly sourceObservedAt: string;
  readonly sourceExpiresAt: string;
}

export interface CanonicalEvidenceInput {
  readonly evidenceId: string;
  readonly sourceRef: string;
  readonly observation: string;
  readonly observedAt: string;
  readonly digest?: string | null;
  readonly reproductionBoundary?: string | null;
}

export interface DomainFindingInput {
  readonly findingId: string;
  readonly claim: string;
  readonly severity: FindingSeverity;
  readonly confidence: number;
  readonly evidenceRefs: readonly string[];
  readonly remediation?: string | null;
}

export interface DomainPathStepInput {
  readonly kind: PathStepKind;
  readonly description: string;
  readonly evidenceRef?: string | null;
}

export interface DomainPathInput {
  readonly pathId: string;
  readonly steps: readonly DomainPathStepInput[];
}

export interface DomainEvidenceProjectionInput {
  readonly projectionId: string;
  readonly evidence: readonly CanonicalEvidenceInput[];
  readonly findings: readonly DomainFindingInput[];
  readonly paths: readonly DomainPathInput[];
}

export type CaseEvidenceProjectionIssueCode =
  | 'MALFORMED_INPUT' | 'INVALID_FIELD' | 'STALE_SOURCE' | 'UNVERIFIED_FINDING_REFERENCE'
  | 'DUPLICATE_EVIDENCE_ID' | 'DUPLICATE_FINDING_ID' | 'DUPLICATE_PATH_ID'
  | 'SECRET_LIKE_VALUE_REJECTED';

export interface CaseEvidenceProjectionIssue {
  readonly code: CaseEvidenceProjectionIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface ProjectedFinding {
  readonly findingId: string;
  readonly claim: string;
  readonly severity: FindingSeverity;
  readonly confidence: number;
  readonly verificationState: FindingVerificationState;
  readonly evidenceRefs: readonly string[];
  readonly remediation: string | null;
}

export interface ProjectedPathStep {
  readonly kind: PathStepKind;
  readonly description: string;
  readonly evidenceRef: string | null;
}

export interface ProjectedPath {
  readonly pathId: string;
  readonly steps: readonly ProjectedPathStep[];
}

export interface ProjectedEvidence {
  readonly evidenceId: string;
  readonly sourceRef: string;
  readonly observation: string;
  readonly observedAt: string;
  readonly digest: string | null;
  readonly reproductionBoundary: string | null;
}

export interface CapabilityCaseEvidenceProjection {
  readonly schemaVersion: typeof CAPABILITY_CASE_EVIDENCE_PROJECTION_CONTRACT_VERSION;
  readonly caseProjectionVersion: typeof CAPABILITY_CASE_PROJECTION_VERSION;
  readonly domainEvidenceProjectionVersion: typeof DOMAIN_EVIDENCE_PROJECTION_VERSION;
  readonly authorityNotice: 'PROJECTION_ONLY';
  readonly authorityMutation: false;
  readonly caseId: string;
  readonly requestId: string;
  readonly workspaceId: string;
  readonly workOrderId: string | null;
  readonly projectionId: string;
  readonly sourceRefs: readonly string[];
  readonly staleness: ProjectionStalenessState;
  readonly currentDisposition: string;
  readonly evidence: readonly ProjectedEvidence[];
  readonly findings: readonly ProjectedFinding[];
  readonly paths: readonly ProjectedPath[];
  readonly projectionDigest: string;
  readonly generatedAt: string;
  readonly issues: readonly CaseEvidenceProjectionIssue[];
}

const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const SECRET_SIGNAL = /(\bsk-[A-Za-z0-9_-]{8,}\b|\bbearer\s+[A-Za-z0-9._~+\/-]{4,}|(?:api[_-]?key|password|passwd|token|secret|credential|cookie|session[_-]?id)\s*[=:]\s*\S+|-----BEGIN [A-Z ]*PRIVATE KEY-----)/i;
const SEVERITIES: readonly FindingSeverity[] = ['INFO', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL'];
const STEP_KINDS: readonly PathStepKind[] = ['DEMONSTRATED', 'INFERRED'];
const ROUTE_STAGES = ['FAST_ROUTE', 'FULL_RESOLUTION_REQUIRED', 'AMBIGUOUS_ROUTE', 'NO_CANDIDATE'] as const;
const READINESS_STATES = [
  'READY', 'READY_WITH_EXISTING_APPROVAL', 'BOOTSTRAP_REQUIRED', 'APPROVAL_REQUIRED',
  'BLOCKED_POLICY', 'BLOCKED_PROVENANCE', 'BLOCKED_INTEGRITY', 'BLOCKED_COMPATIBILITY',
  'BLOCKED_CREDENTIAL', 'BLOCKED_NETWORK', 'BLOCKED_SANDBOX', 'STALE_SNAPSHOT',
  'AMBIGUOUS_ROUTE', 'UNKNOWN',
] as const;
const MAX_COLLECTION_ITEMS = 256;

function issue(code: CaseEvidenceProjectionIssueCode, path: string, message: string): CaseEvidenceProjectionIssue {
  return Object.freeze({ code, path, message });
}

function isPlainRecord(value: unknown): value is Record<string, unknown> {
  if (value === null || typeof value !== 'object' || isProxy(value)) return false;
  const prototype = Object.getPrototypeOf(value);
  if (prototype !== Object.prototype && prototype !== null) return false;
  if (Object.getOwnPropertySymbols(value).length) return false;
  return Object.values(Object.getOwnPropertyDescriptors(value)).every(
    (descriptor) => 'value' in descriptor && descriptor.get === undefined && descriptor.set === undefined,
  );
}

function isPlainArray(value: unknown): value is readonly unknown[] {
  if (!Array.isArray(value) || isProxy(value) || Object.getOwnPropertySymbols(value).length) return false;
  return Object.values(Object.getOwnPropertyDescriptors(value)).every(
    (descriptor) => 'value' in descriptor && descriptor.get === undefined && descriptor.set === undefined,
  );
}

function isBoundedPlainArray(value: unknown): value is readonly unknown[] {
  if (!isPlainArray(value) || value.length > MAX_COLLECTION_ITEMS) return false;
  for (let index = 0; index < value.length; index += 1) {
    if (!Object.prototype.hasOwnProperty.call(value, index)) return false;
  }
  return true;
}

function compareText(left: string, right: string): number {
  return left < right ? -1 : left > right ? 1 : 0;
}

function validUtc(value: unknown): value is string {
  return typeof value === 'string' && ISO_UTC.test(value) && Number.isFinite(Date.parse(value));
}

function validId(value: unknown): value is string {
  return typeof value === 'string' && SAFE_ID.test(value) && !/^sk-[A-Za-z0-9_-]{8,}$/i.test(value);
}

function isSecretLike(value: string): boolean {
  return SECRET_SIGNAL.test(value);
}

/**
 * Canonical, deterministic JSON: object keys sorted by code point, arrays
 * kept in their given (already-normalized) order. Used only for the
 * projection digest, never for filesystem or network serialization.
 */
function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  if (isPlainRecord(value)) {
    return `{${Object.keys(value).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key])}`).join(',')}}`;
  }
  return JSON.stringify(value) ?? 'null';
}

function computeProjectionDigest(value: Omit<CapabilityCaseEvidenceProjection, 'projectionDigest'>): string {
  return createHash('sha256').update(canonicalJson(value)).digest('hex');
}

function safeString(value: unknown): value is string {
  return typeof value === 'string' && value.length > 0 && value.length <= 4096 && !isSecretLike(value);
}

function normalizeNullableSafeString(value: unknown, path: string, issues: CaseEvidenceProjectionIssue[]): string | null {
  if (value === null || value === undefined) return null;
  if (typeof value !== 'string') {
    issues.push(issue('INVALID_FIELD', path, 'Expected a string or null.'));
    return null;
  }
  if (isSecretLike(value)) {
    issues.push(issue('SECRET_LIKE_VALUE_REJECTED', path, 'Value resembles a secret and was rejected.'));
    return null;
  }
  if (value.length > 4096) {
    issues.push(issue('INVALID_FIELD', path, 'Value exceeds the bounded length.'));
    return null;
  }
  return value;
}

function validateEvidence(input: unknown, index: number, issues: CaseEvidenceProjectionIssue[]): ProjectedEvidence | null {
  const path = `$.evidence[${index}]`;
  if (!isPlainRecord(input)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Evidence entry must be a plain non-Proxy object.'));
    return null;
  }
  if (!validId(input.evidenceId) || !validId(input.sourceRef)) {
    issues.push(issue('INVALID_FIELD', `${path}`, 'evidenceId and sourceRef must be bounded safe identifiers.'));
    return null;
  }
  if (!safeString(input.observation)) {
    issues.push(issue(isSecretLike(String(input.observation ?? '')) ? 'SECRET_LIKE_VALUE_REJECTED' : 'INVALID_FIELD', `${path}.observation`, 'Observation must be a bounded, non-secret string.'));
    return null;
  }
  if (!validUtc(input.observedAt)) {
    issues.push(issue('INVALID_FIELD', `${path}.observedAt`, 'observedAt must be ISO-8601 UTC.'));
    return null;
  }
  return Object.freeze({
    evidenceId: input.evidenceId,
    sourceRef: input.sourceRef,
    observation: input.observation,
    observedAt: input.observedAt,
    digest: normalizeNullableSafeString(input.digest, `${path}.digest`, issues),
    reproductionBoundary: normalizeNullableSafeString(input.reproductionBoundary, `${path}.reproductionBoundary`, issues),
  });
}

function validateFinding(
  input: unknown,
  index: number,
  evidenceIds: ReadonlySet<string>,
  issues: CaseEvidenceProjectionIssue[],
): ProjectedFinding | null {
  const path = `$.findings[${index}]`;
  if (!isPlainRecord(input)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Finding entry must be a plain non-Proxy object.'));
    return null;
  }
  if (!validId(input.findingId)) {
    issues.push(issue('INVALID_FIELD', `${path}.findingId`, 'findingId must be a bounded safe identifier.'));
    return null;
  }
  if (!safeString(input.claim)) {
    issues.push(issue(isSecretLike(String(input.claim ?? '')) ? 'SECRET_LIKE_VALUE_REJECTED' : 'INVALID_FIELD', `${path}.claim`, 'Claim must be a bounded, non-secret string.'));
    return null;
  }
  if (typeof input.severity !== 'string' || !SEVERITIES.includes(input.severity as FindingSeverity)) {
    issues.push(issue('INVALID_FIELD', `${path}.severity`, 'Unsupported severity.'));
    return null;
  }
  if (typeof input.confidence !== 'number' || !Number.isFinite(input.confidence)) {
    issues.push(issue('INVALID_FIELD', `${path}.confidence`, 'Confidence must be a finite number.'));
    return null;
  }
  if (!isBoundedPlainArray(input.evidenceRefs) || input.evidenceRefs.some((ref) => !validId(ref))) {
    issues.push(issue('INVALID_FIELD', `${path}.evidenceRefs`, 'evidenceRefs must be an array of bounded safe identifiers.'));
    return null;
  }
  const refs = [...input.evidenceRefs as readonly string[]].sort();
  const unresolved = refs.filter((ref) => !evidenceIds.has(ref));
  if (unresolved.length) issues.push(issue('UNVERIFIED_FINDING_REFERENCE', `${path}.evidenceRefs`, 'One or more evidence references are unresolved.'));
  const verified = refs.length > 0 && unresolved.length === 0;
  return Object.freeze({
    findingId: input.findingId,
    claim: input.claim,
    severity: input.severity as FindingSeverity,
    confidence: Math.max(0, Math.min(1, input.confidence)),
    verificationState: (verified ? 'VERIFIED' : 'UNVERIFIED') as FindingVerificationState,
    evidenceRefs: Object.freeze([...refs]),
    remediation: normalizeNullableSafeString(input.remediation, `${path}.remediation`, issues),
  });
}

function validatePathStep(
  input: unknown,
  pathIndex: number,
  stepIndex: number,
  evidenceIds: ReadonlySet<string>,
  issues: CaseEvidenceProjectionIssue[],
): ProjectedPathStep | null {
  const path = `$.paths[${pathIndex}].steps[${stepIndex}]`;
  if (!isPlainRecord(input)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Path step must be a plain non-Proxy object.'));
    return null;
  }
  if (typeof input.kind !== 'string' || !STEP_KINDS.includes(input.kind as PathStepKind)) {
    issues.push(issue('INVALID_FIELD', `${path}.kind`, 'Unsupported step kind.'));
    return null;
  }
  if (!safeString(input.description)) {
    issues.push(issue(isSecretLike(String(input.description ?? '')) ? 'SECRET_LIKE_VALUE_REJECTED' : 'INVALID_FIELD', `${path}.description`, 'Description must be a bounded, non-secret string.'));
    return null;
  }
  const evidenceRef = normalizeNullableSafeString(input.evidenceRef, `${path}.evidenceRef`, issues);
  const canDemonstrate = evidenceRef !== null && evidenceIds.has(evidenceRef);
  return Object.freeze({
    kind: (input.kind === 'DEMONSTRATED' && canDemonstrate ? 'DEMONSTRATED' : 'INFERRED') as PathStepKind,
    description: input.description,
    evidenceRef,
  });
}

function validatePath(
  input: unknown,
  index: number,
  evidenceIds: ReadonlySet<string>,
  issues: CaseEvidenceProjectionIssue[],
): ProjectedPath | null {
  const path = `$.paths[${index}]`;
  if (!isPlainRecord(input)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Path entry must be a plain non-Proxy object.'));
    return null;
  }
  if (!validId(input.pathId)) {
    issues.push(issue('INVALID_FIELD', `${path}.pathId`, 'pathId must be a bounded safe identifier.'));
    return null;
  }
  if (!isBoundedPlainArray(input.steps)) {
    issues.push(issue('MALFORMED_INPUT', `${path}.steps`, 'steps must be a bounded plain array.'));
    return null;
  }
  const steps: ProjectedPathStep[] = [];
  input.steps.forEach((step, stepIndex) => {
    const validated = validatePathStep(step, index, stepIndex, evidenceIds, issues);
    if (validated) steps.push(validated);
  });
  return Object.freeze({ pathId: input.pathId, steps: Object.freeze(steps) });
}

function evaluateStaleness(
  now: string,
  sourceObservedAt: string,
  sourceExpiresAt: string,
  issues: CaseEvidenceProjectionIssue[],
): ProjectionStalenessState {
  if (!validUtc(now) || !validUtc(sourceObservedAt) || !validUtc(sourceExpiresAt)) {
    issues.push(issue('INVALID_FIELD', '$.sourceObservedAt', 'now, sourceObservedAt, and sourceExpiresAt must each be ISO-8601 UTC.'));
    return 'INVALID';
  }
  if (Date.parse(sourceObservedAt) > Date.parse(now)) {
    issues.push(issue('INVALID_FIELD', '$.sourceObservedAt', 'sourceObservedAt cannot be in the future relative to now.'));
    return 'INVALID';
  }
  if (Date.parse(now) >= Date.parse(sourceExpiresAt)) {
    issues.push(issue('STALE_SOURCE', '$.sourceExpiresAt', 'Source binding has expired relative to now.'));
    return 'STALE';
  }
  return 'CURRENT';
}

/**
 * Project a bounded case/evidence read model from canonical route,
 * readiness, and optional controlled-acquisition results. Returns an
 * immutable, secret-safe, deterministic projection. Never throws; every
 * failure mode is represented as an `issues` entry and a fail-closed field
 * value (`staleness: 'INVALID'`, unresolved findings as `UNVERIFIED`, etc).
 */
export function projectCapabilityCaseEvidence(
  caseInput: CapabilityCaseProjectionInput,
  domainInput: DomainEvidenceProjectionInput,
  now: string,
): CapabilityCaseEvidenceProjection {
  const issues: CaseEvidenceProjectionIssue[] = [];

  if (!isPlainRecord(caseInput)) {
    issues.push(issue('MALFORMED_INPUT', '$.caseInput', 'Case input must be a plain non-Proxy object.'));
  }
  if (!isPlainRecord(domainInput)) {
    issues.push(issue('MALFORMED_INPUT', '$.domainInput', 'Domain input must be a plain non-Proxy object.'));
  }

  const safeCaseInput = isPlainRecord(caseInput) ? (caseInput as unknown as CapabilityCaseProjectionInput) : undefined;
  const safeDomainInput = isPlainRecord(domainInput) ? (domainInput as unknown as DomainEvidenceProjectionInput) : undefined;

  const caseId = safeCaseInput && validId(safeCaseInput.caseId) ? safeCaseInput.caseId : 'invalid';
  const requestId = safeCaseInput && validId(safeCaseInput.requestId) ? safeCaseInput.requestId : 'invalid';
  const workspaceId = safeCaseInput && validId(safeCaseInput.workspaceId) ? safeCaseInput.workspaceId : 'invalid';
  if (!safeCaseInput || !validId(safeCaseInput.caseId) || !validId(safeCaseInput.requestId) || !validId(safeCaseInput.workspaceId)) {
    issues.push(issue('INVALID_FIELD', '$.caseInput', 'caseId, requestId, and workspaceId must be bounded safe identifiers.'));
  }
  const workOrderId = safeCaseInput ? normalizeNullableSafeString(safeCaseInput.workOrderId, '$.caseInput.workOrderId', issues) : null;

  const routeRecord = safeCaseInput && isPlainRecord(safeCaseInput.route) ? safeCaseInput.route : undefined;
  const readinessRecord = safeCaseInput && isPlainRecord(safeCaseInput.readiness) ? safeCaseInput.readiness : undefined;
  const routeDecision = routeRecord as unknown as CapabilityRouteDecision | undefined;
  const routeValid = routeDecision !== undefined
    && routeDecision.schemaVersion === CAPABILITY_ROUTE_DECISION_VERSION
    && validId(routeDecision.routeDecisionId)
    && validId(routeDecision.candidateSetId)
    && validId(routeDecision.requestId)
    && validId(routeDecision.workspaceId)
    && ROUTE_STAGES.includes(routeDecision.stage)
    && typeof routeDecision.confidence === 'number'
    && Number.isFinite(routeDecision.confidence)
    && routeDecision.confidence >= 0
    && routeDecision.confidence <= 1
    && isBoundedPlainArray(routeDecision.supporting)
    && isBoundedPlainArray(routeDecision.rejected)
    && isBoundedPlainArray(routeDecision.fallbacks)
    && isBoundedPlainArray(routeDecision.ambiguityReasons)
    && isBoundedPlainArray(routeDecision.environmentSnapshotRefs)
    && isBoundedPlainArray(routeDecision.issues)
    && validUtc(routeDecision.generatedAt)
    && routeDecision.authorityStatus === 'CANDIDATE_ONLY'
    && routeDecision.executionAuthorized === false
    && routeDecision.requestId === requestId
    && routeDecision.workspaceId === workspaceId;
  if (!routeValid) {
    issues.push(issue('INVALID_FIELD', '$.caseInput.route', 'route must preserve the canonical projection and no-execution invariants.'));
  }
  const readinessDecision = readinessRecord as unknown as CapabilityReadinessDecision | undefined;
  const readinessValid = readinessDecision !== undefined
    && readinessDecision.schemaVersion === CAPABILITY_READINESS_DECISION_VERSION
    && validId(readinessDecision.readinessDecisionId)
    && validId(readinessDecision.routeDecisionId)
    && validId(readinessDecision.snapshotId)
    && READINESS_STATES.includes(readinessDecision.state)
    && isBoundedPlainArray(readinessDecision.missingDependencies)
    && isBoundedPlainArray(readinessDecision.approvalRequirements)
    && isBoundedPlainArray(readinessDecision.blockingReasons)
    && isBoundedPlainArray(readinessDecision.evidenceRefs)
    && safeString(readinessDecision.nextSafeAction)
    && validUtc(readinessDecision.evaluatedAt)
    && readinessDecision.authorityStatus === 'EVIDENCE_ONLY'
    && readinessDecision.executionAuthorized === false
    && routeDecision !== undefined
    && readinessDecision.routeDecisionId === routeDecision.routeDecisionId;
  if (!readinessValid) {
    issues.push(issue('INVALID_FIELD', '$.caseInput.readiness', 'readiness must preserve canonical evidence-only invariants and bind the route decision.'));
  }

  const sourceRefs: string[] = [];
  if (routeValid) sourceRefs.push(`route:${routeDecision.routeDecisionId}`);
  if (readinessValid) {
    sourceRefs.push(`readiness:${readinessDecision.readinessDecisionId}`);
    sourceRefs.push(`snapshot:${readinessDecision.snapshotId}`);
  }

  const acquisitionAuthorization = safeCaseInput?.acquisitionAuthorization ?? null;
  const acquisitionAuthorizationRef = safeCaseInput
    ? normalizeNullableSafeString(safeCaseInput.acquisitionAuthorizationRef, '$.caseInput.acquisitionAuthorizationRef', issues)
    : null;
  const hasAuthorization = isPlainRecord(acquisitionAuthorization)
    && acquisitionAuthorization.contractVersion === CONTROLLED_ACQUISITION_CONTRACT_VERSION
    && (acquisitionAuthorization.decision === 'AUTHORIZED_FOR_SEPARATE_EXECUTOR' || acquisitionAuthorization.decision === 'DENIED')
    && isBoundedPlainArray(acquisitionAuthorization.issues);
  if (acquisitionAuthorization !== null && acquisitionAuthorization !== undefined && !hasAuthorization) {
    issues.push(issue('MALFORMED_INPUT', '$.caseInput.acquisitionAuthorization', 'acquisitionAuthorization must preserve the canonical result shape or be null.'));
  }
  if (hasAuthorization && !validId(acquisitionAuthorizationRef)) {
    issues.push(issue('INVALID_FIELD', '$.caseInput.acquisitionAuthorizationRef', 'A bounded source reference is required with acquisition authorization evidence.'));
  }
  if (!hasAuthorization && acquisitionAuthorizationRef !== null) {
    issues.push(issue('INVALID_FIELD', '$.caseInput.acquisitionAuthorizationRef', 'An authorization source reference cannot exist without authorization evidence.'));
  }
  if (hasAuthorization && validId(acquisitionAuthorizationRef)) sourceRefs.push(`acquisitionAuthorization:${acquisitionAuthorizationRef}:${acquisitionAuthorization.decision}`);

  const acquisitionReceipt = safeCaseInput?.acquisitionReceipt ?? null;
  const acquisitionReceiptRef = safeCaseInput
    ? normalizeNullableSafeString(safeCaseInput.acquisitionReceiptRef, '$.caseInput.acquisitionReceiptRef', issues)
    : null;
  const hasReceipt = isPlainRecord(acquisitionReceipt)
    && (acquisitionReceipt.status === 'SUCCESS' || acquisitionReceipt.status === 'FAIL')
    && isBoundedPlainArray(acquisitionReceipt.issues);
  if (acquisitionReceipt !== null && acquisitionReceipt !== undefined && !hasReceipt) {
    issues.push(issue('MALFORMED_INPUT', '$.caseInput.acquisitionReceipt', 'acquisitionReceipt must preserve the canonical result shape or be null.'));
  }
  if (hasReceipt && !validId(acquisitionReceiptRef)) {
    issues.push(issue('INVALID_FIELD', '$.caseInput.acquisitionReceiptRef', 'A bounded source reference is required with acquisition receipt evidence.'));
  }
  if (!hasReceipt && acquisitionReceiptRef !== null) {
    issues.push(issue('INVALID_FIELD', '$.caseInput.acquisitionReceiptRef', 'A receipt source reference cannot exist without receipt evidence.'));
  }
  if (hasReceipt && validId(acquisitionReceiptRef)) sourceRefs.push(`acquisitionReceipt:${acquisitionReceiptRef}:${acquisitionReceipt.status}`);

  const staleness = safeCaseInput
    ? evaluateStaleness(now, safeCaseInput.sourceObservedAt, safeCaseInput.sourceExpiresAt, issues)
    : (issues.push(issue('INVALID_FIELD', '$.caseInput.sourceObservedAt', 'sourceObservedAt/sourceExpiresAt require a valid case input.')), 'INVALID' as ProjectionStalenessState);

  const projectionId = safeDomainInput && validId(safeDomainInput.projectionId) ? safeDomainInput.projectionId : 'invalid';
  if (!safeDomainInput || !validId(safeDomainInput.projectionId)) {
    issues.push(issue('INVALID_FIELD', '$.domainInput.projectionId', 'projectionId must be a bounded safe identifier.'));
  }

  const evidenceInputs = safeDomainInput && isBoundedPlainArray(safeDomainInput.evidence) ? safeDomainInput.evidence : [];
  if (safeDomainInput && !isBoundedPlainArray(safeDomainInput.evidence)) issues.push(issue('INVALID_FIELD', '$.domainInput.evidence', 'evidence must be a bounded plain array.'));
  const evidence: ProjectedEvidence[] = [];
  const seenEvidenceIds = new Set<string>();
  evidenceInputs.forEach((item, index) => {
    const validated = validateEvidence(item, index, issues);
    if (!validated) return;
    if (seenEvidenceIds.has(validated.evidenceId)) {
      issues.push(issue('DUPLICATE_EVIDENCE_ID', `$.evidence[${index}].evidenceId`, 'Duplicate evidenceId was rejected.'));
      return;
    }
    seenEvidenceIds.add(validated.evidenceId);
    evidence.push(validated);
  });

  evidence.sort((left, right) => compareText(left.evidenceId, right.evidenceId));

  const findingInputs = safeDomainInput && isBoundedPlainArray(safeDomainInput.findings) ? safeDomainInput.findings : [];
  if (safeDomainInput && !isBoundedPlainArray(safeDomainInput.findings)) issues.push(issue('INVALID_FIELD', '$.domainInput.findings', 'findings must be a bounded plain array.'));
  const findings: ProjectedFinding[] = [];
  const seenFindingIds = new Set<string>();
  findingInputs.forEach((item, index) => {
    const validated = validateFinding(item, index, seenEvidenceIds, issues);
    if (!validated) return;
    if (seenFindingIds.has(validated.findingId)) {
      issues.push(issue('DUPLICATE_FINDING_ID', `$.findings[${index}].findingId`, 'Duplicate findingId was rejected.'));
      return;
    }
    seenFindingIds.add(validated.findingId);
    findings.push(validated);
  });

  findings.sort((left, right) => compareText(left.findingId, right.findingId));

  const pathInputs = safeDomainInput && isBoundedPlainArray(safeDomainInput.paths) ? safeDomainInput.paths : [];
  if (safeDomainInput && !isBoundedPlainArray(safeDomainInput.paths)) issues.push(issue('INVALID_FIELD', '$.domainInput.paths', 'paths must be a bounded plain array.'));
  const paths: ProjectedPath[] = [];
  const seenPathIds = new Set<string>();
  pathInputs.forEach((item, index) => {
    const validated = validatePath(item, index, seenEvidenceIds, issues);
    if (!validated) return;
    if (seenPathIds.has(validated.pathId)) {
      issues.push(issue('DUPLICATE_PATH_ID', `$.paths[${index}].pathId`, 'Duplicate pathId was rejected.'));
      return;
    }
    seenPathIds.add(validated.pathId);
    paths.push(validated);
  });

  paths.sort((left, right) => compareText(left.pathId, right.pathId));
  issues.sort((left, right) => compareText(`${left.path}\u0000${left.code}\u0000${left.message}`, `${right.path}\u0000${right.code}\u0000${right.message}`));

  const readinessState = readinessValid ? readinessDecision.state : undefined;
  const hasNonStalenessIssue = issues.some(({ code }) => code !== 'STALE_SOURCE');
  const currentDisposition = hasNonStalenessIssue
    ? 'INVALID'
    : staleness !== 'CURRENT'
    ? staleness
    : (typeof readinessState === 'string' && validId(readinessState) ? readinessState : 'UNKNOWN');

  const generatedAt = validUtc(now) ? now : '1970-01-01T00:00:00Z';

  const base: Omit<CapabilityCaseEvidenceProjection, 'projectionDigest'> = {
    schemaVersion: CAPABILITY_CASE_EVIDENCE_PROJECTION_CONTRACT_VERSION,
    caseProjectionVersion: CAPABILITY_CASE_PROJECTION_VERSION,
    domainEvidenceProjectionVersion: DOMAIN_EVIDENCE_PROJECTION_VERSION,
    authorityNotice: 'PROJECTION_ONLY',
    authorityMutation: false,
    caseId,
    requestId,
    workspaceId,
    workOrderId,
    projectionId,
    sourceRefs: Object.freeze(sourceRefs),
    staleness,
    currentDisposition,
    evidence: Object.freeze(evidence),
    findings: Object.freeze(findings),
    paths: Object.freeze(paths),
    generatedAt,
    issues: Object.freeze(issues),
  };

  return Object.freeze({ ...base, projectionDigest: computeProjectionDigest(base) });
}
