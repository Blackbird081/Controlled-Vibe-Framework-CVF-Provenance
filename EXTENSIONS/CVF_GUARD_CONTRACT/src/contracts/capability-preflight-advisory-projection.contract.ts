/** Pure T4/T5/T8/T10 evidence validation and immutable advisory projection. */
import { isProxy } from 'node:util/types';
import { CAPABILITY_ROUTE_DECISION_VERSION } from './capability-route-readiness.contract';
import type { CapabilityReadinessState, CapabilityRouteStage } from './capability-route-readiness.contract';
import { CAPABILITY_READINESS_DECISION_VERSION } from './capability-route-readiness.contract';
import { CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION } from './capability-bootstrap-approval-evidence.contract';
import { CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION } from './capability-environment-snapshot-evidence.contract';
import type { CapabilityEnvironmentSnapshotEvidenceStatus } from './capability-environment-snapshot-evidence.contract';
import { CAPABILITY_CASE_EVIDENCE_PROJECTION_CONTRACT_VERSION } from './capability-case-evidence-projection.contract';
import type { FindingVerificationState, PathStepKind, ProjectionStalenessState } from './capability-case-evidence-projection.contract';
import {
  CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_CONTRACT_VERSION,
  CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_RESULT_VERSION,
} from './capability-preflight-advisory-projection.types';
import type {
  CapabilityAdvisoryApprovalBoundaryView,
  CapabilityAdvisoryEvidenceView,
  CapabilityAdvisoryReadinessView,
  CapabilityAdvisoryRouteView,
  CapabilityPreflightAdvisoryProjectionIssue,
  CapabilityPreflightAdvisoryProjectionIssueCode,
  CapabilityPreflightAdvisoryProjectionResult,
  CapabilityPreflightAdvisoryProjectionStatus,
} from './capability-preflight-advisory-projection.types';

export * from './capability-preflight-advisory-projection.types';

type PlainRecord = Record<string, unknown>;

const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const SHA256 = /^[a-f0-9]{64}$/;
const SAFE_TEXT = /^[^\x00-\x1f\x7f]{1,1024}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;
const SECRET_SIGNAL = /(?:\b(?:api[_-]?key|password|token|secret|credential|cookie)\b\s*[=:]\s*\S+|\bbearer\s+\S+|-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----)/i;
const MAX_ITEMS = 64;
const MAX_STEPS = 64;
const MAX_EVIDENCE_AGE_SECONDS = 86400;

const ROUTE_STAGES: readonly CapabilityRouteStage[] = ['FAST_ROUTE', 'FULL_RESOLUTION_REQUIRED', 'AMBIGUOUS_ROUTE', 'NO_CANDIDATE'];
const READINESS_STATES: readonly CapabilityReadinessState[] = [
  'READY', 'READY_WITH_EXISTING_APPROVAL', 'BOOTSTRAP_REQUIRED', 'APPROVAL_REQUIRED', 'BLOCKED_POLICY', 'BLOCKED_PROVENANCE',
  'BLOCKED_INTEGRITY', 'BLOCKED_COMPATIBILITY', 'BLOCKED_CREDENTIAL', 'BLOCKED_NETWORK', 'BLOCKED_SANDBOX', 'STALE_SNAPSHOT', 'AMBIGUOUS_ROUTE', 'UNKNOWN',
];
const BLOCKED_READINESS_STATES: readonly CapabilityReadinessState[] = [
  'BLOCKED_POLICY', 'BLOCKED_PROVENANCE', 'BLOCKED_INTEGRITY', 'BLOCKED_COMPATIBILITY', 'BLOCKED_CREDENTIAL',
  'BLOCKED_NETWORK', 'BLOCKED_SANDBOX', 'STALE_SNAPSHOT', 'AMBIGUOUS_ROUTE', 'UNKNOWN',
];
const VERIFICATION_STATES: readonly FindingVerificationState[] = ['VERIFIED', 'UNVERIFIED', 'INCOMPLETE', 'BLOCKED'];
const STEP_KINDS: readonly PathStepKind[] = ['DEMONSTRATED', 'INFERRED'];

const INPUT_KEYS = ['schemaVersion', 'route', 'readiness', 'environment', 'approval', 'caseEvidence', 'now'] as const;
const ROUTE_KEYS = [
  'schemaVersion', 'routeDecisionId', 'candidateSetId', 'requestId', 'workspaceId', 'stage', 'primary', 'supporting', 'rejected',
  'fallbacks', 'confidence', 'ambiguityReasons', 'environmentSnapshotRefs', 'authorityStatus', 'executionAuthorized', 'generatedAt', 'issues',
] as const;
const ROUTE_PRIMARY_KEYS = ['capabilityId', 'packageId', 'packageVersion'] as const;
const ROUTE_REJECTED_KEYS = ['capabilityId', 'reasonCodes'] as const;
const ROUTE_FALLBACK_KEYS = ['capabilityId', 'activationCondition'] as const;
const ROUTE_ISSUE_KEYS = ['code', 'path', 'message'] as const;
const READINESS_KEYS = [
  'schemaVersion', 'readinessDecisionId', 'routeDecisionId', 'snapshotId', 'state', 'missingDependencies', 'approvalRequirements',
  'blockingReasons', 'evidenceRefs', 'nextSafeAction', 'evaluatedAt', 'authorityStatus', 'executionAuthorized',
] as const;
const ENVIRONMENT_KEYS = [
  'schemaVersion', 'status', 'routeDecisionId', 'snapshotId', 'workspaceId',
  'requiredDependencies', 'availableDependencies', 'blockingReasons', 'issues',
  'readiness', 'evaluatedAt', 'authorityStatus', 'snapshotCollected',
  'snapshotPersisted', 'environmentReadAuthorized', 'executionAuthorized',
  'acquisitionAuthorized', 'mutationAuthorized', 'refreshAuthorized',
  'taskAuthorityGranted', 'networkAuthorized',
] as const;
const ENVIRONMENT_ISSUE_KEYS = ['code', 'path', 'message'] as const;
const APPROVAL_RESULT_REQUIRED_KEYS = [
  'schemaVersion', 'disposition', 'replayCheckRequired', 'approvalIssued', 'executionAuthorized',
  'acquisitionAuthorized', 'mutationAuthorized', 'taskAuthorityGranted', 'networkAuthorized', 'issues',
] as const;
const APPROVAL_RESULT_OPTIONAL_KEYS = ['planId', 'planDigest', 'approvalId', 'workspaceId', 'actorId', 'workOrderId'] as const;
const APPROVAL_ISSUE_KEYS = ['code', 'path', 'message'] as const;
const CASE_EVIDENCE_KEYS = [
  'schemaVersion', 'caseProjectionVersion', 'domainEvidenceProjectionVersion', 'authorityNotice',
  'authorityMutation', 'caseId', 'requestId', 'workspaceId', 'workOrderId', 'projectionId',
  'sourceRefs', 'staleness', 'currentDisposition', 'evidence', 'findings', 'paths',
  'projectionDigest', 'generatedAt', 'issues',
] as const;
const CASE_EVIDENCE_ITEM_KEYS = ['evidenceId', 'sourceRef', 'observation', 'observedAt', 'digest', 'reproductionBoundary'] as const;
const CASE_FINDING_KEYS = ['findingId', 'claim', 'severity', 'confidence', 'verificationState', 'evidenceRefs', 'remediation'] as const;
const CASE_PATH_KEYS = ['pathId', 'steps'] as const;
const CASE_PATH_STEP_KEYS = ['kind', 'description', 'evidenceRef'] as const;
const CASE_ISSUE_KEYS = ['code', 'path', 'message'] as const;

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

function hasSecretSignal(value: string): boolean { return SECRET_SIGNAL.test(value); }

function addIssue(issues: CapabilityPreflightAdvisoryProjectionIssue[], code: CapabilityPreflightAdvisoryProjectionIssueCode, path: string, message: string): void {
  issues.push(Object.freeze({ code, path, message }));
}

function inspectRecord(value: unknown, path: string, required: readonly string[], issues: CapabilityPreflightAdvisoryProjectionIssue[], optional: readonly string[] = []): PlainRecord | null {
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

function denseArray(value: unknown): readonly unknown[] | null {
  try {
    if (!Array.isArray(value) || isProxy(value)) return null;
  } catch {
    return null;
  }
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

function inspectString(value: unknown, path: string, issues: CapabilityPreflightAdvisoryProjectionIssue[], options: { id?: boolean; nullable?: boolean } = {}): value is string | null {
  if (options.nullable && value === null) return true;
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
  return true;
}

function inspectArray(value: unknown, path: string, issues: CapabilityPreflightAdvisoryProjectionIssue[], limit = MAX_ITEMS): readonly unknown[] | null {
  try {
    if (Array.isArray(value) && !isProxy(value)) {
      const lengthDescriptor = Object.getOwnPropertyDescriptor(value, 'length');
      if (lengthDescriptor && 'value' in lengthDescriptor
        && typeof lengthDescriptor.value === 'number' && lengthDescriptor.value > limit) {
        addIssue(issues, 'UNBOUNDED_COLLECTION', path, `Array exceeds the ${limit}-item limit.`);
        return null;
      }
    }
  } catch {
    // denseArray records the hostile/revoked shape below without invoking it.
  }
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

function inspectStringArray(value: unknown, path: string, issues: CapabilityPreflightAdvisoryProjectionIssue[], options: { id?: boolean; limit?: number } = {}): string[] | null {
  const array = inspectArray(value, path, issues, options.limit ?? MAX_ITEMS);
  if (!array) return null;
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

function duplicate(values: readonly string[]): boolean { return new Set(values).size !== values.length; }
function isOneOf<T extends string>(value: unknown, allowed: readonly T[]): value is T { return typeof value === 'string' && allowed.includes(value as T); }

function freezeIssues(issues: CapabilityPreflightAdvisoryProjectionIssue[]): readonly CapabilityPreflightAdvisoryProjectionIssue[] {
  return Object.freeze([...issues].sort((left, right) => (
    left.path.localeCompare(right.path)
    || left.code.localeCompare(right.code)
    || left.message.localeCompare(right.message)
  )));
}

function authorityFields() {
  return {
    approvalAuthorityGranted: false as const, taskAuthorityGranted: false as const,
    activationAuthorityGranted: false as const, executionAuthorityGranted: false as const,
    mutationAuthorityGranted: false as const,
    actionInvocationAuthorized: false as const,
  };
}

interface ValidatedRoute {
  readonly routeDecisionId: string; readonly workspaceId: string; readonly stage: CapabilityRouteStage;
  readonly primary: Readonly<{ capabilityId: string; packageId: string; packageVersion: string }> | null;
  readonly supporting: readonly string[];
  readonly rejected: readonly Readonly<{ capabilityId: string; reasonCodes: readonly string[] }>[];
  readonly confidence: number; readonly ambiguityReasons: readonly string[];
  readonly environmentSnapshotRefs: readonly string[]; readonly generatedAt: string; readonly hasIssues: boolean;
}

function validateRoute(value: unknown, issues: CapabilityPreflightAdvisoryProjectionIssue[]): ValidatedRoute | null {
  const path = '$.route';
  const record = inspectRecord(value, path, ROUTE_KEYS, issues);
  if (!record) return null;

  if (data(record, 'schemaVersion') !== CAPABILITY_ROUTE_DECISION_VERSION) {
    addIssue(issues, 'INVALID_FIELD', `${path}.schemaVersion`, 'Unsupported route decision schema.');
  }
  if (data(record, 'authorityStatus') !== 'CANDIDATE_ONLY' || data(record, 'executionAuthorized') !== false) {
    addIssue(issues, 'INVALID_FIELD', path, 'Route authority fields must remain CANDIDATE_ONLY/false.');
  }
  const routeDecisionId = inspectString(data(record, 'routeDecisionId'), `${path}.routeDecisionId`, issues, { id: true }) ? data(record, 'routeDecisionId') as string : null;
  inspectString(data(record, 'candidateSetId'), `${path}.candidateSetId`, issues, { id: true });
  inspectString(data(record, 'requestId'), `${path}.requestId`, issues, { id: true });
  const workspaceId = inspectString(data(record, 'workspaceId'), `${path}.workspaceId`, issues, { id: true }) ? data(record, 'workspaceId') as string : null;

  const stage = data(record, 'stage');
  if (!isOneOf(stage, ROUTE_STAGES)) addIssue(issues, 'INVALID_FIELD', `${path}.stage`, 'Unsupported route stage.');

  const primaryValue = data(record, 'primary');
  let primary: Readonly<{ capabilityId: string; packageId: string; packageVersion: string }> | null = null;
  if (primaryValue !== undefined) {
    const primaryRecord = inspectRecord(primaryValue, `${path}.primary`, ROUTE_PRIMARY_KEYS, issues);
    if (primaryRecord) {
      const capabilityId = inspectString(data(primaryRecord, 'capabilityId'), `${path}.primary.capabilityId`, issues, { id: true }) ? data(primaryRecord, 'capabilityId') as string : null;
      const packageId = inspectString(data(primaryRecord, 'packageId'), `${path}.primary.packageId`, issues, { id: true }) ? data(primaryRecord, 'packageId') as string : null;
      const packageVersion = inspectString(data(primaryRecord, 'packageVersion'), `${path}.primary.packageVersion`, issues, { id: true }) ? data(primaryRecord, 'packageVersion') as string : null;
      if (capabilityId !== null && packageId !== null && packageVersion !== null) {
        primary = Object.freeze({ capabilityId, packageId, packageVersion });
      }
    }
  }

  const supporting = inspectStringArray(data(record, 'supporting'), `${path}.supporting`, issues, { id: true }) ?? [];
  if (duplicate(supporting)) addIssue(issues, 'DUPLICATE_VALUE', `${path}.supporting`, 'Supporting dependency identifiers must be unique.');

  const rejectedArray = inspectArray(data(record, 'rejected'), `${path}.rejected`, issues) ?? [];
  const rejected: Array<Readonly<{ capabilityId: string; reasonCodes: readonly string[] }>> = [];
  rejectedArray.forEach((item, index) => {
    const itemPath = `${path}.rejected[${index}]`;
    const itemRecord = inspectRecord(item, itemPath, ROUTE_REJECTED_KEYS, issues);
    if (!itemRecord) return;
    const capabilityId = inspectString(data(itemRecord, 'capabilityId'), `${itemPath}.capabilityId`, issues, { id: true }) ? data(itemRecord, 'capabilityId') as string : null;
    const reasonCodes = inspectStringArray(data(itemRecord, 'reasonCodes'), `${itemPath}.reasonCodes`, issues, { id: true });
    if (capabilityId !== null && reasonCodes !== null) {
      rejected.push(Object.freeze({ capabilityId, reasonCodes: Object.freeze(reasonCodes) }));
    }
  });

  const fallbacksArray = inspectArray(data(record, 'fallbacks'), `${path}.fallbacks`, issues) ?? [];
  fallbacksArray.forEach((item, index) => {
    const itemPath = `${path}.fallbacks[${index}]`;
    const itemRecord = inspectRecord(item, itemPath, ROUTE_FALLBACK_KEYS, issues);
    if (itemRecord) {
      inspectString(data(itemRecord, 'capabilityId'), `${itemPath}.capabilityId`, issues, { id: true });
      inspectString(data(itemRecord, 'activationCondition'), `${itemPath}.activationCondition`, issues);
    }
  });

  const confidenceValue = data(record, 'confidence');
  const confidence = typeof confidenceValue === 'number' && Number.isFinite(confidenceValue) && confidenceValue >= 0 && confidenceValue <= 1
    ? confidenceValue
    : null;
  if (confidence === null) addIssue(issues, 'INVALID_FIELD', `${path}.confidence`, 'Confidence must be a finite number between zero and one.');

  const ambiguityReasons = inspectStringArray(data(record, 'ambiguityReasons'), `${path}.ambiguityReasons`, issues) ?? [];
  const environmentSnapshotRefs = inspectStringArray(data(record, 'environmentSnapshotRefs'), `${path}.environmentSnapshotRefs`, issues, { id: true }) ?? [];
  if (duplicate(environmentSnapshotRefs)) addIssue(issues, 'DUPLICATE_VALUE', `${path}.environmentSnapshotRefs`, 'Environment snapshot references must be unique.');

  let generatedAt: string | null = null;
  if (validUtc(data(record, 'generatedAt'))) {
    generatedAt = data(record, 'generatedAt') as string;
  } else {
    addIssue(issues, 'INVALID_FIELD', `${path}.generatedAt`, 'Route generation time must be ISO-8601 UTC.');
  }

  const routeIssuesArray = inspectArray(data(record, 'issues'), `${path}.issues`, issues) ?? [];
  routeIssuesArray.forEach((item, index) => {
    const itemPath = `${path}.issues[${index}]`;
    const itemRecord = inspectRecord(item, itemPath, ROUTE_ISSUE_KEYS, issues);
    if (itemRecord) for (const key of ['code', 'path', 'message']) inspectString(data(itemRecord, key), `${itemPath}.${key}`, issues);
  });

  if (routeDecisionId === null || workspaceId === null || stage === undefined || confidence === null || generatedAt === null) return null;

  return {
    routeDecisionId, workspaceId, stage: stage as CapabilityRouteStage, primary, supporting: Object.freeze(supporting),
    rejected: Object.freeze(rejected), confidence, ambiguityReasons: Object.freeze(ambiguityReasons),
    environmentSnapshotRefs: Object.freeze(environmentSnapshotRefs), generatedAt, hasIssues: routeIssuesArray.length > 0,
  };
}

interface ValidatedReadiness {
  readonly readinessDecisionId: string;
  readonly routeDecisionId: string;
  readonly snapshotId: string;
  readonly state: CapabilityReadinessState;
  readonly missingDependencies: readonly string[];
  readonly blockingReasons: readonly string[];
  readonly evidenceRefs: readonly string[];
  readonly nextSafeAction: string;
  readonly evaluatedAt: string;
}

function validateReadiness(
  value: unknown,
  issues: CapabilityPreflightAdvisoryProjectionIssue[],
  path = '$.readiness',
): ValidatedReadiness | null {
  const record = inspectRecord(value, path, READINESS_KEYS, issues);
  if (!record) return null;

  if (data(record, 'schemaVersion') !== CAPABILITY_READINESS_DECISION_VERSION) {
    addIssue(issues, 'INVALID_FIELD', `${path}.schemaVersion`, 'Unsupported readiness decision schema.');
  }
  if (data(record, 'authorityStatus') !== 'EVIDENCE_ONLY' || data(record, 'executionAuthorized') !== false) {
    addIssue(issues, 'INVALID_FIELD', path, 'Readiness authority fields must remain EVIDENCE_ONLY/false.');
  }

  const readinessDecisionId = inspectString(data(record, 'readinessDecisionId'), `${path}.readinessDecisionId`, issues, { id: true }) ? data(record, 'readinessDecisionId') as string : null;
  const routeDecisionId = inspectString(data(record, 'routeDecisionId'), `${path}.routeDecisionId`, issues, { id: true }) ? data(record, 'routeDecisionId') as string : null;
  const snapshotId = inspectString(data(record, 'snapshotId'), `${path}.snapshotId`, issues, { id: true }) ? data(record, 'snapshotId') as string : null;

  const state = data(record, 'state');
  if (!isOneOf(state, READINESS_STATES)) addIssue(issues, 'INVALID_FIELD', `${path}.state`, 'Unsupported readiness state.');

  const missingDependencies = inspectStringArray(data(record, 'missingDependencies'), `${path}.missingDependencies`, issues, { id: true }) ?? [];
  const approvalRequirements = inspectStringArray(data(record, 'approvalRequirements'), `${path}.approvalRequirements`, issues) ?? [];
  void approvalRequirements;
  const blockingReasons = inspectStringArray(data(record, 'blockingReasons'), `${path}.blockingReasons`, issues) ?? [];
  const evidenceRefs = inspectStringArray(data(record, 'evidenceRefs'), `${path}.evidenceRefs`, issues, { id: true }) ?? [];
  if (duplicate(evidenceRefs)) addIssue(issues, 'DUPLICATE_VALUE', `${path}.evidenceRefs`, 'Evidence references must be unique.');

  const nextSafeAction = inspectString(data(record, 'nextSafeAction'), `${path}.nextSafeAction`, issues) ? data(record, 'nextSafeAction') as string : null;

  let evaluatedAt: string | null = null;
  if (validUtc(data(record, 'evaluatedAt'))) {
    evaluatedAt = data(record, 'evaluatedAt') as string;
  } else {
    addIssue(issues, 'INVALID_FIELD', `${path}.evaluatedAt`, 'Readiness evaluation time must be ISO-8601 UTC.');
  }

  if (
    readinessDecisionId === null || routeDecisionId === null || snapshotId === null
    || state === undefined || nextSafeAction === null || evaluatedAt === null
  ) return null;

  return {
    readinessDecisionId,
    routeDecisionId,
    snapshotId,
    state: state as CapabilityReadinessState,
    missingDependencies: Object.freeze(missingDependencies),
    blockingReasons: Object.freeze(blockingReasons),
    evidenceRefs: Object.freeze(evidenceRefs),
    nextSafeAction,
    evaluatedAt,
  };
}

interface ValidatedEnvironment {
  readonly status: CapabilityEnvironmentSnapshotEvidenceStatus;
  readonly routeDecisionId: string;
  readonly snapshotId: string;
  readonly workspaceId: string;
  readonly requiredDependencies: readonly string[];
  readonly availableDependencies: readonly string[];
  readonly blockingReasons: readonly string[];
  readonly readiness: ValidatedReadiness;
  readonly evaluatedAt: string;
}

function validateEnvironment(
  value: unknown,
  issues: CapabilityPreflightAdvisoryProjectionIssue[],
): ValidatedEnvironment | null {
  const path = '$.environment';
  const record = inspectRecord(value, path, ENVIRONMENT_KEYS, issues);
  if (!record) return null;
  if (data(record, 'schemaVersion') !== CAPABILITY_ENVIRONMENT_SNAPSHOT_EVIDENCE_RESULT_VERSION) {
    addIssue(issues, 'INVALID_FIELD', `${path}.schemaVersion`, 'Unsupported environment-evidence result schema.');
  }
  const status = data(record, 'status');
  if (!isOneOf(status, ['VALIDATED_READY_EVIDENCE', 'VALIDATED_BLOCKED_EVIDENCE', 'REJECTED'] as const)) {
    addIssue(issues, 'INVALID_FIELD', `${path}.status`, 'Unsupported environment-evidence status.');
  }
  const routeDecisionId = inspectString(data(record, 'routeDecisionId'), `${path}.routeDecisionId`, issues, { id: true })
    ? data(record, 'routeDecisionId') as string : null;
  const snapshotId = inspectString(data(record, 'snapshotId'), `${path}.snapshotId`, issues, { id: true })
    ? data(record, 'snapshotId') as string : null;
  const workspaceId = inspectString(data(record, 'workspaceId'), `${path}.workspaceId`, issues, { id: true })
    ? data(record, 'workspaceId') as string : null;
  const requiredDependencies = inspectStringArray(data(record, 'requiredDependencies'), `${path}.requiredDependencies`, issues, { id: true }) ?? [];
  const availableDependencies = inspectStringArray(data(record, 'availableDependencies'), `${path}.availableDependencies`, issues, { id: true }) ?? [];
  const blockingReasons = inspectStringArray(data(record, 'blockingReasons'), `${path}.blockingReasons`, issues) ?? [];
  if (duplicate(requiredDependencies)) addIssue(issues, 'DUPLICATE_VALUE', `${path}.requiredDependencies`, 'Required dependencies must be unique.');
  if (duplicate(availableDependencies)) addIssue(issues, 'DUPLICATE_VALUE', `${path}.availableDependencies`, 'Available dependencies must be unique.');
  if (availableDependencies.some((dependency) => !requiredDependencies.includes(dependency))) {
    addIssue(issues, 'READINESS_ENVIRONMENT_BINDING_MISMATCH', `${path}.availableDependencies`, 'Available dependencies must be a subset of required dependencies.');
  }
  const environmentIssues = inspectArray(data(record, 'issues'), `${path}.issues`, issues) ?? [];
  environmentIssues.forEach((item, index) => {
    const itemPath = `${path}.issues[${index}]`;
    const itemRecord = inspectRecord(item, itemPath, ENVIRONMENT_ISSUE_KEYS, issues);
    if (itemRecord) for (const key of ENVIRONMENT_ISSUE_KEYS) inspectString(data(itemRecord, key), `${itemPath}.${key}`, issues);
  });
  if (data(record, 'authorityStatus') !== 'EVIDENCE_ONLY') {
    addIssue(issues, 'INVALID_FIELD', `${path}.authorityStatus`, 'Environment authority status must remain EVIDENCE_ONLY.');
  }
  for (const field of [
    'snapshotCollected', 'snapshotPersisted', 'environmentReadAuthorized',
    'executionAuthorized', 'acquisitionAuthorized', 'mutationAuthorized',
    'refreshAuthorized', 'taskAuthorityGranted', 'networkAuthorized',
  ] as const) {
    if (data(record, field) !== false) {
      addIssue(issues, 'INVALID_FIELD', `${path}.${field}`, `Environment field ${field} must remain literal false.`);
    }
  }
  const evaluatedAt = validUtc(data(record, 'evaluatedAt')) ? data(record, 'evaluatedAt') as string : null;
  if (evaluatedAt === null) addIssue(issues, 'INVALID_FIELD', `${path}.evaluatedAt`, 'Environment evaluation time must be ISO-8601 UTC.');
  const nestedReadinessValue = data(record, 'readiness');
  if (status === 'REJECTED') {
    if (nestedReadinessValue !== null || environmentIssues.length === 0) {
      addIssue(issues, 'ENVIRONMENT_EVIDENCE_REJECTED', path, 'Rejected environment evidence must carry null readiness and at least one issue.');
    } else {
      addIssue(issues, 'ENVIRONMENT_EVIDENCE_REJECTED', path, 'Rejected environment evidence cannot support an advisory projection.');
    }
    return null;
  }
  if (environmentIssues.length > 0) {
    addIssue(issues, 'READINESS_ENVIRONMENT_BINDING_MISMATCH', `${path}.issues`, 'Validated environment evidence must not carry issues.');
  }
  const nestedReadiness = validateReadiness(nestedReadinessValue, issues, `${path}.readiness`);
  if (!isOneOf(status, ['VALIDATED_READY_EVIDENCE', 'VALIDATED_BLOCKED_EVIDENCE'] as const)
    || routeDecisionId === null || snapshotId === null || workspaceId === null
    || evaluatedAt === null || nestedReadiness === null) return null;
  return {
    status,
    routeDecisionId,
    snapshotId,
    workspaceId,
    requiredDependencies: Object.freeze(requiredDependencies),
    availableDependencies: Object.freeze(availableDependencies),
    blockingReasons: Object.freeze(blockingReasons),
    readiness: nestedReadiness,
    evaluatedAt,
  };
}

interface ValidatedApproval {
  readonly disposition: 'VALIDATED_EVIDENCE' | 'REJECTED';
  readonly planId: string | null;
  readonly planDigest: string | null;
  readonly approvalId: string | null;
  readonly workspaceId: string | null;
}

function validateApproval(value: unknown, issues: CapabilityPreflightAdvisoryProjectionIssue[]): ValidatedApproval | null | undefined {
  if (value === null) return null;
  const path = '$.approval';
  const record = inspectRecord(value, path, APPROVAL_RESULT_REQUIRED_KEYS, issues, APPROVAL_RESULT_OPTIONAL_KEYS);
  if (!record) return undefined;

  if (data(record, 'schemaVersion') !== CAPABILITY_BOOTSTRAP_APPROVAL_EVIDENCE_RESULT_VERSION) {
    addIssue(issues, 'INVALID_FIELD', `${path}.schemaVersion`, 'Unsupported approval evidence result schema.');
  }
  const disposition = data(record, 'disposition');
  if (disposition !== 'VALIDATED_EVIDENCE' && disposition !== 'REJECTED') {
    addIssue(issues, 'INVALID_FIELD', `${path}.disposition`, 'Unsupported approval disposition.');
  }
  for (const field of ['replayCheckRequired', 'approvalIssued', 'executionAuthorized', 'acquisitionAuthorized', 'mutationAuthorized', 'taskAuthorityGranted', 'networkAuthorized'] as const) {
    const expected = field === 'replayCheckRequired';
    if (data(record, field) !== expected) {
      addIssue(issues, 'APPROVAL_BINDING_CONTRADICTION', `${path}.${field}`, `Approval evidence field ${field} must remain literal ${expected}.`);
    }
  }
  const approvalIssuesArray = inspectArray(data(record, 'issues'), `${path}.issues`, issues) ?? [];
  approvalIssuesArray.forEach((item, index) => {
    const itemPath = `${path}.issues[${index}]`;
    const itemRecord = inspectRecord(item, itemPath, APPROVAL_ISSUE_KEYS, issues);
    if (itemRecord) for (const key of ['code', 'path', 'message']) inspectString(data(itemRecord, key), `${itemPath}.${key}`, issues);
  });

  let planId: string | null = null;
  let planDigest: string | null = null;
  let approvalId: string | null = null;
  let workspaceId: string | null = null;
  const identityKeys = ['planId', 'planDigest', 'approvalId', 'workspaceId', 'actorId', 'workOrderId'] as const;
  const presentIdentityKeys = identityKeys.filter((key) => Object.prototype.hasOwnProperty.call(record, key));
  if (disposition === 'VALIDATED_EVIDENCE') {
    if (presentIdentityKeys.length !== identityKeys.length) {
      addIssue(issues, 'APPROVAL_BINDING_CONTRADICTION', path, 'A validated approval result must carry all identity fields.');
    }
    if (inspectString(data(record, 'planId'), `${path}.planId`, issues, { id: true })) planId = data(record, 'planId') as string;
    if (inspectString(data(record, 'planDigest'), `${path}.planDigest`, issues, { id: true })) {
      planDigest = data(record, 'planDigest') as string;
      if (!SHA256.test(planDigest)) addIssue(issues, 'APPROVAL_BINDING_CONTRADICTION', `${path}.planDigest`, 'Validated approval plan digest must be a lowercase SHA-256 value.');
    }
    if (inspectString(data(record, 'approvalId'), `${path}.approvalId`, issues, { id: true })) approvalId = data(record, 'approvalId') as string;
    if (inspectString(data(record, 'workspaceId'), `${path}.workspaceId`, issues, { id: true })) workspaceId = data(record, 'workspaceId') as string;
    inspectString(data(record, 'actorId'), `${path}.actorId`, issues, { id: true });
    const workOrderId = data(record, 'workOrderId');
    if (workOrderId !== null) inspectString(workOrderId, `${path}.workOrderId`, issues, { id: true });
    if (approvalIssuesArray.length > 0) {
      addIssue(issues, 'APPROVAL_BINDING_CONTRADICTION', path, 'A validated approval result must not carry issues.');
    }
  } else if (disposition === 'REJECTED') {
    if (presentIdentityKeys.length > 0) {
      addIssue(issues, 'APPROVAL_BINDING_CONTRADICTION', path, 'A rejected approval result must not carry identity fields.');
    }
  }

  if (disposition === undefined) return undefined;
  return { disposition: disposition as 'VALIDATED_EVIDENCE' | 'REJECTED', planId, planDigest, approvalId, workspaceId };
}

interface ValidatedCaseEvidence {
  readonly caseId: string;
  readonly workspaceId: string;
  readonly staleness: ProjectionStalenessState;
  readonly hasIssues: boolean;
  readonly findings: ReadonlyArray<{
    readonly findingId: string;
    readonly claim: string;
    readonly verificationState: FindingVerificationState;
    readonly evidenceRefs: readonly string[];
  }>;
  readonly paths: ReadonlyArray<{
    readonly pathId: string;
    readonly steps: ReadonlyArray<{ readonly kind: PathStepKind; readonly description: string; readonly evidenceRef: string | null }>;
  }>;
}

function validateCaseEvidence(value: unknown, issues: CapabilityPreflightAdvisoryProjectionIssue[]): ValidatedCaseEvidence | null | undefined {
  if (value === null) return null;
  const path = '$.caseEvidence';
  const record = inspectRecord(value, path, CASE_EVIDENCE_KEYS, issues);
  if (!record) return undefined;

  if (data(record, 'schemaVersion') !== CAPABILITY_CASE_EVIDENCE_PROJECTION_CONTRACT_VERSION) {
    addIssue(issues, 'INVALID_FIELD', `${path}.schemaVersion`, 'Unsupported case-evidence projection schema.');
  }
  if (data(record, 'authorityNotice') !== 'PROJECTION_ONLY' || data(record, 'authorityMutation') !== false) {
    addIssue(issues, 'CASE_EVIDENCE_BINDING_CONTRADICTION', path, 'Case-evidence authority fields must remain PROJECTION_ONLY/false.');
  }

  const caseId = inspectString(data(record, 'caseId'), `${path}.caseId`, issues, { id: true }) ? data(record, 'caseId') as string : null;
  inspectString(data(record, 'requestId'), `${path}.requestId`, issues, { id: true });
  const workspaceId = inspectString(data(record, 'workspaceId'), `${path}.workspaceId`, issues, { id: true }) ? data(record, 'workspaceId') as string : null;
  const workOrderId = data(record, 'workOrderId');
  if (workOrderId !== null) inspectString(workOrderId, `${path}.workOrderId`, issues, { id: true });
  inspectString(data(record, 'projectionId'), `${path}.projectionId`, issues, { id: true });
  inspectStringArray(data(record, 'sourceRefs'), `${path}.sourceRefs`, issues, { id: true });

  const staleness = data(record, 'staleness');
  if (typeof staleness !== 'string' || !['CURRENT', 'STALE', 'INVALID'].includes(staleness)) {
    addIssue(issues, 'INVALID_FIELD', `${path}.staleness`, 'Unsupported staleness state.');
  }
  inspectString(data(record, 'currentDisposition'), `${path}.currentDisposition`, issues);

  const evidenceArray = inspectArray(data(record, 'evidence'), `${path}.evidence`, issues, 256) ?? [];
  const evidenceIds = new Set<string>();
  evidenceArray.forEach((item, index) => {
    const itemPath = `${path}.evidence[${index}]`;
    const itemRecord = inspectRecord(item, itemPath, CASE_EVIDENCE_ITEM_KEYS, issues);
    if (!itemRecord) return;
    if (inspectString(data(itemRecord, 'evidenceId'), `${itemPath}.evidenceId`, issues, { id: true })) {
      const evidenceId = data(itemRecord, 'evidenceId') as string;
      if (evidenceIds.has(evidenceId)) addIssue(issues, 'DUPLICATE_VALUE', `${itemPath}.evidenceId`, 'Evidence identifiers must be unique.');
      evidenceIds.add(evidenceId);
    }
    inspectString(data(itemRecord, 'sourceRef'), `${itemPath}.sourceRef`, issues);
    inspectString(data(itemRecord, 'observation'), `${itemPath}.observation`, issues);
    if (!validUtc(data(itemRecord, 'observedAt'))) addIssue(issues, 'INVALID_FIELD', `${itemPath}.observedAt`, 'Observation time must be ISO-8601 UTC.');
    const digest = data(itemRecord, 'digest');
    if (digest !== null) inspectString(digest, `${itemPath}.digest`, issues);
    const reproductionBoundary = data(itemRecord, 'reproductionBoundary');
    if (reproductionBoundary !== null) inspectString(reproductionBoundary, `${itemPath}.reproductionBoundary`, issues);
  });

  const findingsArray = inspectArray(data(record, 'findings'), `${path}.findings`, issues, 256) ?? [];
  const findings: ValidatedCaseEvidence['findings'][number][] = [];
  const seenFindingIds = new Set<string>();
  findingsArray.forEach((item, index) => {
    const itemPath = `${path}.findings[${index}]`;
    const itemRecord = inspectRecord(item, itemPath, CASE_FINDING_KEYS, issues);
    if (!itemRecord) return;
    const findingId = inspectString(data(itemRecord, 'findingId'), `${itemPath}.findingId`, issues, { id: true }) ? data(itemRecord, 'findingId') as string : null;
    const claim = inspectString(data(itemRecord, 'claim'), `${itemPath}.claim`, issues) ? data(itemRecord, 'claim') as string : null;
    if (!['INFO', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL'].includes(data(itemRecord, 'severity') as string)) {
      addIssue(issues, 'INVALID_FIELD', `${itemPath}.severity`, 'Unsupported finding severity.');
    }
    const confidenceValue = data(itemRecord, 'confidence');
    if (typeof confidenceValue !== 'number' || !Number.isFinite(confidenceValue) || confidenceValue < 0 || confidenceValue > 1) {
      addIssue(issues, 'INVALID_FIELD', `${itemPath}.confidence`, 'Finding confidence must be a finite number between zero and one.');
    }
    const verificationState = data(itemRecord, 'verificationState');
    if (!isOneOf(verificationState, VERIFICATION_STATES)) {
      addIssue(issues, 'INVALID_FIELD', `${itemPath}.verificationState`, 'Unsupported finding verification state.');
    }
    const evidenceRefs = inspectStringArray(data(itemRecord, 'evidenceRefs'), `${itemPath}.evidenceRefs`, issues, { id: true }) ?? [];
    evidenceRefs.forEach((evidenceRef) => {
      if (!evidenceIds.has(evidenceRef)) addIssue(issues, 'CASE_EVIDENCE_BINDING_CONTRADICTION', `${itemPath}.evidenceRefs`, 'Finding evidence references must resolve to supplied evidence identifiers.');
    });
    const remediation = data(itemRecord, 'remediation');
    if (remediation !== null) inspectString(remediation, `${itemPath}.remediation`, issues);
    if (findingId !== null && claim !== null && isOneOf(verificationState, VERIFICATION_STATES)) {
      if (seenFindingIds.has(findingId)) {
        addIssue(issues, 'DUPLICATE_VALUE', `${itemPath}.findingId`, 'Finding identifiers must be unique.');
      } else {
        seenFindingIds.add(findingId);
        findings.push({ findingId, claim, verificationState, evidenceRefs: Object.freeze(evidenceRefs) });
      }
    }
  });

  const pathsArray = inspectArray(data(record, 'paths'), `${path}.paths`, issues, 256) ?? [];
  const paths: ValidatedCaseEvidence['paths'][number][] = [];
  const seenPathIds = new Set<string>();
  pathsArray.forEach((item, index) => {
    const itemPath = `${path}.paths[${index}]`;
    const itemRecord = inspectRecord(item, itemPath, CASE_PATH_KEYS, issues);
    if (!itemRecord) return;
    const pathId = inspectString(data(itemRecord, 'pathId'), `${itemPath}.pathId`, issues, { id: true }) ? data(itemRecord, 'pathId') as string : null;
    const stepsArray = inspectArray(data(itemRecord, 'steps'), `${itemPath}.steps`, issues, MAX_STEPS) ?? [];
    const steps: Array<{ kind: PathStepKind; description: string; evidenceRef: string | null }> = [];
    let stepsOk = true;
    stepsArray.forEach((stepItem, stepIndex) => {
      const stepPath = `${itemPath}.steps[${stepIndex}]`;
      const stepRecord = inspectRecord(stepItem, stepPath, CASE_PATH_STEP_KEYS, issues);
      if (!stepRecord) { stepsOk = false; return; }
      const kind = data(stepRecord, 'kind');
      const kindOk = isOneOf(kind, STEP_KINDS);
      if (!kindOk) addIssue(issues, 'INVALID_FIELD', `${stepPath}.kind`, 'Unsupported path step kind.');
      const descriptionOk = inspectString(data(stepRecord, 'description'), `${stepPath}.description`, issues);
      const evidenceRef = data(stepRecord, 'evidenceRef');
      const evidenceRefOk = evidenceRef === null || inspectString(evidenceRef, `${stepPath}.evidenceRef`, issues, { id: true });
      if (evidenceRefOk && evidenceRef !== null && !evidenceIds.has(evidenceRef as string)) {
        addIssue(issues, 'CASE_EVIDENCE_BINDING_CONTRADICTION', `${stepPath}.evidenceRef`, 'Path-step evidence reference must resolve to a supplied evidence identifier.');
      }
      if (kindOk && descriptionOk && evidenceRefOk) {
        steps.push({ kind: kind as PathStepKind, description: data(stepRecord, 'description') as string, evidenceRef: evidenceRef as string | null });
      } else {
        stepsOk = false;
      }
    });
    if (pathId !== null && stepsOk) {
      if (seenPathIds.has(pathId)) {
        addIssue(issues, 'DUPLICATE_VALUE', `${itemPath}.pathId`, 'Path identifiers must be unique.');
      } else {
        seenPathIds.add(pathId);
        paths.push({ pathId, steps: Object.freeze(steps) });
      }
    }
  });

  inspectString(data(record, 'projectionDigest'), `${path}.projectionDigest`, issues);
  if (!validUtc(data(record, 'generatedAt'))) addIssue(issues, 'INVALID_FIELD', `${path}.generatedAt`, 'Case-evidence generation time must be ISO-8601 UTC.');

  const caseIssuesArray = inspectArray(data(record, 'issues'), `${path}.issues`, issues) ?? [];
  caseIssuesArray.forEach((item, index) => {
    const itemPath = `${path}.issues[${index}]`;
    const itemRecord = inspectRecord(item, itemPath, CASE_ISSUE_KEYS, issues);
    if (itemRecord) for (const key of ['code', 'path', 'message']) inspectString(data(itemRecord, key), `${itemPath}.${key}`, issues);
  });

  if (caseId === null || workspaceId === null || typeof staleness !== 'string') return undefined;

  return {
    caseId,
    workspaceId,
    staleness: staleness as ProjectionStalenessState,
    hasIssues: caseIssuesArray.length > 0,
    findings: Object.freeze(findings),
    paths: Object.freeze(paths),
  };
}

function buildResult(
  status: CapabilityPreflightAdvisoryProjectionStatus,
  route: CapabilityAdvisoryRouteView | null,
  readiness: CapabilityAdvisoryReadinessView | null,
  approvalBoundary: CapabilityAdvisoryApprovalBoundaryView | null,
  evidence: CapabilityAdvisoryEvidenceView | null,
  nextSafeAction: string,
  blocked: boolean,
  issues: CapabilityPreflightAdvisoryProjectionIssue[],
  evaluatedAt: string,
): CapabilityPreflightAdvisoryProjectionResult {
  return Object.freeze({
    schemaVersion: CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_RESULT_VERSION,
    status,
    route,
    readiness,
    approvalBoundary,
    evidence,
    nextSafeAction,
    blocked,
    issues: freezeIssues(issues),
    evaluatedAt,
    ...authorityFields(),
  });
}

export function evaluateCapabilityPreflightAdvisoryProjection(
  input: unknown,
): CapabilityPreflightAdvisoryProjectionResult {
  const issues: CapabilityPreflightAdvisoryProjectionIssue[] = [];
  const envelope = inspectRecord(input, '$', INPUT_KEYS, issues);
  if (!envelope) {
    return buildResult('ADVISORY_PROJECTION_BLOCKED', null, null, null, null, 'Collect missing evidence and reevaluate fail closed.', true, issues, '1970-01-01T00:00:00Z');
  }

  if (data(envelope, 'schemaVersion') !== CAPABILITY_PREFLIGHT_ADVISORY_PROJECTION_CONTRACT_VERSION) {
    addIssue(issues, 'INVALID_FIELD', '$.schemaVersion', 'Unsupported advisory-projection input version.');
  }
  let nowValue: string | null = null;
  if (validUtc(data(envelope, 'now'))) {
    nowValue = data(envelope, 'now') as string;
  } else {
    addIssue(issues, 'INVALID_FIELD', '$.now', 'Current time must be ISO-8601 UTC.');
  }
  const evaluatedAt = nowValue ?? '1970-01-01T00:00:00Z';

  const validatedRoute = validateRoute(data(envelope, 'route'), issues);
  const validatedReadiness = validateReadiness(data(envelope, 'readiness'), issues);
  const validatedEnvironment = validateEnvironment(data(envelope, 'environment'), issues);
  const validatedApproval = validateApproval(data(envelope, 'approval'), issues);
  const validatedCaseEvidence = validateCaseEvidence(data(envelope, 'caseEvidence'), issues);

  if (validatedApproval === undefined || validatedCaseEvidence === undefined) {
    return buildResult('ADVISORY_PROJECTION_BLOCKED', null, null, null, null, 'Collect missing evidence and reevaluate fail closed.', true, issues, evaluatedAt);
  }

  if (validatedRoute === null || validatedReadiness === null || validatedEnvironment === null) {
    return buildResult('ADVISORY_PROJECTION_REJECTED', null, null, null, null, 'Collect missing evidence and reevaluate fail closed.', true, issues, evaluatedAt);
  }

  if (validatedReadiness.routeDecisionId !== validatedRoute.routeDecisionId) {
    addIssue(issues, 'ROUTE_READINESS_BINDING_MISMATCH', '$.readiness.routeDecisionId', 'Readiness is not bound to the exact supplied route decision.');
  }
  if (!validatedRoute.environmentSnapshotRefs.includes(validatedReadiness.snapshotId)) {
    addIssue(issues, 'READINESS_ENVIRONMENT_BINDING_MISMATCH', '$.readiness.snapshotId', 'Readiness snapshot is not referenced by the supplied route.');
  }
  if (validatedRoute.environmentSnapshotRefs.length !== 1
    || validatedEnvironment.routeDecisionId !== validatedRoute.routeDecisionId
    || validatedEnvironment.snapshotId !== validatedReadiness.snapshotId
    || validatedEnvironment.workspaceId !== validatedRoute.workspaceId) {
    addIssue(issues, 'READINESS_ENVIRONMENT_BINDING_MISMATCH', '$.environment', 'Environment evidence is not exactly bound to the supplied route, workspace, and readiness snapshot.');
  }
  const nestedReadiness = validatedEnvironment.readiness;
  if (nestedReadiness.readinessDecisionId !== validatedReadiness.readinessDecisionId
    || nestedReadiness.routeDecisionId !== validatedReadiness.routeDecisionId
    || nestedReadiness.snapshotId !== validatedReadiness.snapshotId
    || nestedReadiness.state !== validatedReadiness.state
    || nestedReadiness.nextSafeAction !== validatedReadiness.nextSafeAction
    || nestedReadiness.evaluatedAt !== validatedReadiness.evaluatedAt
    || JSON.stringify(nestedReadiness.missingDependencies) !== JSON.stringify(validatedReadiness.missingDependencies)
    || JSON.stringify(nestedReadiness.blockingReasons) !== JSON.stringify(validatedReadiness.blockingReasons)
    || JSON.stringify(nestedReadiness.evidenceRefs) !== JSON.stringify(validatedReadiness.evidenceRefs)) {
    addIssue(issues, 'READINESS_ENVIRONMENT_BINDING_MISMATCH', '$.environment.readiness', 'Nested environment readiness must exactly match the supplied readiness decision.');
  }
  const readinessIsReady = validatedReadiness.state === 'READY' || validatedReadiness.state === 'READY_WITH_EXISTING_APPROVAL';
  if ((validatedEnvironment.status === 'VALIDATED_READY_EVIDENCE') !== readinessIsReady) {
    addIssue(issues, 'READINESS_ENVIRONMENT_BINDING_MISMATCH', '$.environment.status', 'Environment status contradicts the supplied readiness state.');
  }
  if (validatedApproval?.workspaceId && validatedApproval.workspaceId !== validatedRoute.workspaceId) {
    addIssue(issues, 'APPROVAL_BINDING_CONTRADICTION', '$.approval.workspaceId', 'Approval workspace does not match the supplied route workspace.');
  }
  if (validatedReadiness.state === 'READY_WITH_EXISTING_APPROVAL'
    && validatedApproval?.disposition !== 'VALIDATED_EVIDENCE') {
    addIssue(issues, 'APPROVAL_BINDING_CONTRADICTION', '$.approval', 'READY_WITH_EXISTING_APPROVAL requires validated approval evidence.');
  }
  if (validatedCaseEvidence && validatedCaseEvidence.workspaceId !== validatedRoute.workspaceId) {
    addIssue(issues, 'CASE_EVIDENCE_BINDING_CONTRADICTION', '$.caseEvidence.workspaceId', 'Case-evidence workspace does not match the supplied route workspace.');
  }

  if (nowValue !== null) {
    if (Date.parse(validatedRoute.generatedAt) > Date.parse(nowValue)) {
      addIssue(issues, 'STALE_EVIDENCE_TIME', '$.route.generatedAt', 'Route must not be generated after the projection evaluation time.');
    }
    if (Date.parse(validatedReadiness.evaluatedAt) > Date.parse(nowValue)
      || Date.parse(nowValue) - Date.parse(validatedReadiness.evaluatedAt) > MAX_EVIDENCE_AGE_SECONDS * 1000) {
      addIssue(issues, 'STALE_EVIDENCE_TIME', '$.readiness.evaluatedAt', 'Readiness evidence must be current and not evaluated after the projection time.');
    }
    if (Date.parse(validatedEnvironment.evaluatedAt) > Date.parse(nowValue)
      || Date.parse(nowValue) - Date.parse(validatedEnvironment.evaluatedAt) > MAX_EVIDENCE_AGE_SECONDS * 1000) {
      addIssue(issues, 'STALE_EVIDENCE_TIME', '$.environment.evaluatedAt', 'Environment evidence must be current and not evaluated after the projection time.');
    }
  }

  const routeView: CapabilityAdvisoryRouteView = Object.freeze({
    routeDecisionId: validatedRoute.routeDecisionId,
    stage: validatedRoute.stage,
    primary: validatedRoute.primary,
    supporting: validatedRoute.supporting,
    rejected: validatedRoute.rejected,
    confidence: validatedRoute.confidence,
    ambiguityReasons: validatedRoute.ambiguityReasons,
  });

  const readinessView: CapabilityAdvisoryReadinessView = Object.freeze({
    readinessDecisionId: validatedReadiness.readinessDecisionId,
    snapshotId: validatedReadiness.snapshotId,
    state: validatedReadiness.state,
    missingDependencies: validatedReadiness.missingDependencies,
    blockingReasons: validatedReadiness.blockingReasons,
    evidenceRefs: validatedReadiness.evidenceRefs,
    environmentStatus: validatedEnvironment.status,
    requiredDependencies: validatedEnvironment.requiredDependencies,
    availableDependencies: validatedEnvironment.availableDependencies,
    environmentBlockingReasons: validatedEnvironment.blockingReasons,
  });

  let approvalBoundaryView: CapabilityAdvisoryApprovalBoundaryView;
  if (validatedApproval === null) {
    approvalBoundaryView = Object.freeze({ presence: 'ABSENT', planId: null, planDigest: null, approvalId: null });
  } else if (validatedApproval.disposition === 'VALIDATED_EVIDENCE') {
    approvalBoundaryView = Object.freeze({
      presence: 'PRESENT_VALIDATED',
      planId: validatedApproval.planId,
      planDigest: validatedApproval.planDigest,
      approvalId: validatedApproval.approvalId,
    });
  } else {
    approvalBoundaryView = Object.freeze({ presence: 'PRESENT_REJECTED', planId: null, planDigest: null, approvalId: null });
  }

  let evidenceView: CapabilityAdvisoryEvidenceView;
  if (validatedCaseEvidence === null) {
    evidenceView = Object.freeze({ presence: 'ABSENT', staleness: null, findings: Object.freeze([]), paths: Object.freeze([]) });
  } else {
    evidenceView = Object.freeze({
      presence: 'PRESENT',
      staleness: validatedCaseEvidence.staleness,
      findings: Object.freeze(validatedCaseEvidence.findings.map((finding) => Object.freeze({ ...finding }))),
      paths: Object.freeze(validatedCaseEvidence.paths.map((path) => Object.freeze({
        pathId: path.pathId,
        steps: Object.freeze(path.steps.map((step) => Object.freeze({ ...step }))),
      }))),
    });
  }

  const blocked = BLOCKED_READINESS_STATES.includes(validatedReadiness.state)
    || validatedRoute.stage !== 'FAST_ROUTE'
    || validatedRoute.hasIssues
    || (validatedCaseEvidence !== null
      && (validatedCaseEvidence.staleness !== 'CURRENT' || validatedCaseEvidence.hasIssues));

  if (issues.length > 0) {
    return buildResult('ADVISORY_PROJECTION_REJECTED', null, null, null, null, 'Collect missing evidence and reevaluate fail closed.', true, issues, evaluatedAt);
  }

  return buildResult(
    'ADVISORY_PROJECTION_READY',
    routeView,
    readinessView,
    approvalBoundaryView,
    evidenceView,
    validatedReadiness.nextSafeAction,
    blocked,
    issues,
    evaluatedAt,
  );
}
