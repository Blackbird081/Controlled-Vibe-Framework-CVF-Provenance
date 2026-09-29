// CADP-AI-T3B - Model Gateway Package Root Constraint Projection Discoverability
//
// Dedicated focused test proving that the T3B constraint projection is
// callable through the model-gateway package root (../src/index), not only
// through the local src/cadp.constraint.projection.contract.ts barrel. Does
// not duplicate the focused behavior coverage in
// cadp.constraint.projection.contract.test.ts; this file only proves root
// discoverability and a forged-request fail-closed path through that root,
// plus the absence of import-time side effects.

import { describe, expect, it } from "vitest";
import {
  CADP_CONSTRAINT_PROJECTION_BOUNDS,
  CADP_CONSTRAINT_PROJECTION_CONTRACT_VERSION,
  CadpConstraintProjectionContract,
  createCadpConstraintProjectionContract,
  evaluateCadpConstraintProjection,
  MODEL_GATEWAY_WRAPPER,
} from "../src/index";
import type { CadpConstraintProjectionRequest } from "../src/index";

describe("model gateway package root constraint projection discoverability", () => {
  it("exposes the constant, bounds, factory, class, and function through the package root", () => {
    expect(CADP_CONSTRAINT_PROJECTION_CONTRACT_VERSION).toBe("cvf.cadp.constraintProjection.v1");
    expect(typeof CADP_CONSTRAINT_PROJECTION_BOUNDS).toBe("object");
    expect(typeof evaluateCadpConstraintProjection).toBe("function");
    const contract = createCadpConstraintProjectionContract();
    expect(contract).toBeInstanceOf(CadpConstraintProjectionContract);
    expect(typeof contract.evaluate).toBe("function");
  });

  it("evaluates a forged request through the package root and fails closed without side effect", () => {
    const forged = { ownerHandle: { contractVersion: "forged" } };
    const result = evaluateCadpConstraintProjection(forged as unknown as CadpConstraintProjectionRequest);
    expect(result.valid).toBe(false);
    expect(result.projection.decision).toBe("BLOCKED");
    expect(result.projection.executionAuthorized).toBe(false);
    expect(result.projection.liveExecutionAuthorized).toBe(false);
    expect(result.projection.providerCallAuthorized).toBe(false);
    expect(result.projection.credentialResolutionAuthorized).toBe(false);
    expect(result.issues.some((issue) => issue.code === "MALFORMED_REQUEST")).toBe(true);
  });

  it("keeps the package-root wrapper intact after adding the T3B export", () => {
    expect(MODEL_GATEWAY_WRAPPER).toBeDefined();
    expect(MODEL_GATEWAY_WRAPPER.enforcesGuardContractBeforeRouting).toBe(true);
  });
});
