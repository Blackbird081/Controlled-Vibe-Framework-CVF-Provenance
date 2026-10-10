'use strict';
// Text Encoding Exception: Vietnamese synthetic labels and the intro note use Vietnamese letters with diacritics.
// Builds one standalone, offline HTML preview of the accepted read-only ExpenseList component with synthetic rows.
// CLI: node scripts/cvf_expense_fixture_preview.cjs --output <html> [--variant primary|calendar] [--source <tsx>]
// Helper: require(this).writePreview(...) for test-only runtime negatives. No install, no server, no network, no env/config load.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { pathToFileURL } = require('url');

const ROOT = path.resolve(__dirname, '..');
const WEB = path.join(ROOT, 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web');
const SOURCE = path.join(WEB, 'src/expenses/ExpenseList.tsx');
const PINS = path.join(ROOT, 'docs/reviews/evidence/cvf-expense-browser-dispatch-inputs-2026-10-10.json');
const BUILD = path.join(ROOT, '.cvf/runtime/cvf-expense-browser-worker-20261010/build');
const MAX_HTML = 2 * 1024 * 1024;
const sha256 = (buf) => crypto.createHash('sha256').update(buf).digest('hex');
const posix = (p) => p.replace(/\\/g, '/');

// Synthetic only. "calendar" changes two of the same five rows: EXP-002 becomes an impossible March date
// and EXP-005 becomes a valid-looking wrong-year March date, so the month filter must exclude both from March.
const PRIMARY = [
  { id: 'EXP-001', date: '2026-02-10', label: 'Vé xe mẫu tháng 2', amount: 120000 },
  { id: 'EXP-002', date: '2026-02-27', label: 'Văn phòng phẩm mẫu', amount: 85000 },
  { id: 'EXP-003', date: '2026-03-03', label: 'Cước vận chuyển mẫu', amount: 450000 },
  { id: 'EXP-004', date: '2026-03-18', label: 'Ăn trưa đoàn mẫu', amount: 210000 },
  { id: 'EXP-005', date: '05/03/2026', label: 'Dòng nhập sai định dạng', amount: 99000 },
];
const CALENDAR = PRIMARY.map((row) => {
  if (row.id === 'EXP-002') return { ...row, date: '2026-03-32' };
  if (row.id === 'EXP-005') return { ...row, date: '2025-03-15', label: 'Dòng khác năm mẫu' };
  return row;
});
const ROWS = { primary: PRIMARY, calendar: CALENDAR };

function pinnedSourceSha() {
  const inputs = JSON.parse(fs.readFileSync(PINS, 'utf8'));
  const entry = inputs.sources.find((s) => s.path === posix(path.relative(ROOT, SOURCE)));
  if (!entry) throw new Error('pin missing for ExpenseList.tsx');
  return entry.rawSha256;
}

async function bundle(entryFile) {
  const vite = await import(pathToFileURL(path.join(WEB, 'node_modules/vite/dist/node/index.js')).href);
  const alias = (name) => posix(path.join(WEB, 'node_modules', name));
  const result = await vite.build({
    configFile: false, envFile: false, mode: 'production', root: BUILD, logLevel: 'silent',
    define: { 'process.env.NODE_ENV': JSON.stringify('production') },
    resolve: { alias: [{ find: 'react-dom', replacement: alias('react-dom') }, { find: 'react', replacement: alias('react') }] },
    oxc: { jsx: { runtime: 'automatic' } },
    build: {
      write: false, minify: true, sourcemap: false, emptyOutDir: false, reportCompressedSize: false, modulePreload: false,
      lib: { entry: entryFile, name: 'CvfExpensePreview', formats: ['iife'], fileName: () => 'preview.js' },
    },
  });
  const outputs = (Array.isArray(result) ? result : [result]).flatMap((r) => r.output);
  if (outputs.length !== 1 || outputs[0].type !== 'chunk') throw new Error('bundle must be exactly one JS chunk');
  return outputs[0].code;
}

const TOKENS = {
  '--cvf-bg-shell': '#0d0f1a', '--cvf-bg-page': '#111218', '--cvf-surface': '#1c1d27', '--cvf-border': 'rgba(255,255,255,0.08)',
  '--cvf-border-strong': 'rgba(255,255,255,0.14)', '--cvf-text-primary': '#f4f7fb', '--cvf-text-secondary': '#a3adc2',
  '--cvf-text-muted': '#6f7890', '--cvf-accent': '#5b5cf6', '--cvf-warning': '#f59e0b',
};
const CSS = `:root{color-scheme:dark;${Object.entries(TOKENS).map(([k, v]) => `${k}:${v}`).join(';')}}
body{margin:0;background:var(--cvf-bg-page);color:var(--cvf-text-primary);font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{box-sizing:border-box;max-width:960px;margin:0 auto;padding:16px}
.intro{margin:0 0 12px;color:var(--cvf-text-secondary);font-size:14px;line-height:1.5}
#root section{overflow-x:auto}
#root td:first-child{white-space:nowrap}
:focus-visible{outline:2px solid var(--cvf-accent);outline-offset:2px}`;

function htmlPage(script) {
  return `<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Xem trước chi tiêu - dữ liệu giả</title>
<style>${CSS}</style>
</head>
<body>
<main>
<p class="intro">Xem trước riêng tư bằng dữ liệu tổng hợp để kiểm tra giao diện. Không phải tích hợp ứng dụng, không phải chức năng quản trị AI và không dùng dữ liệu thật.</p>
<div id="root"></div>
</main>
<script>${script}</script>
</body>
</html>
`;
}

// Builds in memory; the on-disk source must match its pin or nothing is built. sourceTextOverride is test-only:
// it compiles a mutated copy of the pinned source and never changes the accepted file.
async function buildPreview({ variant = 'primary', sourcePath = SOURCE, sourceTextOverride = null } = {}) {
  if (!ROWS[variant]) throw new Error('unknown variant: ' + variant);
  const sourceSha256 = sha256(fs.readFileSync(sourcePath));
  if (sourceSha256 !== pinnedSourceSha()) {
    throw new Error('SOURCE_PIN_DRIFT: ' + sourceSha256 + ' != pinned ' + pinnedSourceSha());
  }
  fs.mkdirSync(BUILD, { recursive: true });
  let componentFile = sourcePath;
  if (sourceTextOverride !== null) {
    componentFile = path.join(BUILD, 'ExpenseList.under-test.tsx');
    fs.writeFileSync(componentFile, sourceTextOverride, 'utf8');
  }
  const specifier = posix(path.relative(BUILD, componentFile));
  const entryFile = path.join(BUILD, 'entry-' + variant + '.tsx');
  fs.writeFileSync(entryFile, [
    `import { createElement } from 'react';`,
    `import { createRoot } from 'react-dom/client';`,
    `import { ExpenseList } from ${JSON.stringify(specifier.startsWith('.') ? specifier : './' + specifier)};`,
    `const expenses = ${JSON.stringify(ROWS[variant])};`,
    `createRoot(document.getElementById('root')).render(createElement(ExpenseList, { expenses }));`,
  ].join('\n'), 'utf8');
  let code = await bundle(entryFile);
  if (code.includes('<!--')) throw new Error('bundle contains an HTML comment opener; refusing inline output');
  code = code.replace(/<\/(script)/gi, '<\\/$1');
  const html = htmlPage(code);
  if (Buffer.byteLength(html) > MAX_HTML) throw new Error('preview HTML exceeds 2 MiB cap');
  return { html, variant, sourceSha256, htmlSha256: sha256(Buffer.from(html)), htmlBytes: Buffer.byteLength(html) };
}

// Atomic replace: the output is only replaced after a successful build.
async function writePreview(options) {
  const result = await buildPreview(options);
  const tmp = options.output + '.tmp-' + process.pid;
  fs.mkdirSync(path.dirname(options.output), { recursive: true });
  fs.writeFileSync(tmp, result.html, 'utf8');
  fs.renameSync(tmp, options.output);
  const { html, ...meta } = result;
  return { ...meta, output: options.output };
}

function parseArgs(argv) {
  const args = { variant: 'primary', source: SOURCE };
  for (let i = 0; i < argv.length; i += 2) {
    const key = argv[i], value = argv[i + 1];
    if (key === '--output') args.output = path.resolve(value);
    else if (key === '--variant') args.variant = value;
    else if (key === '--source') args.source = path.resolve(value);
    else throw new Error('unknown argument: ' + key);
  }
  if (!args.output) throw new Error('usage: --output <html> [--variant primary|calendar] [--source <tsx>]');
  return args;
}

async function main(argv) {
  const args = parseArgs(argv);
  const meta = await writePreview({ output: args.output, variant: args.variant, sourcePath: args.source });
  console.log(JSON.stringify(meta));
}

if (require.main === module) {
  main(process.argv.slice(2)).catch((error) => {
    console.error('REFUSED: ' + error.message);
    process.exit(1);
  });
}

module.exports = { buildPreview, writePreview, pinnedSourceSha, ROWS, SOURCE, sha256 };
