import { describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import {
  CADP_CONTRACT_VERSION,
  createDeterministicCadpReceipt,
  validateCapabilityAdmission,
  validateCapabilityAssignment,
  validateCapabilityDistribution,
  validateCompatibilityEvidence,
  CAPABILITY_OWNER_BINDING_CONTRACT_VERSION,
  bindCommittedCapabilityOwnerGrant,
  isBoundCapabilityOwner,
  readBoundArtifact,
  readBoundGrantIdentity,
  reconcileGrantWithObservation,
} from './contracts/index';
import * as contractsBarrel from './contracts/index';
import * as packageRoot from './index';

function loadPackageJson() {
  const packageUrl = new URL('../package.json', import.meta.url);
  return JSON.parse(readFileSync(packageUrl, 'utf8')) as {
    exports?: Record<string, string>;
    files?: string[];
  };
}

describe('package boundary', () => {
  it('exposes the bounded CADP contract through the canonical contracts barrel', () => {
    expect(CADP_CONTRACT_VERSION).toBe('cvf.cadp.v1');
    expect([
      createDeterministicCadpReceipt,
      validateCapabilityAdmission,
      validateCapabilityAssignment,
      validateCapabilityDistribution,
      validateCompatibilityEvidence,
    ].every((value) => typeof value === 'function')).toBe(true);
  });

  it('exposes the T2 owner-binding consumption surface through the same canonical contracts barrel, never a minting function', () => {
    expect(CAPABILITY_OWNER_BINDING_CONTRACT_VERSION).toBe('cvf.cadp.ownerBinding.v3');
    expect([
      bindCommittedCapabilityOwnerGrant,
      isBoundCapabilityOwner,
      readBoundArtifact,
      readBoundGrantIdentity,
      reconcileGrantWithObservation,
    ].every((value) => typeof value === 'function')).toBe(true);
  });

  it('T2A exposes only the deliberate path-only binder, never a generic grant-data mint', () => {
    // This is the corrected version of the round-1 test this same file
    // used to carry, which incorrectly named `bindNamedCapabilityOwner`
    // itself as "the one named adapter" without checking whether that
    // adapter was reachable from a real caller - it was, and an
    // independent review reproduced the exact caller-created-grant ->
    // public-binder -> genuine-handle attack against it. The round-2
    // re-review then found that renaming the binder
    // `_TEST_ONLY_INTERNAL_BINDER` and omitting it from this barrel was
    // STILL not sufficient: a direct module import reached it anyway. The
    // T2A keeps the old generic binders absent and exposes one path-only
    // committed-source binder through the canonical barrel and root.
    const barrel = contractsBarrel as unknown as Record<string, unknown>;
    expect(barrel.bindNamedCapabilityOwner).toBeUndefined();
    expect(barrel.bindNamedCapabilityOwner_TEST_ONLY_INTERNAL_BINDER).toBeUndefined();
    expect(barrel.bindNamedCapabilityOwnerForTest).toBeUndefined();
    expect(typeof barrel.bindCommittedCapabilityOwnerGrant).toBe('function');
    expect(typeof packageRoot.bindCommittedCapabilityOwnerGrant).toBe('function');
    expect(bindCommittedCapabilityOwnerGrant({}).valid).toBe(false);
    // Every exported function on the barrel that touches
    // `CapabilityOwnerHandle` must only ever *consume* an existing handle,
    // never accept an arbitrary evidence/grant record and return one.
    const forged = { contractVersion: 'cvf.cadp.ownerBinding.v3' };
    expect(isBoundCapabilityOwner(forged)).toBe(false);
    expect(readBoundArtifact(forged as never, 'any-ref')).toBeUndefined();
    expect(readBoundGrantIdentity(forged as never)).toBeUndefined();
    expect(reconcileGrantWithObservation(forged as never, {
      workOrderId: 'x', workOrderVersion: 'x', capabilityId: 'x', capabilityVersion: 'x',
      assignmentId: 'x', actionId: 'x',
      transport: 'x', resourceRef: 'x', credentialReference: 'secretref:x',
      workflowTraceId: 'x', receiptId: 'x',
      invocationId: 'x', retryOrdinal: 0, evaluatedAt: '2026-08-13T00:00:00Z',
    }).valid).toBe(false);
  });

  it('direct import exposes no generic grant-data mint and rejects objects at the path-only binder', async () => {
    // This is the exact attack shape the round-2 independent review used
    // to reproduce the residual exploit: import the production module
    // directly by relative/deep path, exactly as
    // `EXTENSIONS/CVF_PLANE_FACADES/tsconfig.json`'s `cvf-guard-contract/*`
    // mapping allows a same-repository consumer to do, skipping the
    // barrel and package.json exports map entirely. The fix is not that
    // this import path is blocked. The security property is that its only
    // binder reads committed repository bytes and rejects a grant object.
    const productionModule = await import('./contracts/capability-owner-binding.contract');
    const moduleExports = productionModule as unknown as Record<string, unknown>;
    expect(moduleExports.bindNamedCapabilityOwner).toBeUndefined();
    expect(moduleExports.bindNamedCapabilityOwner_TEST_ONLY_INTERNAL_BINDER).toBeUndefined();
    expect(moduleExports.bindNamedCapabilityOwnerForTest).toBeUndefined();
    expect((moduleExports.bindCommittedCapabilityOwnerGrant as (value: unknown) => { valid: boolean })({}).valid).toBe(false);
    for (const [exportName, exportValue] of Object.entries(moduleExports)) {
      if (typeof exportValue !== 'function') continue;
      let result: unknown;
      try {
        result = (exportValue as (...args: unknown[]) => unknown)({}, {}, {});
      } catch {
        result = undefined;
      }
      expect(
        isBoundCapabilityOwner(result),
        `direct-imported export \`${exportName}\` must never mint a value isBoundCapabilityOwner accepts`,
      ).toBe(false);
    }
  });

  it('T2 round-2 (R01): package.json exports map declares no subpath under contracts/, so no deep import can reach the module through the package boundary either', () => {
    const packageJson = loadPackageJson();
    const exportKeys = Object.keys(packageJson.exports ?? {});
    expect(exportKeys.some((key) => key.includes('contracts'))).toBe(false);
  });

  it('keeps the public runtime surface limited to the selected helper subpaths', () => {
    const packageJson = loadPackageJson();

    expect(packageJson.exports).toEqual({
      '.': './src/index.ts',
      './types': './src/types.ts',
      './engine': './src/engine.ts',
      './enterprise': './src/enterprise/enterprise.ts',
      './guards/*': './src/guards/*.ts',
      './runtime/agent-handoff': './src/runtime/agent-handoff.ts',
      './runtime/agent-coordination': './src/runtime/agent-coordination.ts',
      './runtime/mandatory-gateway': './src/runtime/mandatory-gateway.ts',
      // LPCI1-WEB-R1: narrow barrel exposing only the self-contained,
      // zero-internal-import receipt envelope and memory tier identity
      // (src/receipt-identity.ts), not the full contracts/ directory. This
      // key intentionally does not contain the substring "contracts", so
      // the round-2 deep-import boundary test above still passes.
      './receipt-identity': './src/receipt-identity.ts',
    });
  });

  it('ships only the bounded files needed by the first-wave guard surface', () => {
    const packageJson = loadPackageJson();

    expect(packageJson.files).toEqual([
      'README.md',
      'src/index.ts',
      'src/types.ts',
      'src/engine.ts',
      'src/enterprise/enterprise.ts',
      'src/guards',
      'src/enterprise',
      'src/runtime/agent-handoff.ts',
      'src/runtime/agent-coordination.ts',
      'src/runtime/mandatory-gateway.ts',
      // LPCI1-WEB-R1: the narrow receipt-identity barrel and the two
      // self-contained contract files it imports (receipt envelope
      // identity and memory tier identity).
      'src/receipt-identity.ts',
      'src/contracts/receipt-envelope.contract.ts',
      'src/contracts/memory-tier.contract.ts',
    ]);
  });
});
