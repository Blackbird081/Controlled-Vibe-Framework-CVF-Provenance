// EVT-2.1 live latency measurement for /api/execute.
// Starts a local cvf-web dev server, sends governed live requests, and writes
// JSONL evidence without printing raw provider keys.

const fs = require('fs');
const path = require('path');
const { spawn, execSync } = require('child_process');

require('./load-repo-env.cjs').loadRepoEnv();
const { buildServiceTokenHeaders } = require('./service-token-signature.cjs');

const REPO_ROOT = path.resolve(__dirname, '..');
const CVF_WEB = path.join(REPO_ROOT, 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web');
const PORT = Number(process.env.EVT2_CVF_WEB_PORT || 3022);
const BASE_URL = process.env.EVT2_CVF_WEB_BASE_URL || `http://localhost:${PORT}`;
const EXECUTE_URL = `${BASE_URL}/api/execute`;
const SERVICE_TOKEN = process.env.CVF_SERVICE_TOKEN || 'pvv-pilot-2026';
const COUNT = Number(process.env.EVT2_SAMPLE_COUNT || process.argv[2] || 20);
const OUT_JSONL = path.join(REPO_ROOT, 'docs', 'assessments', 'CVF_EVT2_LIVE_LATENCY_MEASUREMENT_2026-05-14.jsonl');

function resolveLiveKeyName() {
  return ['DASHSCOPE_API_KEY', 'ALIBABA_API_KEY', 'CVF_ALIBABA_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY']
    .find((name) => String(process.env[name] || '').trim()) || null;
}

function ensureLiveKey() {
  const keyName = resolveLiveKeyName();
  if (!keyName) throw new Error('No DashScope-compatible live key found.');
  if (!process.env.DASHSCOPE_API_KEY) process.env.DASHSCOPE_API_KEY = String(process.env[keyName]).trim();
  return keyName;
}

function startServer() {
  const child = spawn('npm', ['run', 'dev', '--', '--port', String(PORT)], {
    cwd: CVF_WEB,
    shell: true,
    windowsHide: true,
    stdio: ['ignore', 'pipe', 'pipe'],
    env: {
      ...process.env,
      CVF_SERVICE_TOKEN: SERVICE_TOKEN,
      DEFAULT_AI_PROVIDER: 'alibaba',
      DASHSCOPE_API_KEY: process.env.DASHSCOPE_API_KEY,
    },
  });
  const logLines = [];
  const keepLog = (chunk) => {
    for (const line of String(chunk).split(/\r?\n/).filter(Boolean)) {
      logLines.push(line);
      if (logLines.length > 80) logLines.shift();
    }
  };
  child.stdout.on('data', keepLog);
  child.stderr.on('data', keepLog);
  child.getRecentLog = () => logLines.join('\n');
  return child;
}

function stopServer(child) {
  if (!child || child.killed) return;
  try {
    if (process.platform === 'win32') {
      execSync(`taskkill /pid ${child.pid} /T /F`, { stdio: 'ignore' });
    } else {
      child.kill('SIGTERM');
    }
  } catch {
    try { child.kill(); } catch {}
  }
}

async function waitForServer(timeoutMs = 120_000) {
  const started = Date.now();
  while (Date.now() - started < timeoutMs) {
    try {
      const res = await fetch(BASE_URL, { redirect: 'manual' });
      if (res.status >= 200 && res.status < 500) return;
    } catch {
      // keep polling
    }
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }
  throw new Error(`Timed out waiting for cvf-web at ${BASE_URL}`);
}

function buildPayload(index) {
  return {
    templateId: 'documentation',
    templateName: 'EVT-2 Latency Measurement',
    intent: `Analyze an operator handoff checklist for sample ${index}.`,
    inputs: {
      subject: `EVT-2 governed latency sample ${index}`,
      currentNotes: 'Prepare a practical checklist for a local-first SaaS onboarding task. Include context, steps, acceptance checks, owner, and follow-up notes.',
      readerGoal: 'The operator can evaluate the handoff and share it with a builder without extra context.',
      audience: 'Operator',
      mustPreserve: 'Mention scope, acceptance checks, and owner.',
    },
    provider: 'alibaba',
    model: 'qwen-turbo',
    mode: 'governance',
    cvfPhase: 'INTAKE',
    cvfRiskLevel: 'R1',
    skillPreflightPassed: false,
  };
}

async function postExecute(payload) {
  const serviceAuth = buildServiceTokenHeaders(SERVICE_TOKEN, payload);
  const started = Date.now();
  const response = await fetch(EXECUTE_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...serviceAuth.headers,
    },
    body: serviceAuth.body,
  });
  const totalMs = Date.now() - started;
  const data = await response.json().catch(() => ({ error: 'Non-JSON response' }));
  const providerExecutionMs = typeof data.executionTime === 'number' ? data.executionTime : null;
  const overheadMs = providerExecutionMs === null ? null : Math.max(0, totalMs - providerExecutionMs);
  const taxRatio = providerExecutionMs && overheadMs !== null ? overheadMs / providerExecutionMs : null;
  return {
    measuredAt: new Date().toISOString(),
    httpStatus: response.status,
    success: response.ok && data.success === true,
    totalMs,
    providerExecutionMs,
    governanceOverheadMs: overheadMs,
    governanceTaxRatio: taxRatio,
    provider: data.provider || null,
    model: data.model || null,
    decision: data.governanceEvidenceReceipt?.decision || data.enforcement?.status || null,
    riskLevel: data.governanceEvidenceReceipt?.riskLevel || data.enforcement?.riskGate?.riskLevel || null,
    receiptId: data.governanceEvidenceReceipt?.receiptId || null,
    outputLength: typeof data.output === 'string' ? data.output.length : 0,
    error: data.success ? null : String(data.error || ''),
  };
}

async function main() {
  const keyName = ensureLiveKey();
  fs.mkdirSync(path.dirname(OUT_JSONL), { recursive: true });
  fs.writeFileSync(OUT_JSONL, '', 'utf8');

  const server = startServer();
  try {
    await waitForServer();
    console.log(`EVT-2 live latency: key=${keyName}:PRESENT, count=${COUNT}, url=${EXECUTE_URL}`);
    for (let i = 1; i <= COUNT; i += 1) {
      const record = await postExecute(buildPayload(i));
      fs.appendFileSync(OUT_JSONL, `${JSON.stringify(record)}\n`, 'utf8');
      const tax = record.governanceTaxRatio === null ? 'N/A' : `${(record.governanceTaxRatio * 100).toFixed(1)}%`;
      console.log(`${String(i).padStart(2, '0')}/${COUNT} status=${record.httpStatus} success=${record.success} total=${record.totalMs}ms provider=${record.providerExecutionMs}ms tax=${tax}`);
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
    console.log(`Evidence: ${OUT_JSONL}`);
  } finally {
    stopServer(server);
  }
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
});
