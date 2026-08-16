/**
 * CVF controlled-acquisition authorization kernel.
 *
 * Pure decision/evidence logic only: this module never downloads, installs,
 * executes, mutates, rolls back, reads secrets, or grants authority beyond a
 * validated plan/approval pair being eligible for a separately governed
 * executor.
 */

import { createHash } from 'node:crypto';
import { isProxy } from 'node:util/types';

export const CONTROLLED_ACQUISITION_CONTRACT_VERSION = 'cvf.controlledAcquisition.v1' as const;
export const CONTROLLED_ACQUISITION_PLAN_VERSION = 'cvf.controlledAcquisitionPlan.v1' as const;
export const CONTROLLED_ACQUISITION_APPROVAL_VERSION = 'cvf.controlledAcquisitionApproval.v1' as const;
export const CONTROLLED_ACQUISITION_RECEIPT_VERSION = 'cvf.controlledAcquisitionReceipt.v1' as const;

export type AcquisitionOperationPhase = 'ACQUIRE' | 'ROLLBACK' | 'VERIFY';
export type AcquisitionAction =
  | 'DOWNLOAD' | 'INSTALL' | 'UPDATE' | 'REMOVE'
  | 'WRITE_ENV' | 'WRITE_PATH' | 'WRITE_SERVICE'
  | 'GIT_MUTATION' | 'BIND_CREDENTIAL' | 'VERIFY' | 'ROLLBACK';
export type AcquisitionMutationKind =
  | 'WORKSPACE_FILE' | 'USER_FILE' | 'SYSTEM_FILE' | 'ENVIRONMENT'
  | 'PATH' | 'REGISTRY' | 'SERVICE' | 'PROCESS' | 'GIT' | 'CREDENTIAL_BINDING';

export interface ControlledAcquisitionOperation {
  readonly operationId: string;
  readonly phase: AcquisitionOperationPhase;
  readonly action: AcquisitionAction;
  readonly target: string;
  readonly networkDestination?: string;
  readonly requiresPrivilege: boolean;
}

export interface ControlledAcquisitionMutation {
  readonly kind: AcquisitionMutationKind;
  readonly target: string;
}

export interface ControlledAcquisitionPlan {
  readonly schemaVersion: typeof CONTROLLED_ACQUISITION_PLAN_VERSION;
  readonly planId: string;
  readonly dependencyId: string;
  readonly targetVersion: string;
  readonly sourceUri: string;
  readonly provenanceRef: string;
  readonly integrityMethod: 'SHA256' | 'SIGNATURE_AND_SHA256';
  readonly expectedDigest: string;
  readonly operations: readonly ControlledAcquisitionOperation[];
  readonly intendedMutations: readonly ControlledAcquisitionMutation[];
  readonly rollbackOperationIds: readonly string[];
  readonly verificationOperationIds: readonly string[];
  readonly forbiddenMutationKinds: readonly AcquisitionMutationKind[];
  readonly expiresAt: string;
  readonly planDigest: string;
}

export interface ControlledAcquisitionApproval {
  readonly schemaVersion: typeof CONTROLLED_ACQUISITION_APPROVAL_VERSION;
  readonly approvalId: string;
  readonly planId: string;
  readonly planDigest: string;
  readonly decision: 'APPROVED' | 'DENIED';
  readonly approvedAt: string;
  readonly expiresAt: string;
}

export type ControlledAcquisitionIssueCode =
  | 'MALFORMED_INPUT' | 'INVALID_FIELD' | 'RAW_SECRET_INCLUDED'
  | 'PLAN_DIGEST_MISMATCH' | 'APPROVAL_MISMATCH' | 'APPROVAL_DENIED'
  | 'PLAN_EXPIRED' | 'APPROVAL_EXPIRED' | 'UNSAFE_SOURCE'
  | 'INTEGRITY_EVIDENCE_MISSING' | 'ROLLBACK_INCOMPLETE'
  | 'VERIFICATION_INCOMPLETE' | 'FORBIDDEN_MUTATION_PLANNED'
  | 'OPERATION_ID_DUPLICATE' | 'RECEIPT_MISMATCH'
  | 'OPERATION_FAILED' | 'UNAPPROVED_MUTATION_OBSERVED'
  | 'INTEGRITY_VERIFICATION_FAILED' | 'POST_ACQUISITION_VERIFICATION_FAILED'
  | 'REFRESHED_SNAPSHOT_MISSING' | 'RECEIPT_NOT_SECRET_SAFE';

export interface ControlledAcquisitionIssue {
  readonly code: ControlledAcquisitionIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface ControlledAcquisitionAuthorizationResult {
  readonly contractVersion: typeof CONTROLLED_ACQUISITION_CONTRACT_VERSION;
  readonly decision: 'AUTHORIZED_FOR_SEPARATE_EXECUTOR' | 'DENIED';
  readonly planDigest?: string;
  readonly issues: readonly ControlledAcquisitionIssue[];
}

export interface ControlledAcquisitionOperationResult {
  readonly operationId: string;
  readonly status: 'SUCCESS' | 'FAILED' | 'SKIPPED';
}

export interface ControlledAcquisitionReceipt {
  readonly schemaVersion: typeof CONTROLLED_ACQUISITION_RECEIPT_VERSION;
  readonly receiptId: string;
  readonly planId: string;
  readonly planDigest: string;
  readonly approvalId: string;
  readonly startedAt: string;
  readonly finishedAt: string;
  readonly operationResults: readonly ControlledAcquisitionOperationResult[];
  readonly observedMutations: readonly ControlledAcquisitionMutation[];
  readonly integrityVerified: boolean;
  readonly verificationPassed: boolean;
  readonly rollbackState: 'NOT_REQUIRED' | 'COMPLETE' | 'INCOMPLETE';
  readonly refreshedSnapshotId: string;
  readonly secretSafe: boolean;
}

export interface ControlledAcquisitionReceiptResult {
  readonly status: 'SUCCESS' | 'FAIL';
  readonly issues: readonly ControlledAcquisitionIssue[];
}

export interface ControlledAcquisitionRepairInput {
  readonly failedRepairRounds: number;
  readonly newRootCauseEvidence: boolean;
  readonly goalUnchanged: boolean;
  readonly dependencyUnchanged: boolean;
  readonly riskUnchanged: boolean;
  readonly credentialScopeUnchanged: boolean;
  readonly networkDestinationsUnchanged: boolean;
  readonly mutationEnvelopeUnchanged: boolean;
}

export type ControlledAcquisitionRepairDecision = 'REPAIR_ALLOWED' | 'ESCALATE' | 'STOP';

const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const SHA256 = /^[a-f0-9]{64}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const SECRET_SIGNAL = /(secret|token|password|credential\s*=|api[_-]?key)/i;

function issue(code: ControlledAcquisitionIssueCode, path: string, message: string): ControlledAcquisitionIssue {
  return Object.freeze({ code, path, message });
}

function isPlainRecord(value: unknown): value is Record<string, unknown> {
  if (value === null || typeof value !== 'object' || isProxy(value)) return false;
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

function validUtc(value: unknown): value is string {
  return typeof value === 'string' && ISO_UTC.test(value) && Number.isFinite(Date.parse(value));
}

function authorityProjection(plan: ControlledAcquisitionPlan): Readonly<Record<string, unknown>> {
  return {
    schemaVersion: plan.schemaVersion,
    planId: plan.planId,
    dependencyId: plan.dependencyId,
    targetVersion: plan.targetVersion,
    sourceUri: plan.sourceUri,
    provenanceRef: plan.provenanceRef,
    integrityMethod: plan.integrityMethod,
    expectedDigest: plan.expectedDigest,
    operations: plan.operations,
    intendedMutations: plan.intendedMutations,
    rollbackOperationIds: plan.rollbackOperationIds,
    verificationOperationIds: plan.verificationOperationIds,
    forbiddenMutationKinds: plan.forbiddenMutationKinds,
    expiresAt: plan.expiresAt,
  };
}

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  if (isPlainRecord(value)) {
    return `{${Object.keys(value).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key])}`).join(',')}}`;
  }
  return JSON.stringify(value);
}

export function computeControlledAcquisitionPlanDigest(
  plan: Omit<ControlledAcquisitionPlan, 'planDigest'> | ControlledAcquisitionPlan,
): string {
  return createHash('sha256').update(canonicalJson(authorityProjection(plan as ControlledAcquisitionPlan))).digest('hex');
}

function validatePlan(plan: ControlledAcquisitionPlan, now: string): ControlledAcquisitionIssue[] {
  const issues: ControlledAcquisitionIssue[] = [];
  if (!isPlainRecord(plan)) return [issue('MALFORMED_INPUT', '$.plan', 'Plan must be a plain non-Proxy object.')];
  for (const [key, value] of Object.entries({ planId: plan.planId, dependencyId: plan.dependencyId, targetVersion: plan.targetVersion, provenanceRef: plan.provenanceRef })) {
    if (typeof value !== 'string' || !SAFE_ID.test(value)) issues.push(issue('INVALID_FIELD', `$.plan.${key}`, `${key} must be a bounded safe identifier.`));
  }
  if (plan.schemaVersion !== CONTROLLED_ACQUISITION_PLAN_VERSION) issues.push(issue('INVALID_FIELD', '$.plan.schemaVersion', 'Unsupported plan schema.'));
  let source: URL | undefined;
  try { source = new URL(plan.sourceUri); } catch { /* fail below */ }
  if (!source || source.protocol !== 'https:' || source.username || source.password) issues.push(issue('UNSAFE_SOURCE', '$.plan.sourceUri', 'Source must be credential-free HTTPS.'));
  if (!SHA256.test(plan.expectedDigest)) issues.push(issue('INTEGRITY_EVIDENCE_MISSING', '$.plan.expectedDigest', 'A lowercase SHA-256 digest is required.'));
  if (!validUtc(plan.expiresAt) || Date.parse(now) > Date.parse(plan.expiresAt)) issues.push(issue('PLAN_EXPIRED', '$.plan.expiresAt', 'Plan is expired or has an invalid UTC expiry.'));
  if (computeControlledAcquisitionPlanDigest(plan) !== plan.planDigest) issues.push(issue('PLAN_DIGEST_MISMATCH', '$.plan.planDigest', 'Plan digest does not cover the authority projection.'));
  const operationIds = plan.operations.map(({ operationId }) => operationId);
  if (!operationIds.length || new Set(operationIds).size !== operationIds.length) issues.push(issue('OPERATION_ID_DUPLICATE', '$.plan.operations', 'Operation IDs must be non-empty and unique.'));
  const rollback = new Set(plan.operations.filter(({ phase }) => phase === 'ROLLBACK').map(({ operationId }) => operationId));
  if (!plan.rollbackOperationIds.length || plan.rollbackOperationIds.some((id) => !rollback.has(id))) issues.push(issue('ROLLBACK_INCOMPLETE', '$.plan.rollbackOperationIds', 'Rollback IDs must reference declared rollback operations.'));
  const verification = new Set(plan.operations.filter(({ phase }) => phase === 'VERIFY').map(({ operationId }) => operationId));
  if (!plan.verificationOperationIds.length || plan.verificationOperationIds.some((id) => !verification.has(id))) issues.push(issue('VERIFICATION_INCOMPLETE', '$.plan.verificationOperationIds', 'Verification IDs must reference declared verification operations.'));
  if (plan.intendedMutations.some(({ kind }) => plan.forbiddenMutationKinds.includes(kind))) issues.push(issue('FORBIDDEN_MUTATION_PLANNED', '$.plan.intendedMutations', 'A planned mutation is explicitly forbidden.'));
  if (JSON.stringify(authorityProjection(plan)).match(SECRET_SIGNAL)) issues.push(issue('RAW_SECRET_INCLUDED', '$.plan', 'Plan contains a secret-like inline value.'));
  return issues;
}

export function evaluateControlledAcquisitionAuthorization(
  plan: ControlledAcquisitionPlan,
  approval: ControlledAcquisitionApproval,
  now: string,
): ControlledAcquisitionAuthorizationResult {
  const issues = validUtc(now) ? validatePlan(plan, now) : [issue('INVALID_FIELD', '$.now', 'Current time must be ISO-8601 UTC.')];
  if (!isPlainRecord(approval)) issues.push(issue('MALFORMED_INPUT', '$.approval', 'Approval must be a plain non-Proxy object.'));
  else {
    if (approval.schemaVersion !== CONTROLLED_ACQUISITION_APPROVAL_VERSION) issues.push(issue('INVALID_FIELD', '$.approval.schemaVersion', 'Unsupported approval schema.'));
    if (approval.decision !== 'APPROVED') issues.push(issue('APPROVAL_DENIED', '$.approval.decision', 'Approval is not APPROVED.'));
    if (approval.planId !== plan.planId || approval.planDigest !== plan.planDigest) issues.push(issue('APPROVAL_MISMATCH', '$.approval', 'Approval is not bound to the exact plan ID and digest.'));
    if (!validUtc(approval.approvedAt) || !validUtc(approval.expiresAt) || Date.parse(now) > Date.parse(approval.expiresAt)) issues.push(issue('APPROVAL_EXPIRED', '$.approval.expiresAt', 'Approval is expired or malformed.'));
  }
  return Object.freeze({
    contractVersion: CONTROLLED_ACQUISITION_CONTRACT_VERSION,
    decision: issues.length ? 'DENIED' : 'AUTHORIZED_FOR_SEPARATE_EXECUTOR',
    ...(issues.length ? {} : { planDigest: plan.planDigest }),
    issues: Object.freeze(issues),
  });
}

export function reconcileControlledAcquisitionReceipt(
  plan: ControlledAcquisitionPlan,
  approval: ControlledAcquisitionApproval,
  receipt: ControlledAcquisitionReceipt,
): ControlledAcquisitionReceiptResult {
  const issues: ControlledAcquisitionIssue[] = [];
  if (!isPlainRecord(receipt) || receipt.schemaVersion !== CONTROLLED_ACQUISITION_RECEIPT_VERSION) return { status: 'FAIL', issues: [issue('MALFORMED_INPUT', '$.receipt', 'Receipt must be a supported plain object.')] };
  if (!validUtc(receipt.startedAt) || !validUtc(receipt.finishedAt) || Date.parse(receipt.finishedAt) < Date.parse(receipt.startedAt)) {
    issues.push(issue('INVALID_FIELD', '$.receipt.startedAt', 'Receipt timestamps must be ordered ISO-8601 UTC values.'));
  } else if (evaluateControlledAcquisitionAuthorization(plan, approval, receipt.startedAt).decision !== 'AUTHORIZED_FOR_SEPARATE_EXECUTOR') {
    issues.push(issue('RECEIPT_MISMATCH', '$.receipt', 'Receipt cannot attest a plan that was not authorized when acquisition started.'));
  }
  if (receipt.planId !== plan.planId || receipt.planDigest !== plan.planDigest || receipt.approvalId !== approval.approvalId) issues.push(issue('RECEIPT_MISMATCH', '$.receipt', 'Receipt is not bound to the plan and approval.'));
  const results = new Map(receipt.operationResults.map((result) => [result.operationId, result.status]));
  const mandatory = plan.operations.filter(({ phase }) => phase !== 'ROLLBACK').map(({ operationId }) => operationId);
  if (mandatory.some((id) => results.get(id) !== 'SUCCESS')) issues.push(issue('OPERATION_FAILED', '$.receipt.operationResults', 'Every acquisition and verification operation must succeed.'));
  const intended = new Set(plan.intendedMutations.map(({ kind, target }) => `${kind}:${target}`));
  if (receipt.observedMutations.some(({ kind, target }) => !intended.has(`${kind}:${target}`))) issues.push(issue('UNAPPROVED_MUTATION_OBSERVED', '$.receipt.observedMutations', 'Receipt contains a mutation outside the approved envelope.'));
  if (!receipt.integrityVerified) issues.push(issue('INTEGRITY_VERIFICATION_FAILED', '$.receipt.integrityVerified', 'Source integrity was not verified.'));
  if (!receipt.verificationPassed) issues.push(issue('POST_ACQUISITION_VERIFICATION_FAILED', '$.receipt.verificationPassed', 'Post-acquisition verification failed.'));
  if (receipt.rollbackState === 'INCOMPLETE') issues.push(issue('ROLLBACK_INCOMPLETE', '$.receipt.rollbackState', 'Receipt reports an incomplete rollback.'));
  if (!receipt.refreshedSnapshotId || !SAFE_ID.test(receipt.refreshedSnapshotId)) issues.push(issue('REFRESHED_SNAPSHOT_MISSING', '$.receipt.refreshedSnapshotId', 'A refreshed snapshot reference is required.'));
  if (!receipt.secretSafe) issues.push(issue('RECEIPT_NOT_SECRET_SAFE', '$.receipt.secretSafe', 'Receipt must attest secret-safe evidence.'));
  return { status: issues.length ? 'FAIL' : 'SUCCESS', issues };
}

export function evaluateControlledAcquisitionRepair(input: ControlledAcquisitionRepairInput): ControlledAcquisitionRepairDecision {
  if (!Number.isSafeInteger(input.failedRepairRounds) || input.failedRepairRounds < 0) return 'ESCALATE';
  const envelopeUnchanged = input.goalUnchanged && input.dependencyUnchanged && input.riskUnchanged
    && input.credentialScopeUnchanged && input.networkDestinationsUnchanged && input.mutationEnvelopeUnchanged;
  if (!envelopeUnchanged) return 'ESCALATE';
  if (input.failedRepairRounds >= 3 && !input.newRootCauseEvidence) return 'STOP';
  return input.newRootCauseEvidence ? 'REPAIR_ALLOWED' : 'STOP';
}
