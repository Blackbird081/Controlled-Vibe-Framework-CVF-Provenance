export const MCP_PROTOCOL_VERSION_2026_07_28 = "2026-07-28" as const;

export type MCPProtocolInvariantRuleId =
  | "MCP-PR-001"
  | "MCP-PR-002"
  | "MCP-PR-003"
  | "MCP-PR-004"
  | "MCP-PR-005"
  | "MCP-PR-006"
  | "MCP-PR-007"
  | "MCP-PR-008"
  | "MCP-PR-009"
  | "MCP-PR-010";

export type MCPProtocolInvariantDecisionCode =
  | "INVALID_PARAMS"
  | "UNSUPPORTED_PROTOCOL_VERSION"
  | "MISSING_REQUIRED_CLIENT_CAPABILITY"
  | "EXTENSION_NOT_NEGOTIATED"
  | "UNTRUSTED_DISCOVERY_EVIDENCE"
  | "SUBSCRIPTION_PROTOCOL_VIOLATION"
  | "INPUT_REQUIRED_CONTINUATION_VIOLATION"
  | "UNSAFE_CACHE_HINT"
  | "TOKEN_AUDIENCE_MISMATCH"
  | "HEADER_MISMATCH";

export type MCPProtocolJsonRpcErrorCode = -32602 | -32020 | -32021 | -32022;

export interface MCPProtocolRequestProfile {
  protocolVersion?: string;
  supportedProtocolVersions: readonly string[];
  clientCapabilities?: readonly string[];
  requiredClientCapabilities?: readonly string[];
  negotiatedExtensions?: readonly string[];
  usedExtensions?: readonly string[];
}

export interface MCPDiscoveryEvidenceProfile {
  usedForIdentityDecision?: boolean;
  usedForAuthorizationDecision?: boolean;
}

export interface MCPSubscriptionProfile {
  acknowledged: boolean;
  eventObserved: boolean;
  expectedSubscriptionId: string | number;
  eventSubscriptionId?: string | number;
}

export interface MCPResultProfile {
  resultType: string;
  interpretedAsCompletion?: boolean;
  interpretedAsApproval?: boolean;
}

export interface MCPCacheProfile {
  ttlMs?: number;
  cacheScope?: "public" | "private";
  containsUserSpecificData?: boolean;
  usedAsAuthorization?: boolean;
}

export interface MCPAuthorizationProfile {
  tokenAudience?: string;
  intendedAudience: string;
}

export interface MCPHttpMirrorProfile {
  protocolVersionHeader?: string;
  protocolVersionBody?: string;
  methodHeader?: string;
  methodBody?: string;
  nameHeader?: string;
  nameBody?: string;
}

export interface MCPProtocolInvariantProfileInput {
  request: MCPProtocolRequestProfile;
  discovery?: MCPDiscoveryEvidenceProfile;
  subscription?: MCPSubscriptionProfile;
  result?: MCPResultProfile;
  cache?: MCPCacheProfile;
  authorization?: MCPAuthorizationProfile;
  http?: MCPHttpMirrorProfile;
}

export interface MCPProtocolInvariantViolation {
  ruleId: MCPProtocolInvariantRuleId;
  decisionCode: MCPProtocolInvariantDecisionCode;
  reason: string;
  jsonRpcErrorCode?: MCPProtocolJsonRpcErrorCode;
}

export interface MCPProtocolInvariantDecision {
  accepted: boolean;
  violations: MCPProtocolInvariantViolation[];
}

export class MCPProtocolInvariantProfile {
  evaluate(input: MCPProtocolInvariantProfileInput): MCPProtocolInvariantDecision {
    const violations: MCPProtocolInvariantViolation[] = [];
    this.checkRequestMetadata(input.request, violations);
    this.checkExtensions(input.request, violations);
    this.checkDiscovery(input.discovery, violations);
    this.checkSubscription(input.subscription, violations);
    this.checkResult(input.result, violations);
    this.checkCache(input.cache, violations);
    this.checkAuthorization(input.authorization, violations);
    this.checkHttpMirrors(input.http, violations);
    return { accepted: violations.length === 0, violations };
  }

  private checkRequestMetadata(
    request: MCPProtocolRequestProfile,
    violations: MCPProtocolInvariantViolation[],
  ): void {
    if (!request.protocolVersion || !request.clientCapabilities) {
      violations.push({
        ruleId: "MCP-PR-001",
        decisionCode: "INVALID_PARAMS",
        jsonRpcErrorCode: -32602,
        reason: "modern MCP requests require per-request protocol version and client capabilities",
      });
      return;
    }

    if (!request.supportedProtocolVersions.includes(request.protocolVersion)) {
      violations.push({
        ruleId: "MCP-PR-002",
        decisionCode: "UNSUPPORTED_PROTOCOL_VERSION",
        jsonRpcErrorCode: -32022,
        reason: "requested MCP protocol version is not supported",
      });
    }

    const declared = new Set(request.clientCapabilities);
    const missing = (request.requiredClientCapabilities ?? []).filter(
      (capability) => !declared.has(capability),
    );
    if (missing.length > 0) {
      violations.push({
        ruleId: "MCP-PR-003",
        decisionCode: "MISSING_REQUIRED_CLIENT_CAPABILITY",
        jsonRpcErrorCode: -32021,
        reason: `required client capabilities were not declared: ${missing.join(", ")}`,
      });
    }
  }

  private checkExtensions(
    request: MCPProtocolRequestProfile,
    violations: MCPProtocolInvariantViolation[],
  ): void {
    const negotiated = new Set(request.negotiatedExtensions ?? []);
    const unnegotiated = (request.usedExtensions ?? []).filter(
      (extension) => !negotiated.has(extension),
    );
    if (unnegotiated.length > 0) {
      violations.push({
        ruleId: "MCP-PR-004",
        decisionCode: "EXTENSION_NOT_NEGOTIATED",
        reason: `extensions were used without capability negotiation: ${unnegotiated.join(", ")}`,
      });
    }
  }

  private checkDiscovery(
    discovery: MCPDiscoveryEvidenceProfile | undefined,
    violations: MCPProtocolInvariantViolation[],
  ): void {
    if (discovery?.usedForIdentityDecision || discovery?.usedForAuthorizationDecision) {
      violations.push({
        ruleId: "MCP-PR-005",
        decisionCode: "UNTRUSTED_DISCOVERY_EVIDENCE",
        reason: "self-reported discovery metadata cannot decide identity or authorization",
      });
    }
  }

  private checkSubscription(
    subscription: MCPSubscriptionProfile | undefined,
    violations: MCPProtocolInvariantViolation[],
  ): void {
    if (!subscription?.eventObserved) return;
    if (!subscription.acknowledged) {
      violations.push({
        ruleId: "MCP-PR-006",
        decisionCode: "SUBSCRIPTION_PROTOCOL_VIOLATION",
        reason: "subscription event arrived before acknowledgment",
      });
      return;
    }
    if (subscription.eventSubscriptionId !== subscription.expectedSubscriptionId) {
      violations.push({
        ruleId: "MCP-PR-006",
        decisionCode: "SUBSCRIPTION_PROTOCOL_VIOLATION",
        reason: "subscription event does not correlate to the originating request ID",
      });
    }
  }

  private checkResult(
    result: MCPResultProfile | undefined,
    violations: MCPProtocolInvariantViolation[],
  ): void {
    if (
      result?.resultType === "input_required"
      && (result.interpretedAsCompletion || result.interpretedAsApproval)
    ) {
      violations.push({
        ruleId: "MCP-PR-007",
        decisionCode: "INPUT_REQUIRED_CONTINUATION_VIOLATION",
        reason: "input_required is an incomplete continuation, not completion or approval",
      });
    }
  }

  private checkCache(
    cache: MCPCacheProfile | undefined,
    violations: MCPProtocolInvariantViolation[],
  ): void {
    if (!cache) return;
    const negativeTtl = cache.ttlMs !== undefined && cache.ttlMs < 0;
    const unsafePublicScope = cache.cacheScope === "public" && cache.containsUserSpecificData === true;
    if (negativeTtl || unsafePublicScope || cache.usedAsAuthorization) {
      violations.push({
        ruleId: "MCP-PR-008",
        decisionCode: "UNSAFE_CACHE_HINT",
        reason: "cache TTL/scope is invalid or was treated as authorization",
      });
    }
  }

  private checkAuthorization(
    authorization: MCPAuthorizationProfile | undefined,
    violations: MCPProtocolInvariantViolation[],
  ): void {
    if (!authorization) return;
    if (
      !authorization.tokenAudience
      || authorization.tokenAudience !== authorization.intendedAudience
    ) {
      violations.push({
        ruleId: "MCP-PR-009",
        decisionCode: "TOKEN_AUDIENCE_MISMATCH",
        reason: "access token was not issued for the intended MCP server audience",
      });
    }
  }

  private checkHttpMirrors(
    http: MCPHttpMirrorProfile | undefined,
    violations: MCPProtocolInvariantViolation[],
  ): void {
    if (!http) return;
    const mirroredPairs: ReadonlyArray<readonly [string | undefined, string | undefined]> = [
      [http.protocolVersionHeader, http.protocolVersionBody],
      [http.methodHeader, http.methodBody],
      [http.nameHeader, http.nameBody],
    ];
    const mismatch = mirroredPairs.some(([header, body]) => {
      const onlyOneValuePresent = (header === undefined) !== (body === undefined);
      return onlyOneValuePresent || (header !== undefined && header !== body);
    });
    if (mismatch) {
      violations.push({
        ruleId: "MCP-PR-010",
        decisionCode: "HEADER_MISMATCH",
        jsonRpcErrorCode: -32020,
        reason: "required HTTP mirror header does not match the request body",
      });
    }
  }
}

export function createMCPProtocolInvariantProfile(): MCPProtocolInvariantProfile {
  return new MCPProtocolInvariantProfile();
}
