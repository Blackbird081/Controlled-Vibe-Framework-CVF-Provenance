/** Isolated fixture repository for unverified HTML drafts. No active-data profile is wired. */
import * as fs from 'node:fs/promises';
import path from 'node:path';
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
}
export type SaveOutcome = 'SAVED' | 'COLLISION' | 'UNCONFIRMED' | 'UNAVAILABLE';
const safePrincipal = (p: DraftPrincipal) => [p.userId, p.orgId, p.teamId].every(v => typeof v === 'string' && v.length > 0 && v.length <= 150 && /^[A-Za-z0-9_-]+$/.test(v));

export class HtmlDraftSnapshotStore {
  private readonly root: string;
  private readonly jobDecisions: boolean;
  constructor(profile: SyntheticDraftProfile, private readonly clock: () => number = Date.now) {
    if (profile.kind !== 'local-synthetic' || profile.production !== false || !path.isAbsolute(profile.root)
      || path.resolve(profile.root) === path.parse(profile.root).root || profile.root.startsWith('\\\\')) {
      throw new Error('SYNTHETIC_PROFILE_REQUIRED');
    }
    this.root = path.resolve(profile.root);
    this.jobDecisions = profile.jobDecisions === true;
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
}
