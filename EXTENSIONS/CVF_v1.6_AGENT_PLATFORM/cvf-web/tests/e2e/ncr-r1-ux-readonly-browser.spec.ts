// Text Encoding Exception: Vietnamese UI copy is asserted verbatim as the real-browser language oracle.
// UI-only resulting-source verification of the R1 existing-owner UX repair (AGENTS pure-UI exception): 44px targets, visible focus,
// native skip link, localized pill, settled keyboard geometry and one pre-effect validation on the real running app. The browser route
// denies every non-GET/HEAD/OPTIONS request (auth included) and counts it before it is sent; the only credentials POST is the existing
// loginAs APIRequestContext bootstrap, observed by method/path/status only. No provider, evaluate/execute, external network or private data.
import { createRequire } from 'node:module';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

// Resolve installed packages and the existing helper relative to the app cwd; this spec runs from a runtime folder.
const appRequire = createRequire(path.join(process.cwd(), 'package.json'));
const { test, expect } = appRequire('@playwright/test');
const { loginAs } = appRequire(path.join(process.cwd(), 'tests/e2e/utils'));

const RUN_ROOT = process.env.CVF_NCR_RUN_ROOT as string;
const SELECTED = 'ncr-synthetic-ux-job-001';
const GENERIC = 'ux-generic-audit-001';
const LOOPBACK = new Set(['localhost', '127.0.0.1', '[::1]', '::1']);
const VIEWPORTS = [
  { name: 'desktop', width: 1366, height: 900 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'mobile', width: 390, height: 844 },
];
const THEMES = [
  { name: 'dark-indigo', theme: 'dark', accent: 'indigo', rgb: '99 102 241', css: 'rgb(99, 102, 241)' },
  { name: 'light-indigo', theme: 'light', accent: 'indigo', rgb: '99 102 241', css: 'rgb(99, 102, 241)' },
  { name: 'dark-emerald', theme: 'dark', accent: 'emerald', rgb: '16 185 129', css: 'rgb(16, 185, 129)' },
];
const AUDIT_FIXTURE = [
  { id: SELECTED, timestamp: '2026-10-18T02:00:00.000Z', action: 'ncr-synthetic selected job flow', actorId: 'ncr-synthetic-worker',
    actorRole: 'admin', targetResource: 'fixtures/ux-selected.md', outcome: 'SYNTHETIC_READY_FOR_REVIEW' },
  { id: GENERIC, timestamp: '2026-10-18T01:00:00.000Z', action: 'generic audit event', actorId: 'ux-generic-actor',
    actorRole: 'admin', targetResource: 'fixtures/ux-generic.md', outcome: 'RECORDED' },
];
const COPY = {
  en: { goal: 'Goal', criterion: 'Criterion 1', add: 'Add criterion', build: 'Build HTML', title: 'Title', source: 'Source reference', section: 'Local test HTML job',
    candidate: 'Candidate', skip: 'Skip to main content',
    selected: ['local test profile', 'when you choose Save', 'no review receipt is requested', 'unverified and unaccepted', 'not trusted evidence or business acceptance',
      'Stop only acts on this page', 'does not confirm that a remote task stopped or determine cost'],
    generic: ['may send a short excerpt', 'depends on this deployment'], validation: 'Enter the goal and all criteria before building.' },
  vi: { goal: 'Mục tiêu', criterion: 'Tiêu chí 1', add: 'Thêm tiêu chí', build: 'Tạo HTML', title: 'Tiêu đề', source: 'Nguồn tham chiếu', section: 'Tác vụ HTML thử nghiệm cục bộ',
    candidate: 'Bản nháp chờ rà soát', skip: 'Bỏ qua đến nội dung chính',
    selected: ['chế độ thử nghiệm cục bộ', 'khi bạn chọn Lưu', 'không có yêu cầu lấy biên nhận', 'chưa được xác minh và chưa được chấp nhận',
      'không phải bằng chứng đáng tin cậy hay sự chấp nhận trong nghiệp vụ', 'không xác nhận thao tác từ xa đã dừng', 'chi phí vẫn chưa rõ'],
    generic: ['có thể gửi một đoạn ngắn', 'phụ thuộc vào cấu hình triển khai'], validation: 'Hãy nhập mục tiêu và đầy đủ tiêu chí trước khi tạo HTML.' },
} as const;
// Named single-line (and field) controls that must reach 44px height; source pattern per language.
const NAMED_FIELDS: [string, string, boolean][] = [
  ['Title', '^(Title|Tiêu đề)$', false], ['Source reference', '^(Source reference|Nguồn tham chiếu)$', false], ['Record type', '^(Record type|Loại bản ghi)$', false],
  ['Review status', '^(Review status|Trạng thái rà soát)$', false], ['Receipt reference', '^(Receipt reference|Mã receipt)$', false],
  ['Review boundary', '^(Review boundary|Ranh giới rà soát)$', false], ['Source notes', '^(Source notes|Ghi chú nguồn)$', false],
  ['Goal', '^(Goal|Mục tiêu)$', true], ['Criterion 1', '^(Criterion 1|Tiêu chí 1)$', true], ['Add criterion', '^(Add criterion|Thêm tiêu chí)$', true],
];

// In-page measurement of the open inline panel. Pure DOM reads; nothing is activated and nothing is scrolled.
const MEASURE = ({ profile, lang, vw, named }: { profile: string; lang: string; vw: number; vh: number; named: [string, string, boolean][] }) => {
  const styleOf = (el: Element) => {
    const cs = getComputedStyle(el);
    return { outlineStyle: cs.outlineStyle, outlineWidth: cs.outlineWidth, outlineColor: cs.outlineColor, outlineOffset: cs.outlineOffset, boxShadow: cs.boxShadow,
      borderColor: cs.borderTopColor, borderWidth: cs.borderTopWidth, borderStyle: cs.borderTopStyle, background: cs.backgroundColor, opacity: cs.opacity, cursor: cs.cursor };
  };
  const q = (s: string, r: ParentNode = document) => r.querySelector(s) as HTMLElement | null;
  const vis = (el: Element) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const rect = (el: Element) => { const r = el.getBoundingClientRect(); return { x: Math.round(r.x * 10) / 10, y: Math.round(r.y * 10) / 10, w: Math.round(r.width * 10) / 10, h: Math.round(r.height * 10) / 10,
    right: Math.round(r.right * 10) / 10, bottom: Math.round(r.bottom * 10) / 10 }; };
  const nameOf = (el: HTMLElement) => (el.getAttribute('aria-label') || el.innerText || (el as HTMLInputElement).placeholder || el.getAttribute('title') || el.tagName).trim().replace(/\s+/g, ' ').slice(0, 50);
  const panel = q('[data-testid="inline-export-panel"]');
  const out: Record<string, unknown> = { htmlLang: document.documentElement.lang, darkClass: document.documentElement.classList.contains('dark'),
    accentProperty: getComputedStyle(document.documentElement).getPropertyValue('--cvf-accent-rgb').trim(), profile, lang, panelPresent: !!panel };
  out.documentOverflow = { scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth,
    overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1 };
  if (!panel) return out;
  out.panelRect = rect(panel);
  out.panelOverflow = { scrollWidth: panel.scrollWidth, clientWidth: panel.clientWidth, overflowX: panel.scrollWidth > panel.clientWidth + 1 };
  const controls = Array.from(panel.querySelectorAll('button,input,textarea,select,summary,a[href]')).filter(el => vis(el) && !el.closest('details:not([open]) > :not(summary)')) as HTMLElement[];
  const list = controls.map(el => ({ name: nameOf(el), tag: el.tagName.toLowerCase(), testid: el.getAttribute('data-testid'), r: rect(el) }));
  out.controlCount = list.length;
  out.outsideViewport = list.filter(c => c.r.x < -1 || c.r.right > vw + 1).map(c => ({ name: c.name, x: c.r.x, right: c.r.right }));
  const overlaps: string[] = [];
  for (let i = 0; i < list.length; i += 1) for (let j = i + 1; j < list.length; j += 1) {
    const a = list[i].r; const b = list[j].r;
    const w = Math.min(a.right, b.right) - Math.max(a.x, b.x); const h = Math.min(a.bottom, b.bottom) - Math.max(a.y, b.y);
    if (w > 2 && h > 2) overlaps.push(`${list[i].name} x ${list[j].name}`);
  }
  out.overlaps = overlaps;
  const toggle = Array.from(document.querySelectorAll('#tour-lang-switch button')).find(vis) as HTMLElement | undefined;
  const recordButton = q(`[data-testid="export-record-${profile === 'selected' ? 'ncr-synthetic-ux-job-001' : 'ux-generic-audit-001'}"]`);
  const build = controls.find(el => el.tagName === 'BUTTON' && /^(Build HTML|Tạo HTML|Generating|Đang tạo)$/.test(nameOf(el)));
  const targets: { label: string; w: number; h: number; heightMeets44: boolean; widthMeets44: boolean }[] = [];
  const missing: string[] = [];
  const addTarget = (label: string, el: HTMLElement | undefined | null) => {
    if (!el) { missing.push(label); return; }
    const r = rect(el); targets.push({ label, w: r.w, h: r.h, heightMeets44: r.h >= 43.99, widthMeets44: r.w >= 43.99 });
  };
  addTarget('Language toggle', toggle); addTarget('Record export button', recordButton); addTarget('Build', build);
  for (const [label, source, selectedOnly] of named) {
    if (selectedOnly && profile !== 'selected') continue;
    addTarget(label, controls.find(el => new RegExp(source).test(nameOf(el))));
  }
  out.targets = targets; out.missingTargets = missing;
  out.toggleRect = toggle ? rect(toggle) : null; out.recordButtonRect = recordButton ? rect(recordButton) : null;
  out.recordButtonInViewport = recordButton ? rect(recordButton).x >= 0 && rect(recordButton).right <= vw + 1 : null;
  const add = controls.find(el => /^(Add criterion|Thêm tiêu chí)$/.test(nameOf(el)));
  if (add) out.addCriterionLook = { disabled: (add as HTMLButtonElement).disabled, ...styleOf(add) };
  const disclosure = q('[data-testid="pre-generate-disclosure"]', panel);
  if (disclosure) {
    const d = rect(disclosure); const b = build ? rect(build) : null;
    let clipped = false;
    for (let a = disclosure.parentElement; a && a !== document.body; a = a.parentElement) {
      const cs = getComputedStyle(a); const ar = a.getBoundingClientRect();
      if (cs.overflowX !== 'visible' && (d.right > ar.right + 1 || d.x < ar.left - 1)) clipped = true;
    }
    out.disclosure = { text: disclosure.innerText.replace(/\s+/g, ' ').trim(), rect: d, buildRect: b,
      aboveBuild: b ? d.bottom <= b.y + 1 : null, domOrderBeforeBuild: build ? !!(disclosure.compareDocumentPosition(build) & Node.DOCUMENT_POSITION_FOLLOWING) : null,
      textClipped: disclosure.scrollHeight > disclosure.clientHeight + 1 || disclosure.scrollWidth > disclosure.clientWidth + 1, clippedByAncestor: clipped };
  }
  const pills = Array.from(panel.querySelectorAll('span')).filter(el => el.className.includes('rounded-full') && el.className.includes('border')).map(el => (el as HTMLElement).innerText.trim());
  out.pills = pills;
  const lines = panel.innerText.split('\n').map(s => s.trim()).filter(Boolean);
  out.visibleLineCount = lines.length;
  // Informational only: lines with no Vietnamese diacritic while the UI is Vietnamese (identifiers and acronyms excluded).
  out.possiblyUntranslated = lang === 'vi' ? lines.filter(s => s.length > 3 && !/[^\x00-\x7f]/.test(s) && /[a-z]{4,}/.test(s) && !/[/#_.:-]/.test(s)).slice(0, 12) : [];
  return out;
};

const DESCRIBE_FOCUS = () => {
  const styleOf = (el: Element) => {
    const cs = getComputedStyle(el);
    return { outlineStyle: cs.outlineStyle, outlineWidth: cs.outlineWidth, outlineColor: cs.outlineColor, outlineOffset: cs.outlineOffset, boxShadow: cs.boxShadow,
      borderColor: cs.borderTopColor, borderWidth: cs.borderTopWidth, borderStyle: cs.borderTopStyle, background: cs.backgroundColor, opacity: cs.opacity, cursor: cs.cursor };
  };
  const el = document.activeElement as HTMLElement | null;
  if (!el || el === document.body) return { tag: 'body', name: '', rect: null };
  const r = el.getBoundingClientRect();
  return { tag: el.tagName.toLowerCase(), type: (el as HTMLInputElement).type ?? null, id: el.id || null,
    name: (el.getAttribute('aria-label') || el.innerText || el.getAttribute('title') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
    testid: el.getAttribute('data-testid'), inLangSwitch: !!el.closest('#tour-lang-switch'), inPanel: !!el.closest('[data-testid="inline-export-panel"]'),
    focusVisible: el.matches(':focus-visible'), style: styleOf(el),
    rect: { x: Math.round(r.x * 10) / 10, y: Math.round(r.y * 10) / 10, w: Math.round(r.width * 10) / 10, h: Math.round(r.height * 10) / 10 },
    inViewport: r.top >= 0 && r.left >= 0 && r.bottom <= window.innerHeight + 0.5 && r.right <= window.innerWidth + 0.5, scrollY: Math.round(window.scrollY * 10) / 10 };
};

// Bounded polling until scroll offsets, the target rect and its computed focus styles are identical over consecutive animation frames.
const SETTLE = ({ selector, frames, deadlineMs }: { selector: string | null; frames: number; deadlineMs: number }) => new Promise<{ settled: boolean; attempts: number; ms: number }>(resolve => {
  const begin = performance.now(); let stable = 0; let last = ''; let attempts = 0;
  const tick = () => {
    attempts += 1;
    const target = selector ? document.querySelector(selector) : document.activeElement;
    const r = target ? target.getBoundingClientRect() : null;
    const cs = target ? getComputedStyle(target) : null;
    const sig = [Math.round(window.scrollX * 10), Math.round(window.scrollY * 10), r ? Math.round(r.x * 10) : 0, r ? Math.round(r.y * 10) : 0,
      cs ? `${cs.outlineStyle}|${cs.outlineWidth}|${cs.outlineColor}|${cs.borderTopColor}|${cs.backgroundColor}|${cs.boxShadow}` : ''].join(',');
    stable = sig === last ? stable + 1 : 0; last = sig;
    const ms = Math.round(performance.now() - begin);
    if (stable >= frames) return resolve({ settled: true, attempts, ms });
    if (ms > deadlineMs) return resolve({ settled: false, attempts, ms });
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
});
const SETTLE_STYLE = (el: Element, [frames, deadlineMs]: [number, number]) => new Promise<{ style: Record<string, string>; settled: boolean }>(resolve => {
  const begin = performance.now(); let stable = 0; let last = '';
  const read = () => {
    const cs = getComputedStyle(el);
    return { outlineStyle: cs.outlineStyle, outlineWidth: cs.outlineWidth, outlineColor: cs.outlineColor, outlineOffset: cs.outlineOffset, boxShadow: cs.boxShadow,
      borderColor: cs.borderTopColor, borderWidth: cs.borderTopWidth, borderStyle: cs.borderTopStyle, background: cs.backgroundColor, opacity: cs.opacity, cursor: cs.cursor };
  };
  const tick = () => {
    const style = read(); const sig = JSON.stringify(style);
    stable = sig === last ? stable + 1 : 0; last = sig;
    if (stable >= frames) return resolve({ style, settled: true });
    if (performance.now() - begin > deadlineMs) return resolve({ style, settled: false });
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
});

test('resulting-source UX verification: 44px targets, visible focus, skip link, language and settled validation on the real UI', async ({ page, context, browser }: any) => {
  test.setTimeout(780_000);
  expect(browser.browserType().name()).toBe('chromium');
  const traffic: { method: string; host: string; path: string; decision: string; nav?: boolean; status?: number }[] = [];
  const rowOf = new Map<unknown, (typeof traffic)[number]>();
  // The no-write fence is installed before any navigation or login.
  await context.route('**/*', async (route: any) => {
    const req = route.request(); const url = new URL(req.url()); const method = req.method();
    const row = { method, host: url.hostname, path: url.pathname, decision: '', nav: req.isNavigationRequest() };
    traffic.push(row); rowOf.set(req, row);
    if (!LOOPBACK.has(url.hostname)) { row.decision = 'blocked-external'; return route.abort(); }
    if (/^\/api\/(governance\/evaluate|execute)(\/|$)/.test(url.pathname)) { row.decision = 'blocked-effect'; return route.abort(); }
    if (method === 'GET' && url.pathname === '/api/admin/audit') {
      row.decision = 'fixture'; return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ success: true, data: AUDIT_FIXTURE }) });
    }
    if (!['GET', 'HEAD', 'OPTIONS'].includes(method)) { row.decision = url.pathname.startsWith('/api/auth/') ? 'blocked-auth-write' : 'blocked-write'; return route.abort(); }
    row.decision = 'allowed'; return route.continue();
  });
  context.on('response', (r: any) => { const row = rowOf.get(r.request()); if (row) row.status = r.status(); });

  // Observe the existing loginAs APIRequestContext calls by method/path/status only (no form values, no headers).
  const authApi: { method: string; path: string; status: number }[] = [];
  for (const m of ['get', 'post'] as const) {
    const original = (page.request as any)[m].bind(page.request);
    (page.request as any)[m] = async (target: string, options?: unknown) => {
      const response = await original(target, options);
      authApi.push({ method: m.toUpperCase(), path: new URL(target, 'http://localhost:3033').pathname, status: response.status() });
      return response;
    };
  }

  // Onboarding/setup preferences and empty, disabled providers only. No key material.
  await page.addInitScript(() => {
    localStorage.setItem('cvf_settings', JSON.stringify({
      providers: { gemini: { apiKey: '', enabled: false, selectedModel: 'gemini-2.5-flash' }, openai: { apiKey: '', enabled: false, selectedModel: 'gpt-4o' },
        anthropic: { apiKey: '', enabled: false, selectedModel: 'claude-sonnet-4-20250514' } },
      preferences: { defaultProvider: 'gemini', defaultExportMode: 'simple', defaultLanguage: 'vi', autoSaveHistory: true, showWelcomeTour: false } }));
    localStorage.setItem('cvf_onboarding_complete', 'true'); localStorage.setItem('cvf_onboarding_seen', '1'); localStorage.setItem('cvf_setup_banner_dismissed', 'true');
  });
  await loginAs(page, process.env.CVF_ADMIN_USER as string, process.env.CVF_ADMIN_PASS as string);

  const rows: any[] = []; const keyboard: any[] = []; const novice: any[] = []; const shots: { id: string; kind: string; file: string; bytes: number; sha256: string }[] = [];
  const settleLog: { where: string; settled: boolean; attempts: number; ms: number }[] = [];
  const validation: any = { activations: 0 };
  const screens = path.join(RUN_ROOT, 'ux-repair-screens'); fs.mkdirSync(screens, { recursive: true });
  const html = page.locator('html');
  const toggle = page.locator('#tour-lang-switch button:visible');
  const panel = page.getByTestId('inline-export-panel');
  const settle = async (where: string, selector: string | null = null) => {
    const result = await page.evaluate(SETTLE, { selector, frames: 10, deadlineMs: 4000 });
    settleLog.push({ where, ...result }); return result;
  };
  const shot = async (id: string, kind: string, target: 'page' | 'panel' = 'page') => {
    if (shots.length >= 24) throw new Error('SCREENSHOT_CAP');
    const file = path.join(screens, `${id}.png`);
    if (target === 'panel') await panel.screenshot({ path: file, animations: 'disabled' }); else await page.screenshot({ path: file, animations: 'disabled' });
    const bytes = fs.readFileSync(file);
    shots.push({ id, kind, file: path.relative(RUN_ROOT, file).replaceAll('\\', '/'), bytes: bytes.length, sha256: crypto.createHash('sha256').update(bytes).digest('hex') });
  };
  const useLang = async (lang: 'en' | 'vi') => {
    if ((await html.getAttribute('lang')) === lang) return;
    await expect(toggle).toHaveCount(1); await toggle.click(); await expect(html).toHaveAttribute('lang', lang);
  };
  const openRecord = async (id: string) => {
    await page.getByTestId(`export-record-${id}`).click(); await expect(panel).toBeVisible();
    if (id === SELECTED) await expect(page.getByTestId('html-job-controls')).toBeVisible();
  };
  const closeRecord = async (id: string) => { await page.getByTestId(`export-record-${id}`).click(); await expect(panel).toHaveCount(0); };
  const domainWrites = () => traffic.filter(t => t.decision === 'blocked-write').length;
  const authWrites = () => traffic.filter(t => t.decision === 'blocked-auth-write').length;
  const measure = async (rowId: string, profile: 'selected' | 'generic', lang: 'en' | 'vi', vp: any, th: any) => {
    const row: any = { rowId, profile, viewportName: vp.name, language: lang, theme: th.name, viewport: { w: vp.width, h: vp.height } };
    try {
      const c = COPY[lang];
      // Bring the disclosure to the middle first and let smooth scrolling finish; measurement never scrolls.
      await panel.getByTestId('pre-generate-disclosure').evaluate((el: HTMLElement) => el.scrollIntoView({ block: 'center' }));
      const s = await settle(`${rowId}:disclosure`, '[data-testid="pre-generate-disclosure"]'); row.settle = s;
      const m: any = await page.evaluate(MEASURE, { profile, lang, vw: vp.width, vh: vp.height, named: NAMED_FIELDS });
      Object.assign(row, m);
      const d = m.disclosure?.rect; row.disclosureInViewportAfterSettle = !!d && d.x >= 0 && d.right <= vp.width + 1 && d.y >= 0 && d.bottom <= vp.height + 1;
      const visibleLabels: Record<string, boolean> = {};
      const labelChecks: [string, any][] = [['Build', panel.getByRole('button', { name: c.build, exact: true })], ['Title', panel.getByRole('textbox', { name: c.title, exact: true })],
        ['Source reference', panel.getByRole('textbox', { name: c.source, exact: true })]];
      if (profile === 'selected') labelChecks.push(['Goal', panel.getByRole('textbox', { name: c.goal, exact: true })], ['Criterion 1', panel.getByRole('textbox', { name: c.criterion, exact: true })],
        ['Add criterion', panel.getByRole('button', { name: c.add, exact: true })], ['Section label', panel.locator(`[aria-label="${c.section}"]`)]);
      for (const [label, loc] of labelChecks) visibleLabels[label] = await loc.first().isVisible();
      row.ownedLabelsVisible = visibleLabels;
      row.ownedLabelsMissing = Object.entries(visibleLabels).filter(([, v]) => !v).map(([k]) => k);
      const text: string = m.disclosure?.text ?? '';
      const expected = profile === 'selected' ? c.selected : c.generic;
      row.disclosureFragmentsMissing = expected.filter(f => !text.includes(f));
      row.disclosureWrongProfile = profile === 'generic' ? (text.includes(COPY.en.selected[0]) || text.includes(COPY.vi.selected[0])) : (text.includes(COPY.en.generic[0]) || text.includes(COPY.vi.generic[0]));
      row.htmlLangMatches = m.htmlLang === lang;
      row.candidateShown = (m.pills ?? []).includes(c.candidate);
      row.candidateOtherLanguageShown = (m.pills ?? []).includes(lang === 'vi' ? COPY.en.candidate : COPY.vi.candidate);
      row.themeMatches = m.darkClass === (th.theme === 'dark') && m.accentProperty === th.rgb;
    } catch (error) { row.error = String((error as Error).message ?? error).slice(0, 300); }
    rows.push(row); return row;
  };

  const seedTheme = async (th: any) => {
    await page.evaluate(({ theme, accent }: { theme: string; accent: string }) => {
      localStorage.setItem('cvf_theme', theme); localStorage.setItem('cvf_ui_tweaks', JSON.stringify({ accent, radius: 14, density: 'normal' }));
    }, { theme: th.theme, accent: th.accent });
  };

  // Rows follow the locked order: viewport x theme; per combination 4 rows (selected EN/VI, generic VI/EN) and one keyboard pass.
  let comboIndex = 0;
  for (const vp of VIEWPORTS) {
    for (const th of THEMES) {
      const combo = `${vp.name}-${th.name}`; const first = comboIndex === 0; comboIndex += 1;
      const setup: any = { combo, themeAsserted: false };
      try {
        await seedTheme(th);
        await page.setViewportSize({ width: vp.width, height: vp.height });
        await page.goto('/work-transfer', { waitUntil: 'domcontentloaded', timeout: 120_000 });
        await expect(page.getByTestId('history-list')).toBeVisible({ timeout: 120_000 });
        await page.waitForFunction((rgb: string) => getComputedStyle(document.documentElement).getPropertyValue('--cvf-accent-rgb').trim() === rgb, th.rgb);
        await page.waitForFunction((dark: boolean) => document.documentElement.classList.contains('dark') === dark, th.theme === 'dark');
        setup.themeAsserted = true;
      } catch (error) { setup.error = String((error as Error).message ?? error).slice(0, 300); }
      await useLang('en').catch(() => undefined);

      // Selected (ncr-synthetic) profile: EN then VI through the real visible toggle, literal user text carried across.
      const literal = { goal: 'ncr-synthetic literal goal 001', criterion: 'ncr-synthetic literal criterion', title: 'NCR literal title 001' };
      try {
        await openRecord(SELECTED);
        await measure(`selected-${combo}-en`, 'selected', 'en', vp, th);
        await panel.getByRole('textbox', { name: COPY.en.goal, exact: true }).fill(literal.goal);
        await panel.getByRole('textbox', { name: COPY.en.criterion, exact: true }).fill(literal.criterion);
        await panel.getByRole('textbox', { name: COPY.en.title, exact: true }).fill(literal.title);
        await useLang('vi');
        const literalPreserved = { checked: true,
          goal: (await panel.getByRole('textbox', { name: COPY.vi.goal, exact: true }).inputValue()) === literal.goal,
          criterion: (await panel.getByRole('textbox', { name: COPY.vi.criterion, exact: true }).inputValue()) === literal.criterion,
          title: (await panel.getByRole('textbox', { name: COPY.vi.title, exact: true }).inputValue()) === literal.title };
        const r = await measure(`selected-${combo}-vi`, 'selected', 'vi', vp, th); r.literalPreserved = literalPreserved;
        if (vp.name === 'desktop') {
          await panel.evaluate((el: HTMLElement) => el.scrollIntoView({ block: 'start' })); await settle(`${combo}:full-panel`, '[data-testid="inline-export-panel"]');
          await shot(`full-panel-vi-${th.name}`, 'representative-vi-selected-full-panel', 'panel');
        }
        if (vp.name === 'mobile' && th.name === 'dark-indigo') {
          // The ONE invalid Build activation of the whole run: selected profile, mobile, VI, dark+indigo, empty goal, keyboard Enter.
          await panel.getByRole('textbox', { name: COPY.vi.goal, exact: true }).fill('');
          let reachedBuild = false;
          for (let i = 0; i < 20 && !reachedBuild; i += 1) {
            await page.keyboard.press('Tab'); await settle(`validation-tab-${i}`);
            const info: any = await page.evaluate(DESCRIBE_FOCUS); reachedBuild = info.inPanel && info.tag === 'button' && info.name === COPY.vi.build;
          }
          validation.reachedBuildByKeyboard = reachedBuild;
          if (reachedBuild) {
            const before = domainWrites() + authWrites();
            validation.activations += 1; validation.activationContext = { profile: 'selected', viewport: vp.name, language: 'vi', theme: th.name, key: 'Enter', goalEmpty: true };
            await page.keyboard.press('Enter');
            const message = page.getByTestId('export-error-recovery');
            await message.waitFor({ state: 'visible', timeout: 8000 }).catch(() => undefined);
            await settle('validation-message', '[data-testid="export-error-recovery"]');
            const text = ((await message.textContent().catch(() => '')) ?? '').trim();
            const geometry: any = await page.evaluate(() => {
              const el = document.querySelector('[data-testid="export-error-recovery"]') as HTMLElement | null;
              if (!el) return null;
              const box = (el.closest('.text-red-700, [class*="border-red"]') ?? el) as HTMLElement;
              const r = box.getBoundingClientRect();
              let clipped = false;
              for (let a = box.parentElement; a && a !== document.body; a = a.parentElement) {
                const cs = getComputedStyle(a); const ar = a.getBoundingClientRect();
                if ((cs.overflowX !== 'visible' || cs.overflowY !== 'visible') && (r.right > ar.right + 1 || r.left < ar.left - 1 || r.bottom > ar.bottom + 1 || r.top < ar.top - 1)) clipped = true;
              }
              return { rect: { x: r.x, y: r.y, w: r.width, h: r.height, bottom: r.bottom, right: r.right }, inViewport: r.top >= 0 && r.left >= 0 && r.bottom <= window.innerHeight + 0.5 && r.right <= window.innerWidth + 0.5,
                clippedByAncestor: clipped, textClipped: box.scrollHeight > box.clientHeight + 1 || box.scrollWidth > box.clientWidth + 1 };
            });
            Object.assign(validation, { text, expectedText: COPY.vi.validation, matchesExpected: text === COPY.vi.validation, geometry,
              domainWriteAttemptsCaused: domainWrites() + authWrites() - before });
            await shot('mobile-validation-vi-dark-indigo', 'settled-mobile-validation');
            await page.keyboard.press('Tab'); await settle('validation-away');
            const away: any = await page.evaluate(DESCRIBE_FOCUS);
            await page.keyboard.press('Shift+Tab'); await settle('validation-back');
            const back: any = await page.evaluate(DESCRIBE_FOCUS);
            validation.focusMovedAway = !(away.inPanel && away.tag === 'button' && away.name === COPY.vi.build); validation.focusReturned = back.inPanel && back.tag === 'button' && back.name === COPY.vi.build;
          }
        }
        const before = domainWrites();
        await closeRecord(SELECTED);
        if (first) novice.push({ profile: 'selected', viewport: vp.name, language: 'vi', theme: th.name, explanationExcerpt: String((r as any).disclosure?.text ?? '').slice(0, 220),
          action: 'left the panel without Build', domainWriteAttemptsDuring: domainWrites() - before, panelClosed: true });
      } catch (error) { rows.push({ rowId: `selected-${combo}`, error: String((error as Error).message ?? error).slice(0, 300) }); await page.getByTestId(`export-record-${SELECTED}`).click({ timeout: 2000 }).catch(() => undefined); }

      // Generic (non ncr-synthetic) profile: VI then EN.
      try {
        await openRecord(GENERIC);
        await measure(`generic-${combo}-vi`, 'generic', 'vi', vp, th);
        await useLang('en');
        const r = await measure(`generic-${combo}-en`, 'generic', 'en', vp, th);
        const before = domainWrites();
        await closeRecord(GENERIC);
        if (first) novice.push({ profile: 'generic', viewport: vp.name, language: 'en', theme: th.name, explanationExcerpt: String((r as any).disclosure?.text ?? '').slice(0, 220),
          action: 'left the panel without Build', domainWriteAttemptsDuring: domainWrites() - before, panelClosed: true });
      } catch (error) { rows.push({ rowId: `generic-${combo}`, error: String((error as Error).message ?? error).slice(0, 300) }); await page.getByTestId(`export-record-${GENERIC}`).click({ timeout: 2000 }).catch(() => undefined); }

      // Real keyboard pass (selected profile, EN): skip link, language toggle, main, record button, panel fields, Build, leave and return.
      const kb: any = { combo, viewport: vp.name, theme: th.name, setup, stops: [] as any[], found: {} as Record<string, number | null>, sequence: [] as string[] };
      try {
        await useLang('en');
        await page.goto('/work-transfer', { waitUntil: 'domcontentloaded', timeout: 120_000 });
        await expect(page.getByTestId('history-list')).toBeVisible({ timeout: 120_000 });
        let prev: any = null; let count = 0; let sinceMain = 0; let sawMain = false;
        const record = async (info: any, key: string) => {
          info.seq = count; info.key = key;
          if (prev) { const handle = prev; prev = null; const blurred = await handle.evaluate(SETTLE_STYLE, [10, 2000]).catch(() => null); const last = kb.stops[kb.stops.length - 1]; last.blurred = blurred?.style ?? null; last.blurredSettled = blurred?.settled ?? false; }
          kb.stops.push(info); kb.sequence.push(`${key}:${info.tag}${info.id ? '#' + info.id : ''}${info.testid ? '[' + info.testid + ']' : ''}:${info.name}`);
          prev = await page.evaluateHandle(() => document.activeElement); return info;
        };
        const press = async (key: string) => {
          await page.keyboard.press(key); count += 1; if (sawMain && key === 'Tab') sinceMain += 1;
          const s = await settle(`${combo}:kb${count}:${key}`);
          const info: any = await page.evaluate(DESCRIBE_FOCUS); info.settle = s; return record(info, key);
        };
        const until = async (label: string, test: (i: any) => boolean, cap: number, key = 'Tab') => {
          for (let i = 0; i < cap; i += 1) { const info = await press(key); if (test(info)) { kb.found[label] = key === 'Tab' ? (sawMain ? sinceMain : count) : count; return info; } }
          kb.found[label] = null; return null;
        };
        const isSkip = (i: any) => i.testid === 'skip-to-main';
        const skip = await until('skipLink', isSkip, 2);
        if (skip && first) await shot('skip-link-focused-desktop-dark-indigo', 'optional-skip-link');
        const tg = await until('languageToggle', i => i.inLangSwitch, 8);
        if (tg) {
          await shot(`focused-toggle-${combo}`, 'focused-toggle');
          await page.keyboard.press('Enter'); await expect(html).toHaveAttribute('lang', 'vi'); kb.enterToggledToVi = true;
          await page.keyboard.press('Space'); await expect(html).toHaveAttribute('lang', 'en'); kb.spaceToggledToEn = true;
        }
        const back = await press('Shift+Tab'); kb.shiftTabReturnedToSkip = isSkip(back);
        if (kb.shiftTabReturnedToSkip) {
          await page.keyboard.press('Enter'); count += 1;
          const s = await settle(`${combo}:skip-enter`);
          const info: any = await page.evaluate(DESCRIBE_FOCUS); info.settle = s; await record(info, 'Enter');
          kb.enterLandedOnMain = info.id === 'cvf-dashboard-main' && info.tag === 'main'; sawMain = kb.enterLandedOnMain === true; sinceMain = 0;
          if (first && kb.enterLandedOnMain) await shot('skip-main-landed-desktop-dark-indigo', 'optional-skip-link');
        }
        const rec = await until('recordButton', i => i.testid === `export-record-${SELECTED}`, 20);
        if (rec) { await page.keyboard.press('Enter'); await expect(page.getByTestId('html-job-controls')).toBeVisible(); kb.enterOpenedPanel = true; }
        await until('goal', i => i.inPanel && i.name === COPY.en.goal, 4);
        await until('criterion1', i => i.inPanel && i.name === COPY.en.criterion, 3);
        await until('addCriterion', i => i.inPanel && i.name === COPY.en.add, 3);
        const field = await until('panelField', i => i.inPanel && i.name === COPY.en.title, 3);
        if (field) await shot(`focused-field-${combo}`, 'focused-field');
        const bd = await until('build', i => i.inPanel && i.tag === 'button' && i.name === COPY.en.build, 12);
        if (bd) {
          const up = await press('Shift+Tab'); const down = await press('Tab');
          kb.backAndForthReturnedToBuild = down.name === COPY.en.build && !!up;
          const away = await press('Tab'); const returned = await press('Shift+Tab');
          kb.focusMovedAway = away.name !== COPY.en.build || away.tag !== 'button'; kb.focusReturnable = returned.name === COPY.en.build;
        }
        await closeRecord(SELECTED).catch(() => undefined);
        kb.tabsAndKeysUsed = count;
      } catch (error) { kb.error = String((error as Error).message ?? error).slice(0, 300); }
      keyboard.push(kb);
      fs.writeFileSync(path.join(RUN_ROOT, 'ux-repair-partial.json'), JSON.stringify({ combosDone: comboIndex, rows, keyboard, validation, shots, settleCount: settleLog.length, domainWrites: domainWrites(), authWrites: authWrites() }));
    }
  }

  // Consolidate objective criteria. Conformance verdicts are derived from measurements; evidence is written regardless.
  const ok = rows.filter(r => !r.error);
  const isRow = (r: any) => r.panelPresent !== undefined;
  const measured = ok.filter(isRow);
  const accentCss = (name: string) => THEMES.find(t => t.name === name)!.css;
  const STOP_NAMES = new Set<string>([COPY.en.goal, COPY.en.criterion, COPY.en.add, COPY.en.title, COPY.en.source, 'Record type', 'Review status', 'Receipt reference', 'Review boundary', 'Source notes', COPY.en.build]);
  const NAMED_STOP = (s: any) => s.key !== 'Enter' && (s.testid === 'skip-to-main' || s.inLangSwitch || s.testid === `export-record-${SELECTED}` || (s.inPanel && STOP_NAMES.has(s.name)));
  const focusOk = (s: any, kb: any) => !!s.style && s.style.outlineStyle !== 'none' && parseFloat(s.style.outlineWidth) >= 2 && s.style.outlineColor === accentCss(kb.theme) && s.focusVisible === true
    && (s.blurred === undefined || (s.blurred !== null && (s.blurred.outlineStyle === 'none' || parseFloat(s.blurred.outlineWidth) === 0)));
  const focusFailures: string[] = []; const settleFailures = settleLog.filter(s => !s.settled).map(s => s.where);
  for (const kb of keyboard) for (const s of kb.stops ?? []) {
    if (NAMED_STOP(s) && !focusOk(s, kb)) focusFailures.push(`${kb.combo}#${s.seq}:${s.name || s.tag}`);
  }
  const stopsOutsideViewport = keyboard.flatMap(kb => (kb.stops ?? []).filter((s: any) => NAMED_STOP(s) && s.inViewport === false).map((s: any) => `${kb.combo}#${s.seq}:${s.name}`));
  const criteria = {
    rows36: { expected: 36, completed: measured.length, errors: rows.filter(r => r.error).length, pass: measured.length === 36 && rows.every(r => !r.error) },
    themeAsserted: { failing: measured.filter(r => !r.themeMatches).map(r => r.rowId), pass: measured.length === 36 && measured.every(r => r.themeMatches) },
    targets44: { failing: measured.filter(r => r.missingTargets?.length || r.targets?.some((t: any) => !t.heightMeets44 || (t.label === 'Language toggle' && !t.widthMeets44))).map(r => ({ id: r.rowId,
      missing: r.missingTargets, short: r.targets.filter((t: any) => !t.heightMeets44 || (t.label === 'Language toggle' && !t.widthMeets44)).map((t: any) => `${t.label}:${t.w}x${t.h}`) })),
      pass: measured.length === 36 && measured.every(r => !r.missingTargets?.length && r.targets.every((t: any) => t.heightMeets44 && (t.label !== 'Language toggle' || t.widthMeets44))) },
    containment: { failing: measured.filter(r => r.documentOverflow?.overflowX || r.panelOverflow?.overflowX || r.outsideViewport?.length || r.overlaps?.length || r.recordButtonInViewport === false).map(r => r.rowId),
      pass: measured.length === 36 && measured.every(r => !r.documentOverflow?.overflowX && !r.panelOverflow?.overflowX && !r.outsideViewport?.length && !r.overlaps?.length && r.recordButtonInViewport !== false) },
    disclosure: { failing: measured.filter(r => !r.disclosure || r.disclosure.domOrderBeforeBuild === false || r.disclosure.aboveBuild === false || r.disclosure.textClipped || r.disclosure.clippedByAncestor
      || r.disclosureFragmentsMissing?.length || r.disclosureWrongProfile || !r.disclosureInViewportAfterSettle).map(r => r.rowId),
      pass: measured.length === 36 && measured.every(r => r.disclosure && r.disclosure.domOrderBeforeBuild !== false && r.disclosure.aboveBuild !== false && !r.disclosure.textClipped && !r.disclosure.clippedByAncestor
        && !r.disclosureFragmentsMissing?.length && !r.disclosureWrongProfile && r.disclosureInViewportAfterSettle) },
    labelsAndLanguage: { failing: measured.filter(r => r.ownedLabelsMissing?.length || r.htmlLangMatches === false || !r.candidateShown || r.candidateOtherLanguageShown).map(r => r.rowId),
      pass: measured.length === 36 && measured.every(r => !r.ownedLabelsMissing?.length && r.htmlLangMatches !== false && r.candidateShown && !r.candidateOtherLanguageShown) },
    literalPreserved: { failing: measured.filter(r => r.literalPreserved?.checked && !(r.literalPreserved.goal && r.literalPreserved.criterion && r.literalPreserved.title)).map(r => r.rowId),
      selectedSwitches: measured.filter(r => r.literalPreserved?.checked).length, pass: measured.filter(r => r.literalPreserved?.checked).length === 9 && measured.filter(r => r.literalPreserved?.checked).every(r => r.literalPreserved.goal && r.literalPreserved.criterion && r.literalPreserved.title) },
    addCriterionLooksLikeButton: { failing: measured.filter(r => r.addCriterionLook && !(parseFloat(r.addCriterionLook.borderWidth) >= 1 && r.addCriterionLook.borderStyle !== 'none' && r.addCriterionLook.background !== 'rgba(0, 0, 0, 0)')).map(r => r.rowId),
      pass: measured.filter(r => r.profile === 'selected').length === 18 && measured.filter(r => r.profile === 'selected').every(r => r.addCriterionLook && parseFloat(r.addCriterionLook.borderWidth) >= 1 && r.addCriterionLook.borderStyle !== 'none' && r.addCriterionLook.background !== 'rgba(0, 0, 0, 0)') },
    keyboard9: { passes: keyboard.length, errors: keyboard.filter(k => k.error).map(k => ({ combo: k.combo, error: k.error })),
      failing: keyboard.filter(k => k.error || (k.found.skipLink ?? 99) > 2 || !k.enterLandedOnMain || !k.shiftTabReturnedToSkip || k.found.languageToggle === null || !k.enterToggledToVi || !k.spaceToggledToEn
        || k.found.recordButton === null || (k.found.recordButton ?? 99) > 20 || !k.enterOpenedPanel || k.found.goal === null || k.found.criterion1 === null || k.found.addCriterion === null || k.found.panelField === null
        || k.found.build === null || !k.backAndForthReturnedToBuild || !k.focusMovedAway || !k.focusReturnable).map(k => k.combo),
      pass: keyboard.length === 9 && keyboard.every(k => !k.error && (k.found.skipLink ?? 99) <= 2 && k.enterLandedOnMain && k.shiftTabReturnedToSkip && k.found.languageToggle !== null && k.enterToggledToVi && k.spaceToggledToEn
        && k.found.recordButton !== null && (k.found.recordButton ?? 99) <= 20 && k.enterOpenedPanel && k.found.goal !== null && k.found.criterion1 !== null && k.found.addCriterion !== null && k.found.panelField !== null
        && k.found.build !== null && k.backAndForthReturnedToBuild && k.focusMovedAway && k.focusReturnable) },
    visibleFocusIndicator: { failing: focusFailures, pass: keyboard.length === 9 && focusFailures.length === 0 },
    focusedElementsInViewport: { failing: stopsOutsideViewport, pass: keyboard.length === 9 && stopsOutsideViewport.length === 0 },
    settled: { measurements: settleLog.length, failing: settleFailures, pass: settleFailures.length === 0 },
    validation: { activations: validation.activations, pass: validation.activations === 1 && validation.matchesExpected === true && validation.geometry?.inViewport === true && !validation.geometry?.clippedByAncestor
      && !validation.geometry?.textClipped && validation.domainWriteAttemptsCaused === 0 && validation.focusMovedAway === true && validation.focusReturned === true },
  };
  const attemptedDomainWrites = traffic.filter(t => t.decision === 'blocked-write');
  const attemptedAuthWrites = traffic.filter(t => t.decision === 'blocked-auth-write');
  const externalBlocked = traffic.filter(t => t.decision === 'blocked-external');
  const effectBlocked = traffic.filter(t => t.decision === 'blocked-effect');
  const callbackPosts = authApi.filter(a => a.method === 'POST');
  const boundary = {
    domainWriteAttempts: attemptedDomainWrites.length, browserAuthWriteAttempts: attemptedAuthWrites.length, effectBlocked: effectBlocked.length,
    externalBlockedHosts: [...new Set(externalBlocked.map(t => t.host))], externalBlockedCount: externalBlocked.length,
    loginFormFallback: traffic.some(t => t.path === '/login' && t.nav === true),
    apiRequestContext: authApi, callbackOnlyBootstrap: callbackPosts.length === 1 && callbackPosts[0].path === '/api/auth/callback/credentials' && authApi.every(a => a.path.startsWith('/api/auth/')),
    invalidBuildActivations: validation.activations,
    trafficCounts: traffic.reduce((m: Record<string, number>, t) => { m[t.decision] = (m[t.decision] ?? 0) + 1; return m; }, {}),
    note: 'Auth bootstrap used the existing loginAs helper (APIRequestContext), outside BrowserContext routing; observed by method/path/status only.',
  };
  const shotBytes = shots.reduce((n, s) => n + s.bytes, 0);
  const kinds = shots.reduce((m: Record<string, number>, s) => { m[s.kind] = (m[s.kind] ?? 0) + 1; return m; }, {});
  const summary = { criteria: Object.fromEntries(Object.entries(criteria).map(([k, v]: [string, any]) => [k, v.pass])), screenshots: shots.length, screenshotBytes: shotBytes, screenshotKinds: kinds,
    novicePasses: novice.length, boundary };
  const evidence = { schema: 'cvf.ncrR1UxFindingsRepairVerification.v1', browser: browser.version(), viewports: VIEWPORTS, themes: THEMES, rows, keyboard, validation, novice, criteria, shots, settleLog, summary,
    traffic: traffic.filter(t => t.path.startsWith('/api/') || t.method !== 'GET').map(({ method, path: p, decision, status }) => ({ method, path: p, decision, status })) };
  fs.writeFileSync(path.join(RUN_ROOT, 'ux-repair-assessment.json'), JSON.stringify(evidence, null, 2));
  console.log('NCR_R1_UX_REPAIR ' + JSON.stringify({ criteria: summary.criteria, screenshots: shots.length, screenshotBytes: shotBytes, kinds, boundary: { domainWriteAttempts: boundary.domainWriteAttempts,
    browserAuthWriteAttempts: boundary.browserAuthWriteAttempts, effectBlocked: boundary.effectBlocked, invalidBuildActivations: boundary.invalidBuildActivations, callbackOnlyBootstrap: boundary.callbackOnlyBootstrap } }));

  // Safety gates only; UX criteria are reported through the evidence file, never as a pass/fail of this test.
  expect(boundary.domainWriteAttempts).toBe(0);
  expect(boundary.browserAuthWriteAttempts).toBe(0);
  expect(boundary.effectBlocked).toBe(0);
  expect(boundary.loginFormFallback).toBe(false);
  expect(boundary.callbackOnlyBootstrap).toBe(true);
  expect(validation.activations).toBeLessThanOrEqual(1);
  expect(shots.length).toBeLessThanOrEqual(24);
  expect(shotBytes).toBeLessThanOrEqual(32 * 1024 * 1024);
});
