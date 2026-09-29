import { describe, expect, it } from 'vitest';
import {
  ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_CONTRACT_VERSION,
  evaluateAssfCapabilityPreflightCandidateBinding,
  type AssfCapabilityPreflightCandidateBindingInput,
  type AssfCapabilityPreflightCandidateBindingResult,
  type AssfPackageMetadata,
} from './assf-capability-preflight-candidate-binding.contract';
import { evaluateAssfCapabilityPreflightCandidateBinding as contractsBarrelEvaluator } from './index';
import { evaluateAssfCapabilityPreflightCandidateBinding as rootBarrelEvaluator } from '../index';

const NOW = '2026-08-17T10:00:00Z';
const PACKAGE_ID = 'cvf-code-intelligence-context-review';

function metadata(overrides: Partial<AssfPackageMetadata> = {}): AssfPackageMetadata {
  return {
    skillId: PACKAGE_ID,
    version: '0.1.0',
    status: 'CANDIDATE',
    candidateState: 'CANDIDATE',
    approvalState: 'AWAITING_REVIEW',
    uatState: 'NOT_STARTED',
    certificationState: 'NOT_STARTED',
    riskCeiling: 'R1',
    authorityCeiling: 'read-only planning and review guidance',
    externalCliMcpDisposition: 'DEFERRED_WITH_REASON',
    capabilityBoundary: 'no package root, no resolver activation, no runtime',
    platformCompatibility: ['win32', 'linux', 'darwin'],
    taskClasses: ['code-review', 'implementation-planning'],
    dependencies: [],
    conflicts: [],
    sourceArtifacts: ['docs/reviews/CVF_CGE_R2_CODEGRAPH_RESCAN_VALUE_AUDIT_AND_CORRECTION_2026-06-29.md'],
    ...overrides,
  };
}

function approvedActiveMetadata(overrides: Partial<AssfPackageMetadata> = {}): AssfPackageMetadata {
  return metadata({
    status: 'ACTIVE',
    candidateState: 'ACTIVE',
    approvalState: 'APPROVED',
    uatState: 'PASSED',
    certificationState: 'CERTIFIED',
    ...overrides,
  });
}

function input(overrides: Partial<AssfCapabilityPreflightCandidateBindingInput> = {}): AssfCapabilityPreflightCandidateBindingInput {
  return {
    schemaVersion: ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_CONTRACT_VERSION,
    expectedPackageId: PACKAGE_ID,
    metadata: metadata(),
    now: NOW,
    ...overrides,
  };
}

function clone<T>(value: T): T {
  return structuredClone(value);
}

function codes(result: AssfCapabilityPreflightCandidateBindingResult): string[] {
  return result.issues.map((issue) => issue.code);
}

const AUTHORITY_FIELDS = [
  'activationAuthorized', 'loadingAuthorized', 'instructionBodyReadAuthorized',
  'executionAuthorized', 'mutationAuthorized', 'acquisitionAuthorized',
  'externalAdapterAuthorized', 'providerCallAuthorized', 'publicWriteAuthorized',
  'taskAuthorityGranted',
] as const;

describe('ASSF capability-preflight candidate binding', () => {
  it('exports the exact evaluator through both Guard Contract barrels', () => {
    expect(contractsBarrelEvaluator).toBe(evaluateAssfCapabilityPreflightCandidateBinding);
    expect(rootBarrelEvaluator).toBe(evaluateAssfCapabilityPreflightCandidateBinding);
  });

  it('accepts an approved/active, source-backed, certified metadata projection as routing-eligible', () => {
    const evidence = input({ metadata: approvedActiveMetadata() });
    const before = clone(evidence);
    const first = evaluateAssfCapabilityPreflightCandidateBinding(evidence);
    const second = evaluateAssfCapabilityPreflightCandidateBinding(evidence);

    expect(first).toEqual(second);
    expect(evidence).toEqual(before);
    expect(first.bindingStatus).toBe('CANDIDATE_BINDING_ACCEPTED');
    expect(first.packageId).toBe(PACKAGE_ID);
    expect(first.lifecycleStatus).toBe('ACTIVE');
    expect(first.candidateState).toBe('ACTIVE');
    expect(first.approvalState).toBe('APPROVED');
    expect(first.uatState).toBe('PASSED');
    expect(first.certificationState).toBe('CERTIFIED');
    expect(first.riskCeiling).toBe('R1');
    expect(first.authorityCeiling).toBe('read-only planning and review guidance');
    expect(first.externalCliMcpDisposition).toBe('DEFERRED_WITH_REASON');
    expect(first.capabilityBoundary).toBe('no package root, no resolver activation, no runtime');
    expect(first.taskClasses).toEqual(['code-review', 'implementation-planning']);
    expect(first.routingEligible).toBe(true);
    expect(first.authorityStatus).toBe('CANDIDATE_ONLY');
    expect(first.issues).toEqual([]);
    expect(Object.isFrozen(first)).toBe(true);
    expect(Object.isFrozen(first.issues)).toBe(true);
    for (const field of AUTHORITY_FIELDS) expect(first[field]).toBe(false);
  });

  it('accepts a plain CANDIDATE-state metadata projection as non-routable', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(input());
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_ACCEPTED');
    expect(result.routingEligible).toBe(false);
    expect(result.authorityStatus).toBe('CANDIDATE_ONLY');
    expect(result.issues).toEqual([]);
  });

  it.each([
    ['null', null],
    ['array', []],
    ['class', new (class Envelope {})()],
    ['string', 'not-an-object'],
  ])('rejects a malformed %s envelope without throwing', (_label, value) => {
    expect(() => evaluateAssfCapabilityPreflightCandidateBinding(value)).not.toThrow();
    expect(evaluateAssfCapabilityPreflightCandidateBinding(value).bindingStatus).toBe('CANDIDATE_BINDING_BLOCKED');
  });

  it('rejects unknown top-level and metadata keys', () => {
    const withExtra = input() as unknown as Record<string, unknown>;
    withExtra.extra = true;
    const topLevel = evaluateAssfCapabilityPreflightCandidateBinding(withExtra);
    expect(topLevel.bindingStatus).toBe('CANDIDATE_BINDING_BLOCKED');
    expect(codes(topLevel)).toContain('UNKNOWN_KEY');

    const metaExtra = input({ metadata: { ...metadata(), extra: true } as unknown as AssfPackageMetadata });
    const metaResult = evaluateAssfCapabilityPreflightCandidateBinding(metaExtra);
    expect(metaResult.bindingStatus).toBe('CANDIDATE_BINDING_BLOCKED');
    expect(codes(metaResult)).toContain('UNKNOWN_KEY');
  });

  it('rejects proxies, accessors, prototype pollution, and symbol keys without invoking user hooks', () => {
    let invoked = 0;
    const proxied = new Proxy(input(), { get() { invoked += 1; throw new Error('must not run'); } });
    expect(evaluateAssfCapabilityPreflightCandidateBinding(proxied).bindingStatus).toBe('CANDIDATE_BINDING_BLOCKED');

    const accessor = input() as unknown as Record<string, unknown>;
    Object.defineProperty(accessor, 'now', { enumerable: true, get() { invoked += 1; throw new Error('must not run'); } });
    expect(evaluateAssfCapabilityPreflightCandidateBinding(accessor).bindingStatus).toBe('CANDIDATE_BINDING_BLOCKED');

    const inherited = Object.create({ inherited: true });
    Object.assign(inherited, input());
    expect(evaluateAssfCapabilityPreflightCandidateBinding(inherited).bindingStatus).toBe('CANDIDATE_BINDING_BLOCKED');

    const symbolKeyed = input() as unknown as Record<PropertyKey, unknown>;
    symbolKeyed[Symbol('x')] = 'y';
    expect(evaluateAssfCapabilityPreflightCandidateBinding(symbolKeyed).bindingStatus).toBe('CANDIDATE_BINDING_BLOCKED');

    expect(invoked).toBe(0);
  });

  it('rejects a NUL/control-character-bearing string at every free-text boundary', () => {
    const controlBearing = [0, 7, 127].map((code) => 'bad' + String.fromCharCode(code) + 'id');
    for (const bad of controlBearing) {
      const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ metadata: metadata({ skillId: bad }) }));
      expect(result.bindingStatus).not.toBe('CANDIDATE_BINDING_ACCEPTED');
      expect(codes(result)).toContain('UNSAFE_STRING');
    }
  });

  it('rejects secret-like values at every free-text/list boundary', () => {
    const boundaries: Array<Partial<AssfPackageMetadata>> = [
      { authorityCeiling: 'api_key=abcdef123456' },
      { capabilityBoundary: 'password=hunter2hunter2' },
      { taskClasses: ['token=abcdef123456789012'] },
      { sourceArtifacts: ['secret=abcdef123456789012'] },
    ];
    for (const partial of boundaries) {
      const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ metadata: metadata(partial) }));
      expect(result.bindingStatus).not.toBe('CANDIDATE_BINDING_ACCEPTED');
      expect(codes(result)).toContain('RAW_SECRET_DETECTED');
      expect(JSON.stringify(result)).not.toContain('abcdef123456');
      expect(JSON.stringify(result)).not.toContain('hunter2hunter2');
    }
  });

  it('rejects an invalid now timestamp', () => {
    for (const bad of ['not-a-date', '2026-08-17', '2026-13-40T00:00:00Z']) {
      const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ now: bad }));
      expect(result.bindingStatus).not.toBe('CANDIDATE_BINDING_ACCEPTED');
      expect(codes(result)).toContain('INVALID_FIELD');
    }
  });

  it('rejects an unsupported schemaVersion', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ schemaVersion: 'wrong.version' as never }));
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('INVALID_FIELD');
  });

  it('rejects a package identity mismatch between expectedPackageId and metadata.skillId', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ expectedPackageId: 'other-package' }));
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('PACKAGE_ID_MISMATCH');
  });

  it('rejects missing source refs (empty sourceArtifacts)', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ metadata: metadata({ sourceArtifacts: [] }) }));
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('INVALID_FIELD');
  });

  it('rejects self-dependency', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ metadata: metadata({ dependencies: [PACKAGE_ID] }) }));
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('SELF_DEPENDENCY');
  });

  it('rejects self-conflict', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ metadata: metadata({ conflicts: [PACKAGE_ID] }) }));
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('INVALID_FIELD');
  });

  it('rejects dependency/conflict overlap', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: metadata({ dependencies: ['other-package'], conflicts: ['other-package'] }) }),
    );
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('DEPENDENCY_CONFLICT_OVERLAP');
  });

  it('rejects duplicate values in dependencies, conflicts, platforms, task classes, and source artifacts', () => {
    const cases: Array<Partial<AssfPackageMetadata>> = [
      { dependencies: ['a', 'a'] },
      { conflicts: ['b', 'b'] },
      { platformCompatibility: ['win32', 'win32'] },
      { taskClasses: ['code-review', 'code-review'] },
      { sourceArtifacts: ['docs/a.md', 'docs/a.md'] },
    ];
    for (const partial of cases) {
      const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ metadata: metadata(partial) }));
      expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
      expect(codes(result)).toContain('DUPLICATE_VALUE');
    }
  });

  it.each([
    ['DEPRECATED'], ['RETIRED'], ['REJECTED'],
  ])('rejects an ineligible %s lifecycle status as LIFECYCLE_INELIGIBLE', (status) => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: metadata({ status: status as AssfPackageMetadata['status'], candidateState: status as AssfPackageMetadata['status'] }) }),
    );
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('LIFECYCLE_INELIGIBLE');
    expect(result.routingEligible).toBe(false);
  });

  it('rejects contradictory lifecycle evidence: status vs candidateState mismatch', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: metadata({ status: 'CANDIDATE', candidateState: 'APPROVED' }) }),
    );
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('LIFECYCLE_CONTRADICTION');
  });

  it('rejects contradictory lifecycle evidence: rejected approval with an eligible status', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: metadata({ approvalState: 'REJECTED' }) }),
    );
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('LIFECYCLE_CONTRADICTION');
  });

  it('rejects contradictory lifecycle evidence: failed UAT with an approved/active status', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: approvedActiveMetadata({ uatState: 'FAILED' }) }),
    );
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('LIFECYCLE_CONTRADICTION');
  });

  it('rejects contradictory lifecycle evidence: failed certification with ACTIVE status', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: approvedActiveMetadata({ certificationState: 'FAILED' }) }),
    );
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('LIFECYCLE_CONTRADICTION');
  });

  it('requires certification for an ACTIVE package even when approval and UAT pass', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: approvedActiveMetadata({ certificationState: 'NOT_STARTED' }) }),
    );
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('CERTIFICATION_REQUIRED');
  });

  it.each(['NOT_STARTED', 'IN_PROGRESS'] as const)(
    'requires passed UAT evidence for an ACTIVE package when UAT is %s',
    (uatState) => {
      const result = evaluateAssfCapabilityPreflightCandidateBinding(
        input({ metadata: approvedActiveMetadata({ uatState }) }),
      );
      expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
      expect(result.routingEligible).toBe(false);
      expect(codes(result)).toContain('UAT_REQUIRED');
    },
  );

  it('accepts an APPROVED (non-ACTIVE) package as routing-eligible without requiring certification', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(
      input({
        metadata: metadata({
          status: 'APPROVED', candidateState: 'APPROVED', approvalState: 'APPROVED',
          uatState: 'PASSED', certificationState: 'NOT_STARTED',
        }),
      }),
    );
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_ACCEPTED');
    expect(result.routingEligible).toBe(true);
  });

  it('rejects unknown or unsupported lifecycle/approval/UAT/certification/risk/disposition enum values', () => {
    const cases: Array<Partial<AssfPackageMetadata>> = [
      { status: 'BOGUS' as never },
      { candidateState: 'BOGUS' as never },
      { approvalState: 'BOGUS' as never },
      { uatState: 'BOGUS' as never },
      { certificationState: 'BOGUS' as never },
      { riskCeiling: 'R9' as never },
      { externalCliMcpDisposition: 'BOGUS' as never },
    ];
    for (const partial of cases) {
      const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ metadata: metadata(partial) }));
      expect(result.bindingStatus).not.toBe('CANDIDATE_BINDING_ACCEPTED');
      expect(codes(result)).toContain('INVALID_FIELD');
    }
  });

  it('rejects an authority/risk weakening attempt via an implemented external CLI/MCP adapter claim', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: metadata({ externalCliMcpDisposition: 'IMPLEMENTED' }) }),
    );
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
    expect(codes(result)).toContain('EXTERNAL_ADAPTER_FORBIDDEN');
  });

  it('rejects an attempt to supply output/authority fields inside the metadata envelope', () => {
    const polluted = {
      ...metadata(),
      authorityStatus: 'FULL_ACCESS',
      taskAuthorityGranted: true,
    } as unknown as AssfPackageMetadata;
    const result = evaluateAssfCapabilityPreflightCandidateBinding(input({ metadata: polluted }));
    expect(result.bindingStatus).toBe('CANDIDATE_BINDING_BLOCKED');
    expect(codes(result)).toContain('UNKNOWN_KEY');
  });

  it('rejects sparse and oversized arrays', () => {
    const sparse: unknown[] = [];
    sparse[3] = 'win32';
    const sparseResult = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: { ...metadata(), platformCompatibility: sparse } as unknown as AssfPackageMetadata }),
    );
    expect(sparseResult.bindingStatus).not.toBe('CANDIDATE_BINDING_ACCEPTED');
    expect(codes(sparseResult)).toContain('SPARSE_ARRAY');

    const oversized = Array.from({ length: 100 }, (_, i) => `task-${i}`);
    const oversizedResult = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: metadata({ taskClasses: oversized }) }),
    );
    expect(oversizedResult.bindingStatus).not.toBe('CANDIDATE_BINDING_ACCEPTED');
    expect(codes(oversizedResult)).toContain('UNBOUNDED_COLLECTION');
  });

  it('rejects a Proxy array and an Array subclass for a metadata collection field', () => {
    const proxyArray = new Proxy(['win32'], {});
    const proxyResult = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: { ...metadata(), platformCompatibility: proxyArray } as unknown as AssfPackageMetadata }),
    );
    expect(proxyResult.bindingStatus).not.toBe('CANDIDATE_BINDING_ACCEPTED');

    class FancyArray extends Array {}
    const subclassArray = FancyArray.from(['win32']);
    const subclassResult = evaluateAssfCapabilityPreflightCandidateBinding(
      input({ metadata: { ...metadata(), platformCompatibility: subclassArray } as unknown as AssfPackageMetadata }),
    );
    expect(subclassResult.bindingStatus).not.toBe('CANDIDATE_BINDING_ACCEPTED');
  });

  it('rejects a revoked Proxy array without throwing', () => {
    const revocable = Proxy.revocable(['win32'], {});
    revocable.revoke();
    const hostile = input({
      metadata: {
        ...metadata(),
        platformCompatibility: revocable.proxy,
      } as unknown as AssfPackageMetadata,
    });
    expect(() => evaluateAssfCapabilityPreflightCandidateBinding(hostile)).not.toThrow();
    expect(evaluateAssfCapabilityPreflightCandidateBinding(hostile).bindingStatus).toBe('CANDIDATE_BINDING_REJECTED');
  });

  it('always reports authorityStatus CANDIDATE_ONLY and every action-authority field as literal false', () => {
    const accepted = evaluateAssfCapabilityPreflightCandidateBinding(input());
    const rejectedResult = evaluateAssfCapabilityPreflightCandidateBinding(input({ metadata: metadata({ status: 'RETIRED', candidateState: 'RETIRED' }) }));
    const blocked = evaluateAssfCapabilityPreflightCandidateBinding(null);
    for (const result of [accepted, rejectedResult, blocked]) {
      expect(result.authorityStatus).toBe('CANDIDATE_ONLY');
      for (const field of AUTHORITY_FIELDS) expect(result[field]).toBe(false);
    }
  });

  it('produces a deeply frozen result whose nested arrays cannot be mutated', () => {
    const result = evaluateAssfCapabilityPreflightCandidateBinding(input());
    expect(Object.isFrozen(result.issues)).toBe(true);
    expect(Object.isFrozen(result.dependencies)).toBe(true);
    expect(Object.isFrozen(result.taskClasses)).toBe(true);
    expect(() => { (result as { packageId: string }).packageId = 'hacked'; }).toThrow();
    expect(() => { (result.dependencies as unknown as unknown[]).push('x'); }).toThrow();
  });

  it('does not mutate the caller-supplied metadata across repeated evaluation', () => {
    const evidence = input();
    const before = clone(evidence);
    evaluateAssfCapabilityPreflightCandidateBinding(evidence);
    evaluateAssfCapabilityPreflightCandidateBinding(evidence);
    expect(evidence).toEqual(before);
  });
});
