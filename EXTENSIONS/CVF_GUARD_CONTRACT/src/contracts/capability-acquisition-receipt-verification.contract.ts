/**
 * Capability acquisition receipt verification and repair-stop kernel.
 *
 * Pure receipt evidence verification only. This module never persists a
 * receipt, collects evidence, performs acquisition, executes rollback or
 * repair, grants an executor, mutates state, or performs I/O. It composes
 * the current T3 controlled-acquisition plan and the current T8 approval
 * evidence binding evaluator with a strict caller-supplied receipt, and
 * exposes a repair-stop projection, keeping every action-authority literal
 * false on every return path.
 */

import { isProxy } from 'node:util/types';
import {
  evaluateControlledAcquisitionRepair,
} from './controlled-acquisition.contract';
import type {
  AcquisitionMutationKind,
  ControlledAcquisitionPlan,
  ControlledAcquisitionRepairDecision,
  ControlledAcquisitionRepairInput,
} from './controlled-acquisition.contract';
import {
  evaluateCapabilityBootstrapApprovalEvidenceBinding,
} from './capability-bootstrap-approval-evidence.contract';
import type {
  CapabilityBootstrapApprovalEvidence,
} from './capability-bootstrap-approval-evidence.contract';

export const CAPABILITY_ACQUISITION_RECEIPT_VERIFICATION_CONTRACT_VERSION =
  'cvf.capabilityAcquisitionReceiptVerificationContract.v1' as const;
export const CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION =
  'cvf.capabilityAcquisitionReceipt.v1' as const;
export const CAPABILITY_ACQUISITION_RECEIPT_VERIFICATION_RESULT_VERSION =
  'cvf.capabilityAcquisitionReceiptVerificationResult.v1' as const;

export type CapabilityAcquisitionReceiptOperationStatus = 'SUCCESS' | 'FAILED' | 'SKIPPED' | 'BLOCKED';
export type CapabilityAcquisitionReceiptRollbackStatus = 'NOT_REQUIRED' | 'READY' | 'EXECUTED' | 'FAILED' | 'UNAVAILABLE';
export type CapabilityAcquisitionReceiptVerificationStatus = 'PASS' | 'FAIL' | 'UNKNOWN';

export interface CapabilityAcquisitionReceiptOperationResult {
  readonly operationId: string;
  readonly status: CapabilityAcquisitionReceiptOperationStatus;
}

export interface CapabilityAcquisitionReceiptMutation {
  readonly kind: 'FILESYSTEM' | 'REGISTRY' | 'ENVIRONMENT' | 'PROCESS' | 'SERVICE' | 'NETWORK' | 'PACKAGE' | 'GIT' | 'OTHER';
  readonly target: string;
  readonly description: string;
  readonly reversible: boolean;
}

export interface CapabilityAcquisitionReceiptArtifact {
  readonly path: string;
  readonly version: string;
  readonly digest: string;
}

export interface CapabilityAcquisitionReceiptVerification {
  readonly status: CapabilityAcquisitionReceiptVerificationStatus;
  readonly checks: readonly string[];
}

export interface CapabilityAcquisitionReceipt {
  readonly schemaVersion: typeof CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION;
  readonly receiptId: string;
  readonly planId: string;
  readonly planDigest: string;
  readonly approvalId: string;
  readonly executorId: string;
  readonly startedAt: string;
  readonly endedAt: string;
  readonly operationResults: readonly CapabilityAcquisitionReceiptOperationResult[];
  readonly actualMutations: readonly CapabilityAcquisitionReceiptMutation[];
  readonly artifact: CapabilityAcquisitionReceiptArtifact;
  readonly verification: CapabilityAcquisitionReceiptVerification;
  readonly deviations: readonly string[];
  readonly rollbackStatus: CapabilityAcquisitionReceiptRollbackStatus;
  readonly refreshedSnapshotId: string;
  readonly evidenceRefs: readonly string[];
}

export interface CapabilityAcquisitionReceiptVerificationInput {
  readonly plan: ControlledAcquisitionPlan;
  readonly approval: CapabilityBootstrapApprovalEvidence;
  readonly expectedWorkspaceId: string;
  readonly expectedActorId: string;
  readonly expectedWorkOrderId?: string | null;
  readonly receipt: CapabilityAcquisitionReceipt;
  readonly repair?: ControlledAcquisitionRepairInput;
}

export type CapabilityAcquisitionReceiptVerificationIssueCode =
  | 'MALFORMED_INPUT' | 'UNKNOWN_KEYS' | 'INVALID_FIELD' | 'CONTROL_CHARACTER'
  | 'SECRET_LIKE_CONTENT' | 'NON_LOWERCASE_DIGEST'
  | 'APPROVAL_EVIDENCE_REJECTED'
  | 'RECEIPT_SCHEMA_UNSUPPORTED' | 'RECEIPT_BINDING_MISMATCH'
  | 'TIMESTAMP_ORDER_INVALID'
  | 'OPERATION_MISSING' | 'OPERATION_EXTRA' | 'OPERATION_DUPLICATE' | 'OPERATION_NOT_SUCCESSFUL'
  | 'MUTATION_MISSING' | 'MUTATION_EXTRA' | 'MUTATION_DUPLICATE' | 'MUTATION_AMBIGUOUS'
  | 'ARTIFACT_VERSION_MISMATCH' | 'ARTIFACT_DIGEST_MISMATCH' | 'ARTIFACT_DIGEST_INVALID'
  | 'VERIFICATION_NOT_PASSED' | 'DEVIATION_PRESENT'
  | 'ROLLBACK_STATE_UNSAFE' | 'SNAPSHOT_ID_INVALID' | 'EVIDENCE_REFS_MISSING';

export interface CapabilityAcquisitionReceiptVerificationIssue {
  readonly code: CapabilityAcquisitionReceiptVerificationIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface CapabilityAcquisitionReceiptVerificationResult {
  readonly schemaVersion: typeof CAPABILITY_ACQUISITION_RECEIPT_VERIFICATION_RESULT_VERSION;
  readonly disposition: 'VERIFIED_SUCCESS_EVIDENCE' | 'REJECTED';
  readonly receiptId?: string;
  readonly planId?: string;
  readonly planDigest?: string;
  readonly approvalId?: string;
  readonly executorId?: string;
  readonly artifactDigest?: string;
  readonly repairProjection?: ControlledAcquisitionRepairDecision;
  readonly receiptPersisted: false;
  readonly executionAuthorized: false;
  readonly acquisitionAuthorized: false;
  readonly mutationAuthorized: false;
  readonly repairAuthorized: false;
  readonly rollbackAuthorized: false;
  readonly taskAuthorityGranted: false;
  readonly networkAuthorized: false;
  readonly issues: readonly CapabilityAcquisitionReceiptVerificationIssue[];
}

const MAX_STRING = 256;
const MAX_ARRAY = 64;

const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const LOWERCASE_SHA256 = /^[a-f0-9]{64}$/;
const SHA256_DIGEST_CASE_INSENSITIVE = /^[0-9a-fA-F]{64}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const CONTROL_CHAR = /[\u0000-\u001F\u007F]/;
const SECRET_SIGNAL = /(?:\b(?:api[_-]?key|password|token|secret|credential|cookie)\b\s*[=:]\s*\S+|\bbearer\s+\S+|-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----)/i;

const OPERATION_STATUSES: readonly CapabilityAcquisitionReceiptOperationStatus[] = ['SUCCESS', 'FAILED', 'SKIPPED', 'BLOCKED'];
const ROLLBACK_STATUSES: readonly CapabilityAcquisitionReceiptRollbackStatus[] = ['NOT_REQUIRED', 'READY', 'EXECUTED', 'FAILED', 'UNAVAILABLE'];
const ALLOWED_ROLLBACK_STATUSES: readonly CapabilityAcquisitionReceiptRollbackStatus[] = ['NOT_REQUIRED', 'READY'];
const VERIFICATION_STATUSES: readonly CapabilityAcquisitionReceiptVerificationStatus[] = ['PASS', 'FAIL', 'UNKNOWN'];
const MUTATION_CLASSES = ['FILESYSTEM', 'REGISTRY', 'ENVIRONMENT', 'PROCESS', 'SERVICE', 'NETWORK', 'PACKAGE', 'GIT', 'OTHER'] as const;

const MUTATION_KIND_TO_ENVELOPE_CLASS: Readonly<Record<AcquisitionMutationKind, typeof MUTATION_CLASSES[number]>> = {
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

const INPUT_KEYS: readonly string[] = [
  'plan', 'approval', 'expectedWorkspaceId', 'expectedActorId', 'expectedWorkOrderId', 'receipt', 'repair',
];
const RECEIPT_KEYS: readonly string[] = [
  'schemaVersion', 'receiptId', 'planId', 'planDigest', 'approvalId', 'executorId', 'startedAt', 'endedAt',
  'operationResults', 'actualMutations', 'artifact', 'verification', 'deviations', 'rollbackStatus',
  'refreshedSnapshotId', 'evidenceRefs',
];
const OPERATION_RESULT_KEYS: readonly string[] = ['operationId', 'status'];
const MUTATION_KEYS: readonly string[] = ['kind', 'target', 'description', 'reversible'];
const ARTIFACT_KEYS: readonly string[] = ['path', 'version', 'digest'];
const VERIFICATION_KEYS: readonly string[] = ['status', 'checks'];
const REPAIR_KEYS: readonly string[] = [
  'failedRepairRounds', 'newRootCauseEvidence', 'goalUnchanged', 'dependencyUnchanged', 'riskUnchanged',
  'credentialScopeUnchanged', 'networkDestinationsUnchanged', 'mutationEnvelopeUnchanged',
];

function issue(
  code: CapabilityAcquisitionReceiptVerificationIssueCode,
  path: string,
  message: string,
): CapabilityAcquisitionReceiptVerificationIssue {
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
  if (
    !Array.isArray(value)
    || isProxy(value)
    || Object.getPrototypeOf(value) !== Array.prototype
    || hasAccessorProperties(value)
  ) return false;
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
  issues: CapabilityAcquisitionReceiptVerificationIssue[],
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
  issues: CapabilityAcquisitionReceiptVerificationIssue[],
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

function validateBoundedText(
  value: unknown,
  path: string,
  issues: CapabilityAcquisitionReceiptVerificationIssue[],
): value is string {
  if (typeof value !== 'string' || value.length === 0 || value.length > MAX_STRING) {
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

function validateBoundedArray(
  value: unknown,
  path: string,
  issues: CapabilityAcquisitionReceiptVerificationIssue[],
): value is unknown[] {
  if (!isSafeArray(value)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Expected a non-Proxy dense array without accessors.'));
    return false;
  }
  if (value.length > MAX_ARRAY) {
    issues.push(issue('INVALID_FIELD', path, `Array length must be at most ${MAX_ARRAY}.`));
    return false;
  }
  return true;
}

function normalizePlanEnvelope(plan: ControlledAcquisitionPlan): ReadonlySet<string> {
  const normalized = new Set<string>();
  for (const mutation of plan.intendedMutations) {
    normalized.add(`${MUTATION_KIND_TO_ENVELOPE_CLASS[mutation.kind]}:${mutation.target}`);
  }
  return normalized;
}

function validateReceiptShape(
  receipt: unknown,
  issues: CapabilityAcquisitionReceiptVerificationIssue[],
): CapabilityAcquisitionReceipt | null {
  if (!isPlainRecord(receipt) || hasAccessorProperties(receipt)) {
    issues.push(issue('MALFORMED_INPUT', '$.receipt', 'Receipt must be a plain non-Proxy object without accessors.'));
    return null;
  }
  const startIssueCount = issues.length;
  checkUnknownKeys(receipt, RECEIPT_KEYS, '$.receipt', issues);

  if (receipt.schemaVersion !== CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION) {
    issues.push(issue('RECEIPT_SCHEMA_UNSUPPORTED', '$.receipt.schemaVersion', 'Unsupported receipt schema.'));
  }
  validateBoundedId(receipt.receiptId, '$.receipt.receiptId', issues);
  validateBoundedId(receipt.planId, '$.receipt.planId', issues);
  validateBoundedId(receipt.planDigest, '$.receipt.planDigest', issues);
  validateBoundedId(receipt.approvalId, '$.receipt.approvalId', issues);
  validateBoundedId(receipt.executorId, '$.receipt.executorId', issues);

  const startedAtValid = validUtc(receipt.startedAt);
  if (!startedAtValid) issues.push(issue('INVALID_FIELD', '$.receipt.startedAt', 'startedAt must be a valid ISO-8601 UTC timestamp.'));
  const endedAtValid = validUtc(receipt.endedAt);
  if (!endedAtValid) issues.push(issue('INVALID_FIELD', '$.receipt.endedAt', 'endedAt must be a valid ISO-8601 UTC timestamp.'));
  if (startedAtValid && endedAtValid && Date.parse(receipt.endedAt as string) < Date.parse(receipt.startedAt as string)) {
    issues.push(issue('TIMESTAMP_ORDER_INVALID', '$.receipt.endedAt', 'endedAt must not precede startedAt.'));
  }

  const operationResults: CapabilityAcquisitionReceiptOperationResult[] = [];
  if (validateBoundedArray(receipt.operationResults, '$.receipt.operationResults', issues)) {
    const seenOps = new Set<string>();
    (receipt.operationResults as unknown[]).forEach((candidate, index) => {
      const path = `$.receipt.operationResults[${index}]`;
      if (!isPlainRecord(candidate) || hasAccessorProperties(candidate)) {
        issues.push(issue('MALFORMED_INPUT', path, 'Operation result must be a plain non-Proxy object without accessors.'));
        return;
      }
      checkUnknownKeys(candidate, OPERATION_RESULT_KEYS, path, issues);
      const operationId = validateBoundedId(candidate.operationId, `${path}.operationId`, issues);
      const statusValid = typeof candidate.status === 'string' && OPERATION_STATUSES.includes(candidate.status as CapabilityAcquisitionReceiptOperationStatus);
      if (!statusValid) issues.push(issue('INVALID_FIELD', `${path}.status`, 'Unsupported operation status.'));
      if (operationId === null || !statusValid) return;
      if (seenOps.has(operationId)) {
        issues.push(issue('OPERATION_DUPLICATE', path, 'Duplicate operation result entry.'));
        return;
      }
      seenOps.add(operationId);
      operationResults.push(Object.freeze({ operationId, status: candidate.status as CapabilityAcquisitionReceiptOperationStatus }));
    });
  }

  const actualMutations: CapabilityAcquisitionReceiptMutation[] = [];
  if (validateBoundedArray(receipt.actualMutations, '$.receipt.actualMutations', issues)) {
    const seenMutations = new Set<string>();
    (receipt.actualMutations as unknown[]).forEach((candidate, index) => {
      const path = `$.receipt.actualMutations[${index}]`;
      if (!isPlainRecord(candidate) || hasAccessorProperties(candidate)) {
        issues.push(issue('MALFORMED_INPUT', path, 'Mutation must be a plain non-Proxy object without accessors.'));
        return;
      }
      checkUnknownKeys(candidate, MUTATION_KEYS, path, issues);
      const kindValid = typeof candidate.kind === 'string' && (MUTATION_CLASSES as readonly string[]).includes(candidate.kind);
      if (!kindValid) issues.push(issue('INVALID_FIELD', `${path}.kind`, 'Unsupported mutation class.'));
      const target = validateBoundedId(candidate.target, `${path}.target`, issues);
      let descriptionValid = true;
      if (typeof candidate.description !== 'string' || candidate.description.length === 0 || candidate.description.length > MAX_STRING) {
        issues.push(issue('INVALID_FIELD', `${path}.description`, 'Description must be a bounded non-empty string.'));
        descriptionValid = false;
      } else if (hasControlChars(candidate.description)) {
        issues.push(issue('CONTROL_CHARACTER', `${path}.description`, 'Control characters are not allowed.'));
        descriptionValid = false;
      } else if (hasSecretSignal(candidate.description)) {
        issues.push(issue('SECRET_LIKE_CONTENT', `${path}.description`, 'Secret-like content is not allowed.'));
        descriptionValid = false;
      }
      if (typeof candidate.reversible !== 'boolean') {
        issues.push(issue('INVALID_FIELD', `${path}.reversible`, 'Reversible must be a boolean.'));
      }
      if (!kindValid || target === null || !descriptionValid || typeof candidate.reversible !== 'boolean') return;
      const key = `${candidate.kind}:${target}`;
      if (seenMutations.has(key)) {
        issues.push(issue('MUTATION_DUPLICATE', path, 'Duplicate mutation kind+target entry.'));
        return;
      }
      seenMutations.add(key);
      actualMutations.push(Object.freeze({
        kind: candidate.kind as typeof MUTATION_CLASSES[number],
        target,
        description: candidate.description as string,
        reversible: candidate.reversible,
      }));
    });
  }

  let artifact: CapabilityAcquisitionReceiptArtifact | null = null;
  if (!isPlainRecord(receipt.artifact) || hasAccessorProperties(receipt.artifact)) {
    issues.push(issue('MALFORMED_INPUT', '$.receipt.artifact', 'Artifact must be a plain non-Proxy object without accessors.'));
  } else {
    const artifactRecord = receipt.artifact;
    checkUnknownKeys(artifactRecord, ARTIFACT_KEYS, '$.receipt.artifact', issues);
    const pathValid = validateBoundedText(artifactRecord.path, '$.receipt.artifact.path', issues);
    const versionValid = validateBoundedId(artifactRecord.version, '$.receipt.artifact.version', issues);
    let digestValid = false;
    if (typeof artifactRecord.digest !== 'string' || !LOWERCASE_SHA256.test(artifactRecord.digest)) {
      issues.push(issue('ARTIFACT_DIGEST_INVALID', '$.receipt.artifact.digest', 'Artifact digest must be a lowercase SHA-256 value.'));
    } else {
      digestValid = true;
    }
    if (pathValid && versionValid !== null && digestValid) {
      artifact = Object.freeze({
        path: artifactRecord.path as string,
        version: versionValid,
        digest: artifactRecord.digest as string,
      });
    }
  }

  let verification: CapabilityAcquisitionReceiptVerification | null = null;
  if (!isPlainRecord(receipt.verification) || hasAccessorProperties(receipt.verification)) {
    issues.push(issue('MALFORMED_INPUT', '$.receipt.verification', 'Verification must be a plain non-Proxy object without accessors.'));
  } else {
    const verificationRecord = receipt.verification;
    checkUnknownKeys(verificationRecord, VERIFICATION_KEYS, '$.receipt.verification', issues);
    const statusValid = typeof verificationRecord.status === 'string' && VERIFICATION_STATUSES.includes(verificationRecord.status as CapabilityAcquisitionReceiptVerificationStatus);
    if (!statusValid) issues.push(issue('INVALID_FIELD', '$.receipt.verification.status', 'Unsupported verification status.'));
    const checks: string[] = [];
    if (validateBoundedArray(verificationRecord.checks, '$.receipt.verification.checks', issues)) {
      (verificationRecord.checks as unknown[]).forEach((candidate, index) => {
        if (validateBoundedText(candidate, `$.receipt.verification.checks[${index}]`, issues)) checks.push(candidate);
      });
    }
    if (statusValid) {
      verification = Object.freeze({
        status: verificationRecord.status as CapabilityAcquisitionReceiptVerificationStatus,
        checks: Object.freeze(checks),
      });
    }
    if (verificationRecord.status !== 'PASS') {
      issues.push(issue('VERIFICATION_NOT_PASSED', '$.receipt.verification.status', 'Receipt verification status must be PASS for verified success evidence.'));
    }
  }

  const deviations: string[] = [];
  if (validateBoundedArray(receipt.deviations, '$.receipt.deviations', issues)) {
    (receipt.deviations as unknown[]).forEach((candidate, index) => {
      if (validateBoundedText(candidate, `$.receipt.deviations[${index}]`, issues)) deviations.push(candidate);
    });
    if (deviations.length > 0) {
      issues.push(issue('DEVIATION_PRESENT', '$.receipt.deviations', 'Receipt reports at least one deviation.'));
    }
  }

  const rollbackStatusValid = typeof receipt.rollbackStatus === 'string' && ROLLBACK_STATUSES.includes(receipt.rollbackStatus as CapabilityAcquisitionReceiptRollbackStatus);
  if (!rollbackStatusValid) {
    issues.push(issue('INVALID_FIELD', '$.receipt.rollbackStatus', 'Unsupported rollback status.'));
  } else if (!ALLOWED_ROLLBACK_STATUSES.includes(receipt.rollbackStatus as CapabilityAcquisitionReceiptRollbackStatus)) {
    issues.push(issue('ROLLBACK_STATE_UNSAFE', '$.receipt.rollbackStatus', 'Rollback status must be NOT_REQUIRED or READY for verified success evidence.'));
  }

  const refreshedSnapshotId = validateBoundedId(receipt.refreshedSnapshotId, '$.receipt.refreshedSnapshotId', issues);
  if (refreshedSnapshotId === null) {
    issues.push(issue('SNAPSHOT_ID_INVALID', '$.receipt.refreshedSnapshotId', 'A bounded refreshed snapshot ID is required.'));
  }

  const evidenceRefs: string[] = [];
  if (validateBoundedArray(receipt.evidenceRefs, '$.receipt.evidenceRefs', issues)) {
    (receipt.evidenceRefs as unknown[]).forEach((candidate, index) => {
      if (validateBoundedText(candidate, `$.receipt.evidenceRefs[${index}]`, issues)) evidenceRefs.push(candidate);
    });
    if (evidenceRefs.length === 0) {
      issues.push(issue('EVIDENCE_REFS_MISSING', '$.receipt.evidenceRefs', 'At least one bounded evidence reference is required.'));
    }
  }

  if (issues.length !== startIssueCount || artifact === null || verification === null || !startedAtValid || !endedAtValid) {
    return null;
  }

  return Object.freeze({
    schemaVersion: CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION,
    receiptId: receipt.receiptId as string,
    planId: receipt.planId as string,
    planDigest: receipt.planDigest as string,
    approvalId: receipt.approvalId as string,
    executorId: receipt.executorId as string,
    startedAt: receipt.startedAt as string,
    endedAt: receipt.endedAt as string,
    operationResults: Object.freeze(operationResults),
    actualMutations: Object.freeze(actualMutations),
    artifact,
    verification,
    deviations: Object.freeze(deviations),
    rollbackStatus: receipt.rollbackStatus as CapabilityAcquisitionReceiptRollbackStatus,
    refreshedSnapshotId: refreshedSnapshotId as string,
    evidenceRefs: Object.freeze(evidenceRefs),
  });
}

function buildRejected(issues: readonly CapabilityAcquisitionReceiptVerificationIssue[]): CapabilityAcquisitionReceiptVerificationResult {
  return Object.freeze({
    schemaVersion: CAPABILITY_ACQUISITION_RECEIPT_VERIFICATION_RESULT_VERSION,
    disposition: 'REJECTED',
    receiptPersisted: false,
    executionAuthorized: false,
    acquisitionAuthorized: false,
    mutationAuthorized: false,
    repairAuthorized: false,
    rollbackAuthorized: false,
    taskAuthorityGranted: false,
    networkAuthorized: false,
    issues: Object.freeze([...issues]),
  });
}

function computeRepairProjection(repair: unknown, issues: CapabilityAcquisitionReceiptVerificationIssue[]): ControlledAcquisitionRepairDecision | undefined {
  if (repair === undefined) return undefined;
  if (!isPlainRecord(repair) || hasAccessorProperties(repair)) {
    issues.push(issue('MALFORMED_INPUT', '$.repair', 'Repair input must be a plain non-Proxy object without accessors.'));
    return undefined;
  }
  checkUnknownKeys(repair, REPAIR_KEYS, '$.repair', issues);
  const booleanFields = [
    'newRootCauseEvidence', 'goalUnchanged', 'dependencyUnchanged', 'riskUnchanged',
    'credentialScopeUnchanged', 'networkDestinationsUnchanged', 'mutationEnvelopeUnchanged',
  ] as const;
  let valid = true;
  for (const field of booleanFields) {
    if (typeof repair[field] !== 'boolean') {
      issues.push(issue('INVALID_FIELD', `$.repair.${field}`, `${field} must be a boolean.`));
      valid = false;
    }
  }
  if (!Number.isSafeInteger(repair.failedRepairRounds) || (repair.failedRepairRounds as number) < 0) {
    issues.push(issue('INVALID_FIELD', '$.repair.failedRepairRounds', 'failedRepairRounds must be a non-negative safe integer.'));
    valid = false;
  }
  if (!valid) return undefined;
  return evaluateControlledAcquisitionRepair(repair as unknown as ControlledAcquisitionRepairInput);
}

export function evaluateCapabilityAcquisitionReceiptVerification(
  input: unknown,
): CapabilityAcquisitionReceiptVerificationResult {
  if (!isPlainRecord(input) || hasAccessorProperties(input)) {
    return buildRejected([issue('MALFORMED_INPUT', '$', 'Input must be a plain non-Proxy object without accessors.')]);
  }

  const issues: CapabilityAcquisitionReceiptVerificationIssue[] = [];
  checkUnknownKeys(input, INPUT_KEYS, '$', issues);

  const receipt = validateReceiptShape(input.receipt, issues);
  const repairProjection = computeRepairProjection(input.repair, issues);

  if (receipt === null) {
    return buildRejected(issues);
  }

  const approvalResult = evaluateCapabilityBootstrapApprovalEvidenceBinding({
    plan: input.plan,
    approval: input.approval,
    expectedWorkspaceId: input.expectedWorkspaceId,
    expectedActorId: input.expectedActorId,
    ...(input.expectedWorkOrderId !== undefined ? { expectedWorkOrderId: input.expectedWorkOrderId } : {}),
    now: receipt.startedAt,
  });

  if (approvalResult.disposition !== 'VALIDATED_EVIDENCE') {
    issues.push(issue('APPROVAL_EVIDENCE_REJECTED', '$.approval', 'Current T8 approval evidence binding rejected the supplied plan/approval.'));
    return buildRejected(issues);
  }

  const plan = input.plan as ControlledAcquisitionPlan;

  if (
    receipt.planId !== approvalResult.planId
    || receipt.planDigest !== approvalResult.planDigest
    || receipt.approvalId !== approvalResult.approvalId
  ) {
    issues.push(issue('RECEIPT_BINDING_MISMATCH', '$.receipt', 'Receipt is not bound to the exact validated plan and approval.'));
  }

  const mandatoryOperations = plan.operations.filter(({ phase }) => phase !== 'ROLLBACK').map(({ operationId }) => operationId);
  const mandatorySet = new Set(mandatoryOperations);
  const suppliedOperationIds = new Set(receipt.operationResults.map(({ operationId }) => operationId));
  for (const operationId of mandatorySet) {
    const result = receipt.operationResults.find((entry) => entry.operationId === operationId);
    if (result === undefined) {
      issues.push(issue('OPERATION_MISSING', '$.receipt.operationResults', `Missing required operation result for ${operationId}.`));
    } else if (result.status !== 'SUCCESS') {
      issues.push(issue('OPERATION_NOT_SUCCESSFUL', '$.receipt.operationResults', `Operation ${operationId} did not report SUCCESS.`));
    }
  }
  for (const operationId of suppliedOperationIds) {
    if (!mandatorySet.has(operationId)) {
      issues.push(issue('OPERATION_EXTRA', '$.receipt.operationResults', `Operation result ${operationId} is outside the plan's non-rollback operations.`));
    }
  }

  const plannedMutations = normalizePlanEnvelope(plan);
  const suppliedMutations = new Set(receipt.actualMutations.map(({ kind, target }) => `${kind}:${target}`));
  for (const entry of plannedMutations) {
    if (!suppliedMutations.has(entry)) {
      issues.push(issue('MUTATION_MISSING', '$.receipt.actualMutations', 'Receipt is missing a required planned mutation.'));
    }
  }
  for (const entry of suppliedMutations) {
    if (!plannedMutations.has(entry)) {
      issues.push(issue('MUTATION_EXTRA', '$.receipt.actualMutations', 'Receipt reports a mutation outside the planned scope.'));
    }
  }
  const mutationTargets = new Map<string, Set<string>>();
  for (const { kind, target } of receipt.actualMutations) {
    const kinds = mutationTargets.get(target) ?? new Set<string>();
    kinds.add(kind);
    mutationTargets.set(target, kinds);
  }
  for (const kinds of mutationTargets.values()) {
    if (kinds.size > 1) {
      issues.push(issue('MUTATION_AMBIGUOUS', '$.receipt.actualMutations', 'One mutation target is claimed by more than one class.'));
    }
  }

  // Plan schema/digest authenticity was already fail-closed verified inside
  // evaluateCapabilityBootstrapApprovalEvidenceBinding above (current T8
  // owner), which recomputes the plan digest via the current T3 owner
  // function before returning VALIDATED_EVIDENCE. Only the receipt's
  // observed artifact digest against that authenticated plan's expected
  // digest remains to be checked here.
  if (receipt.artifact.digest !== plan.expectedDigest) {
    issues.push(issue('ARTIFACT_DIGEST_MISMATCH', '$.receipt.artifact.digest', 'Artifact digest does not equal the plan expected digest.'));
  }
  if (receipt.artifact.version !== plan.targetVersion) {
    issues.push(issue('ARTIFACT_VERSION_MISMATCH', '$.receipt.artifact.version', 'Artifact version does not equal the authenticated plan target version.'));
  }

  if (issues.length > 0) {
    return buildRejected(issues);
  }

  return Object.freeze({
    schemaVersion: CAPABILITY_ACQUISITION_RECEIPT_VERIFICATION_RESULT_VERSION,
    disposition: 'VERIFIED_SUCCESS_EVIDENCE',
    receiptId: receipt.receiptId,
    planId: receipt.planId,
    planDigest: receipt.planDigest,
    approvalId: receipt.approvalId,
    executorId: receipt.executorId,
    artifactDigest: receipt.artifact.digest,
    ...(repairProjection !== undefined ? { repairProjection } : {}),
    receiptPersisted: false,
    executionAuthorized: false,
    acquisitionAuthorized: false,
    mutationAuthorized: false,
    repairAuthorized: false,
    rollbackAuthorized: false,
    taskAuthorityGranted: false,
    networkAuthorized: false,
    issues: Object.freeze([]),
  });
}
