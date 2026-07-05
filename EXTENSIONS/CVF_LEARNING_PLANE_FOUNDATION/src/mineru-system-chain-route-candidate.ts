/**
 * MinerU bounded system-chain route candidate (MSEA-R28-T25).
 *
 * This helper is a thin foundation-plane coordinator over the accepted T22
 * route-candidate helper. It verifies the T23 authoring-ready disposition and
 * rejects file-backed production persistence, retrieval, vectorization, MinerU
 * runtime execution, private/generated content reads, provider/live proof, and
 * public-sync behavior.
 *
 * Candidate scope only: production memory/RAG route release remains held by
 * PRODUCTION_MEMORY_RAG_ROUTE_NOT_RELEASED_BY_T25_CANDIDATE_ONLY.
 */

import type { DurableMemoryStore } from "./durable-memory-store";
import {
  MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTED_BOUNDED_CANDIDATE,
  releaseMineruMemoryRagRouteCandidate,
  type MineruMemoryRagRouteReleaseInput,
  type MineruMemoryRagRouteReleaseResult,
} from "./mineru-memory-rag-route-release";

export const MINERU_SYSTEM_CHAIN_ROUTE_CANDIDATE_VERSION =
  "cvf.mineruSystemChainRouteCandidate.r28t25.v1";

export const MINERU_SYSTEM_CHAIN_ROUTE_CANDIDATE_ACCEPTED =
  "MINERU_SYSTEM_CHAIN_ROUTE_CANDIDATE_ACCEPTED";

export const PRODUCTION_MEMORY_RAG_ROUTE_NOT_RELEASED_BY_T25_CANDIDATE_ONLY =
  "PRODUCTION_MEMORY_RAG_ROUTE_NOT_RELEASED_BY_T25_CANDIDATE_ONLY";

export const T24_AUTHORING_READY_DISPOSITION =
  "T24_PRODUCTION_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTATION_WORK_ORDER_AUTHORING_READY";

export type MineruSystemChainPersistenceMode = "in-process-only";

export interface MineruSystemChainRouteAuthority {
  t23Disposition: string;
  freshMemoryOwnerAuthorization: boolean;
  productionPersistenceMode: MineruSystemChainPersistenceMode;
  fileBackedPersistenceRequested: boolean;
  retrievalRequested: boolean;
  vectorizationRequested: boolean;
  privateOutputContentRead: boolean;
}

export interface MineruSystemChainRouteCandidateInput {
  authority: MineruSystemChainRouteAuthority;
  routeInput: MineruMemoryRagRouteReleaseInput;
}

export interface MineruSystemChainRouteCandidateResult {
  disposition: string;
  routeCandidateVersion: string;
  productionRouteAuthorized: false;
  systemChainCandidateReady: boolean;
  persistenceMode: MineruSystemChainPersistenceMode | "rejected";
  routeResult: MineruMemoryRagRouteReleaseResult | null;
  preventedReason: string | null;
  heldToken: typeof PRODUCTION_MEMORY_RAG_ROUTE_NOT_RELEASED_BY_T25_CANDIDATE_ONLY;
}

function blocked(
  disposition: string,
  preventedReason: string,
): MineruSystemChainRouteCandidateResult {
  return {
    disposition,
    routeCandidateVersion: MINERU_SYSTEM_CHAIN_ROUTE_CANDIDATE_VERSION,
    productionRouteAuthorized: false,
    systemChainCandidateReady: false,
    persistenceMode: "rejected",
    routeResult: null,
    preventedReason,
    heldToken: PRODUCTION_MEMORY_RAG_ROUTE_NOT_RELEASED_BY_T25_CANDIDATE_ONLY,
  };
}

export function buildMineruSystemChainRouteCandidate(
  store: DurableMemoryStore,
  input: MineruSystemChainRouteCandidateInput,
): MineruSystemChainRouteCandidateResult {
  const { authority } = input;

  if (authority.t23Disposition !== T24_AUTHORING_READY_DISPOSITION) {
    return blocked(
      "FAIL_CLOSED_T23_DISPOSITION_NOT_READY",
      "T23 disposition must authorize only T24 work-order authoring readiness",
    );
  }

  if (authority.freshMemoryOwnerAuthorization !== true) {
    return blocked(
      "FAIL_CLOSED_MEMORY_OWNER_AUTHORIZATION_MISSING",
      "fresh memory-owner authorization must be present before a route candidate",
    );
  }

  if (authority.productionPersistenceMode !== "in-process-only") {
    return blocked(
      "FAIL_CLOSED_UNSUPPORTED_PERSISTENCE_MODE",
      "T25 bounded system-chain candidate supports only in-process persistence",
    );
  }

  if (authority.fileBackedPersistenceRequested !== false) {
    return blocked(
      "FAIL_CLOSED_FILE_BACKED_PERSISTENCE_REQUESTED",
      "file-backed production persistence is not authorized by T25",
    );
  }

  if (authority.retrievalRequested !== false) {
    return blocked(
      "FAIL_CLOSED_RETRIEVAL_REQUESTED",
      "retrieval remains outside the T25 bounded system-chain candidate",
    );
  }

  if (authority.vectorizationRequested !== false) {
    return blocked(
      "FAIL_CLOSED_VECTORIZATION_REQUESTED",
      "vectorization remains outside the T25 bounded system-chain candidate",
    );
  }

  if (authority.privateOutputContentRead !== false) {
    return blocked(
      "FAIL_CLOSED_PRIVATE_OUTPUT_CONTENT_READ",
      "private/generated output content reads remain forbidden",
    );
  }

  const routeResult = releaseMineruMemoryRagRouteCandidate(
    store,
    input.routeInput,
  );
  if (
    routeResult.disposition !==
    MINERU_MEMORY_RAG_ROUTE_RELEASE_IMPLEMENTED_BOUNDED_CANDIDATE
  ) {
    return {
      disposition: `T22_ROUTE_CANDIDATE_NOT_ACCEPTED: ${routeResult.disposition}`,
      routeCandidateVersion: MINERU_SYSTEM_CHAIN_ROUTE_CANDIDATE_VERSION,
      productionRouteAuthorized: false,
      systemChainCandidateReady: false,
      persistenceMode: "rejected",
      routeResult,
      preventedReason: routeResult.preventedReason,
      heldToken: PRODUCTION_MEMORY_RAG_ROUTE_NOT_RELEASED_BY_T25_CANDIDATE_ONLY,
    };
  }

  return {
    disposition: MINERU_SYSTEM_CHAIN_ROUTE_CANDIDATE_ACCEPTED,
    routeCandidateVersion: MINERU_SYSTEM_CHAIN_ROUTE_CANDIDATE_VERSION,
    productionRouteAuthorized: false,
    systemChainCandidateReady: true,
    persistenceMode: "in-process-only",
    routeResult,
    preventedReason: null,
    heldToken: PRODUCTION_MEMORY_RAG_ROUTE_NOT_RELEASED_BY_T25_CANDIDATE_ONLY,
  };
}
