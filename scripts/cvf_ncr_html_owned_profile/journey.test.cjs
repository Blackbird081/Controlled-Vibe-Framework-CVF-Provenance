/* Pure input/branch regressions; no browser/engine/provider/substitute start. */
'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const cp = require('node:child_process');
const path = require('node:path');
const { validateInputs } = require('./journey.cjs');
const input = { title: 'Synthetic Local Draft', sourcePath: 'synthetic/local.md', memoryClass: 'FULL_RECORD',
  status: 'Draft', receiptAnchor: 'local-one', claimBoundary: 'Synthetic only.', sourceContent: 'Owned source.' };

test('Local distinct one-build and worker two-build budgets are explicit', () => {
  validateInputs([input], 1);
  validateInputs([input, { ...input, receiptAnchor: 'second' }], 2);
  for (const cap of [0, 3, true, '1']) assert.throws(() => validateInputs([input], cap));
  assert.throws(() => validateInputs([input], 2));
  assert.throws(() => validateInputs([input, input], 2));
});
test('missing/substituted input fields fail before login', () => {
  assert.throws(() => validateInputs([{ ...input, title: '' }], 1));
  assert.throws(() => validateInputs([{ ...input, memoryClass: 'ADMIN' }], 1));
  assert.throws(() => validateInputs([{ ...input, sourcePath: 'operator/data' }], 1));
  assert.throws(() => validateInputs([{ ...input, added: true }], 1));
});
test('legacy browser branches survive exact routing-only patch', () => {
  const rel = 'scripts/probe_cvf_w05_browser_chain.cjs';
  const current = fs.readFileSync(path.join(__dirname, '..', 'probe_cvf_w05_browser_chain.cjs'), 'utf8');
  const original = cp.execFileSync('git', ['show', 'HEAD:' + rel], { encoding: 'utf8' });
  const route = "  if (mode === 'owned-profile') return require(process.argv[7]).run({ modules, baseURL, output, custody: downloadDir, control: controlChannel(), config: process.argv[8] });\n";
  const restored = current.replace(route, '').replace('}\nmain().catch', '}\n\nmain().catch');
  assert.equal(restored, original);
  assert.ok(current.includes("mode === 'configured-receipt-composition'"));
});
