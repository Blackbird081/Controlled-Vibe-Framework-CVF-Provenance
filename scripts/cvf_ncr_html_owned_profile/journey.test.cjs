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
  status: 'Draft', receiptAnchor: 'local-one', claimBoundary: 'Synthetic only.', sourceContent: '# Owned heading\nOwned source.' };
const COMBINING = String.fromCharCode(0x301); // decomposed (non-NFC) accent
const BLOB_SHA256 = '2f0981b2356a51a85f34d3d6ed94a0d0a0606c48d306888711876a5c2b225dec'; // sha256 of the immutable 0850546 entrypoint blob
const SCRATCH = path.join(__dirname, '..', '..', '.cvf', 'runtime', 'ncr-login-readiness-source-phase-20261017', 'worker', 'node-' + randomBytes(6).toString('hex'));
const MODULES = path.join(__dirname, '..', '..', 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web', 'node_modules');
const ts = require(path.join(MODULES, 'typescript'));
const { JSDOM } = require(path.join(MODULES, 'jsdom'));
const renderer = path.join(MODULES, '..', 'src', 'app', 'api', 'artifacts', 'export', 'route.ts');
const parsed = ts.createSourceFile(renderer, fs.readFileSync(renderer, 'utf8'), ts.ScriptTarget.Latest, true);
const boundary = parsed.statements.findIndex(n => ts.isFunctionDeclaration(n) && n.name?.text === 'POST' && n.modifiers?.some(m => m.kind === ts.SyntaxKind.ExportKeyword));
assert.ok(boundary >= 0, 'exported POST boundary must exist');
const prefix = ts.factory.updateSourceFile(parsed, parsed.statements.slice(0, boundary).filter(n => !ts.isImportDeclaration(n)));
const code = ts.transpileModule(ts.createPrinter().printFile(prefix), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
const buildHtml = require('node:vm').runInNewContext(code + '\nbuildHtml;', {});
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
async function journey(name, answer, failHeading = false) {
  const dir = path.join(SCRATCH, name), modules = path.join(dir, 'modules'), log = [], requests = [], built = [], pending = {}, served = {};
  const defer = () => { const d = {}; d.promise = new Promise(resolve => { d.resolve = resolve; }); return d; };
  const second = { ...input, title: 'Synthetic Second Draft', sourcePath: 'synthetic/second.md', receiptAnchor: 'second', sourceContent: '# Second heading\nSecond source.' };
  fs.mkdirSync(path.join(modules, '@playwright', 'test'), { recursive: true });
  fs.writeFileSync(path.join(modules, '@playwright', 'test', 'package.json'), JSON.stringify({ name: 'fake', main: 'index.js' }));
  fs.writeFileSync(path.join(modules, '@playwright', 'test', 'index.js'), 'module.exports = global.__fakePlaywright;');
  const exportClick = () => {
    const submitted = [input, second][built.length], sourceHash = createHash('sha256').update(submitted.sourceContent.trim(), 'utf8').digest('hex');
    const html = buildHtml(submitted, '2026-10-17T00:00:00Z', sourceHash);
    const post = { method: () => 'POST', url: () => 'http://localhost:1/api/artifacts/export', postDataJSON: () => submitted };
    page.seen(post);
    const data = { html, governanceReceiptStatus: 'PRESENT', governanceReceipt: { receiptId: 'a' + built.length }, governanceReceiptAttemptId: 'a' + built.length,
      receiptAnchor: submitted.receiptAnchor, governanceState: 'DRAFT_UNACCEPTED' };
    built.push(html);
    served.html = html;
    served.wire = Buffer.from(JSON.stringify({ success: true, data, routeGovernanceProof: { authMode: 'session' } }));
    pending.response.resolve({ url: () => post.url(), request: () => post, status: () => 200,
      body: async () => served.wire });
  };
  let loginVisible = false, loginEnabled = false;
  const getByRole = (role, { name, exact }) => {
    assert.equal(role, 'button', 'legacy fake: wrong role');
    assert.equal(exact, true, 'legacy fake: non-exact control');
    const label = name.normalize('NFC');
    assert.ok(['Đăng nhập', 'Tạo HTML', 'Tải HTML'].includes(label), 'legacy fake: unknown button');
    return {
      waitFor: async ({ state }) => {
        assert.equal(label, 'Đăng nhập', 'legacy fake: wrong readiness control');
        assert.equal(state, 'visible', 'legacy fake: wrong readiness state');
        assert.equal(loginVisible, true, 'legacy fake: sign-in not visible');
      },
      isEnabled: async () => {
        assert.equal(label, 'Đăng nhập', 'legacy fake: wrong enabled control');
        return loginEnabled;
      },
      click: async () => {
        if (label === 'Đăng nhập') { assert.equal(loginEnabled, true, 'legacy fake: disabled sign-in'); return; }
        if (label === 'Tạo HTML') exportClick();
        if (label === 'Tải HTML') pending.download.resolve({ saveAs: async target => fs.writeFileSync(target, served.html), suggestedFilename: () => 'x.html' });
      },
    };
  };
  assert.throws(() => getByRole('link', { name: 'Đăng nhập', exact: true }), /wrong role/);
  assert.throws(() => getByRole('button', { name: 'Wrong sign-in', exact: true }), /unknown button/);
  await assert.rejects(getByRole('button', { name: 'Đăng nhập', exact: true }).waitFor({ state: 'hidden' }), /wrong readiness state/);
  await assert.rejects(getByRole('button', { name: 'Đăng nhập', exact: true }).waitFor({ state: 'visible' }), /not visible/);
  const page = {
    on: (event, cb) => { page.seen = cb; }, goto: async () => { loginVisible = true; loginEnabled = true; }, waitForURL: async () => {}, addInitScript: async () => {}, screenshot: async o => fs.writeFileSync(o.path, 'png'),
    locator: () => ({ fill: async () => {} }), getByLabel: () => ({ fill: async () => {}, selectOption: async () => {} }), getByTestId: () => ({ count: async () => 0 }),
    frameLocator: () => ({ locator: selector => ({ selector }) }), waitForEvent: () => (pending.download = defer()).promise,
    waitForResponse: () => (pending.response = defer()).promise,
    getByRole,
  };
  const context = { route: async () => {}, pages: () => [], newPage: async () => page, close: async () => { log.push('close'); },
    request: { get: async () => ({ json: async () => ({ user: { userId: 'usr_3', role: 'developer', authSource: 'local_mock' } }) }) } };
  global.__fakePlaywright = { chromium: { launchPersistentContext: async () => context }, expect: locator => ({
    toHaveAttribute: async () => {},
    toHaveText: async text => {
      const element = new JSDOM(served.html).window.document.querySelector(locator.selector);
      assert.ok(element, 'missing renderer DOM selector: ' + locator.selector);
      assert.equal(element.textContent.trim(), text);
      if (failHeading) throw new Error('known DOM assertion rejection');
    },
  }) };
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
    return { requests, built, log, emitted, dir, wire: served.wire, exit: process.exitCode, json: JSON.parse(fs.readFileSync(output, 'utf8')) };
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
test('original wire and decoded HTML survive a later known DOM assertion failure', async () => {
  const bad = await journey('custody-before-dom', (expected, op) => `${expected} g1 ${op}`, true);
  assert.match(bad.json.error, /known DOM assertion rejection/);
  assert.deepEqual([bad.json.partial, bad.json.builds.length, bad.exit], [true, 0, 1]);
  assert.ok(fs.readFileSync(path.join(bad.dir, 'v1-route.json')).equals(bad.wire));
  assert.ok(fs.readFileSync(path.join(bad.dir, 'v1-decoded.html')).equals(Buffer.from(JSON.parse(bad.wire).data.html, 'utf8')));
});
test('a reply with a tail, a wrong generation or a wrong operation stops the journey before the next effect', async () => {
  for (const [name, answer] of [['tail', (e, op) => `${e} g1 ${op} tail`], ['generation', (e, op) => `${e} g2 ${op}`], ['operation', (e) => `${e} g1 c9`]]) {
    const bad = await journey('journey-' + name, answer);
    assert.deepEqual([bad.requests, bad.built, bad.json.exportPosts, bad.json.partial, bad.exit, bad.log], [['EXPORT_GATE_REQUEST'], [], [], true, 1, ['close']]); // no export click
    assert.match(bad.json.error, /Expected values to be strictly equal|expected/i);
  }
});
test('S14 login readiness waits for hydrated ready form before filling', async () => {
  const vm = require('node:vm');
  const web = path.join(__dirname, '..', '..', 'EXTENSIONS', 'CVF_v1.6_AGENT_PLATFORM', 'cvf-web');
  const modules = path.join(web, 'node_modules');
  const fromWeb = name => require(path.join(modules, name));
  const componentFile = path.join(web, 'src', 'app', 'login', 'LoginPageClient.tsx');
  const componentRaw = fs.readFileSync(componentFile);
  assert.equal(createHash('sha256').update(componentRaw).digest('hex'), '190e13518094c49259b87dddc903c8713c3810f2460644b6a2d8e9d57690586d');
  const dom = new JSDOM('<div id="app"></div>', { url: 'http://localhost.invalid/login?from=%2Fartifacts' });
  const globals = { window: dom.window, document: dom.window.document, navigator: dom.window.navigator,
    HTMLElement: dom.window.HTMLElement, HTMLInputElement: dom.window.HTMLInputElement, Node: dom.window.Node,
    Event: dom.window.Event, MouseEvent: dom.window.MouseEvent, localStorage: dom.window.localStorage,
    IS_REACT_ACT_ENVIRONMENT: true };
  const originalGlobals = Object.fromEntries(Object.keys(globals).map(key => [key, Object.getOwnPropertyDescriptor(global, key)]));
  for (const [key, value] of Object.entries(globals)) Object.defineProperty(global, key, { configurable: true, writable: true, value });
  let mounted;
  try {
    const React = fromWeb('react');
    const server = fromWeb('react-dom/server');
    const client = fromWeb('react-dom/client'); // first client import follows DOM globals
    const { fireEvent } = fromWeb('@testing-library/dom');
    const typescript = fromWeb('typescript');
    let sessionStatus = 'loading', redirect = false, signInCalls = 0, controlledMatch = false;
    const syntheticUser = 'dev', syntheticPass = 'dev123';
    const mocks = { react: React, 'react/jsx-runtime': fromWeb('react/jsx-runtime'),
      'next/navigation': { useRouter: () => ({ replace: () => { redirect = true; } }), useSearchParams: () => ({ get: () => '/artifacts' }) },
      '@/lib/i18n': { useLanguage: () => ({ language: 'vi' }), LanguageToggle: () => null },
      'next-auth/react': { useSession: () => ({ status: sessionStatus }), signIn: async (provider, fields) => {
        signInCalls += 1;
        controlledMatch = provider === 'credentials' && fields.username === syntheticUser && fields.password === syntheticPass;
        return controlledMatch ? { ok: true } : { error: 'synthetic-refusal' };
      } } };
    const compiled = typescript.transpileModule(componentRaw.toString('utf8'), { compilerOptions: {
      module: typescript.ModuleKind.CommonJS, jsx: typescript.JsxEmit.ReactJSX, target: typescript.ScriptTarget.ES2022 } }).outputText;
    const exports = {};
    vm.runInThisContext('(function(require,module,exports){' + compiled + '\n})', { filename: 'LoginPageClient.s14.cjs' })(id => {
      assert.ok(Object.prototype.hasOwnProperty.call(mocks, id), 'UNEXPECTED_COMPONENT_IMPORT'); return mocks[id];
    }, { exports }, exports);
    const Component = exports.default;
    assert.equal(typeof Component, 'function', 'ACTUAL_COMPONENT_EXPORT_ABSENT');
    const host = dom.window.document.querySelector('#app');
    const element = () => React.createElement(Component, { localMockAllowed: true, selectedOAuthProvider: null });
    host.innerHTML = server.renderToString(element());
    const buttonFor = (role, name) => {
      if (role !== 'button') return null;
      const hits = [...host.querySelectorAll('button')].filter(button => button.type === 'submit'
        && button.textContent.trim().normalize('NFC') === name.normalize('NFC'));
      return hits.length === 1 ? hits[0] : null;
    };
    const signInName = 'Đăng nhập';
    const loading = [...host.querySelectorAll('button')].filter(button => button.type === 'submit');
    assert.equal(loading.length, 1, 'SSR_SUBMIT_NOT_UNIQUE');
    assert.equal(loading[0].disabled, true, 'SSR_LOADING_NOT_DISABLED');
    assert.equal(buttonFor('link', signInName), null, 'WRONG_ROLE_ACCEPTED');
    assert.equal(buttonFor('button', 'Wrong sign-in'), null, 'WRONG_NAME_ACCEPTED');
    await React.act(async () => { fireEvent.click(loading[0]); });
    assert.equal(signInCalls, 0, 'DISABLED_SUBMITTED');
    let readyStarted = false, hydrated = false, sessionProbeReached = false, exportCalls = 0, evaluateCalls = 0;
    let notifyPending, releasePending;
    const firstPending = new Promise(resolve => { notifyPending = resolve; });
    const hydrationBarrier = new Promise(resolve => { releasePending = resolve; });
    const actionability = async (role, name) => {
      assert.equal(role, 'button', 'WRONG_ROLE_ACTIONABILITY');
      assert.equal(name, signInName, 'WRONG_NAME_ACTIONABILITY');
      if (!hydrated) {
        if (!readyStarted) { readyStarted = true; notifyPending(); }
        await hydrationBarrier; // only the external test driver releases this actual pending UI wait
      }
      const button = buttonFor(role, name);
      assert.ok(button && !button.disabled, 'READY_SIGNIN_CONTROL_ABSENT');
      return button;
    };
    const fillDom = async (selector, value) => {
      const hits = host.querySelectorAll(selector);
      assert.equal(hits.length, 1, 'INPUT_NOT_UNIQUE');
      const setter = Object.getOwnPropertyDescriptor(dom.window.HTMLInputElement.prototype, 'value').set;
      await React.act(async () => { setter.call(hits[0], value); fireEvent.input(hits[0], { bubbles: true }); });
    };
    const page = { on: () => {}, goto: async () => {}, addInitScript: async () => {},
      screenshot: async o => fs.writeFileSync(o.path, 'png'),
      locator: selector => ({ fill: async value => {
        assert.ok(selector === 'input[placeholder="admin"]' || selector === 'input[placeholder="admin123"]', 'UNEXPECTED_INPUT');
        await fillDom(selector, value);
      } }),
      getByRole: (role, options) => ({
        waitFor: async ({ state }) => { assert.equal(state, 'visible', 'UNEXPECTED_WAIT');
          assert.equal(role, 'button', 'WRONG_ROLE_WAIT'); assert.equal(options.name, signInName, 'WRONG_NAME_WAIT');
          await actionability(role, options.name); },
        isEnabled: async () => { const button = buttonFor(role, options.name); return !!button && !button.disabled; },
        click: async () => { assert.equal(role, 'button', 'WRONG_ROLE_CLICK');
          assert.equal(options.name, signInName, 'WRONG_NAME_CLICK');
          const button = await actionability(role, options.name); await React.act(async () => { fireEvent.click(button); }); },
      }),
      waitForURL: async () => { if (!redirect) throw new Error('CONTROLLED_FIELDS_ABSENT'); },
    };
    const context = { route: async () => {}, pages: () => [], newPage: async () => page, close: async () => {},
      request: { get: async () => { sessionProbeReached = true; throw new Error('SOURCE_CASE_STOP_AFTER_SESSION'); } } };
    const dir = path.join(SCRATCH, 's14-real-component'), modulesFake = path.join(SCRATCH, 's14-modules');
    fs.mkdirSync(path.join(modulesFake, '@playwright', 'test'), { recursive: true });
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(modulesFake, '@playwright', 'test', 'package.json'), JSON.stringify({ name: 'fake', main: 'index.js' }));
    fs.writeFileSync(path.join(modulesFake, '@playwright', 'test', 'index.js'), 'module.exports = global.__s14FakePlaywright;');
    global.__s14FakePlaywright = { chromium: { launchPersistentContext: async () => context }, expect: () => ({}) };
    const config = path.join(dir, 'config.json'), output = path.join(dir, 'browser.json');
    fs.writeFileSync(config, JSON.stringify({ inputs: [input], cap: 1, browserProfile: path.join(dir, 'profile'), ...limits() }));
    const originalDestroy = process.stdin.destroy;
    process.stdin.destroy = () => {};
    try {
      const running = run({ modules: modulesFake, baseURL: 'http://localhost.invalid', output, custody: dir,
        control: async () => {}, config, now: () => T, uptime: () => 0, emit: () => {} });
      const pending = await Promise.race([firstPending.then(() => true), running.then(() => false)]);
      assert.equal(pending, true, 'NO_PENDING_ACTIONABILITY_BEFORE_RUN_END');
      // The driver observes a real pending named-control wait, then releases hydration/status.
      await React.act(async () => { mounted = client.hydrateRoot(host, element()); });
      const stillLoading = [...host.querySelectorAll('button')].filter(button => button.type === 'submit');
      assert.equal(stillLoading.length, 1, 'HYDRATED_SUBMIT_NOT_UNIQUE');
      assert.equal(stillLoading[0].disabled, true, 'HYDRATED_LOADING_NOT_DISABLED');
      sessionStatus = 'unauthenticated';
      await React.act(async () => { mounted.render(element()); });
      hydrated = true;
      releasePending();
      await running;
    }
    finally { process.stdin.destroy = originalDestroy; process.exitCode = undefined; delete global.__s14FakePlaywright; }
    assert.equal(readyStarted, true, 'NO_ACTUAL_ACTIONABILITY_WAIT');
    assert.equal(hydrated, true, 'NO_ACTUAL_HYDRATION');
    assert.equal(signInCalls, 1, 'SUBMIT_COUNT_NOT_ONE');
    assert.equal(controlledMatch, true, 'CONTROLLED_FIELDS_ABSENT');
    assert.equal(redirect, true, 'NO_SYNTHETIC_REDIRECT');
    assert.equal(sessionProbeReached, true, 'NO_SESSION_PROBE');
    assert.equal(exportCalls + evaluateCalls, 0, 'EFFECT_AFTER_SESSION');
  } finally {
    if (mounted) { const React = fromWeb('react'); await React.act(async () => { mounted.unmount(); }); }
    for (const [key, descriptor] of Object.entries(originalGlobals)) {
      if (descriptor) Object.defineProperty(global, key, descriptor); else delete global[key];
    }
    dom.window.close();
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
function guarded(main, realHttp = false) {
  const { EventEmitter } = require('node:events'), vm = require('node:vm');
  const http = realHttp ? require('node:http') : null, originalHttpEmit = http && http.Server.prototype.emit;
  const filename = path.join(__dirname, 'journey.cjs'), entry = path.join(__dirname, '..', 'probe_cvf_w05_browser_chain.cjs');
  const logs = [], loads = [], sentinel = {}, cached = {}, cache = { [entry]: cached, unrelated: sentinel };
  class Server extends EventEmitter {}
  class Socket { connect() {} }
  const fake = id => {
    if (id === entry) { loads.push(id); return {}; }
    if (id === 'node:fs') return { appendFileSync: (file, line) => logs.push(JSON.parse(line)) };
    if (id === 'node:net') return { Socket };
    if (id === 'node:dns') return { promises: {} };
    if (id === 'node:http') return http || { Server };
    return require(id);
  };
  fake.resolve = id => { assert.equal(id, entry); return entry; };
  fake.cache = cache;
  vm.runInNewContext(fs.readFileSync(filename, 'utf8'), {
    require: fake, __dirname, module: { exports: {} }, Buffer,
    process: { env: { CVF_NCR_ALLOWED_PORTS: '[]', CVF_HCR_EGRESS_LOG: 'ignored-vm-log' },
      argv: ['node', main === 'entry' ? entry : main], pid: 7 },
  }, { filename });
  return { logs, loads, cache, cached, sentinel, entry, Server, EventEmitter, http, originalHttpEmit };
}
test('guard import evicts only its exact future main and leaves library or different main cached', () => {
  for (const main of ['entry', undefined, path.join(__dirname, 'different-main.cjs')]) {
    const g = guarded(main);
    assert.deepEqual(g.loads, [g.entry]);
    assert.equal(g.cache.unrelated, g.sentinel);
    assert.equal(g.cache[g.entry], main === 'entry' ? undefined : g.cached);
    assert.deepEqual(Object.keys(g.cache).sort(), main === 'entry' ? ['unrelated'] : [g.entry, 'unrelated'].sort());
    assert.deepEqual(g.logs, []);
  }
});
test('evaluate observer ignores empty GET and records no valid recipient for empty or malformed POST', () => {
  const g = guarded(undefined), server = new g.Server();
  let delegated = 0;
  server.on('request', () => { delegated += 1; });
  const send = (method, raw) => {
    const req = new g.EventEmitter();
    Object.assign(req, { method, url: '/api/governance/evaluate?readiness=1', headers: {} });
    server.emit('request', req, {});
    if (method === 'GET') assert.equal(req.listenerCount('end'), 0);
    req.emit('data', Buffer.from(raw));
    assert.doesNotThrow(() => req.emit('end'));
  };
  send('GET', '');
  assert.deepEqual(g.logs, []);
  for (const raw of ['', '{broken']) {
    send('POST', raw);
    const record = g.logs.at(-1);
    assert.deepEqual(record, { pid: 7, event: 'evaluate-recipient-invalid', bodyBytes: Buffer.byteLength(raw),
      bodySha256: createHash('sha256').update(raw).digest('hex') });
  }
  assert.equal(delegated, 3);
  assert.equal(g.logs.filter(e => e.event === 'evaluate-recipient').length, 0);
});
test('valid evaluate POST preserves exact body hash and header presence while delegating once', () => {
  const g = guarded(undefined), server = new g.Server(), req = new g.EventEmitter();
  const raw = '{"request_id":"synthetic-only","value":1}';
  let delegated = 0;
  server.on('request', () => { delegated += 1; });
  Object.assign(req, { method: 'POST', url: '/api/governance/evaluate', headers: { 'x-cvf-service-token': 'synthetic', cookie: 'synthetic' } });
  server.emit('request', req, {});
  req.emit('data', Buffer.from(raw.slice(0, 5)));
  req.emit('data', Buffer.from(raw.slice(5)));
  assert.doesNotThrow(() => req.emit('end'));
  assert.deepEqual(g.logs, [{ pid: 7, event: 'evaluate-recipient', body: JSON.parse(raw),
    bodySha256: createHash('sha256').update(raw).digest('hex'), serviceTokenPresent: true, cookiePresent: true }]);
  assert.equal(delegated, 1);
});
test('native delayed Request consumes the evaluate body while the observer records it', { timeout: 3000 }, async () => {
  const g = guarded(undefined, true), { http } = g, raw = '{"request_id":"loopback-only","value":1}';
  const server = http.createServer((req, res) => setTimeout(async () => {
    try { res.end(JSON.stringify({ body: await new Request('http://127.0.0.1/api/governance/evaluate', { method: 'POST', body: req, duplex: 'half' }).text() })); }
    catch (error) { res.statusCode = 500; res.end(JSON.stringify({ error: error.message })); }
  }, 25));
  try {
    await new Promise((resolve, reject) => { server.once('error', reject); server.listen(0, '127.0.0.1', resolve); });
    const response = await new Promise((resolve, reject) => {
      const request = http.request({ host: '127.0.0.1', port: server.address().port, path: '/api/governance/evaluate', method: 'POST',
        headers: { 'content-length': Buffer.byteLength(raw), 'x-cvf-service-token': 'synthetic', cookie: 'synthetic', connection: 'close' } }, res => {
        let text = ''; res.setEncoding('utf8'); res.on('data', part => { text += part; }); res.on('end', () => resolve({ status: res.statusCode, body: JSON.parse(text) }));
      });
      request.setTimeout(1200, () => request.destroy(new Error('loopback client timeout'))); request.on('error', reject); request.end(raw);
    });
    assert.equal(response.status, 200, response.body.error || JSON.stringify(response.body));
    assert.equal(response.body.body, raw);
    assert.deepEqual(g.logs, [{ pid: 7, event: 'evaluate-recipient', body: JSON.parse(raw),
      bodySha256: createHash('sha256').update(raw).digest('hex'), serviceTokenPresent: true, cookiePresent: true }]);
  } finally {
    http.Server.prototype.emit = g.originalHttpEmit;
    if (server.listening) await new Promise(resolve => server.close(resolve));
  }
});
