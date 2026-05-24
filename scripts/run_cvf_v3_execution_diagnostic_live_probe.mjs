#!/usr/bin/env node
import { createHmac } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cvfWeb = path.join(repoRoot, 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web');
const envFiles = [path.join(cvfWeb, '.env.local'), path.join(cvfWeb, '.env'), path.join(repoRoot, '.env.local'), path.join(repoRoot, '.env')];
const secretNames = ['CVF_SERVICE_TOKEN', 'DASHSCOPE_API_KEY', 'ALIBABA_API_KEY', 'CVF_ALIBABA_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY'];
const port = Number(process.env.CVF_V3_DIAGNOSTIC_PORT ?? 3233);
const baseUrl = `http://127.0.0.1:${port}`;

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
      if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) value = value.slice(1, -1);
      process.env[key] = value;
    }
  }
  const alias = process.env.ALIBABA_API_KEY ?? process.env.CVF_ALIBABA_API_KEY ?? process.env.CVF_BENCHMARK_ALIBABA_KEY;
  if (!process.env.DASHSCOPE_API_KEY && alias) process.env.DASHSCOPE_API_KEY = alias;
}

function assertNoSecretLeak(value) {
  const serialized = JSON.stringify(value);
  for (const name of secretNames) {
    const secret = process.env[name];
    if (secret && secret.length > 8 && serialized.includes(secret)) throw new Error(`secret_leak_detected:${name}`);
  }
}

function redact(value) {
  let redacted = String(value ?? '');
  for (const name of secretNames) {
    const secret = process.env[name];
    if (secret && secret.length > 8) redacted = redacted.split(secret).join('<redacted>');
  }
  return redacted.slice(-1600);
}

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function buildChildEnv() {
  const childEnv = {};
  for (const [key, value] of Object.entries(process.env)) {
    if (typeof value === 'string' && !value.includes('\u0000')) childEnv[key] = value;
  }
  childEnv.CVF_SERVICE_TOKEN = process.env.CVF_SERVICE_TOKEN;
  childEnv.DASHSCOPE_API_KEY = process.env.DASHSCOPE_API_KEY;
  childEnv.CVF_AI_PROVIDER_TIMEOUT_MS = process.env.CVF_AI_PROVIDER_TIMEOUT_MS ?? '30000';
  childEnv.CVF_PLAYWRIGHT_PORT = String(port);
  childEnv.PORT = String(port);
  return childEnv;
}

async function waitForServer(proc) {
  const startedAt = Date.now();
  while (Date.now() - startedAt < 120_000) {
    if (proc.exitCode !== null) throw new Error(`dev_server_exited:${proc.exitCode}`);
    try {
      const response = await fetch(`${baseUrl}/login`);
      if (response.status < 500) return;
    } catch {}
    await delay(1000);
  }
  throw new Error('dev_server_start_timeout');
}

function killProcessTree(proc) {
  if (proc.exitCode !== null || !proc.pid) return;
  if (process.platform === 'win32') spawnSync('taskkill.exe', ['/PID', String(proc.pid), '/T', '/F'], { stdio: 'ignore' });
  else proc.kill('SIGTERM');
}

function buildPayload() {
  return {
    templateId: 'strategy_analysis',
    templateName: 'Strategy Analysis',
    intent: 'Create a short V3 diagnostic proof note for a provider boundary check.',
    inputs: {
      topic: 'V3 execution diagnostic contract',
      context: 'The route should return a classified diagnostic if the selected provider lane cannot complete.',
      options: 'Record diagnostic\nPreserve receipt evidence\nKeep the output redacted',
      constraints: 'Redacted proof only; no provider stability claim.',
      priority: 'R1',
    },
    provider: 'alibaba',
    model: 'qwen-v3-diagnostic-intentionally-unavailable',
    mode: 'governance',
    cvfPhase: 'PHASE D',
    cvfRiskLevel: 'R1',
    action: 'test',
    skillPreflightPassed: true,
    skillPreflightDeclaration: 'V3 live diagnostic probe declares a bounded provider-boundary check with redacted output.',
    skillPreflightRecordRef: 'v3-execution-diagnostic-live-probe',
    skillIds: ['strategy_analysis'],
    aiCommit: {
      commitId: 'v3-execution-diagnostic-live-probe',
      agentId: 'codex-v3-live-probe',
      timestamp: Date.now(),
      description: 'Bounded V3 diagnostic proof with provider-boundary classification',
    },
  };
}

async function main() {
  loadEnvFiles();
  if (!process.env.CVF_SERVICE_TOKEN) throw new Error('missing_cvf_service_token');
  if (!process.env.DASHSCOPE_API_KEY) throw new Error('missing_dashscope_api_key');

  const server = spawn(process.platform === 'win32' ? 'npm.cmd' : 'npm', ['run', 'dev', '--', '--port', String(port)], {
    cwd: cvfWeb,
    env: buildChildEnv(),
    stdio: ['ignore', 'pipe', 'pipe'],
    shell: process.platform === 'win32',
  });
  let serverTail = '';
  const appendTail = (chunk) => { serverTail = `${serverTail}${chunk.toString()}`.slice(-4000); };
  server.stdout.on('data', appendTail);
  server.stderr.on('data', appendTail);

  try {
    await waitForServer(server);
    const bodyText = JSON.stringify(buildPayload());
    const timestamp = String(Date.now());
    const signature = createHmac('sha256', process.env.CVF_SERVICE_TOKEN).update(`${timestamp}.${bodyText}`).digest('hex');
    const startedAt = Date.now();
    const response = await fetch(`${baseUrl}/api/execute`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-cvf-service-token': process.env.CVF_SERVICE_TOKEN,
        'x-cvf-service-timestamp': timestamp,
        'x-cvf-service-signature': signature,
      },
      body: bodyText,
    });
    const latencyMs = Date.now() - startedAt;
    const data = await response.json();
    const receipt = data.governanceEvidenceReceipt ?? {};
    const diagnostic = data.diagnostic ?? {};
    const assertions = {
      liveRouteReached: response.status === 200,
      intentionalFailure: data.success === false,
      diagnosticPresent: diagnostic.contractVersion === 'cvf.executionDiagnostic.v1',
      diagnosticClassified: typeof diagnostic.class === 'string' && diagnostic.class.length > 0,
      diagnosticActionable: typeof diagnostic.userAction === 'string' && diagnostic.userAction.length > 0,
      diagnosticSecretSafe: typeof diagnostic.safeMessage === 'string' && !/sk-|Bearer|api[_-]?key|token|signature/i.test(diagnostic.safeMessage),
      receiptPresent: typeof receipt.receiptId === 'string',
      receiptLive: receipt.evidenceMode === 'live',
      rawSecretPrintedFalse: true,
    };
    const failedAssertions = Object.entries(assertions).filter(([, passed]) => !passed).map(([name]) => name);
    const proof = {
      schemaVersion: 'cvf-v3-execution-diagnostic-live-result-1',
      status: failedAssertions.length === 0 ? 'PASS' : 'FAIL',
      httpStatus: response.status,
      latencyMs,
      provider: receipt.provider ?? data.provider ?? null,
      model: receipt.model ?? data.model ?? null,
      success: data.success ?? null,
      errorClass: diagnostic.class ?? null,
      userAction: diagnostic.userAction ?? null,
      retryable: diagnostic.retryable ?? null,
      safeMessage: diagnostic.safeMessage ?? null,
      receiptId: receipt.receiptId ?? null,
      traceId: receipt.envelopeId ?? data.governanceEnvelope?.envelopeId ?? null,
      evidenceMode: receipt.evidenceMode ?? null,
      security: { rawSecretPrinted: false, requestHeadersPrinted: false },
      assertions,
      failedAssertions,
    };
    assertNoSecretLeak(proof);
    console.log(JSON.stringify(proof, null, 2));
    process.exitCode = proof.status === 'PASS' ? 0 : 1;
  } catch (error) {
    const failure = { schemaVersion: 'cvf-v3-execution-diagnostic-live-result-1', status: 'ERROR', error: error instanceof Error ? error.message : String(error), serverTail: redact(serverTail) };
    assertNoSecretLeak(failure);
    console.error(JSON.stringify(failure, null, 2));
    process.exitCode = 1;
  } finally {
    killProcessTree(server);
  }
}

main();
