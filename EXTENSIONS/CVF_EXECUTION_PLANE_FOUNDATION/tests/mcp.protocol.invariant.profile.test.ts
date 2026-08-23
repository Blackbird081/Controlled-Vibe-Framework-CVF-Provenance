import { describe, expect, it } from "vitest";

import {
  MCP_PROTOCOL_VERSION_2026_07_28,
  createMCPProtocolInvariantProfile,
  type MCPProtocolInvariantProfileInput,
} from "../src/mcp.protocol.invariant.profile";

function validInput(): MCPProtocolInvariantProfileInput {
  return {
    request: {
      protocolVersion: MCP_PROTOCOL_VERSION_2026_07_28,
      supportedProtocolVersions: [MCP_PROTOCOL_VERSION_2026_07_28],
      clientCapabilities: ["elicitation"],
      requiredClientCapabilities: ["elicitation"],
      negotiatedExtensions: ["io.modelcontextprotocol/ui"],
      usedExtensions: ["io.modelcontextprotocol/ui"],
    },
    discovery: {},
    subscription: {
      acknowledged: true,
      eventObserved: true,
      expectedSubscriptionId: "sub-1",
      eventSubscriptionId: "sub-1",
    },
    result: { resultType: "complete", interpretedAsCompletion: true },
    cache: { ttlMs: 30_000, cacheScope: "private", containsUserSpecificData: true },
    authorization: {
      tokenAudience: "https://mcp.example.test",
      intendedAudience: "https://mcp.example.test",
    },
    http: {
      protocolVersionHeader: MCP_PROTOCOL_VERSION_2026_07_28,
      protocolVersionBody: MCP_PROTOCOL_VERSION_2026_07_28,
      methodHeader: "tools/call",
      methodBody: "tools/call",
    },
  };
}

function evaluate(overrides: Partial<MCPProtocolInvariantProfileInput>) {
  return createMCPProtocolInvariantProfile().evaluate({ ...validInput(), ...overrides });
}

function expectRule(
  result: ReturnType<typeof evaluate>,
  ruleId: string,
  jsonRpcErrorCode?: number,
): void {
  expect(result.accepted).toBe(false);
  const violation = result.violations.find((item) => item.ruleId === ruleId);
  expect(violation).toBeDefined();
  if (jsonRpcErrorCode !== undefined) expect(violation?.jsonRpcErrorCode).toBe(jsonRpcErrorCode);
}

describe("MCPProtocolInvariantProfile", () => {
  it("accepts a composite profile satisfying all eleven rules", () => {
    expect(evaluate({})).toEqual({ accepted: true, violations: [] });
  });

  it.each([
    ["missing protocol version", { protocolVersion: undefined, clientCapabilities: [] }],
    ["missing client capabilities", { protocolVersion: MCP_PROTOCOL_VERSION_2026_07_28, clientCapabilities: undefined }],
  ])("rejects %s as invalid params", (_name, requestOverride) => {
    const result = evaluate({ request: { ...validInput().request, ...requestOverride } });
    expectRule(result, "MCP-PR-001", -32602);
  });

  it("rejects an unsupported protocol version with the exact MCP error", () => {
    const result = evaluate({
      request: { ...validInput().request, protocolVersion: "1900-01-01" },
    });
    expectRule(result, "MCP-PR-002", -32022);
  });

  it("rejects a required but undeclared client capability", () => {
    const result = evaluate({
      request: { ...validInput().request, clientCapabilities: [] },
    });
    expectRule(result, "MCP-PR-003", -32021);
  });

  it("rejects use of an extension that was not negotiated", () => {
    const result = evaluate({
      request: { ...validInput().request, negotiatedExtensions: [] },
    });
    expectRule(result, "MCP-PR-004");
  });

  it("rejects discovery metadata used for identity or authorization", () => {
    expectRule(evaluate({ discovery: { usedForIdentityDecision: true } }), "MCP-PR-005");
    expectRule(evaluate({ discovery: { usedForAuthorizationDecision: true } }), "MCP-PR-005");
  });

  it("rejects a subscription event before acknowledgment", () => {
    const result = evaluate({
      subscription: { ...validInput().subscription!, acknowledged: false },
    });
    expectRule(result, "MCP-PR-006");
  });

  it.each([undefined, "wrong-subscription"])(
    "rejects a missing or wrong subscription correlation ID (%s)",
    (eventSubscriptionId) => {
      const result = evaluate({
        subscription: { ...validInput().subscription!, eventSubscriptionId },
      });
      expectRule(result, "MCP-PR-006");
    },
  );

  it.each([
    { interpretedAsCompletion: true },
    { interpretedAsApproval: true },
  ])("rejects input_required interpreted as terminal authority: %o", (interpretation) => {
    const result = evaluate({
      result: { resultType: "input_required", ...interpretation },
    });
    expectRule(result, "MCP-PR-007");
  });

  it.each([
    { ttlMs: -1, cacheScope: "private" as const },
    { ttlMs: 1, cacheScope: "public" as const, containsUserSpecificData: true },
    { ttlMs: 1, cacheScope: "private" as const, usedAsAuthorization: true },
  ])("rejects unsafe cache semantics: %o", (cache) => {
    expectRule(evaluate({ cache }), "MCP-PR-008");
  });

  it.each([undefined, "https://other.example.test"])(
    "rejects a missing or mismatched token audience (%s)",
    (tokenAudience) => {
      const result = evaluate({
        authorization: { tokenAudience, intendedAudience: "https://mcp.example.test" },
      });
      expectRule(result, "MCP-PR-009");
    },
  );

  it("rejects an HTTP header/body mismatch with HeaderMismatch", () => {
    const result = evaluate({
      http: {
        protocolVersionHeader: MCP_PROTOCOL_VERSION_2026_07_28,
        protocolVersionBody: "2025-11-25",
      },
    });
    expectRule(result, "MCP-PR-010", -32020);
  });

  it("rejects a missing required HTTP mirror header with HeaderMismatch", () => {
    const result = evaluate({
      http: {
        protocolVersionBody: MCP_PROTOCOL_VERSION_2026_07_28,
      },
    });
    expectRule(result, "MCP-PR-010", -32020);
  });

  it.each(["password", "api-key", "access-token", "payment-credential"] as const)(
    "rejects the sensitive %s category in form-mode elicitation",
    (category) => {
      const result = evaluate({
        elicitation: {
          elicitationMode: "form",
          requestedDataCategories: [category],
        },
      });
      expectRule(result, "MCP-PR-011");
      expect(
        result.violations.find((violation) => violation.ruleId === "MCP-PR-011")?.decisionCode,
      ).toBe("UNSAFE_ELICITATION_REQUEST");
    },
  );

  it.each([
    ["unknown category", ["private-key"]],
    ["non-string category", [42]],
    ["empty category list", []],
    ["non-array category container", "contact"],
  ])("fails closed for a malformed form-mode %s", (_name, requestedDataCategories) => {
    const result = evaluate({
      elicitation: {
        elicitationMode: "form",
        requestedDataCategories,
      } as unknown as MCPProtocolInvariantProfileInput["elicitation"],
    });
    expectRule(result, "MCP-PR-011");
  });

  it.each([
    ["unknown mode", "inline"],
    ["non-string mode", 42],
  ])("fails closed for an %s", (_name, elicitationMode) => {
    const result = evaluate({
      elicitation: {
        elicitationMode,
        requestedDataCategories: ["contact"],
      } as unknown as MCPProtocolInvariantProfileInput["elicitation"],
    });
    expectRule(result, "MCP-PR-011");
  });

  it.each(["password", "api-key", "access-token", "payment-credential"] as const)(
    "accepts the sensitive %s category in URL-mode elicitation",
    (category) => {
      expect(evaluate({
        elicitation: {
          elicitationMode: "url",
          requestedDataCategories: [category],
        },
      })).toEqual({ accepted: true, violations: [] });
    },
  );

  it.each(["contact", "profile"] as const)(
    "accepts the ordinary %s category in form-mode elicitation",
    (category) => {
      expect(evaluate({
        elicitation: {
          elicitationMode: "form",
          requestedDataCategories: [category],
        },
      })).toEqual({ accepted: true, violations: [] });
    },
  );

  it("preserves prior composite acceptance when ordinary form elicitation is present", () => {
    expect(evaluate({
      elicitation: {
        elicitationMode: "form",
        requestedDataCategories: ["contact", "profile"],
      },
    })).toEqual({ accepted: true, violations: [] });
  });
});
