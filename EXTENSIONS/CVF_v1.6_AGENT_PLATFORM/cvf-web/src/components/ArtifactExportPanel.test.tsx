/**
 * @vitest-environment jsdom
 */
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

import { ArtifactExportPanel, type ArtifactExportResult } from './ArtifactExportPanel';

const EXPORT_RESULT: ArtifactExportResult = {
  html: '<!doctype html><html lang="en"><body><main><h1>Review Packet</h1></main></body></html>',
  filename: 'review-packet.html',
  receiptAnchor: 'receipt-review-packet',
  generatedAt: '2026-05-16T10:00:00.000Z',
  verification: [
    { label: 'Source path recorded', passed: true, detail: 'docs/reviews/review-packet.md' },
    { label: 'Claim Boundary visible', passed: true, detail: 'HTML presentation candidate only.' },
  ],
};

describe('ArtifactExportPanel', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({
      ok: true,
      status: 200,
      json: async () => ({ success: true, data: EXPORT_RESULT }),
    }));

    Object.defineProperty(navigator, 'clipboard', {
      value: { writeText: vi.fn().mockResolvedValue(undefined) },
      configurable: true,
    });
  });

  afterEach(() => {
    vi.unstubAllGlobals();
    vi.restoreAllMocks();
  });

  it('renders the English-only HTML export surface', () => {
    render(<ArtifactExportPanel />);

    expect(screen.getByText('Artifact Export')).toBeTruthy();
    expect(screen.getByText(/HTML only/i)).toBeTruthy();
    expect(screen.getByLabelText('Title')).toBeTruthy();
    expect(screen.getByLabelText('Source path')).toBeTruthy();
    expect(screen.getByText('Generate HTML')).toBeTruthy();
    expect(document.body.textContent).not.toMatch(new RegExp('[\\u00C0-\\u1EF9]'));
  });

  it('posts the artifact source and renders the returned candidate', async () => {
    const onGenerated = vi.fn();
    render(<ArtifactExportPanel onGenerated={onGenerated} />);

    fireEvent.change(screen.getByLabelText('Title'), {
      target: { value: 'Review Packet' },
    });
    fireEvent.click(screen.getByText('Generate HTML'));

    await waitFor(() => {
      expect(fetch).toHaveBeenCalledWith('/api/artifacts/export', expect.objectContaining({
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      }));
      expect(onGenerated).toHaveBeenCalledWith(EXPORT_RESULT);
    });

    const requestBody = JSON.parse(String((fetch as unknown as { mock: { calls: unknown[][] } }).mock.calls[0][1].body));
    expect(requestBody.title).toBe('Review Packet');
    expect(requestBody.claimBoundary).toMatch(/HTML presentation candidate/i);
    expect(screen.getByText('#receipt-review-packet')).toBeTruthy();
    expect(screen.getByTitle('Sandboxed preview')).toBeTruthy();
    expect(screen.getByText('Source path recorded')).toBeTruthy();
    expect(screen.getByText('2/2')).toBeTruthy();
  });

  it('copies generated HTML after a candidate is available', async () => {
    render(<ArtifactExportPanel initialResult={EXPORT_RESULT} />);

    fireEvent.click(screen.getByText('Copy HTML'));

    await waitFor(() => {
      expect(navigator.clipboard.writeText).toHaveBeenCalledWith(EXPORT_RESULT.html);
      expect(screen.getByText('Copied')).toBeTruthy();
    });
  });
});
