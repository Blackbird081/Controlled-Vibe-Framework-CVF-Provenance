'use strict';
// Qualified browser delegation for one cooperative owned-profile helper only.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { TextDecoder } = require('node:util');
const KEYS = ['CVF_NCR_BROWSER_BINDING_PATH', 'CVF_NCR_BROWSER_BINDING_SHA256'];
const CHROME = { path: 'C:\\Users\\DELL\\AppData\\Local\\ms-playwright\\chromium-1208\\chrome-win64\\chrome.exe',
  sha256: 'ff0c99fc5bb2301cad77930aa76e5354cf2a5fefb7efdcf3b3bc10ba0550c015' };
const verified = new WeakMap();
const installations = new WeakSet();
const insist = (value, reason) => { if (!value) throw new Error(reason); };
const sha = raw => crypto.createHash('sha256').update(raw).digest('hex');
const sorted = value => Array.isArray(value) ? value.map(sorted) : value && typeof value === 'object'
  ? Object.fromEntries(Object.keys(value).sort().map(k => [k, sorted(value[k])])) : value;
const canonical = value => Buffer.from(JSON.stringify(sorted(value)), 'utf8');
const plain = value => value !== null && typeof value === 'object' && !Array.isArray(value)
  && Object.getPrototypeOf(value) === Object.prototype;
const closed = (value, keys) => insist(plain(value) && Object.keys(value).sort().join('|') === keys.split(' ').sort().join('|'), 'closed object shape');
const hex = value => insist(typeof value === 'string' && /^[0-9a-f]{64}$/.test(value), 'invalid digest');
function absolute(value) {
  insist(typeof value === 'string' && value && !value.includes('\0') && path.isAbsolute(value)
    && path.normalize(value) === value && !value.split(/[\\/]/).includes('..'), 'canonical absolute path required');
}
function pair(value) { closed(value, 'path sha256'); absolute(value.path); hex(value.sha256); }
function checkPath(value) {
  absolute(value);
  for (let item = value; ; item = path.dirname(item)) {
    if (fs.existsSync(item)) insist(!fs.lstatSync(item).isSymbolicLink(), 'reparse path refused');
    if (item === path.dirname(item)) break;
  }
}
function read(value) {
  checkPath(value);
  const stat = fs.statSync(value);
  insist(stat.isFile() && stat.size <= 16 * 1024 * 1024, 'bounded regular file required');
  return fs.readFileSync(value);
}
function productionDeps() {
  return { argv: process.argv, read, checkPath, sha,
    load: name => require(name),
    writeObservation: (name, value) => { checkPath(name); fs.writeFileSync(name, canonical(value)); } };
}
function bytesJSON(raw) {
  insist(Buffer.isBuffer(raw) && raw.length <= 2 * 1024 * 1024, 'bounded JSON bytes required');
  const text = new TextDecoder('utf-8', { fatal: true, ignoreBOM: true }).decode(raw);
  const value = JSON.parse(text);
  insist(canonical(value).equals(raw), 'noncanonical JSON bytes');
  return value;
}
function verifyBinding(bytes, expectedDigest, deps) {
  deps = deps || productionDeps();
  hex(expectedDigest);
  insist(deps.sha(bytes) === expectedDigest, 'binding digest mismatch');
  const binding = bytesJSON(bytes);
  closed(binding, 'schemaVersion runId actor cap entry modulesPath journey preload config profilePath observationPath chrome');
  insist(binding.schemaVersion === 'cvf.ncrHtmlBrowserBinding@1' && typeof binding.runId === 'string'
    && /^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$/.test(binding.runId), 'binding identity');
  insist((binding.actor === 'IMPLEMENTATION_WORKER' && binding.cap === 2)
    || (binding.actor === 'LOCAL_REVIEWER' && binding.cap === 1), 'actor/cap mismatch');
  for (const name of ['entry', 'journey', 'preload', 'config', 'chrome']) pair(binding[name]);
  for (const name of ['modulesPath', 'profilePath', 'observationPath']) absolute(binding[name]);
  insist(canonical(binding.chrome).equals(canonical(CHROME)), 'qualified Chrome required');
  const argv = deps.argv;
  insist(argv.length === 9 && argv[1] === binding.entry.path && argv[2] === binding.modulesPath
    && argv[6] === 'owned-profile' && argv[7] === binding.journey.path && argv[8] === binding.config.path, 'helper argv mismatch');
  insist(path.dirname(binding.config.path) === argv[5] && path.dirname(binding.observationPath) === argv[5], 'observation custody');
  insist(binding.profilePath === path.join(path.dirname(argv[5]), 'source', 'browser-profile'), 'profile ownership');
  for (const name of ['entry', 'journey', 'preload', 'config']) {
    deps.checkPath(binding[name].path);
    insist(deps.sha(deps.read(binding[name].path)) === binding[name].sha256, 'binding file drift');
  }
  deps.checkPath(binding.modulesPath);
  const configRaw = deps.read(binding.config.path);
  const cfg = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(configRaw));
  insist(cfg.cap === binding.cap && cfg.browserProfile === binding.profilePath, 'config identity mismatch');
  const journey = deps.load(binding.journey.path);
  journey.validateInputs(cfg.inputs, cfg.cap);
  // Validate original limits now; no replacement deadline or generation is created.
  journey.authority(cfg);
  verified.set(binding, { digest: expectedDigest, cfg, journey });
  return binding;
}
function installFence(binding, deps) {
  deps = deps || productionDeps();
  const record = verified.get(binding);
  insist(record, 'verified binding required');
  const chromium = deps.load(path.join(binding.modulesPath, '@playwright/test')).chromium;
  insist(chromium && !installations.has(chromium) && typeof chromium.launchPersistentContext === 'function', 'duplicate/invalid browser installation');
  installations.add(chromium);
  const original = chromium.launchPersistentContext;
  let invocations = 0;
  function fenced(profile, options) {
    insist(invocations++ === 0, 'browser call already spent');
    insist(this === chromium && profile === binding.profilePath && plain(options) && options.headless === true,
      'browser receiver/profile/options');
    insist(!('channel' in options) && (!('executablePath' in options) || options.executablePath === binding.chrome.path), 'conflicting browser selection');
    insist(typeof options.timeout === 'number' && Number.isFinite(options.timeout) && options.timeout > 0, 'finite positive timeout required');
    // Recheck the frozen config and binary at the last synchronous boundary.
    insist(deps.sha(deps.read(binding.config.path)) === binding.config.sha256, 'config drift');
    deps.checkPath(binding.chrome.path);
    insist(deps.sha(deps.read(binding.chrome.path)) === binding.chrome.sha256, 'Chrome byte drift');
    const observation = { schemaVersion: 'cvf.ncrHtmlBrowserFenceObservation@1', runId: binding.runId,
      actor: binding.actor, cap: binding.cap, bindingSha256: record.digest, configSha256: binding.config.sha256,
      preloadSha256: binding.preload.sha256, chrome: binding.chrome, verified: true, invocations: 1 };
    deps.writeObservation(binding.observationPath, observation);
    const timeout = record.journey.authority(record.cfg).work(options.timeout);
    insist(Number.isInteger(timeout) && timeout > 0 && timeout <= options.timeout, 'invalid restrictive allowance');
    return original.call(this, profile, { ...options, timeout, executablePath: binding.chrome.path });
  }
  chromium.launchPersistentContext = fenced;
  insist(chromium.launchPersistentContext === fenced, 'browser patch not installed');
  return { snapshot: () => ({ invocations }) };
}
module.exports = { verifyBinding, installFence };
const present = KEYS.map(key => Object.hasOwn(process.env, key));
if (present.some(Boolean)) {
  insist(present.every(Boolean), 'partial browser binding environment');
  const deps = productionDeps();
  const location = process.env[KEYS[0]];
  absolute(location);
  const binding = verifyBinding(deps.read(location), process.env[KEYS[1]], deps);
  insist(binding.preload.path === __filename, 'preload identity mismatch');
  installFence(binding, deps);
}
