/**
 * CVF-native capability admission/distribution profile.
 *
 * Adapted from the bounded CADP-R1 external-absorption evidence. The external
 * Python package remains reference evidence only; this file owns the CVF
 * contract and fail-closed, side-effect-free validation behavior.
 */

import { createHash } from 'node:crypto';
import { isProxy } from 'node:util/types';
import {
  isBoundCapabilityOwner,
  readBoundArtifact,
  readBoundGrantIdentity,
  type BoundArtifactType,
  type CapabilityOwnerHandle,
} from './capability-owner-binding.contract';

/**
 * T2A replaces caller-supplied evidence indexes with an opaque owner handle.
 * The only production binder accepts a normalized repository grant path and
 * independently reads the grant plus its pinned artifacts from committed
 * `HEAD`; no caller-authored grant object or artifact map is accepted.
 */

export const CADP_CONTRACT_VERSION = 'cvf.cadp.v1' as const;

export type CadpIssueCode =
  | 'AUTHORITY_MINT'
  | 'RAW_SECRET_INCLUDED'
  | 'SOURCE_UNVERIFIED'
  | 'INVALID_FIELD'
  | 'ADMISSION_NOT_ASSIGNABLE'
  | 'EVIDENCE_LEVEL_INVALID'
  | 'INSTALL_MODE_INVALID'
  | 'DIGEST_INVALID'
  | 'DUPLICATE_VALUE'
  | 'REFERENCE_MISMATCH'
  | 'ACTION_OUTSIDE_ADMISSION'
  | 'ACTION_SCOPE_CONFLICT'
  | 'EVIDENCE_MISSING'
  | 'EVIDENCE_UNTRUSTED'
  | 'EVIDENCE_OWNER_MISMATCH'
  | 'EVIDENCE_SOURCE_NOT_FOUND'
  | 'PRIVATE_PROVENANCE_EXPORT'
  | 'MALFORMED_INPUT_SHAPE';

export interface CadpIssue {
  readonly code: CadpIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface CadpValidationResult<TData = Readonly<Record<string, unknown>>> {
  readonly valid: boolean;
  readonly issues: readonly CadpIssue[];
  readonly data: TData;
}

export type CapabilityAdmissionDecision = 'ADMIT' | 'ADMIT_READ_ONLY' | 'HOLD' | 'BLOCK';

export type CapabilityMutationType = 'read' | 'create' | 'update' | 'delete' | 'system_config';

export interface CapabilityAdmissionAction {
  readonly actionId: string;
  readonly mutationType: CapabilityMutationType;
}

export interface CapabilityAdmissionRecord {
  readonly admissionId: string;
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly decision: CapabilityAdmissionDecision;
  readonly sourceVerified: boolean;
  readonly admittedActions: readonly CapabilityAdmissionAction[];
  readonly executionAuthorized: false;
  readonly rawSecretsAllowed: false;
  readonly duplicateCanonicalOwnerRequired: false;
}

export interface CapabilityAssignmentRecord {
  readonly assignmentId: string;
  readonly admissionId: string;
  readonly capabilityId: string;
  readonly capabilityVersion: string;
  readonly assignedActionIds: readonly string[];
  readonly excludedActionIds: readonly string[];
  readonly workOrderRequired: true;
  readonly executionAuthorized: false;
  readonly rawSecretsIncluded: false;
}

export interface CapabilityDistributionItem {
  readonly path: string;
  readonly sha256: string;
  readonly containsSecret: false;
}

export interface CapabilityDistributionManifest {
  readonly distributionId: string;
  readonly capabilityId: string;
  readonly installMode: 'LOCAL_PRIVATE' | 'INTERNAL_SHARED' | 'PUBLIC_EXPORT';
  readonly contents: readonly CapabilityDistributionItem[];
  readonly distributionGrantsAssignment: false;
  readonly distributionGrantsActivation: false;
  readonly distributionGrantsExecution: false;
  readonly rawSecretsIncluded: false;
}

export type CompatibilityEvidenceLevel =
  | 'DECLARED'
  | 'STATIC_VERIFIED'
  | 'RECEIPT_BACKED'
  | 'ACTION_TESTED'
  | 'REVIEWED'
  | 'CERTIFIED_BOUNDED';

/**
 * `CompatibilityArtifactType` re-exports the owner-binding module's closed
 * artifact-class union so this file's public API keeps a stable name for
 * consumers, while the actual trust decision for any given `ref` is made
 * exclusively by `capability-owner-binding.contract.ts`'s
 * `readBoundArtifact`, never by a caller-suppliable index (see F11 below).
 */
export type CompatibilityArtifactType = BoundArtifactType;

/**
 * High-rank evidence is accepted only when every required reference resolves
 * through a repository-verified opaque handle and the committed grant's
 * capability identity matches this record. Independent review, rather than
 * this implementation comment, owns the final F11 closure disposition.
 */
export interface CompatibilityEvidenceRecord {
  readonly capabilityId: string;
  readonly evidenceLevel: CompatibilityEvidenceLevel;
  readonly receiptRefs: readonly string[];
  readonly workOrderRef?: string;
  readonly reviewRef?: string;
  readonly freezeRef?: string;
  readonly passingActionIds: readonly string[];
  readonly expectedEvidenceOwner: string;
  readonly rawSecretsRecorded: false;
}

const EVIDENCE_LEVELS: readonly CompatibilityEvidenceLevel[] = [
  'DECLARED',
  'STATIC_VERIFIED',
  'RECEIPT_BACKED',
  'ACTION_TESTED',
  'REVIEWED',
  'CERTIFIED_BOUNDED',
];

const ADMISSION_DECISIONS: readonly CapabilityAdmissionDecision[] = ['ADMIT', 'ADMIT_READ_ONLY', 'HOLD', 'BLOCK'];
const INSTALL_MODES: readonly CapabilityDistributionManifest['installMode'][] = ['LOCAL_PRIVATE', 'INTERNAL_SHARED', 'PUBLIC_EXPORT'];
const MUTATION_TYPES: readonly CapabilityMutationType[] = ['read', 'create', 'update', 'delete', 'system_config'];
const MUTATING_TYPES: readonly CapabilityMutationType[] = ['create', 'update', 'delete', 'system_config'];
const SHA256_PATTERN = /^[0-9a-f]{64}$/i;
const ISO8601_UTC_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,9})?Z$/;

function issue(code: CadpIssueCode, path: string, message: string): CadpIssue {
  return { code, path, message };
}

/**
 * The single Proxy-rejection primitive for this file. Proxy is defined as
 * unsupported everywhere this contract performs reflection/introspection
 * (`Object.getOwnPropertyDescriptor`, `Object.getPrototypeOf`,
 * `Object.getOwnPropertyNames`, `Object.getOwnPropertySymbols`, `in`,
 * `Array.isArray`, or any property/index read) because every one of those
 * operations dispatches through a Proxy's traps (`get`,
 * `getOwnPropertyDescriptor`, `getPrototypeOf`, `ownKeys`, etc.) as
 * caller-controlled code, even though the Proxy's target may itself be a
 * plain object that would otherwise pass every shape check.
 * `node:util/types`' `isProxy` is a trap-free predicate: it inspects an
 * internal V8 slot rather than performing any of the reflective operations
 * above, so calling it never invokes a trap - even on a *revoked* Proxy,
 * whose traps (and even `Array.isArray` on a revoked array Proxy, which
 * throws a raw `TypeError` rather than returning a boolean) would otherwise
 * throw. `isSupportedReflectionTarget` must be the first check at every
 * reflection entry point in this file, before any descriptor/prototype/key
 * read and before any `Array.isArray` call on an untrusted value.
 */
function isSupportedReflectionTarget(value: unknown): boolean {
  if (value === null || (typeof value !== 'object' && typeof value !== 'function')) return true;
  return !isProxy(value);
}

/**
 * Produces a safe, non-executing label for an untrusted value used inside an
 * issue message. Never calls a caller-controlled `toString`, `valueOf`, or
 * `Symbol.toPrimitive` hook: primitives are rendered with a fixed,
 * hook-free mapping (so `String(value)` is never invoked on caller data),
 * and every object/array/function/symbol is reduced to a safe category tag
 * before any text is produced, never to its own coerced text. A Proxy is
 * labeled `<proxy>` via the trap-free `isSupportedReflectionTarget` check
 * before `Array.isArray` runs, because `Array.isArray` throws a raw
 * `TypeError` (not a boolean) on a *revoked* array Proxy - so this
 * function's own Proxy handling must come first, or a revoked-Proxy value
 * passed as e.g. an invalid `mutationType` would crash issue-message
 * construction instead of degrading to a label.
 */
function safeTypeLabel(value: unknown): string {
  if (value === undefined) return 'undefined';
  if (value === null) return 'null';
  if (typeof value === 'string') return JSON.stringify(value);
  if (typeof value === 'boolean') return value ? 'true' : 'false';
  if (typeof value === 'number') return Object.is(value, -0) ? '-0' : `${value}`;
  if (typeof value === 'bigint') return '<bigint>';
  if (typeof value === 'symbol') return '<symbol>';
  if (!isSupportedReflectionTarget(value)) return '<proxy>';
  if (typeof value === 'function') return '<function>';
  if (Array.isArray(value)) return '<array>';
  return '<object>';
}

/**
 * Reads an own, enumerable, non-accessor data property. Returns
 * `{ present: false }` for anything else (missing, inherited-only, symbol,
 * non-enumerable, accessor, or a Proxy owner), so callers cannot be fed a
 * value that never existed as real own data on the record, and a Proxy
 * owner is rejected before `Object.getOwnPropertyDescriptor` would dispatch
 * through its `getOwnPropertyDescriptor` trap.
 */
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

function isPlainRecord(value: unknown): value is Record<string, unknown> {
  if (value === null || typeof value !== 'object') return false;
  if (!isSupportedReflectionTarget(value)) return false;
  const proto = Object.getPrototypeOf(value);
  return proto === Object.prototype || proto === null;
}

/**
 * The single caller-array reading mechanism for this file. Walks a caller-owned
 * array using only `Array.isArray`, `Object.getOwnPropertyNames`,
 * `Object.getOwnPropertySymbols`, and `Object.getOwnPropertyDescriptor` -
 * never `map`, `every`, `forEach`, `some`, `find`, spread, `for...of`, or
 * direct index access (`value[i]`), all of which read through a possible
 * index accessor and can invoke caller-defined code before shape validation
 * completes. Rejects: non-arrays; symbol-keyed properties; sparse indices;
 * any extra own property beyond dense numeric indices and `length`; any
 * index that is not an own enumerable data descriptor (so an index getter is
 * rejected by descriptor inspection alone, without ever reading `.value`
 * through the accessor); and any element whose runtime type does not match
 * `elementGuard`. On success, returns a new internal array built only from
 * validated descriptor values, so all later processing reads the internal
 * copy, never the caller's original array.
 */
function readOwnDataArray<T>(
  value: unknown,
  elementGuard: (item: unknown) => item is T,
): readonly T[] | undefined {
  // isSupportedReflectionTarget must run before Array.isArray: on a
  // *revoked* array Proxy, Array.isArray itself throws a raw
  // "Cannot perform 'IsArray' on a proxy that has been revoked" TypeError
  // instead of returning a boolean, because it must consult the (now-dead)
  // target through the revoked proxy's internal slot. isProxy (used by
  // isSupportedReflectionTarget) never touches the target, so it safely
  // rejects a revoked Proxy before Array.isArray ever runs on it.
  if (!isSupportedReflectionTarget(value)) return undefined;
  if (!Array.isArray(value)) return undefined;
  if (Object.getOwnPropertySymbols(value).length > 0) return undefined;
  const ownKeys = Object.getOwnPropertyNames(value);
  const expectedKeyCount = value.length + 1;
  if (ownKeys.length !== expectedKeyCount) return undefined;
  const expectedKeys = new Set<string>(['length']);
  for (let index = 0; index < value.length; index += 1) expectedKeys.add(String(index));
  for (const key of ownKeys) {
    if (!expectedKeys.has(key)) return undefined;
  }
  const result: T[] = [];
  for (let index = 0; index < value.length; index += 1) {
    const descriptor = Object.getOwnPropertyDescriptor(value, index);
    if (!descriptor || !descriptor.enumerable || 'get' in descriptor || 'set' in descriptor) {
      return undefined;
    }
    const item = descriptor.value;
    if (!elementGuard(item)) return undefined;
    result.push(item);
  }
  return result;
}

function isPlainArrayOfRecords(value: unknown): value is readonly Record<string, unknown>[] {
  return readOwnDataArray(value, isPlainRecord) !== undefined;
}

function isPlainStringArray(value: unknown): value is readonly string[] {
  return readOwnDataArray(value, (item): item is string => typeof item === 'string') !== undefined;
}

function requireText(owner: unknown, key: string, path: string, issues: CadpIssue[]): void {
  const field = ownDataField(owner, key);
  if (!field.present || typeof field.value !== 'string' || !field.value.trim()) {
    issues.push(issue('INVALID_FIELD', path, `${path} must be a non-empty own-property string.`));
  }
}

function requireExactFalse(owner: unknown, key: string, path: string, issues: CadpIssue[], code: CadpIssueCode, message: string): void {
  const field = ownDataField(owner, key);
  if (!field.present || field.value !== false) {
    issues.push(issue(code, path, message));
  }
}

function requireExactTrue(owner: unknown, key: string, path: string, issues: CadpIssue[], message: string): void {
  const field = ownDataField(owner, key);
  if (!field.present || field.value !== true) {
    issues.push(issue('MALFORMED_INPUT_SHAPE', path, message));
  }
}

function requireBoolean(owner: unknown, key: string, path: string, issues: CadpIssue[]): boolean | undefined {
  const field = ownDataField(owner, key);
  if (!field.present || typeof field.value !== 'boolean') {
    issues.push(issue('MALFORMED_INPUT_SHAPE', path, `${path} must be an own-property boolean.`));
    return undefined;
  }
  return field.value;
}

function requireStringArray(owner: unknown, key: string, path: string, issues: CadpIssue[]): readonly string[] {
  const field = ownDataField(owner, key);
  const internal = field.present
    ? readOwnDataArray(field.value, (item): item is string => typeof item === 'string')
    : undefined;
  if (!internal) {
    issues.push(issue('MALFORMED_INPUT_SHAPE', path, `${path} must be an own-property array of strings.`));
    return [];
  }
  return internal;
}

function requireRecordArray(owner: unknown, key: string, path: string, issues: CadpIssue[]): readonly Record<string, unknown>[] {
  const field = ownDataField(owner, key);
  const internal = field.present ? readOwnDataArray(field.value, isPlainRecord) : undefined;
  if (!internal) {
    issues.push(issue('MALFORMED_INPUT_SHAPE', path, `${path} must be an own-property array of plain records.`));
    return [];
  }
  return internal;
}

function uniqueSorted(values: readonly string[]): readonly string[] {
  return [...new Set(values)].sort();
}

/**
 * Builds a validated internal admission-identity projection from own-data
 * descriptors only. Used by `validateCapabilityAssignment` so the assignment
 * identity check never dereferences `admission.admissionId` /
 * `admission.capabilityId` / `admission.capabilityVersion` through direct
 * property access on the caller-owned admission record. Returns `undefined`
 * (no further dereference) if any of the three fields is not an own,
 * enumerable, non-accessor string.
 */
function readAdmissionIdentity(
  admission: unknown,
): { readonly admissionId: string; readonly capabilityId: string; readonly capabilityVersion: string } | undefined {
  const admissionIdField = ownDataField(admission, 'admissionId');
  const capabilityIdField = ownDataField(admission, 'capabilityId');
  const capabilityVersionField = ownDataField(admission, 'capabilityVersion');
  if (
    typeof admissionIdField.value !== 'string' ||
    typeof capabilityIdField.value !== 'string' ||
    typeof capabilityVersionField.value !== 'string'
  ) {
    return undefined;
  }
  return {
    admissionId: admissionIdField.value,
    capabilityId: capabilityIdField.value,
    capabilityVersion: capabilityVersionField.value,
  };
}

function readAdmissionDecision(record: unknown, issues: CadpIssue[]): CapabilityAdmissionDecision | undefined {
  const field = ownDataField(record, 'decision');
  if (!field.present || typeof field.value !== 'string' || !ADMISSION_DECISIONS.includes(field.value as CapabilityAdmissionDecision)) {
    issues.push(issue('INVALID_FIELD', '$.decision', `Unknown admission decision: ${safeTypeLabel(field.value)}`));
    return undefined;
  }
  return field.value as CapabilityAdmissionDecision;
}

function readAdmittedActions(
  record: unknown,
  issues: CadpIssue[],
): readonly { readonly actionId: string; readonly mutationType: CapabilityMutationType }[] {
  const rawActions = requireRecordArray(record, 'admittedActions', '$.admittedActions', issues);
  const validated: { readonly actionId: string; readonly mutationType: CapabilityMutationType }[] = [];
  rawActions.forEach((action, index) => {
    const actionIdField = ownDataField(action, 'actionId');
    const mutationField = ownDataField(action, 'mutationType');
    const actionIdOk = actionIdField.present && typeof actionIdField.value === 'string' && actionIdField.value.trim().length > 0;
    const mutationOk = mutationField.present && typeof mutationField.value === 'string' &&
      MUTATION_TYPES.includes(mutationField.value as CapabilityMutationType);
    if (!actionIdOk) {
      issues.push(issue('INVALID_FIELD', `$.admittedActions[${index}].actionId`, 'Admission action IDs must be a non-empty own-property string.'));
    }
    if (!mutationOk) {
      issues.push(issue('INVALID_FIELD', `$.admittedActions[${index}].mutationType`, `Unknown or missing own-property mutation type: ${safeTypeLabel(mutationField.value)}`));
    }
    if (actionIdOk && mutationOk) {
      validated.push({ actionId: actionIdField.value as string, mutationType: mutationField.value as CapabilityMutationType });
    }
  });
  const duplicateAction = validated.find((action, index, actions) =>
    actions.findIndex((candidate) => candidate.actionId === action.actionId) !== index);
  if (duplicateAction) {
    issues.push(issue('DUPLICATE_VALUE', '$.admittedActions', `Duplicate admission action: ${duplicateAction.actionId}`));
  }
  return validated;
}

export function validateCapabilityAdmission(
  record: CapabilityAdmissionRecord,
): CadpValidationResult<{ readonly assignableActionIds: readonly string[] }> {
  const issues: CadpIssue[] = [];
  requireText(record, 'admissionId', '$.admissionId', issues);
  requireText(record, 'capabilityId', '$.capabilityId', issues);
  requireText(record, 'capabilityVersion', '$.capabilityVersion', issues);
  const decision = readAdmissionDecision(record, issues);
  requireExactFalse(record, 'executionAuthorized', '$.executionAuthorized', issues, 'AUTHORITY_MINT', 'Admission cannot grant authority.');
  requireExactFalse(record, 'duplicateCanonicalOwnerRequired', '$.duplicateCanonicalOwnerRequired', issues, 'AUTHORITY_MINT', 'Admission cannot create a duplicate canonical owner.');
  requireExactFalse(record, 'rawSecretsAllowed', '$.rawSecretsAllowed', issues, 'RAW_SECRET_INCLUDED', 'Admission records must never contain raw secrets.');
  const sourceVerified = requireBoolean(record, 'sourceVerified', '$.sourceVerified', issues);
  if (decision !== undefined) {
    if ((decision === 'ADMIT' || decision === 'ADMIT_READ_ONLY') && sourceVerified !== true) {
      issues.push(issue('SOURCE_UNVERIFIED', '$.sourceVerified', 'An unverified source must remain HOLD or BLOCK.'));
    }
    const assignableDecision = decision === 'ADMIT' || decision === 'ADMIT_READ_ONLY';
    if (!assignableDecision) {
      issues.push(issue('ADMISSION_NOT_ASSIGNABLE', '$.decision', `Admission decision ${decision} cannot be assigned.`));
    }
  }
  const admittedActions = readAdmittedActions(record, issues);
  const assignableActions = decision === undefined
    ? []
    : admittedActions.filter((action) => decision !== 'ADMIT_READ_ONLY' || !MUTATING_TYPES.includes(action.mutationType));
  return {
    valid: issues.length === 0,
    issues,
    data: { assignableActionIds: issues.length === 0 ? uniqueSorted(assignableActions.map(({ actionId }) => actionId)) : [] },
  };
}

export function validateCapabilityAssignment(
  admission: CapabilityAdmissionRecord,
  assignment: CapabilityAssignmentRecord,
): CadpValidationResult<{ readonly assignedActionIds: readonly string[]; readonly executionAuthorized: false }> {
  const issues: CadpIssue[] = [];
  requireText(assignment, 'assignmentId', '$.assignmentId', issues);
  requireText(assignment, 'admissionId', '$.admissionId', issues);
  requireText(assignment, 'capabilityId', '$.capabilityId', issues);
  requireText(assignment, 'capabilityVersion', '$.capabilityVersion', issues);
  const admissionResult = validateCapabilityAdmission(admission);
  issues.push(...admissionResult.issues);
  requireExactFalse(assignment, 'executionAuthorized', '$.executionAuthorized', issues, 'AUTHORITY_MINT', 'Assignment cannot grant execution.');
  requireExactTrue(assignment, 'workOrderRequired', '$.workOrderRequired', issues, 'Assignment must require a work order.');
  requireExactFalse(assignment, 'rawSecretsIncluded', '$.rawSecretsIncluded', issues, 'RAW_SECRET_INCLUDED', 'Assignment may contain credential references only.');
  const admissionIdField = ownDataField(assignment, 'admissionId');
  const capabilityIdField = ownDataField(assignment, 'capabilityId');
  const capabilityVersionField = ownDataField(assignment, 'capabilityVersion');
  const admissionIdentity = admissionResult.valid ? readAdmissionIdentity(admission) : undefined;
  if (
    !admissionIdentity ||
    admissionIdField.value !== admissionIdentity.admissionId ||
    capabilityIdField.value !== admissionIdentity.capabilityId ||
    capabilityVersionField.value !== admissionIdentity.capabilityVersion
  ) {
    issues.push(issue('REFERENCE_MISMATCH', '$.admissionId', 'Assignment must bind the exact admitted identity and version.'));
  }
  const excludedActionIds = requireStringArray(assignment, 'excludedActionIds', '$.excludedActionIds', issues);
  const assignedActionIdsRaw = requireStringArray(assignment, 'assignedActionIds', '$.assignedActionIds', issues);
  const excluded = new Set(excludedActionIds);
  const assignedActionIds = uniqueSorted(assignedActionIdsRaw);
  const overlap = assignedActionIds.filter((actionId) => excluded.has(actionId));
  if (overlap.length > 0) {
    issues.push(issue('ACTION_SCOPE_CONFLICT', '$.assignedActionIds', `Assigned and excluded actions overlap: ${overlap.sort().join(', ')}`));
  }
  const admitted = new Set(admissionResult.data.assignableActionIds);
  const outside = assignedActionIds.filter((actionId) => !admitted.has(actionId));
  if (outside.length > 0) {
    issues.push(issue('ACTION_OUTSIDE_ADMISSION', '$.assignedActionIds', `Actions outside admission: ${outside.sort().join(', ')}`));
  }
  return {
    valid: issues.length === 0,
    issues,
    data: { assignedActionIds, executionAuthorized: false },
  };
}

function readDistributionContents(
  manifest: unknown,
  issues: CadpIssue[],
): readonly { readonly path: string; readonly sha256: string }[] {
  const rawContents = requireRecordArray(manifest, 'contents', '$.contents', issues);
  const validated: { readonly path: string; readonly sha256: string }[] = [];
  const seenPaths = new Set<string>();
  rawContents.forEach((item, index) => {
    const pathField = ownDataField(item, 'path');
    const sha256Field = ownDataField(item, 'sha256');
    const pathOk = pathField.present && typeof pathField.value === 'string' && pathField.value.trim().length > 0;
    if (!pathOk) {
      issues.push(issue('INVALID_FIELD', `$.contents[${index}].path`, `$.contents[${index}].path must be a non-empty own-property string.`));
    }
    requireExactFalse(item, 'containsSecret', `$.contents[${index}].containsSecret`, issues, 'RAW_SECRET_INCLUDED', `$.contents[${index}].containsSecret must be an own-property false.`);
    if (pathOk) {
      const normalizedPath = (pathField.value as string).replaceAll('\\', '/');
      if (seenPaths.has(normalizedPath)) {
        issues.push(issue('DUPLICATE_VALUE', `$.contents[${index}].path`, `Duplicate distribution path: ${normalizedPath}`));
      }
      seenPaths.add(normalizedPath);
    }
    const sha256Ok = sha256Field.present && typeof sha256Field.value === 'string' && SHA256_PATTERN.test(sha256Field.value);
    if (!sha256Ok) {
      issues.push(issue('DIGEST_INVALID', `$.contents[${index}].sha256`, `Invalid own-property SHA-256 for content item ${index}.`));
    }
    if (pathOk && sha256Ok) {
      validated.push({ path: pathField.value as string, sha256: sha256Field.value as string });
    }
  });
  return validated;
}

export function validateCapabilityDistribution(
  manifest: CapabilityDistributionManifest,
): CadpValidationResult<{ readonly activationGranted: false; readonly executionAuthorized: false }> {
  const issues: CadpIssue[] = [];
  requireText(manifest, 'distributionId', '$.distributionId', issues);
  requireText(manifest, 'capabilityId', '$.capabilityId', issues);
  const installModeField = ownDataField(manifest, 'installMode');
  const installModeKnown = installModeField.present && typeof installModeField.value === 'string' &&
    INSTALL_MODES.includes(installModeField.value as CapabilityDistributionManifest['installMode']);
  if (!installModeKnown) {
    issues.push(issue('INSTALL_MODE_INVALID', '$.installMode', `Unknown install mode: ${safeTypeLabel(installModeField.value)}`));
  }
  requireExactFalse(manifest, 'distributionGrantsAssignment', '$.distributionGrantsAssignment', issues, 'AUTHORITY_MINT', 'Distribution is transport metadata and cannot grant authority.');
  requireExactFalse(manifest, 'distributionGrantsActivation', '$.distributionGrantsActivation', issues, 'AUTHORITY_MINT', 'Distribution is transport metadata and cannot grant authority.');
  requireExactFalse(manifest, 'distributionGrantsExecution', '$.distributionGrantsExecution', issues, 'AUTHORITY_MINT', 'Distribution is transport metadata and cannot grant authority.');
  requireExactFalse(manifest, 'rawSecretsIncluded', '$.rawSecretsIncluded', issues, 'RAW_SECRET_INCLUDED', 'Distribution content must exclude raw secrets.');
  const validatedContents = readDistributionContents(manifest, issues);
  if (installModeField.value === 'PUBLIC_EXPORT' || !installModeKnown) {
    const privateItem = validatedContents.find((item) => {
      const path = item.path.replaceAll('\\', '/').toLowerCase();
      return path.includes('cvf_session/') || path.includes('/private/') || path.includes('provenance');
    });
    if (privateItem) {
      issues.push(issue('PRIVATE_PROVENANCE_EXPORT', '$.contents', `Public export includes private material: ${privateItem.path}`));
    }
  }
  return { valid: issues.length === 0, issues, data: { activationGranted: false, executionAuthorized: false } };
}

export function validateCompatibilityEvidence(
  record: CompatibilityEvidenceRecord,
  ownerHandle: CapabilityOwnerHandle,
): CadpValidationResult<{ readonly evidenceRank: number }> {
  const issues: CadpIssue[] = [];
  requireText(record, 'capabilityId', '$.capabilityId', issues);
  requireText(record, 'expectedEvidenceOwner', '$.expectedEvidenceOwner', issues);
  requireExactFalse(record, 'rawSecretsRecorded', '$.rawSecretsRecorded', issues, 'RAW_SECRET_INCLUDED', 'Compatibility evidence must never record raw secrets.');
  const evidenceLevelField = ownDataField(record, 'evidenceLevel');
  const rank = evidenceLevelField.present && typeof evidenceLevelField.value === 'string'
    ? EVIDENCE_LEVELS.indexOf(evidenceLevelField.value as CompatibilityEvidenceLevel)
    : -1;
  if (rank < 0) {
    issues.push(issue('EVIDENCE_LEVEL_INVALID', '$.evidenceLevel', `Unknown evidence level: ${safeTypeLabel(evidenceLevelField.value)}`));
  }
  const receiptRefsRaw = requireStringArray(record, 'receiptRefs', '$.receiptRefs', issues);
  const passingActionIdsRaw = requireStringArray(record, 'passingActionIds', '$.passingActionIds', issues);
  const receiptRefs = uniqueSorted(receiptRefsRaw);
  const passingActionIds = uniqueSorted(passingActionIdsRaw);
  if (receiptRefs.some((ref) => !ref.trim())) {
    issues.push(issue('INVALID_FIELD', '$.receiptRefs', 'Receipt references must be non-empty.'));
  }
  if (passingActionIds.some((actionId) => !actionId.trim())) {
    issues.push(issue('INVALID_FIELD', '$.passingActionIds', 'Passing action IDs must be non-empty.'));
  }
  const expectedOwnerField = ownDataField(record, 'expectedEvidenceOwner');
  const expectedEvidenceOwner = typeof expectedOwnerField.value === 'string' ? expectedOwnerField.value : undefined;
  const workOrderRefField = ownDataField(record, 'workOrderRef');
  const reviewRefField = ownDataField(record, 'reviewRef');
  const freezeRefField = ownDataField(record, 'freezeRef');
  const workOrderRef = typeof workOrderRefField.value === 'string' ? workOrderRefField.value : undefined;
  const reviewRef = typeof reviewRefField.value === 'string' ? reviewRefField.value : undefined;
  const freezeRef = typeof freezeRefField.value === 'string' ? freezeRefField.value : undefined;
  const required: Array<readonly [string | undefined, CompatibilityArtifactType]> = [];
  if (rank >= 2) required.push(...receiptRefs.map((ref) => [ref, 'receipt'] as const));
  if (rank >= 2 && receiptRefs.length === 0) issues.push(issue('EVIDENCE_MISSING', '$.receiptRefs', 'Receipt-backed evidence requires at least one receipt.'));
  if (rank >= 3 && passingActionIds.length === 0) issues.push(issue('EVIDENCE_MISSING', '$.passingActionIds', 'Action-tested evidence requires a passing action.'));
  if (rank >= 4) required.push([workOrderRef, 'work_order'], [reviewRef, 'review']);
  if (rank >= 5) required.push([freezeRef, 'freeze']);
  const ownerIsBound = isBoundCapabilityOwner(ownerHandle);
  if (required.length > 0 && !ownerIsBound) {
    issues.push(issue('EVIDENCE_SOURCE_NOT_FOUND', '$.evidence', 'No repository-verified capability owner handle was supplied.'));
  }
  if (required.length > 0 && ownerIsBound) {
    const identity = readBoundGrantIdentity(ownerHandle);
    if (!identity || identity.capabilityId !== record.capabilityId) {
      issues.push(issue('SOURCE_UNVERIFIED', '$.capabilityId', 'Evidence capability does not match the committed owner grant.'));
    }
  }
  for (const [ref, artifactType] of required) {
    if (!ref) {
      issues.push(issue('EVIDENCE_MISSING', '$.evidence', `${artifactType} evidence is required.`));
      continue;
    }
    if (!ownerIsBound) continue;
    const artifact = readBoundArtifact(ownerHandle, ref);
    if (!artifact || artifact.ref !== ref || artifact.artifactType !== artifactType) {
      issues.push(issue('EVIDENCE_UNTRUSTED', '$.evidence', `Evidence reference is not bound by the verified owner: ${ref}`));
    } else if (artifact.owner !== expectedEvidenceOwner) {
      issues.push(issue('EVIDENCE_OWNER_MISMATCH', '$.expectedEvidenceOwner', `Evidence owner mismatch for ${ref}.`));
    }
  }
  return { valid: issues.length === 0, issues, data: { evidenceRank: rank } };
}

export interface DeterministicCadpReceiptInput<TPayload> {
  readonly receiptType: string;
  readonly subjectRef: string;
  readonly issuedAt: string;
  readonly payload: TPayload;
  readonly evidenceRefs?: readonly string[];
}

export interface DeterministicCadpReceipt<TPayload> {
  readonly contractVersion: typeof CADP_CONTRACT_VERSION;
  readonly receiptId: string;
  readonly receiptType: string;
  readonly subjectRef: string;
  readonly issuedAt: string;
  readonly payload: TPayload;
  readonly evidenceRefs: readonly string[];
  readonly integrityHash: string;
  readonly receiptGrantsExecution: false;
  readonly receiptGrantsAcceptance: false;
  readonly receiptGrantsFreeze: false;
}

/**
 * Supported canonical JSON data domain for CADP receipt payloads:
 * `null`; `string`; `boolean`; finite `number` (no `NaN`/`Infinity`/`-Infinity`);
 * a dense array (no holes, no extra own properties beyond numeric indices and
 * `length`, no symbol keys) of supported values; or a plain object
 * (`Object.prototype` or `null` prototype, no class instance) whose own keys
 * are all string keys with enumerable, non-accessor (non-getter/setter) data
 * properties, recursively containing only supported values. Explicitly
 * unsupported and rejected with a typed error: `undefined`, `bigint`,
 * `function`, `symbol` values or keys, non-enumerable own properties,
 * accessor (getter/setter) properties, non-plain-object class instances,
 * sparse arrays, arrays with non-index own properties, and cyclic references.
 *
 * canonicalSnapshot walks the input exactly once. It both serializes the
 * canonical JSON text used for hashing and constructs a frozen, independently
 * owned snapshot value from the same walk, so the returned snapshot and the
 * hashed text can never diverge, and no accessor is ever invoked (every read
 * is a direct property-descriptor `.value` read, never a `[key]` property
 * access that could trigger a getter).
 */
function canonicalSnapshot(value: unknown, active: WeakSet<object>): { readonly json: string; readonly snapshot: unknown } {
  if (value === null) return { json: 'null', snapshot: null };
  if (typeof value === 'string' || typeof value === 'boolean') return { json: JSON.stringify(value), snapshot: value };
  if (typeof value === 'number') {
    if (!Number.isFinite(value)) throw new TypeError('CADP receipt payload numbers must be finite.');
    // JSON.stringify(-0) produces the text "0", identical to +0. Normalize
    // the snapshot to +0 so the returned value's Object.is identity always
    // agrees with the hashed text; otherwise {value:-0} and {value:0} would
    // hash identically while returning observably different numbers.
    const normalized = Object.is(value, -0) ? 0 : value;
    return { json: JSON.stringify(normalized), snapshot: normalized };
  }
  if (typeof value === 'undefined' || typeof value === 'bigint' || typeof value === 'function' || typeof value === 'symbol') {
    throw new TypeError(`CADP receipt payload contains unsupported type: ${typeof value}.`);
  }
  if (active.has(value)) throw new TypeError('CADP receipt payload must not contain cycles.');
  // Proxy is unsupported at every nesting depth of the payload, not only at
  // the top level: `Array.isArray` and `Object.getPrototypeOf` below both
  // dispatch through a Proxy's traps as caller-controlled code (unlike
  // `Array.isArray` alone, which merely unwraps to decide true/false but is
  // followed here by real reflective reads), so the rejection must happen
  // before either branch runs, recursively, for every nested value.
  if (!isSupportedReflectionTarget(value)) {
    throw new TypeError('CADP receipt payload must not contain a Proxy value.');
  }
  active.add(value);
  if (Array.isArray(value)) {
    if (Object.getOwnPropertySymbols(value).length > 0) {
      throw new TypeError('CADP receipt payload arrays must not contain symbol-keyed properties.');
    }
    const ownKeys = Object.getOwnPropertyNames(value);
    const expectedKeys = new Set<string>(['length']);
    for (let index = 0; index < value.length; index += 1) expectedKeys.add(String(index));
    if (ownKeys.length !== expectedKeys.size || !ownKeys.every((key) => expectedKeys.has(key))) {
      throw new TypeError('CADP receipt payload arrays must not contain sparse indices or non-index own properties.');
    }
    // Walk by numeric `for` loop and `Object.getOwnPropertyDescriptor` only.
    // `Array.prototype.map`/`forEach`/spread/iterator all read `value[index]`
    // internally, which invokes an index accessor before any descriptor check
    // can run; a plain `for` loop paired with a descriptor read never touches
    // the accessor path at all.
    const items: { readonly json: string; readonly snapshot: unknown }[] = [];
    for (let index = 0; index < value.length; index += 1) {
      const descriptor = Object.getOwnPropertyDescriptor(value, index);
      if (!descriptor || !descriptor.enumerable || 'get' in descriptor || 'set' in descriptor) {
        throw new TypeError(`CADP receipt payload array index ${index} must be an own enumerable data property.`);
      }
      items.push(canonicalSnapshot(descriptor.value, active));
    }
    active.delete(value);
    const jsonParts: string[] = [];
    const snapshotParts: unknown[] = [];
    for (const item of items) {
      jsonParts.push(item.json);
      snapshotParts.push(item.snapshot);
    }
    const json = `[${jsonParts.join(',')}]`;
    const snapshot = Object.freeze(snapshotParts);
    return { json, snapshot };
  }
  if (value && typeof value === 'object') {
    if (Object.getPrototypeOf(value) !== Object.prototype && Object.getPrototypeOf(value) !== null) {
      throw new TypeError('CADP receipt payload objects must be plain JSON objects.');
    }
    if (Object.getOwnPropertySymbols(value).length > 0) {
      throw new TypeError('CADP receipt payload objects must not contain symbol-keyed properties.');
    }
    const keys = Object.getOwnPropertyNames(value).sort((left, right) => (left < right ? -1 : left > right ? 1 : 0));
    const entries: { readonly key: string; readonly result: { readonly json: string; readonly snapshot: unknown } }[] = [];
    for (const key of keys) {
      const descriptor = Object.getOwnPropertyDescriptor(value, key);
      if (!descriptor || !descriptor.enumerable || 'get' in descriptor || 'set' in descriptor) {
        throw new TypeError(`CADP receipt payload key "${key}" must be an own enumerable data property, not an accessor.`);
      }
      entries.push({ key, result: canonicalSnapshot(descriptor.value, active) });
    }
    active.delete(value);
    const jsonParts: string[] = [];
    const snapshotEntries: [string, unknown][] = [];
    for (const entry of entries) {
      jsonParts.push(`${JSON.stringify(entry.key)}:${entry.result.json}`);
      snapshotEntries.push([entry.key, entry.result.snapshot]);
    }
    const json = `{${jsonParts.join(',')}}`;
    const snapshot = Object.freeze(Object.fromEntries(snapshotEntries));
    return { json, snapshot };
  }
  throw new TypeError('CADP receipt payload contains an unsupported value.');
}

const DAYS_IN_MONTH: readonly number[] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

function isLeapYear(year: number): boolean {
  return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
}

/**
 * Validates `issuedAt` against strict ISO-8601 UTC calendar rules. Rejects
 * any value that merely happens to satisfy the `ISO8601_UTC_PATTERN` regex
 * shape but is not a real calendar date/time (e.g. `2026-02-30`, `2026-13-01`,
 * hour `24`, minute/second `60`), rather than delegating to `Date.parse`
 * normalization, which silently rolls invalid components into a different
 * valid date instead of rejecting them.
 */
function isValidIso8601UtcTimestamp(value: string): boolean {
  const match = ISO8601_UTC_PATTERN.exec(value);
  if (!match) return false;
  const year = Number(value.slice(0, 4));
  const month = Number(value.slice(5, 7));
  const day = Number(value.slice(8, 10));
  const hour = Number(value.slice(11, 13));
  const minute = Number(value.slice(14, 16));
  const second = Number(value.slice(17, 19));
  if (month < 1 || month > 12) return false;
  const maxDay = month === 2 && isLeapYear(year) ? 29 : DAYS_IN_MONTH[month - 1];
  if (day < 1 || day > maxDay) return false;
  if (hour > 23) return false;
  if (minute > 59) return false;
  if (second > 59) return false;
  return true;
}

/**
 * The receipt-input front door. Reads every required field of `input`
 * exclusively through `ownDataField` (own, enumerable, non-accessor data
 * descriptors) - never a destructure, never direct property access, never a
 * string method / regex / coercion applied to a field before its type is
 * confirmed. `input` itself is rejected first if it is a Proxy or otherwise
 * not a supported reflection target, before any descriptor read is
 * attempted on it. Inherited-only fields (e.g. `receiptType` set only on
 * `input`'s prototype) are treated as absent by `ownDataField`, so they are
 * rejected exactly like a missing field, not silently read through the
 * prototype chain. Returns `undefined` if any required field is absent,
 * inherited-only, an accessor, non-enumerable, or the wrong runtime type;
 * the caller converts that into a single controlled `TypeError`, so no raw
 * incidental error (e.g. `value.slice is not a function`, or an uncaught
 * Proxy-trap exception) can ever surface from this function.
 */
function readReceiptInputFrontDoor(
  input: unknown,
): { readonly receiptType: string; readonly subjectRef: string; readonly issuedAt: string; readonly payload: unknown; readonly evidenceRefs: readonly string[] } | undefined {
  if (!isSupportedReflectionTarget(input)) return undefined;
  const receiptTypeField = ownDataField(input, 'receiptType');
  const subjectRefField = ownDataField(input, 'subjectRef');
  const issuedAtField = ownDataField(input, 'issuedAt');
  const payloadField = ownDataField(input, 'payload');
  if (
    typeof receiptTypeField.value !== 'string' || !receiptTypeField.value.trim() ||
    typeof subjectRefField.value !== 'string' || !subjectRefField.value.trim() ||
    typeof issuedAtField.value !== 'string' ||
    !payloadField.present
  ) {
    return undefined;
  }
  if (!isValidIso8601UtcTimestamp(issuedAtField.value)) return undefined;
  // evidenceRefs is optional: a genuinely missing own property is allowed
  // (defaults to an empty list), and an inherited-only value is ignored as
  // absent so it can never participate in identity. An own accessor,
  // non-enumerable, or malformed-shape property must be rejected.
  // `input` was already confirmed a supported (non-Proxy) reflection target
  // at function entry, so this descriptor read cannot dispatch a trap.
  const hasOwnEvidenceRefsKey = Object.getOwnPropertyDescriptor(input as object, 'evidenceRefs') !== undefined;
  let evidenceRefsInternal: readonly string[];
  if (!hasOwnEvidenceRefsKey) {
    evidenceRefsInternal = [];
  } else {
    const evidenceRefsField = ownDataField(input, 'evidenceRefs');
    if (!evidenceRefsField.present) return undefined;
    const internal = readOwnDataArray(evidenceRefsField.value, (item): item is string => typeof item === 'string');
    if (!internal) return undefined;
    for (const ref of internal) {
      if (!ref.trim()) return undefined;
    }
    evidenceRefsInternal = internal;
  }
  return {
    receiptType: receiptTypeField.value,
    subjectRef: subjectRefField.value,
    issuedAt: issuedAtField.value,
    payload: payloadField.value,
    evidenceRefs: evidenceRefsInternal,
  };
}

export function createDeterministicCadpReceipt<TPayload>(
  input: DeterministicCadpReceiptInput<TPayload>,
): DeterministicCadpReceipt<TPayload> {
  const front = readReceiptInputFrontDoor(input);
  if (!front) {
    throw new TypeError(
      'CADP receipt requires non-empty own-property receiptType/subjectRef strings, a strict calendar-valid ISO-8601 UTC issuedAt string (YYYY-MM-DDTHH:mm:ss[.d..d]Z, 1-9 optional fractional digits), an own-property payload, and evidenceRefs that is either absent or a valid own-property dense array of non-empty strings.',
    );
  }
  const { receiptType, subjectRef, issuedAt, payload } = front;
  const evidenceRefs = Object.freeze(uniqueSorted(front.evidenceRefs));
  const identity = { receiptType, subjectRef, issuedAt, payload: payload as TPayload, evidenceRefs };
  const canonical = canonicalSnapshot(identity, new WeakSet<object>());
  const integrityHash = createHash('sha256').update(canonical.json, 'utf8').digest('hex');
  const canonicalIdentity = canonical.snapshot as {
    readonly receiptType: string;
    readonly subjectRef: string;
    readonly issuedAt: string;
    readonly payload: TPayload;
    readonly evidenceRefs: readonly string[];
  };
  return Object.freeze({
    contractVersion: CADP_CONTRACT_VERSION,
    receiptId: `cadp-${integrityHash}`,
    receiptType: canonicalIdentity.receiptType,
    subjectRef: canonicalIdentity.subjectRef,
    issuedAt: canonicalIdentity.issuedAt,
    payload: canonicalIdentity.payload,
    evidenceRefs: canonicalIdentity.evidenceRefs,
    integrityHash,
    receiptGrantsExecution: false,
    receiptGrantsAcceptance: false,
    receiptGrantsFreeze: false,
  });
}
