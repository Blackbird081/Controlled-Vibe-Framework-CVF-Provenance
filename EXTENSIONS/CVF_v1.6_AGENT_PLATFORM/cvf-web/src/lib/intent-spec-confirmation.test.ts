/** @vitest-environment jsdom */
import { webcrypto } from 'node:crypto';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { acknowledgeIntentSpecReview, createIntentSpecReview, updateReviewDecision } from './intent-spec-review';
import { createSpecConfirmationCandidate, MAX_CONFIRMATION_BYTES, reviewBindingKey, verifySpecConfirmationReadback } from './intent-spec-confirmation';

beforeEach(() => vi.stubGlobal('crypto', webcrypto));
function reviewed() {
    let state = createIntentSpecReview({ problem: 'Synthetic fixture' }, 'Exact draft\r\nend');
    for (const decision of state.decisions) state = updateReviewDecision(state, decision.id, { answer: `Decision for ${decision.id}` });
    return acknowledgeIntentSpecReview(state);
}
const bytes = (value: string) => new TextEncoder().encode(value);

describe('portable content binding, without authenticated acceptance or storage claims', () => {
    it('binds exact review, draft, self-declared actor, language and time and verifies readback', async () => {
        const state = reviewed();
        const candidate = await createSpecConfirmationCandidate(state, 'en', 'Test reviewer', '2026-10-05T00:00:00.000Z');
        const file = JSON.parse(candidate.fileContent);
        expect(file.payload.review).toEqual(state);
        expect(file.payload.draft).toContain('Exact draft\r\nend');
        expect(file.payload.reviewer.verification).toBe('SELF_DECLARED');
        expect(file.payload.scope).toBe('SPEC_REVIEW_ONLY_NO_BUILD_AUTHORITY');
        expect(file.payloadSha256).toMatch(/^[a-f0-9]{64}$/);
        expect(await verifySpecConfirmationReadback(candidate, bytes(candidate.fileContent))).toBe(true);
        expect(Object.isFrozen(candidate)).toBe(true);
    });
    it('refuses pending, stale viewing, missing actor and oversized payloads', async () => {
        await expect(createSpecConfirmationCandidate(createIntentSpecReview({}, 'draft'), 'en', 'Reviewer')).rejects.toThrow('CURRENT_REVIEW_REQUIRED');
        const state = reviewed();
        await expect(createSpecConfirmationCandidate(state, 'en', ' ')).rejects.toThrow('REVIEWER_REQUIRED');
        await expect(createSpecConfirmationCandidate({ ...state, acknowledgedRevision: null }, 'en', 'Reviewer')).rejects.toThrow('CURRENT_REVIEW_REQUIRED');
        await expect(createSpecConfirmationCandidate({ ...state, packetSource: 'x'.repeat(MAX_CONFIRMATION_BYTES) }, 'en', 'Reviewer')).rejects.toThrow('FILE_TOO_LARGE');
    });
    it('captures ownership before async hashing, so subsequent caller edits do not alter the file', async () => {
        const state = reviewed();
        const promise = createSpecConfirmationCandidate(state, 'en', 'Reviewer');
        state.values.problem = 'Caller mutation';
        state.decisions[0].answer = 'Caller mutation';
        const candidate = await promise;
        expect(candidate.fileContent).not.toContain('Caller mutation');
        expect(candidate.bindingKey).not.toBe(reviewBindingKey(state, 'en', 'Reviewer'));
    });
    it('rejects changed bytes, newline conversion, malformed JSON and another reviewer candidate', async () => {
        const candidate = await createSpecConfirmationCandidate(reviewed(), 'en', 'Reviewer');
        const other = await createSpecConfirmationCandidate(reviewed(), 'en', 'Other reviewer');
        for (const text of [candidate.fileContent.replace('Reviewer', 'Intruder'), candidate.fileContent.trim(), '{', other.fileContent]) {
            expect(await verifySpecConfirmationReadback(candidate, bytes(text))).toBe(false);
        }
    });
    it('includes state content and language in the key rather than trusting the same revision', () => {
        const state = reviewed();
        const key = reviewBindingKey(state, 'en', 'Reviewer');
        expect(reviewBindingKey({ ...state, packetSource: 'Different bytes' }, 'en', 'Reviewer')).not.toBe(key);
        expect(reviewBindingKey(state, 'vi', 'Reviewer')).not.toBe(key);
    });
    it('fails if cryptographic hashing is unavailable', async () => {
        vi.stubGlobal('crypto', { subtle: { digest: () => Promise.reject(new Error('Unavailable')) } });
        await expect(createSpecConfirmationCandidate(reviewed(), 'en', 'Reviewer')).rejects.toThrow('Unavailable');
    });
});
