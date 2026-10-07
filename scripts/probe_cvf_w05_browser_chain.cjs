/* Disposable W05 browser transport/presentation proof; no provider invocation. */
'use strict';
const assert = require('node:assert/strict');
const { createHash } = require('node:crypto');
const { readFile, writeFile } = require('node:fs/promises');
const path = require('node:path');

async function main() {
  const [modules, baseURL, output, downloadDir] = process.argv.slice(2);
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
