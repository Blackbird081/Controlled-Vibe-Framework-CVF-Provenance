#!/usr/bin/env node
import { createRequire } from 'module';
import { existsSync, readFileSync, writeFileSync } from 'fs';
import { dirname, isAbsolute, relative, resolve } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '..');
const CVF_WEB = resolve(REPO_ROOT, 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web');
const require = createRequire(import.meta.url);
const { chromium } = require(resolve(CVF_WEB, 'node_modules', '@playwright', 'test'));

const BASE_URL = process.env.CVF_C5_WEB_BASE_URL ?? 'http://127.0.0.1:3001';
const ENV_FILE = resolve(CVF_WEB, '.env.local');
const LIVE_KEY_NAMES = ['DASHSCOPE_API_KEY', 'ALIBABA_API_KEY', 'CVF_ALIBABA_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY'];
const C5_EVIDENCE_PATH = resolve(REPO_ROOT, 'docs', 'reviews', 'CVF_C5_WEB_TRIGGERED_FULL_RELEASE_GATE_EVIDENCE_2026-05-08.md');
const RELEASE_GATE_RESULT_PATH = resolve(REPO_ROOT, 'docs', 'reviews', 'CVF_RC2_RELEASE_GATE_RESULT_2026-05-08.md');

function hasConfiguredLiveKey() {
  if (LIVE_KEY_NAMES.some((name) => Boolean(process.env[name]))) return true;
  if (!existsSync(ENV_FILE)) return false;
  const content = readFileSync(ENV_FILE, 'utf8');
  return content.split(/\r?\n/).some((line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) return false;
    const eq = trimmed.indexOf('=');
    if (eq === -1) return false;
    const key = trimmed.slice(0, eq).trim();
    const value = trimmed.slice(eq + 1).trim().replace(/^['"]|['"]$/g, '');
    return LIVE_KEY_NAMES.includes(key) && value.length > 0;
  });
}

async function waitForServer() {
  const deadline = Date.now() + 120_000;
  while (Date.now() < deadline) {
    try {
      const response = await fetch(`${BASE_URL}/login`);
      if (response.ok) return;
    } catch {
      // keep polling
    }
    await new Promise((resolveDelay) => setTimeout(resolveDelay, 1_000));
  }
  throw new Error(`Timed out waiting for ${BASE_URL}`);
}

async function pollFullGate(request, seenJobIds) {
  const deadline = Date.now() + 1_500_000;
  let latest = null;
  let auditPath = '.cvf/runtime/web-governance-jobs.jsonl';
  while (Date.now() < deadline) {
    const response = await request.get(`${BASE_URL}/api/system/jobs`, {
      headers: { 'cache-control': 'no-store' },
    });
    const body = await response.json();
    auditPath = body.auditPath ?? auditPath;
    latest = (body.jobs ?? []).find((job) => (
      job.jobType === 'full_live_release_gate' && !seenJobIds.has(job.jobId)
    )) ?? latest;
    if (latest && ['succeeded', 'failed', 'timed_out', 'blocked_by_policy'].includes(latest.status)) {
      return { job: latest, auditPath };
    }
    await new Promise((resolveDelay) => setTimeout(resolveDelay, 5_000));
  }
  throw new Error('Timed out waiting for full_live_release_gate final event');
}

function parseReleaseGate(stdoutSummary) {
  const parsed = JSON.parse(stdoutSummary);
  return {
    gateResult: parsed.gate_result ?? 'UNKNOWN',
    checks: parsed.checks ?? [],
  };
}

function table(checks) {
  return checks.map((check) => `| ${check.name} | ${check.status} |`).join('\n');
}

function writeEvidence(job, gate, auditPath) {
  const checkTable = table(gate.checks);
  const passCount = gate.checks.filter((check) => check.status === 'PASS').length;
  const command = 'python scripts/run_cvf_release_gate_bundle.py --json';
  const auditPathLabel = isAbsolute(auditPath) ? relative(REPO_ROOT, auditPath) : auditPath;

  writeFileSync(RELEASE_GATE_RESULT_PATH, `<!-- Memory class: FULL_RECORD -->
# CVF RC2 Release Gate Result

**Date:** 2026-05-08
**Command:** \`${command}\`
**Trigger:** Web Governance Operations job \`full_live_release_gate\`
**Result:** ${gate.gateResult}

## Checks

| Check | Status |
|---|---:|
${checkTable}

## Boundary

This artifact closes the RC2 Blocker 1 evidence gap by recording the 7-check
release gate breakdown from a Web-triggered full live release gate. It does not
claim a fresh full W119/W122-W130 adoption replay beyond the separate RC2
Pre-GA regression evidence packet.
`, 'utf8');

  writeFileSync(C5_EVIDENCE_PATH, `<!-- Memory class: FULL_RECORD -->
# CVF C5 Web-Triggered Full Live Release Gate Evidence

**Date:** 2026-05-08
**Roadmap item:** C5 — Full live release gate trigger from Web
**Command executed by Web job:** \`${command}\`
**Web surface:** \`/governance/operations\`
**Audit path:** \`${auditPathLabel}\`
**Job ID:** \`${job.jobId}\`
**Job status:** ${job.status}
**Gate result:** ${gate.gateResult}
**Checks passed:** ${passCount}/${gate.checks.length}

## Control Evidence

| Control | Evidence |
|---|---|
| Web trigger, not CLI-only | Browser probe logged in as admin and clicked the \`Full Live Release Gate\` job card. |
| Fixed command contract | \`${command}\` |
| Role-bound trigger | Job role recorded as \`${job.role}\`; anonymous/viewer paths remain blocked by policy tests. |
| Provider lane | \`${job.providerLane ?? 'none'}\` |
| Handler | \`${job.handlerId ?? 'not recorded'}\` |
| Redaction | \`${job.redactionApplied ? 'applied' : 'not recorded'}\` |
| Cost/quota warning | Web card warns that the action consumes live provider quota and is not dry readiness. |
| Runtime isolation | Full gate child process uses \`NEXT_DIST_DIR=.next-cvf-release-gate\` and \`CVF_PLAYWRIGHT_PORT=3011\` to avoid corrupting the controlling Web dev server. |

## Release Gate Breakdown

| Check | Status |
|---|---:|
${checkTable}

## Boundary

This proves C5.2 for operator/admin Web triggering of the full live release
gate. The persistent job store remains local JSONL for RC2; managed database
storage is future optional infrastructure, not the default CVF dev path.
`, 'utf8');
}

async function main() {
  if (!hasConfiguredLiveKey()) {
    throw new Error('DashScope-compatible live key is required for C5 Web-triggered release gate proof.');
  }
  await waitForServer();

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ baseURL: BASE_URL });
  try {
    await page.addInitScript(() => {
      localStorage.setItem('cvf_onboarding_complete', 'true');
      localStorage.setItem('cvf_onboarding_seen', '1');
      localStorage.setItem('cvf_settings', JSON.stringify({
        providers: {
          alibaba: { apiKey: '', enabled: true, selectedModel: 'qwen-turbo' },
        },
        preferences: {
          defaultProvider: 'alibaba',
          defaultLanguage: 'vi',
          autoSaveHistory: true,
          showWelcomeTour: false,
        },
      }));
    });
    await page.goto('/login');
    await page.locator('input[type="text"][placeholder="admin"]').fill('admin');
    await page.locator('input[type="password"][placeholder="admin123"]').fill('admin123');
    await page.getByRole('button', { name: /Đăng nhập|Sign in/i }).click();
    await page.waitForURL(/\/home|\/templates|\/landing/, { timeout: 30_000 });

    const before = await page.request.get(`${BASE_URL}/api/system/jobs`).then((response) => response.json());
    const seenJobIds = new Set((before.jobs ?? []).map((job) => job.jobId));

    await page.goto('/governance/operations');
    await page.getByTestId('governance-job-card-full_live_release_gate-default').waitFor({ state: 'visible', timeout: 30_000 });
    await page.getByTestId('governance-job-run-full_live_release_gate-default').click();

    const { job, auditPath } = await pollFullGate(page.request, seenJobIds);
    if (job.status !== 'succeeded') {
      throw new Error(`full_live_release_gate ended with ${job.status}: ${job.decisionReason}`);
    }
    if (JSON.stringify(job).match(/DASHSCOPE_API_KEY\s*=|ALIBABA_API_KEY\s*=|CVF_ALIBABA_API_KEY\s*=|CVF_BENCHMARK_ALIBABA_KEY\s*=/)) {
      throw new Error('Redaction check failed: provider key assignment appeared in job payload.');
    }

    const gate = parseReleaseGate(job.stdoutSummary ?? '{}');
    if (gate.gateResult !== 'PASS') {
      throw new Error(`Release gate result was ${gate.gateResult}`);
    }
    if (gate.checks.length !== 7 || !gate.checks.every((check) => check.status === 'PASS')) {
      throw new Error(`Expected 7/7 PASS, got ${gate.checks.filter((check) => check.status === 'PASS').length}/${gate.checks.length}`);
    }

    writeEvidence(job, gate, auditPath);
    console.log(JSON.stringify({
      status: 'PASS',
      jobId: job.jobId,
      gateResult: gate.gateResult,
      checksPassed: gate.checks.length,
      evidence: [
        RELEASE_GATE_RESULT_PATH,
        C5_EVIDENCE_PATH,
      ],
    }, null, 2));
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
});
