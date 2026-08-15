import { describe, expect, it } from 'vitest';

import { projectCadpAuthorization } from './cadp-authorization';
import type { RouteGovernanceAuthorization, RouteGovernanceProof } from '@/lib/route-governance-proof';

function buildProof(overrides: Partial<RouteGovernanceProof> = {}): RouteGovernanceProof {
  return {
    proofVersion: 'cvf.routeGovernanceProof.t2c.v1',
    workflowChainVersion: 'cvf.routeGovernanceProofWorkflow.t2c.v1',
    routeId: '/api/test-cadp',
    surface: 'test-cadp-route',
    riskLevel: 'R1',
    evidenceBasis: 'focused CADP authorization projection test',
    stages: ['BODY_CAPTURED', 'ROUTE_CONFIG_RESOLVED', 'SERVICE_TOKEN_EVALUATED', 'PROOF_EMITTED'],
    terminalStage: 'PROOF_EMITTED',
    authMode: 'service_token',
    decision: 'ALLOW',
    serviceTokenConfigured: true,
    serviceTokenPresented: true,
    serviceSignaturePresented: true,
    actorId: 'service:abc123',
    generatedAt: new Date(0).toISOString(),
    ...overrides,
  };
}

describe('cadp-authorization', () => {
  it('produces every authority field as a literal false for a service-identity authorization', () => {
    const authorization: RouteGovernanceAuthorization = {
      allowed: true,
      session: null,
      proof: buildProof(),
    };

    const projection = projectCadpAuthorization(authorization);

    expect(projection.actorId).toBe('service:abc123');
    expect(projection.realActorId).toBeNull();
    expect(projection.role).toBeNull();
    expect(projection.executionAuthorized).toBe(false);
    expect(projection.mutationAuthorized).toBe(false);
    expect(projection.receiptGrantsExecution).toBe(false);
    expect(projection.receiptGrantsMutation).toBe(false);
    expect(projection.receiptGrantsActivation).toBe(false);
  });

  it('preserves actor and role for a non-impersonated session identity, with every authority field false', () => {
    const authorization: RouteGovernanceAuthorization = {
      allowed: true,
      session: {
        userId: 'user-1',
        user: 'Tester',
        role: 'admin',
        orgId: 'org',
        teamId: 'team',
        expiresAt: Date.now() + 1000,
        authMode: 'session',
      },
      proof: buildProof({ authMode: 'session', actorId: 'user-1', serviceTokenPresented: false, serviceSignaturePresented: false }),
    };

    const projection = projectCadpAuthorization(authorization);

    expect(projection.actorId).toBe('user-1');
    expect(projection.realActorId).toBeNull();
    expect(projection.role).toBe('admin');
    expect(projection.executionAuthorized).toBe(false);
    expect(projection.mutationAuthorized).toBe(false);
    expect(projection.receiptGrantsExecution).toBe(false);
    expect(projection.receiptGrantsMutation).toBe(false);
    expect(projection.receiptGrantsActivation).toBe(false);
  });

  it('preserves both the impersonated actor and the real actor for an impersonated session, with every authority field false', () => {
    const authorization: RouteGovernanceAuthorization = {
      allowed: true,
      session: {
        userId: 'impersonated-1',
        user: 'Impersonated User',
        role: 'developer',
        orgId: 'org',
        teamId: 'team',
        expiresAt: Date.now() + 1000,
        authMode: 'session',
        realUserId: 'real-actor-1',
        realRole: 'admin',
        impersonation: {
          sessionId: 'impersonation-session-1',
          realActorId: 'real-actor-1',
          impersonatedUserId: 'impersonated-1',
          startedAt: new Date(0).toISOString(),
          expiresAt: new Date(1000).toISOString(),
        },
      },
      proof: buildProof({ authMode: 'session', actorId: 'impersonated-1', serviceTokenPresented: false, serviceSignaturePresented: false }),
    };

    const projection = projectCadpAuthorization(authorization);

    expect(projection.actorId).toBe('impersonated-1');
    expect(projection.realActorId).toBe('real-actor-1');
    expect(projection.role).toBe('developer');
    expect(projection.executionAuthorized).toBe(false);
    expect(projection.mutationAuthorized).toBe(false);
    expect(projection.receiptGrantsExecution).toBe(false);
    expect(projection.receiptGrantsMutation).toBe(false);
    expect(projection.receiptGrantsActivation).toBe(false);
  });

  it('produces null actor/role for a denied authorization, with every authority field false', () => {
    const authorization: RouteGovernanceAuthorization = {
      allowed: false,
      session: null,
      proof: buildProof({ authMode: 'unauthorized', decision: 'DENY', actorId: null, serviceTokenPresented: false, serviceSignaturePresented: false }),
    };

    const projection = projectCadpAuthorization(authorization);

    expect(projection.actorId).toBeNull();
    expect(projection.realActorId).toBeNull();
    expect(projection.role).toBeNull();
    expect(projection.executionAuthorized).toBe(false);
    expect(projection.mutationAuthorized).toBe(false);
    expect(projection.receiptGrantsExecution).toBe(false);
    expect(projection.receiptGrantsMutation).toBe(false);
    expect(projection.receiptGrantsActivation).toBe(false);
  });
});
