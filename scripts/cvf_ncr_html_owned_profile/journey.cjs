/* Fresh developer journey and opt-in Node network observation. No policy verdict simulation. */
// Text Encoding Exception: Vietnamese labels are exact current UI locators.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { createHash } = require('node:crypto');
const sha = b => createHash('sha256').update(b).digest('hex');

function installOwnedGuard() {
  require(path.join(__dirname, '..', 'probe_cvf_w05_browser_chain.cjs'));
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
    if (event === 'request' && args[0].url.split('?')[0] === '/api/governance/evaluate') {
      const req = args[0], parts = [];
      req.on('data', b => parts.push(b));
      req.on('end', () => {
        const raw = Buffer.concat(parts);
        log({ event: 'evaluate-recipient', body: JSON.parse(raw.toString('utf8')),
          bodySha256: sha(raw), serviceTokenPresent: Boolean(req.headers['x-cvf-service-token']), cookiePresent: Boolean(req.headers.cookie) });
      });
    }
    return emit.call(this, event, ...args);
  };
}
if (process.env.CVF_NCR_ALLOWED_PORTS && process.env.CVF_HCR_EGRESS_LOG) installOwnedGuard();

function validateInputs(inputs, cap) {
  const keys = ['title', 'sourcePath', 'sourceContent', 'memoryClass', 'status', 'claimBoundary', 'receiptAnchor'];
  assert.ok(Number.isInteger(cap) && cap >= 1 && cap <= 2 && inputs.length === cap);
  for (const input of inputs) {
    assert.deepEqual(Object.keys(input).sort(), keys.slice().sort());
    assert.equal(input.memoryClass, 'FULL_RECORD');
    assert.ok(keys.every(k => typeof input[k] === 'string' && input[k] && input[k].normalize('NFC') === input[k]));
    assert.ok(input.sourcePath.startsWith('synthetic/') && /^[a-zA-Z0-9 -]+$/.test(input.title));
  }
  assert.equal(new Set(inputs.map(x => x.receiptAnchor)).size, cap);
}

async function run({ modules, baseURL, output, custody, control, config }) {
  const cfg = JSON.parse(fs.readFileSync(config, 'utf8'));
  validateInputs(cfg.inputs, cfg.cap);
  const { chromium, expect } = require(path.join(modules, '@playwright/test'));
  const result = { mode: 'owned-profile', partial: true, builds: [], checkpoints: [], exportPosts: [], aiPosts: [], external: [] };
  let context;
  const save = () => fs.writeFileSync(output, JSON.stringify(result, null, 2));
  try {
    context = await chromium.launchPersistentContext(cfg.browserProfile, { headless: true, acceptDownloads: true,
      baseURL, args: ['--disable-background-networking', '--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE 127.0.0.1 , EXCLUDE localhost'] });
    await context.route('**/*', route => {
      const url = new URL(route.request().url());
      if (url.origin === baseURL || ['about:', 'data:', 'blob:'].includes(url.protocol)) return route.continue();
      result.external.push({ host: url.hostname, method: route.request().method() });
      return route.abort('blockedbyclient');
    });
    const page = context.pages()[0] || await context.newPage();
    page.setDefaultTimeout(30000);
    await page.addInitScript(() => {
      localStorage.setItem('cvf_language', 'vi');
      localStorage.setItem('cvf_onboarding_complete', 'true');
      localStorage.setItem('cvf_onboarding_seen', '1');
      localStorage.setItem('cvf_setup_banner_dismissed', 'true');
    });
    page.on('request', r => {
      const url = new URL(r.url());
      if (r.method() === 'POST' && url.pathname === '/api/artifacts/export') result.exportPosts.push(r.postDataJSON());
      if (r.method() === 'POST' && /^\/api\/(ai|execute|generate)(\/|$)/.test(url.pathname)) result.aiPosts.push(url.pathname);
    });
    await page.goto('/login?from=%2Fartifacts', { waitUntil: 'networkidle', timeout: 120000 });
    await page.locator('input[placeholder="admin"]').fill('dev');
    await page.locator('input[placeholder="admin123"]').fill('dev123');
    await page.getByRole('button', { name: 'Đăng nhập', exact: true }).click();
    await page.waitForURL('**/artifacts', { timeout: 120000 });
    const session = await (await context.request.get('/api/auth/session')).json();
    assert.deepEqual([session.user.userId, session.user.role, session.user.authSource], ['usr_3', 'developer', 'local_mock']);
    result.session = { userId: session.user.userId, role: session.user.role, authSource: session.user.authSource };
    const fields = { title: 'Tiêu đề', sourcePath: 'Nguồn tham chiếu', memoryClass: 'Loại bản ghi', status: 'Trạng thái rà soát',
      receiptAnchor: 'Mã receipt', claimBoundary: 'Ranh giới rà soát', sourceContent: 'Ghi chú nguồn' };
    const fill = async input => {
      for (const [key, label] of Object.entries(fields)) {
        const locator = page.getByLabel(label, { exact: true });
        if (key === 'memoryClass') await locator.selectOption(input[key]);
        else await locator.fill(input[key]);
      }
    };
    const preview = page.frameLocator('iframe[title="Xem trước"]');
    const download = async (label, expected) => {
      const waiting = page.waitForEvent('download');
      await page.getByRole('button', { name: 'Tải HTML', exact: true }).click();
      const d = await waiting, target = path.join(custody, label + '-download.html');
      await d.saveAs(target);
      const raw = fs.readFileSync(target);
      assert.ok(raw.equals(expected));
      return { filename: d.suggestedFilename(), bytes: raw.length, sha256: sha(raw) };
    };
    for (const [index, input] of cfg.inputs.entries()) {
      await fill(input);
      if (index) {
        await expect(page.getByTestId('artifact-version-notice')).toHaveAttribute('data-version-state', 'stale');
        await expect(preview.locator('header > h1')).toHaveText(cfg.inputs[index - 1].title);
        const prior = result.builds[index - 1];
        assert.equal(await page.getByTestId('governance-receipt-attempt-id').count(), 0); // PRESENT uses receipt, not absent-attempt label
        result.stale = { priorAttemptId: prior.attemptId, download: await download('stale', Buffer.from(prior.html, 'utf8')), exportPosts: result.exportPosts.length };
        await control('CHECKPOINT stale', 'CHECKPOINT_OK stale');
      }
      assert.equal(result.exportPosts.length, index);
      await control('EXPORT_GATE_REQUEST ' + JSON.stringify({ n: index + 1, external: result.external, aiPosts: result.aiPosts }), 'EXPORT_GATE_OK ' + (index + 1));
      const waiting = page.waitForResponse(r => new URL(r.url()).pathname === '/api/artifacts/export' && r.request().method() === 'POST', { timeout: 120000 });
      const started = Date.now();
      await page.getByRole('button', { name: 'Tạo HTML', exact: true }).click();
      const response = await waiting, wire = await response.body(), packet = JSON.parse(wire.toString('utf8'));
      assert.equal(response.status(), 200);
      assert.equal(packet.success, true);
      assert.deepEqual(response.request().postDataJSON(), input);
      assert.deepEqual(result.exportPosts[index], input);
      const d = packet.data, html = Buffer.from(d.html, 'utf8'), sourceHash = sha(Buffer.from(input.sourceContent.trim(), 'utf8'));
      assert.equal(d.governanceReceiptStatus, 'PRESENT');
      assert.equal(d.governanceReceipt.receiptId, d.governanceReceiptAttemptId);
      assert.equal(d.receiptAnchor, input.receiptAnchor);
      assert.equal(d.governanceState, 'DRAFT_UNACCEPTED');
      assert.equal(packet.routeGovernanceProof.authMode, 'session');
      assert.ok(html.toString('utf8').includes(sourceHash));
      await expect(page.getByTestId('artifact-version-notice')).toHaveAttribute('data-version-state', 'current');
      await expect(preview.locator('header > h1')).toHaveText(input.title);
      const bodyHeading = /^# (.+)$/m.exec(input.sourceContent);
      if (bodyHeading) await expect(preview.locator('main > h1')).toHaveText(bodyHeading[1]);
      fs.writeFileSync(path.join(custody, `v${index + 1}-route.json`), wire);
      fs.writeFileSync(path.join(custody, `v${index + 1}-decoded.html`), html);
      result.builds.push({ attemptId: d.governanceReceiptAttemptId, receiptAnchor: d.receiptAnchor, receipt: d.governanceReceipt,
        sourceHash, wireSha256: sha(wire), htmlSha256: sha(html), html, elapsedMs: Date.now() - started,
        download: await download(`v${index + 1}`, html), submitted: input });
      result.builds[index].html = html.toString('utf8');
      await page.screenshot({ path: path.join(custody, `v${index + 1}.png`), fullPage: true });
      await control(`CHECKPOINT built${index + 1}`, `CHECKPOINT_OK built${index + 1}`);
    }
    assert.equal(result.exportPosts.length, cfg.cap);
    assert.deepEqual(result.aiPosts, []);
    result.partial = false;
  } catch (e) {
    result.error = String(e.message).slice(0, 1200);
    process.exitCode = 1;
  } finally {
    if (context) await context.close();
    save();
    process.stdin.destroy();
  }
}
module.exports = { run, validateInputs, sha };
