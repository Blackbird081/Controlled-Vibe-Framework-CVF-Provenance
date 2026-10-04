// Text Encoding Exception: Vietnamese user-facing copy and matching localization fixtures.
import { describe, expect, it } from 'vitest';
import {
    acknowledgeIntentSpecReview, buildReviewedDraftPacket, createIntentSpecReview,
    getPendingReviewDecisions, isCurrentReviewAcknowledged, synchronizeIntentSpecReview,
    updateReviewDecision, type IntentSpecReviewState,
} from './intent-spec-review';

const values = {
    appName: 'Weekly report', problem: 'Summarize a team report',
    targetUsers: 'Team leads', coreFeatures: 'Collect and review weekly summaries',
    dataNeeds: 'Synthetic reports only', successCriteria: 'Every submitted item is included once',
    constraints: 'No employee scoring', mustPreserve: 'Report column names', outOfScope: 'Sending email',
};
const create = () => createIntentSpecReview(values, 'SOURCE PACKET\nNo email sending.');
const complete = (state: IntentSpecReviewState) => state.decisions.reduce((current, decision) =>
    updateReviewDecision(current, decision.id, { answer: `Explicit decision for ${decision.id}` }), state);

describe('local intent draft review (no AI or execution proof)', () => {
    it('keeps six unresolved business prompts even when all template fields contain text', () => {
        const state = create();
        expect(getPendingReviewDecisions(state).map(item => item.id)).toEqual([
            'workflow', 'access', 'data', 'exceptions', 'acceptance', 'boundaries',
        ]);
        expect(buildReviewedDraftPacket(state, 'en')).toContain('Items still needing a decision: 6');
        expect(buildReviewedDraftPacket(state, 'en')).toContain('No answer yet.');
    });

    it('binds acknowledgement to current content and invalidates it after a user correction', () => {
        const reviewed = acknowledgeIntentSpecReview(complete(create()));
        expect(isCurrentReviewAcknowledged(reviewed)).toBe(true);
        const changed = updateReviewDecision(reviewed, 'access', { answer: 'Only leads may export; contributors may edit their own entries.' });
        expect(isCurrentReviewAcknowledged(changed)).toBe(false);
        const packet = buildReviewedDraftPacket(changed, 'en');
        expect(packet).toContain('Only leads may export');
        expect(packet).not.toContain('Explicit decision for access');
        expect(packet).toContain('Viewed this revision: No');
    });

    it('preserves conflicting text and excludes it from resolved coverage', () => {
        const state = updateReviewDecision(create(), 'data', {
            answer: 'Manager asks for indefinite retention, policy says 30 days.', disposition: 'CONFLICT',
        });
        const viewed = acknowledgeIntentSpecReview(state);
        expect(getPendingReviewDecisions(viewed).some(item => item.id === 'data')).toBe(true);
        expect(buildReviewedDraftPacket(viewed, 'en')).toContain('Status: Conflicting');
        expect(buildReviewedDraftPacket(viewed, 'en')).toContain('policy says 30 days');
    });

    it('requires an explanation for not-applicable and keeps blank answered decisions open', () => {
        const blank = updateReviewDecision(create(), 'exceptions', { disposition: 'NOT_APPLICABLE' });
        expect(getPendingReviewDecisions(blank).some(item => item.id === 'exceptions')).toBe(true);
        const explained = updateReviewDecision(blank, 'exceptions', { answer: 'A manual review is the only operation in this fixture.' });
        expect(getPendingReviewDecisions(explained).some(item => item.id === 'exceptions')).toBe(false);
        const erased = updateReviewDecision(explained, 'exceptions', { answer: '   ', disposition: 'ANSWERED' });
        expect(getPendingReviewDecisions(erased).some(item => item.id === 'exceptions')).toBe(true);
    });

    it('does not resolve a decision with an unresolved placeholder or a bare not-applicable label', () => {
        for (const answer of ['n/a', 'UNKNOWN', 'chưa biết', 'Không áp dụng']) {
            const state = updateReviewDecision(create(), 'data', { answer, disposition: 'NOT_APPLICABLE' });
            expect(getPendingReviewDecisions(state).some(item => item.id === 'data')).toBe(true);
        }
    });

    it('keeps old answers and their original source until affected decisions are reconfirmed', () => {
        const old = acknowledgeIntentSpecReview(complete(create()));
        const changedValues = { ...values, targetUsers: 'All employees' };
        const changed = synchronizeIntentSpecReview(old, changedValues, 'New source packet');
        expect(isCurrentReviewAcknowledged(changed)).toBe(false);
        const access = changed.decisions.find(item => item.id === 'access')!;
        expect(access.answer).toBe('Explicit decision for access');
        expect(access.needsReconfirmation).toBe(true);
        expect(access.sourceValues.targetUsers).toBe('Team leads');
        expect(changed.decisions.find(item => item.id === 'workflow')!.needsReconfirmation).toBe(false);
        const accepted = updateReviewDecision(changed, 'access', { reconfirm: true });
        expect(accepted.decisions.find(item => item.id === 'access')!.sourceValues.targetUsers).toBe('All employees');
        expect(accepted.decisions.find(item => item.id === 'access')!.needsReconfirmation).toBe(false);
        expect(isCurrentReviewAcknowledged(accepted)).toBe(false);
    });

    it('invalidates all answered decisions for an unmapped product identity change', () => {
        const changed = synchronizeIntentSpecReview(complete(create()), { ...values, appName: 'Payroll tool' }, 'New product');
        expect(changed.decisions.every(item => item.needsReconfirmation)).toBe(true);
    });

    it('rebinds review when packet mode, language or context changes without losing business answers', () => {
        const old = acknowledgeIntentSpecReview(complete(create()));
        const changed = synchronizeIntentSpecReview(old, values, 'English full packet with changed context');
        expect(isCurrentReviewAcknowledged(changed)).toBe(false);
        expect(getPendingReviewDecisions(changed)).toHaveLength(0);
        expect(buildReviewedDraftPacket(changed, 'en')).toContain('English full packet with changed context');
    });

    it('does not invalidate on key ordering or no-op changes', () => {
        const state = acknowledgeIntentSpecReview(complete(create()));
        const reordered = Object.fromEntries(Object.entries(values).reverse());
        expect(synchronizeIntentSpecReview(state, reordered, state.packetSource)).toBe(state);
        expect(updateReviewDecision(state, 'access', { answer: 'Explicit decision for access' })).toBe(state);
    });

    it('exports original text, answers, provenance and boundaries as a current draft', () => {
        const state = updateReviewDecision(create(), 'boundaries', { answer: 'Giữ tên cột.\nKhông gửi email.' });
        const packet = buildReviewedDraftPacket(state, 'vi');
        expect(packet).toContain('SOURCE PACKET\nNo email sending.');
        expect(packet).toContain('> Giữ tên cột.\n> Không gửi email.');
        expect(packet).toContain('mustPreserve: Report column names');
        expect(packet).toContain('chưa có actor binding');
        expect(packet).toContain('Các hướng dẫn design/build phía dưới là bước tương lai');
        expect(packet).toContain('Mục còn cần quyết định: 5');
    });
});
