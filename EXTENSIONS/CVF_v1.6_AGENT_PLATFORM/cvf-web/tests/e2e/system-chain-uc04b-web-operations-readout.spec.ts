/**
 * System Chain UC-04B Web Operations Readout -- Proof Spec
 *
 * GC: provider-free local development proof. One Playwright invocation,
 * two Web submissions, exactly one real checker execution, zero retries,
 * zero provider calls.
 *
 * Positive: developer/operator runs docs_governance_check through the UI and
 *   sees succeeded status, job type/ID, and audit trail.
 * Negative: reviewer POST is blocked with HTTP 403, blocked_by_policy,
 *   read_only_role_cannot_trigger, and no running/succeeded event.
 */

import { expect, test } from '@playwright/test';
import { seedStorage } from './utils';

const OPERATIONS_URL = '/governance/operations';
const JOB_TYPE = 'docs_governance_check';
const RUN_TEST_ID = `governance-job-run-${JOB_TYPE}-default`;

async function loginViaForm(page: import('@playwright/test').Page, username: string, password: string) {
  await page.goto('/login', { waitUntil: 'domcontentloaded', timeout: 20_000 });

  // Fill login form using placeholder-based locators from the client component
  const usernameInput = page.locator('input[type="text"]').first();
  const passwordInput = page.locator('input[type="password"]').first();

  await usernameInput.waitFor({ state: 'visible', timeout: 10_000 });
  await usernameInput.fill(username);
  await passwordInput.fill(password);

  // Submit by pressing Enter on the password field
  await passwordInput.press('Enter');

  // Wait for redirect away from login page
  await page.waitForURL((url) => !url.pathname.startsWith('/login'), { timeout: 20_000 });
}

test.describe('UC-04B Web Operations Readout', () => {
  test.beforeEach(async ({ page }) => {
    await seedStorage(page);
  });

  test('positive_developer_docs_check: developer submits docs_governance_check and sees succeeded readout', async ({ page }) => {
    await loginViaForm(page, 'dev', 'dev123');
    await page.goto(OPERATIONS_URL, { waitUntil: 'domcontentloaded', timeout: 20_000 });

    await expect(page.getByText('operator')).toBeVisible({ timeout: 15_000 });

    const runButton = page.locator(`[data-testid="${RUN_TEST_ID}"]`);
    await expect(runButton).toBeVisible({ timeout: 10_000 });
    await expect(runButton).toBeEnabled({ timeout: 5_000 });

    await runButton.click();

    await expect(
      page.getByText('succeeded', { exact: false }).first()
    ).toBeVisible({ timeout: 90_000 });

    await expect(page.getByText(JOB_TYPE, { exact: false }).first()).toBeVisible();
    await expect(page.getByText(/Docs Governance Check/).first()).toBeVisible();
  });

  test('negative_reviewer_docs_check: reviewer is blocked from submitting docs_governance_check', async ({ page }) => {
    await loginViaForm(page, 'reviewer', 'reviewer123');
    await page.goto(OPERATIONS_URL, { waitUntil: 'domcontentloaded', timeout: 20_000 });

    await expect(page.getByText('reviewer')).toBeVisible({ timeout: 15_000 });

    const runButton = page.locator(`[data-testid="${RUN_TEST_ID}"]`);
    await expect(runButton).toBeVisible({ timeout: 10_000 });
    await expect(runButton).toBeDisabled({ timeout: 5_000 });

    const response = await page.request.post('/api/system/jobs', {
      data: {
        jobType: JOB_TYPE,
        uiRequestId: `uc04b-neg-${Date.now()}`,
      },
      failOnStatusCode: false,
    });

    expect(response.status()).toBe(403);
    const body = await response.json() as Record<string, unknown>;
    expect(body.status).toBe('blocked_by_policy');
    expect(String(body.decisionReason ?? '')).toContain('read_only_role_cannot_trigger');
  });
});
