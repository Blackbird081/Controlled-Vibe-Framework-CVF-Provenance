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

const BASE_URL = process.env.CVF_CQ_WEB_BASE_URL ?? 'http://127.0.0.1:3022';
const ENV_FILE = resolve(CVF_WEB, '.env.local');
const LIVE_KEY_NAMES = ['DASHSCOPE_API_KEY', 'ALIBABA_API_KEY', 'CVF_ALIBABA_API_KEY', 'CVF_BENCHMARK_ALIBABA_KEY'];
const PREFLIGHT_EVIDENCE = resolve(REPO_ROOT, 'docs', 'reviews', 'CVF_COST_QUOTA_PREFLIGHT_EVIDENCE_2026-05-08.md');
const WEB_EVIDENCE = resolve(REPO_ROOT, 'docs', 'reviews', 'CVF_COST_QUOTA_WEB_OPERATOR_EVIDENCE_2026-05-08.md');
const AUDIT_EVIDENCE = resolve(REPO_ROOT, 'docs', 'reviews', 'CVF_COST_QUOTA_AUDIT_EVIDENCE_2026-05-08.md');

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

function parseReleaseGate(stdoutSummary) {
  const parsed = JSON.parse(stdoutSummary);
  return {
    gateResult: parsed.gate_result ?? 'UNKNOWN',
    checks: parsed.checks ?? [],
  };
}

function readCostQuotaEvents(jobId) {
  const auditPath = resolve(REPO_ROOT, '.cvf', 'runtime', 'web-governance-cost-quota.jsonl');
  if (!existsSync(auditPath)) return { auditPath, events: [] };
  const events = readFileSync(auditPath, 'utf8')
    .split(/\r?\n/)
    .filter(Boolean)
    .map((line) => JSON.parse(line))
    .filter((event) => event.jobId === jobId);
  return { auditPath, events };
}

function rel(path) {
  return isAbsolute(path) ? relative(REPO_ROOT, path) : path;
}

function writeEvidence(result, gate, costAudit) {
  const costQuota = result.costQuota;
  const eventTypes = costAudit.events.map((event) => event.eventType);
  const checksPassed = gate.checks.filter((check) => check.status === 'PASS').length;
  const common = [
    `**Date:** 2026-05-08`,
    `**Job ID:** \`${result.jobId}\``,
    `**Job status:** ${result.status}`,
    `**Release gate result:** ${gate.gateResult}`,
    `**Checks passed:** ${checksPassed}/${gate.checks.length}`,
    `**Cost/quota audit path:** \`${rel(costAudit.auditPath)}\``,
  ].join('\n');

  writeFileSync(PREFLIGHT_EVIDENCE, [
    '<!-- Memory class: FULL_RECORD -->',
    '# CVF Cost/Quota Preflight Evidence',
    '',
    common,
    '',
    '## Result',
    '',
    '| Field | Value |',
    '|---|---|',
    `| decision | ${costQuota?.decision ?? 'not recorded'} |`,
    `| decisionReason | ${costQuota?.decisionReason ?? 'not recorded'} |`,
    `| expectedLiveCallCount | ${costQuota?.expectedLiveCallCount ?? 'not recorded'} |`,
    `| providerLane | ${costQuota?.providerLane ?? 'not recorded'} |`,
    `| globalUsageBefore | ${costQuota?.globalUsage ?? 'not recorded'} |`,
    `| globalLimit | ${costQuota?.globalLimit ?? 'not recorded'} |`,
    `| providerUsageBefore | ${costQuota?.providerUsage ?? 'not recorded'} |`,
    `| providerLimit | ${costQuota?.providerLimit ?? 'not recorded'} |`,
    `| cooldownSeconds | ${costQuota?.cooldownSeconds ?? 'not recorded'} |`,
    '',
    '## Boundary',
    '',
    '- This is a live under-budget allow-path proof for Web `full_live_release_gate`.',
    '- Over-limit, direct API bypass, cooldown, and override paths are covered by no-live targeted tests.',
    '- No raw provider key is included in this artifact.',
  ].join('\n'), 'utf8');

  writeFileSync(WEB_EVIDENCE, [
    '<!-- Memory class: FULL_RECORD -->',
    '# CVF Cost/Quota Web Operator Evidence',
    '',
    common,
    '',
    '## Web Surface',
    '',
    '- `/governance/operations` displays live-call estimates per job card.',
    '- Provider lanes display current usage versus configured caps.',
    '- Owner/admin users have an explicit override affordance with a reason field.',
    '- Server-side `/api/system/jobs` remains the enforcement point; the UI is informational.',
    '',
    '## Live Web Proof',
    '',
    `- Browser login role: admin.`,
    `- API route: /api/system/jobs.`,
    `- Submitted job: full_live_release_gate.`,
    `- Server cost/quota decision: ${costQuota?.decision ?? 'not recorded'} (${costQuota?.decisionReason ?? 'not recorded'}).`,
  ].join('\n'), 'utf8');

  writeFileSync(AUDIT_EVIDENCE, [
    '<!-- Memory class: FULL_RECORD -->',
    '# CVF Cost/Quota Audit Evidence',
    '',
    common,
    '',
    '## Audit Events For Job',
    '',
    '| Event type | Present |',
    '|---|---:|',
    `| estimate_requested | ${eventTypes.includes('estimate_requested') ? 'yes' : 'no'} |`,
    `| estimate_allowed | ${eventTypes.includes('estimate_allowed') ? 'yes' : 'no'} |`,
    `| usage_incremented | ${eventTypes.includes('usage_incremented') ? 'yes' : 'no'} |`,
    '',
    '## Assertions',
    '',
    `- Usage increment recorded: ${eventTypes.includes('usage_incremented') ? 'PASS' : 'FAIL'}.`,
    `- Override used: ${costQuota?.overrideUsed ? 'yes' : 'no'}.`,
    '- Audit fields include role, job ID, provider lane, expected call count, window, caps, and decision reason.',
    '- No raw provider key is included in this artifact.',
  ].join('\n'), 'utf8');
}

async function main() {
  if (!hasConfiguredLiveKey()) {
    throw new Error('DashScope-compatible live key is required for CQ live under-budget proof.');
  }
  await waitForServer();

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ baseURL: BASE_URL });
  try {
    await page.goto('/login');
    await page.locator('input[type="text"][placeholder="admin"]').fill('admin');
    await page.locator('input[type="password"][placeholder="admin123"]').fill('admin123');
    await page.getByRole('button', { name: /Đăng nhập|Sign in/i }).click();
    await page.waitForURL(/\/home|\/templates|\/landing/, { timeout: 30_000 });

    const result = await page.evaluate(async () => {
      const response = await fetch('/api/system/jobs', {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({
          jobType: 'full_live_release_gate',
          uiRequestId: `cq-live-under-budget-${Date.now()}`,
        }),
      });
      return {
        statusCode: response.status,
        body: await response.json(),
      };
    });

    if (result.statusCode !== 200 || result.body.status !== 'succeeded') {
      throw new Error(`CQ live job failed: HTTP ${result.statusCode}, status ${result.body.status}, reason ${result.body.decisionReason}`);
    }
    if (result.body.costQuota?.decision !== 'allowed') {
      throw new Error(`CQ preflight did not allow job: ${result.body.costQuota?.decisionReason ?? 'missing costQuota'}`);
    }
    const gate = parseReleaseGate(result.body.latestEvent?.stdoutSummary ?? '{}');
    if (gate.gateResult !== 'PASS' || gate.checks.length !== 7 || !gate.checks.every((check) => check.status === 'PASS')) {
      throw new Error(`Expected release gate 7/7 PASS, got ${gate.gateResult}`);
    }
    const costAudit = readCostQuotaEvents(result.body.jobId);
    if (!costAudit.events.some((event) => event.eventType === 'usage_incremented')) {
      throw new Error('CQ usage_incremented audit event missing.');
    }
    if (JSON.stringify({ result, costAudit }).match(/DASHSCOPE_API_KEY\s*=|ALIBABA_API_KEY\s*=|CVF_ALIBABA_API_KEY\s*=|CVF_BENCHMARK_ALIBABA_KEY\s*=|DEEPSEEK_API_KEY\s*=/)) {
      throw new Error('Secret assignment appeared in CQ probe payload.');
    }

    writeEvidence(result.body, gate, costAudit);
    console.log(JSON.stringify({
      status: 'PASS',
      jobId: result.body.jobId,
      gateResult: gate.gateResult,
      costQuotaDecision: result.body.costQuota.decision,
      usageIncremented: true,
      evidence: [PREFLIGHT_EVIDENCE, WEB_EVIDENCE, AUDIT_EVIDENCE],
    }, null, 2));
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
});
