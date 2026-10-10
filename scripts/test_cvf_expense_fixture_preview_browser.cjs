'use strict';
// Text Encoding Exception: Vietnamese labels, notices and row text are matched with their diacritics.
// Browser proof for the expense fixture preview: installed Playwright Chromium only, file:// pages, no HTTP listener, no install.
// Supplementary to the accepted unit evidence; it measures browser transport, interaction, layout and two killed mutants only.
const fs = require('fs'), path = require('path'), crypto = require('crypto'), assert = require('assert');
const { pathToFileURL } = require('url');
const ROOT = path.resolve(__dirname, '..');
const { chromium } = require(path.join(ROOT, 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/@playwright/test'));
const { writePreview, pinnedSourceSha, SOURCE, sha256 } = require('./cvf_expense_fixture_preview.cjs');

const OUT = path.join(ROOT, '.cvf/runtime/cvf-expense-browser-worker-20261010');
const PROFILES = { desktop1280x800: { width: 1280, height: 800 }, mobile390x844: { width: 390, height: 844 } };
const NOTICE = 'VÍ DỤ MINH HỌA - CHƯA CHẠY THẬT - DỮ LIỆU GIẢ';
const LABEL = 'Lọc theo tháng';
const ALL = ['EXP-001', 'EXP-002', 'EXP-003', 'EXP-004'];
const TIMEOUT = 15000;
const results = [], screenshots = [], mutants = [];
let assertions = 0;
const check = (cond, msg) => { assertions++; assert.ok(cond, msg); };
const same = (actual, expected, msg) => { assertions++; assert.deepStrictEqual(actual, expected, msg); };

const read = (page) => page.evaluate(() => ({
  ids: [...document.querySelectorAll('[data-expense-id]')].map((el) => el.dataset.expenseId),
  table: document.querySelectorAll('#root table').length,
  status: document.querySelector('#root [role=status]')?.textContent ?? null,
  body: document.body.innerText,
}));

// Explicit geometry checks: no page-level horizontal scroll, no clipped section, input/note/table inside the viewport.
const layout = (page) => page.evaluate(() => {
  const W = window.innerWidth, inside = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.left >= -0.5 && r.right <= W + 0.5; };
  const section = document.querySelector('#root section'), table = document.querySelector('#root table');
  return {
    hscroll: document.documentElement.scrollWidth - W,
    sectionClipped: section.scrollWidth > section.clientWidth + 1,
    input: inside(document.querySelector('input[type=month]')),
    note: inside(document.querySelector('p[role=note]')),
    table: table ? inside(table) : null,
    dateOneLine: [...document.querySelectorAll('#root tbody td:first-child')].every((td) => {
      const range = document.createRange(); range.selectNodeContents(td); return range.getClientRects().length === 1;
    }),
  };
});

async function primaryFlow(page, profile) {
  await page.waitForSelector('#root table tbody tr');
  let st = await read(page);
  same(st.ids, ALL, 'initial clear filter shows four valid rows in source order');
  check(!st.body.includes('Dòng nhập sai định dạng') && !st.body.includes('05/03/2026'), 'malformed row is absent');
  same(await page.locator('p[role=note]').textContent(), NOTICE, 'existing synthetic notice is exact');
  const input = page.getByLabel(LABEL);
  same([await input.count(), await input.getAttribute('type')], [1, 'month'], 'native month input has the Vietnamese accessible label');
  await input.fill('2026-03');
  st = await read(page);
  same(st.ids, ['EXP-003', 'EXP-004'], 'March 2026 shows exactly the two March rows');
  const geo = await layout(page);
  same([geo.hscroll <= 0, geo.sectionClipped, geo.input, geo.note, geo.table, geo.dateOneLine], [true, false, true, true, true, true], 'March view fits viewport without clipping or split dates ' + JSON.stringify(geo));
  const file = path.join(OUT, 'preview-' + profile + '-march.png');
  await page.screenshot({ path: file, fullPage: true });
  screenshots.push({ path: path.relative(ROOT, file).replace(/\\/g, '/'), bytes: fs.statSync(file).size, sha256: sha256(fs.readFileSync(file)) });
  await input.fill('2026-04');
  st = await read(page);
  same([st.ids, st.table, st.status.includes('Không có khoản chi nào')], [[], 0, true], 'April shows the empty message and no table');
  await input.fill('');
  st = await read(page);
  same(st.ids, ALL, 'clearing the filter restores four valid rows');
}

async function calendarFlow(page) {
  await page.waitForSelector('#root table tbody tr');
  let st = await read(page);
  same(st.ids, ['EXP-001', 'EXP-003', 'EXP-004', 'EXP-005'], 'clear view drops impossible 2026-03-32 and keeps valid rows in order');
  const input = page.getByLabel(LABEL);
  await input.fill('2026-03');
  st = await read(page);
  same(st.ids, ['EXP-003', 'EXP-004'], 'March 2026 excludes wrong-year 2025-03-15 and impossible 2026-03-32');
  await input.fill('2025-03');
  st = await read(page);
  same(st.ids, ['EXP-005'], 'positive control: March 2025 shows only the wrong-year row');
}

// One isolated context per case; external requests are aborted and recorded; page/console errors are failures.
async function runCase(name, profile, browser, htmlPath, flow) {
  const t0 = Date.now(), before = assertions, net = { requests: [], external: [], errors: [] };
  let status = 'PASS', error = null, failureKind = null;
  const ctx = await browser.newContext({ viewport: PROFILES[profile], deviceScaleFactor: 1 });
  try {
    const page = await ctx.newPage();
    page.setDefaultTimeout(TIMEOUT);
    await ctx.route('**/*', (route) => {
      const url = route.request().url();
      if (url.startsWith('file:')) return route.continue();
      net.external.push(url);
      return route.abort();
    });
    page.on('request', (req) => net.requests.push(req.url()));
    page.on('pageerror', (e) => net.errors.push('pageerror: ' + e.message));
    page.on('console', (m) => { if (m.type() === 'error') net.errors.push('console: ' + m.text()); });
    const mainUrl = pathToFileURL(htmlPath).href;
    await page.goto(mainUrl);
    await page.waitForSelector('#root section');
    await flow(page, profile);
  } catch (e) {
    status = 'FAIL';
    failureKind = e.name === 'AssertionError' ? 'ASSERTION' : 'HARNESS_OR_RUNTIME';
    error = String(e.message || e).slice(0, 400);
  } finally { await ctx.close(); }
  const fileOnly = net.requests.filter((u) => !u.startsWith('file:'));
  if (net.external.length || fileOnly.length) { status = 'FAIL'; failureKind = failureKind || 'EXTERNAL_REQUEST'; }
  if (net.errors.length) { status = 'FAIL'; failureKind = failureKind || 'PAGE_ERROR'; error = error || net.errors.join(' | ').slice(0, 400); }
  const record = { name, profile, status, failureKind, assertions: assertions - before, ms: Date.now() - t0, error, externalRequests: net.external.length, pageErrors: net.errors.length };
  results.push(record);
  console.log(status + ' ' + profile + ' ' + name + (error ? ' :: ' + error : ''));
  return record;
}

// Two mutants derived from the pinned source text (exact single-occurrence replacement, never written to the accepted file).
const MUTANTS = [
  { id: 'M1-month-predicate', from: "(month === '' || expense.date.slice(0, 7) === month)", to: "(month === '' || expense.date.slice(5, 7) === month.slice(5, 7))" },
  { id: 'M2-calendar-day-validity', from: 'return day >= 1 && day <= daysInMonth(year, month);', to: 'return day >= 1;' },
];

async function mutantRuns(browser, pinnedText) {
  for (const m of MUTANTS) {
    if (pinnedText.split(m.from).length !== 2) throw new Error('mutant anchor not unique: ' + m.id);
    const html = path.join(OUT, 'mutant-' + m.id + '.html');
    await writePreview({ output: html, variant: 'calendar', sourceTextOverride: pinnedText.replace(m.from, m.to) });
    const rec = await runCase('mutant ' + m.id + ' calendar negatives', 'desktop1280x800', browser, html, calendarFlow);
    mutants.push({ id: m.id, collected: 1, completed: rec.status === 'PASS' || rec.failureKind === 'ASSERTION' ? 1 : 0, killed: rec.failureKind === 'ASSERTION', failureKind: rec.failureKind, firstFailure: rec.error });
  }
}

(async () => {
  const t0 = Date.now(); let browser = null, summary = null;
  try {
    const pinnedText = fs.readFileSync(SOURCE, 'utf8');
    const sourceOk = sha256(fs.readFileSync(SOURCE)) === pinnedSourceSha();
    const primary = path.join(OUT, 'expense-preview.html'), calendar = path.join(OUT, 'expense-preview-calendar.html');
    const calBuild = await writePreview({ output: calendar, variant: 'calendar' });
    check(fs.existsSync(primary) && sourceOk, 'primary preview exists and accepted source matches its pin');
    const primaryBefore = sha256(fs.readFileSync(primary));
    browser = await chromium.launch();
    const browserVersion = browser.version();
    for (const profile of Object.keys(PROFILES)) {
      await runCase('primary march/april/clear flow', profile, browser, primary, (page) => primaryFlow(page, profile));
      await runCase('calendar negatives', profile, browser, calendar, calendarFlow);
    }
    await mutantRuns(browser, pinnedText);
    const restored = await writePreview({ output: calendar, variant: 'calendar' });
    const restoredRun = await runCase('restored calendar negatives after mutants', 'desktop1280x800', browser, calendar, calendarFlow);
    summary = { browserVersion, primaryHtmlSha256: primaryBefore, calendarHtmlSha256: calBuild.htmlSha256, restoredCalendarHtmlSha256: restored.htmlSha256, restoredPass: restoredRun.status === 'PASS', primaryHtmlUnchanged: sha256(fs.readFileSync(primary)) === primaryBefore, sourceSha256: sha256(fs.readFileSync(SOURCE)) };
  } catch (e) {
    results.push({ name: 'harness', status: 'FAIL', failureKind: 'HARNESS_OR_RUNTIME', error: String(e.message).slice(0, 400) });
  } finally { if (browser) await browser.close(); }
  const normal = results.filter((r) => !r.name.startsWith('mutant '));
  const allPass = normal.length > 0 && normal.every((r) => r.status === 'PASS') && mutants.length === MUTANTS.length && mutants.every((m) => m.killed && m.failureKind === 'ASSERTION');
  const shotsOk = screenshots.every((s) => s.bytes <= 3 * 1024 * 1024);
  const report = {
    status: allPass && shotsOk && summary && summary.restoredPass && summary.primaryHtmlUnchanged && summary.sourceSha256 === pinnedSourceSha() ? 'PASS' : 'FAIL',
    ...summary, tests: results, mutants, screenshots, assertions, externalRequests: results.reduce((n, r) => n + (r.externalRequests || 0), 0),
    pageErrors: results.reduce((n, r) => n + (r.pageErrors || 0), 0), elapsedMs: Date.now() - t0,
  };
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, 'browser-results.json'), JSON.stringify(report, null, 2));
  console.log(report.status + ' tests=' + results.length + ' assertions=' + assertions + ' mutantsKilled=' + mutants.filter((m) => m.killed).length + '/' + MUTANTS.length + ' elapsedMs=' + report.elapsedMs);
  process.exit(report.status === 'PASS' ? 0 : 1);
})().catch((e) => { console.error('FATAL ' + e.message); process.exit(1); });
