export const MEMORY_RETRIEVAL_POLICY_VERSION =
  "cvf.memoryRetrievalPolicy.phase2a.v1";

export type MemoryRetrievalMethod =
  | "keyword"
  | "semantic"
  | "recency"
  | "audit_trust"
  | "graph_search";

export interface MemoryRetrievalCandidate {
  id: string;
  scope: string;
  summary: string;
  content?: string;
  createdAt: number;
  auditTrust: number;
  lifecycleState: "working" | "episodic" | "semantic" | "procedural" | "expired" | "disputed";
  containsSecret?: boolean;
}

export interface MemoryRetrievalRequest {
  method: MemoryRetrievalMethod;
  query: string;
  scope: string;
  actorAuthorized: boolean;
  candidates: readonly MemoryRetrievalCandidate[];
  maxResults?: number;
}

export interface MemoryRetrievalResult {
  contractVersion: typeof MEMORY_RETRIEVAL_POLICY_VERSION;
  method: MemoryRetrievalMethod;
  status: "allowed" | "denied" | "deferred";
  reason: string;
  selected: readonly MemoryRetrievalCandidate[];
  excluded: readonly { id: string; reason: string }[];
  rawMemoryReleased: false;
}

const BLOCKED_STATES = new Set(["expired", "disputed"]);

function matchesQuery(candidate: MemoryRetrievalCandidate, query: string): boolean {
  const normalized = query.trim().toLowerCase();
  if (normalized.length === 0) {
    return true;
  }
  return `${candidate.summary} ${candidate.content ?? ""}`.toLowerCase().includes(normalized);
}

export function evaluateRetrievalRequest(
  request: MemoryRetrievalRequest,
): MemoryRetrievalResult {
  if (request.method === "graph_search") {
    return {
      contractVersion: MEMORY_RETRIEVAL_POLICY_VERSION,
      method: request.method,
      status: "deferred",
      reason: "graph_search_deferred_until_aif_b_integration",
      selected: [],
      excluded: request.candidates.map((candidate) => ({
        id: candidate.id,
        reason: "graph_search_not_active_in_phase2a",
      })),
      rawMemoryReleased: false,
    };
  }

  if (!request.actorAuthorized) {
    return {
      contractVersion: MEMORY_RETRIEVAL_POLICY_VERSION,
      method: request.method,
      status: "denied",
      reason: "actor_not_authorized_for_memory_retrieval",
      selected: [],
      excluded: request.candidates.map((candidate) => ({
        id: candidate.id,
        reason: "policy_denied",
      })),
      rawMemoryReleased: false,
    };
  }

  const excluded: { id: string; reason: string }[] = [];
  const selected = request.candidates.filter((candidate) => {
    if (candidate.scope !== request.scope) {
      excluded.push({ id: candidate.id, reason: "out_of_scope" });
      return false;
    }
    if (candidate.containsSecret === true) {
      excluded.push({ id: candidate.id, reason: "privacy_filtered" });
      return false;
    }
    if (BLOCKED_STATES.has(candidate.lifecycleState)) {
      excluded.push({ id: candidate.id, reason: candidate.lifecycleState });
      return false;
    }
    if ((request.method === "keyword" || request.method === "semantic") &&
      !matchesQuery(candidate, request.query)) {
      excluded.push({ id: candidate.id, reason: "low_relevance" });
      return false;
    }
    return true;
  });

  const sorted = [...selected].sort((a, b) => {
    if (request.method === "audit_trust") {
      return b.auditTrust - a.auditTrust || b.createdAt - a.createdAt;
    }
    return b.createdAt - a.createdAt;
  });

  return {
    contractVersion: MEMORY_RETRIEVAL_POLICY_VERSION,
    method: request.method,
    status: "allowed",
    reason: "memory_retrieval_policy_applied",
    selected: sorted.slice(0, request.maxResults ?? 5),
    excluded,
    rawMemoryReleased: false,
  };
}
