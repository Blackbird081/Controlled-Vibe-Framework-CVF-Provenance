'use strict';
// Plain node, no child processes and no native/browser/filesystem effects.
const assert = require('node:assert/strict');
const path = require('node:path');
const crypto = require('node:crypto');
const fencePath = require.resolve('./cvf_ncr_html_browser_fence.cjs');
const { verifyBinding, installFence } = require(fencePath);
const journey = require('./cvf_ncr_html_owned_profile/journey.cjs');
const root = path.resolve(__dirname, '..');
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const sort = value => Array.isArray(value) ? value.map(sort) : value && typeof value === 'object'
  ? Object.fromEntries(Object.keys(value).sort().map(k => [k, sort(value[k])])) : value;
const bytes = value => Buffer.from(JSON.stringify(sort(value)));
let passed = 0;
function test(name, callback) { callback(); passed++; console.log('PASS ' + name); }
function fixture() {
  let now = 0;
  const custody = path.join(root, '.cvf', 'runtime', 'ncr-be-adjunct-source-20261016', 'fake-browser', 'custody');
  const profile = path.join(path.dirname(custody), 'source', 'browser-profile');
  const input = { title: 'Synthetic', sourcePath: 'synthetic/one', sourceContent: 'text', memoryClass: 'FULL_RECORD',
    status: 'DRAFT', claimBoundary: 'fake only', receiptAnchor: 'one' };
  const cfg = { inputs: [input], cap: 1, browserProfile: profile, generation: 'g123',
    deadlineAtMs: 10000, cleanupAtMs: 11000, workMs: 10000, cleanupMs: 1000 };
  const files = new Map();
  const add = (location, raw) => { files.set(location, raw); return { path: location, sha256: sha(raw) }; };
  const binding = { schemaVersion: 'cvf.ncrHtmlBrowserBinding@1', runId: 'fake-local', actor: 'LOCAL_REVIEWER', cap: 1,
    entry: add(path.join(root, 'scripts', 'probe_cvf_w05_browser_chain.cjs'), Buffer.from('entry')),
    journey: add(path.join(root, 'scripts', 'cvf_ncr_html_owned_profile', 'journey.cjs'), Buffer.from('journey')),
    preload: add(fencePath, Buffer.from('preload')),
    config: add(path.join(custody, 'journey-input.json'), bytes(cfg)),
    modulesPath: path.join(root, 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web', 'node_modules'),
    profilePath: profile, observationPath: path.join(custody, 'browser-fence.json'),
    chrome: { path: 'C:\\Users\\DELL\\AppData\\Local\\ms-playwright\\chromium-1208\\chrome-win64\\chrome.exe',
      sha256: 'ff0c99fc5bb2301cad77930aa76e5354cf2a5fefb7efdcf3b3bc10ba0550c015' } };
  const chromeBytes = Buffer.from('modeled qualified Chrome');
  files.set(binding.chrome.path, chromeBytes);
  const calls = [], observations = [];
  const chromium = { launchPersistentContext(profile, options) { calls.push({ receiver: this, profile, options }); return 'original-result'; } };
  const deps = { argv: ['node', binding.entry.path, binding.modulesPath, 'http://localhost:1',
      path.join(custody, 'browser.json'), custody, 'owned-profile', binding.journey.path, binding.config.path],
    read: name => { assert.ok(files.has(name), 'modeled file missing'); return files.get(name); },
    checkPath: name => assert.equal(typeof name, 'string'),
    sha: raw => raw.equals(chromeBytes) ? binding.chrome.sha256 : sha(raw),
    load: name => name === binding.journey.path ? { validateInputs: journey.validateInputs,
      authority: limits => journey.authority(limits, () => now, () => 0) }
      : (assert.equal(name, path.join(binding.modulesPath, '@playwright/test')), { chromium }),
    writeObservation: (location, row) => { assert.equal(location, binding.observationPath); observations.push(row); } };
  const install = () => installFence(verifyBinding(bytes(binding), sha(bytes(binding)), deps), deps);
  return { binding, cfg, files, deps, chromium, calls, observations, install, advance: value => { now = value; } };
}
test('plain import exposes exact APIs without installation', () => {
  assert.deepEqual(Object.keys(require(fencePath)).sort(), ['installFence', 'verifyBinding']);
});
test('qualified path, original receiver, restrictive timeout and observation', () => {
  const f = fixture(); const handle = f.install(); f.advance(9750);
  assert.equal(f.chromium.launchPersistentContext(f.binding.profilePath, { headless: true, timeout: 1000 }), 'original-result');
  assert.equal(f.calls.length, 1); assert.equal(f.calls[0].receiver, f.chromium);
  assert.equal(f.calls[0].options.timeout, 250);
  assert.equal(f.calls[0].options.executablePath, f.binding.chrome.path);
  assert.deepEqual(Object.keys(f.observations[0]).sort(), ['schemaVersion', 'runId', 'actor', 'cap', 'bindingSha256',
    'configSha256', 'preloadSha256', 'chrome', 'verified', 'invocations'].sort());
  assert.equal(f.observations[0].verified, true); assert.equal('launched' in f.observations[0], false);
  assert.deepEqual(handle.snapshot(), { invocations: 1 });
  assert.throws(() => f.chromium.launchPersistentContext(f.binding.profilePath, { headless: true, timeout: 1 }));
  assert.equal(f.calls.length, 1);
});
for (const [name, options] of Object.entries({ channel: { channel: '' }, path: { executablePath: 'other' },
  zero: { timeout: 0 }, negative: { timeout: -1 }, bool: { timeout: true }, nan: { timeout: NaN },
  infinity: { timeout: Infinity }, headless: { headless: false } })) {
  test('refuse options ' + name + ' and spend invocation', () => {
    const f = fixture(); f.install();
    assert.throws(() => f.chromium.launchPersistentContext(f.binding.profilePath, { headless: true, timeout: 100, ...options }));
    assert.throws(() => f.chromium.launchPersistentContext(f.binding.profilePath, { headless: true, timeout: 100 }));
    assert.equal(f.calls.length, 0);
  });
}
for (const kind of ['hash', 'observation']) {
  test('verification ' + kind + ' consumes deadline before delegate', () => {
    const f = fixture(); f.install();
    if (kind === 'hash') {
      const read = f.deps.read;
      f.deps.read = location => { if (location === f.binding.chrome.path) f.advance(10000); return read(location); };
    } else f.deps.writeObservation = () => f.advance(10000);
    assert.throws(() => f.chromium.launchPersistentContext(f.binding.profilePath, { headless: true, timeout: 1000 }));
    assert.equal(f.calls.length, 0);
  });
}
for (const kind of ['profile', 'receiver', 'chrome', 'config', 'persist']) {
  test('call boundary refuses ' + kind, () => {
    const f = fixture(); f.install();
    if (kind === 'chrome') f.files.set(f.binding.chrome.path, Buffer.from('drift'));
    if (kind === 'config') f.files.set(f.binding.config.path, Buffer.from('{}'));
    if (kind === 'persist') f.deps.writeObservation = () => { throw new Error('modeled persist failure'); };
    assert.throws(() => f.chromium.launchPersistentContext.call(kind === 'receiver' ? {} : f.chromium,
      kind === 'profile' ? 'other' : f.binding.profilePath, { headless: true, timeout: 100 }));
    assert.equal(f.calls.length, 0);
  });
}
for (const kind of ['unknown', 'actor', 'cap', 'argv', 'module', 'config', 'profile', 'digest', 'duplicate', 'whitespace', 'bom', 'utf8']) {
  test('binding refusal ' + kind, () => {
    const f = fixture();
    if (kind === 'unknown') f.binding.extra = 1;
    if (kind === 'actor') f.binding.actor = 'IMPLEMENTATION_WORKER';
    if (kind === 'cap') f.binding.cap = true;
    if (kind === 'argv') f.deps.argv[6] = 'legacy';
    if (kind === 'module') f.binding.modulesPath += '-other';
    if (kind === 'config') f.files.set(f.binding.config.path, Buffer.from('{}'));
    if (kind === 'profile') f.binding.profilePath += '-other';
    let raw = bytes(f.binding);
    if (kind === 'duplicate') raw = Buffer.from(raw.toString().replace('"cap":1', '"cap":1,"cap":1'));
    if (kind === 'whitespace') raw = Buffer.concat([raw, Buffer.from('\n')]);
    if (kind === 'bom') raw = Buffer.concat([Buffer.from([239, 187, 191]), raw]);
    if (kind === 'utf8') raw = Buffer.from([255]);
    assert.throws(() => verifyBinding(raw, kind === 'digest' ? '0'.repeat(64) : sha(raw), f.deps));
    assert.equal(f.calls.length, 0);
  });
}
test('partial environment activation refuses with no module or browser effect', () => {
  process.env.CVF_NCR_BROWSER_BINDING_PATH = 'synthetic-only';
  delete require.cache[fencePath];
  try { assert.throws(() => require(fencePath), /partial browser binding/); }
  finally { delete process.env.CVF_NCR_BROWSER_BINDING_PATH; delete require.cache[fencePath]; }
});
console.log(JSON.stringify({ passed, failed: 0, effects: { children: 0, browser: 0, network: 0, provider: 0 }, fixture: 'IN_MEMORY_ONLY' }));
