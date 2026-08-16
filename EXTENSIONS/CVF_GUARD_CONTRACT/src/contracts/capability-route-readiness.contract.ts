/**
 * Capability route/readiness evidence kernel.
 *
 * Pure evaluation only. A route or READY result is evidence, never task
 * authority, package activation, approval, or an invocation command.
 */

import { isProxy } from 'node:util/types';

export const CAPABILITY_ROUTE_READINESS_CONTRACT_VERSION = 'cvf.capabilityRouteReadiness.v1' as const;
export const CAPABILITY_ROUTE_DECISION_VERSION = 'cvf.capabilityRouteDecision.v1' as const;
export const CAPABILITY_READINESS_DECISION_VERSION = 'cvf.capabilityReadinessDecision.v1' as const;

export type CapabilityRiskLevel = 'R0' | 'R1' | 'R2' | 'R3';
export type CapabilityRouteStage = 'FAST_ROUTE' | 'FULL_RESOLUTION_REQUIRED' | 'AMBIGUOUS_ROUTE' | 'NO_CANDIDATE';
export type CapabilityReadinessState =
  | 'READY' | 'READY_WITH_EXISTING_APPROVAL' | 'BOOTSTRAP_REQUIRED' | 'APPROVAL_REQUIRED'
  | 'BLOCKED_POLICY' | 'BLOCKED_PROVENANCE' | 'BLOCKED_INTEGRITY' | 'BLOCKED_COMPATIBILITY'
  | 'BLOCKED_CREDENTIAL' | 'BLOCKED_NETWORK' | 'BLOCKED_SANDBOX'
  | 'STALE_SNAPSHOT' | 'AMBIGUOUS_ROUTE' | 'UNKNOWN';

export interface CapabilityRouteCandidate {
  readonly capabilityId: string;
  readonly packageId: string;
  readonly packageVersion: string;
  readonly score: number;
  readonly reasons: readonly string[];
  readonly riskLevel: CapabilityRiskLevel;
  readonly dependencies: readonly string[];
  readonly conflicts: readonly string[];
  readonly credentialScopeRefs: readonly string[];
  readonly networkDestinations: readonly string[];
  readonly mutationKinds: readonly string[];
  readonly irreversibleEffects: boolean;
  readonly publicOrHumanEffects: boolean;
}

export interface CapabilityCandidateSet {
  readonly candidateSetId: string;
  readonly requestId: string;
  readonly workspaceId: string;
  readonly candidates: readonly CapabilityRouteCandidate[];
  readonly generatedAt: string;
}

export interface CapabilityRouteIssue {
  readonly code: 'MALFORMED_INPUT' | 'INVALID_FIELD' | 'DUPLICATE_CANDIDATE' | 'MATERIAL_AUTHORITY_AMBIGUITY' | 'DEPENDENCY_OR_CONFLICT_REVIEW_REQUIRED';
  readonly path: string;
  readonly message: string;
}

export interface CapabilityRouteDecision {
  readonly schemaVersion: typeof CAPABILITY_ROUTE_DECISION_VERSION;
  readonly routeDecisionId: string;
  readonly candidateSetId: string;
  readonly requestId: string;
  readonly workspaceId: string;
  readonly stage: CapabilityRouteStage;
  readonly primary?: Readonly<{ capabilityId: string; packageId: string; packageVersion: string }>;
  readonly supporting: readonly string[];
  readonly rejected: readonly Readonly<{ capabilityId: string; reasonCodes: readonly string[] }> [];
  readonly fallbacks: readonly Readonly<{ capabilityId: string; activationCondition: string }> [];
  readonly confidence: number;
  readonly ambiguityReasons: readonly string[];
  readonly environmentSnapshotRefs: readonly string[];
  readonly authorityStatus: 'CANDIDATE_ONLY';
  readonly executionAuthorized: false;
  readonly generatedAt: string;
  readonly issues: readonly CapabilityRouteIssue[];
}

export interface CapabilityRouteEvaluationOptions {
  readonly materialScoreDelta?: number;
  readonly environmentSnapshotRefs?: readonly string[];
  readonly now: string;
}

export interface CapabilityReadinessInput {
  readonly readinessDecisionId: string;
  readonly snapshotId: string;
  readonly snapshotObservedAt: string;
  readonly snapshotExpiresAt: string;
  readonly requiredDependencies: readonly string[];
  readonly availableDependencies: readonly string[];
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

export interface CapabilityReadinessDecision {
  readonly schemaVersion: typeof CAPABILITY_READINESS_DECISION_VERSION;
  readonly readinessDecisionId: string;
  readonly routeDecisionId: string;
  readonly snapshotId: string;
  readonly state: CapabilityReadinessState;
  readonly missingDependencies: readonly string[];
  readonly approvalRequirements: readonly string[];
  readonly blockingReasons: readonly string[];
  readonly evidenceRefs: readonly string[];
  readonly nextSafeAction: string;
  readonly evaluatedAt: string;
  readonly authorityStatus: 'EVIDENCE_ONLY';
  readonly executionAuthorized: false;
}

const SAFE_ID = /^[A-Za-z0-9._:/-]{1,256}$/;
const ISO_UTC = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?Z$/;

function isPlainRecord(value: unknown): value is Record<string, unknown> {
  if (value === null || typeof value !== 'object' || isProxy(value)) return false;
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

function validUtc(value: unknown): value is string {
  return typeof value === 'string' && ISO_UTC.test(value) && Number.isFinite(Date.parse(value));
}

function validId(value: unknown): value is string {
  return typeof value === 'string' && SAFE_ID.test(value);
}

function issue(code: CapabilityRouteIssue['code'], path: string, message: string): CapabilityRouteIssue {
  return Object.freeze({ code, path, message });
}

function sameSet(left: readonly string[], right: readonly string[]): boolean {
  return [...new Set(left)].sort().join('\u0000') === [...new Set(right)].sort().join('\u0000');
}

function materialAuthorityDifferences(left: CapabilityRouteCandidate, right: CapabilityRouteCandidate): string[] {
  const differences: string[] = [];
  if (left.riskLevel !== right.riskLevel) differences.push('RISK_LEVEL_DIFFERS');
  if (!sameSet(left.credentialScopeRefs, right.credentialScopeRefs)) differences.push('CREDENTIAL_SCOPE_DIFFERS');
  if (!sameSet(left.networkDestinations, right.networkDestinations)) differences.push('NETWORK_DESTINATIONS_DIFFER');
  if (!sameSet(left.mutationKinds, right.mutationKinds)) differences.push('MUTATION_SCOPE_DIFFERS');
  if (left.irreversibleEffects !== right.irreversibleEffects) differences.push('IRREVERSIBLE_EFFECTS_DIFFER');
  if (left.publicOrHumanEffects !== right.publicOrHumanEffects) differences.push('PUBLIC_OR_HUMAN_EFFECTS_DIFFER');
  return differences;
}

function validateCandidateSet(value: CapabilityCandidateSet, now: string): CapabilityRouteIssue[] {
  const issues: CapabilityRouteIssue[] = [];
  if (!isPlainRecord(value)) return [issue('MALFORMED_INPUT', '$.candidateSet', 'Candidate set must be a plain non-Proxy object.')];
  for (const [key, candidate] of Object.entries({ candidateSetId: value.candidateSetId, requestId: value.requestId, workspaceId: value.workspaceId })) {
    if (!validId(candidate)) issues.push(issue('INVALID_FIELD', `$.candidateSet.${key}`, `${key} must be a bounded safe identifier.`));
  }
  if (!validUtc(value.generatedAt) || Date.parse(value.generatedAt) > Date.parse(now)) issues.push(issue('INVALID_FIELD', '$.candidateSet.generatedAt', 'Candidate set time must be valid UTC and not in the future.'));
  if (!Array.isArray(value.candidates)) return [...issues, issue('MALFORMED_INPUT', '$.candidateSet.candidates', 'Candidates must be an array.')];
  const ids = value.candidates.map((candidate) => candidate?.capabilityId);
  if (new Set(ids).size !== ids.length) issues.push(issue('DUPLICATE_CANDIDATE', '$.candidateSet.candidates', 'Capability IDs must be unique.'));
  value.candidates.forEach((candidate, index) => {
    if (!isPlainRecord(candidate) || !validId(candidate.capabilityId) || !validId(candidate.packageId) || !validId(candidate.packageVersion)) {
      issues.push(issue('INVALID_FIELD', `$.candidateSet.candidates[${index}]`, 'Candidate identity fields are invalid.'));
      return;
    }
    const checked = candidate as unknown as CapabilityRouteCandidate;
    if (!Number.isFinite(checked.score) || checked.score < 0 || checked.score > 1) issues.push(issue('INVALID_FIELD', `$.candidateSet.candidates[${index}].score`, 'Score must be between zero and one.'));
    for (const field of ['reasons', 'dependencies', 'conflicts', 'credentialScopeRefs', 'networkDestinations', 'mutationKinds'] as const) {
      if (!Array.isArray(checked[field]) || checked[field].some((item) => !validId(item))) issues.push(issue('INVALID_FIELD', `$.candidateSet.candidates[${index}].${field}`, `${field} must contain bounded identifiers.`));
    }
    if (!['R0', 'R1', 'R2', 'R3'].includes(checked.riskLevel)) issues.push(issue('INVALID_FIELD', `$.candidateSet.candidates[${index}].riskLevel`, 'Unsupported risk level.'));
    if (typeof checked.irreversibleEffects !== 'boolean' || typeof checked.publicOrHumanEffects !== 'boolean') issues.push(issue('INVALID_FIELD', `$.candidateSet.candidates[${index}]`, 'Effect flags must be boolean.'));
  });
  return issues;
}

export function evaluateCapabilityRoute(
  candidateSet: CapabilityCandidateSet,
  options: CapabilityRouteEvaluationOptions,
): CapabilityRouteDecision {
  const nowValid = validUtc(options.now);
  const issues = nowValid ? validateCandidateSet(candidateSet, options.now) : [issue('INVALID_FIELD', '$.options.now', 'Current time must be ISO-8601 UTC.')];
  const threshold = options.materialScoreDelta ?? 0.1;
  if (!Number.isFinite(threshold) || threshold < 0 || threshold > 1) issues.push(issue('INVALID_FIELD', '$.options.materialScoreDelta', 'Material score delta must be between zero and one.'));
  const candidates = issues.length ? [] : [...(candidateSet.candidates ?? [])]
    .sort((left, right) => right.score - left.score || left.capabilityId.localeCompare(right.capabilityId));
  const primary = candidates[0];
  const second = candidates[1];
  const ambiguityReasons = primary && second && primary.score - second.score < threshold
    ? materialAuthorityDifferences(primary, second) : [];
  if (ambiguityReasons.length) issues.push(issue('MATERIAL_AUTHORITY_AMBIGUITY', '$.candidateSet.candidates', ambiguityReasons.join(', ')));
  const requiresClosure = Boolean(primary && (primary.dependencies.length || primary.conflicts.length));
  if (requiresClosure) issues.push(issue('DEPENDENCY_OR_CONFLICT_REVIEW_REQUIRED', '$.candidateSet.candidates[0]', 'Primary candidate requires full dependency/conflict resolution.'));
  const stage: CapabilityRouteStage = !primary ? 'NO_CANDIDATE'
    : ambiguityReasons.length ? 'AMBIGUOUS_ROUTE'
      : requiresClosure || Boolean(second && primary.score - second.score < threshold) ? 'FULL_RESOLUTION_REQUIRED'
        : 'FAST_ROUTE';
  return Object.freeze({
    schemaVersion: CAPABILITY_ROUTE_DECISION_VERSION,
    routeDecisionId: `route:${candidateSet?.requestId ?? 'invalid'}`,
    candidateSetId: candidateSet?.candidateSetId ?? 'invalid',
    requestId: candidateSet?.requestId ?? 'invalid',
    workspaceId: candidateSet?.workspaceId ?? 'invalid',
    stage,
    ...(primary ? { primary: Object.freeze({ capabilityId: primary.capabilityId, packageId: primary.packageId, packageVersion: primary.packageVersion }) } : {}),
    supporting: Object.freeze(primary?.dependencies.slice() ?? []),
    rejected: Object.freeze(candidates.slice(1).map((candidate) => Object.freeze({ capabilityId: candidate.capabilityId, reasonCodes: Object.freeze(candidate === second && ambiguityReasons.length ? ambiguityReasons : ['LOWER_DETERMINISTIC_SCORE']) }))),
    fallbacks: Object.freeze(candidates.slice(1).map((candidate) => Object.freeze({ capabilityId: candidate.capabilityId, activationCondition: 'PRIMARY_UNAVAILABLE_AND_AUTHORITY_ENVELOPE_REVALIDATED' }))),
    confidence: primary ? (stage === 'FAST_ROUTE' ? primary.score : Math.min(primary.score, 0.79)) : 0,
    ambiguityReasons: Object.freeze(ambiguityReasons),
    environmentSnapshotRefs: Object.freeze((options.environmentSnapshotRefs ?? []).filter(validId)),
    authorityStatus: 'CANDIDATE_ONLY',
    executionAuthorized: false,
    generatedAt: nowValid ? options.now : '1970-01-01T00:00:00Z',
    issues: Object.freeze(issues),
  });
}

function readinessResult(
  route: CapabilityRouteDecision,
  input: CapabilityReadinessInput,
  state: CapabilityReadinessState,
  missing: readonly string[],
  blockingReasons: readonly string[],
  now: string,
): CapabilityReadinessDecision {
  const actions: Record<CapabilityReadinessState, string> = {
    READY: 'Bind the selected capability to SPEC and WORK ORDER before execution.',
    READY_WITH_EXISTING_APPROVAL: 'Revalidate the existing approval at the execution boundary.',
    BOOTSTRAP_REQUIRED: 'Create a controlled-acquisition plan; do not install automatically.',
    APPROVAL_REQUIRED: 'Obtain approval bound to the exact plan and authority envelope.',
    STALE_SNAPSHOT: 'Refresh the read-only environment snapshot.',
    AMBIGUOUS_ROUTE: 'Resolve material route ambiguity with governed review.',
    UNKNOWN: 'Collect missing evidence and reevaluate fail closed.',
    BLOCKED_POLICY: 'Resolve the policy denial before continuing.',
    BLOCKED_PROVENANCE: 'Provide verified source provenance.',
    BLOCKED_INTEGRITY: 'Resolve source or artifact integrity failure.',
    BLOCKED_COMPATIBILITY: 'Select a compatible capability or environment.',
    BLOCKED_CREDENTIAL: 'Bind credentials through the governed credential owner.',
    BLOCKED_NETWORK: 'Resolve the approved network-destination boundary.',
    BLOCKED_SANDBOX: 'Resolve the required sandbox boundary.',
  };
  return Object.freeze({
    schemaVersion: CAPABILITY_READINESS_DECISION_VERSION,
    readinessDecisionId: input.readinessDecisionId,
    routeDecisionId: route.routeDecisionId,
    snapshotId: input.snapshotId,
    state,
    missingDependencies: Object.freeze([...missing]),
    approvalRequirements: Object.freeze(input.approvalRequired && !input.existingApprovalValid ? ['EXACT_PLAN_APPROVAL_REQUIRED'] : []),
    blockingReasons: Object.freeze([...blockingReasons]),
    evidenceRefs: Object.freeze([...input.evidenceRefs]),
    nextSafeAction: actions[state],
    evaluatedAt: now,
    authorityStatus: 'EVIDENCE_ONLY',
    executionAuthorized: false,
  });
}

export function evaluateCapabilityReadiness(
  route: CapabilityRouteDecision,
  input: CapabilityReadinessInput,
  now: string,
): CapabilityReadinessDecision {
  const missing = input.requiredDependencies.filter((dependency) => !input.availableDependencies.includes(dependency));
  const checks: readonly [boolean, CapabilityReadinessState, string][] = [
    [input.integrityVerified === false, 'BLOCKED_INTEGRITY', 'INTEGRITY_FAILED'],
    [input.provenanceVerified === false, 'BLOCKED_PROVENANCE', 'PROVENANCE_FAILED'],
    [input.policyAllowed === false, 'BLOCKED_POLICY', 'POLICY_DENIED'],
    [input.compatible === false, 'BLOCKED_COMPATIBILITY', 'COMPATIBILITY_FAILED'],
    [input.credentialsReady === false, 'BLOCKED_CREDENTIAL', 'CREDENTIALS_NOT_READY'],
    [input.networkReady === false, 'BLOCKED_NETWORK', 'NETWORK_NOT_READY'],
    [input.sandboxReady === false, 'BLOCKED_SANDBOX', 'SANDBOX_NOT_READY'],
    [route.stage === 'AMBIGUOUS_ROUTE', 'AMBIGUOUS_ROUTE', 'MATERIAL_ROUTE_AMBIGUITY'],
    [route.stage !== 'FAST_ROUTE' || route.issues.length > 0, 'UNKNOWN', 'ROUTE_NOT_FULLY_RESOLVED'],
    [!validUtc(now) || !validUtc(input.snapshotObservedAt) || !validUtc(input.snapshotExpiresAt) || Date.parse(input.snapshotObservedAt) > Date.parse(now) || Date.parse(now) >= Date.parse(input.snapshotExpiresAt), 'STALE_SNAPSHOT', 'SNAPSHOT_STALE_OR_INVALID'],
    [[input.policyAllowed, input.provenanceVerified, input.integrityVerified, input.compatible, input.credentialsReady, input.networkReady, input.sandboxReady].some((value) => value === null), 'UNKNOWN', 'REQUIRED_EVIDENCE_UNKNOWN'],
    [input.approvalRequired && !input.existingApprovalValid, 'APPROVAL_REQUIRED', 'APPROVAL_REQUIRED'],
    [missing.length > 0, 'BOOTSTRAP_REQUIRED', 'DEPENDENCIES_MISSING'],
  ];
  const selected = checks.find(([condition]) => condition);
  const state = selected?.[1] ?? (input.approvalRequired ? 'READY_WITH_EXISTING_APPROVAL' : 'READY');
  return readinessResult(route, input, state, missing, selected ? [selected[2]] : [], validUtc(now) ? now : '1970-01-01T00:00:00Z');
}
