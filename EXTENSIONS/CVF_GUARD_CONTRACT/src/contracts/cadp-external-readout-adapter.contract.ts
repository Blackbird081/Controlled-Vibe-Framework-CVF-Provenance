/**
 * CADP-AI-T5-R2 transport-neutral external readout adapter contract.
 *
 * A pure, synchronous, deterministic composition over the accepted T5-R1
 * external-readout foundation. It runs the fixed stage order ingress ->
 * freshness -> redaction rejection -> allowlist -> authentication-required
 * terminal decision -> deterministic receipt for the rejected bounded
 * response, and imports the T5-R1 helpers rather than duplicating their
 * validation logic.
 *
 * No transport, tool, or command is registered by this module. No function
 * exported here accepts a credential, authentication claim, callback, port,
 * store, URL, command, or environment value. Every authority/transport field
 * on every returned envelope is a literal `false`. Because no external
 * authentication owner exists yet, this adapter can never produce an
 * `accepted: true` response; every possible input reaches a controlled
 * rejection.
 */

import { isProxy } from 'node:util/types';
import {
  createDeterministicCadpExternalReadoutReceipt,
  evaluateCadpExternalReadoutFreshness,
  redactCadpExternalReadoutPayload,
  validateCadpExternalReadoutAllowlistedMetadata,
  validateCadpExternalReadoutIngress,
  type CadpExternalReadoutFreshnessInput,
  type CadpExternalReadoutIngressRequest,
  type CadpExternalReadoutAllowlistedMetadata,
  type CadpExternalReadoutIssue,
  type CadpExternalReadoutReceipt,
} from './cadp-external-readout-foundation.contract';

const ISO8601_UTC_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,9})?Z$/;
const DAYS_IN_MONTH: readonly number[] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

function isLeapYear(year: number): boolean {
  return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
}

/**
 * Trap-free receipt-safe timestamp check, mirroring the T5-R1 foundation's
 * own calendar-valid ISO-8601 UTC rule. Used only to decide whether a
 * caller-supplied `issuedAt` may be passed to the receipt constructor; an
 * invalid value never reaches `createDeterministicCadpExternalReadoutReceipt`
 * unguarded, so a malformed timestamp always resolves to a controlled
 * rejection rather than an uncaught constructor error.
 */
function isReceiptSafeTimestamp(value: unknown): value is string {
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

export const CADP_EXTERNAL_READOUT_ADAPTER_CONTRACT_VERSION = 'cvf.cadp.externalReadoutAdapter.v1' as const;

export type CadpExternalReadoutAdapterStage =
  | 'INGRESS'
  | 'FRESHNESS'
  | 'REDACTION'
  | 'ALLOWLIST'
  | 'AUTHENTICATION';

export type CadpExternalReadoutAdapterIssueCode =
  | CadpExternalReadoutIssue['code']
  | 'AUTHENTICATION_REQUIRED';

export interface CadpExternalReadoutAdapterIssue {
  readonly stage: CadpExternalReadoutAdapterStage;
  readonly code: CadpExternalReadoutAdapterIssueCode;
  readonly path: string;
  readonly message: string;
}

/**
 * Exact public request shape. Contains only the ingress request, explicit
 * freshness input, and candidate allowlisted metadata. No credential,
 * authentication claim, callback, port, function, store, URL, command, or
 * environment value can be represented by this type.
 */
export interface CadpExternalReadoutAdapterRequest {
  readonly ingress: CadpExternalReadoutIngressRequest;
  readonly freshness: CadpExternalReadoutFreshnessInput;
  readonly candidateMetadata: CadpExternalReadoutAllowlistedMetadata;
}

/**
 * Deterministic rejected-response payload. Never carries candidate metadata,
 * because no authentication owner is implemented in this tranche.
 */
export interface CadpExternalReadoutAdapterRejectedPayload {
  readonly rejectedAtStage: CadpExternalReadoutAdapterStage;
  readonly issueCount: number;
}

/**
 * The adapter's full response envelope. Every authority/transport field is a
 * literal `false` in both type and value position, so no branch of this
 * contract can ever represent an authorized external action.
 */
export interface CadpExternalReadoutAdapterResponse {
  readonly accepted: false;
  readonly authenticationVerified: false;
  readonly externalTransportRegistered: false;
  readonly externalInvocationAuthorized: false;
  readonly externalMutationAuthorized: false;
  readonly externalActivationAuthorized: false;
  readonly externalExecutionAuthorized: false;
  readonly externalProviderCallAuthorized: false;
  readonly externalCredentialResolutionAuthorized: false;
  readonly issues: readonly CadpExternalReadoutAdapterIssue[];
  readonly receipt: CadpExternalReadoutReceipt<CadpExternalReadoutAdapterRejectedPayload>;
}

function toAdapterIssues(
  stage: CadpExternalReadoutAdapterStage,
  issues: readonly CadpExternalReadoutIssue[],
): readonly CadpExternalReadoutAdapterIssue[] {
  return Object.freeze(issues.map((issue) => Object.freeze({ stage, code: issue.code, path: issue.path, message: issue.message })));
}

function adapterIssue(
  stage: CadpExternalReadoutAdapterStage,
  code: CadpExternalReadoutAdapterIssueCode,
  path: string,
  message: string,
): CadpExternalReadoutAdapterIssue {
  return Object.freeze({ stage, code, path, message });
}

const DETERMINISTIC_REJECTION_TIMESTAMP = '1970-01-01T00:00:00.000Z';

/**
 * Builds the fixed, literal-false-authority rejected response, attaching a
 * deterministic receipt keyed only on the caller-supplied request identity,
 * the rejecting stage, and the issue count. The receipt never echoes a raw
 * rejected value; it records only the stage and a count.
 */
function buildRejectedResponse(
  stage: CadpExternalReadoutAdapterStage,
  issues: readonly CadpExternalReadoutAdapterIssue[],
  requestId: string,
  issuedAt: string,
): CadpExternalReadoutAdapterResponse {
  const payload: CadpExternalReadoutAdapterRejectedPayload = Object.freeze({
    rejectedAtStage: stage,
    issueCount: issues.length,
  });
  const receipt = createDeterministicCadpExternalReadoutReceipt<CadpExternalReadoutAdapterRejectedPayload>({
    requestId,
    issuedAt,
    payload,
  });
  return Object.freeze({
    accepted: false,
    authenticationVerified: false,
    externalTransportRegistered: false,
    externalInvocationAuthorized: false,
    externalMutationAuthorized: false,
    externalActivationAuthorized: false,
    externalExecutionAuthorized: false,
    externalProviderCallAuthorized: false,
    externalCredentialResolutionAuthorized: false,
    issues,
    receipt,
  });
}

/**
 * Derives a stable, non-ambient request identity for the receipt from the
 * caller-supplied `issuedAt` timestamp and rejecting stage. This function
 * reads no clock, UUID source, environment value, or module-level ordinal.
 */
function deriveRequestId(issuedAt: string, stage: CadpExternalReadoutAdapterStage): string {
  return `cadp-external-readout-adapter-${stage.toLowerCase()}-${issuedAt}`;
}

/**
 * Evaluates a transport-neutral external readout request and always returns
 * a rejected, literal-false-authority envelope, because no authentication
 * owner is implemented in this tranche. The function performs no I/O, reads
 * no clock or environment value, and never invokes a caller-supplied
 * function, callback, or port (the input type cannot represent one).
 *
 * Stage order (fixed, never reordered): ingress -> freshness -> redaction
 * rejection -> allowlist -> authentication-required terminal decision.
 * Any stage failure stops evaluation immediately; later stages never run and
 * later-stage caller data is never inspected once an earlier stage rejects.
 */
export function evaluateCadpExternalReadoutAdapter(
  request: CadpExternalReadoutAdapterRequest,
): CadpExternalReadoutAdapterResponse {
  const fallbackIssuedAt = DETERMINISTIC_REJECTION_TIMESTAMP;

  const isRealObject = request !== null && (typeof request === 'object' || typeof request === 'function');
  const isPlainRequest =
    isRealObject &&
    !isProxy(request) &&
    Object.getPrototypeOf(request) === Object.prototype;

  if (!isPlainRequest) {
    const issues = [adapterIssue('INGRESS', 'MALFORMED_REQUEST', '$', 'Adapter request must be a plain data object.')];
    return buildRejectedResponse('INGRESS', issues, deriveRequestId(fallbackIssuedAt, 'INGRESS'), fallbackIssuedAt);
  }

  const requestNames = Object.getOwnPropertyNames(request);
  const expectedRequestKeys = ['ingress', 'freshness', 'candidateMetadata'];
  if (
    Object.getOwnPropertySymbols(request).length > 0 ||
    requestNames.length !== expectedRequestKeys.length ||
    requestNames.some((name) => !expectedRequestKeys.includes(name))
  ) {
    const issues = [adapterIssue('INGRESS', 'UNKNOWN_FIELD', '$', 'Adapter request has unknown or missing top-level fields; only ingress, freshness, and candidateMetadata are accepted.')];
    return buildRejectedResponse('INGRESS', issues, deriveRequestId(fallbackIssuedAt, 'INGRESS'), fallbackIssuedAt);
  }

  const ingressDescriptor = Object.getOwnPropertyDescriptor(request, 'ingress');
  const freshnessDescriptor = Object.getOwnPropertyDescriptor(request, 'freshness');
  const candidateMetadataDescriptor = Object.getOwnPropertyDescriptor(request, 'candidateMetadata');
  if (
    !ingressDescriptor || !ingressDescriptor.enumerable || 'get' in ingressDescriptor || 'set' in ingressDescriptor ||
    !freshnessDescriptor || !freshnessDescriptor.enumerable || 'get' in freshnessDescriptor || 'set' in freshnessDescriptor ||
    !candidateMetadataDescriptor || !candidateMetadataDescriptor.enumerable || 'get' in candidateMetadataDescriptor || 'set' in candidateMetadataDescriptor
  ) {
    const issues = [adapterIssue('INGRESS', 'MALFORMED_REQUEST', '$', 'ingress, freshness, and candidateMetadata must be own enumerable data properties.')];
    return buildRejectedResponse('INGRESS', issues, deriveRequestId(fallbackIssuedAt, 'INGRESS'), fallbackIssuedAt);
  }

  // Stage 1: ingress. Runs before any other stage inspects request data.
  const ingressResult = validateCadpExternalReadoutIngress(ingressDescriptor.value);
  if (!ingressResult.valid || !ingressResult.data.request) {
    const issues = toAdapterIssues('INGRESS', ingressResult.issues);
    return buildRejectedResponse('INGRESS', issues, deriveRequestId(fallbackIssuedAt, 'INGRESS'), fallbackIssuedAt);
  }

  // Stage 2: freshness. Only the already-validated freshness input is read.
  const freshnessValue = freshnessDescriptor.value;
  const freshnessResult = evaluateCadpExternalReadoutFreshness(freshnessValue as CadpExternalReadoutFreshnessInput);
  const freshnessIssuedAtField =
    freshnessValue !== null && typeof freshnessValue === 'object' && !isProxy(freshnessValue)
      ? Object.getOwnPropertyDescriptor(freshnessValue, 'issuedAt')
      : undefined;
  const rawIssuedAt =
    freshnessIssuedAtField && freshnessIssuedAtField.enumerable && !('get' in freshnessIssuedAtField) && !('set' in freshnessIssuedAtField)
      ? freshnessIssuedAtField.value
      : undefined;
  // Only a calendar-valid timestamp may reach the receipt constructor, which
  // itself throws on an invalid value; an invalid caller-supplied issuedAt
  // always falls back to the deterministic per-call fallback instead.
  const issuedAt = isReceiptSafeTimestamp(rawIssuedAt) ? rawIssuedAt : fallbackIssuedAt;
  if (freshnessResult.disposition !== 'FRESH') {
    const issues = toAdapterIssues('FRESHNESS', freshnessResult.issues.length > 0
      ? freshnessResult.issues
      : [{ code: 'STALE_REQUEST', path: '$.freshness', message: `Freshness disposition was ${freshnessResult.disposition}, not FRESH.` }]);
    return buildRejectedResponse('FRESHNESS', issues, deriveRequestId(issuedAt, 'FRESHNESS'), issuedAt);
  }

  // Stage 3: redaction rejection. Rejects secret/private-provenance fields
  // present anywhere in the already-validated ingress request before any
  // allowlist logic runs.
  const redactionResult = redactCadpExternalReadoutPayload(candidateMetadataDescriptor.value);
  if (!redactionResult.valid) {
    const issues = toAdapterIssues('REDACTION', redactionResult.issues);
    return buildRejectedResponse('REDACTION', issues, deriveRequestId(issuedAt, 'REDACTION'), issuedAt);
  }

  // Stage 4: allowlist. Candidate metadata is validated but is never copied
  // into the response: authentication remains absent and therefore cannot
  // authorize disclosure of even a well-shaped candidate.
  const allowlistResult = validateCadpExternalReadoutAllowlistedMetadata(candidateMetadataDescriptor.value);
  if (!allowlistResult.valid || !allowlistResult.data.metadata) {
    const issues = toAdapterIssues('ALLOWLIST', allowlistResult.issues);
    return buildRejectedResponse('ALLOWLIST', issues, deriveRequestId(issuedAt, 'ALLOWLIST'), issuedAt);
  }

  // Stage 5: authentication-required terminal decision. This tranche
  // implements no authentication owner, so every request reaches this
  // terminal rejection; no caller-supplied data can ever produce
  // `accepted: true`.
  const authenticationIssue = adapterIssue(
    'AUTHENTICATION',
    'AUTHENTICATION_REQUIRED',
    '$.identity',
    'External authentication is not implemented; no caller can obtain an accepted external readout.',
  );

  return buildRejectedResponse(
    'AUTHENTICATION',
    Object.freeze([authenticationIssue]),
    deriveRequestId(issuedAt, 'AUTHENTICATION'),
    issuedAt,
  );
}
