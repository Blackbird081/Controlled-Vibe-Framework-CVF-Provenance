/**
 * @vitest-environment jsdom
 */
// Text Encoding Exception: asserts against localized Vietnamese copy from ArtifactExportPanel's existing convention.
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, onTestFinished, vi } from 'vitest';

import { ArtifactExportPanel, type ArtifactExportResult } from './ArtifactExportPanel';

let mockLanguage: 'en' | 'vi' = 'en';

vi.mock('@/lib/i18n', () => ({
  useLanguage: () => ({ language: mockLanguage }),
}));

const EXPORT_RESULT: ArtifactExportResult = {
  html: '<!doctype html><html lang="en"><body><main><h1>Review Packet</h1></main></body></html>',
  filename: 'review-packet.html',
  receiptAnchor: 'receipt-review-packet',
  generatedAt: '2026-05-16T10:00:00.000Z',
  governanceState: 'DRAFT_UNACCEPTED',
  verification: [
    { label: 'Source reference recorded', passed: true, detail: 'docs/reviews/review-packet.md' },
    { label: 'Review boundary visible', passed: true, detail: 'HTML review packet only.' },
  ],
};

describe('ArtifactExportPanel', () => {
  beforeEach(() => {
    mockLanguage = 'en';
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

  it('renders the English HTML export surface', () => {
    render(<ArtifactExportPanel />);

    expect(screen.getByText('Review Packet Export')).toBeTruthy();
    expect(screen.getByText(/HTML only/i)).toBeTruthy();
    expect(screen.getByLabelText('Title')).toBeTruthy();
    expect(screen.getByLabelText('Source reference')).toBeTruthy();
    expect(screen.getByText('Build HTML')).toBeTruthy();
  });

  it('renders Vietnamese labels when the app language is Vietnamese', () => {
    mockLanguage = 'vi';
    render(<ArtifactExportPanel />);

    expect(screen.getByText('Xuất gói rà soát')).toBeTruthy();
    expect(screen.getByLabelText('Tiêu đề')).toBeTruthy();
    expect(screen.getByText('Tạo HTML')).toBeTruthy();
  });

  it('posts the artifact source and renders the returned candidate', async () => {
    const onGenerated = vi.fn();
    render(<ArtifactExportPanel onGenerated={onGenerated} />);

    fireEvent.change(screen.getByLabelText('Title'), {
      target: { value: 'Review Packet' },
    });
    fireEvent.click(screen.getByText('Build HTML'));

    await waitFor(() => {
      expect(fetch).toHaveBeenCalledWith('/api/artifacts/export', expect.objectContaining({
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      }));
      expect(onGenerated).toHaveBeenCalledWith(EXPORT_RESULT);
    });

    const fetchCalls = (fetch as unknown as { mock: { calls: Array<[string, RequestInit]> } }).mock.calls;
    const requestBody = JSON.parse(String(fetchCalls[0][1].body));
    expect(requestBody.title).toBe('Review Packet');
    expect(requestBody.claimBoundary).toMatch(/HTML review packet/i);
    expect(screen.getByText('#receipt-review-packet')).toBeTruthy();
    expect(screen.getByTitle('Preview')).toBeTruthy();
    expect(screen.getByText('Source reference recorded')).toBeTruthy();
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

  it('shows the pre-generate disclosure before the Build HTML button in English', () => {
    render(<ArtifactExportPanel />);

    const disclosure = screen.getByTestId('pre-generate-disclosure');
    expect(disclosure.textContent).toMatch(/may send a short excerpt of your text/i);
    expect(
      disclosure.compareDocumentPosition(screen.getByText('Build HTML')) & Node.DOCUMENT_POSITION_FOLLOWING,
    ).toBeTruthy();
  });

  it('shows the pre-generate disclosure in Vietnamese', () => {
    mockLanguage = 'vi';
    render(<ArtifactExportPanel />);

    expect(screen.getByTestId('pre-generate-disclosure').textContent).toMatch(/có thể gửi một đoạn ngắn nội dung/);
  });

  it('shows an absent-receipt note when a generated result carries no governance receipt', async () => {
    render(<ArtifactExportPanel />);

    fireEvent.click(screen.getByText('Build HTML'));

    await waitFor(() => {
      expect(screen.getByTestId('governance-receipt-absent-note').textContent).toMatch(
        /does not necessarily mean nothing was sent/i,
      );
    });
    expect(screen.queryByTestId('governance-receipt-badge')).toBeNull();
  });

  it('shows the timeout and attempt ID without offering an approval badge', async () => {
    (fetch as unknown as { mockResolvedValue: (v: unknown) => void }).mockResolvedValue({
      ok: true, status: 200,
      json: async () => ({ success: true, data: {
        ...EXPORT_RESULT,
        governanceReceiptStatus: 'TIMED_OUT',
        governanceReceiptAttemptId: 'artifact-proof-timeout-1',
      } }),
    });
    render(<ArtifactExportPanel />);
    fireEvent.click(screen.getByText('Build HTML'));
    await waitFor(() => expect(screen.getByTestId('governance-receipt-absent-note').textContent)
      .toMatch(/may still have processed the request/i));
    expect(screen.getByTestId('governance-receipt-attempt-id').textContent).toBe('artifact-proof-timeout-1');
    expect(screen.queryByTestId('governance-receipt-badge')).toBeNull();
    expect(screen.getByTestId('artifact-draft-state')).toBeTruthy();
  });

  it('shows a governance receipt badge instead of the absent-receipt note when a receipt is present', async () => {
    (fetch as unknown as { mockResolvedValue: (v: unknown) => void }).mockResolvedValue({
      ok: true,
      status: 200,
      json: async () => ({
        success: true,
        data: { ...EXPORT_RESULT, governanceState: 'RECEIPT_ALLOW_REVIEW_REQUIRED', governanceReceipt: { receiptId: 'r1', decision: 'APPROVED', evaluatedAt: '2026-05-16T10:00:00.000Z', riskLevel: 'R0' } },
      }),
    });
    render(<ArtifactExportPanel />);

    fireEvent.click(screen.getByText('Build HTML'));

    await waitFor(() => {
      expect(screen.getByTestId('governance-receipt-badge').textContent).toMatch(/Final artifact acceptance is still required/);
    });
    expect(screen.queryByTestId('governance-receipt-absent-note')).toBeNull();
  });

  it('shows DENY as draft and unaccepted, without a positive receipt badge', async () => {
    (fetch as unknown as { mockResolvedValue: (v: unknown) => void }).mockResolvedValue({
      ok: true, status: 200,
      json: async () => ({ success: true, data: { ...EXPORT_RESULT, governanceReceipt: {
        receiptId: 'r-deny', decision: 'DENY', evaluatedAt: '2026-05-16T10:00:00.000Z', riskLevel: 'R0',
      } } }),
    });
    render(<ArtifactExportPanel />);
    fireEvent.click(screen.getByText('Build HTML'));
    await waitFor(() => expect(screen.getByTestId('governance-receipt-denied-note').textContent).toMatch(/draft and unaccepted/));
    expect(screen.queryByTestId('governance-receipt-badge')).toBeNull();
    expect(screen.getByTestId('artifact-draft-state').textContent).toMatch(/DRAFT \/ UNACCEPTED/);
  });

  it('shows an ALLOW evaluation as evidence without calling it artifact approval', async () => {
    (fetch as unknown as { mockResolvedValue: (v: unknown) => void }).mockResolvedValue({
      ok: true, status: 200,
      json: async () => ({ success: true, data: { ...EXPORT_RESULT, governanceReceiptStatus: 'PRESENT', governanceReceipt: {
        receiptId: 'r-allow', decision: 'ALLOW', evaluatedAt: '2026-05-16T10:00:00.000Z', riskLevel: 'R0',
      } } }),
    });
    render(<ArtifactExportPanel />);
    fireEvent.click(screen.getByText('Build HTML'));
    await waitFor(() => expect(screen.getByTestId('governance-receipt-evaluated-note').textContent)
      .toMatch(/not artifact approval/i));
    expect(screen.queryByTestId('governance-receipt-denied-note')).toBeNull();
    expect(screen.queryByTestId('governance-receipt-badge')).toBeNull();
  });

  it('keeps an approved receipt truthful when presentation checks leave the packet draft', async () => {
    (fetch as unknown as { mockResolvedValue: (v: unknown) => void }).mockResolvedValue({
      ok: true, status: 200,
      json: async () => ({ success: true, data: { ...EXPORT_RESULT, governanceReceipt: {
        receiptId: 'r-approved', decision: 'APPROVED', evaluatedAt: '2026-05-16T10:00:00.000Z', riskLevel: 'R0',
      } } }),
    });
    render(<ArtifactExportPanel />);
    fireEvent.click(screen.getByText('Build HTML'));
    await waitFor(() => expect(screen.getByTestId('governance-approved-checks-note').textContent).toMatch(/Presentation checks still need attention/));
    expect(screen.queryByTestId('governance-receipt-denied-note')).toBeNull();
    expect(screen.getByTestId('artifact-draft-state')).toBeTruthy();
  });

  it('maps the secret-pattern rejection to plain-language recovery, keeping the raw error as secondary detail', async () => {
    (fetch as unknown as { mockResolvedValue: (v: unknown) => void }).mockResolvedValue({
      ok: false,
      status: 400,
      json: async () => ({ success: false, error: 'Potential secret-like value detected in source content.' }),
    });
    render(<ArtifactExportPanel />);

    fireEvent.click(screen.getByText('Build HTML'));

    await waitFor(() => {
      expect(screen.getByTestId('export-error-recovery').textContent).toMatch(/private key or token/i);
    });
    expect(screen.getByTestId('export-error-detail').textContent).toBe(
      'Potential secret-like value detected in source content.',
    );
  });

  it('maps the missing-field rejection to plain-language recovery, keeping the raw error as secondary detail', async () => {
    (fetch as unknown as { mockResolvedValue: (v: unknown) => void }).mockResolvedValue({
      ok: false,
      status: 400,
      json: async () => ({ success: false, error: 'Missing required artifact export fields.' }),
    });
    render(<ArtifactExportPanel />);

    fireEvent.click(screen.getByText('Build HTML'));

    await waitFor(() => {
      expect(screen.getByTestId('export-error-recovery').textContent).toMatch(/fill in the missing fields/i);
    });
    expect(screen.getByTestId('export-error-detail').textContent).toBe('Missing required artifact export fields.');
  });

  it('keeps an unrelated or network error generic, without a secondary detail line', async () => {
    (fetch as unknown as { mockRejectedValue: (v: unknown) => void }).mockRejectedValue(new Error('Failed to fetch'));
    render(<ArtifactExportPanel />);

    fireEvent.click(screen.getByText('Build HTML'));

    await waitFor(() => {
      expect(screen.getByTestId('export-error-recovery').textContent).toBe('Failed to fetch');
    });
    expect(screen.queryByTestId('export-error-detail')).toBeNull();
  });

  describe('B1 version binding', () => {
    type Deferred = { promise: Promise<unknown>; resolve: (v: unknown) => void };
    const deferred = (): Deferred => {
      let resolve: (v: unknown) => void = () => undefined;
      const promise = new Promise<unknown>(r => { resolve = r; });
      return { promise, resolve };
    };
    const okResponse = (data: ArtifactExportResult) => ({
      ok: true, status: 200, json: async () => ({ success: true, data }),
    });
    const failResponse = (error: string) => ({
      ok: false, status: 500, json: async () => ({ success: false, error }),
    });
    const resultFor = (tag: string, extra: Partial<ArtifactExportResult> = {}): ArtifactExportResult => ({
      ...EXPORT_RESULT,
      html: `<!doctype html><html><body><h1>synthetic ${tag}</h1></body></html>`,
      receiptAnchor: `receipt-${tag}`,
      filename: `packet-${tag}.html`,
      ...extra,
    });
    const fetchMock = () => fetch as unknown as {
      mockResolvedValueOnce: (v: unknown) => void;
      mockImplementationOnce: (fn: () => Promise<unknown>) => void;
      mock: { calls: Array<[string, RequestInit]> };
    };
    const buildButton = () => screen.getByRole('button', { name: /Build HTML|Generating/ });
    const iframeHtml = () => (screen.getByTitle('Preview') as HTMLIFrameElement).getAttribute('srcdoc');
    const noticeState = () => screen.getByTestId('artifact-version-notice').getAttribute('data-version-state');

    it('snapshots all seven request fields at submit', async () => {
      render(<ArtifactExportPanel />);
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic A' } });
      fireEvent.change(screen.getByLabelText('Source reference'), { target: { value: 'docs/synthetic-a.md' } });
      fireEvent.change(screen.getByLabelText('Record type'), { target: { value: 'POINTER_RECORD' } });
      fireEvent.change(screen.getByLabelText('Review status'), { target: { value: 'REVIEW' } });
      fireEvent.change(screen.getByLabelText('Receipt reference'), { target: { value: 'receipt-synth-a' } });
      fireEvent.change(screen.getByLabelText('Review boundary'), { target: { value: 'boundary A' } });
      fireEvent.change(screen.getByLabelText('Source notes'), { target: { value: 'notes A' } });
      fireEvent.click(buildButton());
      await waitFor(() => expect(screen.getByTestId('artifact-version-notice')).toBeTruthy());

      expect(JSON.parse(String(fetchMock().mock.calls[0][1].body))).toEqual({
        title: 'Synthetic A',
        sourcePath: 'docs/synthetic-a.md',
        sourceContent: 'notes A',
        memoryClass: 'POINTER_RECORD',
        status: 'REVIEW',
        claimBoundary: 'boundary A',
        receiptAnchor: 'receipt-synth-a',
      });
      expect(noticeState()).toBe('current');
    });

    for (const [field, value] of [
      ['Title', 'Synthetic title B'],
      ['Review boundary', 'Synthetic boundary B'],
      ['Source reference', 'docs/other.md'],
      ['Review status', 'FINAL'],
      ['Receipt reference', 'receipt-other'],
    ] as const) {
      it(`marks the prior version stale when only ${field} changes and source notes stay identical`, async () => {
        fetchMock().mockResolvedValueOnce(okResponse(resultFor('A')));
        render(<ArtifactExportPanel />);
        fireEvent.click(buildButton());
        await waitFor(() => expect(noticeState()).toBe('current'));
        const sourceNotes = (screen.getByLabelText('Source notes') as HTMLTextAreaElement).value;

        fireEvent.change(screen.getByLabelText(field), { target: { value } });

        expect((screen.getByLabelText('Source notes') as HTMLTextAreaElement).value).toBe(sourceNotes);
        expect(noticeState()).toBe('stale');
        expect(screen.getByTestId('artifact-version-notice').textContent).toMatch(/Earlier version \(build #1\)/);
        expect(screen.getByTestId('artifact-version-tag').textContent).toMatch(/earlier version/);
        expect(iframeHtml()).toContain('synthetic A');
        expect(screen.getByText('#receipt-A')).toBeTruthy();
        expect(screen.getByTestId('artifact-draft-state')).toBeTruthy();
      });
    }

    it('returns to current when the form is edited back to the submitted values', async () => {
      fetchMock().mockResolvedValueOnce(okResponse(resultFor('A')));
      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      await waitFor(() => expect(noticeState()).toBe('current'));
      const original = (screen.getByLabelText('Title') as HTMLInputElement).value;
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'changed' } });
      expect(noticeState()).toBe('stale');
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: original } });
      expect(noticeState()).toBe('current');
    });

    it('does not present a response as the edited form when the form changes while the request is pending', async () => {
      const d = deferred();
      fetchMock().mockImplementationOnce(() => d.promise);
      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Review boundary'), { target: { value: 'edited while pending' } });

      d.resolve(okResponse(resultFor('A', {
        governanceState: 'RECEIPT_ALLOW_REVIEW_REQUIRED',
        governanceReceipt: { receiptId: 'r-a', decision: 'APPROVED', evaluatedAt: '2026-05-16T10:00:00.000Z', riskLevel: 'R0' },
      })));

      await waitFor(() => expect(screen.getByTestId('artifact-version-notice')).toBeTruthy());
      expect(noticeState()).toBe('stale');
      expect(screen.getByTestId('artifact-version-notice').textContent).toMatch(/Earlier version \(build #1\)/);
      expect(screen.getByTestId('governance-receipt-badge').textContent).toMatch(/Final artifact acceptance is still required/);
      const body = JSON.parse(String(fetchMock().mock.calls[0][1].body));
      expect(body.claimBoundary).not.toBe('edited while pending');
    });

    it('lets the latest attempt win when an older attempt succeeds late', async () => {
      const dA = deferred();
      const dB = deferred();
      fetchMock().mockImplementationOnce(() => dA.promise);
      fetchMock().mockImplementationOnce(() => dB.promise);
      const onGenerated = vi.fn();
      render(<ArtifactExportPanel onGenerated={onGenerated} />);

      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());

      const resultB = resultFor('B');
      dB.resolve(okResponse(resultB));
      await waitFor(() => expect(iframeHtml()).toContain('synthetic B'));
      expect(noticeState()).toBe('current');

      dA.resolve(okResponse(resultFor('A')));
      await new Promise(r => setTimeout(r, 0));
      await new Promise(r => setTimeout(r, 0));

      expect(iframeHtml()).toContain('synthetic B');
      expect(screen.getByText('#receipt-B')).toBeTruthy();
      expect(screen.queryByText('#receipt-A')).toBeNull();
      expect(noticeState()).toBe('current');
      expect(screen.getByTestId('artifact-version-notice').textContent).toMatch(/build #2/);
      expect(onGenerated).toHaveBeenCalledTimes(1);
      expect(onGenerated).toHaveBeenCalledWith(resultB);
    });

    it('does not let a superseded attempt dismiss the busy state of the newer attempt', async () => {
      const dA = deferred();
      const dB = deferred();
      fetchMock().mockImplementationOnce(() => dA.promise);
      fetchMock().mockImplementationOnce(() => dB.promise);
      render(<ArtifactExportPanel />);

      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());
      dA.resolve(okResponse(resultFor('A')));
      await new Promise(r => setTimeout(r, 0));
      await new Promise(r => setTimeout(r, 0));

      expect(buildButton().getAttribute('aria-busy')).toBe('true');
      expect(screen.getByText('Generating')).toBeTruthy();
      expect(screen.queryByTestId('artifact-version-notice')).toBeNull();

      dB.resolve(okResponse(resultFor('B')));
      await waitFor(() => expect(iframeHtml()).toContain('synthetic B'));
      expect(buildButton().getAttribute('aria-busy')).toBe('false');
    });

    it('ignores a superseded attempt error and keeps the newer result', async () => {
      const dA = deferred();
      const dB = deferred();
      fetchMock().mockImplementationOnce(() => dA.promise);
      fetchMock().mockImplementationOnce(() => dB.promise);
      render(<ArtifactExportPanel />);

      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());
      dB.resolve(okResponse(resultFor('B')));
      await waitFor(() => expect(iframeHtml()).toContain('synthetic B'));

      dA.resolve(failResponse('late failure from attempt A'));
      await new Promise(r => setTimeout(r, 0));
      await new Promise(r => setTimeout(r, 0));

      expect(screen.queryByTestId('export-error-recovery')).toBeNull();
      expect(iframeHtml()).toContain('synthetic B');
    });

    it('does not erase a valid earlier result when a newer attempt fails, and attaches the error to the newer attempt', async () => {
      fetchMock().mockResolvedValueOnce(okResponse(resultFor('A')));
      fetchMock().mockResolvedValueOnce(failResponse('synthetic outage'));
      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      await waitFor(() => expect(iframeHtml()).toContain('synthetic A'));

      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());
      await waitFor(() => expect(screen.getByTestId('export-error-recovery').textContent).toBe('synthetic outage'));

      expect(iframeHtml()).toContain('synthetic A');
      expect(noticeState()).toBe('stale');
      expect(screen.getByTestId('artifact-version-notice').textContent).toMatch(/build #1/);
    });

    it('labels an initialResult conservatively as unknown source, never as matching the form', () => {
      render(<ArtifactExportPanel initialResult={EXPORT_RESULT} />);

      expect(noticeState()).toBe('unknown');
      expect(screen.getByTestId('artifact-version-notice').textContent).toMatch(/unknown source/i);
      expect(screen.getByTestId('artifact-version-notice').textContent).not.toMatch(/still matches/i);
      expect(screen.getByTestId('artifact-version-tag').textContent).toMatch(/Source unknown/);
      expect(screen.getByTestId('artifact-draft-state')).toBeTruthy();
      expect(screen.getByRole('button', { name: 'Copy HTML' }).getAttribute('aria-describedby'))
        .toBe('artifact-version-notice');
    });

    it('keeps the draft and ALLOW distinction truthful for a stale result', async () => {
      fetchMock().mockResolvedValueOnce(okResponse(resultFor('A', {
        governanceReceiptStatus: 'PRESENT',
        governanceReceipt: { receiptId: 'r-allow', decision: 'ALLOW', evaluatedAt: '2026-05-16T10:00:00.000Z', riskLevel: 'R0' },
      })));
      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      await waitFor(() => expect(screen.getByTestId('governance-receipt-evaluated-note')).toBeTruthy());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });

      expect(noticeState()).toBe('stale');
      expect(screen.getByTestId('governance-receipt-evaluated-note').textContent).toMatch(/not artifact approval/i);
      expect(screen.queryByTestId('governance-receipt-badge')).toBeNull();
      expect(screen.getByTestId('artifact-draft-state').textContent).toMatch(/DRAFT \/ UNACCEPTED/);
    });

    it('copies, downloads and prints the displayed older version while the notice stays visible', async () => {
      fetchMock().mockResolvedValueOnce(okResponse(resultFor('A')));
      const blobs: Blob[] = [];
      const createObjectURL = vi.fn((blob: Blob) => { blobs.push(blob); return 'blob:synthetic'; });
      const revokeObjectURL = vi.fn();
      const urlApi = URL as unknown as Record<string, unknown>;
      const priorCreate = urlApi.createObjectURL;
      const priorRevoke = urlApi.revokeObjectURL;
      urlApi.createObjectURL = createObjectURL;
      urlApi.revokeObjectURL = revokeObjectURL;
      onTestFinished(() => { urlApi.createObjectURL = priorCreate; urlApi.revokeObjectURL = priorRevoke; });
      const anchorClick = vi.spyOn(HTMLAnchorElement.prototype, 'click').mockImplementation(() => undefined);
      const printWindow = { document: { write: vi.fn(), close: vi.fn() }, focus: vi.fn(), print: vi.fn() };
      const openSpy = vi.spyOn(window, 'open').mockReturnValue(printWindow as unknown as Window);

      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      await waitFor(() => expect(noticeState()).toBe('current'));
      fireEvent.change(screen.getByLabelText('Review boundary'), { target: { value: 'Synthetic boundary B' } });
      expect(noticeState()).toBe('stale');

      for (const name of ['Copy HTML', 'Download HTML', 'Print preview']) {
        expect(screen.getByRole('button', { name }).getAttribute('aria-describedby')).toBe('artifact-version-notice');
      }
      const html = resultFor('A').html;

      fireEvent.click(screen.getByRole('button', { name: 'Copy HTML' }));
      await waitFor(() => expect(navigator.clipboard.writeText).toHaveBeenCalledWith(html));

      fireEvent.click(screen.getByRole('button', { name: 'Download HTML' }));
      expect(createObjectURL).toHaveBeenCalledTimes(1);
      expect(anchorClick).toHaveBeenCalledTimes(1);
      const blobText = await new Promise<string>(resolve => {
        const reader = new FileReader();
        reader.onload = () => resolve(String(reader.result));
        reader.readAsText(blobs[0]);
      });
      expect(blobText).toBe(html);

      fireEvent.click(screen.getByRole('button', { name: 'Print preview' }));
      expect(openSpy).toHaveBeenCalled();
      expect(printWindow.document.write).toHaveBeenCalledWith(html);
      expect(printWindow.print).toHaveBeenCalledTimes(1);

      expect(screen.getByTestId('artifact-version-notice').textContent).toMatch(/copy, download and print/);
      expect(noticeState()).toBe('stale');
    });

    it('uses a fresh build for actions after rebuilding with the edited form', async () => {
      fetchMock().mockResolvedValueOnce(okResponse(resultFor('A')));
      fetchMock().mockResolvedValueOnce(okResponse(resultFor('B')));
      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      await waitFor(() => expect(iframeHtml()).toContain('synthetic A'));
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      expect(noticeState()).toBe('stale');

      fireEvent.click(buildButton());
      await waitFor(() => expect(iframeHtml()).toContain('synthetic B'));
      expect(noticeState()).toBe('current');
      expect(screen.getByTestId('artifact-version-tag').textContent).toMatch(/Build #2 · matches form/);
      fireEvent.click(screen.getByRole('button', { name: 'Copy HTML' }));
      await waitFor(() => expect(navigator.clipboard.writeText).toHaveBeenCalledWith(resultFor('B').html));
      expect(screen.getByRole('button', { name: /Copied|Copy HTML/ }).getAttribute('aria-describedby')).toBeNull();
    });

    it('does not create a second request when Build is pressed twice with the same snapshot', async () => {
      const d = deferred();
      fetchMock().mockImplementationOnce(() => d.promise);
      render(<ArtifactExportPanel />);

      fireEvent.click(buildButton());
      fireEvent.click(buildButton());
      fireEvent.click(buildButton());

      expect(fetchMock().mock.calls).toHaveLength(1);
      expect(screen.queryByTestId('superseded-attempts')).toBeNull();
      d.resolve(okResponse(resultFor('A')));
      await waitFor(() => expect(iframeHtml()).toContain('synthetic A'));
      expect(fetchMock().mock.calls).toHaveLength(1);

      // Once the attempt settled, the same snapshot may be submitted again as a new build.
      fetchMock().mockResolvedValueOnce(okResponse(resultFor('A2')));
      fireEvent.click(buildButton());
      await waitFor(() => expect(iframeHtml()).toContain('synthetic A2'));
      expect(fetchMock().mock.calls).toHaveLength(2);
    });

    it('Local probe: A to B to A does not resend a snapshot still in flight', async () => {
      const dA = deferred();
      const dB = deferred();
      fetchMock().mockImplementationOnce(() => dA.promise);
      fetchMock().mockImplementationOnce(() => dB.promise);
      render(<ArtifactExportPanel />);
      const original = (screen.getByLabelText('Title') as HTMLInputElement).value;

      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: original } });
      fireEvent.click(buildButton());

      expect(fetchMock().mock.calls).toHaveLength(2);
      dB.resolve(okResponse(resultFor('B')));
      await waitFor(() => expect(iframeHtml()).toContain('synthetic B'));
      expect(noticeState()).toBe('stale');
      dA.resolve(okResponse(resultFor('A', { governanceReceiptAttemptId: 'probe-attempt-A' })));
      await waitFor(() => expect(screen.getByTestId('superseded-attempt-notice').textContent).toContain('probe-attempt-A'));
      expect(iframeHtml()).toContain('synthetic B');
    });

    it('records a replaced pending attempt separately and never lets its late success reach the preview', async () => {
      const dA = deferred();
      const dB = deferred();
      fetchMock().mockImplementationOnce(() => dA.promise);
      fetchMock().mockImplementationOnce(() => dB.promise);
      render(<ArtifactExportPanel />);

      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());
      expect(fetchMock().mock.calls).toHaveLength(2);
      const pendingNote = screen.getByTestId('superseded-attempt-notice');
      expect(pendingNote.getAttribute('data-status')).toBe('pending');
      expect(pendingNote.textContent).toMatch(/Build #1 was replaced by a newer build/);

      dB.resolve(okResponse(resultFor('B')));
      await waitFor(() => expect(iframeHtml()).toContain('synthetic B'));
      dA.resolve(okResponse(resultFor('A', { governanceReceiptAttemptId: 'attempt-id-synthetic-1' })));
      await waitFor(() => expect(screen.getByTestId('superseded-attempt-notice').getAttribute('data-status')).toBe('success'));

      const note = screen.getByTestId('superseded-attempt-notice').textContent ?? '';
      expect(note).toMatch(/Build #1/);
      expect(note).toContain('attempt-id-synthetic-1');
      expect(note).toMatch(/cannot establish a governance result/);
      expect(note).not.toMatch(/retry|try again/i);
      expect(iframeHtml()).toContain('synthetic B');
      expect(screen.queryByText('#receipt-A')).toBeNull();
      expect(screen.queryByTestId('governance-receipt-attempt-id')).toBeNull();
    });

    it('falls back to the receipt ID when a superseded success has no attempt ID', async () => {
      const dA = deferred();
      const dB = deferred();
      fetchMock().mockImplementationOnce(() => dA.promise);
      fetchMock().mockImplementationOnce(() => dB.promise);
      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());
      dA.resolve(okResponse(resultFor('A', {
        governanceReceipt: { receiptId: 'receipt-id-synthetic-1', decision: 'ALLOW', evaluatedAt: '2026-05-16T10:00:00.000Z', riskLevel: 'R0' },
      })));
      await waitFor(() => expect(screen.getByTestId('superseded-attempt-notice').getAttribute('data-status')).toBe('success'));
      expect(screen.getByTestId('superseded-attempt-notice').textContent).toContain('receipt-id-synthetic-1');
    });

    it('states that no governance result could be established for a superseded success without an ID', async () => {
      const dA = deferred();
      const dB = deferred();
      fetchMock().mockImplementationOnce(() => dA.promise);
      fetchMock().mockImplementationOnce(() => dB.promise);
      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());
      dA.resolve(okResponse(resultFor('A')));
      await waitFor(() => expect(screen.getByTestId('superseded-attempt-notice').getAttribute('data-status')).toBe('success'));
      const note = screen.getByTestId('superseded-attempt-notice').textContent ?? '';
      expect(note).toMatch(/carried no ID/);
      expect(note).toMatch(/no governance result could be established/);
      expect(note).not.toMatch(/retry|try again/i);
    });

    it('states that no governance result could be established for a superseded failure', async () => {
      const dA = deferred();
      const dB = deferred();
      fetchMock().mockImplementationOnce(() => dA.promise);
      fetchMock().mockImplementationOnce(() => dB.promise);
      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());
      dA.resolve(failResponse('synthetic timeout'));
      await waitFor(() => expect(screen.getByTestId('superseded-attempt-notice').getAttribute('data-status')).toBe('failure'));
      const note = screen.getByTestId('superseded-attempt-notice').textContent ?? '';
      expect(note).toMatch(/Build #1 was replaced/);
      expect(note).toMatch(/request failed/);
      expect(note).toMatch(/No governance result could be established/);
      expect(note).not.toMatch(/retry|try again/i);
      expect(screen.queryByTestId('export-error-recovery')).toBeNull();
    });

    it('labels a newer failure with its build number apart from the older preview that stays visible', async () => {
      fetchMock().mockResolvedValueOnce(okResponse(resultFor('A')));
      fetchMock().mockResolvedValueOnce(failResponse('synthetic outage'));
      render(<ArtifactExportPanel />);
      fireEvent.click(buildButton());
      await waitFor(() => expect(iframeHtml()).toContain('synthetic A'));
      fireEvent.change(screen.getByLabelText('Title'), { target: { value: 'Synthetic B' } });
      fireEvent.click(buildButton());
      await waitFor(() => expect(screen.getByTestId('export-error-recovery').textContent).toBe('synthetic outage'));

      expect(screen.getByTestId('export-error-build').textContent).toBe('Build #2');
      expect(screen.getByTestId('export-error-preview-note').textContent).toMatch(/still shows build #1, not this build/);
      expect(screen.getByTestId('artifact-version-tag').textContent).toMatch(/Build #1 · earlier version/);
      expect(iframeHtml()).toContain('synthetic A');
    });

    it('labels a newer failure against an initialResult preview as unknown source', async () => {
      fetchMock().mockResolvedValueOnce(failResponse('synthetic outage'));
      render(<ArtifactExportPanel initialResult={EXPORT_RESULT} />);
      fireEvent.click(buildButton());
      await waitFor(() => expect(screen.getByTestId('export-error-build').textContent).toBe('Build #1'));
      expect(screen.getByTestId('export-error-preview-note').textContent).toMatch(/unknown source, not this build/);
    });

    it('shows superseded-attempt copy in Vietnamese without retry advice', async () => {
      mockLanguage = 'vi';
      const dA = deferred();
      const dB = deferred();
      fetchMock().mockImplementationOnce(() => dA.promise);
      fetchMock().mockImplementationOnce(() => dB.promise);
      render(<ArtifactExportPanel />);
      const vnButton = () => screen.getByRole('button', { name: /Tạo HTML|Đang tạo/ });
      fireEvent.click(vnButton());
      fireEvent.change(screen.getByLabelText('Tiêu đề'), { target: { value: 'Tiêu đề mới' } });
      fireEvent.click(vnButton());
      dA.resolve(okResponse(resultFor('A', { governanceReceiptAttemptId: 'attempt-id-vi-1' })));
      await waitFor(() => expect(screen.getByTestId('superseded-attempt-notice').getAttribute('data-status')).toBe('success'));
      const note = screen.getByTestId('superseded-attempt-notice').textContent ?? '';
      expect(note).toMatch(/Lần tạo #1 đã bị thay/);
      expect(note).toContain('attempt-id-vi-1');
      expect(note).not.toMatch(/thử lại/);
    });

    it('shows the stale-version notice in Vietnamese', async () => {
      mockLanguage = 'vi';
      fetchMock().mockResolvedValueOnce(okResponse(resultFor('A')));
      render(<ArtifactExportPanel />);
      fireEvent.click(screen.getByRole('button', { name: /Tạo HTML|Đang tạo/ }));
      await waitFor(() => expect(noticeState()).toBe('current'));
      fireEvent.change(screen.getByLabelText('Tiêu đề'), { target: { value: 'Tiêu đề mới' } });

      expect(noticeState()).toBe('stale');
      expect(screen.getByTestId('artifact-version-notice').textContent).toMatch(/Phiên bản cũ \(lần tạo #1\)/);
      expect(screen.getByTestId('artifact-version-tag').textContent).toMatch(/phiên bản cũ/);
    });
  });

});
