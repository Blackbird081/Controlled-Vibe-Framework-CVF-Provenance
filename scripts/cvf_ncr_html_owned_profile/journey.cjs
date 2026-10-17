/* Fresh developer journey and opt-in Node network observation. No policy verdict simulation. */
// Text Encoding Exception: Vietnamese labels are exact current UI locators.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { createHash } = require('node:crypto');
const sha = b => createHash('sha256').update(b).digest('hex');

function installOwnedGuard() {
  const entry = require.resolve(path.join(__dirname, '..', 'probe_cvf_w05_browser_chain.cjs'));
  require(entry);
  // Its preload import installed the guard; only the future main must execute again as main.
  if (process.argv[1] === entry) delete require.cache[entry];
  const net = require('node:net'), dns = require('node:dns'), http = require('node:http');
  const ports = new Set(JSON.parse(process.env.CVF_NCR_ALLOWED_PORTS));
  const local = h => ['127.0.0.1', 'localhost', '::1'].includes(String(h).replace(/^\[|\]$/g, ''));
  const log = e => fs.appendFileSync(process.env.CVF_HCR_EGRESS_LOG, JSON.stringify({ pid: process.pid, ...e }) + '\n');
  const deny = (host, via) => log({ event: 'denied', host: String(host), via });
  const connect = net.Socket.prototype.connect;
  net.Socket.prototype.connect = function (...args) {
    let a = Array.isArray(args[0]) ? args[0][0] : args[0];
    if (typeof a !== 'object') a = /^\d+$/.test(String(a)) ? { port: Number(a), host: typeof args[1] === 'string' ? args[1] : 'localhost' } : { path: a };
    if (!a.path && local(a.host || 'localhost') && !ports.has(Number(a.port))) {
      deny(a.host || 'localhost', 'unadmitted-loopback-port');
      process.nextTick(() => this.destroy(new Error('unadmitted loopback port')));
      return this;
    }
    return connect.apply(this, args);
  };
  for (const name of Object.keys(dns).filter(n => /^resolve/.test(n) || n === 'reverse')) {
    if (typeof dns[name] !== 'function') continue;
    const old = dns[name];
    dns[name] = function (host, ...args) {
      if (!local(host)) {
        deny(host, 'dns-' + name);
        return process.nextTick(args[args.length - 1], new Error('egress denied'));
      }
      return old.call(this, host, ...args);
    };
    if (typeof dns.promises[name] === 'function') {
      const original = dns.promises[name];
      dns.promises[name] = async function (host, ...args) {
        if (!local(host)) { deny(host, 'dns-promises-' + name); throw new Error('egress denied'); }
        return original.call(this, host, ...args);
      };
    }
  }
  const emit = http.Server.prototype.emit;
  http.Server.prototype.emit = function (event, ...args) {
    if (event === 'request' && args[0].method === 'POST' && args[0].url.split('?')[0] === '/api/governance/evaluate') {
      const req = args[0], parts = [], requestEmit = req.emit;
      let ended = false;
      req.emit = function (name, ...events) {
        let result;
        try { result = requestEmit.call(this, name, ...events); }
        catch (error) { if (name === 'end') this.emit = requestEmit; throw error; }
        try {
          if (name === 'data' && !ended) parts.push(Buffer.from(events[0]));
          else if (name === 'end' && !ended) {
            ended = true;
            const raw = Buffer.concat(parts);
            let body, invalid = false;
            try { body = JSON.parse(raw.toString('utf8')); } catch (_) { invalid = true; }
            if (invalid) log({ event: 'evaluate-recipient-invalid', bodyBytes: raw.length, bodySha256: sha(raw) });
            else log({ event: 'evaluate-recipient', body,
              bodySha256: sha(raw), serviceTokenPresent: Boolean(req.headers['x-cvf-service-token']), cookiePresent: Boolean(req.headers.cookie) });
          }
        } catch (_) { /* Observation cannot change native request delivery. */ }
        if (name === 'end') this.emit = requestEmit;
        return result;
      };
    }
    return emit.call(this, event, ...args);
  };
}
if (process.env.CVF_NCR_ALLOWED_PORTS && process.env.CVF_HCR_EGRESS_LOG) installOwnedGuard();

const KEYS = ['title', 'sourcePath', 'sourceContent', 'memoryClass', 'status', 'claimBoundary', 'receiptAnchor'];
const plain = x => x !== null && typeof x === 'object' && !Array.isArray(x) && Object.getPrototypeOf(x) === Object.prototype;

// Exact-shape admission; profile.validate_inputs enforces the same contract in Python before any namespace or child exists.
function validateInputs(inputs, cap) {
  assert.ok(Number.isInteger(cap) && cap >= 1 && cap <= 2 && Array.isArray(inputs) && inputs.length === cap);
  for (const input of inputs) {
    assert.ok(plain(input));
    assert.deepEqual(Object.keys(input).sort(), KEYS.slice().sort());
    assert.equal(input.memoryClass, 'FULL_RECORD');
    assert.ok(KEYS.every(k => typeof input[k] === 'string' && input[k] && input[k].normalize('NFC') === input[k]));
    assert.ok(/^synthetic\/[A-Za-z0-9._-]+(\/[A-Za-z0-9._-]+)*$/.test(input.sourcePath) && !input.sourcePath.split('/').some(x => x === '.' || x === '..'));
    assert.ok(/^[a-zA-Z0-9 -]+$/.test(input.title));
  }
  assert.equal(new Set(inputs.map(x => x.receiptAnchor)).size, cap);
}

// The parent's limits are advisory here: this clock can only SHORTEN what a wait may take. The absolute epoch cutoff already spends the
// child's startup delay; the relative budget minus monotonic process uptime survives a wall-clock rollback; the smaller of both governs.
// One sample per allowance; a sub-unit remainder is refused (never turned into timeout 0, which Playwright treats as unlimited).
function authority(limits, now = Date.now, uptime = () => process.uptime() * 1000) {
  const finite = n => typeof n === 'number' && Number.isFinite(n);
  assert.ok(plain(limits) && finite(limits.deadlineAtMs) && finite(limits.cleanupAtMs) && /^g[0-9a-f]{1,16}$/.test(limits.generation));
  assert.ok(finite(limits.workMs) && limits.workMs >= 1 && limits.workMs <= 900000 && finite(limits.cleanupMs) && limits.cleanupMs >= 1 && limits.cleanupMs <= 120000);
  const left = (absolute, relative) => Math.min(absolute - now(), relative - uptime());
  const take = (ms, remaining) => {
    const wait = Math.floor(Math.min(ms, remaining));
    if (!(wait >= 1)) throw new Error('allowance exhausted before the call; nothing started');
    return wait;
  };
  const work = ms => take(ms, left(limits.deadlineAtMs, limits.workMs));
  const cleanup = ms => take(ms, left(limits.cleanupAtMs, limits.workMs + limits.cleanupMs));
  return { work, cleanup };
}

// A wait bound, not cancellation. The operation is a thunk invoked only after its allowance exists, so an exhausted deadline starts nothing;
// a lost race leaves the underlying call in flight, so its outcome is UNKNOWN and the parent kills this process.
function withBudget(thunk, ms, label) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error(`${label}: no completion within ${ms}ms; outcome UNKNOWN`)), ms);
    Promise.resolve().then(thunk).then(v => { clearTimeout(timer); resolve(v); }, e => { clearTimeout(timer); reject(e); });
  });
}

// Independent teardown: each step has its own fresh cleanup allowance and recorded outcome; an exhausted remainder is NOT_ATTEMPTED.
async function teardown(steps, cleanup, ms) {
  const report = {};
  for (const [name, thunk] of steps) {
    let wait;
    try { wait = cleanup(ms); } catch (e) { report[name] = 'NOT_ATTEMPTED: cleanup remainder exhausted'; continue; }
    try {
      await withBudget(thunk, wait, name);
      report[name] = 'OK';
    } catch (e) {
      report[name] = 'FAILED: ' + String((e && e.message) || e).slice(0, 160);
    }
  }
  return report;
}

// The legacy control channel checks only a reply PREFIX. The whole line must be this request's kind, argument, run generation and operation.
function validateReply(line, expected, generation, op) {
  assert.equal(line, `${expected} ${generation} ${op}`);
  return line;
}

// Lazy, allowance-first call wrappers: the allowance is computed BEFORE the operation exists, so an exhausted deadline invokes nothing.
const actor = work => (label, ms, fn) => { const wait = work(ms); return withBudget(() => fn({ timeout: wait }), wait, label); };
const controller = (control, work, generation) => {
  let seq = 0;
  return async (build, expected) => {
    const op = 'c' + (++seq), wait = work(90000);
    return validateReply(await withBudget(() => control(build(op), expected), wait, 'control'), expected, generation, op);
  };
};

async function run({ modules, baseURL, output, custody, control, config, now, uptime, emit = s => process.stdout.write(s) }) {
  const cfg = JSON.parse(fs.readFileSync(config, 'utf8'));
  validateInputs(cfg.inputs, cfg.cap);
  const { work, cleanup } = authority(cfg, now, uptime);
  const act = actor(work), ctl = controller(control, work, cfg.generation);
  const { chromium, expect } = require(path.join(modules, '@playwright/test'));
  const result = { mode: 'owned-profile', partial: true, builds: [], checkpoints: [], exportPosts: [], aiPosts: [], external: [] };
  let context;
  try {
    context = await act('launch', 60000, o => chromium.launchPersistentContext(cfg.browserProfile, { headless: true, acceptDownloads: true, ...o,
      baseURL, args: ['--disable-background-networking', '--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE 127.0.0.1 , EXCLUDE localhost'] }));
    await act('route', 30000, () => context.route('**/*', route => {
      const url = new URL(route.request().url());
      if (url.origin === baseURL || ['about:', 'data:', 'blob:'].includes(url.protocol)) return route.continue();
      result.external.push({ host: url.hostname, method: route.request().method() });
      return route.abort('blockedbyclient');
    }));
    const page = await act('page', 30000, () => context.pages()[0] || context.newPage());
    await act('init-script', 30000, () => page.addInitScript(() => {
      localStorage.setItem('cvf_language', 'vi');
      localStorage.setItem('cvf_onboarding_complete', 'true');
      localStorage.setItem('cvf_onboarding_seen', '1');
      localStorage.setItem('cvf_setup_banner_dismissed', 'true');
    }));
    page.on('request', r => {
      const url = new URL(r.url());
      if (r.method() === 'POST' && url.pathname === '/api/artifacts/export') result.exportPosts.push(r.postDataJSON());
      if (r.method() === 'POST' && /^\/api\/(ai|execute|generate)(\/|$)/.test(url.pathname)) result.aiPosts.push(url.pathname);
    });
    await act('login-page', 120000, o => page.goto('/login?from=%2Fartifacts', { waitUntil: 'networkidle', ...o }));
    await act('fill-user', 30000, o => page.locator('input[placeholder="admin"]').fill('dev', o));
    await act('fill-password', 30000, o => page.locator('input[placeholder="admin123"]').fill('dev123', o));
    await act('login', 30000, o => page.getByRole('button', { name: 'Đăng nhập', exact: true }).click(o));
    await act('login-url', 120000, o => page.waitForURL('**/artifacts', o));
    const sessionReply = await act('session', 30000, o => context.request.get('/api/auth/session', o));
    const session = await act('session-json', 30000, () => sessionReply.json());
    assert.deepEqual([session.user.userId, session.user.role, session.user.authSource], ['usr_3', 'developer', 'local_mock']);
    result.session = { userId: session.user.userId, role: session.user.role, authSource: session.user.authSource };
    const fields = { title: 'Tiêu đề', sourcePath: 'Nguồn tham chiếu', memoryClass: 'Loại bản ghi', status: 'Trạng thái rà soát',
      receiptAnchor: 'Mã receipt', claimBoundary: 'Ranh giới rà soát', sourceContent: 'Ghi chú nguồn' };
    const fill = async input => {
      for (const [key, label] of Object.entries(fields)) {
        const locator = page.getByLabel(label, { exact: true });
        await act('fill-' + key, 30000, o => key === 'memoryClass' ? locator.selectOption(input[key], o) : locator.fill(input[key], o));
      }
    };
    const preview = page.frameLocator('iframe[title="Xem trước"]');
    const attr = (state, label) => act(label, 15000, o => expect(page.getByTestId('artifact-version-notice')).toHaveAttribute('data-version-state', state, o));
    const heading = (selector, text, label) => act(label, 15000, o => expect(preview.locator(selector)).toHaveText(text, o));
    const download = async (label, expected) => {
      const wait = work(60000), waiting = withBudget(() => page.waitForEvent('download', { timeout: wait }), wait, 'download-wait');
      waiting.catch(() => {});  // the click below is its trigger; a failure still surfaces at the await
      await act('download-click', 30000, o => page.getByRole('button', { name: 'Tải HTML', exact: true }).click(o));
      const d = await waiting, target = path.join(custody, label + '-download.html');
      await act('download-save', 30000, () => d.saveAs(target));
      const raw = fs.readFileSync(target);
      assert.ok(raw.equals(expected));
      return { filename: d.suggestedFilename(), bytes: raw.length, sha256: sha(raw) };
    };
    for (const [index, input] of cfg.inputs.entries()) {
      await fill(input);
      if (index) {
        await attr('stale', 'stale-state');
        await heading('header > h1', cfg.inputs[index - 1].title, 'stale-heading');
        const prior = result.builds[index - 1];
        assert.equal(await act('attempt-count', 15000, () => page.getByTestId('governance-receipt-attempt-id').count()), 0);  // PRESENT uses receipt
        result.stale = { priorAttemptId: prior.attemptId, download: await download('stale', Buffer.from(prior.html, 'utf8')), exportPosts: result.exportPosts.length };
        await ctl(op => `CHECKPOINT stale ${cfg.generation} ${op}`, 'CHECKPOINT_OK stale');
      }
      assert.equal(result.exportPosts.length, index);
      await ctl(op => 'EXPORT_GATE_REQUEST ' + JSON.stringify({ n: index + 1, external: result.external, aiPosts: result.aiPosts, op, generation: cfg.generation }), 'EXPORT_GATE_OK ' + (index + 1));
      const wait = work(120000), waiting = withBudget(() => page.waitForResponse(r => new URL(r.url()).pathname === '/api/artifacts/export' && r.request().method() === 'POST', { timeout: wait }), wait, 'export-response');
      waiting.catch(() => {});
      const started = Date.now();
      await act('export-click', 30000, o => page.getByRole('button', { name: 'Tạo HTML', exact: true }).click(o));
      const response = await waiting, wire = await act('response-body', 30000, () => response.body());
      fs.writeFileSync(path.join(custody, `v${index + 1}-route.json`), wire);
      const packet = JSON.parse(wire.toString('utf8')), d = packet.data;
      const html = typeof d?.html === 'string' ? Buffer.from(d.html, 'utf8') : null;
      if (html) fs.writeFileSync(path.join(custody, `v${index + 1}-decoded.html`), html);
      assert.equal(response.status(), 200);
      assert.equal(packet.success, true);
      assert.deepEqual(response.request().postDataJSON(), input);
      assert.deepEqual(result.exportPosts[index], input);
      const sourceHash = sha(Buffer.from(input.sourceContent.trim(), 'utf8'));
      assert.equal(d.governanceReceiptStatus, 'PRESENT');
      assert.equal(d.governanceReceipt.receiptId, d.governanceReceiptAttemptId);
      assert.equal(d.receiptAnchor, input.receiptAnchor);
      assert.equal(d.governanceState, 'DRAFT_UNACCEPTED');
      assert.equal(packet.routeGovernanceProof.authMode, 'session');
      assert.ok(html.toString('utf8').includes(sourceHash));
      await attr('current', 'current-state');
      await heading('header > h1', input.title, 'current-heading');
      const bodyHeading = /^# (.+)$/m.exec(input.sourceContent);
      if (bodyHeading) await heading('main > section > h1', bodyHeading[1], 'body-heading');
      result.builds.push({ attemptId: d.governanceReceiptAttemptId, receiptAnchor: d.receiptAnchor, receipt: d.governanceReceipt,
        sourceHash, wireSha256: sha(wire), htmlSha256: sha(html), html, elapsedMs: Date.now() - started,
        download: await download(`v${index + 1}`, html), submitted: input });
      result.builds[index].html = html.toString('utf8');
      await act('screenshot', 30000, o => page.screenshot({ path: path.join(custody, `v${index + 1}.png`), fullPage: true, ...o }));
      await ctl(op => `CHECKPOINT built${index + 1} ${cfg.generation} ${op}`, `CHECKPOINT_OK built${index + 1}`);
    }
    assert.equal(result.exportPosts.length, cfg.cap);
    assert.deepEqual(result.aiPosts, []);
    result.partial = false;
  } catch (e) {
    result.error = String(e.message).slice(0, 1200);
    process.exitCode = 1;
  } finally {
    // Teardown steps are independent attempts that finish BEFORE the single immutable snapshot, so the saved bytes carry the context-close and
    // stdin outcomes. The snapshot never certifies its own save: the parent reads the file back, recomputes its hash and observes the exit.
    const report = {}, step = async (name, thunk) => Object.assign(report, await teardown([[name, thunk]], cleanup, 15000));
    if (context) await step('contextClose', () => context.close());
    else report.contextClose = 'NOT_LAUNCHED';
    await step('stdinDestroy', async () => process.stdin.destroy());
    result.teardown = report;
    const bytes = Buffer.from(JSON.stringify(result, null, 2), 'utf8');
    const saved = await teardown([['save', async () => fs.writeFileSync(output, bytes)]], cleanup, 15000);
    if (saved.save === 'OK') emit(`SNAPSHOT ${sha(bytes)} ${bytes.length}\n`);  // diagnostic claim only, compared by the parent
    if (saved.save !== 'OK' || Object.values(report).some(v => v !== 'OK')) process.exitCode = 1;
  }
}
module.exports = { run, validateInputs, authority, withBudget, teardown, validateReply, actor, controller, sha };
