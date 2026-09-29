// CADP-AI-T3A - Execution Package Root CADP Capability Consumer Discoverability
//
// Dedicated focused test proving that the T3A CADP capability consumer is
// callable through the execution-plane package root (../src/index), not only
// through the local src/cadp.capability.consumer.contract.ts barrel. Does not
// duplicate the focused behavior coverage in
// cadp.capability.consumer.contract.test.ts; this file only proves root
// discoverability and a forged-request fail-closed path through that root.

import { describe, expect, it } from "vitest";
import {
  CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION,
  CadpCapabilityConsumerContract,
  createCadpCapabilityConsumerContract,
  evaluateCadpCapabilityConsumer,
} from "../src/index";
import type { CadpCapabilityConsumerRequest } from "../src/index";

describe("execution package root CADP capability consumer discoverability", () => {
  it("exposes the adapter constant, factory, class and function through the package root", () => {
    expect(CADP_CAPABILITY_CONSUMER_CONTRACT_VERSION).toBe("cvf.cadp.consumer.v1");
    expect(typeof evaluateCadpCapabilityConsumer).toBe("function");
    const contract = createCadpCapabilityConsumerContract();
    expect(contract).toBeInstanceOf(CadpCapabilityConsumerContract);
    expect(typeof contract.evaluate).toBe("function");
  });

  it("evaluates a forged request through the package root and fails closed", () => {
    const forged = { ownerHandle: { contractVersion: "forged" } };
    const result = evaluateCadpCapabilityConsumer(forged as unknown as CadpCapabilityConsumerRequest);
    expect(result.valid).toBe(false);
    expect(result.projection.executionAuthorized).toBe(false);
    expect(result.issues.some((issue) => issue.code === "MALFORMED_REQUEST")).toBe(true);
  });
});
