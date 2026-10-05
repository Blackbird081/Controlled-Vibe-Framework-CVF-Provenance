/** @vitest-environment jsdom */
import { createHash, webcrypto } from 'node:crypto';
import { beforeEach, afterEach, describe, expect, it, vi } from 'vitest';
const verifier = vi.hoisted(() => vi.fn());
vi.mock('./middleware-auth', () => ({ verifySessionCookie: verifier }));
import { resolveIntentSpecActor } from './intent-spec-actor';
import { prepareIntentSpecAcceptance, commitIntentSpecAcceptanceCandidate, type IntentSpecAcceptanceStorePort } from './intent-spec-acceptance';
import { createSpecConfirmationCandidate, MAX_CONFIRMATION_BYTES } from './intent-spec-confirmation';
import { acknowledgeIntentSpecReview, createIntentSpecReview, updateReviewDecision } from './intent-spec-review';

const now = 1791158400000;
const bytes = (text: string) => new TextEncoder().encode(text);
const hash = (input: Uint8Array) => createHash('sha256').update(input).digest('hex');
beforeEach(() => {
    vi.stubGlobal('crypto', webcrypto);
    verifier.mockReset();
    verifier.mockResolvedValue({ userId: 'user_fixture', user: 'Fixture', role: 'developer', orgId: 'org_fixture', teamId: 'team_fixture', expiresAt: now + 60000, authMode: 'session' });
});
afterEach(() => vi.unstubAllGlobals());
async function fixture() {
    let state = createIntentSpecReview({ coreFeatures: 'Synthetic reporting' }, 'Exact source packet\r\nend');
    for (const decision of state.decisions) state = updateReviewDecision(state, decision.id, { answer: `Decision for ${decision.id}` });
    const file = await createSpecConfirmationCandidate(acknowledgeIntentSpecReview(state), 'en', 'Self-declared fixture', new Date(now).toISOString());
    const actor = await resolveIntentSpecActor(new Request('http://localhost/local-contract'), now);
    return { file, actor };
}
type MutablePayload = {
    schema: string; scope: string; extra?: string; reviewer: { verification: string };
    language: string; createdAt: string; draft: string;
    review: { revision: number; acknowledgedRevision: number | null; decisions: {
        id: string; disposition: string; answer: string; needsReconfirmation: boolean;
        sourceValues: Record<string, string>;
    }[] };
};
function modified(text: string, mutate: (payload: MutablePayload) => void): Uint8Array {
    const file = JSON.parse(text);
    mutate(file.payload);
    file.payloadSha256 = hash(bytes(JSON.stringify(file.payload)));
    return bytes(JSON.stringify(file) + '\n');
}
function memoryPort(): IntentSpecAcceptanceStorePort & { records: Map<string, Uint8Array> } {
    const records = new Map<string, Uint8Array>();
    return {
        records,
        async createIfAbsent(id, data) {
            const existing = records.get(id);
            if (existing && hash(existing) !== hash(data)) throw new Error('Conflict');
            records.set(id, new Uint8Array(data));
        },
        async read(id) { return records.get(id) ?? null; },
    };
}

describe('content and store-port contract, with synthetic identities and no durable backend', () => {
    it('binds resolved actor and exact bytes, then verifies readback without claiming durability', async () => {
        const { file, actor } = await fixture();
        const input = bytes(file.fileContent);
        const candidate = prepareIntentSpecAcceptance(actor, input, file.fileSha256, now);
        input.fill(0);
        const store = memoryPort();
        const result = await commitIntentSpecAcceptanceCandidate(actor, candidate, store, () => now);
        expect(result.state).toBe('STORE_PORT_READBACK_VERIFIED');
        expect(result.claimBoundary).toBe('NO_DURABILITY_OR_BUILD_AUTHORITY');
        expect(candidate.state).toBe('PENDING_STORE_COMMIT');
        const saved = JSON.parse(new TextDecoder().decode(store.records.get(candidate.id)));
        expect(saved.actor.userId).toBe('user_fixture');
        expect(saved.sourceFile).toBe(file.fileContent);
        expect(candidate.actor.userId).not.toBe('Self-declared fixture');
        expect(hash(store.records.get(candidate.id)!)).toBe(candidate.id);
    });
    it.each([
        (p: MutablePayload) => { p.schema = 'Other'; }, (p: MutablePayload) => { p.scope = 'BUILD_APPROVED'; },
        (p: MutablePayload) => { p.extra = 'Hidden'; }, (p: MutablePayload) => { p.reviewer.verification = 'AUTHENTICATED'; },
        (p: MutablePayload) => { p.language = 'unknown'; }, (p: MutablePayload) => { p.createdAt = 'yesterday'; },
        (p: MutablePayload) => { p.review.revision = 1.5; }, (p: MutablePayload) => { p.review.acknowledgedRevision = null; },
        (p: MutablePayload) => { p.review.decisions.pop(); }, (p: MutablePayload) => { p.review.decisions[1].id = 'workflow'; },
        (p: MutablePayload) => { p.review.decisions[0].disposition = 'CONFLICT'; },
        (p: MutablePayload) => { p.review.decisions[0].answer = 'unknown'; },
        (p: MutablePayload) => { p.review.decisions[0].needsReconfirmation = true; },
        (p: MutablePayload) => { p.review.decisions[0].sourceValues.coreFeatures = 'Different'; },
        (p: MutablePayload) => { p.draft += '\nHidden override'; },
    ])('rejects semantically invalid candidates even with recomputed self-consistent hashes (%#)', async mutate => {
        const { file, actor } = await fixture();
        const input = modified(file.fileContent, mutate);
        expect(() => prepareIntentSpecAcceptance(actor, input, hash(input), now)).toThrow('INVALID_SPEC_REVIEW_FILE');
    });
    it('rejects malformed/duplicate JSON, bad UTF-8, BOM, wrong file identity and tampered payload hash', async () => {
        const { file, actor } = await fixture();
        const input = bytes(file.fileContent);
        expect(() => prepareIntentSpecAcceptance(actor, input, '0'.repeat(64), now)).toThrow();
        const tampered = JSON.parse(file.fileContent); tampered.payloadSha256 = '0'.repeat(64);
        for (const data of [bytes('{'), bytes(file.fileContent.replace('{"payload":', '{"payload":null,"payload":')),
            new Uint8Array([0xff]), bytes('\uFEFF' + file.fileContent), bytes(JSON.stringify(tampered) + '\n')]) {
            expect(() => prepareIntentSpecAcceptance(actor, data, hash(data), now)).toThrow('INVALID_SPEC_REVIEW_FILE');
        }
    });
    it('rejects oversized input without parsing it', async () => {
        const { actor } = await fixture();
        const input = new Uint8Array(MAX_CONFIRMATION_BYTES + 1);
        const parser = vi.spyOn(JSON, 'parse');
        expect(() => prepareIntentSpecAcceptance(actor, input, '0'.repeat(64), now)).toThrow('INVALID_SPEC_REVIEW_FILE');
        expect(parser).not.toHaveBeenCalled();
        parser.mockRestore();
    });
    it('rejects forged candidate/actor objects and another valid actor context before calling I/O', async () => {
        const { file, actor } = await fixture();
        const candidate = prepareIntentSpecAcceptance(actor, bytes(file.fileContent), file.fileSha256, now);
        const store = { createIfAbsent: vi.fn(), read: vi.fn() };
        await expect(commitIntentSpecAcceptanceCandidate(actor, { ...candidate }, store, () => now)).rejects.toThrow('OWNED_ACTOR_CANDIDATE_REQUIRED');
        const other = await resolveIntentSpecActor(new Request('http://localhost/local-contract'), now);
        await expect(commitIntentSpecAcceptanceCandidate(other, candidate, store, () => now)).rejects.toThrow('OWNED_ACTOR_CANDIDATE_REQUIRED');
        expect(store.createIfAbsent).not.toHaveBeenCalled();
    });
    it.each(['write', 'read', 'missing', 'changed', 'expired'])('never returns success when %s fails', async failure => {
        const { file, actor } = await fixture();
        const candidate = prepareIntentSpecAcceptance(actor, bytes(file.fileContent), file.fileSha256, now);
        const store = memoryPort();
        if (failure === 'write') store.createIfAbsent = async () => { throw new Error('Write failed'); };
        if (failure === 'read') store.read = async () => { throw new Error('Read failed'); };
        if (failure === 'missing') store.read = async () => null;
        if (failure === 'changed') store.read = async id => { const result = store.records.get(id)!; result[0] ^= 1; return result; };
        let calls = 0;
        const clock = () => failure === 'expired' && calls++ > 0 ? now + 60000 : now;
        await expect(commitIntentSpecAcceptanceCandidate(actor, candidate, store, clock)).rejects.toThrow('STORE_COMMIT_UNCONFIRMED');
        expect(candidate.state).toBe('PENDING_STORE_COMMIT');
    });
    it('keeps owned expected bytes when an adapter mutates the write argument', async () => {
        const { file, actor } = await fixture();
        const candidate = prepareIntentSpecAcceptance(actor, bytes(file.fileContent), file.fileSha256, now);
        const store = memoryPort();
        const write = store.createIfAbsent.bind(store);
        store.createIfAbsent = async (id, data) => { await write(id, data); data.fill(0); };
        await expect(commitIntentSpecAcceptanceCandidate(actor, candidate, store, () => now)).resolves.toMatchObject({ state: 'STORE_PORT_READBACK_VERIFIED' });
    });
});
