import { describe, expect, it } from 'vitest';
import {
  CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION,
  evaluateCapabilityAcquisitionReceiptVerification,
  type CapabilityAcquisitionReceipt,
  type CapabilityAcquisitionReceiptMutation,
} from './capability-acquisition-receipt-verification.contract';
import {
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION,
  type CapabilityBootstrapApprovalEvidence,
  type CapabilityBootstrapMutationEnvelopeEntry,
} from './capability-bootstrap-approval-evidence.contract';
import {
  CONTROLLED_ACQUISITION_PLAN_VERSION,
  computeControlledAcquisitionPlanDigest,
  type ControlledAcquisitionPlan,
} from './controlled-acquisition.contract';
import { evaluateCapabilityAcquisitionReceiptVerification as contractsBarrelEvaluator } from './index';
import { evaluateCapabilityAcquisitionReceiptVerification as rootBarrelEvaluator } from '../index';

function plan(overrides: Partial<ControlledAcquisitionPlan> = {}): ControlledAcquisitionPlan {
  const base = {
    schemaVersion: CONTROLLED_ACQUISITION_PLAN_VERSION,
    planId: 'plan-t9-001',
    dependencyId: 'ripgrep',
    targetVersion: '14.1.1',
    sourceUri: 'https://publisher.example/ripgrep-14.1.1.zip',
    provenanceRef: 'publisher-release-14.1.1',
    integrityMethod: 'SHA256' as const,
    expectedDigest: 'a'.repeat(64),
    operations: [
      { operationId: 'download', phase: 'ACQUIRE' as const, action: 'DOWNLOAD' as const, target: 'workspace-cache', networkDestination: 'publisher.example', requiresPrivilege: false },
      { operationId: 'install', phase: 'ACQUIRE' as const, action: 'INSTALL' as const, target: 'workspace-demo/.cvf/tools/ripgrep', requiresPrivilege: false },
      { operationId: 'rollback', phase: 'ROLLBACK' as const, action: 'ROLLBACK' as const, target: 'workspace-demo/.cvf/tools/ripgrep', requiresPrivilege: false },
      { operationId: 'verify', phase: 'VERIFY' as const, action: 'VERIFY' as const, target: 'rg-version', requiresPrivilege: false },
    ],
    intendedMutations: [{ kind: 'WORKSPACE_FILE' as const, target: 'workspace-demo/.cvf/tools/ripgrep' }],
    rollbackOperationIds: ['rollback'],
    verificationOperationIds: ['verify'],
    forbiddenMutationKinds: ['SYSTEM_FILE' as const, 'SERVICE' as const],
    expiresAt: '2026-08-17T00:00:00Z',
    ...overrides,
  };
  const withoutDigest = { ...base };
  delete (withoutDigest as Partial<ControlledAcquisitionPlan>).planDigest;
  const planDigest = overrides.planDigest ?? computeControlledAcquisitionPlanDigest(withoutDigest as ControlledAcquisitionPlan);
  return { ...base, planDigest } as ControlledAcquisitionPlan;
}

function envelopeEntry(overrides: Partial<CapabilityBootstrapMutationEnvelopeEntry> = {}): CapabilityBootstrapMutationEnvelopeEntry {
  return {
    kind: 'FILESYSTEM',
    target: 'workspace-demo/.cvf/tools/ripgrep',
    description: 'Create workspace-local tool directory.',
    reversible: true,
    ...overrides,
  };
}

function approval(value: ControlledAcquisitionPlan = plan(), overrides: Partial<CapabilityBootstrapApprovalEvidence> = {}): CapabilityBootstrapApprovalEvidence {
  return {
    schemaVersion: CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION,
    approvalId: 'approval-t9-001',
    planId: value.planId,
    planDigest: value.planDigest,
    workspaceId: 'workspace-demo',
    workOrderId: null,
    decision: 'APPROVE',
    actorId: 'operator-demo',
    issuedAt: '2026-08-16T04:00:00Z',
    expiresAt: '2026-08-16T05:00:00Z',
    replayNonce: 'nonce-demo-001',
    mutationEnvelope: [envelopeEntry()],
    ...overrides,
  };
}

function receiptMutation(overrides: Partial<CapabilityAcquisitionReceiptMutation> = {}): CapabilityAcquisitionReceiptMutation {
  return {
    kind: 'FILESYSTEM',
    target: 'workspace-demo/.cvf/tools/ripgrep',
    description: 'Create workspace-local tool directory.',
    reversible: true,
    ...overrides,
  };
}

function receipt(planValue: ControlledAcquisitionPlan = plan(), approvalValue: CapabilityBootstrapApprovalEvidence = approval(planValue), overrides: Partial<CapabilityAcquisitionReceipt> = {}): CapabilityAcquisitionReceipt {
  return {
    schemaVersion: CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION,
    receiptId: 'receipt-t9-001',
    planId: planValue.planId,
    planDigest: planValue.planDigest,
    approvalId: approvalValue.approvalId,
    executorId: 'fixture-executor',
    startedAt: '2026-08-16T04:05:00Z',
    endedAt: '2026-08-16T04:06:00Z',
    operationResults: [
      { operationId: 'download', status: 'SUCCESS' },
      { operationId: 'install', status: 'SUCCESS' },
      { operationId: 'verify', status: 'SUCCESS' },
    ],
    actualMutations: [receiptMutation()],
    artifact: {
      path: 'workspace-demo/.cvf/tools/ripgrep/rg.exe',
      version: '14.1.1',
      digest: 'a'.repeat(64),
    },
    verification: { status: 'PASS', checks: ['digest matched', 'mutation envelope matched'] },
    deviations: [],
    rollbackStatus: 'READY',
    refreshedSnapshotId: 'snap-ready-002',
    evidenceRefs: ['trace:fixture-001'],
    ...overrides,
  };
}

function input(overrides: Partial<Record<string, unknown>> = {}) {
  const planValue = plan();
  const approvalValue = approval(planValue);
  return {
    plan: planValue,
    approval: approvalValue,
    expectedWorkspaceId: 'workspace-demo',
    expectedActorId: 'operator-demo',
    receipt: receipt(planValue, approvalValue),
    ...overrides,
  };
}

describe('capability acquisition receipt verification and repair-stop kernel', () => {
  it('exports the exact evaluator through both Guard Contract barrels', () => {
    expect(contractsBarrelEvaluator).toBe(evaluateCapabilityAcquisitionReceiptVerification);
    expect(rootBarrelEvaluator).toBe(evaluateCapabilityAcquisitionReceiptVerification);
  });

  it('verifies an exact matching plan/approval/receipt as evidence-only success', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input());
    expect(result).toEqual(expect.objectContaining({
      disposition: 'VERIFIED_SUCCESS_EVIDENCE',
      receiptPersisted: false,
      executionAuthorized: false,
      acquisitionAuthorized: false,
      mutationAuthorized: false,
      repairAuthorized: false,
      rollbackAuthorized: false,
      taskAuthorityGranted: false,
      networkAuthorized: false,
      issues: [],
    }));
  });

  it('composes a repair-stop projection when repair input is supplied', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      repair: {
        failedRepairRounds: 1,
        newRootCauseEvidence: true,
        goalUnchanged: true,
        dependencyUnchanged: true,
        riskUnchanged: true,
        credentialScopeUnchanged: true,
        networkDestinationsUnchanged: true,
        mutationEnvelopeUnchanged: true,
      },
    }));
    expect(result.disposition).toBe('VERIFIED_SUCCESS_EVIDENCE');
    expect(result.repairProjection).toBe('REPAIR_ALLOWED');
  });

  it('returns STOP after three failed repair rounds without new root-cause evidence', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      repair: {
        failedRepairRounds: 3,
        newRootCauseEvidence: false,
        goalUnchanged: true,
        dependencyUnchanged: true,
        riskUnchanged: true,
        credentialScopeUnchanged: true,
        networkDestinationsUnchanged: true,
        mutationEnvelopeUnchanged: true,
      },
    }));
    expect(result.disposition).toBe('VERIFIED_SUCCESS_EVIDENCE');
    expect(result.repairProjection).toBe('STOP');
  });

  it('returns ESCALATE when the mutation envelope changed', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      repair: {
        failedRepairRounds: 1,
        newRootCauseEvidence: true,
        goalUnchanged: true,
        dependencyUnchanged: true,
        riskUnchanged: true,
        credentialScopeUnchanged: true,
        networkDestinationsUnchanged: true,
        mutationEnvelopeUnchanged: false,
      },
    }));
    expect(result.disposition).toBe('VERIFIED_SUCCESS_EVIDENCE');
    expect(result.repairProjection).toBe('ESCALATE');
  });

  it('keeps all authority literals false even on a rejected path', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({ plan: 'not-a-plan' }));
    expect(result).toEqual(expect.objectContaining({
      disposition: 'REJECTED',
      receiptPersisted: false,
      executionAuthorized: false,
      acquisitionAuthorized: false,
      mutationAuthorized: false,
      repairAuthorized: false,
      rollbackAuthorized: false,
      taskAuthorityGranted: false,
      networkAuthorized: false,
    }));
  });

  it('rejects non-plain-object top-level input without throwing', () => {
    expect(evaluateCapabilityAcquisitionReceiptVerification(null).disposition).toBe('REJECTED');
    expect(evaluateCapabilityAcquisitionReceiptVerification(undefined).disposition).toBe('REJECTED');
    expect(evaluateCapabilityAcquisitionReceiptVerification('string').disposition).toBe('REJECTED');
    expect(evaluateCapabilityAcquisitionReceiptVerification(42).disposition).toBe('REJECTED');
    expect(evaluateCapabilityAcquisitionReceiptVerification([]).disposition).toBe('REJECTED');
  });

  it('rejects a Proxy-wrapped top-level input without invoking traps', () => {
    let trapped = false;
    const proxied = new Proxy(input(), {
      get(target, key, receiver) {
        trapped = true;
        return Reflect.get(target, key, receiver);
      },
    });
    const result = evaluateCapabilityAcquisitionReceiptVerification(proxied);
    expect(result.disposition).toBe('REJECTED');
    expect(trapped).toBe(false);
  });

  it('rejects a Proxy-wrapped receipt object without invoking traps', () => {
    let trapped = false;
    const proxiedReceipt = new Proxy(receipt(), {
      get(target, key, receiver) {
        trapped = true;
        return Reflect.get(target, key, receiver);
      },
    });
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({ receipt: proxiedReceipt }));
    expect(result.disposition).toBe('REJECTED');
    expect(trapped).toBe(false);
  });

  it('rejects a receipt object with accessor properties without invoking the getter', () => {
    let getterCalled = false;
    const hostile = receipt();
    Object.defineProperty(hostile, 'executorId', {
      enumerable: true,
      get() {
        getterCalled = true;
        return 'fixture-executor';
      },
    });
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({ receipt: hostile }));
    expect(result.disposition).toBe('REJECTED');
    expect(getterCalled).toBe(false);
  });

  it('rejects a sparse operationResults array', () => {
    const sparse: unknown[] = [{ operationId: 'download', status: 'SUCCESS' }];
    sparse[3] = { operationId: 'install', status: 'SUCCESS' };
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { operationResults: sparse as CapabilityAcquisitionReceipt['operationResults'] }),
    }));
    expect(result.disposition).toBe('REJECTED');
  });

  it('rejects an oversized actualMutations array', () => {
    const oversized = Array.from({ length: 65 }, (_unused, index) => receiptMutation({ target: `target-${index}` }));
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { actualMutations: oversized }),
    }));
    expect(result.disposition).toBe('REJECTED');
  });

  it('rejects an Array subclass without invoking inherited iteration hooks', () => {
    let inheritedHookCalled = false;
    class HostileOperationArray extends Array<CapabilityAcquisitionReceipt['operationResults'][number]> {
      override forEach(): void {
        inheritedHookCalled = true;
        throw new Error('inherited array hook must not run');
      }
    }
    const hostile = new HostileOperationArray(
      { operationId: 'download', status: 'SUCCESS' },
      { operationId: 'install', status: 'SUCCESS' },
      { operationId: 'verify', status: 'SUCCESS' },
    );
    const call = () => evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { operationResults: hostile }),
    }));
    expect(call).not.toThrow();
    expect(call().disposition).toBe('REJECTED');
    expect(inheritedHookCalled).toBe(false);
  });

  it('rejects unknown keys on the receipt object', () => {
    const hostile = { ...receipt(), extraField: 'not allowed' };
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({ receipt: hostile }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'UNKNOWN_KEYS')).toBe(true);
  });

  it('rejects an unsupported receipt schema version', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: { ...receipt(), schemaVersion: 'wrong.version.v1' },
    }));
    expect(result.disposition).toBe('REJECTED');
  });

  it('rejects when T8 approval-evidence binding rejects the plan/approval', () => {
    const planValue = plan();
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      plan: planValue,
      approval: approval(planValue, { workspaceId: 'workspace-other' }),
      receipt: receipt(planValue, approval(planValue, { workspaceId: 'workspace-other' })),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'APPROVAL_EVIDENCE_REJECTED')).toBe(true);
  });

  it('rejects a receipt not bound to the exact validated plan/approval IDs', () => {
    const planValue = plan();
    const approvalValue = approval(planValue);
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      plan: planValue,
      approval: approvalValue,
      receipt: receipt(planValue, approvalValue, { approvalId: 'approval-other' }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'RECEIPT_BINDING_MISMATCH')).toBe(true);
  });

  it('rejects when the receipt start time is after approval expiry, via T8 fail-closed APPROVAL_EXPIRED using receipt.startedAt as the validation time', () => {
    const planValue = plan();
    const approvalValue = approval(planValue, { issuedAt: '2026-08-16T04:00:00Z', expiresAt: '2026-08-16T04:02:00Z' });
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      plan: planValue,
      approval: approvalValue,
      receipt: receipt(planValue, approvalValue, { startedAt: '2026-08-16T04:05:00Z', endedAt: '2026-08-16T04:06:00Z' }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'APPROVAL_EVIDENCE_REJECTED')).toBe(true);
  });

  it('rejects endedAt preceding startedAt', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { startedAt: '2026-08-16T04:10:00Z', endedAt: '2026-08-16T04:05:00Z' }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'TIMESTAMP_ORDER_INVALID')).toBe(true);
  });

  it('rejects a missing mandatory operation result', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, {
        operationResults: [{ operationId: 'download', status: 'SUCCESS' }, { operationId: 'install', status: 'SUCCESS' }],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'OPERATION_MISSING')).toBe(true);
  });

  it('rejects an extra operation result outside the plan non-rollback operations', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, {
        operationResults: [
          { operationId: 'download', status: 'SUCCESS' },
          { operationId: 'install', status: 'SUCCESS' },
          { operationId: 'verify', status: 'SUCCESS' },
          { operationId: 'rollback', status: 'SUCCESS' },
        ],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'OPERATION_EXTRA')).toBe(true);
  });

  it('rejects a duplicate operation result entry', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, {
        operationResults: [
          { operationId: 'download', status: 'SUCCESS' },
          { operationId: 'download', status: 'SUCCESS' },
          { operationId: 'install', status: 'SUCCESS' },
          { operationId: 'verify', status: 'SUCCESS' },
        ],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'OPERATION_DUPLICATE')).toBe(true);
  });

  it('rejects a FAILED mandatory operation result', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, {
        operationResults: [
          { operationId: 'download', status: 'SUCCESS' },
          { operationId: 'install', status: 'FAILED' },
          { operationId: 'verify', status: 'SUCCESS' },
        ],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'OPERATION_NOT_SUCCESSFUL')).toBe(true);
  });

  it('rejects a SKIPPED mandatory operation result', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, {
        operationResults: [
          { operationId: 'download', status: 'SUCCESS' },
          { operationId: 'install', status: 'SKIPPED' },
          { operationId: 'verify', status: 'SUCCESS' },
        ],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'OPERATION_NOT_SUCCESSFUL')).toBe(true);
  });

  it('rejects a missing required mutation', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { actualMutations: [] }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'MUTATION_MISSING')).toBe(true);
  });

  it('rejects an extra mutation outside the planned scope', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, {
        actualMutations: [receiptMutation(), receiptMutation({ kind: 'ENVIRONMENT', target: 'unexpected-target' })],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'MUTATION_EXTRA')).toBe(true);
  });

  it('rejects a duplicate mutation entry', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { actualMutations: [receiptMutation(), receiptMutation()] }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'MUTATION_DUPLICATE')).toBe(true);
  });

  it('preserves intended-mutation multiplicity instead of collapsing the plan to a set', () => {
    const duplicatedMutation = { kind: 'WORKSPACE_FILE' as const, target: 'workspace-demo/.cvf/tools/ripgrep' };
    const planValue = plan({ intendedMutations: [duplicatedMutation, duplicatedMutation] });
    const approvalValue = approval(planValue);
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      plan: planValue,
      approval: approvalValue,
      receipt: receipt(planValue, approvalValue),
    }));
    expect(result.disposition).toBe('REJECTED');
  });

  it('rejects an artifact digest that does not equal the plan expected digest', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { artifact: { path: 'workspace-demo/.cvf/tools/ripgrep/rg.exe', version: '14.1.1', digest: 'b'.repeat(64) } }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ARTIFACT_DIGEST_MISMATCH')).toBe(true);
  });

  it('rejects a non-lowercase or malformed artifact digest', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { artifact: { path: 'workspace-demo/.cvf/tools/ripgrep/rg.exe', version: '14.1.1', digest: 'A'.repeat(64) } }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ARTIFACT_DIGEST_INVALID')).toBe(true);
  });

  it('rejects an artifact version that differs from the authenticated plan target version', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, {
        artifact: { path: 'workspace-demo/.cvf/tools/ripgrep/rg.exe', version: '14.1.0', digest: 'a'.repeat(64) },
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ARTIFACT_VERSION_MISMATCH')).toBe(true);
  });

  it('rejects high-confidence raw secret-like content in receipt evidence without echoing it', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, {
        actualMutations: [receiptMutation({ description: 'Binds api_key=abcdef into the workspace.' })],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'SECRET_LIKE_CONTENT')).toBe(true);
    expect(JSON.stringify(result)).not.toContain('abcdef');
  });

  it('does not create a false secret positive from a field name alone', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input());
    expect(result.disposition).toBe('VERIFIED_SUCCESS_EVIDENCE');
  });

  it('does not treat ordinary words containing secret vocabulary as raw-secret evidence', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, {
        actualMutations: [receiptMutation({ description: 'Update tokenizer metadata for the passwordless helper.' })],
        evidenceRefs: ['trace:secretary-review'],
      }),
    }));
    expect(result.disposition).toBe('VERIFIED_SUCCESS_EVIDENCE');
  });

  it('rejects a verification status other than PASS', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { verification: { status: 'UNKNOWN', checks: [] } }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'VERIFICATION_NOT_PASSED')).toBe(true);
  });

  it('rejects a receipt reporting at least one deviation', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { deviations: ['unexpected file touched'] }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'DEVIATION_PRESENT')).toBe(true);
  });

  it('rejects an unsafe rollback status', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { rollbackStatus: 'FAILED' }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ROLLBACK_STATE_UNSAFE')).toBe(true);
  });

  it('rejects a missing evidence reference list', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input({
      receipt: receipt(undefined, undefined, { evidenceRefs: [] }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'EVIDENCE_REFS_MISSING')).toBe(true);
  });

  it('never echoes receipt path, executor detail, or check text beyond bounded IDs', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input());
    const serialized = JSON.stringify(result);
    expect(serialized).not.toContain('rg.exe');
    expect(serialized).not.toContain('digest matched');
  });

  it('produces stable issue ordering and identical output for identical explicit input', () => {
    const first = evaluateCapabilityAcquisitionReceiptVerification(input());
    const second = evaluateCapabilityAcquisitionReceiptVerification(input());
    expect(first).toEqual(second);
  });

  it('does not mutate the caller-supplied input', () => {
    const planValue = plan();
    const approvalValue = approval(planValue);
    const receiptValue = receipt(planValue, approvalValue);
    const frozenInput = Object.freeze({
      plan: planValue,
      approval: approvalValue,
      expectedWorkspaceId: 'workspace-demo',
      expectedActorId: 'operator-demo',
      receipt: receiptValue,
    });
    expect(() => evaluateCapabilityAcquisitionReceiptVerification(frozenInput)).not.toThrow();
    const result = evaluateCapabilityAcquisitionReceiptVerification(frozenInput);
    expect(result.disposition).toBe('VERIFIED_SUCCESS_EVIDENCE');
  });

  it('keeps every authority literal false on the positive path', () => {
    const result = evaluateCapabilityAcquisitionReceiptVerification(input());
    expect(result.receiptPersisted).toBe(false);
    expect(result.executionAuthorized).toBe(false);
    expect(result.acquisitionAuthorized).toBe(false);
    expect(result.mutationAuthorized).toBe(false);
    expect(result.repairAuthorized).toBe(false);
    expect(result.rollbackAuthorized).toBe(false);
    expect(result.taskAuthorityGranted).toBe(false);
    expect(result.networkAuthorized).toBe(false);
  });
});
