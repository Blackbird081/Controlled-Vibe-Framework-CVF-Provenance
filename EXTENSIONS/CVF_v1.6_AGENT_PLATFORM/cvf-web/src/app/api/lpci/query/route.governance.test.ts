import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { NextRequest } from 'next/server';

import { POST } from './route';

const verifySessionCookieMock = vi.hoisted(() => vi.fn());

vi.mock('@/lib/middleware-auth', () => ({
  verifySessionCookie: verifySessionCookieMock,
}));

function makeRequest(body: unknown) {
  return new NextRequest('http://localhost/api/lpci/query', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'x-cvf-service-token': 'test-service-token' },
    body: JSON.stringify(body),
  });
}

describe('POST /api/lpci/query route governance proof', () => {
  beforeEach(() => {
    process.env.CVF_SERVICE_TOKEN = 'test-service-token';
    verifySessionCookieMock.mockReset();
    verifySessionCookieMock.mockResolvedValue(null);
  });

  afterEach(() => {
    delete process.env.CVF_SERVICE_TOKEN;
  });

  it('denies an unauthenticated request without creating an audit receipt', async () => {
    delete process.env.CVF_SERVICE_TOKEN;
    const request = new NextRequest('http://localhost/api/lpci/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: 'policy', corpusId: 'registered' }),
    });

    const res = await POST(request);
    const data = await res.json();

    expect(res.status).toBe(401);
    expect(data.outcome).toBe('AUTHORIZATION_DENIED');
    expect(data.routeGovernanceProof.decision).toBe('DENY');
    expect(Object.keys(data).sort()).toEqual([
      'message', 'outcome', 'routeGovernanceProof',
    ].sort());
    expect(data).not.toHaveProperty('auditReceipt');
    expect(data).not.toHaveProperty('auditId');
  });

  it('emits routeGovernanceProof on validation denial after auth', async () => {
    const res = await POST(makeRequest({ query: '', corpusId: '' }));
    const data = await res.json();

    expect(res.status).toBe(400);
    expect(data.routeGovernanceProof.routeId).toBe('/api/lpci/query');
    expect(data.routeGovernanceProof.authMode).toBe('service_token');
    expect(data.routeGovernanceProof.decision).toBe('ALLOW');
    expect(data.outcome).toBe('INVALID_REQUEST');
    expect(Object.keys(data).sort()).toEqual([
      'message', 'outcome', 'routeGovernanceProof',
    ].sort());
    expect(data).not.toHaveProperty('auditReceipt');
  });

  it('rejects malformed JSON before audit creation', async () => {
    const request = new NextRequest('http://localhost/api/lpci/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-cvf-service-token': 'test-service-token' },
      body: '{not-json',
    });

    const res = await POST(request);
    const data = await res.json();

    expect(res.status).toBe(400);
    expect(data.outcome).toBe('INVALID_REQUEST');
    expect(data.routeGovernanceProof.decision).toBe('ALLOW');
    expect(Object.keys(data).sort()).toEqual([
      'message', 'outcome', 'routeGovernanceProof',
    ].sort());
    expect(data).not.toHaveProperty('auditReceipt');
  });

  it('rejects an unpaired surrogate before audit creation', async () => {
    const res = await POST(makeRequest({
      query: '\uD800',
      corpusId: 'registered',
    }));
    const data = await res.json();

    expect(res.status).toBe(400);
    expect(data.outcome).toBe('INVALID_REQUEST');
    expect(Object.keys(data).sort()).toEqual([
      'message', 'outcome', 'routeGovernanceProof',
    ].sort());
    expect(data).not.toHaveProperty('auditReceipt');
  });
});
