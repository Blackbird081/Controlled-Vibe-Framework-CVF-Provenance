/**
 * CADP-AI-T5-R1 external readout authority foundation.
 *
 * Pure, deterministic, side-effect-free TypeScript contracts for a possible
 * future CADP external read/query surface. This file defines shape-only
 * building blocks: an exact read-only metadata allowlist, a caller-identity
 * input contract, an ingress schema/size validator, a secret/private-
 * provenance redaction function, a deterministic external receipt/error
 * contract, and a replay/freshness contract.
 *
 * This module does not register a transport, does not accept or resolve a
 * credential, does not call a provider or the network, and does not mutate
 * state. `externalReadoutAuthorized` and every other authority-adjacent
 * field is a literal `false`. No export from this module authorizes an MCP
 * tool, CLI command, or external-agent invocation; the invocation moratorium
 * recorded in `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md`
 * is unaffected by this file.
 */

import { createHash } from 'node:crypto';
import { isProxy } from 'node:util/types';

export const CADP_EXTERNAL_READOUT_FOUNDATION_CONTRACT_VERSION = 'cvf.cadp.externalReadoutFoundation.v1' as const;

/**
 * Field names this foundation treats as secret or private-provenance
 * material. Mirrors the rejection intent of the T1 contract's
 * `RAW_SECRET_INCLUDED` / `PRIVATE_PROVENANCE_EXPORT` invariants
 * (`capability-admission-distribution-profile.contract.ts`), narrowed to the
 * field-name shapes an external read-only payload could plausibly carry.
 */
export const CADP_EXTERNAL_READOUT_REDACTED_FIELD_NAMES: readonly string[] = Object.freeze([
  'secret',
  'secrets',
  'rawSecret',
  'rawSecrets',
  'credential',
  'credentials',
  'credentialReference',
  'token',
  'apiKey',
  'privateProvenance',
  'privateProvenanceRef',
]);

/** Path-substring markers this foundation treats as private-provenance. */
const PRIVATE_PROVENANCE_PATH_MARKERS: readonly string[] = Object.freeze([
  'cvf_session/',
  '/private/',
  'provenance',
]);

export type CadpExternalReadoutIssueCode =
  | 'MALFORMED_REQUEST'
  | 'UNKNOWN_FIELD'
  | 'REQUEST_TOO_LARGE'
  | 'INVALID_CALLER_IDENTITY'
  | 'REDACTED_FIELD_PRESENT'
  | 'PRIVATE_PROVENANCE_PATH'
  | 'STALE_REQUEST'
  | 'REPLAY_WINDOW_EXCEEDED'
  | 'INVALID_TIMESTAMP';

export interface CadpExternalReadoutIssue {
  readonly code: CadpExternalReadoutIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface CadpExternalReadoutValidationResult<TData> {
  readonly valid: boolean;
  readonly issues: readonly CadpExternalReadoutIssue[];
  readonly data: TData;
}

/**
 * Exact read-only metadata field allowlist for a future CADP external
 * readout response. Every field is either a plain scalar/array of scalars
 * or a literal `false` authority marker; no field carries a secret,
 * credential, or provenance path.
 */
export interface CadpExternalReadoutAllowlistedMetadata {
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly admissionDecision: string;
  readonly assignedActionIds: readonly string[];
  readonly evidenceLevel: string;
  readonly externalReadoutAuthorized: false;
  readonly externalMutationAuthorized: false;
  readonly externalActivationAuthorized: false;
  readonly externalExecutionAuthorized: false;
  readonly externalProviderCallAuthorized: false;
  readonly externalCredentialResolutionAuthorized: false;
}

/**
 * External caller identity input contract. Shape only: this type carries no
 * credential, token, or secret, and no function in this module resolves or
 * validates it against any credential store. It exists so a future ingress
 * contract has a stable, source-verified identity shape to reference.
 */
export interface CadpExternalCallerIdentityInput {
  readonly callerId: string;
  readonly requestedScope: readonly string[];
  readonly requestTimestamp: string;
}

/** Ingress envelope for a hypothetical external readout request. */
export interface CadpExternalReadoutIngressRequest {
  readonly identity: CadpExternalCallerIdentityInput;
  readonly capabilityId: string;
  readonly requestedFields: readonly string[];
}

export interface CadpExternalReadoutFreshnessInput {
  readonly issuedAt: string;
  readonly expiresAt: string;
  readonly observedAt: string;
}

export type CadpExternalReadoutFreshnessDisposition = 'FRESH' | 'STALE' | 'EXPIRED' | 'INVALID';

export interface CadpExternalReadoutFreshnessResult {
  readonly disposition: CadpExternalReadoutFreshnessDisposition;
  readonly issues: readonly CadpExternalReadoutIssue[];
}

export interface CadpExternalReadoutReceiptInput<TPayload> {
  readonly requestId: string;
  readonly issuedAt: string;
  readonly payload: TPayload;
}

export interface CadpExternalReadoutReceipt<TPayload> {
  readonly contractVersion: typeof CADP_EXTERNAL_READOUT_FOUNDATION_CONTRACT_VERSION;
  readonly receiptId: string;
  readonly requestId: string;
  readonly issuedAt: string;
  readonly payload: TPayload;
  readonly integrityHash: string;
  readonly receiptGrantsExecution: false;
  readonly receiptGrantsMutation: false;
  readonly receiptGrantsActivation: false;
}

const MAX_INGRESS_REQUESTED_FIELDS = 32;
const MAX_INGRESS_SCOPE_ENTRIES = 16;
const MAX_INGRESS_STRING_LENGTH = 512;
const REPLAY_WINDOW_MILLISECONDS = 5 * 60 * 1000;
const STALE_REQUEST_MILLISECONDS = 24 * 60 * 60 * 1000;
const ISO8601_UTC_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,9})?Z$/;
const DAYS_IN_MONTH: readonly number[] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

const ALLOWLISTED_METADATA_KEYS: readonly string[] = Object.freeze([
  'capabilityId',
  'capabilityVersion',
  'admissionDecision',
  'assignedActionIds',
  'evidenceLevel',
  'externalReadoutAuthorized',
  'externalMutationAuthorized',
  'externalActivationAuthorized',
  'externalExecutionAuthorized',
  'externalProviderCallAuthorized',
  'externalCredentialResolutionAuthorized',
]);

function issue(code: CadpExternalReadoutIssueCode, path: string, message: string): CadpExternalReadoutIssue {
  return Object.freeze({ code, path, message });
}

/** Trap-free reflection-target check, matching the T1 contract's Proxy-rejection idiom. */
function isSupportedReflectionTarget(value: unknown): boolean {
  if (value === null || (typeof value !== 'object' && typeof value !== 'function')) return true;
  return !isProxy(value);
}

function isPlainRecord(value: unknown): value is Record<string, unknown> {
  if (value === null || typeof value !== 'object') return false;
  if (!isSupportedReflectionTarget(value)) return false;
  const proto = Object.getPrototypeOf(value);
  return proto === Object.prototype || proto === null;
}

/** Own, enumerable, non-accessor data property read only; never a caller-controlled accessor. */
function ownDataField(owner: unknown, key: string): { readonly present: boolean; readonly value: unknown } {
  if (owner === null || (typeof owner !== 'object' && typeof owner !== 'function')) {
    return { present: false, value: undefined };
  }
  if (!isSupportedReflectionTarget(owner)) {
    return { present: false, value: undefined };
  }
  const descriptor = Object.getOwnPropertyDescriptor(owner, key);
  if (!descriptor || !descriptor.enumerable || 'get' in descriptor || 'set' in descriptor) {
    return { present: false, value: undefined };
  }
  return { present: true, value: descriptor.value };
}

function readOwnDataStringArray(value: unknown, maxLength: number): readonly string[] | undefined {
  if (!isSupportedReflectionTarget(value)) return undefined;
  if (!Array.isArray(value)) return undefined;
  if (Object.getOwnPropertySymbols(value).length > 0) return undefined;
  if (value.length > maxLength) return undefined;
  const ownKeys = Object.getOwnPropertyNames(value);
  const expectedKeyCount = value.length + 1;
  if (ownKeys.length !== expectedKeyCount) return undefined;
  const expectedKeys = new Set<string>(['length']);
  for (let index = 0; index < value.length; index += 1) expectedKeys.add(String(index));
  for (const key of ownKeys) {
    if (!expectedKeys.has(key)) return undefined;
  }
  const result: string[] = [];
  for (let index = 0; index < value.length; index += 1) {
    const descriptor = Object.getOwnPropertyDescriptor(value, index);
    if (!descriptor || !descriptor.enumerable || 'get' in descriptor || 'set' in descriptor) return undefined;
    if (typeof descriptor.value !== 'string' || descriptor.value.length > MAX_INGRESS_STRING_LENGTH) return undefined;
    result.push(descriptor.value);
  }
  return result;
}

function isLeapYear(year: number): boolean {
  return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
}

/** Reject regex-shaped timestamps that are not real UTC calendar instants. */
function isValidIso8601UtcTimestamp(value: unknown): value is string {
  if (typeof value !== 'string' || !ISO8601_UTC_PATTERN.test(value)) return false;
  const year = Number(value.slice(0, 4));
  const month = Number(value.slice(5, 7));
  const day = Number(value.slice(8, 10));
  const hour = Number(value.slice(11, 13));
  const minute = Number(value.slice(14, 16));
  const second = Number(value.slice(17, 19));
  if (month < 1 || month > 12) return false;
  const maxDay = month === 2 && isLeapYear(year) ? 29 : DAYS_IN_MONTH[month - 1];
  return day >= 1 && day <= maxDay && hour <= 23 && minute <= 59 && second <= 59;
}

/**
 * Canonicalize the supported JSON data domain without invoking accessors,
 * proxy traps, iterators, or caller-defined `toJSON` methods. The returned
 * snapshot is independently owned and recursively frozen.
 */
function canonicalSnapshot(
  value: unknown,
  active: WeakSet<object>,
): { readonly json: string; readonly snapshot: unknown } {
  if (value === null) return { json: 'null', snapshot: null };
  if (typeof value === 'string' || typeof value === 'boolean') {
    return { json: JSON.stringify(value), snapshot: value };
  }
  if (typeof value === 'number') {
    if (!Number.isFinite(value)) throw new TypeError('CADP external readout receipt numbers must be finite.');
    const normalized = Object.is(value, -0) ? 0 : value;
    return { json: JSON.stringify(normalized), snapshot: normalized };
  }
  if (typeof value === 'undefined' || typeof value === 'bigint' || typeof value === 'function' || typeof value === 'symbol') {
    throw new TypeError(`CADP external readout receipt contains unsupported type: ${typeof value}.`);
  }
  if (!isSupportedReflectionTarget(value)) {
    throw new TypeError('CADP external readout receipt must not contain a Proxy value.');
  }
  if (active.has(value)) throw new TypeError('CADP external readout receipt must not contain cycles.');
  active.add(value);

  if (Array.isArray(value)) {
    if (Object.getOwnPropertySymbols(value).length > 0) {
      throw new TypeError('CADP external readout receipt arrays must not contain symbol-keyed properties.');
    }
    const keys = Object.getOwnPropertyNames(value);
    const expected = new Set<string>(['length']);
    for (let index = 0; index < value.length; index += 1) expected.add(String(index));
    if (keys.length !== expected.size || keys.some((key) => !expected.has(key))) {
      throw new TypeError('CADP external readout receipt arrays must be dense and contain no extra properties.');
    }
    const jsonParts: string[] = [];
    const snapshotParts: unknown[] = [];
    for (let index = 0; index < value.length; index += 1) {
      const descriptor = Object.getOwnPropertyDescriptor(value, index);
      if (!descriptor || !descriptor.enumerable || 'get' in descriptor || 'set' in descriptor) {
        throw new TypeError(`CADP external readout receipt array index ${index} must be an enumerable data property.`);
      }
      const item = canonicalSnapshot(descriptor.value, active);
      jsonParts.push(item.json);
      snapshotParts.push(item.snapshot);
    }
    active.delete(value);
    return { json: `[${jsonParts.join(',')}]`, snapshot: Object.freeze(snapshotParts) };
  }

  const proto = Object.getPrototypeOf(value);
  if (proto !== Object.prototype && proto !== null) {
    throw new TypeError('CADP external readout receipt objects must be plain JSON objects.');
  }
  if (Object.getOwnPropertySymbols(value).length > 0) {
    throw new TypeError('CADP external readout receipt objects must not contain symbol-keyed properties.');
  }
  const keys = Object.getOwnPropertyNames(value).sort((left, right) => (left < right ? -1 : left > right ? 1 : 0));
  const jsonParts: string[] = [];
  const snapshotEntries: [string, unknown][] = [];
  for (const key of keys) {
    const descriptor = Object.getOwnPropertyDescriptor(value, key);
    if (!descriptor || !descriptor.enumerable || 'get' in descriptor || 'set' in descriptor) {
      throw new TypeError(`CADP external readout receipt key "${key}" must be an enumerable data property.`);
    }
    const item = canonicalSnapshot(descriptor.value, active);
    jsonParts.push(`${JSON.stringify(key)}:${item.json}`);
    snapshotEntries.push([key, item.snapshot]);
  }
  active.delete(value);
  return {
    json: `{${jsonParts.join(',')}}`,
    snapshot: Object.freeze(Object.fromEntries(snapshotEntries)),
  };
}

/**
 * Validates a caller identity input shape only. Never resolves, stores, or
 * compares the identity against any credential, token, or account record.
 */
export function validateCadpExternalCallerIdentityInput(
  value: unknown,
): CadpExternalReadoutValidationResult<{ readonly identity?: CadpExternalCallerIdentityInput }> {
  const issues: CadpExternalReadoutIssue[] = [];
  if (!isPlainRecord(value)) {
    issues.push(issue('MALFORMED_REQUEST', '$.identity', 'Caller identity input must be a plain data object.'));
    return { valid: false, issues, data: {} };
  }
  const names = Object.getOwnPropertyNames(value);
  const expectedKeys = ['callerId', 'requestedScope', 'requestTimestamp'];
  if (Object.getOwnPropertySymbols(value).length > 0 || names.length !== expectedKeys.length || names.some((name) => !expectedKeys.includes(name))) {
    issues.push(issue('UNKNOWN_FIELD', '$.identity', 'Caller identity input has missing or unknown fields.'));
    return { valid: false, issues, data: {} };
  }
  const callerIdField = ownDataField(value, 'callerId');
  const requestTimestampField = ownDataField(value, 'requestTimestamp');
  const requestedScope = readOwnDataStringArray(ownDataField(value, 'requestedScope').value, MAX_INGRESS_SCOPE_ENTRIES);

  const callerIdOk = callerIdField.present
    && typeof callerIdField.value === 'string'
    && /^[A-Za-z0-9][A-Za-z0-9._-]{2,127}$/.test(callerIdField.value);
  if (!callerIdOk) {
    issues.push(issue('INVALID_CALLER_IDENTITY', '$.identity.callerId', 'callerId must be a 3-128 character identifier of letters, digits, dot, underscore, or hyphen.'));
  }
  if (!requestedScope) {
    issues.push(issue('INVALID_CALLER_IDENTITY', '$.identity.requestedScope', 'requestedScope must be an own-property array of at most 16 short strings.'));
  }
  if (!requestTimestampField.present || !isValidIso8601UtcTimestamp(requestTimestampField.value)) {
    issues.push(issue('INVALID_TIMESTAMP', '$.identity.requestTimestamp', 'requestTimestamp must be a strict ISO-8601 UTC timestamp.'));
  }
  if (issues.length > 0) return { valid: false, issues, data: {} };
  return {
    valid: true,
    issues: [],
    data: {
      identity: Object.freeze({
        callerId: callerIdField.value as string,
        requestedScope: requestedScope as readonly string[],
        requestTimestamp: requestTimestampField.value as string,
      }),
    },
  };
}

/**
 * Fail-closed ingress schema and size validator. Rejects unknown fields and
 * oversize input before any allowlist or redaction logic runs, per the
 * Adversarial Test Matrix `unknown fields` and `oversize input` rows.
 */
export function validateCadpExternalReadoutIngress(
  value: unknown,
): CadpExternalReadoutValidationResult<{ readonly request?: CadpExternalReadoutIngressRequest }> {
  const issues: CadpExternalReadoutIssue[] = [];
  if (!isPlainRecord(value)) {
    issues.push(issue('MALFORMED_REQUEST', '$', 'Ingress request must be a plain data object.'));
    return { valid: false, issues, data: {} };
  }
  const names = Object.getOwnPropertyNames(value);
  const expectedKeys = ['identity', 'capabilityId', 'requestedFields'];
  if (Object.getOwnPropertySymbols(value).length > 0 || names.length !== expectedKeys.length || names.some((name) => !expectedKeys.includes(name))) {
    issues.push(issue('UNKNOWN_FIELD', '$', `Ingress request has unknown or missing top-level fields; only ${expectedKeys.join(', ')} are accepted.`));
    return { valid: false, issues, data: {} };
  }
  const identityResult = validateCadpExternalCallerIdentityInput(ownDataField(value, 'identity').value);
  issues.push(...identityResult.issues);

  const capabilityIdField = ownDataField(value, 'capabilityId');
  const capabilityIdOk = capabilityIdField.present
    && typeof capabilityIdField.value === 'string'
    && capabilityIdField.value.trim().length > 0
    && capabilityIdField.value.length <= MAX_INGRESS_STRING_LENGTH;
  if (!capabilityIdOk) {
    issues.push(issue('MALFORMED_REQUEST', '$.capabilityId', 'capabilityId must be a non-empty own-property string within the size bound.'));
  }

  const requestedFieldsRaw = ownDataField(value, 'requestedFields').value;
  const requestedFields = readOwnDataStringArray(requestedFieldsRaw, MAX_INGRESS_REQUESTED_FIELDS);
  if (!requestedFields) {
    issues.push(issue('REQUEST_TOO_LARGE', '$.requestedFields', `requestedFields must be an own-property array of at most ${MAX_INGRESS_REQUESTED_FIELDS} short strings.`));
  } else {
    const unknown = requestedFields.filter((field) => !ALLOWLISTED_METADATA_KEYS.includes(field));
    if (unknown.length > 0) {
      issues.push(issue('UNKNOWN_FIELD', '$.requestedFields', `requestedFields contains field(s) outside the exact allowlist: ${unknown.sort().join(', ')}`));
    }
  }

  if (issues.length > 0 || !identityResult.data.identity) return { valid: false, issues, data: {} };
  return {
    valid: true,
    issues: [],
    data: {
      request: Object.freeze({
        identity: identityResult.data.identity,
        capabilityId: capabilityIdField.value as string,
        requestedFields: requestedFields as readonly string[],
      }),
    },
  };
}

/**
 * Rejects secret and private-provenance field names or path-shaped values
 * from a candidate readout payload before it may be treated as allowlisted.
 * Mirrors the T1 `RAW_SECRET_INCLUDED` / `PRIVATE_PROVENANCE_EXPORT`
 * rejection intent for an external-facing read-only surface.
 */
export function redactCadpExternalReadoutPayload(
  value: unknown,
): CadpExternalReadoutValidationResult<{ readonly redactedFieldNames: readonly string[] }> {
  const issues: CadpExternalReadoutIssue[] = [];
  if (!isPlainRecord(value)) {
    issues.push(issue('MALFORMED_REQUEST', '$', 'Payload to redact must be a plain data object.'));
    return { valid: false, issues, data: { redactedFieldNames: [] } };
  }
  const redacted: string[] = [];
  const names = Object.getOwnPropertyNames(value);
  for (const name of names) {
    if (CADP_EXTERNAL_READOUT_REDACTED_FIELD_NAMES.includes(name)) {
      issues.push(issue('REDACTED_FIELD_PRESENT', `$.${name}`, `Field ${name} is a secret or private-provenance field and must never appear in an external readout payload.`));
      redacted.push(name);
      continue;
    }
    const field = ownDataField(value, name);
    if (field.present && typeof field.value === 'string') {
      const lowered = field.value.replaceAll('\\', '/').toLowerCase();
      if (PRIVATE_PROVENANCE_PATH_MARKERS.some((marker) => lowered.includes(marker))) {
        issues.push(issue('PRIVATE_PROVENANCE_PATH', `$.${name}`, `Field ${name} contains a private-provenance path marker and must never appear in an external readout payload.`));
        redacted.push(name);
      }
    }
  }
  return { valid: issues.length === 0, issues, data: { redactedFieldNames: Object.freeze(redacted) } as { readonly redactedFieldNames: readonly string[] } };
}

/**
 * Validates an already-allowlisted, already-redacted metadata record's
 * literal-`false` authority fields. Does not itself build a live response;
 * it is a shape/authority check only.
 */
export function validateCadpExternalReadoutAllowlistedMetadata(
  value: unknown,
): CadpExternalReadoutValidationResult<{ readonly metadata?: CadpExternalReadoutAllowlistedMetadata }> {
  const issues: CadpExternalReadoutIssue[] = [];
  if (!isPlainRecord(value)) {
    issues.push(issue('MALFORMED_REQUEST', '$', 'Allowlisted metadata must be a plain data object.'));
    return { valid: false, issues, data: {} };
  }
  const names = Object.getOwnPropertyNames(value);
  if (Object.getOwnPropertySymbols(value).length > 0 || names.length !== ALLOWLISTED_METADATA_KEYS.length || names.some((name) => !ALLOWLISTED_METADATA_KEYS.includes(name))) {
    issues.push(issue('UNKNOWN_FIELD', '$', `Allowlisted metadata has unknown or missing fields; only ${ALLOWLISTED_METADATA_KEYS.join(', ')} are accepted.`));
    return { valid: false, issues, data: {} };
  }
  const authorityFields: readonly string[] = [
    'externalReadoutAuthorized',
    'externalMutationAuthorized',
    'externalActivationAuthorized',
    'externalExecutionAuthorized',
    'externalProviderCallAuthorized',
    'externalCredentialResolutionAuthorized',
  ];
  for (const field of authorityFields) {
    const descriptorField = ownDataField(value, field);
    if (!descriptorField.present || descriptorField.value !== false) {
      issues.push(issue('MALFORMED_REQUEST', `$.${field}`, `${field} must be an own-property literal false.`));
    }
  }
  const capabilityIdField = ownDataField(value, 'capabilityId');
  const capabilityVersionField = ownDataField(value, 'capabilityVersion');
  const admissionDecisionField = ownDataField(value, 'admissionDecision');
  const evidenceLevelField = ownDataField(value, 'evidenceLevel');
  const assignedActionIds = readOwnDataStringArray(ownDataField(value, 'assignedActionIds').value, MAX_INGRESS_REQUESTED_FIELDS);
  if (!capabilityIdField.present || typeof capabilityIdField.value !== 'string' || !capabilityIdField.value.trim()) {
    issues.push(issue('MALFORMED_REQUEST', '$.capabilityId', 'capabilityId must be a non-empty own-property string.'));
  }
  if (!capabilityVersionField.present || typeof capabilityVersionField.value !== 'string' || !capabilityVersionField.value.trim()) {
    issues.push(issue('MALFORMED_REQUEST', '$.capabilityVersion', 'capabilityVersion must be a non-empty own-property string.'));
  }
  if (!admissionDecisionField.present || typeof admissionDecisionField.value !== 'string' || !admissionDecisionField.value.trim()) {
    issues.push(issue('MALFORMED_REQUEST', '$.admissionDecision', 'admissionDecision must be a non-empty own-property string.'));
  }
  if (!evidenceLevelField.present || typeof evidenceLevelField.value !== 'string' || !evidenceLevelField.value.trim()) {
    issues.push(issue('MALFORMED_REQUEST', '$.evidenceLevel', 'evidenceLevel must be a non-empty own-property string.'));
  }
  if (!assignedActionIds) {
    issues.push(issue('MALFORMED_REQUEST', '$.assignedActionIds', 'assignedActionIds must be an own-property array of strings.'));
  }
  if (issues.length > 0) return { valid: false, issues, data: {} };
  return {
    valid: true,
    issues: [],
    data: {
      metadata: Object.freeze({
        capabilityId: capabilityIdField.value as string,
        capabilityVersion: capabilityVersionField.value as string,
        admissionDecision: admissionDecisionField.value as string,
        assignedActionIds: assignedActionIds as readonly string[],
        evidenceLevel: evidenceLevelField.value as string,
        externalReadoutAuthorized: false,
        externalMutationAuthorized: false,
        externalActivationAuthorized: false,
        externalExecutionAuthorized: false,
        externalProviderCallAuthorized: false,
        externalCredentialResolutionAuthorized: false,
      }),
    },
  };
}

/**
 * Replay/freshness contract for a stateless external readout call. Compares
 * three explicit timestamps supplied by the caller of this function; it
 * never reads a clock itself, so the result is fully deterministic for a
 * given input triple.
 */
export function evaluateCadpExternalReadoutFreshness(
  input: CadpExternalReadoutFreshnessInput,
): CadpExternalReadoutFreshnessResult {
  const issues: CadpExternalReadoutIssue[] = [];
  if (!isPlainRecord(input)) {
    return { disposition: 'INVALID', issues: [issue('MALFORMED_REQUEST', '$', 'Freshness input must be a plain data object.')] };
  }
  const issuedAtField = ownDataField(input, 'issuedAt');
  const expiresAtField = ownDataField(input, 'expiresAt');
  const observedAtField = ownDataField(input, 'observedAt');
  if (!isValidIso8601UtcTimestamp(issuedAtField.value)) {
    issues.push(issue('INVALID_TIMESTAMP', '$.issuedAt', 'issuedAt must be a strict ISO-8601 UTC timestamp.'));
  }
  if (!isValidIso8601UtcTimestamp(expiresAtField.value)) {
    issues.push(issue('INVALID_TIMESTAMP', '$.expiresAt', 'expiresAt must be a strict ISO-8601 UTC timestamp.'));
  }
  if (!isValidIso8601UtcTimestamp(observedAtField.value)) {
    issues.push(issue('INVALID_TIMESTAMP', '$.observedAt', 'observedAt must be a strict ISO-8601 UTC timestamp.'));
  }
  if (issues.length > 0) return { disposition: 'INVALID', issues };

  const issuedAtMs = Date.parse(issuedAtField.value as string);
  const expiresAtMs = Date.parse(expiresAtField.value as string);
  const observedAtMs = Date.parse(observedAtField.value as string);
  if (!Number.isFinite(issuedAtMs) || !Number.isFinite(expiresAtMs) || !Number.isFinite(observedAtMs)) {
    return { disposition: 'INVALID', issues: [issue('INVALID_TIMESTAMP', '$', 'One or more timestamps could not be parsed as a real calendar instant.')] };
  }
  if (expiresAtMs <= issuedAtMs) {
    return { disposition: 'INVALID', issues: [issue('INVALID_TIMESTAMP', '$.expiresAt', 'expiresAt must be strictly after issuedAt.')] };
  }
  if (observedAtMs > expiresAtMs) {
    return { disposition: 'EXPIRED', issues: [issue('REPLAY_WINDOW_EXCEEDED', '$.observedAt', 'Request observed after its declared expiry; treat as expired.')] };
  }
  if (observedAtMs < issuedAtMs - REPLAY_WINDOW_MILLISECONDS) {
    return { disposition: 'INVALID', issues: [issue('REPLAY_WINDOW_EXCEEDED', '$.observedAt', 'Request observed materially before it was issued; treat as invalid.')] };
  }
  if (observedAtMs - issuedAtMs > STALE_REQUEST_MILLISECONDS) {
    return { disposition: 'STALE', issues: [issue('STALE_REQUEST', '$.observedAt', 'Request observed materially later than its issued time; treat as stale.')] };
  }
  return { disposition: 'FRESH', issues: [] };
}

/**
 * Deterministic external error/receipt contract. Extends the T1
 * `createDeterministicCadpReceipt` explicit-time pattern: no ambient clock,
 * no ambient UUID, and identical input always produces an identical
 * `integrityHash`.
 */
export function createDeterministicCadpExternalReadoutReceipt<TPayload>(
  input: CadpExternalReadoutReceiptInput<TPayload>,
): CadpExternalReadoutReceipt<TPayload> {
  if (!isPlainRecord(input as unknown)) {
    throw new TypeError('CADP external readout receipt input must be a plain data object.');
  }
  const requestIdField = ownDataField(input, 'requestId');
  const issuedAtField = ownDataField(input, 'issuedAt');
  const payloadField = ownDataField(input, 'payload');
  if (
    typeof requestIdField.value !== 'string' || !requestIdField.value.trim() ||
    !isValidIso8601UtcTimestamp(issuedAtField.value) ||
    !payloadField.present
  ) {
    throw new TypeError('CADP external readout receipt requires a non-empty own-property requestId, a strict ISO-8601 UTC issuedAt string, and an own-property payload.');
  }
  // Apply the hardened T1 canonical-snapshot pattern locally so this
  // copyable foundation does not import T1's repository-owner module graph.
  const canonical = canonicalSnapshot({
    requestId: requestIdField.value,
    issuedAt: issuedAtField.value as string,
    payload: payloadField.value as TPayload,
  }, new WeakSet<object>());
  const canonicalIdentity = canonical.snapshot as {
    readonly requestId: string;
    readonly issuedAt: string;
    readonly payload: TPayload;
  };
  const integrityHash = createHash('sha256').update(canonical.json, 'utf8').digest('hex');
  return Object.freeze({
    contractVersion: CADP_EXTERNAL_READOUT_FOUNDATION_CONTRACT_VERSION,
    receiptId: `cadp-external-readout-${integrityHash}`,
    requestId: canonicalIdentity.requestId,
    issuedAt: canonicalIdentity.issuedAt,
    payload: canonicalIdentity.payload,
    integrityHash,
    receiptGrantsExecution: false,
    receiptGrantsMutation: false,
    receiptGrantsActivation: false,
  });
}
