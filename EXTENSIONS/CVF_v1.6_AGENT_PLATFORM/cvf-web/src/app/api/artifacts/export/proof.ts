import { canonicalJson, envelopeSha256, parseEnvelope, type ControlledEvaluateRequest, type ControlledInvoker, type OperationEnvelope,
  type OperationOutcomeKind, type OperationReceipt, type OutcomeInput, type PresenceLookup } from '@/lib/artifacts-receipt-operation-contract';
import { sha256, type DraftPrincipal } from '@/lib/html-draft-recovery-contract';
import type { ExistingOperation, HtmlDraftSnapshotStore } from '@/lib/server/html-draft-snapshot-store';

const GOVERNANCE_EVALUATE_URL = '/api/governance/evaluate';
const PROOF_TIMEOUT_MS = 4000;
const MAX_PROOF_TIMEOUT_MS = 30000;

export type GovernanceReceiptStatus = 'PRESENT' | 'NOT_CONFIGURED' | 'TIMED_OUT' | 'UNAVAILABLE' | 'INVALID_RESPONSE';

export interface GovernanceReceipt {
  receiptId: string;
  decision: string;
  evaluatedAt: string;
  riskLevel: string;
}

export interface GovernanceReceiptCheck {
  status: GovernanceReceiptStatus;
  receipt: GovernanceReceipt | null;
  requestId?: string;
}

function proofTimeoutMs(): number {
  const configured = Number(process.env.CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS);
  return Number.isInteger(configured) && configured >= 1000 && configured <= MAX_PROOF_TIMEOUT_MS
    ? configured
    : PROOF_TIMEOUT_MS;
}

interface EvaluateResponseData {
  report?: {
    status?: string;
    risk_level?: string;
    cvf_enforcement?: { action?: string };
    request_summary?: { request_id?: string; artifact_id?: string };
    decision_analysis?: { final_decision?: string };
    report_metadata?: { generated_at?: string };
    cvf_risk_level?: string;
    integrity?: { has_ledger_reference?: boolean };
  };
  execution_record?: {
    request_id?: string;
    timestamp?: string;
    final_decision?: string;
    ledger_attached?: boolean;
  };
  [key: string]: unknown;
}

interface EvaluateResponse {
  success: boolean;
  data?: EvaluateResponseData;
}

function isAbsoluteUrl(url: string): boolean {
  return url.startsWith('http://') || url.startsWith('https://');
}

function resolveEvaluateUrl(base: string): string {
  if (isAbsoluteUrl(base)) return base;
  if (typeof process !== 'undefined' && process.env.NEXTAUTH_URL) {
    return `${process.env.NEXTAUTH_URL.replace(/\/$/, '')}${base}`;
  }
  return base;
}

export async function fetchGovernanceReceipt(
  artifactId: string,
  sourceContent: string,
  serviceToken?: string,
): Promise<GovernanceReceiptCheck> {
  const url = resolveEvaluateUrl(GOVERNANCE_EVALUATE_URL);

  if (!isAbsoluteUrl(url)) {
    return { status: 'NOT_CONFIGURED', receipt: null };
  }

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), proofTimeoutMs());
  const requestId = `artifact-proof-${artifactId}-${Date.now()}`;
  const failure = (status: GovernanceReceiptStatus): GovernanceReceiptCheck => ({ status, receipt: null, requestId });

  try {
    const headers: Record<string, string> = { 'Content-Type': 'application/json' };
    if (serviceToken) headers['x-cvf-service-token'] = serviceToken;

    const response = await fetch(url, {
      method: 'POST',
      headers,
      signal: controller.signal,
      body: JSON.stringify({
        request_id: requestId,
        artifact_id: artifactId,
        payload: { content: sourceContent.slice(0, 500) },
        cvf_phase: 'REVIEW',
        cvf_risk_level: 'R0',
      }),
    });

    if (!response.ok) return failure('UNAVAILABLE');

    let payload: EvaluateResponse;
    try {
      payload = await response.json() as EvaluateResponse;
    } catch {
      return failure('INVALID_RESPONSE');
    }
    if (payload.success !== true || !payload.data) return failure('INVALID_RESPONSE');

    const data = payload.data;
    // Current Governance Engine reports the request identity and decision in
    // nested report sections; its execution record does not repeat the ID.
    const report = data.report;
    const engineDecision = report?.decision_analysis?.final_decision;
    if (report?.request_summary) {
      const expectedAction: Record<string, string> = {
        ALLOW: 'ALLOW', DENY: 'BLOCK', REVIEW: 'NEEDS_APPROVAL',
        ESCALATE: 'ESCALATE', SANDBOX: 'LOG_ONLY',
      };
      if (report.request_summary.request_id !== requestId ||
        report.request_summary.artifact_id !== artifactId ||
        !engineDecision || !expectedAction[engineDecision] ||
        report.cvf_enforcement?.action !== expectedAction[engineDecision] ||
        data.execution_record?.final_decision !== engineDecision ||
        data.execution_record?.ledger_attached !== true ||
        report.integrity?.has_ledger_reference !== true ||
        typeof report.report_metadata?.generated_at !== 'string' || !report.report_metadata.generated_at ||
        typeof report.cvf_risk_level !== 'string' || !/^R[0-4]$/.test(report.cvf_risk_level)) return failure('INVALID_RESPONSE');
      return {
        status: 'PRESENT', requestId,
        receipt: {
          receiptId: requestId,
          decision: engineDecision,
          evaluatedAt: report.report_metadata.generated_at,
          riskLevel: report.cvf_risk_level,
        },
      };
    }

    // Retain the older explicit approval envelope for compatible callers.
    const status = data.report?.status;
    if (data.execution_record?.request_id !== requestId ||
      !['APPROVED', 'MANUAL_REVIEW', 'REJECTED', 'FROZEN'].includes(String(status)) ||
      typeof data.execution_record.timestamp !== 'string' || !data.execution_record.timestamp ||
      typeof data.report?.risk_level !== 'string' || !data.report.risk_level ||
      (status === 'APPROVED' && data.report.cvf_enforcement?.action !== 'ALLOW')) return failure('INVALID_RESPONSE');
    return {
      status: 'PRESENT', requestId,
      receipt: {
        receiptId: requestId,
        decision: status as string,
        evaluatedAt: data.execution_record.timestamp,
        riskLevel: data.report.risk_level,
      },
    };
  } catch (error) {
    return failure(controller.signal.aborted ||
      (error !== null && typeof error === 'object' && 'name' in error && error.name === 'AbortError')
      ? 'TIMED_OUT' : 'UNAVAILABLE');
  } finally {
    clearTimeout(timer);
  }
}

// ---- Controlled receipt operation: injected synthetic fixture only. fetchGovernanceReceipt above is retained as the separate legacy R0 path.
// This code never calls global fetch, reads credentials or imports an engine. Results establish protocol and invocation counters only. ----

export function buildControlledEvaluateRequest(attemptId: string, artifactId: string, sourceContent: string): ControlledEvaluateRequest {
  return { request_id: attemptId, artifact_id: artifactId, payload: { content: sourceContent.slice(0, 500) }, cvf_phase: 'REVIEW', cvf_risk_level: 'R1' };
}
export const controlledRequestSha256 = (request: ControlledEvaluateRequest): string => sha256(canonicalJson(request));

const EXPECTED_ACTION: Record<string, string> = { ALLOW: 'ALLOW', DENY: 'BLOCK', REVIEW: 'NEEDS_APPROVAL', ESCALATE: 'ESCALATE', SANDBOX: 'LOG_ONLY' };

/** Strict current-engine shape only. The older explicit approval envelope is not accepted on the controlled path. */
export function parseControlledReceipt(payload: unknown, request: ControlledEvaluateRequest): OperationReceipt | null {
  const response = payload as EvaluateResponse | null | undefined;
  const report = response?.success === true ? response.data?.report : undefined;
  const execution = response?.data?.execution_record;
  const decision = report?.decision_analysis?.final_decision;
  if (!report?.request_summary || report.request_summary.request_id !== request.request_id || report.request_summary.artifact_id !== request.artifact_id
    || !decision || !Object.hasOwn(EXPECTED_ACTION, decision) || report.cvf_enforcement?.action !== EXPECTED_ACTION[decision]
    || execution?.final_decision !== decision || execution?.ledger_attached !== true || report.integrity?.has_ledger_reference !== true
    || report.cvf_risk_level !== request.cvf_risk_level || typeof report.report_metadata?.generated_at !== 'string'
    || !report.report_metadata.generated_at) return null;
  return { receiptId: request.request_id, decision, evaluatedAt: report.report_metadata.generated_at, riskLevel: request.cvf_risk_level };
}

export type ControlledReceiptResult =
  | { kind: 'DENIED'; reason: string; sends: 0 }
  | { kind: 'ALREADY_PROCESSED'; operationKey: string; state: string; outcome: OperationOutcomeKind | null; sends: 0 }
  | { kind: 'REUSED'; operationKey: string; receipt: OperationReceipt; sends: 0 }
  | { kind: 'EXECUTED'; operationKey: string; outcome: OperationOutcomeKind; receipt: OperationReceipt | null; reason: string | null; persisted: boolean; sends: 1 };
export type ReceiptOperationStore = Pick<HtmlDraftSnapshotStore, 'admitOperation' | 'startOperation' | 'consumeGrant' | 'writeOutcome'>;
export interface ControlledReceiptOptions {
  store: ReceiptOperationStore;
  owner: DraftPrincipal;
  envelope: unknown;
  request: ControlledEvaluateRequest;
  invoker: ControlledInvoker;
  timeoutMs: number;
  signal?: AbortSignal;
}

/** Bounded wait for local store work. A timeout or error yields null; it never proves the work did not happen. */
function bounded<T>(work: Promise<T>, ms: number): Promise<T | null> {
  return new Promise<T | null>(resolve => {
    const timer = setTimeout(() => resolve(null), ms);
    work.then(value => { clearTimeout(timer); resolve(value); }, () => { clearTimeout(timer); resolve(null); });
  });
}

function settleExisting(envelope: OperationEnvelope, existing: ExistingOperation): ControlledReceiptResult {
  if (!('intent' in existing)) return { kind: 'DENIED', reason: `OPERATION_${existing.state}`, sends: 0 };
  const outcome = existing.state === 'OUTCOME' ? existing.outcome : null;
  if (outcome?.outcome === 'RECEIPT_VERIFIED' && outcome.receipt && existing.intent.envelopeSha256 === envelopeSha256(envelope)) {
    return { kind: 'REUSED', operationKey: envelope.operationKey, receipt: outcome.receipt, sends: 0 };
  }
  return { kind: 'ALREADY_PROCESSED', operationKey: envelope.operationKey, state: existing.state, outcome: outcome?.outcome ?? null, sends: 0 };
}

type Settled = { kind: 'RESPONSE'; value: unknown } | { kind: 'UNKNOWN'; reason: string };
/** One invocation, bounded. A late response after settlement is dropped and cannot publish an outcome. */
function invokeOnce(invoker: ControlledInvoker, request: ControlledEvaluateRequest, timeoutMs: number, external?: AbortSignal): Promise<Settled> {
  return new Promise<Settled>(resolve => {
    const controller = new AbortController();
    let done = false;
    const timer = setTimeout(() => { controller.abort(); finish({ kind: 'UNKNOWN', reason: 'TIMED_OUT' }); }, timeoutMs);
    const onAbort = () => { controller.abort(); finish({ kind: 'UNKNOWN', reason: 'ABORTED' }); };
    const finish = (value: Settled) => {
      if (done) return;
      done = true;
      clearTimeout(timer);
      external?.removeEventListener('abort', onAbort);
      resolve(value);
    };
    external?.addEventListener('abort', onAbort, { once: true });
    const copy = JSON.parse(JSON.stringify(request)) as ControlledEvaluateRequest;
    Promise.resolve().then(() => invoker(copy, controller.signal)).then(
      value => finish({ kind: 'RESPONSE', value }),
      () => finish({ kind: 'UNKNOWN', reason: controller.signal.aborted ? 'ABORTED' : 'INVOKER_ERROR' }),
    );
  });
}

/** Consume the grant before invoking. A fabricated, copied or spent grant denies with zero sends. */
export async function invokeWithGrant(options: ControlledReceiptOptions, grant: unknown): Promise<ControlledReceiptResult> {
  const { store, invoker, request, timeoutMs, signal } = options;
  const consumed = store.consumeGrant(grant, invoker);
  if (!consumed) return { kind: 'DENIED', reason: 'GRANT_REJECTED', sends: 0 };
  if (signal?.aborted) {
    await bounded(store.writeOutcome(consumed, { outcome: 'FAILED_BEFORE_SEND', receipt: null, reason: 'ABORTED_BEFORE_SEND' }), timeoutMs);
    return { kind: 'DENIED', reason: 'FAILED_BEFORE_SEND', sends: 0 };
  }
  const settled = await invokeOnce(invoker, request, timeoutMs, signal);
  let input: OutcomeInput;
  if (settled.kind === 'RESPONSE') {
    const receipt = parseControlledReceipt(settled.value, request);
    input = receipt
      ? { outcome: receipt.decision === 'DENY' ? 'DENIED' : 'RECEIPT_VERIFIED', receipt, reason: null }
      : { outcome: 'OUTCOME_UNKNOWN', receipt: null, reason: 'INVALID_RESPONSE' };
  } else {
    input = { outcome: 'OUTCOME_UNKNOWN', receipt: null, reason: settled.reason };
  }
  const saved = await bounded(store.writeOutcome(consumed, input), timeoutMs);
  if (saved?.kind === 'SAVED') {
    return { kind: 'EXECUTED', operationKey: consumed.operationKey, outcome: saved.outcome.outcome, receipt: saved.outcome.receipt,
      reason: saved.outcome.reason, persisted: true, sends: 1 };
  }
  return { kind: 'EXECUTED', operationKey: consumed.operationKey, outcome: 'OUTCOME_UNKNOWN', receipt: null,
    reason: `OUTCOME_WRITE_${saved ? saved.kind : 'UNCONFIRMED'}`, persisted: false, sends: 1 };
}

/** Admit, start and invoke the injected callback at most once for one immutable logical operation. */
export async function runControlledReceipt(options: ControlledReceiptOptions): Promise<ControlledReceiptResult> {
  const { store, owner, request, invoker, timeoutMs } = options;
  const denied = (reason: string): ControlledReceiptResult => ({ kind: 'DENIED', reason, sends: 0 });
  const envelope = parseEnvelope(options.envelope);
  if (!envelope || !request || typeof invoker !== 'function' || !Number.isInteger(timeoutMs) || timeoutMs < 1 || timeoutMs > MAX_PROOF_TIMEOUT_MS
    || request.cvf_phase !== 'REVIEW' || request.cvf_risk_level !== 'R1' || request.request_id !== envelope.attemptId
    || request.artifact_id !== envelope.output.artifactId || controlledRequestSha256(request) !== envelope.payloadSha256) return denied('INVALID_PROOF_INPUT');
  const admitted = await bounded(store.admitOperation(envelope, owner), timeoutMs);
  if (!admitted) return denied('STORE_UNAVAILABLE');
  if (admitted.kind === 'DENIED') return denied(admitted.reason);
  if (admitted.kind === 'EXISTING') return settleExisting(envelope, admitted.operation);
  const started = await bounded(store.startOperation(owner, envelope.operationKey, invoker), timeoutMs);
  if (!started) return denied('STORE_UNAVAILABLE');
  if (started.kind === 'DENIED') return denied(started.reason);
  if (started.kind === 'EXISTING') return settleExisting(envelope, started.operation);
  return invokeWithGrant(options, started.grant);
}

export interface PresenceDiagnostic { status: 'REMOTE_PRESENCE_OBSERVED' | 'UNKNOWN'; releasesUnknown: false; grantsReplay: false }
/** Reconcile B: optional pure diagnostic over an injected lookup. It never writes, releases UNKNOWN or grants a replay. */
export async function diagnoseRemotePresence(lookup: PresenceLookup, envelope: OperationEnvelope, timeoutMs = PROOF_TIMEOUT_MS): Promise<PresenceDiagnostic> {
  const entry = await bounded(Promise.resolve().then(() => lookup({ requestId: envelope.attemptId })), timeoutMs);
  const present = !!entry && entry.requestId === envelope.attemptId && entry.actor === envelope.owner.userId
    && entry.configDigest === envelope.config.configDigest && entry.storeId === envelope.config.storeId;
  return { status: present ? 'REMOTE_PRESENCE_OBSERVED' : 'UNKNOWN', releasesUnknown: false, grantsReplay: false };
}
