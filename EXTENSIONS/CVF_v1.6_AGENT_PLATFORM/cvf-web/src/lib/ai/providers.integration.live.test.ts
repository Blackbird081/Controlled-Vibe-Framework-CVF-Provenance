/**
 * @vitest-environment jsdom
 */
import { describe, it, expect } from 'vitest';
import { executeAI } from './providers';

const prompt = 'Return only the word OK.';
const options = { maxTokens: 32, temperature: 0 };

const openaiKey = process.env.OPENAI_API_KEY;
const geminiKey = process.env.GOOGLE_AI_API_KEY;
const claudeKey = process.env.ANTHROPIC_API_KEY;

// EAFR-R1D activation barrier. These cases perform real, billable provider
// requests. An available API key is NOT sufficient to activate them: the shared
// test setup loads `.env.local` into `process.env`, so a key is present in
// ordinary local runs without anyone intending live traffic. Activation
// therefore requires an explicit opt-in that no default run sets. When the
// opt-in is absent the cases skip; they never fail for lack of it.
const liveProviderCallsAllowed = process.env.CVF_ALLOW_LIVE_TESTS === '1';

describe('AI provider integration (real)', () => {
    const testOpenAI = liveProviderCallsAllowed && openaiKey ? it : it.skip;
    const testGemini = liveProviderCallsAllowed && geminiKey ? it : it.skip;
    const testClaude = liveProviderCallsAllowed && claudeKey ? it : it.skip;

    testOpenAI('executes OpenAI provider', { timeout: 60000 }, async () => {
        const result = await executeAI('openai', openaiKey as string, prompt, options);
        expect(result.success).toBe(true);
        expect(result.output).toBeTruthy();
    });

    testGemini('executes Gemini provider', { timeout: 60000 }, async () => {
        const result = await executeAI('gemini', geminiKey as string, prompt, options);
        expect(result.success).toBe(true);
        expect(result.output).toBeTruthy();
    });

    testClaude('executes Claude provider', { timeout: 60000 }, async () => {
        const result = await executeAI('claude', claudeKey as string, prompt, options);
        expect(result.success).toBe(true);
        expect(result.output).toBeTruthy();
    });
});
