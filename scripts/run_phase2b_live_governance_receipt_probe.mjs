#!/usr/bin/env node
/**
 * Phase 2.B live governance receipt probe.
 *
 * Starts the CVF web app locally, performs an authenticated governed
 * `/api/execute` request on the Alibaba lane, and emits a redacted JSON proof
 * containing the live receipt/envelope ids. Raw provider keys are loaded from
 * local environment files but are never printed.
 */

import { spawn, spawnSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cvfWeb = path.join(repoRoot, 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web');
const envFiles = [
  path.join(cvfWeb, '.env.local'),
  path.join(cvfWeb, '.env'),
  path.join(repoRoot, '.env.local'),
  path.join(repoRoot, '.env'),
];
const keyNames = ['DASHSCOPE_API_KEY', 'ALIBABA_API_KEY', 'CVF_ALIBABA_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY'];
const port = Number(process.env.CVF_PHASE2B_LIVE_PROOF_PORT ?? 3217);
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

  if (!process.env.DASHSCOPE_API_KEY) {
    const aliasValue = keyNames.map((key) => process.env[key]).find((value) => value && value.trim());
    if (aliasValue) process.env.DASHSCOPE_API_KEY = aliasValue;
  }
}

function assertNoSecretLeak(value) {
  const serialized = JSON.stringify(value);
  for (const keyName of [...keyNames, 'DEEPSEEK_API_KEY']) {
    const secret = process.env[keyName];
    if (secret && secret.length > 8 && serialized.includes(secret)) {
      throw new Error(`secret_leak_detected:${keyName}`);
    }
  }
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
  childEnv.DASHSCOPE_API_KEY = process.env.DASHSCOPE_API_KEY;
  childEnv.CVF_PLAYWRIGHT_PORT = String(port);
  childEnv.PORT = String(port);
  return childEnv;
}

async function waitForServer(proc) {
  const startedAt = Date.now();
  while (Date.now() - startedAt < 120_000) {
    if (proc.exitCode !== null) {
      throw new Error(`dev_server_exited:${proc.exitCode}`);
    }
    try {
      const response = await fetch(`${baseUrl}/login`);
      if (response.status < 500) return;
    } catch {
      // Server is not ready yet.
    }
    await delay(1000);
  }
  throw new Error('dev_server_start_timeout');
}

async function fetchWithTimeout(url, options = {}, timeoutMs = 120_000) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);
  try {
    return await fetch(url, { ...options, signal: controller.signal });
  } finally {
    clearTimeout(timeout);
  }
}

function killProcessTree(proc) {
  if (proc.exitCode !== null || !proc.pid) return;
  if (process.platform === 'win32') {
    spawnSync('taskkill.exe', ['/PID', String(proc.pid), '/T', '/F'], { stdio: 'ignore' });
  } else {
    proc.kill('SIGTERM');
  }
}

async function main() {
  loadEnvFiles();

  if (!process.env.DASHSCOPE_API_KEY) {
    throw new Error('missing_dashscope_compatible_key');
  }

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
  let browser;

  try {
    await waitForServer(server);

    const playwright = await import(pathToFileURL(path.join(cvfWeb, 'node_modules', '@playwright', 'test', 'index.mjs')));
    browser = await playwright.chromium.launch({ headless: true });
    const context = await browser.newContext({ baseURL: baseUrl });
    const page = await context.newPage();

    await page.addInitScript((key) => {
      localStorage.setItem('cvf_settings', JSON.stringify({
        providers: {
          alibaba: { apiKey: key, enabled: true, selectedModel: 'qwen-turbo' },
        },
        preferences: {
          defaultProvider: 'alibaba',
          defaultLanguage: 'vi',
          autoSaveHistory: true,
          showWelcomeTour: false,
        },
      }));
      localStorage.setItem('cvf_onboarding_complete', 'true');
      localStorage.setItem('cvf_onboarding_seen', '1');
    }, process.env.DASHSCOPE_API_KEY);

    await page.goto('/login');
    await page.locator('input[type="text"][placeholder="admin"]').fill('admin');
    await page.locator('input[type="password"][placeholder="admin123"]').fill('admin123');
    await page.getByRole('button', { name: /Dang nhap|Đăng nhập|Sign in/i }).click();
    await page.getByRole('heading', { name: /Templates/i }).first().waitFor({ timeout: 30_000 });

    const executeResponse = await page.request.post('/api/execute', {
      data: {
        templateId: 'strategy_analysis',
        templateName: 'Phan tich Chien luoc',
        intent: `INTENT:
Analyze a Phase 2.B live governance proof route for a non-coder strategy brief.

CONTEXT:
Small B2B software company expanding from Hanoi to Da Nang.

OPTIONS:
1. Hire local sales
2. Use local reseller
3. Run demand-generation campaign first

CONSTRAINTS:
Budget is 300 million VND and decision window is 6 months.

SUCCESS CRITERIA:
Clear recommendation, risk notes, and governance receipt evidence.`,
        inputs: {
          topic: 'Phase 2.B live governance proof',
          context: 'B2B software company expanding to Da Nang.',
          options: 'Hire local sales\nUse reseller\nRun demand generation first',
          constraints: '300 million VND budget, 6 month decision window',
          priority: 'Governed live proof',
        },
        provider: 'alibaba',
        model: 'qwen-turbo',
        mode: 'simple',
        action: 'analyze',
        aiCommit: {
          commitId: 'phase2b-live-governance-proof',
          agentId: 'codex-phase2b-live-proof',
          timestamp: Date.now(),
          description: 'Phase 2.B live governance proof route',
        },
      },
      timeout: 180_000,
    });

    const body = await executeResponse.json();
    const output = String(body.output ?? '');
    const receipt = body.governanceEvidenceReceipt ?? {};
    const envelope = body.governanceEnvelope ?? {};
    const providerRouting = body.providerRouting ?? {};

    const assertions = {
      httpStatus200: executeResponse.status() === 200,
      successTrue: body.success === true,
      outputNonMock: output.length > 100 && !output.includes('MOCK_'),
      receiptPresent: typeof receipt.receiptId === 'string' && receipt.receiptId.length > 5,
      envelopeLive: envelope.evidenceMode === 'live',
      routeGoverned: envelope.routeId === '/api/execute' && receipt.routeId === '/api/execute',
      providerAlibaba: providerRouting.selectedProvider === 'alibaba' && receipt.provider === 'alibaba',
      routingAllowed: providerRouting.decision === 'ALLOW' || receipt.routingDecision === 'ALLOW',
      noMockFallback: !JSON.stringify(body).includes('mock_fallback') && !output.includes('MOCK_'),
    };

    const failed = Object.entries(assertions)
      .filter(([, passed]) => !passed)
      .map(([name]) => name);
    if (failed.length > 0) {
      throw new Error(`live_proof_assertion_failed:${failed.join(',')}:http_${executeResponse.status()}:${JSON.stringify({
        success: body.success,
        error: body.error,
        selectedProvider: providerRouting.selectedProvider,
        routingDecision: providerRouting.decision,
        receiptIdPresent: typeof receipt.receiptId === 'string',
        envelopeMode: envelope.evidenceMode,
      })}`);
    }

    const proof = {
      schemaVersion: 'phase2b-live-governance-proof-result-1',
      status: 'PASS',
      providerLane: 'alibaba',
      model: receipt.model ?? 'qwen-turbo',
      decision: receipt.decision ?? providerRouting.decision,
      routingDecision: receipt.routingDecision ?? providerRouting.decision,
      receiptId: receipt.receiptId,
      traceId: envelope.envelopeId ?? receipt.envelopeId,
      policySnapshotId: receipt.policySnapshotId ?? envelope.policySnapshotId,
      evidenceMode: receipt.evidenceMode ?? envelope.evidenceMode,
      routeId: receipt.routeId ?? envelope.routeId,
      outputLength: output.length,
      runtimeCoherence: {
        completion: 'docs/reviews/CVF_PHASE_2B_RUNTIME_COHERENCE_COMPLETION_2026-05-21.md',
        graphSchemaVersion: 'phase2b-runtime-coherence-graph-1',
        adapterInventoryChecksum: 'fnv1a32:5d3d2dac',
      },
      fallbackBypassRejected: true,
      rawSecretPrinted: false,
      assertions,
    };

    assertNoSecretLeak(proof);
    process.stdout.write(`${JSON.stringify(proof, null, 2)}\n`);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    const failure = {
      schemaVersion: 'phase2b-live-governance-proof-result-1',
      status: 'FAIL',
      message,
      serverTail: serverTail
        .replace(/(DASHSCOPE_API_KEY|ALIBABA_API_KEY|CVF_ALIBABA_API_KEY|CVF_BENCHMARK_ALIBABA_KEY|DEEPSEEK_API_KEY)=\S+/g, '$1=<redacted>')
        .split(/\r?\n/)
        .slice(-8),
    };
    assertNoSecretLeak(failure);
    process.stdout.write(`${JSON.stringify(failure, null, 2)}\n`);
    process.exitCode = 1;
  } finally {
    if (browser) {
      await browser.close().catch(() => undefined);
    }
    killProcessTree(server);
  }
}

main();
