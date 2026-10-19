/** Isolated fixture repository for unverified HTML drafts. No active-data profile is wired. */
import { randomBytes } from 'node:crypto';
import * as fs from 'node:fs/promises';
import path from 'node:path';
import { MAX_OPERATIONS_PER_OWNER, MAX_OPERATION_RECORD_BYTES, decodeRecord, makeIntent, makeOutcome, makeReservation, makeStart, ownerSha256,
  parseEnvelope, parseIntent, parseOutcome, parseReservation, parseStart, recordBytes,
  type IntentRecord, type OutcomeInput, type OutcomeRecord, type OperationEnvelope, type StartRecord } from '../artifacts-receipt-operation-contract';
import { DRAFT_TTL_MS, MAX_SNAPSHOT_BYTES, SOURCE_ID, VERSION_ID, makeSnapshot, sha256, validateSnapshot,
  type DraftInput, type DraftPrincipal, type DraftSnapshot } from '../html-draft-recovery-contract';
import { MAX_JOB_METADATA_BYTES, makeDecision, makeJob, makeVersion, parseAcceptVersion, parseCreateJob, parseLinkVersion,
  reviewMatches, validateDecision, validateJob, validateVersion,
  type AcceptVersionInput, type CreateJobInput, type HtmlJob, type HtmlJobDecision, type HtmlJobVersion, type LinkVersionInput } from '../html-job-contract';

export interface SyntheticDraftProfile {
  kind: 'local-synthetic';
  root: string;
  production: false;
  jobDecisions?: true;
  /** Fixture-only: enables the immutable receipt-operation records in the operations child directory. */
  receiptOperations?: true;
}
export type SaveOutcome = 'SAVED' | 'COLLISION' | 'UNCONFIRMED' | 'UNAVAILABLE';
const safePrincipal = (p: DraftPrincipal) => [p.userId, p.orgId, p.teamId].every(v => typeof v === 'string' && v.length > 0 && v.length <= 150 && /^[A-Za-z0-9_-]+$/.test(v));
const sameOwner = (a: DraftPrincipal, b: DraftPrincipal) => a.userId === b.userId && a.orgId === b.orgId && a.teamId === b.teamId;

export type OperationState =
  | { state: 'ABSENT' }
  | { state: 'INTENT'; intent: IntentRecord }
  | { state: 'STARTED'; intent: IntentRecord; start: StartRecord }
  | { state: 'OUTCOME'; intent: IntentRecord; start: StartRecord; outcome: OutcomeRecord }
  | { state: 'CORRUPT' | 'UNCONFIRMED' | 'UNSUPPORTED'; reason: string };
export type ExistingOperation = Exclude<OperationState, { state: 'ABSENT' }>;
export type OperationDenial = 'DISABLED' | 'INVALID_INPUT' | 'UNSAFE_NAMESPACE' | 'CAPACITY_FULL' | 'UNKNOWN_ENTRY' | 'SCAN_BOUND_EXCEEDED'
  | 'RESERVATION_UNCONFIRMED' | 'INTENT_UNCONFIRMED' | 'NO_INTENT' | 'START_UNCONFIRMED' | 'LOOKUP_FAILED';
export type AdmitResult = { kind: 'ADMITTED'; intent: IntentRecord } | { kind: 'EXISTING'; operation: ExistingOperation } | { kind: 'DENIED'; reason: OperationDenial };
export type StartResult = { kind: 'STARTED'; grant: OperationGrant } | { kind: 'EXISTING'; operation: ExistingOperation } | { kind: 'DENIED'; reason: OperationDenial };
export type OutcomeWrite = { kind: 'SAVED'; outcome: OutcomeRecord } | { kind: 'COLLISION' | 'UNCONFIRMED' | 'UNAVAILABLE' };
/** Opaque in-memory single-use grant. Only a verified exclusive STARTED create mints one; copies and fabrications are not recognized. */
export interface OperationGrant { readonly kind: 'OPERATION_GRANT' }
export interface ConsumedGrant { owner: DraftPrincipal; operationKey: string; envelopeSha256: string; attemptId: string; startNonce: string }
interface GrantState extends ConsumedGrant { store: object; invoker: unknown; spent: boolean }
const grants = new WeakMap<object, GrantState>();
const OPERATIONS_DIR = 'operations';
const SLOT_FILE = /^slot-(\d{3})\.json$/;
const LIFECYCLE_FILE = /^op-[a-f0-9]{64}\.(?:intent|start|outcome)\.json$/;
const MAX_OPERATION_ENTRIES = MAX_OPERATIONS_PER_OWNER * 4;
const slotName = (slot: number) => `slot-${String(slot).padStart(3, '0')}.json`;
const lifecycleName = (key: string, kind: 'intent' | 'start' | 'outcome') => `op-${key}.${kind}.json`;
const errno = (error: unknown) => (error as NodeJS.ErrnoException).code;
type FileRead = { kind: 'MISSING' } | { kind: 'OK'; bytes: Buffer } | { kind: 'CORRUPT' | 'UNCONFIRMED'; reason: string };
type RecordRead<T> = { kind: 'MISSING' } | { kind: 'OK'; value: T } | { kind: 'BAD'; state: 'CORRUPT' | 'UNCONFIRMED' | 'UNSUPPORTED'; reason: string };

export class HtmlDraftSnapshotStore {
  private readonly root: string;
  private readonly jobDecisions: boolean;
  private readonly receiptOperations: boolean;
  constructor(profile: SyntheticDraftProfile, private readonly clock: () => number = Date.now) {
    if (profile.kind !== 'local-synthetic' || profile.production !== false || !path.isAbsolute(profile.root)
      || path.resolve(profile.root) === path.parse(profile.root).root || profile.root.startsWith('\\\\')) {
      throw new Error('SYNTHETIC_PROFILE_REQUIRED');
    }
    this.root = path.resolve(profile.root);
    this.jobDecisions = profile.jobDecisions === true;
    this.receiptOperations = profile.receiptOperations === true;
  }
  private async directory(owner: DraftPrincipal, create: boolean): Promise<string | null> {
    if (!safePrincipal(owner)) throw new Error('INVALID_PRINCIPAL');
    const rootStat = await fs.lstat(this.root);
    if (!rootStat.isDirectory() || rootStat.isSymbolicLink() || await fs.realpath(this.root) !== this.root) throw new Error('UNSAFE_ROOT');
    const dir = path.join(this.root, sha256(JSON.stringify([owner.userId, owner.orgId, owner.teamId])));
    if (create) {
      try { await fs.mkdir(dir, { mode: 0o700 }); }
      catch (error) { if ((error as NodeJS.ErrnoException).code !== 'EEXIST') throw error; }
    }
    let stat;
    try { stat = await fs.lstat(dir); }
    catch (error) { if (!create && (error as NodeJS.ErrnoException).code === 'ENOENT') return null; throw error; }
    if (!stat.isDirectory() || stat.isSymbolicLink() || await fs.realpath(dir) !== dir) throw new Error('UNSAFE_NAMESPACE');
    return dir;
  }
  async save(input: DraftInput, owner: DraftPrincipal): Promise<SaveOutcome> {
    if (!safePrincipal(owner) || !VERSION_ID.test(input.versionId) || !SOURCE_ID.test(input.sourceRecordId)) return 'UNAVAILABLE';
    let snapshot: DraftSnapshot;
    try { snapshot = makeSnapshot(input, owner, this.clock()); }
    catch { return 'UNAVAILABLE'; }
    try {
      const dir = (await this.directory(owner, true))!;
      const file = path.join(dir, `${input.versionId}.json`);
      // Exclusive create: even an incomplete prior file consumes the ID. Never overwrite or retry.
      let handle;
      try { handle = await fs.open(file, 'wx', 0o600); }
      catch (error) { return (error as NodeJS.ErrnoException).code === 'EEXIST' ? 'COLLISION' : 'UNAVAILABLE'; }
      try { await handle.writeFile(JSON.stringify(snapshot), 'utf8'); await handle.sync(); }
      catch { return 'UNCONFIRMED'; }
      finally { try { await handle.close(); } catch { /* readback determines availability */ } }
      const stored = await this.get(input.versionId, input.sourceRecordId, owner);
      return stored && JSON.stringify(stored) === JSON.stringify(snapshot) ? 'SAVED' : 'UNCONFIRMED';
    } catch { return 'UNAVAILABLE'; }
  }
  async get(versionId: string, sourceRecordId: string, owner: DraftPrincipal): Promise<DraftSnapshot | null> {
    if (!VERSION_ID.test(versionId) || !SOURCE_ID.test(sourceRecordId)) return null;
    try {
      const dir = await this.directory(owner, false);
      if (!dir) return null;
      const file = path.join(dir, `${versionId}.json`);
      const stat = await fs.lstat(file);
      if (!stat.isFile() || stat.isSymbolicLink() || stat.size > MAX_SNAPSHOT_BYTES || stat.size === 0) return null;
      const bytes = await fs.readFile(file);
      if (bytes.byteLength !== stat.size || bytes.byteLength > MAX_SNAPSHOT_BYTES) return null;
      const value = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes));
      const snapshot = validateSnapshot(value, owner, this.clock());
      return snapshot?.versionId === versionId && snapshot.sourceRecordId === sourceRecordId ? snapshot : null;
    } catch { return null; }
  }
  async list(sourceRecordId: string, owner: DraftPrincipal): Promise<Array<Pick<DraftSnapshot, 'versionId' | 'sourceRecordId' | 'filename' | 'generatedAt' | 'createdAt' | 'expiresAt' | 'state' | 'acceptance'>>> {
    if (!SOURCE_ID.test(sourceRecordId)) return [];
    try {
      const dir = await this.directory(owner, false);
      if (!dir) return [];
      const entries = await fs.readdir(dir);
      const valid: DraftSnapshot[] = [];
      for (const entry of entries) {
        if (!entry.endsWith('.json') || !VERSION_ID.test(entry.slice(0, -5))) continue;
        const snapshot = await this.get(entry.slice(0, -5), sourceRecordId, owner);
        if (snapshot) valid.push(snapshot);
      }
      return valid.sort((a, b) => b.createdAt.localeCompare(a.createdAt) || a.versionId.localeCompare(b.versionId))
        .slice(0, 8).map(({ versionId, sourceRecordId: record, filename, generatedAt, createdAt, expiresAt, state, acceptance }) => ({
          versionId, sourceRecordId: record, filename, generatedAt, createdAt, expiresAt, state, acceptance,
        }));
    } catch { return []; }
  }
  static readonly fixtureTtlMs = DRAFT_TTL_MS;

  private async readSidecar(name: string, owner: DraftPrincipal): Promise<unknown | null> {
    try {
      const dir = await this.directory(owner, false);
      if (!dir) return null;
      const file = path.join(dir, name);
      const stat = await fs.lstat(file);
      if (!stat.isFile() || stat.isSymbolicLink() || stat.size < 1 || stat.size > MAX_JOB_METADATA_BYTES) return null;
      const bytes = await fs.readFile(file);
      if (bytes.byteLength !== stat.size || bytes.byteLength > MAX_JOB_METADATA_BYTES) return null;
      return JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes));
    } catch { return null; }
  }

  private async writeSidecar(name: string, value: unknown, owner: DraftPrincipal): Promise<SaveOutcome> {
    const bytes = Buffer.from(JSON.stringify(value), 'utf8');
    if (bytes.byteLength > MAX_JOB_METADATA_BYTES) return 'UNAVAILABLE';
    try {
      const dir = (await this.directory(owner, true))!;
      let handle;
      try { handle = await fs.open(path.join(dir, name), 'wx', 0o600); }
      catch (error) { return (error as NodeJS.ErrnoException).code === 'EEXIST' ? 'COLLISION' : 'UNAVAILABLE'; }
      try { await handle.writeFile(bytes); await handle.sync(); }
      catch { return 'UNCONFIRMED'; }
      finally { try { await handle.close(); } catch { /* readback is authoritative */ } }
      return JSON.stringify(await this.readSidecar(name, owner)) === JSON.stringify(value) ? 'SAVED' : 'UNCONFIRMED';
    } catch { return 'UNAVAILABLE'; }
  }

  async createJob(input: CreateJobInput, owner: DraftPrincipal): Promise<SaveOutcome> {
    if (!this.jobDecisions || !parseCreateJob(input) || !safePrincipal(owner)
      || !input.sourceRecordId.startsWith('ncr-synthetic-')) return 'UNAVAILABLE';
    return this.writeSidecar(`job-${input.jobId}.json`, makeJob(input, owner, this.clock()), owner);
  }
  async getJob(jobId: string, sourceRecordId: string, owner: DraftPrincipal): Promise<HtmlJob | null> {
    if (!this.jobDecisions || !VERSION_ID.test(jobId) || !SOURCE_ID.test(sourceRecordId)) return null;
    const job = validateJob(await this.readSidecar(`job-${jobId}.json`, owner), owner, this.clock());
    return job?.jobId === jobId && job.sourceRecordId === sourceRecordId ? job : null;
  }

  async linkVersion(input: LinkVersionInput, owner: DraftPrincipal): Promise<SaveOutcome> {
    if (!this.jobDecisions || !parseLinkVersion(input) || !safePrincipal(owner)) return 'UNAVAILABLE';
    const job = await this.getJob(input.jobId, input.sourceRecordId, owner);
    const snapshot = await this.get(input.versionId, input.sourceRecordId, owner);
    if (!job || !snapshot || snapshot.requestSha256 !== job.requestSha256) return 'UNAVAILABLE';
    const link = makeVersion(job, snapshot, this.clock());
    return this.writeSidecar(`version-${input.versionId}-job.json`, link, owner);
  }
  async getVersion(jobId: string, sourceRecordId: string, versionId: string, owner: DraftPrincipal): Promise<HtmlJobVersion | null> {
    if (!this.jobDecisions || !VERSION_ID.test(jobId) || !VERSION_ID.test(versionId) || !SOURCE_ID.test(sourceRecordId)) return null;
    const link = validateVersion(await this.readSidecar(`version-${versionId}-job.json`, owner), owner, this.clock());
    if (!link || link.jobId !== jobId || link.sourceRecordId !== sourceRecordId || link.versionId !== versionId) return null;
    const job = await this.getJob(jobId, sourceRecordId, owner);
    const snapshot = await this.get(versionId, sourceRecordId, owner);
    if (!job || !snapshot || link.requestSha256 !== job.requestSha256 || link.requestSha256 !== snapshot.requestSha256
      || link.htmlSha256 !== snapshot.htmlSha256 || link.expiresAt !== new Date(Math.min(Date.parse(job.expiresAt), Date.parse(snapshot.expiresAt))).toISOString()) return null;
    return link;
  }

  async acceptVersion(input: AcceptVersionInput, owner: DraftPrincipal): Promise<SaveOutcome> {
    if (!this.jobDecisions || !parseAcceptVersion(input) || !safePrincipal(owner)) return 'UNAVAILABLE';
    const job = await this.getJob(input.jobId, input.sourceRecordId, owner);
    const link = await this.getVersion(input.jobId, input.sourceRecordId, input.versionId, owner);
    const snapshot = await this.get(input.versionId, input.sourceRecordId, owner);
    if (!job || !link || !snapshot || !reviewMatches(job.criteria, input.criteriaReview)
      || input.requestSha256 !== link.requestSha256 || input.htmlSha256 !== link.htmlSha256) return 'UNAVAILABLE';
    const expiry = new Date(Math.min(Date.parse(job.expiresAt), Date.parse(link.expiresAt), Date.parse(snapshot.expiresAt))).toISOString();
    const decision = makeDecision(input, owner, expiry, this.clock());
    return this.writeSidecar(`job-${input.jobId}-decision-${input.versionId}.json`, decision, owner);
  }
  async getDecision(jobId: string, sourceRecordId: string, versionId: string, decisionId: string, owner: DraftPrincipal): Promise<HtmlJobDecision | null> {
    if (!this.jobDecisions || ![jobId, versionId, decisionId].every(x => VERSION_ID.test(x)) || !SOURCE_ID.test(sourceRecordId)) return null;
    const decision = validateDecision(await this.readSidecar(`job-${jobId}-decision-${versionId}.json`, owner), owner, this.clock());
    if (!decision || decision.jobId !== jobId || decision.sourceRecordId !== sourceRecordId || decision.versionId !== versionId
      || decision.decisionId !== decisionId) return null;
    const job = await this.getJob(jobId, sourceRecordId, owner);
    const link = await this.getVersion(jobId, sourceRecordId, versionId, owner);
    const snapshot = await this.get(versionId, sourceRecordId, owner);
    if (!job || !link || !snapshot || !reviewMatches(job.criteria, decision.criteriaReview)
      || decision.expiresAt !== new Date(Math.min(Date.parse(job.expiresAt), Date.parse(link.expiresAt), Date.parse(snapshot.expiresAt))).toISOString()
      || decision.requestSha256 !== link.requestSha256 || decision.htmlSha256 !== link.htmlSha256) return null;
    return decision;
  }

  // ---- Receipt operations: one-shot, monotonic exclusive-create records in an operations-only child directory. ----
  // No lock, rollback, append, TTL, eviction, retry or recycled slot. File sync does not establish directory or power-loss durability.

  private async operationDirectory(owner: DraftPrincipal, create: boolean): Promise<string | null> {
    const base = await this.directory(owner, create);
    if (!base) return null;
    const dir = path.join(base, OPERATIONS_DIR);
    if (create) {
      try { await fs.mkdir(dir, { mode: 0o700 }); }
      catch (error) { if (errno(error) !== 'EEXIST') throw error; }
    }
    let stat;
    try { stat = await fs.lstat(dir); }
    catch (error) { if (!create && errno(error) === 'ENOENT') return null; throw error; }
    if (!stat.isDirectory() || stat.isSymbolicLink() || await fs.realpath(dir) !== dir) throw new Error('UNSAFE_OPERATIONS_NAMESPACE');
    return dir;
  }

  private async readFileExact(dir: string, name: string): Promise<FileRead> {
    const file = path.join(dir, name);
    let stat;
    try { stat = await fs.lstat(file); }
    catch (error) { return errno(error) === 'ENOENT' ? { kind: 'MISSING' } : { kind: 'UNCONFIRMED', reason: 'LSTAT_FAILED' }; }
    if (!stat.isFile() || stat.isSymbolicLink()) return { kind: 'CORRUPT', reason: 'NOT_REGULAR_FILE' };
    if (stat.size === 0 || stat.size > MAX_OPERATION_RECORD_BYTES) return { kind: 'CORRUPT', reason: stat.size === 0 ? 'EMPTY_RECORD' : 'OVERSIZE_RECORD' };
    try {
      const bytes = await fs.readFile(file);
      return bytes.byteLength === stat.size ? { kind: 'OK', bytes } : { kind: 'UNCONFIRMED', reason: 'SIZE_CHANGED' };
    } catch { return { kind: 'UNCONFIRMED', reason: 'READ_FAILED' }; }
  }

  private async readRecord<T>(dir: string, name: string, parse: (value: unknown) => T | null): Promise<RecordRead<T>> {
    const read = await this.readFileExact(dir, name);
    if (read.kind === 'MISSING') return read;
    if (read.kind !== 'OK') return { kind: 'BAD', state: read.kind, reason: read.reason };
    const decoded = decodeRecord(read.bytes);
    if (decoded.kind === 'UNSUPPORTED') return { kind: 'BAD', state: 'UNSUPPORTED', reason: 'UNSUPPORTED_REVISION' };
    const value = decoded.kind === 'OK' ? parse(decoded.value) : null;
    return value === null ? { kind: 'BAD', state: 'CORRUPT', reason: 'INVALID_RECORD' } : { kind: 'OK', value };
  }

  /** Exclusive create, sync and exact byte readback. A file that exists after any failure stays consumed. */
  private async createOnce(dir: string, name: string, bytes: Buffer): Promise<'CREATED' | 'EXISTS' | 'UNCONFIRMED' | 'UNAVAILABLE'> {
    let handle;
    try { handle = await fs.open(path.join(dir, name), 'wx', 0o600); }
    catch (error) { return errno(error) === 'EEXIST' ? 'EXISTS' : 'UNAVAILABLE'; }
    try { await handle.writeFile(bytes); await handle.sync(); }
    catch { return 'UNCONFIRMED'; }
    finally { try { await handle.close(); } catch { /* exact readback is authoritative */ } }
    const back = await this.readFileExact(dir, name);
    return back.kind === 'OK' && Buffer.compare(back.bytes, bytes) === 0 ? 'CREATED' : 'UNCONFIRMED';
  }

  /** Read-only lookup. Distinguishes missing from corrupt, unconfirmed and unsupported; never reserves, creates or repairs. */
  async readOperation(key: string, owner: DraftPrincipal): Promise<OperationState> {
    if (!this.receiptOperations || !/^[a-f0-9]{64}$/.test(key) || !safePrincipal(owner)) return { state: 'UNCONFIRMED', reason: 'LOOKUP_REFUSED' };
    let dir: string | null;
    try { dir = await this.operationDirectory(owner, false); }
    catch { return { state: 'UNCONFIRMED', reason: 'UNSAFE_NAMESPACE' }; }
    if (!dir) return { state: 'ABSENT' };
    const intent = await this.readRecord(dir, lifecycleName(key, 'intent'), parseIntent);
    const start = await this.readRecord(dir, lifecycleName(key, 'start'), parseStart);
    const outcome = await this.readRecord(dir, lifecycleName(key, 'outcome'), parseOutcome);
    if (intent.kind === 'BAD') return { state: intent.state, reason: intent.reason };
    if (start.kind === 'BAD') return { state: start.state, reason: start.reason };
    if (outcome.kind === 'BAD') return { state: outcome.state, reason: outcome.reason };
    if (intent.kind === 'MISSING') {
      return start.kind === 'MISSING' && outcome.kind === 'MISSING' ? { state: 'ABSENT' } : { state: 'CORRUPT', reason: 'ORPHAN_LIFECYCLE' };
    }
    const record = intent.value;
    if (record.operationKey !== key || !sameOwner(record.envelope.owner, owner)) return { state: 'CORRUPT', reason: 'KEY_MISMATCH' };
    const reservation = await this.readRecord(dir, slotName(record.slot), parseReservation);
    if (reservation.kind === 'BAD') return { state: reservation.state, reason: reservation.reason };
    if (reservation.kind === 'MISSING' || reservation.value.operationKey !== key || reservation.value.slot !== record.slot
      || reservation.value.configDigest !== record.envelope.config.configDigest || reservation.value.ownerSha256 !== ownerSha256(owner)) {
      return { state: 'CORRUPT', reason: 'RESERVATION_MISMATCH' };
    }
    if (start.kind === 'MISSING') {
      return outcome.kind === 'MISSING' ? { state: 'INTENT', intent: record } : { state: 'CORRUPT', reason: 'OUTCOME_WITHOUT_START' };
    }
    if (start.value.operationKey !== key || start.value.envelopeSha256 !== record.envelopeSha256 || start.value.attemptId !== record.envelope.attemptId) {
      return { state: 'CORRUPT', reason: 'START_MISMATCH' };
    }
    if (outcome.kind === 'MISSING') return { state: 'STARTED', intent: record, start: start.value };
    if (outcome.value.operationKey !== key || outcome.value.envelopeSha256 !== record.envelopeSha256
      || outcome.value.attemptId !== start.value.attemptId || outcome.value.startNonce !== start.value.startNonce) {
      return { state: 'CORRUPT', reason: 'OUTCOME_MISMATCH' };
    }
    return { state: 'OUTCOME', intent: record, start: start.value, outcome: outcome.value };
  }

  /** Bounded scan of the operations directory only. Unknown names deny; they are never ignored. */
  private async scanOperations(dir: string): Promise<{ kind: 'OK'; slots: Set<number> } | { kind: 'DENIED'; reason: OperationDenial }> {
    const entries = await fs.readdir(dir);
    if (entries.length > MAX_OPERATION_ENTRIES) return { kind: 'DENIED', reason: 'SCAN_BOUND_EXCEEDED' };
    const slots = new Set<number>();
    for (const entry of entries) {
      const slot = SLOT_FILE.exec(entry);
      if (slot && Number(slot[1]) < MAX_OPERATIONS_PER_OWNER) { slots.add(Number(slot[1])); continue; }
      if (!LIFECYCLE_FILE.test(entry)) return { kind: 'DENIED', reason: 'UNKNOWN_ENTRY' };
    }
    return { kind: 'OK', slots };
  }

  /** Claim one of 256 fixed numbered markers. A lost race moves on; a consumed marker is never released or recycled. */
  private async reserveSlot(dir: string, taken: Set<number>, envelope: OperationEnvelope): Promise<number | 'CAPACITY_FULL' | 'RESERVATION_UNCONFIRMED'> {
    for (let slot = 0; slot < MAX_OPERATIONS_PER_OWNER; slot++) {
      if (taken.has(slot)) continue;
      const bytes = recordBytes(makeReservation(slot, envelope.owner, envelope.operationKey, envelope.config.configDigest, this.clock()));
      if (!bytes) return 'RESERVATION_UNCONFIRMED';
      const result = await this.createOnce(dir, slotName(slot), bytes);
      if (result === 'EXISTS') continue;
      return result === 'CREATED' ? slot : 'RESERVATION_UNCONFIRMED';
    }
    return 'CAPACITY_FULL';
  }

  /** Existing-record lookup first (no new slot), then reservation, then the exclusive key/intent record. */
  async admitOperation(input: unknown, owner: DraftPrincipal): Promise<AdmitResult> {
    if (!this.receiptOperations) return { kind: 'DENIED', reason: 'DISABLED' };
    const envelope = parseEnvelope(input);
    if (!envelope || !safePrincipal(owner) || !sameOwner(envelope.owner, owner)) return { kind: 'DENIED', reason: 'INVALID_INPUT' };
    const existing = await this.readOperation(envelope.operationKey, owner);
    if (existing.state === 'UNCONFIRMED' && existing.reason === 'UNSAFE_NAMESPACE') return { kind: 'DENIED', reason: 'UNSAFE_NAMESPACE' };
    if (existing.state !== 'ABSENT') return { kind: 'EXISTING', operation: existing };
    let dir: string | null;
    try { dir = await this.operationDirectory(owner, true); }
    catch { return { kind: 'DENIED', reason: 'UNSAFE_NAMESPACE' }; }
    if (!dir) return { kind: 'DENIED', reason: 'UNSAFE_NAMESPACE' };
    let scan;
    try { scan = await this.scanOperations(dir); }
    catch { return { kind: 'DENIED', reason: 'LOOKUP_FAILED' }; }
    if (scan.kind === 'DENIED') return scan;
    const reserved = await this.reserveSlot(dir, scan.slots, envelope);
    if (typeof reserved !== 'number') return { kind: 'DENIED', reason: reserved };
    const intent = makeIntent(reserved, envelope, this.clock());
    const bytes = recordBytes(intent);
    if (!bytes) return { kind: 'DENIED', reason: 'INVALID_INPUT' };
    const created = await this.createOnce(dir, lifecycleName(envelope.operationKey, 'intent'), bytes);
    if (created === 'CREATED') return { kind: 'ADMITTED', intent };
    if (created === 'EXISTS') {
      const raced = await this.readOperation(envelope.operationKey, owner);
      return raced.state === 'ABSENT' ? { kind: 'DENIED', reason: 'LOOKUP_FAILED' } : { kind: 'EXISTING', operation: raced };
    }
    return { kind: 'DENIED', reason: 'INTENT_UNCONFIRMED' };
  }

  /** The caller that wins the exclusive STARTED create mints the only grant. Durable start existence never mints one. */
  async startOperation(owner: DraftPrincipal, key: string, invoker: unknown): Promise<StartResult> {
    if (!this.receiptOperations) return { kind: 'DENIED', reason: 'DISABLED' };
    if (typeof invoker !== 'function') return { kind: 'DENIED', reason: 'INVALID_INPUT' };
    const state = await this.readOperation(key, owner);
    if (state.state === 'ABSENT') return { kind: 'DENIED', reason: 'NO_INTENT' };
    if (state.state !== 'INTENT') return { kind: 'EXISTING', operation: state };
    let dir: string | null;
    try { dir = await this.operationDirectory(owner, false); }
    catch { return { kind: 'DENIED', reason: 'UNSAFE_NAMESPACE' }; }
    if (!dir) return { kind: 'DENIED', reason: 'UNSAFE_NAMESPACE' };
    const start = makeStart(state.intent.envelope, randomBytes(16).toString('hex'), this.clock());
    const bytes = recordBytes(start);
    if (!bytes) return { kind: 'DENIED', reason: 'INVALID_INPUT' };
    const created = await this.createOnce(dir, lifecycleName(key, 'start'), bytes);
    if (created === 'EXISTS') {
      const raced = await this.readOperation(key, owner);
      return raced.state === 'ABSENT' ? { kind: 'DENIED', reason: 'LOOKUP_FAILED' } : { kind: 'EXISTING', operation: raced };
    }
    if (created !== 'CREATED') return { kind: 'DENIED', reason: 'START_UNCONFIRMED' };
    const grant: OperationGrant = Object.freeze({ kind: 'OPERATION_GRANT' as const });
    grants.set(grant, { owner: { ...owner }, operationKey: key, envelopeSha256: start.envelopeSha256, attemptId: start.attemptId,
      startNonce: start.startNonce, store: this, invoker, spent: false });
    return { kind: 'STARTED', grant };
  }

  /** Consume before invoke. Fabricated, copied, spent, foreign-store or different-invoker grants return null. */
  consumeGrant(grant: unknown, invoker: unknown): ConsumedGrant | null {
    if (grant === null || typeof grant !== 'object') return null;
    const state = grants.get(grant);
    if (!state || state.spent || state.store !== this || state.invoker !== invoker) return null;
    state.spent = true;
    return { owner: { ...state.owner }, operationKey: state.operationKey, envelopeSha256: state.envelopeSha256, attemptId: state.attemptId, startNonce: state.startNonce };
  }

  /** The single immutable terminal record for a consumed start. A second writer collides and cannot change the outcome. */
  async writeOutcome(consumed: ConsumedGrant, input: OutcomeInput): Promise<OutcomeWrite> {
    if (!this.receiptOperations || !safePrincipal(consumed.owner)) return { kind: 'UNAVAILABLE' };
    const state = await this.readOperation(consumed.operationKey, consumed.owner);
    if (state.state === 'OUTCOME') return { kind: 'COLLISION' };
    if (state.state !== 'STARTED' || state.start.startNonce !== consumed.startNonce || state.start.attemptId !== consumed.attemptId
      || state.start.envelopeSha256 !== consumed.envelopeSha256) return { kind: 'UNAVAILABLE' };
    const outcome = parseOutcome(makeOutcome(state.start, input, this.clock()));
    const bytes = outcome ? recordBytes(outcome) : null;
    if (!outcome || !bytes) return { kind: 'UNAVAILABLE' };
    let dir: string | null;
    try { dir = await this.operationDirectory(consumed.owner, false); }
    catch { return { kind: 'UNAVAILABLE' }; }
    if (!dir) return { kind: 'UNAVAILABLE' };
    const created = await this.createOnce(dir, lifecycleName(consumed.operationKey, 'outcome'), bytes);
    if (created === 'CREATED') return { kind: 'SAVED', outcome };
    return { kind: created === 'EXISTS' ? 'COLLISION' : created };
  }
}
