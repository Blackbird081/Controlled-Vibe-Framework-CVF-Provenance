import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { NextRequest } from 'next/server';

const fsMocks = vi.hoisted(() => ({ existsSync: vi.fn(), readFileSync: vi.fn() }));
const verifySessionCookieMock = vi.hoisted(() => vi.fn());

vi.mock('node:fs', () => ({ ...fsMocks, default: fsMocks }));
vi.mock('@/lib/middleware-auth', () => ({ verifySessionCookie: verifySessionCookieMock }));

import { sha256Hex } from '@/lib/lpci/audit-receipt';
import { serializeExactJson } from '@/lib/lpci/query-conformance';
import { deriveServiceTokenIdentity } from '@/lib/service-token-auth';
import { POST } from './route';

const corpusId = 'TEST_CORPUS';
let indexValue: unknown;
let registered = true;

const baseRecord = (overrides: Record<string, unknown> = {}) => ({
  normalizedPath: 'public/leave.pdf', sourceHash: 'must-not-leak', documentType: 'policy',
  status: 'effective', answerClass: 'DIRECT_CITED_ANSWER', rawDisposition: 'ACCEPT',
  dispositionAlias: 'ACCEPT', sensitivityLevel: 'public', effectiveDate: '2026-01-02',
  authorityLevel: 'policy', titleSnippet: 'Leave policy', contentSnippet: 'leave policy public evidence',
  ...overrides,
});

function request(body: unknown) {
  return new NextRequest('http://localhost/api/lpci/query', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'x-cvf-service-token': 'fake-service-token' },
    body: typeof body === 'string' ? body : JSON.stringify(body),
  });
}

async function post(body: unknown = { query: 'leave policy', corpusId, filters: {} }) {
  const response = await POST(request(body));
  return { response, data: await response.json() };
}

function expectAuditedCorrelation(
  data: Record<string, unknown>,
  evidenceOutcome?: string,
  matchedPaths?: string[],
) {
  const audit = data.auditReceipt as Record<string, unknown>;
  const proof = data.routeGovernanceProof as Record<string, unknown>;
  expect(data.auditId).toBe(audit.auditId);
  expect(data.corpusId).toBe(corpusId);
  expect(data.authorizationDecision).toBe('PUBLIC_ONLY');
  if (evidenceOutcome) expect(data.evidenceOutcome).toBe(evidenceOutcome);
  if (matchedPaths) expect(audit.matched_paths).toEqual(matchedPaths);
  expect(proof.authMode).toBe('service_token');
  expect(proof.actorId).toBe(deriveServiceTokenIdentity('fake-service-token'));
  expect(proof.decision).toBe('ALLOW');
  expect(proof.routeId).toBe('/api/lpci/query');
}

function expectExactKeys(data: Record<string, unknown>, keys: string[]) {
  expect(Object.keys(data).sort()).toEqual([...keys].sort());
}

describe('POST /api/lpci/query conformance', () => {
  beforeEach(() => {
    registered = true;
    indexValue = [baseRecord()];
    process.env.CVF_SERVICE_TOKEN = 'fake-service-token';
    delete process.env.LPCI_LLM_API_KEY;
    verifySessionCookieMock.mockReset();
    verifySessionCookieMock.mockResolvedValue(null);
    fsMocks.existsSync.mockReset();
    fsMocks.existsSync.mockReturnValue(true);
    fsMocks.readFileSync.mockReset();
    fsMocks.readFileSync.mockImplementation((path: unknown) => {
      const text = String(path);
      if (text.includes('CVF_CORPUS_SCAN_REGISTRY.json')) {
        return JSON.stringify({ corpora: registered ? [{ id: corpusId }] : [] });
      }
      return typeof indexValue === 'string' ? indexValue : JSON.stringify(indexValue);
    });
    vi.stubGlobal('fetch', vi.fn());
  });

  afterEach(() => {
    delete process.env.LPCI_LLM_API_KEY;
    delete process.env.CVF_SERVICE_TOKEN;
    vi.unstubAllGlobals();
  });

  it('returns minimized CORPUS_NOT_REGISTERED with sanitized filters and zero fetches', async () => {
    registered = false;
    const { response, data } = await post({
      query: 'leave policy', corpusId, filters: { sensitivityClearance: true, jurisdiction: ' Vietnam ' },
    });
    expect(response.status).toBe(403);
    expect(Object.keys(data).sort()).toEqual([
      'auditId', 'auditReceipt', 'authorizationDecision', 'corpusId', 'evidenceOutcome',
      'message', 'outcome', 'query', 'routeGovernanceProof',
    ].sort());
    expect(data.outcome).toBe('CORPUS_NOT_REGISTERED');
    expect(data.auditReceipt.applied_filters).toEqual({ jurisdiction: 'Vietnam', sensitivityClearance: false });
    expect(data.auditReceipt.matched_paths).toEqual([]);
    expectAuditedCorrelation(data);
    expect(fetch).not.toHaveBeenCalled();
  });

  it.each(['not-json', '{}', '[1]'])('maps malformed registered index to grounding unavailable: %s', async (value) => {
    indexValue = value;
    const { data } = await post();
    expect(data.outcome).toBe('GROUNDING_EVIDENCE_UNAVAILABLE');
    expect(data.message).toBe('Grounding evidence is unavailable for this query.');
    expect(data.auditReceipt.matched_paths).toEqual([]);
    expect(data.auditReceipt.sensitivity_pre_filter_applied).toBe(false);
    expect(fetch).not.toHaveBeenCalled();
  });

  it('maps missing index and invalid sensitivity to pre-filter grounding failures', async () => {
    fsMocks.existsSync.mockReturnValue(false);
    expect((await post()).data.outcome).toBe('GROUNDING_EVIDENCE_UNAVAILABLE');
    fsMocks.existsSync.mockReturnValue(true);
    indexValue = [{ sensitivityLevel: 'Public', normalizedPath: 'secret' }];
    const { data } = await post();
    expect(data.auditReceipt.sensitivity_pre_filter_applied).toBe(false);
    expect(data.auditReceipt.matched_paths).toEqual([]);
    expect(fetch).not.toHaveBeenCalled();
  });

  it('filters non-public rows before malformed nonsensitivity fields can influence output', async () => {
    indexValue = [
      baseRecord(),
      { sensitivityLevel: 'classified', normalizedPath: '../secret', contentSnippet: 'secret', status: null },
    ];
    const { data } = await post();
    expect(data.outcome).toBe('NO_PROVIDER_CONFIGURED');
    expect(data.auditReceipt.matched_paths).toEqual(['public/leave.pdf']);
    expect(JSON.stringify(data)).not.toContain('secret');
    expect(fetch).not.toHaveBeenCalled();
  });

  it('returns top-level Phase 1 receipts with compatibility and exact hash bytes', async () => {
    indexValue = [baseRecord({ contentSnippet: 'other topic', titleSnippet: 'other topic' })];
    const { data } = await post();
    expect(data.outcome).toBe('PHASE1_NEGATIVE');
    expect(data.receiptType).toBe('NO_RESULTS');
    expect(data.auditReceipt.phase1_receipt_type).toBe(data.receiptType);
    expect(data.auditReceipt.matched_paths).toEqual([]);
    expect(data.phase1Receipt).toBeUndefined();
    const expected = serializeExactJson({
      outcome: 'PHASE1_NEGATIVE', receiptType: 'NO_RESULTS', query: 'leave policy', corpusId,
      authorizationDecision: 'PUBLIC_ONLY', evidenceOutcome: 'NO_MATCHES',
    });
    expect(data.auditReceipt.model_response_hash).toBe(sha256Hex(expected));
    expect(fetch).not.toHaveBeenCalled();
  });

  it('preserves all three canonical Phase 1 variants at top level', async () => {
    const cases = [
      {
        records: [baseRecord({ contentSnippet: 'other topic', titleSnippet: 'other topic' })],
        receiptType: 'NO_RESULTS', evidenceOutcome: 'NO_MATCHES', reason: undefined,
      },
      {
        records: [baseRecord({ sensitivityLevel: 'classified' })],
        receiptType: 'FILTERED_OUT', evidenceOutcome: 'FILTERED_PUBLIC_ONLY',
        reason: 'all records excluded by sensitivity filter',
      },
      {
        records: [baseRecord({ answerClass: 'ESCALATE_OR_ABSTAIN' })],
        receiptType: 'ESCALATED', evidenceOutcome: 'ABSTAINED',
        reason: 'all matched records require escalation or abstention',
      },
    ] as const;

    for (const testCase of cases) {
      indexValue = testCase.records;
      const { data } = await post();
      expect(data).toMatchObject({
        outcome: 'PHASE1_NEGATIVE', receiptType: testCase.receiptType,
        query: 'leave policy', evidenceOutcome: testCase.evidenceOutcome,
      });
      expect(data.reason).toBe(testCase.reason);
      expect(data.phase1Receipt).toBeUndefined();
      expect(data.auditReceipt.phase1_receipt_type).toBe(testCase.receiptType);
      expectExactKeys(data, [
        'outcome', 'receiptType', 'query',
        ...(testCase.reason === undefined ? [] : ['reason']),
        'corpusId', 'auditId', 'authorizationDecision', 'evidenceOutcome',
        'auditReceipt', 'routeGovernanceProof',
      ]);
      expectAuditedCorrelation(data, testCase.evidenceOutcome, []);
    }
    expect(fetch).not.toHaveBeenCalled();
  });

  it('returns FILTERED_OUT for all denied records regardless of client clearance', async () => {
    indexValue = [baseRecord({ sensitivityLevel: 'classified' })];
    const { data } = await post({ query: 'leave policy', corpusId, filters: { sensitivityClearance: true } });
    expect(data).toMatchObject({ outcome: 'PHASE1_NEGATIVE', receiptType: 'FILTERED_OUT' });
    expect(data.auditReceipt.applied_filters.sensitivityClearance).toBe(false);
    expect(data.auditReceipt.matched_paths).toEqual([]);
    expect(fetch).not.toHaveBeenCalled();
  });

  it('fails malformed admitted-public records before search with empty audit paths', async () => {
    indexValue = [baseRecord({ normalizedPath: '../bad' })];
    const { data } = await post();
    expect(data.outcome).toBe('GROUNDING_EVIDENCE_UNAVAILABLE');
    expect(data.auditReceipt.sensitivity_pre_filter_applied).toBe(true);
    expect(data.auditReceipt.matched_paths).toEqual([]);
    expect(fetch).not.toHaveBeenCalled();
  });

  it.each([
    ['status', 'invalid'],
    ['answerClass', 'INVALID'],
    ['effectiveDate', '2026-02-30'],
    ['normalizedPath', '../bad'],
    ['contentSnippet', 7],
    ['authorityLevel', []],
  ])('fails admitted-public invalid %s before matching', async (field, value) => {
    indexValue = [baseRecord({ [field]: value })];
    const { data } = await post();
    expect(data.outcome).toBe('GROUNDING_EVIDENCE_UNAVAILABLE');
    expectAuditedCorrelation(data, 'UNAVAILABLE', []);
    expect(data.auditReceipt.sensitivity_pre_filter_applied).toBe(true);
    expect(fetch).not.toHaveBeenCalled();
  });

  it('abstains on mixed direct and escalate matches with zero fetches', async () => {
    indexValue = [
      baseRecord(),
      baseRecord({ normalizedPath: 'public/escalate.pdf', answerClass: 'ESCALATE_OR_ABSTAIN' }),
    ];
    const { data } = await post();
    expect(data.outcome).toBe('ABSTAINED');
    expect(data.auditReceipt.matched_paths).toEqual(['public/leave.pdf', 'public/escalate.pdf']);
    expect(data.auditReceipt.response_boundary_class).toBe('ABSTAINED');
    expectAuditedCorrelation(data);
    expect(fetch).not.toHaveBeenCalled();
  });

  it('returns minimized no-provider response and audit-path count source', async () => {
    const { data } = await post();
    expect(data.outcome).toBe('NO_PROVIDER_CONFIGURED');
    expect(data.message).toBe('No answer provider is configured.');
    expect(data.retrievalReceipt).toBeUndefined();
    expect(data.matchedSources).toBeUndefined();
    expect(data.auditReceipt.matched_paths).toEqual(['public/leave.pdf']);
    expect(data.auditReceipt.sensitivity_pre_filter_applied).toBe(true);
    expectAuditedCorrelation(data);
    expect(fetch).not.toHaveBeenCalled();
  });

  it('sends one allowlisted JSON evidence object and emits correlated answer', async () => {
    process.env.LPCI_LLM_API_KEY = 'fixed-fake-test-key';
    vi.mocked(fetch).mockResolvedValue(new Response(JSON.stringify({
      choices: [{ message: { content: 'Based on retrieved documents only. Answer.' } }],
    }), { status: 200, headers: { 'Content-Type': 'application/json' } }));
    const { data } = await post();
    expect(fetch).toHaveBeenCalledTimes(1);
    const call = vi.mocked(fetch).mock.calls[0];
    const providerBody = JSON.parse(String((call[1] as RequestInit).body));
    const prompt = providerBody.messages[0].content as string;
    expect(prompt.match(/"schemaVersion"/g)).toHaveLength(1);
    expect(prompt).toContain('leave policy public evidence');
    expect(prompt).not.toContain('must-not-leak');
    expect(data.outcome).toBe('ANSWER_EMITTED');
    expect(data.matchedSources).toEqual(data.auditReceipt.matched_paths);
    expect(data.auditReceipt.model_response_hash).toBe(sha256Hex(data.response));
    expectAuditedCorrelation(data);
  });

  it('sends four valid boundary records in exactly one mocked provider call', async () => {
    indexValue = Array.from({ length: 4 }, (_, index) => baseRecord({
      normalizedPath: `public/${index}.pdf`,
      contentSnippet: `${'x'.repeat(499)} leave policy`,
    }));
    process.env.LPCI_LLM_API_KEY = 'fixed-fake-test-key';
    vi.mocked(fetch).mockResolvedValue(new Response(JSON.stringify({
      choices: [{ message: { content: 'Based on retrieved documents only. Four records.' } }],
    }), { status: 200, headers: { 'Content-Type': 'application/json' } }));

    const { data } = await post();

    expect(data.outcome).toBe('ANSWER_EMITTED');
    expect(data.auditReceipt.matched_paths).toHaveLength(4);
    expect(fetch).toHaveBeenCalledTimes(1);
    const providerBody = JSON.parse(String((vi.mocked(fetch).mock.calls[0][1] as RequestInit).body));
    const prompt = providerBody.messages[0].content as string;
    expect((prompt.match(/"normalizedPath"/g) ?? [])).toHaveLength(4);
  });

  it('returns fixed safe provider error after exactly one mocked fetch', async () => {
    process.env.LPCI_LLM_API_KEY = 'fixed-fake-test-key';
    vi.mocked(fetch).mockResolvedValue(new Response('sensitive provider body', { status: 500 }));
    const { response, data } = await post();
    expect(fetch).toHaveBeenCalledTimes(1);
    expect(response.status).toBe(502);
    expect(data.outcome).toBe('PROVIDER_ERROR');
    expect(data.message).toBe('The answer provider is temporarily unavailable.');
    expect(JSON.stringify(data)).not.toContain('sensitive provider body');
    expect(data.error).toBeUndefined();
    const expected = serializeExactJson({
      outcome: 'PROVIDER_ERROR', query: 'leave policy', corpusId,
      authorizationDecision: 'PUBLIC_ONLY', evidenceOutcome: 'PROVIDER_FAILED',
      message: 'The answer provider is temporarily unavailable.',
    });
    expect(data.auditReceipt.model_response_hash).toBe(sha256Hex(expected));
    expectAuditedCorrelation(data, 'PROVIDER_FAILED', ['public/leave.pdf']);
  });

  it('enforces exact response allowlists and correlation for every audited variant', async () => {
    const common = [
      'outcome', 'query', 'corpusId', 'auditId', 'authorizationDecision',
      'evidenceOutcome', 'auditReceipt', 'routeGovernanceProof',
    ];

    registered = false;
    let result = (await post()).data;
    expectExactKeys(result, [...common, 'message']);
    expectAuditedCorrelation(result, 'NOT_EVALUATED', []);

    registered = true;
    indexValue = 'not-json';
    result = (await post()).data;
    expectExactKeys(result, [...common, 'message']);
    expectAuditedCorrelation(result, 'UNAVAILABLE', []);

    indexValue = [baseRecord({ contentSnippet: 'other topic', titleSnippet: 'other topic' })];
    result = (await post()).data;
    expectExactKeys(result, [...common, 'receiptType']);
    expectAuditedCorrelation(result, 'NO_MATCHES', []);

    indexValue = [baseRecord(), baseRecord({
      normalizedPath: 'public/escalate.pdf', answerClass: 'ESCALATE_OR_ABSTAIN',
    })];
    result = (await post()).data;
    expectExactKeys(result, [...common, 'response', 'answerClass']);
    expectAuditedCorrelation(result, 'ABSTAINED', ['public/leave.pdf', 'public/escalate.pdf']);

    indexValue = [baseRecord()];
    result = (await post()).data;
    expectExactKeys(result, [...common, 'message']);
    expectAuditedCorrelation(result, 'ELIGIBLE_NOT_SENT', ['public/leave.pdf']);

    process.env.LPCI_LLM_API_KEY = 'fixed-fake-test-key';
    vi.mocked(fetch).mockResolvedValueOnce(new Response('private provider diagnostic', { status: 500 }));
    result = (await post()).data;
    expectExactKeys(result, [...common, 'message']);
    expectAuditedCorrelation(result, 'PROVIDER_FAILED', ['public/leave.pdf']);

    vi.mocked(fetch).mockResolvedValueOnce(new Response(JSON.stringify({
      choices: [{ message: { content: 'Based on retrieved documents only. Answer.' } }],
    }), { status: 200, headers: { 'Content-Type': 'application/json' } }));
    result = (await post()).data;
    expectExactKeys(result, [
      ...common, 'response', 'answerClass', 'matchedSources', 'freshnessFlag', 'conflictFlag',
    ]);
    expectAuditedCorrelation(result, 'ANSWER_EMITTED', ['public/leave.pdf']);
    expect(result.matchedSources).toEqual((result.auditReceipt as { matched_paths: string[] }).matched_paths);
    expect(fetch).toHaveBeenCalledTimes(2);
  });

  it('fails record and aggregate evidence limits with zero fetches', async () => {
    indexValue = Array.from({ length: 5 }, (_, index) => baseRecord({ normalizedPath: `public/${index}.pdf` }));
    let data = (await post()).data;
    expect(data.outcome).toBe('GROUNDING_EVIDENCE_UNAVAILABLE');
    expectAuditedCorrelation(data, 'UNAVAILABLE', [
      'public/0.pdf', 'public/1.pdf', 'public/2.pdf', 'public/3.pdf', 'public/4.pdf',
    ]);
    expect(fetch).not.toHaveBeenCalled();
    indexValue = [baseRecord({ contentSnippet: 'x'.repeat(513), titleSnippet: 'leave policy' })];
    data = (await post()).data;
    expect(data.outcome).toBe('GROUNDING_EVIDENCE_UNAVAILABLE');
    expectAuditedCorrelation(data, 'UNAVAILABLE', []);
    expect(fetch).not.toHaveBeenCalled();
  });

  it('rejects unpaired request strings before corpus work', async () => {
    const { response, data } = await post({ query: `leave\ud800`, corpusId });
    expect(response.status).toBe(400);
    expect(data.outcome).toBe('INVALID_REQUEST');
    expect(data.auditReceipt).toBeUndefined();
    expect(fsMocks.readFileSync).not.toHaveBeenCalled();
    expect(fetch).not.toHaveBeenCalled();
  });
});
