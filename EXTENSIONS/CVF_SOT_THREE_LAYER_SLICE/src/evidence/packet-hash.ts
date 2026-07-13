import { createHash } from "node:crypto";
import type { RefineryPacket } from "cvf-refinery";

/**
 * Refinery's RefineryPacket carries no top-level content_hash field; the
 * Kernel's RefineryPacketRef.content_hash and EvaluateInput.packetHash are
 * a binding identity the caller must supply. This is pure type mapping and
 * serialization over Refinery's already-produced packet fields - it adds
 * no normalization, conflict resolution, or trust judgment of its own.
 */
export function packetContentHash(packet: RefineryPacket): string {
  const canonicalize = (value: unknown): unknown => {
    if (Array.isArray(value)) return value.map(canonicalize);
    if (value !== null && typeof value === "object") {
      return Object.fromEntries(
        Object.entries(value as Record<string, unknown>)
          .sort(([left], [right]) => left.localeCompare(right))
          .map(([key, item]) => [key, canonicalize(item)]),
      );
    }
    return value;
  };
  return `sha256:${createHash("sha256").update(JSON.stringify(canonicalize(packet))).digest("hex")}`;
}
