/**
 * Capability environment-snapshot evidence validation kernel.
 *
 * This module only evaluates caller-supplied in-memory evidence. It neither
 * observes nor persists an environment and every action-authority output is
 * deliberately false.
 */

import { isProxy } from 'node:util/types';
import {
  CAPABILITY_ROUTE_DECISION_VERSION,
  evaluateCapabilityReadiness,
  type CapabilityReadinessDecision,
  type CapabilityRouteDecision,
} from './capability-route-readiness.contract';

export const CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_CONTRACT_VERSION =
  'cvf.capabilityEnvironmentSnapshotEvidence.v1' as const;
export const CAPABILITY_ENVIRONMENT_SNAPSHOT_VERSION =
  'cvf.capabilityEnvironmentSnapshot.v1' as const;
export const CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION =
  'cvf.capabilityEnvironmentSnapshotEvidenceResult.v1' as const;

export type CapabilityDependencyKind = 'CLI' | 'MCP' | 'API' | 'NATIVE' | 'PACKAGE';
export type CapabilityDependencyAvailability = 'AVAILABLE' | 'MISSING' | 'BLOCKED' | 'UNKNOWN';
export type CapabilityDependencyVerificationLevel =
  | 'DECLARED' | 'DISCOVERED' | 'RESPONSIVE' | 'INTEGRITY_VERIFIED' | 'POLICY_VERIFIED';
export type CapabilityNetworkMode = 'NORMAL' | 'RESTRICTED' | 'OFFLINE';
export type CapabilitySandboxStatus = 'AVAILABLE' | 'UNAVAILABLE' | 'UNKNOWN';
export type CapabilityCredentialBindingStatus = 'BOUND' | 'MISSING' | 'EXPIRED' | 'UNKNOWN';
export type CapabilitySnapshotVerificationStatus = 'PASS' | 'WARN' | 'FAIL' | 'UNKNOWN';

export interface CapabilityEnvironmentSnapshotPackage {
  readonly packageId: string;
  readonly packageVersion: string;
}

export interface CapabilityEnvironmentSnapshotDependency {
  readonly dependencyId: string;
  readonly kind: CapabilityDependencyKind;
  readonly availability: CapabilityDependencyAvailability;
  readonly resolvedPath: string | null;
  readonly endpoint: string | null;
  readonly detectedVersion: string | null;
  readonly sourceOrigin: string | null;
  readonly artifactHash: string | null;
  readonly license: string | null;
  readonly verificationLevel: CapabilityDependencyVerificationLevel;
  readonly blockingReasons: readonly string[];
}

export interface CapabilityEnvironmentSnapshot {
  readonly schemaVersion: typeof CAPABILITY_ENVIRONMENT_SNAPSHOT_VERSION;
  readonly snapshotId: string;
  readonly workspaceId: string;
  readonly observedAt: string;
  readonly expiresAt: string;
  readonly workspaceProfile: string;
  readonly platform: Readonly<{ os: string; arch: string; shell: string }>;
  readonly packages: readonly CapabilityEnvironmentSnapshotPackage[];
  readonly dependencies: readonly CapabilityEnvironmentSnapshotDependency[];
  readonly network: Readonly<{ mode: CapabilityNetworkMode; allowedDestinations: readonly string[] }>;
  readonly sandbox: Readonly<{ status: CapabilitySandboxStatus; profile: string | null }>;
  readonly credentialBindings: readonly Readonly<{
    bindingRef: string;
    status: CapabilityCredentialBindingStatus;
  }>[];
  readonly writableBoundaries: readonly string[];
  readonly verification: Readonly<{
    status: CapabilitySnapshotVerificationStatus;
    reasons: readonly string[];
  }>;
}

export interface CapabilityEnvironmentSnapshotReadinessPolicyEvidence {
  readonly readinessDecisionId: string;
  readonly approvalRequired: boolean;
  readonly existingApprovalValid: boolean;
  readonly policyAllowed: boolean | null;
  readonly provenanceVerified: boolean | null;
  readonly integrityVerified: boolean | null;
  readonly compatible: boolean | null;
  readonly credentialsReady: boolean | null;
  readonly networkReady: boolean | null;
  readonly sandboxReady: boolean | null;
  readonly evidenceRefs: readonly string[];
}

export interface CapabilityEnvironmentSnapshotEvidenceInput {
  readonly schemaVersion: typeof CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_CONTRACT_VERSION;
  readonly route: CapabilityRouteDecision;
  readonly snapshot: CapabilityEnvironmentSnapshot;
  readonly readinessPolicy: CapabilityEnvironmentSnapshotReadinessPolicyEvidence;
  readonly now: string;
}

export type CapabilityEnvironmentSnapshotEvidenceIssueCode =
  | 'MALFORMED_INPUT'
  | 'UNKNOWN_KEY'
  | 'INVALID_FIELD'
  | 'UNSAFE_STRING'
  | 'RAW_SECRET_DETECTED'
  | 'UNBOUNDED_COLLECTION'
  | 'SPARSE_ARRAY'
  | 'DUPLICATE_IDENTIFIER'
  | 'ROUTE_REJECTED'
  | 'BINDING_MISMATCH'
  | 'FRESHNESS_INVALID';

export interface CapabilityEnvironmentSnapshotEvidenceIssue {
  readonly code: CapabilityEnvironmentSnapshotEvidenceIssueCode;
  readonly path: string;
  readonly message: string;
}

export type CapabilityEnvironmentSnapshotEvidenceStatus =
  | 'VALIDATED_READY_EVIDENCE'
  | 'VALIDATED_BLOCKED_EVIDENCE'
  | 'REJECTED';

export interface CapabilityEnvironmentSnapshotEvidenceResult {
  readonly schemaVersion: typeof CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION;
  readonly status: CapabilityEnvironmentSnapshotEvidenceStatus;
  readonly routeDecisionId: string;
  readonly snapshotId: string;
  readonly workspaceId: string;
  readonly requiredDependencies: readonly string[];
  readonly availableDependencies: readonly string[];
  readonly blockingReasons: readonly string[];
  readonly issues: readonly CapabilityEnvironmentSnapshotEvidenceIssue[];
  readonly readiness: CapabilityReadinessDecision | null;
  readonly evaluatedAt: string;
  readonly authorityStatus: 'EVIDENCE_ONLY';
  readonly snapshotCollected: false;
  readonly snapshotPersisted: false;
  readonly environmentReadAuthorized: false;
  readonly executionAuthorized: false;
  readonly acquisitionAuthorized: false;
  readonly mutationAuthorized: false;
  readonly refreshAuthorized: false;
  readonly taskAuthorityGranted: false;
  readonly networkAuthorized: false;
}

type PlainRecord = Record<string, unknown>;

const SAFE_TEXT = /^[^\u0000-\u001F\u007F]{1,512}$/;
const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const SHA256 = /^[a-f0-9]{64}$/;
const MAX_ITEMS = 64;
const MAX_REASONS = 32;
const ROUTE_KEYS = [
  'schemaVersion', 'routeDecisionId', 'candidateSetId', 'requestId', 'workspaceId', 'stage',
  'primary', 'supporting', 'rejected', 'fallbacks', 'confidence', 'ambiguityReasons',
  'environmentSnapshotRefs', 'authorityStatus', 'executionAuthorized', 'generatedAt', 'issues',
] as const;

function descriptorRecord(value: unknown): PlainRecord | null {
  if (value === null || typeof value !== 'object' || isProxy(value)) return null;
  let prototype: object | null;
  let descriptors: PropertyDescriptorMap;
  let symbols: symbol[];
  try {
    prototype = Object.getPrototypeOf(value);
    descriptors = Object.getOwnPropertyDescriptors(value);
    symbols = Object.getOwnPropertySymbols(value);
  } catch {
    return null;
  }
  if ((prototype !== Object.prototype && prototype !== null) || symbols.length > 0) return null;
  if (Object.values(descriptors).some((descriptor) => 'get' in descriptor || 'set' in descriptor)) return null;
  return value as PlainRecord;
}

function data(record: PlainRecord, key: string): unknown {
  return Object.getOwnPropertyDescriptor(record, key)?.value;
}

function denseArray(value: unknown): readonly unknown[] | null {
  if (!Array.isArray(value) || isProxy(value)) return null;
  try {
    if (Object.getPrototypeOf(value) !== Array.prototype || Object.getOwnPropertySymbols(value).length > 0) return null;
    const descriptors = Object.getOwnPropertyDescriptors(value);
    if (Object.values(descriptors).some((descriptor) => 'get' in descriptor || 'set' in descriptor)) return null;
    const ownNames = Object.getOwnPropertyNames(value);
    if (ownNames.some((key) => key !== 'length' && !/^(0|[1-9]\d*)$/.test(key))) return null;
    for (let index = 0; index < value.length; index += 1) {
      if (!Object.prototype.hasOwnProperty.call(value, index)) return null;
    }
    return value;
  } catch {
    return null;
  }
}

function hasExactKeys(record: PlainRecord, required: readonly string[], optional: readonly string[] = []): boolean {
  const keys = Object.keys(record);
  return required.every((key) => keys.includes(key))
    && keys.every((key) => required.includes(key) || optional.includes(key));
}

function validUtc(value: unknown): value is string {
  if (typeof value !== 'string') return false;
  const match = ISO_UTC.exec(value);
  if (!match) return false;
  const parsed = Date.parse(value);
  if (!Number.isFinite(parsed)) return false;
  const instant = new Date(parsed);
  const components = value.slice(0, 19).split(/[-T:]/).map(Number);
  return instant.getUTCFullYear() === components[0]
    && instant.getUTCMonth() + 1 === components[1]
    && instant.getUTCDate() === components[2]
    && instant.getUTCHours() === components[3]
    && instant.getUTCMinutes() === components[4]
    && instant.getUTCSeconds() === components[5];
}

function secretLike(value: string): boolean {
  return /-----BEGIN [A-Z ]*PRIVATE KEY-----/i.test(value)
    || /\bBearer\s+[A-Za-z0-9._~+\/-]{12,}/i.test(value)
    || /\bsk-[A-Za-z0-9_-]{16,}\b/.test(value)
    || /\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|password|passwd|client[_-]?secret)\s*[:=]\s*[^\s,;]{8,}/i.test(value);
}

function validString(value: unknown, id = false): value is string {
  return typeof value === 'string' && SAFE_TEXT.test(value) && !secretLike(value) && (!id || SAFE_ID.test(value));
}

function addIssue(
  issues: CapabilityEnvironmentSnapshotEvidenceIssue[],
  code: CapabilityEnvironmentSnapshotEvidenceIssueCode,
  path: string,
  message: string,
): void {
  issues.push(Object.freeze({ code, path, message }));
}

function inspectString(
  value: unknown,
  path: string,
  issues: CapabilityEnvironmentSnapshotEvidenceIssue[],
  options: { nullable?: boolean; id?: boolean; hash?: boolean } = {},
): value is string | null {
  if (options.nullable && value === null) return true;
  if (typeof value !== 'string' || !SAFE_TEXT.test(value)) {
    addIssue(issues, 'UNSAFE_STRING', path, 'Value must be a bounded control-character-free string.');
    return false;
  }
  if (secretLike(value)) {
    addIssue(issues, 'RAW_SECRET_DETECTED', path, 'Secret-like material is forbidden.');
    return false;
  }
  if (options.id && !SAFE_ID.test(value)) {
    addIssue(issues, 'UNSAFE_STRING', path, 'Value must be a bounded safe identifier.');
    return false;
  }
  if (options.hash && !SHA256.test(value)) {
    addIssue(issues, 'INVALID_FIELD', path, 'Artifact hash must be a lowercase SHA-256 value.');
    return false;
  }
  return true;
}

function inspectRecord(
  value: unknown,
  path: string,
  required: readonly string[],
  issues: CapabilityEnvironmentSnapshotEvidenceIssue[],
  optional: readonly string[] = [],
): PlainRecord | null {
  const record = descriptorRecord(value);
  if (!record) {
    addIssue(issues, 'MALFORMED_INPUT', path, 'Value must be a plain non-Proxy data object without accessors or symbols.');
    return null;
  }
  if (!hasExactKeys(record, required, optional)) {
    addIssue(issues, 'UNKNOWN_KEY', path, 'Object keys do not match the bounded contract.');
    return null;
  }
  return record;
}

function inspectArray(
  value: unknown,
  path: string,
  issues: CapabilityEnvironmentSnapshotEvidenceIssue[],
  limit = MAX_ITEMS,
): readonly unknown[] | null {
  const array = denseArray(value);
  if (!array) {
    addIssue(issues, 'SPARSE_ARRAY', path, 'Value must be a dense base Array without accessors, symbols, or extra properties.');
    return null;
  }
  if (array.length > limit) {
    addIssue(issues, 'UNBOUNDED_COLLECTION', path, `Array exceeds the ${limit}-item limit.`);
    return null;
  }
  return array;
}

function inspectStringArray(
  value: unknown,
  path: string,
  issues: CapabilityEnvironmentSnapshotEvidenceIssue[],
  id = false,
  limit = MAX_ITEMS,
): string[] | null {
  const array = inspectArray(value, path, issues, limit);
  if (!array) return null;
  const output: string[] = [];
  array.forEach((item, index) => {
    if (inspectString(item, `${path}[${index}]`, issues, { id })) output.push(item as string);
  });
  return output;
}

function duplicate(values: readonly string[]): boolean {
  return new Set(values).size !== values.length;
}

function isOneOf(value: unknown, allowed: readonly string[]): value is string {
  return typeof value === 'string' && allowed.includes(value);
}

function validateRoute(value: unknown, issues: CapabilityEnvironmentSnapshotEvidenceIssue[]): CapabilityRouteDecision | null {
  const route = inspectRecord(value, '$.route', ROUTE_KEYS, issues, ['primary']);
  if (!route) return null;
  for (const key of ['routeDecisionId', 'candidateSetId', 'requestId', 'workspaceId'] as const) {
    inspectString(data(route, key), `$.route.${key}`, issues, { id: true });
  }
  if (data(route, 'schemaVersion') !== CAPABILITY_ROUTE_DECISION_VERSION
    || data(route, 'authorityStatus') !== 'CANDIDATE_ONLY'
    || data(route, 'executionAuthorized') !== false) {
    addIssue(issues, 'ROUTE_REJECTED', '$.route', 'Route must preserve the current CANDIDATE_ONLY/false T4 boundary.');
  }
  if (!isOneOf(data(route, 'stage'), ['FAST_ROUTE', 'FULL_RESOLUTION_REQUIRED', 'AMBIGUOUS_ROUTE', 'NO_CANDIDATE'])) {
    addIssue(issues, 'INVALID_FIELD', '$.route.stage', 'Unsupported route stage.');
  }
  const confidence = data(route, 'confidence');
  if (typeof confidence !== 'number' || !Number.isFinite(confidence) || confidence < 0 || confidence > 1) {
    addIssue(issues, 'INVALID_FIELD', '$.route.confidence', 'Confidence must be finite and between zero and one.');
  }
  if (!validUtc(data(route, 'generatedAt'))) addIssue(issues, 'INVALID_FIELD', '$.route.generatedAt', 'Route time must be ISO-8601 UTC.');
  for (const key of ['supporting', 'ambiguityReasons', 'environmentSnapshotRefs'] as const) {
    const values = inspectStringArray(data(route, key), `$.route.${key}`, issues, true);
    if (values && duplicate(values)) addIssue(issues, 'DUPLICATE_IDENTIFIER', `$.route.${key}`, 'Identifiers must be unique.');
  }
  const primary = inspectRecord(data(route, 'primary'), '$.route.primary', ['capabilityId', 'packageId', 'packageVersion'], issues);
  if (primary) for (const key of ['capabilityId', 'packageId', 'packageVersion']) inspectString(data(primary, key), `$.route.primary.${key}`, issues, { id: true });
  const rejected = inspectArray(data(route, 'rejected'), '$.route.rejected', issues);
  rejected?.forEach((item, index) => {
    const row = inspectRecord(item, `$.route.rejected[${index}]`, ['capabilityId', 'reasonCodes'], issues);
    if (row) {
      inspectString(data(row, 'capabilityId'), `$.route.rejected[${index}].capabilityId`, issues, { id: true });
      inspectStringArray(data(row, 'reasonCodes'), `$.route.rejected[${index}].reasonCodes`, issues, true);
    }
  });
  const fallbacks = inspectArray(data(route, 'fallbacks'), '$.route.fallbacks', issues);
  fallbacks?.forEach((item, index) => {
    const row = inspectRecord(item, `$.route.fallbacks[${index}]`, ['capabilityId', 'activationCondition'], issues);
    if (row) {
      inspectString(data(row, 'capabilityId'), `$.route.fallbacks[${index}].capabilityId`, issues, { id: true });
      inspectString(data(row, 'activationCondition'), `$.route.fallbacks[${index}].activationCondition`, issues);
    }
  });
  const routeIssues = inspectArray(data(route, 'issues'), '$.route.issues', issues);
  routeIssues?.forEach((item, index) => {
    const row = inspectRecord(item, `$.route.issues[${index}]`, ['code', 'path', 'message'], issues);
    if (row) for (const key of ['code', 'path', 'message']) inspectString(data(row, key), `$.route.issues[${index}].${key}`, issues);
  });
  return route as unknown as CapabilityRouteDecision;
}

interface ValidSnapshot {
  readonly snapshot: CapabilityEnvironmentSnapshot;
  readonly dependencyIds: readonly string[];
  readonly availableIds: readonly string[];
  readonly blockingReasons: readonly string[];
}

function validateSnapshot(value: unknown, issues: CapabilityEnvironmentSnapshotEvidenceIssue[]): ValidSnapshot | null {
  const required = ['schemaVersion', 'snapshotId', 'workspaceId', 'observedAt', 'expiresAt', 'workspaceProfile', 'platform', 'packages', 'dependencies', 'network', 'sandbox', 'credentialBindings', 'writableBoundaries', 'verification'];
  const snapshot = inspectRecord(value, '$.snapshot', required, issues);
  if (!snapshot) return null;
  if (data(snapshot, 'schemaVersion') !== CAPABILITY_ENVIRONMENT_SNAPSHOT_VERSION) addIssue(issues, 'INVALID_FIELD', '$.snapshot.schemaVersion', 'Unsupported snapshot version.');
  for (const key of ['snapshotId', 'workspaceId', 'workspaceProfile']) inspectString(data(snapshot, key), `$.snapshot.${key}`, issues, { id: true });
  for (const key of ['observedAt', 'expiresAt']) if (!validUtc(data(snapshot, key))) addIssue(issues, 'INVALID_FIELD', `$.snapshot.${key}`, 'Time must be ISO-8601 UTC.');

  const platform = inspectRecord(data(snapshot, 'platform'), '$.snapshot.platform', ['os', 'arch', 'shell'], issues);
  if (platform) for (const key of ['os', 'arch', 'shell']) inspectString(data(platform, key), `$.snapshot.platform.${key}`, issues, { id: true });

  const packages = inspectArray(data(snapshot, 'packages'), '$.snapshot.packages', issues);
  const packageIds: string[] = [];
  packages?.forEach((item, index) => {
    const row = inspectRecord(item, `$.snapshot.packages[${index}]`, ['packageId', 'packageVersion'], issues);
    if (!row) return;
    if (inspectString(data(row, 'packageId'), `$.snapshot.packages[${index}].packageId`, issues, { id: true })) packageIds.push(data(row, 'packageId') as string);
    inspectString(data(row, 'packageVersion'), `$.snapshot.packages[${index}].packageVersion`, issues, { id: true });
  });
  if (duplicate(packageIds)) addIssue(issues, 'DUPLICATE_IDENTIFIER', '$.snapshot.packages', 'Package IDs must be unique.');

  const dependencies = inspectArray(data(snapshot, 'dependencies'), '$.snapshot.dependencies', issues);
  const dependencyIds: string[] = [];
  const availableIds: string[] = [];
  const blockingReasons: string[] = [];
  dependencies?.forEach((item, index) => {
    const path = `$.snapshot.dependencies[${index}]`;
    const row = inspectRecord(item, path, ['dependencyId', 'kind', 'availability', 'resolvedPath', 'endpoint', 'detectedVersion', 'sourceOrigin', 'artifactHash', 'license', 'verificationLevel', 'blockingReasons'], issues);
    if (!row) return;
    const dependencyId = data(row, 'dependencyId');
    const availability = data(row, 'availability');
    const kind = data(row, 'kind');
    if (inspectString(dependencyId, `${path}.dependencyId`, issues, { id: true })) dependencyIds.push(dependencyId as string);
    if (!isOneOf(kind, ['CLI', 'MCP', 'API', 'NATIVE', 'PACKAGE'])) addIssue(issues, 'INVALID_FIELD', `${path}.kind`, 'Unsupported dependency kind.');
    if (!isOneOf(availability, ['AVAILABLE', 'MISSING', 'BLOCKED', 'UNKNOWN'])) addIssue(issues, 'INVALID_FIELD', `${path}.availability`, 'Unsupported availability.');
    const resolvedPath = data(row, 'resolvedPath');
    const endpoint = data(row, 'endpoint');
    const detectedVersion = data(row, 'detectedVersion');
    for (const key of ['resolvedPath', 'endpoint', 'detectedVersion', 'sourceOrigin', 'license'] as const) inspectString(data(row, key), `${path}.${key}`, issues, { nullable: true });
    inspectString(data(row, 'artifactHash'), `${path}.artifactHash`, issues, { nullable: true, hash: data(row, 'artifactHash') !== null });
    if (!isOneOf(data(row, 'verificationLevel'), ['DECLARED', 'DISCOVERED', 'RESPONSIVE', 'INTEGRITY_VERIFIED', 'POLICY_VERIFIED'])) addIssue(issues, 'INVALID_FIELD', `${path}.verificationLevel`, 'Unsupported verification level.');
    const reasons = inspectStringArray(data(row, 'blockingReasons'), `${path}.blockingReasons`, issues, false, MAX_REASONS) ?? [];
    if (availability === 'AVAILABLE') {
      if (detectedVersion === null || ((kind === 'CLI' || kind === 'NATIVE' || kind === 'PACKAGE')
        ? resolvedPath === null || endpoint !== null
        : endpoint === null || resolvedPath !== null)) addIssue(issues, 'INVALID_FIELD', path, 'AVAILABLE evidence has inconsistent path, endpoint, or version fields.');
      if (reasons.length) addIssue(issues, 'INVALID_FIELD', `${path}.blockingReasons`, 'AVAILABLE evidence cannot contain blocking reasons.');
      if (typeof dependencyId === 'string') availableIds.push(dependencyId);
    } else {
      if (resolvedPath !== null || endpoint !== null || detectedVersion !== null) addIssue(issues, 'INVALID_FIELD', path, 'Unavailable evidence must use null path, endpoint, and detected version.');
      if (reasons.length === 0) addIssue(issues, 'INVALID_FIELD', `${path}.blockingReasons`, 'Unavailable evidence requires a bounded reason.');
      const safeDependencyId = validString(dependencyId, true) ? dependencyId : 'invalid';
      reasons.forEach((reason) => blockingReasons.push(`${safeDependencyId}:${reason}`));
    }
  });
  if (duplicate(dependencyIds)) addIssue(issues, 'DUPLICATE_IDENTIFIER', '$.snapshot.dependencies', 'Dependency IDs must be unique.');

  const network = inspectRecord(data(snapshot, 'network'), '$.snapshot.network', ['mode', 'allowedDestinations'], issues);
  if (network) {
    if (!isOneOf(data(network, 'mode'), ['NORMAL', 'RESTRICTED', 'OFFLINE'])) addIssue(issues, 'INVALID_FIELD', '$.snapshot.network.mode', 'Unsupported network mode.');
    const destinations = inspectStringArray(data(network, 'allowedDestinations'), '$.snapshot.network.allowedDestinations', issues, true);
    if (destinations && duplicate(destinations)) addIssue(issues, 'DUPLICATE_IDENTIFIER', '$.snapshot.network.allowedDestinations', 'Destinations must be unique.');
    if (data(network, 'mode') === 'OFFLINE' && destinations?.length) addIssue(issues, 'INVALID_FIELD', '$.snapshot.network', 'OFFLINE evidence cannot allow destinations.');
  }
  const sandbox = inspectRecord(data(snapshot, 'sandbox'), '$.snapshot.sandbox', ['status', 'profile'], issues);
  if (sandbox) {
    const status = data(sandbox, 'status');
    if (!isOneOf(status, ['AVAILABLE', 'UNAVAILABLE', 'UNKNOWN'])) addIssue(issues, 'INVALID_FIELD', '$.snapshot.sandbox.status', 'Unsupported sandbox status.');
    inspectString(data(sandbox, 'profile'), '$.snapshot.sandbox.profile', issues, { nullable: true, id: data(sandbox, 'profile') !== null });
    if ((status === 'AVAILABLE') !== (data(sandbox, 'profile') !== null)) addIssue(issues, 'INVALID_FIELD', '$.snapshot.sandbox.profile', 'Sandbox profile must exist only when AVAILABLE.');
  }
  const bindings = inspectArray(data(snapshot, 'credentialBindings'), '$.snapshot.credentialBindings', issues);
  const bindingIds: string[] = [];
  bindings?.forEach((item, index) => {
    const row = inspectRecord(item, `$.snapshot.credentialBindings[${index}]`, ['bindingRef', 'status'], issues);
    if (!row) return;
    if (inspectString(data(row, 'bindingRef'), `$.snapshot.credentialBindings[${index}].bindingRef`, issues, { id: true })) bindingIds.push(data(row, 'bindingRef') as string);
    if (!isOneOf(data(row, 'status'), ['BOUND', 'MISSING', 'EXPIRED', 'UNKNOWN'])) addIssue(issues, 'INVALID_FIELD', `$.snapshot.credentialBindings[${index}].status`, 'Unsupported binding status.');
  });
  if (duplicate(bindingIds)) addIssue(issues, 'DUPLICATE_IDENTIFIER', '$.snapshot.credentialBindings', 'Credential binding references must be unique.');
  const boundaries = inspectStringArray(data(snapshot, 'writableBoundaries'), '$.snapshot.writableBoundaries', issues, true);
  if (boundaries && duplicate(boundaries)) addIssue(issues, 'DUPLICATE_IDENTIFIER', '$.snapshot.writableBoundaries', 'Writable boundaries must be unique.');
  const verification = inspectRecord(data(snapshot, 'verification'), '$.snapshot.verification', ['status', 'reasons'], issues);
  if (verification) {
    const status = data(verification, 'status');
    if (!isOneOf(status, ['PASS', 'WARN', 'FAIL', 'UNKNOWN'])) addIssue(issues, 'INVALID_FIELD', '$.snapshot.verification.status', 'Unsupported verification status.');
    const reasons = inspectStringArray(data(verification, 'reasons'), '$.snapshot.verification.reasons', issues, false, MAX_REASONS) ?? [];
    if (status === 'PASS' && reasons.length) addIssue(issues, 'INVALID_FIELD', '$.snapshot.verification.reasons', 'PASS verification cannot contain reasons.');
    if (status !== 'PASS' && reasons.length === 0) addIssue(issues, 'INVALID_FIELD', '$.snapshot.verification.reasons', 'Non-PASS verification requires reasons.');
    if (status !== 'PASS') reasons.forEach((reason) => blockingReasons.push(`verification:${reason}`));
  }
  return { snapshot: snapshot as unknown as CapabilityEnvironmentSnapshot, dependencyIds, availableIds, blockingReasons };
}

function validatePolicy(value: unknown, issues: CapabilityEnvironmentSnapshotEvidenceIssue[]): CapabilityEnvironmentSnapshotReadinessPolicyEvidence | null {
  const keys = ['readinessDecisionId', 'approvalRequired', 'existingApprovalValid', 'policyAllowed', 'provenanceVerified', 'integrityVerified', 'compatible', 'credentialsReady', 'networkReady', 'sandboxReady', 'evidenceRefs'];
  const policy = inspectRecord(value, '$.readinessPolicy', keys, issues);
  if (!policy) return null;
  inspectString(data(policy, 'readinessDecisionId'), '$.readinessPolicy.readinessDecisionId', issues, { id: true });
  for (const key of ['approvalRequired', 'existingApprovalValid'] as const) if (typeof data(policy, key) !== 'boolean') addIssue(issues, 'INVALID_FIELD', `$.readinessPolicy.${key}`, 'A boolean is required.');
  for (const key of ['policyAllowed', 'provenanceVerified', 'integrityVerified', 'compatible', 'credentialsReady', 'networkReady', 'sandboxReady'] as const) {
    const item = data(policy, key);
    if (item !== true && item !== false && item !== null) addIssue(issues, 'INVALID_FIELD', `$.readinessPolicy.${key}`, 'An explicit boolean or null is required.');
  }
  const refs = inspectStringArray(data(policy, 'evidenceRefs'), '$.readinessPolicy.evidenceRefs', issues, true);
  if (refs && duplicate(refs)) addIssue(issues, 'DUPLICATE_IDENTIFIER', '$.readinessPolicy.evidenceRefs', 'Evidence references must be unique.');
  return policy as unknown as CapabilityEnvironmentSnapshotReadinessPolicyEvidence;
}

function sameMembers(left: readonly string[], right: readonly string[]): boolean {
  return left.length === right.length && [...left].sort().every((item, index) => item === [...right].sort()[index]);
}

function safeResultIdentity(record: PlainRecord | null, key: string): string {
  const value = record ? data(record, key) : undefined;
  return validString(value, true) ? value : 'invalid';
}

function authorityFields() {
  return {
    authorityStatus: 'EVIDENCE_ONLY' as const,
    snapshotCollected: false as const,
    snapshotPersisted: false as const,
    environmentReadAuthorized: false as const,
    executionAuthorized: false as const,
    acquisitionAuthorized: false as const,
    mutationAuthorized: false as const,
    refreshAuthorized: false as const,
    taskAuthorityGranted: false as const,
    networkAuthorized: false as const,
  };
}

function freezeIssues(issues: CapabilityEnvironmentSnapshotEvidenceIssue[]): readonly CapabilityEnvironmentSnapshotEvidenceIssue[] {
  return Object.freeze([...issues].sort((left, right) => left.path.localeCompare(right.path) || left.code.localeCompare(right.code) || left.message.localeCompare(right.message)));
}

export function evaluateCapabilityEnvironmentSnapshotEvidence(input: unknown): CapabilityEnvironmentSnapshotEvidenceResult {
  const issues: CapabilityEnvironmentSnapshotEvidenceIssue[] = [];
  const envelope = inspectRecord(input, '$', ['schemaVersion', 'route', 'snapshot', 'readinessPolicy', 'now'], issues);
  if (envelope && data(envelope, 'schemaVersion') !== CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_CONTRACT_VERSION) addIssue(issues, 'INVALID_FIELD', '$.schemaVersion', 'Unsupported evidence-input version.');
  const nowValue = envelope ? data(envelope, 'now') : undefined;
  if (!validUtc(nowValue)) addIssue(issues, 'INVALID_FIELD', '$.now', 'Current time must be ISO-8601 UTC.');
  const route = envelope ? validateRoute(data(envelope, 'route'), issues) : null;
  const validatedSnapshot = envelope ? validateSnapshot(data(envelope, 'snapshot'), issues) : null;
  const policy = envelope ? validatePolicy(data(envelope, 'readinessPolicy'), issues) : null;
  const snapshotRecord = envelope ? descriptorRecord(data(envelope, 'snapshot')) : null;
  const routeRecord = envelope ? descriptorRecord(data(envelope, 'route')) : null;

  if (route && validatedSnapshot) {
    const snapshot = validatedSnapshot.snapshot;
    if (!route.primary) addIssue(issues, 'ROUTE_REJECTED', '$.route.primary', 'A primary route package is required.');
    if (route.stage !== 'FAST_ROUTE' || route.issues.length > 0) addIssue(issues, 'ROUTE_REJECTED', '$.route', 'Only a resolved issue-free FAST_ROUTE can support validated evidence.');
    if (route.workspaceId !== snapshot.workspaceId) addIssue(issues, 'BINDING_MISMATCH', '$.snapshot.workspaceId', 'Snapshot workspace does not match the route.');
    if (!route.environmentSnapshotRefs.includes(snapshot.snapshotId)) addIssue(issues, 'BINDING_MISMATCH', '$.snapshot.snapshotId', 'Route does not reference this snapshot.');
    if (route.environmentSnapshotRefs.length !== 1) addIssue(issues, 'BINDING_MISMATCH', '$.route.environmentSnapshotRefs', 'The route must reference exactly this one snapshot.');
    const packages = snapshot.packages;
    if (!route.primary || packages.length !== 1 || packages[0]?.packageId !== route.primary.packageId || packages[0]?.packageVersion !== route.primary.packageVersion) {
      addIssue(issues, 'BINDING_MISMATCH', '$.snapshot.packages', 'Snapshot packages must exactly match the primary route package and version.');
    }
    if (!sameMembers(route.supporting, validatedSnapshot.dependencyIds)) addIssue(issues, 'BINDING_MISMATCH', '$.snapshot.dependencies', 'Snapshot dependencies must exactly match route supporting dependencies.');
    if (validUtc(snapshot.observedAt) && validUtc(snapshot.expiresAt) && validUtc(nowValue)) {
      const observed = Date.parse(snapshot.observedAt);
      const expires = Date.parse(snapshot.expiresAt);
      const now = Date.parse(nowValue);
      if (!(observed <= now && now < expires && observed < expires)) addIssue(issues, 'FRESHNESS_INVALID', '$.snapshot', 'Snapshot must satisfy observedAt <= now < expiresAt and observedAt < expiresAt.');
    }
  }

  const evaluatedAt = validUtc(nowValue) ? nowValue : '1970-01-01T00:00:00Z';
  if (issues.length || !route || !validatedSnapshot || !policy) {
    return Object.freeze({
      schemaVersion: CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION,
      status: 'REJECTED',
      routeDecisionId: safeResultIdentity(routeRecord, 'routeDecisionId'),
      snapshotId: safeResultIdentity(snapshotRecord, 'snapshotId'),
      workspaceId: safeResultIdentity(snapshotRecord, 'workspaceId'),
      requiredDependencies: Object.freeze([]),
      availableDependencies: Object.freeze([]),
      blockingReasons: Object.freeze([]),
      issues: freezeIssues(issues),
      readiness: null,
      evaluatedAt,
      ...authorityFields(),
    });
  }

  const snapshot = validatedSnapshot.snapshot;
  const allCredentialsBound = snapshot.credentialBindings.every((binding) => binding.status === 'BOUND');
  const snapshotNetworkReady = snapshot.network.mode === 'NORMAL';
  const snapshotSandboxReady = snapshot.sandbox.status === 'AVAILABLE';
  const verificationPass = snapshot.verification.status === 'PASS';
  const readiness = evaluateCapabilityReadiness(route, {
    readinessDecisionId: policy.readinessDecisionId,
    snapshotId: snapshot.snapshotId,
    snapshotObservedAt: snapshot.observedAt,
    snapshotExpiresAt: snapshot.expiresAt,
    requiredDependencies: validatedSnapshot.dependencyIds,
    availableDependencies: validatedSnapshot.availableIds,
    approvalRequired: policy.approvalRequired,
    existingApprovalValid: policy.existingApprovalValid,
    policyAllowed: policy.policyAllowed,
    provenanceVerified: policy.provenanceVerified,
    integrityVerified: policy.integrityVerified === false || !verificationPass ? false : policy.integrityVerified,
    compatible: policy.compatible,
    credentialsReady: policy.credentialsReady === false || !allCredentialsBound ? false : policy.credentialsReady,
    networkReady: policy.networkReady === false || !snapshotNetworkReady ? false : policy.networkReady,
    sandboxReady: policy.sandboxReady === false || !snapshotSandboxReady ? false : policy.sandboxReady,
    evidenceRefs: policy.evidenceRefs,
  }, evaluatedAt);
  const ready = readiness.state === 'READY' || readiness.state === 'READY_WITH_EXISTING_APPROVAL';
  const blockingReasons = Object.freeze([...new Set([...validatedSnapshot.blockingReasons, ...readiness.blockingReasons])].sort());
  return Object.freeze({
    schemaVersion: CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION,
    status: ready ? 'VALIDATED_READY_EVIDENCE' : 'VALIDATED_BLOCKED_EVIDENCE',
    routeDecisionId: route.routeDecisionId,
    snapshotId: snapshot.snapshotId,
    workspaceId: snapshot.workspaceId,
    requiredDependencies: Object.freeze([...validatedSnapshot.dependencyIds]),
    availableDependencies: Object.freeze([...validatedSnapshot.availableIds]),
    blockingReasons,
    issues: Object.freeze([]),
    readiness,
    evaluatedAt,
    ...authorityFields(),
  });
}
