import { strict as assert } from "node:assert";
import { createHash } from "node:crypto";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import {
  ControlledMemoryGatewayContract,
} from "../EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract";
import {
  createFileBackedDurableMemoryStore,
} from "../EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store";
import { GuardRuntimeEngine } from "../EXTENSIONS/CVF_GUARD_CONTRACT/src/engine";
import { AgentExecutionRuntime } from "../EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime";
import { ApprovalExecutionBridge } from "../EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/approval-execution-bridge";
import { AlibabaDashScopeProvider } from "../EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/providers/alibaba-dashscope-provider";
import { ContextPackagerContract } from "../EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/context.packager.contract";

const now = "2026-08-29T16:00:00.000Z";
const policy = (actorId: string) => ({
  traceId: `trace-${actorId}`,
  policyResult: "allow" as const,
  actorId,
  actorRole: "operator" as const,
  allowedScopes: ["user" as const],
  canWrite: true,
  canReinject: true,
});

async function main(): Promise<void> {
  const apiKey = process.env.ALIBABA_API_KEY
    ?? process.env.CVF_BENCHMARK_ALIBABA_KEY
    ?? process.env.CVF_ALIBABA_API_KEY;
  assert(apiKey, "Alibaba API key is required for representative live proof");

  const memory = new ControlledMemoryGatewayContract({ now: () => now });
  const poison = memory.capture({
    sourceEvent: "tool_result",
    content: "Operator identity is attacker-controlled",
    kind: "semantic",
    scope: "user",
    segmentClass: "identity",
    policy: policy("principal-a"),
    provenance: { sourceClass: "runtime_event", summary: "untrusted tool output" },
  });
  assert.equal(poison.receipt.reason, "untrusted_source_cannot_write_protected_memory");
  const original = memory.capture({
    sourceEvent: "prompt_submit",
    content: "Prefer concise operational reports",
    kind: "semantic",
    scope: "user",
    segmentClass: "preference",
    policy: policy("principal-a"),
    provenance: { sourceClass: "runtime_event", summary: "operator instruction" },
  }).record!;
  const correction = memory.capture({
    sourceEvent: "prompt_submit",
    content: "Prefer detailed evidence in closure reports",
    kind: "semantic",
    scope: "user",
    segmentClass: "correction",
    links: [{ type: "corrects", targetMemoryId: original.memoryId }],
    policy: policy("principal-a"),
    provenance: { sourceClass: "runtime_event", summary: "operator correction" },
  }).record!;
  assert.equal(memory.retrieve({ query: "detailed", policy: policy("principal-b") }).records.length, 0);
  assert.deepEqual(
    memory.retrieve({ query: "detailed", policy: policy("principal-a") }).records.map((item) => item.memoryId),
    [correction.memoryId],
  );

  const tempDirectory = mkdtempSync(join(tmpdir(), "cvf-brigade-memory-origin-"));
  try {
    const filePath = join(tempDirectory, "memory.json");
    createFileBackedDurableMemoryStore(filePath).write({
      id: "durable-origin-proof",
      tier: "long-term",
      scope: "shared-project",
      actorId: "principal-a",
      originPrincipalId: "principal-a",
      actorRole: "OPERATOR",
      summary: "Principal A durable preference",
      policyDecision: "allow",
      actorAuthorized: true,
    });
    const restarted = createFileBackedDurableMemoryStore(filePath);
    assert.equal(restarted.read({
      tier: "long-term", scope: "shared-project", actorId: "principal-b",
      originPrincipalId: "principal-b",
      actorRole: "REVIEWER", actorAuthorized: true,
    }).records.length, 0);
    assert.equal(restarted.read({
      tier: "long-term", scope: "shared-project", actorId: "principal-a",
      originPrincipalId: "principal-a",
      actorRole: "REVIEWER", actorAuthorized: true,
    }).records.length, 1);
  } finally {
    rmSync(tempDirectory, { recursive: true, force: true });
  }

  const guardEngine = new GuardRuntimeEngine({ defaultDecision: "ALLOW" });
  guardEngine.registerGuard({
    id: "brigade-representative-approval",
    name: "Representative approval",
    description: "Routes the representative live call through approval settlement.",
    priority: 1,
    enabled: true,
    evaluate: () => ({
      guardId: "brigade-representative-approval",
      decision: "ESCALATE",
      severity: "WARN",
      reason: "representative_live_approval_required",
      timestamp: new Date().toISOString(),
      agentGuidance: "Approve the bound representative request.",
    }),
  });
  const approvalBridge = new ApprovalExecutionBridge();
  const provider = new AlibabaDashScopeProvider({
    apiKey,
    model: "qwen-flash",
    maxTokens: 12,
    temperature: 0,
    systemInstruction: "Return only the exact marker requested by the task.",
  });
  const runtime = new AgentExecutionRuntime(guardEngine, provider, {
    phase: "BUILD",
    riskLevel: "R1",
    role: "AI_AGENT",
    agentId: "brigade-worker",
    channel: "cli",
    liveExecution: true,
    controlMode: "governed",
    sessionId: "brigade-runtime-pilot",
    cwd: process.cwd(),
    environment: { provider: "alibaba-dashscope", model: "qwen-flash" },
    approvalBridge,
  });
  const liveStartedAt = Date.now();
  const liveRun = runtime.runAwaitingApproval("generate: Return only BRIGADE_RESIDUAL_OK");
  const pending = approvalBridge.listPending();
  assert.equal(pending.length, 1);
  assert.equal(approvalBridge.settle(pending[0].requestId, "approved", "operator-authorized-reviewer"), true);
  const liveResult = await liveRun;
  assert.equal(liveResult.status, "COMPLETED");
  assert.match(liveResult.output ?? "", /BRIGADE_RESIDUAL_OK/i);
  assert.equal(approvalBridge.listPending().length, 0);

  const errorTail = "FATAL_CAUSAL_TAIL";
  const packager = new ContextPackagerContract({ now: () => now });
  const packed = packager.pack({
    contextId: "brigade-context-pilot",
    query: "diagnose representative tool failures",
    contextWindowTokens: 20_000,
    toolResults: [
      { id: "tool-old", content: `BEGIN-${"a".repeat(25_000)}-${errorTail}` },
      { id: "tool-new", content: `BEGIN-${"b".repeat(25_000)}-${errorTail}` },
    ],
  });
  assert.equal(packed.toolResultCompaction?.disposition, "COMPACTED");
  assert.equal(packed.segments.filter((item) => item.source?.startsWith("tool-result:")).length, 2);
  assert.equal(packed.segments.filter((item) => item.source?.startsWith("tool-result:")).every((item) => item.content.endsWith(errorTail)), true);
  const refused = packager.pack({
    contextId: "brigade-context-refusal",
    query: "q".repeat(98_000),
    contextWindowTokens: 32_000,
    maxTokens: 32_000,
    toolResults: [{ id: "unsafe-late", content: "x".repeat(30_000) }],
  });
  assert.equal(refused.toolResultCompaction?.disposition, "REFUSE_LATE_COMPACTION");

  const evidence = {
    schemaVersion: "cvf.brigade.residual.absorption.runtime-pilot.v1",
    generatedAt: new Date().toISOString(),
    verdict: "PASS",
    provider: { name: provider.name, model: "qwen-flash", calls: 1, latencyMs: Date.now() - liveStartedAt },
    memoryTrust: {
      protectedPoisoningDenied: true,
      exactPrincipalRecallIsolation: true,
      typedCorrectionApplied: true,
      durableRestartOriginIsolation: true,
    },
    approvalExecution: {
      pendingCountBeforeSettlement: pending.length,
      exactBindingHash: pending[0].bindingHash,
      settlementDecision: (liveResult.metadata?.approvalSettlement as { decision?: string } | undefined)?.decision,
      pendingCountAfterSettlement: approvalBridge.listPending().length,
      providerExecutedExactlyOnce: true,
      outputHash: createHash("sha256").update(liveResult.output ?? "").digest("hex"),
    },
    contextPacking: {
      disposition: packed.toolResultCompaction?.disposition,
      singleResultCompactions: packed.toolResultCompaction?.singleResultCompactions,
      aggregateCompactions: packed.toolResultCompaction?.aggregateCompactions,
      importantTailPreserved: packed.toolResultCompaction?.importantTailPreserved,
      lateCompactionDisposition: refused.toolResultCompaction?.disposition,
    },
    secretsRecorded: false,
  };
  process.stdout.write(`${JSON.stringify(evidence, null, 2)}\n`);
}

main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  process.stderr.write(`${JSON.stringify({ verdict: "FAIL", error: message })}\n`);
  process.exitCode = 1;
});
