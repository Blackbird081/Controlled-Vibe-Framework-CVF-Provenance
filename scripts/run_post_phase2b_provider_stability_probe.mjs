#!/usr/bin/env node
/**
 * Post Phase 2.B narrow provider stability probe.
 *
 * Starts the CVF web app locally, signs in through the real login UI, then
 * performs repeated governed `/api/execute` requests for the configured
 * provider lanes. Raw provider keys are loaded from approved local env sources
 * and are never printed.
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

const secretKeyNames = [
  'DASHSCOPE_API_KEY',
  'ALIBABA_API_KEY',
  'CVF_ALIBABA_API_KEY',
  'CVF_BENCHMARK_ALIBABA_KEY',
  'DEEPSEEK_API_KEY',
  'CVF_BENCHMARK_DEEPSEEK_KEY',
  'CVF_DEEPSEEK_API_KEY',
];

const providerSpecs = {
  alibaba: {
    provider: 'alibaba',
    model: 'qwen-turbo',
    envNames: ['DASHSCOPE_API_KEY', 'ALIBABA_API_KEY', 'CVF_ALIBABA_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY'],
    canonicalEnv: 'DASHSCOPE_API_KEY',
  },
  deepseek: {
    provider: 'deepseek',
    model: 'deepseek-chat',
    envNames: ['DEEPSEEK_API_KEY', 'CVF_BENCHMARK_DEEPSEEK_KEY', 'CVF_DEEPSEEK_API_KEY'],
    canonicalEnv: 'DEEPSEEK_API_KEY',
  },
};

const providers = String(process.env.CVF_POST_PHASE2B_PROVIDERS ?? 'alibaba,deepseek')
  .split(',')
  .map((item) => item.trim())
  .filter(Boolean);
const repeats = Number(process.env.CVF_POST_PHASE2B_REPEATS ?? 2);
const port = Number(process.env.CVF_POST_PHASE2B_PROVIDER_STABILITY_PORT ?? 3218);
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

  for (const spec of Object.values(providerSpecs)) {
    if (process.env[spec.canonicalEnv]) continue;
    const aliasValue = spec.envNames.map((key) => process.env[key]).find((value) => value && value.trim());
    if (aliasValue) process.env[spec.canonicalEnv] = aliasValue;
  }
}

function assertNoSecretLeak(value) {
  const serialized = JSON.stringify(value);
  for (const keyName of secretKeyNames) {
    const secret = process.env[keyName];
    if (secret && secret.length > 8 && serialized.includes(secret)) {
      throw new Error(`secret_leak_detected:${keyName}`);
    }
  }
}

function redactServerTail(value) {
  let redacted = String(value ?? '');
  for (const keyName of secretKeyNames) {
    const secret = process.env[keyName];
    if (secret && secret.length > 8) redacted = redacted.split(secret).join('<redacted>');
  }
  return redacted
    .replace(/(DASHSCOPE_API_KEY|ALIBABA_API_KEY|CVF_ALIBABA_API_KEY|CVF_BENCHMARK_ALIBABA_KEY|DEEPSEEK_API_KEY|CVF_BENCHMARK_DEEPSEEK_KEY|CVF_DEEPSEEK_API_KEY)=\S+/g, '$1=<redacted>')
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
  childEnv.DASHSCOPE_API_KEY = process.env.DASHSCOPE_API_KEY;
  childEnv.DEEPSEEK_API_KEY = process.env.DEEPSEEK_API_KEY;
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
      // Server is still booting.
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

function buildPayload(spec, journeyIndex) {
  return {
    templateId: 'strategy_analysis',
    templateName: 'Strategy Analysis',
    intent: `INTENT:
Create a bounded publicization readiness note for Post Phase 2.B provider stability journey ${journeyIndex + 1}.

CONTEXT:
CVF has internal runtime coherence and a live governance receipt proof. The operator wants public claims to advance only as far as evidence supports.

SUCCESS CRITERIA:
- Return a practical recommendation
- Mention governance receipt evidence
- Keep provider stability claims bounded
- Avoid claiming global freeze lift or Maika proof`,
    inputs: {
      topic: 'Post Phase 2.B provider stability',
      context: `Bounded publicization readiness after Phase 2.B live proof. Journey variant ${journeyIndex + 1} should stay narrow and evidence-backed.`,
      options: 'Publish bounded private-evidence claim\nRun more provider stability proof first\nDefer public claim until product readiness review',
      constraints: 'Do not overclaim broad provider stability or product readiness. Do not claim Maika proof or global freeze lift.',
      priority: `provider=${spec.provider}; journey=${journeyIndex + 1}`,
    },
    provider: spec.provider,
    model: spec.model,
    mode: 'simple',
    action: 'analyze',
    aiCommit: {
      commitId: `post-phase2b-provider-stability-${spec.provider}-${journeyIndex + 1}`,
      agentId: 'codex-post-phase2b-stability',
      timestamp: Date.now(),
      description: 'Post Phase 2.B narrow provider stability probe',
    },
  };
}

async function main() {
  loadEnvFiles();

  const selectedSpecs = providers.map((provider) => providerSpecs[provider]).filter(Boolean);
  if (selectedSpecs.length === 0) {
    throw new Error('no_supported_providers_requested');
  }

  const unavailable = selectedSpecs
    .filter((spec) => !process.env[spec.canonicalEnv])
    .map((spec) => spec.provider);
  if (unavailable.length > 0) {
    throw new Error(`missing_provider_keys:${unavailable.join(',')}`);
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

    await page.addInitScript((keys) => {
      localStorage.setItem('cvf_settings', JSON.stringify({
        providers: {
          alibaba: { apiKey: keys.alibaba, enabled: Boolean(keys.alibaba), selectedModel: 'qwen-turbo' },
          deepseek: { apiKey: keys.deepseek, enabled: Boolean(keys.deepseek), selectedModel: 'deepseek-chat' },
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
    }, {
      alibaba: process.env.DASHSCOPE_API_KEY ?? '',
      deepseek: process.env.DEEPSEEK_API_KEY ?? '',
    });

    await page.goto('/login');
    await page.locator('input[type="text"][placeholder="admin"]').fill('admin');
    await page.locator('input[type="password"][placeholder="admin123"]').fill('admin123');
    await page.getByRole('button', { name: /Dang nhap|Đăng nhập|Sign in/i }).click();
    await page.getByRole('heading', { name: /Templates/i }).first().waitFor({ timeout: 30_000 });

    const results = [];
    for (const spec of selectedSpecs) {
      for (let journeyIndex = 0; journeyIndex < repeats; journeyIndex += 1) {
        const startedAt = Date.now();
        const response = await page.request.post('/api/execute', {
          data: buildPayload(spec, journeyIndex),
          timeout: 210_000,
        });
        const latencyMs = Date.now() - startedAt;
        let body = {};
        try {
          body = await response.json();
        } catch (error) {
          body = { parseError: String(error) };
        }
        const output = String(body.output ?? '');
        const receipt = body.governanceEvidenceReceipt ?? {};
        const envelope = body.governanceEnvelope ?? {};
        const routing = body.providerRouting ?? {};
        const assertions = {
          httpStatus200: response.status() === 200,
          successTrue: body.success === true,
          outputNonMock: output.length > 100 && !output.includes('MOCK_'),
          receiptPresent: typeof receipt.receiptId === 'string' && receipt.receiptId.length > 5,
          envelopeLive: envelope.evidenceMode === 'live',
          routeGoverned: envelope.routeId === '/api/execute' && receipt.routeId === '/api/execute',
          providerMatched: routing.selectedProvider === spec.provider && receipt.provider === spec.provider,
          routingAllowed: routing.decision === 'ALLOW' || receipt.routingDecision === 'ALLOW',
          noMockFallback: !JSON.stringify(body).includes('mock_fallback') && !output.includes('MOCK_'),
        };
        const failedAssertions = Object.entries(assertions)
          .filter(([, passed]) => !passed)
          .map(([name]) => name);
        results.push({
          provider: spec.provider,
          model: receipt.model ?? spec.model,
          journey: journeyIndex + 1,
          status: failedAssertions.length === 0 ? 'PASS' : 'FAIL',
          httpStatus: response.status(),
          latencyMs,
          decision: receipt.decision ?? routing.decision ?? null,
          routingDecision: receipt.routingDecision ?? routing.decision ?? null,
          receiptId: receipt.receiptId ?? null,
          traceId: envelope.envelopeId ?? receipt.envelopeId ?? null,
          evidenceMode: receipt.evidenceMode ?? envelope.evidenceMode ?? null,
          routeId: receipt.routeId ?? envelope.routeId ?? null,
          outputLength: output.length,
          failedAssertions,
        });
      }
    }

    const passCount = results.filter((result) => result.status === 'PASS').length;
    const failCount = results.length - passCount;
    const providersPassed = [...new Set(results.filter((result) => result.status === 'PASS').map((result) => result.provider))];
    const providersFailed = [...new Set(results.filter((result) => result.status !== 'PASS').map((result) => result.provider))];
    const proof = {
      schemaVersion: 'post-phase2b-provider-stability-result-1',
      status: failCount === 0 ? 'PASS' : 'FAIL',
      claimClass: failCount === 0 ? 'narrow_two_provider_repeatability' : 'partial_provider_stability_evidence',
      providersRequested: selectedSpecs.map((spec) => spec.provider),
      repeatsPerProvider: repeats,
      passCount,
      failCount,
      providersPassed,
      providersFailed,
      runtimeCoherence: {
        completion: 'docs/reviews/CVF_PHASE_2B_RUNTIME_COHERENCE_COMPLETION_2026-05-21.md',
        graphSchemaVersion: 'phase2b-runtime-coherence-graph-1',
        adapterInventoryChecksum: 'fnv1a32:5d3d2dac',
      },
      assertions: {
        liveEvidenceModeRequired: true,
        receiptRequired: true,
        governedRouteRequired: '/api/execute',
        mockFallbackRejected: true,
        rawSecretPrinted: false,
      },
      results,
    };
    assertNoSecretLeak(proof);
    console.log(JSON.stringify(proof, null, 2));
    process.exitCode = proof.status === 'PASS' ? 0 : 1;
  } catch (error) {
    const failure = {
      schemaVersion: 'post-phase2b-provider-stability-result-1',
      status: 'ERROR',
      error: error instanceof Error ? error.message : String(error),
      serverTail: redactServerTail(serverTail),
    };
    assertNoSecretLeak(failure);
    console.error(JSON.stringify(failure, null, 2));
    process.exitCode = 1;
  } finally {
    if (browser) await browser.close().catch(() => {});
    killProcessTree(server);
  }
}

main();
