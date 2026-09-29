import { describe, expect, it } from 'vitest';
import {
  CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION,
  evaluateCapabilityBootstrapApprovalEvidenceBinding,
  type CapabilityBootstrapApprovalEvidence,
  type CapabilityBootstrapMutationEnvelopeEntry,
} from './capability-bootstrap-approval-evidence.contract';
import {
  CONTROLLED_ACQUISITION_PLAN_VERSION,
  computeControlledAcquisitionPlanDigest,
  type ControlledAcquisitionPlan,
} from './controlled-acquisition.contract';
import { evaluateCapabilityBootstrapApprovalEvidenceBinding as contractsBarrelEvaluator } from './index';
import { evaluateCapabilityBootstrapApprovalEvidenceBinding as rootBarrelEvaluator } from '../index';

function plan(overrides: Partial<ControlledAcquisitionPlan> = {}): ControlledAcquisitionPlan {
  const base = {
    schemaVersion: CONTROLLED_ACQUISITION_PLAN_VERSION,
    planId: 'plan-t8-001',
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

function envelopeEntry(overrides: Partial<CapabilityBootstrapMutationEnvelopeEntry> = {}): CapabilityBootstrapMutationEnvelopeEntry {
  return {
    kind: 'FILESYSTEM',
    target: 'workspace-demo/.cvf/tools/ripgrep',
    description: 'Create workspace-local tool directory.',
    reversible: true,
    ...overrides,
  };
}

function approval(value: ControlledAcquisitionPlan = plan(), overrides: Partial<CapabilityBootstrapApprovalEvidence> = {}): CapabilityBootstrapApprovalEvidence {
  return {
    schemaVersion: CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION,
    approvalId: 'approval-t8-001',
    planId: value.planId,
    planDigest: value.planDigest,
    workspaceId: 'workspace-demo',
    workOrderId: null,
    decision: 'APPROVE',
    actorId: 'operator-demo',
    issuedAt: '2026-08-16T04:00:00Z',
    expiresAt: '2026-08-16T05:00:00Z',
    replayNonce: 'nonce-demo-001',
    mutationEnvelope: [envelopeEntry()],
    ...overrides,
  };
}

function input(overrides: Partial<Record<string, unknown>> = {}) {
  const value = plan();
  return {
    plan: value,
    approval: approval(value),
    expectedWorkspaceId: 'workspace-demo',
    expectedActorId: 'operator-demo',
    now: '2026-08-16T04:30:00Z',
    ...overrides,
  };
}

describe('capability bootstrap approval evidence binding kernel', () => {
  it('exports the exact evaluator through both Guard Contract barrels', () => {
    expect(contractsBarrelEvaluator).toBe(evaluateCapabilityBootstrapApprovalEvidenceBinding);
    expect(rootBarrelEvaluator).toBe(evaluateCapabilityBootstrapApprovalEvidenceBinding);
  });

  it('validates an exact matching plan/approval/workspace/actor/envelope binding as evidence only', () => {
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input());
    expect(result).toEqual(expect.objectContaining({
      disposition: 'VALIDATED_EVIDENCE',
      replayCheckRequired: true,
      approvalIssued: false,
      executionAuthorized: false,
      acquisitionAuthorized: false,
      mutationAuthorized: false,
      taskAuthorityGranted: false,
      networkAuthorized: false,
      issues: [],
    }));
  });

  it('accepts an explicit work-order expectation match', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      approval: approval(value, { workOrderId: 'wo-1' }),
      expectedWorkOrderId: 'wo-1',
    }));
    expect(result.disposition).toBe('VALIDATED_EVIDENCE');
  });

  it('keeps all authority literals false even on a rejected path', () => {
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({ plan: 'not-a-plan' }));
    expect(result).toEqual(expect.objectContaining({
      disposition: 'REJECTED',
      replayCheckRequired: true,
      approvalIssued: false,
      executionAuthorized: false,
      acquisitionAuthorized: false,
      mutationAuthorized: false,
      taskAuthorityGranted: false,
      networkAuthorized: false,
    }));
  });

  it('rejects non-plain-object top-level input without throwing', () => {
    expect(evaluateCapabilityBootstrapApprovalEvidenceBinding(null).disposition).toBe('REJECTED');
    expect(evaluateCapabilityBootstrapApprovalEvidenceBinding(undefined).disposition).toBe('REJECTED');
    expect(evaluateCapabilityBootstrapApprovalEvidenceBinding('string').disposition).toBe('REJECTED');
    expect(evaluateCapabilityBootstrapApprovalEvidenceBinding(42).disposition).toBe('REJECTED');
    expect(evaluateCapabilityBootstrapApprovalEvidenceBinding([]).disposition).toBe('REJECTED');
  });

  it('rejects a Proxy-wrapped top-level input without invoking traps', () => {
    let trapped = false;
    const proxied = new Proxy(input(), {
      get(target, key, receiver) {
        trapped = true;
        return Reflect.get(target, key, receiver);
      },
    });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(proxied);
    expect(result.disposition).toBe('REJECTED');
    expect(trapped).toBe(false);
  });

  it('rejects a Proxy-wrapped approval object without invoking traps', () => {
    let trapped = false;
    const value = plan();
    const proxiedApproval = new Proxy(approval(value), {
      get(target, key, receiver) {
        trapped = true;
        return Reflect.get(target, key, receiver);
      },
    });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({ approval: proxiedApproval }));
    expect(result.disposition).toBe('REJECTED');
    expect(trapped).toBe(false);
  });

  it('rejects an approval object with accessor properties without invoking the getter', () => {
    let getterCalled = false;
    const value = plan();
    const hostile = approval(value);
    Object.defineProperty(hostile, 'actorId', {
      enumerable: true,
      get() {
        getterCalled = true;
        return 'operator-demo';
      },
    });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({ approval: hostile }));
    expect(result.disposition).toBe('REJECTED');
    expect(getterCalled).toBe(false);
  });

  it('rejects a sparse mutation envelope array', () => {
    const value = plan();
    const sparse: unknown[] = [envelopeEntry()];
    sparse[3] = envelopeEntry({ target: 'other' });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      approval: approval(value, { mutationEnvelope: sparse as CapabilityBootstrapMutationEnvelopeEntry[] }),
    }));
    expect(result.disposition).toBe('REJECTED');
  });

  it('rejects symbol or extra properties attached to arrays without echoing them', () => {
    const value = plan();
    const hostile = [envelopeEntry()] as Array<CapabilityBootstrapMutationEnvelopeEntry> & Record<PropertyKey, unknown>;
    hostile[Symbol('api_key=must-not-leak')] = true;
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      approval: approval(value, { mutationEnvelope: hostile }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(JSON.stringify(result)).not.toContain('must-not-leak');
  });

  it('rejects an oversized mutation envelope array', () => {
    const value = plan();
    const oversized = Array.from({ length: 65 }, (_unused, index) => envelopeEntry({ target: `target-${index}` }));
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      approval: approval(value, { mutationEnvelope: oversized }),
    }));
    expect(result.disposition).toBe('REJECTED');
  });

  it('rejects unknown keys on the approval object', () => {
    const value = plan();
    const hostile = { ...approval(value), extraField: 'not allowed' };
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({ approval: hostile }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'UNKNOWN_KEYS')).toBe(true);
  });

  it('rejects a symbol key on the input object without leaking it', () => {
    const value = plan();
    const hostile = input() as Record<PropertyKey, unknown>;
    hostile[Symbol('hidden')] = 'value';
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(hostile);
    expect(result.disposition).toBe('REJECTED');
  });

  it('rejects control characters embedded in identifiers', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      approval: approval(value, { actorId: 'operator demo' }),
    }));
    expect(result.disposition).toBe('REJECTED');
  });

  it('rejects a stale controlled-acquisition plan', () => {
    const value = plan({ expiresAt: '2026-08-16T00:00:00Z' });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { expiresAt: '2026-08-15T23:00:00Z' }),
      now: '2026-08-16T04:30:00Z',
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'PLAN_EXPIRED')).toBe(true);
  });

  it('rejects a plan whose digest was tampered after signing', () => {
    const value = plan();
    const tampered = { ...value, targetVersion: '99.0.0' };
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: tampered,
      approval: approval(value),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'PLAN_DIGEST_MISMATCH')).toBe(true);
  });

  it('rejects unknown plan keys even when the T3 authority digest ignores them', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: { ...value, parallelAuthority: 'not-allowed' },
      approval: approval(value),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((candidate) => candidate.code === 'UNKNOWN_KEYS')).toBe(true);
  });

  it('rejects a nested plan mutation accessor without invoking its getter', () => {
    let getterCalled = false;
    const value = plan();
    const hostileMutation: Record<string, unknown> = { kind: 'WORKSPACE_FILE' };
    Object.defineProperty(hostileMutation, 'target', {
      enumerable: true,
      get() {
        getterCalled = true;
        return 'workspace-demo/.cvf/tools/ripgrep';
      },
    });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: { ...value, intendedMutations: [hostileMutation] },
      approval: approval(value),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(getterCalled).toBe(false);
  });

  it('rejects a nested plan operation Proxy without invoking traps', () => {
    let trapped = false;
    const value = plan();
    const proxiedOperation = new Proxy(value.operations[0], {
      get(target, key, receiver) {
        trapped = true;
        return Reflect.get(target, key, receiver);
      },
    });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: { ...value, operations: [proxiedOperation, ...value.operations.slice(1)] },
      approval: approval(value),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(trapped).toBe(false);
  });

  it('rejects sparse and oversized nested plan arrays before digest evaluation', () => {
    const value = plan();
    const sparse = [value.operations[0]];
    sparse[3] = value.operations[1];
    const sparseResult = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: { ...value, operations: sparse },
      approval: approval(value),
    }));
    expect(sparseResult.disposition).toBe('REJECTED');

    const oversized = Array.from({ length: 129 }, () => value.operations[0]);
    const oversizedResult = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: { ...value, operations: oversized },
      approval: approval(value),
    }));
    expect(oversizedResult.disposition).toBe('REJECTED');
  });

  it('reuses current T3 semantics to reject unsafe source and invalid integrity evidence', () => {
    const unsafe = plan({ sourceUri: 'http://publisher.example/tool.zip' });
    const unsafeResult = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: unsafe,
      approval: approval(unsafe),
    }));
    expect(unsafeResult.disposition).toBe('REJECTED');
    expect(unsafeResult.issues.some((candidate) => candidate.code === 'PLAN_T3_REJECTED')).toBe(true);

    const invalidDigest = plan({ expectedDigest: 'not-a-sha256' });
    const digestResult = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: invalidDigest,
      approval: approval(invalidDigest),
    }));
    expect(digestResult.disposition).toBe('REJECTED');
  });

  it('reuses current T3 semantics to reject duplicate operations and incomplete rollback', () => {
    const seed = plan();
    const duplicate = plan({ operations: [...seed.operations, seed.operations[0]] });
    const duplicateResult = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: duplicate,
      approval: approval(duplicate),
    }));
    expect(duplicateResult.disposition).toBe('REJECTED');
    expect(duplicateResult.issues.some((candidate) => candidate.code === 'PLAN_T3_REJECTED')).toBe(true);

    const incomplete = plan({ rollbackOperationIds: [] });
    const incompleteResult = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: incomplete,
      approval: approval(incomplete),
    }));
    expect(incompleteResult.disposition).toBe('REJECTED');
  });

  it('reuses current T3 semantics to reject a forbidden planned mutation', () => {
    const value = plan({
      intendedMutations: [{ kind: 'SYSTEM_FILE', target: 'system/tool' }],
      forbiddenMutationKinds: ['SYSTEM_FILE'],
    });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, {
        mutationEnvelope: [envelopeEntry({ target: 'system/tool' })],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((candidate) => candidate.code === 'PLAN_T3_REJECTED')).toBe(true);
  });

  it('rejects plan mutations that collapse to one ambiguous normalized envelope entry', () => {
    const value = plan({
      intendedMutations: [
        { kind: 'WORKSPACE_FILE', target: 'shared-target' },
        { kind: 'USER_FILE', target: 'shared-target' },
      ],
    });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, {
        mutationEnvelope: [envelopeEntry({ target: 'shared-target' })],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((candidate) => candidate.code === 'ENVELOPE_AMBIGUOUS_ENTRY')).toBe(true);
  });

  it('rejects approval not bound to the exact plan id/digest', () => {
    const value = plan();
    const other = plan({ planId: 'plan-other' });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(other, { planId: value.planId }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'PLAN_BINDING_MISMATCH')).toBe(true);
  });

  it('rejects workspace drift from the expected workspace', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { workspaceId: 'workspace-other' }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'WORKSPACE_MISMATCH')).toBe(true);
  });

  it('rejects actor drift from the expected actor', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { actorId: 'operator-other' }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ACTOR_MISMATCH')).toBe(true);
  });

  it('rejects a work-order mismatch when an explicit expectation is set', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { workOrderId: 'wo-actual' }),
      expectedWorkOrderId: 'wo-expected',
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'WORK_ORDER_MISMATCH')).toBe(true);
  });

  it('rejects a null work-order when a non-null work order was expected', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { workOrderId: null }),
      expectedWorkOrderId: 'wo-expected',
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'WORK_ORDER_MISMATCH')).toBe(true);
  });

  it('rejects a replay nonce carrying secret-like content', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { replayNonce: 'api_key=abcdef' }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'NONCE_INVALID')).toBe(true);
  });

  it('rejects a non-APPROVE decision', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: { ...approval(value), decision: 'REJECT' },
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'APPROVAL_NOT_APPROVED')).toBe(true);
  });

  it('rejects an expired approval', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { issuedAt: '2026-08-16T02:00:00Z', expiresAt: '2026-08-16T03:00:00Z' }),
      now: '2026-08-16T04:30:00Z',
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'APPROVAL_EXPIRED')).toBe(true);
  });

  it('rejects an approval whose expiry exceeds the plan expiry', () => {
    const value = plan({ expiresAt: '2026-08-16T06:00:00Z' });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { issuedAt: '2026-08-16T04:00:00Z', expiresAt: '2026-08-17T00:00:00Z' }),
      now: '2026-08-16T04:30:00Z',
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'APPROVAL_EXPIRY_EXCEEDS_PLAN_EXPIRY')).toBe(true);
  });

  it('rejects invalid issued/expiry date ordering and non-ISO timestamps', () => {
    const value = plan();
    const backwards = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { issuedAt: '2026-08-16T05:00:00Z', expiresAt: '2026-08-16T04:00:00Z' }),
    }));
    expect(backwards.disposition).toBe('REJECTED');

    const malformed = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { issuedAt: 'not-a-date' }),
    }));
    expect(malformed.disposition).toBe('REJECTED');
  });

  it('rejects approval evidence issued after the explicit current time', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { issuedAt: '2026-08-16T04:45:00Z' }),
      now: '2026-08-16T04:30:00Z',
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((candidate) => candidate.path === '$.approval.issuedAt')).toBe(true);
  });

  it('rejects a missing required mutation-envelope entry', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { mutationEnvelope: [] }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ENVELOPE_MISSING_ENTRY')).toBe(true);
  });

  it('rejects an extra mutation-envelope entry outside the planned scope', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, {
        mutationEnvelope: [envelopeEntry(), envelopeEntry({ kind: 'REGISTRY', target: 'HKCU:/Software/Extra' })],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ENVELOPE_EXTRA_ENTRY')).toBe(true);
  });

  it('rejects a duplicate mutation-envelope entry', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, { mutationEnvelope: [envelopeEntry(), envelopeEntry()] }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ENVELOPE_DUPLICATE_ENTRY')).toBe(true);
  });

  it('rejects an ambiguous mutation-envelope entry claiming one target under two classes', () => {
    const value = plan({
      intendedMutations: [
        { kind: 'WORKSPACE_FILE', target: 'shared-target' },
      ],
    });
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, {
        mutationEnvelope: [
          envelopeEntry({ kind: 'FILESYSTEM', target: 'shared-target' }),
          envelopeEntry({ kind: 'ENVIRONMENT', target: 'shared-target' }),
        ],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ENVELOPE_AMBIGUOUS_ENTRY' || issue.code === 'ENVELOPE_EXTRA_ENTRY')).toBe(true);
  });

  it('rejects an irreversible envelope entry without an explicit irreversible marker', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, {
        mutationEnvelope: [envelopeEntry({ reversible: false, description: 'Removes the tool directory.' })],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ENVELOPE_IRREVERSIBLE_WITHOUT_MARKER')).toBe(true);
  });

  it('accepts an irreversible envelope entry that carries an explicit irreversible marker', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, {
        mutationEnvelope: [envelopeEntry({ reversible: false, description: 'Irreversible removal of the tool directory.' })],
      }),
    }));
    expect(result.disposition).toBe('VALIDATED_EVIDENCE');
  });

  it('rejects a mutation-envelope entry with secret-like description content', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, {
        mutationEnvelope: [envelopeEntry({ description: 'Binds credential=abc123 into the workspace.' })],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'ENVELOPE_SECRET_LIKE_ENTRY')).toBe(true);
  });

  it('rejects an unsupported envelope class', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: approval(value, {
        mutationEnvelope: [{ ...envelopeEntry(), kind: 'UNKNOWN_CLASS' as unknown as 'FILESYSTEM' }],
      }),
    }));
    expect(result.disposition).toBe('REJECTED');
  });

  it('rejects an unsupported approval schema version', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: value,
      approval: { ...approval(value), schemaVersion: 'wrong.version.v1' as unknown as typeof CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_SCHEMA_VERSION },
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'APPROVAL_SCHEMA_UNSUPPORTED')).toBe(true);
  });

  it('rejects an unsupported plan schema version', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({
      plan: { ...value, schemaVersion: 'wrong.plan.version.v1' },
      approval: approval(value),
    }));
    expect(result.disposition).toBe('REJECTED');
    expect(result.issues.some((issue) => issue.code === 'PLAN_SCHEMA_UNSUPPORTED')).toBe(true);
  });

  it('never echoes notes, raw source URI, or mutation descriptions into the result', () => {
    const value = plan();
    const withNotes = { ...approval(value), notes: 'do not leak this note' } as unknown as CapabilityBootstrapApprovalEvidence;
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({ plan: value, approval: withNotes }));
    const serialized = JSON.stringify(result);
    expect(serialized).not.toContain('do not leak this note');
    expect(serialized).not.toContain(value.sourceUri);
    expect(serialized).not.toContain('Create workspace-local tool directory.');
  });

  it('does not echo a secret-like unknown property name into rejection issues', () => {
    const value = plan();
    const hostile = { ...approval(value), 'api_key=must-not-leak': true };
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({ approval: hostile }));
    expect(result.disposition).toBe('REJECTED');
    expect(JSON.stringify(result)).not.toContain('must-not-leak');
  });

  it('never echoes the raw replay nonce or full actor detail beyond the validated actor id', () => {
    const value = plan();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input({ plan: value }));
    const serialized = JSON.stringify(result);
    expect(serialized).not.toContain('nonce-demo-001');
  });

  it('produces stable issue ordering and identical output for identical explicit input', () => {
    const first = evaluateCapabilityBootstrapApprovalEvidenceBinding(input());
    const second = evaluateCapabilityBootstrapApprovalEvidenceBinding(input());
    expect(first).toEqual(second);

    const invalid = input({ expectedActorId: 'operator-other', unknownField: true });
    const firstRejected = evaluateCapabilityBootstrapApprovalEvidenceBinding(invalid);
    const secondRejected = evaluateCapabilityBootstrapApprovalEvidenceBinding(invalid);
    expect(firstRejected).toEqual(secondRejected);
    expect(firstRejected.issues.map(({ code, path }) => ({ code, path }))).toEqual(
      secondRejected.issues.map(({ code, path }) => ({ code, path })),
    );
  });

  it('does not mutate the caller-supplied input', () => {
    const value = plan();
    const approvalValue = approval(value);
    const frozenInput = Object.freeze({
      plan: value,
      approval: approvalValue,
      expectedWorkspaceId: 'workspace-demo',
      expectedActorId: 'operator-demo',
      now: '2026-08-16T04:30:00Z',
    });
    expect(() => evaluateCapabilityBootstrapApprovalEvidenceBinding(frozenInput)).not.toThrow();
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(frozenInput);
    expect(result.disposition).toBe('VALIDATED_EVIDENCE');
  });

  it('keeps every authority literal false on the positive path', () => {
    const result = evaluateCapabilityBootstrapApprovalEvidenceBinding(input());
    expect(result.approvalIssued).toBe(false);
    expect(result.executionAuthorized).toBe(false);
    expect(result.acquisitionAuthorized).toBe(false);
    expect(result.mutationAuthorized).toBe(false);
    expect(result.taskAuthorityGranted).toBe(false);
    expect(result.networkAuthorized).toBe(false);
    expect(result.replayCheckRequired).toBe(true);
  });
});
