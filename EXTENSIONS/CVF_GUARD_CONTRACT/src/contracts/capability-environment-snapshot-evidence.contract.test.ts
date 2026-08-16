import { describe, expect, it } from 'vitest';
import {
  CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_CONTRACT_VERSION,
  CAPABILITY_ENVIRONMENT_SNAPSHOT_VERSION,
  evaluateCapabilityEnvironmentSnapshotEvidence,
  type CapabilityEnvironmentSnapshotEvidenceInput,
} from './capability-environment-snapshot-evidence.contract';
import {
  CAPABILITY_ROUTE_DECISION_VERSION,
  type CapabilityRouteDecision,
} from './capability-route-readiness.contract';

const NOW = '2026-08-17T10:00:00Z';

function route(overrides: Partial<CapabilityRouteDecision> = {}): CapabilityRouteDecision {
  return {
    schemaVersion: CAPABILITY_ROUTE_DECISION_VERSION,
    routeDecisionId: 'route:req-1',
    candidateSetId: 'cset-1',
    requestId: 'req-1',
    workspaceId: 'workspace-1',
    stage: 'FAST_ROUTE',
    primary: { capabilityId: 'git.read', packageId: 'cvf.git-read', packageVersion: '1.0.0' },
    supporting: [],
    rejected: [],
    fallbacks: [],
    confidence: 0.98,
    ambiguityReasons: [],
    environmentSnapshotRefs: ['snap-1'],
    authorityStatus: 'CANDIDATE_ONLY',
    executionAuthorized: false,
    generatedAt: '2026-08-17T09:00:00Z',
    issues: [],
    ...overrides,
  };
}

function input(): CapabilityEnvironmentSnapshotEvidenceInput {
  return {
    schemaVersion: CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_CONTRACT_VERSION,
    route: route(),
    snapshot: {
      schemaVersion: CAPABILITY_ENVIRONMENT_SNAPSHOT_VERSION,
      snapshotId: 'snap-1',
      workspaceId: 'workspace-1',
      observedAt: '2026-08-17T09:30:00Z',
      expiresAt: '2026-08-17T10:30:00Z',
      workspaceProfile: 'windows-local',
      platform: { os: 'win32', arch: 'x64', shell: 'powershell' },
      packages: [{ packageId: 'cvf.git-read', packageVersion: '1.0.0' }],
      dependencies: [],
      network: { mode: 'NORMAL', allowedDestinations: [] },
      sandbox: { status: 'AVAILABLE', profile: 'workspace-readonly' },
      credentialBindings: [],
      writableBoundaries: ['workspace-1'],
      verification: { status: 'PASS', reasons: [] },
    },
    readinessPolicy: {
      readinessDecisionId: 'ready-1',
      approvalRequired: false,
      existingApprovalValid: false,
      policyAllowed: true,
      provenanceVerified: true,
      integrityVerified: true,
      compatible: true,
      credentialsReady: true,
      networkReady: true,
      sandboxReady: true,
      evidenceRefs: ['evidence-1'],
    },
    now: NOW,
  };
}

function clone<T>(value: T): T {
  return structuredClone(value);
}

const AUTHORITY_FIELDS = [
  'snapshotCollected', 'snapshotPersisted', 'environmentReadAuthorized',
  'executionAuthorized', 'acquisitionAuthorized', 'mutationAuthorized',
  'refreshAuthorized', 'taskAuthorityGranted', 'networkAuthorized',
] as const;

describe('capability environment snapshot evidence', () => {
  it('returns frozen, deterministic, authority-free ready evidence without mutating input', () => {
    const evidence = input();
    const before = clone(evidence);
    const first = evaluateCapabilityEnvironmentSnapshotEvidence(evidence);
    const second = evaluateCapabilityEnvironmentSnapshotEvidence(evidence);

    expect(first).toEqual(second);
    expect(evidence).toEqual(before);
    expect(first.status).toBe('VALIDATED_READY_EVIDENCE');
    expect(first.readiness?.state).toBe('READY');
    expect(first.routeDecisionId).toBe(evidence.route.routeDecisionId);
    expect(first.snapshotId).toBe(evidence.snapshot.snapshotId);
    expect(Object.isFrozen(first)).toBe(true);
    expect(Object.isFrozen(first.issues)).toBe(true);
    expect(Object.isFrozen(first.requiredDependencies)).toBe(true);
    expect(Object.isFrozen(first.readiness)).toBe(true);
    for (const field of AUTHORITY_FIELDS) expect(first[field]).toBe(false);
  });

  it.each([
    ['null', null],
    ['array', []],
    ['class', new (class Envelope {})()],
  ])('rejects a malformed %s envelope without throwing', (_label, value) => {
    expect(() => evaluateCapabilityEnvironmentSnapshotEvidence(value)).not.toThrow();
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(value).status).toBe('REJECTED');
  });

  it('rejects proxies and accessors without invoking user hooks', () => {
    let invoked = 0;
    const proxied = new Proxy(input(), { get() { invoked += 1; throw new Error('must not run'); } });
    const accessor = input() as unknown as Record<string, unknown>;
    Object.defineProperty(accessor, 'now', { enumerable: true, get() { invoked += 1; throw new Error('must not run'); } });
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(proxied).status).toBe('REJECTED');
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(accessor).status).toBe('REJECTED');

    const coercion = input();
    (coercion.route as { supporting: string[] }).supporting = ['git'];
    (coercion.snapshot as { dependencies: unknown[] }).dependencies = [{
      dependencyId: 'git',
      kind: { toString() { invoked += 1; throw new Error('must not coerce'); } },
      availability: 'UNKNOWN', resolvedPath: null, endpoint: null,
      detectedVersion: null, sourceOrigin: null, artifactHash: null, license: null,
      verificationLevel: 'DECLARED', blockingReasons: ['not observed'],
    }];
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(coercion).status).toBe('REJECTED');
    expect(invoked).toBe(0);
  });

  it('rejects unknown keys, symbols, sparse arrays, Array subclasses, and oversized arrays', () => {
    const unknown = input() as unknown as Record<string, unknown>;
    unknown.extra = true;
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(unknown).issues.some((issue) => issue.code === 'UNKNOWN_KEY')).toBe(true);

    const symbol = input() as unknown as Record<PropertyKey, unknown>;
    symbol[Symbol('hidden')] = 'value';
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(symbol).status).toBe('REJECTED');

    const sparse = input();
    const reasons = new Array(2) as string[];
    reasons[1] = 'gap';
    (sparse.snapshot.verification as { status: 'WARN'; reasons: string[] }).status = 'WARN';
    (sparse.snapshot.verification as { status: 'WARN'; reasons: string[] }).reasons = reasons;
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(sparse).issues.some((issue) => issue.code === 'SPARSE_ARRAY')).toBe(true);

    const subclass = input();
    class Items<T> extends Array<T> {}
    (subclass.snapshot as { writableBoundaries: string[] }).writableBoundaries = new Items('workspace-1');
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(subclass).status).toBe('REJECTED');

    const oversized = input();
    (oversized.snapshot as { writableBoundaries: string[] }).writableBoundaries = Array.from({ length: 65 }, (_, index) => `w-${index}`);
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(oversized).issues.some((issue) => issue.code === 'UNBOUNDED_COLLECTION')).toBe(true);
  });

  it('rejects route authority, resolution, workspace, snapshot, and package binding drift', () => {
    const cases: CapabilityEnvironmentSnapshotEvidenceInput[] = [];
    const authority = input();
    (authority.route as unknown as { executionAuthorized: boolean }).executionAuthorized = true;
    cases.push(authority);
    const unresolved = input();
    (unresolved.route as { stage: CapabilityRouteDecision['stage'] }).stage = 'AMBIGUOUS_ROUTE';
    cases.push(unresolved);
    const workspace = input();
    (workspace.snapshot as { workspaceId: string }).workspaceId = 'workspace-2';
    cases.push(workspace);
    const ref = input();
    (ref.route as { environmentSnapshotRefs: string[] }).environmentSnapshotRefs = ['snap-other'];
    cases.push(ref);
    const pkg = input();
    (pkg.snapshot.packages[0] as { packageVersion: string }).packageVersion = '2.0.0';
    cases.push(pkg);
    const extraPkg = input();
    (extraPkg.snapshot as { packages: { packageId: string; packageVersion: string }[] }).packages = [
      ...extraPkg.snapshot.packages,
      { packageId: 'cvf.extra', packageVersion: '1.0.0' },
    ];
    cases.push(extraPkg);
    for (const value of cases) expect(evaluateCapabilityEnvironmentSnapshotEvidence(value).status).toBe('REJECTED');
  });

  it('binds dependencies exactly and treats only AVAILABLE as available', () => {
    const evidence = input();
    (evidence.route as { stage: CapabilityRouteDecision['stage']; supporting: string[] }).stage = 'FULL_RESOLUTION_REQUIRED';
    (evidence.route as { supporting: string[] }).supporting = ['git'];
    (evidence.snapshot as { dependencies: unknown[] }).dependencies = [{
      dependencyId: 'git', kind: 'CLI', availability: 'MISSING', resolvedPath: null,
      endpoint: null, detectedVersion: null, sourceOrigin: 'local', artifactHash: null,
      license: 'GPL-2.0', verificationLevel: 'DECLARED', blockingReasons: ['not installed'],
    }];
    const result = evaluateCapabilityEnvironmentSnapshotEvidence(evidence);
    expect(result.status).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ROUTE_REJECTED')).toBe(true);

    const missing = input();
    (missing.snapshot as { dependencies: unknown[] }).dependencies = [{
      dependencyId: 'extra', kind: 'CLI', availability: 'UNKNOWN', resolvedPath: null,
      endpoint: null, detectedVersion: null, sourceOrigin: null, artifactHash: null,
      license: null, verificationLevel: 'DECLARED', blockingReasons: ['not observed'],
    }];
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(missing).issues.some((issue) => issue.code === 'BINDING_MISMATCH')).toBe(true);
  });

  it('rejects duplicate dependencies and inconsistent availability fields', () => {
    const evidence = input();
    (evidence.route as { supporting: string[] }).supporting = ['git'];
    const row = {
      dependencyId: 'git', kind: 'CLI', availability: 'AVAILABLE', resolvedPath: null,
      endpoint: null, detectedVersion: null, sourceOrigin: 'local', artifactHash: null,
      license: null, verificationLevel: 'RESPONSIVE', blockingReasons: [],
    };
    (evidence.snapshot as { dependencies: unknown[] }).dependencies = [row, { ...row }];
    const result = evaluateCapabilityEnvironmentSnapshotEvidence(evidence);
    expect(result.issues.some((issue) => issue.code === 'DUPLICATE_IDENTIFIER')).toBe(true);
    expect(result.issues.some((issue) => issue.code === 'INVALID_FIELD')).toBe(true);
  });

  it('rejects uppercase/short artifact hashes', () => {
    for (const artifactHash of ['A'.repeat(64), 'abc']) {
      const evidence = input();
      (evidence.route as { supporting: string[] }).supporting = ['git'];
      (evidence.snapshot as { dependencies: unknown[] }).dependencies = [{
        dependencyId: 'git', kind: 'CLI', availability: 'AVAILABLE', resolvedPath: 'C:/git.exe',
        endpoint: null, detectedVersion: '2.51.0', sourceOrigin: 'local', artifactHash,
        license: 'GPL-2.0', verificationLevel: 'INTEGRITY_VERIFIED', blockingReasons: [],
      }];
      expect(evaluateCapabilityEnvironmentSnapshotEvidence(evidence).status).toBe('REJECTED');
    }
  });

  it('rejects high-confidence secrets without echoing them and accepts benign near misses', () => {
    const rawSecret = 'api_key=1234567890abcdef';
    const secret = input();
    (secret.snapshot.platform as { shell: string }).shell = rawSecret;
    const rejected = evaluateCapabilityEnvironmentSnapshotEvidence(secret);
    expect(rejected.status).toBe('REJECTED');
    expect(JSON.stringify(rejected)).not.toContain(rawSecret);
    expect(rejected.issues.some((issue) => issue.code === 'RAW_SECRET_DETECTED')).toBe(true);

    for (const benign of ['tokenizer', 'passwordless', 'secretary-review']) {
      const evidence = input();
      (evidence.snapshot.platform as { shell: string }).shell = benign;
      expect(evaluateCapabilityEnvironmentSnapshotEvidence(evidence).status).toBe('VALIDATED_READY_EVIDENCE');
    }
  });

  it.each([
    ['future observation', '2026-08-17T10:01:00Z', '2026-08-17T11:00:00Z'],
    ['expired', '2026-08-17T09:00:00Z', NOW],
    ['inverted', '2026-08-17T09:30:00Z', '2026-08-17T09:00:00Z'],
  ])('rejects %s time evidence', (_label, observedAt, expiresAt) => {
    const evidence = input();
    (evidence.snapshot as { observedAt: string }).observedAt = observedAt;
    (evidence.snapshot as { expiresAt: string }).expiresAt = expiresAt;
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(evidence).issues.some((issue) => issue.code === 'FRESHNESS_INVALID')).toBe(true);
  });

  it('rejects calendar-normalized timestamps that do not name a real UTC date', () => {
    const evidence = input();
    (evidence.snapshot as { observedAt: string }).observedAt = '2026-02-30T09:30:00Z';
    (evidence.snapshot as { expiresAt: string }).expiresAt = '2026-03-03T10:30:00Z';
    (evidence as { now: string }).now = '2026-03-02T10:00:00Z';
    const result = evaluateCapabilityEnvironmentSnapshotEvidence(evidence);
    expect(result.status).toBe('REJECTED');
    expect(result.issues).toContainEqual(expect.objectContaining({
      code: 'INVALID_FIELD',
      path: '$.snapshot.observedAt',
    }));
  });

  it('fails restricted or offline snapshot network evidence closed', () => {
    for (const mode of ['RESTRICTED', 'OFFLINE'] as const) {
      const evidence = input();
      (evidence.snapshot.network as { mode: 'RESTRICTED' | 'OFFLINE' }).mode = mode;
      const result = evaluateCapabilityEnvironmentSnapshotEvidence(evidence);
      expect(result.status).toBe('VALIDATED_BLOCKED_EVIDENCE');
      expect(result.readiness?.state).toBe('BLOCKED_NETWORK');
    }
  });

  it('rejects AVAILABLE endpoint dependencies that also claim a resolved path', () => {
    const evidence = input();
    (evidence.route as { supporting: string[] }).supporting = ['service-api'];
    (evidence.snapshot as { dependencies: unknown[] }).dependencies = [{
      dependencyId: 'service-api', kind: 'API', availability: 'AVAILABLE',
      resolvedPath: 'C:/unexpected-client.exe', endpoint: 'https://api.example.test',
      detectedVersion: '1.0.0', sourceOrigin: 'local', artifactHash: null,
      license: null, verificationLevel: 'RESPONSIVE', blockingReasons: [],
    }];
    const result = evaluateCapabilityEnvironmentSnapshotEvidence(evidence);
    expect(result.status).toBe('REJECTED');
    expect(result.issues).toContainEqual(expect.objectContaining({
      code: 'INVALID_FIELD',
      path: '$.snapshot.dependencies[0]',
    }));
  });

  it('requires explicit readiness booleans and maps snapshot verification, credential, and sandbox gaps to blocked evidence', () => {
    const absent = input() as unknown as { readinessPolicy: Record<string, unknown> };
    delete absent.readinessPolicy.networkReady;
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(absent).status).toBe('REJECTED');

    const verification = input();
    (verification.snapshot.verification as { status: string; reasons: string[] }).status = 'WARN';
    (verification.snapshot.verification as { status: string; reasons: string[] }).reasons = ['partial verification'];
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(verification).readiness?.state).toBe('BLOCKED_INTEGRITY');

    const credential = input();
    (credential.snapshot as { credentialBindings: unknown[] }).credentialBindings = [{ bindingRef: 'cred-1', status: 'MISSING' }];
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(credential).readiness?.state).toBe('BLOCKED_CREDENTIAL');

    const sandbox = input();
    (sandbox.snapshot.sandbox as { status: string; profile: string | null }).status = 'UNAVAILABLE';
    (sandbox.snapshot.sandbox as { status: string; profile: string | null }).profile = null;
    expect(evaluateCapabilityEnvironmentSnapshotEvidence(sandbox).readiness?.state).toBe('BLOCKED_SANDBOX');
  });

  it('preserves null/unknown policy evidence as fail-closed blocked evidence', () => {
    const evidence = input();
    (evidence.readinessPolicy as { networkReady: boolean | null }).networkReady = null;
    const result = evaluateCapabilityEnvironmentSnapshotEvidence(evidence);
    expect(result.status).toBe('VALIDATED_BLOCKED_EVIDENCE');
    expect(result.readiness?.state).toBe('UNKNOWN');
    for (const field of AUTHORITY_FIELDS) expect(result[field]).toBe(false);
  });

  it('orders rejection issues deterministically by path then code', () => {
    const evidence = input();
    (evidence.snapshot as { workspaceId: string }).workspaceId = 'bad workspace';
    (evidence.snapshot.platform as { shell: string }).shell = '\u0001';
    const issues = evaluateCapabilityEnvironmentSnapshotEvidence(evidence).issues;
    expect(issues).toEqual([...issues].sort((left, right) => left.path.localeCompare(right.path) || left.code.localeCompare(right.code) || left.message.localeCompare(right.message)));
  });
});
