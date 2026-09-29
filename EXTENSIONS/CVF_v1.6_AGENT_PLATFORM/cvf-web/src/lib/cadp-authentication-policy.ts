import { NextRequest } from 'next/server';

import {
  authorizeRouteGovernanceProof,
  type RouteGovernanceAuthorization,
  type RouteGovernanceProofConfig,
} from '@/lib/route-governance-proof';

/**
 * CADP-AI-T5-R5: the only CADP authentication policy wrapper. It composes
 * the existing `authorizeRouteGovernanceProof` helper with the
 * operator-selected Option A precedence and does not register any route.
 */
export const CADP_FAIL_CLOSED_ON_INVALID_TOKEN = 'CADP_FAIL_CLOSED_ON_INVALID_TOKEN' as const;

export interface CadpAuthenticationPolicyOptions {
  /**
   * Injectable millisecond timestamp propagated to the underlying proof
   * helper for deterministic tests. Defaults to `Date.now()`.
   */
  now?: number;
}

/**
 * Authenticate a request under the mandatory CADP Option A policy: a
 * presented-but-invalid service token denies immediately and never falls
 * through to session evaluation. Existing non-CADP callers of
 * `authorizeRouteGovernanceProof` are unaffected by this wrapper.
 */
export async function authorizeCadpAuthenticationRequest(
  request: NextRequest,
  bodyText: string,
  config: RouteGovernanceProofConfig,
  options: CadpAuthenticationPolicyOptions = {},
): Promise<RouteGovernanceAuthorization> {
  return authorizeRouteGovernanceProof(request, bodyText, config, {
    now: options.now,
    invalidTokenPrecedence: 'FAIL_CLOSED',
  });
}
