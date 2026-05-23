import { describe, expect, it } from "vitest";
import {
  evaluateRetrievalRequest,
  MEMORY_RETRIEVAL_POLICY_VERSION,
  type MemoryRetrievalCandidate,
} from "../src/memory-retrieval-policy";

const candidates: MemoryRetrievalCandidate[] = [
  {
    id: "mem-1",
    scope: "project-a",
    summary: "Qwen provider routing requires R1 payload",
    createdAt: 100,
    auditTrust: 0.9,
    lifecycleState: "semantic",
  },
  {
    id: "mem-2",
    scope: "project-b",
    summary: "different scope",
    createdAt: 200,
    auditTrust: 1,
    lifecycleState: "semantic",
  },
  {
    id: "mem-3",
    scope: "project-a",
    summary: "secret value",
    createdAt: 300,
    auditTrust: 1,
    lifecycleState: "semantic",
    containsSecret: true,
  },
];

describe("memory retrieval policy phase 2a", () => {
  it("filters by scope, privacy, and query before returning summaries", () => {
    const result = evaluateRetrievalRequest({
      method: "keyword",
      query: "qwen",
      scope: "project-a",
      actorAuthorized: true,
      candidates,
    });

    expect(result).toMatchObject({
      contractVersion: MEMORY_RETRIEVAL_POLICY_VERSION,
      status: "allowed",
      rawMemoryReleased: false,
    });
    expect(result.selected.map((item) => item.id)).toEqual(["mem-1"]);
    expect(result.excluded).toEqual([
      { id: "mem-2", reason: "out_of_scope" },
      { id: "mem-3", reason: "privacy_filtered" },
    ]);
  });

  it("denies unauthorized actors", () => {
    expect(evaluateRetrievalRequest({
      method: "recency",
      query: "",
      scope: "project-a",
      actorAuthorized: false,
      candidates,
    })).toMatchObject({
      status: "denied",
      reason: "actor_not_authorized_for_memory_retrieval",
      selected: [],
      rawMemoryReleased: false,
    });
  });

  it("keeps graph search deferred in phase 2a", () => {
    expect(evaluateRetrievalRequest({
      method: "graph_search",
      query: "routing",
      scope: "project-a",
      actorAuthorized: true,
      candidates,
    })).toMatchObject({
      status: "deferred",
      reason: "graph_search_deferred_until_aif_b_integration",
      selected: [],
    });
  });
});
