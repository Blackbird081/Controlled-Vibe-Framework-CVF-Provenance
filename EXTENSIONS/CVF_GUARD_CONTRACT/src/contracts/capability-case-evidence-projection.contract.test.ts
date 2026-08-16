import { describe, expect, it } from 'vitest';
import { projectCapabilityCaseEvidence, type CapabilityCaseProjectionInput, type DomainEvidenceProjectionInput } from './capability-case-evidence-projection.contract';
import { evaluateCapabilityRoute, evaluateCapabilityReadiness, type CapabilityCandidateSet } from './capability-route-readiness.contract';

const NOW = '2026-08-16T10:00:00Z';

function candidateSet(): CapabilityCandidateSet {
  return {
    candidateSetId: 'cset-1', requestId: 'request-1', workspaceId: 'workspace-1',
    candidates: [{
      capabilityId: 'git.read', packageId: 'cvf.git-read', packageVersion: '1.0.0', score: 0.9,
      reasons: ['TASK_CLASS_MATCH'], riskLevel: 'R0', dependencies: [], conflicts: [],
      credentialScopeRefs: [], networkDestinations: [], mutationKinds: [], irreversibleEffects: false,
      publicOrHumanEffects: false,
    }],
    generatedAt: '2026-08-16T09:59:00Z',
  };
}

function route() {
  return evaluateCapabilityRoute(candidateSet(), { now: NOW });
}

function readiness() {
  return evaluateCapabilityReadiness(route(), {
    readinessDecisionId: 'ready-1', snapshotId: 'snapshot-1', snapshotObservedAt: '2026-08-16T09:55:00Z',
    snapshotExpiresAt: '2026-08-16T10:05:00Z', requiredDependencies: [], availableDependencies: [],
    approvalRequired: false, existingApprovalValid: false, policyAllowed: true, provenanceVerified: true,
    integrityVerified: true, compatible: true, credentialsReady: true, networkReady: true, sandboxReady: true,
    evidenceRefs: ['snapshot:snapshot-1'],
  }, NOW);
}

function caseInput(overrides: Partial<CapabilityCaseProjectionInput> = {}): CapabilityCaseProjectionInput {
  return {
    caseId: 'case-1', requestId: 'request-1', workspaceId: 'workspace-1', workOrderId: null,
    route: route(), readiness: readiness(),
    acquisitionAuthorization: null, acquisitionAuthorizationRef: null,
    acquisitionReceipt: null, acquisitionReceiptRef: null,
    sourceObservedAt: '2026-08-16T09:55:00Z', sourceExpiresAt: '2026-08-16T10:05:00Z',
    ...overrides,
  };
}

function domainInput(overrides: Partial<DomainEvidenceProjectionInput> = {}): DomainEvidenceProjectionInput {
  return {
    projectionId: 'proj-1',
    evidence: [{ evidenceId: 'ev-1', sourceRef: 'route:route:request-1', observation: 'route resolved', observedAt: '2026-08-16T09:59:00Z', digest: null, reproductionBoundary: null }],
    findings: [{ findingId: 'f-1', claim: 'route is deterministic', severity: 'LOW', confidence: 0.9, evidenceRefs: ['ev-1'], remediation: null }],
    paths: [{ pathId: 'p-1', steps: [{ kind: 'DEMONSTRATED', description: 'evaluated route', evidenceRef: 'ev-1' }] }],
    ...overrides,
  };
}

describe('capability case and domain evidence projection kernel', () => {
  it('projects a valid case without acquisition evidence as projection-only', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput(), NOW);
    expect(result.authorityNotice).toBe('PROJECTION_ONLY');
    expect(result.authorityMutation).toBe(false);
    expect(result.staleness).toBe('CURRENT');
    expect(result.issues).toEqual([]);
    expect(result.sourceRefs).toEqual(expect.arrayContaining([expect.stringContaining('route:'), expect.stringContaining('readiness:'), expect.stringContaining('snapshot:')]));
  });

  it('binds optional controlled-acquisition authorization and receipt results', () => {
    const authorization = { contractVersion: 'cvf.controlledAcquisition.v1' as const, decision: 'DENIED' as const, issues: [] };
    const receipt = { status: 'FAIL' as const, issues: [] };
    const result = projectCapabilityCaseEvidence(caseInput({
      acquisitionAuthorization: authorization, acquisitionAuthorizationRef: 'authorization:auth-1',
      acquisitionReceipt: receipt, acquisitionReceiptRef: 'receipt:receipt-1',
    }), domainInput(), NOW);
    expect(result.sourceRefs).toEqual(expect.arrayContaining([expect.stringContaining('acquisitionAuthorization:'), expect.stringContaining('acquisitionReceipt:')]));
    expect(result.issues).toEqual([]);
  });

  it('fails closed without throwing on a malformed case input', () => {
    expect(() => projectCapabilityCaseEvidence(null as any, domainInput(), NOW)).not.toThrow();
    const result = projectCapabilityCaseEvidence(null as any, domainInput(), NOW);
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'INVALID_FIELD' })]));
    expect(result.authorityMutation).toBe(false);
  });

  it('fails closed without throwing on a malformed domain input', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), undefined as any, NOW);
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'MALFORMED_INPUT' })]));
  });

  it('fails closed without throwing on a Proxy input', () => {
    const trap = new Proxy({}, { get() { throw new Error('adversarial getter'); } });
    expect(() => projectCapabilityCaseEvidence(trap as any, domainInput(), NOW)).not.toThrow();
    const result = projectCapabilityCaseEvidence(trap as any, domainInput(), NOW);
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'MALFORMED_INPUT' })]));
  });

  it('fails closed without throwing on a throwing-getter evidence entry', () => {
    const throwing = {};
    Object.defineProperty(throwing, 'observation', { get() { throw new Error('boom'); }, enumerable: true });
    expect(() => projectCapabilityCaseEvidence(caseInput(), domainInput({ evidence: [throwing as any] }), NOW)).not.toThrow();
  });

  it('fails closed without throwing when an accessed case field is a getter', () => {
    const hostile = { ...caseInput() } as any;
    Object.defineProperty(hostile, 'caseId', { get() { throw new Error('case getter'); }, enumerable: true });
    expect(() => projectCapabilityCaseEvidence(hostile, domainInput(), NOW)).not.toThrow();
    expect(projectCapabilityCaseEvidence(hostile, domainInput(), NOW).currentDisposition).toBe('INVALID');
  });

  it('fails closed without throwing when acquisition evidence has an accessor', () => {
    const hostile = {} as any;
    Object.defineProperty(hostile, 'decision', { get() { throw new Error('decision getter'); }, enumerable: true });
    expect(() => projectCapabilityCaseEvidence(caseInput({ acquisitionAuthorization: hostile }), domainInput(), NOW)).not.toThrow();
    expect(projectCapabilityCaseEvidence(caseInput({ acquisitionAuthorization: hostile }), domainInput(), NOW).currentDisposition).toBe('INVALID');
  });

  it('fails closed when optional acquisition evidence lacks its exact source reference', () => {
    const authorization = { contractVersion: 'cvf.controlledAcquisition.v1' as const, decision: 'DENIED' as const, issues: [] };
    const result = projectCapabilityCaseEvidence(caseInput({ acquisitionAuthorization: authorization }), domainInput(), NOW);
    expect(result.currentDisposition).toBe('INVALID');
    expect(result.sourceRefs.some((ref) => ref.startsWith('acquisitionAuthorization:'))).toBe(false);
  });

  it('reports STALE when now is at or after sourceExpiresAt', () => {
    const result = projectCapabilityCaseEvidence(caseInput({ sourceExpiresAt: NOW }), domainInput(), NOW);
    expect(result.staleness).toBe('STALE');
    expect(result.currentDisposition).toBe('STALE');
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'STALE_SOURCE' })]));
  });

  it('reports INVALID staleness for malformed timestamps and never reports CURRENT for bad input', () => {
    const result = projectCapabilityCaseEvidence(caseInput({ sourceObservedAt: 'not-a-date' }), domainInput(), NOW);
    expect(result.staleness).toBe('INVALID');
    expect(result.staleness).not.toBe('CURRENT');
  });

  it('marks a finding with a missing evidence reference as UNVERIFIED and non-current, not silently dropped', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput({
      findings: [{ findingId: 'f-2', claim: 'unsupported claim', severity: 'HIGH', confidence: 0.5, evidenceRefs: ['missing-ev'], remediation: null }],
    }), NOW);
    expect(result.findings[0].verificationState).toBe('UNVERIFIED');
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'UNVERIFIED_FINDING_REFERENCE' })]));
    expect(result.currentDisposition).toBe('INVALID');
  });

  it('downgrades an unsupported demonstrated path step to INFERRED', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput({
      paths: [{ pathId: 'p-2', steps: [{ kind: 'DEMONSTRATED', description: 'claimed but unproven', evidenceRef: 'missing-ev' }] }],
    }), NOW);
    expect(result.paths[0].steps[0].kind).toBe('INFERRED');
  });

  it('keeps a demonstrated step demonstrated only when its evidence reference resolves', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput(), NOW);
    expect(result.paths[0].steps[0].kind).toBe('DEMONSTRATED');
  });

  it('rejects a secret-like evidence observation without echoing it', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput({
      evidence: [{ evidenceId: 'ev-2', sourceRef: 'route:x', observation: 'api_key=sk-live-abcdef', observedAt: NOW, digest: null, reproductionBoundary: null }],
    }), NOW);
    expect(result.evidence).toEqual([]);
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'SECRET_LIKE_VALUE_REJECTED' })]));
    expect(JSON.stringify(result)).not.toContain('sk-live-abcdef');
    expect(result.currentDisposition).toBe('INVALID');
  });

  it('rejects a standalone provider-key-shaped value without echoing it', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput({
      evidence: [{ evidenceId: 'ev-2', sourceRef: 'route:x', observation: 'sk-live-abcdefghijk', observedAt: NOW, digest: null, reproductionBoundary: null }],
    }), NOW);
    expect(result.evidence).toEqual([]);
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'SECRET_LIKE_VALUE_REJECTED' })]));
    expect(JSON.stringify(result)).not.toContain('sk-live-abcdefghijk');
  });

  it('rejects a secret-like finding claim without echoing it', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput({
      findings: [{ findingId: 'f-3', claim: 'bearer token=xyz-secret-value', severity: 'LOW', confidence: 0.5, evidenceRefs: [], remediation: null }],
    }), NOW);
    expect(result.findings).toEqual([]);
    expect(JSON.stringify(result)).not.toContain('xyz-secret-value');
  });

  it('rejects a secret-like nested remediation string without echoing it', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput({
      findings: [{ findingId: 'f-4', claim: 'safe claim', severity: 'LOW', confidence: 0.5, evidenceRefs: ['ev-1'], remediation: 'rotate password=hunter2' }],
    }), NOW);
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'SECRET_LIKE_VALUE_REJECTED' })]));
    expect(JSON.stringify(result)).not.toContain('hunter2');
  });

  it('produces an identical canonical digest for equivalent reordered input', () => {
    const evidence = [
      ...domainInput().evidence,
      { evidenceId: 'ev-2', sourceRef: 'readiness:ready-1', observation: 'readiness resolved', observedAt: NOW, digest: null, reproductionBoundary: null },
    ];
    const findings = [
      ...domainInput().findings,
      { findingId: 'f-2', claim: 'readiness is evidence only', severity: 'MEDIUM' as const, confidence: 0.8, evidenceRefs: ['ev-2'], remediation: null },
    ];
    const paths = [
      ...domainInput().paths,
      { pathId: 'p-2', steps: [{ kind: 'DEMONSTRATED' as const, description: 'evaluated readiness', evidenceRef: 'ev-2' }] },
    ];
    const a = projectCapabilityCaseEvidence(caseInput(), domainInput({ evidence, findings, paths }), NOW);
    const b = projectCapabilityCaseEvidence(caseInput(), domainInput({
      evidence: [...evidence].reverse(), findings: [...findings].reverse(), paths: [...paths].reverse(),
    }), NOW);
    expect(a.projectionDigest).toBe(b.projectionDigest);
    expect(a.evidence.map(({ evidenceId }) => evidenceId)).toEqual(['ev-1', 'ev-2']);
    expect(b.evidence.map(({ evidenceId }) => evidenceId)).toEqual(['ev-1', 'ev-2']);
  });

  it('fails closed for route/readiness lookalikes that omit canonical authority invariants', () => {
    const result = projectCapabilityCaseEvidence(caseInput({
      route: { routeDecisionId: 'route-x' } as any,
      readiness: { readinessDecisionId: 'ready-x', snapshotId: 'snapshot-x', state: 'READY' } as any,
    }), domainInput(), NOW);
    expect(result.currentDisposition).toBe('INVALID');
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'INVALID_FIELD' })]));
  });

  it('fails closed when a top-level collection exceeds its bound', () => {
    const evidence = Array.from({ length: 257 }, (_, index) => ({
      evidenceId: `ev-${index}`, sourceRef: `source:${index}`, observation: 'bounded observation', observedAt: NOW,
    }));
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput({ evidence }), NOW);
    expect(result.currentDisposition).toBe('INVALID');
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'INVALID_FIELD' })]));
  });

  it('produces a different digest when an authority-relevant input changes', () => {
    const a = projectCapabilityCaseEvidence(caseInput(), domainInput(), NOW);
    const b = projectCapabilityCaseEvidence(caseInput({ workOrderId: 'wo-1' }), domainInput(), NOW);
    expect(a.projectionDigest).not.toBe(b.projectionDigest);
  });

  it('never represents a material route/readiness state as authorization', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput(), NOW);
    expect(result.authorityMutation).toBe(false);
    expect(result.authorityNotice).toBe('PROJECTION_ONLY');
    expect(JSON.stringify(result)).not.toMatch(/"executionAuthorized"\s*:\s*true/);
  });

  it('detects duplicate evidence, finding, and path identifiers', () => {
    const result = projectCapabilityCaseEvidence(caseInput(), domainInput({
      evidence: [domainInput().evidence[0], domainInput().evidence[0]],
    }), NOW);
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'DUPLICATE_EVIDENCE_ID' })]));
  });

  it('rejects a non-array evidence/findings/paths field without throwing', () => {
    expect(() => projectCapabilityCaseEvidence(caseInput(), { projectionId: 'p', evidence: null, findings: [], paths: [] } as any, NOW)).not.toThrow();
    const result = projectCapabilityCaseEvidence(caseInput(), { projectionId: 'p', evidence: null, findings: [], paths: [] } as any, NOW);
    expect(result.issues).toEqual(expect.arrayContaining([expect.objectContaining({ code: 'INVALID_FIELD' })]));
  });

  it('is frozen and resists mutation attempts', () => {
    const result: any = projectCapabilityCaseEvidence(caseInput(), domainInput(), NOW);
    let threw = false;
    try { result.authorityMutation = true; } catch { threw = true; }
    expect(threw).toBe(true);
    expect(result.authorityMutation).toBe(false);
    expect(Object.isFrozen(result)).toBe(true);
  });

  it('does not use an ambient clock; identical now yields identical generatedAt and digest', () => {
    const a = projectCapabilityCaseEvidence(caseInput(), domainInput(), NOW);
    const b = projectCapabilityCaseEvidence(caseInput(), domainInput(), NOW);
    expect(a.generatedAt).toBe(NOW);
    expect(a.generatedAt).toBe(b.generatedAt);
    expect(a.projectionDigest).toBe(b.projectionDigest);
  });
});
