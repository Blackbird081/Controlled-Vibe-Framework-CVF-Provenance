import { describe, expect, it } from 'vitest';
import type {
  CapabilityAdmissionRecord,
  CapabilityAssignmentRecord,
  CapabilityDistributionManifest,
  CompatibilityEvidenceRecord,
} from './capability-admission-distribution-profile.contract';
import {
  createDeterministicCadpReceipt,
  validateCapabilityAdmission,
  validateCapabilityAssignment,
  validateCapabilityDistribution,
  validateCompatibilityEvidence,
} from './capability-admission-distribution-profile.contract';
import { bindCommittedCapabilityOwnerGrant, type CapabilityOwnerHandle } from './capability-owner-binding.contract';
const FORGED_HANDLE_SHAPE = { contractVersion: 'cvf.cadp.ownerBinding.v3' } as unknown as CapabilityOwnerHandle;

const admission: CapabilityAdmissionRecord = {
  admissionId: 'admission-1', capabilityId: 'cap-1', capabilityVersion: '1.0.0',
  decision: 'ADMIT_READ_ONLY', sourceVerified: true,
  admittedActions: [{ actionId: 'read', mutationType: 'read' }],
  executionAuthorized: false, rawSecretsAllowed: false, duplicateCanonicalOwnerRequired: false,
};

describe('CVF capability admission/distribution profile', () => {
  it('admits a verified record without minting execution authority', () => {
    expect(validateCapabilityAdmission(admission)).toEqual({
      valid: true, issues: [], data: { assignableActionIds: ['read'] },
    });
  });

  it('fails closed when assignment exceeds admitted actions', () => {
    const assignment: CapabilityAssignmentRecord = {
      assignmentId: 'assignment-1', admissionId: 'admission-1', capabilityId: 'cap-1',
      capabilityVersion: '1.0.0', assignedActionIds: ['write'], excludedActionIds: [],
      workOrderRequired: true, executionAuthorized: false, rawSecretsIncluded: false,
    };
    expect(validateCapabilityAssignment(admission, assignment).issues.map(({ code }) => code))
      .toContain('ACTION_OUTSIDE_ADMISSION');
  });

  it('rejects HOLD/BLOCK assignment and filters mutations from read-only admission (R03/R04)', () => {
    const blocked = { ...admission, decision: 'BLOCK' as const };
    expect(validateCapabilityAdmission(blocked)).toMatchObject({
      valid: false,
      data: { assignableActionIds: [] },
    });
    const readOnly = {
      ...admission,
      admittedActions: [
        { actionId: 'read', mutationType: 'read' as const },
        { actionId: 'delete', mutationType: 'delete' as const },
      ],
    };
    expect(validateCapabilityAdmission(readOnly).data.assignableActionIds).toEqual(['read']);
  });

  it('rejects empty identities and duplicate admission actions (R09)', () => {
    const invalid = {
      ...admission,
      admissionId: ' ',
      admittedActions: [
        { actionId: 'read', mutationType: 'read' as const },
        { actionId: 'read', mutationType: 'read' as const },
      ],
    };
    expect(validateCapabilityAdmission(invalid).issues.map(({ code }) => code))
      .toEqual(expect.arrayContaining(['INVALID_FIELD', 'DUPLICATE_VALUE']));
  });

  it('rank>=2 evidence without a repository-bound owner fails closed with EVIDENCE_SOURCE_NOT_FOUND', () => {
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'cap-1', evidenceLevel: 'REVIEWED', receiptRefs: ['receipt-1'],
      workOrderRef: 'wo-1', reviewRef: 'review-1', passingActionIds: ['read'],
      expectedEvidenceOwner: 'CVF_GUARD_CONTRACT', rawSecretsRecorded: false,
    };
    const result = validateCompatibilityEvidence(evidence, {} as never);
    expect(result.valid).toBe(false);
    expect(result.issues.some(({ code }) => code === 'EVIDENCE_SOURCE_NOT_FOUND')).toBe(true);
  });

  it('rejects high-rank evidence paired with a caller-forged handle shape', () => {
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'cap-1', evidenceLevel: 'REVIEWED', receiptRefs: ['receipt-1'],
      workOrderRef: 'wo-1', reviewRef: 'review-1', passingActionIds: ['read'],
      expectedEvidenceOwner: 'CVF_GUARD_CONTRACT', rawSecretsRecorded: false,
    };
    const result = validateCompatibilityEvidence(evidence, FORGED_HANDLE_SHAPE);
    expect(result.valid).toBe(false);
    expect(result.issues.some(({ code }) => code === 'EVIDENCE_SOURCE_NOT_FOUND')).toBe(true);
  });

  it('T2A accepts certified evidence only through the committed repository owner handle', () => {
    const binding = bindCommittedCapabilityOwnerGrant('governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v1.json');
    expect(binding.valid).toBe(true);
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'cvf.cadp.owner-bound-evidence', evidenceLevel: 'CERTIFIED_BOUNDED',
      receiptRefs: ['docs/reviews/evidence/cadp-ai-t2-fail-closed-checkpoint-receipt-2026-08-13.json'],
      workOrderRef: 'docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T2A_REPOSITORY_OWNER_BINDING_CONTINUATION_2026-08-13.md',
      reviewRef: 'docs/reviews/CVF_CADP_AI_T2_INDEPENDENT_ADVERSARIAL_REVIEW_2026-08-13.md',
      freezeRef: 'docs/baselines/CVF_GC018_CADP_AI_T2A_REPOSITORY_OWNER_BINDING_CONTINUATION_2026-08-13.md',
      passingActionIds: ['validateCompatibilityEvidence'],
      expectedEvidenceOwner: 'CVF_GOVERNANCE_REPOSITORY', rawSecretsRecorded: false,
    };
    expect(validateCompatibilityEvidence(evidence, binding.data.handle!).valid).toBe(true);
    expect(validateCompatibilityEvidence(evidence, { ...binding.data.handle! } as CapabilityOwnerHandle).valid).toBe(false);
  });

  it('rejects an invalid evidence level and raw-secret evidence (R02/R05)', () => {
    const evidence = {
      capabilityId: 'cap-1', evidenceLevel: 'TOTALLY_BOGUS', receiptRefs: [],
      passingActionIds: [], expectedEvidenceOwner: 'CVF_GUARD_CONTRACT', rawSecretsRecorded: true,
    } as unknown as CompatibilityEvidenceRecord;
    expect(validateCompatibilityEvidence(evidence, {}).issues.map(({ code }) => code))
      .toEqual(expect.arrayContaining(['EVIDENCE_LEVEL_INVALID', 'RAW_SECRET_INCLUDED']));
  });

  it('validates distribution mode, digest, duplicate paths, secrets and private export (R08)', () => {
    const manifest = {
      distributionId: 'dist-1', capabilityId: 'cap-1', installMode: 'TOTALLY_UNKNOWN',
      contents: [
        { path: 'CVF_SESSION/private.json', sha256: 'zzz', containsSecret: false },
        { path: 'CVF_SESSION/private.json', sha256: 'a'.repeat(64), containsSecret: false },
      ],
      distributionGrantsAssignment: false, distributionGrantsActivation: false,
      distributionGrantsExecution: false, rawSecretsIncluded: false,
    } as unknown as CapabilityDistributionManifest;
    expect(validateCapabilityDistribution(manifest).issues.map(({ code }) => code))
      .toEqual(expect.arrayContaining([
        'INSTALL_MODE_INVALID', 'DIGEST_INVALID', 'DUPLICATE_VALUE', 'PRIVATE_PROVENANCE_EXPORT',
      ]));
  });

  it('accepts a valid local distribution without granting authority', () => {
    const manifest: CapabilityDistributionManifest = {
      distributionId: 'dist-1', capabilityId: 'cap-1', installMode: 'LOCAL_PRIVATE',
      contents: [{ path: 'records/admission.json', sha256: 'a'.repeat(64), containsSecret: false }],
      distributionGrantsAssignment: false, distributionGrantsActivation: false,
      distributionGrantsExecution: false, rawSecretsIncluded: false,
    };
    expect(validateCapabilityDistribution(manifest)).toEqual({
      valid: true, issues: [], data: { activationGranted: false, executionAuthorized: false },
    });
  });

  it('creates receipts deterministic for identical supported input under the implemented canonicalization algorithm (F12)', () => {
    const input = { receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: { b: 2, a: 1 } };
    const first = createDeterministicCadpReceipt(input);
    const second = createDeterministicCadpReceipt(input);
    expect(first).toEqual(second);
    expect(first.receiptId).toBe(`cadp-${first.integrityHash}`);
    expect(first.receiptGrantsExecution).toBe(false);
  });

  it('prevents hostile input fields from overriding receipt identity (R01)', () => {
    const hostile = {
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { safe: true }, receiptId: 'FAKE', contractVersion: 'FAKE', integrityHash: 'FAKE',
    };
    const receipt = createDeterministicCadpReceipt(hostile);
    expect(receipt.receiptId).toBe(`cadp-${receipt.integrityHash}`);
    expect(receipt.contractVersion).toBe('cvf.cadp.v1');
    expect(receipt.integrityHash).not.toBe('FAKE');
  });

  it('uses ordinal key ordering and rejects ambiguous or unsupported payload values (R06/R07)', () => {
    const left = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { z: 1, A: 2, _: 3, a: 4, '\u00e4': 5 },
    });
    const right = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { '\u00e4': 5, a: 4, _: 3, A: 2, z: 1 },
    });
    expect(left).toEqual(right);
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { value: Number.NaN },
    })).toThrow('must be finite');
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { value: BigInt(1) },
    })).toThrow('unsupported type');
  });

  it('deduplicates receipt references before hashing (R09)', () => {
    const receipt = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { safe: true }, evidenceRefs: ['r2', 'r1', 'r2'],
    });
    expect(receipt.evidenceRefs).toEqual(['r1', 'r2']);
  });

  it('rejects non-ISO-8601 issuedAt shapes accepted by loose Date.parse (D6)', () => {
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1',
      issuedAt: 'Thu Jan 01 1970', payload: {},
    })).toThrow('ISO-8601');
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1',
      issuedAt: '2026-13-45T99:99:99Z', payload: {},
    })).toThrow();
    const accepted = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1',
      issuedAt: '2026-08-13T00:00:00.123Z', payload: {},
    });
    expect(accepted.issuedAt).toBe('2026-08-13T00:00:00.123Z');
  });

  it('ignores inherited/prototype-chain properties on record inputs (D10)', () => {
    function AdmissionWithInheritedId(this: Record<string, unknown>) {
      this.decision = 'ADMIT';
      this.sourceVerified = true;
      this.capabilityId = 'cap-1';
      this.capabilityVersion = '1.0.0';
      this.admittedActions = [{ actionId: 'read', mutationType: 'read' }];
      this.executionAuthorized = false;
      this.rawSecretsAllowed = false;
      this.duplicateCanonicalOwnerRequired = false;
    }
    (AdmissionWithInheritedId.prototype as Record<string, unknown>).admissionId = 'inherited-id';
    const inst = new (AdmissionWithInheritedId as unknown as new () => CapabilityAdmissionRecord)();
    expect(Object.prototype.hasOwnProperty.call(inst, 'admissionId')).toBe(false);
    const result = validateCapabilityAdmission(inst);
    expect(result.valid).toBe(false);
    expect(result.issues.map(({ code }) => code)).toContain('INVALID_FIELD');
  });

  it('rejects inherited non-text admission state: decision, sourceVerified, authority and secret flags, admittedActions (R13)', () => {
    function Base(this: Record<string, unknown>) {}
    (Base.prototype as Record<string, unknown>).decision = 'ADMIT';
    (Base.prototype as Record<string, unknown>).sourceVerified = true;
    (Base.prototype as Record<string, unknown>).executionAuthorized = false;
    (Base.prototype as Record<string, unknown>).rawSecretsAllowed = false;
    (Base.prototype as Record<string, unknown>).duplicateCanonicalOwnerRequired = false;
    (Base.prototype as Record<string, unknown>).admittedActions = [{ actionId: 'read', mutationType: 'read' }];
    const inst = new (Base as unknown as new () => CapabilityAdmissionRecord)();
    (inst as unknown as Record<string, unknown>).admissionId = 'a1';
    (inst as unknown as Record<string, unknown>).capabilityId = 'c1';
    (inst as unknown as Record<string, unknown>).capabilityVersion = '1.0.0';
    expect(validateCapabilityAdmission(inst).valid).toBe(false);
  });

  it('rejects a nested admission action with an inherited mutationType (R13)', () => {
    function ActionBase(this: Record<string, unknown>) {}
    (ActionBase.prototype as Record<string, unknown>).mutationType = 'read';
    const action = new (ActionBase as unknown as new () => { actionId: string; mutationType: string })();
    (action as unknown as Record<string, unknown>).actionId = 'x';
    const record = { ...admission, admittedActions: [action] } as unknown as CapabilityAdmissionRecord;
    expect(validateCapabilityAdmission(record).valid).toBe(false);
  });

  it('rejects a distribution content item with an inherited containsSecret field (R13)', () => {
    function ItemBase(this: Record<string, unknown>) {}
    (ItemBase.prototype as Record<string, unknown>).containsSecret = false;
    const item = new (ItemBase as unknown as new () => { path: string; sha256: string })();
    (item as unknown as Record<string, unknown>).path = 'x/y.txt';
    (item as unknown as Record<string, unknown>).sha256 = 'a'.repeat(64);
    const manifest = {
      distributionId: 'd', capabilityId: 'c', installMode: 'LOCAL_PRIVATE',
      contents: [item],
      distributionGrantsAssignment: false, distributionGrantsActivation: false,
      distributionGrantsExecution: false, rawSecretsIncluded: false,
    } as unknown as CapabilityDistributionManifest;
    expect(validateCapabilityDistribution(manifest).valid).toBe(false);
  });

  it('rejects a trustedIndex entry reachable only through the prototype chain (R13)', () => {
    function IndexBase(this: Record<string, unknown>) {}
    (IndexBase.prototype as Record<string, unknown>).r1 = {
      ref: 'r1', artifactType: 'receipt', owner: 'O', integrityVerified: true, authoritative: true,
    };
    const inheritedIndex = new (IndexBase as unknown as new () => Record<string, unknown>)();
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'c1', evidenceLevel: 'RECEIPT_BACKED', receiptRefs: ['r1'],
      passingActionIds: [], expectedEvidenceOwner: 'O', rawSecretsRecorded: false,
    };
    expect(validateCompatibilityEvidence(evidence, inheritedIndex as never).valid).toBe(false);
  });

  it('fails closed rather than throwing on malformed runtime-cast array-shaped fields (R13)', () => {
    const record = { ...admission, admittedActions: 'not-an-array' } as unknown as CapabilityAdmissionRecord;
    expect(() => validateCapabilityAdmission(record)).not.toThrow();
    expect(validateCapabilityAdmission(record).valid).toBe(false);

    const assignment = {
      assignmentId: 's', admissionId: 'admission-1', capabilityId: 'cap-1', capabilityVersion: '1.0.0',
      assignedActionIds: { 0: 'read' }, excludedActionIds: [], workOrderRequired: true,
      executionAuthorized: false, rawSecretsIncluded: false,
    } as unknown as CapabilityAssignmentRecord;
    expect(() => validateCapabilityAssignment(admission, assignment)).not.toThrow();
    expect(validateCapabilityAssignment(admission, assignment).valid).toBe(false);
  });

  it('owns an immutable canonical snapshot unaffected by post-create input mutation (R14)', () => {
    const nested = { a: { b: 1 } };
    const receipt = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: nested,
    });
    const hashBefore = receipt.integrityHash;
    const payloadTextBefore = JSON.stringify(receipt.payload);
    nested.a.b = 999;
    (nested as Record<string, unknown>).newKey = 'injected';
    expect(receipt.integrityHash).toBe(hashBefore);
    expect(JSON.stringify(receipt.payload)).toBe(payloadTextBefore);
  });

  it('rejects mutation of the returned receipt payload, including nested objects and arrays (R14)', () => {
    const receipt = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { a: 1, nested: { b: 2 }, arr: [1, 2, 3] },
    });
    const hashBefore = receipt.integrityHash;
    const payload = receipt.payload as { a: number; nested: { b: number }; arr: number[] };
    expect(() => { payload.a = 999; }).toThrow();
    expect(() => { payload.nested.b = 999; }).toThrow();
    expect(() => { payload.arr.push(4); }).toThrow();
    expect(payload.a).toBe(1);
    expect(payload.nested.b).toBe(2);
    expect(payload.arr).toEqual([1, 2, 3]);
    expect(receipt.integrityHash).toBe(hashBefore);
    expect(receipt.receiptId).toBe(`cadp-${hashBefore}`);
  });

  it('rejects an enumerable accessor property without invoking it (R15)', () => {
    let getterCalls = 0;
    const evil: Record<string, unknown> = {};
    Object.defineProperty(evil, 'x', {
      enumerable: true, configurable: true,
      get() { getterCalls += 1; return Math.random(); },
    });
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: evil,
    })).toThrow(TypeError);
    expect(getterCalls).toBe(0);
  });

  it('rejects symbol-keyed payload data instead of silently excluding it from the hash (R16)', () => {
    const withSymbol: Record<string | symbol, unknown> = { a: 1 };
    withSymbol[Symbol('secret')] = 'hidden-value';
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: withSymbol,
    })).toThrow(TypeError);
  });

  it('rejects a non-enumerable own property instead of silently excluding it from the hash (R16)', () => {
    const hidden: Record<string, unknown> = { visible: 1 };
    Object.defineProperty(hidden, 'secret', { value: 'hidden', enumerable: false, configurable: true });
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: hidden,
    })).toThrow(TypeError);
  });

  it('rejects an array carrying an extra non-index own property (R16)', () => {
    const withExtra: number[] & { extra?: string } = [1, 2, 3];
    withExtra.extra = 'sneaky';
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: { list: withExtra },
    })).toThrow(TypeError);
  });

  it('rejects a symbol-keyed array element (R16)', () => {
    const withSymbol: unknown[] = [1, 2, 3];
    (withSymbol as unknown as Record<symbol, unknown>)[Symbol('tag')] = 'hidden';
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: { list: withSymbol },
    })).toThrow(TypeError);
  });

  it('rejects calendar-invalid timestamps that only match the ISO-8601 regex shape (R17)', () => {
    for (const bad of [
      '2026-02-30T00:00:00Z', '2026-13-01T00:00:00Z', '2026-04-31T00:00:00Z',
      '2026-01-01T24:00:00Z', '2026-01-01T00:60:00Z', '2026-01-01T00:00:60Z',
    ]) {
      expect(() => createDeterministicCadpReceipt({
        receiptType: 'validation', subjectRef: 'cap-1', issuedAt: bad, payload: {},
      }), `expected ${bad} to be rejected`).toThrow();
    }
  });

  it('validates the leap-year boundary exactly: 2024-02-29 accepted, 2026-02-29 rejected (R17)', () => {
    const leapYear = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2024-02-29T00:00:00Z', payload: {},
    });
    expect(leapYear.issuedAt).toBe('2024-02-29T00:00:00Z');
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-02-29T00:00:00Z', payload: {},
    })).toThrow();
  });

  it('rejects a free-form Date-parseable timestamp under exact calendar validation (R17)', () => {
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: 'Thu Jan 01 1970', payload: {},
    })).toThrow();
  });

  it('T2 F11 CLOSURE PROBE: the exact T1 caller-self-attested plain-object index attack is rejected (SUPERSEDED_BY_T2)', () => {
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'c1', evidenceLevel: 'CERTIFIED_BOUNDED',
      receiptRefs: ['r1'], workOrderRef: 'w1', reviewRef: 'v1', freezeRef: 'f1',
      passingActionIds: ['a'], expectedEvidenceOwner: 'SELF_ATTESTED_OWNER', rawSecretsRecorded: false,
    };
    const callerForgedIndex = Object.fromEntries(
      ['r1', 'w1', 'v1', 'f1'].map((ref, index) => [ref, {
        ref, artifactType: (['receipt', 'work_order', 'review', 'freeze'] as const)[index],
        owner: 'SELF_ATTESTED_OWNER', integrityVerified: true, authoritative: true,
      }]),
    );
    // SUPERSEDED_BY_T2_ROUND_2: rounds 1-6 (T1) recorded this exact
    // plain-object index as a residual attack that reached valid=true,
    // evidenceRank=5. T2 round 1 removed the caller-suppliable second
    // parameter entirely; T2 round 2 (this repair, after an independent
    // review reproduced a caller-created-grant-plus-public-binder variant
    // of the same attack against round 1) additionally removed the public
    // binder itself, so no caller path can ever produce a genuine handle.
    // The result is now the more precise `EVIDENCE_SOURCE_NOT_FOUND`
    // disposition rather than the generic `EVIDENCE_UNTRUSTED`, honestly
    // distinguishing "no authenticated owner seam is reachable" from an
    // ordinary mismatch against a real owner.
    const result = validateCompatibilityEvidence(evidence, callerForgedIndex as never);
    expect(result.valid).toBe(false);
    expect(result.issues.some(({ code }) => code === 'EVIDENCE_SOURCE_NOT_FOUND')).toBe(true);
  });

  it('canonical payload array getter is never invoked; getter count remains 0 (R19)', () => {
    let getterCalls = 0;
    const evilArray: unknown[] = [1, 2];
    Object.defineProperty(evilArray, 0, {
      enumerable: true, configurable: true,
      get() { getterCalls += 1; return 1; },
    });
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { list: evilArray },
    })).toThrow(TypeError);
    expect(getterCalls).toBe(0);
  });

  it('validator record-array reader getter count remains 0 (R20)', () => {
    let getterCalls = 0;
    const evilActions: unknown[] = [{ actionId: 'read', mutationType: 'read' }];
    Object.defineProperty(evilActions, 0, {
      enumerable: true, configurable: true,
      get() { getterCalls += 1; return { actionId: 'read', mutationType: 'read' }; },
    });
    const record = { ...admission, admittedActions: evilActions } as unknown as CapabilityAdmissionRecord;
    expect(validateCapabilityAdmission(record).valid).toBe(false);
    expect(getterCalls).toBe(0);
  });

  it('validator string-array reader getter count remains 0 (R20)', () => {
    let getterCalls = 0;
    const evilExcluded: unknown[] = ['x'];
    Object.defineProperty(evilExcluded, 0, {
      enumerable: true, configurable: true,
      get() { getterCalls += 1; return 'x'; },
    });
    const assignment: CapabilityAssignmentRecord = {
      assignmentId: 'assignment-1', admissionId: 'admission-1', capabilityId: 'cap-1',
      capabilityVersion: '1.0.0', assignedActionIds: ['read'],
      excludedActionIds: evilExcluded as unknown as readonly string[],
      workOrderRequired: true, executionAuthorized: false, rawSecretsIncluded: false,
    };
    expect(validateCapabilityAssignment(admission, assignment).valid).toBe(false);
    expect(getterCalls).toBe(0);
  });

  it('rejects a non-enumerable validator array item (R20)', () => {
    const nonEnumerable: unknown[] = [];
    Object.defineProperty(nonEnumerable, 0, {
      enumerable: false, configurable: true, writable: true, value: { actionId: 'read', mutationType: 'read' },
    });
    Object.defineProperty(nonEnumerable, 'length', { value: 1 });
    const record = { ...admission, admittedActions: nonEnumerable } as unknown as CapabilityAdmissionRecord;
    expect(validateCapabilityAdmission(record).valid).toBe(false);
  });

  it('admission identity read for assignment binding invokes zero accessors; getter count remains 0 (R21)', () => {
    let getterCalls = 0;
    const evilAdmission: Record<string, unknown> = { ...admission };
    Object.defineProperty(evilAdmission, 'admissionId', {
      enumerable: true, configurable: true,
      get() { getterCalls += 1; return 'admission-1'; },
    });
    const assignment: CapabilityAssignmentRecord = {
      assignmentId: 'assignment-1', admissionId: 'admission-1', capabilityId: 'cap-1',
      capabilityVersion: '1.0.0', assignedActionIds: ['read'], excludedActionIds: [],
      workOrderRequired: true, executionAuthorized: false, rawSecretsIncluded: false,
    };
    const result = validateCapabilityAssignment(evilAdmission as unknown as CapabilityAdmissionRecord, assignment);
    expect(result.valid).toBe(false);
    expect(getterCalls).toBe(0);
  });

  it('active toString/valueOf/Symbol.toPrimitive hooks are never invoked while building issue messages; count remains 0 (R22)', () => {
    let coercionCalls = 0;
    const hostileDecision = {
      toString() { coercionCalls += 1; return 'ADMIT'; },
      valueOf() { coercionCalls += 1; return 'ADMIT'; },
      [Symbol.toPrimitive]() { coercionCalls += 1; return 'ADMIT'; },
    };
    const admissionResult = validateCapabilityAdmission(
      { ...admission, decision: hostileDecision } as unknown as CapabilityAdmissionRecord,
    );
    expect(admissionResult.valid).toBe(false);

    const hostileMutation = {
      toString() { coercionCalls += 1; return 'read'; },
      valueOf() { coercionCalls += 1; return 'read'; },
      [Symbol.toPrimitive]() { coercionCalls += 1; return 'read'; },
    };
    const withHostileMutation = {
      ...admission,
      admittedActions: [{ actionId: 'read', mutationType: hostileMutation }],
    } as unknown as CapabilityAdmissionRecord;
    expect(validateCapabilityAdmission(withHostileMutation).valid).toBe(false);

    const hostileInstallMode = {
      toString() { coercionCalls += 1; return 'LOCAL_PRIVATE'; },
      valueOf() { coercionCalls += 1; return 'LOCAL_PRIVATE'; },
      [Symbol.toPrimitive]() { coercionCalls += 1; return 'LOCAL_PRIVATE'; },
    };
    const manifest = {
      distributionId: 'd', capabilityId: 'c', installMode: hostileInstallMode,
      contents: [], distributionGrantsAssignment: false, distributionGrantsActivation: false,
      distributionGrantsExecution: false, rawSecretsIncluded: false,
    } as unknown as CapabilityDistributionManifest;
    expect(validateCapabilityDistribution(manifest).valid).toBe(false);

    const hostileEvidenceLevel = {
      toString() { coercionCalls += 1; return 'DECLARED'; },
      valueOf() { coercionCalls += 1; return 'DECLARED'; },
      [Symbol.toPrimitive]() { coercionCalls += 1; return 'DECLARED'; },
    };
    const evidence = {
      capabilityId: 'cap-1', evidenceLevel: hostileEvidenceLevel, receiptRefs: [],
      passingActionIds: [], expectedEvidenceOwner: 'CVF_GUARD_CONTRACT', rawSecretsRecorded: false,
    } as unknown as CompatibilityEvidenceRecord;
    expect(validateCompatibilityEvidence(evidence, {}).valid).toBe(false);

    expect(coercionCalls).toBe(0);
  });

  it('receipt evidenceRefs array getter is never invoked; getter count remains 0 (R24)', () => {
    let getterCalls = 0;
    const evilRefs: unknown[] = ['r1'];
    Object.defineProperty(evilRefs, 0, {
      enumerable: true, configurable: true,
      get() { getterCalls += 1; return 'r1'; },
    });
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { safe: true }, evidenceRefs: evilRefs as unknown as readonly string[],
    })).toThrow(TypeError);
    expect(getterCalls).toBe(0);
  });

  it('rejects malformed evidenceRefs shapes: non-enumerable item, sparse array, symbol key, extra property, non-string, empty/whitespace (R24)', () => {
    const nonEnumerable: unknown[] = [];
    Object.defineProperty(nonEnumerable, 0, { enumerable: false, configurable: true, writable: true, value: 'r1' });
    Object.defineProperty(nonEnumerable, 'length', { value: 1 });
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: {}, evidenceRefs: nonEnumerable as unknown as readonly string[],
    })).toThrow(TypeError);

    const sparse: string[] = [];
    sparse[1] = 'r1';
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: {}, evidenceRefs: sparse,
    })).toThrow(TypeError);

    const symbolKeyed: unknown[] = ['r1'];
    (symbolKeyed as unknown as Record<symbol, unknown>)[Symbol('tag')] = 'hidden';
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: {}, evidenceRefs: symbolKeyed as unknown as readonly string[],
    })).toThrow(TypeError);

    const extraProp: string[] & { extra?: string } = ['r1'];
    extraProp.extra = 'sneaky';
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: {}, evidenceRefs: extraProp,
    })).toThrow(TypeError);

    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: {}, evidenceRefs: [123] as unknown as readonly string[],
    })).toThrow(TypeError);

    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: {}, evidenceRefs: ['   '],
    })).toThrow(TypeError);
  });

  it('negative-zero payload normalizes to +0: matching hash and Object.is-consistent returned value (R23)', () => {
    const negativeZero = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { value: -0 },
    });
    const positiveZero = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { value: 0 },
    });
    expect(negativeZero.integrityHash).toBe(positiveZero.integrityHash);
    const returnedValue = (negativeZero.payload as { value: number }).value;
    expect(Object.is(returnedValue, -0)).toBe(false);
    expect(Object.is(returnedValue, 0)).toBe(true);
  });

  it('negative-zero identity holds for nested objects and arrays without mutating caller input (R23)', () => {
    const inputPayload = { nested: { value: -0 }, list: [-0, 1, -0] };
    const receipt = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: inputPayload,
    });
    expect(Object.is(inputPayload.nested.value, -0)).toBe(true);
    expect(Object.is(inputPayload.list[0], -0)).toBe(true);
    const returnedPayload = receipt.payload as { nested: { value: number }; list: number[] };
    expect(Object.is(returnedPayload.nested.value, -0)).toBe(false);
    expect(Object.is(returnedPayload.list[0], -0)).toBe(false);
    expect(Object.is(returnedPayload.list[2], -0)).toBe(false);
    const positiveEquivalent = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { nested: { value: 0 }, list: [0, 1, 0] },
    });
    expect(receipt.integrityHash).toBe(positiveEquivalent.integrityHash);
  });

  it('fractional-second timestamp rule matches the error message exactly: 1-9 optional digits accepted, 10+ rejected (R25)', () => {
    const oneDigit = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00.1Z', payload: {},
    });
    expect(oneDigit.issuedAt).toBe('2026-08-13T00:00:00.1Z');
    const nineDigits = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00.123456789Z', payload: {},
    });
    expect(nineDigits.issuedAt).toBe('2026-08-13T00:00:00.123456789Z');
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00.1234567890Z', payload: {},
    })).toThrow('1-9 optional fractional digits');
  });

  it('SUPERSEDED_BY_T2_ROUND_2: the R19-R25-era F11 residual probe now shows the same attack rejected (BLOCKED_SOURCE_NOT_FOUND)', () => {
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'c1', evidenceLevel: 'CERTIFIED_BOUNDED',
      receiptRefs: ['r1'], workOrderRef: 'w1', reviewRef: 'v1', freezeRef: 'f1',
      passingActionIds: ['a'], expectedEvidenceOwner: 'SELF_ATTESTED_OWNER', rawSecretsRecorded: false,
    };
    const callerForgedIndex = Object.fromEntries(
      ['r1', 'w1', 'v1', 'f1'].map((ref, index) => [ref, {
        ref, artifactType: (['receipt', 'work_order', 'review', 'freeze'] as const)[index],
        owner: 'SELF_ATTESTED_OWNER', integrityVerified: true, authoritative: true,
      }]),
    );
    const result = validateCompatibilityEvidence(evidence, callerForgedIndex as never);
    expect(result.valid).toBe(false);
    expect(result.issues.some(({ code }) => code === 'EVIDENCE_SOURCE_NOT_FOUND')).toBe(true);
  });

  it('receipt front door: top-level receiptType getter is never invoked; getter count remains 0 (R26)', () => {
    let getterCalls = 0;
    const evilInput: Record<string, unknown> = { subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: {} };
    Object.defineProperty(evilInput, 'receiptType', {
      enumerable: true, configurable: true,
      get() { getterCalls += 1; return 'validation'; },
    });
    expect(() => createDeterministicCadpReceipt(evilInput as never)).toThrow(TypeError);
    expect(getterCalls).toBe(0);
  });

  it('receipt front door: inherited-only receiptType/subjectRef/issuedAt are rejected, not read through the prototype chain (R26)', () => {
    function InheritedInput(this: Record<string, unknown>) {}
    (InheritedInput.prototype as Record<string, unknown>).receiptType = 'inherited-type';
    (InheritedInput.prototype as Record<string, unknown>).subjectRef = 'inherited-ref';
    (InheritedInput.prototype as Record<string, unknown>).issuedAt = '2026-08-13T00:00:00Z';
    const inst = new (InheritedInput as unknown as new () => Record<string, unknown>)();
    inst.payload = {};
    expect(() => createDeterministicCadpReceipt(inst as never)).toThrow(TypeError);
  });

  it('receipt front door: active toString/valueOf/Symbol.toPrimitive on receiptType are never invoked; count remains 0 (R26)', () => {
    let coercionCalls = 0;
    const hostileReceiptType = {
      toString() { coercionCalls += 1; return 'validation'; },
      valueOf() { coercionCalls += 1; return 'validation'; },
      [Symbol.toPrimitive]() { coercionCalls += 1; return 'validation'; },
    };
    expect(() => createDeterministicCadpReceipt({
      receiptType: hostileReceiptType as never, subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: {},
    })).toThrow(TypeError);
    expect(coercionCalls).toBe(0);
  });

  it('receipt front door: a payload accessor is rejected without invocation; getter count remains 0 (R26)', () => {
    let getterCalls = 0;
    const evilInput: Record<string, unknown> = { receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z' };
    Object.defineProperty(evilInput, 'payload', {
      enumerable: true, configurable: true,
      get() { getterCalls += 1; return {}; },
    });
    expect(() => createDeterministicCadpReceipt(evilInput as never)).toThrow(TypeError);
    expect(getterCalls).toBe(0);
  });

  it('receipt front door: a top-level evidenceRefs accessor is rejected without invocation; getter count remains 0 (R26)', () => {
    let getterCalls = 0;
    const evilInput: Record<string, unknown> = { receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: {} };
    Object.defineProperty(evilInput, 'evidenceRefs', {
      enumerable: true, configurable: true,
      get() { getterCalls += 1; return ['r1']; },
    });
    expect(() => createDeterministicCadpReceipt(evilInput as never)).toThrow(TypeError);
    expect(getterCalls).toBe(0);
  });

  it('receipt front door: a non-enumerable required field is rejected (R26)', () => {
    const evilInput: Record<string, unknown> = { subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: {} };
    Object.defineProperty(evilInput, 'receiptType', { value: 'validation', enumerable: false, configurable: true });
    expect(() => createDeterministicCadpReceipt(evilInput as never)).toThrow(TypeError);
  });

  it('receipt front door: a genuinely missing evidenceRefs own property is allowed and defaults to empty (R26)', () => {
    const receipt = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: {},
    });
    expect(receipt.evidenceRefs).toEqual([]);
  });

  it('Proxy boundary: a Proxy admission record returns valid=false with zero traps invoked, root record (R27)', () => {
    let trapCalls = 0;
    const target: CapabilityAdmissionRecord = {
      admissionId: 'a', capabilityId: 'c', capabilityVersion: '1.0.0',
      decision: 'ADMIT', sourceVerified: true,
      admittedActions: [{ actionId: 'read', mutationType: 'read' }],
      executionAuthorized: false, rawSecretsAllowed: false, duplicateCanonicalOwnerRequired: false,
    };
    const proxied = new Proxy(target, {
      get(t, k, r) { trapCalls += 1; return Reflect.get(t, k, r); },
      getPrototypeOf(t) { trapCalls += 1; return Reflect.getPrototypeOf(t); },
      ownKeys(t) { trapCalls += 1; return Reflect.ownKeys(t); },
      getOwnPropertyDescriptor(t, k) { trapCalls += 1; return Reflect.getOwnPropertyDescriptor(t, k); },
    });
    const result = validateCapabilityAdmission(proxied);
    expect(result.valid).toBe(false);
    expect(trapCalls).toBe(0);
  });

  it('Proxy boundary: a Proxy distribution manifest returns valid=false with zero traps invoked (R27)', () => {
    let trapCalls = 0;
    const target: CapabilityDistributionManifest = {
      distributionId: 'd', capabilityId: 'c', installMode: 'LOCAL_PRIVATE',
      contents: [], distributionGrantsAssignment: false, distributionGrantsActivation: false,
      distributionGrantsExecution: false, rawSecretsIncluded: false,
    };
    const proxied = new Proxy(target, {
      get() { trapCalls += 1; return undefined; },
      getOwnPropertyDescriptor() { trapCalls += 1; return undefined; },
      getPrototypeOf() { trapCalls += 1; return null; },
      ownKeys() { trapCalls += 1; return []; },
    });
    expect(() => validateCapabilityDistribution(proxied)).not.toThrow();
    expect(validateCapabilityDistribution(proxied).valid).toBe(false);
    expect(trapCalls).toBe(0);
  });

  it('Proxy boundary: a Proxy trustedIndex and a Proxy artifact record are both rejected with zero traps invoked (R27)', () => {
    let trapCalls = 0;
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'c1', evidenceLevel: 'RECEIPT_BACKED', receiptRefs: ['r1'],
      passingActionIds: [], expectedEvidenceOwner: 'O', rawSecretsRecorded: false,
    };
    const artifactProxy = new Proxy(
      { ref: 'r1', artifactType: 'receipt', owner: 'O', integrityVerified: true, authoritative: true },
      {
        get() { trapCalls += 1; return undefined; },
        getOwnPropertyDescriptor() { trapCalls += 1; return undefined; },
      },
    );
    const withArtifactProxy = validateCompatibilityEvidence(evidence, { r1: artifactProxy } as never);
    expect(withArtifactProxy.valid).toBe(false);
    expect(trapCalls).toBe(0);

    const trustedIndexProxy = new Proxy({}, {
      get() { trapCalls += 1; return undefined; },
      getOwnPropertyDescriptor() { trapCalls += 1; return undefined; },
      ownKeys() { trapCalls += 1; return []; },
    });
    const withIndexProxy = validateCompatibilityEvidence(evidence, trustedIndexProxy as never);
    expect(withIndexProxy.valid).toBe(false);
    expect(trapCalls).toBe(0);
  });

  it('Proxy boundary: a Proxy nested admission action record and a Proxy caller-owned array are both rejected with zero traps invoked (R27)', () => {
    let trapCalls = 0;
    const actionProxy = new Proxy({ actionId: 'read', mutationType: 'read' }, {
      get() { trapCalls += 1; return undefined; },
      getOwnPropertyDescriptor() { trapCalls += 1; return undefined; },
    });
    const withProxiedAction = {
      ...admission,
      admittedActions: [actionProxy],
    } as unknown as CapabilityAdmissionRecord;
    expect(validateCapabilityAdmission(withProxiedAction).valid).toBe(false);
    expect(trapCalls).toBe(0);

    const arrayProxy = new Proxy([{ actionId: 'read', mutationType: 'read' }], {
      get() { trapCalls += 1; return undefined; },
      getOwnPropertyDescriptor() { trapCalls += 1; return undefined; },
      ownKeys() { trapCalls += 1; return []; },
    });
    const withProxiedArray = { ...admission, admittedActions: arrayProxy } as unknown as CapabilityAdmissionRecord;
    expect(() => validateCapabilityAdmission(withProxiedArray)).not.toThrow();
    expect(validateCapabilityAdmission(withProxiedArray).valid).toBe(false);
    expect(trapCalls).toBe(0);
  });

  it('Proxy boundary: a Proxy receipt input throws a controlled TypeError with zero traps invoked (R27)', () => {
    let trapCalls = 0;
    const proxiedInput = new Proxy(
      { receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: {} },
      {
        get() { trapCalls += 1; return undefined; },
        getOwnPropertyDescriptor() { trapCalls += 1; return undefined; },
        getPrototypeOf() { trapCalls += 1; return null; },
        ownKeys() { trapCalls += 1; return []; },
      },
    );
    expect(() => createDeterministicCadpReceipt(proxiedInput)).toThrow(TypeError);
    expect(trapCalls).toBe(0);
  });

  it('Proxy boundary: a Proxy nested inside the receipt payload throws a controlled TypeError with zero traps invoked (R27)', () => {
    let trapCalls = 0;
    const innerProxy = new Proxy({ a: 1 }, {
      get() { trapCalls += 1; return 1; },
      getPrototypeOf() { trapCalls += 1; return Object.prototype; },
      ownKeys() { trapCalls += 1; return ['a']; },
      getOwnPropertyDescriptor() { trapCalls += 1; return { value: 1, enumerable: true, configurable: true, writable: true }; },
    });
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z',
      payload: { nested: innerProxy },
    })).toThrow(TypeError);
    expect(trapCalls).toBe(0);
  });

  it('Proxy boundary: a revoked object Proxy in the receipt payload throws a controlled TypeError, not an incidental error (R27)', () => {
    const { proxy, revoke } = Proxy.revocable({}, {});
    revoke();
    expect(() => createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: proxy,
    })).toThrow(TypeError);
  });

  it('Proxy boundary: a revoked array Proxy used as a validator array field fails closed, not an incidental error (R27)', () => {
    const { proxy, revoke } = Proxy.revocable([{ actionId: 'read', mutationType: 'read' }], {});
    revoke();
    const withRevokedArray = { ...admission, admittedActions: proxy } as unknown as CapabilityAdmissionRecord;
    expect(() => validateCapabilityAdmission(withRevokedArray)).not.toThrow();
    expect(validateCapabilityAdmission(withRevokedArray).valid).toBe(false);
  });

  it('Proxy boundary: a revoked object Proxy used as a validator record field fails closed, not an incidental error (R27)', () => {
    const { proxy, revoke } = Proxy.revocable(
      { admissionId: 'a', capabilityId: 'c', capabilityVersion: '1.0.0' },
      {},
    );
    revoke();
    const assignment: CapabilityAssignmentRecord = {
      assignmentId: 's', admissionId: 'admission-1', capabilityId: 'cap-1', capabilityVersion: '1.0.0',
      assignedActionIds: ['read'], excludedActionIds: [], workOrderRequired: true,
      executionAuthorized: false, rawSecretsIncluded: false,
    };
    expect(() => validateCapabilityAssignment(proxy as unknown as CapabilityAdmissionRecord, assignment)).not.toThrow();
    expect(validateCapabilityAssignment(proxy as unknown as CapabilityAdmissionRecord, assignment).valid).toBe(false);
  });

  it('R28: negative-zero snapshot/hash consistency remains normalized to +0 after the reflection-boundary repair (SUPERSEDED_BY_R23 sanity check)', () => {
    const negativeZero = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: { value: -0 },
    });
    const positiveZero = createDeterministicCadpReceipt({
      receiptType: 'validation', subjectRef: 'cap-1', issuedAt: '2026-08-13T00:00:00Z', payload: { value: 0 },
    });
    expect(negativeZero.integrityHash).toBe(positiveZero.integrityHash);
    expect(Object.is((negativeZero.payload as { value: number }).value, -0)).toBe(false);
  });

  it('SUPERSEDED_BY_T2_ROUND_2: the R26-R28-era F11 residual probe now shows the same attack rejected (BLOCKED_SOURCE_NOT_FOUND)', () => {
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'c1', evidenceLevel: 'CERTIFIED_BOUNDED',
      receiptRefs: ['r1'], workOrderRef: 'w1', reviewRef: 'v1', freezeRef: 'f1',
      passingActionIds: ['a'], expectedEvidenceOwner: 'SELF_ATTESTED_OWNER', rawSecretsRecorded: false,
    };
    const callerForgedIndex = Object.fromEntries(
      ['r1', 'w1', 'v1', 'f1'].map((ref, index) => [ref, {
        ref, artifactType: (['receipt', 'work_order', 'review', 'freeze'] as const)[index],
        owner: 'SELF_ATTESTED_OWNER', integrityVerified: true, authoritative: true,
      }]),
    );
    const result = validateCompatibilityEvidence(evidence, callerForgedIndex as never);
    expect(result.valid).toBe(false);
    expect(result.issues.some(({ code }) => code === 'EVIDENCE_SOURCE_NOT_FOUND')).toBe(true);
  });

  it('T2: an unbound/forged CapabilityOwnerHandle-shaped object never satisfies isBoundCapabilityOwner (F11 closure)', () => {
    const forgedHandle = { contractVersion: 'cvf.cadp.ownerBinding.v1' } as unknown as CapabilityOwnerHandle;
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'cap-1', evidenceLevel: 'RECEIPT_BACKED', receiptRefs: ['receipt-1'],
      passingActionIds: [], expectedEvidenceOwner: 'CVF_GUARD_CONTRACT', rawSecretsRecorded: false,
    };
    expect(validateCompatibilityEvidence(evidence, forgedHandle).valid).toBe(false);
  });

  it('rejects a spread copy of a handle shape', () => {
    const copiedHandle = { ...FORGED_HANDLE_SHAPE } as CapabilityOwnerHandle;
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'cap-1', evidenceLevel: 'RECEIPT_BACKED', receiptRefs: ['receipt-1'],
      passingActionIds: [], expectedEvidenceOwner: 'CVF_GUARD_CONTRACT', rawSecretsRecorded: false,
    };
    expect(validateCompatibilityEvidence(evidence, FORGED_HANDLE_SHAPE).valid).toBe(false);
    expect(validateCompatibilityEvidence(evidence, copiedHandle).valid).toBe(false);
  });

  it('rejects a JSON round trip of a handle shape', () => {
    const roundTripped = JSON.parse(JSON.stringify(FORGED_HANDLE_SHAPE)) as CapabilityOwnerHandle;
    const evidence: CompatibilityEvidenceRecord = {
      capabilityId: 'cap-1', evidenceLevel: 'RECEIPT_BACKED', receiptRefs: ['receipt-1'],
      passingActionIds: [], expectedEvidenceOwner: 'CVF_GUARD_CONTRACT', rawSecretsRecorded: false,
    };
    expect(validateCompatibilityEvidence(evidence, roundTripped).valid).toBe(false);
  });

  it('direct module exports contain no generic caller-data owner binder', () => {
    return import('./capability-owner-binding.contract').then((productionModule) => {
      const moduleExports = productionModule as unknown as Record<string, unknown>;
      expect(moduleExports.bindNamedCapabilityOwner).toBeUndefined();
      expect(moduleExports.bindNamedCapabilityOwner_TEST_ONLY_INTERNAL_BINDER).toBeUndefined();
      expect(moduleExports.bindNamedCapabilityOwnerForTest).toBeUndefined();
      expect((moduleExports.bindCommittedCapabilityOwnerGrant as (value: unknown) => { valid: boolean })({}).valid).toBe(false);
    });
  });
});
