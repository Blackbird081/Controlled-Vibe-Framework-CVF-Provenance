import { test, expect } from '@playwright/test';

import { login, seedStorageWithAlibaba } from './utils';

const hasAlibabaKey = Boolean(
  process.env.DASHSCOPE_API_KEY
  || process.env.ALIBABA_API_KEY
  || process.env.CVF_ALIBABA_API_KEY
  || process.env.CVF_BENCHMARK_ALIBABA_KEY,
);

test.beforeEach(async ({ page }) => {
  test.skip(!hasAlibabaKey, 'Phase E workflow binding live proof requires a DashScope-compatible key.');
  await seedStorageWithAlibaba(page);
});

test('Phase E E.4 emits workflow step traces and receipt pointers on live Product Brief execution', async ({ page }) => {
  await login(page);

  const response = await page.request.post('/api/execute', {
    data: {
      templateId: 'app_builder_complete',
      templateName: 'App Builder Complete',
      intent: 'Create a concise product brief for TaskFlow, a lightweight task-planning app for small product teams.',
      inputs: {
        appName: 'TaskFlow',
        appType: 'Web App',
        problem: 'Small teams need a lighter way to plan, triage, and hand off work.',
        targetUsers: 'Small product teams and founders',
        coreFeatures: 'Task board, owner fields, status filters, acceptance criteria, weekly summary',
        successCriteria: 'A user can create, assign, filter, and review tasks without onboarding friction.',
        platforms: 'Web browser',
      },
      provider: 'alibaba',
      model: 'qwen-turbo',
      cvfPhase: 'BUILD',
      cvfRiskLevel: 'R1',
      action: 'build template execution request',
      skillPreflightPassed: true,
      skillPreflightDeclaration: 'SKILL PREFLIGHT PASS: product brief only, no implementation.',
      skillIds: ['product-brief-authoring'],
      aiCommit: {
        commitId: 'phase-e-e4-workflow-live-proof',
        agentId: 'cvf-playwright-live',
        timestamp: Date.now(),
        description: 'Phase E E.4 workflow trace live proof',
      },
    },
  });

  const body = await response.json();

  expect(response.status()).toBe(200);
  expect(body.success).toBe(true);
  expect(body.providerRouting?.selectedProvider).toBe('alibaba');
  expect(body.workflowId).toBe('workflow.product.create_product_brief.v1');
  expect(body.stepTraces.map((trace: { stepId: string }) => trace.stepId)).toEqual([
    'step-1-intake-validation',
    'step-2-knowledge-retrieval',
    'step-3-provider-call',
    'step-5-receipt-emit',
  ]);
  expect(body.stepTraces).not.toContainEqual(
    expect.objectContaining({ stepId: 'step-4-review-gate' }),
  );
  expect(body.receipts).toEqual(body.stepTraces.map((trace: { stepId: string }) => ({
    stepId: trace.stepId,
    receiptId: body.governanceEvidenceReceipt.receiptId,
    source: 'governance_evidence_receipt',
  })));
  expect(body.deferredStepIds).toEqual(['step-4-review-gate']);
  expect(String(body.output ?? '')).not.toContain('MOCK_');
});
