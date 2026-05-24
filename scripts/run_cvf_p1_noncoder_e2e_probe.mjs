#!/usr/bin/env node
/**
 * P1 non-coder/small-team production-readiness proof.
 *
 * Sends a signed hosted `/api/execute` request that follows the minimum
 * non-coder setup path: select a trusted template, provide plain-language
 * inputs, and verify a live governance receipt.
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
Act as a non-coder small-team user creating a first governed business brief.

CONTEXT:
The user selected the Strategy Analysis template, entered plain business notes, and needs a usable receipt-backed answer without reading source code.

SUCCESS CRITERIA:
- Produce a concise strategy brief
- Mention that a governance receipt should be retained
- Keep production-readiness language bounded to this proven small-team path
- Avoid enterprise SaaS, broad provider stability, or GA claims`,
    inputs: {
      topic: 'Small-team launch plan',
      context: 'A non-coder founder wants a short plan for testing a customer onboarding offer with five pilot customers.',
      options: 'Use strategy_analysis template\nUse Alibaba qwen-turbo\nExport or copy the governance receipt after execution',
      constraints: 'Plain-language output; no code required; do not claim broad production stability.',
      priority: 'P1 non-coder first receipt',
    },
    provider: 'alibaba',
    model: 'qwen-turbo',
    mode: 'simple',
    action: 'analyze',
    aiCommit: {
      commitId: 'p1-noncoder-production-readiness-2026-05-24',
      agentId: 'codex-p1-noncoder-proof',
      timestamp: Date.now(),
      description: 'P1 non-coder first governed receipt proof',
    },
  };
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
  const data = await response.json();
  const output = String(data.output ?? '');
  const receipt = data.governanceEvidenceReceipt ?? {};
  const envelope = data.governanceEnvelope ?? {};
  const routing = data.providerRouting ?? {};
  const assertions = {
    httpStatus200: response.status === 200,
    successTrue: data.success === true,
    outputUseful: output.length > 300 && !output.includes('MOCK_'),
    receiptPresent: typeof receipt.receiptId === 'string' && receipt.receiptId.length > 5,
    evidenceModeLive: receipt.evidenceMode === 'live' || envelope.evidenceMode === 'live',
    routeGoverned: receipt.routeId === '/api/execute' || envelope.routeId === '/api/execute',
    providerMatched: receipt.provider === 'alibaba' || routing.selectedProvider === 'alibaba',
    routingAllowed: receipt.routingDecision === 'ALLOW' || routing.decision === 'ALLOW',
    noMockFallback: !JSON.stringify(data).includes('mock_fallback') && !output.includes('MOCK_'),
  };
  const failedAssertions = Object.entries(assertions)
    .filter(([, passed]) => !passed)
    .map(([name]) => name);
  const proof = {
    schemaVersion: 'cvf-p1-noncoder-e2e-result-1',
    status: failedAssertions.length === 0 ? 'PASS' : 'FAIL',
    claimClass: failedAssertions.length === 0
      ? 'bounded_small_team_noncoder_production_path'
      : 'small_team_noncoder_production_path_blocked',
    target,
    httpStatus: response.status,
    latencyMs,
    templateId: payload.templateId,
    provider: receipt.provider ?? routing.selectedProvider ?? null,
    model: receipt.model ?? data.model ?? null,
    receiptId: receipt.receiptId ?? null,
    traceId: envelope.envelopeId ?? receipt.envelopeId ?? null,
    evidenceMode: receipt.evidenceMode ?? envelope.evidenceMode ?? null,
    routeId: receipt.routeId ?? envelope.routeId ?? null,
    decision: receipt.decision ?? data.enforcement?.status ?? null,
    routingDecision: receipt.routingDecision ?? routing.decision ?? null,
    outputLength: output.length,
    security: {
      signedServiceTokenAuthUsed: true,
      rawSecretPrinted: false,
      requestHeadersPrinted: false,
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
    schemaVersion: 'cvf-p1-noncoder-e2e-result-1',
    status: 'ERROR',
    error: error instanceof Error ? error.message : String(error),
  };
  assertNoSecretLeak(failure);
  console.error(JSON.stringify(failure, null, 2));
  process.exitCode = 1;
});
