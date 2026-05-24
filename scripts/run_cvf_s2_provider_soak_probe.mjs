#!/usr/bin/env node
import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const probePath = path.join(repoRoot, 'scripts', 'run_post_phase2b_provider_stability_probe.mjs');

const env = {
  ...process.env,
  CVF_POST_PHASE2B_PROVIDERS: process.env.CVF_POST_PHASE2B_PROVIDERS ?? 'alibaba,deepseek,openai',
  CVF_POST_PHASE2B_REPEATS: process.env.CVF_POST_PHASE2B_REPEATS ?? '5',
  CVF_POST_PHASE2B_INTER_JOURNEY_DELAY_MS: process.env.CVF_POST_PHASE2B_INTER_JOURNEY_DELAY_MS ?? '1500',
  CVF_POST_PHASE2B_PROVIDER_STABILITY_PORT: process.env.CVF_POST_PHASE2B_PROVIDER_STABILITY_PORT ?? '3228',
};

const child = spawn(process.execPath, [probePath], {
  cwd: repoRoot,
  env,
  stdio: 'inherit',
});

child.on('exit', (code, signal) => {
  if (signal) {
    console.error(JSON.stringify({ schemaVersion: 'cvf-s2-provider-soak-wrapper-1', status: 'ERROR', signal }, null, 2));
    process.exitCode = 1;
    return;
  }
  process.exitCode = code ?? 1;
});
