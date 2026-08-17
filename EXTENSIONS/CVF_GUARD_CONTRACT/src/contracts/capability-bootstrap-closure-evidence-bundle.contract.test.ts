import { describe, expect, it } from 'vitest';
import {
  CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_CONTRACT_VERSION,
  evaluateCapabilityBootstrapClosureEvidenceBundle,
  type CapabilityBootstrapClosureEvidenceBundleInput,
  type CapabilityBootstrapClosureEvidenceBundleResult,
} from './capability-bootstrap-closure-evidence-bundle.contract';
import {
  CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION,
  type CapabilityAcquisitionReceipt,
  type CapabilityAcquisitionReceiptVerificationInput,
} from './capability-acquisition-receipt-verification.contract';
import {
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION,
  type CapabilityBootstrapApprovalEvidence,
} from './capability-bootstrap-approval-evidence.contract';
import {
  CONTROLLED_ACQUISITION_PLAN_VERSION,
  computeControlledAcquisitionPlanDigest,
  type ControlledAcquisitionPlan,
} from './controlled-acquisition.contract';
import {
  CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_CONTRACT_VERSION,
  CAPABILITY_ENVIRONMENT_SNAPSHOT_VERSION,
  type CapabilityEnvironmentSnapshotEvidenceInput,
} from './capability-environment-snapshot-evidence.contract';
import {
  CAPABILITY_ROUTE_DECISION_VERSION,
  type CapabilityRouteDecision,
} from './capability-route-readiness.contract';
import {
  CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION,
  type CapabilityWorkspaceBootstrapPolicy,
  type CapabilityWorkspaceBootstrapPolicyBundleInput,
  type CapabilityWorkspaceBootstrapProfile,
} from './capability-workspace-bootstrap-policy-bundle.contract';
import { evaluateCapabilityBootstrapClosureEvidenceBundle as contractsBarrelEvaluator } from './index';
import { evaluateCapabilityBootstrapClosureEvidenceBundle as rootBarrelEvaluator } from '../index';

const NOW = '2026-08-17T10:00:00Z';
const WORKSPACE_ID = 'workspace-demo';

function plan(overrides: Partial<ControlledAcquisitionPlan> = {}): ControlledAcquisitionPlan {
  const base = {
    schemaVersion: CONTROLLED_ACQUISITION_PLAN_VERSION,
    planId: 'plan-t12-001',
    dependencyId: 'ripgrep',
    targetVersion: '14.1.1',
    sourceUri: 'https://publisher.example/ripgrep-14.1.1.zip',
    provenanceRef: 'publisher-release-14.1.1',
    integrityMethod: 'SHA256' as const,
    expectedDigest: 'a'.repeat(64),
    operations: [
      { operationId: 'download', phase: 'ACQUIRE' as const, action: 'DOWNLOAD' as const, target: 'workspace-cache', networkDestination: 'publisher.example', requiresPrivilege: false },
      { operationId: 'install', phase: 'ACQUIRE' as const, action: 'INSTALL' as const, target: 'workspace-demo/.cvf/tools/ripgrep', requiresPrivilege: false },
      { operationId: 'rollback', phase: 'ROLLBACK' as const, action: 'ROLLBACK' as const, target: 'workspace-demo/.cvf/tools/ripgrep', requiresPrivilege: false },
      { operationId: 'verify', phase: 'VERIFY' as const, action: 'VERIFY' as const, target: 'rg-version', requiresPrivilege: false },
    ],
    intendedMutations: [{ kind: 'WORKSPACE_FILE' as const, target: 'workspace-demo/.cvf/tools/ripgrep' }],
    rollbackOperationIds: ['rollback'],
    verificationOperationIds: ['verify'],
    forbiddenMutationKinds: ['SYSTEM_FILE' as const, 'SERVICE' as const],
    expiresAt: '2026-08-17T00:00:00Z',
    ...overrides,
  };
  const withoutDigest = { ...base };
  delete (withoutDigest as Partial<ControlledAcquisitionPlan>).planDigest;
  const planDigest = overrides.planDigest ?? computeControlledAcquisitionPlanDigest(withoutDigest as ControlledAcquisitionPlan);
  return { ...base, planDigest } as ControlledAcquisitionPlan;
}

function approval(value: ControlledAcquisitionPlan = plan(), overrides: Partial<CapabilityBootstrapApprovalEvidence> = {}): CapabilityBootstrapApprovalEvidence {
  return {
    schemaVersion: CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION,
    approvalId: 'approval-t12-001',
    planId: value.planId,
    planDigest: value.planDigest,
    workspaceId: WORKSPACE_ID,
    workOrderId: null,
    decision: 'APPROVE',
    actorId: 'operator-demo',
    issuedAt: '2026-08-16T04:00:00Z',
    expiresAt: '2026-08-16T05:00:00Z',
    replayNonce: 'nonce-t12-001',
    mutationEnvelope: [{
      kind: 'FILESYSTEM',
      target: 'workspace-demo/.cvf/tools/ripgrep',
      description: 'Create workspace-local tool directory.',
      reversible: true,
    }],
    ...overrides,
  };
}

function receipt(planValue: ControlledAcquisitionPlan = plan(), approvalValue: CapabilityBootstrapApprovalEvidence = approval(planValue), overrides: Partial<CapabilityAcquisitionReceipt> = {}): CapabilityAcquisitionReceipt {
  return {
    schemaVersion: CAPABILITY_ACQUISITION_RECEIPT_SCHEMA_VERSION,
    receiptId: 'receipt-t12-001',
    planId: planValue.planId,
    planDigest: planValue.planDigest,
    approvalId: approvalValue.approvalId,
    executorId: 'fixture-executor',
    startedAt: '2026-08-16T04:05:00Z',
    endedAt: '2026-08-16T04:06:00Z',
    operationResults: [
      { operationId: 'download', status: 'SUCCESS' },
      { operationId: 'install', status: 'SUCCESS' },
      { operationId: 'verify', status: 'SUCCESS' },
    ],
    actualMutations: [{
      kind: 'FILESYSTEM',
      target: 'workspace-demo/.cvf/tools/ripgrep',
      description: 'Create workspace-local tool directory.',
      reversible: true,
    }],
    artifact: {
      path: 'workspace-demo/.cvf/tools/ripgrep/rg.exe',
      version: '14.1.1',
      digest: 'a'.repeat(64),
    },
    verification: { status: 'PASS', checks: ['digest matched', 'mutation envelope matched'] },
    deviations: [],
    rollbackStatus: 'READY',
    refreshedSnapshotId: 'snap-t12-001',
    evidenceRefs: ['trace:fixture-001'],
    ...overrides,
  };
}

function receiptVerificationInput(overrides: Partial<CapabilityAcquisitionReceiptVerificationInput> = {}): CapabilityAcquisitionReceiptVerificationInput {
  const planValue = plan();
  const approvalValue = approval(planValue);
  return {
    plan: planValue,
    approval: approvalValue,
    expectedWorkspaceId: WORKSPACE_ID,
    expectedActorId: 'operator-demo',
    receipt: receipt(planValue, approvalValue),
    ...overrides,
  };
}

function route(overrides: Partial<CapabilityRouteDecision> = {}): CapabilityRouteDecision {
  return {
    schemaVersion: CAPABILITY_ROUTE_DECISION_VERSION,
    routeDecisionId: 'route:req-t12',
    candidateSetId: 'cset-t12',
    requestId: 'req-t12',
    workspaceId: WORKSPACE_ID,
    stage: 'FAST_ROUTE',
    primary: { capabilityId: 'ripgrep.acquire', packageId: 'ripgrep', packageVersion: '14.1.1' },
    supporting: [],
    rejected: [],
    fallbacks: [],
    confidence: 0.98,
    ambiguityReasons: [],
    environmentSnapshotRefs: ['snap-t12-001'],
    authorityStatus: 'CANDIDATE_ONLY',
    executionAuthorized: false,
    generatedAt: '2026-08-17T09:00:00Z',
    issues: [],
    ...overrides,
  };
}

function snapshotEvidenceInput(overrides: Partial<CapabilityEnvironmentSnapshotEvidenceInput> = {}): CapabilityEnvironmentSnapshotEvidenceInput {
  return {
    schemaVersion: CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_CONTRACT_VERSION,
    route: route(),
    snapshot: {
      schemaVersion: CAPABILITY_ENVIRONMENT_SNAPSHOT_VERSION,
      snapshotId: 'snap-t12-001',
      workspaceId: WORKSPACE_ID,
      observedAt: '2026-08-17T09:30:00Z',
      expiresAt: '2026-08-17T10:30:00Z',
      workspaceProfile: 'windows-local',
      platform: { os: 'win32', arch: 'x64', shell: 'powershell' },
      packages: [{ packageId: 'ripgrep', packageVersion: '14.1.1' }],
      dependencies: [],
      network: { mode: 'NORMAL', allowedDestinations: [] },
      sandbox: { status: 'AVAILABLE', profile: 'workspace-readonly' },
      credentialBindings: [],
      writableBoundaries: [WORKSPACE_ID],
      verification: { status: 'PASS', reasons: [] },
    },
    readinessPolicy: {
      readinessDecisionId: 'ready-t12-001',
      approvalRequired: false,
      existingApprovalValid: false,
      policyAllowed: true,
      provenanceVerified: true,
      integrityVerified: true,
      compatible: true,
      credentialsReady: true,
      networkReady: true,
      sandboxReady: true,
      evidenceRefs: ['evidence-t12-001'],
    },
    now: NOW,
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
    writableBoundaries: ['${WORKSPACE_ROOT}'],
    credentialBindings: [],
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

function policyBundleInput(overrides: Partial<CapabilityWorkspaceBootstrapPolicyBundleInput> = {}): CapabilityWorkspaceBootstrapPolicyBundleInput {
  const profile = windowsProfile();
  return {
    schemaVersion: CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION,
    profile,
    bootstrapPolicy: windowsPolicy(),
    requestedProfileId: profile.profileId,
    observedPlatform: 'win32',
    riskLevel: 'R2',
    now: NOW,
    ...overrides,
  };
}

function bundle(overrides: Partial<CapabilityBootstrapClosureEvidenceBundleInput> = {}): CapabilityBootstrapClosureEvidenceBundleInput {
  return {
    schemaVersion: CAPABILITY_BOOTSTRAP_CLOSURE_EVIDENCE_BUNDLE_CONTRACT_VERSION,
    expectedWorkspaceId: WORKSPACE_ID,
    receiptVerification: receiptVerificationInput(),
    snapshotEvidence: snapshotEvidenceInput(),
    policyBundle: policyBundleInput(),
    now: NOW,
    ...overrides,
  };
}

function clone<T>(value: T): T {
  return structuredClone(value);
}

function codes(result: CapabilityBootstrapClosureEvidenceBundleResult): string[] {
  return result.issues.map((issue) => issue.code);
}

const AUTHORITY_FIELDS = [
  'executionAuthorized', 'rollbackAuthorized', 'materializationAuthorized',
  'promotionAuthorized', 'acquisitionAuthorized', 'mutationAuthorized',
  'networkAuthorized', 'taskAuthorityGranted',
] as const;

describe('capability bootstrap closure evidence bundle', () => {
  it('exports the exact evaluator through both Guard Contract barrels', () => {
    expect(contractsBarrelEvaluator).toBe(evaluateCapabilityBootstrapClosureEvidenceBundle);
    expect(rootBarrelEvaluator).toBe(evaluateCapabilityBootstrapClosureEvidenceBundle);
  });

  it('accepts a fully composed happy-path T9/T10/T11 bundle deterministically without mutating input', () => {
    const evidence = bundle();
    const before = clone(evidence);
    const first = evaluateCapabilityBootstrapClosureEvidenceBundle(evidence);
    const second = evaluateCapabilityBootstrapClosureEvidenceBundle(evidence);

    expect(first).toEqual(second);
    expect(evidence).toEqual(before);
    expect(first.closureStatus).toBe('CLOSURE_EVIDENCE_ACCEPTED');
    expect(first.workspaceId).toBe(WORKSPACE_ID);
    expect(first.planId).toBe('plan-t12-001');
    expect(first.routeDecisionId).toBe('route:req-t12');
    expect(first.snapshotId).toBe('snap-t12-001');
    expect(first.selectedProfileId).toBe('windows-local');
    expect(first.policyId).toBe('capability-bootstrap.windows-local');
    expect(first.receiptVerification?.disposition).toBe('VERIFIED_SUCCESS_EVIDENCE');
    expect(first.snapshotEvidence?.status).toBe('VALIDATED_READY_EVIDENCE');
    expect(first.policyBundle?.status).toBe('VALIDATED_POLICY_EVIDENCE');
    expect(first.issues).toEqual([]);
    expect(Object.isFrozen(first)).toBe(true);
    expect(Object.isFrozen(first.issues)).toBe(true);
    expect(Object.isFrozen(first.receiptVerification)).toBe(true);
    expect(Object.isFrozen(first.snapshotEvidence)).toBe(true);
    expect(Object.isFrozen(first.policyBundle)).toBe(true);
    expect(Object.isFrozen(first.snapshotEvidence?.readiness)).toBe(true);
    expect(Object.isFrozen(first.policyBundle?.selectionEvidence)).toBe(true);
    for (const field of AUTHORITY_FIELDS) expect(first[field]).toBe(false);
  });

  it.each([
    ['null', null],
    ['array', []],
    ['class', new (class Envelope {})()],
    ['string', 'not-an-object'],
  ])('rejects a malformed %s envelope without throwing', (_label, value) => {
    expect(() => evaluateCapabilityBootstrapClosureEvidenceBundle(value)).not.toThrow();
    expect(evaluateCapabilityBootstrapClosureEvidenceBundle(value).closureStatus).toBe('CLOSURE_EVIDENCE_BLOCKED');
  });

  it('rejects unknown top-level keys', () => {
    const withExtra = bundle() as unknown as Record<string, unknown>;
    withExtra.extra = true;
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(withExtra);
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_BLOCKED');
    expect(codes(result)).toContain('UNKNOWN_KEY');
  });

  it('rejects proxies and accessors without invoking user hooks', () => {
    let invoked = 0;
    const proxied = new Proxy(bundle(), { get() { invoked += 1; throw new Error('must not run'); } });
    expect(evaluateCapabilityBootstrapClosureEvidenceBundle(proxied).closureStatus).toBe('CLOSURE_EVIDENCE_BLOCKED');

    const accessor = bundle() as unknown as Record<string, unknown>;
    Object.defineProperty(accessor, 'now', { enumerable: true, get() { invoked += 1; throw new Error('must not run'); } });
    expect(evaluateCapabilityBootstrapClosureEvidenceBundle(accessor).closureStatus).toBe('CLOSURE_EVIDENCE_BLOCKED');

    const nestedProxy = bundle() as unknown as Record<string, unknown>;
    nestedProxy.receiptVerification = new Proxy({}, { get() { invoked += 1; throw new Error('must not run'); } });
    expect(evaluateCapabilityBootstrapClosureEvidenceBundle(nestedProxy).closureStatus).toBe('CLOSURE_EVIDENCE_BLOCKED');

    expect(invoked).toBe(0);
  });

  it('rejects a malformed expectedWorkspaceId (control chars, secret-like, oversized, non-identifier)', () => {
    for (const bad of ['bad\u0000id', 'password=hunter2', 'a'.repeat(300), 'has spaces']) {
      const result = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle({ expectedWorkspaceId: bad }));
      expect(result.closureStatus).not.toBe('CLOSURE_EVIDENCE_ACCEPTED');
    }
  });

  it('rejects an invalid now timestamp', () => {
    for (const bad of ['not-a-date', '2026-08-17', '2026-13-40T00:00:00Z']) {
      const result = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle({ now: bad }));
      expect(result.closureStatus).not.toBe('CLOSURE_EVIDENCE_ACCEPTED');
      expect(codes(result)).toContain('INVALID_FIELD');
    }
  });

  it('propagates T9 receipt-verification rejection as RECEIPT_VERIFICATION_REJECTED', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({ receiptVerification: receiptVerificationInput({ receipt: receipt(plan(), approval(), { verification: { status: 'FAIL', checks: ['digest mismatch'] } }) }) }),
    );
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('RECEIPT_VERIFICATION_REJECTED');
    expect(result.receiptVerification?.disposition).toBe('REJECTED');
  });

  it('propagates T10 snapshot-evidence rejection as SNAPSHOT_EVIDENCE_REJECTED', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({ snapshotEvidence: snapshotEvidenceInput({ route: route({ stage: 'AMBIGUOUS_ROUTE' }) }) }),
    );
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('SNAPSHOT_EVIDENCE_REJECTED');
  });

  it('propagates T11 policy-bundle rejection as POLICY_BUNDLE_REJECTED', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({ policyBundle: policyBundleInput({ bootstrapPolicy: windowsPolicy({ requireIntegrity: false }) }) }),
    );
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('POLICY_BUNDLE_REJECTED');
  });

  it('rejects when all three upstream evaluators fail simultaneously with all three issue codes present', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle({
      receiptVerification: receiptVerificationInput({ receipt: receipt(plan(), approval(), { rollbackStatus: 'FAILED' }) }),
      snapshotEvidence: snapshotEvidenceInput({ snapshot: { ...snapshotEvidenceInput().snapshot, verification: { status: 'FAIL', reasons: ['not observed'] } } }),
      policyBundle: policyBundleInput({ bootstrapPolicy: windowsPolicy({ defaultDecision: 'ALLOW' as never }) }),
    }));
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toEqual(expect.arrayContaining([
      'RECEIPT_VERIFICATION_REJECTED', 'SNAPSHOT_EVIDENCE_REJECTED', 'POLICY_BUNDLE_REJECTED',
    ]));
  });

  it('rejects a cross-record workspace-id mismatch between receipt-verification and snapshot-evidence', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({ snapshotEvidence: snapshotEvidenceInput({ route: route({ workspaceId: 'workspace-other' }), snapshot: { ...snapshotEvidenceInput().snapshot, workspaceId: 'workspace-other' } }) }),
    );
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('WORKSPACE_BINDING_MISMATCH');
  });

  it('rejects a cross-record plan/route package mismatch', () => {
    const mismatchedRoute = route({ primary: { capabilityId: 'other.acquire', packageId: 'other-package', packageVersion: '1.0.0' } });
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({
        snapshotEvidence: snapshotEvidenceInput({
          route: mismatchedRoute,
          snapshot: { ...snapshotEvidenceInput().snapshot, packages: [{ packageId: 'other-package', packageVersion: '1.0.0' }] },
        }),
      }),
    );
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('PLAN_BINDING_MISMATCH');
  });

  it('rejects a receipt refreshed-snapshot identity that differs from the validated T10 snapshot', () => {
    const receiptInput = receiptVerificationInput();
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle({
      receiptVerification: {
        ...receiptInput,
        receipt: { ...receiptInput.receipt, refreshedSnapshotId: 'snap-other' },
      },
    }));
    expect(result.receiptVerification?.disposition).toBe('VERIFIED_SUCCESS_EVIDENCE');
    expect(result.snapshotEvidence?.status).toBe('VALIDATED_READY_EVIDENCE');
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('SNAPSHOT_BINDING_MISMATCH');
  });

  it('rejects a T10 workspace-profile identity that differs from the validated T11 profile', () => {
    const snapshotInput = snapshotEvidenceInput();
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle({
      snapshotEvidence: {
        ...snapshotInput,
        snapshot: { ...snapshotInput.snapshot, workspaceProfile: 'profile-other' },
      },
    }));
    expect(result.snapshotEvidence?.status).toBe('VALIDATED_READY_EVIDENCE');
    expect(result.policyBundle?.status).toBe('VALIDATED_POLICY_EVIDENCE');
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('PROFILE_BINDING_MISMATCH');
  });

  it('rejects contradictory cross-record platform evidence even when T10 and T11 each accept', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle({
      policyBundle: policyBundleInput({
        profile: windowsProfile({ platforms: ['win32', 'linux'] }),
        observedPlatform: 'linux',
      }),
    }));
    expect(result.policyBundle?.status).toBe('VALIDATED_POLICY_EVIDENCE');
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('PROFILE_BINDING_MISMATCH');
  });

  it('rejects contradictory cross-record network evidence even when T10 and T11 each accept', () => {
    const offlineProfile = windowsProfile({
      profileId: 'offline-local',
      platforms: ['win32', 'linux', 'darwin'],
      shellPreference: ['sh'],
      networkMode: 'OFFLINE',
      installPreference: ['existing-only', 'verified-local-artifact'],
      scanTtlSeconds: { R0: 1800, R1: 900, R2: 180, R3: 60 },
      pathDiscovery: [],
      notes: ['No network acquisition permitted.'],
    });
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle({
      policyBundle: policyBundleInput({
        profile: offlineProfile,
        bootstrapPolicy: {
          policyId: 'capability-bootstrap.offline-local',
          defaultDecision: 'BLOCK',
          networkDefault: 'DENY',
          allowNetwork: false,
          allowVerifiedLocalArtifact: true,
          requireIntegrity: true,
          maxRepairRoundsWithoutNewEvidence: 3,
        },
        requestedProfileId: 'offline-local',
      }),
    }));
    expect(result.snapshotEvidence?.status).toBe('VALIDATED_READY_EVIDENCE');
    expect(result.policyBundle?.status).toBe('VALIDATED_POLICY_EVIDENCE');
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('PROFILE_BINDING_MISMATCH');
  });

  it('rejects stale receipt evidence whose endedAt is after the closure evaluation time', () => {
    const planValue = plan({ expiresAt: '2026-08-18T00:00:00Z' });
    const approvalValue = approval(planValue, { issuedAt: '2026-08-17T10:04:00Z', expiresAt: '2026-08-17T11:30:00Z' });
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({ receiptVerification: receiptVerificationInput({ plan: planValue, approval: approvalValue, receipt: receipt(planValue, approvalValue, { startedAt: '2026-08-17T10:05:00Z', endedAt: '2026-08-17T11:00:00Z' }) }) }),
    );
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(result.receiptVerification?.disposition).toBe('VERIFIED_SUCCESS_EVIDENCE');
    expect(codes(result)).toContain('STALE_EVIDENCE_TIME');
  });

  it('rejects a snapshot-evidence time that does not equal the closure evaluation time', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({ snapshotEvidence: snapshotEvidenceInput({ now: '2026-08-17T09:59:00Z' }) }),
    );
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('STALE_EVIDENCE_TIME');
  });

  it('rejects a policy-bundle time that does not equal the closure evaluation time', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({ policyBundle: policyBundleInput({ now: '2026-08-17T09:59:00Z' }) }),
    );
    expect(result.closureStatus).toBe('CLOSURE_EVIDENCE_REJECTED');
    expect(codes(result)).toContain('STALE_EVIDENCE_TIME');
  });

  it('rejects huge arrays and sparse arrays inside nested upstream evidence', () => {
    const hugeDeviations = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({ receiptVerification: receiptVerificationInput({ receipt: receipt(plan(), approval(), { deviations: Array.from({ length: 200 }, (_, i) => `deviation-${i}`) }) }) }),
    );
    expect(hugeDeviations.closureStatus).not.toBe('CLOSURE_EVIDENCE_ACCEPTED');

    const sparsePackages = bundle() as unknown as { snapshotEvidence: { snapshot: { packages: unknown[] } } };
    const sparseArray: unknown[] = [];
    sparseArray[5] = { packageId: 'ripgrep', packageVersion: '14.1.1' };
    sparsePackages.snapshotEvidence.snapshot.packages = sparseArray;
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(sparsePackages);
    expect(result.closureStatus).not.toBe('CLOSURE_EVIDENCE_ACCEPTED');
  });

  it('redacts and rejects secret-like content in the expectedWorkspaceId', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(
      bundle({ expectedWorkspaceId: 'api_key=abcdef123456' }),
    );
    expect(result.closureStatus).not.toBe('CLOSURE_EVIDENCE_ACCEPTED');
    expect(codes(result)).toContain('RAW_SECRET_DETECTED');
    expect(JSON.stringify(result)).not.toContain('abcdef123456');
  });

  it('always reports every action-authority field as literal false, including on acceptance', () => {
    const accepted = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle());
    const rejected = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle({ policyBundle: policyBundleInput({ bootstrapPolicy: windowsPolicy({ requireIntegrity: false }) }) }));
    const blocked = evaluateCapabilityBootstrapClosureEvidenceBundle(null);
    for (const result of [accepted, rejected, blocked]) {
      expect(result.authorityStatus).toBe('EVIDENCE_ONLY');
      for (const field of AUTHORITY_FIELDS) expect(result[field]).toBe(false);
    }
  });

  it('produces a deeply frozen result whose nested arrays cannot be mutated', () => {
    const result = evaluateCapabilityBootstrapClosureEvidenceBundle(bundle());
    expect(Object.isFrozen(result.issues)).toBe(true);
    expect(() => { (result as { workspaceId: string }).workspaceId = 'hacked'; }).toThrow();
    expect(() => { (result.issues as unknown as unknown[]).push({}); }).toThrow();
  });

  it('does not mutate the caller-supplied nested T9/T10/T11 inputs across repeated evaluation', () => {
    const evidence = bundle();
    const before = clone(evidence);
    evaluateCapabilityBootstrapClosureEvidenceBundle(evidence);
    evaluateCapabilityBootstrapClosureEvidenceBundle(evidence);
    expect(evidence).toEqual(before);
  });
});
