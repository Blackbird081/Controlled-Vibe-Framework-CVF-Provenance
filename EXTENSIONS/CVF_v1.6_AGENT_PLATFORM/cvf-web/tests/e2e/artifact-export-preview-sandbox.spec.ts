import { expect, test, type Request } from '@playwright/test';
import { login, seedStorage } from './utils';

// Synthetic B1 preview sandbox proof (one Chromium profile, intercepted export).
// The inline script is harmless: it only sets an in-memory marker on its own
// document and on the parent window. No network, storage, or external URL.
const SENTINEL = '__cvfB1Sentinel';
const SELF_MARKER = 'data-cvf-b1-ran';
const FIXTURE_SCRIPT =
  `document.documentElement.setAttribute('${SELF_MARKER}','1');` +
  `try{window.parent.${SENTINEL}='executed';}catch(e){}`;
const FIXTURE_HTML =
  '<!doctype html><html lang="en"><body><main><h1>B1 Sandbox Synthetic Heading</h1>' +
  `<script>${FIXTURE_SCRIPT}</script></main></body></html>`;

test.beforeEach(async ({ page }) => {
  await seedStorage(page);
});

test('B1 preview iframe blocks inline script in Chromium while an unsandboxed control executes it', async ({ page, browserName }) => {
  const fixtureRequests: string[] = [];
  const unexpectedRequests: string[] = [];
  let routeHits = 0;

  // Positive control: same fixture, unsandboxed same-origin srcdoc iframe.
  await page.setContent('<!doctype html><html><body><iframe id="control"></iframe></body></html>');
  await page.evaluate(({ html, sentinel }) => {
    (window as unknown as Record<string, unknown>)[sentinel] = 'unset';
    (document.getElementById('control') as HTMLIFrameElement).srcdoc = html;
  }, { html: FIXTURE_HTML, sentinel: SENTINEL });
  await expect.poll(() => page.evaluate((s) => (window as unknown as Record<string, unknown>)[s], SENTINEL)).toBe('executed');
  const controlSelfMarker = await page.evaluate((marker) => {
    const doc = (document.getElementById('control') as HTMLIFrameElement).contentDocument;
    return doc ? doc.documentElement.getAttribute(marker) : 'NO_DOCUMENT_ACCESS';
  }, SELF_MARKER);
  expect(controlSelfMarker).toBe('1');
  const controlSandboxAttr = await page.evaluate(() => document.getElementById('control')!.getAttribute('sandbox'));
  expect(controlSandboxAttr).toBeNull();

  // Remove control and reset the sentinel before the real panel run.
  await page.evaluate((sentinel) => {
    document.getElementById('control')?.remove();
    (window as unknown as Record<string, unknown>)[sentinel] = 'unset';
  }, SENTINEL);

  await page.route('**/api/artifacts/export', async route => {
    routeHits += 1;
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        success: true,
        data: {
          html: FIXTURE_HTML,
          filename: 'b1-sandbox-synthetic.html',
          receiptAnchor: 'receipt-b1-sandbox',
          generatedAt: '2026-10-01T10:00:00.000Z',
          governanceState: 'DRAFT_UNACCEPTED',
          verification: [{ label: 'Synthetic fixture', passed: true, detail: 'In-memory only.' }],
        },
      }),
    });
  });

  page.on('request', (request: Request) => {
    const url = request.url();
    if (url.includes('b1-sandbox-synthetic') || url.includes('B1 Sandbox')) fixtureRequests.push(url);
    const frame = request.frame();
    const fromSubframe = frame !== page.mainFrame();
    if (fromSubframe && !url.startsWith('about:') && !url.startsWith('data:') && !url.startsWith('blob:')) {
      unexpectedRequests.push(url);
    }
  });

  await login(page);
  await page.evaluate(() => localStorage.setItem('cvf_language', 'en'));
  await page.goto('/artifacts');
  await page.evaluate((sentinel) => {
    (window as unknown as Record<string, unknown>)[sentinel] = 'unset';
  }, SENTINEL);
  await page.getByLabel('Title').fill('B1 Sandbox Synthetic');
  await page.getByRole('button', { name: /Build HTML/i }).click();

  const iframe = page.locator('iframe[title="Preview"]');
  await expect(iframe).toBeVisible();
  const heading = page.frameLocator('iframe[title="Preview"]').getByRole('heading', { name: 'B1 Sandbox Synthetic Heading' });
  await expect(heading).toBeVisible();

  // Give any (blocked) script ample time to run before asserting absence.
  await page.waitForTimeout(1000);

  const sandboxAttr = await iframe.getAttribute('sandbox');
  const sandboxTokens = await iframe.evaluate((el) => Array.from((el as HTMLIFrameElement).sandbox));
  const parentSentinel = await page.evaluate((s) => (window as unknown as Record<string, unknown>)[s], SENTINEL);
  const panelSelfMarker = await page
    .frameLocator('iframe[title="Preview"]')
    .locator('html')
    .getAttribute(SELF_MARKER);
  // Opaque origin: parent cannot reach the document of a sandboxed (no allow-same-origin) frame.
  const contentDocumentReachable = await iframe.evaluate((el) => (el as HTMLIFrameElement).contentDocument !== null);
  const frameOrigin = await page
    .frameLocator('iframe[title="Preview"]')
    .locator('html')
    .evaluate(() => location.origin);

  console.log('B1_SANDBOX_OBSERVATIONS ' + JSON.stringify({
    browserName,
    browserVersion: page.context().browser()?.version(),
    controlParentSentinel: 'executed',
    controlSelfMarker,
    controlSandboxAttr,
    sandboxAttr,
    sandboxTokens,
    parentSentinel,
    panelSelfMarker,
    contentDocumentReachable,
    frameOrigin,
    routeHits,
    fixtureRequestCount: fixtureRequests.length,
    unexpectedRequestCount: unexpectedRequests.length,
  }));

  expect(routeHits).toBeGreaterThanOrEqual(1);
  expect(sandboxAttr).toBe('');
  expect(sandboxTokens).toEqual([]);
  expect(parentSentinel).toBe('unset');
  expect(panelSelfMarker).toBeNull();
  expect(contentDocumentReachable).toBe(false);
  expect(frameOrigin).toBe('null');
  expect(fixtureRequests).toEqual([]);
  expect(unexpectedRequests).toEqual([]);
});
