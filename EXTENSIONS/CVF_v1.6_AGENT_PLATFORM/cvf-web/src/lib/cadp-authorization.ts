import type { TeamRole } from 'cvf-guard-contract/enterprise';

import type { RouteGovernanceAuthorization } from '@/lib/route-governance-proof';

/**
 * CADP-AI-T5-R5: a pure projection from an authenticated
 * `RouteGovernanceAuthorization` to CADP authority metadata. This module
 * makes no route-access decision, persists nothing, and never registers a
 * route. Every authority field below is a literal `false`; only a future,
 * separately-selected CADP authorization owner may change that, subject to
 * `governance/compat/check_cadp_authority_boundary_drift.py`.
 */
export interface CadpAuthorizationProjection {
  readonly actorId: string | null;
  readonly realActorId: string | null;
  readonly role: TeamRole | null;
  readonly executionAuthorized: false;
  readonly mutationAuthorized: false;
  readonly receiptGrantsExecution: false;
  readonly receiptGrantsMutation: false;
  readonly receiptGrantsActivation: false;
}

export function projectCadpAuthorization(
  authorization: RouteGovernanceAuthorization,
): CadpAuthorizationProjection {
  const session = authorization.session;
  const actorId = authorization.proof.actorId;
  const realActorId = session?.impersonation?.realActorId ?? null;
  const role = session?.role ?? null;

  return {
    actorId,
    realActorId,
    role,
    executionAuthorized: false,
    mutationAuthorized: false,
    receiptGrantsExecution: false,
    receiptGrantsMutation: false,
    receiptGrantsActivation: false,
  };
}
