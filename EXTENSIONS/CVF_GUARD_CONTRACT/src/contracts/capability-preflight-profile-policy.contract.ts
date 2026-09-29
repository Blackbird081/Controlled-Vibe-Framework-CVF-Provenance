/**
 * Capability preflight profile policy selection kernel.
 *
 * Pure validation and selection only. This module never reads the filesystem,
 * observes the environment, grants authority, or executes anything. A selected
 * profile is a deterministic set of constraints and every result keeps all
 * action-authority literals false.
 */

import { isProxy } from 'node:util/types';
import {
  CAPABILITY_READINESS_DECISION_VERSION,
  CAPABILITY_ROUTE_DECISION_VERSION,
} from './capability-route-readiness.contract';
import type {
  CapabilityReadinessDecision,
  CapabilityRouteDecision,
} from './capability-route-readiness.contract';

export const CAPABILITY_PREFLIGHT_PROFILE_POLICY_CONTRACT_VERSION = 'cvf.capabilityPreflightProfilePolicy.v1' as const;
export const CAPABILITY_PREFLIGHT_PROFILE_POLICY_RESULT_VERSION = 'cvf.capabilityPreflightProfilePolicyResult.v1' as const;

export type CapabilityPreflightRiskLevel = 'R0' | 'R1' | 'R2' | 'R3';
export type CapabilityPreflightNetworkMode = 'NORMAL' | 'OFFLINE' | 'RESTRICTED';
export type CapabilityPreflightPrivilegePolicy = 'EXPLICIT_APPROVAL';

export interface CapabilityPreflightProfile {
  readonly profileId: string;
  readonly platforms: readonly string[];
  readonly shellPreference: readonly string[];
  readonly networkMode: CapabilityPreflightNetworkMode;
  readonly installPreference: readonly string[];
  readonly scanTtlSeconds: Readonly<Record<CapabilityPreflightRiskLevel, number>>;
  readonly privilegePolicy: CapabilityPreflightPrivilegePolicy;
  readonly pathDiscovery: readonly string[];
  readonly allowedDestinations: readonly string[];
  readonly notes: readonly string[];
}

export interface CapabilityPreflightProfilePolicyInput {
  readonly catalog: readonly CapabilityPreflightProfile[];
  readonly requestedProfileId: string;
  readonly observedPlatform: string;
  readonly riskLevel: CapabilityPreflightRiskLevel;
  readonly now: string;
  readonly routeEvidence?: CapabilityRouteDecision;
  readonly readinessEvidence?: CapabilityReadinessDecision;
}

export type CapabilityPreflightProfilePolicyIssueCode =
  | 'MALFORMED_INPUT'
  | 'INVALID_FIELD'
  | 'UNKNOWN_KEYS'
  | 'DUPLICATE_PROFILE_ID'
  | 'UNKNOWN_PROFILE'
  | 'PLATFORM_MISMATCH'
  | 'INVALID_TTL'
  | 'TTL_ORDERING_VIOLATION'
  | 'TTL_EXCEEDS_BOUND'
  | 'OFFLINE_DESTINATIONS_FORBIDDEN'
  | 'OFFLINE_INSTALL_PREFERENCE_FORBIDDEN'
  | 'PRIVILEGE_POLICY_VIOLATION'
  | 'SECRET_LIKE_CONTENT'
  | 'UNSAFE_PATH_FRAGMENT'
  | 'CONTROL_CHARACTER'
  | 'NON_LOWERCASE_DIGEST'
  | 'STALE_T4_EVIDENCE'
  | 'MALFORMED_T4_EVIDENCE'
  | 'T4_AUTHORITY_VIOLATION'
  | 'T4_BINDING_VIOLATION';

export interface CapabilityPreflightProfilePolicyIssue {
  readonly code: CapabilityPreflightProfilePolicyIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface CapabilityPreflightProfilePolicyResult {
  readonly schemaVersion: typeof CAPABILITY_PREFLIGHT_PROFILE_POLICY_RESULT_VERSION;
  readonly disposition: 'SELECTED' | 'REJECTED';
  readonly selectedProfileId: string;
  readonly observedPlatform: string;
  readonly riskLevel: CapabilityPreflightRiskLevel;
  readonly ttlSeconds: number;
  readonly networkMode: CapabilityPreflightNetworkMode;
  readonly platforms: readonly string[];
  readonly shellPreference: readonly string[];
  readonly installPreference: readonly string[];
  readonly pathDiscovery: readonly string[];
  readonly allowedDestinations: readonly string[];
  readonly privilegePolicy: CapabilityPreflightPrivilegePolicy;
  readonly notes: readonly string[];
  readonly executionAuthorized: false;
  readonly acquisitionAuthorized: false;
  readonly networkAuthorized: false;
  readonly taskAuthorityGranted: false;
  readonly mutationAuthorized: false;
  readonly evaluatedAt: string;
  readonly issues: readonly CapabilityPreflightProfilePolicyIssue[];
}

const RISK_LEVELS: readonly CapabilityPreflightRiskLevel[] = ['R0', 'R1', 'R2', 'R3'];
const NETWORK_MODES: readonly CapabilityPreflightNetworkMode[] = ['NORMAL', 'OFFLINE', 'RESTRICTED'];
const ROUTE_STAGES = ['FAST_ROUTE', 'FULL_RESOLUTION_REQUIRED', 'AMBIGUOUS_ROUTE', 'NO_CANDIDATE'] as const;
const READINESS_STATES = [
  'READY', 'READY_WITH_EXISTING_APPROVAL', 'BOOTSTRAP_REQUIRED', 'APPROVAL_REQUIRED',
  'BLOCKED_POLICY', 'BLOCKED_PROVENANCE', 'BLOCKED_INTEGRITY', 'BLOCKED_COMPATIBILITY',
  'BLOCKED_CREDENTIAL', 'BLOCKED_NETWORK', 'BLOCKED_SANDBOX', 'STALE_SNAPSHOT',
  'AMBIGUOUS_ROUTE', 'UNKNOWN',
] as const;
const PROFILE_KEYS: readonly string[] = [
  'profileId', 'platforms', 'shellPreference', 'networkMode', 'installPreference',
  'scanTtlSeconds', 'privilegePolicy', 'pathDiscovery', 'allowedDestinations', 'notes',
];
const INPUT_KEYS: readonly string[] = [
  'catalog', 'requestedProfileId', 'observedPlatform', 'riskLevel', 'now',
  'routeEvidence', 'readinessEvidence',
];
const OFFLINE_INSTALL_PREFERENCES: readonly string[] = ['existing-only', 'verified-local-artifact'];

const MAX_STRING = 256;
const MAX_ARRAY = 64;
const MAX_CATALOG = 32;
const MAX_TTL = 86400;
const MAX_EVIDENCE_AGE_SECONDS = 86400;

const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const SAFE_TOKEN = /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/;
const SAFE_PATH_DISCOVERY = /^[A-Za-z0-9][A-Za-z0-9._ -]{0,127}$/;
const SAFE_DESTINATION = /^[A-Za-z0-9][A-Za-z0-9._:/-]{0,255}$/;
const CONTROL_CHAR = /[\u0000-\u001F\u007F]/;
const SECRET_SIGNAL = /(secret|token|password|credential\s*=|api[_-]?key)/i;
const UNSAFE_PATH_FRAGMENT = /(\.\.|^[/\\]|[;|&<>`$]|[\u0000-\u001F\u007F])/;
const SHA256_DIGEST = /^[0-9a-fA-F]{64}$/;
const LOWERCASE_SHA256 = /^[a-f0-9]{64}$/;

function issue(code: CapabilityPreflightProfilePolicyIssueCode, path: string, message: string): CapabilityPreflightProfilePolicyIssue {
  return Object.freeze({ code, path, message });
}

function isPlainRecord(value: unknown): value is Record<string, unknown> {
  if (value === null || typeof value !== 'object' || isProxy(value)) return false;
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

function hasAccessorProperties(value: object): boolean {
  for (const key of Reflect.ownKeys(value)) {
    const descriptor = Object.getOwnPropertyDescriptor(value, key);
    if (descriptor && (typeof descriptor.get === 'function' || typeof descriptor.set === 'function')) return true;
  }
  return false;
}

function validUtc(value: unknown): value is string {
  if (typeof value !== 'string' || !ISO_UTC.test(value) || !Number.isFinite(Date.parse(value))) return false;
  const [datePart, timePart] = value.split('T');
  const [year, month, day] = datePart.split('-').map(Number);
  const [hour, minute, second] = timePart.slice(0, 8).split(':').map(Number);
  const parsed = new Date(0);
  parsed.setUTCFullYear(year, month - 1, day);
  parsed.setUTCHours(hour, minute, second, 0);
  return parsed.getUTCFullYear() === year
    && parsed.getUTCMonth() === month - 1
    && parsed.getUTCDate() === day
    && parsed.getUTCHours() === hour
    && parsed.getUTCMinutes() === minute
    && parsed.getUTCSeconds() === second;
}

function isSafeArray(value: unknown): value is unknown[] {
  return Array.isArray(value) && !isProxy(value) && !hasAccessorProperties(value);
}

function validId(value: unknown): value is string {
  return typeof value === 'string' && SAFE_ID.test(value);
}

function isSafeToken(value: unknown): value is string {
  return typeof value === 'string' && SAFE_TOKEN.test(value);
}

function hasControlChars(value: string): boolean {
  return CONTROL_CHAR.test(value);
}

function hasSecretSignal(value: string): boolean {
  return SECRET_SIGNAL.test(value);
}

function hasNonLowercaseDigest(value: string): boolean {
  return SHA256_DIGEST.test(value) && !LOWERCASE_SHA256.test(value);
}

function checkUnknownKeys(record: Record<string, unknown>, allowed: readonly string[], path: string, issues: CapabilityPreflightProfilePolicyIssue[]): void {
  for (const key of Reflect.ownKeys(record)) {
    if (typeof key !== 'string' || !allowed.includes(key)) {
      const renderedKey = typeof key === 'symbol' ? key.toString() : key;
      issues.push(issue('UNKNOWN_KEYS', `${path}.${renderedKey}`, `Unknown key "${renderedKey}" is not allowed.`));
    }
  }
}

function validateBoundedString(
  value: unknown,
  path: string,
  kind: 'id' | 'token' | 'path-discovery' | 'destination' | 'free',
  issues: CapabilityPreflightProfilePolicyIssue[],
): string | null {
  if (typeof value !== 'string') {
    issues.push(issue('INVALID_FIELD', path, 'Expected a string.'));
    return null;
  }
  if (value.length === 0 || value.length > MAX_STRING) {
    issues.push(issue('INVALID_FIELD', path, `String length must be between 1 and ${MAX_STRING}.`));
    return null;
  }
  if (hasControlChars(value)) {
    issues.push(issue('CONTROL_CHARACTER', path, 'Control characters are not allowed.'));
    return null;
  }
  if (hasSecretSignal(value)) {
    issues.push(issue('SECRET_LIKE_CONTENT', path, 'Secret-like content is not allowed.'));
    return null;
  }
  if (hasNonLowercaseDigest(value)) {
    issues.push(issue('NON_LOWERCASE_DIGEST', path, 'SHA-256 digests must be lowercase.'));
    return null;
  }
  if (kind === 'id' && !validId(value)) {
    issues.push(issue('INVALID_FIELD', path, 'Expected a bounded safe identifier.'));
    return null;
  }
  if (kind === 'token' && !isSafeToken(value)) {
    issues.push(issue('INVALID_FIELD', path, 'Expected a bounded safe token.'));
    return null;
  }
  if (kind === 'path-discovery') {
    if (!SAFE_PATH_DISCOVERY.test(value) || UNSAFE_PATH_FRAGMENT.test(value)) {
      issues.push(issue('UNSAFE_PATH_FRAGMENT', path, 'Path-discovery string contains an unsafe fragment.'));
      return null;
    }
  }
  if (kind === 'destination' && !SAFE_DESTINATION.test(value)) {
    issues.push(issue('INVALID_FIELD', path, 'Expected a bounded destination string.'));
    return null;
  }
  return value;
}

function validateStringArray(
  value: unknown,
  path: string,
  kind: 'id' | 'token' | 'path-discovery' | 'destination' | 'free',
  allowEmpty: boolean,
  issues: CapabilityPreflightProfilePolicyIssue[],
): readonly string[] {
  if (!isSafeArray(value)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Expected a non-Proxy array without accessors.'));
    return [];
  }
  if (value.length > MAX_ARRAY || (!allowEmpty && value.length === 0)) {
    issues.push(issue('INVALID_FIELD', path, `Array length must be ${allowEmpty ? 'at most' : 'between 1 and'} ${MAX_ARRAY}.`));
    return [];
  }
  for (let index = 0; index < value.length; index += 1) {
    if (!(index in value)) {
      issues.push(issue('MALFORMED_INPUT', `${path}[${index}]`, 'Sparse arrays are not allowed.'));
      return [];
    }
  }
  const result: string[] = [];
  value.forEach((item, index) => {
    const validated = validateBoundedString(item, `${path}[${index}]`, kind, issues);
    if (validated !== null) result.push(validated);
  });
  return Object.freeze(result);
}

function validateProfile(profile: unknown, index: number, issues: CapabilityPreflightProfilePolicyIssue[]): CapabilityPreflightProfile | null {
  const path = `$.catalog[${index}]`;
  if (!isPlainRecord(profile) || hasAccessorProperties(profile)) {
    issues.push(issue('MALFORMED_INPUT', path, 'Profile must be a plain non-Proxy object without accessors.'));
    return null;
  }
  checkUnknownKeys(profile, PROFILE_KEYS, path, issues);
  const profileId = validateBoundedString(profile.profileId, `${path}.profileId`, 'id', issues);
  const platforms = validateStringArray(profile.platforms, `${path}.platforms`, 'token', false, issues);
  const shellPreference = validateStringArray(profile.shellPreference, `${path}.shellPreference`, 'token', false, issues);
  const installPreference = validateStringArray(profile.installPreference, `${path}.installPreference`, 'token', false, issues);
  const pathDiscovery = validateStringArray(profile.pathDiscovery, `${path}.pathDiscovery`, 'path-discovery', true, issues);
  const allowedDestinations = validateStringArray(profile.allowedDestinations, `${path}.allowedDestinations`, 'destination', true, issues);
  const notes = validateStringArray(profile.notes, `${path}.notes`, 'free', true, issues);

  if (typeof profile.networkMode !== 'string' || !NETWORK_MODES.includes(profile.networkMode as CapabilityPreflightNetworkMode)) {
    issues.push(issue('INVALID_FIELD', `${path}.networkMode`, 'Unsupported network mode.'));
  }
  if (profile.privilegePolicy !== 'EXPLICIT_APPROVAL') {
    issues.push(issue('PRIVILEGE_POLICY_VIOLATION', `${path}.privilegePolicy`, 'Privilege policy must remain EXPLICIT_APPROVAL.'));
  }

  const ttlRecord: Record<CapabilityPreflightRiskLevel, number> = { R0: NaN, R1: NaN, R2: NaN, R3: NaN };
  const scanTtlSeconds = isPlainRecord(profile.scanTtlSeconds) && !hasAccessorProperties(profile.scanTtlSeconds)
    ? profile.scanTtlSeconds
    : null;
  if (scanTtlSeconds === null) {
    issues.push(issue('MALFORMED_INPUT', `${path}.scanTtlSeconds`, 'TTL map must be a plain object.'));
  } else {
    checkUnknownKeys(scanTtlSeconds, RISK_LEVELS, `${path}.scanTtlSeconds`, issues);
    for (const level of RISK_LEVELS) {
      const raw = scanTtlSeconds[level];
      if (raw === undefined) {
        issues.push(issue('INVALID_TTL', `${path}.scanTtlSeconds.${level}`, `Missing TTL for ${level}.`));
        continue;
      }
      if (typeof raw !== 'number' || !Number.isInteger(raw) || raw <= 0) {
        issues.push(issue('INVALID_TTL', `${path}.scanTtlSeconds.${level}`, `TTL for ${level} must be a positive integer.`));
        continue;
      }
      if (raw > MAX_TTL) {
        issues.push(issue('TTL_EXCEEDS_BOUND', `${path}.scanTtlSeconds.${level}`, `TTL for ${level} must be at most ${MAX_TTL}.`));
        continue;
      }
      ttlRecord[level] = raw;
    }
    for (let i = 1; i < RISK_LEVELS.length; i += 1) {
      const previous = ttlRecord[RISK_LEVELS[i - 1]];
      const current = ttlRecord[RISK_LEVELS[i]];
      if (Number.isFinite(previous) && Number.isFinite(current) && current > previous) {
        issues.push(issue('TTL_ORDERING_VIOLATION', `${path}.scanTtlSeconds.${RISK_LEVELS[i]}`, 'TTL must not increase as risk increases.'));
      }
    }
  }

  const networkMode = typeof profile.networkMode === 'string' && NETWORK_MODES.includes(profile.networkMode as CapabilityPreflightNetworkMode)
    ? profile.networkMode as CapabilityPreflightNetworkMode
    : 'NORMAL';

  if (networkMode === 'OFFLINE') {
    if (allowedDestinations.length > 0) {
      issues.push(issue('OFFLINE_DESTINATIONS_FORBIDDEN', `${path}.allowedDestinations`, 'OFFLINE profile must declare zero destinations.'));
    }
    for (let i = 0; i < installPreference.length; i += 1) {
      if (!OFFLINE_INSTALL_PREFERENCES.includes(installPreference[i])) {
        issues.push(issue('OFFLINE_INSTALL_PREFERENCE_FORBIDDEN', `${path}.installPreference[${i}]`, 'OFFLINE install preferences are limited to existing or verified-local artifact classes.'));
      }
    }
  }

  if (profileId === null || platforms.length === 0) {
    return null;
  }

  return Object.freeze({
    profileId,
    platforms,
    shellPreference,
    networkMode,
    installPreference,
    scanTtlSeconds: Object.freeze(ttlRecord),
    privilegePolicy: 'EXPLICIT_APPROVAL' as const,
    pathDiscovery,
    allowedDestinations,
    notes,
  });
}

function validateT4Evidence(
  route: unknown,
  readiness: unknown,
  now: string,
  issues: CapabilityPreflightProfilePolicyIssue[],
): { route: CapabilityRouteDecision | null; readiness: CapabilityReadinessDecision | null } {
  let validRoute: CapabilityRouteDecision | null = null;
  let validReadiness: CapabilityReadinessDecision | null = null;

  if (route !== undefined) {
    if (!isPlainRecord(route) || hasAccessorProperties(route)) {
      issues.push(issue('MALFORMED_T4_EVIDENCE', '$.routeEvidence', 'Route evidence must be a plain object.'));
    } else {
      const record = route as unknown as Record<string, unknown>;
      if (record.schemaVersion !== CAPABILITY_ROUTE_DECISION_VERSION) {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.routeEvidence.schemaVersion', 'Unsupported route evidence schema.'));
      }
      if (record.authorityStatus !== 'CANDIDATE_ONLY') {
        issues.push(issue('T4_AUTHORITY_VIOLATION', '$.routeEvidence.authorityStatus', 'Route evidence must remain candidate-only.'));
      }
      if (record.executionAuthorized !== false) {
        issues.push(issue('T4_AUTHORITY_VIOLATION', '$.routeEvidence.executionAuthorized', 'Route evidence must keep executionAuthorized false.'));
      }
      if (!isSafeArray(record.issues)) {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.routeEvidence.issues', 'Route evidence issues must be a non-Proxy array without accessors.'));
      } else if (record.issues.length > 0) {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.routeEvidence.issues', 'Route evidence must be issue-free.'));
      }
      if (typeof record.stage !== 'string' || !ROUTE_STAGES.includes(record.stage as typeof ROUTE_STAGES[number])) {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.routeEvidence.stage', 'Route evidence stage is invalid.'));
      } else if (record.stage === 'AMBIGUOUS_ROUTE') {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.routeEvidence.stage', 'Ambiguous route evidence is not accepted.'));
      }
      if (!validUtc(record.generatedAt) || Date.parse(record.generatedAt as string) > Date.parse(now)) {
        issues.push(issue('STALE_T4_EVIDENCE', '$.routeEvidence.generatedAt', 'Route evidence must be valid and not in the future.'));
      } else if (Date.parse(now) - Date.parse(record.generatedAt as string) > MAX_EVIDENCE_AGE_SECONDS * 1000) {
        issues.push(issue('STALE_T4_EVIDENCE', '$.routeEvidence.generatedAt', 'Route evidence is stale.'));
      }
      if (!validId(record.routeDecisionId)) {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.routeEvidence.routeDecisionId', 'Route decision id is invalid.'));
      } else {
        validRoute = route as unknown as CapabilityRouteDecision;
      }
    }
  }

  if (readiness !== undefined) {
    if (!isPlainRecord(readiness) || hasAccessorProperties(readiness)) {
      issues.push(issue('MALFORMED_T4_EVIDENCE', '$.readinessEvidence', 'Readiness evidence must be a plain object.'));
    } else {
      const record = readiness as unknown as Record<string, unknown>;
      if (record.schemaVersion !== CAPABILITY_READINESS_DECISION_VERSION) {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.readinessEvidence.schemaVersion', 'Unsupported readiness evidence schema.'));
      }
      if (record.authorityStatus !== 'EVIDENCE_ONLY') {
        issues.push(issue('T4_AUTHORITY_VIOLATION', '$.readinessEvidence.authorityStatus', 'Readiness evidence must remain evidence-only.'));
      }
      if (record.executionAuthorized !== false) {
        issues.push(issue('T4_AUTHORITY_VIOLATION', '$.readinessEvidence.executionAuthorized', 'Readiness evidence must keep executionAuthorized false.'));
      }
      if (!validUtc(record.evaluatedAt) || Date.parse(record.evaluatedAt as string) > Date.parse(now)) {
        issues.push(issue('STALE_T4_EVIDENCE', '$.readinessEvidence.evaluatedAt', 'Readiness evidence must be valid and not in the future.'));
      } else if (Date.parse(now) - Date.parse(record.evaluatedAt as string) > MAX_EVIDENCE_AGE_SECONDS * 1000) {
        issues.push(issue('STALE_T4_EVIDENCE', '$.readinessEvidence.evaluatedAt', 'Readiness evidence is stale.'));
      }
      if (!validId(record.readinessDecisionId) || !validId(record.routeDecisionId) || !validId(record.snapshotId)) {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.readinessEvidence', 'Readiness evidence ids are invalid.'));
      }
      const blockedStates: readonly string[] = ['BLOCKED_POLICY', 'BLOCKED_PROVENANCE', 'BLOCKED_INTEGRITY', 'BLOCKED_COMPATIBILITY', 'BLOCKED_CREDENTIAL', 'BLOCKED_NETWORK', 'BLOCKED_SANDBOX', 'STALE_SNAPSHOT', 'AMBIGUOUS_ROUTE', 'UNKNOWN'];
      if (typeof record.state !== 'string' || !READINESS_STATES.includes(record.state as typeof READINESS_STATES[number])) {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.readinessEvidence.state', 'Readiness evidence state is invalid.'));
      } else if (blockedStates.includes(record.state)) {
        issues.push(issue('MALFORMED_T4_EVIDENCE', '$.readinessEvidence.state', 'Readiness evidence must not be in a blocked or unknown state.'));
      } else {
        validReadiness = readiness as unknown as CapabilityReadinessDecision;
      }
    }
  }

  if (validRoute !== null && validReadiness !== null && validReadiness.routeDecisionId !== validRoute.routeDecisionId) {
    issues.push(issue('T4_BINDING_VIOLATION', '$.readinessEvidence.routeDecisionId', 'Readiness evidence is not bound to the route decision.'));
  }

  return { route: validRoute, readiness: validReadiness };
}

function buildResult(
  disposition: 'SELECTED' | 'REJECTED',
  selected: CapabilityPreflightProfile | null,
  requestedProfileId: string,
  observedPlatform: string,
  riskLevel: CapabilityPreflightRiskLevel,
  now: string,
  issues: readonly CapabilityPreflightProfilePolicyIssue[],
): CapabilityPreflightProfilePolicyResult {
  const ttl = selected !== null ? selected.scanTtlSeconds[riskLevel] : 0;
  return Object.freeze({
    schemaVersion: CAPABILITY_PREFLIGHT_PROFILE_POLICY_RESULT_VERSION,
    disposition,
    selectedProfileId: selected?.profileId ?? (validId(requestedProfileId) ? requestedProfileId : 'invalid'),
    observedPlatform: isSafeToken(observedPlatform) ? observedPlatform : 'invalid',
    riskLevel,
    ttlSeconds: Number.isFinite(ttl) ? ttl : 0,
    networkMode: selected?.networkMode ?? 'NORMAL',
    platforms: Object.freeze(selected?.platforms.slice() ?? []),
    shellPreference: Object.freeze(selected?.shellPreference.slice() ?? []),
    installPreference: Object.freeze(selected?.installPreference.slice() ?? []),
    pathDiscovery: Object.freeze(selected?.pathDiscovery.slice() ?? []),
    allowedDestinations: Object.freeze(selected?.allowedDestinations.slice() ?? []),
    privilegePolicy: selected?.privilegePolicy ?? 'EXPLICIT_APPROVAL',
    notes: Object.freeze(selected?.notes.slice() ?? []),
    executionAuthorized: false,
    acquisitionAuthorized: false,
    networkAuthorized: false,
    taskAuthorityGranted: false,
    mutationAuthorized: false,
    evaluatedAt: validUtc(now) ? now : '1970-01-01T00:00:00Z',
    issues: Object.freeze([...issues]),
  });
}

export function evaluateCapabilityPreflightProfilePolicy(
  input: unknown,
): CapabilityPreflightProfilePolicyResult {
  const issues: CapabilityPreflightProfilePolicyIssue[] = [];
  if (!isPlainRecord(input) || hasAccessorProperties(input)) {
    return buildResult('REJECTED', null, 'invalid', 'invalid', 'R0', '1970-01-01T00:00:00Z', [
      issue('MALFORMED_INPUT', '$', 'Input must be a plain non-Proxy object without accessors.'),
    ]);
  }
  checkUnknownKeys(input, INPUT_KEYS, '$', issues);

  const now = typeof input.now === 'string' && validUtc(input.now) ? input.now : null;
  if (now === null) {
    issues.push(issue('INVALID_FIELD', '$.now', 'Current time must be ISO-8601 UTC.'));
  }
  const requestedProfileId = validateBoundedString(input.requestedProfileId, '$.requestedProfileId', 'id', issues);
  const observedPlatform = validateBoundedString(input.observedPlatform, '$.observedPlatform', 'token', issues);
  const riskLevel = typeof input.riskLevel === 'string' && RISK_LEVELS.includes(input.riskLevel as CapabilityPreflightRiskLevel)
    ? input.riskLevel as CapabilityPreflightRiskLevel
    : 'R0';
  if (!RISK_LEVELS.includes(input.riskLevel as CapabilityPreflightRiskLevel)) {
    issues.push(issue('INVALID_FIELD', '$.riskLevel', 'Unsupported risk level.'));
  }

  const catalogValue = input.catalog;
  let profiles: CapabilityPreflightProfile[] = [];
  if (!isSafeArray(catalogValue)) {
    issues.push(issue('MALFORMED_INPUT', '$.catalog', 'Catalog must be a non-Proxy array without accessors.'));
  } else if (catalogValue.length === 0 || catalogValue.length > MAX_CATALOG) {
    issues.push(issue('INVALID_FIELD', '$.catalog', `Catalog length must be between 1 and ${MAX_CATALOG}.`));
  } else {
    for (let index = 0; index < catalogValue.length; index += 1) {
      if (!(index in catalogValue)) {
        issues.push(issue('MALFORMED_INPUT', `$.catalog[${index}]`, 'Sparse arrays are not allowed.'));
        break;
      }
    }
    const seen = new Set<string>();
    const parsed: CapabilityPreflightProfile[] = [];
    catalogValue.forEach((profile, index) => {
      const validated = validateProfile(profile, index, issues);
      if (validated !== null) {
        if (seen.has(validated.profileId)) {
          issues.push(issue('DUPLICATE_PROFILE_ID', `$.catalog[${index}].profileId`, 'Profile IDs must be unique.'));
        } else {
          seen.add(validated.profileId);
          parsed.push(validated);
        }
      }
    });
    profiles = parsed;
  }

  validateT4Evidence(input.routeEvidence, input.readinessEvidence, now ?? '1970-01-01T00:00:00Z', issues);

  let selected: CapabilityPreflightProfile | null = null;
  if (requestedProfileId !== null && profiles.length > 0) {
    const match = profiles.find((profile) => profile.profileId === requestedProfileId);
    if (match === undefined) {
      issues.push(issue('UNKNOWN_PROFILE', '$.requestedProfileId', 'Requested profile was not found in the catalog.'));
    } else if (observedPlatform !== null && !match.platforms.includes(observedPlatform)) {
      issues.push(issue('PLATFORM_MISMATCH', '$.observedPlatform', 'Observed platform is not a member of the requested profile.'));
    } else {
      selected = match;
    }
  }

  const disposition = issues.length === 0 && selected !== null ? 'SELECTED' : 'REJECTED';
  return buildResult(
    disposition,
    disposition === 'SELECTED' ? selected : null,
    requestedProfileId ?? 'invalid',
    observedPlatform ?? 'invalid',
    riskLevel,
    now ?? '1970-01-01T00:00:00Z',
    issues,
  );
}
