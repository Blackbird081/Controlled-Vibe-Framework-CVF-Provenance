/** Portable review candidate only; no authenticated acceptance or storage guarantee. */
import {
    buildReviewedDraftPacket, getPendingReviewDecisions, getReviewOpenItems, isCurrentReviewAcknowledged,
    type IntentSpecReviewState, type ReviewLanguage,
} from './intent-spec-review';
import { validateOpenItemSet, validateStoredOpenItem } from './intent-spec-open-items';

export const CANDIDATE_SCHEMA_V1 = 'cvf.intentSpecReviewCandidate.v1';
/** Used only when the user declared at least one open item; a state with none keeps the v1 bytes. */
export const CANDIDATE_SCHEMA_V2 = 'cvf.intentSpecReviewCandidate.v2';

export const MAX_CONFIRMATION_BYTES = 2 * 1024 * 1024;

export interface SpecConfirmationCandidate {
    readonly bindingKey: string;
    readonly fileContent: string;
    readonly fileSha256: string;
    readonly revision: number;
}

/** Exact current state, including acknowledgement, is bound rather than revision alone. */
export function reviewBindingKey(state: IntentSpecReviewState, language: ReviewLanguage, reviewer: string): string {
    return JSON.stringify({ state, language, reviewer: reviewer.trim() });
}

async function sha256(bytes: Uint8Array): Promise<string> {
    const owned = new Uint8Array(bytes);
    const digest = await globalThis.crypto.subtle.digest('SHA-256', owned.buffer);
    return Array.from(new Uint8Array(digest), byte => byte.toString(16).padStart(2, '0')).join('');
}

export async function createSpecConfirmationCandidate(
    state: IntentSpecReviewState, language: ReviewLanguage, reviewer: string,
    createdAt = new Date().toISOString(),
): Promise<SpecConfirmationCandidate> {
    if (!reviewer.trim() || reviewer.trim().length > 120) throw new Error('REVIEWER_REQUIRED');
    if (!isCurrentReviewAcknowledged(state) || getPendingReviewDecisions(state).length) {
        throw new Error('CURRENT_REVIEW_REQUIRED');
    }
    const items = getReviewOpenItems(state);
    // Items must be fresh and valid; the acceptance verifier applies the same rules to the saved bytes.
    if (items.length && (validateOpenItemSet(items)
        || items.some(item => validateStoredOpenItem(item, state.values)))) throw new Error('CURRENT_REVIEW_REQUIRED');
    // Copy to immutable strings before the first await; caller edits cannot affect the snapshot.
    const bindingKey = reviewBindingKey(state, language, reviewer);
    const payload = JSON.stringify({
        schema: items.length ? CANDIDATE_SCHEMA_V2 : CANDIDATE_SCHEMA_V1,
        scope: 'SPEC_REVIEW_ONLY_NO_BUILD_AUTHORITY',
        reviewer: { name: reviewer.trim(), verification: 'SELF_DECLARED' },
        createdAt, language, review: JSON.parse(JSON.stringify(state)),
        draft: buildReviewedDraftPacket(state, language),
    });
    const payloadBytes = new TextEncoder().encode(payload);
    if (payloadBytes.length > MAX_CONFIRMATION_BYTES - 1024) throw new Error('FILE_TOO_LARGE');
    const revision = state.revision;
    const payloadSha256 = await sha256(payloadBytes);
    const fileContent = JSON.stringify({ payload: JSON.parse(payload), payloadSha256 }) + '\n';
    const fileSha256 = await sha256(new TextEncoder().encode(fileContent));
    return Object.freeze({ bindingKey, fileContent, fileSha256, revision });
}

/** Verify selected bytes against this session's owned expected candidate; never adopt imports. */
export async function verifySpecConfirmationReadback(
    candidate: SpecConfirmationCandidate, received: Uint8Array,
): Promise<boolean> {
    const owned = new Uint8Array(received);
    const expected = new TextEncoder().encode(candidate.fileContent);
    if (owned.length > MAX_CONFIRMATION_BYTES || owned.length !== expected.length) return false;
    if (!owned.every((byte, index) => byte === expected[index])) return false;
    return await sha256(owned) === candidate.fileSha256;
}
