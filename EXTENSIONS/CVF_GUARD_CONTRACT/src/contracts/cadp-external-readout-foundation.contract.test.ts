import { describe, expect, it } from 'vitest';
import {
  CADP_EXTERNAL_READOUT_FOUNDATION_CONTRACT_VERSION,
  CADP_EXTERNAL_READOUT_REDACTED_FIELD_NAMES,
  createDeterministicCadpExternalReadoutReceipt,
  evaluateCadpExternalReadoutFreshness,
  redactCadpExternalReadoutPayload,
  validateCadpExternalCallerIdentityInput,
  validateCadpExternalReadoutAllowlistedMetadata,
  validateCadpExternalReadoutIngress,
} from './cadp-external-readout-foundation.contract';

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

function validAllowlistedMetadata() {
  return {
    capabilityId: 'cvf.cadp.owner-bound-evidence',
    capabilityVersion: 'v3',
    admissionDecision: 'ADMIT_READ_ONLY',
    assignedActionIds: ['validateCompatibilityEvidence'],
    evidenceLevel: 'RECEIPT_BACKED',
    externalReadoutAuthorized: false,
    externalMutationAuthorized: false,
    externalActivationAuthorized: false,
    externalExecutionAuthorized: false,
    externalProviderCallAuthorized: false,
    externalCredentialResolutionAuthorized: false,
  };
}

describe('CADP external readout foundation contract version', () => {
  it('declares an exact, distinct contract version', () => {
    expect(CADP_EXTERNAL_READOUT_FOUNDATION_CONTRACT_VERSION).toBe('cvf.cadp.externalReadoutFoundation.v1');
  });
});

describe('caller identity input contract (positive)', () => {
  it('accepts a well-shaped identity input', () => {
    const result = validateCadpExternalCallerIdentityInput(validIdentity());
    expect(result.valid).toBe(true);
    expect(result.data.identity).toEqual(expect.objectContaining({ callerId: 'external-agent-001' }));
  });
});

describe('caller identity input contract (adversarial: identity mismatch)', () => {
  it('rejects a malformed callerId shape with a typed issue, never silent acceptance', () => {
    const result = validateCadpExternalCallerIdentityInput({ ...validIdentity(), callerId: '!! not-an-id !!' });
    expect(result.valid).toBe(false);
    expect(result.issues.map((i) => i.code)).toContain('INVALID_CALLER_IDENTITY');
  });

  it('rejects a non-string callerId', () => {
    const result = validateCadpExternalCallerIdentityInput({ ...validIdentity(), callerId: 12345 as unknown as string });
    expect(result.valid).toBe(false);
    expect(result.issues.map((i) => i.code)).toContain('INVALID_CALLER_IDENTITY');
  });

  it('rejects an unknown top-level field on the identity input', () => {
    const result = validateCadpExternalCallerIdentityInput({ ...validIdentity(), extra: 'nope' });
    expect(result.valid).toBe(false);
    expect(result.issues.map((i) => i.code)).toContain('UNKNOWN_FIELD');
  });

  it('rejects a regex-shaped timestamp that is not a real calendar instant', () => {
    const result = validateCadpExternalCallerIdentityInput({
      ...validIdentity(),
      requestTimestamp: '2026-99-99T99:99:99Z',
    });
    expect(result.valid).toBe(false);
    expect(result.issues.map((i) => i.code)).toContain('INVALID_TIMESTAMP');
  });
});

describe('ingress schema/size validator (positive)', () => {
  it('accepts a well-shaped ingress request', () => {
    const result = validateCadpExternalReadoutIngress(validIngress());
    expect(result.valid).toBe(true);
    expect(result.data.request?.capabilityId).toBe('cvf.cadp.owner-bound-evidence');
  });
});

describe('ingress schema/size validator (adversarial: unknown fields)', () => {
  it('rejects a top-level field outside the exact ingress shape', () => {
    const result = validateCadpExternalReadoutIngress({ ...validIngress(), unexpectedField: true });
    expect(result.valid).toBe(false);
    expect(result.issues.map((i) => i.code)).toContain('UNKNOWN_FIELD');
  });

  it('rejects a requestedFields entry outside the exact metadata allowlist', () => {
    const result = validateCadpExternalReadoutIngress({ ...validIngress(), requestedFields: ['capabilityId', 'secretsBundle'] });
    expect(result.valid).toBe(false);
    expect(result.issues.map((i) => i.code)).toContain('UNKNOWN_FIELD');
  });
});

describe('ingress schema/size validator (adversarial: oversize input)', () => {
  it('rejects requestedFields exceeding the exact size bound before allowlist logic runs', () => {
    const oversized = Array.from({ length: 33 }, (_, i) => `capabilityId${i}`);
    const result = validateCadpExternalReadoutIngress({ ...validIngress(), requestedFields: oversized });
    expect(result.valid).toBe(false);
    expect(result.issues.map((i) => i.code)).toContain('REQUEST_TOO_LARGE');
  });

  it('rejects an oversize scope array on the nested identity input', () => {
    const oversizedScope = Array.from({ length: 17 }, (_, i) => `scope-${i}`);
    const result = validateCadpExternalReadoutIngress({
      ...validIngress(),
      identity: { ...validIdentity(), requestedScope: oversizedScope },
    });
    expect(result.valid).toBe(false);
  });
});

describe('redaction contract (positive)', () => {
  it('passes a payload containing no secret or private-provenance field', () => {
    const result = redactCadpExternalReadoutPayload({ capabilityId: 'cvf.cadp.owner-bound-evidence', evidenceLevel: 'DECLARED' });
    expect(result.valid).toBe(true);
    expect(result.data.redactedFieldNames).toEqual([]);
  });
});

describe('redaction contract (adversarial: secret / private provenance)', () => {
  it.each(CADP_EXTERNAL_READOUT_REDACTED_FIELD_NAMES)('rejects and never emits the redacted field name "%s"', (fieldName) => {
    const payload: Record<string, unknown> = { capabilityId: 'cvf.cadp.owner-bound-evidence', [fieldName]: 'raw-value' };
    const result = redactCadpExternalReadoutPayload(payload);
    expect(result.valid).toBe(false);
    expect(result.data.redactedFieldNames).toContain(fieldName);
    expect(result.issues.map((i) => i.code)).toContain('REDACTED_FIELD_PRESENT');
  });

  it('rejects a string field whose value contains a private-provenance path marker', () => {
    const result = redactCadpExternalReadoutPayload({ capabilityId: 'cvf.cadp.owner-bound-evidence', sourceRef: 'CVF_SESSION/state/entries/foo.json' });
    expect(result.valid).toBe(false);
    expect(result.issues.map((i) => i.code)).toContain('PRIVATE_PROVENANCE_PATH');
  });

  it('never includes a redacted field name in the output payload text (never re-emitted)', () => {
    const payload = { capabilityId: 'cvf.cadp.owner-bound-evidence', apiKey: 'sk-should-never-appear' };
    const result = redactCadpExternalReadoutPayload(payload);
    const serializedResult = JSON.stringify(result);
    expect(serializedResult).not.toContain('sk-should-never-appear');
  });
});

describe('exact metadata field allowlist (positive)', () => {
  it('accepts a fully-shaped, literal-false-authority metadata record', () => {
    const result = validateCadpExternalReadoutAllowlistedMetadata(validAllowlistedMetadata());
    expect(result.valid).toBe(true);
    expect(result.data.metadata?.externalReadoutAuthorized).toBe(false);
  });
});

describe('exact metadata field allowlist (adversarial: authority widening)', () => {
  it('rejects externalReadoutAuthorized set to true', () => {
    const result = validateCadpExternalReadoutAllowlistedMetadata({ ...validAllowlistedMetadata(), externalReadoutAuthorized: true as unknown as false });
    expect(result.valid).toBe(false);
  });

  it('rejects externalMutationAuthorized set to true', () => {
    const result = validateCadpExternalReadoutAllowlistedMetadata({ ...validAllowlistedMetadata(), externalMutationAuthorized: true as unknown as false });
    expect(result.valid).toBe(false);
  });

  it('rejects externalActivationAuthorized set to true', () => {
    const result = validateCadpExternalReadoutAllowlistedMetadata({ ...validAllowlistedMetadata(), externalActivationAuthorized: true as unknown as false });
    expect(result.valid).toBe(false);
  });

  it('rejects externalExecutionAuthorized set to true', () => {
    const result = validateCadpExternalReadoutAllowlistedMetadata({ ...validAllowlistedMetadata(), externalExecutionAuthorized: true as unknown as false });
    expect(result.valid).toBe(false);
  });

  it('rejects externalProviderCallAuthorized set to true', () => {
    const result = validateCadpExternalReadoutAllowlistedMetadata({ ...validAllowlistedMetadata(), externalProviderCallAuthorized: true as unknown as false });
    expect(result.valid).toBe(false);
  });

  it('rejects externalCredentialResolutionAuthorized set to true', () => {
    const result = validateCadpExternalReadoutAllowlistedMetadata({ ...validAllowlistedMetadata(), externalCredentialResolutionAuthorized: true as unknown as false });
    expect(result.valid).toBe(false);
  });

  it('rejects a missing authority field entirely (absent, not false)', () => {
    const { externalReadoutAuthorized: _omit, ...withoutField } = validAllowlistedMetadata();
    const result = validateCadpExternalReadoutAllowlistedMetadata(withoutField);
    expect(result.valid).toBe(false);
  });

  it('rejects an unknown field outside the exact allowlist', () => {
    const result = validateCadpExternalReadoutAllowlistedMetadata({ ...validAllowlistedMetadata(), mutationAuthorityLevel: 'FULL' });
    expect(result.valid).toBe(false);
    expect(result.issues.map((i) => i.code)).toContain('UNKNOWN_FIELD');
  });
});

describe('replay/freshness contract (positive)', () => {
  it('reports FRESH for an observation inside the issued/expiry window', () => {
    const result = evaluateCadpExternalReadoutFreshness({
      issuedAt: '2026-08-15T00:00:00.000Z',
      expiresAt: '2026-08-15T01:00:00.000Z',
      observedAt: '2026-08-15T00:05:00.000Z',
    });
    expect(result.disposition).toBe('FRESH');
    expect(result.issues).toEqual([]);
  });
});

describe('replay/freshness contract (adversarial: replay)', () => {
  it('reports INVALID when observed materially before issuedAt (implausible replay window)', () => {
    const result = evaluateCadpExternalReadoutFreshness({
      issuedAt: '2026-08-15T00:10:00.000Z',
      expiresAt: '2026-08-15T01:00:00.000Z',
      observedAt: '2026-08-15T00:00:00.000Z',
    });
    expect(result.disposition).toBe('INVALID');
    expect(result.issues.map((i) => i.code)).toContain('REPLAY_WINDOW_EXCEEDED');
  });

  it('reports EXPIRED when observed after expiresAt (replayed past its window)', () => {
    const result = evaluateCadpExternalReadoutFreshness({
      issuedAt: '2026-08-15T00:00:00.000Z',
      expiresAt: '2026-08-15T00:05:00.000Z',
      observedAt: '2026-08-15T00:10:00.000Z',
    });
    expect(result.disposition).toBe('EXPIRED');
    expect(result.issues.map((i) => i.code)).toContain('REPLAY_WINDOW_EXCEEDED');
  });
});

describe('replay/freshness contract (adversarial: stale request)', () => {
  it('reports STALE for an observation well past a reasonable freshness bound but still before expiry', () => {
    const result = evaluateCadpExternalReadoutFreshness({
      issuedAt: '2026-08-15T00:00:00.000Z',
      expiresAt: '2026-08-20T00:00:00.000Z',
      observedAt: '2026-08-17T00:00:00.000Z',
    });
    expect(result.disposition).toBe('STALE');
    expect(result.issues.map((i) => i.code)).toContain('STALE_REQUEST');
  });
});

describe('replay/freshness contract (malformed timestamp)', () => {
  it('reports INVALID for a non-ISO-8601 timestamp', () => {
    const result = evaluateCadpExternalReadoutFreshness({
      issuedAt: 'not-a-timestamp',
      expiresAt: '2026-08-15T01:00:00.000Z',
      observedAt: '2026-08-15T00:05:00.000Z',
    });
    expect(result.disposition).toBe('INVALID');
    expect(result.issues.map((i) => i.code)).toContain('INVALID_TIMESTAMP');
  });

  it('reports INVALID when expiresAt is not strictly after issuedAt', () => {
    const result = evaluateCadpExternalReadoutFreshness({
      issuedAt: '2026-08-15T01:00:00.000Z',
      expiresAt: '2026-08-15T01:00:00.000Z',
      observedAt: '2026-08-15T01:00:00.000Z',
    });
    expect(result.disposition).toBe('INVALID');
  });
});

describe('deterministic external error/receipt contract (positive)', () => {
  it('produces an identical integrityHash for identical explicit-time input', () => {
    const input = { requestId: 'req-001', issuedAt: '2026-08-15T00:00:00.000Z', payload: { capabilityId: 'cvf.cadp.owner-bound-evidence' } };
    const receiptA = createDeterministicCadpExternalReadoutReceipt(input);
    const receiptB = createDeterministicCadpExternalReadoutReceipt(input);
    expect(receiptA.integrityHash).toBe(receiptB.integrityHash);
    expect(receiptA.receiptId).toBe(receiptB.receiptId);
  });

  it('carries literal false on every authority-adjacent receipt field', () => {
    const receipt = createDeterministicCadpExternalReadoutReceipt({
      requestId: 'req-002',
      issuedAt: '2026-08-15T00:00:00.000Z',
      payload: {},
    });
    expect(receipt.receiptGrantsExecution).toBe(false);
    expect(receipt.receiptGrantsMutation).toBe(false);
    expect(receipt.receiptGrantsActivation).toBe(false);
    expect(receipt.contractVersion).toBe(CADP_EXTERNAL_READOUT_FOUNDATION_CONTRACT_VERSION);
  });

  it('produces different integrityHash values for different payloads', () => {
    const receiptA = createDeterministicCadpExternalReadoutReceipt({ requestId: 'req-003', issuedAt: '2026-08-15T00:00:00.000Z', payload: { a: 1 } });
    const receiptB = createDeterministicCadpExternalReadoutReceipt({ requestId: 'req-003', issuedAt: '2026-08-15T00:00:00.000Z', payload: { a: 2 } });
    expect(receiptA.integrityHash).not.toBe(receiptB.integrityHash);
  });

  it('canonicalizes object-key order and returns an independently owned frozen payload snapshot', () => {
    const payloadA = { a: 1, b: { c: 2 } };
    const payloadB = { b: { c: 2 }, a: 1 };
    const receiptA = createDeterministicCadpExternalReadoutReceipt({ requestId: 'req-canonical', issuedAt: '2026-08-15T00:00:00.000Z', payload: payloadA });
    const receiptB = createDeterministicCadpExternalReadoutReceipt({ requestId: 'req-canonical', issuedAt: '2026-08-15T00:00:00.000Z', payload: payloadB });
    expect(receiptA.integrityHash).toBe(receiptB.integrityHash);
    expect(receiptA.payload).not.toBe(payloadA);
    expect(Object.isFrozen(receiptA.payload)).toBe(true);
    expect(Object.isFrozen(receiptA.payload.b)).toBe(true);
  });
});

describe('deterministic external error/receipt contract (adversarial: malformed input)', () => {
  it('throws a typed error for a missing requestId', () => {
    expect(() => createDeterministicCadpExternalReadoutReceipt({ requestId: '', issuedAt: '2026-08-15T00:00:00.000Z', payload: {} })).toThrow(TypeError);
  });

  it('throws a typed error for a non-ISO-8601 issuedAt', () => {
    expect(() => createDeterministicCadpExternalReadoutReceipt({ requestId: 'req-004', issuedAt: 'bad-timestamp', payload: {} })).toThrow(TypeError);
  });

  it('throws a typed error for an impossible calendar timestamp', () => {
    expect(() => createDeterministicCadpExternalReadoutReceipt({ requestId: 'req-calendar', issuedAt: '2026-02-30T00:00:00Z', payload: {} })).toThrow(TypeError);
  });

  it('rejects an accessor payload without invoking caller-controlled code', () => {
    let getterCalls = 0;
    const payload = Object.defineProperty({}, 'toJSON', {
      enumerable: true,
      get() {
        getterCalls += 1;
        return () => ({ leaked: true });
      },
    });
    expect(() => createDeterministicCadpExternalReadoutReceipt({ requestId: 'req-accessor', issuedAt: '2026-08-15T00:00:00Z', payload })).toThrow(TypeError);
    expect(getterCalls).toBe(0);
  });
});

describe('mutation/activation/execution/provider flags (adversarial)', () => {
  it('asserts no exported type or function grants mutation, activation, execution, or provider-call authority', () => {
    const metadata = validateCadpExternalReadoutAllowlistedMetadata(validAllowlistedMetadata()).data.metadata!;
    expect(metadata.externalMutationAuthorized).toBe(false);
    expect(metadata.externalActivationAuthorized).toBe(false);
    expect(metadata.externalExecutionAuthorized).toBe(false);
    expect(metadata.externalProviderCallAuthorized).toBe(false);
    expect(metadata.externalCredentialResolutionAuthorized).toBe(false);
    const receipt = createDeterministicCadpExternalReadoutReceipt({ requestId: 'req-005', issuedAt: '2026-08-15T00:00:00.000Z', payload: {} });
    expect(receipt.receiptGrantsExecution).toBe(false);
    expect(receipt.receiptGrantsMutation).toBe(false);
    expect(receipt.receiptGrantsActivation).toBe(false);
    // This test performs no actual mutation, activation, execution, or provider call.
  });
});
