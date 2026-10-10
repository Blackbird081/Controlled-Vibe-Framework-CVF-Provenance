'use strict';
// Text Encoding Exception: Vietnamese synthetic labels, notices and row text use Vietnamese letters with diacritics.
// Browser proof for the ExpenseList month-input touch-target correction: installed Playwright Chromium, file:// pages only,
// no HTTP listener, no install, no network. It bundles the ACTUAL tracked component; the 36px mutant is an ignored copy.
const fs = require('fs'), path = require('path'), crypto = require('crypto'), assert = require('assert');
const { pathToFileURL } = require('url');
const ROOT = path.resolve(__dirname, '..'), WEB = path.join(ROOT, 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web');
const SOURCE = path.join(WEB, 'src/expenses/ExpenseList.tsx'), OUT = path.join(ROOT, '.cvf/runtime/cvf-expense-touch-worker-20261010');
const BUILD = path.join(OUT, 'build');
const PREIMAGE_SHA = '801f305238f2512db663fee7ada837a7bf53a84036ea6efcd305d29985339f19';
const MAX_HTML = 2 * 1024 * 1024, MAX_PNG = 3 * 1024 * 1024, TIMEOUT = 15000;
const { chromium } = require(path.join(WEB, 'node_modules/@playwright/test'));

const sha256 = (buf) => crypto.createHash('sha256').update(buf).digest('hex');
const posix = (p) => p.replace(/\\/g, '/');
const sourceSha = () => sha256(fs.readFileSync(SOURCE));
const hexRgb = (hex) => 'rgb(' + [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16)).join(', ') + ')';
const parseRgb = (s) => s.match(/[\d.]+/g).slice(0, 3).map(Number);
const lin = (c) => { const v = c / 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
const lum = ([r, g, b]) => 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b);
const ratio = (a, b) => { const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x); return (hi + 0.05) / (lo + 0.05); };
const round = (n) => Math.round(n * 100) / 100;

// Literal oracle: five synthetic rows authored for this proof (not imported from unit expectations).
const ROWS = [
  { id: 'TT-001', date: '2026-02-11', label: 'Chi phí kiểm thử A', amount: 50000 },
  { id: 'TT-002', date: '2026-02-24', label: 'Chi phí kiểm thử B', amount: 75000 },
  { id: 'TT-003', date: '2026-03-02', label: 'Chi phí kiểm thử C', amount: 130000 },
  { id: 'TT-004', date: '2026-03-19', label: 'Chi phí kiểm thử D', amount: 260000 },
  { id: 'TT-005', date: '05/03/2026', label: 'Dòng định dạng sai kiểm thử', amount: 99000 },
];
const CLEAR_IDS = ['TT-001', 'TT-002', 'TT-003', 'TT-004'];
const MARCH_IDS = ['TT-003', 'TT-004'];
const LABEL = 'Lọc theo tháng';
const NOTICE = 'VÍ DỤ MINH HỌA - CHƯA CHẠY THẬT - DỮ LIỆU GIẢ';
const INVALID_TEXT = 'Dòng định dạng sai kiểm thử';

// DESIGN.md core dark tokens; light values are the explicit synthetic fixture overrides from the work order.
const DARK = { '--cvf-bg-page': '#111218', '--cvf-surface': '#1c1d27', '--cvf-border': 'rgba(255,255,255,0.08)', '--cvf-border-strong': 'rgba(255,255,255,0.14)', '--cvf-text-primary': '#f4f7fb', '--cvf-text-secondary': '#a3adc2', '--cvf-text-muted': '#6f7890', '--cvf-warning': '#f59e0b' };
const LIGHT = { '--cvf-bg-page': '#f8fafc', '--cvf-surface': '#ffffff', '--cvf-border': 'rgba(15,23,42,0.12)', '--cvf-border-strong': 'rgba(15,23,42,0.24)', '--cvf-text-primary': '#0f172a', '--cvf-text-secondary': '#334155', '--cvf-text-muted': '#475569', '--cvf-warning': '#92400e' };
const PROFILES = {
  'dark-desktop-1280x800': { width: 1280, height: 800, scheme: 'dark', theme: DARK, accent: '#5b5cf6', screenshot: false },
  'dark-mobile-390x844': { width: 390, height: 844, scheme: 'dark', theme: DARK, accent: '#5b5cf6', screenshot: true },
  'light-mobile-390x844': { width: 390, height: 844, scheme: 'light', theme: LIGHT, accent: '#5b5cf6', screenshot: true },
  'light-alt-mobile-390x844': { width: 390, height: 844, scheme: 'light', theme: LIGHT, accent: '#0f766e', screenshot: true },
};

const results = [], mutants = [], shots = [], metrics = []; let assertions = 0, browser = null;
const check = (cond, msg) => { assertions++; assert.ok(cond, msg); };
const same = (actual, expected, msg) => { assertions++; assert.deepStrictEqual(actual, expected, msg); };

async function bundle(entryFile) {
  const vite = await import(pathToFileURL(path.join(WEB, 'node_modules/vite/dist/node/index.js')).href);
  const alias = (name) => posix(path.join(WEB, 'node_modules', name));
  const result = await vite.build({
    configFile: false, envFile: false, mode: 'production', root: BUILD, logLevel: 'silent',
    define: { 'process.env.NODE_ENV': JSON.stringify('production') },
    resolve: { alias: [{ find: 'react-dom', replacement: alias('react-dom') }, { find: 'react', replacement: alias('react') }] },
    oxc: { jsx: { runtime: 'automatic' } },
    build: { write: false, minify: true, sourcemap: false, emptyOutDir: false, reportCompressedSize: false, modulePreload: false,
      lib: { entry: entryFile, name: 'CvfTouchTarget', formats: ['iife'], fileName: () => 'touch.js' } },
  });
  const outputs = (Array.isArray(result) ? result : [result]).flatMap((r) => r.output);
  if (outputs.length !== 1 || outputs[0].type !== 'chunk') throw new Error('bundle must be exactly one JS chunk');
  return outputs[0].code;
}

function pageHtml(p, script) {
  const vars = Object.entries({ ...p.theme, '--cvf-accent': p.accent }).map(([k, v]) => `${k}:${v}`).join(';');
  return `<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kiểm tra vùng chạm chi tiêu - dữ liệu giả</title>
<style>:root{color-scheme:${p.scheme};${vars}}
body{margin:0;background:var(--cvf-bg-page);color:var(--cvf-text-primary);font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{box-sizing:border-box;max-width:960px;margin:0 auto;padding:16px}
#root section{overflow-x:auto}#root td:first-child{white-space:nowrap}
:focus-visible{outline:2px solid var(--cvf-accent);outline-offset:2px}</style></head>
<body><main><div id="root"></div></main><script>${script}</script></body></html>
`;
}

// Bundles one component file (the tracked file or an ignored mutant copy) into one offline page per profile.
async function buildPages(componentFile, tag) {
  fs.mkdirSync(BUILD, { recursive: true });
  const spec = posix(path.relative(BUILD, componentFile));
  const entry = path.join(BUILD, 'entry-' + tag + '.tsx');
  fs.writeFileSync(entry, [
    `import { createElement } from 'react'; import { createRoot } from 'react-dom/client';`,
    `import { ExpenseList } from ${JSON.stringify(spec.startsWith('.') ? spec : './' + spec)};`,
    `const expenses = ${JSON.stringify(ROWS)};`,
    `createRoot(document.getElementById('root')).render(createElement(ExpenseList, { expenses }));`,
  ].join('\n'), 'utf8');
  let code = await bundle(entry);
  if (code.includes('<!--')) throw new Error('bundle contains an HTML comment opener; refusing inline output');
  code = code.replace(/<\/(script)/gi, '<\\/$1');
  const pages = {};
  for (const [name, p] of Object.entries(PROFILES)) {
    const file = path.join(OUT, 'page-' + tag + '-' + name + '.html');
    const html = pageHtml(p, code);
    if (Buffer.byteLength(html) > MAX_HTML) throw new Error('page exceeds 2 MiB cap');
    fs.writeFileSync(file, html, 'utf8');
    pages[name] = file;
  }
  return pages;
}

// One read-only measurement pass: DOM ids, computed tokens, boxes and row/notice colors. Assertions run in Node.
const probe = (page) => page.evaluate(() => {
  const q = (s) => document.querySelector(s), style = (el) => getComputedStyle(el);
  const box = (el) => { const r = el.getBoundingClientRect(); return { w: r.width, h: r.height, l: r.left, r: r.right }; };
  const input = q('input[type=month]'), note = q('p[role=note]'), table = q('#root table'), section = q('#root section');
  return {
    vw: window.innerWidth,
    ids: [...document.querySelectorAll('[data-expense-id]')].map((el) => el.dataset.expenseId),
    tables: document.querySelectorAll('#root table').length,
    status: q('#root [role=status]') ? q('#root [role=status]').textContent : null,
    body: document.body.innerText,
    scheme: style(document.documentElement).colorScheme,
    hscroll: document.documentElement.scrollWidth - window.innerWidth,
    clipped: section.scrollWidth > section.clientWidth + 1,
    input: box(input), note: box(note), table: table ? box(table) : null,
    inputBg: style(input).backgroundColor, inputFg: style(input).color,
    noteFg: style(note).color, surface: style(section).backgroundColor,
    rowFgs: [...document.querySelectorAll('#root tbody td')].map((td) => style(td).color),
    dateOneLine: [...document.querySelectorAll('#root tbody td:first-child')].every((td) => { const r = document.createRange(); r.selectNodeContents(td); return r.getClientRects().length === 1; }),
  };
});

// The geometry assertion: outer target of the month input must be at least 44 x 44 CSS px.
function touch(s, label) {
  check(s.input.h >= 44, 'touch target<44: ' + label + ' input outer height ' + s.input.h);
  check(s.input.w >= 44, 'touch target<44: ' + label + ' input outer width ' + s.input.w);
}

function layout(s, label) {
  check(s.hscroll <= 0, label + ' no page horizontal scroll');
  check(!s.clipped, label + ' section not clipped');
  for (const [name, b] of [['input', s.input], ['note', s.note], ['table', s.table]]) check(b !== null && b.w > 0 && b.l >= -0.5 && b.r <= s.vw + 0.5, label + ' ' + name + ' inside viewport');
  check(s.dateOneLine, label + ' dates stay on one line');
}

function tokens(s, p, label) {
  const t = p.theme;
  same(s.scheme, p.scheme, label + ' color-scheme matches theme');
  same(s.inputBg, hexRgb(t['--cvf-bg-page']), label + ' input background token');
  same(s.inputFg, hexRgb(t['--cvf-text-primary']), label + ' input text token');
  same(s.surface, hexRgb(t['--cvf-surface']), label + ' surface token');
  same(s.noteFg, hexRgb(t['--cvf-warning']), label + ' notice token');
  same([...new Set(s.rowFgs)], [hexRgb(t['--cvf-text-primary'])], label + ' row text token');
}

function contrast(s, label) {
  check(s.rowFgs.length > 0, label + ' rows rendered for contrast');
  const surface = parseRgb(s.surface);
  const rowMin = Math.min(...s.rowFgs.map((fg) => ratio(parseRgb(fg), surface)));
  const note = ratio(parseRgb(s.noteFg), surface);
  check(rowMin >= 4.5, label + ' row text contrast ' + rowMin.toFixed(2));
  check(note >= 4.5, label + ' notice contrast ' + note.toFixed(2));
  return { profile: label, rowTextContrastMin: round(rowMin), noticeContrast: round(note) };
}

// Keyboard focus from a non-focused page: the first Tab must reach the month input with a visible accent outline.
async function focusCheck(page, p, label) {
  await page.evaluate(() => { if (document.activeElement) document.activeElement.blur(); });
  const before = await probe(page);
  await page.keyboard.press('Tab');
  const f = await page.evaluate(() => {
    const el = document.activeElement, cs = getComputedStyle(el), r = el.getBoundingClientRect();
    return { tag: el.tagName, type: el.type, visible: el.matches(':focus-visible'), outlineStyle: cs.outlineStyle, outlineWidth: cs.outlineWidth, outlineColor: cs.outlineColor, outlineOffset: cs.outlineOffset, h: r.height, w: r.width };
  });
  check(f.tag === 'INPUT' && f.type === 'month', label + ' Tab reaches the month input');
  check(f.visible, label + ' focus-visible matches');
  same([f.outlineStyle, f.outlineWidth, f.outlineOffset], ['solid', '2px', '2px'], label + ' focus outline is 2px solid, offset 2px');
  same(f.outlineColor, hexRgb(p.accent), label + ' focus outline uses the active accent token');
  same([f.h, f.w], [before.input.h, before.input.w], label + ' focus keeps control geometry');
  return { outlineColor: f.outlineColor, outlineWidth: f.outlineWidth };
}

async function shot(page, name, p) {
  if (!p.screenshot) return;
  const file = path.join(OUT, 'march-' + name + '.png');
  await page.screenshot({ path: file, fullPage: true });
  const buf = fs.readFileSync(file);
  check(buf.length <= MAX_PNG, name + ' screenshot within 3 MiB');
  shots.push({ profile: name, path: posix(path.relative(ROOT, file)), bytes: buf.length, sha256: sha256(buf) });
}

async function waitState(page) {
  await page.waitForSelector('#root table tbody tr', { timeout: TIMEOUT });
  return probe(page);
}

async function marchFlow(page, name, p) {
  let s = await waitState(page);
  same(s.ids, CLEAR_IDS, name + ' clear view shows four valid rows in source order');
  check(!s.body.includes(INVALID_TEXT) && !s.body.includes('05/03/2026'), name + ' invalid row absent');
  check(s.body.includes(NOTICE), name + ' synthetic notice present');
  touch(s, name + ' clear');
  layout(s, name + ' clear');
  const focus = await focusCheck(page, p, name);
  await page.getByLabel(LABEL).fill('2026-03');
  s = await probe(page);
  same(s.ids, MARCH_IDS, name + ' March shows the two March rows');
  touch(s, name + ' March');
  layout(s, name + ' March');
  tokens(s, p, name + ' March');
  metrics.push({ ...contrast(s, name), inputOuterWidth: s.input.w, inputOuterHeight: s.input.h, focusOutlineWidth: focus.outlineWidth, focusOutlineColor: focus.outlineColor });
  await shot(page, name, p);
}

// The one ordinary March -> April -> clear flow, run on dark mobile only.
async function ordinaryFlow(page, name, p) {
  await marchFlow(page, name, p);
  const input = page.getByLabel(LABEL);
  await input.fill('2026-04');
  let s = await probe(page);
  same([s.ids, s.tables, (s.status || '').includes('Không có khoản chi nào')], [[], 0, true], 'April shows empty state and no table');
  await input.fill('');
  s = await probe(page);
  same(s.ids, CLEAR_IDS, 'clearing the filter restores four valid rows');
  check(!s.body.includes(INVALID_TEXT), 'invalid row stays absent after clearing');
}

// Sizing-only flow for the mutant and the restored re-run: the same geometry assertion, nothing else.
async function geometryFlow(page) {
  touch(await waitState(page), 'geometry');
}

async function runCase(label, name, pageFile, flow) {
  const p = PROFILES[name], t0 = Date.now(), before = assertions;
  const net = { external: [], errors: [] };
  let status = 'PASS', failureKind = null, error = null, ctx = null;
  try {
    ctx = await browser.newContext({ viewport: { width: p.width, height: p.height }, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    page.setDefaultTimeout(TIMEOUT);
    await ctx.route('**/*', (route) => (route.request().url().startsWith('file:') ? route.continue() : route.abort()));
    page.on('request', (req) => { if (!req.url().startsWith('file:')) net.external.push(req.url()); });
    page.on('pageerror', (e) => net.errors.push('pageerror: ' + e.message));
    page.on('console', (m) => { if (m.type() === 'error') net.errors.push('console: ' + m.text()); });
    await page.goto(pathToFileURL(pageFile).href);
    await flow(page, name, p);
  } catch (e) {
    status = 'FAIL';
    failureKind = e.name === 'AssertionError' ? 'ASSERTION' : 'HARNESS_OR_RUNTIME';
    error = String(e.message || e).slice(0, 400);
  } finally { if (ctx) await ctx.close(); }
  if (net.external.length) { status = 'FAIL'; failureKind = failureKind || 'EXTERNAL_REQUEST'; }
  if (net.errors.length) { status = 'FAIL'; failureKind = failureKind || 'PAGE_ERROR'; error = error || net.errors.join(' | ').slice(0, 400); }
  const record = { label, profile: name, status, failureKind, assertions: assertions - before, ms: Date.now() - t0, error, externalRequests: net.external.length, pageErrors: net.errors.length };
  results.push(record); console.log(status + ' ' + label + ' ' + name + (error ? ' :: ' + error : ''));
  return record;
}

(async () => {
  const t0 = Date.now(), shaStart = sourceSha();
  let report = null;
  try {
    check(shaStart !== PREIMAGE_SHA, 'tracked component is the post-change source, not the inherited preimage');
    const pages = await buildPages(SOURCE, 'tracked');
    const shaAfterBuild = sourceSha();
    same(shaAfterBuild, shaStart, 'tracked source unchanged by bundling');
    browser = await chromium.launch();
    const browserVersion = browser.version();
    for (const name of Object.keys(PROFILES)) await runCase('baseline', name, pages[name], name === 'dark-mobile-390x844' ? ordinaryFlow : marchFlow);
    // Sizing mutant: a 36px copy in the ignored runtime. Only the geometry assertion is rerun; the tracked file is never touched.
    const mutantDir = path.join(OUT, 'mutant'), mutantFile = path.join(mutantDir, 'ExpenseList.mutant.tsx');
    const src = fs.readFileSync(SOURCE, 'utf8');
    same(src.split('height: 44,').length, 2, 'mutant anchor is unique in the tracked source');
    fs.mkdirSync(mutantDir, { recursive: true });
    fs.writeFileSync(mutantFile, src.replace('height: 44,', 'height: 36,'), 'utf8');
    const mutantSha = sha256(fs.readFileSync(mutantFile));
    check(mutantSha !== shaStart, 'mutant copy differs from the tracked source');
    const mutantPages = await buildPages(mutantFile, 'mutant');
    const mut = await runCase('mutant-36px', 'dark-mobile-390x844', mutantPages['dark-mobile-390x844'], geometryFlow);
    mutants.push({ id: 'mutant-36px', collected: 1, completed: mut.failureKind === 'ASSERTION' || mut.status === 'PASS' ? 1 : 0, killed: mut.failureKind === 'ASSERTION' && /touch target<44/.test(mut.error || ''), failureKind: mut.failureKind, firstFailure: mut.error });
    const restored = await runCase('restored', 'dark-mobile-390x844', pages['dark-mobile-390x844'], geometryFlow);
    const shaEnd = sourceSha();
    same(shaEnd, shaStart, 'tracked source unchanged across all proofs');
    report = { browserVersion, sourceSha256: { start: shaStart, afterBuild: shaAfterBuild, end: shaEnd }, mutantSourceSha256: mutantSha, restoredPass: restored.status === 'PASS' };
  } catch (e) {
    results.push({ label: 'harness', status: 'FAIL', failureKind: 'HARNESS_OR_RUNTIME', error: String(e.message).slice(0, 400) });
  } finally { if (browser) await browser.close(); }
  const baseline = results.filter((r) => r.label === 'baseline');
  const allPass = baseline.length === Object.keys(PROFILES).length && baseline.every((r) => r.status === 'PASS') && report && report.restoredPass;
  const mutantOk = mutants.length === 1 && mutants[0].killed && mutants[0].completed === 1;
  const clean = results.every((r) => (r.externalRequests || 0) === 0 && (r.pageErrors || 0) === 0);
  const final = {
    status: allPass && mutantOk && shots.length === 3 && clean && report && report.sourceSha256.start === report.sourceSha256.end ? 'PASS' : 'FAIL',
    ...(report || {}), tests: results, mutants, screenshots: shots, metrics, assertions,
    externalRequests: results.reduce((n, r) => n + (r.externalRequests || 0), 0),
    pageErrors: results.reduce((n, r) => n + (r.pageErrors || 0), 0), elapsedMs: Date.now() - t0,
  };
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, 'browser-results.json'), JSON.stringify(final, null, 2));
  console.log(final.status + ' cases=' + results.length + ' assertions=' + assertions + ' mutantKilled=' + mutants.filter((m) => m.killed).length + '/1 screenshots=' + shots.length + ' elapsedMs=' + final.elapsedMs);
  process.exit(final.status === 'PASS' ? 0 : 1);
})().catch((e) => { console.error('FATAL ' + e.message); process.exit(1); });
