#!/usr/bin/env node
/**
 * R2 durable memory route live proof.
 *
 * Starts the local CVF web app and performs one signed, live-provider
 * `/api/execute` call that reads summary-only durable memory from the route
 * file-backed store.
 */

import { createHmac } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import os from 'node:os';
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
];

const port = Number(process.env.CVF_R2_DURABLE_MEMORY_PORT ?? 3223);
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
      if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
        value = value.slice(1, -1);
      }
      process.env[key] = value;
    }
  }
  const alias = process.env.ALIBABA_API_KEY
    ?? process.env.CVF_ALIBABA_API_KEY
    ?? process.env.CVF_BENCHMARK_ALIBABA_KEY;
  if (!process.env.DASHSCOPE_API_KEY && alias) process.env.DASHSCOPE_API_KEY = alias;
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

function createDurableMemoryStore() {
  const tempDir = path.join(os.tmpdir(), `cvf-r2-live-${Date.now()}`);
  mkdirSync(tempDir, { recursive: true });
  const storePath = path.join(tempDir, 'durable-memory.json');
  writeFileSync(storePath, `${JSON.stringify([
    {
      id: 'r2-skill-safe',
      tier: 'skill',
      scope: 'project:r2-route',
      actorId: 'operator-1',
      summary: 'durable-route-memory: Use strategy_analysis for first-receipt setup and keep durable-memory claims summary-only.',
      lifecycleState: 'semantic',
      provenanceScore: 0.97,
      createdAt: Date.now(),
      updatedAt: Date.now(),
    },
  ], null, 2)}\n`, 'utf8');
  return { tempDir, storePath };
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
    } catch {
      // still booting
    }
    await delay(1000);
  }
  throw new Error('dev_server_start_timeout');
}

function killProcessTree(proc) {
  if (proc.exitCode !== null || !proc.pid) return;
  if (process.platform === 'win32') {
    spawnSync('taskkill.exe', ['/PID', String(proc.pid), '/T', '/F'], { stdio: 'ignore' });
  } else {
    proc.kill('SIGTERM');
  }
}

function buildPayload() {
  return {
    templateId: 'strategy_analysis',
    templateName: 'Strategy Analysis',
    intent: `INTENT:
Use route-read durable memory to prepare a bounded R2 proof note.

SUCCESS CRITERIA:
- Mention memory id r2-skill-safe if available
- Keep the claim bounded to route-read summary memory
- Mention that canReinject remains false
- Do not expose raw keys or raw memory payloads`,
    inputs: {
      topic: 'R2 durable memory route wiring',
      context: 'The route reads a durable skill memory summary from a file-backed store under explicit request policy.',
      options: 'Close R2 if receipt proves route-read memory\nHold if receipt missing\nEscalate if raw memory appears',
      constraints: 'Do not claim autonomous reinjection, durable writes through the route, or hosted/cloud persistence.',
      priority: 'R2',
    },
    provider: 'alibaba',
    model: 'qwen-turbo',
    mode: 'governance',
    cvfPhase: 'PHASE D',
    cvfRiskLevel: 'R1',
    action: 'read durable memory context',
    durableMemory: {
      enabled: true,
      tier: 'skill',
      scope: 'project:r2-route',
      query: 'durable-route-memory',
      maxResults: 2,
      policy: { actorAuthorized: true },
    },
  };
}

async function main() {
  loadEnvFiles();
  if (!process.env.CVF_SERVICE_TOKEN) throw new Error('missing_cvf_service_token');
  if (!process.env.DASHSCOPE_API_KEY) throw new Error('missing_dashscope_api_key');

  const durableStore = createDurableMemoryStore();
  const server = spawn(
    process.platform === 'win32' ? 'npm.cmd' : 'npm',
    ['run', 'dev', '--', '--port', String(port)],
    {
      cwd: cvfWeb,
      env: buildChildEnv(durableStore.storePath),
      stdio: ['ignore', 'pipe', 'pipe'],
      shell: process.platform === 'win32',
    },
  );
  let serverTail = '';
  const appendTail = (chunk) => {
    serverTail = `${serverTail}${chunk.toString()}`.slice(-4000);
  };
  server.stdout.on('data', appendTail);
  server.stderr.on('data', appendTail);

  try {
    await waitForServer(server);
    const bodyText = JSON.stringify(buildPayload());
    const timestamp = String(Date.now());
    const signature = createHmac('sha256', process.env.CVF_SERVICE_TOKEN)
      .update(`${timestamp}.${bodyText}`)
      .digest('hex');
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
    const durable = data.durableMemoryRead ?? receipt.durableMemoryRead ?? {};
    const assertions = {
      httpStatus200: response.status === 200,
      successTrue: data.success === true,
      receiptPresent: typeof receipt.receiptId === 'string' && receipt.receiptId.length > 5,
      evidenceModeLive: receipt.evidenceMode === 'live' || data.governanceEnvelope?.evidenceMode === 'live',
      providerMatched: receipt.provider === 'alibaba',
      durableReadAllowed: durable.decision === 'allowed',
      durableMemoryIdProven: Array.isArray(durable.memoryIds) && durable.memoryIds.includes('r2-skill-safe'),
      durableSummaryOnly: durable.summaryOnly === true,
      durableCanReinjectFalse: durable.canReinject === false,
      rawMemoryReleasedFalse: durable.rawMemoryReleased === false,
    };
    const failedAssertions = Object.entries(assertions)
      .filter(([, passed]) => !passed)
      .map(([name]) => name);
    const proof = {
      schemaVersion: 'cvf-r2-durable-memory-route-live-result-1',
      status: failedAssertions.length === 0 ? 'PASS' : 'FAIL',
      claimClass: failedAssertions.length === 0
        ? 'bounded_execute_route_durable_memory_read'
        : 'execute_route_durable_memory_read_blocked',
      httpStatus: response.status,
      latencyMs,
      provider: receipt.provider ?? null,
      model: receipt.model ?? data.model ?? null,
      error: data.error ?? null,
      responseModel: data.model ?? null,
      guardDecision: data.guardResult?.finalDecision ?? null,
      guardBlockedBy: data.guardResult?.blockedBy ?? null,
      receiptId: receipt.receiptId ?? null,
      traceId: receipt.envelopeId ?? data.governanceEnvelope?.envelopeId ?? null,
      evidenceMode: receipt.evidenceMode ?? data.governanceEnvelope?.evidenceMode ?? null,
      durableMemoryIds: durable.memoryIds ?? [],
      durableReason: durable.reason ?? null,
      outputLength: String(data.output ?? '').length,
      security: {
        rawSecretPrinted: false,
        rawMemoryReleased: durable.rawMemoryReleased !== false,
        requestHeadersPrinted: false,
      },
      assertions,
      failedAssertions,
    };
    assertNoSecretLeak(proof);
    console.log(JSON.stringify(proof, null, 2));
    process.exitCode = proof.status === 'PASS' ? 0 : 1;
  } catch (error) {
    const failure = {
      schemaVersion: 'cvf-r2-durable-memory-route-live-result-1',
      status: 'ERROR',
      error: error instanceof Error ? error.message : String(error),
      serverTail: redact(serverTail),
    };
    assertNoSecretLeak(failure);
    console.error(JSON.stringify(failure, null, 2));
    process.exitCode = 1;
  } finally {
    killProcessTree(server);
    rmSync(durableStore.tempDir, { recursive: true, force: true });
  }
}

main();
