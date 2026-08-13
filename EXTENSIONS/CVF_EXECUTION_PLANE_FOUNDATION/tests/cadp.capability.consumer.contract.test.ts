import { execFileSync } from 'node:child_process';
import { randomUUID } from 'node:crypto';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { beforeAll, describe, expect, it } from 'vitest';
import {
  CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION,
  evaluateCadpCapabilityConsumer,
  type CadpCapabilityConsumerIssue,
  type CadpCapabilityConsumerRequest,
} from '../src/cadp.capability.consumer.contract';
import { bindCommittedCapabilityOwnerGrant, type CapabilityOwnerHandle } from '../../CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract';
import type {
  CapabilityAdmissionRecord,
  CapabilityAssignmentRecord,
  CapabilityDistributionManifest,
  CompatibilityEvidenceRecord,
} from '../../CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract';

const GRANT_REF = 'governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v2.json';
const TRACE_ID = 'cadp-ai-t2-fail-closed-checkpoint-f4b99100e';
const CAPABILITY_ID = 'cvf.cadp.owner-bound-evidence';
const CAPABILITY_VERSION = 'v3';
const ACTION_ID = 'validateCompatibilityEvidence';
const GRANT_ASSIGNMENT_ID = 'cadp-ai-t2a-owner-binding';

let handle: CapabilityOwnerHandle;
const runId = randomUUID();

function admission(overrides: Partial<CapabilityAdmissionRecord> = {}): CapabilityAdmissionRecord {
  return {
    admissionId: 'cadp-ai-t3a-consumer-admission',
    capabilityId: CAPABILITY_ID,
    capabilityVersion: CAPABILITY_VERSION,
    decision: 'ADMIT_READ_ONLY',
    sourceVerified: true,
    admittedActions: [{ actionId: ACTION_ID, mutationType: 'read' }],
    executionAuthorized: false,
    rawSecretsAllowed: false,
    duplicateCanonicalOwnerRequired: false,
    ...overrides,
  };
}

function assignment(overrides: Partial<CapabilityAssignmentRecord> = {}): CapabilityAssignmentRecord {
  return {
    assignmentId: GRANT_ASSIGNMENT_ID,
    admissionId: 'cadp-ai-t3a-consumer-admission',
    capabilityId: CAPABILITY_ID,
    capabilityVersion: CAPABILITY_VERSION,
    assignedActionIds: [ACTION_ID],
    excludedActionIds: [],
    workOrderRequired: true,
    executionAuthorized: false,
    rawSecretsIncluded: false,
    ...overrides,
  };
}

function distribution(overrides: Partial<CapabilityDistributionManifest> = {}): CapabilityDistributionManifest {
  return {
    distributionId: 'cadp-ai-t3a-consumer-distribution',
    capabilityId: CAPABILITY_ID,
    installMode: 'LOCAL_PRIVATE',
    contents: [{ path: 'records/admission.json', sha256: 'a'.repeat(64), containsSecret: false }],
    distributionGrantsAssignment: false,
    distributionGrantsActivation: false,
    distributionGrantsExecution: false,
    rawSecretsIncluded: false,
    ...overrides,
  };
}

function evidence(overrides: Partial<CompatibilityEvidenceRecord> = {}): CompatibilityEvidenceRecord {
  return {
    capabilityId: CAPABILITY_ID,
    evidenceLevel: 'CERTIFIED_BOUNDED',
    receiptRefs: ['docs/reviews/evidence/cadp-ai-t2-fail-closed-checkpoint-receipt-2026-08-13.json'],
    workOrderRef: 'docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T2A_REPOSITORY_OWNER_BINDING_CONTINUATION_2026-08-13.md',
    reviewRef: 'docs/reviews/CVF_CADP_AI_T2_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-13.md',
    freezeRef: 'docs/baselines/CVF_GC018_CADP_AI_T2A_REPOSITORY_OWNER_BINDING_CONTINUATION_2026-08-13.md',
    passingActionIds: [ACTION_ID],
    expectedEvidenceOwner: 'CVF_GOVERNANCE_REPOSITORY',
    rawSecretsRecorded: false,
    ...overrides,
  };
}

function observation(invocationId: string, retryOrdinal = 0) {
  return {
    workOrderId: 'CADP-AI-T2A',
    workOrderVersion: '2026-08-13.2',
    capabilityId: CAPABILITY_ID,
    capabilityVersion: CAPABILITY_VERSION,
    assignmentId: GRANT_ASSIGNMENT_ID,
    actionId: ACTION_ID,
    transport: 'local_git_object_database',
    resourceRef: GRANT_REF,
    credentialReference: 'none:private-provenance-git',
    workflowTraceId: TRACE_ID,
    receiptId: TRACE_ID,
    invocationId,
    retryOrdinal,
    evaluatedAt: '2026-08-13T12:30:00.000Z',
  };
}

function request(overrides: Partial<CadpCapabilityConsumerRequest> = {}): CadpCapabilityConsumerRequest {
  const invocationId = `${runId}-${randomUUID()}`;
  return {
    ownerHandle: handle,
    admission: admission(),
    assignment: assignment(),
    distribution: distribution(),
    evidence: evidence(),
    observation: observation(invocationId),
    ...overrides,
  };
}

beforeAll(() => {
  const binding = bindCommittedCapabilityOwnerGrant(GRANT_REF);
  expect(binding.valid).toBe(true);
  handle = binding.data.handle!;
});

describe('cadp capability consumer eligibility projection', () => {
  it('exposes its contract version', () => {
    expect(CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION).toBe('cvf.cadp.consumer.v1');
  });

  it('produces an eligible frozen projection with literal executionAuthorized=false for a genuine v2-bound request', () => {
    const result = evaluateCadpCapabilityConsumer(request());
    expect(result.valid).toBe(true);
    expect(result.issues).toEqual([]);
    expect(result.projection.decision).toBe('ELIGIBLE');
    expect(result.projection.executionAuthorized).toBe(false);
    expect(result.projection.capabilityId).toBe(CAPABILITY_ID);
    expect(result.projection.capabilityVersion).toBe(CAPABILITY_VERSION);
    expect(result.projection.assignmentId).toBe(GRANT_ASSIGNMENT_ID);
    expect(result.projection.actionId).toBe(ACTION_ID);
    expect(result.projection.reconciled).toBe(true);
  });

  it('rejects forged, copied, serialized, proxied, revoked and absent owner handles', () => {
    const forgedHandles: unknown[] = [
      { contractVersion: 'cvf.cadp.ownerBinding.v3' },
      { ...handle },
      JSON.parse(JSON.stringify(handle)),
      Object.create(handle),
    ];
    for (const forged of forgedHandles) {
      const result = evaluateCadpCapabilityConsumer(request({ ownerHandle: forged as CapabilityOwnerHandle }));
      expect(result.valid).toBe(false);
      expect(result.issues.some((issue) => issue.code === 'NOT_A_BOUND_OWNER')).toBe(true);
    }
    const { proxy, revoke } = Proxy.revocable(handle, {});
    revoke();
    const revoked = evaluateCadpCapabilityConsumer(request({ ownerHandle: proxy as CapabilityOwnerHandle }));
    expect(revoked.valid).toBe(false);
    const absent = evaluateCadpCapabilityConsumer(request({ ownerHandle: undefined as unknown as CapabilityOwnerHandle }));
    expect(absent.valid).toBe(false);
    expect(absent.issues.some((issue) => issue.code === 'NOT_A_BOUND_OWNER')).toBe(true);
  });

  it('fails closed on a non-ADMIT/ADMIT_READ_ONLY admission decision', () => {
    const result = evaluateCadpCapabilityConsumer(request({ admission: admission({ decision: 'BLOCK' }) }));
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === 'ADMISSION_NOT_ASSIGNABLE')).toBe(true);
  });

  it('fails closed when the assignment exceeds admitted actions', () => {
    const result = evaluateCadpCapabilityConsumer(request({ assignment: assignment({ assignedActionIds: ['write'] }) }));
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === 'ACTION_OUTSIDE_ADMISSION')).toBe(true);
  });

  it('fails closed on distribution authority flags', () => {
    const hostileDistribution = {
      ...distribution(),
      distributionGrantsExecution: true,
    } as unknown as CapabilityDistributionManifest;
    const result = evaluateCadpCapabilityConsumer(request({ distribution: hostileDistribution }));
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === 'AUTHORITY_MINT')).toBe(true);
  });

  it('fails closed on invalid evidence level and raw-secret evidence', () => {
    const hostileEvidence = {
      ...evidence(),
      evidenceLevel: 'BOGUS',
      rawSecretsRecorded: true,
    } as unknown as CompatibilityEvidenceRecord;
    const result = evaluateCadpCapabilityConsumer(request({ evidence: hostileEvidence }));
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === 'EVIDENCE_LEVEL_INVALID')).toBe(true);
    expect(result.issues.some((issue) => issue.code === 'RAW_SECRET_INCLUDED')).toBe(true);
  });

  it('fails closed on a cross-record capability mismatch the validators cannot see', () => {
    const result = evaluateCadpCapabilityConsumer(request({ distribution: distribution({ capabilityId: 'cvf.cadp.unrelated' }) }));
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === 'CROSS_RECORD_MISMATCH')).toBe(true);
  });

  it('requires the committed action to be both admitted and assigned', () => {
    const notAdmitted = evaluateCadpCapabilityConsumer(request({
      admission: admission({ admittedActions: [{ actionId: 'other', mutationType: 'read' }] }),
      assignment: assignment({ assignedActionIds: ['other'] }),
    }));
    expect(notAdmitted.valid).toBe(false);
    expect(notAdmitted.issues.some((issue) => issue.code === 'ACTION_NOT_ADMITTED')).toBe(true);

    const admittedButNotAssigned = evaluateCadpCapabilityConsumer(request({
      assignment: assignment({ assignedActionIds: [] }),
    }));
    expect(admittedButNotAssigned.valid).toBe(false);
    expect(admittedButNotAssigned.issues.some((issue) => issue.code === 'ACTION_NOT_ASSIGNED')).toBe(true);
  });

  it('requires the assignment record identity to match the committed grant', () => {
    const result = evaluateCadpCapabilityConsumer(request({
      assignment: assignment({ assignmentId: 'caller-selected-assignment' }),
    }));
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === 'CROSS_RECORD_MISMATCH' && issue.path === '$.assignment.assignmentId')).toBe(true);
  });

  it('requires compatibility evidence for the committed action', () => {
    const result = evaluateCadpCapabilityConsumer(request({
      evidence: evidence({ passingActionIds: ['unrelated-action'] }),
    }));
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === 'ACTION_NOT_EVIDENCED')).toBe(true);
  });

  it('does not consume an invocation when the chain is invalid; the same ID passes once valid', () => {
    const invocationId = `${runId}-invalid-then-valid`;
    const invalid = evaluateCadpCapabilityConsumer(request({
      distribution: distribution({ capabilityId: 'cvf.cadp.unrelated' }),
      observation: observation(invocationId),
    }));
    expect(invalid.valid).toBe(false);
    expect(invalid.projection.reconciled).toBe(false);

    const valid = evaluateCadpCapabilityConsumer(request({ observation: observation(invocationId) }));
    expect(valid.valid).toBe(true);
    expect(valid.projection.reconciled).toBe(true);
  });

  it('consumes a valid invocation exactly once and rejects the duplicate', () => {
    const invocationId = `${runId}-consume-once`;
    const first = evaluateCadpCapabilityConsumer(request({ observation: observation(invocationId) }));
    expect(first.valid).toBe(true);

    const duplicate = evaluateCadpCapabilityConsumer(request({ observation: observation(invocationId) }));
    expect(duplicate.valid).toBe(false);
    expect(duplicate.issues.some((issue) => issue.code === 'DUPLICATE_INVOCATION_REJECTED')).toBe(true);
  });

  it('does not let distribution or evidence widen action authority', () => {
    const wideEvidence = evaluateCadpCapabilityConsumer(request({
      evidence: evidence({ passingActionIds: [ACTION_ID, 'extra-write-action'] }),
    }));
    expect(wideEvidence.valid).toBe(true);
    expect(wideEvidence.projection.actionId).toBe(ACTION_ID);
    expect(wideEvidence.projection.executionAuthorized).toBe(false);

    const executionWidening = evaluateCadpCapabilityConsumer(request({
      distribution: { ...distribution(), distributionGrantsExecution: true } as unknown as CapabilityDistributionManifest,
    }));
    expect(executionWidening.valid).toBe(false);
    expect(executionWidening.projection.executionAuthorized).toBe(false);
  });

  it('returns deeply frozen output and nested collections', () => {
    const result = evaluateCadpCapabilityConsumer(request());
    expect(Object.isFrozen(result)).toBe(true);
    expect(Object.isFrozen(result.projection)).toBe(true);
    expect(Object.isFrozen(result.issues)).toBe(true);
    expect(() => {
      (result.projection as { executionAuthorized: boolean }).executionAuthorized = true;
    }).toThrow();
    expect(() => {
      (result.issues as CadpCapabilityConsumerIssue[]).push({} as CadpCapabilityConsumerIssue);
    }).toThrow();

    const invalid = evaluateCadpCapabilityConsumer(request({ ownerHandle: { contractVersion: 'x' } as unknown as CapabilityOwnerHandle }));
    expect(Object.isFrozen(invalid)).toBe(true);
    expect(Object.isFrozen(invalid.projection)).toBe(true);
    expect(Object.isFrozen(invalid.issues)).toBe(true);
  });

  it('rejects a request envelope carrying raw-secret-shaped material', () => {
    const secretShaped = { ...request(), rawSecret: 'sk-live-secret-token' };
    const result = evaluateCadpCapabilityConsumer(secretShaped as unknown as CadpCapabilityConsumerRequest);
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === 'MALFORMED_REQUEST')).toBe(true);
  });
});

describe('T3A SQLite narrow ignore hygiene', () => {
  const MODULE_DIRECTORY = dirname(fileURLToPath(import.meta.url));
  const REPO_ROOT = execFileSync(
    'git',
    ['-C', MODULE_DIRECTORY, 'rev-parse', '--show-toplevel'],
    { encoding: 'utf8', windowsHide: true },
  ).trim();

  function matchingIgnorePattern(relativePath: string): string | null {
    try {
      return execFileSync(
        'git',
        ['-C', REPO_ROOT, 'check-ignore', '-v', '--no-index', relativePath],
        { encoding: 'utf8', windowsHide: true, stdio: ['ignore', 'pipe', 'pipe'] },
      ).trim();
    } catch {
      return null;
    }
  }

  it('ignores the T2A SQLite DB/WAL/SHM files through the narrow committed patterns', () => {
    expect(matchingIgnorePattern('logs/capability-owner/cadp-owner.db')).toContain('/logs/capability-owner/*.db');
    expect(matchingIgnorePattern('logs/capability-owner/cadp-owner.db-wal')).toContain('/logs/capability-owner/*.db-wal');
    expect(matchingIgnorePattern('logs/capability-owner/cadp-owner.db-shm')).toContain('/logs/capability-owner/*.db-shm');
  });

  it('does not ignore unrelated logs or databases outside the narrow capability-owner scope', () => {
    expect(matchingIgnorePattern('logs/capability-owner/operator-notes.txt')).toBeNull();
    expect(matchingIgnorePattern('logs/unrelated/other.db')).toBeNull();
  });
});
