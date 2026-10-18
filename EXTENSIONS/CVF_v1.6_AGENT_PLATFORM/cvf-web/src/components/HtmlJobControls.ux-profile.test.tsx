// Text Encoding Exception: localized Vietnamese user-facing copy assertions follow the existing bilingual UI convention.
// UI-structure proof only (AGENTS pure-UI-structure mock exception): real HtmlJobControls and ArtifactExportPanel render in jsdom
// against deterministic fetch spies. All fixtures are invented ncr-synthetic values; spy POSTs are not real writes. HtmlDraftRecovery
// is a disclosed presentation stub, so no draft-save/recovery correctness claim follows. This is not governance, auth/writer,
// cancellation, browser, keyboard, small-screen or human-comprehension evidence.
import { act, fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { ReactElement } from 'react';
import { ArtifactExportPanel } from './ArtifactExportPanel';
import { HtmlJobControls } from './HtmlJobControls';

const h = vi.hoisted(() => ({
  lang: 'en' as 'en' | 'vi',
  session: null as unknown as { status: string; data: { user: { userId: string; orgId: string; teamId: string }; expires: string } },
}));
vi.mock('next-auth/react', () => ({ useSession: () => h.session }));
vi.mock('@/lib/i18n', () => ({ useLanguage: () => ({ language: h.lang }) }));
// Disclosed presentation fixture: simulated confirmed Save goes through the fetch spy, then reports the snapshot upward.
vi.mock('./HtmlDraftRecovery', () => ({
  HtmlDraftRecovery: ({ displayed, onConfirmedSnapshot }: {
    displayed: { job?: { jobId: string } } | null; onConfirmedSnapshot?: (snapshot: unknown, jobId?: string) => void }) => (
    <button type="button" data-testid="stub-save" disabled={!displayed} onClick={() => {
      void fetch('/api/artifacts/drafts', { method: 'POST', body: JSON.stringify({ action: 'SAVE_DRAFT' }) }).then(() => onConfirmedSnapshot?.({
        versionId: '123e4567-e89b-42d3-a456-426614174002', sourceRecordId: 'ncr-synthetic-ux-proof', requestSha256: '1'.repeat(64),
        htmlSha256: '2'.repeat(64), state: 'CLIENT_SUBMITTED_UNVERIFIED', acceptance: 'DRAFT_UNACCEPTED' }, displayed?.job?.jobId));
    }}>Stub: confirmed Save</button>),
}));

const SRC = 'ncr-synthetic-ux-proof';
const JOB = '123e4567-e89b-42d3-a456-426614174001';
const VERSION = '123e4567-e89b-42d3-a456-426614174002';
const DECISION = '123e4567-e89b-42d3-a456-426614174003';
const OWNER = { userId: 'u1', orgId: 'o1', teamId: 't1' };
const JOURNAL_KEY = 'cvf-html-job-pending-v1';
const REQ = { title: 'ncr-synthetic title', sourcePath: 'docs/reviews/ncr-synthetic.md', sourceContent: '# ncr-synthetic packet\n\nSynthetic only.',
  status: 'DRAFT', claimBoundary: 'ncr-synthetic boundary', receiptAnchor: 'ncr-synthetic-anchor' };
const EXPORT_RESULT = { html: '<!doctype html><html><body><p>ncr-synthetic</p></body></html>', filename: 'ncr-synthetic.html',
  receiptAnchor: 'ncr-synthetic-anchor', verification: [{ label: 'ncr-synthetic check', passed: true }],
  generatedAt: '2026-10-18T00:00:00.000Z', governanceReceiptStatus: 'NOT_CONFIGURED' };
const GENERIC_EN = 'may send a short excerpt';
const GENERIC_VI = 'có thể gửi một đoạn ngắn';
const PROFILE_EN = ['local test profile', 'when you choose Save', 'no review receipt is requested', 'unverified and unaccepted',
  'not trusted evidence or business acceptance', 'Stop only acts on this page', 'does not confirm that a remote task stopped or determine cost'];
const PROFILE_VI = ['chế độ thử nghiệm cục bộ', 'khi bạn chọn Lưu', 'không có yêu cầu lấy biên nhận', 'chưa được xác minh và chưa được chấp nhận',
  'không phải bằng chứng đáng tin cậy hay sự chấp nhận trong nghiệp vụ', 'không xác nhận thao tác từ xa đã dừng', 'chi phí vẫn chưa rõ'];

type Call = { method: string; url: string; action?: string };
type Row = { role: string; fixture: string; language: string; visibleEvidence: string; action: string; observed: string; uncertainty: string };
const calls: Call[] = [];
const denied: string[] = [];
const newSession = (userId = 'u1') => ({ status: 'authenticated', data: { user: { ...OWNER, userId }, expires: '2999-01-01T00:00:00.000Z' } });
const reply = (data: unknown, ok = true, status = 200) => ({ ok, status, json: async () => (ok ? { success: true, data } : { success: false, error: data }) });
function deferred<T>() { let resolve!: (value: T) => void; const promise = new Promise<T>(r => { resolve = r; }); return { promise, resolve }; }
const flush = () => act(async () => { await new Promise(r => setTimeout(r, 30)); });
const text = (el: Element | null) => (el?.textContent ?? '').replace(/\s+/g, ' ').trim();
const excerpt = (el: Element | null, n = 150) => text(el).slice(0, n);
const walk = (task: { meta: object }, row: Row) => { const meta = task.meta as Record<string, Row[]>; (meta.walkthrough ??= []).push(row); };
const posts = () => calls.filter(c => c.method === 'POST');
const actions = () => posts().map(c => c.action ?? (c.url.endsWith('/export') ? 'export' : c.url.endsWith('/drafts') ? 'save' : c.url));
const switchTo = (view: { rerender: (ui: ReactElement) => void }, lang: 'en' | 'vi', ui: ReactElement) => { h.lang = lang; view.rerender(ui); };

type Opts = { caps?: () => unknown; exportReply?: () => unknown };
function installFetch(o: Opts = {}) {
  calls.length = 0;
  const ids = [JOB, DECISION, '123e4567-e89b-42d3-a456-426614174004'];
  vi.stubGlobal('crypto', { randomUUID: () => ids.shift() ?? JOB });
  const spy = vi.fn(async (input: RequestInfo | URL, init?: RequestInit) => {
    const url = String(input); const method = init?.method ?? 'GET';
    const body = init?.body ? JSON.parse(String(init.body)) : undefined;
    calls.push({ method, url, action: body?.action });
    if (method === 'GET' && url.includes('kind=capabilities')) return o.caps ? o.caps() : reply({ jobDecisions: true, effectBoundary: 'LOCAL_SYNTHETIC' });
    if (method === 'POST' && url === '/api/artifacts/jobs' && body.action === 'CREATE_JOB') return reply({ jobId: body.jobId, sourceRecordId: body.sourceRecordId,
      owner: OWNER, goal: body.goal, criteria: body.criteria, requestSha256: '1'.repeat(64) });
    if (method === 'POST' && url === '/api/artifacts/jobs' && body.action === 'LINK_VERSION') return reply({ jobId: body.jobId, sourceRecordId: body.sourceRecordId,
      versionId: body.versionId, requestSha256: '1'.repeat(64), htmlSha256: '2'.repeat(64) });
    if (method === 'POST' && url === '/api/artifacts/jobs' && body.action === 'ACCEPT_VERSION') return reply({ decisionId: body.decisionId, jobId: body.jobId,
      versionId: body.versionId, requestSha256: body.requestSha256, htmlSha256: body.htmlSha256 });
    if (method === 'POST' && url === '/api/artifacts/export') return o.exportReply ? o.exportReply() : reply(EXPORT_RESULT);
    if (method === 'POST' && url === '/api/artifacts/drafts') return reply({ saved: true });
    denied.push(`${method} ${url}`);
    throw new Error(`DENIED_UNEXPECTED_FETCH ${method} ${url}`);
  });
  vi.stubGlobal('fetch', spy);
  return spy;
}
const jobUi = (source = SRC) => <HtmlJobControls sourceRecordId={source} initialRequest={REQ} />;
async function mountJob(o?: Opts) {
  installFetch(o);
  const view = render(jobUi());
  await waitFor(() => expect(screen.queryByTestId('pre-generate-disclosure')).not.toBeNull());
  return view;
}
const fillJob = () => {
  fireEvent.change(screen.getByRole('textbox', { name: h.lang === 'vi' ? 'Mục tiêu' : 'Goal' }), { target: { value: 'ncr-synthetic goal' } });
  fireEvent.change(screen.getByRole('textbox', { name: h.lang === 'vi' ? 'Tiêu chí 1' : 'Criterion 1' }), { target: { value: 'ncr-synthetic criterion' } });
};
const clickBuild = () => fireEvent.click(screen.getByRole('button', { name: h.lang === 'vi' ? 'Tạo HTML' : 'Build HTML' }));
const disclosure = () => text(screen.getByTestId('pre-generate-disclosure'));
const expectAll = (haystack: string, needles: string[]) => needles.forEach(n => expect(haystack).toContain(n));

beforeEach(() => { h.lang = 'en'; h.session = newSession(); calls.length = 0; denied.length = 0; });
afterEach(() => { expect(denied).toEqual([]); });

describe('ArtifactExportPanel standalone (real component)', () => {
  it('shows owned EN/VI labels and accessible names; user text and wire values stay literal across a language rerender', async ({ task }) => {
    installFetch();
    const ui = () => <ArtifactExportPanel initialRequest={REQ} />;
    const view = render(ui());
    const names = {
      en: { heading: 'Review Packet Export', boxes: ['Title', 'Source reference', 'Review status', 'Receipt reference', 'Review boundary', 'Source notes'],
        select: 'Record type', build: 'Build HTML', output: ['Copy HTML', 'Download HTML', 'Print preview'], full: 'Complete record', pointer: 'Reference record' },
      vi: { heading: 'Xuất gói rà soát', boxes: ['Tiêu đề', 'Nguồn tham chiếu', 'Trạng thái rà soát', 'Mã receipt', 'Ranh giới rà soát', 'Ghi chú nguồn'],
        select: 'Loại bản ghi', build: 'Tạo HTML', output: ['Sao chép HTML', 'Tải HTML', 'Xem bản in'], full: 'Bản đầy đủ', pointer: 'Bản tham chiếu' },
    };
    const check = (lang: 'en' | 'vi') => {
      const n = names[lang];
      expect(screen.getByRole('heading', { level: 2, name: n.heading })).toBeTruthy();
      n.boxes.forEach(b => expect(screen.getByRole('textbox', { name: b })).toBeTruthy());
      expect(screen.getByRole('combobox', { name: n.select })).toBeTruthy();
      expect((screen.getByRole('button', { name: n.build }) as HTMLButtonElement).disabled).toBe(false);
      n.output.forEach(b => expect((screen.getByRole('button', { name: b }) as HTMLButtonElement).disabled).toBe(true));
      expect((screen.getByRole('option', { name: n.full }) as HTMLOptionElement).value).toBe('FULL_RECORD');
      expect((screen.getByRole('option', { name: n.pointer }) as HTMLOptionElement).value).toBe('POINTER_RECORD');
    };
    check('en');
    fireEvent.change(screen.getByRole('textbox', { name: 'Title' }), { target: { value: 'ncr-synthetic typed title' } });
    switchTo(view, 'vi', ui());
    check('vi');
    expect((screen.getByRole('textbox', { name: 'Tiêu đề' }) as HTMLInputElement).value).toBe('ncr-synthetic typed title');
    expect((screen.getByRole('textbox', { name: 'Nguồn tham chiếu' }) as HTMLInputElement).value).toBe(REQ.sourcePath);
    expect(posts()).toEqual([]);
    walk(task, { role: 'simulated non-coder reviewer (agent)', fixture: 'standalone panel, invented request, no job props', language: 'en then vi by rerender',
      visibleEvidence: `heading ${names.vi.heading}; build button ${names.vi.build}`, action: 'type title, switch language',
      observed: `title input value kept literal; option values FULL_RECORD/POINTER_RECORD unchanged; zero POST; ${excerpt(screen.getByRole('heading', { level: 2 }))}`,
      uncertainty: 'jsdom DOM names only; no layout, focus or real reader comprehension' });
  });

  it('keeps the standalone disclosure generic in EN and VI', ({ task }) => {
    installFetch();
    const ui = () => <ArtifactExportPanel initialRequest={REQ} />;
    const view = render(ui());
    expect(disclosure()).toContain(GENERIC_EN);
    expect(disclosure()).not.toContain('local test profile');
    switchTo(view, 'vi', ui());
    expect(disclosure()).toContain(GENERIC_VI);
    expect(disclosure()).not.toContain('chế độ thử nghiệm cục bộ');
    walk(task, { role: 'simulated non-coder reviewer (agent)', fixture: 'standalone panel, no profileDisclosure prop', language: 'vi',
      visibleEvidence: excerpt(screen.getByTestId('pre-generate-disclosure')), action: 'read disclosure only', observed: 'generic review-checking-service wording; no local-test-profile wording',
      uncertainty: 'does not show what a deployment actually does' });
  });

  it('translates an already-created error while the raw backend text stays literal under collapsed technical detail', async ({ task }) => {
    installFetch({ exportReply: () => reply('Missing required artifact export fields.', false, 400) });
    const ui = () => <ArtifactExportPanel initialRequest={REQ} />;
    const view = render(ui());
    fireEvent.click(screen.getByRole('button', { name: 'Build HTML' }));
    await screen.findByTestId('export-error-recovery');
    expect(text(screen.getByTestId('export-error-recovery'))).toContain('Some required fields are empty');
    expect(text(screen.getByTestId('export-error-build'))).toBe('Build #1');
    switchTo(view, 'vi', ui());
    expect(text(screen.getByTestId('export-error-recovery'))).toContain('Một số trường bắt buộc còn trống');
    expect(text(screen.getByTestId('export-error-build'))).toBe('Lần tạo #1');
    expect(text(screen.getByText('Chi tiết kỹ thuật'))).toBe('Chi tiết kỹ thuật');
    const detail = screen.getByTestId('export-error-detail');
    expect(text(detail)).toBe('Missing required artifact export fields.');
    expect((detail.closest('details') as HTMLDetailsElement).open).toBe(false);
    expect(actions()).toEqual(['export']);
    walk(task, { role: 'simulated non-coder reviewer (agent)', fixture: 'standalone panel; mocked export 400 with an owned backend message', language: 'en then vi by rerender',
      visibleEvidence: excerpt(screen.getByTestId('export-error-recovery')), action: 'click Build, then switch language', observed: `message and "${text(screen.getByTestId('export-error-build'))}" re-rendered in vi; detail literal and <details> closed; 1 export POST spy call`,
      uncertainty: 'DOM open flag is not a visual collapse check' });
  });

  it.each([
    ['Potential secret-like value detected in artifact export fields.', 'may contain a private key or token', 'khóa riêng tư hoặc mã token'],
    ['Potential secret-like value detected in source content.', 'may contain a private key or token', 'khóa riêng tư hoặc mã token'],
    ['Upstream exploded: ncr-synthetic-trace-42', 'This build could not be confirmed', 'Chưa xác nhận được kết quả tạo'],
  ])('gives localized primary guidance for backend message %j and keeps raw text under technical detail', async (raw, enText, viText) => {
    installFetch({ exportReply: () => reply(raw, false, 400) });
    const ui = () => <ArtifactExportPanel initialRequest={REQ} />;
    const view = render(ui());
    fireEvent.click(screen.getByRole('button', { name: 'Build HTML' }));
    await screen.findByTestId('export-error-recovery');
    expect(text(screen.getByTestId('export-error-recovery'))).toContain(enText);
    expect(text(screen.getByTestId('export-error-recovery'))).not.toContain(raw);
    switchTo(view, 'vi', ui());
    expect(text(screen.getByTestId('export-error-recovery'))).toContain(viText);
    expect(text(screen.getByTestId('export-error-recovery'))).not.toContain(raw);
    expect(text(screen.getByTestId('export-error-detail'))).toBe(raw);
    expect((screen.getByTestId('export-error-detail').closest('details') as HTMLDetailsElement).open).toBe(false);
  });

  it.each([
    ['Complete the goal and criteria first.', 'Enter the goal and all criteria before building.', 'Hãy nhập mục tiêu và đầy đủ tiêu chí trước khi tạo HTML.'],
    ['Resolve the pending operation before another write.', 'A pending operation could not be recorded. Reconcile it before another write.',
      'Chưa ghi nhận được thao tác đang chờ. Hãy đối soát thao tác đó trước khi ghi thêm.'],
  ])('shows actionable EN/VI guidance for owned pre-Build message %j with no export call', async (raw, enText, viText) => {
    installFetch();
    const prepareJob = rejecting(raw);
    const ui = () => <ArtifactExportPanel initialRequest={REQ} prepareJob={prepareJob} />;
    const view = render(ui());
    fireEvent.click(screen.getByRole('button', { name: 'Build HTML' }));
    await screen.findByTestId('export-error-recovery');
    expect(text(screen.getByTestId('export-error-recovery'))).toBe(enText);
    switchTo(view, 'vi', ui());
    expect(text(screen.getByTestId('export-error-recovery'))).toBe(viText);
    expect(text(screen.getByTestId('export-error-detail'))).toBe(raw);
    expect(posts()).toEqual([]);
    expect(prepareJob).toHaveBeenCalledTimes(1);
  });
});
function rejecting(message: string) { return vi.fn(async () => { throw new Error(message); }); }

describe('HtmlJobControls with real ArtifactExportPanel (composition)', () => {
  it('discloses the observed local-test profile before Build in EN and VI, in DOM order, and switches owned labels by rerender', async ({ task }) => {
    const view = await mountJob();
    const build = screen.getByRole('button', { name: 'Build HTML' });
    expectAll(disclosure(), PROFILE_EN);
    expect(disclosure()).not.toContain(GENERIC_EN);
    expect(screen.getByTestId('pre-generate-disclosure').compareDocumentPosition(build) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
    expect(screen.getByLabelText('Local test HTML job')).toBeTruthy();
    expect(screen.getByRole('button', { name: 'Add criterion' })).toBeTruthy();
    fireEvent.change(screen.getByRole('textbox', { name: 'Goal' }), { target: { value: 'ncr-synthetic typed goal' } });
    switchTo(view, 'vi', jobUi());
    expectAll(disclosure(), PROFILE_VI);
    expect(disclosure()).not.toContain(GENERIC_VI);
    expect(screen.getByTestId('pre-generate-disclosure').compareDocumentPosition(screen.getByRole('button', { name: 'Tạo HTML' })) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
    expect(screen.getByLabelText('Tác vụ HTML thử nghiệm cục bộ')).toBeTruthy();
    expect(screen.getByRole('button', { name: 'Thêm tiêu chí' })).toBeTruthy();
    expect(screen.getByRole('textbox', { name: 'Tiêu chí 1' })).toBeTruthy();
    expect((screen.getByRole('textbox', { name: 'Mục tiêu' }) as HTMLTextAreaElement).value).toBe('ncr-synthetic typed goal');
    expect(posts()).toEqual([]);
    walk(task, { role: 'simulated non-coder reviewer (agent)', fixture: 'caps {jobDecisions:true, effectBoundary:"LOCAL_SYNTHETIC"}; invented session u1/o1/t1', language: 'en then vi by rerender',
      visibleEvidence: excerpt(screen.getByTestId('pre-generate-disclosure'), 200), action: 'read disclosure before Build; switch language', observed: 'all 7 profile fragments present in both languages; disclosure precedes the Build button in DOM order; typed goal literal; zero POST',
      uncertainty: 'DOM order is not visual order; wording comprehension unevaluated' });
  });

  it.each([
    ['missing boundary', { jobDecisions: true }, true],
    ['lowercase boundary', { jobDecisions: true, effectBoundary: 'local_synthetic' }, true],
    ['numeric boundary', { jobDecisions: true, effectBoundary: 42 }, true],
    ['other string boundary', { jobDecisions: true, effectBoundary: 'PROVIDER_LIVE' }, true],
    ['jobDecisions false with exact boundary', { jobDecisions: false, effectBoundary: 'LOCAL_SYNTHETIC' }, false],
    ['jobDecisions non-boolean with exact boundary', { jobDecisions: 'true', effectBoundary: 'LOCAL_SYNTHETIC' }, false],
  ])('keeps the generic disclosure for %s and preserves job controls only when jobDecisions is true', async (_name, caps, controls) => {
    const view = await mountJob({ caps: () => reply(caps) });
    expect(disclosure()).toContain(GENERIC_EN);
    expect(disclosure()).not.toContain('local test profile');
    expect(!!screen.queryByTestId('html-job-controls')).toBe(controls);
    expect(!!screen.queryByRole('textbox', { name: 'Goal' })).toBe(controls);
    switchTo(view, 'vi', jobUi());
    expect(disclosure()).toContain(GENERIC_VI);
    expect(posts()).toEqual([]);
  });

  it.each(['owner', 'sourceRecordId'] as const)('ignores a late exact-boundary capability reply after the %s changed (UI negative only)', async (change) => {
    const first = deferred<unknown>(); const second = deferred<unknown>(); let n = 0;
    installFetch({ caps: () => (++n === 1 ? first.promise : second.promise) });
    const view = render(jobUi());
    await waitFor(() => expect(n).toBe(1));
    if (change === 'owner') { h.session = newSession('u2'); view.rerender(jobUi()); } else view.rerender(jobUi('ncr-synthetic-ux-proof-other'));
    await waitFor(() => expect(n).toBe(2));
    second.resolve(reply({ jobDecisions: true }));
    await screen.findByTestId('html-job-controls');
    expect(disclosure()).toContain(GENERIC_EN);
    first.resolve(reply({ jobDecisions: true, effectBoundary: 'LOCAL_SYNTHETIC' }));
    await flush();
    expect(disclosure()).toContain(GENERIC_EN);
    expect(disclosure()).not.toContain('local test profile');
    expect(posts()).toEqual([]);
  });

  it('lets the reader read the disclosure and decline: zero mocked write invocations without a Build click', async ({ task }) => {
    const view = await mountJob();
    fillJob();
    expectAll(disclosure(), PROFILE_EN);
    expect((screen.getByRole('button', { name: 'Build HTML' }) as HTMLButtonElement).disabled).toBe(false);
    const readText = excerpt(screen.getByTestId('pre-generate-disclosure'));
    view.unmount();
    expect(calls.map(c => `${c.method} ${c.url.split('?')[0]}`)).toEqual(['GET /api/artifacts/jobs']);
    expect(posts()).toEqual([]);
    expect(sessionStorage.getItem(JOURNAL_KEY)).toBeNull();
    walk(task, { role: 'simulated non-coder reviewer (agent)', fixture: 'selected profile; goal and criterion typed', language: 'en',
      visibleEvidence: readText, action: 'read disclosure, do not click Build, unmount',
      observed: 'only the capabilities GET was recorded; 0 POST; no pending journal', uncertainty: 'proves wiring/UI availability, not informed consent' });
  });

  it('localizes pending-operation presentation and owned pre-Build guidance; operation values stay literal in the journal; no write is sent', async ({ task }) => {
    sessionStorage.setItem(JOURNAL_KEY, JSON.stringify({ schema: 'cvf.htmlJobPending.v1', owner: OWNER, sourceRecordId: SRC, jobId: JOB, operation: 'CREATE_JOB' }));
    const view = await mountJob();
    const reconcile = screen.getByTestId('reconcile-job-operation');
    expect(text(reconcile)).toContain('Reconcile job creation');
    expect(text(reconcile)).toContain(JOB);
    clickBuild();
    await screen.findByTestId('export-error-recovery');
    expect(text(screen.getByTestId('export-error-recovery'))).toBe('Enter the goal and all criteria before building.');
    switchTo(view, 'vi', jobUi());
    expect(text(screen.getByTestId('reconcile-job-operation'))).toContain('Đối soát tạo tác vụ');
    expect(text(screen.getByTestId('reconcile-job-operation'))).toContain(JOB);
    expect(text(screen.getByTestId('export-error-recovery'))).toBe('Hãy nhập mục tiêu và đầy đủ tiêu chí trước khi tạo HTML.');
    fillJob();
    clickBuild();
    await waitFor(() => expect(text(screen.getByTestId('export-error-detail'))).toBe('Resolve the pending operation before another write.'));
    expect(text(screen.getByTestId('export-error-recovery'))).toBe('Chưa ghi nhận được thao tác đang chờ. Hãy đối soát thao tác đó trước khi ghi thêm.');
    switchTo(view, 'en', jobUi());
    expect(text(screen.getByTestId('export-error-recovery'))).toBe('A pending operation could not be recorded. Reconcile it before another write.');
    expect(sessionStorage.getItem(JOURNAL_KEY)).toContain('"operation":"CREATE_JOB"');
    expect(posts()).toEqual([]);
    walk(task, { role: 'simulated non-coder reviewer (agent)', fixture: 'pre-seeded invented pending CREATE_JOB journal for the same owner and record', language: 'en, vi, en by rerender',
      visibleEvidence: excerpt(screen.getByTestId('reconcile-job-operation')), action: 'click Build with empty goal, then with goal filled', observed: 'reconcile label "job creation"/"tạo tác vụ" with literal job ID; both owned messages localized; journal still holds CREATE_JOB; 0 POST',
      uncertainty: 'no reconciliation was exercised here; Reconcile button not clicked' });
  });

  it('shows Stop and status while an export is in flight, suppresses the late result after a local stop, and sends no stop request', async ({ task }) => {
    const gate = deferred<unknown>();
    const view = await mountJob({ exportReply: () => gate.promise });
    fillJob();
    clickBuild();
    await screen.findByTestId('stop-html-build');
    await waitFor(() => expect(actions()).toEqual(['CREATE_JOB', 'export']));
    expect(text(screen.getByTestId('stop-html-build'))).toBe('Stop locally');
    expect(screen.getByRole('button', { name: 'Generating' }).getAttribute('aria-busy')).toBe('true');
    switchTo(view, 'vi', jobUi());
    expect(text(screen.getByTestId('stop-html-build'))).toBe('Dừng tại đây');
    expect(screen.getByRole('button', { name: 'Đang tạo' }).getAttribute('aria-busy')).toBe('true');
    fireEvent.click(screen.getByTestId('stop-html-build'));
    expect(screen.queryByTestId('stop-html-build')).toBeNull();
    expect(text(screen.getByTestId('stopped-unknown'))).toContain('Đã dừng tại đây. Thao tác từ xa có thể vẫn tiếp tục và chi phí chưa rõ.');
    switchTo(view, 'en', jobUi());
    expect(text(screen.getByTestId('stopped-unknown'))).toContain('Stopped locally. Remote completion and cost are unknown.');
    gate.resolve(reply(EXPORT_RESULT));
    await flush();
    expect(screen.queryByTestId('artifact-draft-state')).toBeNull();
    expect(screen.getAllByText('Build an HTML review packet to preview it here.').length).toBeGreaterThan(0);
    expect(actions()).toEqual(['CREATE_JOB', 'export']);
    clickBuild();
    await flush();
    expect(actions()).toEqual(['CREATE_JOB', 'export']);
    walk(task, { role: 'simulated non-coder reviewer (agent)', fixture: 'export POST held open by a deferred mock; selected profile', language: 'en, vi, en by rerender',
      visibleEvidence: `${excerpt(screen.getByTestId('stopped-unknown'), 110)}`, action: 'Build, read Stop/status, click Stop, release the late mocked response, click Build again',
      observed: 'Stop and aria-busy Build shown in both languages; after Stop the late success is not displayed (no draft state), preview stays empty; spy ledger CREATE_JOB, export only; same request not re-sent',
      uncertainty: 'client-side fence only; no abort-signal, remote-stop or cost behavior is claimed' });
  });

  it('records separate simulated Build, Save, link and review spy calls; notices and the review record translate on rerender', async ({ task }) => {
    const view = await mountJob();
    fillJob();
    clickBuild();
    await screen.findByTestId('artifact-draft-state');
    expect(text(screen.getByTestId('artifact-draft-state'))).toContain('DRAFT / UNACCEPTED');
    expect(text(screen.getByTestId('current-job-id'))).toContain(JOB);
    fireEvent.click(screen.getByTestId('stub-save'));
    await screen.findByText('Exact saved version linked.');
    const review = screen.getByLabelText('Review saved HTML version');
    expect(text(review)).toContain(`Saved draft ${VERSION}: sent from this device, not verified, not accepted.`);
    expect(text(review)).toContain('Current displayed job and saved version.');
    switchTo(view, 'vi', jobUi());
    expect(text(screen.getByText('Đã liên kết đúng phiên bản đã lưu.'))).toBe('Đã liên kết đúng phiên bản đã lưu.');
    expect(text(screen.getByLabelText('Rà soát phiên bản HTML đã lưu'))).toContain(`Bản nháp đã lưu ${VERSION}: đã gửi từ thiết bị này, chưa xác minh, chưa được chấp nhận.`);
    fireEvent.click(screen.getByRole('checkbox', { name: /Tôi đã rà soát đúng phiên bản đã lưu này/ }));
    fireEvent.click(screen.getByTestId('accept-synthetic-version'));
    await screen.findByText('Hãy thêm ghi chú có thể kiểm tra cho từng tiêu chí.');
    expect(actions()).toEqual(['CREATE_JOB', 'export', 'SAVE_DRAFT', 'LINK_VERSION']);
    switchTo(view, 'en', jobUi());
    expect(screen.getByText('Add an inspectable note for every criterion.')).toBeTruthy();
    fireEvent.change(screen.getByRole('textbox', { name: 'Review note c1' }), { target: { value: 'ncr-synthetic observed note' } });
    fireEvent.click(screen.getByTestId('accept-synthetic-version'));
    await screen.findByTestId('synthetic-review-decision');
    expectAll(text(screen.getByTestId('synthetic-review-decision')), ['A local test review by the same user was recorded for this original version:', DECISION, 'Draft provenance remains unverified.']);
    switchTo(view, 'vi', jobUi());
    expectAll(text(screen.getByTestId('synthetic-review-decision')), ['Đã ghi nhận lượt rà soát thử nghiệm cục bộ của cùng người dùng', DECISION, 'Nguồn gốc bản nháp vẫn chưa được xác minh.']);
    expect(actions()).toEqual(['CREATE_JOB', 'export', 'SAVE_DRAFT', 'LINK_VERSION', 'ACCEPT_VERSION']);
    expect((screen.getByRole('textbox', { name: 'Ghi chú rà soát c1' }) as HTMLTextAreaElement).value).toBe('ncr-synthetic observed note');
    walk(task, { role: 'simulated non-coder reviewer (agent)', fixture: 'selected profile; mocked CREATE_JOB/export/LINK_VERSION/ACCEPT_VERSION; Save via disclosed stub', language: 'en and vi by rerender',
      visibleEvidence: excerpt(screen.getByTestId('synthetic-review-decision'), 160), action: 'Build, stub Save, tick confirmation without note, add note, record review',
      observed: 'spy order CREATE_JOB, export, SAVE_DRAFT, LINK_VERSION, ACCEPT_VERSION; empty-note notice shown in vi then en; decision text and literal decision ID present; typed note literal',
      uncertainty: 'Save is a stub and these POSTs are mocked; no draft-save, link, review, writer or auth correctness is claimed' });
  });
});
