import { describe, expect, it } from 'vitest';
import {
  CAPABILITY_OWNER_BINDING_CONTRACT_VERSION,
  isBoundCapabilityOwner,
  readBoundArtifact,
  readBoundGrantIdentity,
  reconcileGrantWithObservation,
  type CapabilityExecutionObservationInput,
  type CapabilityOwnerHandle,
} from './capability-owner-binding.contract';
import * as ownerBindingModule from './capability-owner-binding.contract';
import * as contractsBarrel from './index';

/**
 * Round-4 re-review repair (final narrow cleanup, R12). This file tests
 * production's actual exported functions directly. There is no
 * test-double, no parallel implementation, no private registry, and no
 * mint/register/bind or positive-owner fixture anywhere in this
 * repository: the round-2 `capability-owner-binding.test-double.ts` file
 * was deleted (R10) because it was not among the work order's literal 11
 * allowed paths, and round 4 removed the last of production's unreachable
 * private state (`BOUND_OWNERS`, `OWNER_RECORDS`,
 * `CapabilityOwnerGrantRecord`) so that `isBoundCapabilityOwner`,
 * `readBoundArtifact`, `readBoundGrantIdentity`, and
 * `reconcileGrantWithObservation` now implement their permanent
 * fail-closed result directly, with no state to check and no dead branch
 * below it. This tranche is correctly and permanently blocked on the
 * absence of a real owner, so there is no genuine positive path to test.
 *
 * Every test below exercises `capability-owner-binding.contract.ts`'s own
 * exported functions against handle-shaped values a real caller could
 * actually construct (forged plain objects, spread copies, JSON round
 * trips, prototype tricks, casts) and confirms the permanent fail-closed
 * result. R02/R04/R05/R06/R07 grant-validation and reconciliation rules
 * are NOT tested here, because production contains no code path that
 * could ever exercise them (no mint function exists to produce a bound
 * handle in the first place); those rules are `BLOCKED_SOURCE_NOT_FOUND` /
 * `NOT_EXECUTABLE_IN_CURRENT_SCOPE` in this hermetic scope, not proven by
 * any implementation, parallel or otherwise.
 */

const OBSERVATION_SHAPE_ANY_REAL_CALLER_COULD_SUPPLY: CapabilityExecutionObservationInput = {
  workOrderId: 'wo-1', workOrderVersion: '1.0.0',
  capabilityId: 'cap-1', capabilityVersion: '1.0.0',
  assignmentId: 'assignment-1', actionId: 'read',
  transport: 'internal', resourceRef: 'resource-1',
  credentialReference: 'secretref:cred-1',
  invocationId: 'invocation-1', retryOrdinal: 0,
  evaluatedAt: '2026-08-13T01:00:00Z',
};

describe('CVF capability owner binding (production module: permanent fail-closed contract, no parallel implementation)', () => {
  it('exports no mint/register/bind function of any kind, under any name', () => {
    const productionModule = ownerBindingModule as unknown as Record<string, unknown>;
    expect(productionModule.bindNamedCapabilityOwner).toBeUndefined();
    expect(productionModule.bindNamedCapabilityOwner_TEST_ONLY_INTERNAL_BINDER).toBeUndefined();
    expect(productionModule.bindNamedCapabilityOwnerForTest).toBeUndefined();
    for (const [exportName, exportValue] of Object.entries(productionModule)) {
      if (typeof exportValue !== 'function') continue;
      // Every exported function must be consume-only: calling it with any
      // attacker-controlled input must never produce a value
      // isBoundCapabilityOwner accepts.
      let result: unknown;
      try {
        result = (exportValue as (...args: unknown[]) => unknown)({}, {}, {});
      } catch {
        result = undefined;
      }
      expect(
        isBoundCapabilityOwner(result),
        `exported function \`${exportName}\` must never mint a value isBoundCapabilityOwner accepts`,
      ).toBe(false);
    }
  });

  it('the contracts barrel re-exports no mint/register/bind function either', () => {
    const barrel = contractsBarrel as unknown as Record<string, unknown>;
    expect(barrel.bindNamedCapabilityOwner).toBeUndefined();
    expect(barrel.bindNamedCapabilityOwner_TEST_ONLY_INTERNAL_BINDER).toBeUndefined();
    expect(barrel.bindNamedCapabilityOwnerForTest).toBeUndefined();
  });

  it('package.json exports map declares no subpath under contracts/, so no deep import can reach this module through the package boundary', async () => {
    const { readFileSync } = await import('node:fs');
    const packageUrl = new URL('../../package.json', import.meta.url);
    const packageJson = JSON.parse(readFileSync(packageUrl, 'utf8')) as { exports?: Record<string, string> };
    const exportKeys = Object.keys(packageJson.exports ?? {});
    expect(exportKeys.some((key) => key.includes('contracts'))).toBe(false);
  });

  it('CAPABILITY_OWNER_BINDING_CONTRACT_VERSION is exported and stable', () => {
    expect(CAPABILITY_OWNER_BINDING_CONTRACT_VERSION).toBe('cvf.cadp.ownerBinding.v2');
  });

  // === isBoundCapabilityOwner: unconditional false for every constructible value ===

  it('isBoundCapabilityOwner rejects a plain object shaped exactly like a handle', () => {
    const forged: unknown = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION };
    expect(isBoundCapabilityOwner(forged)).toBe(false);
  });

  it('isBoundCapabilityOwner rejects a frozen plain object shaped like a handle', () => {
    const forged: unknown = Object.freeze({ contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION });
    expect(isBoundCapabilityOwner(forged)).toBe(false);
  });

  it('isBoundCapabilityOwner rejects a JSON.parse(JSON.stringify(...)) round trip of a handle-shaped object', () => {
    const roundTripped: unknown = JSON.parse(JSON.stringify({ contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION }));
    expect(isBoundCapabilityOwner(roundTripped)).toBe(false);
  });

  it('isBoundCapabilityOwner rejects a value cast with `as CapabilityOwnerHandle`', () => {
    const cast = ({} as unknown) as CapabilityOwnerHandle;
    expect(isBoundCapabilityOwner(cast)).toBe(false);
  });

  it('isBoundCapabilityOwner rejects Object.create(handleShapedObject) style prototype forgery', () => {
    const base = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION };
    const prototypeForgery: unknown = Object.create(base);
    expect(isBoundCapabilityOwner(prototypeForgery)).toBe(false);
  });

  it('isBoundCapabilityOwner rejects a spread copy of a handle-shaped object', () => {
    const base = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION };
    const copy: unknown = { ...base };
    expect(isBoundCapabilityOwner(copy)).toBe(false);
  });

  it('isBoundCapabilityOwner rejects a Proxy wrapping a handle-shaped object without invoking any trap', () => {
    let trapCalls = 0;
    const proxied = new Proxy({ contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION }, {
      get() { trapCalls += 1; return undefined; },
      getOwnPropertyDescriptor() { trapCalls += 1; return undefined; },
      getPrototypeOf() { trapCalls += 1; return null; },
    });
    expect(isBoundCapabilityOwner(proxied)).toBe(false);
    expect(trapCalls).toBe(0);
  });

  it('isBoundCapabilityOwner rejects a revoked Proxy without throwing an incidental error', () => {
    const { proxy, revoke } = Proxy.revocable({ contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION }, {});
    revoke();
    expect(() => isBoundCapabilityOwner(proxy)).not.toThrow();
    expect(isBoundCapabilityOwner(proxy)).toBe(false);
  });

  it('isBoundCapabilityOwner rejects primitives, null, arrays and functions', () => {
    expect(isBoundCapabilityOwner(null)).toBe(false);
    expect(isBoundCapabilityOwner(undefined)).toBe(false);
    expect(isBoundCapabilityOwner('cvf.cadp.ownerBinding.v2')).toBe(false);
    expect(isBoundCapabilityOwner(42)).toBe(false);
    expect(isBoundCapabilityOwner([])).toBe(false);
    expect(isBoundCapabilityOwner(() => undefined)).toBe(false);
  });

  it('isBoundCapabilityOwner rejects two independently forged handle-shaped objects identically (no first-mover advantage)', () => {
    const first: unknown = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION };
    const second: unknown = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION };
    expect(isBoundCapabilityOwner(first)).toBe(false);
    expect(isBoundCapabilityOwner(second)).toBe(false);
  });

  // === readBoundArtifact: unconditional undefined ===

  it('readBoundArtifact returns undefined for a forged handle-shaped object', () => {
    const forged = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION } as unknown as CapabilityOwnerHandle;
    expect(readBoundArtifact(forged, 'any-ref')).toBeUndefined();
  });

  it('readBoundArtifact returns undefined regardless of the ref queried', () => {
    const forged = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION } as unknown as CapabilityOwnerHandle;
    for (const ref of ['receipt-1', 'wo-1', '', 'nonexistent']) {
      expect(readBoundArtifact(forged, ref)).toBeUndefined();
    }
  });

  it('readBoundArtifact returns undefined for a cast empty object', () => {
    const cast = ({} as unknown) as CapabilityOwnerHandle;
    expect(readBoundArtifact(cast, 'receipt-1')).toBeUndefined();
  });

  // === readBoundGrantIdentity: unconditional undefined ===

  it('readBoundGrantIdentity returns undefined for a forged handle-shaped object', () => {
    const forged = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION } as unknown as CapabilityOwnerHandle;
    expect(readBoundGrantIdentity(forged)).toBeUndefined();
  });

  it('readBoundGrantIdentity returns undefined for a cast empty object', () => {
    const cast = ({} as unknown) as CapabilityOwnerHandle;
    expect(readBoundGrantIdentity(cast)).toBeUndefined();
  });

  // === reconcileGrantWithObservation: unconditional NOT_A_BOUND_OWNER ===

  it('reconcileGrantWithObservation returns NOT_A_BOUND_OWNER for a forged handle-shaped object, for any observation content', () => {
    const forged = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION } as unknown as CapabilityOwnerHandle;
    const result = reconcileGrantWithObservation(forged, OBSERVATION_SHAPE_ANY_REAL_CALLER_COULD_SUPPLY);
    expect(result.valid).toBe(false);
    expect(result.issues).toEqual([
      { code: 'NOT_A_BOUND_OWNER', path: '$.handle', message: expect.any(String) },
    ]);
    expect(result.data.reconciled).toBe(false);
  });

  it('reconcileGrantWithObservation returns NOT_A_BOUND_OWNER for a cast empty object', () => {
    const cast = ({} as unknown) as CapabilityOwnerHandle;
    const result = reconcileGrantWithObservation(cast, OBSERVATION_SHAPE_ANY_REAL_CALLER_COULD_SUPPLY);
    expect(result.valid).toBe(false);
    expect(result.issues.every(({ code }) => code === 'NOT_A_BOUND_OWNER')).toBe(true);
  });

  it('reconcileGrantWithObservation returns NOT_A_BOUND_OWNER regardless of how well-formed the observation is', () => {
    const forged = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION } as unknown as CapabilityOwnerHandle;
    const wellFormed = reconcileGrantWithObservation(forged, OBSERVATION_SHAPE_ANY_REAL_CALLER_COULD_SUPPLY);
    const malformed = reconcileGrantWithObservation(forged, {} as unknown as CapabilityExecutionObservationInput);
    expect(wellFormed.valid).toBe(false);
    expect(malformed.valid).toBe(false);
    expect(wellFormed.issues).toEqual(malformed.issues);
  });

  it('reconcileGrantWithObservation never mutates its inputs', () => {
    const forged = Object.freeze({ contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION }) as unknown as CapabilityOwnerHandle;
    const observation = Object.freeze({ ...OBSERVATION_SHAPE_ANY_REAL_CALLER_COULD_SUPPLY });
    expect(() => reconcileGrantWithObservation(forged, observation)).not.toThrow();
  });

  // === End-to-end: the exact F11 self-attestation attack shape is rejected ===

  it('the exact caller-self-attestation attack shape (forged handle -> reconcile -> read artifact) is rejected end to end', () => {
    const forged = { contractVersion: CAPABILITY_OWNER_BINDING_CONTRACT_VERSION } as unknown as CapabilityOwnerHandle;
    expect(isBoundCapabilityOwner(forged)).toBe(false);
    const reconciled = reconcileGrantWithObservation(forged, OBSERVATION_SHAPE_ANY_REAL_CALLER_COULD_SUPPLY);
    expect(reconciled.valid).toBe(false);
    expect(readBoundArtifact(forged, 'receipt-1')).toBeUndefined();
    expect(readBoundGrantIdentity(forged)).toBeUndefined();
  });
});
