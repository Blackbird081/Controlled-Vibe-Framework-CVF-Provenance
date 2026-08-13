import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { beforeAll, describe, expect, it } from "vitest";
import {
  CADP_CONSTRAINT_PROJECTION_BOUNDS,
  CADP_CONSTRAINT_PROJECTION_CONTRACT_VERSION,
  evaluateCadpConstraintProjection,
  type CadpConstraintProjectionConstraints,
  type CadpConstraintProjectionEligibilityInput,
  type CadpConstraintProjectionIssue,
  type CadpConstraintProjectionRequest,
} from "../src/cadp.constraint.projection.contract";
import { bindCommittedCapabilityOwnerGrant, type CapabilityOwnerHandle } from "../../CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract";

const GRANT_REF = "governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v2.json";
const CAPABILITY_ID = "cvf.cadp.owner-bound-evidence";
const CAPABILITY_VERSION = "v3";
const GRANT_ASSIGNMENT_ID = "cadp-ai-t2a-owner-binding";
const ACTION_ID = "validateCompatibilityEvidence";

const PROVIDER_ID = "alibaba";
const MODEL_ID = "qwen-turbo";
const METHOD_NAME = "complete" as const;

let handle: CapabilityOwnerHandle;

function projection(overrides: Partial<CadpConstraintProjectionEligibilityInput> = {}): CadpConstraintProjectionEligibilityInput {
  return {
    decision: "ELIGIBLE",
    executionAuthorized: false,
    capabilityId: CAPABILITY_ID,
    capabilityVersion: CAPABILITY_VERSION,
    assignmentId: GRANT_ASSIGNMENT_ID,
    actionId: ACTION_ID,
    reconciled: true,
    ...overrides,
  };
}

function constraints(overrides: Partial<CadpConstraintProjectionConstraints> = {}): CadpConstraintProjectionConstraints {
  return {
    costCeiling: 5_000,
    tokenCeiling: 2_000_000,
    requestCeiling: 1_000,
    retentionPolicy: "BOUNDED_RETENTION",
    remoteSideEffectPolicy: "READ_ONLY",
    credentialMode: "REFERENCE_ONLY",
    ...overrides,
  };
}

function request(overrides: Partial<CadpConstraintProjectionRequest> = {}): CadpConstraintProjectionRequest {
  return {
    ownerHandle: handle,
    projection: projection(),
    providerId: PROVIDER_ID,
    modelId: MODEL_ID,
    methodName: METHOD_NAME,
    constraints: constraints(),
    ...overrides,
  };
}

beforeAll(() => {
  const binding = bindCommittedCapabilityOwnerGrant(GRANT_REF);
  expect(binding.valid).toBe(true);
  handle = binding.data.handle!;
});

describe("cadp model gateway constraint projection", () => {
  it("exposes its contract version and bounded ceilings", () => {
    expect(CADP_CONSTRAINT_PROJECTION_CONTRACT_VERSION).toBe("cvf.cadp.constraintProjection.v1");
    expect(CADP_CONSTRAINT_PROJECTION_BOUNDS.costCeilingMax).toBeGreaterThan(0);
    expect(CADP_CONSTRAINT_PROJECTION_BOUNDS.tokenCeilingMax).toBeGreaterThan(0);
    expect(CADP_CONSTRAINT_PROJECTION_BOUNDS.requestCeilingMax).toBeGreaterThan(0);
  });

  it("produces a frozen SATISFIED projection with four literal false flags for a genuine matching owner and eligible T3A projection", () => {
    const result = evaluateCadpConstraintProjection(request());
    expect(result.valid).toBe(true);
    expect(result.issues).toEqual([]);
    expect(result.projection.decision).toBe("SATISFIED");
    expect(result.projection.providerId).toBe(PROVIDER_ID);
    expect(result.projection.modelId).toBe(MODEL_ID);
    expect(result.projection.requestedMethod).toBe("complete");
    expect(result.projection.effectiveMethod).toBe("complete");
    expect(result.projection.supportedMethods).toContain("complete");
    expect(result.projection.constraints.costCeiling).toBe(5_000);
    expect(result.projection.constraints.credentialMode).toBe("REFERENCE_ONLY");
    expect(result.projection.executionAuthorized).toBe(false);
    expect(result.projection.liveExecutionAuthorized).toBe(false);
    expect(result.projection.providerCallAuthorized).toBe(false);
    expect(result.projection.credentialResolutionAuthorized).toBe(false);
  });

  it("treats a copied or reconstructed matching T3A projection as copyable metadata but never grants it authority", () => {
    const copies: unknown[] = [
      { ...projection() },
      JSON.parse(JSON.stringify(projection())),
    ];
    for (const copied of copies) {
      const result = evaluateCadpConstraintProjection(request({ projection: copied as CadpConstraintProjectionEligibilityInput }));
      expect(result.valid).toBe(true);
      expect(result.projection.decision).toBe("SATISFIED");
      expect(result.projection.executionAuthorized).toBe(false);
      expect(result.projection.liveExecutionAuthorized).toBe(false);
      expect(result.projection.providerCallAuthorized).toBe(false);
      expect(result.projection.credentialResolutionAuthorized).toBe(false);
    }
  });

  it("rejects forged, copied, serialized, proxied, revoked, and absent owner handles", () => {
    const forgedHandles: unknown[] = [
      { contractVersion: "cvf.cadp.ownerBinding.v3" },
      { ...handle },
      JSON.parse(JSON.stringify(handle)),
      Object.create(handle),
    ];
    for (const forged of forgedHandles) {
      const result = evaluateCadpConstraintProjection(request({ ownerHandle: forged as CapabilityOwnerHandle }));
      expect(result.valid).toBe(false);
      expect(result.issues.some((issue) => issue.code === "NOT_A_BOUND_OWNER")).toBe(true);
      expect(result.projection.executionAuthorized).toBe(false);
    }
    const proxied = new Proxy(handle, {});
    const proxiedResult = evaluateCadpConstraintProjection(request({ ownerHandle: proxied as CapabilityOwnerHandle }));
    expect(proxiedResult.valid).toBe(false);
    expect(proxiedResult.issues.some((issue) => issue.code === "NOT_A_BOUND_OWNER")).toBe(true);

    const { proxy, revoke } = Proxy.revocable(handle, {});
    revoke();
    const revoked = evaluateCadpConstraintProjection(request({ ownerHandle: proxy as CapabilityOwnerHandle }));
    expect(revoked.valid).toBe(false);

    const absent = evaluateCadpConstraintProjection(request({ ownerHandle: undefined as unknown as CapabilityOwnerHandle }));
    expect(absent.valid).toBe(false);
    expect(absent.issues.some((issue) => issue.code === "NOT_A_BOUND_OWNER")).toBe(true);
  });

  it("rejects a projection whose identity does not match the authentic owner grant", () => {
    const mismatches: Array<Partial<CadpConstraintProjectionEligibilityInput>> = [
      { capabilityId: "cvf.cadp.unrelated" },
      { capabilityVersion: "v99" },
      { assignmentId: "caller-selected-assignment" },
      { actionId: "unrelated-action" },
    ];
    for (const mismatch of mismatches) {
      const result = evaluateCadpConstraintProjection(request({ projection: projection(mismatch) }));
      expect(result.valid).toBe(false);
      expect(result.issues.some((issue) => issue.code === "PROJECTION_GRANT_MISMATCH")).toBe(true);
    }
  });

  it("fails closed on a non-ELIGIBLE, unreconciled, or execution-authorized projection", () => {
    const notEligible = evaluateCadpConstraintProjection(request({
      projection: projection({ decision: "NOT_ELIGIBLE" }),
    }));
    expect(notEligible.valid).toBe(false);
    expect(notEligible.issues.some((issue) => issue.code === "PROJECTION_NOT_ELIGIBLE")).toBe(true);

    const unreconciled = evaluateCadpConstraintProjection(request({
      projection: projection({ reconciled: false }),
    }));
    expect(unreconciled.valid).toBe(false);
    expect(unreconciled.issues.some((issue) => issue.code === "PROJECTION_UNRECONCILED")).toBe(true);

    const executionAuthorized = evaluateCadpConstraintProjection(request({
      projection: projection({ executionAuthorized: true as false }),
    }));
    expect(executionAuthorized.valid).toBe(false);
    expect(executionAuthorized.projection.executionAuthorized).toBe(false);
  });

  it("rejects a malformed, extra-field, or secret-shaped request envelope", () => {
    const secretShaped = { ...request(), rawSecret: "sk-live-secret-token" };
    const result = evaluateCadpConstraintProjection(secretShaped as unknown as CadpConstraintProjectionRequest);
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === "MALFORMED_REQUEST")).toBe(true);
  });

  it("rejects an extra-field or accessor-carrying projection", () => {
    const extraField = { ...projection(), rawSecret: "sk-secret" };
    const extraResult = evaluateCadpConstraintProjection(request({ projection: extraField as unknown as CadpConstraintProjectionEligibilityInput }));
    expect(extraResult.valid).toBe(false);
    expect(extraResult.issues.some((issue) => issue.code === "MALFORMED_PROJECTION")).toBe(true);

    const accessorProjection: Record<string, unknown> = { ...projection() };
    Object.defineProperty(accessorProjection, "capabilityId", {
      enumerable: true,
      get: () => CAPABILITY_ID,
    });
    const accessorResult = evaluateCadpConstraintProjection(request({ projection: accessorProjection as unknown as CadpConstraintProjectionEligibilityInput }));
    expect(accessorResult.valid).toBe(false);
    expect(accessorResult.issues.some((issue) => issue.code === "MALFORMED_PROJECTION")).toBe(true);
  });

  it("rejects a Proxy request envelope", () => {
    const proxied = new Proxy(request(), {});
    const result = evaluateCadpConstraintProjection(proxied as unknown as CadpConstraintProjectionRequest);
    expect(result.valid).toBe(false);
    expect(result.issues.some((issue) => issue.code === "MALFORMED_REQUEST")).toBe(true);
  });

  it("rejects cyclic input in the request and constraint object", () => {
    const cyclicRequest: Record<string, unknown> = { ...request() };
    cyclicRequest.self = cyclicRequest;
    const cyclicRequestResult = evaluateCadpConstraintProjection(cyclicRequest as unknown as CadpConstraintProjectionRequest);
    expect(cyclicRequestResult.valid).toBe(false);
    expect(cyclicRequestResult.issues.some((issue) => issue.code === "MALFORMED_REQUEST")).toBe(true);

    const cyclicConstraints: Record<string, unknown> = {};
    cyclicConstraints.self = cyclicConstraints;
    const cyclicConstraintsResult = evaluateCadpConstraintProjection(request({
      constraints: cyclicConstraints as unknown as CadpConstraintProjectionConstraints,
    }));
    expect(cyclicConstraintsResult.valid).toBe(false);
    expect(cyclicConstraintsResult.issues.some((issue) => issue.code === "MALFORMED_CONSTRAINTS")).toBe(true);
  });

  it("fails closed on unknown provider, model, and method", () => {
    const unknownProvider = evaluateCadpConstraintProjection(request({ providerId: "bogus-provider" }));
    expect(unknownProvider.valid).toBe(false);
    expect(unknownProvider.issues.some((issue) => issue.code === "UNKNOWN_PROVIDER")).toBe(true);

    const unknownModel = evaluateCadpConstraintProjection(request({ providerId: "alibaba", modelId: "bogus-model" }));
    expect(unknownModel.valid).toBe(false);
    expect(unknownModel.issues.some((issue) => issue.code === "UNKNOWN_MODEL")).toBe(true);

    const unknownMethod = evaluateCadpConstraintProjection(request({
      providerId: "alibaba",
      modelId: "qwen-vl-plus",
      methodName: "complete",
    }));
    expect(unknownMethod.valid).toBe(false);
    expect(unknownMethod.issues.some((issue) => issue.code === "METHOD_NOT_SUPPORTED")).toBe(true);
  });

  it("fails closed when caller-supplied constraints exceed the T3B contract-owned bounded envelope", () => {
    const widenCost = evaluateCadpConstraintProjection(request({
      constraints: constraints({ costCeiling: CADP_CONSTRAINT_PROJECTION_BOUNDS.costCeilingMax + 1 }),
    }));
    expect(widenCost.valid).toBe(false);
    expect(widenCost.issues.some((issue) => issue.code === "CONSTRAINT_EXCEEDS_CONTRACT_BOUNDS")).toBe(true);

    const widenToken = evaluateCadpConstraintProjection(request({
      constraints: constraints({ tokenCeiling: CADP_CONSTRAINT_PROJECTION_BOUNDS.tokenCeilingMax + 1 }),
    }));
    expect(widenToken.valid).toBe(false);
    expect(widenToken.issues.some((issue) => issue.code === "CONSTRAINT_EXCEEDS_CONTRACT_BOUNDS")).toBe(true);

    const widenRequest = evaluateCadpConstraintProjection(request({
      constraints: constraints({ requestCeiling: CADP_CONSTRAINT_PROJECTION_BOUNDS.requestCeilingMax + 1 }),
    }));
    expect(widenRequest.valid).toBe(false);
    expect(widenRequest.issues.some((issue) => issue.code === "CONSTRAINT_EXCEEDS_CONTRACT_BOUNDS")).toBe(true);
  });

  it("rejects caller-supplied capability widening and provider-specific payload fields in constraints", () => {
    const capabilityWidening = { ...constraints(), supportedMethods: ["complete", "stream", "tool_call"] };
    const wideningResult = evaluateCadpConstraintProjection(request({
      constraints: capabilityWidening as unknown as CadpConstraintProjectionConstraints,
    }));
    expect(wideningResult.valid).toBe(false);
    expect(wideningResult.issues.some((issue) => issue.code === "MALFORMED_CONSTRAINTS")).toBe(true);

    const providerPayload = { ...constraints(), headers: { authorization: "Bearer x" }, requestBody: { model: "qwen-turbo" } };
    const payloadResult = evaluateCadpConstraintProjection(request({
      constraints: providerPayload as unknown as CadpConstraintProjectionConstraints,
    }));
    expect(payloadResult.valid).toBe(false);
    expect(payloadResult.issues.some((issue) => issue.code === "MALFORMED_CONSTRAINTS")).toBe(true);
  });

  it("rejects secret-shaped constraint fields and non-REFERENCE_ONLY credential modes", () => {
    const secretConstraint = { ...constraints(), apiKey: "sk-live-secret", secret: "password" };
    const secretResult = evaluateCadpConstraintProjection(request({
      constraints: secretConstraint as unknown as CadpConstraintProjectionConstraints,
    }));
    expect(secretResult.valid).toBe(false);
    expect(secretResult.issues.some((issue) => issue.code === "MALFORMED_CONSTRAINTS")).toBe(true);

    const nonReference = evaluateCadpConstraintProjection(request({
      constraints: constraints({ credentialMode: "INLINE" as unknown as "REFERENCE_ONLY" }),
    }));
    expect(nonReference.valid).toBe(false);
    expect(nonReference.issues.some((issue) => issue.code === "INVALID_CONSTRAINT_FIELD")).toBe(true);
  });

  it("rejects invalid constraint field types and closed-enum violations", () => {
    const negative = evaluateCadpConstraintProjection(request({ constraints: constraints({ costCeiling: -1 }) }));
    expect(negative.valid).toBe(false);
    expect(negative.issues.some((issue) => issue.code === "INVALID_CONSTRAINT_FIELD")).toBe(true);

    const nonSafe = evaluateCadpConstraintProjection(request({ constraints: constraints({ tokenCeiling: Number.MAX_SAFE_INTEGER + 1 }) }));
    expect(nonSafe.valid).toBe(false);
    expect(nonSafe.issues.some((issue) => issue.code === "INVALID_CONSTRAINT_FIELD" || issue.code === "CONSTRAINT_EXCEEDS_CONTRACT_BOUNDS")).toBe(true);

    const badRetention = evaluateCadpConstraintProjection(request({
      constraints: constraints({ retentionPolicy: "UNLIMITED" as unknown as "BOUNDED_RETENTION" }),
    }));
    expect(badRetention.valid).toBe(false);
    expect(badRetention.issues.some((issue) => issue.code === "INVALID_CONSTRAINT_FIELD")).toBe(true);

    const badSideEffect = evaluateCadpConstraintProjection(request({
      constraints: constraints({ remoteSideEffectPolicy: "WRITE" as unknown as "READ_ONLY" }),
    }));
    expect(badSideEffect.valid).toBe(false);
    expect(badSideEffect.issues.some((issue) => issue.code === "INVALID_CONSTRAINT_FIELD")).toBe(true);
  });

  it("returns deeply frozen output and nested collections", () => {
    const result = evaluateCadpConstraintProjection(request());
    expect(Object.isFrozen(result)).toBe(true);
    expect(Object.isFrozen(result.projection)).toBe(true);
    expect(Object.isFrozen(result.projection.constraints)).toBe(true);
    expect(Object.isFrozen(result.projection.supportedMethods)).toBe(true);
    expect(Object.isFrozen(result.issues)).toBe(true);
    expect(() => {
      (result.projection as { executionAuthorized: boolean }).executionAuthorized = true;
    }).toThrow();
    expect(() => {
      (result.projection.supportedMethods as string[]).push("stream");
    }).toThrow();
    expect(() => {
      (result.issues as CadpConstraintProjectionIssue[]).push({} as CadpConstraintProjectionIssue);
    }).toThrow();

    const blocked = evaluateCadpConstraintProjection(request({ ownerHandle: { contractVersion: "x" } as unknown as CapabilityOwnerHandle }));
    expect(Object.isFrozen(blocked)).toBe(true);
    expect(Object.isFrozen(blocked.projection)).toBe(true);
    expect(Object.isFrozen(blocked.projection.constraints)).toBe(true);
    expect(Object.isFrozen(blocked.issues)).toBe(true);
  });

  it("keeps all four authorization flags literal false on every satisfied and blocked path", () => {
    const satisfied = evaluateCadpConstraintProjection(request());
    const blockedCases = [
      evaluateCadpConstraintProjection(request({ ownerHandle: { contractVersion: "x" } as unknown as CapabilityOwnerHandle })),
      evaluateCadpConstraintProjection(request({ projection: projection({ capabilityId: "cvf.cadp.unrelated" }) })),
      evaluateCadpConstraintProjection(request({ providerId: "bogus-provider" })),
      evaluateCadpConstraintProjection(request({ constraints: constraints({ costCeiling: CADP_CONSTRAINT_PROJECTION_BOUNDS.costCeilingMax + 1 }) })),
    ];
    const all = [satisfied, ...blockedCases];
    for (const outcome of all) {
      expect(outcome.projection.executionAuthorized).toBe(false);
      expect(outcome.projection.liveExecutionAuthorized).toBe(false);
      expect(outcome.projection.providerCallAuthorized).toBe(false);
      expect(outcome.projection.credentialResolutionAuthorized).toBe(false);
    }
  });

  it("never references forbidden credential, quota, execution, or network seams", () => {
    const sourcePath = fileURLToPath(new URL("../src/cadp.constraint.projection.contract.ts", import.meta.url));
    const source = readFileSync(sourcePath, "utf8");
    const forbidden = [
      "CredentialBoundary",
      "resolveSecretForRuntime",
      "resolveMetadata",
      "recordUse",
      "ProviderExecutionBridge",
      ".execute(",
      "process.",
      "fetch(",
      "import(",
      "require(",
    ];
    for (const symbol of forbidden) {
      expect(source).not.toContain(symbol);
    }
  });
});
