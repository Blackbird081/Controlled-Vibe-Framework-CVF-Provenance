/**
 * Capability bootstrap approval evidence binding kernel.
 *
 * Pure evidence binding only. This module never issues approval, signs
 * anything, consumes or stores a replay nonce, grants an executor, mutates
 * state, or performs I/O. It validates caller-supplied approval evidence
 * against a current controlled-acquisition plan, explicit workspace/actor/
 * work-order expectations, and an exact mutation-envelope scope, keeping
 * every action-authority literal false on every return path.
 */

import { isProxy } from 'node:util/types';
import {
  computeControlledAcquisitionPlanDigest,
  evaluateControlledAcquisitionAuthorization,
  CONTROLLED_ACQUISITION_APPROVAL_VERSION,
  CONTROLLED_ACQUISITION_PLAN_VERSION,
} from './controlled-acquisition.contract';
import type {
  AcquisitionMutationKind,
  ControlledAcquisitionPlan,
} from './controlled-acquisition.contract';

export const CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_CONTRACT_VERSION =
  'cvf.capabilityBootstrapApprovalEvidenceContract.v1' as const;
export const CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION =
  'cvf.capabilityBootstrapApprovalEvidence.v1' as const;
export const CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION =
  'cvf.capabilityBootstrapApprovalEvidenceResult.v1' as const;

export type CapabilityBootstrapApprovalEnvelopeClass =
  | 'FILESYSTEM' | 'REGISTRY' | 'ENVIRONMENT' | 'PROCESS'
  | 'SERVICE' | 'NETWORK' | 'PACKAGE' | 'GIT' | 'OTHER';

export interface CapabilityBootstrapMutationEnvelopeEntry {
  readonly kind: CapabilityBootstrapApprovalEnvelopeClass;
  readonly target: string;
  readonly description: string;
  readonly reversible: boolean;
}

export interface CapabilityBootstrapApprovalEvidence {
  readonly schemaVersion: typeof CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION;
  readonly approvalId: string;
  readonly planId: string;
  readonly planDigest: string;
  readonly workspaceId: string;
  readonly workOrderId: string | null;
  readonly decision: 'APPROVE';
  readonly actorId: string;
  readonly issuedAt: string;
  readonly expiresAt: string;
  readonly replayNonce: string;
  readonly mutationEnvelope: readonly CapabilityBootstrapMutationEnvelopeEntry[];
}

export interface CapabilityBootstrapApprovalEvidenceBindingInput {
  readonly plan: ControlledAcquisitionPlan;
  readonly approval: CapabilityBootstrapApprovalEvidence;
  readonly expectedWorkspaceId: string;
  readonly expectedActorId: string;
  readonly expectedWorkOrderId?: string | null;
  readonly now: string;
}

export type CapabilityBootstrapApprovalEvidenceIssueCode =
  | 'MALFORMED_INPUT' | 'UNKNOWN_KEYS' | 'INVALID_FIELD' | 'CONTROL_CHARACTER'
  | 'SECRET_LIKE_CONTENT' | 'NON_LOWERCASE_DIGEST'
  | 'PLAN_SCHEMA_UNSUPPORTED' | 'PLAN_DIGEST_MISMATCH' | 'PLAN_EXPIRED' | 'PLAN_T3_REJECTED'
  | 'APPROVAL_SCHEMA_UNSUPPORTED' | 'APPROVAL_ID_INVALID'
  | 'APPROVAL_NOT_APPROVED' | 'APPROVAL_EXPIRED'
  | 'APPROVAL_EXPIRY_EXCEEDS_PLAN_EXPIRY'
  | 'PLAN_BINDING_MISMATCH' | 'WORKSPACE_MISMATCH' | 'ACTOR_MISMATCH'
  | 'WORK_ORDER_MISMATCH' | 'NONCE_INVALID'
  | 'ENVELOPE_MISSING_ENTRY' | 'ENVELOPE_EXTRA_ENTRY' | 'ENVELOPE_DUPLICATE_ENTRY'
  | 'ENVELOPE_AMBIGUOUS_ENTRY' | 'ENVELOPE_IRREVERSIBLE_WITHOUT_MARKER'
  | 'ENVELOPE_SECRET_LIKE_ENTRY';

export interface CapabilityBootstrapApprovalEvidenceIssue {
  readonly code: CapabilityBootstrapApprovalEvidenceIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface CapabilityBootstrapApprovalEvidenceBindingResult {
  readonly schemaVersion: typeof CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION;
  readonly disposition: 'VALIDATED_EVIDENCE' | 'REJECTED';
  readonly planId?: string;
  readonly planDigest?: string;
  readonly approvalId?: string;
  readonly workspaceId?: string;
  readonly actorId?: string;
  readonly workOrderId?: string | null;
  readonly replayCheckRequired: true;
  readonly approvalIssued: false;
  readonly executionAuthorized: false;
  readonly acquisitionAuthorized: false;
  readonly mutationAuthorized: false;
  readonly taskAuthorityGranted: false;
  readonly networkAuthorized: false;
  readonly issues: readonly CapabilityBootstrapApprovalEvidenceIssue[];
}

const MAX_STRING = 256;
const MAX_ENVELOPE = 64;
const MAX_PLAN_ARRAY = 128;
const MAX_SOURCE_URI = 2048;

const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const LOWERCASE_SHA256 = /^[a-f0-9]{64}$/;
const SHA256_DIGEST_CASE_INSENSITIVE = /^[0-9a-fA-F]{64}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const CONTROL_CHAR = /[\u0000-\u001F\u007F]/;
const SECRET_SIGNAL = /(secret|token|password|credential\s*=|api[_-]?key)/i;

const ENVELOPE_CLASSES: readonly CapabilityBootstrapApprovalEnvelopeClass[] = [
  'FILESYSTEM', 'REGISTRY', 'ENVIRONMENT', 'PROCESS',
  'SERVICE', 'NETWORK', 'PACKAGE', 'GIT', 'OTHER',
];

const INPUT_KEYS: readonly string[] = [
  'plan', 'approval', 'expectedWorkspaceId', 'expectedActorId', 'expectedWorkOrderId', 'now',
];

const APPROVAL_KEYS: readonly string[] = [
  'schemaVersion', 'approvalId', 'planId', 'planDigest', 'workspaceId', 'workOrderId',
  'decision', 'actorId', 'issuedAt', 'expiresAt', 'replayNonce', 'mutationEnvelope',
];

const ENVELOPE_ENTRY_KEYS: readonly string[] = ['kind', 'target', 'description', 'reversible'];
const PLAN_KEYS: readonly string[] = [
  'schemaVersion', 'planId', 'dependencyId', 'targetVersion', 'sourceUri', 'provenanceRef',
  'integrityMethod', 'expectedDigest', 'operations', 'intendedMutations', 'rollbackOperationIds',
  'verificationOperationIds', 'forbiddenMutationKinds', 'expiresAt', 'planDigest',
];
const OPERATION_KEYS: readonly string[] = [
  'operationId', 'phase', 'action', 'target', 'networkDestination', 'requiresPrivilege',
];
const MUTATION_KEYS: readonly string[] = ['kind', 'target'];
const OPERATION_PHASES = ['ACQUIRE', 'ROLLBACK', 'VERIFY'] as const;
const ACQUISITION_ACTIONS = [
  'DOWNLOAD', 'INSTALL', 'UPDATE', 'REMOVE', 'WRITE_ENV', 'WRITE_PATH', 'WRITE_SERVICE',
  'GIT_MUTATION', 'BIND_CREDENTIAL', 'VERIFY', 'ROLLBACK',
] as const;
const MUTATION_KINDS: readonly AcquisitionMutationKind[] = [
  'WORKSPACE_FILE', 'USER_FILE', 'SYSTEM_FILE', 'ENVIRONMENT', 'PATH',
  'REGISTRY', 'SERVICE', 'PROCESS', 'GIT', 'CREDENTIAL_BINDING',
];

// Bounded normalization from the current controlled-acquisition mutation
// vocabulary into the approval-envelope class vocabulary. No new mutation
// kind is introduced; this is a pure relabeling for exact set-equality
// comparison against caller-supplied envelope entries.
const MUTATION_KIND_TO_ENVELOPE_CLASS: Readonly<Record<AcquisitionMutationKind, CapabilityBootstrapApprovalEnvelopeClass>> = {
  WORKSPACE_FILE: 'FILESYSTEM',
  USER_FILE: 'FILESYSTEM',
  SYSTEM_FILE: 'FILESYSTEM',
  ENVIRONMENT: 'ENVIRONMENT',
  PATH: 'ENVIRONMENT',
  REGISTRY: 'REGISTRY',
  SERVICE: 'SERVICE',
  PROCESS: 'PROCESS',
  GIT: 'GIT',
  CREDENTIAL_BINDING: 'OTHER',
};

function issue(
  code: CapabilityBootstrapApprovalEvidenceIssueCode,
  path: string,
  message: string,
): CapabilityBootstrapApprovalEvidenceIssue {
  return Object.freeze({ code, path, message });
}

function isPlainRecord(value: unknown): value is Record<string, unknown> {
  if (value === null || typeof value !== 'object' || isProxy(value)) return false;
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

function hasAccessorProperties(value: object): boolean {
  for (const key of Reflect.ownKeys(value)) {
    const descriptor = Object.getOwnPropertyDescriptor(value, key);
    if (descriptor && (typeof descriptor.get === 'function' || typeof descriptor.set === 'function')) return true;
  }
  return false;
}

function isSafeArray(value: unknown): value is unknown[] {
  if (!Array.isArray(value) || isProxy(value) || hasAccessorProperties(value)) return false;
  for (const key of Reflect.ownKeys(value)) {
    if (key === 'length') continue;
    if (typeof key !== 'string' || !/^(?:0|[1-9]\d*)$/.test(key) || Number(key) >= value.length) return false;
  }
  for (let index = 0; index < value.length; index += 1) {
    if (!(index in value)) return false;
  }
  return true;
}

function validUtc(value: unknown): value is string {
  if (typeof value !== 'string' || !ISO_UTC.test(value) || !Number.isFinite(Date.parse(value))) return false;
  const [datePart, timePart] = value.split('T');
  const [year, month, day] = datePart.split('-').map(Number);
  const [hour, minute, second] = timePart.slice(0, 8).split(':').map(Number);
  const parsed = new Date(0);
  parsed.setUTCFullYear(year, month - 1, day);
  parsed.setUTCHours(hour, minute, second, 0);
  return parsed.getUTCFullYear() === year
    && parsed.getUTCMonth() === month - 1
    && parsed.getUTCDate() === day
    && parsed.getUTCHours() === hour
    && parsed.getUTCMinutes() === minute
    && parsed.getUTCSeconds() === second;
}

function hasControlChars(value: string): boolean {
  return CONTROL_CHAR.test(value);
}

function hasSecretSignal(value: string): boolean {
  return SECRET_SIGNAL.test(value);
}

function hasNonLowercaseDigest(value: string): boolean {
  return SHA256_DIGEST_CASE_INSENSITIVE.test(value) && !LOWERCASE_SHA256.test(value);
}

function checkUnknownKeys(
  record: Record<string, unknown>,
  allowed: readonly string[],
  path: string,
  issues: CapabilityBootstrapApprovalEvidenceIssue[],
): void {
  for (const key of Reflect.ownKeys(record)) {
    if (typeof key !== 'string' || !allowed.includes(key)) {
      issues.push(issue('UNKNOWN_KEYS', `${path}.[unknown]`, 'An unknown or symbol key is not allowed.'));
    }
  }
}

function validateBoundedId(
  value: unknown,
  path: string,
  issues: CapabilityBootstrapApprovalEvidenceIssue[],
): string | null {
  if (typeof value !== 'string' || value.length === 0 || value.length > MAX_STRING) {
    issues.push(issue('INVALID_FIELD', path, 'Expected a bounded string.'));
    return null;
  }
  if (hasControlChars(value)) {
    issues.push(issue('CONTROL_CHARACTER', path, 'Control characters are not allowed.'));
    return null;
  }
  if (hasSecretSignal(value)) {
    issues.push(issue('SECRET_LIKE_CONTENT', path, 'Secret-like content is not allowed.'));
    return null;
  }
  if (hasNonLowercaseDigest(value)) {
    issues.push(issue('NON_LOWERCASE_DIGEST', path, 'SHA-256 digests must be lowercase.'));
    return null;
  }
  if (!SAFE_ID.test(value)) {
    issues.push(issue('INVALID_FIELD', path, 'Expected a bounded safe identifier.'));
    return null;
  }
  return value;
}

function validateEnvelopeEntry(
  entry: unknown,
  index: number,
  issues: CapabilityBootstrapApprovalEvidenceIssue[],
): CapabilityBootstrapMutationEnvelopeEntry | null {
  const path = `$.approval.mutationEnvelope[${index}]`;
  if (!isPlainRecord(entry) || hasAccessorProperties(entry)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Envelope entry must be a plain non-Proxy object without accessors.'));
    return null;
  }
  checkUnknownKeys(entry, ENVELOPE_ENTRY_KEYS, path, issues);

  let kindValid = true;
  if (typeof entry.kind !== 'string' || !ENVELOPE_CLASSES.includes(entry.kind as CapabilityBootstrapApprovalEnvelopeClass)) {
    issues.push(issue('INVALID_FIELD', `${path}.kind`, 'Unsupported envelope class.'));
    kindValid = false;
  }

  const target = validateBoundedId(entry.target, `${path}.target`, issues);

  if (typeof entry.description !== 'string' || entry.description.length === 0 || entry.description.length > MAX_STRING) {
    issues.push(issue('INVALID_FIELD', `${path}.description`, 'Description must be a bounded non-empty string.'));
  } else if (hasControlChars(entry.description)) {
    issues.push(issue('CONTROL_CHARACTER', `${path}.description`, 'Control characters are not allowed.'));
  } else if (hasSecretSignal(entry.description)) {
    issues.push(issue('ENVELOPE_SECRET_LIKE_ENTRY', `${path}.description`, 'Envelope description must not contain secret-like content.'));
  }

  if (typeof entry.reversible !== 'boolean') {
    issues.push(issue('INVALID_FIELD', `${path}.reversible`, 'Reversible must be a boolean.'));
  } else if (entry.reversible === false && typeof entry.description === 'string' && !/irreversible/i.test(entry.description)) {
    issues.push(issue('ENVELOPE_IRREVERSIBLE_WITHOUT_MARKER', `${path}.description`, 'Irreversible entries must carry an explicit irreversible marker in the description.'));
  }

  if (!kindValid || target === null) return null;

  return Object.freeze({
    kind: entry.kind as CapabilityBootstrapApprovalEnvelopeClass,
    target,
    description: typeof entry.description === 'string' ? entry.description : '',
    reversible: entry.reversible === true,
  });
}

function validateEnvelope(
  value: unknown,
  issues: CapabilityBootstrapApprovalEvidenceIssue[],
): readonly CapabilityBootstrapMutationEnvelopeEntry[] {
  const path = '$.approval.mutationEnvelope';
  if (!isSafeArray(value)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Mutation envelope must be a non-Proxy array without accessors.'));
    return [];
  }
  if (value.length > MAX_ENVELOPE) {
    issues.push(issue('INVALID_FIELD', path, `Envelope length must be at most ${MAX_ENVELOPE}.`));
    return [];
  }
  const parsed: CapabilityBootstrapMutationEnvelopeEntry[] = [];
  const seen = new Set<string>();
  value.forEach((entry, index) => {
    const validated = validateEnvelopeEntry(entry, index, issues);
    if (validated === null) return;
    const key = `${validated.kind}:${validated.target}`;
    if (seen.has(key)) {
      issues.push(issue('ENVELOPE_DUPLICATE_ENTRY', `${path}[${index}]`, 'Duplicate envelope kind+target entry.'));
      return;
    }
    seen.add(key);
    parsed.push(validated);
  });
  return Object.freeze(parsed);
}

function validateBoundedText(
  value: unknown,
  path: string,
  maximum: number,
  issues: CapabilityBootstrapApprovalEvidenceIssue[],
): value is string {
  if (typeof value !== 'string' || value.length === 0 || value.length > maximum) {
    issues.push(issue('INVALID_FIELD', path, 'Expected a bounded non-empty string.'));
    return false;
  }
  if (hasControlChars(value)) {
    issues.push(issue('CONTROL_CHARACTER', path, 'Control characters are not allowed.'));
    return false;
  }
  if (hasSecretSignal(value)) {
    issues.push(issue('SECRET_LIKE_CONTENT', path, 'Secret-like content is not allowed.'));
    return false;
  }
  return true;
}

function validatePlanArray(value: unknown, path: string, issues: CapabilityBootstrapApprovalEvidenceIssue[]): value is unknown[] {
  if (!isSafeArray(value)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Plan array must be non-Proxy, dense, and accessor-free.'));
    return false;
  }
  if (value.length > MAX_PLAN_ARRAY) {
    issues.push(issue('INVALID_FIELD', path, `Plan array length must be at most ${MAX_PLAN_ARRAY}.`));
    return false;
  }
  return true;
}

function validateExactPlanShape(plan: Record<string, unknown>, issues: CapabilityBootstrapApprovalEvidenceIssue[]): boolean {
  const startIssueCount = issues.length;
  checkUnknownKeys(plan, PLAN_KEYS, '$.plan', issues);

  validateBoundedId(plan.planId, '$.plan.planId', issues);
  validateBoundedId(plan.dependencyId, '$.plan.dependencyId', issues);
  validateBoundedId(plan.targetVersion, '$.plan.targetVersion', issues);
  validateBoundedId(plan.provenanceRef, '$.plan.provenanceRef', issues);
  validateBoundedText(plan.sourceUri, '$.plan.sourceUri', MAX_SOURCE_URI, issues);
  if (plan.integrityMethod !== 'SHA256' && plan.integrityMethod !== 'SIGNATURE_AND_SHA256') {
    issues.push(issue('INVALID_FIELD', '$.plan.integrityMethod', 'Unsupported integrity method.'));
  }
  if (typeof plan.expectedDigest !== 'string' || !LOWERCASE_SHA256.test(plan.expectedDigest)) {
    issues.push(issue('INVALID_FIELD', '$.plan.expectedDigest', 'Expected digest must be lowercase SHA-256.'));
  }
  if (typeof plan.planDigest !== 'string' || !LOWERCASE_SHA256.test(plan.planDigest)) {
    issues.push(issue('INVALID_FIELD', '$.plan.planDigest', 'Plan digest must be lowercase SHA-256.'));
  }

  if (validatePlanArray(plan.operations, '$.plan.operations', issues)) {
    plan.operations.forEach((candidate, index) => {
      const path = `$.plan.operations[${index}]`;
      if (!isPlainRecord(candidate) || hasAccessorProperties(candidate)) {
        issues.push(issue('MALFORMED_INPUT', path, 'Operation must be a plain non-Proxy object without accessors.'));
        return;
      }
      checkUnknownKeys(candidate, OPERATION_KEYS, path, issues);
      validateBoundedId(candidate.operationId, `${path}.operationId`, issues);
      if (typeof candidate.phase !== 'string' || !OPERATION_PHASES.includes(candidate.phase as typeof OPERATION_PHASES[number])) {
        issues.push(issue('INVALID_FIELD', `${path}.phase`, 'Unsupported operation phase.'));
      }
      if (typeof candidate.action !== 'string' || !ACQUISITION_ACTIONS.includes(candidate.action as typeof ACQUISITION_ACTIONS[number])) {
        issues.push(issue('INVALID_FIELD', `${path}.action`, 'Unsupported acquisition action.'));
      }
      validateBoundedText(candidate.target, `${path}.target`, MAX_STRING, issues);
      if (candidate.networkDestination !== undefined) {
        validateBoundedText(candidate.networkDestination, `${path}.networkDestination`, MAX_STRING, issues);
      }
      if (typeof candidate.requiresPrivilege !== 'boolean') {
        issues.push(issue('INVALID_FIELD', `${path}.requiresPrivilege`, 'Privilege requirement must be boolean.'));
      }
    });
  }

  if (validatePlanArray(plan.intendedMutations, '$.plan.intendedMutations', issues)) {
    const normalized = new Set<string>();
    plan.intendedMutations.forEach((candidate, index) => {
      const path = `$.plan.intendedMutations[${index}]`;
      if (!isPlainRecord(candidate) || hasAccessorProperties(candidate)) {
        issues.push(issue('MALFORMED_INPUT', path, 'Mutation must be a plain non-Proxy object without accessors.'));
        return;
      }
      checkUnknownKeys(candidate, MUTATION_KEYS, path, issues);
      const kindValid = typeof candidate.kind === 'string' && MUTATION_KINDS.includes(candidate.kind as AcquisitionMutationKind);
      if (!kindValid) issues.push(issue('INVALID_FIELD', `${path}.kind`, 'Unsupported mutation kind.'));
      const targetValid = validateBoundedText(candidate.target, `${path}.target`, MAX_STRING, issues);
      if (kindValid && targetValid) {
        const normalizedKey = `${MUTATION_KIND_TO_ENVELOPE_CLASS[candidate.kind as AcquisitionMutationKind]}:${candidate.target}`;
        if (normalized.has(normalizedKey)) {
          issues.push(issue('ENVELOPE_AMBIGUOUS_ENTRY', path, 'Plan mutations collapse to a duplicate approval-envelope entry.'));
        }
        normalized.add(normalizedKey);
      }
    });
  }

  for (const [field, value] of [
    ['rollbackOperationIds', plan.rollbackOperationIds],
    ['verificationOperationIds', plan.verificationOperationIds],
  ] as const) {
    const path = `$.plan.${field}`;
    if (validatePlanArray(value, path, issues)) {
      value.forEach((candidate, index) => validateBoundedId(candidate, `${path}[${index}]`, issues));
    }
  }

  if (validatePlanArray(plan.forbiddenMutationKinds, '$.plan.forbiddenMutationKinds', issues)) {
    plan.forbiddenMutationKinds.forEach((candidate, index) => {
      if (typeof candidate !== 'string' || !MUTATION_KINDS.includes(candidate as AcquisitionMutationKind)) {
        issues.push(issue('INVALID_FIELD', `$.plan.forbiddenMutationKinds[${index}]`, 'Unsupported forbidden mutation kind.'));
      }
    });
  }
  return issues.length === startIssueCount;
}

function validatePlan(
  plan: unknown,
  now: string,
  issues: CapabilityBootstrapApprovalEvidenceIssue[],
): ControlledAcquisitionPlan | null {
  if (!isPlainRecord(plan) || hasAccessorProperties(plan)) {
    issues.push(issue('MALFORMED_INPUT', '$.plan', 'Plan must be a plain non-Proxy object without accessors.'));
    return null;
  }
  if (plan.schemaVersion !== CONTROLLED_ACQUISITION_PLAN_VERSION) {
    issues.push(issue('PLAN_SCHEMA_UNSUPPORTED', '$.plan.schemaVersion', 'Unsupported plan schema.'));
    return null;
  }
  if (!validateExactPlanShape(plan, issues)) return null;
  const typedPlan = plan as unknown as ControlledAcquisitionPlan;
  if (!validUtc(typedPlan.expiresAt) || Date.parse(now) > Date.parse(typedPlan.expiresAt)) {
    issues.push(issue('PLAN_EXPIRED', '$.plan.expiresAt', 'Plan is expired or has an invalid UTC expiry.'));
    return null;
  }
  let recomputedDigest: string;
  try {
    recomputedDigest = computeControlledAcquisitionPlanDigest(typedPlan);
  } catch {
    issues.push(issue('MALFORMED_INPUT', '$.plan', 'Plan digest could not be recomputed from the supplied fields.'));
    return null;
  }
  if (recomputedDigest !== typedPlan.planDigest) {
    issues.push(issue('PLAN_DIGEST_MISMATCH', '$.plan.planDigest', 'Plan digest does not match the recomputed authority projection.'));
    return null;
  }
  const t3Result = evaluateControlledAcquisitionAuthorization(typedPlan, {
    schemaVersion: CONTROLLED_ACQUISITION_APPROVAL_VERSION,
    approvalId: 't8-plan-validation',
    planId: typedPlan.planId,
    planDigest: typedPlan.planDigest,
    decision: 'APPROVED',
    approvedAt: now,
    expiresAt: typedPlan.expiresAt,
  }, now);
  if (t3Result.decision !== 'AUTHORIZED_FOR_SEPARATE_EXECUTOR') {
    for (const t3Issue of t3Result.issues) {
      issues.push(issue('PLAN_T3_REJECTED', t3Issue.path, `Current T3 plan validation rejected the supplied plan (${t3Issue.code}).`));
    }
    return null;
  }
  return typedPlan;
}

function normalizePlanEnvelope(plan: ControlledAcquisitionPlan): ReadonlySet<string> {
  const normalized = new Set<string>();
  for (const mutation of plan.intendedMutations) {
    const envelopeClass = MUTATION_KIND_TO_ENVELOPE_CLASS[mutation.kind];
    normalized.add(`${envelopeClass}:${mutation.target}`);
  }
  return normalized;
}

function buildRejected(issues: readonly CapabilityBootstrapApprovalEvidenceIssue[]): CapabilityBootstrapApprovalEvidenceBindingResult {
  return Object.freeze({
    schemaVersion: CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION,
    disposition: 'REJECTED',
    replayCheckRequired: true,
    approvalIssued: false,
    executionAuthorized: false,
    acquisitionAuthorized: false,
    mutationAuthorized: false,
    taskAuthorityGranted: false,
    networkAuthorized: false,
    issues: Object.freeze([...issues]),
  });
}

export function evaluateCapabilityBootstrapApprovalEvidenceBinding(
  input: unknown,
): CapabilityBootstrapApprovalEvidenceBindingResult {
  if (!isPlainRecord(input) || hasAccessorProperties(input)) {
    return buildRejected([issue('MALFORMED_INPUT', '$', 'Input must be a plain non-Proxy object without accessors.')]);
  }

  const issues: CapabilityBootstrapApprovalEvidenceIssue[] = [];
  checkUnknownKeys(input, INPUT_KEYS, '$', issues);

  const now = typeof input.now === 'string' && validUtc(input.now) ? input.now : null;
  if (now === null) {
    issues.push(issue('INVALID_FIELD', '$.now', 'Current time must be ISO-8601 UTC.'));
  }

  const expectedWorkspaceId = validateBoundedId(input.expectedWorkspaceId, '$.expectedWorkspaceId', issues);
  const expectedActorId = validateBoundedId(input.expectedActorId, '$.expectedActorId', issues);

  let expectedWorkOrderId: string | null | undefined;
  if (input.expectedWorkOrderId === undefined) {
    expectedWorkOrderId = undefined;
  } else if (input.expectedWorkOrderId === null) {
    expectedWorkOrderId = null;
  } else {
    expectedWorkOrderId = validateBoundedId(input.expectedWorkOrderId, '$.expectedWorkOrderId', issues);
  }

  const plan = validatePlan(input.plan, now ?? '1970-01-01T00:00:00Z', issues);

  if (!isPlainRecord(input.approval) || hasAccessorProperties(input.approval)) {
    issues.push(issue('MALFORMED_INPUT', '$.approval', 'Approval must be a plain non-Proxy object without accessors.'));
    return buildRejected(issues);
  }
  const approval = input.approval;
  checkUnknownKeys(approval, APPROVAL_KEYS, '$.approval', issues);

  if (approval.schemaVersion !== CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION) {
    issues.push(issue('APPROVAL_SCHEMA_UNSUPPORTED', '$.approval.schemaVersion', 'Unsupported approval evidence schema.'));
  }

  const approvalId = validateBoundedId(approval.approvalId, '$.approval.approvalId', issues);
  const planIdRef = validateBoundedId(approval.planId, '$.approval.planId', issues);
  const planDigestRef = validateBoundedId(approval.planDigest, '$.approval.planDigest', issues);
  const workspaceId = validateBoundedId(approval.workspaceId, '$.approval.workspaceId', issues);
  const actorId = validateBoundedId(approval.actorId, '$.approval.actorId', issues);
  const replayNonce = validateBoundedId(approval.replayNonce, '$.approval.replayNonce', issues);

  const workOrderId: string | null = approval.workOrderId === null
    ? null
    : validateBoundedId(approval.workOrderId, '$.approval.workOrderId', issues);

  if (approval.decision !== 'APPROVE') {
    issues.push(issue('APPROVAL_NOT_APPROVED', '$.approval.decision', 'Approval decision must be exactly APPROVE.'));
  }

  const issuedAtValid = validUtc(approval.issuedAt);
  if (!issuedAtValid) {
    issues.push(issue('INVALID_FIELD', '$.approval.issuedAt', 'Issued-at must be a valid ISO-8601 UTC timestamp.'));
  }
  const expiresAtValid = validUtc(approval.expiresAt);
  if (!expiresAtValid) {
    issues.push(issue('INVALID_FIELD', '$.approval.expiresAt', 'Expires-at must be a valid ISO-8601 UTC timestamp.'));
  } else if (now !== null && Date.parse(now) > Date.parse(approval.expiresAt as string)) {
    issues.push(issue('APPROVAL_EXPIRED', '$.approval.expiresAt', 'Approval is expired.'));
  }
  if (issuedAtValid && expiresAtValid && Date.parse(approval.expiresAt as string) < Date.parse(approval.issuedAt as string)) {
    issues.push(issue('INVALID_FIELD', '$.approval.expiresAt', 'Expiry must not precede issuance.'));
  }
  if (issuedAtValid && now !== null && Date.parse(approval.issuedAt as string) > Date.parse(now)) {
    issues.push(issue('INVALID_FIELD', '$.approval.issuedAt', 'Approval evidence cannot be issued in the future.'));
  }
  if (plan !== null && expiresAtValid && Date.parse(approval.expiresAt as string) > Date.parse(plan.expiresAt)) {
    issues.push(issue('APPROVAL_EXPIRY_EXCEEDS_PLAN_EXPIRY', '$.approval.expiresAt', 'Approval expiry must not exceed plan expiry.'));
  }

  const envelope = validateEnvelope(approval.mutationEnvelope, issues);

  if (plan !== null && planIdRef !== null && planDigestRef !== null) {
    if (planIdRef !== plan.planId || planDigestRef !== plan.planDigest) {
      issues.push(issue('PLAN_BINDING_MISMATCH', '$.approval', 'Approval is not bound to the exact current plan ID and digest.'));
    }
  }
  if (expectedWorkspaceId !== null && workspaceId !== null && workspaceId !== expectedWorkspaceId) {
    issues.push(issue('WORKSPACE_MISMATCH', '$.approval.workspaceId', 'Approval workspace does not match the expected workspace.'));
  }
  if (expectedActorId !== null && actorId !== null && actorId !== expectedActorId) {
    issues.push(issue('ACTOR_MISMATCH', '$.approval.actorId', 'Approval actor does not match the expected actor.'));
  }
  if (expectedWorkOrderId !== undefined && expectedWorkOrderId !== workOrderId) {
    issues.push(issue('WORK_ORDER_MISMATCH', '$.approval.workOrderId', 'Approval work-order reference does not match the expected work order.'));
  }
  if (typeof approval.replayNonce === 'string' && hasSecretSignal(approval.replayNonce)) {
    issues.push(issue('NONCE_INVALID', '$.approval.replayNonce', 'Replay nonce must not carry secret-like content.'));
  }

  if (plan !== null) {
    const planned = normalizePlanEnvelope(plan);
    const supplied = new Set(envelope.map(({ kind, target }) => `${kind}:${target}`));
    for (const entry of planned) {
      if (!supplied.has(entry)) {
        issues.push(issue('ENVELOPE_MISSING_ENTRY', '$.approval.mutationEnvelope', 'Approval envelope is missing a required planned entry.'));
      }
    }
    for (const entry of supplied) {
      if (!planned.has(entry)) {
        issues.push(issue('ENVELOPE_EXTRA_ENTRY', '$.approval.mutationEnvelope', 'Approval envelope contains an entry outside the planned scope.'));
      }
    }
    const suppliedByTarget = new Map<string, Set<string>>();
    for (const { kind, target } of envelope) {
      const kinds = suppliedByTarget.get(target) ?? new Set<string>();
      kinds.add(kind);
      suppliedByTarget.set(target, kinds);
    }
    for (const [target, kinds] of suppliedByTarget) {
      if (kinds.size > 1) {
        issues.push(issue('ENVELOPE_AMBIGUOUS_ENTRY', '$.approval.mutationEnvelope', 'One envelope target is claimed by more than one class.'));
      }
    }
  }

  if (issues.length > 0) {
    return buildRejected(issues);
  }

  return Object.freeze({
    schemaVersion: CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION,
    disposition: 'VALIDATED_EVIDENCE',
    planId: (plan as ControlledAcquisitionPlan).planId,
    planDigest: (plan as ControlledAcquisitionPlan).planDigest,
    approvalId: approvalId as string,
    workspaceId: workspaceId as string,
    actorId: actorId as string,
    workOrderId,
    replayCheckRequired: true,
    approvalIssued: false,
    executionAuthorized: false,
    acquisitionAuthorized: false,
    mutationAuthorized: false,
    taskAuthorityGranted: false,
    networkAuthorized: false,
    issues: Object.freeze([]),
  });
}
