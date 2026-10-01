import { expect, test, type BrowserContext, type Page, type Request } from '@playwright/test';
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

// ---------------------------------------------------------------------------------------
// Passive-resource isolation for the Preview (synthetic, one Chromium profile, no forwarding).
//
// The script sandbox above does not stop passive loads: an empty sandbox still fetches
// images, stylesheets, CSS imports/backgrounds, fonts and nested frames. The oracle below is
// answered on the REAL Artifacts Preview:
//   control   - the same markup in a disposable context, empty sandbox and NO resource policy,
//               produces same-origin and off-origin hits for every passive class (no scripts).
//   negative  - the actual product Preview, before any Print click, produces zero hits and
//               still renders benign text and inline style; sandbox/origin/script unchanged.
//   mutation  - only the Preview resource policy is removed from the real product path
//               (sandbox kept): the same negative oracle must fail with passive hits.
// Interception is installed before any payload is inserted and fulfills locally (the off-origin
// host never resolves and nothing is forwarded). Print behavior is covered by the Print spec.
const PROBE_PATH = '/api/cvf-preview-probe';
const OFF_ORIGIN = 'https://offorigin.cvf-preview-probe.test';
const BASE_URL = process.env.PLAYWRIGHT_BASE_URL || `http://localhost:${process.env.CVF_PLAYWRIGHT_PORT ?? 3001}`;
const APP_ORIGIN = new URL(BASE_URL).origin;
const POLICY_META_PREFIX = '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'';
const PNG_B64 = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==';
const PNG_1X1 = Buffer.from(PNG_B64, 'base64');
const DATA_IMG = `data:image/png;base64,${PNG_B64}`;
const PASSIVE_KINDS = ['img', 'srcset', 'link-css', 'css-import', 'css-bg', 'font', 'frame', 'frame-img', 'object', 'object-img'] as const;
const EXPECTED_HITS = (['same', 'off'] as const).flatMap(where => PASSIVE_KINDS.map(kind => `${where}:${kind}`));
const H1_COLOR = 'rgb(1, 2, 3)';
const P_BACKGROUND = 'rgb(4, 5, 6)';
const POLICY_SCRIPT_MARKER = 'data-cvf-preview-script-ran';

const whereOf = (origin: string) => (origin === APP_ORIGIN ? 'same' : 'off');
const probeUrl = (origin: string, kind: string) => `${origin}${PROBE_PATH}?k=${kind}`;
const hitKey = (url: URL) => `${url.origin === APP_ORIGIN ? 'same' : 'off'}:${url.searchParams.get('k') ?? 'none'}`;

function passiveMarkup(origin: string): string {
  const u = (kind: string) => probeUrl(origin, kind);
  return (
    `<img src="${u('img')}" alt=""><img srcset="${u('srcset')} 1x" alt="">` +
    `<link rel="stylesheet" href="${u('link-css')}">` +
    `<object data="${u('object')}" type="text/html"></object><iframe src="${u('frame')}"></iframe>` +
    `<div class="cvf-bg-${whereOf(origin)}">bg</div><span class="cvf-font-${whereOf(origin)}">font</span>`
  );
}

const benignBody =
  '<main><h1>Preview Passive Heading</h1>' +
  `<p style="background-color:${P_BACKGROUND}">Preview passive benign paragraph.</p>` +
  `<img id="cvf-data-img" src="${DATA_IMG}" alt="">` +
  `<script>document.documentElement.setAttribute('${POLICY_SCRIPT_MARKER}','1');</script></main>`;
const inlineStyle = `<style>h1{color:${H1_COLOR}}</style>`;

// Default-producer shape: plain leading doctype, head with inline style.
const DOCTYPE_FIXTURE =
  `<!doctype html><html lang="en"><head>${inlineStyle}</head><body>${benignBody}${passiveMarkup(APP_ORIGIN)}${passiveMarkup(OFF_ORIGIN)}</body></html>`;
// Adversary shape: passive markup before the doctype and any head, duplicate heads, and a
// payload-supplied permissive policy that tries to reopen network authority.
const EARLY_FIXTURE =
  `${passiveMarkup(APP_ORIGIN)}${passiveMarkup(OFF_ORIGIN)}<!doctype html><html lang="en"><head>` +
  `<meta http-equiv="Content-Security-Policy" content="default-src * 'unsafe-inline' data: blob:">${inlineStyle}</head><head></head><body>${benignBody}</body></html>`;

function probeResponse(kind: string, origin: string): { contentType: string; body: string | Buffer } {
  const u = (k: string) => probeUrl(origin, k);
  switch (kind) {
    case 'img': case 'srcset': case 'css-bg': case 'frame-img': case 'object-img':
      return { contentType: 'image/png', body: PNG_1X1 };
    case 'link-css':
      return {
        contentType: 'text/css',
        body: `@import url(${u('css-import')});.cvf-bg-${whereOf(origin)}{background-image:url(${u('css-bg')});width:4px;height:4px}` +
          `@font-face{font-family:CvfProbe${whereOf(origin)};src:url(${u('font')})}.cvf-font-${whereOf(origin)}{font-family:CvfProbe${whereOf(origin)}}`,
      };
    case 'css-import': return { contentType: 'text/css', body: 'body{}' };
    case 'font': return { contentType: 'font/woff2', body: Buffer.from('not-a-real-font') };
    case 'frame': return { contentType: 'text/html', body: `<!doctype html><body><img src="${u('frame-img')}" alt=""></body>` };
    case 'object': return { contentType: 'text/html', body: `<!doctype html><body><img src="${u('object-img')}" alt=""></body>` };
    default: return { contentType: 'text/plain', body: 'unknown' };
  }
}

// Fulfills the controlled endpoint locally on both origins and records each hit by class.
async function installProbe(context: BrowserContext, hits: Map<string, number>) {
  await context.route(url => url.pathname === PROBE_PATH && (url.origin === APP_ORIGIN || url.origin === OFF_ORIGIN), async route => {
    const url = new URL(route.request().url());
    hits.set(hitKey(url), (hits.get(hitKey(url)) ?? 0) + 1);
    const { contentType, body } = probeResponse(url.searchParams.get('k') ?? 'none', url.origin);
    await route.fulfill({ status: 200, contentType, body, headers: { 'access-control-allow-origin': '*' } });
  });
}

const hitList = (hits: Map<string, number>) => [...hits.keys()].sort();

// Control: disposable context, the existing empty sandbox, no resource policy, no script reliance.
test('B1 Preview passive-resource control: an empty sandbox without a resource policy loads same-origin and off-origin passive resources', async ({ browser, browserName }) => {
  const context = await browser.newContext();
  try {
    const hits = new Map<string, number>();
    await installProbe(context, hits);
    const page = await context.newPage();
    await page.setContent('<!doctype html><html><body><iframe id="control" sandbox></iframe></body></html>');
    await page.evaluate((html) => { (document.getElementById('control') as HTMLIFrameElement).srcdoc = html; }, EARLY_FIXTURE);
    await expect.poll(() => EXPECTED_HITS.filter(k => !hits.has(k)), { timeout: 15_000 }).toEqual([]);
    const control = page.frameLocator('#control');
    const sandboxAttr = await page.evaluate(() => document.getElementById('control')!.getAttribute('sandbox'));
    const dataImg = await control.locator('#cvf-data-img').evaluate((el) => ({ complete: (el as HTMLImageElement).complete, naturalWidth: (el as HTMLImageElement).naturalWidth }));
    const scriptRan = await control.locator('html').getAttribute(POLICY_SCRIPT_MARKER);
    console.log('B1_PREVIEW_RESOURCE_CONTROL ' + JSON.stringify({ browserName, browserVersion: browser.version(), sandboxAttr, expectedHits: EXPECTED_HITS, observedHits: hitList(hits), dataImg, scriptRan }));
    // Passive hits happened with the script sandbox intact, so the control is not an inert fixture.
    expect(sandboxAttr).toBe('');
    expect(scriptRan).toBeNull();
    // A data image really decodes without a policy, so a blocked data image later is the policy.
    expect(dataImg).toEqual({ complete: true, naturalWidth: 1 });
    expect(hitList(hits)).toEqual([...EXPECTED_HITS].sort());
  } finally {
    await context.close();
  }
});

type PreviewMutation = 'policy' | null;

// Test-only mutation: removes ONLY the Preview resource policy meta from the real product's
// iframe srcdoc. The empty sandbox and everything else stay as the product produced them.
const policyMutationScript = (metaPrefix: string) => `(() => {
  const PREFIX = ${JSON.stringify(metaPrefix)};
  const strip = (value) => {
    const text = String(value);
    const start = text.indexOf(PREFIX);
    if (start < 0) return text;
    const end = text.indexOf('>', start);
    window.__cvfPolicyStripped = true;
    return text.slice(0, start) + text.slice(end + 1);
  };
  const setAttribute = Element.prototype.setAttribute;
  Element.prototype.setAttribute = function (name, value) {
    if (this.tagName === 'IFRAME' && String(name).toLowerCase() === 'srcdoc') return setAttribute.call(this, name, strip(value));
    return setAttribute.call(this, name, value);
  };
  const d = Object.getOwnPropertyDescriptor(HTMLIFrameElement.prototype, 'srcdoc');
  Object.defineProperty(HTMLIFrameElement.prototype, 'srcdoc', { ...d, set(value) { return d.set.call(this, strip(value)); } });
})();`;

async function previewScenario(page: Page, context: BrowserContext, browserName: string, opts: { fixture: string; mutation: PreviewMutation }) {
  const hits = new Map<string, number>();
  const unexpected: string[] = [];
  let exportHits = 0;
  await installProbe(context, hits);
  if (opts.mutation === 'policy') await page.addInitScript(policyMutationScript(POLICY_META_PREFIX));
  await page.route('**/api/artifacts/export', async route => {
    exportHits += 1;
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        success: true,
        data: {
          html: opts.fixture,
          filename: 'b1-preview-passive.html',
          receiptAnchor: 'receipt-b1-preview-passive',
          generatedAt: '2026-10-01T10:00:00.000Z',
          governanceState: 'DRAFT_UNACCEPTED',
          verification: [{ label: 'Synthetic fixture', passed: true, detail: 'In-memory only.' }],
        },
      }),
    });
  });
  // Every page and frame of the context is observed; sub-frame requests that are not local
  // schemes or the controlled endpoint are unexpected. Same-origin is never exempted.
  context.on('request', (request: Request) => {
    const url = request.url();
    const owner = request.frame();
    if (owner === owner.page().mainFrame()) return;
    if (url.startsWith('about:') || url.startsWith('data:') || url.startsWith('blob:')) return;
    const parsed = new URL(url);
    if (parsed.pathname === PROBE_PATH && (parsed.origin === APP_ORIGIN || parsed.origin === OFF_ORIGIN)) return;
    unexpected.push(url);
  });

  await login(page);
  await page.evaluate(() => localStorage.setItem('cvf_language', 'en'));
  await page.goto('/artifacts');
  await page.evaluate(() => { (window as unknown as Record<string, unknown>).__cvfPreviewSentinel = 'unset'; });
  // Interception is live and counters are reset before the actual Preview exists; no Print click happens.
  hits.clear();
  await page.getByLabel('Title').fill('B1 Preview Passive');
  await page.getByRole('button', { name: /Build HTML/i }).click();
  const iframe = page.locator('iframe[title="Preview"]');
  await expect(iframe).toBeVisible();
  const frame = page.frameLocator('iframe[title="Preview"]');
  await expect(frame.getByRole('heading', { name: 'Preview Passive Heading' })).toBeVisible();
  // Give any permitted passive load (and its downstream dependencies) time to arrive.
  await page.waitForTimeout(2_000);

  const srcdoc = await iframe.getAttribute('srcdoc');
  const sandboxAttr = await iframe.getAttribute('sandbox');
  const frameOrigin = await frame.locator('html').evaluate(() => location.origin).catch(() => null);
  const scriptRan = await frame.locator('html').getAttribute(POLICY_SCRIPT_MARKER);
  const h1Color = await frame.locator('h1').evaluate(el => getComputedStyle(el).color);
  const paragraphBackground = await frame.locator('p').evaluate(el => getComputedStyle(el).backgroundColor);
  const paragraphText = await frame.locator('p').textContent();
  const dataImg = await frame.locator('#cvf-data-img').evaluate((el) => ({ complete: (el as HTMLImageElement).complete, naturalWidth: (el as HTMLImageElement).naturalWidth }));
  const parentSentinel = await page.evaluate(() => (window as unknown as Record<string, unknown>).__cvfPreviewSentinel);
  const policyStripped = await page.evaluate(() => (window as unknown as Record<string, unknown>).__cvfPolicyStripped === true);
  const policyIndex = srcdoc ? srcdoc.indexOf(POLICY_META_PREFIX) : -1;
  const resourceIndexes = srcdoc ? ['<img', '<link', '<object', '<iframe'].map(t => srcdoc.indexOf(t)).filter(i => i >= 0) : [];
  const firstResourceIndex = resourceIndexes.length > 0 ? Math.min(...resourceIndexes) : Number.MAX_SAFE_INTEGER;
  const observations = {
    browserName,
    browserVersion: page.context().browser()?.version(),
    mutation: opts.mutation,
    policyStrippedByMutation: policyStripped,
    interceptionInstalledBeforeBuild: true,
    exportRouteHits: exportHits,
    pageCount: context.pages().length,
    sandboxAttr,
    frameOrigin,
    scriptRan,
    parentSentinel,
    srcdocDiffersFromCanonical: srcdoc !== opts.fixture,
    policyBeforeFirstResource: policyIndex >= 0 && policyIndex < firstResourceIndex,
    policyPresentInSrcdoc: policyIndex >= 0,
    h1Color,
    paragraphBackground,
    paragraphText,
    dataImg,
    observedHits: hitList(hits),
    unexpectedRequests: unexpected,
  };
  console.log('B1_PREVIEW_RESOURCE_OBSERVATIONS ' + JSON.stringify(observations));
  return observations;
}

type PreviewObservations = Awaited<ReturnType<typeof previewScenario>>;

// The negative oracle: any entry means the actual Preview broke resource isolation or lost
// the benign inline rendering / script sandbox it must keep.
function previewViolations(o: PreviewObservations): string[] {
  const v: string[] = [];
  if (o.observedHits.length > 0) v.push(`passive resource request reached the controlled endpoint: ${o.observedHits.join(',')}`);
  if (o.unexpectedRequests.length > 0) v.push('unexpected sub-frame request');
  if (o.dataImg.naturalWidth !== 0) v.push('data image must be blocked in Preview');
  if (o.sandboxAttr !== '') v.push('preview frame must carry an empty sandbox attribute');
  if (o.frameOrigin !== 'null') v.push('preview frame origin must be opaque');
  if (o.scriptRan !== null || o.parentSentinel !== 'unset') v.push('payload script must not execute');
  if (o.h1Color !== H1_COLOR) v.push('inline stylesheet must still style the heading');
  if (o.paragraphBackground !== P_BACKGROUND) v.push('inline style attribute must still apply');
  if (o.paragraphText !== 'Preview passive benign paragraph.') v.push('benign text must stay visible');
  return v;
}

const previewCases = [
  ['early passive markup before any head, duplicate heads and permissive payload policy', EARLY_FIXTURE],
  ['plain doctype fixture with head inline style', DOCTYPE_FIXTURE],
] as const;

for (const [name, fixture] of previewCases) {
  test(`B1 Preview passive-resource negative: actual Preview before Print has zero hits and keeps benign inline render (${name})`, async ({ page, context, browserName }) => {
    const o = await previewScenario(page, context, browserName, { fixture, mutation: null });
    expect(o.exportRouteHits).toBe(1);
    expect(o.pageCount).toBe(1);
    expect(o.policyPresentInSrcdoc).toBe(true);
    expect(o.policyBeforeFirstResource).toBe(true);
    expect(o.srcdocDiffersFromCanonical).toBe(true);
    expect(previewViolations(o), JSON.stringify(o)).toEqual([]);
  });
}

test('B1 Preview passive-resource mutation: removing only the resource policy restores passive hits and fails the same oracle', async ({ page, context, browserName }) => {
  const o = await previewScenario(page, context, browserName, { fixture: EARLY_FIXTURE, mutation: 'policy' });
  const violations = previewViolations(o);

  // The mutation applied to the real product path and nothing else changed.
  expect(o.policyStrippedByMutation, JSON.stringify(o)).toBe(true);
  expect(o.policyPresentInSrcdoc, JSON.stringify(o)).toBe(false);
  expect(o.sandboxAttr).toBe('');
  expect(o.frameOrigin).toBe('null');
  expect(o.scriptRan).toBeNull();
  expect(o.parentSentinel).toBe('unset');
  expect(o.paragraphText).toBe('Preview passive benign paragraph.');
  // Same oracle, same fixture: it now fails, and only through passive resources.
  expect(violations.length, JSON.stringify(o)).toBeGreaterThan(0);
  expect(violations.every(entry => entry.startsWith('passive resource request') || entry.startsWith('data image'))).toBe(true);
  expect(violations.some(entry => entry.startsWith('passive resource request')), JSON.stringify(o)).toBe(true);
  expect(o.observedHits, JSON.stringify(o)).toEqual([...EXPECTED_HITS].sort());
});
