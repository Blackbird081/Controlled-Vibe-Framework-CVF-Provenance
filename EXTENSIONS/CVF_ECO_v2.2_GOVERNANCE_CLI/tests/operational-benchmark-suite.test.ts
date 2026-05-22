import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { CommandRegistry } from "../src/command.registry";
import {
  buildOperationalBenchmarkReport,
  formatOperationalBenchmarkReport,
  parseOperationalBenchmarkInput,
} from "../src/operational-benchmark-suite";

describe("operational benchmark suite", () => {
  it("builds the Review-CVF operational metric envelope from mixed evidence modes", () => {
    const events = parseOperationalBenchmarkInput([
      JSON.stringify({
        executionId: "exec-live-1",
        runId: "run-live",
        eventType: "execution_requested",
        evidenceMode: "live",
        provider: "alibaba",
        model: "qwen-turbo",
        receiptId: "receipt-live",
        decision: "allow",
        enforcement: { status: "allow" },
      }),
      JSON.stringify({
        executionId: "exec-live-1",
        eventType: "retry",
        evidenceMode: "live",
        enforcement: { status: "retry" },
      }),
      JSON.stringify({
        executionId: "exec-offline-1",
        runId: "run-offline",
        eventType: "operator_correction",
        evidenceMode: "offline",
        correctedAt: "2026-05-22T00:00:00Z",
        correctionSource: "operator",
      }),
      JSON.stringify({
        executionId: "exec-offline-2",
        eventType: "rollback",
        evidenceMode: "offline",
        rolledBackAt: "2026-05-22T00:00:00Z",
        success: true,
      }),
    ].join("\n"));

    const report = buildOperationalBenchmarkReport(events, "audit.jsonl");

    expect(report.schemaVersion).toBe("cvf.operationalBenchmark.v1");
    expect(report.source).toMatchObject({
      input: "audit.jsonl",
      eventCount: 4,
      evidenceModes: ["live", "offline"],
      providerLanes: ["alibaba"],
      modelLanes: ["qwen-turbo"],
    });
    expect(report.metrics.retryCount).toEqual({ count: 1, total: 4 });
    expect(report.metrics.humanCorrectionCount).toEqual({ count: 1, total: 3 });
    expect(report.metrics.rollbackSuccessRate).toEqual({ rate: 1, count: 1, total: 1 });
    expect(report.evidenceModeBreakdown.map((entry) => entry.evidenceMode)).toEqual(["live", "offline"]);
    expect(report.deferredMetrics[0]).toMatchObject({
      metric: "hallucinationRecovery",
      status: "deferred",
    });
  });

  it("ingests release-gate JSON output with nested receipt evidence", () => {
    const events = parseOperationalBenchmarkInput(JSON.stringify({
      date: "2026-05-22",
      gate_result: "PASS",
      checks: [
        { name: "Web build", status: "PASS" },
        {
          name: "Live governance",
          status: "PASS",
          evidenceMode: "live",
          governanceEvidenceReceipt: {
            traceId: "trace-live",
            receiptId: "receipt-live",
            provider: "alibaba",
            model: "qwen-turbo",
            decision: "ALLOW",
          },
        },
      ],
    }));

    const report = buildOperationalBenchmarkReport(events);

    expect(events).toHaveLength(3);
    expect(report.source.evidenceModes).toEqual(["live", "unknown"]);
    expect(report.source.providerLanes).toEqual(["alibaba"]);
    expect(report.metrics.receiptIntegrityRate.count).toBe(1);
  });

  it("formats an operational report as a table with claim boundary", () => {
    const report = buildOperationalBenchmarkReport([
      {
        executionId: "exec-1",
        eventType: "execution_requested",
        evidenceMode: "fixture",
        receiptId: "receipt-1",
        decision: "allow",
        enforcement: { status: "allow" },
      },
    ]);

    const output = formatOperationalBenchmarkReport(report, "table");

    expect(output).toContain("CVF Operational Governance Benchmark");
    expect(output).toContain("retryCount 0/1");
    expect(output).toContain("deferred: hallucinationRecovery");
    expect(output).toContain("claimBoundary:");
  });

  it("runs cvf benchmark operational against JSONL", () => {
    const tempDir = mkdtempSync(join(tmpdir(), "cvf-operational-benchmark-"));
    const inputPath = join(tempDir, "audit.jsonl");
    writeFileSync(inputPath, [
      JSON.stringify({
        executionId: "exec-1",
        eventType: "execution_requested",
        evidenceMode: "live",
        provider: "alibaba",
        model: "qwen-turbo",
        receiptId: "receipt-1",
        decision: "allow",
        enforcement: { status: "allow" },
      }),
    ].join("\n"));

    try {
      const result = new CommandRegistry().execute({
        command: "benchmark",
        positional: ["operational"],
        flags: { input: inputPath, format: "json" },
      });

      expect(result.success).toBe(true);
      expect(JSON.parse(result.message)).toMatchObject({
        schemaVersion: "cvf.operationalBenchmark.v1",
        source: {
          evidenceModes: ["live"],
          providerLanes: ["alibaba"],
          modelLanes: ["qwen-turbo"],
        },
        metrics: {
          taskCompletionRate: { count: 1, total: 1 },
        },
      });
    } finally {
      rmSync(tempDir, { recursive: true, force: true });
    }
  });
});
