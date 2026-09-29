import { describe, expect, it } from 'vitest';
import {
  CADP_EXTERNAL_READOUT_ADAPTER_CONTRACT_VERSION,
  evaluateCadpExternalReadoutAdapter,
} from './cadp-external-readout-adapter.contract';

function validIdentity() {
  return {
    callerId: 'external-agent-001',
    requestedScope: ['read'],
    requestTimestamp: '2026-08-15T00:00:00.000Z',
  };
}

function validIngress() {
  return {
    identity: validIdentity(),
    capabilityId: 'cvf.cadp.owner-bound-evidence',
    requestedFields: ['capabilityId', 'capabilityVersion'],
  };
}

function validFreshness(overrides: Partial<{ issuedAt: string; expiresAt: string; observedAt: string }> = {}) {
  return {
    issuedAt: '2026-08-15T00:00:00.000Z',
    expiresAt: '2026-08-15T01:00:00.000Z',
    observedAt: '2026-08-15T00:05:00.000Z',
    ...overrides,
  };
}

function validCandidateMetadata() {
  return {
    capabilityId: 'cvf.cadp.owner-bound-evidence',
    capabilityVersion: '1.0.0',
    admissionDecision: 'ADMITTED',
    assignedActionIds: ['read-capability'],
    evidenceLevel: 'OWNER_BOUND',
    externalReadoutAuthorized: false as const,
    externalMutationAuthorized: false as const,
    externalActivationAuthorized: false as const,
    externalExecutionAuthorized: false as const,
    externalProviderCallAuthorized: false as const,
    externalCredentialResolutionAuthorized: false as const,
  };
}

function validRequest() {
  return {
    ingress: validIngress(),
    freshness: validFreshness(),
    candidateMetadata: validCandidateMetadata(),
  };
}

describe('CADP external readout adapter contract version', () => {
  it('declares an exact, distinct contract version', () => {
    expect(CADP_EXTERNAL_READOUT_ADAPTER_CONTRACT_VERSION).toBe('cvf.cadp.externalReadoutAdapter.v1');
  });
});

describe('valid shapes with no auth owner', () => {
  it('rejects a fully well-shaped request with a controlled AUTHENTICATION_REQUIRED issue and no metadata', () => {
    const response = evaluateCadpExternalReadoutAdapter(validRequest());
    expect(response.accepted).toBe(false);
    expect(response.authenticationVerified).toBe(false);
    expect(response.issues.map((i) => i.code)).toContain('AUTHENTICATION_REQUIRED');
    expect(response.issues.find((i) => i.code === 'AUTHENTICATION_REQUIRED')?.stage).toBe('AUTHENTICATION');
    // No candidate metadata field exists anywhere on the response envelope.
    expect(Object.keys(response)).not.toContain('metadata');
    expect(Object.keys(response)).not.toContain('candidate');
  });

  it('never returns accepted: true for any input shape', () => {
    const response = evaluateCadpExternalReadoutAdapter(validRequest());
    expect(response.accepted).toBe(false);
  });
});

describe('malformed/unknown/oversize/proxy/accessor input', () => {
  it('rejects a non-object request before any later stage runs', () => {
    const response = evaluateCadpExternalReadoutAdapter('not-an-object' as unknown as ReturnType<typeof validRequest>);
    expect(response.accepted).toBe(false);
    expect(response.issues[0]?.stage).toBe('INGRESS');
  });

  it('rejects null', () => {
    const response = evaluateCadpExternalReadoutAdapter(null as unknown as ReturnType<typeof validRequest>);
    expect(response.accepted).toBe(false);
    expect(response.issues[0]?.stage).toBe('INGRESS');
  });

  it('rejects an unknown top-level field on the adapter request', () => {
    const response = evaluateCadpExternalReadoutAdapter({ ...validRequest(), extra: true } as unknown as ReturnType<typeof validRequest>);
    expect(response.accepted).toBe(false);
    expect(response.issues.some((i) => i.stage === 'INGRESS')).toBe(true);
  });

  it('rejects a request whose ingress field is an accessor property, never reading its getter', () => {
    let getterInvoked = false;
    const request = {};
    Object.defineProperty(request, 'ingress', {
      enumerable: true,
      configurable: true,
      get() {
        getterInvoked = true;
        return validIngress();
      },
    });
    Object.defineProperty(request, 'freshness', { enumerable: true, configurable: true, value: validFreshness() });
    Object.defineProperty(request, 'candidateMetadata', { enumerable: true, configurable: true, value: validCandidateMetadata() });
    const response = evaluateCadpExternalReadoutAdapter(request as unknown as ReturnType<typeof validRequest>);
    expect(response.accepted).toBe(false);
    expect(getterInvoked).toBe(false);
  });

  it('rejects a Proxy-wrapped request without invoking any trap-triggered code path that would leak a value', () => {
    let trapped = false;
    const proxyRequest = new Proxy(validRequest(), {
      get(target, prop, receiver) {
        trapped = true;
        return Reflect.get(target, prop, receiver);
      },
    });
    const response = evaluateCadpExternalReadoutAdapter(proxyRequest);
    expect(response.accepted).toBe(false);
    // The adapter's own prototype/own-property checks reject the Proxy at the
    // ingress stage before any deeper composition logic would need to trust it.
    expect(response.issues[0]?.stage).toBe('INGRESS');
    void trapped;
  });

  it('rejects an oversize requestedFields array inside ingress (propagated through the adapter)', () => {
    const oversized = Array.from({ length: 33 }, (_, i) => `capabilityId${i}`);
    const response = evaluateCadpExternalReadoutAdapter({
      ingress: { ...validIngress(), requestedFields: oversized },
      freshness: validFreshness(),
      candidateMetadata: validCandidateMetadata(),
    });
    expect(response.accepted).toBe(false);
    expect(response.issues.some((i) => i.code === 'REQUEST_TOO_LARGE')).toBe(true);
  });
});

describe('stale/expired/invalid timestamp', () => {
  it('deterministically rejects a stale freshness window', () => {
    const response = evaluateCadpExternalReadoutAdapter({
      ingress: validIngress(),
      freshness: validFreshness({ expiresAt: '2026-08-20T00:00:00.000Z', observedAt: '2026-08-17T00:00:00.000Z' }),
      candidateMetadata: validCandidateMetadata(),
    });
    expect(response.accepted).toBe(false);
    expect(response.issues.some((i) => i.stage === 'FRESHNESS')).toBe(true);
  });

  it('deterministically rejects an expired freshness window', () => {
    const response = evaluateCadpExternalReadoutAdapter({
      ingress: validIngress(),
      freshness: validFreshness({ expiresAt: '2026-08-15T00:05:00.000Z', observedAt: '2026-08-15T00:10:00.000Z' }),
      candidateMetadata: validCandidateMetadata(),
    });
    expect(response.accepted).toBe(false);
    expect(response.issues.some((i) => i.stage === 'FRESHNESS')).toBe(true);
  });

  it('deterministically rejects an invalid (non-calendar) timestamp', () => {
    const response = evaluateCadpExternalReadoutAdapter({
      ingress: validIngress(),
      freshness: validFreshness({ issuedAt: '2026-99-99T99:99:99Z' }),
      candidateMetadata: validCandidateMetadata(),
    });
    expect(response.accepted).toBe(false);
    expect(response.issues.some((i) => i.stage === 'FRESHNESS')).toBe(true);
  });
});

describe('secret field or private path', () => {
  it('rejects a secret-named candidate field without echoing the raw value', () => {
    const response = evaluateCadpExternalReadoutAdapter({
      ingress: validIngress(),
      freshness: validFreshness(),
      candidateMetadata: { ...validCandidateMetadata(), apiKey: 'sk-sensitive-value' },
    });
    const serialized = JSON.stringify(response);
    expect(response.issues.some((i) => i.stage === 'REDACTION')).toBe(true);
    expect(serialized).not.toContain('sk-sensitive-value');
  });

  it('rejects a request whose identity carries a private-provenance path marker before allowlist runs', () => {
    const response = evaluateCadpExternalReadoutAdapter({
      ingress: { ...validIngress(), capabilityId: 'CVF_SESSION/state/entries/foo.json' },
      freshness: validFreshness(),
      candidateMetadata: { ...validCandidateMetadata(), capabilityId: 'CVF_SESSION/state/entries/foo.json' },
    });
    expect(response.accepted).toBe(false);
    expect(response.issues.some((i) => i.stage === 'REDACTION')).toBe(true);
  });
});

describe('field outside allowlist', () => {
  it('rejects a candidate metadata field outside the exact T5-R1 allowlist without returning metadata', () => {
    const response = evaluateCadpExternalReadoutAdapter({
      ingress: validIngress(),
      freshness: validFreshness(),
      candidateMetadata: { ...validCandidateMetadata(), unsupportedReadoutField: 'value' },
    });
    expect(response.accepted).toBe(false);
    expect(response.issues.every((i) => i.stage === 'ALLOWLIST')).toBe(true);
    expect(response.issues.some((i) => i.code === 'UNKNOWN_FIELD')).toBe(true);
  });
});

describe('authority-shaped input', () => {
  it('cannot widen accepted, authenticationVerified, or any external authority field via request-shaped injection', () => {
    const response = evaluateCadpExternalReadoutAdapter({
      ...validRequest(),
      accepted: true,
      authenticationVerified: true,
      externalExecutionAuthorized: true,
    } as unknown as ReturnType<typeof validRequest>);
    expect(response.accepted).toBe(false);
    expect(response.authenticationVerified).toBe(false);
    expect(response.externalTransportRegistered).toBe(false);
    expect(response.externalInvocationAuthorized).toBe(false);
    expect(response.externalMutationAuthorized).toBe(false);
    expect(response.externalActivationAuthorized).toBe(false);
    expect(response.externalExecutionAuthorized).toBe(false);
    expect(response.externalProviderCallAuthorized).toBe(false);
    expect(response.externalCredentialResolutionAuthorized).toBe(false);
  });
});

describe('key-order and post-call mutation', () => {
  it('produces an identical receipt integrityHash for identical rejecting stage/issuedAt across repeated calls', () => {
    const responseA = evaluateCadpExternalReadoutAdapter(validRequest());
    const responseB = evaluateCadpExternalReadoutAdapter(validRequest());
    expect(responseA.receipt.integrityHash).toBe(responseB.receipt.integrityHash);
  });

  it('produces an identical receipt for repeated malformed input without ambient ordinal state', () => {
    const malformed = null as unknown as ReturnType<typeof validRequest>;
    const responseA = evaluateCadpExternalReadoutAdapter(malformed);
    const responseB = evaluateCadpExternalReadoutAdapter(malformed);
    expect(responseA.receipt.integrityHash).toBe(responseB.receipt.integrityHash);
    expect(responseA.receipt.receiptId).toBe(responseB.receipt.receiptId);
  });

  it('freezes the response envelope and its receipt so post-call mutation cannot alter authority fields', () => {
    const response = evaluateCadpExternalReadoutAdapter(validRequest());
    expect(Object.isFrozen(response)).toBe(true);
    expect(Object.isFrozen(response.receipt)).toBe(true);
    expect(Object.isFrozen(response.issues)).toBe(true);
    'use strict';
    expect(() => {
      (response as { accepted: boolean }).accepted = true;
    }).toThrow();
    expect(response.accepted).toBe(false);
  });
});

describe('callback/function/port injection', () => {
  it('cannot represent a function in the public request type, and a runtime-injected function field never widens authority', () => {
    const injectedCallback = () => 'invoked';
    let callbackInvoked = false;
    const wrapped = () => {
      callbackInvoked = true;
      return injectedCallback();
    };
    const response = evaluateCadpExternalReadoutAdapter({
      ...validRequest(),
      onAccept: wrapped,
    } as unknown as ReturnType<typeof validRequest>);
    expect(response.accepted).toBe(false);
    expect(callbackInvoked).toBe(false);
  });
});
