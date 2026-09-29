/**
 * T3A Execution Plane verified capability consumer.
 *
 * A hermetic, non-executing downstream consumer of the T2A repository-owned
 * CADP owner handle and the existing admission, assignment, distribution, and
 * evidence validators. It produces only a frozen pre-execution eligibility
 * projection with a literal `executionAuthorized: false`. It never invokes an
 * action or provider, never accepts or returns raw secret material, and never
 * creates a second authority source.
 */

import { isProxy } from 'node:util/types';
import {
  isBoundCapabilityOwner,
  readBoundGrantIdentity,
  reconcileGrantWithObservation,
  type CapabilityExecutionObservationInput,
  type CapabilityOwnerHandle,
} from '../../CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract';
import {
  validateCapabilityAdmission,
  validateCapabilityAssignment,
  validateCapabilityDistribution,
  validateCompatibilityEvidence,
  type CapabilityAdmissionRecord,
  type CapabilityAssignmentRecord,
  type CapabilityDistributionManifest,
  type CompatibilityEvidenceRecord,
} from '../../CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract';

export const CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION = 'cvf.cadp.consumer.v1' as const;

/** Adapter-local issue codes. Upstream validator issue codes pass through unchanged. */
export type CadpCapabilityConsumerIssueCode =
  | 'MALFORMED_REQUEST'
  | 'NOT_A_BOUND_OWNER'
  | 'OWNER_IDENTITY_UNAVAILABLE'
  | 'CROSS_RECORD_MISMATCH'
  | 'ACTION_NOT_ADMITTED'
  | 'ACTION_NOT_ASSIGNED'
  | 'ACTION_NOT_EVIDENCED';

export interface CadpCapabilityConsumerIssue {
  readonly code: string;
  readonly path: string;
  readonly message: string;
}

/**
 * Strict plain-data, non-Proxy request envelope. The caller supplies only an
 * already bound opaque owner handle plus the non-mutating CADP records and the
 * execution observation. No grant object or repository path is accepted, so a
 * caller cannot self-certify authority.
 */
export interface CadpCapabilityConsumerRequest {
  readonly ownerHandle: CapabilityOwnerHandle;
  readonly admission: CapabilityAdmissionRecord;
  readonly assignment: CapabilityAssignmentRecord;
  readonly distribution: CapabilityDistributionManifest;
  readonly evidence: CompatibilityEvidenceRecord;
  readonly observation: CapabilityExecutionObservationInput;
}

export type CadpCapabilityConsumerDecision = 'ELIGIBLE' | 'NOT_ELIGIBLE';

/** Frozen pre-execution eligibility projection. Never carries execution authority. */
export interface CadpCapabilityEligibilityProjection {
  readonly decision: CadpCapabilityConsumerDecision;
  readonly executionAuthorized: false;
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly assignmentId: string;
  readonly actionId: string;
  readonly reconciled: boolean;
}

export interface CadpCapabilityConsumerResult {
  readonly valid: boolean;
  readonly issues: readonly CadpCapabilityConsumerIssue[];
  readonly projection: CadpCapabilityEligibilityProjection;
}

const REQUEST_KEYS = ['ownerHandle', 'admission', 'assignment', 'distribution', 'evidence', 'observation'] as const;

function makeIssue(code: string, path: string, message: string): CadpCapabilityConsumerIssue {
  return Object.freeze({ code, path, message });
}

function mapIssues(upstream: readonly { readonly code: string; readonly path: string; readonly message: string }[]): CadpCapabilityConsumerIssue[] {
  return upstream.map((issue) => Object.freeze({ code: issue.code, path: issue.path, message: issue.message }));
}

function emptyProjection(): CadpCapabilityEligibilityProjection {
  return Object.freeze({
    decision: 'NOT_ELIGIBLE',
    executionAuthorized: false,
    capabilityId: '',
    capabilityVersion: '',
    assignmentId: '',
    actionId: '',
    reconciled: false,
  });
}

function freezeResult(
  valid: boolean,
  issues: CadpCapabilityConsumerIssue[],
  projection: CadpCapabilityEligibilityProjection,
): CadpCapabilityConsumerResult {
  return Object.freeze({ valid, issues: Object.freeze([...issues]), projection });
}

function isPlainNonProxyRecord(value: unknown): value is Record<string, unknown> {
  if (value === null || typeof value !== 'object') return false;
  if (isProxy(value)) return false;
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

/** Trap-free own enumerable data descriptor read. Never invokes an accessor. */
function ownDataField(owner: unknown, key: string): { readonly present: boolean; readonly value: unknown } {
  if (owner === null || (typeof owner !== 'object' && typeof owner !== 'function')) {
    return { present: false, value: undefined };
  }
  if (isProxy(owner)) return { present: false, value: undefined };
  const descriptor = Object.getOwnPropertyDescriptor(owner, key);
  if (!descriptor || !descriptor.enumerable || 'get' in descriptor || 'set' in descriptor) {
    return { present: false, value: undefined };
  }
  return { present: true, value: descriptor.value };
}

/** Safe scalar read for cross-record identity checks on already-validated records. */
function ownDataString(owner: unknown, key: string): string | undefined {
  const field = ownDataField(owner, key);
  return typeof field.value === 'string' ? field.value : undefined;
}

/** Copies an already-validator-approved string array without retaining caller data. */
function ownDataStringArray(owner: unknown, key: string): readonly string[] {
  const field = ownDataField(owner, key);
  if (!field.present || !Array.isArray(field.value) || isProxy(field.value)) return [];
  const result: string[] = [];
  for (let index = 0; index < field.value.length; index += 1) {
    const descriptor = Object.getOwnPropertyDescriptor(field.value, index);
    if (!descriptor || !descriptor.enumerable || 'get' in descriptor || 'set' in descriptor || typeof descriptor.value !== 'string') {
      return [];
    }
    result.push(descriptor.value);
  }
  return result;
}

interface ParsedRequest {
  ownerHandle: unknown;
  admission: unknown;
  assignment: unknown;
  distribution: unknown;
  evidence: unknown;
  observation: unknown;
}

function readRequestEnvelope(value: unknown): { readonly request?: ParsedRequest; readonly issues: CadpCapabilityConsumerIssue[] } {
  if (!isPlainNonProxyRecord(value)) {
    return { issues: [makeIssue('MALFORMED_REQUEST', '$.request', 'Request envelope must be a non-Proxy plain data object.')] };
  }
  const names = Object.getOwnPropertyNames(value);
  if (
    Object.getOwnPropertySymbols(value).length > 0 ||
    names.length !== REQUEST_KEYS.length ||
    names.some((name) => !(REQUEST_KEYS as readonly string[]).includes(name))
  ) {
    return {
      issues: [makeIssue('MALFORMED_REQUEST', '$.request', 'Request envelope has missing or unknown fields; raw secret material is not accepted.')],
    };
  }
  const fields: Record<string, unknown> = {};
  for (const key of REQUEST_KEYS) {
    const field = ownDataField(value, key);
    if (!field.present) {
      return { issues: [makeIssue('MALFORMED_REQUEST', `$.request.${key}`, `Request field ${key} must be an own enumerable data property.`)] };
    }
    fields[key] = field.value;
  }
  return { request: fields as unknown as ParsedRequest, issues: [] };
}

/**
 * Evaluates the full non-mutating CADP record chain against the committed
 * grant identity, then reconciles the observation last. Any upstream failure
 * returns before `reconcileGrantWithObservation`, so malformed or unauthorized
 * requests never consume invocation or retry state.
 */
export function evaluateCadpCapabilityConsumer(
  request: CadpCapabilityConsumerRequest,
): CadpCapabilityConsumerResult {
  const envelope = readRequestEnvelope(request as unknown);
  if (!envelope.request) return freezeResult(false, envelope.issues, emptyProjection());

  const { ownerHandle, admission, assignment, distribution, evidence, observation } = envelope.request;

  if (!isBoundCapabilityOwner(ownerHandle)) {
    return freezeResult(
      false,
      [makeIssue('NOT_A_BOUND_OWNER', '$.ownerHandle', 'Owner handle is not authenticated by the repository owner source.')],
      emptyProjection(),
    );
  }
  const identity = readBoundGrantIdentity(ownerHandle as CapabilityOwnerHandle);
  if (!identity) {
    return freezeResult(
      false,
      [makeIssue('OWNER_IDENTITY_UNAVAILABLE', '$.ownerHandle', 'Bound owner grant identity is unavailable.')],
      emptyProjection(),
    );
  }

  const issues: CadpCapabilityConsumerIssue[] = [];

  const admissionResult = validateCapabilityAdmission(admission as CapabilityAdmissionRecord);
  issues.push(...mapIssues(admissionResult.issues));
  const assignmentResult = validateCapabilityAssignment(
    admission as CapabilityAdmissionRecord,
    assignment as CapabilityAssignmentRecord,
  );
  issues.push(...mapIssues(assignmentResult.issues));
  const distributionResult = validateCapabilityDistribution(distribution as CapabilityDistributionManifest);
  issues.push(...mapIssues(distributionResult.issues));
  const evidenceResult = validateCompatibilityEvidence(
    evidence as CompatibilityEvidenceRecord,
    ownerHandle as CapabilityOwnerHandle,
  );
  issues.push(...mapIssues(evidenceResult.issues));

  if (!admissionResult.valid || !assignmentResult.valid || !distributionResult.valid || !evidenceResult.valid) {
    return freezeResult(false, issues, emptyProjection());
  }

  // Cross-record identity consistency against the committed grant.
  const admissionCapabilityId = ownDataString(admission, 'capabilityId');
  const admissionCapabilityVersion = ownDataString(admission, 'capabilityVersion');
  const assignmentCapabilityId = ownDataString(assignment, 'capabilityId');
  const assignmentCapabilityVersion = ownDataString(assignment, 'capabilityVersion');
  const assignmentId = ownDataString(assignment, 'assignmentId');
  const distributionCapabilityId = ownDataString(distribution, 'capabilityId');
  const evidenceCapabilityId = ownDataString(evidence, 'capabilityId');
  const evidencedActionIds = ownDataStringArray(evidence, 'passingActionIds');

  if (admissionCapabilityId !== identity.capabilityId) {
    issues.push(makeIssue('CROSS_RECORD_MISMATCH', '$.admission.capabilityId', 'Admission capability does not match the committed grant.'));
  }
  if (admissionCapabilityVersion !== identity.capabilityVersion) {
    issues.push(makeIssue('CROSS_RECORD_MISMATCH', '$.admission.capabilityVersion', 'Admission capability version does not match the committed grant.'));
  }
  if (assignmentCapabilityId !== identity.capabilityId) {
    issues.push(makeIssue('CROSS_RECORD_MISMATCH', '$.assignment.capabilityId', 'Assignment capability does not match the committed grant.'));
  }
  if (assignmentCapabilityVersion !== identity.capabilityVersion) {
    issues.push(makeIssue('CROSS_RECORD_MISMATCH', '$.assignment.capabilityVersion', 'Assignment capability version does not match the committed grant.'));
  }
  if (assignmentId !== identity.assignmentId) {
    issues.push(makeIssue('CROSS_RECORD_MISMATCH', '$.assignment.assignmentId', 'Assignment identity does not match the committed grant.'));
  }
  if (distributionCapabilityId !== identity.capabilityId) {
    issues.push(makeIssue('CROSS_RECORD_MISMATCH', '$.distribution.capabilityId', 'Distribution capability does not match the committed grant.'));
  }
  if (evidenceCapabilityId !== identity.capabilityId) {
    issues.push(makeIssue('CROSS_RECORD_MISMATCH', '$.evidence.capabilityId', 'Evidence capability does not match the committed grant.'));
  }

  // The committed action must be both admitted and assigned; no other record
  // may widen action authority.
  const actionId = identity.actionId;
  if (!admissionResult.data.assignableActionIds.includes(actionId)) {
    issues.push(makeIssue('ACTION_NOT_ADMITTED', '$.admission.admittedActions', `Committed action ${actionId} is not admitted.`));
  }
  if (!assignmentResult.data.assignedActionIds.includes(actionId)) {
    issues.push(makeIssue('ACTION_NOT_ASSIGNED', '$.assignment.assignedActionIds', `Committed action ${actionId} is not assigned.`));
  }
  if (!evidencedActionIds.includes(actionId)) {
    issues.push(makeIssue('ACTION_NOT_EVIDENCED', '$.evidence.passingActionIds', `Committed action ${actionId} is not supported by compatibility evidence.`));
  }

  if (issues.length > 0) return freezeResult(false, issues, emptyProjection());

  // Durable consumption happens last, only after the entire non-mutating chain
  // has validated. reconcileGrantWithObservation validates the observation and
  // consumes the invocation only on a full pass.
  const reconciliation = reconcileGrantWithObservation(
    ownerHandle as CapabilityOwnerHandle,
    observation as CapabilityExecutionObservationInput,
  );
  if (!reconciliation.valid) {
    return freezeResult(false, mapIssues(reconciliation.issues), emptyProjection());
  }

  const projection = Object.freeze({
    decision: 'ELIGIBLE',
    executionAuthorized: false,
    capabilityId: identity.capabilityId,
    capabilityVersion: identity.capabilityVersion,
    assignmentId: identity.assignmentId,
    actionId: identity.actionId,
    reconciled: reconciliation.data.reconciled,
  } satisfies CadpCapabilityEligibilityProjection);

  return freezeResult(true, [], projection);
}

export class CadpCapabilityConsumerContract {
  evaluate(request: CadpCapabilityConsumerRequest): CadpCapabilityConsumerResult {
    return evaluateCadpCapabilityConsumer(request);
  }
}

export function createCadpCapabilityConsumerContract(): CadpCapabilityConsumerContract {
  return new CadpCapabilityConsumerContract();
}
