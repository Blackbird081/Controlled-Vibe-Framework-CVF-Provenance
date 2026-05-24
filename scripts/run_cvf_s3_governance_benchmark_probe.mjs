#!/usr/bin/env node
import { createHmac } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cvfWeb = path.join(repoRoot, 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web');
const cliRoot = path.join(repoRoot, 'EXTENSIONS', 'CVF_ECO_v2.2_GOVERNANCE_CLI');
const evidencePath = path.join(repoRoot, 'docs', 'reviews', 'CVF_S3_GOVERNANCE_BENCHMARK_PUBLIC_CLAIM_EVIDENCE_2026-05-24.json');
const hostedUrl = process.env.CVF_S3_HOSTED_EXECUTE_URL ?? 'https://vibcode.netlify.app/api/execute';
const runs = Number(process.env.CVF_S3_BENCHMARK_RUNS ?? 5);
const envFiles = [path.join(cvfWeb, '.env.local'), path.join(cvfWeb, '.env'), path.join(repoRoot, '.env.local'), path.join(repoRoot, '.env')];
const secretNames = ['CVF_SERVICE_TOKEN', 'DASHSCOPE_API_KEY', 'ALIBABA_API_KEY', 'CVF_ALIBABA_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY'];

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
}

function assertNoSecretLeak(value) {
  const serialized = JSON.stringify(value);
  for (const name of secretNames) {
    const secret = process.env[name];
    if (secret && secret.length > 8 && serialized.includes(secret)) throw new Error(`secret_leak_detected:${name}`);
  }
}

function buildPayload(index) {
  return {
    templateId: 'strategy_analysis',
    templateName: 'Strategy Analysis',
    intent: `Create a bounded live governance benchmark note for S3 run ${index + 1}. Mention receipt-backed governance and avoid production-readiness claims.`,
    inputs: {
      topic: 'S3 governance benchmark public claim',
      context: 'Hosted /api/execute live benchmark run for quantitative governance evidence.',
      options: 'Publish bounded metric row\nHold if receipts are missing\nDefer production readiness claim',
      constraints: 'No SLA, no enterprise certification, no universal provider stability claim.',
      priority: `benchmark-run-${index + 1}`,
    },
    provider: 'alibaba',
    model: 'qwen-turbo',
    mode: 'governance',
    cvfPhase: 'PHASE D',
    cvfRiskLevel: 'R1',
    action: 'test',
    aiCommit: {
      commitId: `s3-governance-benchmark-${index + 1}`,
      agentId: 'codex-s3-benchmark',
      timestamp: Date.now(),
      description: 'S3 live governance benchmark probe',
    },
  };
}

async function importBenchmarkBuilder() {
  const build = spawnSync(process.platform === 'win32' ? 'npm.cmd' : 'npm', ['run', 'build', '--', '--pretty', 'false'], {
    cwd: cliRoot,
    encoding: 'utf8',
    shell: process.platform === 'win32',
  });
  if (build.status !== 0) {
    throw new Error(`governance_cli_build_failed:${(build.stderr || build.stdout || '').slice(-600)}`);
  }
  const modulePath = path.join(cliRoot, 'dist', 'src', 'operational-benchmark-suite.js');
  const mod = await import(pathToFileURL(modulePath));
  return mod.buildOperationalBenchmarkReport;
}

async function callHosted(index) {
  const bodyText = JSON.stringify(buildPayload(index));
  const timestamp = String(Date.now());
  const signature = createHmac('sha256', process.env.CVF_SERVICE_TOKEN).update(`${timestamp}.${bodyText}`).digest('hex');
  const startedAt = Date.now();
  const response = await fetch(hostedUrl, {
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
  let body = {};
  try {
    body = await response.json();
  } catch (error) {
    body = { parseError: String(error) };
  }
  const receipt = body.governanceEvidenceReceipt ?? {};
  return {
    run: index + 1,
    httpStatus: response.status,
    success: body.success === true,
    latencyMs,
    receiptId: receipt.receiptId ?? null,
    traceId: receipt.envelopeId ?? body.governanceEnvelope?.envelopeId ?? null,
    evidenceMode: receipt.evidenceMode ?? body.governanceEnvelope?.evidenceMode ?? null,
    provider: receipt.provider ?? body.provider ?? null,
    model: receipt.model ?? body.model ?? null,
    decision: receipt.decision ?? null,
    routingDecision: receipt.routingDecision ?? body.providerRouting?.decision ?? null,
    error: body.error ?? null,
    outputLength: String(body.output ?? '').length,
  };
}

function toBenchmarkEvents(results) {
  return results.flatMap((result) => {
    const base = {
      executionId: result.traceId ?? `s3-run-${result.run}`,
      runId: 's3-governance-benchmark-2026-05-24',
      evidenceMode: result.evidenceMode === 'live' ? 'live' : 'unknown',
      provider: result.provider ?? undefined,
      model: result.model ?? undefined,
      timestamp: new Date().toISOString(),
    };
    return [
      {
        ...base,
        eventType: 'execution_completed',
        receiptId: result.receiptId,
        decision: result.success ? 'allow' : 'deny',
        enforcement: { status: result.success ? 'allow' : 'deny' },
      },
      {
        ...base,
        eventType: 'receipt_emitted',
        receiptId: result.receiptId,
        decision: result.receiptId ? 'captured' : 'missing',
        enforcement: { status: result.success ? 'allow' : 'deny' },
      },
    ];
  });
}

async function main() {
  loadEnvFiles();
  if (!process.env.CVF_SERVICE_TOKEN) throw new Error('missing_cvf_service_token');
  const buildOperationalBenchmarkReport = await importBenchmarkBuilder();
  const results = [];
  for (let index = 0; index < runs; index += 1) {
    results.push(await callHosted(index));
  }
  const events = toBenchmarkEvents(results);
  const report = buildOperationalBenchmarkReport(events, hostedUrl);
  const proof = {
    schemaVersion: 'cvf-s3-governance-benchmark-live-evidence-1',
    status: results.every((result) => result.success && result.receiptId && result.evidenceMode === 'live') ? 'PASS' : 'FAIL',
    hostedUrl,
    liveCallCount: runs,
    sourceFilesRead: [
      'EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts',
      'EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts',
    ],
    metrics: {
      taskCompletionRate: report.metrics.taskCompletionRate,
      policyViolationRate: report.metrics.policyViolationRate,
      receiptIntegrityRate: report.metrics.receiptIntegrityRate,
    },
    report,
    results,
    security: { rawSecretPrinted: false, requestHeadersPrinted: false },
  };
  assertNoSecretLeak(proof);
  mkdirSync(path.dirname(evidencePath), { recursive: true });
  writeFileSync(evidencePath, `${JSON.stringify(proof, null, 2)}\n`, 'utf8');
  console.log(JSON.stringify(proof, null, 2));
  process.exitCode = proof.status === 'PASS' ? 0 : 1;
}

main().catch((error) => {
  const failure = { schemaVersion: 'cvf-s3-governance-benchmark-live-evidence-1', status: 'ERROR', error: error instanceof Error ? error.message : String(error) };
  assertNoSecretLeak(failure);
  console.error(JSON.stringify(failure, null, 2));
  process.exitCode = 1;
});
