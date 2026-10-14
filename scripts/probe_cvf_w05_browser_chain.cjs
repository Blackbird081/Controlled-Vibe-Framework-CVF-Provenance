/* Disposable W05 browser transport/presentation proof; no provider invocation. */
'use strict';
const assert = require('node:assert/strict');
const { createHash } = require('node:crypto');
const { readFile, writeFile } = require('node:fs/promises');
const path = require('node:path');

const sha = buffer => createHash('sha256').update(buffer).digest('hex');
const LOCAL_HOSTS = new Set(['127.0.0.1', 'localhost']);
const EXPORT_PATH = '/api/artifacts/export';

function waitOwnedEngineStopped() {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('OWNED_ENGINE_STOPPED not received')), 60000);
    require('node:readline').createInterface({ input: process.stdin }).on('line', line => {
      if (line.trim() === 'OWNED_ENGINE_STOPPED') { clearTimeout(timer); resolve(); }
    });
  });
}

// Opt-in mode: composed mechanical observations of the selected HTML chain; no policy verdict assertions.
async function composition(modules, baseURL, output, custody) {
  const { chromium, expect } = require(path.join(modules, '@playwright/test'));
  const steps = [];
  const mark = (step, extra = {}) => steps.push({ step, atMs: Date.now(), ...extra });
  const result = { mode: 'configured-receipt-browser-composition', partial: true, steps };
  const browser = await chromium.launch({ headless: true, args: ['--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE 127.0.0.1 , EXCLUDE localhost'] });
  try {
    const context = await browser.newContext({ baseURL, acceptDownloads: true });
    const externalRequests = [];
    const category = host => (/(^|\.)(googleapis|gstatic)\.com$/i.test(host) ? 'passive-font-asset' : 'other-external');
    await context.route('**/*', route => {
      const url = new URL(route.request().url());
      if (LOCAL_HOSTS.has(url.hostname)) return route.continue();
      externalRequests.push({ method: route.request().method(), category: category(url.hostname) });
      return route.abort('blockedbyclient');
    });
    const csrf = await (await context.request.get('/api/auth/csrf')).json();
    const signIn = await context.request.post('/api/auth/callback/credentials?redirect=false', {
      form: { username: 'admin', password: 'admin123', csrfToken: csrf.csrfToken, callbackUrl: '/work-transfer', json: 'true' },
    });
    assert.ok(signIn.ok());
    assert.ok((await (await context.request.get('/api/auth/session')).json()).user);
    const records = {};
    for (const name of ['alpha', 'beta']) {
      const seeded = await context.request.post('/api/admin/audit', { data: {
        eventType: 'SYNTHETIC_CONFIGURED_RECEIPT_FIXTURE', action: `HCR_SOURCE_${name.toUpperCase()}`,
        targetResource: `synthetic/hcr-${name}.md`, outcome: 'DRAFT',
      } });
      assert.equal(seeded.status(), 200);
      records[name] = (await seeded.json()).data.id;
      assert.ok(records[name]);
    }
    result.fixtureRecordIds = records;
    const page = await context.newPage();
    page.setDefaultTimeout(15000);
    await page.addInitScript(() => {
      localStorage.setItem('cvf_language', 'en');
      localStorage.setItem('cvf_onboarding_complete', 'true');
      localStorage.setItem('cvf_onboarding_seen', '1');
      localStorage.setItem('cvf_setup_banner_dismissed', 'true');
    });
    const exportPosts = [];
    const aiRequests = [];
    page.on('request', request => {
      const pathname = new URL(request.url()).pathname;
      if (pathname === EXPORT_PATH && request.method() === 'POST') exportPosts.push(request.postDataJSON());
      if (request.method() === 'POST' && /^\/api\/(ai|execute|generate)(\/|$)/.test(pathname)) aiRequests.push(pathname);
    });
    const panel = page.getByTestId('inline-export-panel');
    const field = label => page.getByLabel(label, { exact: true });
    const preview = page.frameLocator('iframe[title="Preview"]');
    const select = async name => { await page.getByTestId(`export-record-${records[name]}`).click(); };
    const build = async label => {
      assert.ok(exportPosts.length < 3, 'export POST cap');
      const pending = page.waitForResponse(r => new URL(r.url()).pathname === EXPORT_PATH && r.request().method() === 'POST', { timeout: 30000 });
      await page.getByRole('button', { name: 'Build HTML', exact: true }).click();
      const response = await pending;
      const raw = await response.body();
      const payload = JSON.parse(raw.toString('utf8'));
      const html = Buffer.from(payload.data.html, 'utf8');
      await writeFile(path.join(custody, `${label}-route.json`), raw);
      await writeFile(path.join(custody, `${label}-decoded.html`), html);
      const submitted = response.request().postDataJSON();
      return { status: response.status(), payload, data: payload.data, raw, html, submitted };
    };
    const download = async (label, expected) => {
      const pending = page.waitForEvent('download');
      await page.getByRole('button', { name: 'Download HTML', exact: true }).click();
      const saved = await pending;
      const target = path.join(custody, `${label}-download.html`);
      await saved.saveAs(target);
      const bytes = await readFile(target);
      assert.ok(bytes.equals(expected), `${label} download bytes equal route HTML`);
      return { filename: saved.suggestedFilename(), bytes: bytes.length, sha256: sha(bytes) };
    };
    const noteOf = async data => {
      const decision = data.governanceReceipt && data.governanceReceipt.decision;
      const id = decision === 'ALLOW' ? 'governance-receipt-evaluated-note' : 'governance-receipt-denied-note';
      await expect(page.getByTestId(id)).toBeVisible();
      return id;
    };
    const summary = (b, extra) => ({
      httpStatus: b.status, success: b.payload.success, authMode: b.payload.routeGovernanceProof.authMode,
      routeDecision: b.payload.routeGovernanceProof.decision, receiptStatus: b.data.governanceReceiptStatus,
      receiptPresent: b.data.governanceReceipt !== undefined, receiptDecision: b.data.governanceReceipt && b.data.governanceReceipt.decision,
      attemptId: b.data.governanceReceiptAttemptId, receiptId: b.data.governanceReceipt && b.data.governanceReceipt.receiptId,
      governanceState: b.data.governanceState, receiptAnchor: b.data.receiptAnchor, filename: b.data.filename,
      wireBytes: b.raw.length, wireSha256: sha(b.raw), htmlBytes: b.html.length, htmlSha256: sha(b.html),
      sourceTrimmedSha256: sha(Buffer.from(b.submitted.sourceContent.trim(), 'utf8')), ...extra,
    });

    await page.goto('/work-transfer', { waitUntil: 'networkidle', timeout: 45000 });
    await select('alpha');
    await expect(panel).toBeVisible();
    const title1 = 'HCR Browser Packet One';
    const marker1 = 'HCR marker build one';
    const source1 = `Record type: Complete review record\n\nReview status: Draft\n\nReview Boundary: synthetic only.\n\n${marker1}\n\nByte cases: Tiếng Việt, 日本語, mid BOM x﻿y.`;
    await field('Title').fill(title1);
    await field('Source notes').fill(source1);
    await field('Review boundary').fill('Synthetic configured-receipt composition only.');
    mark('build-1-start');
    const b1 = await build('build1');
    mark('build-1-end');
    assert.equal(b1.status, 200);
    assert.equal(b1.payload.success, true);
    assert.equal(b1.data.governanceReceiptStatus, 'PRESENT');
    assert.ok(b1.data.governanceReceiptAttemptId);
    assert.equal(b1.data.governanceReceipt.receiptId, b1.data.governanceReceiptAttemptId);
    assert.equal(b1.data.governanceState, 'DRAFT_UNACCEPTED');
    await expect(page.getByTestId('artifact-draft-state')).toContainText('DRAFT / UNACCEPTED');
    const note1 = await noteOf(b1.data);
    result.req01 = summary(b1, { visibleNote: note1, submittedFields: ['title', 'sourceContent', 'claimBoundary'].every(k => b1.submitted[k] !== undefined) });
    assert.equal(b1.submitted.title, title1);
    assert.equal(b1.submitted.sourceContent, source1);

    await expect(preview.locator('header > h1')).toHaveText(title1);
    await expect(preview.getByText(marker1)).toBeVisible();
    assert.ok(b1.html.toString('utf8').includes(result.req01.sourceTrimmedSha256));
    assert.notEqual(result.req01.sourceTrimmedSha256, result.req01.htmlSha256);
    assert.notEqual(result.req01.wireSha256, result.req01.htmlSha256);
    const d1 = await download('build1', b1.html);
    result.req03 = { build1: { ...d1, previewHeadingMatches: true, previewMarkerVisible: true, routeHtmlEqualsDownload: true } };

    const staleTitle = 'HCR Unsent Later Edit';
    const unsentMarker = 'HCR marker unsent';
    mark('stale-edit-start');
    await field('Title').fill(staleTitle);
    await field('Source notes').fill(`${source1}\n\n${unsentMarker}`);
    await expect(page.getByTestId('artifact-version-notice')).toHaveAttribute('data-version-state', 'stale');
    await expect(preview.locator('header > h1')).toHaveText(title1);
    await expect(preview.getByText(unsentMarker)).toHaveCount(0);
    await noteOf(b1.data);
    await page.waitForTimeout(900);
    const staleDownload = await download('stale', b1.html);
    assert.ok(!(await readFile(path.join(custody, 'stale-download.html'))).toString('utf8').includes(unsentMarker));
    assert.equal(exportPosts.length, 1);
    mark('stale-window-end');

    mark('build-2-start');
    const b2 = await build('build2');
    mark('build-2-end');
    assert.equal(b2.status, 200);
    assert.equal(b2.data.governanceReceiptStatus, 'PRESENT');
    assert.notEqual(b2.data.governanceReceiptAttemptId, b1.data.governanceReceiptAttemptId);
    await expect(page.getByTestId('artifact-version-notice')).toHaveAttribute('data-version-state', 'current');
    await expect(preview.locator('header > h1')).toHaveText(staleTitle);
    await expect(preview.getByText(unsentMarker)).toBeVisible();
    const d2 = await download('build2', b2.html);
    assert.ok(b2.html.toString('utf8').includes(unsentMarker));
    result.req03.build2 = { ...d2, previewHeadingMatches: true, routeHtmlEqualsDownload: true };
    result.req04 = { stale: { versionState: 'stale', previewRetained: true, oldDownload: staleDownload, exportPostsBeforeRebuild: 1 },
      build1: { attemptId: b1.data.governanceReceiptAttemptId }, build2: summary(b2, { versionState: 'current' }), exportPostsAfterRebuild: exportPosts.length };

    mark('reset-start');
    await select('alpha');
    await expect(panel).toHaveCount(0);
    await select('alpha');
    await expect(panel).toBeVisible();
    await expect(page.getByTestId('artifact-draft-state')).toHaveCount(0);
    await select('beta');
    await expect(field('Source reference')).toHaveValue('synthetic/hcr-beta.md');
    await expect(page.getByTestId('artifact-draft-state')).toHaveCount(0);
    await page.reload();
    await expect(page.getByTestId('history-list')).toBeVisible();
    await expect(panel).toHaveCount(0);
    await select('alpha');
    await expect(panel).toBeVisible();
    await expect(page.getByTestId('artifact-draft-state')).toHaveCount(0);
    await expect(page.locator('iframe[title="Preview"]')).toHaveCount(0);
    await page.waitForTimeout(900);
    const bodyText = await page.locator('body').innerText();
    result.req05 = { deselectReselectReset: true, otherFixtureReset: true, reloadReset: true, priorPacketShownAsCurrent: false,
      reloadLossWarningObserved: /unsaved|will be lost|lost on reload|not saved/i.test(bodyText), exportPostsAfterReset: exportPosts.length };
    assert.equal(exportPosts.length, 2);
    mark('reset-end');

    process.stdout.write('OWNED_ENGINE_STOP_REQUEST\n');
    mark('engine-stop-requested');
    await waitOwnedEngineStopped();
    mark('engine-stopped');
    await field('Title').fill('HCR Engine Down Packet');
    mark('build-3-start');
    const b3 = await build('build3');
    mark('build-3-end');
    assert.equal(b3.status, 200);
    assert.equal(b3.payload.success, true);
    assert.ok(['UNAVAILABLE', 'TIMED_OUT'].includes(b3.data.governanceReceiptStatus), `actual status ${b3.data.governanceReceiptStatus}`);
    assert.equal(b3.data.governanceReceipt, undefined);
    assert.equal(b3.data.governanceState, 'DRAFT_UNACCEPTED');
    await expect(page.getByTestId('governance-receipt-absent-note')).toBeVisible();
    await expect(page.getByTestId('governance-receipt-attempt-id')).toHaveText(b3.data.governanceReceiptAttemptId);
    const d3 = await download('build3', b3.html);
    result.req06 = summary(b3, { attemptIdVisible: true, absentNoteVisible: true, download: d3, exportPostsTotal: exportPosts.length });
    assert.equal(exportPosts.length, 3);
    assert.deepEqual(aiRequests, []);
    result.req07 = { exportPostCount: exportPosts.length, observedBrowserAiPosts: aiRequests, externalRequests, browserVersion: browser.version() };
    result.exportPosts = exportPosts.map(p => ({ title: p.title, receiptAnchor: p.receiptAnchor, sourceSha256: sha(Buffer.from(p.sourceContent.trim(), 'utf8')) }));
    result.partial = false;
  } catch (error) {
    result.error = String(error && error.message).slice(0, 1500);
    process.exitCode = 1;
  } finally {
    await writeFile(output, JSON.stringify(result, null, 2));
    await browser.close();
    process.stdin.destroy();
  }
}

async function main() {
  const [modules, baseURL, output, downloadDir, mode] = process.argv.slice(2);
  if (mode === 'configured-receipt-composition') return composition(modules, baseURL, output, downloadDir);
  const { chromium, expect } = require(path.join(modules, '@playwright/test'));
  const browser = await chromium.launch({ headless: true });
  try {
    const context = await browser.newContext({ baseURL, acceptDownloads: true });
    const csrf = await (await context.request.get('/api/auth/csrf')).json();
    assert.ok(csrf.csrfToken);
    const signIn = await context.request.post('/api/auth/callback/credentials?redirect=false', {
      form: { username: 'admin', password: 'admin123', csrfToken: csrf.csrfToken,
        callbackUrl: '/work-transfer', json: 'true' },
    });
    assert.ok(signIn.ok());
    assert.ok((await (await context.request.get('/api/auth/session')).json()).user);
    // Work Transfer opens the panel from an audit event. Seed one event through
    // the real admin route into the runner's disposable file store.
    const seedResponse = await context.request.post('/api/admin/audit', { data: {
      eventType: 'SYNTHETIC_BROWSER_FIXTURE', action: 'W05_SYNTHETIC_SOURCE',
      targetResource: 'synthetic/w05-browser-notes.md', outcome: 'DRAFT',
    } });
    assert.equal(seedResponse.status(), 200);
    const seed = await seedResponse.json();
    assert.equal(seed.success, true);
    assert.ok(seed.data.id);
    const page = await context.newPage();
    page.setDefaultTimeout(15000);
    await page.addInitScript(() => {
      localStorage.setItem('cvf_language', 'en');
      localStorage.setItem('cvf_onboarding_complete', 'true');
      localStorage.setItem('cvf_onboarding_seen', '1');
      localStorage.setItem('cvf_setup_banner_dismissed', 'true');
    });
    const exports = [];
    const aiRequests = [];
    page.on('request', request => {
      const pathname = new URL(request.url()).pathname;
      if (pathname === '/api/artifacts/export') exports.push(request.postDataJSON());
      if (request.method() === 'POST' && /^\/api\/(ai|execute|generate)(\/|$)/.test(pathname)) {
        aiRequests.push(pathname);
      }
    });
    await page.goto('/work-transfer', { waitUntil: 'networkidle', timeout: 45000 });
    await page.getByTestId(`export-record-${seed.data.id}`).click();
    await expect(page.getByTestId('inline-export-panel')).toBeVisible();
    const title = 'W05 Synthetic Browser Packet';
    const source = 'Record type: Complete review record\n\nReview status: Draft\n\n'
      + 'Review Boundary: synthetic browser transport only.\n\n'
      + 'Byte cases: Ti\u1ebfng Vi\u1ec7t, \u65e5\u672c\u8a9e, \ud83d\ude00, mid BOM x\ufeffy.';
    await page.getByLabel('Title', { exact: true }).fill(title);
    await page.getByLabel('Source notes', { exact: true }).fill(source);
    await page.getByLabel('Receipt reference', { exact: true }).fill('w05-synthetic-browser');
    await page.getByLabel('Review boundary', { exact: true }).fill('Synthetic browser transport only.');
    const responsePending = page.waitForResponse(response =>
      new URL(response.url()).pathname === '/api/artifacts/export' && response.request().method() === 'POST',
      { timeout: 30000 });
    await page.getByRole('button', { name: 'Build HTML', exact: true }).click();
    const response = await responsePending;
    const payload = await response.json();
    assert.equal(response.status(), 200);
    assert.equal(payload.success, true);
    const data = payload.data;
    assert.equal(payload.routeGovernanceProof.authMode, 'session');
    assert.equal(payload.routeGovernanceProof.decision, 'ALLOW');
    assert.equal(data.governanceReceiptStatus, 'PRESENT');
    assert.equal(data.governanceState, 'DRAFT_UNACCEPTED');
    assert.ok(data.governanceReceiptAttemptId);
    assert.equal(data.governanceReceipt.receiptId, data.governanceReceiptAttemptId);
    assert.equal(data.governanceReceipt.decision, 'ALLOW');
    await expect(page.getByTestId('artifact-draft-state')).toContainText('DRAFT / UNACCEPTED');
    await expect(page.getByTestId('governance-receipt-evaluated-note')).toContainText('not artifact approval');
    assert.equal(exports.length, 1);
    assert.equal(exports[0].title, title);
    assert.equal(exports[0].sourceContent, source);
    const expected = Buffer.from(data.html, 'utf8');
    const hashes = [];
    for (let index = 0; index < 2; index++) {
      if (index === 1) {
        await page.getByLabel('Title', { exact: true }).fill('Unsent later form edit');
        await expect(page.getByText(/Earlier version \(build #1\)/)).toBeVisible();
      }
      const downloadPending = page.waitForEvent('download');
      await page.getByRole('button', { name: 'Download HTML', exact: true }).click();
      const download = await downloadPending;
      assert.equal(download.suggestedFilename(), data.filename);
      const savedPath = path.join(downloadDir, `packet-${index}.html`);
      await download.saveAs(savedPath);
      const saved = await readFile(savedPath);
      assert.deepEqual(saved, expected);
      hashes.push(createHash('sha256').update(saved).digest('hex'));
    }
    assert.equal(exports.length, 1);
    assert.deepEqual(aiRequests, []);
    await writeFile(output, JSON.stringify({
      httpStatus: response.status(), authMode: payload.routeGovernanceProof.authMode,
      routeDecision: payload.routeGovernanceProof.decision,
      attemptId: data.governanceReceiptAttemptId, receiptId: data.governanceReceipt.receiptId,
      receiptStatus: data.governanceReceiptStatus, receiptDecision: data.governanceReceipt.decision,
      artifactState: data.governanceState, exportRequests: exports.length,
      observedBrowserAiPosts: aiRequests, bytes: expected.length, savedSha256: hashes,
      staleFormDownloadMatchesSubmittedVersion: true, browserVersion: browser.version(),
      sourceAuditEventId: seed.data.id, syntheticAuditSeedRequests: 1,
      claimBoundary: 'Synthetic browser transport/presentation; no semantic governance or artifact acceptance proof.',
    }, null, 2));
  } finally {
    await browser.close();
  }
}

main().catch(error => { console.error(error.message); process.exitCode = 1; });
