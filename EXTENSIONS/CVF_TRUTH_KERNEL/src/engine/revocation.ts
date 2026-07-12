import type { KernelStores } from "../stores/kernel-stores.js";
import type { TruthReceipt } from "../types/truth-receipt.js";

export type RevocationRejectionReason = "RECEIPT_NOT_FOUND" | "RECEIPT_NOT_ISSUED";

export interface RevocationResult {
  revoked: boolean;
  reasons: RevocationRejectionReason[];
}

/**
 * Revokes an ISSUED receipt. The ImmutableStore is append-only and
 * forbids overwriting an existing key, so revocation is recorded as a
 * new entry in stores.revocations keyed by receipt_id rather than
 * mutating the original receipt snapshot. currentReceiptStatus()
 * consults this store to compute effective status.
 */
export function revokeReceipt(receiptId: string, stores: KernelStores): RevocationResult {
  const receipt = stores.receipts.get(receiptId);
  if (!receipt) {
    return { revoked: false, reasons: ["RECEIPT_NOT_FOUND"] };
  }
  if (receipt.status !== "ISSUED") {
    return { revoked: false, reasons: ["RECEIPT_NOT_ISSUED"] };
  }
  stores.revocations.insert(receiptId, { receipt_id: receiptId });
  return { revoked: true, reasons: [] };
}

export function isReceiptRevoked(receiptId: string, stores: KernelStores): boolean {
  return stores.revocations.has(receiptId);
}

export function currentReceiptStatus(
  receipt: TruthReceipt,
  stores: KernelStores,
): TruthReceipt["status"] {
  if (isReceiptRevoked(receipt.receipt_id, stores)) return "REVOKED";
  return receipt.status;
}
