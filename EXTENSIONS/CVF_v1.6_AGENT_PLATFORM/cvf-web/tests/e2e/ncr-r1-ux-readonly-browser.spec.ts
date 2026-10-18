// UI-only focused completion of the R1 existing-owner UX repair (AGENTS pure-UI exception): six real-keyboard passes
// (mobile 390x844 and tablet 768x1024 x dark+indigo, light+indigo, dark+emerald) on the real running app. The browser route
// denies every non-GET/HEAD/OPTIONS request (auth included) and counts it before it is sent; the only credentials POST is the existing
// loginAs APIRequestContext bootstrap, observed by method/path/status only. No provider, evaluate/execute, external network or private data.
// Focus is only ever moved by real keyboard presses; the test never calls focus() or scrolls a focused field.
import type { Browser, BrowserContext, JSHandle, Page, Request, Route } from '@playwright/test';
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
const RING_MARGIN = 4;
const VIEWPORTS = [
  { name: 'mobile', width: 390, height: 844 },
  { name: 'tablet', width: 768, height: 1024 },
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
// Panel stops in DOM order after the record opens: [found key, accessible name, maximum Tab steps to reach it].
const PANEL_STOPS: [string, string, number][] = [
  ['goal', 'Goal', 4], ['criterion1', 'Criterion 1', 3], ['addCriterion', 'Add criterion', 3], ['title', 'Title', 4],
  ['sourceReference', 'Source reference', 3], ['recordType', 'Record type', 3], ['reviewStatus', 'Review status', 3],
  ['receipt', 'Receipt reference', 3], ['boundary', 'Review boundary', 3], ['sourceNotes', 'Source notes', 3], ['build', 'Build HTML', 3],
];
const BUILD_NAME = /^(Build HTML|Generating)$/;

type Style = Record<string, string>;
type Visibility = { fits: boolean; insideViewport: boolean; clippedBy: string[]; obscuredPoints: number; fullyVisible: boolean };
type FocusInfo = {
  tag: string; id: string | null; name: string; testid: string | null; inLangSwitch: boolean; inPanel: boolean; focusVisible: boolean;
  style: Style | null; rect: { x: number; y: number; w: number; h: number } | null; vis: Visibility | null; scrollY: number; viewport: { w: number; h: number };
};
type Settle = { settled: boolean; attempts: number; ms: number };
type Stop = FocusInfo & { seq: number; key: string; settle: Settle; blurred?: Style | null; blurredSettled?: boolean };
type Pass = {
  combo: string; viewport: string; theme: string; themeAsserted: boolean; stops: Stop[]; found: Record<string, number | null>;
  flags: Record<string, boolean>; sequence: string[]; error?: string;
};
type Shot = { id: string; kind: string; file: string; bytes: number; sha256: string };
type TrafficRow = { method: string; host: string; path: string; decision: string; nav: boolean; status?: number };

// Pure DOM read of the currently focused element: identity, computed focus style and full-visibility geometry.
const DESCRIBE_FOCUS = (margin: number): FocusInfo => {
  const viewport = { w: window.innerWidth, h: window.innerHeight };
  const el = document.activeElement as HTMLElement | null;
  const empty = { tag: 'body', id: null, name: '', testid: null, inLangSwitch: false, inPanel: false, focusVisible: false, style: null, rect: null, vis: null,
    scrollY: Math.round(window.scrollY * 10) / 10, viewport };
  if (!el || el === document.body) return empty;
  const cs = getComputedStyle(el);
  const style: Style = { outlineStyle: cs.outlineStyle, outlineWidth: cs.outlineWidth, outlineColor: cs.outlineColor, outlineOffset: cs.outlineOffset, boxShadow: cs.boxShadow,
    borderColor: cs.borderTopColor, borderWidth: cs.borderTopWidth, borderStyle: cs.borderTopStyle, background: cs.backgroundColor, opacity: cs.opacity, cursor: cs.cursor };
  const r = el.getBoundingClientRect();
  const box = { left: r.left - margin, top: r.top - margin, right: r.right + margin, bottom: r.bottom + margin };
  const fits = box.right - box.left <= viewport.w + 0.5 && box.bottom - box.top <= viewport.h + 0.5;
  const insideViewport = box.left >= -0.5 && box.top >= -0.5 && box.right <= viewport.w + 0.5 && box.bottom <= viewport.h + 0.5;
  const clippedBy: string[] = [];
  for (let a = el.parentElement; a && a !== document.documentElement; a = a.parentElement) {
    const acs = getComputedStyle(a);
    if (acs.overflowX === 'visible' && acs.overflowY === 'visible') continue;
    const ar = a.getBoundingClientRect();
    if (box.left < ar.left - 0.5 || box.top < ar.top - 0.5 || box.right > ar.right + 0.5 || box.bottom > ar.bottom + 0.5) clippedBy.push(a.tagName.toLowerCase() + (a.id ? `#${a.id}` : ''));
  }
  const points: [number, number][] = [[r.left + r.width / 2, r.top + r.height / 2], [r.left + 6, r.top + 6], [r.right - 6, r.bottom - 6]];
  let obscuredPoints = 0;
  for (const [x, y] of points) {
    if (x < 0 || y < 0 || x > viewport.w || y > viewport.h) { obscuredPoints += 1; continue; }
    const top = document.elementFromPoint(x, y);
    if (!top || !(top === el || el.contains(top))) obscuredPoints += 1;
  }
  return { tag: el.tagName.toLowerCase(), id: el.id || null,
    name: (el.getAttribute('aria-label') || el.innerText || el.getAttribute('title') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
    testid: el.getAttribute('data-testid'), inLangSwitch: !!el.closest('#tour-lang-switch'), inPanel: !!el.closest('[data-testid="inline-export-panel"]'),
    focusVisible: el.matches(':focus-visible'), style, rect: { x: Math.round(r.x * 10) / 10, y: Math.round(r.y * 10) / 10, w: Math.round(r.width * 10) / 10, h: Math.round(r.height * 10) / 10 },
    vis: { fits, insideViewport, clippedBy, obscuredPoints, fullyVisible: insideViewport && clippedBy.length === 0 && obscuredPoints === 0 },
    scrollY: Math.round(window.scrollY * 10) / 10, viewport };
};

// Bounded polling until scroll offsets, the target rect and its computed focus styles are identical over consecutive animation frames.
const SETTLE = ({ frames, deadlineMs }: { frames: number; deadlineMs: number }) => new Promise<Settle>(resolve => {
  const begin = performance.now(); let stable = 0; let last = ''; let attempts = 0;
  const tick = () => {
    attempts += 1;
    const target = document.activeElement;
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
const SETTLE_STYLE = (el: Element, [frames, deadlineMs]: [number, number]) => new Promise<{ style: Style; settled: boolean }>(resolve => {
  const begin = performance.now(); let stable = 0; let last = '';
  const read = (): Style => {
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

const sameStyle = (a: Style | null | undefined, b: Style | null | undefined) => !!a && !!b && JSON.stringify(a) === JSON.stringify(b);
const outlineVisible = (s: Style | null | undefined, css: string) => !!s && s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) >= 2 && s.outlineColor === css;
const blurredHidden = (s: Style | null | undefined) => !!s && (s.outlineStyle === 'none' || parseFloat(s.outlineWidth) === 0);
const focusChanges = (s: Stop | null | undefined, css: string) => !!s && s.focusVisible && outlineVisible(s.style, css) && blurredHidden(s.blurred) && !sameStyle(s.style, s.blurred);

test('focused completion: six real-keyboard passes with full Source notes focus visibility on mobile and tablet', async ({ page, context, browser }: { page: Page; context: BrowserContext; browser: Browser }) => {
  test.setTimeout(660_000);
  expect(browser.browserType().name()).toBe('chromium');
  const traffic: TrafficRow[] = [];
  const rowOf = new Map<Request, TrafficRow>();
  // The no-write fence is installed before any navigation or login.
  await context.route('**/*', async (route: Route) => {
    const req = route.request(); const url = new URL(req.url()); const method = req.method();
    const row: TrafficRow = { method, host: url.hostname, path: url.pathname, decision: '', nav: req.isNavigationRequest() };
    traffic.push(row); rowOf.set(req, row);
    if (!LOOPBACK.has(url.hostname)) { row.decision = 'blocked-external'; return route.abort(); }
    if (/^\/api\/(governance\/evaluate|execute)(\/|$)/.test(url.pathname)) { row.decision = 'blocked-effect'; return route.abort(); }
    if (method === 'GET' && url.pathname === '/api/admin/audit') {
      row.decision = 'fixture'; return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ success: true, data: AUDIT_FIXTURE }) });
    }
    if (!['GET', 'HEAD', 'OPTIONS'].includes(method)) { row.decision = url.pathname.startsWith('/api/auth/') ? 'blocked-auth-write' : 'blocked-write'; return route.abort(); }
    row.decision = 'allowed'; return route.continue();
  });
  context.on('response', (r) => { const row = rowOf.get(r.request()); if (row) row.status = r.status(); });

  // Observe the existing loginAs APIRequestContext calls by method/path/status only (no form values, no headers).
  const authApi: { method: string; path: string; status: number }[] = [];
  const requestApi = page.request as unknown as Record<string, (target: string, options?: unknown) => Promise<{ status(): number }>>;
  for (const m of ['get', 'post']) {
    const original = requestApi[m].bind(page.request);
    requestApi[m] = async (target: string, options?: unknown) => {
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

  const passes: Pass[] = []; const shots: Shot[] = [];
  const settleLog: { where: string; settled: boolean; attempts: number; ms: number }[] = [];
  const buildActivations: string[] = [];
  const screens = path.join(RUN_ROOT, 'ux-focused-screens'); fs.mkdirSync(screens, { recursive: true });
  const html = page.locator('html');
  const toggle = page.locator('#tour-lang-switch button:visible');
  const domainWrites = () => traffic.filter(t => t.decision === 'blocked-write').length;
  const authWrites = () => traffic.filter(t => t.decision === 'blocked-auth-write').length;
  const settle = async (where: string) => {
    const result = await page.evaluate(SETTLE, { frames: 10, deadlineMs: 4000 });
    settleLog.push({ where, ...result }); return result;
  };
  const shot = async (id: string, kind: string) => {
    if (shots.length >= 12) throw new Error('SCREENSHOT_CAP');
    const file = path.join(screens, `${id}.png`);
    await page.screenshot({ path: file, animations: 'disabled' });
    const bytes = fs.readFileSync(file);
    shots.push({ id, kind, file: path.relative(RUN_ROOT, file).replaceAll('\\', '/'), bytes: bytes.length, sha256: crypto.createHash('sha256').update(bytes).digest('hex') });
  };
  // Enter/Space are only ever sent to the skip link, language toggle or record button; a focused Build control stops the test.
  const activate = async (key: string) => {
    const focused = await page.evaluate(DESCRIBE_FOCUS, RING_MARGIN);
    if (BUILD_NAME.test(focused.name) && focused.tag === 'button') { buildActivations.push(key); throw new Error('BUILD_ACTIVATION_REFUSED'); }
    await page.keyboard.press(key);
  };
  const switchLang = async (lang: 'en' | 'vi') => {
    if ((await html.getAttribute('lang')) === lang) return;
    await expect(toggle).toHaveCount(1); await toggle.click(); await expect(html).toHaveAttribute('lang', lang);
  };

  const runPass = async (vp: (typeof VIEWPORTS)[number], th: (typeof THEMES)[number], first: boolean): Promise<Pass> => {
    const combo = `${vp.name}-${th.name}`;
    const pass: Pass = { combo, viewport: vp.name, theme: th.name, themeAsserted: false, stops: [], found: {}, flags: {}, sequence: [] };
    try {
      await page.evaluate(({ theme, accent }: { theme: string; accent: string }) => {
        localStorage.setItem('cvf_theme', theme); localStorage.setItem('cvf_ui_tweaks', JSON.stringify({ accent, radius: 14, density: 'normal' }));
      }, { theme: th.theme, accent: th.accent });
      await page.setViewportSize({ width: vp.width, height: vp.height });
      await page.goto('/work-transfer', { waitUntil: 'domcontentloaded', timeout: 120_000 });
      await expect(page.getByTestId('history-list')).toBeVisible({ timeout: 120_000 });
      await page.waitForFunction((rgb: string) => getComputedStyle(document.documentElement).getPropertyValue('--cvf-accent-rgb').trim() === rgb, th.rgb);
      await page.waitForFunction((dark: boolean) => document.documentElement.classList.contains('dark') === dark, th.theme === 'dark');
      pass.themeAsserted = true;
      await switchLang('en');
      await page.goto('/work-transfer', { waitUntil: 'domcontentloaded', timeout: 120_000 });
      await expect(page.getByTestId('history-list')).toBeVisible({ timeout: 120_000 });
      await switchLang('en');

      let prev: { handle: JSHandle; stop: Stop } | null = null; let count = 0;
      const record = async (stop: Stop): Promise<Stop> => {
        if (prev) {
          const done = prev; prev = null;
          let blurred = await done.handle.evaluate(SETTLE_STYLE, [10, 2000] as [number, number]).catch(() => null);
          if (!blurred && done.stop.inLangSwitch) blurred = await toggle.first().evaluate(SETTLE_STYLE, [10, 2000] as [number, number]).catch(() => null);
          done.stop.blurred = blurred?.style ?? null; done.stop.blurredSettled = blurred?.settled ?? false;
        }
        pass.stops.push(stop); pass.sequence.push(`${stop.key}:${stop.tag}${stop.id ? `#${stop.id}` : ''}${stop.testid ? `[${stop.testid}]` : ''}:${stop.name}`);
        prev = { handle: await page.evaluateHandle(() => document.activeElement as Element), stop }; return stop;
      };
      const press = async (key: string): Promise<Stop> => {
        await page.keyboard.press(key); count += 1;
        const s = await settle(`${combo}:kb${count}:${key}`);
        const info = await page.evaluate(DESCRIBE_FOCUS, RING_MARGIN);
        return record({ ...info, seq: count, key, settle: s });
      };
      const until = async (label: string, test: (s: Stop) => boolean, cap: number, key = 'Tab'): Promise<Stop | null> => {
        for (let i = 0; i < cap; i += 1) { const stop = await press(key); if (test(stop)) { pass.found[label] = i + 1; return stop; } }
        pass.found[label] = null; return null;
      };
      const isSkip = (s: Stop) => s.testid === 'skip-to-main';

      const skip = await until('skipLink', isSkip, 2);
      if (skip && first) await shot('skip-link-focused-mobile-dark-indigo', 'optional-skip-link');
      const tg = await until('languageToggle', s => s.inLangSwitch, 8);
      if (tg) {
        await activate('Enter'); await expect(html).toHaveAttribute('lang', 'vi'); pass.flags.enterToggledToVi = true;
        await activate('Space'); await expect(html).toHaveAttribute('lang', 'en'); pass.flags.spaceToggledToEn = true;
      }
      const backToSkip = await until('shiftTabToSkip', isSkip, 8, 'Shift+Tab');
      if (backToSkip) {
        await activate('Enter'); count += 1;
        const s = await settle(`${combo}:skip-enter`);
        const info = await page.evaluate(DESCRIBE_FOCUS, RING_MARGIN);
        await record({ ...info, seq: count, key: 'Enter', settle: s });
        pass.flags.enterLandedOnMain = info.id === 'cvf-dashboard-main' && info.tag === 'main';
        if (first && pass.flags.enterLandedOnMain) await shot('skip-main-landed-mobile-dark-indigo', 'optional-skip-link');
      }
      const rec = await until('recordButton', s => s.testid === `export-record-${SELECTED}`, 20);
      if (rec) { await activate('Enter'); await expect(page.getByTestId('html-job-controls')).toBeVisible(); pass.flags.enterOpenedPanel = true; }
      let missing = false;
      for (const [key, name, cap] of PANEL_STOPS) {
        if (missing) { pass.found[key] = null; continue; }
        const stop = await until(key, s => s.inPanel && s.name === name, cap);
        if (!stop) { missing = true; continue; }
        if (key === 'title' && vp.name === 'mobile') await shot(`focused-title-${combo}`, 'required-title');
        if (key === 'sourceNotes') await shot(`focused-source-notes-${combo}`, 'required-source-notes');
      }
      if (pass.found.build !== null && pass.found.build !== undefined) {
        const up = await press('Shift+Tab'); const down = await press('Tab');
        pass.flags.backAndForthReturnedToBuild = down.name === 'Build HTML' && up.inPanel;
        const away = await press('Tab'); const returned = await press('Shift+Tab');
        pass.flags.focusMovedAway = away.name !== 'Build HTML' || away.tag !== 'button'; pass.flags.focusReturnable = returned.name === 'Build HTML';
      }
    } catch (error) { pass.error = String((error as Error).message ?? error).slice(0, 300); }
    return pass;
  };

  let index = 0;
  for (const vp of VIEWPORTS) {
    for (const th of THEMES) {
      passes.push(await runPass(vp, th, index === 0)); index += 1;
      fs.writeFileSync(path.join(RUN_ROOT, 'ux-focused-partial.json'), JSON.stringify({ passesDone: index, passes, shots, domainWrites: domainWrites(), authWrites: authWrites() }));
    }
  }

  // Consolidate objective criteria. Evidence is written before any assertion can fail the test.
  const NAMED = new Set(PANEL_STOPS.map(([, name]) => name).filter(name => name !== 'Build HTML'));
  const REQUIRED_FOUND: [string, number][] = [['skipLink', 2], ['languageToggle', 8], ['shiftTabToSkip', 8], ['recordButton', 20], ...PANEL_STOPS.map(([k]): [string, number] => [k, 99])];
  const REQUIRED_FLAGS = ['enterToggledToVi', 'spaceToggledToEn', 'enterLandedOnMain', 'enterOpenedPanel', 'backAndForthReturnedToBuild', 'focusMovedAway', 'focusReturnable'];
  const cssOf = (name: string) => THEMES.find(t => t.name === name)?.css ?? '';
  const lastStop = (p: Pass, test: (s: Stop) => boolean): Stop | null => [...p.stops].reverse().find(test) ?? null;
  const passRows = passes.map(p => {
    const missingFound = REQUIRED_FOUND.filter(([k, cap]) => p.found[k] === null || p.found[k] === undefined || (p.found[k] as number) > cap).map(([k]) => k);
    const missingFlags = REQUIRED_FLAGS.filter(f => p.flags[f] !== true);
    const notes = lastStop(p, s => s.inPanel && s.name === 'Source notes' && s.key === 'Tab');
    const titleStop = lastStop(p, s => s.inPanel && s.name === 'Title' && s.key === 'Tab');
    const toggleStop = lastStop(p, s => s.inLangSwitch);
    const namedStops = p.stops.filter(s => s.inPanel && NAMED.has(s.name) && s.key === 'Tab');
    const namedNotVisible = namedStops.filter(s => s.vis && s.vis.fits && !s.vis.fullyVisible).map(s => `${s.name}:${JSON.stringify(s.vis)}`);
    const narrow = namedStops.filter(s => s.rect && (s.rect.h < 43.99 || s.rect.x < -1 || s.rect.x + s.rect.w > s.viewport.w + 1)).map(s => `${s.name}:${s.rect?.w}x${s.rect?.h}`);
    const row = { combo: p.combo, error: p.error ?? null, themeAsserted: p.themeAsserted, complete: !p.error && p.themeAsserted && !missingFound.length && !missingFlags.length, missingFound, missingFlags,
      sourceNotes: notes ? { rect: notes.rect, vis: notes.vis, scrollY: notes.scrollY, settle: notes.settle } : null,
      sourceNotesFullyVisible: !!notes && notes.vis?.fits === true && notes.vis.fullyVisible && notes.settle.settled,
      toggleFocusChange: focusChanges(toggleStop, cssOf(p.theme)), titleFocusChange: focusChanges(titleStop, cssOf(p.theme)),
      namedNotVisible, narrow };
    return row;
  });
  const requiredIds = new Set(['focused-title-mobile-dark-indigo', 'focused-title-mobile-light-indigo', 'focused-title-mobile-dark-emerald',
    ...VIEWPORTS.flatMap(v => THEMES.map(t => `focused-source-notes-${v.name}-${t.name}`))]);
  const requiredShots = shots.filter(s => requiredIds.has(s.id) && s.bytes > 0);
  const settleFailures = settleLog.filter(s => !s.settled).map(s => s.where);
  const stopsMissingTargets = passRows.reduce((n, r) => n + r.missingFound.length, 0);
  const shotBytes = shots.reduce((n, s) => n + s.bytes, 0);
  const criteria = {
    passes6: passRows.length === 6 && passRows.every(r => r.complete),
    sourceNotesFullyVisible6: passRows.length === 6 && passRows.every(r => r.sourceNotesFullyVisible),
    namedFieldsFullyVisible: passRows.every(r => r.namedNotVisible.length === 0),
    toggleAndTitleFocusChange: passRows.length === 6 && passRows.every(r => r.toggleFocusChange && r.titleFocusChange),
    fieldSizeAndContainment: passRows.every(r => r.narrow.length === 0),
    requiredPhotos9: requiredShots.length === 9,
    missingTargets0: stopsMissingTargets === 0,
    unstableRows0: settleFailures.length === 0 && passRows.every(r => r.themeAsserted),
  };
  const callbackPosts = authApi.filter(a => a.method === 'POST');
  const boundary = {
    domainWriteAttempts: domainWrites(), browserAuthWriteAttempts: authWrites(), effectBlocked: traffic.filter(t => t.decision === 'blocked-effect').length,
    externalBlockedHosts: [...new Set(traffic.filter(t => t.decision === 'blocked-external').map(t => t.host))],
    externalBlockedCount: traffic.filter(t => t.decision === 'blocked-external').length,
    loginFormFallback: traffic.some(t => t.path === '/login' && t.nav === true), apiRequestContext: authApi,
    callbackOnlyBootstrap: callbackPosts.length === 1 && callbackPosts[0].path === '/api/auth/callback/credentials' && authApi.every(a => a.path.startsWith('/api/auth/')),
    buildActivations: buildActivations.length, invalidBuildActivations: 0, validBuildActivations: 0,
    trafficCounts: traffic.reduce((m: Record<string, number>, t) => { m[t.decision] = (m[t.decision] ?? 0) + 1; return m; }, {}),
  };
  const evidence = { schema: 'cvf.ncrR1UxFocusedCompletion.v1', browser: browser.version(), viewports: VIEWPORTS, themes: THEMES, ringMargin: RING_MARGIN, passes, passRows, criteria,
    shots, requiredShotIds: [...requiredIds], settleLog, settleFailures, boundary, screenshotBytes: shotBytes,
    traffic: traffic.filter(t => t.path.startsWith('/api/') || t.method !== 'GET').map(({ method, path: p, decision, status }) => ({ method, path: p, decision, status })) };
  fs.writeFileSync(path.join(RUN_ROOT, 'ux-focused-assessment.json'), JSON.stringify(evidence, null, 2));
  console.log('NCR_R1_UX_FOCUSED ' + JSON.stringify({ criteria, screenshots: shots.length, screenshotBytes: shotBytes,
    boundary: { domainWriteAttempts: boundary.domainWriteAttempts, browserAuthWriteAttempts: boundary.browserAuthWriteAttempts, effectBlocked: boundary.effectBlocked,
      buildActivations: boundary.buildActivations, callbackOnlyBootstrap: boundary.callbackOnlyBootstrap } }));

  // Safety and conformance assertions; the evidence file above is written first so a failure never hides the measurements.
  expect(boundary.domainWriteAttempts).toBe(0);
  expect(boundary.browserAuthWriteAttempts).toBe(0);
  expect(boundary.effectBlocked).toBe(0);
  expect(boundary.loginFormFallback).toBe(false);
  expect(boundary.callbackOnlyBootstrap).toBe(true);
  expect(boundary.buildActivations).toBe(0);
  expect(shots.length).toBeLessThanOrEqual(12);
  expect(shotBytes).toBeLessThanOrEqual(16 * 1024 * 1024);
  expect(passRows.length).toBe(6);
  expect(criteria.passes6).toBe(true);
  expect(criteria.sourceNotesFullyVisible6).toBe(true);
  expect(criteria.requiredPhotos9).toBe(true);
  expect(criteria.missingTargets0).toBe(true);
  expect(criteria.unstableRows0).toBe(true);
  expect(criteria.toggleAndTitleFocusChange).toBe(true);
  expect(criteria.namedFieldsFullyVisible).toBe(true);
  expect(criteria.fieldSizeAndContainment).toBe(true);
});
