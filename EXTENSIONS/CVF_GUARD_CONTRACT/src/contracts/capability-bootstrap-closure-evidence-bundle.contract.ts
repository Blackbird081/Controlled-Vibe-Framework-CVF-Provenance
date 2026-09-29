/**
 * Capability bootstrap closure evidence bundle validation kernel.
 *
 * Pure in-memory composition only. This module accepts an unknown
 * caller-supplied bundle of T9 receipt-verification input, T10
 * environment-snapshot-evidence input, and T11 workspace-profile /
 * bootstrap-policy-bundle input, validates the bounded envelope shape,
 * invokes the current T9, T10, and T11 evaluators unchanged with the
 * caller-supplied evidence and time only, binds the shared workspace/plan
 * identity across all three results, and projects one immutable closure
 * disposition. It never loads a file, observes an environment, persists or
 * materializes anything, executes rollback or repair, or grants any action
 * authority; every action-authority output is deliberately false on every
 * return path.
 */

import { isProxy } from 'node:util/types';
import {
  evaluateCapabilityAcquisitionReceiptVerification,
  type CapabilityAcquisitionReceiptVerificationInput,
  type CapabilityAcquisitionReceiptVerificationResult,
} from './capability-acquisition-receipt-verification.contract';
import {
  evaluateCapabilityEnvironmentSnapshotEvidence,
  type CapabilityEnvironmentSnapshotEvidenceInput,
  type CapabilityEnvironmentSnapshotEvidenceResult,
} from './capability-environment-snapshot-evidence.contract';
import {
  evaluateCapabilityWorkspaceBootstrapPolicyBundle,
  type CapabilityWorkspaceBootstrapPolicyBundleInput,
  type CapabilityWorkspaceBootstrapPolicyBundleResult,
} from './capability-workspace-bootstrap-policy-bundle.contract';

export const CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_CONTRACT_VERSION =
  'cvf.capabilityBootstrapClosureEvidenceBundle.v1' as const;
export const CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_RESULT_VERSION =
  'cvf.capabilityBootstrapClosureEvidenceBundleResult.v1' as const;

export interface CapabilityBootstrapClosureEvidenceBundleInput {
  readonly schemaVersion: typeof CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_CONTRACT_VERSION;
  readonly expectedWorkspaceId: string;
  readonly receiptVerification: CapabilityAcquisitionReceiptVerificationInput;
  readonly snapshotEvidence: CapabilityEnvironmentSnapshotEvidenceInput;
  readonly policyBundle: CapabilityWorkspaceBootstrapPolicyBundleInput;
  readonly now: string;
}

export type CapabilityBootstrapClosureEvidenceBundleIssueCode =
  | 'MALFORMED_INPUT'
  | 'UNKNOWN_KEY'
  | 'INVALID_FIELD'
  | 'UNSAFE_STRING'
  | 'RAW_SECRET_DETECTED'
  | 'RECEIPT_VERIFICATION_REJECTED'
  | 'SNAPSHOT_EVIDENCE_REJECTED'
  | 'POLICY_BUNDLE_REJECTED'
  | 'WORKSPACE_BINDING_MISMATCH'
  | 'PLAN_BINDING_MISMATCH'
  | 'SNAPSHOT_BINDING_MISMATCH'
  | 'PROFILE_BINDING_MISMATCH'
  | 'STALE_EVIDENCE_TIME';

export interface CapabilityBootstrapClosureEvidenceBundleIssue {
  readonly code: CapabilityBootstrapClosureEvidenceBundleIssueCode;
  readonly path: string;
  readonly message: string;
}

export type CapabilityBootstrapClosureEvidenceBundleStatus =
  | 'CLOSURE_EVIDENCE_ACCEPTED'
  | 'CLOSURE_EVIDENCE_REJECTED'
  | 'CLOSURE_EVIDENCE_BLOCKED';

export interface CapabilityBootstrapClosureEvidenceBundleResult {
  readonly schemaVersion: typeof CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_RESULT_VERSION;
  readonly closureStatus: CapabilityBootstrapClosureEvidenceBundleStatus;
  readonly workspaceId: string;
  readonly planId: string;
  readonly routeDecisionId: string;
  readonly snapshotId: string;
  readonly selectedProfileId: string;
  readonly policyId: string;
  readonly receiptVerification: CapabilityAcquisitionReceiptVerificationResult | null;
  readonly snapshotEvidence: CapabilityEnvironmentSnapshotEvidenceResult | null;
  readonly policyBundle: CapabilityWorkspaceBootstrapPolicyBundleResult | null;
  readonly issues: readonly CapabilityBootstrapClosureEvidenceBundleIssue[];
  readonly evaluatedAt: string;
  readonly authorityStatus: 'EVIDENCE_ONLY';
  readonly executionAuthorized: false;
  readonly rollbackAuthorized: false;
  readonly materializationAuthorized: false;
  readonly promotionAuthorized: false;
  readonly acquisitionAuthorized: false;
  readonly mutationAuthorized: false;
  readonly networkAuthorized: false;
  readonly taskAuthorityGranted: false;
}

type PlainRecord = Record<string, unknown>;

const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const SECRET_SIGNAL = /(?:\b(?:api[_-]?key|password|token|secret|credential|cookie)\b\s*[=:]\s*\S+|\bbearer\s+\S+|-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----)/i;

const INPUT_KEYS = [
  'schemaVersion', 'expectedWorkspaceId', 'receiptVerification', 'snapshotEvidence', 'policyBundle', 'now',
] as const;

function descriptorRecord(value: unknown): PlainRecord | null {
  if (value === null || typeof value !== 'object' || isProxy(value)) return null;
  let prototype: object | null;
  let descriptors: PropertyDescriptorMap;
  let symbols: symbol[];
  try {
    prototype = Object.getPrototypeOf(value);
    descriptors = Object.getOwnPropertyDescriptors(value);
    symbols = Object.getOwnPropertySymbols(value);
  } catch {
    return null;
  }
  if ((prototype !== Object.prototype && prototype !== null) || symbols.length > 0) return null;
  if (Object.values(descriptors).some((descriptor) => 'get' in descriptor || 'set' in descriptor)) return null;
  return value as PlainRecord;
}

function data(record: PlainRecord, key: string): unknown {
  return Object.getOwnPropertyDescriptor(record, key)?.value;
}

function hasExactKeys(record: PlainRecord, required: readonly string[]): boolean {
  const keys = Object.keys(record);
  return required.every((key) => keys.includes(key))
    && keys.every((key) => required.includes(key));
}

function validUtc(value: unknown): value is string {
  if (typeof value !== 'string') return false;
  const match = ISO_UTC.exec(value);
  if (!match) return false;
  const parsed = Date.parse(value);
  if (!Number.isFinite(parsed)) return false;
  const instant = new Date(parsed);
  const components = value.slice(0, 19).split(/[-T:]/).map(Number);
  return instant.getUTCFullYear() === components[0]
    && instant.getUTCMonth() + 1 === components[1]
    && instant.getUTCDate() === components[2]
    && instant.getUTCHours() === components[3]
    && instant.getUTCMinutes() === components[4]
    && instant.getUTCSeconds() === components[5];
}

function hasSecretSignal(value: string): boolean {
  return SECRET_SIGNAL.test(value);
}

function inspectId(
  value: unknown,
  path: string,
  issues: CapabilityBootstrapClosureEvidenceBundleIssue[],
): value is string {
  if (typeof value !== 'string' || value.length === 0 || value.length > 256) {
    addIssue(issues, 'UNSAFE_STRING', path, 'Value must be a bounded non-empty string.');
    return false;
  }
  if (hasSecretSignal(value)) {
    addIssue(issues, 'RAW_SECRET_DETECTED', path, 'Secret-like material is forbidden.');
    return false;
  }
  if (!SAFE_ID.test(value)) {
    addIssue(issues, 'INVALID_FIELD', path, 'Value must be a bounded safe identifier.');
    return false;
  }
  return true;
}

function addIssue(
  issues: CapabilityBootstrapClosureEvidenceBundleIssue[],
  code: CapabilityBootstrapClosureEvidenceBundleIssueCode,
  path: string,
  message: string,
): void {
  issues.push(Object.freeze({ code, path, message }));
}

function inspectRecord(
  value: unknown,
  path: string,
  required: readonly string[],
  issues: CapabilityBootstrapClosureEvidenceBundleIssue[],
): PlainRecord | null {
  const record = descriptorRecord(value);
  if (!record) {
    addIssue(issues, 'MALFORMED_INPUT', path, 'Value must be a plain non-Proxy data object without accessors or symbols.');
    return null;
  }
  if (!hasExactKeys(record, required)) {
    addIssue(issues, 'UNKNOWN_KEY', path, 'Object keys do not match the bounded contract.');
    return null;
  }
  return record;
}

function freezeIssues(
  issues: CapabilityBootstrapClosureEvidenceBundleIssue[],
): readonly CapabilityBootstrapClosureEvidenceBundleIssue[] {
  return Object.freeze([...issues].sort((left, right) => (
    left.path.localeCompare(right.path)
    || left.code.localeCompare(right.code)
    || left.message.localeCompare(right.message)
  )));
}

function authorityFields() {
  return {
    authorityStatus: 'EVIDENCE_ONLY' as const,
    executionAuthorized: false as const,
    rollbackAuthorized: false as const,
    materializationAuthorized: false as const,
    promotionAuthorized: false as const,
    acquisitionAuthorized: false as const,
    mutationAuthorized: false as const,
    networkAuthorized: false as const,
    taskAuthorityGranted: false as const,
  };
}

function buildResult(
  closureStatus: CapabilityBootstrapClosureEvidenceBundleStatus,
  workspaceId: string,
  planId: string,
  routeDecisionId: string,
  snapshotId: string,
  selectedProfileId: string,
  policyId: string,
  receiptVerification: CapabilityAcquisitionReceiptVerificationResult | null,
  snapshotEvidence: CapabilityEnvironmentSnapshotEvidenceResult | null,
  policyBundle: CapabilityWorkspaceBootstrapPolicyBundleResult | null,
  issues: CapabilityBootstrapClosureEvidenceBundleIssue[],
  evaluatedAt: string,
): CapabilityBootstrapClosureEvidenceBundleResult {
  return Object.freeze({
    schemaVersion: CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_RESULT_VERSION,
    closureStatus,
    workspaceId,
    planId,
    routeDecisionId,
    snapshotId,
    selectedProfileId,
    policyId,
    receiptVerification,
    snapshotEvidence,
    policyBundle,
    issues: freezeIssues(issues),
    evaluatedAt,
    ...authorityFields(),
  });
}

export function evaluateCapabilityBootstrapClosureEvidenceBundle(
  input: unknown,
): CapabilityBootstrapClosureEvidenceBundleResult {
  const issues: CapabilityBootstrapClosureEvidenceBundleIssue[] = [];
  const envelope = inspectRecord(input, '$', INPUT_KEYS, issues);

  if (!envelope) {
    return buildResult('CLOSURE_EVIDENCE_BLOCKED', 'invalid', 'invalid', 'invalid', 'invalid', 'invalid', 'invalid', null, null, null, issues, '1970-01-01T00:00:00Z');
  }

  if (data(envelope, 'schemaVersion') !== CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_CONTRACT_VERSION) {
    addIssue(issues, 'INVALID_FIELD', '$.schemaVersion', 'Unsupported bundle-input version.');
  }
  let nowValue: string | null = null;
  if (validUtc(data(envelope, 'now'))) {
    nowValue = data(envelope, 'now') as string;
  } else {
    addIssue(issues, 'INVALID_FIELD', '$.now', 'Current time must be ISO-8601 UTC.');
  }
  let expectedWorkspaceId: string | null = null;
  if (inspectId(data(envelope, 'expectedWorkspaceId'), '$.expectedWorkspaceId', issues)) {
    expectedWorkspaceId = data(envelope, 'expectedWorkspaceId') as string;
  }

  const receiptVerificationInput = data(envelope, 'receiptVerification');
  const snapshotEvidenceInput = data(envelope, 'snapshotEvidence');
  const policyBundleInput = data(envelope, 'policyBundle');

  const evaluatedAt = nowValue ?? '1970-01-01T00:00:00Z';

  if (
    descriptorRecord(receiptVerificationInput) === null
    || descriptorRecord(snapshotEvidenceInput) === null
    || descriptorRecord(policyBundleInput) === null
  ) {
    if (descriptorRecord(receiptVerificationInput) === null) addIssue(issues, 'MALFORMED_INPUT', '$.receiptVerification', 'Value must be a plain non-Proxy data object without accessors or symbols.');
    if (descriptorRecord(snapshotEvidenceInput) === null) addIssue(issues, 'MALFORMED_INPUT', '$.snapshotEvidence', 'Value must be a plain non-Proxy data object without accessors or symbols.');
    if (descriptorRecord(policyBundleInput) === null) addIssue(issues, 'MALFORMED_INPUT', '$.policyBundle', 'Value must be a plain non-Proxy data object without accessors or symbols.');
    return buildResult('CLOSURE_EVIDENCE_BLOCKED', 'invalid', 'invalid', 'invalid', 'invalid', 'invalid', 'invalid', null, null, null, issues, evaluatedAt);
  }

  const receiptVerification = evaluateCapabilityAcquisitionReceiptVerification(receiptVerificationInput);
  const snapshotEvidence = evaluateCapabilityEnvironmentSnapshotEvidence(snapshotEvidenceInput);
  const policyBundle = evaluateCapabilityWorkspaceBootstrapPolicyBundle(policyBundleInput);

  const receiptRejected = receiptVerification.disposition !== 'VERIFIED_SUCCESS_EVIDENCE';
  const snapshotRejected = snapshotEvidence.status !== 'VALIDATED_READY_EVIDENCE';
  const policyRejected = policyBundle.status !== 'VALIDATED_POLICY_EVIDENCE';

  if (receiptRejected) addIssue(issues, 'RECEIPT_VERIFICATION_REJECTED', '$.receiptVerification', 'Current T9 receipt verification did not return VERIFIED_SUCCESS_EVIDENCE.');
  if (snapshotRejected) addIssue(issues, 'SNAPSHOT_EVIDENCE_REJECTED', '$.snapshotEvidence', 'Current T10 environment-snapshot evidence did not return VALIDATED_READY_EVIDENCE.');
  if (policyRejected) addIssue(issues, 'POLICY_BUNDLE_REJECTED', '$.policyBundle', 'Current T11 workspace bootstrap policy bundle did not return VALIDATED_POLICY_EVIDENCE.');

  const closureBlocked = receiptRejected || snapshotRejected || policyRejected;

  if (expectedWorkspaceId !== null) {
    if (!receiptRejected && receiptVerification.disposition === 'VERIFIED_SUCCESS_EVIDENCE') {
      const receiptWorkspace = (receiptVerificationInput as PlainRecord).expectedWorkspaceId;
      if (receiptWorkspace !== expectedWorkspaceId) {
        addIssue(issues, 'WORKSPACE_BINDING_MISMATCH', '$.receiptVerification.expectedWorkspaceId', 'Receipt-verification workspace does not match the expected workspace.');
      }
    }
    if (!snapshotRejected && snapshotEvidence.workspaceId !== expectedWorkspaceId) {
      addIssue(issues, 'WORKSPACE_BINDING_MISMATCH', '$.snapshotEvidence.workspaceId', 'Snapshot-evidence workspace does not match the expected workspace.');
    }
  }

  let planId = 'invalid';
  if (!receiptRejected && receiptVerification.planId !== undefined) {
    planId = receiptVerification.planId;
  }
  if (!receiptRejected && !snapshotRejected) {
    const receiptPlan = descriptorRecord((receiptVerificationInput as PlainRecord).plan);
    const receiptRecord = descriptorRecord((receiptVerificationInput as PlainRecord).receipt);
    const routeInput = descriptorRecord((snapshotEvidenceInput as PlainRecord).route);
    const routePrimary = routeInput ? descriptorRecord(data(routeInput, 'primary')) : null;
    const planDependencyId = receiptPlan ? data(receiptPlan, 'dependencyId') : undefined;
    const routePackageId = routePrimary ? data(routePrimary, 'packageId') : undefined;
    if (planDependencyId !== undefined && routePackageId !== undefined && planDependencyId !== routePackageId) {
      addIssue(issues, 'PLAN_BINDING_MISMATCH', '$.snapshotEvidence.route.primary.packageId', 'Route primary package does not match the receipt-verified plan dependency.');
    }
    if (receiptRecord && data(receiptRecord, 'refreshedSnapshotId') !== snapshotEvidence.snapshotId) {
      addIssue(issues, 'SNAPSHOT_BINDING_MISMATCH', '$.receiptVerification.receipt.refreshedSnapshotId', 'Receipt refreshed snapshot does not match the validated environment snapshot.');
    }
  }

  if (!snapshotRejected && !policyRejected) {
    const snapshotInputRecord = snapshotEvidenceInput as PlainRecord;
    const snapshotRecord = descriptorRecord(data(snapshotInputRecord, 'snapshot'));
    const platformRecord = snapshotRecord ? descriptorRecord(data(snapshotRecord, 'platform')) : null;
    const networkRecord = snapshotRecord ? descriptorRecord(data(snapshotRecord, 'network')) : null;
    const policyInputRecord = policyBundleInput as PlainRecord;
    if (snapshotRecord && data(snapshotRecord, 'workspaceProfile') !== policyBundle.selectedProfileId) {
      addIssue(issues, 'PROFILE_BINDING_MISMATCH', '$.snapshotEvidence.snapshot.workspaceProfile', 'Snapshot workspace profile does not match the validated policy profile.');
    }
    if (platformRecord && data(platformRecord, 'os') !== data(policyInputRecord, 'observedPlatform')) {
      addIssue(issues, 'PROFILE_BINDING_MISMATCH', '$.policyBundle.observedPlatform', 'Policy observed platform does not match the validated snapshot platform.');
    }
    if (networkRecord && data(networkRecord, 'mode') !== policyBundle.networkMode) {
      addIssue(issues, 'PROFILE_BINDING_MISMATCH', '$.snapshotEvidence.snapshot.network.mode', 'Snapshot network mode does not match the validated policy profile.');
    }
  }

  if (nowValue !== null && !receiptRejected) {
    const receiptInputRecord = receiptVerificationInput as PlainRecord;
    const receiptRecord = descriptorRecord(data(receiptInputRecord, 'receipt'));
    const endedAt = receiptRecord ? data(receiptRecord, 'endedAt') : undefined;
    if (typeof endedAt === 'string' && validUtc(endedAt) && Date.parse(endedAt) > Date.parse(nowValue)) {
      addIssue(issues, 'STALE_EVIDENCE_TIME', '$.receiptVerification.receipt.endedAt', 'Receipt endedAt must not be after the closure evaluation time.');
    }
  }
  if (nowValue !== null && !snapshotRejected) {
    const snapshotInputRecord = snapshotEvidenceInput as PlainRecord;
    if (typeof snapshotInputRecord.now === 'string' && snapshotInputRecord.now !== nowValue) {
      addIssue(issues, 'STALE_EVIDENCE_TIME', '$.snapshotEvidence.now', 'Snapshot-evidence time must equal the closure evaluation time.');
    }
  }
  if (nowValue !== null && !policyRejected) {
    const policyInputRecord = policyBundleInput as PlainRecord;
    if (typeof policyInputRecord.now === 'string' && policyInputRecord.now !== nowValue) {
      addIssue(issues, 'STALE_EVIDENCE_TIME', '$.policyBundle.now', 'Policy-bundle time must equal the closure evaluation time.');
    }
  }

  const routeDecisionId = !snapshotRejected ? snapshotEvidence.routeDecisionId : 'invalid';
  const snapshotId = !snapshotRejected ? snapshotEvidence.snapshotId : 'invalid';
  const workspaceId = !snapshotRejected ? snapshotEvidence.workspaceId : (expectedWorkspaceId ?? 'invalid');
  const selectedProfileId = !policyRejected ? policyBundle.selectedProfileId : 'invalid';
  const policyId = !policyRejected ? policyBundle.policyId : 'invalid';

  if (closureBlocked || issues.length > 0) {
    return buildResult(
      'CLOSURE_EVIDENCE_REJECTED',
      workspaceId,
      planId,
      routeDecisionId,
      snapshotId,
      selectedProfileId,
      policyId,
      receiptVerification,
      snapshotEvidence,
      policyBundle,
      issues,
      evaluatedAt,
    );
  }

  return buildResult(
    'CLOSURE_EVIDENCE_ACCEPTED',
    workspaceId,
    planId,
    routeDecisionId,
    snapshotId,
    selectedProfileId,
    policyId,
    receiptVerification,
    snapshotEvidence,
    policyBundle,
    issues,
    evaluatedAt,
  );
}
