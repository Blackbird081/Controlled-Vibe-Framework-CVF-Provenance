/** Owner-bound CADP evidence contract backed by committed repository authority. */

import { isProxy } from 'node:util/types';
import {
  consumeRepositoryGrantInvocation,
  loadCommittedRepositoryCapabilityGrant,
  RepositoryOwnerSourceError,
  type RepositoryArtifactType,
  type VerifiedRepositoryGrant,
} from './repository-capability-owner.source';

export const CAPABILITY_OWNER_BINDING_CONTRACT_VERSION = 'cvf.cadp.ownerBinding.v3' as const;

export type CapabilityOwnerBindingIssueCode =
  | 'INVALID_FIELD'
  | 'MALFORMED_INPUT_SHAPE'
  | 'RAW_SECRET_INCLUDED'
  | 'GRANT_MISMATCH'
  | 'NOT_A_BOUND_OWNER'
  | 'EVALUATION_NOT_YET_VALID'
  | 'EVALUATION_EXPIRED'
  | 'INVOCATION_LIMIT_EXCEEDED'
  | 'RETRY_LIMIT_EXCEEDED'
  | 'TRACE_LINKAGE_MISSING'
  | 'RECEIPT_LINKAGE_MISSING'
  | 'DUPLICATE_INVOCATION_REJECTED'
  | 'ARTIFACT_NOT_BOUND'
  | 'CREDENTIAL_REFERENCE_INVALID'
  | 'SOURCE_VERIFICATION_FAILED';

export interface CapabilityOwnerBindingIssue {
  readonly code: CapabilityOwnerBindingIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface CapabilityOwnerBindingResult<TData = Readonly<Record<string, unknown>>> {
  readonly valid: boolean;
  readonly issues: readonly CapabilityOwnerBindingIssue[];
  readonly data: TData;
}

export type BoundArtifactType = RepositoryArtifactType;

/** Opaque by identity: only this module's WeakSet can authenticate a handle. */
export interface CapabilityOwnerHandle {
  readonly contractVersion: typeof CAPABILITY_OWNER_BINDING_CONTRACT_VERSION;
}

export interface CapabilityOwnerBindData {
  readonly handle?: CapabilityOwnerHandle;
  readonly grantHash?: string;
}

export interface BoundArtifactProjection {
  readonly ref: string;
  readonly artifactType: BoundArtifactType;
  readonly owner: string;
}

export interface CapabilityOwnerGrantProjection {
  readonly workOrderId: string;
  readonly workOrderVersion: string;
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly assignmentId: string;
  readonly actionId: string;
  readonly grantHash: string;
}

export interface CapabilityExecutionObservationInput {
  readonly workOrderId: string;
  readonly workOrderVersion: string;
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly assignmentId: string;
  readonly actionId: string;
  readonly transport: string;
  readonly resourceRef: string;
  readonly credentialReference: string;
  readonly workflowTraceId: string;
  readonly receiptId: string;
  readonly invocationId: string;
  readonly retryOrdinal: number;
  readonly evaluatedAt: string;
}

const BOUND_OWNERS = new WeakSet<object>();
const OWNER_RECORDS = new WeakMap<object, VerifiedRepositoryGrant>();
const OBSERVATION_KEYS = [
  'workOrderId', 'workOrderVersion', 'capabilityId', 'capabilityVersion', 'assignmentId',
  'actionId', 'transport', 'resourceRef', 'credentialReference', 'workflowTraceId',
  'receiptId', 'invocationId', 'retryOrdinal', 'evaluatedAt',
] as const;
const TEXT_KEYS = OBSERVATION_KEYS.filter((key) => key !== 'retryOrdinal');
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const SAFE_OBSERVATION_ID = /^[A-Za-z0-9._:/-]{1,256}$/;

function issue(code: CapabilityOwnerBindingIssueCode, path: string, message: string): CapabilityOwnerBindingIssue {
  return Object.freeze({ code, path, message });
}

function sourceIssue(error: unknown): CapabilityOwnerBindingIssue {
  if (!(error instanceof RepositoryOwnerSourceError)) {
    return issue('SOURCE_VERIFICATION_FAILED', '$.grantRef', 'Repository owner verification failed closed.');
  }
  const code: CapabilityOwnerBindingIssueCode = error.code === 'INVOCATION_LIMIT_EXCEEDED'
    ? 'INVOCATION_LIMIT_EXCEEDED'
    : error.code === 'RETRY_LIMIT_EXCEEDED'
      ? 'RETRY_LIMIT_EXCEEDED'
      : error.code === 'DUPLICATE_INVOCATION_REJECTED'
        ? 'DUPLICATE_INVOCATION_REJECTED'
        : 'SOURCE_VERIFICATION_FAILED';
  return issue(code, '$.repositoryOwner', error.message);
}

/**
 * Deliberate authority front door. The caller supplies only a normalized path;
 * all grant and artifact values are independently read from committed HEAD.
 */
export function bindCommittedCapabilityOwnerGrant(grantRef: unknown): CapabilityOwnerBindingResult<CapabilityOwnerBindData> {
  try {
    const record = loadCommittedRepositoryCapabilityGrant(grantRef);
    const handle: CapabilityOwnerHandle = Object.freeze({ contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION });
    BOUND_OWNERS.add(handle);
    OWNER_RECORDS.set(handle, record);
    return Object.freeze({ valid: true, issues: Object.freeze([]), data: Object.freeze({ handle, grantHash: record.grantHash }) });
  } catch (error) {
    return Object.freeze({ valid: false, issues: Object.freeze([sourceIssue(error)]), data: Object.freeze({}) });
  }
}

export function isBoundCapabilityOwner(value: unknown): value is CapabilityOwnerHandle {
  return value !== null && typeof value === 'object' && BOUND_OWNERS.has(value);
}

export function readBoundArtifact(handle: CapabilityOwnerHandle, ref: string): BoundArtifactProjection | undefined {
  if (!isBoundCapabilityOwner(handle) || typeof ref !== 'string') return undefined;
  const artifact = OWNER_RECORDS.get(handle)?.artifacts.find((candidate) => candidate.ref === ref);
  return artifact ? Object.freeze({ ref: artifact.ref, artifactType: artifact.artifactType, owner: artifact.owner }) : undefined;
}

export function readBoundGrantIdentity(handle: CapabilityOwnerHandle): CapabilityOwnerGrantProjection | undefined {
  if (!isBoundCapabilityOwner(handle)) return undefined;
  const record = OWNER_RECORDS.get(handle);
  return record ? Object.freeze({
    workOrderId: record.workOrderId, workOrderVersion: record.workOrderVersion,
    capabilityId: record.capabilityId, capabilityVersion: record.capabilityVersion,
    assignmentId: record.assignmentId, actionId: record.actionId, grantHash: record.grantHash,
  }) : undefined;
}

function readObservation(value: unknown): { observation?: CapabilityExecutionObservationInput; issues: CapabilityOwnerBindingIssue[] } {
  const issues: CapabilityOwnerBindingIssue[] = [];
  if (value === null || typeof value !== 'object' || isProxy(value)) {
    return { issues: [issue('MALFORMED_INPUT_SHAPE', '$.observation', 'Observation must be a non-Proxy plain data object.')] };
  }
  const prototype = Object.getPrototypeOf(value);
  if (prototype !== Object.prototype && prototype !== null) {
    return { issues: [issue('MALFORMED_INPUT_SHAPE', '$.observation', 'Observation must have a plain prototype.')] };
  }
  const names = Object.getOwnPropertyNames(value);
  if (Object.getOwnPropertySymbols(value).length || names.length !== OBSERVATION_KEYS.length ||
      names.some((name) => !OBSERVATION_KEYS.includes(name as typeof OBSERVATION_KEYS[number]))) {
    return { issues: [issue('MALFORMED_INPUT_SHAPE', '$.observation', 'Observation has missing or unknown fields.')] };
  }
  const data: Record<string, unknown> = {};
  for (const key of OBSERVATION_KEYS) {
    const descriptor = Object.getOwnPropertyDescriptor(value, key);
    if (!descriptor || !('value' in descriptor) || !descriptor.enumerable) {
      issues.push(issue('MALFORMED_INPUT_SHAPE', `$.observation.${key}`, 'Observation fields must be enumerable data properties.'));
      continue;
    }
    data[key] = descriptor.value;
  }
  for (const key of TEXT_KEYS) {
    if (typeof data[key] !== 'string' || !(data[key] as string).trim()) {
      issues.push(issue('INVALID_FIELD', `$.observation.${key}`, 'A non-empty string is required.'));
    }
  }
  if (!Number.isSafeInteger(data.retryOrdinal) || (data.retryOrdinal as number) < 0) {
    issues.push(issue('INVALID_FIELD', '$.observation.retryOrdinal', 'retryOrdinal must be a non-negative safe integer.'));
  }
  for (const key of ['workflowTraceId', 'receiptId', 'invocationId'] as const) {
    if (typeof data[key] === 'string' && !SAFE_OBSERVATION_ID.test(data[key])) {
      issues.push(issue('INVALID_FIELD', `$.observation.${key}`, `${key} must be a bounded safe identifier.`));
    }
  }
  if (typeof data.evaluatedAt === 'string' && (!ISO_UTC.test(data.evaluatedAt) || !Number.isFinite(Date.parse(data.evaluatedAt)))) {
    issues.push(issue('INVALID_FIELD', '$.observation.evaluatedAt', 'evaluatedAt must be an ISO-8601 UTC timestamp.'));
  }
  return issues.length ? { issues } : { observation: data as unknown as CapabilityExecutionObservationInput, issues };
}

export function reconcileGrantWithObservation(
  handle: CapabilityOwnerHandle,
  observationInput: CapabilityExecutionObservationInput,
): CapabilityOwnerBindingResult<{ readonly reconciled: boolean }> {
  if (!isBoundCapabilityOwner(handle)) {
    return { valid: false, issues: [issue('NOT_A_BOUND_OWNER', '$.handle', 'Handle is not authenticated by the repository owner source.')], data: { reconciled: false } };
  }
  const record = OWNER_RECORDS.get(handle);
  if (!record) {
    return { valid: false, issues: [issue('NOT_A_BOUND_OWNER', '$.handle', 'Bound owner state is unavailable.')], data: { reconciled: false } };
  }
  const parsed = readObservation(observationInput);
  if (!parsed.observation) return { valid: false, issues: parsed.issues, data: { reconciled: false } };
  const observation = parsed.observation;
  const issues = parsed.issues;
  const exact: Array<readonly [keyof CapabilityExecutionObservationInput, string]> = [
    ['workOrderId', record.workOrderId], ['workOrderVersion', record.workOrderVersion],
    ['capabilityId', record.capabilityId], ['capabilityVersion', record.capabilityVersion],
    ['assignmentId', record.assignmentId], ['actionId', record.actionId],
    ['transport', record.transport], ['resourceRef', record.resourceRef],
    ['credentialReference', record.credentialReference],
  ];
  for (const [key, expected] of exact) {
    if (observation[key] !== expected) issues.push(issue('GRANT_MISMATCH', `$.observation.${key}`, `${key} does not match the committed grant.`));
  }
  if (!record.boundWorkflowTraceIds.includes(observation.workflowTraceId)) {
    issues.push(issue('TRACE_LINKAGE_MISSING', '$.observation.workflowTraceId', 'Workflow trace is not bound by the committed grant.'));
  }
  if (!record.boundReceiptIds.includes(observation.receiptId)) {
    issues.push(issue('RECEIPT_LINKAGE_MISSING', '$.observation.receiptId', 'Receipt is not bound by the committed grant.'));
  }
  const evaluated = Date.parse(observation.evaluatedAt);
  if (evaluated < Date.parse(record.validFrom)) issues.push(issue('EVALUATION_NOT_YET_VALID', '$.observation.evaluatedAt', 'Evaluation precedes grant validity.'));
  if (evaluated > Date.parse(record.validUntil)) issues.push(issue('EVALUATION_EXPIRED', '$.observation.evaluatedAt', 'Evaluation exceeds grant validity.'));
  if (issues.length) return { valid: false, issues, data: { reconciled: false } };
  try {
    consumeRepositoryGrantInvocation(record, observation.invocationId, observation.retryOrdinal);
    return { valid: true, issues: [], data: { reconciled: true } };
  } catch (error) {
    return { valid: false, issues: [sourceIssue(error)], data: { reconciled: false } };
  }
}
