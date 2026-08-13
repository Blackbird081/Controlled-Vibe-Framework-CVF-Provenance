/**
 * T3B Model Gateway constraint projection.
 *
 * A pure local, fail-closed, provider-neutral projection that combines a
 * non-authoritative T3A eligibility projection with repository-owned provider
 * capability metadata. It never resolves a credential, calls a provider,
 * records quota use, or authorizes execution. All four authorization flags are
 * literal false. The T3A projection is treated only as copyable metadata, so a
 * copied or reconstructed matching projection never gains execution authority.
 */

import { isProxy } from "node:util/types";
import {
  isBoundCapabilityOwner,
  readBoundGrantIdentity,
  type CapabilityOwnerHandle,
} from "../../CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract";
import {
  negotiateProviderCapability,
  type CapabilityNegotiationResult,
} from "./provider-capability-negotiation";
import {
  PROVIDER_CAPABILITY_REGISTRY,
} from "./provider-capability-registry";
import type {
  ProviderMethodName,
} from "./provider-method-contract";

export const CADP_CONSTRAINT_PROJECTION_CONTRACT_VERSION = "cvf.cadp.constraintProjection.v1" as const;

/**
 * Repository-owned bounded constraint ceilings. These are validation bounds of
 * the projection contract, not a provider capability registry; the caller may
 * supply a ceiling at or below each bound but may never widen beyond it.
 */
export const CADP_CONSTRAINT_PROJECTION_BOUNDS = Object.freeze({
  costCeilingMax: 1_000_000,
  tokenCeilingMax: 100_000_000,
  requestCeilingMax: 1_000_000,
} as const);

export type CadpConstraintProjectionIssueCode =
  | "MALFORMED_REQUEST"
  | "NOT_A_BOUND_OWNER"
  | "OWNER_IDENTITY_UNAVAILABLE"
  | "MALFORMED_PROJECTION"
  | "PROJECTION_NOT_ELIGIBLE"
  | "PROJECTION_UNRECONCILED"
  | "PROJECTION_GRANT_MISMATCH"
  | "UNKNOWN_PROVIDER"
  | "UNKNOWN_MODEL"
  | "METHOD_NOT_SUPPORTED"
  | "MALFORMED_CONSTRAINTS"
  | "INVALID_CONSTRAINT_FIELD"
  | "CONSTRAINT_EXCEEDS_CONTRACT_BOUNDS";

export interface CadpConstraintProjectionIssue {
  readonly code: string;
  readonly path: string;
  readonly message: string;
}

export type CadpConstraintRetentionPolicy = "NO_RETENTION" | "BOUNDED_RETENTION";
export type CadpConstraintRemoteSideEffectPolicy = "NONE" | "READ_ONLY";
export type CadpConstraintCredentialMode = "REFERENCE_ONLY";

/** Closed provider-neutral constraint object. Every field is a bounded integer
 * or a closed enum; no secret, provider payload, function, symbol, accessor,
 * or cyclic value is accepted. */
export interface CadpConstraintProjectionConstraints {
  readonly costCeiling: number;
  readonly tokenCeiling: number;
  readonly requestCeiling: number;
  readonly retentionPolicy: CadpConstraintRetentionPolicy;
  readonly remoteSideEffectPolicy: CadpConstraintRemoteSideEffectPolicy;
  readonly credentialMode: CadpConstraintCredentialMode;
}

/**
 * The non-authoritative T3A eligibility projection consumed as plain metadata.
 * Structurally compatible with the Execution Plane
 * `CadpCapabilityEligibilityProjection`; declared locally so T3B treats the
 * projection as copyable data rather than a type-bound receipt and does not
 * couple the Model Gateway package root to the Execution Plane module graph.
 */
export interface CadpConstraintProjectionEligibilityInput {
  readonly decision: "ELIGIBLE" | "NOT_ELIGIBLE";
  readonly executionAuthorized: false;
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly assignmentId: string;
  readonly actionId: string;
  readonly reconciled: boolean;
}

/** Strict plain-data, non-Proxy request envelope. The caller supplies only an
 * already bound opaque owner handle, a T3A eligibility projection, a concrete
 * provider/model/method selection, and a closed constraint object. */
export interface CadpConstraintProjectionRequest {
  readonly ownerHandle: CapabilityOwnerHandle;
  readonly projection: CadpConstraintProjectionEligibilityInput;
  readonly providerId: string;
  readonly modelId: string;
  readonly methodName: ProviderMethodName;
  readonly constraints: CadpConstraintProjectionConstraints;
}

export type CadpConstraintProjectionDecision = "SATISFIED" | "BLOCKED";

/** Frozen provider-neutral constraint projection. All four authorization flags
 * are literal false by construction. */
export interface CadpConstraintProjection {
  readonly decision: CadpConstraintProjectionDecision;
  readonly providerId: string;
  readonly modelId: string;
  readonly requestedMethod: ProviderMethodName;
  readonly effectiveMethod: ProviderMethodName;
  readonly supportedMethods: readonly ProviderMethodName[];
  readonly constraints: CadpConstraintProjectionConstraints;
  readonly executionAuthorized: false;
  readonly liveExecutionAuthorized: false;
  readonly providerCallAuthorized: false;
  readonly credentialResolutionAuthorized: false;
}

export interface CadpConstraintProjectionResult {
  readonly valid: boolean;
  readonly issues: readonly CadpConstraintProjectionIssue[];
  readonly projection: CadpConstraintProjection;
}

const REQUEST_KEYS = ["ownerHandle", "projection", "providerId", "modelId", "methodName", "constraints"] as const;
const PROJECTION_KEYS = ["decision", "executionAuthorized", "capabilityId", "capabilityVersion", "assignmentId", "actionId", "reconciled"] as const;
const CONSTRAINT_KEYS = ["costCeiling", "tokenCeiling", "requestCeiling", "retentionPolicy", "remoteSideEffectPolicy", "credentialMode"] as const;
const METHOD_NAMES: readonly ProviderMethodName[] = [
  "complete", "chat", "stream", "tool_call", "reasoning", "json_mode", "vision", "embedding", "receipt",
] as const;
const RETENTION_POLICIES: readonly CadpConstraintRetentionPolicy[] = ["NO_RETENTION", "BOUNDED_RETENTION"] as const;
const REMOTE_SIDE_EFFECT_POLICIES: readonly CadpConstraintRemoteSideEffectPolicy[] = ["NONE", "READ_ONLY"] as const;

function makeIssue(code: CadpConstraintProjectionIssueCode, path: string, message: string): CadpConstraintProjectionIssue {
  return Object.freeze({ code, path, message });
}

function isPlainNonProxyRecord(value: unknown): value is Record<string, unknown> {
  if (value === null || typeof value !== "object") return false;
  if (isProxy(value)) return false;
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

/** Trap-free own enumerable data descriptor read. Never invokes an accessor. */
function ownDataField(owner: unknown, key: string): { readonly present: boolean; readonly value: unknown } {
  if (owner === null || (typeof owner !== "object" && typeof owner !== "function")) {
    return { present: false, value: undefined };
  }
  if (isProxy(owner)) return { present: false, value: undefined };
  const descriptor = Object.getOwnPropertyDescriptor(owner, key);
  if (!descriptor || !descriptor.enumerable || "get" in descriptor || "set" in descriptor) {
    return { present: false, value: undefined };
  }
  return { present: true, value: descriptor.value };
}

interface ExactShapeRead {
  readonly fields?: Record<string, unknown>;
  readonly issues: CadpConstraintProjectionIssue[];
}

/** Exact-shape, non-Proxy, accessor-free, symbol-free plain data reader. */
function readExactShape(
  value: unknown,
  keys: readonly string[],
  path: string,
  malformedCode: CadpConstraintProjectionIssueCode,
): ExactShapeRead {
  if (!isPlainNonProxyRecord(value)) {
    return { issues: [makeIssue(malformedCode, path, "Value must be a non-Proxy plain data object.")] };
  }
  const names = Object.getOwnPropertyNames(value);
  if (
    Object.getOwnPropertySymbols(value).length > 0 ||
    names.length !== keys.length ||
    names.some((name) => !keys.includes(name))
  ) {
    return { issues: [makeIssue(malformedCode, path, "Value has missing or unknown fields.")] };
  }
  const fields: Record<string, unknown> = {};
  for (const key of keys) {
    const field = ownDataField(value, key);
    if (!field.present) {
      return { issues: [makeIssue(malformedCode, `${path}.${key}`, `Field ${key} must be an own enumerable data property.`)] };
    }
    fields[key] = field.value;
  }
  return { fields, issues: [] };
}

function isProviderMethodName(value: unknown): value is ProviderMethodName {
  return typeof value === "string" && (METHOD_NAMES as readonly string[]).includes(value);
}

function readBoundedInteger(
  constraints: Record<string, unknown>,
  key: string,
  maximum: number,
  issues: CadpConstraintProjectionIssue[],
): void {
  const value = constraints[key];
  if (!Number.isSafeInteger(value) || (value as number) < 0) {
    issues.push(makeIssue("INVALID_CONSTRAINT_FIELD", `$.constraints.${key}`, `${key} must be a non-negative safe integer.`));
    return;
  }
  if ((value as number) > maximum) {
    issues.push(makeIssue("CONSTRAINT_EXCEEDS_CONTRACT_BOUNDS", `$.constraints.${key}`, `${key} exceeds the T3B contract-owned bounded ceiling of ${maximum}.`));
  }
}

function emptyConstraints(): CadpConstraintProjectionConstraints {
  return Object.freeze({
    costCeiling: 0,
    tokenCeiling: 0,
    requestCeiling: 0,
    retentionPolicy: "NO_RETENTION",
    remoteSideEffectPolicy: "NONE",
    credentialMode: "REFERENCE_ONLY",
  });
}

function emptyProjection(): CadpConstraintProjection {
  return Object.freeze({
    decision: "BLOCKED",
    providerId: "",
    modelId: "",
    requestedMethod: "complete",
    effectiveMethod: "complete",
    supportedMethods: Object.freeze([]),
    constraints: emptyConstraints(),
    executionAuthorized: false,
    liveExecutionAuthorized: false,
    providerCallAuthorized: false,
    credentialResolutionAuthorized: false,
  });
}

function blockedResult(issues: CadpConstraintProjectionIssue[]): CadpConstraintProjectionResult {
  return Object.freeze({ valid: false, issues: Object.freeze([...issues]), projection: emptyProjection() });
}

/**
 * Evaluates a provider-neutral constraint projection for a T3A-eligible grant.
 *
 * The opaque owner handle authenticates the grant identity; the T3A projection
 * is only non-authoritative metadata that must agree with that identity. The
 * provider/model/method selection is resolved solely through the repository
 * capability registry, and caller constraints may narrow but never widen the
 * repository-owned envelope. No credential, quota, provider, or execution seam
 * is reachable.
 */
export function evaluateCadpConstraintProjection(
  request: CadpConstraintProjectionRequest,
): CadpConstraintProjectionResult {
  const envelope = readExactShape(request as unknown, REQUEST_KEYS, "$.request", "MALFORMED_REQUEST");
  if (!envelope.fields) return blockedResult(envelope.issues);

  const { ownerHandle, projection: projectionValue, providerId, modelId, methodName, constraints: constraintsValue } = envelope.fields;

  if (!isBoundCapabilityOwner(ownerHandle)) {
    return blockedResult([
      makeIssue("NOT_A_BOUND_OWNER", "$.ownerHandle", "Owner handle is not authenticated by the repository owner source."),
    ]);
  }
  const identity = readBoundGrantIdentity(ownerHandle as CapabilityOwnerHandle);
  if (!identity) {
    return blockedResult([
      makeIssue("OWNER_IDENTITY_UNAVAILABLE", "$.ownerHandle", "Bound owner grant identity is unavailable."),
    ]);
  }

  const projectionRead = readExactShape(projectionValue, PROJECTION_KEYS, "$.projection", "MALFORMED_PROJECTION");
  if (!projectionRead.fields) return blockedResult(projectionRead.issues);

  const projection = projectionRead.fields;
  const constraintsRead = readExactShape(constraintsValue, CONSTRAINT_KEYS, "$.constraints", "MALFORMED_CONSTRAINTS");
  if (!constraintsRead.fields) return blockedResult(constraintsRead.issues);

  const constraints = constraintsRead.fields;
  const issues: CadpConstraintProjectionIssue[] = [];

  if (projection.decision !== "ELIGIBLE") {
    issues.push(makeIssue("PROJECTION_NOT_ELIGIBLE", "$.projection.decision", "Projection decision must be ELIGIBLE."));
  }
  if (projection.reconciled !== true) {
    issues.push(makeIssue("PROJECTION_UNRECONCILED", "$.projection.reconciled", "Projection must be reconciled."));
  }
  if (projection.executionAuthorized !== false) {
    issues.push(makeIssue("PROJECTION_NOT_ELIGIBLE", "$.projection.executionAuthorized", "Projection must carry literal executionAuthorized false."));
  }
  if (projection.capabilityId !== identity.capabilityId) {
    issues.push(makeIssue("PROJECTION_GRANT_MISMATCH", "$.projection.capabilityId", "Projection capability does not match the bound grant."));
  }
  if (projection.capabilityVersion !== identity.capabilityVersion) {
    issues.push(makeIssue("PROJECTION_GRANT_MISMATCH", "$.projection.capabilityVersion", "Projection capability version does not match the bound grant."));
  }
  if (projection.assignmentId !== identity.assignmentId) {
    issues.push(makeIssue("PROJECTION_GRANT_MISMATCH", "$.projection.assignmentId", "Projection assignment does not match the bound grant."));
  }
  if (projection.actionId !== identity.actionId) {
    issues.push(makeIssue("PROJECTION_GRANT_MISMATCH", "$.projection.actionId", "Projection action does not match the bound grant."));
  }

  if (typeof providerId !== "string" || !providerId.trim()) {
    issues.push(makeIssue("UNKNOWN_PROVIDER", "$.providerId", "providerId must be a non-empty string."));
  }
  if (typeof modelId !== "string" || !modelId.trim()) {
    issues.push(makeIssue("UNKNOWN_MODEL", "$.modelId", "modelId must be a non-empty string."));
  }
  if (!isProviderMethodName(methodName)) {
    issues.push(makeIssue("METHOD_NOT_SUPPORTED", "$.methodName", "methodName must be a closed provider method name."));
  }

  readBoundedInteger(constraints, "costCeiling", CADP_CONSTRAINT_PROJECTION_BOUNDS.costCeilingMax, issues);
  readBoundedInteger(constraints, "tokenCeiling", CADP_CONSTRAINT_PROJECTION_BOUNDS.tokenCeilingMax, issues);
  readBoundedInteger(constraints, "requestCeiling", CADP_CONSTRAINT_PROJECTION_BOUNDS.requestCeilingMax, issues);

  if (!(RETENTION_POLICIES as readonly string[]).includes(constraints.retentionPolicy as string)) {
    issues.push(makeIssue("INVALID_CONSTRAINT_FIELD", "$.constraints.retentionPolicy", "retentionPolicy must be a closed policy value."));
  }
  if (!(REMOTE_SIDE_EFFECT_POLICIES as readonly string[]).includes(constraints.remoteSideEffectPolicy as string)) {
    issues.push(makeIssue("INVALID_CONSTRAINT_FIELD", "$.constraints.remoteSideEffectPolicy", "remoteSideEffectPolicy must be a closed policy value."));
  }
  if (constraints.credentialMode !== "REFERENCE_ONLY") {
    issues.push(makeIssue("INVALID_CONSTRAINT_FIELD", "$.constraints.credentialMode", "credentialMode must be literal REFERENCE_ONLY."));
  }

  let negotiation: CapabilityNegotiationResult | undefined;
  if (
    typeof providerId === "string" && providerId.trim() &&
    typeof modelId === "string" && modelId.trim() &&
    isProviderMethodName(methodName)
  ) {
    negotiation = negotiateProviderCapability(
      providerId,
      modelId,
      methodName,
      PROVIDER_CAPABILITY_REGISTRY,
    );
    if (negotiation.status === "blocked") {
      if (negotiation.supportedMethods.length === 0) {
        const providerKnown = PROVIDER_CAPABILITY_REGISTRY.some((entry) => entry.providerId === providerId);
        issues.push(makeIssue(
          providerKnown ? "UNKNOWN_MODEL" : "UNKNOWN_PROVIDER",
          "$.providerId/$modelId",
          providerKnown ? "modelId is not present in the repository registry." : "providerId is not present in the repository registry.",
        ));
      } else {
        issues.push(makeIssue("METHOD_NOT_SUPPORTED", "$.methodName", "Requested method is not supported for the selected provider and model."));
      }
    }
  }

  if (issues.length > 0) return blockedResult(issues);

  const settled = negotiation as CapabilityNegotiationResult;
  const supportedMethods = Object.freeze([...settled.supportedMethods] as ProviderMethodName[]);

  const projectionOutput = Object.freeze({
    decision: "SATISFIED",
    providerId: providerId as string,
    modelId: modelId as string,
    requestedMethod: methodName as ProviderMethodName,
    effectiveMethod: settled.effectiveMethod as ProviderMethodName,
    supportedMethods,
    constraints: Object.freeze({
      costCeiling: constraints.costCeiling as number,
      tokenCeiling: constraints.tokenCeiling as number,
      requestCeiling: constraints.requestCeiling as number,
      retentionPolicy: constraints.retentionPolicy as CadpConstraintRetentionPolicy,
      remoteSideEffectPolicy: constraints.remoteSideEffectPolicy as CadpConstraintRemoteSideEffectPolicy,
      credentialMode: "REFERENCE_ONLY",
    }),
    executionAuthorized: false,
    liveExecutionAuthorized: false,
    providerCallAuthorized: false,
    credentialResolutionAuthorized: false,
  } satisfies CadpConstraintProjection);

  return Object.freeze({ valid: true, issues: Object.freeze([]), projection: projectionOutput });
}

export class CadpConstraintProjectionContract {
  evaluate(request: CadpConstraintProjectionRequest): CadpConstraintProjectionResult {
    return evaluateCadpConstraintProjection(request);
  }
}

export function createCadpConstraintProjectionContract(): CadpConstraintProjectionContract {
  return new CadpConstraintProjectionContract();
}
