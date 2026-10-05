// Text Encoding Exception: Vietnamese user-facing copy and matching localization fixtures.
/** @vitest-environment jsdom */
import { afterEach, describe, expect, it, vi } from 'vitest';
import { cleanup, fireEvent, render, screen, within } from '@testing-library/react';
const auth = vi.hoisted(() => ({
    session: { status: 'authenticated', data: { user: { userId: 'user_a', orgId: 'org_a', teamId: 'team_a' }, expires: '2999-01-01T00:00:00.000Z' } } as
        { status: string; data: { user: { userId: string; orgId: string; teamId: string }; expires: string } | null },
}));
vi.mock('next-auth/react', () => ({ useSession: () => auth.session }));
import { IntentSpecReview, useIntentSpecReview } from './IntentSpecReview';
import type { ReviewLanguage } from '@/lib/intent-spec-review';

afterEach(cleanup);
const values = { targetUsers: 'Team leads', dataNeeds: 'Synthetic report entries', coreFeatures: 'Compile weekly reports' };

function Harness({ input = values, language = 'en', packet = 'Initial packet', templateId = 'app_builder_complete' }: {
    input?: Record<string, string>; language?: ReviewLanguage; packet?: string; templateId?: string;
}) {
    const draft = useIntentSpecReview(templateId, input, packet, language);
    return <>
        {draft.review && <IntentSpecReview review={draft.review} language={language}
            onUpdate={draft.update} onAcknowledge={draft.acknowledge} />}
        <textarea aria-label="Exported draft" readOnly value={draft.spec} />
        <button disabled={!draft.canContinue}>Continue draft handoff</button>
    </>;
}

describe('requirements review UI structure and local interactions', () => {
    it('shows three prompts without discarding the remaining unknowns', () => {
        render(<Harness />);
        expect(screen.getAllByRole('textbox')).toHaveLength(4);
        expect(screen.getByRole('status').textContent).toContain('6 items need a decision');
        expect((screen.getByLabelText('Exported draft') as HTMLTextAreaElement).value).toContain('exceptions');
        fireEvent.click(screen.getByRole('button', { name: 'Show all 6 questions' }));
        expect(screen.getAllByRole('textbox')).toHaveLength(7);
        fireEvent.click(screen.getByRole('button', { name: 'Show fewer' }));
        expect(screen.getByRole('status').textContent).toContain('6 items need a decision');
    });

    it('keeps partial viewing separate from complete answers and resets viewing after an edit', () => {
        render(<Harness />);
        fireEvent.click(screen.getByRole('button', { name: 'I have viewed this draft' }));
        expect(screen.getByRole('status').textContent).toContain('Viewed this revision');
        expect((screen.getByRole('button', { name: 'Continue draft handoff' }) as HTMLButtonElement).disabled).toBe(true);
        fireEvent.change(screen.getByLabelText('Who may view, edit or export information, and who may not?'), { target: { value: 'Only leads may export.' } });
        expect(screen.getByRole('status').textContent).toContain('Not viewed yet');
        expect((screen.getByLabelText('Exported draft') as HTMLTextAreaElement).value).toContain('Only leads may export.');
    });

    it('retains a stale answer visibly when related brief fields change', () => {
        const { rerender } = render(<Harness />);
        fireEvent.change(screen.getByLabelText('Who may view, edit or export information, and who may not?'), { target: { value: 'Lead-only access.' } });
        fireEvent.click(screen.getByRole('button', { name: 'I have viewed this draft' }));
        rerender(<Harness input={{ ...values, targetUsers: 'All employees' }} packet="Updated packet" />);
        expect(screen.getByRole('status').textContent).toContain('Not viewed yet');
        expect((screen.getByLabelText('Who may view, edit or export information, and who may not?') as HTMLTextAreaElement).value).toBe('Lead-only access.');
        expect(screen.getByText('Related brief information changed. The old answer is kept for you to review.')).toBeDefined();
        fireEvent.click(screen.getByRole('button', { name: 'Keep answer for new revision' }));
        expect(screen.queryByText('Related brief information changed. The old answer is kept for you to review.')).toBeNull();
    });

    it('requires a not-applicable reason, preserves conflicts and localizes the controls', () => {
        const { rerender } = render(<Harness />);
        const section = screen.getByRole('region', { name: 'Requirements review' });
        fireEvent.change(within(section).getAllByRole('combobox')[0], { target: { value: 'NOT_APPLICABLE' } });
        expect(screen.getByText('Please give a reason why this does not apply.')).toBeDefined();
        fireEvent.change(screen.getByLabelText('What steps does the user take from start to completion?'), { target: { value: 'This fixture uses manual review only.' } });
        expect(screen.queryByText('Please give a reason why this does not apply.')).toBeNull();
        fireEvent.change(within(section).getAllByRole('combobox')[1], { target: { value: 'CONFLICT' } });
        fireEvent.change(screen.getByLabelText('Who may view, edit or export information, and who may not?'), { target: { value: 'Two owners disagree.' } });
        expect((screen.getByLabelText('Exported draft') as HTMLTextAreaElement).value).toContain('Status: Conflicting');
        rerender(<Harness language="vi" packet="Bản tiếng Việt" />);
        expect(screen.getByRole('region', { name: 'Review yêu cầu' })).toBeDefined();
        expect(screen.getByRole('button', { name: 'Tôi đã xem bản nháp này' })).toBeDefined();
        expect(screen.getByText(/Bản review chỉ nằm trong phiên này/)).toBeDefined();
    });

    it('requires all explicit decisions and current viewing before draft continuation', () => {
        render(<Harness />);
        fireEvent.click(screen.getByRole('button', { name: 'Show all 6 questions' }));
        const region = screen.getByRole('region', { name: 'Requirements review' });
        within(region).getAllByRole('textbox').forEach((input, index) => {
            fireEvent.change(input, { target: { value: `User decision ${index}` } });
        });
        const button = screen.getByRole('button', { name: 'Continue draft handoff' }) as HTMLButtonElement;
        expect(button.disabled).toBe(true);
        fireEvent.click(screen.getByRole('button', { name: 'I have viewed this draft' }));
        expect(button.disabled).toBe(false);
    });

    it('leaves unrelated templates and their packet untouched', () => {
        render(<Harness templateId="unrelated" packet="Legacy packet exactly" />);
        expect(screen.queryByRole('region')).toBeNull();
        expect((screen.getByLabelText('Exported draft') as HTMLTextAreaElement).value).toBe('Legacy packet exactly');
        expect((screen.getByRole('button', { name: 'Continue draft handoff' }) as HTMLButtonElement).disabled).toBe(false);
    });
});
