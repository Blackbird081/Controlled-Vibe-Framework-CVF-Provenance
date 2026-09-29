import { describe, expect, it } from 'vitest';
import {
  CONTROLLED_ACQUISITION_APPROVAL_VERSION,
  CONTROLLED_ACQUISITION_PLAN_VERSION,
  CONTROLLED_ACQUISITION_RECEIPT_VERSION,
  computeControlledAcquisitionPlanDigest,
  evaluateControlledAcquisitionAuthorization,
  evaluateControlledAcquisitionRepair,
  reconcileControlledAcquisitionReceipt,
  type ControlledAcquisitionApproval,
  type ControlledAcquisitionPlan,
  type ControlledAcquisitionReceipt,
} from './controlled-acquisition.contract';

function plan(): ControlledAcquisitionPlan {
  const base = {
    schemaVersion: CONTROLLED_ACQUISITION_PLAN_VERSION,
    planId: 'plan-1', dependencyId: 'node', targetVersion: '22.17.0',
    sourceUri: 'https://publisher.example/node.zip', provenanceRef: 'publisher-release-22.17.0',
    integrityMethod: 'SHA256' as const, expectedDigest: 'a'.repeat(64),
    operations: [
      { operationId: 'download', phase: 'ACQUIRE' as const, action: 'DOWNLOAD' as const, target: 'workspace-cache', networkDestination: 'publisher.example', requiresPrivilege: false },
      { operationId: 'install', phase: 'ACQUIRE' as const, action: 'INSTALL' as const, target: 'workspace-tools/node', requiresPrivilege: false },
      { operationId: 'rollback', phase: 'ROLLBACK' as const, action: 'ROLLBACK' as const, target: 'workspace-tools/node', requiresPrivilege: false },
      { operationId: 'verify', phase: 'VERIFY' as const, action: 'VERIFY' as const, target: 'node-version', requiresPrivilege: false },
    ],
    intendedMutations: [{ kind: 'WORKSPACE_FILE' as const, target: 'workspace-tools/node' }],
    rollbackOperationIds: ['rollback'], verificationOperationIds: ['verify'],
    forbiddenMutationKinds: ['SYSTEM_FILE' as const, 'SERVICE' as const],
    expiresAt: '2026-08-17T00:00:00Z',
  };
  return { ...base, planDigest: computeControlledAcquisitionPlanDigest(base as ControlledAcquisitionPlan) };
}

function approval(value = plan()): ControlledAcquisitionApproval {
  return { schemaVersion: CONTROLLED_ACQUISITION_APPROVAL_VERSION, approvalId: 'approval-1', planId: value.planId, planDigest: value.planDigest, decision: 'APPROVED', approvedAt: '2026-08-16T00:00:00Z', expiresAt: '2026-08-17T00:00:00Z' };
}

function receipt(value = plan(), approved = approval(value)): ControlledAcquisitionReceipt {
  return { schemaVersion: CONTROLLED_ACQUISITION_RECEIPT_VERSION, receiptId: 'receipt-1', planId: value.planId, planDigest: value.planDigest, approvalId: approved.approvalId, startedAt: '2026-08-16T00:00:00Z', finishedAt: '2026-08-16T00:01:00Z', operationResults: [{ operationId: 'download', status: 'SUCCESS' }, { operationId: 'install', status: 'SUCCESS' }, { operationId: 'verify', status: 'SUCCESS' }], observedMutations: value.intendedMutations, integrityVerified: true, verificationPassed: true, rollbackState: 'NOT_REQUIRED', refreshedSnapshotId: 'snapshot-2', secretSafe: true };
}

describe('controlled acquisition authorization kernel', () => {
  it('authorizes an exact fresh plan and digest-bound approval for a separate executor', () => {
    const value = plan();
    expect(evaluateControlledAcquisitionAuthorization(value, approval(value), '2026-08-16T01:00:00Z')).toEqual(expect.objectContaining({ decision: 'AUTHORIZED_FOR_SEPARATE_EXECUTOR', planDigest: value.planDigest, issues: [] }));
  });

  it('computes a canonical digest independent of nested object key order', () => {
    const value = plan();
    const reordered = { ...value, operations: value.operations.map(({ requiresPrivilege, target, action, phase, operationId, networkDestination }) => ({ requiresPrivilege, target, action, phase, operationId, ...(networkDestination ? { networkDestination } : {}) })) };
    expect(computeControlledAcquisitionPlanDigest(reordered)).toBe(value.planDigest);
  });

  it.each([
    ['changed target', (value: ControlledAcquisitionPlan) => ({ ...value, targetVersion: '23.0.0' })],
    ['unsafe source', (value: ControlledAcquisitionPlan) => ({ ...value, sourceUri: 'http://publisher.example/node.zip' })],
    ['missing integrity', (value: ControlledAcquisitionPlan) => ({ ...value, expectedDigest: '' })],
    ['expired plan', (value: ControlledAcquisitionPlan) => ({ ...value, expiresAt: '2026-08-15T00:00:00Z' })],
    ['forbidden mutation', (value: ControlledAcquisitionPlan) => ({ ...value, intendedMutations: [{ kind: 'SYSTEM_FILE' as const, target: 'system32' }] })],
    ['missing rollback', (value: ControlledAcquisitionPlan) => ({ ...value, rollbackOperationIds: [] })],
    ['missing verification', (value: ControlledAcquisitionPlan) => ({ ...value, verificationOperationIds: [] })],
  ])('fails closed for %s', (_label, mutate) => {
    const value = plan();
    expect(evaluateControlledAcquisitionAuthorization(mutate(value), approval(value), '2026-08-16T01:00:00Z').decision).toBe('DENIED');
  });

  it('rejects approval drift, denial, and expiry', () => {
    const value = plan();
    expect(evaluateControlledAcquisitionAuthorization(value, { ...approval(value), planDigest: 'b'.repeat(64) }, '2026-08-16T01:00:00Z').decision).toBe('DENIED');
    expect(evaluateControlledAcquisitionAuthorization(value, { ...approval(value), decision: 'DENIED' }, '2026-08-16T01:00:00Z').decision).toBe('DENIED');
    expect(evaluateControlledAcquisitionAuthorization(value, approval(value), '2026-08-18T01:00:00Z').decision).toBe('DENIED');
  });

  it('requires receipt success beyond process exit semantics', () => {
    const value = plan(); const approved = approval(value);
    expect(reconcileControlledAcquisitionReceipt(value, approved, receipt(value, approved)).status).toBe('SUCCESS');
    expect(reconcileControlledAcquisitionReceipt(value, approved, { ...receipt(value, approved), integrityVerified: false }).status).toBe('FAIL');
    expect(reconcileControlledAcquisitionReceipt(value, approved, { ...receipt(value, approved), operationResults: [{ operationId: 'download', status: 'SUCCESS' }] }).status).toBe('FAIL');
    expect(reconcileControlledAcquisitionReceipt(value, approved, { ...receipt(value, approved), observedMutations: [{ kind: 'SYSTEM_FILE', target: 'outside-envelope' }] }).status).toBe('FAIL');
    expect(reconcileControlledAcquisitionReceipt(value, approved, { ...receipt(value, approved), refreshedSnapshotId: '' }).status).toBe('FAIL');
    expect(reconcileControlledAcquisitionReceipt(value, approved, { ...receipt(value, approved), secretSafe: false }).status).toBe('FAIL');
    expect(reconcileControlledAcquisitionReceipt(value, approved, { ...receipt(value, approved), startedAt: '2026-08-18T00:00:00Z', finishedAt: '2026-08-18T00:01:00Z' }).status).toBe('FAIL');
    expect(reconcileControlledAcquisitionReceipt(value, approved, { ...receipt(value, approved), rollbackState: 'INCOMPLETE' }).status).toBe('FAIL');
  });

  it('allows repair only inside the unchanged envelope with new root-cause evidence', () => {
    const unchanged = { failedRepairRounds: 1, newRootCauseEvidence: true, goalUnchanged: true, dependencyUnchanged: true, riskUnchanged: true, credentialScopeUnchanged: true, networkDestinationsUnchanged: true, mutationEnvelopeUnchanged: true };
    expect(evaluateControlledAcquisitionRepair(unchanged)).toBe('REPAIR_ALLOWED');
    expect(evaluateControlledAcquisitionRepair({ ...unchanged, mutationEnvelopeUnchanged: false })).toBe('ESCALATE');
    expect(evaluateControlledAcquisitionRepair({ ...unchanged, failedRepairRounds: 3, newRootCauseEvidence: false })).toBe('STOP');
  });
});
