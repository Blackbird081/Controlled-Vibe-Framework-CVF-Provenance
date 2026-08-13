/**
 * CVF CADP-AI-T2 capability owner binding and grant-observation reconciliation.
 *
 * Round-4 re-review repair (final narrow cleanup). The round-4 independent
 * adversarial review's amendment accepted the round-3 security-boundary
 * correction as bounded evidence: no production mint exists, handles from
 * caller-controlled values are rejected under hostile inputs, and every
 * owner-requiring evidence rank fails with `EVIDENCE_SOURCE_NOT_FOUND`. It
 * returned the tranche for one final narrow cleanup (R12) because:
 *
 * - R12 (MEDIUM): the round-3 module still declared a permanently empty
 *   `WeakSet` (`BOUND_OWNERS`), a permanently empty `WeakMap`
 *   (`OWNER_RECORDS`), a `CapabilityOwnerGrantRecord` type, and
 *   artifact/grant lookup logic and post-authentication branches inside
 *   `readBoundArtifact`, `readBoundGrantIdentity`, and
 *   `reconcileGrantWithObservation` that could never execute - the exact
 *   "unreachable production weight" R11 required removing, restated under
 *   new field/type names rather than actually removed. This file now
 *   implements the current contract directly, with no private state to
 *   declare and no dead branch to justify: `isBoundCapabilityOwner` always
 *   returns `false`; `readBoundArtifact` and `readBoundGrantIdentity`
 *   always return `undefined`; `reconcileGrantWithObservation` always
 *   returns the explicit `NOT_A_BOUND_OWNER` / `BLOCKED_SOURCE_NOT_FOUND`
 *   result. There is no `WeakSet`, no `WeakMap`, no record type, and no
 *   lookup logic anywhere in this file, because there is nothing for any
 *   of that machinery to ever store or retrieve: no function in this file,
 *   or any other file in this repository, can ever produce a genuine
 *   bound owner.
 *
 * Every owner-dependent behavior this module's earlier rounds discussed
 * (grant-version reconciliation, credential-reference validation,
 * trace/receipt-linkage checks, invocation/retry/replay bookkeeping,
 * artifact/grant-identity projection) is `BLOCKED_SOURCE_NOT_FOUND` /
 * `NOT_EXECUTABLE_IN_CURRENT_SCOPE` in this hermetic scope, not `CLOSED`:
 * no code in this file implements them, and this round does not implement
 * a parallel/test-double module, a private registry, or any other
 * mechanism to claim otherwise. They remain a specification for whatever
 * module a future, separately authorized T3+ tranche writes when it wires
 * a real source-verified owner registry into new code - not evidence this
 * tranche can claim today.
 *
 * `isBoundCapabilityOwner` returns `false` for every value any real caller
 * can construct, unconditionally and directly - there is no state to
 * check membership against. `readBoundArtifact` and `readBoundGrantIdentity`
 * therefore always return `undefined`, directly, with no lookup attempted.
 * `reconcileGrantWithObservation` therefore always returns
 * `{ valid: false, issues: [{ code: 'NOT_A_BOUND_OWNER', ... }] }`,
 * directly, with no branch below that result. `validateCompatibilityEvidence`
 * (in `capability-admission-distribution-profile.contract.ts`) therefore
 * fails closed with `EVIDENCE_SOURCE_NOT_FOUND` (`BLOCKED_SOURCE_NOT_FOUND`)
 * for every rank>=2 evidence record and every real caller, permanently. F11
 * (`F11_RESIDUAL_OPEN_CALLER_SELF_ATTESTATION`) remains open pending
 * independent review and any future, separately authorized T3+ owner-
 * registry work; this module must never be described as closing F11 on
 * its own. The correct T2 state, per the governing work order, is
 * `BLOCKED_SOURCE_NOT_FOUND`, not `COMPLETE_PENDING_REVIEW` and not
 * `CLOSED`. Passing structural gates (typecheck, tests, worker-return fast
 * gate) confirm this file's shape and behavior; they are not F11-closure
 * or T2-acceptance evidence.
 *
 * Every exported symbol below is retained only because
 * `capability-admission-distribution-profile.contract.ts`'s public API,
 * `contracts/index.ts`'s barrel re-exports, or this module's own test file
 * requires it for compatibility - not because any of it is load-bearing
 * production logic.
 */

export const CAPABILITY_OWNER_BINDING_CONTRACT_VERSION = 'cvf.cadp.ownerBinding.v2' as const;

export type CapabilityOwnerBindingIssueCode =
  | 'INVALID_FIELD'
  | 'MALFORMED_INPUT_SHAPE'
  | 'RAW_SECRET_INCLUDED'
  | 'GRANT_MISMATCH'
  | 'NOT_A_BOUND_OWNER'
  | 'EVALUATION_NOT_YET_VALID'
  | 'EVALUATION_EXPIRED'
  | 'INVOCATION_LIMIT_EXCEEDED'
  | 'RETRY_LIMIT_EXCEEDED'
  | 'TRACE_LINKAGE_MISSING'
  | 'RECEIPT_LINKAGE_MISSING'
  | 'DUPLICATE_INVOCATION_REJECTED'
  | 'ARTIFACT_NOT_BOUND'
  | 'CREDENTIAL_REFERENCE_INVALID';

export interface CapabilityOwnerBindingIssue {
  readonly code: CapabilityOwnerBindingIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface CapabilityOwnerBindingResult<TData = Readonly<Record<string, unknown>>> {
  readonly valid: boolean;
  readonly issues: readonly CapabilityOwnerBindingIssue[];
  readonly data: TData;
}

/**
 * Named evidence-artifact classes this module's compatibility types
 * reference. Retained only as a type: no function in this file ever
 * constructs or returns a genuine value carrying this type.
 */
export type BoundArtifactType = 'receipt' | 'work_order' | 'review' | 'freeze';

/**
 * `CapabilityOwnerHandle` is intentionally an empty, opaque public shape.
 * No function in this file, or any other file in this repository, can
 * ever produce a value of this type that `isBoundCapabilityOwner` accepts:
 * there is no private state anywhere in this module for such a value to
 * be registered into. The type is exported only so a future, separately
 * authorized T3+ owner registry can describe the shape it will eventually
 * return, and so this module's consume-only functions have a parameter
 * type to declare for compatibility with their existing callers.
 */
export interface CapabilityOwnerHandle {
  readonly contractVersion: typeof CAPABILITY_OWNER_BINDING_CONTRACT_VERSION;
}

/**
 * Direct implementation of the current contract: this file has no mint,
 * bind, or registration function, and no private state (no `WeakSet`, no
 * `WeakMap`, no record type) for one to populate. `value` is intentionally
 * unused; the parameter and its type exist only so this function's
 * signature stays compatible with every existing caller.
 */
export function isBoundCapabilityOwner(value: unknown): value is CapabilityOwnerHandle {
  void value;
  return false;
}

export interface BoundArtifactProjection {
  readonly ref: string;
  readonly artifactType: BoundArtifactType;
  readonly owner: string;
}

/**
 * Direct implementation of the current contract: `BLOCKED_SOURCE_NOT_
 * FOUND` / `NOT_EXECUTABLE_IN_CURRENT_SCOPE`. `handle` and `ref` are
 * intentionally unused; the parameters exist only so this function's
 * signature stays compatible with every existing caller.
 */
export function readBoundArtifact(
  handle: CapabilityOwnerHandle,
  ref: string,
): BoundArtifactProjection | undefined {
  void handle;
  void ref;
  return undefined;
}

export interface CapabilityOwnerGrantProjection {
  readonly workOrderId: string;
  readonly workOrderVersion: string;
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly assignmentId: string;
  readonly actionId: string;
  readonly grantHash: string;
}

/**
 * Direct implementation of the current contract: `BLOCKED_SOURCE_NOT_
 * FOUND` / `NOT_EXECUTABLE_IN_CURRENT_SCOPE`. `handle` is intentionally
 * unused; the parameter exists only so this function's signature stays
 * compatible with every existing caller.
 */
export function readBoundGrantIdentity(handle: CapabilityOwnerHandle): CapabilityOwnerGrantProjection | undefined {
  void handle;
  return undefined;
}

export interface CapabilityExecutionObservationInput {
  readonly workOrderId: string;
  readonly workOrderVersion: string;
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly assignmentId: string;
  readonly actionId: string;
  readonly transport: string;
  readonly resourceRef: string;
  readonly credentialReference: string;
  readonly invocationId: string;
  readonly retryOrdinal: number;
  readonly evaluatedAt: string;
}

/**
 * Direct implementation of the current contract: always returns the
 * explicit blocked result. `handle` and `observation` are intentionally
 * unused; the parameters exist only so this function's signature stays
 * compatible with every existing caller. Grant-version reconciliation,
 * credential-reference validation, trace/receipt-linkage checks, and
 * invocation/retry/replay bookkeeping are not implemented in this file:
 * no production code path can ever reach a branch that would exercise
 * them, and this round does not carry that logic here as unreachable
 * weight or claim those behaviors closed via any implementation.
 */
export function reconcileGrantWithObservation(
  handle: CapabilityOwnerHandle,
  observation: CapabilityExecutionObservationInput,
): CapabilityOwnerBindingResult<{ readonly reconciled: boolean }> {
  void handle;
  void observation;
  return {
    valid: false,
    issues: [{ code: 'NOT_A_BOUND_OWNER', path: '$.handle', message: 'BLOCKED_SOURCE_NOT_FOUND: no authenticated capability owner seam is reachable from this hermetic package.' }],
    data: { reconciled: false },
  };
}
