/**
 * Capability workspace profile / bootstrap policy bundle validation kernel.
 *
 * Pure in-memory validation only. This module accepts an unknown
 * caller-supplied workspace-profile and bootstrap-policy bundle, validates the
 * T11-owned workspace-boundary and policy fields, projects the profile through
 * the current T7 selector, and binds the selected profile to a fail-closed
 * bootstrap policy. It never reads, copies, materializes, persists, installs,
 * acquires, or executes anything, and every action-authority output is
 * deliberately false.
 */

import { isProxy } from 'node:util/types';
import {
  evaluateCapabilityPreflightProfilePolicy,
  type CapabilityPreflightNetworkMode,
  type CapabilityPreflightProfile,
  type CapabilityPreflightProfilePolicyResult,
  type CapabilityPreflightRiskLevel,
} from './capability-preflight-profile-policy.contract';

export const CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION =
  'cvf.capabilityWorkspaceBootstrapPolicyBundle.v1' as const;
export const CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_RESULT_VERSION =
  'cvf.capabilityWorkspaceBootstrapPolicyBundleResult.v1' as const;

export interface CapabilityWorkspaceBootstrapProfile extends CapabilityPreflightProfile {
  readonly writableBoundaries: readonly string[];
  readonly credentialBindings: readonly string[];
}

export interface CapabilityWorkspaceBootstrapPolicy {
  readonly policyId: string;
  readonly defaultDecision: 'BLOCK';
  readonly requireIntegrity: boolean;
  readonly maxRepairRoundsWithoutNewEvidence: number;
  readonly networkDefault?: string;
  readonly allowNetwork?: boolean;
  readonly allowVerifiedLocalArtifact?: boolean;
  readonly requireDestinationAllowlist?: boolean;
  readonly allowOfflineArtifacts?: boolean;
  readonly allowWorkspaceLocal?: boolean;
  readonly allowUserLocalWithApproval?: boolean;
  readonly allowSystemInstallWithApproval?: boolean;
  readonly requirePublisher?: boolean;
  readonly requireLicense?: boolean;
  readonly forbiddenMutations?: readonly string[];
}

export interface CapabilityWorkspaceBootstrapPolicyBundleInput {
  readonly schemaVersion: typeof CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION;
  readonly profile: CapabilityWorkspaceBootstrapProfile;
  readonly bootstrapPolicy: CapabilityWorkspaceBootstrapPolicy;
  readonly requestedProfileId: string;
  readonly observedPlatform: string;
  readonly riskLevel: CapabilityPreflightRiskLevel;
  readonly now: string;
}

export type CapabilityWorkspaceBootstrapPolicyBundleIssueCode =
  | 'MALFORMED_INPUT'
  | 'UNKNOWN_KEY'
  | 'INVALID_FIELD'
  | 'UNSAFE_STRING'
  | 'RAW_SECRET_DETECTED'
  | 'UNBOUNDED_COLLECTION'
  | 'SPARSE_ARRAY'
  | 'DUPLICATE_VALUE'
  | 'POLICY_ID_MISMATCH'
  | 'POLICY_BLOCK_DEFAULT_WEAKENED'
  | 'POLICY_INTEGRITY_WEAKENED'
  | 'POLICY_REPAIR_BOUNDS_INVALID'
  | 'POLICY_VARIANT_INVALID'
  | 'POLICY_VARIANT_WEAKENED'
  | 'BINDING_MISMATCH'
  | 'T7_SELECTION_REJECTED';

export interface CapabilityWorkspaceBootstrapPolicyBundleIssue {
  readonly code: CapabilityWorkspaceBootstrapPolicyBundleIssueCode;
  readonly path: string;
  readonly message: string;
}

export interface CapabilityWorkspaceBootstrapPolicyBundleResult {
  readonly schemaVersion: typeof CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_RESULT_VERSION;
  readonly status: 'VALIDATED_POLICY_EVIDENCE' | 'REJECTED';
  readonly selectedProfileId: string;
  readonly policyId: string;
  readonly networkMode: CapabilityPreflightNetworkMode;
  readonly ttlSeconds: number;
  readonly installPreference: readonly string[];
  readonly writableBoundaries: readonly string[];
  readonly credentialBindings: readonly string[];
  readonly maxRepairRoundsWithoutNewEvidence: number;
  readonly issues: readonly CapabilityWorkspaceBootstrapPolicyBundleIssue[];
  readonly selectionEvidence: CapabilityPreflightProfilePolicyResult | null;
  readonly evaluatedAt: string;
  readonly authorityStatus: 'EVIDENCE_ONLY';
  readonly profileMaterialized: false;
  readonly policyPersisted: false;
  readonly workspaceInitialized: false;
  readonly environmentReadAuthorized: false;
  readonly installationAuthorized: false;
  readonly executionAuthorized: false;
  readonly acquisitionAuthorized: false;
  readonly mutationAuthorized: false;
  readonly networkAuthorized: false;
  readonly taskAuthorityGranted: false;
}

type PlainRecord = Record<string, unknown>;

const SAFE_TEXT = /^[^\u0000-\u001F\u007F]{1,512}$/;
const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const SAFE_TOKEN = /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const MAX_ITEMS = 64;

const RISK_LEVELS = ['R0', 'R1', 'R2', 'R3'] as const;
const NETWORK_MODES = ['NORMAL', 'OFFLINE', 'RESTRICTED'] as const;

const WORKSPACE_ROOT = '${WORKSPACE_ROOT}';

const INPUT_KEYS = [
  'schemaVersion', 'profile', 'bootstrapPolicy', 'requestedProfileId',
  'observedPlatform', 'riskLevel', 'now',
] as const;
const PROFILE_KEYS = [
  'profileId', 'platforms', 'shellPreference', 'networkMode', 'installPreference',
  'scanTtlSeconds', 'privilegePolicy', 'pathDiscovery', 'allowedDestinations', 'notes',
  'writableBoundaries', 'credentialBindings',
] as const;
const T7_PROFILE_KEYS = [
  'profileId', 'platforms', 'shellPreference', 'networkMode', 'installPreference',
  'scanTtlSeconds', 'privilegePolicy', 'pathDiscovery', 'allowedDestinations', 'notes',
] as const;

const OFFLINE_POLICY_KEYS = [
  'policyId', 'defaultDecision', 'networkDefault', 'allowNetwork',
  'allowVerifiedLocalArtifact', 'requireIntegrity', 'maxRepairRoundsWithoutNewEvidence',
] as const;
const RESTRICTED_POLICY_KEYS = [
  'policyId', 'defaultDecision', 'networkDefault', 'requireDestinationAllowlist',
  'allowOfflineArtifacts', 'requireIntegrity', 'maxRepairRoundsWithoutNewEvidence',
] as const;
const NORMAL_POLICY_KEYS = [
  'policyId', 'defaultDecision', 'allowWorkspaceLocal', 'allowUserLocalWithApproval',
  'allowSystemInstallWithApproval', 'requireIntegrity', 'requirePublisher',
  'requireLicense', 'maxRepairRoundsWithoutNewEvidence', 'forbiddenMutations',
] as const;

const REQUIRED_FORBIDDEN_MUTATIONS = [
  'unapproved system PATH',
  'unapproved registry',
  'unapproved services',
  'raw credential storage',
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

function denseArray(value: unknown, limit: number): readonly unknown[] | null {
  if (!Array.isArray(value) || isProxy(value)) return null;
  try {
    if (Object.getPrototypeOf(value) !== Array.prototype || Object.getOwnPropertySymbols(value).length > 0) return null;
    if (value.length > limit) return value;
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

function hasExactKeys(record: PlainRecord, required: readonly string[]): boolean {
  const keys = Object.keys(record);
  return required.every((key) => keys.includes(key))
    && keys.every((key) => required.includes(key));
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

function addIssue(
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
  code: CapabilityWorkspaceBootstrapPolicyBundleIssueCode,
  path: string,
  message: string,
): void {
  issues.push(Object.freeze({ code, path, message }));
}

function inspectString(
  value: unknown,
  path: string,
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
  options: { id?: boolean; token?: boolean } = {},
): value is string | null {
  if (typeof value !== 'string' || !SAFE_TEXT.test(value)) {
    addIssue(issues, 'UNSAFE_STRING', path, 'Value must be a bounded control-character-free string.');
    return false;
  }
  if (secretLike(value)) {
    addIssue(issues, 'RAW_SECRET_DETECTED', path, 'Secret-like material is forbidden.');
    return false;
  }
  if (options.id && !SAFE_ID.test(value)) {
    addIssue(issues, 'INVALID_FIELD', path, 'Value must be a bounded safe identifier.');
    return false;
  }
  if (options.token && !SAFE_TOKEN.test(value)) {
    addIssue(issues, 'INVALID_FIELD', path, 'Value must be a bounded safe token.');
    return false;
  }
  return true;
}

function inspectRecord(
  value: unknown,
  path: string,
  required: readonly string[],
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
): PlainRecord | null {
  const record = descriptorRecord(value);
  if (!record) {
    addIssue(issues, 'MALFORMED_INPUT', path, 'Value must be a plain non-Proxy data object without accessors or symbols.');
    return null;
  }
  if (!hasExactKeys(record, required)) {
    addIssue(issues, 'UNKNOWN_KEY', path, 'Object keys do not match the bounded contract.');
    return null;
  }
  return record;
}

function inspectArray(
  value: unknown,
  path: string,
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
  limit = MAX_ITEMS,
): readonly unknown[] | null {
  const array = denseArray(value, limit);
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

function duplicate(values: readonly string[]): boolean {
  return new Set(values).size !== values.length;
}

function isOneOf(value: unknown, allowed: readonly string[]): value is string {
  return typeof value === 'string' && allowed.includes(value);
}

function freezeIssues(
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
): readonly CapabilityWorkspaceBootstrapPolicyBundleIssue[] {
  return Object.freeze([...issues].sort((left, right) => (
    left.path.localeCompare(right.path)
    || left.code.localeCompare(right.code)
    || left.message.localeCompare(right.message)
  )));
}

function validateWritableBoundaries(
  value: unknown,
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
): readonly string[] {
  const array = inspectArray(value, '$.profile.writableBoundaries', issues);
  if (!array) return Object.freeze([]);
  if (array.length === 0) {
    addIssue(issues, 'INVALID_FIELD', '$.profile.writableBoundaries', 'Writable boundaries must be non-empty.');
    return Object.freeze([]);
  }
  const result: string[] = [];
  array.forEach((item, index) => {
    const path = `$.profile.writableBoundaries[${index}]`;
    if (!inspectString(item, path, issues)) return;
    const text = item as string;
    if (text !== WORKSPACE_ROOT) {
      addIssue(issues, 'INVALID_FIELD', path, 'Writable boundary must be the literal ${WORKSPACE_ROOT} placeholder in this tranche.');
      return;
    }
    result.push(text);
  });
  if (duplicate(result)) {
    addIssue(issues, 'DUPLICATE_VALUE', '$.profile.writableBoundaries', 'Writable boundaries must be unique.');
  }
  return Object.freeze(result);
}

function validateCredentialBindings(
  value: unknown,
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
): readonly string[] {
  const array = inspectArray(value, '$.profile.credentialBindings', issues);
  if (!array) return Object.freeze([]);
  const result: string[] = [];
  array.forEach((item, index) => {
    const path = `$.profile.credentialBindings[${index}]`;
    if (inspectString(item, path, issues, { id: true })) result.push(item as string);
  });
  if (duplicate(result)) {
    addIssue(issues, 'DUPLICATE_VALUE', '$.profile.credentialBindings', 'Credential binding references must be unique.');
  }
  return Object.freeze(result);
}

interface ValidatedProfile {
  readonly record: PlainRecord;
  readonly profileId: string;
  readonly networkMode: CapabilityPreflightNetworkMode;
  readonly writableBoundaries: readonly string[];
  readonly credentialBindings: readonly string[];
}

function validateProfile(
  value: unknown,
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
): ValidatedProfile | null {
  const profile = inspectRecord(value, '$.profile', PROFILE_KEYS, issues);
  if (!profile) return null;
  const networkModeValue = data(profile, 'networkMode');
  if (!isOneOf(networkModeValue, NETWORK_MODES)) {
    addIssue(issues, 'INVALID_FIELD', '$.profile.networkMode', 'Unsupported network mode.');
    return null;
  }
  const profileIdValue = data(profile, 'profileId');
  const writableBoundaries = validateWritableBoundaries(data(profile, 'writableBoundaries'), issues);
  const credentialBindings = validateCredentialBindings(data(profile, 'credentialBindings'), issues);
  return {
    record: profile,
    profileId: typeof profileIdValue === 'string' ? profileIdValue : 'invalid',
    networkMode: networkModeValue as CapabilityPreflightNetworkMode,
    writableBoundaries,
    credentialBindings,
  };
}

function validateForbiddenMutations(
  value: unknown,
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
): void {
  const array = inspectArray(value, '$.bootstrapPolicy.forbiddenMutations', issues);
  if (!array) return;
  if (array.length === 0) {
    addIssue(issues, 'INVALID_FIELD', '$.bootstrapPolicy.forbiddenMutations', 'Forbidden mutations must be non-empty.');
    return;
  }
  const result: string[] = [];
  array.forEach((item, index) => {
    const path = `$.bootstrapPolicy.forbiddenMutations[${index}]`;
    if (inspectString(item, path, issues)) result.push(item as string);
  });
  if (duplicate(result)) {
    addIssue(issues, 'DUPLICATE_VALUE', '$.bootstrapPolicy.forbiddenMutations', 'Forbidden mutations must be unique.');
  }
  for (const required of REQUIRED_FORBIDDEN_MUTATIONS) {
    if (!result.includes(required)) {
      addIssue(issues, 'POLICY_VARIANT_WEAKENED', '$.bootstrapPolicy.forbiddenMutations', 'Forbidden mutations must protect system PATH, registry, services, and raw credential storage.');
      return;
    }
  }
}

interface ValidatedPolicy {
  readonly policyId: string;
  readonly maxRepairRoundsWithoutNewEvidence: number;
}

function validatePolicy(
  value: unknown,
  networkMode: CapabilityPreflightNetworkMode | null,
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
): ValidatedPolicy | null {
  if (networkMode === null) return null;
  const keys = networkMode === 'OFFLINE' ? OFFLINE_POLICY_KEYS
    : networkMode === 'RESTRICTED' ? RESTRICTED_POLICY_KEYS
    : NORMAL_POLICY_KEYS;
  const policy = inspectRecord(value, '$.bootstrapPolicy', keys, issues);
  if (!policy) return null;

  if (data(policy, 'defaultDecision') !== 'BLOCK') {
    addIssue(issues, 'POLICY_BLOCK_DEFAULT_WEAKENED', '$.bootstrapPolicy.defaultDecision', 'Default decision must remain BLOCK.');
  }
  if (data(policy, 'requireIntegrity') !== true) {
    addIssue(issues, 'POLICY_INTEGRITY_WEAKENED', '$.bootstrapPolicy.requireIntegrity', 'Integrity must be required.');
  }
  const maxRounds = data(policy, 'maxRepairRoundsWithoutNewEvidence');
  if (typeof maxRounds !== 'number' || !Number.isInteger(maxRounds) || maxRounds < 1 || maxRounds > 3) {
    addIssue(issues, 'POLICY_REPAIR_BOUNDS_INVALID', '$.bootstrapPolicy.maxRepairRoundsWithoutNewEvidence', 'Repair rounds must be an integer from 1 through 3.');
  }

  if (networkMode === 'OFFLINE') {
    if (data(policy, 'networkDefault') !== 'DENY' || data(policy, 'allowNetwork') !== false || data(policy, 'allowVerifiedLocalArtifact') !== true) {
      addIssue(issues, 'POLICY_VARIANT_WEAKENED', '$.bootstrapPolicy', 'OFFLINE policy must deny network and allow only verified local artifacts.');
    }
  } else if (networkMode === 'RESTRICTED') {
    if (data(policy, 'networkDefault') !== 'DENY' || data(policy, 'requireDestinationAllowlist') !== true || data(policy, 'allowOfflineArtifacts') !== true) {
      addIssue(issues, 'POLICY_VARIANT_WEAKENED', '$.bootstrapPolicy', 'RESTRICTED policy must deny network, require destination allowlisting, and allow offline artifacts.');
    }
  } else {
    if (data(policy, 'allowWorkspaceLocal') !== true
      || data(policy, 'allowUserLocalWithApproval') !== true
      || data(policy, 'allowSystemInstallWithApproval') !== true
      || data(policy, 'requirePublisher') !== true
      || data(policy, 'requireLicense') !== true) {
      addIssue(issues, 'POLICY_VARIANT_WEAKENED', '$.bootstrapPolicy', 'NORMAL local-install policy must require workspace allowance, approval, publisher, and license checks.');
    }
    validateForbiddenMutations(data(policy, 'forbiddenMutations'), issues);
  }

  const policyIdValue = data(policy, 'policyId');
  return {
    policyId: typeof policyIdValue === 'string' ? policyIdValue : 'invalid',
    maxRepairRoundsWithoutNewEvidence: typeof maxRounds === 'number' && Number.isInteger(maxRounds) ? maxRounds : 0,
  };
}

function toT7Projection(profile: PlainRecord): Record<string, unknown> {
  const projection: Record<string, unknown> = {};
  for (const key of T7_PROFILE_KEYS) {
    projection[key] = data(profile, key);
  }
  return projection;
}

function authorityFields() {
  return {
    authorityStatus: 'EVIDENCE_ONLY' as const,
    profileMaterialized: false as const,
    policyPersisted: false as const,
    workspaceInitialized: false as const,
    environmentReadAuthorized: false as const,
    installationAuthorized: false as const,
    executionAuthorized: false as const,
    acquisitionAuthorized: false as const,
    mutationAuthorized: false as const,
    networkAuthorized: false as const,
    taskAuthorityGranted: false as const,
  };
}

function buildResult(
  status: 'VALIDATED_POLICY_EVIDENCE' | 'REJECTED',
  selectionEvidence: CapabilityPreflightProfilePolicyResult | null,
  profile: ValidatedProfile | null,
  policy: ValidatedPolicy | null,
  issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[],
  evaluatedAt: string,
): CapabilityWorkspaceBootstrapPolicyBundleResult {
  if (status === 'VALIDATED_POLICY_EVIDENCE' && selectionEvidence !== null && profile !== null && policy !== null) {
    return Object.freeze({
      schemaVersion: CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_RESULT_VERSION,
      status,
      selectedProfileId: selectionEvidence.selectedProfileId,
      policyId: policy.policyId,
      networkMode: selectionEvidence.networkMode,
      ttlSeconds: selectionEvidence.ttlSeconds,
      installPreference: Object.freeze([...selectionEvidence.installPreference]),
      writableBoundaries: Object.freeze([...profile.writableBoundaries]),
      credentialBindings: Object.freeze([...profile.credentialBindings]),
      maxRepairRoundsWithoutNewEvidence: policy.maxRepairRoundsWithoutNewEvidence,
      issues: Object.freeze([]),
      selectionEvidence,
      evaluatedAt,
      ...authorityFields(),
    });
  }
  return Object.freeze({
    schemaVersion: CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_RESULT_VERSION,
    status: 'REJECTED' as const,
    selectedProfileId: 'invalid',
    policyId: 'invalid',
    networkMode: 'NORMAL' as const,
    ttlSeconds: 0,
    installPreference: Object.freeze([]),
    writableBoundaries: Object.freeze([]),
    credentialBindings: Object.freeze([]),
    maxRepairRoundsWithoutNewEvidence: 0,
    issues: freezeIssues(issues),
    selectionEvidence: null,
    evaluatedAt,
    ...authorityFields(),
  });
}

export function evaluateCapabilityWorkspaceBootstrapPolicyBundle(
  input: unknown,
): CapabilityWorkspaceBootstrapPolicyBundleResult {
  const issues: CapabilityWorkspaceBootstrapPolicyBundleIssue[] = [];
  const envelope = inspectRecord(input, '$', INPUT_KEYS, issues);

  let nowValue: string | null = null;
  let requestedProfileId: string | null = null;
  let observedPlatform: string | null = null;
  let riskLevel: CapabilityPreflightRiskLevel | null = null;
  let profile: ValidatedProfile | null = null;
  let policy: ValidatedPolicy | null = null;

  if (envelope) {
    if (data(envelope, 'schemaVersion') !== CAPABILITY_WORKSPACE_BOOTSTRAP_POLICY_BUNDLE_CONTRACT_VERSION) {
      addIssue(issues, 'INVALID_FIELD', '$.schemaVersion', 'Unsupported bundle-input version.');
    }
    if (validUtc(data(envelope, 'now'))) {
      nowValue = data(envelope, 'now') as string;
    } else {
      addIssue(issues, 'INVALID_FIELD', '$.now', 'Current time must be ISO-8601 UTC.');
    }
    const requested = data(envelope, 'requestedProfileId');
    if (inspectString(requested, '$.requestedProfileId', issues, { id: true })) requestedProfileId = requested as string;
    const observed = data(envelope, 'observedPlatform');
    if (inspectString(observed, '$.observedPlatform', issues, { token: true })) observedPlatform = observed as string;
    const risk = data(envelope, 'riskLevel');
    if (isOneOf(risk, RISK_LEVELS)) {
      riskLevel = risk as CapabilityPreflightRiskLevel;
    } else {
      addIssue(issues, 'INVALID_FIELD', '$.riskLevel', 'Unsupported risk level.');
    }

    profile = validateProfile(data(envelope, 'profile'), issues);
    policy = validatePolicy(data(envelope, 'bootstrapPolicy'), profile?.networkMode ?? null, issues);
  }

  let selectionEvidence: CapabilityPreflightProfilePolicyResult | null = null;
  if (profile !== null) {
    const projection = toT7Projection(profile.record);
    selectionEvidence = evaluateCapabilityPreflightProfilePolicy({
      catalog: [projection as unknown as CapabilityPreflightProfile],
      requestedProfileId: requestedProfileId ?? 'invalid',
      observedPlatform: observedPlatform ?? 'invalid',
      riskLevel: riskLevel ?? 'R0',
      now: nowValue ?? '1970-01-01T00:00:00Z',
    });
    if (selectionEvidence.disposition !== 'SELECTED') {
      addIssue(issues, 'T7_SELECTION_REJECTED', '$.profile', 'The projected profile did not pass T7 selection.');
    }
  }

  if (profile !== null && policy !== null) {
    const expectedPolicyId = `capability-bootstrap.${profile.profileId}`;
    if (policy.policyId !== expectedPolicyId) {
      addIssue(issues, 'POLICY_ID_MISMATCH', '$.bootstrapPolicy.policyId', 'Policy id must equal the capability-bootstrap.<profileId> binding.');
    }
    if (profile.networkMode === 'NORMAL') {
      const platforms = data(profile.record, 'platforms');
      const isWin32 = Array.isArray(platforms) && !isProxy(platforms) && platforms.includes('win32');
      if (!isWin32) {
        addIssue(issues, 'BINDING_MISMATCH', '$.profile.platforms', 'NORMAL local-install policy requires a win32-compatible profile.');
      }
    }
  }

  const evaluatedAt = nowValue ?? '1970-01-01T00:00:00Z';
  const accepted = issues.length === 0 && profile !== null && policy !== null && selectionEvidence !== null && selectionEvidence.disposition === 'SELECTED';
  return buildResult(
    accepted ? 'VALIDATED_POLICY_EVIDENCE' : 'REJECTED',
    accepted ? selectionEvidence : null,
    accepted ? profile : null,
    accepted ? policy : null,
    issues,
    evaluatedAt,
  );
}
