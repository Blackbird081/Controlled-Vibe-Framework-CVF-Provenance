import { beforeEach, describe, expect, it, vi } from 'vitest';
import { NextRequest } from 'next/server';

import { CADP_FAIL_CLOSED_ON_INVALID_TOKEN, authorizeCadpAuthenticationRequest } from './cadp-authentication-policy';
import { computeServiceRequestSignature } from './service-token-auth';

const verifySessionCookieMock = vi.hoisted(() => vi.fn());

vi.mock('@/lib/middleware-auth', () => ({
  verifySessionCookie: verifySessionCookieMock,
}));

const CONFIG = {
  routeId: '/api/test-cadp',
  surface: 'test-cadp-route',
  riskLevel: 'R1' as const,
  evidenceBasis: 'focused CADP authentication policy test',
};

const SERVICE_TOKEN = 'test-service-token';

function request(body: string, headers: Record<string, string> = {}) {
  return new NextRequest('http://localhost/api/test-cadp', {
    method: 'POST',
    headers,
    body,
  });
}

function signedTokenHeaders(body: string, now: number, token: string = SERVICE_TOKEN): Record<string, string> {
  const timestamp = String(now);
  return {
    'x-cvf-service-token': token,
    'x-cvf-service-timestamp': timestamp,
    'x-cvf-service-signature': computeServiceRequestSignature(token, timestamp, body),
  };
}

describe('cadp-authentication-policy', () => {
  beforeEach(() => {
    verifySessionCookieMock.mockReset();
    verifySessionCookieMock.mockResolvedValue(null);
    process.env.CVF_SERVICE_TOKEN = 'test-service-token';
  });

  it('exposes the exact Option A policy token', () => {
    expect(CADP_FAIL_CLOSED_ON_INVALID_TOKEN).toBe('CADP_FAIL_CLOSED_ON_INVALID_TOKEN');
  });

  it('denies an invalid presented token without evaluating session', async () => {
    verifySessionCookieMock.mockResolvedValueOnce({
      userId: 'user-1',
      user: 'Tester',
      role: 'admin',
      orgId: 'org',
      teamId: 'team',
      expiresAt: Date.now() + 1000,
      authMode: 'session',
    });

    const result = await authorizeCadpAuthenticationRequest(
      request('{"ok":true}', { 'x-cvf-service-token': 'wrong-token' }),
      '{"ok":true}',
      CONFIG,
    );

    expect(result.allowed).toBe(false);
    expect(result.response?.status).toBe(401);
    expect(result.proof.actorId).toBeNull();
    expect(verifySessionCookieMock).not.toHaveBeenCalled();
  });

  it('allows a valid signed service token', async () => {
    const body = '{"ok":true}';
    const now = Date.now();

    const result = await authorizeCadpAuthenticationRequest(
      request(body, signedTokenHeaders(body, now)),
      body,
      CONFIG,
      { now },
    );

    expect(result.allowed).toBe(true);
    expect(result.proof.authMode).toBe('service_token');
  });

  it('allows a valid session when no token is presented', async () => {
    verifySessionCookieMock.mockResolvedValueOnce({
      userId: 'user-1',
      user: 'Tester',
      role: 'admin',
      orgId: 'org',
      teamId: 'team',
      expiresAt: Date.now() + 1000,
      authMode: 'session',
    });

    const result = await authorizeCadpAuthenticationRequest(request('{"ok":true}'), '{"ok":true}', CONFIG);

    expect(result.allowed).toBe(true);
    expect(result.proof.authMode).toBe('session');
  });

  it('denies when neither token nor session is present', async () => {
    const result = await authorizeCadpAuthenticationRequest(request('{"ok":true}'), '{"ok":true}', CONFIG);

    expect(result.allowed).toBe(false);
    expect(result.proof.actorId).toBeNull();
  });

  it('propagates an injected time to the proof', async () => {
    const fixedNow = 1_700_000_000_000;
    const body = '{"ok":true}';

    const result = await authorizeCadpAuthenticationRequest(
      request(body, signedTokenHeaders(body, fixedNow)),
      body,
      CONFIG,
      { now: fixedNow },
    );

    expect(result.proof.generatedAt).toBe(new Date(fixedNow).toISOString());
  });
});
