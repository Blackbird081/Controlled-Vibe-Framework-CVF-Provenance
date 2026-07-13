import { createHash } from 'node:crypto';
import { describe, expect, it } from 'vitest';
import { DeterministicClock, SequentialIdFactory } from 'cvf-refinery';
import {
  evaluateSot3KnowledgeActivation,
  resolveSot3KnowledgeActivationMode,
  type Sot3KnowledgeChunkInput,
} from './sot3-knowledge-adapter';
import type { Sot3KnowledgeSourceMetadata } from './knowledge-store';

/** Mirrors cvf-refinery's integrityStage.computeContentHash exactly. */
function computeExpectedContentHash(records: Array<Record<string, unknown>>): string {
  const sorted = records.map((record) => {
    const keys = Object.keys(record).sort();
    return keys.map((key) => [key, record[key]]);
  });
  return `sha256:${createHash('sha256').update(JSON.stringify(sorted)).digest('hex')}`;
}

function buildValidChunk(overrides: Partial<Sot3KnowledgeSourceMetadata> = {}): Sot3KnowledgeChunkInput {
  const sourceId = overrides.sourceId ?? 'src-001';
  const content = 'Governed knowledge chunk content';
  const rawRecord = { source_id: sourceId, id: 'chunk-001', content };
  const meta: Sot3KnowledgeSourceMetadata = {
    sourceId,
    sourceType: 'INTERNAL',
    owner: 'team-eng',
    capturedAtUtc: '2026-07-13T00:00:00.000Z',
    purpose: ['execute-route-context'],
    confidentiality: 'INTERNAL',
    expectedContentHash: computeExpectedContentHash([rawRecord]),
    rawReference: { type: 'object', location: 'knowledge-store://chunk-001' },
    captureStatus: 'CAPTURED',
    declaredVersion: null,
    validFromUtc: null,
    validUntilUtc: null,
    ...overrides,
  };
  return { id: 'chunk-001', content, collectionId: 'col-1', sot3Source: meta };
}

function buildInputBase() {
  return {
    organization: 'org_a',
    team: 'team_a',
    actorId: 'usr_a',
    requestId: 'req-1',
    policyVersion: 'v1',
    ruleVersion: 'v1',
    clock: new DeterministicClock('2026-07-13T00:00:00.000Z', 1000),
    ids: new SequentialIdFactory(),
  };
}

describe('resolveSot3KnowledgeActivationMode', () => {
  it('resolves missing value to OFF', () => {
    expect(resolveSot3KnowledgeActivationMode(undefined)).toBe('OFF');
  });

  it('resolves empty value to OFF', () => {
    expect(resolveSot3KnowledgeActivationMode('')).toBe('OFF');
  });

  it('resolves invalid value to OFF', () => {
    expect(resolveSot3KnowledgeActivationMode('BOGUS')).toBe('OFF');
  });

  it('resolves SHADOW and ENFORCE', () => {
    expect(resolveSot3KnowledgeActivationMode('SHADOW')).toBe('SHADOW');
    expect(resolveSot3KnowledgeActivationMode('ENFORCE')).toBe('ENFORCE');
  });
});

describe('evaluateSot3KnowledgeActivation', () => {
  it('returns NO_CONTEXT with no chunks', () => {
    const result = evaluateSot3KnowledgeActivation({ ...buildInputBase(), chunks: [] }, 'ENFORCE');
    expect(result.terminalOutcome).toBe('NO_CONTEXT');
    expect(result.injectionPermitted).toBe(false);
    expect(result.approvedContext).toBeNull();
    expect(result.failureStage).toBe('NO_CHUNKS');
  });

  it('rejects with MISSING_PROVENANCE when sot3Source is absent', () => {
    const chunk: Sot3KnowledgeChunkInput = { id: 'c1', content: 'x', collectionId: 'col-1', sot3Source: undefined };
    const result = evaluateSot3KnowledgeActivation({ ...buildInputBase(), chunks: [chunk] }, 'ENFORCE');
    expect(result.terminalOutcome).toBe('REJECTED');
    expect(result.failureStage).toBe('MISSING_PROVENANCE');
    expect(result.injectionPermitted).toBe(false);
    expect(result.approvedContext).toBeNull();
  });

  it('approves valid provenance through Refinery, Kernel, and Flow in ENFORCE', () => {
    const chunk = buildValidChunk();
    const result = evaluateSot3KnowledgeActivation({ ...buildInputBase(), chunks: [chunk] }, 'ENFORCE');
    expect(result.terminalOutcome).toBe('APPROVED');
    expect(result.injectionPermitted).toBe(true);
    expect(result.approvedContext).toContain('Governed knowledge chunk content');
    expect(result.failureStage).toBeNull();
    expect(result.refineryStatus).toBe('READY_FOR_KERNEL');
    expect(result.kernelDecision).toBe('ACCEPT_EVIDENCE_CANDIDATE');
    expect(result.truthReferenceId).toBeTruthy();
    expect(result.flowPackageId).toBeTruthy();
    expect(result.flowAcknowledgementState).toBe('ACKNOWLEDGED');
  });

  it('does not permit injection in SHADOW even when approved', () => {
    const chunk = buildValidChunk();
    const result = evaluateSot3KnowledgeActivation({ ...buildInputBase(), chunks: [chunk] }, 'SHADOW');
    expect(result.terminalOutcome).toBe('APPROVED');
    expect(result.injectionPermitted).toBe(false);
  });

  it('rejects with REFINERY_NOT_READY on incorrect expected content hash', () => {
    const chunk = buildValidChunk({ expectedContentHash: 'sha256:0000000000000000000000000000000000000000000000000000000000000000' });
    const result = evaluateSot3KnowledgeActivation({ ...buildInputBase(), chunks: [chunk] }, 'ENFORCE');
    expect(result.terminalOutcome).toBe('REJECTED');
    expect(result.failureStage).toBe('REFINERY_NOT_READY');
    expect(result.injectionPermitted).toBe(false);
    expect(result.approvedContext).toBeNull();
  });

  it('rejects with KERNEL_NOT_ACCEPTED when provenance is captured as REJECTED_AT_INTAKE', () => {
    const rawRecord = { source_id: 'src-003', id: 'chunk-001', content: 'Governed knowledge chunk content' };
    const chunk = buildValidChunk({
      sourceId: 'src-003',
      captureStatus: 'REJECTED_AT_INTAKE',
      expectedContentHash: computeExpectedContentHash([rawRecord]),
    });
    const result = evaluateSot3KnowledgeActivation({ ...buildInputBase(), chunks: [chunk] }, 'ENFORCE');
    expect(result.terminalOutcome).toBe('REJECTED');
    expect(result.failureStage).toBe('KERNEL_NOT_ACCEPTED');
    expect(result.kernelDecision).toBe('REJECT');
    expect(result.injectionPermitted).toBe(false);
    expect(result.approvedContext).toBeNull();
  });

  it('registers evidence for every source included in approved context', () => {
    const first = buildValidChunk();
    const secondContent = 'Second source content must not bypass Kernel evidence checks';
    const secondRecord = { source_id: 'src-002', id: 'chunk-002', content: secondContent };
    const second: Sot3KnowledgeChunkInput = {
      id: 'chunk-002',
      content: secondContent,
      collectionId: 'col-1',
      sot3Source: {
        ...first.sot3Source!,
        sourceId: 'src-002',
        expectedContentHash: computeExpectedContentHash([secondRecord]),
        rawReference: { type: 'object', location: 'knowledge-store://chunk-002' },
      },
    };

    const result = evaluateSot3KnowledgeActivation(
      { ...buildInputBase(), chunks: [first, second] },
      'ENFORCE',
    );

    expect(result.terminalOutcome).toBe('APPROVED');
    expect(result.kernelEvidenceCount).toBe(2);
    expect(result.approvedContext).toContain(first.content);
    expect(result.approvedContext).toContain(second.content);
  });

  it('fails closed when the Truth Reference is no longer active before Flow creation', () => {
    const chunk = buildValidChunk();
    const input = {
      ...buildInputBase(),
      chunks: [chunk],
      clock: new DeterministicClock('2026-07-13T00:00:00.000Z', 10 * 60 * 1000),
    };

    const result = evaluateSot3KnowledgeActivation(input, 'ENFORCE');

    expect(result.terminalOutcome).toBe('REJECTED');
    expect(result.failureStage).toBe('FLOW_NOT_CREATED');
    expect(result.injectionPermitted).toBe(false);
    expect(result.approvedContext).toBeNull();
  });

  it('never returns raw chunk content in approvedContext field name when rejected', () => {
    const chunk = buildValidChunk({ expectedContentHash: 'sha256:bad' });
    const result = evaluateSot3KnowledgeActivation({ ...buildInputBase(), chunks: [chunk] }, 'ENFORCE');
    expect(result.approvedContext).toBeNull();
  });
});
