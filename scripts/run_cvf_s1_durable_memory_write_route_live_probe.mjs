#!/usr/bin/env node
import { createHmac } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, rmSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cvfWeb = path.join(repoRoot, 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web');
const envFiles = [path.join(cvfWeb, '.env.local'), path.join(cvfWeb, '.env'), path.join(repoRoot, '.env.local'), path.join(repoRoot, '.env')];
const secretNames = ['CVF_SERVICE_TOKEN', 'DASHSCOPE_API_KEY', 'ALIBABA_API_KEY', 'CVF_ALIBABA_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY'];
const port = Number(process.env.CVF_S1_DURABLE_MEMORY_PORT ?? 3227);
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

function buildChildEnv(storePath) {
  const childEnv = {};
  for (const [key, value] of Object.entries(process.env)) {
    if (typeof value === 'string' && !value.includes('\u0000')) childEnv[key] = value;
  }
  childEnv.CVF_SERVICE_TOKEN = process.env.CVF_SERVICE_TOKEN;
  childEnv.DASHSCOPE_API_KEY = process.env.DASHSCOPE_API_KEY;
  childEnv.CVF_DURABLE_MEMORY_STORE_PATH = storePath;
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
    intent: 'Create a bounded S1 durable memory write proof note. Do not claim autonomous reinjection or raw memory release.',
    inputs: {
      topic: 'S1 durable memory write route',
      context: 'The route may write a summary-only skill memory after successful governed execution.',
      options: 'Close S1 if write receipt is allowed\nHold if receipt missing\nBlock if raw memory released',
      constraints: 'Summary-only memory; canReinject remains false; no hosted/cloud persistence claim.',
      priority: 'R1',
    },
    provider: 'alibaba',
    model: 'qwen-turbo',
    mode: 'governance',
    cvfPhase: 'PHASE D',
    cvfRiskLevel: 'R1',
    action: 'test',
    skillPreflightPassed: true,
    skillPreflightDeclaration: 'S1 live probe declares bounded strategy_analysis execution before provider dispatch.',
    skillPreflightRecordRef: 's1-durable-memory-write-route-live-probe',
    skillIds: ['strategy_analysis'],
    aiCommit: {
      commitId: 's1-durable-memory-write-route-live-probe',
      agentId: 'codex-s1-live-probe',
      timestamp: Date.now(),
      description: 'Bounded S1 durable memory write route proof',
    },
    durableMemoryWrite: {
      enabled: true,
      tier: 'skill',
      scope: 'project:s1-route',
      policy: { actorAuthorized: true },
      maxSummaryLength: 240,
    },
  };
}

async function main() {
  loadEnvFiles();
  if (!process.env.CVF_SERVICE_TOKEN) throw new Error('missing_cvf_service_token');
  if (!process.env.DASHSCOPE_API_KEY) throw new Error('missing_dashscope_api_key');

  const tempDir = path.join(os.tmpdir(), `cvf-s1-live-${Date.now()}`);
  mkdirSync(tempDir, { recursive: true });
  const storePath = path.join(tempDir, 'durable-memory.json');
  const server = spawn(process.platform === 'win32' ? 'npm.cmd' : 'npm', ['run', 'dev', '--', '--port', String(port)], {
    cwd: cvfWeb,
    env: buildChildEnv(storePath),
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
    const writeReceipt = data.durableMemoryWriteReceipt ?? receipt.durableMemoryWriteReceipt ?? {};
    const records = existsSync(storePath) ? JSON.parse(readFileSync(storePath, 'utf8')) : [];
    const assertions = {
      httpStatus200: response.status === 200,
      successTrue: data.success === true,
      executionReceiptPresent: typeof receipt.receiptId === 'string',
      evidenceModeLive: receipt.evidenceMode === 'live',
      writeReceiptAllowed: writeReceipt.operation === 'write' && writeReceipt.decision === 'allowed',
      rawMemoryReleasedFalse: writeReceipt.rawMemoryReleased === false,
      canReinjectFalse: writeReceipt.canReinject === false,
      recordPersisted: Array.isArray(records) && records.length === 1 && records[0]?.scope === 'project:s1-route',
      summaryOnlyRecord: typeof records[0]?.summary === 'string' && records[0].summary.length <= 280,
    };
    const failedAssertions = Object.entries(assertions).filter(([, passed]) => !passed).map(([name]) => name);
    const proof = {
      schemaVersion: 'cvf-s1-durable-memory-write-route-live-result-1',
      status: failedAssertions.length === 0 ? 'PASS' : 'FAIL',
      httpStatus: response.status,
      latencyMs,
      provider: receipt.provider ?? null,
      model: receipt.model ?? data.model ?? null,
      error: data.error ?? null,
      guardResult: data.guardResult ?? null,
      receiptId: receipt.receiptId ?? null,
      traceId: receipt.envelopeId ?? data.governanceEnvelope?.envelopeId ?? null,
      evidenceMode: receipt.evidenceMode ?? null,
      durableMemoryWriteReceipt: {
        decision: writeReceipt.decision ?? null,
        reason: writeReceipt.reason ?? null,
        memoryIds: writeReceipt.memoryIds ?? [],
        rawMemoryReleased: writeReceipt.rawMemoryReleased ?? null,
        canReinject: writeReceipt.canReinject ?? null,
      },
      persistedRecordCount: Array.isArray(records) ? records.length : 0,
      security: { rawSecretPrinted: false, requestHeadersPrinted: false },
      assertions,
      failedAssertions,
    };
    assertNoSecretLeak(proof);
    console.log(JSON.stringify(proof, null, 2));
    process.exitCode = proof.status === 'PASS' ? 0 : 1;
  } catch (error) {
    const failure = { schemaVersion: 'cvf-s1-durable-memory-write-route-live-result-1', status: 'ERROR', error: error instanceof Error ? error.message : String(error), serverTail: redact(serverTail) };
    assertNoSecretLeak(failure);
    console.error(JSON.stringify(failure, null, 2));
    process.exitCode = 1;
  } finally {
    killProcessTree(server);
    rmSync(tempDir, { recursive: true, force: true });
  }
}

main();
