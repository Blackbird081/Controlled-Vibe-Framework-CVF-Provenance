import { describe, expect, it } from 'vitest';
import {
  CAPABILITY_PREFLIGHT_PROFILE_POLICY_RESULT_VERSION,
  evaluateCapabilityPreflightProfilePolicy,
  type CapabilityPreflightProfile,
  type CapabilityPreflightProfilePolicyInput,
} from './capability-preflight-profile-policy.contract';
import {
  CAPABILITY_READINESS_DECISION_VERSION,
  CAPABILITY_ROUTE_DECISION_VERSION,
  type CapabilityReadinessDecision,
  type CapabilityRouteDecision,
} from './capability-route-readiness.contract';

const NOW = '2026-08-16T10:00:00Z';

function profile(overrides: Partial<CapabilityPreflightProfile> = {}): CapabilityPreflightProfile {
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
    notes: ['Windows is first-class for local deployment.'],
    ...overrides,
  };
}

function linuxProfile(): CapabilityPreflightProfile {
  return profile({
    profileId: 'linux-local',
    platforms: ['linux'],
    shellPreference: ['bash', 'sh', 'zsh'],
    pathDiscovery: ['command -v', 'which'],
  });
}

function macosProfile(): CapabilityPreflightProfile {
  return profile({
    profileId: 'macos-local',
    platforms: ['darwin'],
    shellPreference: ['zsh', 'bash'],
    pathDiscovery: ['command -v', 'which'],
  });
}

function offlineProfile(): CapabilityPreflightProfile {
  return profile({
    profileId: 'offline-local',
    platforms: ['win32', 'linux', 'darwin'],
    networkMode: 'OFFLINE',
    installPreference: ['existing-only', 'verified-local-artifact'],
    scanTtlSeconds: { R0: 1800, R1: 900, R2: 180, R3: 60 },
    pathDiscovery: [],
    notes: ['No acquisition step may require network access.'],
  });
}

function restrictedProfile(overrides: Partial<CapabilityPreflightProfile> = {}): CapabilityPreflightProfile {
  return profile({
    profileId: 'restricted-network',
    platforms: ['win32', 'linux', 'darwin'],
    networkMode: 'RESTRICTED',
    installPreference: ['existing-only', 'offline-artifact-with-approval'],
    scanTtlSeconds: { R0: 1800, R1: 900, R2: 180, R3: 60 },
    pathDiscovery: [],
    notes: ['Destinations must be assigned per work order.'],
    ...overrides,
  });
}

function input(overrides: Partial<CapabilityPreflightProfilePolicyInput> = {}): CapabilityPreflightProfilePolicyInput {
  return {
    catalog: [profile()],
    requestedProfileId: 'windows-local',
    observedPlatform: 'win32',
    riskLevel: 'R2',
    now: NOW,
    ...overrides,
  };
}

function routeEvidence(overrides: Partial<CapabilityRouteDecision> = {}): CapabilityRouteDecision {
  return {
    schemaVersion: CAPABILITY_ROUTE_DECISION_VERSION,
    routeDecisionId: 'route:t7-test',
    candidateSetId: 'cset-1',
    requestId: 'request-1',
    workspaceId: 'workspace-1',
    stage: 'FAST_ROUTE',
    primary: { capabilityId: 'cap-1', packageId: 'pkg-1', packageVersion: '1.0.0' },
    supporting: [],
    rejected: [],
    fallbacks: [],
    confidence: 0.9,
    ambiguityReasons: [],
    environmentSnapshotRefs: [],
    authorityStatus: 'CANDIDATE_ONLY',
    executionAuthorized: false,
    generatedAt: '2026-08-16T09:50:00Z',
    issues: [],
    ...overrides,
  };
}

function readinessEvidence(overrides: Partial<CapabilityReadinessDecision> = {}): CapabilityReadinessDecision {
  return {
    schemaVersion: CAPABILITY_READINESS_DECISION_VERSION,
    readinessDecisionId: 'ready-1',
    routeDecisionId: 'route:t7-test',
    snapshotId: 'snapshot-1',
    state: 'READY',
    missingDependencies: [],
    approvalRequirements: [],
    blockingReasons: [],
    evidenceRefs: [],
    nextSafeAction: 'Bind the selected capability to SPEC and WORK ORDER.',
    evaluatedAt: '2026-08-16T09:55:00Z',
    authorityStatus: 'EVIDENCE_ONLY',
    executionAuthorized: false,
    ...overrides,
  };
}

describe('capability preflight profile policy selection kernel', () => {
  it('selects windows-local with risk-scoped TTL and all authority literals false', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input());
    expect(result.disposition).toBe('SELECTED');
    expect(result.selectedProfileId).toBe('windows-local');
    expect(result.riskLevel).toBe('R2');
    expect(result.ttlSeconds).toBe(300);
    expect(result.networkMode).toBe('NORMAL');
    expect(result).toEqual(expect.objectContaining({
      executionAuthorized: false,
      acquisitionAuthorized: false,
      networkAuthorized: false,
      taskAuthorityGranted: false,
      mutationAuthorized: false,
    }));
    expect(result.issues).toEqual([]);
  });

  it.each([
    ['linux-local', 'linux', linuxProfile()],
    ['macos-local', 'darwin', macosProfile()],
  ])('selects %s for platform %s without ambient detection', (_id, platform, prof) => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [prof], requestedProfileId: prof.profileId, observedPlatform: platform, riskLevel: 'R1',
    }));
    expect(result.disposition).toBe('SELECTED');
    expect(result.selectedProfileId).toBe(prof.profileId);
    expect(result.ttlSeconds).toBe(1800);
    expect(result.executionAuthorized).toBe(false);
  });

  it('selects offline-local with zero destinations and constrained install preferences', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [offlineProfile()], requestedProfileId: 'offline-local', observedPlatform: 'linux', riskLevel: 'R0',
    }));
    expect(result.disposition).toBe('SELECTED');
    expect(result.networkMode).toBe('OFFLINE');
    expect(result.allowedDestinations).toEqual([]);
    expect(result.ttlSeconds).toBe(1800);
    expect(result.networkAuthorized).toBe(false);
    expect(result.acquisitionAuthorized).toBe(false);
  });

  it('keeps restricted-network destinations as constraints and never grants network authority', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [restrictedProfile({ allowedDestinations: ['publisher.example'] })],
      requestedProfileId: 'restricted-network', observedPlatform: 'darwin', riskLevel: 'R3',
    }));
    expect(result.disposition).toBe('SELECTED');
    expect(result.networkMode).toBe('RESTRICTED');
    expect(result.allowedDestinations).toEqual(['publisher.example']);
    expect(result.networkAuthorized).toBe(false);
    expect(result.executionAuthorized).toBe(false);
  });

  it('maps each risk level to the selected profile TTL deterministically', () => {
    for (const [risk, ttl] of [['R0', 3600], ['R1', 1800], ['R2', 300], ['R3', 60]] as const) {
      const result = evaluateCapabilityPreflightProfilePolicy(input({ riskLevel: risk }));
      expect(result.ttlSeconds).toBe(ttl);
      expect(result.riskLevel).toBe(risk);
    }
  });

  it('rejects non-object, null, proxy, and accessor inputs without throwing', () => {
    const proxy = new Proxy(input(), {});
    const accessor: Record<string, unknown> = { catalog: [profile()] };
    Object.defineProperty(accessor, 'requestedProfileId', { get: () => 'windows-local', enumerable: true });
    for (const bad of [null, 42, 'nope', [], proxy, accessor]) {
      const result = evaluateCapabilityPreflightProfilePolicy(bad);
      expect(result.disposition).toBe('REJECTED');
      expect(result.executionAuthorized).toBe(false);
      expect(result.issues.length).toBeGreaterThan(0);
    }
  });

  it('rejects proxy and accessor arrays without invoking their traps or getters', () => {
    let proxyReads = 0;
    const proxyCatalog = new Proxy([profile()], {
      get(target, property, receiver) {
        proxyReads += 1;
        return Reflect.get(target, property, receiver);
      },
    });
    const proxyResult = evaluateCapabilityPreflightProfilePolicy(input({ catalog: proxyCatalog }));
    expect(proxyResult.disposition).toBe('REJECTED');
    expect(proxyReads).toBe(0);

    let accessorReads = 0;
    const accessorCatalog: CapabilityPreflightProfile[] = [];
    Object.defineProperty(accessorCatalog, '0', {
      enumerable: true,
      get: () => {
        accessorReads += 1;
        return profile();
      },
    });
    accessorCatalog.length = 1;
    const accessorResult = evaluateCapabilityPreflightProfilePolicy(input({ catalog: accessorCatalog }));
    expect(accessorResult.disposition).toBe('REJECTED');
    expect(accessorReads).toBe(0);

    let nestedProxyReads = 0;
    const destinations = new Proxy(['publisher.example'], {
      get(target, property, receiver) {
        nestedProxyReads += 1;
        return Reflect.get(target, property, receiver);
      },
    });
    const hostileOffline = offlineProfile() as unknown as Record<string, unknown>;
    hostileOffline.allowedDestinations = destinations;
    const hostileResult = evaluateCapabilityPreflightProfilePolicy(input({ catalog: [hostileOffline as never], requestedProfileId: 'offline-local', observedPlatform: 'linux' }));
    expect(hostileResult.disposition).toBe('REJECTED');
    expect(nestedProxyReads).toBe(0);
  });

  it('rejects unknown keys in the input, profile, and TTL map', () => {
    const withInputKey = input() as unknown as Record<string, unknown>;
    withInputKey.extra = 'x';
    expect(evaluateCapabilityPreflightProfilePolicy(withInputKey).issues.map((i) => i.code)).toContain('UNKNOWN_KEYS');

    const withProfileKey = input() as unknown as CapabilityPreflightProfilePolicyInput;
    (withProfileKey.catalog as unknown as Record<string, unknown>[])[0] = { ...profile(), extra: 'x' } as unknown as Record<string, unknown>;
    expect(evaluateCapabilityPreflightProfilePolicy(withProfileKey).issues.map((i) => i.code)).toContain('UNKNOWN_KEYS');

    const withTtlKey = input() as unknown as CapabilityPreflightProfilePolicyInput;
    (withTtlKey.catalog as unknown as Record<string, unknown>[])[0] = {
      ...profile(), scanTtlSeconds: { R0: 1, R1: 1, R2: 1, R3: 1, R4: 1 },
    } as unknown as Record<string, unknown>;
    expect(evaluateCapabilityPreflightProfilePolicy(withTtlKey).issues.map((i) => i.code)).toContain('UNKNOWN_KEYS');
  });

  it('rejects duplicate profile IDs', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({ catalog: [profile(), profile()] }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.map((i) => i.code)).toContain('DUPLICATE_PROFILE_ID');
  });

  it('rejects an unknown requested profile', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({ requestedProfileId: 'nope' }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.map((i) => i.code)).toContain('UNKNOWN_PROFILE');
  });

  it('rejects a platform that is not a member of the selected profile', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({ observedPlatform: 'linux' }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.map((i) => i.code)).toContain('PLATFORM_MISMATCH');
  });

  it('rejects zero, negative, non-integer, and oversized TTLs', () => {
    for (const ttls of [
      { R0: 0, R1: 0, R2: 0, R3: 0 },
      { R0: -1, R1: -1, R2: -1, R3: -1 },
      { R0: 1.5, R1: 1, R2: 1, R3: 1 },
      { R0: 90000, R1: 1, R2: 1, R3: 1 },
    ]) {
      const result = evaluateCapabilityPreflightProfilePolicy(input({ catalog: [profile({ scanTtlSeconds: ttls as never })] }));
      expect(result.disposition).toBe('REJECTED');
      const codes = result.issues.map((i) => i.code);
      expect(codes.some((c) => c === 'INVALID_TTL' || c === 'TTL_EXCEEDS_BOUND')).toBe(true);
    }
  });

  it('rejects TTL ordering that increases with risk', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [profile({ scanTtlSeconds: { R0: 60, R1: 120, R2: 300, R3: 3600 } })],
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.map((i) => i.code)).toContain('TTL_ORDERING_VIOLATION');
  });

  it('rejects OFFLINE profiles with destinations or non-local install preferences', () => {
    const withDest = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [offlineProfile()], requestedProfileId: 'offline-local', observedPlatform: 'win32', riskLevel: 'R0',
    }));
    expect(withDest.disposition).toBe('SELECTED');

    const badOffline = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [profile({
        profileId: 'offline-bad', platforms: ['win32', 'linux', 'darwin'], networkMode: 'OFFLINE',
        installPreference: ['workspace-local'], scanTtlSeconds: { R0: 1, R1: 1, R2: 1, R3: 1 },
        allowedDestinations: ['publisher.example'],
      })],
      requestedProfileId: 'offline-bad', observedPlatform: 'win32', riskLevel: 'R0',
    }));
    expect(badOffline.disposition).toBe('REJECTED');
    const codes = badOffline.issues.map((i) => i.code);
    expect(codes).toContain('OFFLINE_DESTINATIONS_FORBIDDEN');
    expect(codes).toContain('OFFLINE_INSTALL_PREFERENCE_FORBIDDEN');
  });

  it('rejects a privilege policy other than EXPLICIT_APPROVAL', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [profile({ privilegePolicy: 'AUTO_APPROVE' as never })],
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.map((i) => i.code)).toContain('PRIVILEGE_POLICY_VIOLATION');
  });

  it('rejects secret-like values and control characters', () => {
    const secretNote = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [profile({ notes: ['api_key=deadbeef'] })],
    }));
    expect(secretNote.issues.map((i) => i.code)).toContain('SECRET_LIKE_CONTENT');

    const control = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [profile({ notes: ['bad\u0000note'] })],
    }));
    expect(control.issues.map((i) => i.code)).toContain('CONTROL_CHARACTER');
  });

  it('rejects unsafe path-discovery fragments and non-lowercase digests', () => {
    const unsafe = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [profile({ pathDiscovery: ['../../etc/passwd'] })],
    }));
    expect(unsafe.issues.map((i) => i.code)).toContain('UNSAFE_PATH_FRAGMENT');

    const digest = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [profile({ notes: ['A'.repeat(64)] })],
    }));
    expect(digest.issues.map((i) => i.code)).toContain('NON_LOWERCASE_DIGEST');
  });

  it('rejects sparse catalogs and oversized input', () => {
    const sparse: unknown[] = [];
    sparse[1] = profile();
    const sparseResult = evaluateCapabilityPreflightProfilePolicy(input({ catalog: sparse as never }));
    expect(sparseResult.disposition).toBe('REJECTED');

    const oversized = evaluateCapabilityPreflightProfilePolicy(input({
      catalog: [profile({ notes: ['x'.repeat(400)] })],
    }));
    expect(oversized.disposition).toBe('REJECTED');
  });

  it('accepts valid current T4 evidence and rejects stale, malformed, or authority-strong evidence', () => {
    const valid = evaluateCapabilityPreflightProfilePolicy(input({
      routeEvidence: routeEvidence(), readinessEvidence: readinessEvidence(),
    }));
    expect(valid.disposition).toBe('SELECTED');

    const stale = evaluateCapabilityPreflightProfilePolicy(input({
      routeEvidence: routeEvidence({ generatedAt: '2026-08-15T00:00:00Z' }),
    }));
    expect(stale.disposition).toBe('REJECTED');
    expect(stale.issues.map((i) => i.code)).toContain('STALE_T4_EVIDENCE');

    const malformed = evaluateCapabilityPreflightProfilePolicy(input({
      routeEvidence: routeEvidence({ schemaVersion: 'bad' as never }),
    }));
    expect(malformed.issues.map((i) => i.code)).toContain('MALFORMED_T4_EVIDENCE');

    const authority = evaluateCapabilityPreflightProfilePolicy(input({
      routeEvidence: routeEvidence({ executionAuthorized: true as never, authorityStatus: 'CANDIDATE_ONLY' as never }),
    }));
    expect(authority.issues.map((i) => i.code)).toContain('T4_AUTHORITY_VIOLATION');
  });

  it('rejects malformed T4 issue arrays, route stages, and readiness states', () => {
    const malformedIssues = evaluateCapabilityPreflightProfilePolicy(input({
      routeEvidence: routeEvidence({ issues: 'not-an-array' as never }),
    }));
    expect(malformedIssues.disposition).toBe('REJECTED');
    expect(malformedIssues.issues.map((item) => item.code)).toContain('MALFORMED_T4_EVIDENCE');

    const ambiguousRoute = evaluateCapabilityPreflightProfilePolicy(input({
      routeEvidence: routeEvidence({ stage: 'AMBIGUOUS_ROUTE', issues: [] }),
    }));
    expect(ambiguousRoute.disposition).toBe('REJECTED');

    const invalidReadiness = evaluateCapabilityPreflightProfilePolicy(input({
      readinessEvidence: readinessEvidence({ state: 'UNRECOGNIZED' as never }),
    }));
    expect(invalidReadiness.disposition).toBe('REJECTED');
    expect(invalidReadiness.issues.map((item) => item.code)).toContain('MALFORMED_T4_EVIDENCE');
  });

  it('rejects normalized but impossible UTC calendar dates', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({ now: '2026-02-30T10:00:00Z' }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.map((item) => item.path)).toContain('$.now');
  });

  it('rejects unbound readiness evidence', () => {
    const result = evaluateCapabilityPreflightProfilePolicy(input({
      routeEvidence: routeEvidence(),
      readinessEvidence: readinessEvidence({ routeDecisionId: 'route:other' }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.map((i) => i.code)).toContain('T4_BINDING_VIOLATION');
  });

  it('is deterministic and does not mutate its input', () => {
    const value = input({ catalog: [profile(), linuxProfile()], requestedProfileId: 'linux-local', observedPlatform: 'linux' });
    const before = JSON.stringify(value);
    const first = evaluateCapabilityPreflightProfilePolicy(value);
    const second = evaluateCapabilityPreflightProfilePolicy(value);
    expect(first).toEqual(second);
    expect(JSON.stringify(value)).toBe(before);
    expect(first.selectedProfileId).toBe('linux-local');
  });

  it('always emits literal false authority on every return path', () => {
    const selected = evaluateCapabilityPreflightProfilePolicy(input());
    const rejected = evaluateCapabilityPreflightProfilePolicy(input({ observedPlatform: 'linux' }));
    for (const result of [selected, rejected]) {
      expect(result.executionAuthorized).toBe(false);
      expect(result.acquisitionAuthorized).toBe(false);
      expect(result.networkAuthorized).toBe(false);
      expect(result.taskAuthorityGranted).toBe(false);
      expect(result.mutationAuthorized).toBe(false);
    }
  });

  it('exposes the stable result schema version', () => {
    expect(evaluateCapabilityPreflightProfilePolicy(input()).schemaVersion).toBe(CAPABILITY_PREFLIGHT_PROFILE_POLICY_RESULT_VERSION);
  });
});
