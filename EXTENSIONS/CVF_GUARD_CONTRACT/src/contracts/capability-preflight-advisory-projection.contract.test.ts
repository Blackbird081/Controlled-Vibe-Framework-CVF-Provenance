import { describe, expect, it } from 'vitest';
import {
  CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_CONTRACT_VERSION,
  evaluateCapabilityPreflightAdvisoryProjection,
  type CapabilityPreflightAdvisoryProjectionInput,
  type CapabilityPreflightAdvisoryProjectionResult,
} from './capability-preflight-advisory-projection.contract';
import {
  CAPABILITY_READINESS_DECISION_VERSION,
  CAPABILITY_ROUTE_DECISION_VERSION,
  type CapabilityReadinessDecision,
  type CapabilityRouteDecision,
} from './capability-route-readiness.contract';
import {
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION,
  type CapabilityBootstrapApprovalEvidenceBindingResult,
} from './capability-bootstrap-approval-evidence.contract';
import {
  CAPABILITY_CASE_EVIDENCE_PROJECTION_CONTRACT_VERSION,
  CAPABILITY_CASE_PROJECTION_VERSION,
  DOMAIN_EVIDENCE_PROJECTION_VERSION,
  type CapabilityCaseEvidenceProjection,
} from './capability-case-evidence-projection.contract';
import {
  CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION,
  type CapabilityEnvironmentSnapshotEvidenceResult,
} from './capability-environment-snapshot-evidence.contract';
import { evaluateCapabilityPreflightAdvisoryProjection as contractsBarrelEvaluator } from './index';
import { evaluateCapabilityPreflightAdvisoryProjection as rootBarrelEvaluator } from '../index';

const NOW = '2026-08-17T10:00:00Z';
const WORKSPACE_ID = 'workspace-demo';

function route(overrides: Partial<CapabilityRouteDecision> = {}): CapabilityRouteDecision {
  return {
    schemaVersion: CAPABILITY_ROUTE_DECISION_VERSION,
    routeDecisionId: 'route:req-t14',
    candidateSetId: 'cset-t14',
    requestId: 'req-t14',
    workspaceId: WORKSPACE_ID,
    stage: 'FAST_ROUTE',
    primary: { capabilityId: 'ripgrep.acquire', packageId: 'ripgrep', packageVersion: '14.1.1' },
    supporting: [],
    rejected: [],
    fallbacks: [],
    confidence: 0.95,
    ambiguityReasons: [],
    environmentSnapshotRefs: ['snap-t14-001'],
    authorityStatus: 'CANDIDATE_ONLY',
    executionAuthorized: false,
    generatedAt: '2026-08-17T09:00:00Z',
    issues: [],
    ...overrides,
  };
}

function readiness(overrides: Partial<CapabilityReadinessDecision> = {}): CapabilityReadinessDecision {
  return {
    schemaVersion: CAPABILITY_READINESS_DECISION_VERSION,
    readinessDecisionId: 'ready-t14-001',
    routeDecisionId: 'route:req-t14',
    snapshotId: 'snap-t14-001',
    state: 'READY',
    missingDependencies: [],
    approvalRequirements: [],
    blockingReasons: [],
    evidenceRefs: ['evidence-t14-001'],
    nextSafeAction: 'Bind the selected capability to SPEC and WORK ORDER before execution.',
    evaluatedAt: '2026-08-17T09:30:00Z',
    authorityStatus: 'EVIDENCE_ONLY',
    executionAuthorized: false,
    ...overrides,
  };
}

function environment(
  readinessValue: CapabilityReadinessDecision = readiness(),
  overrides: Partial<CapabilityEnvironmentSnapshotEvidenceResult> = {},
): CapabilityEnvironmentSnapshotEvidenceResult {
  const ready = readinessValue.state === 'READY' || readinessValue.state === 'READY_WITH_EXISTING_APPROVAL';
  return {
    schemaVersion: CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION,
    status: ready ? 'VALIDATED_READY_EVIDENCE' : 'VALIDATED_BLOCKED_EVIDENCE',
    routeDecisionId: readinessValue.routeDecisionId,
    snapshotId: readinessValue.snapshotId,
    workspaceId: WORKSPACE_ID,
    requiredDependencies: [],
    availableDependencies: [],
    blockingReasons: readinessValue.blockingReasons,
    issues: [],
    readiness: readinessValue,
    evaluatedAt: readinessValue.evaluatedAt,
    authorityStatus: 'EVIDENCE_ONLY',
    snapshotCollected: false,
    snapshotPersisted: false,
    environmentReadAuthorized: false,
    executionAuthorized: false,
    acquisitionAuthorized: false,
    mutationAuthorized: false,
    refreshAuthorized: false,
    taskAuthorityGranted: false,
    networkAuthorized: false,
    ...overrides,
  };
}

function approval(overrides: Partial<CapabilityBootstrapApprovalEvidenceBindingResult> = {}): CapabilityBootstrapApprovalEvidenceBindingResult {
  return {
    schemaVersion: CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION,
    disposition: 'VALIDATED_EVIDENCE',
    planId: 'plan-t14-001',
    planDigest: 'a'.repeat(64),
    approvalId: 'approval-t14-001',
    workspaceId: WORKSPACE_ID,
    actorId: 'operator-demo',
    workOrderId: null,
    replayCheckRequired: true,
    approvalIssued: false,
    executionAuthorized: false,
    acquisitionAuthorized: false,
    mutationAuthorized: false,
    taskAuthorityGranted: false,
    networkAuthorized: false,
    issues: [],
    ...overrides,
  };
}

function rejectedApproval(): CapabilityBootstrapApprovalEvidenceBindingResult {
  return {
    schemaVersion: CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION,
    disposition: 'REJECTED',
    replayCheckRequired: true,
    approvalIssued: false,
    executionAuthorized: false,
    acquisitionAuthorized: false,
    mutationAuthorized: false,
    taskAuthorityGranted: false,
    networkAuthorized: false,
    issues: [{ code: 'PLAN_EXPIRED', path: '$.plan.expiresAt', message: 'Plan is expired.' }],
  };
}

function caseEvidence(overrides: Partial<CapabilityCaseEvidenceProjection> = {}): CapabilityCaseEvidenceProjection {
  return {
    schemaVersion: CAPABILITY_CASE_EVIDENCE_PROJECTION_CONTRACT_VERSION,
    caseProjectionVersion: CAPABILITY_CASE_PROJECTION_VERSION,
    domainEvidenceProjectionVersion: DOMAIN_EVIDENCE_PROJECTION_VERSION,
    authorityNotice: 'PROJECTION_ONLY',
    authorityMutation: false,
    caseId: 'case-t14-001',
    requestId: 'req-t14',
    workspaceId: WORKSPACE_ID,
    workOrderId: null,
    projectionId: 'projection-t14-001',
    sourceRefs: ['evidence-t14-001'],
    staleness: 'CURRENT',
    currentDisposition: 'route ready for review',
    evidence: [{
      evidenceId: 'ev-1',
      sourceRef: 'docs/reviews/example.md',
      observation: 'ripgrep binary present in workspace cache.',
      observedAt: '2026-08-17T09:15:00Z',
      digest: 'a'.repeat(64),
      reproductionBoundary: 'local workspace only',
    }],
    findings: [{
      findingId: 'finding-1',
      claim: 'ripgrep 14.1.1 matches expected digest.',
      severity: 'INFO',
      confidence: 0.99,
      verificationState: 'VERIFIED',
      evidenceRefs: ['ev-1'],
      remediation: null,
    }],
    paths: [{
      pathId: 'path-1',
      steps: [
        { kind: 'DEMONSTRATED', description: 'Digest matched expected plan digest.', evidenceRef: 'ev-1' },
        { kind: 'INFERRED', description: 'Package version compatible with target platform.', evidenceRef: null },
      ],
    }],
    projectionDigest: 'b'.repeat(64),
    generatedAt: '2026-08-17T09:45:00Z',
    issues: [],
    ...overrides,
  };
}

function input(overrides: Partial<CapabilityPreflightAdvisoryProjectionInput> = {}): CapabilityPreflightAdvisoryProjectionInput {
  const readinessValue = overrides.readiness ?? readiness();
  return {
    schemaVersion: CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_CONTRACT_VERSION,
    route: route(),
    readiness: readinessValue,
    environment: environment(readinessValue),
    approval: null,
    caseEvidence: null,
    now: NOW,
    ...overrides,
  };
}

function clone<T>(value: T): T {
  return structuredClone(value);
}

function codes(result: CapabilityPreflightAdvisoryProjectionResult): string[] {
  return result.issues.map((issue) => issue.code);
}

const AUTHORITY_FIELDS = [
  'approvalAuthorityGranted', 'taskAuthorityGranted', 'activationAuthorityGranted',
  'executionAuthorityGranted', 'mutationAuthorityGranted', 'actionInvocationAuthorized',
] as const;

describe('capability preflight advisory operator projection', () => {
  it('exports the exact evaluator through both Guard Contract barrels', () => {
    expect(contractsBarrelEvaluator).toBe(evaluateCapabilityPreflightAdvisoryProjection);
    expect(rootBarrelEvaluator).toBe(evaluateCapabilityPreflightAdvisoryProjection);
  });

  it('accepts a valid composed route/readiness projection deterministically without mutating input', () => {
    const evidence = input();
    const before = clone(evidence);
    const first = evaluateCapabilityPreflightAdvisoryProjection(evidence);
    const second = evaluateCapabilityPreflightAdvisoryProjection(evidence);

    expect(first).toEqual(second);
    expect(evidence).toEqual(before);
    expect(first.status).toBe('ADVISORY_PROJECTION_READY');
    expect(first.route?.routeDecisionId).toBe('route:req-t14');
    expect(first.readiness?.state).toBe('READY');
    expect(first.readiness?.environmentStatus).toBe('VALIDATED_READY_EVIDENCE');
    expect(first.approvalBoundary).toEqual({ presence: 'ABSENT', planId: null, planDigest: null, approvalId: null });
    expect(first.evidence).toEqual({ presence: 'ABSENT', staleness: null, findings: [], paths: [] });
    expect(first.blocked).toBe(false);
    expect(first.nextSafeAction).toBe('Bind the selected capability to SPEC and WORK ORDER before execution.');
    expect(first.issues).toEqual([]);
    expect(Object.isFrozen(first)).toBe(true);
    expect(Object.isFrozen(first.issues)).toBe(true);
    for (const field of AUTHORITY_FIELDS) expect(first[field]).toBe(false);
  });

  it('accepts a fully composed projection including validated approval and case evidence', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ approval: approval(), caseEvidence: caseEvidence() }),
    );
    expect(result.status).toBe('ADVISORY_PROJECTION_READY');
    expect(result.approvalBoundary).toEqual({
      presence: 'PRESENT_VALIDATED', planId: 'plan-t14-001', planDigest: 'a'.repeat(64), approvalId: 'approval-t14-001',
    });
    expect(result.evidence?.presence).toBe('PRESENT');
    expect(result.evidence?.staleness).toBe('CURRENT');
    expect(result.evidence?.findings).toEqual([{
      findingId: 'finding-1', claim: 'ripgrep 14.1.1 matches expected digest.',
      verificationState: 'VERIFIED', evidenceRefs: ['ev-1'],
    }]);
    expect(result.evidence?.paths).toEqual([{
      pathId: 'path-1',
      steps: [
        { kind: 'DEMONSTRATED', description: 'Digest matched expected plan digest.', evidenceRef: 'ev-1' },
        { kind: 'INFERRED', description: 'Package version compatible with target platform.', evidenceRef: null },
      ],
    }]);
    expect(result.blocked).toBe(false);
  });

  it('marks a rejected approval as PRESENT_REJECTED and grants nothing', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(input({ approval: rejectedApproval() }));
    expect(result.status).toBe('ADVISORY_PROJECTION_READY');
    expect(result.approvalBoundary).toEqual({ presence: 'PRESENT_REJECTED', planId: null, planDigest: null, approvalId: null });
  });

  it('surfaces an ambiguous route and every blocked/unknown readiness class as visible, blocked advisory state', () => {
    const ambiguous = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: route({ stage: 'AMBIGUOUS_ROUTE', ambiguityReasons: ['RISK_LEVEL_DIFFERS'] }) }),
    );
    expect(ambiguous.status).toBe('ADVISORY_PROJECTION_READY');
    expect(ambiguous.route?.stage).toBe('AMBIGUOUS_ROUTE');
    expect(ambiguous.blocked).toBe(true);

    for (const state of ['BLOCKED_POLICY', 'BLOCKED_INTEGRITY', 'UNKNOWN', 'STALE_SNAPSHOT'] as const) {
      const result = evaluateCapabilityPreflightAdvisoryProjection(input({ readiness: readiness({ state }) }));
      expect(result.status).toBe('ADVISORY_PROJECTION_READY');
      expect(result.readiness?.state).toBe(state);
      expect(result.blocked).toBe(true);
    }
  });

  it('rejects a cross-boundary route/readiness routeDecisionId mismatch fail-closed', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ readiness: readiness({ routeDecisionId: 'route:other' }) }),
    );
    expect(result.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(result)).toContain('ROUTE_READINESS_BINDING_MISMATCH');
    expect(result.route).toBeNull();
  });

  it('rejects a readiness snapshot not referenced by the route fail-closed', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ readiness: readiness({ snapshotId: 'snap-other' }) }),
    );
    expect(result.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(result)).toContain('READINESS_ENVIRONMENT_BINDING_MISMATCH');
  });

  it('requires the accepted T10 environment result and exact route/readiness/workspace binding', () => {
    const missing = evaluateCapabilityPreflightAdvisoryProjection({ ...input(), environment: undefined });
    expect(missing.status).not.toBe('ADVISORY_PROJECTION_READY');

    const wrongRoute = evaluateCapabilityPreflightAdvisoryProjection(
      input({ environment: environment(readiness(), { routeDecisionId: 'route:other' }) }),
    );
    expect(codes(wrongRoute)).toContain('READINESS_ENVIRONMENT_BINDING_MISMATCH');

    const wrongWorkspace = evaluateCapabilityPreflightAdvisoryProjection(
      input({ environment: environment(readiness(), { workspaceId: 'workspace-other' }) }),
    );
    expect(codes(wrongWorkspace)).toContain('READINESS_ENVIRONMENT_BINDING_MISMATCH');
  });

  it('rejects a T10 rejected result and a T10 status that contradicts readiness', () => {
    const rejected = evaluateCapabilityPreflightAdvisoryProjection(input({
      environment: environment(readiness(), {
        status: 'REJECTED',
        readiness: null,
        issues: [{ code: 'INVALID_FIELD', path: '$.snapshot', message: 'invalid snapshot' }],
      }),
    }));
    expect(codes(rejected)).toContain('ENVIRONMENT_EVIDENCE_REJECTED');

    const contradictory = evaluateCapabilityPreflightAdvisoryProjection(input({
      environment: environment(readiness(), { status: 'VALIDATED_BLOCKED_EVIDENCE' }),
    }));
    expect(codes(contradictory)).toContain('READINESS_ENVIRONMENT_BINDING_MISMATCH');
  });

  it('rejects a validated approval bound to another workspace', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ approval: approval({ workspaceId: 'workspace-other' }) }),
    );
    expect(codes(result)).toContain('APPROVAL_BINDING_CONTRADICTION');
  });

  it('rejects a case-evidence workspace that does not match the route workspace', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ caseEvidence: caseEvidence({ workspaceId: 'workspace-other' }) }),
    );
    expect(result.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(result)).toContain('CASE_EVIDENCE_BINDING_CONTRADICTION');
  });

  it('missing optional approval and case evidence is explicit and grants nothing', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(input());
    expect(result.approvalBoundary?.presence).toBe('ABSENT');
    expect(result.evidence?.presence).toBe('ABSENT');
    for (const field of AUTHORITY_FIELDS) expect(result[field]).toBe(false);
  });

  it('never lets malformed approval or case evidence become valid or verified', () => {
    const badApproval = evaluateCapabilityPreflightAdvisoryProjection(
      input({ approval: { ...approval(), disposition: 'BOGUS' as never } }),
    );
    expect(badApproval.status).not.toBe('ADVISORY_PROJECTION_READY');

    const badCase = evaluateCapabilityPreflightAdvisoryProjection(
      input({ caseEvidence: { ...caseEvidence(), staleness: 'BOGUS' as never } }),
    );
    expect(badCase.status).not.toBe('ADVISORY_PROJECTION_READY');
  });

  it('rejects a validated approval result that still carries issues (contradiction)', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ approval: { ...approval(), issues: [{ code: 'NONCE_INVALID', path: '$.approval.replayNonce', message: 'bad nonce' }] } }),
    );
    expect(result.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(result)).toContain('APPROVAL_BINDING_CONTRADICTION');
  });

  it('requires a lowercase SHA-256 digest for validated approval evidence', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ approval: approval({ planDigest: 'not-a-digest' }) }),
    );
    expect(result.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(result)).toContain('APPROVAL_BINDING_CONTRADICTION');
  });

  it('requires validated approval evidence when readiness claims READY_WITH_EXISTING_APPROVAL', () => {
    const readinessValue = readiness({ state: 'READY_WITH_EXISTING_APPROVAL' });
    const absent = evaluateCapabilityPreflightAdvisoryProjection(input({ readiness: readinessValue }));
    expect(absent.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(absent)).toContain('APPROVAL_BINDING_CONTRADICTION');

    const accepted = evaluateCapabilityPreflightAdvisoryProjection(
      input({ readiness: readinessValue, approval: approval() }),
    );
    expect(accepted.status).toBe('ADVISORY_PROJECTION_READY');
  });

  it('rejects a rejected approval result that still carries identity fields (contradiction)', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ approval: { ...rejectedApproval(), planId: 'plan-should-not-be-here' } }),
    );
    expect(result.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(result)).toContain('APPROVAL_BINDING_CONTRADICTION');
  });

  it('does not coerce confidence or free text from strings/objects', () => {
    const stringConfidence = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: { ...route(), confidence: '0.9' as unknown as number } }),
    );
    expect(stringConfidence.status).not.toBe('ADVISORY_PROJECTION_READY');

    const objectConfidence = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: { ...route(), confidence: { valueOf: () => 0.9 } as unknown as number } }),
    );
    expect(objectConfidence.status).not.toBe('ADVISORY_PROJECTION_READY');
  });

  it('rejects duplicate IDs in supporting, environmentSnapshotRefs, and finding/path collections', () => {
    const dupSupporting = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: route({ supporting: ['a', 'a'] }) }),
    );
    expect(codes(dupSupporting)).toContain('DUPLICATE_VALUE');

    const dupSnapshotRefs = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: route({ environmentSnapshotRefs: ['snap-t14-001', 'snap-t14-001'] }) }),
    );
    expect(codes(dupSnapshotRefs)).toContain('DUPLICATE_VALUE');

    const dupFinding = evaluateCapabilityPreflightAdvisoryProjection(
      input({
        caseEvidence: caseEvidence({
          findings: [
            { findingId: 'finding-1', claim: 'a', severity: 'INFO', confidence: 0.5, verificationState: 'VERIFIED', evidenceRefs: [], remediation: null },
            { findingId: 'finding-1', claim: 'b', severity: 'INFO', confidence: 0.5, verificationState: 'VERIFIED', evidenceRefs: [], remediation: null },
          ],
        }),
      }),
    );
    expect(dupFinding.status).not.toBe('ADVISORY_PROJECTION_READY');
  });

  it('rejects sparse arrays and excessive sizes', () => {
    const sparse: unknown[] = [];
    sparse[3] = 'a';
    const sparseResult = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: { ...route(), supporting: sparse } as unknown as CapabilityRouteDecision }),
    );
    expect(sparseResult.status).not.toBe('ADVISORY_PROJECTION_READY');

    const oversized = Array.from({ length: 200 }, (_, i) => `dep-${i}`);
    const oversizedResult = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: route({ supporting: oversized }) }),
    );
    expect(oversizedResult.status).not.toBe('ADVISORY_PROJECTION_READY');
  });

  it.each([
    ['null', null],
    ['array', []],
    ['class', new (class Envelope {})()],
    ['string', 'not-an-object'],
  ])('rejects a malformed %s envelope without throwing', (_label, value) => {
    expect(() => evaluateCapabilityPreflightAdvisoryProjection(value)).not.toThrow();
    expect(evaluateCapabilityPreflightAdvisoryProjection(value).status).toBe('ADVISORY_PROJECTION_BLOCKED');
  });

  it('rejects unknown keys at top level and every nested level', () => {
    const topLevel = evaluateCapabilityPreflightAdvisoryProjection({ ...input(), extra: true });
    expect(topLevel.status).toBe('ADVISORY_PROJECTION_BLOCKED');
    expect(codes(topLevel)).toContain('UNKNOWN_KEY');

    const nested = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: { ...route(), extra: true } as unknown as CapabilityRouteDecision }),
    );
    expect(nested.status).not.toBe('ADVISORY_PROJECTION_READY');
    expect(codes(nested)).toContain('UNKNOWN_KEY');
  });

  it('getter-throwing and revoked-Proxy objects/arrays never escape as exceptions', () => {
    let invoked = 0;
    const proxied = new Proxy(input(), { get() { invoked += 1; throw new Error('must not run'); } });
    expect(() => evaluateCapabilityPreflightAdvisoryProjection(proxied)).not.toThrow();
    expect(evaluateCapabilityPreflightAdvisoryProjection(proxied).status).toBe('ADVISORY_PROJECTION_BLOCKED');

    const accessor = input() as unknown as Record<string, unknown>;
    Object.defineProperty(accessor, 'now', { enumerable: true, get() { invoked += 1; throw new Error('must not run'); } });
    expect(() => evaluateCapabilityPreflightAdvisoryProjection(accessor)).not.toThrow();
    expect(evaluateCapabilityPreflightAdvisoryProjection(accessor).status).toBe('ADVISORY_PROJECTION_BLOCKED');

    const revokedHandle = Proxy.revocable([], {});
    revokedHandle.revoke();
    const withRevokedArray = input({ route: { ...route(), supporting: revokedHandle.proxy as unknown as string[] } });
    expect(() => evaluateCapabilityPreflightAdvisoryProjection(withRevokedArray)).not.toThrow();
    expect(evaluateCapabilityPreflightAdvisoryProjection(withRevokedArray).status).not.toBe('ADVISORY_PROJECTION_READY');

    expect(invoked).toBe(0);
  });

  it('rejects secret-like content at free-text boundaries', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ readiness: readiness({ nextSafeAction: 'api_key=abcdef123456' }) }),
    );
    expect(result.status).not.toBe('ADVISORY_PROJECTION_READY');
    expect(codes(result)).toContain('RAW_SECRET_DETECTED');
    expect(JSON.stringify(result)).not.toContain('abcdef123456');
  });

  it('rejects control/NUL-character-bearing strings', () => {
    const bad = 'route' + String.fromCharCode(0) + 'id';
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: route({ routeDecisionId: bad }) }),
    );
    expect(result.status).not.toBe('ADVISORY_PROJECTION_READY');
    expect(codes(result)).toContain('UNSAFE_STRING');
  });

  it('rejects stale readiness evidence relative to now', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ now: '2026-08-19T10:00:00Z' }),
    );
    expect(result.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(result)).toContain('STALE_EVIDENCE_TIME');
  });

  it('does not elevate: an UNVERIFIED finding stays UNVERIFIED in the projection', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({
        caseEvidence: caseEvidence({
          findings: [{
            findingId: 'finding-2', claim: 'unverified claim', severity: 'LOW', confidence: 0.2,
            verificationState: 'UNVERIFIED', evidenceRefs: [], remediation: null,
          }],
        }),
      }),
    );
    expect(result.status).toBe('ADVISORY_PROJECTION_READY');
    expect(result.evidence?.findings[0]?.verificationState).toBe('UNVERIFIED');
  });

  it('keeps stale or invalid case evidence visibly blocked without elevating it', () => {
    for (const staleness of ['STALE', 'INVALID'] as const) {
      const result = evaluateCapabilityPreflightAdvisoryProjection(
        input({ caseEvidence: caseEvidence({ staleness }) }),
      );
      expect(result.status).toBe('ADVISORY_PROJECTION_READY');
      expect(result.blocked).toBe(true);
      expect(result.evidence?.staleness).toBe(staleness);
    }
  });

  it('keeps accepted case evidence with owner-reported issues visibly blocked', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(input({
      caseEvidence: caseEvidence({
        issues: [{ code: 'STALE_EVIDENCE', path: '$.evidence', message: 'Evidence requires refresh.' }],
      }),
    }));
    expect(result.status).toBe('ADVISORY_PROJECTION_READY');
    expect(result.blocked).toBe(true);
  });

  it('rejects dangling finding and path-step evidence references', () => {
    const finding = evaluateCapabilityPreflightAdvisoryProjection(input({
      caseEvidence: caseEvidence({
        findings: [{
          findingId: 'finding-1', claim: 'dangling evidence', severity: 'LOW', confidence: 0.5,
          verificationState: 'UNVERIFIED', evidenceRefs: ['missing-evidence'], remediation: null,
        }],
      }),
    }));
    expect(finding.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(finding)).toContain('CASE_EVIDENCE_BINDING_CONTRADICTION');

    const path = evaluateCapabilityPreflightAdvisoryProjection(input({
      caseEvidence: caseEvidence({
        paths: [{ pathId: 'path-1', steps: [{ kind: 'DEMONSTRATED', description: 'dangling', evidenceRef: 'missing-evidence' }] }],
      }),
    }));
    expect(path.status).toBe('ADVISORY_PROJECTION_REJECTED');
    expect(codes(path)).toContain('CASE_EVIDENCE_BINDING_CONTRADICTION');
  });

  it('rejects a huge sparse array by its bound without iterating its declared length', () => {
    const huge: unknown[] = [];
    huge.length = 0xfffffff0;
    const result = evaluateCapabilityPreflightAdvisoryProjection(
      input({ route: { ...route(), supporting: huge } as unknown as CapabilityRouteDecision }),
    );
    expect(codes(result)).toContain('UNBOUNDED_COLLECTION');
  });

  it('keeps next-safe-action as inert text with all authority/action flags false', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(input());
    expect(typeof result.nextSafeAction).toBe('string');
    for (const field of AUTHORITY_FIELDS) expect(result[field]).toBe(false);
  });

  it('always reports every authority/action field as literal false, including on acceptance/rejection/block', () => {
    const accepted = evaluateCapabilityPreflightAdvisoryProjection(input());
    const rejected = evaluateCapabilityPreflightAdvisoryProjection(input({ readiness: readiness({ snapshotId: 'snap-other' }) }));
    const blocked = evaluateCapabilityPreflightAdvisoryProjection(null);
    for (const result of [accepted, rejected, blocked]) {
      for (const field of AUTHORITY_FIELDS) expect(result[field]).toBe(false);
    }
  });

  it('produces a deeply frozen result whose nested arrays cannot be mutated', () => {
    const result = evaluateCapabilityPreflightAdvisoryProjection(input({ caseEvidence: caseEvidence() }));
    expect(Object.isFrozen(result.issues)).toBe(true);
    expect(Object.isFrozen(result.route)).toBe(true);
    expect(Object.isFrozen(result.evidence)).toBe(true);
    expect(() => { (result as { nextSafeAction: string }).nextSafeAction = 'hacked'; }).toThrow();
    expect(() => { (result.issues as unknown as unknown[]).push({}); }).toThrow();
  });

  it('does not mutate the caller-supplied nested route/readiness/approval/case-evidence inputs across repeated evaluation', () => {
    const evidence = input({ approval: approval(), caseEvidence: caseEvidence() });
    const before = clone(evidence);
    evaluateCapabilityPreflightAdvisoryProjection(evidence);
    evaluateCapabilityPreflightAdvisoryProjection(evidence);
    expect(evidence).toEqual(before);
  });
});
