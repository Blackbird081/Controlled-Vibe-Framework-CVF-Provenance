import { describe, expect, it } from 'vitest';
import {
  CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION,
  CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_RESULT_VERSION,
  evaluateCapabilityWorkspaceBootstrapPolicyBundle,
  type CapabilityWorkspaceBootstrapPolicy,
  type CapabilityWorkspaceBootstrapPolicyBundleInput,
  type CapabilityWorkspaceBootstrapPolicyBundleResult,
  type CapabilityWorkspaceBootstrapProfile,
} from './capability-workspace-bootstrap-policy-bundle.contract';

const NOW = '2026-08-17T10:00:00Z';
const WORKSPACE_ROOT = '${WORKSPACE_ROOT}';

function offlineProfile(overrides: Partial<CapabilityWorkspaceBootstrapProfile> = {}): CapabilityWorkspaceBootstrapProfile {
  return {
    profileId: 'offline-local',
    platforms: ['win32', 'linux', 'darwin'],
    shellPreference: ['sh'],
    networkMode: 'OFFLINE',
    installPreference: ['existing-only', 'verified-local-artifact'],
    scanTtlSeconds: { R0: 1800, R1: 900, R2: 180, R3: 60 },
    privilegePolicy: 'EXPLICIT_APPROVAL',
    pathDiscovery: [],
    allowedDestinations: [],
    notes: ['No network acquisition permitted.'],
    writableBoundaries: [WORKSPACE_ROOT],
    credentialBindings: [],
    ...overrides,
  };
}

function restrictedProfile(overrides: Partial<CapabilityWorkspaceBootstrapProfile> = {}): CapabilityWorkspaceBootstrapProfile {
  return {
    profileId: 'restricted-network',
    platforms: ['win32', 'linux', 'darwin'],
    shellPreference: ['sh'],
    networkMode: 'RESTRICTED',
    installPreference: ['existing-only', 'offline-artifact-with-approval'],
    scanTtlSeconds: { R0: 1800, R1: 900, R2: 180, R3: 60 },
    privilegePolicy: 'EXPLICIT_APPROVAL',
    pathDiscovery: [],
    allowedDestinations: [],
    notes: ['Network destinations must be explicitly inserted by a governed workspace materializer.'],
    writableBoundaries: [WORKSPACE_ROOT],
    credentialBindings: [],
    ...overrides,
  };
}

function windowsProfile(overrides: Partial<CapabilityWorkspaceBootstrapProfile> = {}): CapabilityWorkspaceBootstrapProfile {
  return {
    profileId: 'windows-local',
    platforms: ['win32'],
    shellPreference: ['powershell', 'pwsh', 'cmd'],
    networkMode: 'NORMAL',
    installPreference: ['workspace-local', 'user-local', 'system-with-approval'],
    scanTtlSeconds: { R0: 3600, R1: 1800, R2: 300, R3: 60 },
    privilegePolicy: 'EXPLICIT_APPROVAL',
    pathDiscovery: ['where.exe', 'Get-Command'],
    allowedDestinations: [],
    notes: ['Template only; ${WORKSPACE_ROOT} must be resolved by the governed initializer.'],
    writableBoundaries: [WORKSPACE_ROOT],
    credentialBindings: [],
    ...overrides,
  };
}

function offlinePolicy(overrides: Partial<CapabilityWorkspaceBootstrapPolicy> = {}): CapabilityWorkspaceBootstrapPolicy {
  return {
    policyId: 'capability-bootstrap.offline-local',
    defaultDecision: 'BLOCK',
    networkDefault: 'DENY',
    allowNetwork: false,
    allowVerifiedLocalArtifact: true,
    requireIntegrity: true,
    maxRepairRoundsWithoutNewEvidence: 3,
    ...overrides,
  };
}

function restrictedPolicy(overrides: Partial<CapabilityWorkspaceBootstrapPolicy> = {}): CapabilityWorkspaceBootstrapPolicy {
  return {
    policyId: 'capability-bootstrap.restricted-network',
    defaultDecision: 'BLOCK',
    networkDefault: 'DENY',
    requireDestinationAllowlist: true,
    allowOfflineArtifacts: true,
    requireIntegrity: true,
    maxRepairRoundsWithoutNewEvidence: 3,
    ...overrides,
  };
}

function windowsPolicy(overrides: Partial<CapabilityWorkspaceBootstrapPolicy> = {}): CapabilityWorkspaceBootstrapPolicy {
  return {
    policyId: 'capability-bootstrap.windows-local',
    defaultDecision: 'BLOCK',
    allowWorkspaceLocal: true,
    allowUserLocalWithApproval: true,
    allowSystemInstallWithApproval: true,
    requireIntegrity: true,
    requirePublisher: true,
    requireLicense: true,
    maxRepairRoundsWithoutNewEvidence: 3,
    forbiddenMutations: [
      'unapproved system PATH',
      'unapproved registry',
      'unapproved services',
      'raw credential storage',
    ],
    ...overrides,
  };
}

function makeBundle(
  profile: CapabilityWorkspaceBootstrapProfile,
  policy: CapabilityWorkspaceBootstrapPolicy,
  overrides: Partial<CapabilityWorkspaceBootstrapPolicyBundleInput> = {},
): CapabilityWorkspaceBootstrapPolicyBundleInput {
  return {
    schemaVersion: CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION,
    profile,
    bootstrapPolicy: policy,
    requestedProfileId: profile.profileId,
    observedPlatform: 'win32',
    riskLevel: 'R2',
    now: NOW,
    ...overrides,
  };
}

function bundle(overrides: Partial<CapabilityWorkspaceBootstrapPolicyBundleInput> = {}): CapabilityWorkspaceBootstrapPolicyBundleInput {
  return makeBundle(windowsProfile(), windowsPolicy(), overrides);
}

function codes(result: CapabilityWorkspaceBootstrapPolicyBundleResult): string[] {
  return result.issues.map((issue) => issue.code);
}

function clone<T>(value: T): T {
  return structuredClone(value);
}

const AUTHORITY_FIELDS = [
  'profileMaterialized', 'policyPersisted', 'workspaceInitialized',
  'environmentReadAuthorized', 'installationAuthorized', 'executionAuthorized',
  'acquisitionAuthorized', 'mutationAuthorized', 'networkAuthorized',
  'taskAuthorityGranted',
] as const;

const PAIRS = [
  ['offline-local', offlineProfile(), offlinePolicy(), 'win32', 'R0', 1800],
  ['restricted-network', restrictedProfile(), restrictedPolicy(), 'win32', 'R2', 180],
  ['windows-local', windowsProfile(), windowsPolicy(), 'win32', 'R2', 300],
] as const;

describe('capability workspace bootstrap policy bundle', () => {
  it.each(PAIRS)(
    'accepts the adapted %s pair for matching platform/risk/time from in-memory fixtures only',
    (_label, prof, pol, platform, risk, ttl) => {
      const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
        makeBundle(prof as CapabilityWorkspaceBootstrapProfile, pol as CapabilityWorkspaceBootstrapPolicy, {
          observedPlatform: platform as string,
          riskLevel: risk as CapabilityWorkspaceBootstrapPolicyBundleInput['riskLevel'],
        }),
      );
      expect(result.status).toBe('VALIDATED_POLICY_EVIDENCE');
      expect(result.ttlSeconds).toBe(ttl);
      expect(result.selectionEvidence?.disposition).toBe('SELECTED');
      expect(result.issues).toEqual([]);
    },
  );

  it('embeds a successful T7 selection and exact profile/policy bindings in every accepted result', () => {
    for (const [prof, pol] of [[offlineProfile(), offlinePolicy()], [restrictedProfile(), restrictedPolicy()], [windowsProfile(), windowsPolicy()]] as const) {
      const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(makeBundle(prof, pol));
      expect(result.status).toBe('VALIDATED_POLICY_EVIDENCE');
      expect(result.selectionEvidence?.disposition).toBe('SELECTED');
      expect(result.selectedProfileId).toBe(prof.profileId);
      expect(result.policyId).toBe(`capability-bootstrap.${prof.profileId}`);
      expect(result.networkMode).toBe(prof.networkMode);
      expect(result.ttlSeconds).toBe(prof.scanTtlSeconds.R2);
      expect(result.installPreference).toEqual(prof.installPreference);
      expect(result.writableBoundaries).toEqual(prof.writableBoundaries);
      expect(result.credentialBindings).toEqual(prof.credentialBindings);
      expect(result.maxRepairRoundsWithoutNewEvidence).toBe(3);
    }
  });

  it('rejects a policy id that does not bind to the selected profile', () => {
    const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ bootstrapPolicy: windowsPolicy({ policyId: 'capability-bootstrap.other' }) }),
    );
    expect(result.status).toBe('REJECTED');
    expect(codes(result)).toContain('POLICY_ID_MISMATCH');
  });

  it('rejects unsupported variant keys on the bootstrap policy', () => {
    const offlineWithNormal = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      makeBundle(offlineProfile(), { ...offlinePolicy(), allowWorkspaceLocal: true } as unknown as CapabilityWorkspaceBootstrapPolicy),
    );
    expect(codes(offlineWithNormal)).toContain('UNKNOWN_KEY');

    const normalWithNetwork = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      makeBundle(windowsProfile(), { ...windowsPolicy(), networkDefault: 'DENY' } as unknown as CapabilityWorkspaceBootstrapPolicy),
    );
    expect(codes(normalWithNetwork)).toContain('UNKNOWN_KEY');
  });

  it('rejects a weakened default decision', () => {
    const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ bootstrapPolicy: { ...windowsPolicy(), defaultDecision: 'ALLOW' } as unknown as CapabilityWorkspaceBootstrapPolicy }),
    );
    expect(codes(result)).toContain('POLICY_BLOCK_DEFAULT_WEAKENED');
  });

  it('rejects integrity weakening', () => {
    const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ bootstrapPolicy: windowsPolicy({ requireIntegrity: false }) }),
    );
    expect(codes(result)).toContain('POLICY_INTEGRITY_WEAKENED');
  });

  it('rejects approval, publisher, and license weakening on the NORMAL policy', () => {
    for (const over of [
      { allowWorkspaceLocal: false },
      { allowUserLocalWithApproval: false },
      { allowSystemInstallWithApproval: false },
      { requirePublisher: false },
      { requireLicense: false },
    ]) {
      const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
        bundle({ bootstrapPolicy: windowsPolicy(over) }),
      );
      expect(result.status).toBe('REJECTED');
      expect(codes(result)).toContain('POLICY_VARIANT_WEAKENED');
    }
  });

  it('rejects invalid repair bounds', () => {
    for (const value of [0, 4, 1.5, '3']) {
      const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
        bundle({ bootstrapPolicy: windowsPolicy({ maxRepairRoundsWithoutNewEvidence: value as never }) }),
      );
      expect(codes(result)).toContain('POLICY_REPAIR_BOUNDS_INVALID');
    }
  });

  it('rejects OFFLINE network weakening and destination-bearing profiles', () => {
    const weakOffline = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      makeBundle(offlineProfile(), offlinePolicy({ allowNetwork: true })),
    );
    expect(codes(weakOffline)).toContain('POLICY_VARIANT_WEAKENED');

    const offlineWithDest = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      makeBundle(offlineProfile({ allowedDestinations: ['publisher.example'] }), offlinePolicy()),
    );
    expect(offlineWithDest.status).toBe('REJECTED');
    expect(codes(offlineWithDest)).toContain('T7_SELECTION_REJECTED');
  });

  it('rejects RESTRICTED network weakening', () => {
    for (const over of [
      { requireDestinationAllowlist: false },
      { allowOfflineArtifacts: false },
      { networkDefault: 'ALLOW' },
    ]) {
      const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
        makeBundle(restrictedProfile(), restrictedPolicy(over as Partial<CapabilityWorkspaceBootstrapPolicy>)),
      );
      expect(codes(result)).toContain('POLICY_VARIANT_WEAKENED');
    }
  });

  it('rejects a forbiddenMutations list missing a mandated protection or carrying duplicates', () => {
    const missing = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ bootstrapPolicy: windowsPolicy({ forbiddenMutations: ['unapproved registry', 'unapproved services', 'raw credential storage'] }) }),
    );
    expect(codes(missing)).toContain('POLICY_VARIANT_WEAKENED');

    const duplicateList = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ bootstrapPolicy: windowsPolicy({ forbiddenMutations: ['unapproved system PATH', 'unapproved system PATH', 'unapproved registry', 'unapproved services', 'raw credential storage'] }) }),
    );
    expect(codes(duplicateList)).toContain('DUPLICATE_VALUE');
  });

  it('rejects a NORMAL local-install policy on a non-win32 profile', () => {
    const nonWin = windowsProfile({ platforms: ['linux'] });
    const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      makeBundle(nonWin, windowsPolicy(), { observedPlatform: 'linux' }),
    );
    expect(result.status).toBe('REJECTED');
    expect(codes(result)).toContain('BINDING_MISMATCH');
  });

  it('keeps T7 platform, TTL, offline-install, path-discovery, and secret-safety failures rejected through composition', () => {
    const platform = evaluateCapabilityWorkspaceBootstrapPolicyBundle(bundle({ observedPlatform: 'linux' }));
    expect(platform.status).toBe('REJECTED');
    expect(codes(platform)).toContain('T7_SELECTION_REJECTED');

    const ttl = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ scanTtlSeconds: { R0: 0, R1: 0, R2: 0, R3: 0 } }) }),
    );
    expect(ttl.status).toBe('REJECTED');
    expect(codes(ttl)).toContain('T7_SELECTION_REJECTED');

    const offlineInstall = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      makeBundle(offlineProfile({ installPreference: ['workspace-local'] }), offlinePolicy()),
    );
    expect(offlineInstall.status).toBe('REJECTED');
    expect(codes(offlineInstall)).toContain('T7_SELECTION_REJECTED');

    const path = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ pathDiscovery: ['../../etc/passwd'] }) }),
    );
    expect(path.status).toBe('REJECTED');
    expect(codes(path)).toContain('T7_SELECTION_REJECTED');

    const secret = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ notes: ['api_key=deadbeef'] }) }),
    );
    expect(secret.status).toBe('REJECTED');
    expect(codes(secret)).toContain('T7_SELECTION_REJECTED');
  });

  it('rejects Proxy and accessor envelopes without invoking traps or getters', () => {
    let reads = 0;
    const proxied = new Proxy(bundle(), {
      get() {
        reads += 1;
        throw new Error('must not run');
      },
    });
    expect(evaluateCapabilityWorkspaceBootstrapPolicyBundle(proxied).status).toBe('REJECTED');
    expect(reads).toBe(0);

    const accessor = bundle() as unknown as Record<string, unknown>;
    Object.defineProperty(accessor, 'now', {
      enumerable: true,
      get() {
        reads += 1;
        throw new Error('must not run');
      },
    });
    expect(evaluateCapabilityWorkspaceBootstrapPolicyBundle(accessor).status).toBe('REJECTED');
    expect(reads).toBe(0);
  });

  it('rejects symbol keys and prototype-polluted inputs', () => {
    const withSymbol = { ...bundle(), [Symbol('x')]: 1 };
    expect(evaluateCapabilityWorkspaceBootstrapPolicyBundle(withSymbol).status).toBe('REJECTED');

    const polluted = Object.assign(Object.create({ polluted: true }), bundle());
    expect(evaluateCapabilityWorkspaceBootstrapPolicyBundle(polluted).status).toBe('REJECTED');
  });

  it('rejects sparse arrays and Array subclasses', () => {
    const sparse: unknown[] = [];
    sparse[1] = WORKSPACE_ROOT;
    const sparseResult = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ writableBoundaries: sparse as never }) }),
    );
    expect(sparseResult.status).toBe('REJECTED');
    expect(codes(sparseResult)).toContain('SPARSE_ARRAY');

    class SubArray extends Array<string> {
      extra = true;
    }
    const sub = new SubArray(WORKSPACE_ROOT);
    const subResult = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ writableBoundaries: sub as never }) }),
    );
    expect(subResult.status).toBe('REJECTED');
  });

  it('rejects an oversized sparse array before scanning its declared length', () => {
    const oversizedSparse: unknown[] = [];
    oversizedSparse.length = 0xffff_ffff;
    const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ writableBoundaries: oversizedSparse as never }) }),
    );
    expect(result.status).toBe('REJECTED');
    expect(codes(result)).toContain('UNBOUNDED_COLLECTION');
  });

  it('rejects unknown keys, oversized data, duplicate values, and control characters', () => {
    const unknown = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: { ...windowsProfile(), extra: 'x' } as unknown as CapabilityWorkspaceBootstrapProfile }),
    );
    expect(codes(unknown)).toContain('UNKNOWN_KEY');

    const oversized = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ writableBoundaries: ['x'.repeat(600)] }) }),
    );
    expect(oversized.status).toBe('REJECTED');

    const duplicateValues = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ credentialBindings: ['cred:a', 'cred:a'] }) }),
    );
    expect(codes(duplicateValues)).toContain('DUPLICATE_VALUE');

    const control = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ notes: ['bad\u0000note'] }) }),
    );
    expect(control.status).toBe('REJECTED');
  });

  it('rejects unsafe writable boundaries', () => {
    for (const bad of ['../../etc', '/abs/path', 'C:\\windows', '; rm -rf', '${HOME}', '$(...)', 'publisher.example']) {
      const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
        bundle({ profile: windowsProfile({ writableBoundaries: [bad] }) }),
      );
      expect(result.status).toBe('REJECTED');
      expect(codes(result)).toContain('INVALID_FIELD');
    }
  });

  it('rejects raw credential-like text without echoing the secret', () => {
    const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: windowsProfile({ credentialBindings: ['password=supersecret'] }) }),
    );
    expect(result.status).toBe('REJECTED');
    expect(codes(result)).toContain('RAW_SECRET_DETECTED');
    expect(JSON.stringify(result)).not.toContain('supersecret');
  });

  it('rejects thrown getters without executing them', () => {
    let invoked = 0;
    const profile = windowsProfile() as unknown as Record<string, unknown>;
    Object.defineProperty(profile, 'writableBoundaries', {
      enumerable: true,
      get() {
        invoked += 1;
        throw new Error('must not run');
      },
    });
    const result = evaluateCapabilityWorkspaceBootstrapPolicyBundle(
      bundle({ profile: profile as unknown as CapabilityWorkspaceBootstrapProfile }),
    );
    expect(result.status).toBe('REJECTED');
    expect(invoked).toBe(0);
  });

  it('does not mutate input and returns frozen deterministic results', () => {
    const value = bundle();
    const before = clone(value);
    const first = evaluateCapabilityWorkspaceBootstrapPolicyBundle(value);
    const second = evaluateCapabilityWorkspaceBootstrapPolicyBundle(value);

    expect(first).toEqual(second);
    expect(value).toEqual(before);
    expect(Object.isFrozen(first)).toBe(true);
    expect(Object.isFrozen(first.installPreference)).toBe(true);
    expect(Object.isFrozen(first.writableBoundaries)).toBe(true);
    expect(Object.isFrozen(first.credentialBindings)).toBe(true);
    expect(Object.isFrozen(first.issues)).toBe(true);
    expect(Object.isFrozen(first.selectionEvidence)).toBe(true);
  });

  it('keeps all ten authority fields literal false on every branch', () => {
    const accepted = evaluateCapabilityWorkspaceBootstrapPolicyBundle(bundle());
    const rejected = evaluateCapabilityWorkspaceBootstrapPolicyBundle(bundle({ observedPlatform: 'linux' }));
    const malformed = evaluateCapabilityWorkspaceBootstrapPolicyBundle(null);
    for (const result of [accepted, rejected, malformed]) {
      expect(result.authorityStatus).toBe('EVIDENCE_ONLY');
      for (const field of AUTHORITY_FIELDS) expect(result[field]).toBe(false);
    }
  });

  it('exposes the stable input and result schema versions', () => {
    expect(CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION).toBe('cvf.capabilityWorkspaceBootstrapPolicyBundle.v1');
    expect(CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_RESULT_VERSION).toBe('cvf.capabilityWorkspaceBootstrapPolicyBundleResult.v1');
    expect(evaluateCapabilityWorkspaceBootstrapPolicyBundle(bundle()).schemaVersion).toBe(CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_RESULT_VERSION);
  });
});
