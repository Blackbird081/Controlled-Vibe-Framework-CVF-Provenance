import { createHash } from 'node:crypto';
import * as fs from 'node:fs/promises';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  attemptIdFor, buildEnvelope, makeOperationConfig, operationKey, type ControlledEvaluateRequest, type ControlledInvoker, type OperationConfig,
} from '@/lib/artifacts-receipt-operation-contract';
import { HtmlDraftSnapshotStore } from '@/lib/server/html-draft-snapshot-store';
import {
  buildControlledEvaluateRequest, controlledRequestSha256, diagnoseRemotePresence, fetchGovernanceReceipt, invokeWithGrant, parseControlledReceipt,
  runControlledReceipt, type ControlledReceiptOptions, type ReceiptOperationStore,
} from './proof';

const ROOTS = path.resolve(process.cwd(), '..', '..', '..', '.cvf', 'runtime', 'ncr-r2-w05-offline-source-20261019', 'worker', 'roots');
const owner = { userId: 'u1', orgId: 'o1', teamId: 't1' };
const hex = (text: string) => createHash('sha256').update(text).digest('hex');
const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));
const config = makeOperationConfig({ policyRevision: 'policy-r1', transformRevision: 'transform-1', endpointId: 'synthetic-endpoint-1',
  storeId: 'synthetic-store-1', authReference: 'no-credential-synthetic-fixture', authScope: 'NONE' })!;
const jobId = '123e4567-e89b-42d3-a456-426614174001';
const NOW = Date.parse('2026-10-19T01:00:00.000Z');

async function newRoot(label: string) {
  await fs.mkdir(ROOTS, { recursive: true });
  return fs.realpath(await fs.mkdtemp(path.join(ROOTS, `${label}-`)));
}
const makeStore = (root: string, enabled = true) =>
  new HtmlDraftSnapshotStore({ kind: 'local-synthetic', root, production: false, ...(enabled ? { receiptOperations: true as const } : {}) }, () => NOW);
const opsDir = (root: string) => path.join(root, hex(JSON.stringify([owner.userId, owner.orgId, owner.teamId])), 'operations');

interface Prep { html?: string; job?: string; version?: string | null; cfg?: OperationConfig; content?: string }
function prepared(index: number, prep: Prep = {}) {
  const sourceRecordId = `ncr-synthetic-${index}`;
  const requestSha256 = hex(`request-${index}`);
  const key = operationKey({ owner, sourceRecordId, requestSha256 })!;
  const attemptId = attemptIdFor(key);
  const request = buildControlledEvaluateRequest(attemptId, 'receipt-anchor', prep.content ?? `# source ${index}`);
  const envelope = buildEnvelope({ owner, sourceRecordId, requestSha256, jobId: prep.job ?? jobId, versionId: prep.version ?? null, attemptId,
    payloadSha256: controlledRequestSha256(request), config: prep.cfg ?? config,
    output: { generatedAt: '2026-10-19T01:00:00.000Z', sourceHash: hex(`source-${index}`), htmlSha256: prep.html ?? hex(`html-${index}`), artifactId: 'receipt-anchor', filename: 'review.html' } })!;
  return { envelope, request, attemptId, key };
}
type Prepared = ReturnType<typeof prepared>;

const ACTION: Record<string, string> = { ALLOW: 'ALLOW', DENY: 'BLOCK', REVIEW: 'NEEDS_APPROVAL', ESCALATE: 'ESCALATE', SANDBOX: 'LOG_ONLY' };
function engine(request: ControlledEvaluateRequest, fault: string | null = null, decision = 'ALLOW') {
  return { success: fault === 'string-success' ? 'false' : true, data: fault === 'no-data' ? undefined : {
    report: { request_summary: { request_id: fault === 'request-id' ? 'other' : request.request_id, artifact_id: fault === 'artifact-id' ? 'other' : request.artifact_id },
      decision_analysis: { final_decision: decision }, report_metadata: { generated_at: '2026-10-19T01:00:01.000Z' },
      cvf_risk_level: fault === 'risk-r0' ? 'R0' : 'R1', cvf_enforcement: { action: fault === 'enforcement' ? 'LOG_ONLY' : ACTION[decision] },
      integrity: { has_ledger_reference: fault !== 'ledger-ref' } },
    execution_record: { final_decision: fault === 'decision' ? 'DENY' : decision, ledger_attached: fault !== 'ledger' } } };
}
function counting(respond: (request: ControlledEvaluateRequest, signal: AbortSignal) => unknown) {
  const calls: Array<{ request: ControlledEvaluateRequest; signal: AbortSignal }> = [];
  const invoker: ControlledInvoker = async (request, signal) => { calls.push({ request, signal }); return respond(request, signal); };
  return { invoker, calls };
}
const run = (store: ReceiptOperationStore, p: Prepared, invoker: ControlledInvoker, extra: Partial<ControlledReceiptOptions> = {}) =>
  runControlledReceipt({ store, owner, envelope: p.envelope, request: p.request, invoker, timeoutMs: 2000, ...extra });
function wrapped(real: HtmlDraftSnapshotStore, overrides: Partial<ReceiptOperationStore>): ReceiptOperationStore {
  return { admitOperation: (e, o) => real.admitOperation(e, o), startOperation: (o, k, i) => real.startOperation(o, k, i),
    consumeGrant: (g, i) => real.consumeGrant(g, i), writeOutcome: (c, i) => real.writeOutcome(c, i), ...overrides };
}
const hang = () => new Promise<never>(() => undefined);
const snapshot = async (root: string) => Promise.all((await fs.readdir(opsDir(root))).sort().map(async name => `${name}:${hex((await fs.readFile(path.join(opsDir(root), name))).toString('binary'))}`));

const fetchMock = vi.fn();
beforeEach(() => { fetchMock.mockReset(); vi.stubGlobal('fetch', fetchMock); });
afterEach(() => { vi.unstubAllGlobals(); });

describe('PC/REQ-PROOF one injected send and exact joined outcome', () => {
  it('invokes the injected callback once with the exact R1/REVIEW payload and stores the joined verified receipt', async () => {
    const root = await newRoot('proof-positive');
    const store = makeStore(root);
    const p = prepared(1);
    const { invoker, calls } = counting(request => engine(request));
    const result = await run(store, p, invoker);
    expect(result).toMatchObject({ kind: 'EXECUTED', outcome: 'RECEIPT_VERIFIED', persisted: true, sends: 1, operationKey: p.key, reason: null });
    expect(calls).toHaveLength(1);
    expect(calls[0].request).toEqual({ request_id: p.attemptId, artifact_id: 'receipt-anchor', payload: { content: '# source 1' }, cvf_phase: 'REVIEW', cvf_risk_level: 'R1' });
    expect(controlledRequestSha256(calls[0].request)).toBe(p.envelope.payloadSha256);
    expect(calls[0].request).not.toBe(p.request);
    expect(calls[0].signal.aborted).toBe(false);
    const state = await store.readOperation(p.key, owner);
    expect(state.state).toBe('OUTCOME');
    if (state.state === 'OUTCOME') {
      expect(state.outcome.receipt).toEqual({ receiptId: p.attemptId, decision: 'ALLOW', evaluatedAt: '2026-10-19T01:00:01.000Z', riskLevel: 'R1' });
      expect(state.outcome.attemptId).toBe(p.envelope.attemptId);
      expect(state.intent.envelope).toEqual(p.envelope);
    }
    expect(fetchMock).not.toHaveBeenCalled();
  });
  it('slices the evaluated content to 500 characters and keeps fixed R1/REVIEW fields', () => {
    expect(buildControlledEvaluateRequest('ncr-op-aaaaaaaa', 'a', 'x'.repeat(900)).payload.content).toHaveLength(500);
    expect(buildControlledEvaluateRequest('ncr-op-aaaaaaaa', 'a', 'x')).toMatchObject({ cvf_phase: 'REVIEW', cvf_risk_level: 'R1' });
  });
  it('reuses an identical verified target with zero sends and never attaches the receipt to a different target', async () => {
    const root = await newRoot('proof-reuse');
    const store = makeStore(root);
    const p = prepared(1);
    const { invoker, calls } = counting(request => engine(request));
    await run(store, p, invoker);
    const again = await run(makeStore(root), p, invoker);
    expect(again).toMatchObject({ kind: 'REUSED', sends: 0, receipt: { receiptId: p.attemptId, decision: 'ALLOW' } });
    for (const changed of [prepared(1, { html: hex('newly rendered html') }), prepared(1, { job: '123e4567-e89b-42d3-a456-426614174077' }),
      prepared(1, { version: '123e4567-e89b-42d3-a456-426614174078' }),
      prepared(1, { cfg: makeOperationConfig({ policyRevision: 'policy-r2', transformRevision: 'transform-1', endpointId: 'synthetic-endpoint-1', storeId: 'synthetic-store-1', authReference: 'x', authScope: 'NONE' })! })]) {
      expect(changed.key).toBe(p.key);
      const mismatch = await run(store, changed, invoker);
      expect(mismatch).toEqual({ kind: 'ALREADY_PROCESSED', operationKey: p.key, state: 'OUTCOME', outcome: 'RECEIPT_VERIFIED', sends: 0 });
      expect(JSON.stringify(mismatch)).not.toMatch(/"receipt"|html/i);
    }
    expect(calls).toHaveLength(1);
  });
  it('maps a remote DENY to DENIED and never reuses it; review decisions stay verified receipts', async () => {
    const root = await newRoot('proof-decisions');
    const store = makeStore(root);
    const deny = prepared(1);
    const denied = counting(request => engine(request, null, 'DENY'));
    expect(await run(store, deny, denied.invoker)).toMatchObject({ kind: 'EXECUTED', outcome: 'DENIED', receipt: { decision: 'DENY' }, persisted: true });
    expect(await run(store, deny, denied.invoker)).toMatchObject({ kind: 'ALREADY_PROCESSED', outcome: 'DENIED', sends: 0 });
    expect(denied.calls).toHaveLength(1);
    for (const [index, decision] of [[2, 'REVIEW'], [3, 'ESCALATE'], [4, 'SANDBOX']] as const) {
      const p = prepared(index);
      const { invoker } = counting(request => engine(request, null, decision));
      expect(await run(store, p, invoker)).toMatchObject({ kind: 'EXECUTED', outcome: 'RECEIPT_VERIFIED', receipt: { decision, riskLevel: 'R1' } });
    }
  });
  it.each(['request-id', 'artifact-id', 'decision', 'ledger', 'ledger-ref', 'enforcement', 'risk-r0', 'string-success', 'no-data'])(
    'records an invalid current-engine response (%s) as OUTCOME_UNKNOWN with no receipt and no replay', async fault => {
      const root = await newRoot('proof-invalid');
      const store = makeStore(root);
      const p = prepared(1);
      const { invoker, calls } = counting(request => engine(request, fault));
      expect(await run(store, p, invoker)).toMatchObject({ kind: 'EXECUTED', outcome: 'OUTCOME_UNKNOWN', receipt: null, reason: 'INVALID_RESPONSE', persisted: true });
      expect(await run(store, p, invoker)).toMatchObject({ kind: 'ALREADY_PROCESSED', outcome: 'OUTCOME_UNKNOWN', sends: 0 });
      const rejob = prepared(1, { job: '123e4567-e89b-42d3-a456-426614174077' });
      expect(await run(store, rejob, invoker)).toMatchObject({ kind: 'ALREADY_PROCESSED', outcome: 'OUTCOME_UNKNOWN', sends: 0 });
      expect(calls).toHaveLength(1);
    });
  it('does not accept the older explicit approval envelope on the controlled path', async () => {
    const p = prepared(1);
    const legacy = { success: true, data: { report: { status: 'APPROVED', risk_level: 'R1', cvf_enforcement: { action: 'ALLOW' } },
      execution_record: { request_id: p.attemptId, timestamp: '2026-10-19T01:00:01.000Z' } } };
    expect(parseControlledReceipt(legacy, p.request)).toBeNull();
    expect(parseControlledReceipt(engine(p.request), p.request)).not.toBeNull();
    expect(parseControlledReceipt(null, p.request)).toBeNull();
    expect(parseControlledReceipt(engine(p.request, null, 'constructor'), p.request)).toBeNull();
  });
});

describe('PC/REQ-PROOF failure, timeout, abort and late response keep unknown', () => {
  it.each([
    ['rejecting invoker', () => Promise.reject(new Error('network down'))],
    ['synchronously throwing invoker', () => { throw new Error('boom'); }],
  ])('records %s as OUTCOME_UNKNOWN and denies replay', async (_label, respond) => {
    const root = await newRoot('proof-throw');
    const store = makeStore(root);
    const p = prepared(1);
    const { invoker, calls } = counting(respond);
    expect(await run(store, p, invoker)).toMatchObject({ kind: 'EXECUTED', outcome: 'OUTCOME_UNKNOWN', reason: 'INVOKER_ERROR', receipt: null, sends: 1 });
    expect(await run(store, p, invoker)).toMatchObject({ kind: 'ALREADY_PROCESSED', sends: 0 });
    expect(calls).toHaveLength(1);
  });
  it('treats an invoker that throws synchronously as an unknown outcome after one call', async () => {
    const root = await newRoot('proof-sync-throw');
    const store = makeStore(root);
    const p = prepared(1);
    let calls = 0;
    const invoker = ((): Promise<unknown> => { calls += 1; throw new Error('sync failure'); }) as ControlledInvoker;
    expect(await run(store, p, invoker)).toMatchObject({ kind: 'EXECUTED', outcome: 'OUTCOME_UNKNOWN', reason: 'INVOKER_ERROR', sends: 1 });
    expect(await run(store, p, invoker)).toMatchObject({ kind: 'ALREADY_PROCESSED', sends: 0 });
    expect(calls).toBe(1);
  });
  it('marks a timeout unknown, aborts the signal, and a late success cannot publish or release the operation', async () => {
    const root = await newRoot('proof-timeout');
    const store = makeStore(root);
    const p = prepared(1);
    const { invoker, calls } = counting(async request => { await sleep(900); return engine(request); });
    const started = Date.now();
    const result = await run(store, p, invoker, { timeoutMs: 250 });
    expect(Date.now() - started).toBeLessThan(800);
    expect(result).toMatchObject({ kind: 'EXECUTED', outcome: 'OUTCOME_UNKNOWN', reason: 'TIMED_OUT', receipt: null, persisted: true });
    expect(calls[0].signal.aborted).toBe(true);
    await sleep(1300);
    const state = await store.readOperation(p.key, owner);
    expect(state.state === 'OUTCOME' && state.outcome).toMatchObject({ outcome: 'OUTCOME_UNKNOWN', reason: 'TIMED_OUT', receipt: null });
    expect(await run(store, p, invoker)).toMatchObject({ kind: 'ALREADY_PROCESSED', outcome: 'OUTCOME_UNKNOWN', sends: 0 });
    expect(calls).toHaveLength(1);
  });
  it('marks an external abort during flight unknown and records FAILED_BEFORE_SEND for a pre-aborted signal with zero sends', async () => {
    const root = await newRoot('proof-abort');
    const store = makeStore(root);
    const during = prepared(1);
    const controller = new AbortController();
    const slow = counting(async request => { controller.abort(); await sleep(200); return engine(request); });
    expect(await run(store, during, slow.invoker, { signal: controller.signal })).toMatchObject({ kind: 'EXECUTED', outcome: 'OUTCOME_UNKNOWN', reason: 'ABORTED', sends: 1 });
    expect(slow.calls[0].signal.aborted).toBe(true);
    const before = prepared(2);
    const aborted = new AbortController();
    aborted.abort();
    const never = counting(request => engine(request));
    expect(await run(store, before, never.invoker, { signal: aborted.signal })).toEqual({ kind: 'DENIED', reason: 'FAILED_BEFORE_SEND', sends: 0 });
    expect(never.calls).toHaveLength(0);
    const state = await store.readOperation(before.key, owner);
    expect(state.state === 'OUTCOME' && state.outcome).toMatchObject({ outcome: 'FAILED_BEFORE_SEND', reason: 'ABORTED_BEFORE_SEND' });
    expect(await run(store, before, never.invoker)).toMatchObject({ kind: 'ALREADY_PROCESSED', outcome: 'FAILED_BEFORE_SEND', sends: 0 });
    expect(never.calls).toHaveLength(0);
  });
  it('yields unknown, not a verified receipt, when the outcome write fails, hangs or throws', async () => {
    for (const [label, writeOutcome] of [
      ['unconfirmed', async () => ({ kind: 'UNCONFIRMED' as const })],
      ['hanging', hang],
      ['throwing', async () => { throw new Error('disk'); }],
    ] as const) {
      const root = await newRoot(`proof-write-${label}`);
      const real = makeStore(root);
      const p = prepared(1);
      const { invoker, calls } = counting(request => engine(request));
      const started = Date.now();
      const result = await run(wrapped(real, { writeOutcome }), p, invoker, { timeoutMs: 400 });
      expect(Date.now() - started, label).toBeLessThan(1500);
      expect(result, label).toMatchObject({ kind: 'EXECUTED', outcome: 'OUTCOME_UNKNOWN', receipt: null, persisted: false, reason: 'OUTCOME_WRITE_UNCONFIRMED', sends: 1 });
      expect((await real.readOperation(p.key, owner)).state, label).toBe('STARTED');
      expect(await run(real, p, invoker), label).toMatchObject({ kind: 'ALREADY_PROCESSED', state: 'STARTED', sends: 0 });
      expect(calls, label).toHaveLength(1);
    }
  });
  it('denies before invoking when admission or start errors or hangs', async () => {
    const root = await newRoot('proof-pre-faults');
    const real = makeStore(root);
    const { invoker, calls } = counting(request => engine(request));
    const cases: Array<[string, Partial<ReceiptOperationStore>]> = [
      ['admit throws', { admitOperation: async () => { throw new Error('x'); } }],
      ['admit hangs', { admitOperation: hang }],
      ['start hangs', { startOperation: hang }],
      ['start throws', { startOperation: async () => { throw new Error('x'); } }],
    ];
    for (const [index, [label, override]] of cases.entries()) {
      expect(await run(wrapped(real, override), prepared(10 + index), invoker, { timeoutMs: 40 }), label).toEqual({ kind: 'DENIED', reason: 'STORE_UNAVAILABLE', sends: 0 });
    }
    expect(calls).toHaveLength(0);
  });
});

describe('PC/REQ-PROOF grant and input denial with zero sends', () => {
  it('rejects fabricated, copied, wrong-invoker and spent grants before invoking', async () => {
    const root = await newRoot('proof-grant');
    const store = makeStore(root);
    const p = prepared(1);
    const { invoker, calls } = counting(request => engine(request));
    expect((await store.admitOperation(p.envelope, owner)).kind).toBe('ADMITTED');
    const started = await store.startOperation(owner, p.key, invoker);
    if (started.kind !== 'STARTED') throw new Error('start');
    const options: ControlledReceiptOptions = { store, owner, envelope: p.envelope, request: p.request, invoker, timeoutMs: 2000 };
    const denied = { kind: 'DENIED', reason: 'GRANT_REJECTED', sends: 0 };
    expect(await invokeWithGrant(options, { kind: 'OPERATION_GRANT' })).toEqual(denied);
    expect(await invokeWithGrant(options, { ...started.grant })).toEqual(denied);
    expect(await invokeWithGrant(options, null)).toEqual(denied);
    expect(await invokeWithGrant({ ...options, invoker: counting(() => ({})).invoker }, started.grant)).toEqual(denied);
    expect(calls).toHaveLength(0);
    expect(await invokeWithGrant(options, started.grant)).toMatchObject({ kind: 'EXECUTED', outcome: 'RECEIPT_VERIFIED', sends: 1 });
    expect(await invokeWithGrant(options, started.grant)).toEqual(denied);
    expect(calls).toHaveLength(1);
  });
  it('denies invalid proof input, a disabled profile, a full namespace and a corrupt existing record with zero sends', async () => {
    const root = await newRoot('proof-denials');
    const store = makeStore(root);
    const { invoker, calls } = counting(request => engine(request));
    const p = prepared(1);
    const bad: Array<[string, Partial<ControlledReceiptOptions>]> = [
      ['tampered envelope', { envelope: { ...p.envelope, callLimit: 2 } }],
      ['payload digest mismatch', { request: { ...p.request, payload: { content: 'changed' } } }],
      ['phase', { request: { ...p.request, cvf_phase: 'EXECUTE' } as never }],
      ['risk', { request: { ...p.request, cvf_risk_level: 'R0' } as never }],
      ['attempt id', { request: { ...p.request, request_id: 'ncr-op-someoneelse' } }],
      ['artifact id', { request: { ...p.request, artifact_id: 'other-anchor' } }],
      ['timeout zero', { timeoutMs: 0 }], ['timeout high', { timeoutMs: 30_001 }], ['timeout fraction', { timeoutMs: 1.5 }], ['timeout NaN', { timeoutMs: Number.NaN }],
      ['invoker', { invoker: 'not-a-function' as never }],
    ];
    for (const [label, override] of bad) expect(await run(store, p, invoker, override), label).toEqual({ kind: 'DENIED', reason: 'INVALID_PROOF_INPUT', sends: 0 });
    expect(await run(makeStore(root, false), p, invoker)).toEqual({ kind: 'DENIED', reason: 'DISABLED', sends: 0 });
    const fullRoot = await newRoot('proof-full');
    await fs.mkdir(opsDir(fullRoot), { recursive: true, mode: 0o700 });
    for (let i = 0; i < 256; i++) await fs.writeFile(path.join(opsDir(fullRoot), `slot-${String(i).padStart(3, '0')}.json`), Buffer.alloc(0));
    expect(await run(makeStore(fullRoot), p, invoker)).toEqual({ kind: 'DENIED', reason: 'CAPACITY_FULL', sends: 0 });
    const corruptRoot = await newRoot('proof-corrupt');
    const corrupt = makeStore(corruptRoot);
    await corrupt.admitOperation(p.envelope, owner);
    await fs.writeFile(path.join(opsDir(corruptRoot), `op-${p.key}.intent.json`), '{garbage');
    expect(await run(corrupt, p, invoker)).toEqual({ kind: 'DENIED', reason: 'OPERATION_CORRUPT', sends: 0 });
    expect(calls).toHaveLength(0);
    expect(fetchMock).not.toHaveBeenCalled();
  });
});

describe('PD/REQ-PROOF Reconcile B is a presence diagnostic only', () => {
  const entry = (p: Prepared, patch: Record<string, string> = {}) => ({ requestId: p.attemptId, actor: owner.userId, configDigest: config.configDigest, storeId: config.storeId, ...patch });
  it('observes presence only for the exact attempt, actor, config and store and never releases or invokes', async () => {
    const p = prepared(1);
    const flags = { releasesUnknown: false, grantsReplay: false };
    expect(await diagnoseRemotePresence(async () => entry(p), p.envelope)).toEqual({ status: 'REMOTE_PRESENCE_OBSERVED', ...flags });
    for (const lookup of [
      async () => null, async () => undefined, async () => entry(p, { requestId: 'other-attempt' }), async () => entry(p, { actor: 'someone-else' }),
      async () => entry(p, { configDigest: '0'.repeat(64) }), async () => entry(p, { storeId: 'synthetic-other-store' }),
      async () => { throw new Error('ledger down'); }, hang,
    ]) expect(await diagnoseRemotePresence(lookup, p.envelope, 40)).toEqual({ status: 'UNKNOWN', ...flags });
    expect(fetchMock).not.toHaveBeenCalled();
  });
  it('leaves an UNKNOWN operation unchanged and unreplayable even when the lookup reports presence', async () => {
    const root = await newRoot('proof-reconcile');
    const store = makeStore(root);
    const p = prepared(1);
    const { invoker, calls } = counting(request => { throw new Error(`down ${request.request_id}`); });
    expect(await run(store, p, invoker)).toMatchObject({ outcome: 'OUTCOME_UNKNOWN' });
    const before = await snapshot(root);
    const lookup = vi.fn(async () => entry(p));
    expect(await diagnoseRemotePresence(lookup, p.envelope)).toMatchObject({ status: 'REMOTE_PRESENCE_OBSERVED', releasesUnknown: false, grantsReplay: false });
    expect(lookup).toHaveBeenCalledTimes(1);
    expect(await snapshot(root)).toEqual(before);
    expect(await run(store, p, invoker)).toMatchObject({ kind: 'ALREADY_PROCESSED', outcome: 'OUTCOME_UNKNOWN', sends: 0 });
    expect(calls).toHaveLength(1);
  });
});

describe('PF/REQ-PROOF legacy helper is retained separately', () => {
  it('still sends the legacy R0 REVIEW request through global fetch and parses the same response shape', async () => {
    const prior = process.env.NEXTAUTH_URL;
    process.env.NEXTAUTH_URL = 'http://localhost:3000';
    try {
      fetchMock.mockImplementation(async (_url: string, options: RequestInit) => {
        const sent = JSON.parse(String(options.body)) as ControlledEvaluateRequest;
        return { ok: true, json: async () => engine(sent, 'risk-r0') };
      });
      const legacy = await fetchGovernanceReceipt('legacy-anchor', 'x'.repeat(900));
      expect(fetchMock).toHaveBeenCalledTimes(1);
      const sent = JSON.parse(String(fetchMock.mock.calls[0][1].body)) as Record<string, unknown>;
      expect(sent).toMatchObject({ cvf_phase: 'REVIEW', cvf_risk_level: 'R0', artifact_id: 'legacy-anchor', payload: { content: 'x'.repeat(500) } });
      expect(legacy).toMatchObject({ status: 'PRESENT', receipt: { decision: 'ALLOW', riskLevel: 'R0' } });
    } finally {
      if (prior === undefined) delete process.env.NEXTAUTH_URL; else process.env.NEXTAUTH_URL = prior;
    }
  });
});
