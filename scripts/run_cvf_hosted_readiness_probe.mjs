#!/usr/bin/env node
/**
 * Hosted readiness smoke for the protected CVF `/api/execute` workflow.
 *
 * Loads operator-provided service token and provider keys from approved local
 * env files, signs a concrete request, and prints only sanitized response facts.
 */

import { createHmac } from 'node:crypto';
import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cvfWeb = path.join(repoRoot, 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web');
const envFiles = [
  path.join(cvfWeb, '.env.local'),
  path.join(cvfWeb, '.env'),
  path.join(repoRoot, '.env.local'),
  path.join(repoRoot, '.env'),
];

const secretNames = [
  'CVF_SERVICE_TOKEN',
  'DASHSCOPE_API_KEY',
  'ALIBABA_API_KEY',
  'CVF_ALIBABA_API_KEY',
  'CVF_BENCHMARK_ALIBABA_KEY',
  'DEEPSEEK_API_KEY',
  'OPENAI_API_KEY',
];

const DEFAULT_HOSTED_EXECUTE_URL = 'https://vibcode.netlify.app/api/execute';

function loadEnvFiles() {
  for (const envPath of envFiles) {
    if (!existsSync(envPath)) continue;
    for (const line of readFileSync(envPath, 'utf8').split(/\r?\n/)) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) continue;
      const [rawKey, ...rest] = trimmed.replace(/^export\s+/, '').split('=');
      const key = rawKey.trim();
      if (!key || process.env[key]) continue;
      let value = rest.join('=').trim();
      if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
        value = value.slice(1, -1);
      }
      process.env[key] = value;
    }
  }
}

function assertNoSecretLeak(value) {
  const serialized = JSON.stringify(value);
  for (const name of secretNames) {
    const secret = process.env[name];
    if (secret && secret.length > 8 && serialized.includes(secret)) {
      throw new Error(`secret_leak_detected:${name}`);
    }
  }
}

function buildPayload() {
  return {
    templateId: 'strategy_analysis',
    templateName: 'Strategy Analysis',
    intent: `INTENT:
Create a concise production-readiness smoke note for the CVF hosted protected workflow.

CONTEXT:
This is a live signed service-token request to the hosted CVF governance endpoint. The response must stay bounded to the evidence in this request.

SUCCESS CRITERIA:
- State whether the hosted protected workflow is reachable
- Mention governance receipt evidence
- Keep production-readiness claims bounded to this smoke proof
- Avoid claiming broad provider stability, public GA, or Maika end-user proof`,
    inputs: {
      topic: 'CVF hosted protected workflow readiness smoke',
      context: 'Signed hosted /api/execute call with service-token auth, live governance envelope, and receipt assertions.',
      options: 'Close bounded hosted smoke readiness\nHold production readiness pending observability and rollback packet\nEscalate if governance receipt is missing',
      constraints: 'Do not overclaim public runtime availability beyond this hosted protected workflow smoke.',
      priority: 'C5 hosted readiness proof',
    },
    provider: 'alibaba',
    model: 'qwen-turbo',
    mode: 'simple',
    action: 'analyze',
    aiCommit: {
      commitId: 'c5-hosted-readiness-smoke-2026-05-24',
      agentId: 'codex-c5-hosted-readiness',
      timestamp: Date.now(),
      description: 'C5 hosted protected workflow readiness smoke',
    },
  };
}

function classifyFailure(assertions) {
  if (!assertions.httpStatus200) return 'http_status_failure';
  if (!assertions.successTrue) return 'execute_failure';
  if (!assertions.receiptPresent || !assertions.envelopeLive) return 'governance_receipt_failure';
  if (!assertions.routeGoverned) return 'route_governance_failure';
  if (!assertions.providerMatched || !assertions.routingAllowed) return 'provider_routing_failure';
  if (!assertions.outputNonMock || !assertions.noMockFallback) return 'mock_or_output_failure';
  return null;
}

async function main() {
  loadEnvFiles();
  const token = process.env.CVF_SERVICE_TOKEN;
  if (!token) throw new Error('missing_cvf_service_token');

  const target = process.env.CVF_HOSTED_EXECUTE_URL
    ?? process.env.CVF_EXECUTE_URL
    ?? DEFAULT_HOSTED_EXECUTE_URL;
  const payload = buildPayload();
  const bodyText = JSON.stringify(payload);
  const timestamp = String(Date.now());
  const signature = createHmac('sha256', token)
    .update(`${timestamp}.${bodyText}`)
    .digest('hex');

  const startedAt = Date.now();
  const response = await fetch(target, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-cvf-service-token': token,
      'x-cvf-service-timestamp': timestamp,
      'x-cvf-service-signature': signature,
    },
    body: bodyText,
  });
  const latencyMs = Date.now() - startedAt;

  let data = {};
  try {
    data = await response.json();
  } catch (error) {
    data = { parseError: String(error) };
  }

  const output = String(data.output ?? '');
  const receipt = data.governanceEvidenceReceipt ?? {};
  const envelope = data.governanceEnvelope ?? {};
  const routing = data.providerRouting ?? {};
  const assertions = {
    httpStatus200: response.status === 200,
    successTrue: data.success === true,
    outputNonMock: output.length > 100 && !output.includes('MOCK_'),
    receiptPresent: typeof receipt.receiptId === 'string' && receipt.receiptId.length > 5,
    envelopeLive: envelope.evidenceMode === 'live' || receipt.evidenceMode === 'live',
    routeGoverned: envelope.routeId === '/api/execute' && receipt.routeId === '/api/execute',
    providerMatched: receipt.provider === 'alibaba' || routing.selectedProvider === 'alibaba',
    routingAllowed: routing.decision === 'ALLOW' || receipt.routingDecision === 'ALLOW',
    noMockFallback: !JSON.stringify(data).includes('mock_fallback') && !output.includes('MOCK_'),
  };
  const failedAssertions = Object.entries(assertions)
    .filter(([, passed]) => !passed)
    .map(([name]) => name);

  const proof = {
    schemaVersion: 'cvf-hosted-readiness-smoke-result-1',
    status: failedAssertions.length === 0 ? 'PASS' : 'FAIL',
    claimClass: failedAssertions.length === 0
      ? 'bounded_hosted_protected_workflow_readiness_smoke'
      : 'hosted_readiness_blocked',
    target,
    httpStatus: response.status,
    latencyMs,
    failureClass: classifyFailure(assertions),
    receiptId: receipt.receiptId ?? null,
    traceId: envelope.envelopeId ?? receipt.envelopeId ?? null,
    policySnapshotId: receipt.policySnapshotId ?? envelope.policySnapshotId ?? data.policySnapshotId ?? null,
    evidenceMode: receipt.evidenceMode ?? envelope.evidenceMode ?? null,
    routeId: receipt.routeId ?? envelope.routeId ?? null,
    provider: receipt.provider ?? routing.selectedProvider ?? null,
    model: receipt.model ?? data.model ?? null,
    decision: receipt.decision ?? data.enforcement?.status ?? null,
    routingDecision: receipt.routingDecision ?? routing.decision ?? null,
    outputLength: output.length,
    observability: {
      traceIdPresent: Boolean(envelope.envelopeId ?? receipt.envelopeId),
      receiptIdPresent: typeof receipt.receiptId === 'string' && receipt.receiptId.length > 5,
      policySnapshotPresent: Boolean(receipt.policySnapshotId ?? envelope.policySnapshotId ?? data.policySnapshotId),
    },
    security: {
      signedServiceTokenAuthUsed: true,
      rawSecretPrinted: false,
      requestHeadersPrinted: false,
    },
    rollbackBoundary: {
      fallback: 'disable hosted protected workflow consumers or revert endpoint target to last passing deployment',
      incidentTrigger: 'missing receipt, non-live evidence, auth failure, provider routing mismatch, or mock fallback',
    },
    assertions,
    failedAssertions,
  };

  assertNoSecretLeak(proof);
  console.log(JSON.stringify(proof, null, 2));
  process.exitCode = proof.status === 'PASS' ? 0 : 1;
}

main().catch((error) => {
  const failure = {
    schemaVersion: 'cvf-hosted-readiness-smoke-result-1',
    status: 'ERROR',
    error: error instanceof Error ? error.message : String(error),
  };
  assertNoSecretLeak(failure);
  console.error(JSON.stringify(failure, null, 2));
  process.exitCode = 1;
});
