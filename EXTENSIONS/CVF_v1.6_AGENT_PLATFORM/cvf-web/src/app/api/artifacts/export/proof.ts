const GOVERNANCE_EVALUATE_URL = '/api/governance/evaluate';
const PROOF_TIMEOUT_MS = 4000;

export interface GovernanceReceipt {
  receiptId: string;
  decision: string;
  evaluatedAt: string;
  riskLevel: string;
}

interface EvaluateResponseData {
  report?: {
    status?: string;
    risk_level?: string;
    cvf_enforcement?: { action?: string };
    request_summary?: { request_id?: string; artifact_id?: string };
    decision_analysis?: { final_decision?: string };
    report_metadata?: { generated_at?: string };
    cvf_risk_level?: string;
    integrity?: { has_ledger_reference?: boolean };
  };
  execution_record?: {
    request_id?: string;
    timestamp?: string;
    final_decision?: string;
    ledger_attached?: boolean;
  };
  [key: string]: unknown;
}

interface EvaluateResponse {
  success: boolean;
  data?: EvaluateResponseData;
}

function isAbsoluteUrl(url: string): boolean {
  return url.startsWith('http://') || url.startsWith('https://');
}

function resolveEvaluateUrl(base: string): string {
  if (isAbsoluteUrl(base)) return base;
  if (typeof process !== 'undefined' && process.env.NEXTAUTH_URL) {
    return `${process.env.NEXTAUTH_URL.replace(/\/$/, '')}${base}`;
  }
  return base;
}

export async function fetchGovernanceReceipt(
  artifactId: string,
  sourceContent: string,
  serviceToken?: string,
): Promise<GovernanceReceipt | null> {
  const url = resolveEvaluateUrl(GOVERNANCE_EVALUATE_URL);

  if (!isAbsoluteUrl(url)) {
    return null;
  }

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), PROOF_TIMEOUT_MS);

  try {
    const headers: Record<string, string> = { 'Content-Type': 'application/json' };
    if (serviceToken) headers['x-cvf-service-token'] = serviceToken;

    const requestId = `artifact-proof-${artifactId}-${Date.now()}`;
    const response = await fetch(url, {
      method: 'POST',
      headers,
      signal: controller.signal,
      body: JSON.stringify({
        request_id: requestId,
        artifact_id: artifactId,
        payload: { content: sourceContent.slice(0, 500) },
        cvf_phase: 'REVIEW',
        cvf_risk_level: 'R0',
      }),
    });

    if (!response.ok) return null;

    const payload = await response.json() as EvaluateResponse;
    if (payload.success !== true || !payload.data) return null;

    const data = payload.data;
    // Current Governance Engine reports the request identity and decision in
    // nested report sections; its execution record does not repeat the ID.
    const report = data.report;
    const engineDecision = report?.decision_analysis?.final_decision;
    if (report?.request_summary) {
      if (report.request_summary.request_id !== requestId ||
        report.request_summary.artifact_id !== artifactId ||
        !['ALLOW', 'DENY', 'REVIEW', 'ESCALATE', 'SANDBOX'].includes(String(engineDecision)) ||
        data.execution_record?.final_decision !== engineDecision ||
        data.execution_record?.ledger_attached !== true ||
        report.integrity?.has_ledger_reference !== true ||
        typeof report.report_metadata?.generated_at !== 'string' || !report.report_metadata.generated_at ||
        typeof report.cvf_risk_level !== 'string' || !/^R[0-4]$/.test(report.cvf_risk_level)) return null;
      return {
        receiptId: requestId,
        decision: engineDecision as string,
        evaluatedAt: report.report_metadata.generated_at,
        riskLevel: report.cvf_risk_level,
      };
    }

    // Retain the older explicit approval envelope for compatible callers.
    const status = data.report?.status;
    if (data.execution_record?.request_id !== requestId ||
      !['APPROVED', 'MANUAL_REVIEW', 'REJECTED', 'FROZEN'].includes(String(status)) ||
      typeof data.execution_record.timestamp !== 'string' || !data.execution_record.timestamp ||
      typeof data.report?.risk_level !== 'string' || !data.report.risk_level ||
      (status === 'APPROVED' && data.report.cvf_enforcement?.action !== 'ALLOW')) return null;
    return {
      receiptId: requestId,
      decision: status as string,
      evaluatedAt: data.execution_record.timestamp,
      riskLevel: data.report.risk_level,
    };
  } catch {
    return null;
  } finally {
    clearTimeout(timer);
  }
}
