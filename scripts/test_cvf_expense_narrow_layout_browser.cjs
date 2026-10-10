'use strict';
// Text Encoding Exception: Vietnamese synthetic labels, notices and row text use Vietnamese letters with diacritics.
// Browser proof for the ExpenseList long-label containment correction: installed Playwright Chromium, file:// pages only,
// no HTTP listener, no install, no network. It bundles the ACTUAL tracked component; the mutant is the saved admitted preimage.
const fs = require('fs'), path = require('path'), crypto = require('crypto'), assert = require('assert');
const { pathToFileURL } = require('url');
const ROOT = path.resolve(__dirname, '..'), WEB = path.join(ROOT, 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web');
const SOURCE = path.join(WEB, 'src/expenses/ExpenseList.tsx'), OUT = path.join(ROOT, '.cvf/runtime/cvf-expense-layout-worker-20261010');
const BUILD = path.join(OUT, 'build'), PREIMAGE = path.join(OUT, 'preimage/ExpenseList.preimage.tsx');
const PREIMAGE_SHA = '628862816a8dd77c78fab1dc1e2c94d55e3f29e78b8068878d22a236fd5f85b7';
const MAX_HTML = 2 * 1024 * 1024, MAX_PNG = 3 * 1024 * 1024, TIMEOUT = 15000, TOL = 1;
const { chromium } = require(path.join(WEB, 'node_modules/@playwright/test'));

const sha256 = (buf) => crypto.createHash('sha256').update(buf).digest('hex'), posix = (p) => p.replace(/\\/g, '/');
const sourceSha = () => sha256(fs.readFileSync(SOURCE));
const hexRgb = (hex) => 'rgb(' + [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16)).join(', ') + ')';
const parseRgb = (s) => s.match(/[\d.]+/g).slice(0, 3).map(Number);
const lin = (c) => { const v = c / 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
const lum = ([r, g, b]) => 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b);
const ratio = (a, b) => { const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x); return (hi + 0.05) / (lo + 0.05); }, round = (n) => Math.round(n * 100) / 100;

// Literal oracle authored for this proof (not imported from the unit fixture or the prior browser scripts).
const LONG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + 'ABCDEFGHIJKLMNOPQR';
const ROWS = [
  { id: 'NL-001', date: '2026-02-11', label: 'Chi phí A', amount: 50000 },
  { id: 'NL-002', date: '2026-02-24', label: 'Chi phí B', amount: 75000 },
  { id: 'NL-003', date: '2026-03-02', label: 'Independent row', amount: 130000 },
  { id: 'NL-004', date: '2026-03-19', label: LONG, amount: 260000 },
  { id: 'NL-005', date: '05/03/2026', label: 'Dòng định dạng sai', amount: 99000 },
];
const CLEAR_IDS = ['NL-001', 'NL-002', 'NL-003', 'NL-004'], MARCH_IDS = ['NL-003', 'NL-004'];
const HEADERS = ['Ngày', 'Nội dung', 'Số tiền'], LABEL = 'Lọc theo tháng';
const NOTICE = 'VÍ DỤ MINH HỌA - CHƯA CHẠY THẬT - DỮ LIỆU GIẢ', INVALID_TEXT = 'Dòng định dạng sai';
const DARK = { '--cvf-bg-page': '#111218', '--cvf-surface': '#1c1d27', '--cvf-border': 'rgba(255,255,255,0.08)', '--cvf-border-strong': 'rgba(255,255,255,0.14)', '--cvf-text-primary': '#f4f7fb', '--cvf-text-secondary': '#a3adc2', '--cvf-text-muted': '#6f7890', '--cvf-warning': '#f59e0b' };
const PROFILES = {
  'dark-320x844': { width: 320, height: 844, screenshot: true, flow: 'ordinary' },
  'dark-390x844': { width: 390, height: 844, screenshot: true, flow: 'march' },
  'dark-1280x800': { width: 1280, height: 800, screenshot: false, flow: 'march' },
};

const results = [], mutants = [], shots = [], metrics = []; let assertions = 0, browser = null;
const check = (cond, msg) => { assertions++; assert.ok(cond, msg); }, same = (actual, expected, msg) => { assertions++; assert.deepStrictEqual(actual, expected, msg); };

async function bundle(entryFile) {
  const vite = await import(pathToFileURL(path.join(WEB, 'node_modules/vite/dist/node/index.js')).href);
  const alias = (name) => posix(path.join(WEB, 'node_modules', name));
  const result = await vite.build({
    configFile: false, envFile: false, mode: 'production', root: BUILD, logLevel: 'silent',
    define: { 'process.env.NODE_ENV': JSON.stringify('production') },
    resolve: { alias: [{ find: 'react-dom', replacement: alias('react-dom') }, { find: 'react', replacement: alias('react') }] },
    oxc: { jsx: { runtime: 'automatic' } },
    build: { write: false, minify: true, sourcemap: false, emptyOutDir: false, reportCompressedSize: false, modulePreload: false,
      lib: { entry: entryFile, name: 'CvfNarrowLayout', formats: ['iife'], fileName: () => 'layout.js' } },
  });
  const outputs = (Array.isArray(result) ? result : [result]).flatMap((r) => r.output);
  if (outputs.length !== 1 || outputs[0].type !== 'chunk') throw new Error('bundle must be exactly one JS chunk');
  return outputs[0].code;
}

// Page fixture: margin 0, 16px container padding, system-ui 16px; no table, cell, nowrap or overflow overrides.
function pageHtml(script) {
  const vars = Object.entries({ ...DARK, '--cvf-accent': '#5b5cf6' }).map(([k, v]) => `${k}:${v}`).join(';');
  return `<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kiểm tra bố cục chi tiêu - dữ liệu giả</title>
<style>:root{color-scheme:dark;${vars}}
body{margin:0;font-family:system-ui;font-size:16px;background:var(--cvf-bg-page);color:var(--cvf-text-primary)}
main{padding:16px}
:focus-visible{outline:2px solid var(--cvf-accent);outline-offset:2px}</style></head>
<body><main><div id="root"></div></main><script>${script}</script></body></html>
`;
}

// Bundles one component file (the tracked file or the saved preimage) into one offline page.
async function buildPage(componentFile, tag) {
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
  const html = pageHtml(code);
  if (Buffer.byteLength(html) > MAX_HTML) throw new Error('page exceeds 2 MiB cap');
  const file = path.join(OUT, 'page-' + tag + '.html');
  fs.writeFileSync(file, html, 'utf8');
  return file;
}

// One read-only measurement pass. Geometry is measured in the page; assertions run in Node.
const probe = (page) => page.evaluate(() => {
  const q = (s) => document.querySelector(s), style = (el) => getComputedStyle(el), num = (v) => parseFloat(v) || 0;
  const box = (el) => { const r = el.getBoundingClientRect(); return { l: r.left, r: r.right, t: r.top, b: r.bottom, w: r.width, h: r.height }; };
  const inner = (el) => { const r = box(el), s = style(el); return { l: r.l + num(s.borderLeftWidth) + num(s.paddingLeft), r: r.r - num(s.borderRightWidth) - num(s.paddingRight), t: r.t + num(s.borderTopWidth) + num(s.paddingTop), b: r.b - num(s.borderBottomWidth) - num(s.paddingBottom) }; };
  const lines = (el) => { const out = [], w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) { const rg = document.createRange(); rg.selectNodeContents(n); for (const x of rg.getClientRects()) out.push({ l: x.left, r: x.right, t: x.top, b: x.bottom }); } return out; };
  const input = q('input[type=month]'), note = q('p[role=note]'), table = q('#root table'), section = q('#root section');
  return {
    vw: window.innerWidth,
    ids: [...document.querySelectorAll('[data-expense-id]')].map((el) => el.dataset.expenseId),
    tables: document.querySelectorAll('#root table').length,
    status: q('#root [role=status]') ? q('#root [role=status]').textContent : null,
    body: document.body.innerText,
    scheme: style(document.documentElement).colorScheme,
    hscroll: document.documentElement.scrollWidth - window.innerWidth,
    sectionOverflow: section.scrollWidth - section.clientWidth,
    content: inner(section),
    input: box(input), note: box(note), noteLines: lines(note), table: table ? box(table) : null,
    inputBg: style(input).backgroundColor, inputFg: style(input).color,
    noteFg: style(note).color, surface: style(section).backgroundColor,
    rowFgs: [...document.querySelectorAll('#root tbody td')].map((td) => style(td).color),
    cells: [...document.querySelectorAll('#root th, #root td')].map((c) => ({ tag: c.tagName, text: c.textContent, box: box(c), inner: inner(c), lines: lines(c) })),
  };
});

// Containment against the section content box (real rect minus border and padding), with a 1px tolerance.
const within = (r, box, label) => check(r.l >= box.l - TOL && r.r <= box.r + TOL && r.t >= box.t - TOL && r.b <= box.b + TOL,
  label + ' outside content box: x ' + r.l.toFixed(1) + '-' + r.r.toFixed(1) + ' vs ' + box.l.toFixed(1) + '-' + box.r.toFixed(1));

function containment(s, label) {
  check(s.table !== null, label + ' table rendered');
  within(s.table, s.content, label + ' table rectangle');
  for (const c of s.cells) {
    within(c.box, s.content, label + ' cell "' + c.text.slice(0, 12) + '" rectangle');
    for (const r of c.lines) within(r, c.inner, label + ' text line of "' + c.text.slice(0, 12) + '"');
  }
  within(s.note, s.content, label + ' notice rectangle');
  for (const r of s.noteLines) within(r, s.note, label + ' notice text line');
  within(s.input, s.content, label + ' input rectangle');
  check(s.hscroll <= 0 && s.sectionOverflow <= TOL, label + ' no document or section horizontal overflow');
}

function literal(s, expectedIds, label) {
  const rows = ROWS.filter((r) => expectedIds.includes(r.id)).map((r) => [r.date, r.label, String(r.amount)]);
  same(s.cells.filter((c) => c.tag === 'TH').map((c) => c.text), HEADERS, label + ' header text');
  same(s.cells.filter((c) => c.tag === 'TD').map((c) => c.text), rows.flat(), label + ' cell text equality');
}

function touch(s, label) {
  check(s.input.h >= 44, 'touch target<44: ' + label + ' input outer height ' + s.input.h);
  check(s.input.w >= 44, 'touch target<44: ' + label + ' input outer width ' + s.input.w);
}

function tokens(s, label) {
  const t = DARK;
  same(s.scheme, 'dark', label + ' color-scheme dark');
  same([s.inputBg, s.inputFg, s.surface, s.noteFg], [hexRgb(t['--cvf-bg-page']), hexRgb(t['--cvf-text-primary']), hexRgb(t['--cvf-surface']), hexRgb(t['--cvf-warning'])], label + ' input, surface and notice tokens');
  same([...new Set(s.rowFgs)], [hexRgb(t['--cvf-text-primary'])], label + ' row text token');
}

function contrast(s, label) {
  check(s.rowFgs.length > 0, label + ' rows rendered for contrast');
  const surface = parseRgb(s.surface);
  const rowMin = Math.min(...s.rowFgs.map((fg) => ratio(parseRgb(fg), surface)));
  const note = ratio(parseRgb(s.noteFg), surface);
  check(rowMin >= 4.5, label + ' row text contrast ' + rowMin.toFixed(2));
  check(note >= 4.5, label + ' notice contrast ' + note.toFixed(2));
  return { rowTextContrastMin: round(rowMin), noticeContrast: round(note) };
}

// Keyboard focus from a non-focused page: the first Tab must reach the month input with a visible accent outline.
async function focusCheck(page, label) {
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
  same(f.outlineColor, hexRgb('#5b5cf6'), label + ' focus outline uses the accent token');
  same([f.h, f.w], [before.input.h, before.input.w], label + ' focus keeps control geometry');
}

async function shot(page, name) {
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
  containment(s, name + ' clear');
  await focusCheck(page, name);
  await page.getByLabel(LABEL).fill('2026-03');
  s = await probe(page);
  same(s.ids, MARCH_IDS, name + ' March shows the two March rows');
  touch(s, name + ' March');
  containment(s, name + ' March');
  literal(s, MARCH_IDS, name + ' March');
  tokens(s, name + ' March');
  const labelCell = s.cells.find((c) => c.text === LONG);
  metrics.push({ profile: name, ...contrast(s, name), inputOuterWidth: s.input.w, inputOuterHeight: s.input.h, contentBox: s.content, tableBox: s.table, tableSlackLeft: round(s.table.l - s.content.l), tableSlackRight: round(s.content.r - s.table.r), longLabelLines: new Set(labelCell.lines.map((r) => Math.round(r.t))).size });
  if (p.screenshot) await shot(page, name);
}

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
  touch(s, name + ' restored clear');
  containment(s, name + ' restored clear');
  literal(s, CLEAR_IDS, name + ' restored clear');
}

// Layout-only flow for the preimage mutant and the restored corrected source: same containment oracle, no screenshot.
async function containmentFlow(page, name) {
  await waitState(page);
  await page.getByLabel(LABEL).fill('2026-03');
  const s = await probe(page);
  touch(s, name + ' March');
  containment(s, name + ' March');
  literal(s, MARCH_IDS, name + ' March');
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
    check(shaStart !== PREIMAGE_SHA, 'tracked component is the corrected source, not the admitted preimage');
    same(sha256(fs.readFileSync(PREIMAGE)), PREIMAGE_SHA, 'saved preimage matches the admitted SHA-256');
    const pageTracked = await buildPage(SOURCE, 'tracked');
    const shaAfterBuild = sourceSha(); same(shaAfterBuild, shaStart, 'tracked source unchanged by bundling');
    browser = await chromium.launch();
    const browserVersion = browser.version();
    for (const name of Object.keys(PROFILES)) await runCase('baseline', name, pageTracked, PROFILES[name].flow === 'ordinary' ? ordinaryFlow : marchFlow);
    // Layout mutant: the saved admitted preimage (ignored runtime copy). The tracked file is never mutated.
    const mutantSha = sha256(fs.readFileSync(PREIMAGE)), pagePreimage = await buildPage(PREIMAGE, 'preimage');
    const mut = await runCase('mutant-preimage', 'dark-320x844', pagePreimage, containmentFlow);
    mutants.push({ id: 'mutant-preimage-320', collected: 1, completed: mut.failureKind === 'ASSERTION' || mut.status === 'PASS' ? 1 : 0, killed: mut.failureKind === 'ASSERTION' && /rectangle|text line|horizontal|inner horizontal/.test(mut.error || ''), failureKind: mut.failureKind, firstFailure: mut.error, sourceSha256: mutantSha });
    const restored = await runCase('restored', 'dark-320x844', pageTracked, containmentFlow);
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
    status: allPass && mutantOk && shots.length === 2 && clean && report && report.sourceSha256.start === report.sourceSha256.end ? 'PASS' : 'FAIL',
    ...(report || {}), tests: results, mutants, screenshots: shots, metrics, assertions,
    externalRequests: results.reduce((n, r) => n + (r.externalRequests || 0), 0),
    pageErrors: results.reduce((n, r) => n + (r.pageErrors || 0), 0), elapsedMs: Date.now() - t0,
  };
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, 'browser-results.json'), JSON.stringify(final, null, 2));
  console.log(final.status + ' cases=' + results.length + ' assertions=' + assertions + ' mutantKilled=' + mutants.filter((m) => m.killed).length + '/1 screenshots=' + shots.length + ' elapsedMs=' + final.elapsedMs);
  process.exit(final.status === 'PASS' ? 0 : 1);
})().catch((e) => { console.error('FATAL ' + e.message); process.exit(1); });
