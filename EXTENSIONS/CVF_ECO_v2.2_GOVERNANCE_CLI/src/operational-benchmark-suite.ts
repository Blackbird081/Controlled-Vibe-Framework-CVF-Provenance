import {
  computeGovernanceReliabilityReport,
  humanCorrectionCount,
  parseAuditJsonl,
  policyViolationRate,
  receiptIntegrityRate,
  retryCount,
  rollbackSuccessRate,
  taskCompletionRate,
  type AuditEvent,
  type MetricResult,
} from "./governance-reliability-metrics";

export type OperationalBenchmarkEvidenceMode = "live" | "offline" | "fixture" | "unknown";

export interface CountMetricResult {
  readonly count: number;
  readonly total: number;
}

export interface OperationalBenchmarkMetrics {
  readonly taskCompletionRate: MetricResult;
  readonly retryCount: CountMetricResult;
  readonly policyViolationRate: MetricResult;
  readonly humanCorrectionCount: CountMetricResult;
  readonly crossSessionContinuityRate: MetricResult;
  readonly longHorizonStabilityRate: MetricResult;
  readonly receiptIntegrityRate: MetricResult;
  readonly deterministicConsistencyRate: MetricResult;
  readonly rollbackSuccessRate: MetricResult;
}

export interface OperationalBenchmarkModeBreakdown {
  readonly evidenceMode: OperationalBenchmarkEvidenceMode;
  readonly eventCount: number;
  readonly taskCompletionRate: MetricResult;
  readonly policyViolationRate: MetricResult;
  readonly receiptIntegrityRate: MetricResult;
}

export interface DeferredOperationalMetric {
  readonly metric: "hallucinationRecovery";
  readonly status: "deferred";
  readonly replacementMetrics: readonly string[];
  readonly reason: string;
}

export interface OperationalBenchmarkReport {
  readonly schemaVersion: "cvf.operationalBenchmark.v1";
  readonly source: {
    readonly input?: string;
    readonly eventCount: number;
    readonly evidenceModes: readonly OperationalBenchmarkEvidenceMode[];
    readonly providerLanes: readonly string[];
    readonly modelLanes: readonly string[];
  };
  readonly metrics: OperationalBenchmarkMetrics;
  readonly evidenceModeBreakdown: readonly OperationalBenchmarkModeBreakdown[];
  readonly deferredMetrics: readonly DeferredOperationalMetric[];
  readonly claimBoundary: string;
}

export function parseOperationalBenchmarkInput(content: string): AuditEvent[] {
  const trimmed = content.trim();
  if (!trimmed) return [];
  if (trimmed.startsWith("{") || trimmed.startsWith("[")) {
    try {
      return extractOperationalEvents(JSON.parse(trimmed));
    } catch {
      return parseAuditJsonl(content);
    }
  }
  return parseAuditJsonl(content);
}

export function buildOperationalBenchmarkReport(
  events: AuditEvent[],
  input?: string,
): OperationalBenchmarkReport {
  const reliability = computeGovernanceReliabilityReport(events);
  const modes = uniqueSorted(events.map(readEvidenceMode));
  const providerLanes = uniqueSorted(events.map((event) => readString(event.provider)));
  const modelLanes = uniqueSorted(events.map((event) => readString(event.model)));

  return {
    schemaVersion: "cvf.operationalBenchmark.v1",
    source: {
      input,
      eventCount: events.length,
      evidenceModes: modes.length ? modes : ["unknown"],
      providerLanes,
      modelLanes,
    },
    metrics: {
      taskCompletionRate: reliability.taskCompletionRate,
      retryCount: { count: retryCount(events), total: events.length },
      policyViolationRate: reliability.policyViolationRate,
      humanCorrectionCount: { count: humanCorrectionCount(events), total: distinctExecutionTotal(events) },
      crossSessionContinuityRate: reliability.crossSessionContinuityRate,
      longHorizonStabilityRate: reliability.longHorizonStabilityRate,
      receiptIntegrityRate: reliability.receiptIntegrityRate,
      deterministicConsistencyRate: reliability.deterministicConsistencyRate,
      rollbackSuccessRate: reliability.rollbackSuccessRate,
    },
    evidenceModeBreakdown: buildEvidenceModeBreakdown(events),
    deferredMetrics: [
      {
        metric: "hallucinationRecovery",
        status: "deferred",
        replacementMetrics: ["policyViolationRate", "humanCorrectionCount", "rollbackSuccessRate"],
        reason: "No bounded hallucination-recovery event contract exists in the current private baseline.",
      },
    ],
    claimBoundary: "Operational benchmark foundation only; report does not prove broad provider reliability or output quality.",
  };
}

export function formatOperationalBenchmarkReport(
  report: OperationalBenchmarkReport,
  format: "json" | "table",
): string {
  if (format === "json") {
    return JSON.stringify(report, null, 2);
  }
  return [
    "CVF Operational Governance Benchmark",
    "====================================",
    `schemaVersion: ${report.schemaVersion}`,
    `events: ${report.source.eventCount}`,
    `evidenceModes: ${report.source.evidenceModes.join(", ")}`,
    `providerLanes: ${report.source.providerLanes.join(", ") || "n/a"}`,
    `modelLanes: ${report.source.modelLanes.join(", ") || "n/a"}`,
    "",
    "metric value",
    `taskCompletionRate ${formatRate(report.metrics.taskCompletionRate.rate)}`,
    `retryCount ${report.metrics.retryCount.count}/${report.metrics.retryCount.total}`,
    `policyViolationRate ${formatRate(report.metrics.policyViolationRate.rate)}`,
    `humanCorrectionCount ${report.metrics.humanCorrectionCount.count}/${report.metrics.humanCorrectionCount.total}`,
    `crossSessionContinuityRate ${formatRate(report.metrics.crossSessionContinuityRate.rate)}`,
    `longHorizonStabilityRate ${formatRate(report.metrics.longHorizonStabilityRate.rate)}`,
    `receiptIntegrityRate ${formatRate(report.metrics.receiptIntegrityRate.rate)}`,
    `deterministicConsistencyRate ${formatRate(report.metrics.deterministicConsistencyRate.rate)}`,
    `rollbackSuccessRate ${formatRate(report.metrics.rollbackSuccessRate.rate)}`,
    "",
    "evidenceModeBreakdown",
    ...report.evidenceModeBreakdown.map((entry) => {
      return `${entry.evidenceMode}: events=${entry.eventCount} task=${formatRate(entry.taskCompletionRate.rate)} policy=${formatRate(entry.policyViolationRate.rate)} receipt=${formatRate(entry.receiptIntegrityRate.rate)}`;
    }),
    "",
    `deferred: hallucinationRecovery -> ${report.deferredMetrics[0]?.replacementMetrics.join(", ")}`,
    `claimBoundary: ${report.claimBoundary}`,
  ].join("\n");
}

function extractOperationalEvents(value: unknown): AuditEvent[] {
  if (Array.isArray(value)) {
    return value.flatMap(extractOperationalEvents);
  }
  if (!isRecord(value)) return [];
  if (isAuditEventLike(value)) {
    const receiptEvent = extractReceiptEvent(value);
    return receiptEvent ? [normalizeOperationalEvent(value), receiptEvent] : [normalizeOperationalEvent(value)];
  }

  const directContainers = ["events", "records", "auditEvents", "checks", "results"];
  const events = directContainers.flatMap((key) => extractOperationalEvents(value[key]));
  const receiptEvent = extractReceiptEvent(value);
  return receiptEvent ? [...events, receiptEvent] : events;
}

function normalizeOperationalEvent(value: Record<string, unknown>): AuditEvent {
  return {
    ...value,
    executionId: readString(value.executionId) ?? readString(value.traceId) ?? readString(value.runId),
    receiptId: readString(value.receiptId) ?? readString(value.governanceReceiptId),
    decision: normalizeDecision(value),
    evidenceMode: readEvidenceMode(value),
    provider: readString(value.provider),
    model: readString(value.model),
    enforcement: isRecord(value.enforcement) ? value.enforcement as AuditEvent["enforcement"] : value.enforcement === "allow"
      ? { status: "allow" }
      : undefined,
  };
}

function extractReceiptEvent(value: Record<string, unknown>): AuditEvent | null {
  const receipt = isRecord(value.governanceEvidenceReceipt)
    ? value.governanceEvidenceReceipt
    : isRecord(value.receipt)
      ? value.receipt
      : null;
  if (!receipt) return null;

  return {
    eventType: "receipt_emitted",
    executionId: readString(receipt.traceId) ?? readString(value.traceId),
    receiptId: readString(receipt.receiptId) ?? readString(value.receiptId),
    decision: "captured",
    evidenceMode: readEvidenceMode(value),
    provider: readString(receipt.provider) ?? readString(value.provider),
    model: readString(receipt.model) ?? readString(value.model),
    enforcement: { status: normalizeDecision(receipt) === "allow" ? "allow" : "deny" },
    timestamp: readString(value.timestamp) ?? readString(value.date),
  };
}

function buildEvidenceModeBreakdown(events: AuditEvent[]): OperationalBenchmarkModeBreakdown[] {
  const groups = new Map<OperationalBenchmarkEvidenceMode, AuditEvent[]>();
  events.forEach((event) => {
    const mode = readEvidenceMode(event);
    groups.set(mode, [...(groups.get(mode) ?? []), event]);
  });
  return [...groups.entries()]
    .sort(([left], [right]) => left.localeCompare(right))
    .map(([evidenceMode, group]) => ({
      evidenceMode,
      eventCount: group.length,
      taskCompletionRate: taskCompletionRate(group),
      policyViolationRate: policyViolationRate(group),
      receiptIntegrityRate: receiptIntegrityRate(group),
    }));
}

function isAuditEventLike(value: Record<string, unknown>): boolean {
  return Boolean(
    value.eventType
    || value.type
    || value.executionId
    || value.runId
    || value.receiptId
    || value.enforcement
    || value.decision
    || value.status
    || value.governanceEvidenceReceipt
    || value.receipt,
  );
}

function normalizeDecision(value: Record<string, unknown>): string | null {
  const raw = readString(value.decision) ?? readString(value.routingDecision) ?? readString(value.status);
  if (!raw) return null;
  const lower = raw.toLowerCase();
  if (lower === "allow" || lower === "allowed" || lower === "pass" || lower === "passed") return "allow";
  if (lower === "deny" || lower === "blocked" || lower === "fail" || lower === "failed") return "deny";
  if (lower === "captured") return "captured";
  return lower;
}

function readEvidenceMode(value: Record<string, unknown> | AuditEvent): OperationalBenchmarkEvidenceMode {
  const record = value as Record<string, unknown>;
  const raw = readString(record.evidenceMode) ?? readString(record.mode);
  if (raw === "live" || raw === "offline" || raw === "fixture") return raw;
  return "unknown";
}

function distinctExecutionTotal(events: AuditEvent[]): number {
  const keys = new Set(
    events
      .map((event) => readString(event.executionId) ?? readString(event.runId))
      .filter((value): value is string => Boolean(value)),
  );
  return keys.size || events.length;
}

function uniqueSorted<T extends string>(values: Array<T | undefined>): T[] {
  return [...new Set(values.filter((value): value is T => Boolean(value)))].sort();
}

function formatRate(rate: number | null): string {
  return rate === null ? "n/a" : rate.toFixed(3);
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === "object" && !Array.isArray(value);
}

function readString(value: unknown): string | undefined {
  return typeof value === "string" && value.trim() ? value.trim() : undefined;
}
