'use strict';
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const net = require('node:net');
const http = require('node:http');
const { spawn, spawnSync } = require('node:child_process');

const repo = path.resolve(__dirname, '..');
const app = path.join(repo, 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web');
const runHome = path.join(repo, '.cvf/runtime/ncr-r1-integrated-html-job-browser-20261018');
const preload = path.join(app, 'tests/e2e/support/ncr-draft-recovery-isolation.cjs');
const config = path.join(app, 'playwright.config.ncr-recovery.ts');
const workerSpec = path.join(app, 'tests/e2e/ncr-r1-integrated-html-job-browser.spec.ts');
const nextBin = path.join(app, 'node_modules/next/dist/bin/next');
const playwrightBin = path.join(app, 'node_modules/@playwright/test/cli.js');
const authorityFiles = [
  'docs/baselines/CVF_GC018_NCR_R1_INTEGRATED_HTML_JOB_BROWSER_2026-10-18.md',
  'docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R1_INTEGRATED_HTML_JOB_BROWSER_2026-10-18.md',
  'docs/reviews/CVF_NCR_R1_INTEGRATED_HTML_JOB_SOURCE_LOCAL_COMPLETION_REVIEW_2026-10-18.md',
  'docs/baselines/CVF_NCR_R1_INTEGRATED_HTML_JOB_DESIGN_2026-10-18.md',
  'CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json',
].map(name=>path.join(repo,name));
const transient = ['tsconfig.json', 'next-env.d.ts'];
const productSource = [
  'src/app/(dashboard)/work-transfer/page.tsx', 'src/app/api/artifacts/export/route.ts',
  'src/app/api/artifacts/jobs/route.ts', 'src/components/ArtifactExportPanel.tsx',
  'src/components/HtmlDraftRecovery.tsx', 'src/components/HtmlJobControls.tsx',
  'src/components/useHtmlBuildAttempts.ts', 'src/lib/html-job-contract.ts',
  'src/lib/server/html-draft-snapshot-store.ts', 'src/lib/server/html-job-api.ts',
  'src/lib/server/html-job-synthetic-profile.ts',
].map(name => path.join(app,name));
const sha = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const relative = file => path.relative(repo, file).replaceAll('\\', '/');
function fileInfo(file) { const bytes = fs.readFileSync(file); return { path: relative(file), bytes: bytes.length, sha256: sha(bytes) }; }
function pinPath(pin) { return path.isAbsolute(pin.path) ? pin.path : path.join(repo,pin.path); }
function verifiedNextDelta(name, before, after, dist) {
  if (!before || !after) return false;
  if (name === 'next-env.d.ts') {
    const original = before.toString('utf8');
    const current = after.toString('utf8');
    const line = /^import "\.\/[^"\r\n]+\/dev\/types\/routes\.d\.ts";$/m;
    return line.test(original) && current === original.replace(line, `import "./${dist}/dev/types/routes.d.ts";`);
  }
  if (name === 'tsconfig.json') {
    try {
      const old = JSON.parse(before.toString('utf8'));
      const now = JSON.parse(after.toString('utf8'));
      const allowed = [`${dist}/types/**/*.ts`, `${dist}/dev/types/**/*.ts`];
      if (!Array.isArray(old.include) || !Array.isArray(now.include) || !allowed.every(item=>now.include.includes(item))) return false;
      now.include = now.include.filter(item=>!allowed.includes(item));
      return JSON.stringify(now) === JSON.stringify(old);
    } catch { return false; }
  }
  return false;
}
function treeSize(directory) {
  if (!fs.existsSync(directory)) return { bytes:0, files:0 };
  let bytes=0, files=0; const pending=[directory];
  while (pending.length) {
    const current=pending.pop();
    for (const entry of fs.readdirSync(current,{ withFileTypes:true })) {
      const target=path.join(current, entry.name);
      if (entry.isDirectory()) pending.push(target);
      else if (entry.isFile()) { bytes+=fs.statSync(target).size; files++; }
      else throw new Error('UNEXPECTED_OUTPUT_KIND');
    }
  }
  return { bytes, files };
}
function safeEnvironment(root, id, dist) {
  const env = {
    SystemRoot: process.env.SystemRoot || 'C:\\Windows', WINDIR: process.env.WINDIR || 'C:\\Windows',
    PATH: [path.dirname(process.execPath), path.join(process.env.SystemRoot || 'C:\\Windows', 'System32')].join(path.delimiter),
    TEMP: path.join(root, 'temp'), TMP: path.join(root, 'temp'),
    NODE_ENV: 'development', NEXTAUTH_URL: '', AUTH_URL: 'http://localhost:3033',
    NEXTAUTH_SECRET: `ncr-fixture-${id}`, CVF_ADMIN_USER: 'ncr_fixture_admin', CVF_ADMIN_PASS: `ncr-fixture-pass-${id}`,
    CVF_STORAGE_ADAPTER_TYPE: 'file', CVF_CONTROL_PLANE_EVENTS_PATH: path.join(root, 'events.json'),
    CVF_POLICY_SNAPSHOT_DIR: path.join(root, 'policy'), CVF_DURABLE_MEMORY_STORE_PATH: path.join(root, 'memory.json'),
    CVF_FALSE_POSITIVE_REPORTS_PATH: path.join(root, 'false-positive.jsonl'),
    CVF_NCR_DRAFT_PROFILE: 'LOCAL_SYNTHETIC', CVF_NCR_DRAFT_ROOT: path.join(root, 'drafts'),
    CVF_NCR_DRAFT_RUN_ID: id, CVF_NCR_HTML_JOB_PROFILE: 'LOCAL_SYNTHETIC',
    CVF_NCR_RUN_ROOT: root, CVF_NCR_RUNNER_PROFILE: 'LOCAL_SYNTHETIC',
    CVF_NCR_ISOLATION_LOG: path.join(root, 'isolation.jsonl'), NEXT_DIST_DIR: dist,
    PLAYWRIGHT_BASE_URL: 'http://localhost:3033',
    NODE_OPTIONS: `--require="${preload.replaceAll('\\', '/')}"`,
    NEXT_TELEMETRY_DISABLED: '1', CI: '1',
  };
  return env;
}
function validateBoundary(env, root) {
  const allowed = new Set(['SystemRoot','WINDIR','PATH','TEMP','TMP','NODE_ENV','NEXTAUTH_URL','AUTH_URL','NEXTAUTH_SECRET',
    'CVF_ADMIN_USER','CVF_ADMIN_PASS','CVF_STORAGE_ADAPTER_TYPE','CVF_CONTROL_PLANE_EVENTS_PATH','CVF_POLICY_SNAPSHOT_DIR',
    'CVF_DURABLE_MEMORY_STORE_PATH','CVF_FALSE_POSITIVE_REPORTS_PATH','CVF_NCR_DRAFT_PROFILE','CVF_NCR_DRAFT_ROOT',
    'CVF_NCR_DRAFT_RUN_ID','CVF_NCR_HTML_JOB_PROFILE','CVF_NCR_RUN_ROOT','CVF_NCR_RUNNER_PROFILE','CVF_NCR_ISOLATION_LOG','NEXT_DIST_DIR',
    'PLAYWRIGHT_BASE_URL','NODE_OPTIONS','NEXT_TELEMETRY_DISABLED','CI']);
  if (Object.keys(env).some(key => !allowed.has(key)) || env.NODE_ENV !== 'development'
    || env.NEXTAUTH_URL !== '' || env.AUTH_URL !== env.PLAYWRIGHT_BASE_URL
    || env.CVF_NCR_DRAFT_PROFILE !== 'LOCAL_SYNTHETIC' || env.CVF_NCR_HTML_JOB_PROFILE !== 'LOCAL_SYNTHETIC'
    || env.CVF_STORAGE_ADAPTER_TYPE !== 'file'
    || !env.CVF_NCR_DRAFT_ROOT.startsWith(root + path.sep)
    || !env.CVF_CONTROL_PLANE_EVENTS_PATH.startsWith(root + path.sep)
    || !env.CVF_POLICY_SNAPSHOT_DIR.startsWith(root + path.sep)
    || env.NODE_OPTIONS !== `--require="${preload.replaceAll('\\', '/')}"`) throw new Error('CHILD_ENV_BOUNDARY_FAILED');
  return true;
}
function portFree() { return new Promise((resolve, reject) => { const server = net.createServer(); server.once('error', reject); server.listen(3033, 'localhost', () => server.close(() => resolve(true))); }); }
function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }
function requestStatus() { return new Promise(resolve => {
  const req = http.get('http://localhost:3033/api/auth/session', response => { response.resume(); resolve(response.statusCode); });
  req.on('error', () => resolve(null)); req.setTimeout(3000, () => { req.destroy(); resolve(null); });
}); }
async function waitReady(child, deadline) {
  while (Date.now() < deadline && child.exitCode === null) {
    const status = await requestStatus(); if (status === 200) return status;
    await sleep(500);
  }
  throw new Error(`NEXT_NOT_READY:${child.exitCode}`);
}
function stopOwned(child) {
  if (!child?.pid) return { attempted: false };
  const result = process.platform === 'win32'
    ? spawnSync('taskkill', ['/PID', String(child.pid), '/T', '/F'], { encoding: 'utf8', timeout: 10000 })
    : (() => { try { process.kill(-child.pid, 'SIGTERM'); return { status: 0 }; } catch { return { status: 1 }; } })();
  return { attempted: true, pid: child.pid, status: result.status };
}
function runProcess(argv, options, deadline) { return new Promise((resolve, reject) => {
  const child = spawn(argv[0], argv.slice(1), { ...options, shell: false });
  const timer = setTimeout(() => { stopOwned(child); reject(new Error('PLAYWRIGHT_DEADLINE')); }, Math.max(1, deadline - Date.now()));
  child.once('error', error => { clearTimeout(timer); reject(error); });
  child.once('exit', (code, signal) => { clearTimeout(timer); resolve({ code, signal, pid: child.pid }); });
}); }
async function main() {
  const start = Date.now(); const deadline = start + 15 * 60_000;
  const option = process.argv[2];
  if (process.argv.length > 2 && option !== '--probe-spec') throw new Error('UNKNOWN_ARG');
  const spec = option ? path.resolve(process.argv[3] || '') : workerSpec;
  if (option && (!spec.startsWith(path.join(repo, '.cvf/runtime') + path.sep) || !spec.endsWith('.spec.ts') || !fs.statSync(spec).isFile())) throw new Error('INVALID_PROBE_SPEC');
  fs.mkdirSync(runHome, { recursive: true });
  const root = fs.mkdtempSync(path.join(runHome, 'run-'));
  const id = `ncr_job_${crypto.randomBytes(12).toString('hex')}`;
  for (const dir of ['drafts','policy','temp']) fs.mkdirSync(path.join(root, dir), { recursive: false });
  fs.writeFileSync(path.join(root, 'drafts/.cvf-html-draft-synthetic.json'), JSON.stringify({ schemaVersion: 1, kind: 'CVF_HTML_DRAFT_SYNTHETIC', syntheticOnly: true, runId: id }), { flag: 'wx' });
  const dist = `.next-cvf-ncr-job-${id}`;
  const env = safeEnvironment(root, id, dist);
  validateBoundary(env, root);
  const preimages = Object.fromEntries(transient.map(name => [name, fs.existsSync(path.join(app,name)) ? fs.readFileSync(path.join(app,name)) : null]));
  const chromiumPath = require(path.join(app,'node_modules/@playwright/test')).chromium.executablePath();
  if (!fs.existsSync(chromiumPath)) throw new Error('CHROMIUM_BINARY_NOT_INSTALLED');
  const pins = [__filename, preload, config, spec, nextBin, playwrightBin, chromiumPath, ...authorityFiles,
    path.join(app,'src/lib/server/html-draft-synthetic-profile.ts'), path.join(app,'src/lib/server/html-draft-recovery-api.ts'),
    path.join(app,'src/app/api/artifacts/drafts/route.ts'), ...productSource].map(fileInfo);
  const executionBaseHead = spawnSync('git',['rev-parse','HEAD'],{cwd:repo,encoding:'utf8',timeout:5000}).stdout.trim();
  const manifest = { id, root, start, deadline, executionBaseHead, spec: relative(spec), argv: [], pins,
    port: 3033, chromiumBinary: chromiumPath,
    markerSha256: fileInfo(path.join(root,'drafts/.cvf-html-draft-synthetic.json')).sha256,
    envNames: Object.keys(env).sort(), preimages: Object.fromEntries(Object.entries(preimages).map(([k,v]) => [k, v ? sha(v) : null])) };
  fs.writeFileSync(path.join(root,'manifest.json'), JSON.stringify(manifest,null,2));
  let next; const result = { id, root, startedAt: new Date(start).toISOString(), manifest: 'manifest.json', outcomes: [] };
  try {
    await portFree(); result.outcomes.push({ phase:'port-preflight', status:'FREE' });
    const nextArgs = [process.execPath, nextBin, 'dev', '--webpack', '--hostname', 'localhost', '--port', '3033'];
    manifest.argv.push(nextArgs.map((value,i) => i === 0 ? 'node' : relativeOrValue(value)));
    const nextLog = fs.openSync(path.join(root,'next.log'),'wx');
    next = spawn(nextArgs[0], nextArgs.slice(1), { cwd: app, env, stdio: ['ignore',nextLog,nextLog], shell:false, detached: process.platform !== 'win32' });
    result.nextPid = next.pid;
    const ready = await waitReady(next, Math.min(deadline, Date.now()+120000));
    result.outcomes.push({ phase:'next-startup', status: ready, durationMs:Date.now()-start });
    const isolation = fs.readFileSync(env.CVF_NCR_ISOLATION_LOG,'utf8').split('\n').filter(Boolean).map(JSON.parse);
    if (!isolation.some(row => row.event === 'PRELOAD_ACTIVE' && row.nextauthEmpty) || isolation.some(row => row.event === 'EVALUATE_DISPATCH_BLOCKED')) throw new Error('ISOLATION_FENCE_NOT_ACTIVE');
    result.outcomes.push({ phase:'post-init-fence', status:'ACTIVE', contexts:isolation.filter(row=>row.event==='PRELOAD_ACTIVE').length,
      blockedExternalAttempts:isolation.filter(row=>row.event==='BLOCKED').length });
    const playArgs = [process.execPath, playwrightBin, 'test', relative(spec), '--config', config, '--workers=1', '--retries=0'];
    manifest.argv.push(playArgs.map((value,i) => i === 0 ? 'node' : relativeOrValue(value)));
    fs.writeFileSync(path.join(root,'manifest.json'), JSON.stringify(manifest,null,2));
    const playLog = fs.openSync(path.join(root,'playwright.log'),'wx');
    const completed = await runProcess(playArgs, { cwd:app, env, stdio:['ignore',playLog,playLog], detached:process.platform!=='win32' }, deadline);
    result.outcomes.push({ phase:'playwright', ...completed, durationMs:Date.now()-start });
    if (completed.code !== 0) throw new Error(`PLAYWRIGHT_EXIT_${completed.code}`);
  } catch(error) { result.error = String(error.message || error); process.exitCode = 1; }
  finally {
    result.teardown = stopOwned(next);
    await sleep(800);
    result.teardown.portFree = await portFree().then(()=>true,()=>false);
    result.teardown.processGone = !next?.pid || (()=>{ try { process.kill(next.pid,0); return false; } catch { return true; } })();
    const stopped = result.teardown.portFree && result.teardown.processGone && result.teardown.status === 0;
    result.teardown.ownedStopped = stopped;
    let transientBlocked = false;
    for (const [name, bytes] of Object.entries(preimages)) {
      const target = path.join(app,name);
      const current = fs.existsSync(target) ? fs.readFileSync(target) : null;
      const altered = current === null ? bytes !== null : bytes === null || !current.equals(bytes);
      if (altered) {
        if (!stopped || !verifiedNextDelta(name, bytes, current, dist)) { transientBlocked=true; result.outcomes.push({ phase:'transient-restore', file:name, status:'BLOCKED_UNVERIFIED_OR_RUNNING' }); continue; }
        fs.writeFileSync(target, bytes); result.outcomes.push({ phase:'transient-restore', file:name, sha256:sha(bytes) });
      }
    }
    result.teardown.transientExact = !transientBlocked && transient.every(name => fs.readFileSync(path.join(app,name)).equals(preimages[name]));
    const isolationPath = env.CVF_NCR_ISOLATION_LOG;
    if (fs.existsSync(isolationPath)) {
      const events = fs.readFileSync(isolationPath,'utf8').split('\n').filter(Boolean).map(JSON.parse);
      result.isolation = { preloadContexts: events.filter(e=>e.event==='PRELOAD_ACTIVE').length,
        envBlocked:events.filter(e=>e.event==='ENV_READ_BLOCKED').length,
        networkBlocked:events.filter(e=>e.event==='BLOCKED').length,
        evaluateBlocked:events.filter(e=>e.event==='EVALUATE_DISPATCH_BLOCKED').length };
    }
    result.finishedAt = new Date().toISOString(); result.durationMs = Date.now()-start;
    result.outputBudget = { run:treeSize(root), build:treeSize(path.join(app,dist)), snapshots:treeSize(path.join(root,'drafts')) };
    result.outputBudget.withinCaps = result.outputBudget.run.bytes <= 256*1024*1024 && result.outputBudget.build.bytes <= 1024*1024*1024
      && result.outputBudget.snapshots.files <= 32 && result.outputBudget.snapshots.bytes <= 8*1024*1024;
    result.sourceDrift = pins.map(pin=>({ path:pin.path, unchanged:fileInfo(pinPath(pin)).sha256===pin.sha256 }));
    const outputs = ['next.log','playwright.log','isolation.jsonl'].filter(name=>fs.existsSync(path.join(root,name))).map(name=>fileInfo(path.join(root,name)));
    result.outputs = outputs;
    fs.writeFileSync(path.join(root,'result.json'), JSON.stringify(result,null,2));
    process.stdout.write(JSON.stringify({ root, status: process.exitCode ? 'FAIL' : 'PASS', result: path.join(root,'result.json'), teardown:result.teardown, isolation:result.isolation })+'\n');
    if (!result.teardown.ownedStopped || !result.teardown.transientExact || !result.outputBudget.withinCaps || result.sourceDrift.some(item=>!item.unchanged)) process.exitCode=1;
  }
}
function relativeOrValue(value) { return path.isAbsolute(value) && value.startsWith(repo) ? relative(value) : value; }
if (require.main === module) main().catch(error=>{ console.error(String(error.message||error)); process.exitCode=1; });
module.exports = { safeEnvironment, validateBoundary, verifiedNextDelta };
