import { describe, expect, it } from 'vitest';
import {
  evaluateCapabilityReadiness,
  evaluateCapabilityRoute,
  type CapabilityCandidateSet,
  type CapabilityReadinessInput,
  type CapabilityRouteCandidate,
} from './capability-route-readiness.contract';

const NOW = '2026-08-16T10:00:00Z';

function candidate(overrides: Partial<CapabilityRouteCandidate> = {}): CapabilityRouteCandidate {
  return {
    capabilityId: 'git.read', packageId: 'cvf.git-read', packageVersion: '1.0.0', score: 0.9,
    reasons: ['TASK_CLASS_MATCH'], riskLevel: 'R0', dependencies: [], conflicts: [],
    credentialScopeRefs: [], networkDestinations: [], mutationKinds: [], irreversibleEffects: false,
    publicOrHumanEffects: false, ...overrides,
  };
}

function candidateSet(candidates = [candidate()]): CapabilityCandidateSet {
  return { candidateSetId: 'cset-1', requestId: 'request-1', workspaceId: 'workspace-1', candidates, generatedAt: '2026-08-16T09:59:00Z' };
}

function readiness(overrides: Partial<CapabilityReadinessInput> = {}): CapabilityReadinessInput {
  return {
    readinessDecisionId: 'ready-1', snapshotId: 'snapshot-1', snapshotObservedAt: '2026-08-16T09:55:00Z',
    snapshotExpiresAt: '2026-08-16T10:05:00Z', requiredDependencies: ['git'], availableDependencies: ['git'],
    approvalRequired: false, existingApprovalValid: false, policyAllowed: true, provenanceVerified: true,
    integrityVerified: true, compatible: true, credentialsReady: true, networkReady: true, sandboxReady: true,
    evidenceRefs: ['snapshot:snapshot-1'], ...overrides,
  };
}

describe('capability route and readiness evidence kernel', () => {
  it('fast-routes a clear candidate without granting execution authority', () => {
    const result = evaluateCapabilityRoute(candidateSet(), { now: NOW });
    expect(result).toEqual(expect.objectContaining({ stage: 'FAST_ROUTE', authorityStatus: 'CANDIDATE_ONLY', executionAuthorized: false, confidence: 0.9 }));
  });

  it('uses deterministic capability identity as a low-impact tie break', () => {
    const result = evaluateCapabilityRoute(candidateSet([candidate({ capabilityId: 'zeta', packageId: 'zeta' }), candidate({ capabilityId: 'alpha', packageId: 'alpha' })]), { now: NOW });
    expect(result.stage).toBe('FULL_RESOLUTION_REQUIRED');
    expect(result.primary?.capabilityId).toBe('alpha');
    expect(result.executionAuthorized).toBe(false);
  });

  it.each([
    ['risk', { riskLevel: 'R2' as const }, 'RISK_LEVEL_DIFFERS'],
    ['credentials', { credentialScopeRefs: ['secret-ref'] }, 'CREDENTIAL_SCOPE_DIFFERS'],
    ['network', { networkDestinations: ['api.example'] }, 'NETWORK_DESTINATIONS_DIFFER'],
    ['mutation', { mutationKinds: ['WORKSPACE_FILE'] }, 'MUTATION_SCOPE_DIFFERS'],
    ['irreversible', { irreversibleEffects: true }, 'IRREVERSIBLE_EFFECTS_DIFFER'],
    ['human effects', { publicOrHumanEffects: true }, 'PUBLIC_OR_HUMAN_EFFECTS_DIFFER'],
  ])('escalates close-score %s differences as material ambiguity', (_label, delta, reason) => {
    const result = evaluateCapabilityRoute(candidateSet([candidate(), candidate({ capabilityId: 'other', packageId: 'other', score: 0.85, ...delta })]), { now: NOW });
    expect(result.stage).toBe('AMBIGUOUS_ROUTE');
    expect(result.ambiguityReasons).toContain(reason);
  });

  it('requires full resolution for dependencies or conflicts and exposes fallback activation', () => {
    const result = evaluateCapabilityRoute(candidateSet([candidate({ dependencies: ['git-core'] }), candidate({ capabilityId: 'fallback', packageId: 'fallback', score: 0.5 })]), { now: NOW });
    expect(result.stage).toBe('FULL_RESOLUTION_REQUIRED');
    expect(result.supporting).toEqual(['git-core']);
    expect(result.fallbacks[0].activationCondition).toContain('AUTHORITY_ENVELOPE_REVALIDATED');
    expect(evaluateCapabilityReadiness(result, readiness(), NOW).state).toBe('UNKNOWN');
    expect(evaluateCapabilityReadiness(result, readiness({ integrityVerified: false }), NOW).state).toBe('BLOCKED_INTEGRITY');
  });

  it('fails closed for malformed, duplicate, future, and invalid-score candidate evidence', () => {
    expect(evaluateCapabilityRoute(candidateSet([candidate(), candidate()]), { now: NOW }).issues.map(({ code }) => code)).toContain('DUPLICATE_CANDIDATE');
    expect(evaluateCapabilityRoute({ ...candidateSet(), generatedAt: '2026-08-17T00:00:00Z' }, { now: NOW }).issues.length).toBeGreaterThan(0);
    expect(evaluateCapabilityRoute(candidateSet([candidate({ score: 2 })]), { now: NOW }).issues.length).toBeGreaterThan(0);
  });

  it('returns no candidate without claiming authority', () => {
    const result = evaluateCapabilityRoute(candidateSet([]), { now: NOW });
    expect(result).toEqual(expect.objectContaining({ stage: 'NO_CANDIDATE', executionAuthorized: false }));
    expect(evaluateCapabilityReadiness(result, readiness(), NOW).state).toBe('UNKNOWN');
  });

  it('returns READY as evidence only', () => {
    const route = evaluateCapabilityRoute(candidateSet(), { now: NOW });
    expect(evaluateCapabilityReadiness(route, readiness(), NOW)).toEqual(expect.objectContaining({ state: 'READY', authorityStatus: 'EVIDENCE_ONLY', executionAuthorized: false }));
  });

  it('applies fail-closed precedence before availability and approval states', () => {
    const route = evaluateCapabilityRoute(candidateSet(), { now: NOW });
    expect(evaluateCapabilityReadiness(route, readiness({ integrityVerified: false, availableDependencies: [], approvalRequired: true }), NOW).state).toBe('BLOCKED_INTEGRITY');
    expect(evaluateCapabilityReadiness(route, readiness({ provenanceVerified: false, availableDependencies: [] }), NOW).state).toBe('BLOCKED_PROVENANCE');
    expect(evaluateCapabilityReadiness(route, readiness({ policyAllowed: false, availableDependencies: [] }), NOW).state).toBe('BLOCKED_POLICY');
  });

  it('blocks READY on material route ambiguity and stale or unknown evidence', () => {
    const ambiguous = evaluateCapabilityRoute(candidateSet([candidate(), candidate({ capabilityId: 'other', packageId: 'other', score: 0.85, riskLevel: 'R2' })]), { now: NOW });
    expect(evaluateCapabilityReadiness(ambiguous, readiness(), NOW).state).toBe('AMBIGUOUS_ROUTE');
    const route = evaluateCapabilityRoute(candidateSet(), { now: NOW });
    expect(evaluateCapabilityReadiness(route, readiness({ snapshotExpiresAt: NOW }), NOW).state).toBe('STALE_SNAPSHOT');
    expect(evaluateCapabilityReadiness(route, readiness({ networkReady: null }), NOW).state).toBe('UNKNOWN');
  });

  it('routes approval and missing dependency states with safe next actions', () => {
    const route = evaluateCapabilityRoute(candidateSet(), { now: NOW });
    const approval = evaluateCapabilityReadiness(route, readiness({ approvalRequired: true }), NOW);
    expect(approval.state).toBe('APPROVAL_REQUIRED');
    expect(approval.approvalRequirements).toEqual(['EXACT_PLAN_APPROVAL_REQUIRED']);
    const bootstrap = evaluateCapabilityReadiness(route, readiness({ availableDependencies: [] }), NOW);
    expect(bootstrap.state).toBe('BOOTSTRAP_REQUIRED');
    expect(bootstrap.nextSafeAction).toContain('do not install automatically');
  });

  it('recognizes ready-with-existing-approval without treating it as execution authority', () => {
    const route = evaluateCapabilityRoute(candidateSet(), { now: NOW });
    expect(evaluateCapabilityReadiness(route, readiness({ approvalRequired: true, existingApprovalValid: true }), NOW)).toEqual(expect.objectContaining({ state: 'READY_WITH_EXISTING_APPROVAL', executionAuthorized: false }));
  });
});
