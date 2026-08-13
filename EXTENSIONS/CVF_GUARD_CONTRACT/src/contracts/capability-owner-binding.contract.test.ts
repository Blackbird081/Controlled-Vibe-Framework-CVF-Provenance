import { beforeAll, describe, expect, it } from 'vitest';
import { randomUUID } from 'node:crypto';
import {
  CAPABILITY_OWNER_BINDING_CONTRACT_VERSION,
  bindCommittedCapabilityOwnerGrant,
  isBoundCapabilityOwner,
  readBoundArtifact,
  readBoundGrantIdentity,
  reconcileGrantWithObservation,
  type CapabilityExecutionObservationInput,
  type CapabilityOwnerHandle,
} from './capability-owner-binding.contract';

const GRANT_REF = 'governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v1.json';
const TRACE_ID = 'cadp-ai-t2-fail-closed-checkpoint-f4b99100e';
let handle: CapabilityOwnerHandle;
const runId = randomUUID();

function observation(invocationId: string, retryOrdinal = 0): CapabilityExecutionObservationInput {
  return {
    workOrderId: 'CADP-AI-T2A', workOrderVersion: '2026-08-13.1',
    capabilityId: 'cvf.cadp.owner-bound-evidence', capabilityVersion: 'v3',
    assignmentId: 'cadp-ai-t2a-owner-binding', actionId: 'validateCompatibilityEvidence',
    transport: 'local_git_object_database', resourceRef: GRANT_REF,
    credentialReference: 'none:private-provenance-git', workflowTraceId: TRACE_ID,
    receiptId: TRACE_ID, invocationId, retryOrdinal, evaluatedAt: '2026-08-13T12:30:00.000Z',
  };
}

beforeAll(() => {
  const result = bindCommittedCapabilityOwnerGrant(GRANT_REF);
  expect(result.valid).toBe(true);
  handle = result.data.handle!;
});

describe('repository-bound capability owner contract', () => {
  it('authenticates only the opaque identity returned from committed binding', () => {
    expect(CAPABILITY_OWNER_BINDING_CONTRACT_VERSION).toBe('cvf.cadp.ownerBinding.v3');
    expect(isBoundCapabilityOwner(handle)).toBe(true);
    for (const forged of [
      { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION },
      { ...handle }, JSON.parse(JSON.stringify(handle)), Object.create(handle),
    ]) expect(isBoundCapabilityOwner(forged)).toBe(false);
    const { proxy, revoke } = Proxy.revocable(handle, {});
    revoke();
    expect(() => isBoundCapabilityOwner(proxy)).not.toThrow();
    expect(isBoundCapabilityOwner(proxy)).toBe(false);
  });

  it('returns immutable, fresh scalar projections for committed grant data', () => {
    const identityA = readBoundGrantIdentity(handle)!;
    const identityB = readBoundGrantIdentity(handle)!;
    expect(identityA).toEqual(expect.objectContaining({
      workOrderId: 'CADP-AI-T2A', capabilityId: 'cvf.cadp.owner-bound-evidence',
    }));
    expect(identityA).not.toBe(identityB);
    expect(Object.isFrozen(identityA)).toBe(true);
    const artifact = readBoundArtifact(handle, 'docs/reviews/evidence/cadp-ai-t2-fail-closed-checkpoint-receipt-2026-08-13.json');
    expect(artifact).toEqual(expect.objectContaining({ artifactType: 'receipt', owner: 'CVF_GOVERNANCE_REPOSITORY' }));
    expect(Object.isFrozen(artifact)).toBe(true);
  });

  it('reconciles every owner field and rejects mismatches before consuming state', () => {
    const mismatch = reconcileGrantWithObservation(handle, { ...observation(`${runId}-mismatch-then-valid`), actionId: 'other' });
    expect(mismatch.valid).toBe(false);
    expect(mismatch.issues.map(({ code }) => code)).toContain('GRANT_MISMATCH');
    expect(reconcileGrantWithObservation(handle, observation(`${runId}-mismatch-then-valid`)).valid).toBe(true);
  });

  it('requires concrete trace and receipt identities', () => {
    const wrongTrace = reconcileGrantWithObservation(handle, { ...observation(`${runId}-wrong-trace`), workflowTraceId: 'not-bound' });
    expect(wrongTrace.issues.map(({ code }) => code)).toContain('TRACE_LINKAGE_MISSING');
    const wrongReceipt = reconcileGrantWithObservation(handle, { ...observation(`${runId}-wrong-receipt`), receiptId: 'not-bound' });
    expect(wrongReceipt.issues.map(({ code }) => code)).toContain('RECEIPT_LINKAGE_MISSING');
  });

  it('persists duplicate and ordered retry enforcement across independent binds', () => {
    const invocationId = `${runId}-durable-replay`;
    expect(reconcileGrantWithObservation(handle, observation(invocationId)).valid).toBe(true);
    const rebound = bindCommittedCapabilityOwnerGrant(GRANT_REF).data.handle!;
    expect(reconcileGrantWithObservation(rebound, observation(invocationId)).issues.map(({ code }) => code))
      .toContain('DUPLICATE_INVOCATION_REJECTED');
    expect(reconcileGrantWithObservation(rebound, observation(invocationId, 1)).valid).toBe(true);
    expect(reconcileGrantWithObservation(rebound, observation(invocationId, 3)).issues.map(({ code }) => code))
      .toContain('RETRY_LIMIT_EXCEEDED');
  });

  it('rejects hostile or forged observation inputs without executing accessors', () => {
    let reads = 0;
    const hostile = new Proxy(observation(`${runId}-hostile`), { get() { reads += 1; throw new Error('trap'); } });
    expect(reconcileGrantWithObservation(handle, hostile).issues.map(({ code }) => code)).toContain('MALFORMED_INPUT_SHAPE');
    expect(reads).toBe(0);
    const forged = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION } as CapabilityOwnerHandle;
    expect(reconcileGrantWithObservation(forged, observation(`${runId}-forged`)).issues.map(({ code }) => code)).toContain('NOT_A_BOUND_OWNER');
  });
});
