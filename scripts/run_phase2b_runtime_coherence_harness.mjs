#!/usr/bin/env node
/**
 * Phase 2.B runtime-coherence harness wrapper.
 *
 * Runs the targeted Guard Contract coherence validator tests and emits a small
 * machine-readable result. This wrapper does not load live provider keys and
 * does not perform web/provider runtime work.
 */

import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const guardContract = path.join(repoRoot, 'EXTENSIONS', 'CVF_GUARD_CONTRACT');
const args = new Set(process.argv.slice(2));
const jsonOut = args.has('--json');

const command = [
  'npm',
  'test',
  '--',
  '--run',
  'src/contracts/contracts.phase2b-runtime-coherence.test.ts',
];

const startedAt = new Date().toISOString();
const result = spawnSync(command[0], command.slice(1), {
  cwd: guardContract,
  shell: process.platform === 'win32',
  encoding: 'utf8',
});
const completedAt = new Date().toISOString();
const combinedOutput = `${result.stdout ?? ''}\n${result.stderr ?? ''}`;
const pass = result.status === 0;
const testSummary = combinedOutput
  .split(/\r?\n/)
  .filter((line) => /Test Files|Tests|passed|failed/i.test(line.trim()))
  .slice(-6);

const payload = {
  schemaVersion: 'phase2b-runtime-coherence-harness-result-1',
  status: pass ? 'PASS' : 'FAIL',
  evidenceMode: 'internal_fixture',
  command: command.join(' '),
  cwd: path.relative(repoRoot, guardContract),
  startedAt,
  completedAt,
  runtimeCoherenceProven: pass,
  liveProofProven: false,
  testSummary,
};

if (jsonOut) {
  process.stdout.write(`${JSON.stringify(payload, null, 2)}\n`);
} else {
  process.stdout.write(`Phase 2.B runtime coherence: ${payload.status}\n`);
  for (const line of testSummary) {
    process.stdout.write(`${line}\n`);
  }
}

process.exit(pass ? 0 : 1);
