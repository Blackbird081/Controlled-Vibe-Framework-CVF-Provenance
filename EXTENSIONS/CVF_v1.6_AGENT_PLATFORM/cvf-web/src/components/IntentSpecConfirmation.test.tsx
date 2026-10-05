// Text Encoding Exception: Vietnamese localization assertion for user-facing copy.
/** @vitest-environment jsdom */
import { webcrypto } from 'node:crypto';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { act, cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react';
import { IntentSpecConfirmation } from './IntentSpecConfirmation';
import { acknowledgeIntentSpecReview, createIntentSpecReview, updateReviewDecision } from '@/lib/intent-spec-review';
import { MAX_CONFIRMATION_BYTES } from '@/lib/intent-spec-confirmation';
import * as confirmation from '@/lib/intent-spec-confirmation';

beforeEach(() => vi.stubGlobal('crypto', webcrypto));
afterEach(() => { cleanup(); vi.unstubAllGlobals(); vi.restoreAllMocks(); });
function reviewed() {
    let state = createIntentSpecReview({}, 'Synthetic current packet');
    for (const decision of state.decisions) state = updateReviewDecision(state, decision.id, { answer: `Decision ${decision.id}` });
    return acknowledgeIntentSpecReview(state);
}
function open() {
    fireEvent.click(screen.getByRole('button', { name: 'Keep a review copy for comparison' }));
    fireEvent.change(screen.getByLabelText('Reviewer name (self-declared)'), { target: { value: 'Reviewer' } });
}
async function create() {
    fireEvent.click(screen.getByRole('button', { name: 'Create file for reviewed revision' }));
    await screen.findByRole('button', { name: 'Download review file' });
}
function select(content: string, size = content.length, arrayBuffer = async () => new TextEncoder().encode(content).buffer) {
    fireEvent.change(screen.getByLabelText('Select saved file for comparison'), {
        target: { files: [{ size, arrayBuffer }] },
    });
}

describe('portable review UI and failure handling', () => {
    it('requires current review and an explicit reviewer name', () => {
        render(<IntentSpecConfirmation review={createIntentSpecReview({}, 'draft')} language="en" />);
        open();
        expect((screen.getByRole('button', { name: 'Create file for reviewed revision' }) as HTMLButtonElement).disabled).toBe(true);
    });
    it('distinguishes download request from exact saved-file readback and rejects mismatches', async () => {
        const state = reviewed();
        render(<IntentSpecConfirmation review={state} language="en" />); open(); await create();
        vi.spyOn(URL, 'createObjectURL').mockReturnValue('blob:test');
        vi.spyOn(URL, 'revokeObjectURL').mockImplementation(() => {});
        vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(() => {});
        fireEvent.click(screen.getByRole('button', { name: 'Download review file' }));
        expect(screen.getByRole('status').textContent).toContain('Download requested');
        // Capture the actual exported candidate; a recreated timestamp would identify another file.
        const blob = vi.mocked(URL.createObjectURL).mock.calls[0][0] as Blob;
        const content = await new Promise<string>((resolve, reject) => {
            const reader = new FileReader(); reader.onload = () => resolve(reader.result as string); reader.onerror = reject; reader.readAsText(blob);
        });
        select(content);
        await waitFor(() => expect(screen.getByRole('status').textContent).toContain('matches this exact'));
        select(content.replace('Reviewer', 'Different'));
        await waitFor(() => expect(screen.getByRole('status').textContent).toContain('does not match'));
    });
    it('invalidates files immediately on reviewer or revision change, including returning to the previous name', async () => {
        const state = reviewed();
        const { rerender } = render(<IntentSpecConfirmation review={state} language="en" />); open(); await create();
        const name = screen.getByLabelText('Reviewer name (self-declared)');
        fireEvent.change(name, { target: { value: 'Other' } });
        fireEvent.change(name, { target: { value: 'Reviewer' } });
        expect(screen.queryByRole('button', { name: 'Download review file' })).toBeNull();
        await create();
        rerender(<IntentSpecConfirmation review={updateReviewDecision(state, 'data', { answer: 'Changed' })} language="en" />);
        expect(screen.queryByRole('button', { name: 'Download review file' })).toBeNull();
    });
    it('rejects oversized and failed reads before reporting success', async () => {
        render(<IntentSpecConfirmation review={reviewed()} language="en" />); open(); await create();
        const read = vi.fn(async () => new ArrayBuffer(0));
        select('', MAX_CONFIRMATION_BYTES + 1, read);
        await screen.findByText('Could not verify the file. This revision is unconfirmed.');
        expect(read).not.toHaveBeenCalled();
        select('', 1, async () => { throw new Error('Read failed'); });
        await screen.findByText('Could not verify the file. This revision is unconfirmed.');
    });
    it('does not publish an async hash result after the language changes', async () => {
        const state = reviewed();
        const candidate = await confirmation.createSpecConfirmationCandidate(state, 'en', 'Reviewer');
        let release!: (value: typeof candidate) => void;
        vi.spyOn(confirmation, 'createSpecConfirmationCandidate').mockImplementation(() => new Promise(resolve => { release = resolve; }));
        const { rerender } = render(<IntentSpecConfirmation review={state} language="en" />); open();
        fireEvent.click(screen.getByRole('button', { name: 'Create file for reviewed revision' }));
        rerender(<IntentSpecConfirmation review={state} language="vi" />);
        await act(async () => release(candidate));
        expect(screen.queryByRole('button', { name: 'Tải gói review' })).toBeNull();
        expect(screen.getByText(/Tên này chưa được xác thực/)).toBeDefined();
    });
    it('cannot carry a readback success across a concurrent reviewer edit', async () => {
        render(<IntentSpecConfirmation review={reviewed()} language="en" />); open(); await create();
        let release!: (value: boolean) => void;
        const verifier = vi.spyOn(confirmation, 'verifySpecConfirmationReadback')
            .mockImplementation(() => new Promise(resolve => { release = resolve; }));
        select('fixture');
        await waitFor(() => expect(verifier).toHaveBeenCalled());
        fireEvent.change(screen.getByLabelText('Reviewer name (self-declared)'), { target: { value: 'Other' } });
        await act(async () => release(true));
        expect(screen.queryByRole('status')).toBeNull();
    });
    it('reports hash failure without exposing a candidate', async () => {
        vi.stubGlobal('crypto', { subtle: { digest: () => Promise.reject(new Error('Hash unavailable')) } });
        render(<IntentSpecConfirmation review={reviewed()} language="en" />); open();
        fireEvent.click(screen.getByRole('button', { name: 'Create file for reviewed revision' }));
        await screen.findByText('Could not create the file. Check the review and try again.');
        expect(screen.queryByRole('button', { name: 'Download review file' })).toBeNull();
    });
    it('does not label failed downloads as saved', async () => {
        render(<IntentSpecConfirmation review={reviewed()} language="en" />); open(); await create();
        vi.spyOn(URL, 'createObjectURL').mockImplementation(() => { throw new Error('Download unavailable'); });
        fireEvent.click(screen.getByRole('button', { name: 'Download review file' }));
        expect(screen.getByRole('status').textContent).toContain('No saved-file confirmation');
    });
});
