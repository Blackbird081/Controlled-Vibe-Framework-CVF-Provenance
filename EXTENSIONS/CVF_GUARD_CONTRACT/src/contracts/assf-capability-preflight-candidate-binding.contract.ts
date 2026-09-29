/**
 * ASSF package metadata to capability-preflight candidate binding kernel.
 *
 * Pure in-memory validation and projection only. This module accepts an
 * unknown caller-supplied bundle of ASSF package metadata fields (identity,
 * lifecycle, composition, risk/authority, external disposition, platform,
 * and source evidence) and projects a bounded capability-preflight candidate
 * binding. It never reads the ASSF registry or generated index, resolves or
 * loads a package, opens an instruction body, executes composition, or
 * mutates package lifecycle state. `authorityStatus` is the literal
 * `CANDIDATE_ONLY` on every return path, and every action-authority output
 * is deliberately false. Loading, composing, or referencing this binding
 * never grants new authority, matching the ASSF No-Self-Activation and
 * No-Automatic-Promotion invariants.
 */

import { isProxy } from 'node:util/types';

export const ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_CONTRACT_VERSION =
  'cvf.assfCapabilityPreflightCandidateBinding.v1' as const;
export const ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_RESULT_VERSION =
  'cvf.assfCapabilityPreflightCandidateBindingResult.v1' as const;

export type AssfPackageLifecycleStatus =
  | 'CANDIDATE' | 'PROPOSED' | 'APPROVED' | 'ACTIVE' | 'DEPRECATED' | 'RETIRED' | 'REJECTED';
export type AssfPackageRiskLevel = 'R0' | 'R1' | 'R2' | 'R3';
export type AssfCliMcpDisposition =
  | 'CONTRACT_ONLY' | 'IMPLEMENTED' | 'DEFERRED_WITH_REASON' | 'N/A_WITH_REASON' | 'PROHIBITED';
export type AssfCandidateApprovalState = 'AWAITING_REVIEW' | 'APPROVED' | 'REJECTED';
export type AssfCandidateUatState = 'NOT_STARTED' | 'IN_PROGRESS' | 'PASSED' | 'FAILED';
export type AssfCandidateCertificationState = 'NOT_STARTED' | 'IN_PROGRESS' | 'CERTIFIED' | 'FAILED';

export interface AssfPackageMetadata {
  readonly skillId: string;
  readonly version: string;
  readonly status: AssfPackageLifecycleStatus;
  readonly candidateState: AssfPackageLifecycleStatus;
  readonly approvalState: AssfCandidateApprovalState;
  readonly uatState: AssfCandidateUatState;
  readonly certificationState: AssfCandidateCertificationState;
  readonly riskCeiling: AssfPackageRiskLevel;
  readonly authorityCeiling: string;
  readonly externalCliMcpDisposition: AssfCliMcpDisposition;
  readonly capabilityBoundary: string;
  readonly platformCompatibility: readonly string[];
  readonly taskClasses: readonly string[];
  readonly dependencies: readonly string[];
  readonly conflicts: readonly string[];
  readonly sourceArtifacts: readonly string[];
}

export interface AssfCapabilityPreflightCandidateBindingInput {
  readonly schemaVersion: typeof ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_CONTRACT_VERSION;
  readonly expectedPackageId: string;
  readonly metadata: AssfPackageMetadata;
  readonly now: string;
}

export type AssfCapabilityPreflightCandidateBindingIssueCode =
  | 'MALFORMED_INPUT'
  | 'UNKNOWN_KEY'
  | 'INVALID_FIELD'
  | 'UNSAFE_STRING'
  | 'RAW_SECRET_DETECTED'
  | 'UNBOUNDED_COLLECTION'
  | 'SPARSE_ARRAY'
  | 'DUPLICATE_VALUE'
  | 'PACKAGE_ID_MISMATCH'
  | 'SELF_DEPENDENCY'
  | 'DEPENDENCY_CONFLICT_OVERLAP'
  | 'LIFECYCLE_INELIGIBLE'
  | 'LIFECYCLE_CONTRADICTION'
  | 'UAT_REQUIRED'
  | 'CERTIFICATION_REQUIRED'
  | 'EXTERNAL_ADAPTER_FORBIDDEN';

export interface AssfCapabilityPreflightCandidateBindingIssue {
  readonly code: AssfCapabilityPreflightCandidateBindingIssueCode;
  readonly path: string;
  readonly message: string;
}

export type AssfCapabilityPreflightCandidateBindingStatus =
  | 'CANDIDATE_BINDING_ACCEPTED'
  | 'CANDIDATE_BINDING_REJECTED'
  | 'CANDIDATE_BINDING_BLOCKED';

export interface AssfCapabilityPreflightCandidateBindingResult {
  readonly schemaVersion: typeof ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_RESULT_VERSION;
  readonly bindingStatus: AssfCapabilityPreflightCandidateBindingStatus;
  readonly packageId: string;
  readonly version: string;
  readonly lifecycleStatus: AssfPackageLifecycleStatus | 'invalid';
  readonly candidateState: AssfPackageLifecycleStatus | 'invalid';
  readonly approvalState: AssfCandidateApprovalState | 'invalid';
  readonly uatState: AssfCandidateUatState | 'invalid';
  readonly certificationState: AssfCandidateCertificationState | 'invalid';
  readonly riskCeiling: AssfPackageRiskLevel | 'invalid';
  readonly authorityCeiling: string;
  readonly externalCliMcpDisposition: AssfCliMcpDisposition | 'invalid';
  readonly capabilityBoundary: string;
  readonly routingEligible: boolean;
  readonly taskClasses: readonly string[];
  readonly dependencies: readonly string[];
  readonly conflicts: readonly string[];
  readonly platformCompatibility: readonly string[];
  readonly sourceArtifacts: readonly string[];
  readonly issues: readonly AssfCapabilityPreflightCandidateBindingIssue[];
  readonly evaluatedAt: string;
  readonly authorityStatus: 'CANDIDATE_ONLY';
  readonly activationAuthorized: false;
  readonly loadingAuthorized: false;
  readonly instructionBodyReadAuthorized: false;
  readonly executionAuthorized: false;
  readonly mutationAuthorized: false;
  readonly acquisitionAuthorized: false;
  readonly externalAdapterAuthorized: false;
  readonly providerCallAuthorized: false;
  readonly publicWriteAuthorized: false;
  readonly taskAuthorityGranted: false;
}

type PlainRecord = Record<string, unknown>;

const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const SAFE_VERSION = /^[A-Za-z0-9._-]{1,64}$/;
const SAFE_TEXT = /^[^\x00-\x1f\x7f]{1,512}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const SECRET_SIGNAL = /(?:\b(?:api[_-]?key|password|token|secret|credential|cookie)\b\s*[=:]\s*\S+|\bbearer\s+\S+|-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----)/i;
const MAX_ITEMS = 32;

const RISK_LEVELS: readonly AssfPackageRiskLevel[] = ['R0', 'R1', 'R2', 'R3'];
const LIFECYCLE_STATUSES: readonly AssfPackageLifecycleStatus[] = [
  'CANDIDATE', 'PROPOSED', 'APPROVED', 'ACTIVE', 'DEPRECATED', 'RETIRED', 'REJECTED',
];
const CLI_MCP_DISPOSITIONS: readonly AssfCliMcpDisposition[] = [
  'CONTRACT_ONLY', 'IMPLEMENTED', 'DEFERRED_WITH_REASON', 'N/A_WITH_REASON', 'PROHIBITED',
];
const APPROVAL_STATES: readonly AssfCandidateApprovalState[] = ['AWAITING_REVIEW', 'APPROVED', 'REJECTED'];
const UAT_STATES: readonly AssfCandidateUatState[] = ['NOT_STARTED', 'IN_PROGRESS', 'PASSED', 'FAILED'];
const CERTIFICATION_STATES: readonly AssfCandidateCertificationState[] = ['NOT_STARTED', 'IN_PROGRESS', 'CERTIFIED', 'FAILED'];

// Only ACTIVE packages require the extra pass-through CERTIFIED gate; ASSF-T1
// does not mandate certification for CANDIDATE/PROPOSED/APPROVED states.
const CERTIFICATION_REQUIRED_STATUSES: readonly AssfPackageLifecycleStatus[] = ['ACTIVE'];
const INELIGIBLE_STATUSES: readonly AssfPackageLifecycleStatus[] = ['DEPRECATED', 'RETIRED', 'REJECTED'];
const ROUTABLE_STATUSES: readonly AssfPackageLifecycleStatus[] = ['APPROVED', 'ACTIVE'];

const INPUT_KEYS = ['schemaVersion', 'expectedPackageId', 'metadata', 'now'] as const;
const METADATA_KEYS = [
  'skillId', 'version', 'status', 'candidateState', 'approvalState', 'uatState',
  'certificationState', 'riskCeiling', 'authorityCeiling', 'externalCliMcpDisposition',
  'capabilityBoundary', 'platformCompatibility', 'taskClasses', 'dependencies',
  'conflicts', 'sourceArtifacts',
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

function hasSecretSignal(value: string): boolean {
  return SECRET_SIGNAL.test(value);
}

function addIssue(
  issues: AssfCapabilityPreflightCandidateBindingIssue[],
  code: AssfCapabilityPreflightCandidateBindingIssueCode,
  path: string,
  message: string,
): void {
  issues.push(Object.freeze({ code, path, message }));
}

function inspectRecord(
  value: unknown,
  path: string,
  required: readonly string[],
  issues: AssfCapabilityPreflightCandidateBindingIssue[],
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

function denseArray(value: unknown): readonly unknown[] | null {
  if (isProxy(value) || !Array.isArray(value)) return null;
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

function inspectString(
  value: unknown,
  path: string,
  issues: AssfCapabilityPreflightCandidateBindingIssue[],
  options: { id?: boolean; version?: boolean } = {},
): value is string {
  if (typeof value !== 'string' || !SAFE_TEXT.test(value)) {
    addIssue(issues, 'UNSAFE_STRING', path, 'Value must be a bounded control-character-free string.');
    return false;
  }
  if (hasSecretSignal(value)) {
    addIssue(issues, 'RAW_SECRET_DETECTED', path, 'Secret-like material is forbidden.');
    return false;
  }
  if (options.id && !SAFE_ID.test(value)) {
    addIssue(issues, 'INVALID_FIELD', path, 'Value must be a bounded safe identifier.');
    return false;
  }
  if (options.version && !SAFE_VERSION.test(value)) {
    addIssue(issues, 'INVALID_FIELD', path, 'Value must be a bounded safe version token.');
    return false;
  }
  return true;
}

function inspectArray(
  value: unknown,
  path: string,
  issues: AssfCapabilityPreflightCandidateBindingIssue[],
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
  issues: AssfCapabilityPreflightCandidateBindingIssue[],
  options: { id?: boolean; allowEmpty?: boolean } = {},
): string[] | null {
  const array = inspectArray(value, path, issues);
  if (!array) return null;
  if (!options.allowEmpty && array.length === 0) {
    addIssue(issues, 'INVALID_FIELD', path, 'Array must be non-empty.');
    return null;
  }
  const output: string[] = [];
  let ok = true;
  array.forEach((item, index) => {
    if (inspectString(item, `${path}[${index}]`, issues, { id: options.id })) {
      output.push(item as string);
    } else {
      ok = false;
    }
  });
  if (!ok) return null;
  return output;
}

function duplicate(values: readonly string[]): boolean {
  return new Set(values).size !== values.length;
}

function isOneOf<T extends string>(value: unknown, allowed: readonly T[]): value is T {
  return typeof value === 'string' && allowed.includes(value as T);
}

function freezeIssues(
  issues: AssfCapabilityPreflightCandidateBindingIssue[],
): readonly AssfCapabilityPreflightCandidateBindingIssue[] {
  return Object.freeze([...issues].sort((left, right) => (
    left.path.localeCompare(right.path)
    || left.code.localeCompare(right.code)
    || left.message.localeCompare(right.message)
  )));
}

function authorityFields() {
  return {
    authorityStatus: 'CANDIDATE_ONLY' as const,
    activationAuthorized: false as const,
    loadingAuthorized: false as const,
    instructionBodyReadAuthorized: false as const,
    executionAuthorized: false as const,
    mutationAuthorized: false as const,
    acquisitionAuthorized: false as const,
    externalAdapterAuthorized: false as const,
    providerCallAuthorized: false as const,
    publicWriteAuthorized: false as const,
    taskAuthorityGranted: false as const,
  };
}

function buildResult(
  bindingStatus: AssfCapabilityPreflightCandidateBindingStatus,
  packageId: string,
  version: string,
  lifecycleStatus: AssfPackageLifecycleStatus | 'invalid',
  candidateState: AssfPackageLifecycleStatus | 'invalid',
  approvalState: AssfCandidateApprovalState | 'invalid',
  uatState: AssfCandidateUatState | 'invalid',
  certificationState: AssfCandidateCertificationState | 'invalid',
  riskCeiling: AssfPackageRiskLevel | 'invalid',
  authorityCeiling: string,
  externalCliMcpDisposition: AssfCliMcpDisposition | 'invalid',
  capabilityBoundary: string,
  routingEligible: boolean,
  taskClasses: readonly string[],
  dependencies: readonly string[],
  conflicts: readonly string[],
  platformCompatibility: readonly string[],
  sourceArtifacts: readonly string[],
  issues: AssfCapabilityPreflightCandidateBindingIssue[],
  evaluatedAt: string,
): AssfCapabilityPreflightCandidateBindingResult {
  return Object.freeze({
    schemaVersion: ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_RESULT_VERSION,
    bindingStatus,
    packageId,
    version,
    lifecycleStatus,
    candidateState,
    approvalState,
    uatState,
    certificationState,
    riskCeiling,
    authorityCeiling,
    externalCliMcpDisposition,
    capabilityBoundary,
    routingEligible,
    taskClasses: Object.freeze([...taskClasses]),
    dependencies: Object.freeze([...dependencies]),
    conflicts: Object.freeze([...conflicts]),
    platformCompatibility: Object.freeze([...platformCompatibility]),
    sourceArtifacts: Object.freeze([...sourceArtifacts]),
    issues: freezeIssues(issues),
    evaluatedAt,
    ...authorityFields(),
  });
}

function rejected(
  issues: AssfCapabilityPreflightCandidateBindingIssue[],
  evaluatedAt: string,
  status: AssfCapabilityPreflightCandidateBindingStatus = 'CANDIDATE_BINDING_REJECTED',
): AssfCapabilityPreflightCandidateBindingResult {
  return buildResult(
    status,
    'invalid',
    'invalid',
    'invalid',
    'invalid',
    'invalid',
    'invalid',
    'invalid',
    'invalid',
    'invalid',
    'invalid',
    'invalid',
    false,
    [],
    [],
    [],
    [],
    [],
    issues,
    evaluatedAt,
  );
}

export function evaluateAssfCapabilityPreflightCandidateBinding(
  input: unknown,
): AssfCapabilityPreflightCandidateBindingResult {
  const issues: AssfCapabilityPreflightCandidateBindingIssue[] = [];
  const envelope = inspectRecord(input, '$', INPUT_KEYS, issues);
  if (!envelope) {
    return rejected(issues, '1970-01-01T00:00:00Z', 'CANDIDATE_BINDING_BLOCKED');
  }

  if (data(envelope, 'schemaVersion') !== ASSF_CAPABILITY_PREFLIGHT_CANDIDATE_BINDING_CONTRACT_VERSION) {
    addIssue(issues, 'INVALID_FIELD', '$.schemaVersion', 'Unsupported candidate-binding input version.');
  }

  let nowValue: string | null = null;
  if (validUtc(data(envelope, 'now'))) {
    nowValue = data(envelope, 'now') as string;
  } else {
    addIssue(issues, 'INVALID_FIELD', '$.now', 'Current time must be ISO-8601 UTC.');
  }
  const evaluatedAt = nowValue ?? '1970-01-01T00:00:00Z';

  let expectedPackageId: string | null = null;
  if (inspectString(data(envelope, 'expectedPackageId'), '$.expectedPackageId', issues, { id: true })) {
    expectedPackageId = data(envelope, 'expectedPackageId') as string;
  }

  const metadataRecord = inspectRecord(data(envelope, 'metadata'), '$.metadata', METADATA_KEYS, issues);
  if (!metadataRecord) {
    return rejected(issues, evaluatedAt, 'CANDIDATE_BINDING_BLOCKED');
  }

  let skillId: string | null = null;
  if (inspectString(data(metadataRecord, 'skillId'), '$.metadata.skillId', issues, { id: true })) {
    skillId = data(metadataRecord, 'skillId') as string;
  }
  let version: string | null = null;
  if (inspectString(data(metadataRecord, 'version'), '$.metadata.version', issues, { version: true })) {
    version = data(metadataRecord, 'version') as string;
  }

  const status = data(metadataRecord, 'status');
  if (!isOneOf(status, LIFECYCLE_STATUSES)) {
    addIssue(issues, 'INVALID_FIELD', '$.metadata.status', 'Unsupported lifecycle status.');
  }
  const candidateState = data(metadataRecord, 'candidateState');
  if (!isOneOf(candidateState, LIFECYCLE_STATUSES)) {
    addIssue(issues, 'INVALID_FIELD', '$.metadata.candidateState', 'Unsupported candidate-state value.');
  }
  const approvalState = data(metadataRecord, 'approvalState');
  if (!isOneOf(approvalState, APPROVAL_STATES)) {
    addIssue(issues, 'INVALID_FIELD', '$.metadata.approvalState', 'Unsupported approval state.');
  }
  const uatState = data(metadataRecord, 'uatState');
  if (!isOneOf(uatState, UAT_STATES)) {
    addIssue(issues, 'INVALID_FIELD', '$.metadata.uatState', 'Unsupported UAT state.');
  }
  const certificationState = data(metadataRecord, 'certificationState');
  if (!isOneOf(certificationState, CERTIFICATION_STATES)) {
    addIssue(issues, 'INVALID_FIELD', '$.metadata.certificationState', 'Unsupported certification state.');
  }
  const riskCeilingValue = data(metadataRecord, 'riskCeiling');
  if (!isOneOf(riskCeilingValue, RISK_LEVELS)) {
    addIssue(issues, 'INVALID_FIELD', '$.metadata.riskCeiling', 'Unsupported risk ceiling.');
  }
  const cliMcpDisposition = data(metadataRecord, 'externalCliMcpDisposition');
  if (!isOneOf(cliMcpDisposition, CLI_MCP_DISPOSITIONS)) {
    addIssue(issues, 'INVALID_FIELD', '$.metadata.externalCliMcpDisposition', 'Unsupported external CLI/MCP disposition.');
  } else if (cliMcpDisposition === 'IMPLEMENTED') {
    addIssue(issues, 'EXTERNAL_ADAPTER_FORBIDDEN', '$.metadata.externalCliMcpDisposition', 'This tranche cannot bind a package that claims an implemented external adapter.');
  }

  let authorityCeiling: string | null = null;
  if (inspectString(data(metadataRecord, 'authorityCeiling'), '$.metadata.authorityCeiling', issues)) {
    authorityCeiling = data(metadataRecord, 'authorityCeiling') as string;
  }
  let capabilityBoundary: string | null = null;
  if (inspectString(data(metadataRecord, 'capabilityBoundary'), '$.metadata.capabilityBoundary', issues)) {
    capabilityBoundary = data(metadataRecord, 'capabilityBoundary') as string;
  }

  const platformCompatibility = inspectStringArray(data(metadataRecord, 'platformCompatibility'), '$.metadata.platformCompatibility', issues, { allowEmpty: false }) ?? [];
  if (duplicate(platformCompatibility)) addIssue(issues, 'DUPLICATE_VALUE', '$.metadata.platformCompatibility', 'Platform entries must be unique.');

  const taskClasses = inspectStringArray(data(metadataRecord, 'taskClasses'), '$.metadata.taskClasses', issues, { allowEmpty: false }) ?? [];
  if (duplicate(taskClasses)) addIssue(issues, 'DUPLICATE_VALUE', '$.metadata.taskClasses', 'Task classes must be unique.');

  const dependencies = inspectStringArray(data(metadataRecord, 'dependencies'), '$.metadata.dependencies', issues, { id: true, allowEmpty: true }) ?? [];
  if (duplicate(dependencies)) addIssue(issues, 'DUPLICATE_VALUE', '$.metadata.dependencies', 'Dependencies must be unique.');

  const conflicts = inspectStringArray(data(metadataRecord, 'conflicts'), '$.metadata.conflicts', issues, { id: true, allowEmpty: true }) ?? [];
  if (duplicate(conflicts)) addIssue(issues, 'DUPLICATE_VALUE', '$.metadata.conflicts', 'Conflicts must be unique.');

  const sourceArtifacts = inspectStringArray(data(metadataRecord, 'sourceArtifacts'), '$.metadata.sourceArtifacts', issues, { allowEmpty: false }) ?? [];
  if (duplicate(sourceArtifacts)) addIssue(issues, 'DUPLICATE_VALUE', '$.metadata.sourceArtifacts', 'Source artifacts must be unique.');

  if (skillId !== null) {
    if (dependencies.includes(skillId)) {
      addIssue(issues, 'SELF_DEPENDENCY', '$.metadata.dependencies', 'A package cannot depend on itself.');
    }
    if (conflicts.includes(skillId)) {
      addIssue(issues, 'INVALID_FIELD', '$.metadata.conflicts', 'A package cannot conflict with itself.');
    }
  }
  const dependencyConflictOverlap = dependencies.filter((dependency) => conflicts.includes(dependency));
  if (dependencyConflictOverlap.length > 0) {
    addIssue(issues, 'DEPENDENCY_CONFLICT_OVERLAP', '$.metadata', 'A package cannot both depend on and conflict with the same identifier.');
  }

  if (expectedPackageId !== null && skillId !== null && expectedPackageId !== skillId) {
    addIssue(issues, 'PACKAGE_ID_MISMATCH', '$.metadata.skillId', 'Metadata package identity does not match the expected package identity.');
  }

  if (isOneOf(status, LIFECYCLE_STATUSES) && isOneOf(candidateState, LIFECYCLE_STATUSES) && status !== candidateState) {
    addIssue(issues, 'LIFECYCLE_CONTRADICTION', '$.metadata.candidateState', 'Lifecycle status and candidate state must agree.');
  }
  if (isOneOf(approvalState, APPROVAL_STATES) && approvalState === 'REJECTED' && isOneOf(status, LIFECYCLE_STATUSES) && !INELIGIBLE_STATUSES.includes(status)) {
    addIssue(issues, 'LIFECYCLE_CONTRADICTION', '$.metadata.approvalState', 'A rejected approval state requires a non-eligible lifecycle status.');
  }
  if (isOneOf(uatState, UAT_STATES) && uatState === 'FAILED' && isOneOf(status, LIFECYCLE_STATUSES) && ROUTABLE_STATUSES.includes(status)) {
    addIssue(issues, 'LIFECYCLE_CONTRADICTION', '$.metadata.uatState', 'A failed UAT state cannot coexist with an approved or active lifecycle status.');
  }
  if (isOneOf(certificationState, CERTIFICATION_STATES) && certificationState === 'FAILED' && status === 'ACTIVE') {
    addIssue(issues, 'LIFECYCLE_CONTRADICTION', '$.metadata.certificationState', 'A failed certification state cannot coexist with an active lifecycle status.');
  }
  if (status === 'ACTIVE' && uatState !== 'PASSED') {
    addIssue(issues, 'UAT_REQUIRED', '$.metadata.uatState', 'An active package requires passed UAT evidence before it can be routing-eligible.');
  }

  let routingEligible = false;
  if (isOneOf(status, LIFECYCLE_STATUSES)) {
    if (INELIGIBLE_STATUSES.includes(status)) {
      addIssue(issues, 'LIFECYCLE_INELIGIBLE', '$.metadata.status', 'A deprecated, retired, or rejected package is not eligible for routing.');
    } else if (
      ROUTABLE_STATUSES.includes(status)
      && approvalState === 'APPROVED'
      && uatState !== 'FAILED'
      && certificationState !== 'FAILED'
    ) {
      if (CERTIFICATION_REQUIRED_STATUSES.includes(status) && certificationState !== 'CERTIFIED') {
        addIssue(issues, 'CERTIFICATION_REQUIRED', '$.metadata.certificationState', 'An active package requires a certified certification state to be routing-eligible.');
      } else {
        routingEligible = true;
      }
    }
  }

  if (
    issues.length !== 0
    || skillId === null
    || version === null
    || authorityCeiling === null
    || capabilityBoundary === null
    || !isOneOf(status, LIFECYCLE_STATUSES)
    || !isOneOf(candidateState, LIFECYCLE_STATUSES)
    || !isOneOf(approvalState, APPROVAL_STATES)
    || !isOneOf(uatState, UAT_STATES)
    || !isOneOf(certificationState, CERTIFICATION_STATES)
    || !isOneOf(riskCeilingValue, RISK_LEVELS)
    || !isOneOf(cliMcpDisposition, CLI_MCP_DISPOSITIONS)
  ) {
    return rejected(issues, evaluatedAt);
  }

  return buildResult(
    'CANDIDATE_BINDING_ACCEPTED',
    skillId,
    version,
    status,
    candidateState,
    approvalState,
    uatState,
    certificationState,
    riskCeilingValue,
    authorityCeiling,
    cliMcpDisposition,
    capabilityBoundary,
    routingEligible,
    taskClasses,
    dependencies,
    conflicts,
    platformCompatibility,
    sourceArtifacts,
    issues,
    evaluatedAt,
  );
}
