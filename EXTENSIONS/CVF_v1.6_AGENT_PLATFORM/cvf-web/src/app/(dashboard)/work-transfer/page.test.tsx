// Text Encoding Exception: localized Vietnamese user-facing copy follows this file's existing convention.

import React from 'react';
import { cleanup, fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach, afterEach, Mock } from 'vitest';
import WorkTransferPage from './page';

vi.mock('@/components', () => ({
    KnowledgeJourneyNav: ({ currentStep }: { currentStep: number }) => (
        <div data-testid="knowledge-journey-nav">Step {currentStep}</div>
    ),
}));

vi.mock('@/components/KnowledgeJourneyNav', () => ({
    KnowledgeJourneyNav: ({ currentStep }: { currentStep: number }) => (
        <div data-testid="knowledge-journey-nav">Step {currentStep}</div>
    ),
}));

vi.mock('@/components/ArtifactExportPanel', () => ({
    ArtifactExportPanel: ({ initialRequest }: { initialRequest?: unknown }) => (
        <div data-testid="artifact-export-panel" data-request={JSON.stringify(initialRequest ?? null)} />
    ),
}));

let mockLang = 'vi';
vi.mock('@/lib/i18n', () => ({
    useLanguage: () => ({
        language: mockLang,
        setLanguage: vi.fn(),
    }),
}));

const fetchMock = vi.fn() as Mock;
global.fetch = fetchMock;

function respondWith(payload: unknown) {
    fetchMock.mockImplementation(() => Promise.resolve({ json: () => Promise.resolve(payload) }));
}

// Synthetic audit record. The id carries its chronological rank (evt-12 is the newest), so the
// expected sequences below are literal ids and never a second copy of the production comparator.
function rec(rank: number) {
    const hh = String(rank).padStart(2, '0');
    return {
        id: `evt-${hh}`,
        timestamp: `2026-10-01T${hh}:00:00.000Z`,
        action: `ACTION-${hh}`,
        actorId: `actor-${hh}`,
        actorRole: 'admin',
        targetResource: `resource-${hh}`,
        outcome: 'OK',
    };
}

function tied(id: string, hour: number) {
    return { ...rec(hour), id, action: `ACTION-${id}`, actorId: `actor-${id}`, targetResource: `resource-${id}` };
}

function renderedIds(): string[] {
    const list = screen.getByTestId('history-list');
    return within(list)
        .getAllByTestId(/^export-record-/)
        .map(button => (button.getAttribute('data-testid') ?? '').replace('export-record-', ''));
}

const NEWEST_EIGHT_OF_TWELVE = ['evt-12', 'evt-11', 'evt-10', 'evt-09', 'evt-08', 'evt-07', 'evt-06', 'evt-05'];

describe('WorkTransferPage', () => {
    beforeEach(() => {
        mockLang = 'vi';
        fetchMock.mockReset();
        respondWith({ success: true, data: [] });
    });

    afterEach(() => {
        cleanup();
    });

    it('renders KnowledgeJourneyNav at step 5', async () => {
        render(<WorkTransferPage />);
        expect(screen.getByTestId('knowledge-journey-nav').textContent).toBe('Step 5');
        await waitFor(() => expect(global.fetch).toHaveBeenCalled());
    });

    it('renders Vietnamese content correctly', async () => {
        render(<WorkTransferPage />);
        expect(screen.getByText('Bàn giao')).toBeTruthy();
        expect(screen.getByText('Bàn giao công việc cho bước tiếp theo')).toBeTruthy();
        expect(screen.getByDisplayValue('Kiến thức mới đã sẵn sàng để rà soát. Hãy giữ ghi chú nguồn, biên nhận và ranh giới khẳng định cùng nhau.')).toBeTruthy();
        expect(screen.getByText('Đã hoàn tất')).toBeTruthy();
        expect(screen.queryByText('Decision: ALLOW')).toBeNull();
        expect(screen.getByText('Quyết định: ALLOW')).toBeTruthy();
        await waitFor(() => expect(global.fetch).toHaveBeenCalled());
    });

    it('renders English content correctly', async () => {
        mockLang = 'en';
        render(<WorkTransferPage />);
        expect(screen.getByText('Work Transfer')).toBeTruthy();
        expect(screen.getByText('Pass reviewed work forward with less guesswork')).toBeTruthy();
        await waitFor(() => expect(global.fetch).toHaveBeenCalled());
    });

    describe('recent history order (WT-F03)', () => {
        it('shows the newest eight of twelve records, newest first, when the response is ascending', async () => {
            respondWith({ success: true, data: Array.from({ length: 12 }, (_, i) => rec(i + 1)) });
            render(<WorkTransferPage />);
            await screen.findByTestId('history-list');
            expect(renderedIds()).toEqual(NEWEST_EIGHT_OF_TWELVE);
            for (const excluded of ['evt-01', 'evt-02', 'evt-03', 'evt-04']) {
                expect(screen.queryByTestId(`export-record-${excluded}`)).toBeNull();
            }
        });

        it('applies the same order and cap to a shuffled response', async () => {
            const shuffled = [7, 12, 3, 9, 1, 11, 5, 8, 2, 10, 4, 6].map(rec);
            respondWith({ success: true, data: shuffled });
            render(<WorkTransferPage />);
            await screen.findByTestId('history-list');
            expect(renderedIds()).toEqual(NEWEST_EIGHT_OF_TWELVE);
            expect(screen.queryByTestId('export-record-evt-01')).toBeNull();
            expect(screen.queryByTestId('export-record-evt-04')).toBeNull();
        });

        it('keeps the upstream relative order of equal timestamps and applies the cap after ordering', async () => {
            const upstream = [
                tied('a1', 1), tied('a2', 2), tied('a3', 3), tied('a4', 4), tied('a5', 5), tied('a6', 6),
                tied('p1', 7), tied('p2', 7), tied('q1', 8), tied('q2', 8),
            ];
            respondWith({ success: true, data: upstream });
            render(<WorkTransferPage />);
            await screen.findByTestId('history-list');
            expect(renderedIds()).toEqual(['q1', 'q2', 'p1', 'p2', 'a6', 'a5', 'a4', 'a3']);
            expect(screen.queryByTestId('export-record-a2')).toBeNull();
            expect(screen.queryByTestId('export-record-a1')).toBeNull();
        });

        it('does not mutate the response array or its records', async () => {
            const data = [5, 2, 9, 1, 12, 3, 8, 4, 11, 6, 10, 7].map(rec);
            const snapshot = JSON.stringify(data);
            const idsBefore = data.map(item => item.id);
            data.forEach(item => Object.freeze(item));
            Object.freeze(data);
            respondWith({ success: true, data });
            render(<WorkTransferPage />);
            await screen.findByTestId('history-list');
            expect(renderedIds()).toEqual(NEWEST_EIGHT_OF_TWELVE);
            expect(JSON.stringify(data)).toBe(snapshot);
            expect(data.map(item => item.id)).toEqual(idsBefore);
        });

        it('orders fewer than eight, exactly eight, and shows the empty and error states', async () => {
            respondWith({ success: true, data: [rec(2), rec(3), rec(1)] });
            const first = render(<WorkTransferPage />);
            await screen.findByTestId('history-list');
            expect(renderedIds()).toEqual(['evt-03', 'evt-02', 'evt-01']);
            first.unmount();

            respondWith({ success: true, data: [4, 8, 2, 6, 1, 7, 3, 5].map(rec) });
            const second = render(<WorkTransferPage />);
            await screen.findByTestId('history-list');
            expect(renderedIds()).toEqual(['evt-08', 'evt-07', 'evt-06', 'evt-05', 'evt-04', 'evt-03', 'evt-02', 'evt-01']);
            second.unmount();

            respondWith({ success: true, data: [] });
            const third = render(<WorkTransferPage />);
            await screen.findByTestId('history-empty');
            third.unmount();

            respondWith({ success: false, error: 'Unauthorized' });
            const fourth = render(<WorkTransferPage />);
            await screen.findByTestId('history-error');
            fourth.unmount();

            fetchMock.mockImplementation(() => Promise.reject(new Error('network')));
            render(<WorkTransferPage />);
            await screen.findByTestId('history-error');
        });

        it('keeps the English recent-history title with the corrected order', async () => {
            mockLang = 'en';
            respondWith({ success: true, data: Array.from({ length: 12 }, (_, i) => rec(i + 1)) });
            render(<WorkTransferPage />);
            await screen.findByTestId('history-list');
            expect(screen.getByText('Recent transfers')).toBeTruthy();
            expect(renderedIds()[0]).toBe('evt-12');
        });

        it('maps a displayed record to its own export request, then deselects', async () => {
            respondWith({ success: true, data: Array.from({ length: 12 }, (_, i) => rec(i + 1)) });
            render(<WorkTransferPage />);
            await screen.findByTestId('history-list');

            fireEvent.click(screen.getByTestId('export-record-evt-12'));
            const panel = await screen.findByTestId('artifact-export-panel');
            expect(JSON.parse(panel.getAttribute('data-request') ?? 'null')).toEqual({
                title: 'Work Transfer — ACTION-12',
                sourcePath: 'resource-12',
                sourceContent: [
                    '# Work Transfer Record',
                    '',
                    'Action: ACTION-12',
                    'Actor: actor-12 (admin)',
                    'Outcome: OK',
                    'Timestamp: 2026-10-01T12:00:00.000Z',
                    '',
                    '## Claim Boundary',
                    'This is an HTML export of an audit record. It is not final governance proof by itself.',
                ].join('\n'),
                memoryClass: 'FULL_RECORD',
                status: 'OK',
                claimBoundary: 'HTML export of an audit record. Not final governance proof by itself.',
                receiptAnchor: 'transfer-evt-12',
            });

            fireEvent.click(screen.getByTestId('export-record-evt-05'));
            const switched = await screen.findByTestId('artifact-export-panel');
            const request = JSON.parse(switched.getAttribute('data-request') ?? 'null');
            expect(request.title).toBe('Work Transfer — ACTION-05');
            expect(request.receiptAnchor).toBe('transfer-evt-05');
            expect(request.sourcePath).toBe('resource-05');

            fireEvent.click(screen.getByTestId('export-record-evt-05'));
            expect(screen.queryByTestId('artifact-export-panel')).toBeNull();
        });
    });
});
