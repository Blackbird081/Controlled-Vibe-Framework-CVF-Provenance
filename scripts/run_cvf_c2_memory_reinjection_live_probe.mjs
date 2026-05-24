#!/usr/bin/env node
/**
 * C2 live memory reinjection proof.
 *
 * Starts the local CVF web app and performs one signed, live-provider
 * `/api/execute` call with route-level AIF memory reinjection enabled.
 */

import { createHmac } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
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
];

const port = Number(process.env.CVF_C2_MEMORY_REINJECTION_PORT ?? 3221);
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

function redactServerTail(value) {
  let redacted = String(value ?? '');
  for (const name of secretNames) {
    const secret = process.env[name];
    if (secret && secret.length > 8) redacted = redacted.split(secret).join('<redacted>');
  }
  return redacted
    .replace(/(CVF_SERVICE_TOKEN|DASHSCOPE_API_KEY|ALIBABA_API_KEY|CVF_ALIBABA_API_KEY|CVF_BENCHMARK_ALIBABA_KEY)=\S+/g, '$1=<redacted>')
    .slice(-1600);
}

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function buildChildEnv() {
  const childEnv = {};
  for (const [key, value] of Object.entries(process.env)) {
    if (typeof value !== 'string') continue;
    if (value.includes('\u0000')) continue;
    childEnv[key] = value;
  }
  childEnv.CVF_SERVICE_TOKEN = process.env.CVF_SERVICE_TOKEN;
  childEnv.DASHSCOPE_API_KEY = process.env.DASHSCOPE_API_KEY;
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
Use authorized continuity memory to prepare a bounded C2 proof note.

CONTEXT:
This request proves route-level live memory reinjection. The model should receive only approved memory summaries and must not receive raw memory payloads.

SUCCESS CRITERIA:
- Mention the approved memory id c2-safe
- Keep the claim bounded to summary-only memory reinjection
- Mention governance receipt evidence
- Do not expose raw memory payload text`,
    inputs: {
      topic: 'C2 live memory reinjection',
      context: 'Authorized route-level summary memory reinjection with one safe item and one raw payload item that must be excluded.',
      options: 'Close bounded C2 proof\nHold if receipt missing\nEscalate if raw memory appears',
      constraints: 'Do not claim long-term memory persistence or autonomous reinjection.',
      priority: 'C2',
    },
    provider: 'alibaba',
    model: 'qwen-turbo',
    mode: 'simple',
    action: 'analyze',
    aifMemoryReinjection: {
      enabled: true,
      purpose: 'C2 live proof',
      scope: 'post-aif-claim-graduation',
      policy: {
        actorAuthorized: true,
        canReinject: true,
        provenanceScoreThreshold: 0.7,
        maxItems: 2,
      },
      memory: [
        {
          id: 'c2-safe',
          summary: 'C2 may claim only bounded summary-only live memory reinjection after receipt proof.',
          lifecycleState: 'semantic',
          provenanceScore: 0.96,
        },
        {
          id: 'c2-raw-rejected',
          summary: 'Raw memory payload must be excluded.',
          content: 'RAW-MEMORY-PAYLOAD-DO-NOT-INJECT',
          lifecycleState: 'semantic',
          provenanceScore: 0.99,
        },
      ],
    },
  };
}

async function main() {
  loadEnvFiles();
  if (!process.env.CVF_SERVICE_TOKEN) throw new Error('missing_cvf_service_token');
  if (!process.env.DASHSCOPE_API_KEY) throw new Error('missing_dashscope_api_key');

  const server = spawn(
    process.platform === 'win32' ? 'npm.cmd' : 'npm',
    ['run', 'dev', '--', '--port', String(port)],
    {
      cwd: cvfWeb,
      env: buildChildEnv(),
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
    const output = String(data.output ?? '');
    const receipt = data.governanceEvidenceReceipt ?? {};
    const reinjection = data.aifMemoryReinjection ?? receipt.aifMemoryReinjection ?? {};
    const assertions = {
      httpStatus200: response.status === 200,
      successTrue: data.success === true,
      receiptPresent: typeof receipt.receiptId === 'string' && receipt.receiptId.length > 5,
      evidenceModeLive: receipt.evidenceMode === 'live' || data.governanceEnvelope?.evidenceMode === 'live',
      reinjectionInjected: reinjection.injected === true,
      summaryOnly: reinjection.mode === 'summary_only' && reinjection.summaryOnly === true,
      memoryIdProven: Array.isArray(reinjection.memoryIds) && reinjection.memoryIds.includes('c2-safe'),
      rawMemoryRejected: Array.isArray(reinjection.excluded)
        && reinjection.excluded.some((item) => item.id === 'c2-raw-rejected' && item.reason === 'raw_memory_payload_rejected'),
      rawMemoryNotInOutput: !output.includes('RAW-MEMORY-PAYLOAD-DO-NOT-INJECT'),
      providerMatched: receipt.provider === 'alibaba',
    };
    const failedAssertions = Object.entries(assertions)
      .filter(([, passed]) => !passed)
      .map(([name]) => name);
    const proof = {
      schemaVersion: 'cvf-c2-memory-reinjection-live-result-1',
      status: failedAssertions.length === 0 ? 'PASS' : 'FAIL',
      claimClass: failedAssertions.length === 0
        ? 'bounded_live_summary_memory_reinjection'
        : 'memory_reinjection_live_blocked',
      httpStatus: response.status,
      latencyMs,
      provider: receipt.provider ?? null,
      model: receipt.model ?? data.model ?? null,
      receiptId: receipt.receiptId ?? null,
      traceId: receipt.envelopeId ?? data.governanceEnvelope?.envelopeId ?? null,
      evidenceMode: receipt.evidenceMode ?? data.governanceEnvelope?.evidenceMode ?? null,
      routeId: receipt.routeId ?? data.governanceEnvelope?.routeId ?? null,
      memoryIds: reinjection.memoryIds ?? [],
      excluded: reinjection.excluded ?? [],
      outputLength: output.length,
      assertions,
      failedAssertions,
    };
    assertNoSecretLeak(proof);
    console.log(JSON.stringify(proof, null, 2));
    process.exitCode = proof.status === 'PASS' ? 0 : 1;
  } catch (error) {
    const failure = {
      schemaVersion: 'cvf-c2-memory-reinjection-live-result-1',
      status: 'ERROR',
      error: error instanceof Error ? error.message : String(error),
      serverTail: redactServerTail(serverTail),
    };
    assertNoSecretLeak(failure);
    console.error(JSON.stringify(failure, null, 2));
    process.exitCode = 1;
  } finally {
    killProcessTree(server);
  }
}

main();
