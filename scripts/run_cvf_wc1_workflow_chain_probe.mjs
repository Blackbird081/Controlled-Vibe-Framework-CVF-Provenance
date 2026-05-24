#!/usr/bin/env node
import { createHmac } from 'node:crypto';
import { spawn, spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, rmSync } from 'node:fs';
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
const port = Number(process.env.CVF_WC1_WORKFLOW_CHAIN_PORT ?? 3235);
const baseUrl = `http://127.0.0.1:${port}`;
const scope = 'project:wc1-workflow-chain';

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

function buildWritePayload() {
  return {
    templateId: 'strategy_analysis',
    templateName: 'Strategy Analysis',
    intent: 'WC1 turn 1: create a bounded workflow-chain memory note. Include the phrase WC1 workflow chain in the useful summary.',
    inputs: {
      topic: 'WC1 workflow chain proof turn 1',
      context: 'This turn should produce a bounded note that can be stored as summary-only durable skill memory.',
      options: 'Write memory after live ALLOW execution\nKeep receipt evidence\nDo not claim autonomous reinjection',
      constraints: 'Summary-only memory; canReinject remains false; raw memory must not be released.',
      priority: 'R1',
    },
    provider: 'alibaba',
    model: 'qwen-turbo',
    mode: 'governance',
    cvfPhase: 'PHASE D',
    cvfRiskLevel: 'R1',
    action: 'test',
    skillPreflightPassed: true,
    skillPreflightDeclaration: 'WC1 live probe turn 1 declares bounded strategy_analysis execution before provider dispatch.',
    skillPreflightRecordRef: 'wc1-workflow-chain-turn-1',
    skillIds: ['strategy_analysis'],
    aiCommit: {
      commitId: `wc1-workflow-chain-turn-1-${Date.now()}`,
      agentId: 'codex-wc1-live-probe',
      timestamp: Date.now(),
      description: 'WC1 turn 1 bounded durable memory write proof',
    },
    durableMemoryWrite: {
      enabled: true,
      tier: 'skill',
      scope,
      policy: { actorAuthorized: true },
      maxSummaryLength: 300,
    },
  };
}

function buildReadPayload(writeReceipt) {
  return {
    templateId: 'strategy_analysis',
    templateName: 'Strategy Analysis',
    intent: `WC1 turn 2: read the prior summary-only durable memory context. Reference prior receipt ${writeReceipt.receiptId ?? 'unknown'} only as evidence metadata, not as authority.`,
    inputs: {
      topic: 'WC1 workflow chain proof turn 2',
      context: 'This turn should use route-injected summary-only durable memory if the receipt proves it was read.',
      options: 'Read previous memory summary\nPreserve canReinject=false\nDo not expose raw memory',
      constraints: 'Receipt evidence is the proof of retrieval. Model output alone is not enough.',
      priority: 'R1',
    },
    provider: 'alibaba',
    model: 'qwen-turbo',
    mode: 'governance',
    cvfPhase: 'PHASE D',
    cvfRiskLevel: 'R1',
    action: 'test',
    skillPreflightPassed: true,
    skillPreflightDeclaration: 'WC1 live probe turn 2 declares bounded durable-memory read before provider dispatch.',
    skillPreflightRecordRef: 'wc1-workflow-chain-turn-2',
    skillIds: ['strategy_analysis'],
    aiCommit: {
      commitId: `wc1-workflow-chain-turn-2-${Date.now()}`,
      agentId: 'codex-wc1-live-probe',
      timestamp: Date.now(),
      description: 'WC1 turn 2 bounded durable memory read proof',
    },
    durableMemory: {
      enabled: true,
      tier: 'skill',
      scope,
      query: '',
      maxResults: 3,
      policy: { actorAuthorized: true },
    },
  };
}

async function signedExecute(payload) {
  const bodyText = JSON.stringify(payload);
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
  return { response, latencyMs, data };
}

function readStoreRecords(storePath) {
  if (!existsSync(storePath)) return [];
  const parsed = JSON.parse(readFileSync(storePath, 'utf8'));
  return Array.isArray(parsed) ? parsed : [];
}

async function main() {
  loadEnvFiles();
  if (!process.env.CVF_SERVICE_TOKEN) throw new Error('missing_cvf_service_token');
  if (!process.env.DASHSCOPE_API_KEY) throw new Error('missing_dashscope_api_key');

  const tempDir = path.join(os.tmpdir(), `cvf-wc1-live-${Date.now()}`);
  mkdirSync(tempDir, { recursive: true });
  const storePath = path.join(tempDir, 'durable-memory.json');
  const server = spawn(process.platform === 'win32' ? 'npm.cmd' : 'npm', ['run', 'dev', '--', '--port', String(port)], {
    cwd: cvfWeb,
    env: buildChildEnv(storePath),
    stdio: ['ignore', 'pipe', 'pipe'],
    shell: process.platform === 'win32',
  });
  let serverTail = '';
  const appendTail = (chunk) => {
    serverTail = `${serverTail}${chunk.toString()}`.slice(-4000);
  };
  server.stdout.on('data', appendTail);
  server.stderr.on('data', appendTail);

  try {
    await waitForServer(server);

    const turn1 = await signedExecute(buildWritePayload());
    const turn1Receipt = turn1.data.governanceEvidenceReceipt ?? {};
    const writeReceipt = turn1.data.durableMemoryWriteReceipt
      ?? turn1Receipt.durableMemoryWriteReceipt
      ?? {};
    const recordsAfterWrite = readStoreRecords(storePath);

    const turn2 = await signedExecute(buildReadPayload(turn1Receipt));
    const turn2Receipt = turn2.data.governanceEvidenceReceipt ?? {};
    const readReceipt = turn2.data.durableMemoryRead
      ?? turn2Receipt.durableMemoryRead
      ?? {};
    const recordsAfterRead = readStoreRecords(storePath);

    const writtenMemoryIds = Array.isArray(writeReceipt.memoryIds) ? writeReceipt.memoryIds : [];
    const readMemoryIds = Array.isArray(readReceipt.memoryIds) ? readReceipt.memoryIds : [];
    const assertions = {
      turn1HttpStatus200: turn1.response.status === 200,
      turn1SuccessTrue: turn1.data.success === true,
      turn1EvidenceModeLive: turn1Receipt.evidenceMode === 'live',
      turn1ReceiptPresent: typeof turn1Receipt.receiptId === 'string' && turn1Receipt.receiptId.length > 5,
      writeReceiptAllowed: writeReceipt.operation === 'write' && writeReceipt.decision === 'allowed',
      writeRawMemoryReleasedFalse: writeReceipt.rawMemoryReleased === false,
      writeCanReinjectFalse: writeReceipt.canReinject === false,
      writePersistedRecord: recordsAfterWrite.some((record) => writtenMemoryIds.includes(record.id) && record.scope === scope),
      turn2HttpStatus200: turn2.response.status === 200,
      turn2SuccessTrue: turn2.data.success === true,
      turn2EvidenceModeLive: turn2Receipt.evidenceMode === 'live',
      turn2ReceiptPresent: typeof turn2Receipt.receiptId === 'string' && turn2Receipt.receiptId.length > 5,
      readReceiptAllowed: readReceipt.operation === 'read' && readReceipt.decision === 'allowed',
      readIncludesWrittenMemory: writtenMemoryIds.length > 0 && writtenMemoryIds.every((id) => readMemoryIds.includes(id)),
      readSummaryOnly: readReceipt.summaryOnly === true,
      readRawMemoryReleasedFalse: readReceipt.rawMemoryReleased === false,
      readCanReinjectFalse: readReceipt.canReinject === false,
      storeStillContainsRecord: recordsAfterRead.some((record) => writtenMemoryIds.includes(record.id) && record.scope === scope),
    };
    const failedAssertions = Object.entries(assertions)
      .filter(([, passed]) => !passed)
      .map(([name]) => name);
    const proof = {
      schemaVersion: 'cvf-wc1-workflow-chain-live-result-1',
      status: failedAssertions.length === 0 ? 'PASS' : 'FAIL',
      claimClass: failedAssertions.length === 0
        ? 'bounded_two_turn_workflow_chain_write_then_read'
        : 'workflow_chain_proof_blocked',
      scope,
      turn1: {
        httpStatus: turn1.response.status,
        latencyMs: turn1.latencyMs,
        success: turn1.data.success ?? null,
        provider: turn1Receipt.provider ?? turn1.data.provider ?? null,
        model: turn1Receipt.model ?? turn1.data.model ?? null,
        receiptId: turn1Receipt.receiptId ?? null,
        traceId: turn1Receipt.envelopeId ?? turn1.data.governanceEnvelope?.envelopeId ?? null,
        evidenceMode: turn1Receipt.evidenceMode ?? null,
        durableMemoryWriteReceipt: {
          decision: writeReceipt.decision ?? null,
          reason: writeReceipt.reason ?? null,
          memoryIds: writtenMemoryIds,
          rawMemoryReleased: writeReceipt.rawMemoryReleased ?? null,
          canReinject: writeReceipt.canReinject ?? null,
        },
      },
      turn2: {
        httpStatus: turn2.response.status,
        latencyMs: turn2.latencyMs,
        success: turn2.data.success ?? null,
        provider: turn2Receipt.provider ?? turn2.data.provider ?? null,
        model: turn2Receipt.model ?? turn2.data.model ?? null,
        receiptId: turn2Receipt.receiptId ?? null,
        traceId: turn2Receipt.envelopeId ?? turn2.data.governanceEnvelope?.envelopeId ?? null,
        evidenceMode: turn2Receipt.evidenceMode ?? null,
        durableMemoryRead: {
          decision: readReceipt.decision ?? null,
          reason: readReceipt.reason ?? null,
          memoryIds: readMemoryIds,
          summaryOnly: readReceipt.summaryOnly ?? null,
          rawMemoryReleased: readReceipt.rawMemoryReleased ?? null,
          canReinject: readReceipt.canReinject ?? null,
        },
      },
      persistedRecordCount: recordsAfterRead.length,
      security: {
        rawSecretPrinted: false,
        rawMemoryReleased: false,
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
      schemaVersion: 'cvf-wc1-workflow-chain-live-result-1',
      status: 'ERROR',
      error: error instanceof Error ? error.message : String(error),
      serverTail: redact(serverTail),
    };
    assertNoSecretLeak(failure);
    console.error(JSON.stringify(failure, null, 2));
    process.exitCode = 1;
  } finally {
    killProcessTree(server);
    rmSync(tempDir, { recursive: true, force: true });
  }
}

main();
