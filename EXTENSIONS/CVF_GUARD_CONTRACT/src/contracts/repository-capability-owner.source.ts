/** Repository-owned authority source for CADP evidence binding. */

import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, isAbsolute, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import type Database from 'better-sqlite3';

export type RepositoryArtifactType = 'receipt' | 'work_order' | 'review' | 'freeze';

export interface VerifiedRepositoryArtifact {
  readonly ref: string;
  readonly artifactType: RepositoryArtifactType;
  readonly owner: string;
  readonly sha256: string;
}

export interface VerifiedRepositoryGrant {
  readonly schemaVersion: 'cvf.cadp.repositoryGrant.v1';
  readonly repositoryId: 'CVF_PRIVATE_PROVENANCE';
  readonly status: 'ACTIVE';
  readonly grantId: string;
  readonly owner: string;
  readonly workOrderId: string;
  readonly workOrderVersion: string;
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly assignmentId: string;
  readonly actionId: string;
  readonly transport: 'local_git_object_database';
  readonly resourceRef: string;
  readonly credentialReference: string;
  readonly evaluatedAt: string;
  readonly validFrom: string;
  readonly validUntil: string;
  readonly maxInvocations: number;
  readonly maxRetriesPerInvocation: number;
  readonly boundWorkflowTraceIds: readonly string[];
  readonly boundReceiptIds: readonly string[];
  readonly artifacts: readonly VerifiedRepositoryArtifact[];
  readonly rawSecretsIncluded: false;
  readonly grantHash: string;
}

export type RepositoryOwnerSourceErrorCode =
  | 'INVALID_GRANT_REF'
  | 'REPOSITORY_NOT_FOUND'
  | 'GIT_OBJECT_INVALID'
  | 'GRANT_SCHEMA_INVALID'
  | 'ARTIFACT_HASH_MISMATCH'
  | 'GRANT_ID_REBOUND'
  | 'STATE_STORE_ERROR'
  | 'INVOCATION_LIMIT_EXCEEDED'
  | 'RETRY_LIMIT_EXCEEDED'
  | 'DUPLICATE_INVOCATION_REJECTED';

export class RepositoryOwnerSourceError extends Error {
  constructor(readonly code: RepositoryOwnerSourceErrorCode, message: string) {
    super(message);
    this.name = 'RepositoryOwnerSourceError';
  }
}

const MODULE_DIRECTORY = dirname(fileURLToPath(import.meta.url));
const GRANT_PREFIX = 'governance/capability-grants/';
const SHA256 = /^[0-9a-f]{64}$/;
const SAFE_REF = /^[A-Za-z0-9._/-]+$/;
const SAFE_ID = /^[A-Za-z0-9._:/-]+$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const ARTIFACT_TYPES: readonly RepositoryArtifactType[] = ['receipt', 'work_order', 'review', 'freeze'];
const VERIFIED_RECORDS = new WeakSet<object>();
const require = createRequire(import.meta.url);

function controlledGitEnvironment(): NodeJS.ProcessEnv {
  const environment = { ...process.env };
  for (const key of [
    'GIT_DIR', 'GIT_WORK_TREE', 'GIT_COMMON_DIR', 'GIT_OBJECT_DIRECTORY',
    'GIT_ALTERNATE_OBJECT_DIRECTORIES', 'GIT_INDEX_FILE',
  ]) delete environment[key];
  environment.GIT_CONFIG_NOSYSTEM = '1';
  environment.GIT_CONFIG_GLOBAL = process.platform === 'win32' ? 'NUL' : '/dev/null';
  environment.GIT_NO_REPLACE_OBJECTS = '1';
  return environment;
}

function fail(code: RepositoryOwnerSourceErrorCode, message: string): never {
  throw new RepositoryOwnerSourceError(code, message);
}

function sha256(bytes: Buffer): string {
  return createHash('sha256').update(bytes).digest('hex');
}

function normalizeRepositoryRef(value: unknown, grantOnly = false): string {
  if (typeof value !== 'string' || !value || value.length > 1024 || value.includes('\\') || value.includes('\0') ||
      isAbsolute(value) || !SAFE_REF.test(value)) {
    fail('INVALID_GRANT_REF', 'Repository reference is not a normalized relative path.');
  }
  const segments = value.split('/');
  if (segments.some((part) => !part || part === '.' || part === '..')) {
    fail('INVALID_GRANT_REF', 'Repository reference contains an unsafe path segment.');
  }
  if (grantOnly && (!value.startsWith(GRANT_PREFIX) || !value.endsWith('.json'))) {
    fail('INVALID_GRANT_REF', 'Grant reference must name a JSON file under governance/capability-grants/.');
  }
  return value;
}

export function resolveCanonicalRepositoryRoot(): string {
  try {
    return execFileSync('git', ['-C', MODULE_DIRECTORY, 'rev-parse', '--show-toplevel'], {
      encoding: 'utf8',
      windowsHide: true,
      env: controlledGitEnvironment(),
      stdio: ['ignore', 'pipe', 'pipe'],
    }).trim();
  } catch {
    return fail('REPOSITORY_NOT_FOUND', 'The canonical repository cannot be resolved from the production module location.');
  }
}

function readHeadBlob(repositoryRoot: string, ref: string): Buffer {
  const objectSpec = `HEAD:${ref}`;
  try {
    const objectType = execFileSync('git', ['-C', repositoryRoot, 'cat-file', '-t', objectSpec], {
      encoding: 'utf8', windowsHide: true, env: controlledGitEnvironment(), stdio: ['ignore', 'pipe', 'pipe'],
    }).trim();
    if (objectType !== 'blob') fail('GIT_OBJECT_INVALID', `Committed object is not a blob: ${ref}`);
    return execFileSync('git', ['-C', repositoryRoot, 'show', objectSpec], {
      encoding: 'buffer', windowsHide: true, maxBuffer: 16 * 1024 * 1024,
      env: controlledGitEnvironment(), stdio: ['ignore', 'pipe', 'pipe'],
    });
  } catch (error) {
    if (error instanceof RepositoryOwnerSourceError) throw error;
    return fail('GIT_OBJECT_INVALID', `Committed blob is unavailable: ${ref}`);
  }
}

function asObject(value: unknown, path: string): Record<string, unknown> {
  if (value === null || typeof value !== 'object' || Array.isArray(value) || Object.getPrototypeOf(value) !== Object.prototype) {
    return fail('GRANT_SCHEMA_INVALID', `${path} must be a plain JSON object.`);
  }
  return value as Record<string, unknown>;
}

function requireExactKeys(object: Record<string, unknown>, keys: readonly string[], path: string): void {
  const actual = Object.keys(object).sort();
  const expected = [...keys].sort();
  if (actual.length !== expected.length || actual.some((key, index) => key !== expected[index])) {
    fail('GRANT_SCHEMA_INVALID', `${path} contains missing or unknown fields.`);
  }
}

function textField(object: Record<string, unknown>, key: string): string {
  const value = object[key];
  if (typeof value !== 'string' || !value || value.length > 512 || !SAFE_ID.test(value)) {
    return fail('GRANT_SCHEMA_INVALID', `$.${key} must be a non-empty safe identifier.`);
  }
  return value;
}

function utcField(object: Record<string, unknown>, key: string): string {
  const value = object[key];
  if (typeof value !== 'string' || !ISO_UTC.test(value) || !Number.isFinite(Date.parse(value))) {
    return fail('GRANT_SCHEMA_INVALID', `$.${key} must be an ISO-8601 UTC timestamp.`);
  }
  return value;
}

function integerField(object: Record<string, unknown>, key: string, minimum: number, maximum: number): number {
  const value = object[key];
  if (!Number.isSafeInteger(value) || (value as number) < minimum || (value as number) > maximum) {
    return fail('GRANT_SCHEMA_INVALID', `$.${key} is outside its allowed integer range.`);
  }
  return value as number;
}

function idArray(object: Record<string, unknown>, key: string): readonly string[] {
  const value = object[key];
  if (!Array.isArray(value) || value.length === 0 || value.some((item) => typeof item !== 'string' || !item || !SAFE_ID.test(item))) {
    return fail('GRANT_SCHEMA_INVALID', `$.${key} must be a non-empty safe identifier array.`);
  }
  if (new Set(value).size !== value.length) fail('GRANT_SCHEMA_INVALID', `$.${key} contains duplicates.`);
  return Object.freeze([...value] as string[]);
}

const GRANT_KEYS = [
  'schemaVersion', 'repositoryId', 'status', 'grantId', 'owner', 'workOrderId',
  'workOrderVersion', 'capabilityId', 'capabilityVersion', 'assignmentId', 'actionId',
  'transport', 'resourceRef', 'credentialReference', 'evaluatedAt', 'validFrom',
  'validUntil', 'maxInvocations', 'maxRetriesPerInvocation', 'boundWorkflowTraceIds',
  'boundReceiptIds', 'artifacts', 'rawSecretsIncluded',
] as const;

function parseGrant(bytes: Buffer, grantRef: string, repositoryRoot: string): VerifiedRepositoryGrant {
  let parsed: unknown;
  try {
    parsed = JSON.parse(bytes.toString('utf8'));
  } catch {
    return fail('GRANT_SCHEMA_INVALID', 'Committed grant is not valid UTF-8 JSON.');
  }
  const object = asObject(parsed, '$');
  requireExactKeys(object, GRANT_KEYS, '$');
  if (object.schemaVersion !== 'cvf.cadp.repositoryGrant.v1' || object.repositoryId !== 'CVF_PRIVATE_PROVENANCE' ||
      object.status !== 'ACTIVE' || object.transport !== 'local_git_object_database' ||
      object.rawSecretsIncluded !== false) {
    fail('GRANT_SCHEMA_INVALID', 'Grant constants do not match the repository-owner schema.');
  }
  const resourceRef = normalizeRepositoryRef(object.resourceRef, true);
  if (resourceRef !== grantRef) fail('GRANT_SCHEMA_INVALID', 'Grant resourceRef does not bind its own committed path.');
  const credentialReference = textField(object, 'credentialReference');
  if (!/^none:[a-z0-9._-]+$/.test(credentialReference)) {
    fail('GRANT_SCHEMA_INVALID', 'credentialReference must be a non-secret none: reference.');
  }
  const validFrom = utcField(object, 'validFrom');
  const validUntil = utcField(object, 'validUntil');
  const evaluatedAt = utcField(object, 'evaluatedAt');
  if (Date.parse(validFrom) >= Date.parse(validUntil) || Date.parse(evaluatedAt) < Date.parse(validFrom) || Date.parse(evaluatedAt) > Date.parse(validUntil)) {
    fail('GRANT_SCHEMA_INVALID', 'Grant validity timestamps are inconsistent.');
  }
  if (!Array.isArray(object.artifacts) || object.artifacts.length === 0) {
    fail('GRANT_SCHEMA_INVALID', '$.artifacts must be a non-empty array.');
  }
  const seenRefs = new Set<string>();
  const seenTypes = new Set<RepositoryArtifactType>();
  const owner = textField(object, 'owner');
  const artifacts = object.artifacts.map((item, index): VerifiedRepositoryArtifact => {
    const artifact = asObject(item, `$.artifacts[${index}]`);
    requireExactKeys(artifact, ['ref', 'artifactType', 'owner', 'sha256'], `$.artifacts[${index}]`);
    const ref = normalizeRepositoryRef(artifact.ref);
    const artifactType = artifact.artifactType;
    if (typeof artifactType !== 'string' || !ARTIFACT_TYPES.includes(artifactType as RepositoryArtifactType)) {
      return fail('GRANT_SCHEMA_INVALID', `$.artifacts[${index}].artifactType is invalid.`);
    }
    if (artifact.owner !== owner || typeof artifact.sha256 !== 'string' || !SHA256.test(artifact.sha256)) {
      return fail('GRANT_SCHEMA_INVALID', `$.artifacts[${index}] owner or digest is invalid.`);
    }
    if (seenRefs.has(ref) || seenTypes.has(artifactType as RepositoryArtifactType)) {
      return fail('GRANT_SCHEMA_INVALID', 'Artifact references and semantic types must be unique.');
    }
    seenRefs.add(ref);
    seenTypes.add(artifactType as RepositoryArtifactType);
    if (sha256(readHeadBlob(repositoryRoot, ref)) !== artifact.sha256) {
      return fail('ARTIFACT_HASH_MISMATCH', `Committed artifact hash mismatch: ${ref}`);
    }
    return Object.freeze({ ref, artifactType: artifactType as RepositoryArtifactType, owner, sha256: artifact.sha256 });
  });
  const record: VerifiedRepositoryGrant = Object.freeze({
    schemaVersion: 'cvf.cadp.repositoryGrant.v1', repositoryId: 'CVF_PRIVATE_PROVENANCE', status: 'ACTIVE',
    grantId: textField(object, 'grantId'), owner,
    workOrderId: textField(object, 'workOrderId'), workOrderVersion: textField(object, 'workOrderVersion'),
    capabilityId: textField(object, 'capabilityId'), capabilityVersion: textField(object, 'capabilityVersion'),
    assignmentId: textField(object, 'assignmentId'), actionId: textField(object, 'actionId'),
    transport: 'local_git_object_database', resourceRef, credentialReference, evaluatedAt, validFrom, validUntil,
    maxInvocations: integerField(object, 'maxInvocations', 1, 1_000_000),
    maxRetriesPerInvocation: integerField(object, 'maxRetriesPerInvocation', 0, 100),
    boundWorkflowTraceIds: idArray(object, 'boundWorkflowTraceIds'),
    boundReceiptIds: idArray(object, 'boundReceiptIds'), artifacts: Object.freeze(artifacts),
    rawSecretsIncluded: false, grantHash: sha256(bytes),
  });
  VERIFIED_RECORDS.add(record);
  return record;
}

function statePath(repositoryRoot: string): string {
  return resolve(repositoryRoot, 'logs/capability-owner/cadp-owner.db');
}

function withState<T>(repositoryRoot: string, operation: (database: Database.Database) => T): T {
  const path = statePath(repositoryRoot);
  try {
    mkdirSync(dirname(path), { recursive: true });
    const DatabaseConstructor = require('better-sqlite3') as typeof import('better-sqlite3');
    const database = new DatabaseConstructor(path);
    try {
      database.pragma('journal_mode = WAL');
      database.pragma('synchronous = FULL');
      database.pragma('busy_timeout = 5000');
      database.exec(`
        CREATE TABLE IF NOT EXISTS capability_owner_grants (
          grant_id TEXT PRIMARY KEY, grant_hash TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS capability_owner_invocations (
          grant_id TEXT NOT NULL, invocation_id TEXT NOT NULL, max_retry_ordinal INTEGER NOT NULL,
          PRIMARY KEY (grant_id, invocation_id)
        );
      `);
      return operation(database);
    } finally {
      database.close();
    }
  } catch (error) {
    if (error instanceof RepositoryOwnerSourceError) throw error;
    return fail('STATE_STORE_ERROR', 'Capability-owner durable state operation failed.');
  }
}

function registerGrant(record: VerifiedRepositoryGrant, repositoryRoot: string): void {
  withState(repositoryRoot, (database) => database.transaction(() => {
    database.prepare('INSERT OR IGNORE INTO capability_owner_grants (grant_id, grant_hash) VALUES (?, ?)')
      .run(record.grantId, record.grantHash);
    const prior = database.prepare('SELECT grant_hash FROM capability_owner_grants WHERE grant_id = ?')
      .get(record.grantId) as { grant_hash: string };
    if (prior.grant_hash !== record.grantHash) fail('GRANT_ID_REBOUND', 'A grant ID cannot be rebound to different committed bytes.');
  })());
}

export function loadCommittedRepositoryCapabilityGrant(grantRefInput: unknown): VerifiedRepositoryGrant {
  const grantRef = normalizeRepositoryRef(grantRefInput, true);
  const repositoryRoot = resolveCanonicalRepositoryRoot();
  const record = parseGrant(readHeadBlob(repositoryRoot, grantRef), grantRef, repositoryRoot);
  registerGrant(record, repositoryRoot);
  return record;
}

export function consumeRepositoryGrantInvocation(
  record: VerifiedRepositoryGrant,
  invocationId: string,
  retryOrdinal: number,
): void {
  if (!VERIFIED_RECORDS.has(record as object)) fail('GRANT_SCHEMA_INVALID', 'Invocation record is not source-verified.');
  const repositoryRoot = resolveCanonicalRepositoryRoot();
  withState(repositoryRoot, (database) => database.transaction(() => {
    const priorGrant = database.prepare('SELECT grant_hash FROM capability_owner_grants WHERE grant_id = ?').get(record.grantId) as { grant_hash: string } | undefined;
    if (!priorGrant || priorGrant.grant_hash !== record.grantHash) fail('GRANT_ID_REBOUND', 'Durable grant identity no longer matches.');
    const prior = database.prepare('SELECT max_retry_ordinal FROM capability_owner_invocations WHERE grant_id = ? AND invocation_id = ?')
      .get(record.grantId, invocationId) as { max_retry_ordinal: number } | undefined;
    if (prior) {
      if (retryOrdinal <= prior.max_retry_ordinal) fail('DUPLICATE_INVOCATION_REJECTED', 'Invocation/retry pair was already consumed.');
      if (retryOrdinal !== prior.max_retry_ordinal + 1 || retryOrdinal > record.maxRetriesPerInvocation) {
        fail('RETRY_LIMIT_EXCEEDED', 'Retry ordinal is non-contiguous or exceeds the committed ceiling.');
      }
      database.prepare('UPDATE capability_owner_invocations SET max_retry_ordinal = ? WHERE grant_id = ? AND invocation_id = ?')
        .run(retryOrdinal, record.grantId, invocationId);
      return;
    }
    if (retryOrdinal !== 0) fail('RETRY_LIMIT_EXCEEDED', 'A new invocation must begin at retry ordinal zero.');
    const count = database.prepare('SELECT COUNT(*) AS count FROM capability_owner_invocations WHERE grant_id = ?')
      .get(record.grantId) as { count: number };
    if (count.count >= record.maxInvocations) fail('INVOCATION_LIMIT_EXCEEDED', 'Committed invocation ceiling is exhausted.');
    database.prepare('INSERT INTO capability_owner_invocations (grant_id, invocation_id, max_retry_ordinal) VALUES (?, ?, 0)')
      .run(record.grantId, invocationId);
  })());
}
