import type { KernelStores } from "../stores/kernel-stores.js";
import type { TruthReference } from "../types/truth-reference.js";
import type { StageDeps } from "./deps-context.js";
import { currentReceiptStatus } from "./revocation.js";
import { computeReceiptHash } from "../receipt/receipt-hash.js";

export type ReferenceRejectionReason =
  | "RECEIPT_NOT_FOUND"
  | "RECEIPT_REVOKED"
  | "RECEIPT_HASH_INVALID"
  | "DECISION_NOT_FOUND"
  | "REQUEST_NOT_FOUND"
  | "DECISION_MISMATCH"
  | "VERIFICATION_RESULT_REFS_MISMATCH"
  | "EVIDENCE_REFS_MISMATCH"
  | "OBLIGATION_REFS_MISMATCH"
  | "CONTENT_HASH_MISMATCH"
  | "POLICY_VERSION_MISMATCH"
  | "RULE_VERSION_MISMATCH"
  | "NOT_ACCEPTANCE_DECISION"
  | "FAILED_OBLIGATIONS_NON_EMPTY"
  | "BLOCKING_VERIFICATION_RESULT"
  | "VERIFICATION_RESULT_NOT_FOUND"
  | "INVALID_VALIDITY_INTERVAL";

export interface ReferenceIssuanceResult {
  issued: boolean;
  reference?: TruthReference;
  reasons: ReferenceRejectionReason[];
}

function sameSet(a: string[], b: string[]): boolean {
  if (a.length !== b.length) return false;
  const sortedA = [...a].sort();
  const sortedB = [...b].sort();
  return sortedA.every((value, index) => value === sortedB[index]);
}

/**
 * Implements the T2 contract chain's Decision-Resolution Model and
 * Eligible-Acceptance-Only Issuance Rule (TruthReference section) and
 * Invariant 6 in the invariants file: resolves receipt -> decision ->
 * request, verifies every binding/content/version equality, confirms
 * failed_obligations is empty and no blocking verification result
 * exists, and only then mints a TruthReference. Every missing record,
 * broken link, or mismatch fails closed (Negative Cases NC-04A, NC-04B).
 */
export function issueReference(
  receiptId: string,
  scope: string,
  version: string,
  validFromUtc: string,
  validUntilUtc: string,
  stores: KernelStores,
  deps: StageDeps,
): ReferenceIssuanceResult {
  const receipt = stores.receipts.get(receiptId);
  if (!receipt) {
    return { issued: false, reasons: ["RECEIPT_NOT_FOUND"] };
  }
  if (currentReceiptStatus(receipt, stores) === "REVOKED") {
    return { issued: false, reasons: ["RECEIPT_REVOKED"] };
  }
  const expectedReceiptHash = computeReceiptHash({
    receipt_id: receipt.receipt_id,
    decision_id: receipt.decision_id,
    decision: receipt.decision,
    evaluated_content_hash: receipt.evaluated_content_hash,
    evidence_refs: receipt.evidence_refs,
    obligation_refs: receipt.obligation_refs,
    verification_result_refs: receipt.verification_result_refs,
    policy_version: receipt.policy_version,
    rule_version: receipt.rule_version,
    decided_at_utc: receipt.decided_at_utc,
    issued_at_utc: receipt.issued_at_utc,
    predecessor_receipt_hash: receipt.predecessor_receipt_hash,
  });
  if (receipt.receipt_hash !== expectedReceiptHash) {
    return { issued: false, reasons: ["RECEIPT_HASH_INVALID"] };
  }

  const decision = stores.decisions.get(receipt.decision_id);
  if (!decision) {
    return { issued: false, reasons: ["DECISION_NOT_FOUND"] };
  }

  const request = stores.requests.get(decision.request_id);
  if (!request) {
    return { issued: false, reasons: ["REQUEST_NOT_FOUND"] };
  }

  const reasons: ReferenceRejectionReason[] = [];

  if (receipt.decision !== decision.decision) reasons.push("DECISION_MISMATCH");
  if (!sameSet(receipt.verification_result_refs, decision.verification_result_refs)) {
    reasons.push("VERIFICATION_RESULT_REFS_MISMATCH");
  }
  if (!sameSet(receipt.evidence_refs, request.evidence_refs)) {
    reasons.push("EVIDENCE_REFS_MISMATCH");
  }
  if (!sameSet(receipt.obligation_refs, request.obligation_refs)) {
    reasons.push("OBLIGATION_REFS_MISMATCH");
  }
  if (
    receipt.evaluated_content_hash !== decision.packet_hash ||
    receipt.evaluated_content_hash !== request.packet_hash
  ) {
    reasons.push("CONTENT_HASH_MISMATCH");
  }
  if (
    receipt.policy_version !== decision.policy_version ||
    receipt.policy_version !== request.policy_version
  ) {
    reasons.push("POLICY_VERSION_MISMATCH");
  }
  if (
    receipt.rule_version !== decision.rule_version ||
    receipt.rule_version !== request.rule_version
  ) {
    reasons.push("RULE_VERSION_MISMATCH");
  }
  if (reasons.length > 0) {
    return { issued: false, reasons };
  }

  if (receipt.decision !== "ACCEPT_EVIDENCE_CANDIDATE") {
    return { issued: false, reasons: ["NOT_ACCEPTANCE_DECISION"] };
  }
  if (decision.failed_obligations.length > 0) {
    return { issued: false, reasons: ["FAILED_OBLIGATIONS_NON_EMPTY"] };
  }

  const resolvedVerificationResults = receipt.verification_result_refs.map((id) =>
    stores.verificationResults.get(id),
  );
  if (resolvedVerificationResults.some((result) => !result)) {
    return { issued: false, reasons: ["VERIFICATION_RESULT_NOT_FOUND"] };
  }
  const blockingVerification = resolvedVerificationResults.some(
    (result) => result!.status === "FAIL" || result!.status === "BLOCKED",
  );
  if (blockingVerification) {
    return { issued: false, reasons: ["BLOCKING_VERIFICATION_RESULT"] };
  }

  if (Date.parse(validFromUtc) >= Date.parse(validUntilUtc) || Number.isNaN(Date.parse(validFromUtc)) || Number.isNaN(Date.parse(validUntilUtc))) {
    return { issued: false, reasons: ["INVALID_VALIDITY_INTERVAL"] };
  }

  const reference: TruthReference = {
    reference_id: deps.ids.nextId("TREF"),
    receipt_id: receiptId,
    scope,
    version,
    valid_from_utc: validFromUtc,
    valid_until_utc: validUntilUtc,
    reference_state: "ACTIVE",
  };
  stores.references.insert(reference.reference_id, reference);
  return { issued: true, reference, reasons: [] };
}

/**
 * Computes reference_state at read time per the T2 precedence rule:
 * REVOKED > SUPERSEDED > EXPIRED > ACTIVE. Expiry is derived from
 * valid_until_utc, never a separately stored flag.
 */
export function computeReferenceState(
  reference: TruthReference,
  stores: KernelStores,
  nowUtcIso: string,
  isRevoked: boolean,
  isSuperseded: boolean,
): TruthReference["reference_state"] {
  if (isRevoked) return "REVOKED";
  if (isSuperseded) return "SUPERSEDED";
  if (Date.parse(nowUtcIso) >= Date.parse(reference.valid_until_utc)) return "EXPIRED";
  return "ACTIVE";
}
