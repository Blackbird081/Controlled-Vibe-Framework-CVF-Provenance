/* Pure input, timing, lazy-call, reply and teardown regressions; no browser, engine, provider, substitute start or Git. Fake modules live in ignored worker custody. */
'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const net = require('node:net');
const path = require('node:path');
const { createHash, randomBytes } = require('node:crypto');

if (process.env.CVF_NCR_ALLOWED_PORTS || process.env.CVF_HCR_EGRESS_LOG) throw new Error('inherited network-guard activation is refused in the pure test environment');
const connect = net.Socket.prototype.connect;
const { validateInputs, authority, withBudget, teardown, validateReply, actor, controller, run } = require('./journey.cjs');
const input = { title: 'Synthetic Local Draft', sourcePath: 'synthetic/local.md', memoryClass: 'FULL_RECORD',
  status: 'Draft', receiptAnchor: 'local-one', claimBoundary: 'Synthetic only.', sourceContent: 'Owned source.' };
const COMBINING = String.fromCharCode(0x301); // decomposed (non-NFC) accent
const BLOB_SHA256 = '2f0981b2356a51a85f34d3d6ed94a0d0a0606c48d306888711876a5c2b225dec'; // sha256 of the immutable 0850546 entrypoint blob
const SCRATCH = path.join(__dirname, '..', '..', '.cvf', 'runtime', 'ncr-html-root-local-repair-20261016', 'node-' + randomBytes(6).toString('hex'));
const T = 1_000_000; // injected wall clock at the moment the parent wrote the limits
const limits = (over = {}) => ({ generation: 'g1', deadlineAtMs: T + 60000, workMs: 60000, cleanupAtMs: T + 70000, cleanupMs: 10000, ...over });
const clocks = (wall = T, up = 0) => [() => wall, () => up];

test('Local distinct one-build and worker two-build budgets are explicit', () => {
  validateInputs([input], 1);
  validateInputs([input, { ...input, receiptAnchor: 'second' }], 2);
  for (const cap of [0, 3, true, '1', 1.5, null]) assert.throws(() => validateInputs([input], cap));
  assert.throws(() => validateInputs([input], 2));
  assert.throws(() => validateInputs([input, input], 2));
});

test('missing, extra, mistyped and non-synthetic inputs fail before login', () => {
  const bad = [{ ...input, title: '' }, { ...input, memoryClass: 'ADMIN' }, { ...input, sourcePath: 'operator/data' }, { ...input, added: true },
    { ...input, status: 7 }, { ...input, title: 'Bad/Title' }, { ...input, sourcePath: 'synthetic/../secret' }, { ...input, sourcePath: 'synthetic/./x' },
    { ...input, sourcePath: 'synthetic\\win' }, { ...input, title: 'Cafe' + COMBINING }, { ...input, claimBoundary: 'e' + COMBINING }, null, [], 'text'];
  for (const value of bad) assert.throws(() => validateInputs([value], 1), JSON.stringify(value));
  const { title, ...missing } = input;
  assert.throws(() => validateInputs([missing], 1));
  for (const value of [null, {}, 'x', [[input]]]) assert.throws(() => validateInputs(value, 1));
  assert.throws(() => validateInputs([input, { ...input, receiptAnchor: input.receiptAnchor }], 2));
});

test('every allowance is one clock sample, a positive integer, never zero, and refuses a sub-unit or exhausted remainder', () => {
  let samples = 0;
  const { work, cleanup } = authority(limits(), () => { samples += 1; return T; }, () => 0);
  assert.equal(work(30000), 30000);
  assert.equal(work(900000), 60000);
  assert.equal(cleanup(900000), 70000);
  assert.equal(samples, 3);
  assert.throws(() => authority(limits(), () => T + 59999.5, () => 0).work(1000), /allowance exhausted/); // .5ms left: nothing starts, never timeout 0
  let t = T;  // the clock advances at every sample, so a deadline can be crossed between check and use
  const steady = authority(limits({ deadlineAtMs: T + 1000 }), () => (t += 400), () => 0), waits = [];
  for (let i = 0; i < 4; i += 1) { try { waits.push(steady.work(30000)); } catch (e) { waits.push('refused'); } }
  assert.deepEqual(waits, [600, 200, 'refused', 'refused']);
  for (const bad of [{ workMs: 900001 }, { workMs: 0 }, { cleanupMs: 120001 }, { generation: 'x' }, { deadlineAtMs: NaN }, { cleanupAtMs: '5' }]) assert.throws(() => authority(limits(bad), ...clocks()));
  assert.throws(() => authority(null, ...clocks()));
});

test('child startup delay and a wall-clock rollback can only shorten the parent authority', () => {
  assert.equal(authority(limits(), ...clocks()).work(900000), 60000);
  assert.equal(authority(limits(), ...clocks(T, 59000)).work(900000), 1000);          // started 59s late: that time is already spent
  assert.equal(authority(limits(), ...clocks(T - 500000, 1000)).work(900000), 59000); // wall clock rolled back: monotonic uptime still governs
  assert.equal(authority(limits(), ...clocks(T + 30000, 0)).work(900000), 30000);     // a late wall clock shortens through the absolute cutoff
  assert.equal(authority(limits(), ...clocks(T, 50000)).cleanup(900000), 20000);
});

test('an exhausted deadline invokes neither the control callback nor any lazily admitted operation', async () => {
  const calls = [], spent = authority(limits({ deadlineAtMs: T }), ...clocks());
  const act = actor(spent.work), ctl = controller(async () => { calls.push('control'); return ''; }, spent.work, 'g1');
  assert.throws(() => act('fill', 30000, () => calls.push('fill')), /allowance exhausted/);
  await assert.rejects(ctl(op => 'CHECKPOINT stale g1 ' + op, 'CHECKPOINT_OK stale'), /allowance exhausted/);
  assert.deepEqual(calls, []);
  const seen = [];
  assert.equal(await actor(authority(limits(), ...clocks()).work)('ok', 5000, o => { seen.push(o.timeout); return 1; }), 1);
  assert.deepEqual(seen, [5000]);
});

test('the whole reply must match kind, argument, generation and operation; tails and partial prefixes are refused', async () => {
  const good = 'EXPORT_GATE_OK 1 g1 c1';
  assert.equal(validateReply(good, 'EXPORT_GATE_OK 1', 'g1', 'c1'), good);
  for (const bad of ['EXPORT_GATE_OK 1', 'EXPORT_GATE_OK 1 g1', 'EXPORT_GATE_OK 1 g1 c2', 'EXPORT_GATE_OK 1 g2 c1', 'EXPORT_GATE_OK 2 g1 c1',
    'EXPORT_GATE_OK 1 g1 c1 extra', ' ' + good, good + ' ', 'CHECKPOINT_OK 1 g1 c1', 'EXPORT_GATE_OK 10 g1 c1']) {
    assert.throws(() => validateReply(bad, 'EXPORT_GATE_OK 1', 'g1', 'c1'), assert.AssertionError);
  }
  const { work } = authority(limits(), ...clocks());  // the prefix-only legacy channel would accept every one of these replies
  const reply = suffix => controller(async request => 'CHECKPOINT_OK stale g1 ' + request.split(' ').pop() + suffix, work, 'g1');
  const build = op => 'CHECKPOINT stale g1 ' + op;
  await assert.rejects(controller(async () => 'EXPORT_GATE_OK 1 g9 c1', work, 'g1')(op => 'x', 'EXPORT_GATE_OK 1'), assert.AssertionError);
  await assert.rejects(reply(' tail')(build, 'CHECKPOINT_OK stale'), assert.AssertionError);
  const exact = reply('');
  assert.equal(await exact(build, 'CHECKPOINT_OK stale'), 'CHECKPOINT_OK stale g1 c1');
  assert.equal(await exact(build, 'CHECKPOINT_OK stale'), 'CHECKPOINT_OK stale g1 c2'); // each call is a fresh operation
});

test('withBudget is a lazy wait bound that reports UNKNOWN; teardown steps stay independent and an exhausted remainder is NOT_ATTEMPTED', async () => {
  assert.equal(await withBudget(() => 7, 1000, 'quick'), 7);
  let started = false;
  await assert.rejects(withBudget(() => new Promise(() => { started = true; }), 20, 'hung'), /hung: no completion within 20ms; outcome UNKNOWN/);
  assert.ok(started);
  await assert.rejects(withBudget(() => Promise.reject(new Error('boom')), 1000, 'bad'), /boom/);
  const ran = [];
  const report = await teardown([['close', async () => { ran.push('close'); throw new Error('close rejected'); }], ['hang', () => new Promise(() => ran.push('hang'))],
    ['save', () => ran.push('save')], ['stdin', () => ran.push('stdin')]], authority(limits({ cleanupAtMs: T + 5000 }), ...clocks()).cleanup, 30);
  assert.deepEqual(ran, ['close', 'hang', 'save', 'stdin']);
  assert.deepEqual(Object.keys(report), ['close', 'hang', 'save', 'stdin']);
  assert.match(report.close, /^FAILED: close rejected/);
  assert.match(report.hang, /outcome UNKNOWN/);
  assert.deepEqual([report.save, report.stdin], ['OK', 'OK']);
  const spent = await teardown([['late', () => ran.push('late')]], authority(limits({ cleanupAtMs: T }), ...clocks()).cleanup, 30);
  assert.match(spent.late, /^NOT_ATTEMPTED/);
  assert.ok(!ran.includes('late'));
});

async function drive(name, { close, destroy = () => {}, over = {} } = {}) {
  // Fake @playwright/test lives in a real directory, so the module path is resolved by the OS, never by a platform-sensitive selector.
  const dir = path.join(SCRATCH, name), modules = path.join(dir, 'modules'), calls = [], emitted = [];
  fs.mkdirSync(path.join(modules, '@playwright', 'test'), { recursive: true });
  fs.writeFileSync(path.join(modules, '@playwright', 'test', 'package.json'), JSON.stringify({ name: 'fake', main: 'index.js' }));
  fs.writeFileSync(path.join(modules, '@playwright', 'test', 'index.js'), 'module.exports = { expect: () => ({}), chromium: { launchPersistentContext: async () => { global.__calls.push("launch"); return global.__fakeContext; } } };');
  global.__calls = calls;
  global.__fakeContext = { route: () => { calls.push('route'); throw new Error('stop after launch'); }, close: () => { calls.push('close'); return close ? close() : undefined; } };
  const config = path.join(dir, 'config.json'), output = path.join(dir, 'browser.json');
  fs.writeFileSync(config, JSON.stringify({ inputs: [input], cap: 1, browserProfile: path.join(dir, 'profile'), ...limits(over) }));
  const original = process.stdin.destroy;
  process.stdin.destroy = () => { calls.push('stdinDestroy'); return destroy(); };
  try {
    await run({ modules, baseURL: 'http://localhost:1', output, custody: dir, control: async () => {}, config, now: () => T, uptime: () => 0, emit: s => emitted.push(s) });
    const saved = fs.existsSync(output) ? fs.readFileSync(output) : null;
    return { calls, emitted, exit: process.exitCode, saved, json: saved && JSON.parse(saved.toString('utf8')) };
  } finally {
    process.stdin.destroy = original;
    process.exitCode = undefined;
    delete global.__fakeContext;
    delete global.__calls;
  }
}

test('close rejection, hang or stdin failure never skips the save and every outcome is inside the one frozen snapshot', async () => {
  const claimOf = r => `SNAPSHOT ${createHash('sha256').update(r.saved).digest('hex')} ${r.saved.length}\n`;
  const rejected = await drive('close-rejected', { close: async () => { throw new Error('close rejected'); } });
  assert.deepEqual(rejected.calls, ['launch', 'route', 'close', 'stdinDestroy']);
  assert.match(rejected.json.error, /stop after launch/);
  assert.match(rejected.json.teardown.contextClose, /^FAILED: close rejected/);
  assert.equal(rejected.json.teardown.stdinDestroy, 'OK');
  assert.deepEqual([rejected.json.partial, rejected.exit, rejected.emitted], [true, 1, [claimOf(rejected)]]); // a failed attempt is never a zero exit
  assert.deepEqual(Object.keys(rejected.json.teardown), ['contextClose', 'stdinDestroy']); // the snapshot never claims its own save
  const hung = await drive('close-hung', { close: () => new Promise(() => {}), over: { cleanupAtMs: T + 50 } });
  assert.match(hung.json.teardown.contextClose, /outcome UNKNOWN/);
  assert.deepEqual([hung.calls, hung.json.teardown.stdinDestroy, hung.emitted], [['launch', 'route', 'close', 'stdinDestroy'], 'OK', [claimOf(hung)]]);
  const stdin = await drive('stdin-failed', { destroy: () => { throw new Error('stdin boom'); } });
  assert.equal(stdin.json.teardown.contextClose, 'OK');
  assert.match(stdin.json.teardown.stdinDestroy, /^FAILED: stdin boom/); // the failed teardown is in the SAVED bytes, not only in memory
  assert.equal(stdin.emitted[0], claimOf(stdin));
});

test('an exhausted cleanup window starts no teardown or write, and an exhausted work window starts no browser', async () => {
  const noCleanup = await drive('cleanup-spent', { over: { cleanupAtMs: T } });
  assert.deepEqual([noCleanup.calls, noCleanup.saved, noCleanup.emitted, noCleanup.exit], [['launch', 'route'], null, [], 1]);
  const noWork = await drive('work-spent', { over: { deadlineAtMs: T } });
  assert.deepEqual(noWork.calls, ['stdinDestroy']); // neither launch nor route ran
  assert.match(noWork.json.error, /allowance exhausted/);
  assert.equal(noWork.json.teardown.contextClose, 'NOT_LAUNCHED');
});

// Full-journey control: a recording fake browser drives every branch of run(); nothing real starts. The fake obeys only what it was asked.
async function journey(name, answer) {
  const dir = path.join(SCRATCH, name), modules = path.join(dir, 'modules'), log = [], requests = [], built = [], pending = {}, served = {};
  const defer = () => { const d = {}; d.promise = new Promise(resolve => { d.resolve = resolve; }); return d; };
  const second = { ...input, title: 'Synthetic Second Draft', sourcePath: 'synthetic/second.md', receiptAnchor: 'second', sourceContent: 'Second source.' };
  fs.mkdirSync(path.join(modules, '@playwright', 'test'), { recursive: true });
  fs.writeFileSync(path.join(modules, '@playwright', 'test', 'package.json'), JSON.stringify({ name: 'fake', main: 'index.js' }));
  fs.writeFileSync(path.join(modules, '@playwright', 'test', 'index.js'), 'module.exports = global.__fakePlaywright;');
  const exportClick = () => {
    const submitted = [input, second][built.length], html = `<html>${createHash('sha256').update(submitted.sourceContent.trim(), 'utf8').digest('hex')}</html>`;
    const post = { method: () => 'POST', url: () => 'http://localhost:1/api/artifacts/export', postDataJSON: () => submitted };
    page.seen(post);
    const data = { html, governanceReceiptStatus: 'PRESENT', governanceReceipt: { receiptId: 'a' + built.length }, governanceReceiptAttemptId: 'a' + built.length,
      receiptAnchor: submitted.receiptAnchor, governanceState: 'DRAFT_UNACCEPTED' };
    built.push(html);
    served.html = html;
    pending.response.resolve({ url: () => post.url(), request: () => post, status: () => 200,
      body: async () => Buffer.from(JSON.stringify({ success: true, data, routeGovernanceProof: { authMode: 'session' } })) });
  };
  const page = {
    on: (event, cb) => { page.seen = cb; }, goto: async () => {}, waitForURL: async () => {}, addInitScript: async () => {}, screenshot: async o => fs.writeFileSync(o.path, 'png'),
    locator: () => ({ fill: async () => {} }), getByLabel: () => ({ fill: async () => {}, selectOption: async () => {} }), getByTestId: () => ({ count: async () => 0 }),
    frameLocator: () => ({ locator: () => ({}) }), waitForEvent: () => (pending.download = defer()).promise,
    waitForResponse: () => (pending.response = defer()).promise,
    getByRole: (role, { name }) => ({ click: async () => {
      const label = name.normalize('NFC');
      if (label === 'T\u1EA1o HTML') exportClick();
      if (label === 'T\u1EA3i HTML') pending.download.resolve({ saveAs: async target => fs.writeFileSync(target, served.html), suggestedFilename: () => 'x.html' });
    } }),
  };
  const context = { route: async () => {}, pages: () => [], newPage: async () => page, close: async () => { log.push('close'); },
    request: { get: async () => ({ json: async () => ({ user: { userId: 'usr_3', role: 'developer', authSource: 'local_mock' } }) }) } };
  global.__fakePlaywright = { chromium: { launchPersistentContext: async () => context }, expect: () => ({ toHaveAttribute: async () => {}, toHaveText: async () => {} }) };
  const control = async (request, expected) => {
    requests.push(request.split(' ').slice(0, request.startsWith('CHECKPOINT') ? 2 : 1).join(' '));
    return answer(expected, request.startsWith('EXPORT_GATE_REQUEST ') ? JSON.parse(request.slice(20)).op : request.split(' ').pop());
  };
  const config = path.join(dir, 'config.json'), output = path.join(dir, 'browser.json'), emitted = [];
  fs.writeFileSync(config, JSON.stringify({ inputs: [input, second], cap: 2, browserProfile: path.join(dir, 'profile'), ...limits() }));
  const original = process.stdin.destroy;
  process.stdin.destroy = () => {};
  try {
    await run({ modules, baseURL: 'http://localhost:1', output, custody: dir, control, config, now: () => T, uptime: () => 0, emit: s => emitted.push(s) });
    return { requests, built, log, emitted, exit: process.exitCode, json: JSON.parse(fs.readFileSync(output, 'utf8')) };
  } finally {
    process.stdin.destroy = original;
    process.exitCode = undefined;
    delete global.__fakePlaywright;
  }
}

test('a complete two-build journey completes only through whole-line replies and freezes one clean snapshot', async () => {
  const ok = await journey('journey-ok', (expected, op) => `${expected} g1 ${op}`);
  assert.deepEqual(ok.requests, ['EXPORT_GATE_REQUEST', 'CHECKPOINT built1', 'CHECKPOINT stale', 'EXPORT_GATE_REQUEST', 'CHECKPOINT built2']);
  assert.deepEqual([ok.json.partial, ok.json.builds.length, ok.json.exportPosts.length, ok.json.teardown, ok.exit], [false, 2, 2, { contextClose: 'OK', stdinDestroy: 'OK' }, undefined]);
  assert.equal(ok.json.stale.priorAttemptId, 'a0');
  assert.equal(ok.emitted.length, 1);
});

test('a reply with a tail, a wrong generation or a wrong operation stops the journey before the next effect', async () => {
  for (const [name, answer] of [['tail', (e, op) => `${e} g1 ${op} tail`], ['generation', (e, op) => `${e} g2 ${op}`], ['operation', (e) => `${e} g1 c9`]]) {
    const bad = await journey('journey-' + name, answer);
    assert.deepEqual([bad.requests, bad.built, bad.json.exportPosts, bad.json.partial, bad.exit, bad.log], [['EXPORT_GATE_REQUEST'], [], [], true, 1, ['close']]); // no export click
    assert.match(bad.json.error, /Expected values to be strictly equal|expected/i);
  }
});
test('import installs no network guard and starts no runtime', () => {
  assert.equal(net.Socket.prototype.connect, connect);
  assert.equal(process.env.CVF_NCR_ALLOWED_PORTS, undefined);
});

test('legacy browser branches survive exact routing-only patch against the pinned immutable blob digest', () => {
  const current = fs.readFileSync(path.join(__dirname, '..', 'probe_cvf_w05_browser_chain.cjs'), 'utf8');
  const route = "  if (mode === 'owned-profile') return require(process.argv[7]).run({ modules, baseURL, output, custody: downloadDir, control: controlChannel(), config: process.argv[8] });\n";
  const restored = current.replace(route, '').replace('}\nmain().catch', '}\n\nmain().catch');
  assert.equal(createHash('sha256').update(restored, 'utf8').digest('hex'), BLOB_SHA256);
  assert.ok(current.includes("mode === 'configured-receipt-composition'"));
});
