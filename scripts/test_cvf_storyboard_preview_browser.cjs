'use strict';
// Text Encoding Exception: Vietnamese UI labels are matched with their diacritics.
// Offline UI tests for the storyboard preview: existing Playwright/Chromium only, no install, file:// page, virtual clock for pure UI timers.
// The virtual clock verifies timer logic only; it is NOT a measured narration, audio or video duration.
const fs = require('fs'), path = require('path'), crypto = require('crypto'), assert = require('assert');
const ROOT = path.resolve(__dirname, '..');
const { chromium } = require(path.join(ROOT, 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/@playwright/test'));
const HTML = path.resolve(ROOT, process.argv[2] || 'docs/reviews/evidence/cvf-storyboard-preview-2026-10-09.html');
const DESIGN = path.join(ROOT, 'docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md');
const OUT = path.join(ROOT, '.cvf/runtime/cvf-offline-preview-worker-20261009');
const VIEWPORTS = { desktop1440x1050: { width: 1440, height: 1050 }, mobile390x844: { width: 390, height: 844 } };
const TIMEOUT = 90000, L = { play: 'Phát preview', pause: 'Tạm dừng', replay: 'Phát lại' };
const designBytes = fs.readFileSync(DESIGN), design = designBytes.toString('utf8').replace(/\r\n/g, '\n');
const section = design.split('\n## Scene Handoff')[1].split('\n## ')[0];
const scenes = [...section.matchAll(/^### (S\d{2}) \| (\d+)-(\d+) \| \d+ s\n- Narration: (.*)\n- On-screen: (.*)\n/gm)].map(m => ({ id: m[1], start: +m[2], end: +m[3], nar: m[4], scr: m[5] }));
const BADGE = design.match(/"(VÍ DỤ MINH HỌA[^"]*)"/)[1];
const results = [], requests = [], errors = [], screenshots = [];
let assertions = 0, browserVersion = '';
const ok = (c, m) => { assertions++; assert.ok(c, m); }, eq = (a, b, m) => { assertions++; assert.deepStrictEqual(a, b, m); };
const sceneAt = s => (scenes.find(x => s < x.end) || scenes[9]).id, mmss = s => String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
const state = p => p.evaluate(() => ({ vis: [...document.querySelectorAll('.scene:not([hidden])')].map(s => s.dataset.scene), timer: document.getElementById('timer').textContent,
  seek: Number(document.getElementById('seek').value), pressed: document.getElementById('play').getAttribute('aria-pressed'), label: document.getElementById('play').textContent,
  cur: [...document.querySelectorAll('.sc')].map((b, i) => b.getAttribute('aria-current') === 'true' ? i : -1).filter(i => i >= 0), prev: document.getElementById('prev').disabled, next: document.getElementById('next').disabled }));
const layout = p => p.evaluate(() => { const W = innerWidth, bad = [];
  for (const el of document.querySelectorAll('.scene:not([hidden]) *, .ctl *, header *')) { const r = el.getBoundingClientRect(); if (r.width && (r.right > W + 0.5 || r.left < -0.5)) bad.push(el.tagName + '.' + el.className); }
  const clip = [...document.querySelectorAll('.scene:not([hidden]) :is(h2,.card,.narration,.onscreen,.badge,.stage footer)')].filter(e => e.scrollWidth > e.clientWidth + 1).map(e => e.className || e.tagName);
  const st = document.querySelector('.scene:not([hidden]) .stage'), r = st.getBoundingClientRect();
  return { hscroll: document.documentElement.scrollWidth - W, bad, clip, ratio: r.width / r.height, overflowY: st.scrollHeight - st.clientHeight }; });

async function withPage(vpName, fn, browser) {
  const ctx = await browser.newContext({ viewport: VIEWPORTS[vpName], deviceScaleFactor: 1 }), page = await ctx.newPage();
  try {
    page.on('request', r => requests.push(r.url())); page.on('pageerror', e => errors.push('pageerror: ' + e.message));
    page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });
    await page.clock.install({ time: 0 }); await page.goto('file:///' + HTML.replace(/\\/g, '/')); await page.clock.pauseAt(100000);
    await fn(page, VIEWPORTS[vpName]);
  } finally { await ctx.close(); }
}
async function run(name, vp, fn, browser) {
  const t0 = Date.now(), before = assertions; let timer, status = 'PASS', error = null;
  try { await Promise.race([withPage(vp, fn, browser), new Promise((_, rej) => { timer = setTimeout(() => rej(new Error('per-test timeout')), TIMEOUT); })]); }
  catch (e) { status = 'FAIL'; error = String(e.message || e).slice(0, 500); } finally { clearTimeout(timer); }
  results.push({ name, viewport: vp, status, assertions: assertions - before, ms: Date.now() - t0, error });
  console.log(status + ' ' + vp + ' ' + name + (error ? ' :: ' + error : ''));
}

const tests = {
  async 'all ten scenes: exact narration, source screen, badges, selection, layout'(p, vp) {
    ok(scenes.length === 10, 'ten scenes parsed from design');
    const meta = await p.locator('.meta').textContent(); ok(meta.includes(crypto.createHash('sha256').update(designBytes).digest('hex')), 'page shows derived source SHA');
    for (let i = 0; i < 10; i++) {
      const s = scenes[i]; await p.locator('.sc').nth(i).click();
      const st = await state(p); eq(st.vis, [s.id], s.id + ' is the only visible scene'); eq(st.cur, [i], 'active selection'); eq(st.seek, s.start, 'seek follows scene'); eq(st.timer, mmss(s.start) + ' / 04:00', 'timer follows scene');
      eq(await p.locator('.scene:not([hidden]) .narration').textContent(), s.nar, s.id + ' narration exact'); eq(await p.locator('.scene:not([hidden]) .onscreen').textContent(), s.scr, s.id + ' on-screen exact');
      const badges = p.locator('.scene:not([hidden]) .badge'), illustrated = i >= 4 && i <= 7; eq(await badges.count(), illustrated ? 1 : 0, s.id + ' badge count');
      if (illustrated) { ok(await badges.isVisible(), s.id + ' badge visible'); eq(await badges.textContent(), BADGE, s.id + ' complete badge text'); }
      eq([st.prev, st.next], [i === 0, i === 9], 'prev/next disabled only at ends'); ok((await p.locator('.scene:not([hidden]) .stage').getAttribute('aria-label')).includes(s.id), 'stage label names scene');
      const m = await layout(p); eq([m.hscroll <= 0, m.bad, m.clip], [true, [], []], s.id + ' no horizontal overflow or clipped text ' + JSON.stringify(m));
      if (vp.width > 640) ok(Math.abs(m.ratio - 16 / 9) < 0.02 && m.overflowY <= 1, s.id + ' 16:9 stage without clipped content ' + JSON.stringify(m));
      if (i === 4 || i === 9) { const f = path.join(OUT, 'preview-' + vp.width + 'x' + vp.height + '-' + s.id + '.png'); await p.screenshot({ path: f, fullPage: true }); screenshots.push({ path: path.relative(ROOT, f).replace(/\\/g, '/'), sha256: crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex') }); }
    }
    eq(await p.locator('audio,video,canvas').count(), 0, 'no media elements');
  },
  async 'timer, pause, resume, seek boundaries, reset, prev/next'(p) {
    const play = p.locator('#play'); eq(await play.textContent(), L.play, 'initial label');
    await play.click(); let st = await state(p); eq([st.pressed, st.label], ['true', L.pause], 'playing state'); await p.clock.runFor(5000);
    eq((await state(p)).timer, '00:05 / 04:00', 'timer advances in virtual clock'); await play.click(); st = await state(p); eq([st.pressed, st.label], ['false', L.play], 'paused state');
    await p.clock.runFor(20000); eq((await state(p)).timer, '00:05 / 04:00', 'pause is stable'); await play.click(); await p.clock.runFor(11000);
    st = await state(p); eq([st.vis, st.timer], [['S02'], '00:16 / 04:00'], 'resume continues from paused time into S02');
    for (const t of [0, 14, 15, 94, 95, 189, 190, 239, 240]) { await p.locator('#seek').fill(String(t)); st = await state(p); eq([st.vis[0], st.seek, st.pressed], [sceneAt(t), t, 'false'], 'seek ' + t); }
    await p.evaluate(() => { const e = document.getElementById('seek'); e.value = '999'; e.dispatchEvent(new Event('input', { bubbles: true })); }); eq((await state(p)).seek, 240, 'range input clamps at max');
    await p.evaluate(() => seek(999)); eq((await state(p)).timer, '04:00 / 04:00', 'seek() clamps above the end (timer text)'); await p.evaluate(() => seek(-5)); eq((await state(p)).timer, '00:00 / 04:00', 'seek() clamps below zero');
    await play.click(); await p.clock.runFor(3000); await p.locator('#seek').fill('100'); await p.clock.runFor(5000); st = await state(p); eq([st.pressed, st.seek], ['false', 100], 'seeking while playing pauses and stays put');
    await p.locator('#reset').click(); st = await state(p); eq([st.vis, st.timer], [['S01'], '00:00 / 04:00'], 'reset');
    await p.locator('.sc').nth(2).click(); await p.locator('#prev').click(); eq((await state(p)).seek, 15, 'prev goes to S02 start'); await p.locator('#next').click(); eq((await state(p)).seek, 40, 'next goes to S03 start');
  },
  async 'keyboard navigation, focus order, accessible names, hidden-page pause'(p, vp) {
    await p.evaluate(() => document.activeElement && document.activeElement.blur());
    for (let i = 0; i < 4; i++) await p.keyboard.press('ArrowRight'); eq((await state(p)).vis, ['S05'], 'ArrowRight x4 reaches S05');
    await p.keyboard.press('ArrowLeft'); eq((await state(p)).vis, ['S04'], 'ArrowLeft'); await p.keyboard.press('Space'); eq((await state(p)).pressed, 'true', 'Space plays');
    await p.clock.runFor(2000); await p.keyboard.press('Space'); const paused = await state(p); eq(paused.pressed, 'false', 'Space pauses'); await p.clock.runFor(5000); eq((await state(p)).timer, paused.timer, 'keyboard pause stable');
    await p.locator('.sc').nth(5).focus(); await p.keyboard.press('Enter'); eq((await state(p)).vis, ['S06'], 'Enter activates focused scene button');
    await p.evaluate(() => { document.activeElement.blur(); window.scrollTo(0, 0); });
    const names = []; for (let i = 0; i < 40; i++) { await p.keyboard.press('Tab'); const f = await p.evaluate(() => { const e = document.activeElement; if (!e || e === document.body) return null; const cs = getComputedStyle(e);
      return { tag: e.tagName, id: e.id, name: (e.getAttribute('aria-label') || e.textContent || (e.labels && e.labels[0] && e.labels[0].textContent) || '').trim(), outline: parseFloat(cs.outlineWidth), h: e.getBoundingClientRect().height, w: e.getBoundingClientRect().width }; });
      if (f) names.push(f); }
    const ids = names.map(n => n.id || n.tag); for (const need of ['prev', 'play', 'next', 'reset', 'seek']) ok(ids.includes(need), need + ' reachable by Tab');
    eq(names.filter(n => n.tag === 'BUTTON' && !n.id).length >= 10, true, 'ten scene buttons reachable by Tab');
    for (const n of names) { ok(n.name.length > 0, 'accessible name for ' + (n.id || n.tag)); ok(n.outline > 0, 'visible keyboard focus ring for ' + (n.id || n.tag)); ok(n.h >= 43.5, 'touch target height for ' + (n.id || n.tag)); }
    eq(await p.locator('label[for=seek]').count(), 1, 'seek has a visible label');
    await p.locator('#play').click(); await p.clock.runFor(2000);
    await p.evaluate(() => { Object.defineProperty(document, 'hidden', { configurable: true, get: () => true }); document.dispatchEvent(new Event('visibilitychange')); });
    const h = await state(p); eq(h.pressed, 'false', 'page hidden pauses playback (simulated visibilitychange event)'); await p.clock.runFor(5000); eq((await state(p)).timer, h.timer, 'hidden pause is stable');
  },
  async 'end-stop and replay across 240 seconds'(p) {
    await p.locator('#play').click(); await p.clock.runFor(239000); let st = await state(p); eq([st.vis, st.timer, st.pressed], [['S10'], '03:59 / 04:00', 'true'], 'S10 at 239 s');
    await p.clock.runFor(3000); st = await state(p); eq([st.timer, st.pressed, st.label, st.next, st.seek], ['04:00 / 04:00', 'false', L.replay, true, 240], 'ends and stops at 240');
    await p.clock.runFor(10000); eq((await state(p)).timer, '04:00 / 04:00', 'no run past the end');
    await p.locator('#play').click(); await p.clock.runFor(3000); st = await state(p); eq([st.vis, st.timer, st.pressed], [['S01'], '00:03 / 04:00', 'true'], 'replay restarts at 0');
  },
};

(async () => {
  const t0 = Date.now(); let browser;
  try {
    ok(fs.existsSync(HTML), 'preview HTML exists'); browser = await chromium.launch(); browserVersion = browser.version();
    for (const vp of Object.keys(VIEWPORTS)) for (const [name, fn] of Object.entries(tests)) await run(name, vp, fn, browser);
  } finally { if (browser) await browser.close(); }
  const nonFile = requests.filter(u => !u.startsWith('file:')), failed = results.filter(r => r.status !== 'PASS');
  const summary = { status: failed.length || errors.length || nonFile.length ? 'FAIL' : 'PASS', browserVersion, html: path.relative(ROOT, HTML).replace(/\\/g, '/'), htmlSha256: crypto.createHash('sha256').update(fs.readFileSync(HTML)).digest('hex'),
    viewports: Object.keys(VIEWPORTS), tests: results, assertions, httpRequests: nonFile.length, totalRequests: requests.length, pageErrors: errors.length, errors, screenshots, timer: 'Playwright virtual clock; pure UI timer only, not measured playback duration', elapsedMs: Date.now() - t0 };
  fs.mkdirSync(OUT, { recursive: true }); fs.writeFileSync(path.join(OUT, 'browser-results.json'), JSON.stringify(summary, null, 2));
  console.log(summary.status + ' tests=' + results.length + ' assertions=' + assertions + ' http=' + nonFile.length + ' errors=' + errors.length + ' elapsedMs=' + summary.elapsedMs);
  process.exit(summary.status === 'PASS' ? 0 : 1);
})().catch(e => { console.error('FATAL ' + e.message); process.exit(1); });
