// Text Encoding Exception: Vietnamese UI copy is asserted verbatim as the real-browser language oracle.
// UI-only read assessment (AGENTS pure-UI exception): language switching, keyboard focus, viewport geometry and pre-effect/refusal
// explanation on the real running app. Zero domain-write attempts are allowed: every non-auth write is blocked and counted before it is
// sent. Findings are assessment outputs, not conformance claims. No provider, evaluate/execute, external network or private data.
import { createRequire } from 'node:module';
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
const AUDIT_FIXTURE = [
  { id: SELECTED, timestamp: '2026-10-18T02:00:00.000Z', action: 'ncr-synthetic selected job flow', actorId: 'ncr-synthetic-worker',
    actorRole: 'admin', targetResource: 'fixtures/ux-selected.md', outcome: 'SYNTHETIC_READY_FOR_REVIEW' },
  { id: GENERIC, timestamp: '2026-10-18T01:00:00.000Z', action: 'generic audit event', actorId: 'ux-generic-actor',
    actorRole: 'admin', targetResource: 'fixtures/ux-generic.md', outcome: 'RECORDED' },
];
const COPY = {
  en: { goal: 'Goal', criterion: 'Criterion 1', add: 'Add criterion', build: 'Build HTML', title: 'Title', source: 'Source reference', section: 'Local test HTML job',
    selected: ['local test profile', 'when you choose Save', 'no review receipt is requested', 'unverified and unaccepted', 'not trusted evidence or business acceptance',
      'Stop only acts on this page', 'does not confirm that a remote task stopped or determine cost'],
    generic: ['may send a short excerpt', 'depends on this deployment'], validation: 'Enter the goal and all criteria before building.' },
  vi: { goal: 'Mục tiêu', criterion: 'Tiêu chí 1', add: 'Thêm tiêu chí', build: 'Tạo HTML', title: 'Tiêu đề', source: 'Nguồn tham chiếu', section: 'Tác vụ HTML thử nghiệm cục bộ',
    selected: ['chế độ thử nghiệm cục bộ', 'khi bạn chọn Lưu', 'không có yêu cầu lấy biên nhận', 'chưa được xác minh và chưa được chấp nhận',
      'không phải bằng chứng đáng tin cậy hay sự chấp nhận trong nghiệp vụ', 'không xác nhận thao tác từ xa đã dừng', 'chi phí vẫn chưa rõ'],
    generic: ['có thể gửi một đoạn ngắn', 'phụ thuộc vào cấu hình triển khai'], validation: 'Hãy nhập mục tiêu và đầy đủ tiêu chí trước khi tạo HTML.' },
} as const;

// In-page measurement of the open inline panel. Pure DOM reads; nothing is activated.
const MEASURE = ({ profile, lang, vw, vh }: { profile: string; lang: string; vw: number; vh: number }) => {
  const q = (s: string, r: ParentNode = document) => r.querySelector(s) as HTMLElement | null;
  const vis = (el: Element) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const rect = (el: Element) => { const r = el.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height), right: Math.round(r.right), bottom: Math.round(r.bottom) }; };
  const nameOf = (el: HTMLElement) => (el.getAttribute('aria-label') || el.innerText || (el as HTMLInputElement).placeholder || el.getAttribute('title') || el.tagName).trim().replace(/\s+/g, ' ').slice(0, 50);
  const panel = q('[data-testid="inline-export-panel"]');
  const out: Record<string, unknown> = { htmlLang: document.documentElement.lang, profile, lang, viewport: { w: vw, h: vh }, panelPresent: !!panel };
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
  const find = (re: RegExp) => controls.find(el => re.test(nameOf(el)));
  const targets: [string, HTMLElement | undefined | null][] = [
    ['language toggle', toggle], ['record export button', recordButton], ['Build', controls.find(el => el.tagName === 'BUTTON' && /^(Build HTML|Tạo HTML|Generating|Đang tạo)$/.test(nameOf(el)))],
    ['Title field', find(/^(Title|Tiêu đề)$/)], ['Goal field', find(/^(Goal|Mục tiêu)$/)], ['Criterion 1 field', find(/^(Criterion 1|Tiêu chí 1)$/)],
    ['Add criterion', find(/^(Add criterion|Thêm tiêu chí)$/)],
  ];
  out.targets = targets.filter(([, el]) => el).map(([label, el]) => { const r = rect(el as HTMLElement);
    return { label, w: r.w, h: r.h, meets44: r.w >= 44 && r.h >= 44, heightMeets44: r.h >= 44 }; });
  const disclosure = q('[data-testid="pre-generate-disclosure"]', panel);
  const build = targets[2][1] as HTMLElement | undefined;
  if (disclosure) {
    disclosure.scrollIntoView({ block: 'center' });
    const d = rect(disclosure); const b = build ? rect(build) : null;
    let clipped = false;
    for (let a = disclosure.parentElement; a && a !== document.body; a = a.parentElement) {
      const cs = getComputedStyle(a); const ar = a.getBoundingClientRect();
      if (cs.overflowX !== 'visible' && (d.right > ar.right + 1 || d.x < ar.left - 1)) clipped = true;
    }
    out.disclosure = { text: disclosure.innerText.replace(/\s+/g, ' ').trim(), rect: d, buildRect: b,
      aboveBuild: b ? d.bottom <= b.y + 1 : null, domOrderBeforeBuild: build ? !!(disclosure.compareDocumentPosition(build) & Node.DOCUMENT_POSITION_FOLLOWING) : null,
      inViewportAfterScroll: d.x >= 0 && d.right <= vw + 1 && d.y >= 0 && d.bottom <= vh + 1,
      textClipped: disclosure.scrollHeight > disclosure.clientHeight + 1 || disclosure.scrollWidth > disclosure.clientWidth + 1, clippedByAncestor: clipped };
  }
  const lines = panel.innerText.split('\n').map(s => s.trim()).filter(Boolean);
  out.visibleLineCount = lines.length;
  // Informational only: lines with no Vietnamese diacritic while the UI is Vietnamese (identifiers and acronyms excluded).
  out.possiblyUntranslated = lang === 'vi' ? lines.filter(s => s.length > 3 && !/[^\x00-\x7f]/.test(s) && /[a-z]{4,}/.test(s) && !/[/#_.:-]/.test(s)).slice(0, 12) : [];
  return out;
};

const DESCRIBE_FOCUS = () => {
  const el = document.activeElement as HTMLElement | null;
  if (!el || el === document.body) return { tag: 'body', name: '', rect: null };
  const cs = getComputedStyle(el); const r = el.getBoundingClientRect();
  return { tag: el.tagName.toLowerCase(), type: (el as HTMLInputElement).type ?? null, role: el.getAttribute('role'), id: el.id || null,
    name: (el.getAttribute('aria-label') || el.innerText || el.getAttribute('title') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
    testid: el.getAttribute('data-testid'), inLangSwitch: !!el.closest('#tour-lang-switch'), inPanel: !!el.closest('[data-testid="inline-export-panel"]'),
    focusVisible: el.matches(':focus-visible'), outline: `${cs.outlineStyle} ${cs.outlineWidth} ${cs.outlineColor}`, boxShadow: cs.boxShadow,
    rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
    inViewport: r.top >= 0 && r.left >= 0 && r.bottom <= window.innerHeight && r.right <= window.innerWidth };
};
const STYLE_OF = (el: Element) => { const cs = getComputedStyle(el); return { outline: `${cs.outlineStyle} ${cs.outlineWidth} ${cs.outlineColor}`, boxShadow: cs.boxShadow }; };

test('read-only browser assessment: language, keyboard, geometry and pre-effect refusal on the real UI', async ({ page, context, browser }) => {
  test.setTimeout(600_000);
  expect(browser.browserType().name()).toBe('chromium');
  const traffic: { method: string; host: string; path: string; decision: string; status?: number }[] = [];
  const rowOf = new Map<unknown, (typeof traffic)[number]>();
  await context.route('**/*', async (route: any) => {
    const req = route.request(); const url = new URL(req.url()); const method = req.method();
    const row = { method, host: url.hostname, path: url.pathname, decision: '' };
    traffic.push(row); rowOf.set(req, row);
    if (!LOOPBACK.has(url.hostname)) { row.decision = 'blocked-external'; return route.abort(); }
    if (/^\/api\/(governance\/evaluate|execute)(\/|$)/.test(url.pathname)) { row.decision = 'blocked-effect'; return route.abort(); }
    if (method === 'GET' && url.pathname === '/api/admin/audit') {
      row.decision = 'fixture'; return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ success: true, data: AUDIT_FIXTURE }) });
    }
    if (!['GET', 'HEAD', 'OPTIONS'].includes(method)) {
      if (url.pathname.startsWith('/api/auth/')) { row.decision = 'auth-allowed'; return route.continue(); }
      row.decision = 'blocked-write'; return route.abort();
    }
    row.decision = 'allowed'; return route.continue();
  });
  context.on('response', (r: any) => { const row = rowOf.get(r.request()); if (row) row.status = r.status(); });

  // Onboarding/setup preferences and empty, disabled providers only. No key material.
  await page.addInitScript(() => {
    localStorage.setItem('cvf_settings', JSON.stringify({
      providers: { gemini: { apiKey: '', enabled: false, selectedModel: 'gemini-2.5-flash' }, openai: { apiKey: '', enabled: false, selectedModel: 'gpt-4o' },
        anthropic: { apiKey: '', enabled: false, selectedModel: 'claude-sonnet-4-20250514' } },
      preferences: { defaultProvider: 'gemini', defaultExportMode: 'simple', defaultLanguage: 'vi', autoSaveHistory: true, showWelcomeTour: false } }));
    localStorage.setItem('cvf_onboarding_complete', 'true'); localStorage.setItem('cvf_onboarding_seen', '1'); localStorage.setItem('cvf_setup_banner_dismissed', 'true');
  });
  await loginAs(page, process.env.CVF_ADMIN_USER as string, process.env.CVF_ADMIN_PASS as string);

  const rows: any[] = []; const keyboard: any[] = []; const novice: any[] = []; const shots: { id: string; file: string; bytes: number }[] = [];
  const screens = path.join(RUN_ROOT, 'ux-screens'); fs.mkdirSync(screens, { recursive: true });
  const html = page.locator('html');
  const toggle = page.locator('#tour-lang-switch button:visible');
  const panel = page.getByTestId('inline-export-panel');
  const shot = async (id: string) => {
    if (shots.length >= 12) return;
    await page.screenshot({ path: path.join(screens, `${id}.png`), animations: 'disabled' });
    const file = path.join(screens, `${id}.png`); shots.push({ id, file: path.relative(RUN_ROOT, file).replaceAll('\\', '/'), bytes: fs.statSync(file).size });
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
  const writes = () => traffic.filter(t => t.decision === 'blocked-write').length;
  const measure = async (rowId: string, profile: 'selected' | 'generic', lang: 'en' | 'vi', vp: any, shotId?: string) => {
    const row: any = { rowId, profile, viewportName: vp.name, language: lang };
    try {
      const c = COPY[lang];
      const m: any = await page.evaluate(MEASURE, { profile, lang, vw: vp.width, vh: vp.height });
      Object.assign(row, m);
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
      row.disclosureWrongProfile = profile === 'generic' ? (COPY.en.selected[0] && (text.includes(COPY.en.selected[0]) || text.includes(COPY.vi.selected[0]))) : (text.includes(COPY.en.generic[0]) || text.includes(COPY.vi.generic[0]));
      row.htmlLangMatches = m.htmlLang === lang;
      if (shotId) { await panel.scrollIntoViewIfNeeded(); await shot(shotId); row.screenshot = shotId; }
    } catch (error) { row.error = String((error as Error).message ?? error).slice(0, 300); }
    rows.push(row); return row;
  };

  for (const vp of VIEWPORTS) {
    await page.setViewportSize({ width: vp.width, height: vp.height });
    await page.goto('/work-transfer', { waitUntil: 'domcontentloaded', timeout: 120_000 });
    await expect(page.getByTestId('history-list')).toBeVisible({ timeout: 120_000 });
    await useLang('en');
    // Selected (ncr-synthetic) profile, EN then VI through the real visible toggle, with literal user text carried across.
    const literal = { goal: 'ncr-synthetic literal goal 001', criterion: 'ncr-synthetic literal criterion', title: 'NCR literal title 001' };
    let literalPreserved: any = { checked: false };
    try {
      await openRecord(SELECTED);
      await measure(`selected-${vp.name}-en`, 'selected', 'en', vp, `${vp.name}-selected-en`);
      await panel.getByRole('textbox', { name: COPY.en.goal, exact: true }).fill(literal.goal);
      await panel.getByRole('textbox', { name: COPY.en.criterion, exact: true }).fill(literal.criterion);
      await panel.getByRole('textbox', { name: COPY.en.title, exact: true }).fill(literal.title);
      await useLang('vi');
      literalPreserved = { checked: true,
        goal: (await panel.getByRole('textbox', { name: COPY.vi.goal, exact: true }).inputValue()) === literal.goal,
        criterion: (await panel.getByRole('textbox', { name: COPY.vi.criterion, exact: true }).inputValue()) === literal.criterion,
        title: (await panel.getByRole('textbox', { name: COPY.vi.title, exact: true }).inputValue()) === literal.title };
      const r = await measure(`selected-${vp.name}-vi`, 'selected', 'vi', vp, `${vp.name}-selected-vi`); r.literalPreserved = literalPreserved;
      // Agent-simulated novice decision (selected): read the pre-effect text, decline, leave the panel without Build.
      const before = writes();
      await closeRecord(SELECTED);
      novice.push({ profile: 'selected', viewport: vp.name, language: 'vi', explanationExcerpt: String((r as any).disclosure?.text ?? '').slice(0, 220),
        ambiguity: 'disclosure states a local test profile and says later export may use a different profile', action: 'left the panel without Build', domainWriteAttemptsDuring: writes() - before,
        panelClosed: true });
    } catch (error) { rows.push({ rowId: `selected-${vp.name}`, error: String((error as Error).message ?? error).slice(0, 300) }); }
    // Generic (non ncr-synthetic) profile: VI then EN.
    try {
      await openRecord(GENERIC);
      await measure(`generic-${vp.name}-vi`, 'generic', 'vi', vp);
      await useLang('en');
      const r = await measure(`generic-${vp.name}-en`, 'generic', 'en', vp, `${vp.name}-generic-en`);
      const before = writes();
      await closeRecord(GENERIC);
      novice.push({ profile: 'generic', viewport: vp.name, language: 'en', explanationExcerpt: String((r as any).disclosure?.text ?? '').slice(0, 220),
        ambiguity: 'destination of the excerpt and whether a receipt appears are not stated here', action: 'left the panel without Build', domainWriteAttemptsDuring: writes() - before, panelClosed: true });
    } catch (error) { rows.push({ rowId: `generic-${vp.name}`, error: String((error as Error).message ?? error).slice(0, 300) }); }

    // Real keyboard pass (selected profile, EN): Tab to the toggle, Enter/Space on it, Tab to the record button, Enter, Tab to Build.
    const kb: any = { viewport: vp.name, stops: [] as any[], found: {} as Record<string, number | null> };
    try {
      await useLang('en');
      await page.goto('/work-transfer', { waitUntil: 'domcontentloaded', timeout: 120_000 });
      await expect(page.getByTestId('history-list')).toBeVisible({ timeout: 120_000 });
      let prev: any = null; let count = 0;
      const press = async (key: string) => {
        await page.keyboard.press(key); count += 1;
        const info: any = await page.evaluate(DESCRIBE_FOCUS); info.seq = count; info.key = key;
        if (prev) { const st = await prev.evaluate(STYLE_OF).catch(() => null); kb.stops[kb.stops.length - 1].styleWhenBlurred = st; }
        kb.stops.push(info); prev = await page.evaluateHandle(() => document.activeElement); return info;
      };
      const until = async (label: string, test: (i: any) => boolean, cap: number) => {
        for (let i = 0; i < cap; i += 1) { const info = await press('Tab'); if (test(info)) { kb.found[label] = count; return info; } }
        kb.found[label] = null; return null;
      };
      const tg = await until('languageToggle', i => i.inLangSwitch, 60);
      if (tg) {
        await page.keyboard.press('Enter'); await expect(html).toHaveAttribute('lang', 'vi'); kb.enterToggledToVi = true;
        await page.keyboard.press('Space'); await expect(html).toHaveAttribute('lang', 'en'); kb.spaceToggledToEn = true;
      }
      const rec = await until('recordButton', i => i.testid === `export-record-${SELECTED}`, 80);
      if (rec) { await page.keyboard.press('Enter'); await expect(page.getByTestId('html-job-controls')).toBeVisible(); kb.enterOpenedPanel = true; }
      await until('goal', i => i.inPanel && i.name === COPY.en.goal, 20);
      await until('criterion1', i => i.inPanel && i.name === COPY.en.criterion, 5);
      const bd = await until('build', i => i.inPanel && i.tag === 'button' && i.name === COPY.en.build, 40);
      if (bd && kb.enterOpenedPanel) {
        await press('Shift+Tab'); await press('Shift+Tab'); const back = await press('Tab'); const again = await press('Tab');
        kb.backAndForthReturnedToBuild = again.name === COPY.en.build && !!back;
        const preWrites = writes();
        await page.keyboard.press('Enter');
        const validation = page.getByTestId('export-error-recovery');
        await validation.waitFor({ state: 'visible', timeout: 8000 }).catch(() => undefined);
        kb.emptyGoalValidation = { visible: await validation.isVisible(), text: (await validation.textContent().catch(() => '')) ?? '',
          expectedText: COPY.en.validation, matchesExpected: ((await validation.textContent().catch(() => '')) ?? '').trim() === COPY.en.validation,
          domainWriteAttemptsCaused: writes() - preWrites };
        await shot(`${vp.name}-keyboard-build-validation`);
        const away = await press('Tab'); const backAgain = await press('Shift+Tab');
        kb.focusMovedAway = away.name !== COPY.en.build || away.tag !== 'button'; kb.focusReturnable = backAgain.name === COPY.en.build;
      }
      kb.tabsUsed = count;
      kb.indicatorByStop = kb.stops.filter((s: any) => s.styleWhenBlurred).map((s: any) => ({ seq: s.seq, name: s.name, testid: s.testid,
        focusedOutline: s.outline, focusedBoxShadow: s.boxShadow, blurredOutline: s.styleWhenBlurred.outline, blurredBoxShadow: s.styleWhenBlurred.boxShadow,
        indicatorChanges: s.outline !== s.styleWhenBlurred.outline || s.boxShadow !== s.styleWhenBlurred.boxShadow, focusVisible: s.focusVisible, inViewport: s.inViewport }));
    } catch (error) { kb.error = String((error as Error).message ?? error).slice(0, 300); }
    keyboard.push(kb);
  }

  // Consolidate explicit findings from measurements (evidence completeness is separate from conformance).
  const findings: any[] = [];
  const add = (id: string, severity: string, rowIds: string[], detail: string, locator: string, fix: string) => { if (rowIds.length) findings.push({ id, severity, rowIds, detail, sourceLocator: locator, suggestedBoundedFix: fix }); };
  const ok = rows.filter(r => !r.error);
  add('UXF-DOC-OVERFLOW', 'HIGH', ok.filter(r => r.documentOverflow?.overflowX).map(r => r.rowId), 'Document is wider than the viewport (horizontal page scroll).', 'work-transfer/page.tsx and the shell layout', 'Contain the overflowing block (min-w-0 / overflow-x-auto on the wide child).');
  add('UXF-PANEL-OVERFLOW', 'HIGH', ok.filter(r => r.panelOverflow?.overflowX).map(r => r.rowId), 'Inline export panel content is wider than its container.', 'ArtifactExportPanel.tsx grid columns', 'Add min-w-0 on grid children or stack earlier.');
  add('UXF-OFFSCREEN-CONTROL', 'HIGH', ok.filter(r => r.outsideViewport?.length).map(r => r.rowId), 'A control lies partly outside the viewport width.', 'ArtifactExportPanel.tsx / HtmlJobControls.tsx', 'Wrap or shrink the control row.');
  add('UXF-CONTROL-OVERLAP', 'MEDIUM', ok.filter(r => r.overlaps?.length).map(r => r.rowId), 'Controls overlap each other.', 'ArtifactExportPanel.tsx', 'Stack or add gap.');
  add('UXF-TARGET-HEIGHT-LT44', 'MEDIUM', ok.filter(r => r.targets?.some((t: any) => !t.heightMeets44)).map(r => r.rowId),
    'One or more primary targets are shorter than 44px (see per-row targets).', 'CompactHeader/i18n LanguageToggle; work-transfer record button; HtmlJobControls Add criterion', 'Give those controls min-h-11 / min-w-11.');
  add('UXF-DISCLOSURE-NOT-BEFORE-BUILD', 'HIGH', ok.filter(r => r.disclosure && (r.disclosure.domOrderBeforeBuild === false || r.disclosure.aboveBuild === false)).map(r => r.rowId), 'Disclosure is not above the Build control.', 'ArtifactExportPanel.tsx', 'Move disclosure before Build.');
  add('UXF-DISCLOSURE-CLIPPED', 'HIGH', ok.filter(r => r.disclosure?.textClipped || r.disclosure?.clippedByAncestor).map(r => r.rowId), 'Disclosure text is clipped.', 'ArtifactExportPanel.tsx', 'Remove clipping on the disclosure container.');
  add('UXF-LABELS-MISSING', 'HIGH', ok.filter(r => r.ownedLabelsMissing?.length).map(r => r.rowId), 'Owned labels not visible in the active language.', 'HtmlJobControls.tsx / ArtifactExportPanel.tsx', 'Restore the missing label.');
  add('UXF-DISCLOSURE-COPY', 'HIGH', ok.filter(r => r.disclosureFragmentsMissing?.length || r.disclosureWrongProfile).map(r => r.rowId), 'Expected disclosure fragments absent, or the wrong profile text shown.', 'ArtifactExportPanel.tsx', 'Align copy and profile branch.');
  add('UXF-HTML-LANG-MISMATCH', 'HIGH', ok.filter(r => r.htmlLangMatches === false).map(r => r.rowId), 'html lang attribute does not match the selected language.', 'src/lib/i18n.tsx', 'Set html lang on every switch.');
  add('UXF-LITERAL-LOST', 'HIGH', ok.filter(r => r.literalPreserved?.checked && !(r.literalPreserved.goal && r.literalPreserved.criterion && r.literalPreserved.title)).map(r => r.rowId), 'User-entered text changed across the language switch.', 'HtmlJobControls.tsx', 'Keep form state across language change.');
  add('UXF-POSSIBLY-UNTRANSLATED', 'LOW', ok.filter(r => r.possiblyUntranslated?.length).map(r => r.rowId), 'Vietnamese view still shows ASCII-only English-looking lines (heuristic, verify by screenshot).', 'ArtifactExportPanel.tsx (for example the Candidate and HTML pills)', 'Localize the remaining pill text.');
  for (const kb of keyboard) {
    const tag = (s: string) => `keyboard-${kb.viewport}-${s}`;
    add('UXF-KB-UNREACHABLE', 'HIGH', ['languageToggle', 'recordButton', 'goal', 'criterion1', 'build'].filter(k => kb.found?.[k] === null).map(tag), 'Control not reached by Tab within the bounded sequence.', 'work-transfer page / header', 'Fix tab order or tabindex.');
    add('UXF-KB-NO-FOCUS-INDICATOR', 'HIGH', (kb.indicatorByStop ?? []).filter((s: any) => !s.indicatorChanges).map((s: any) => tag(`stop${s.seq}:${s.name}`)), 'Focused element shows no outline/box-shadow change versus blurred.', 'global focus styles', 'Add a visible focus ring.');
    add('UXF-KB-OFFSCREEN-FOCUS', 'MEDIUM', (kb.indicatorByStop ?? []).filter((s: any) => s.inViewport === false).map((s: any) => tag(`stop${s.seq}:${s.name}`)), 'Focused element is outside the viewport at the moment of focus.', 'page layout', 'Scroll focus into view.');
    add('UXF-KB-VALIDATION', 'HIGH', kb.emptyGoalValidation && !kb.emptyGoalValidation.matchesExpected ? [tag('emptyGoal')] : [], 'Empty-goal validation text missing or different.', 'ArtifactExportPanel.tsx recoveryMessageFor', 'Restore the owned message.');
  }
  const attemptedWrites = traffic.filter(t => t.decision === 'blocked-write');
  const externalBlocked = traffic.filter(t => t.decision === 'blocked-external');
  const effectBlocked = traffic.filter(t => t.decision === 'blocked-effect');
  const external = [...new Set(externalBlocked.map(t => t.host))];
  const shotBytes = shots.reduce((n, s) => n + s.bytes, 0);
  const summary = {
    rowsExpected: 12, rowsCompleted: ok.filter(r => r.panelPresent).length, rowErrors: rows.filter(r => r.error).map(r => ({ id: r.rowId, error: r.error })),
    keyboardPasses: keyboard.length, keyboardErrors: keyboard.filter(k => k.error).map(k => ({ viewport: k.viewport, error: k.error })),
    novicePasses: novice.length, domainWriteAttempts: attemptedWrites.length, attemptedWrites, effectBlocked: effectBlocked.length, externalBlockedHosts: external,
    externalBlockedCount: externalBlocked.length, screenshots: shots.length, screenshotBytes: shotBytes,
    trafficCounts: traffic.reduce((m: Record<string, number>, t) => { m[t.decision] = (m[t.decision] ?? 0) + 1; return m; }, {}),
    authPostsAllowed: traffic.filter(t => t.decision === 'auth-allowed').map(t => ({ method: t.method, path: t.path, status: t.status })),
    note: 'Auth bootstrap used the existing loginAs helper (APIRequestContext), which context routing cannot observe; browser-level auth GETs are in the traffic counts.',
  };
  const evidence = { schema: 'cvf.ncrR1UxReadonlyBrowserAssessment.v1', browser: browser.version(), viewports: VIEWPORTS, rows, keyboard, novice, findings, shots, summary,
    traffic: traffic.filter(t => t.path.startsWith('/api/') || t.method !== 'GET').map(({ method, path: p, decision, status }) => ({ method, path: p, decision, status })) };
  fs.writeFileSync(path.join(RUN_ROOT, 'ux-assessment.json'), JSON.stringify(evidence, null, 2));
  console.log('NCR_R1_UX_ASSESSMENT ' + JSON.stringify({ rowsCompleted: summary.rowsCompleted, findings: findings.map(f => `${f.id}:${f.rowIds.length}`), domainWriteAttempts: summary.domainWriteAttempts,
    screenshots: summary.screenshots, screenshotBytes: summary.screenshotBytes }));

  // Safety and completeness gates. UX findings above never fail the test.
  expect(summary.domainWriteAttempts).toBe(0);
  expect(summary.effectBlocked).toBe(0);
  expect(summary.rowErrors).toEqual([]);
  expect(summary.rowsCompleted).toBe(12);
  expect(summary.keyboardErrors).toEqual([]);
  expect(summary.novicePasses).toBe(6);
  expect(shots.length).toBeLessThanOrEqual(12);
  expect(shotBytes).toBeLessThanOrEqual(24 * 1024 * 1024);
});
