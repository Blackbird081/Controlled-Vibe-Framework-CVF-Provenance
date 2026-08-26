import { describe, expect, it, vi } from "vitest";
import { CredentialBoundary } from "../src/credential-boundary";
import {
  createCredentialBoundOpenAiCompatibleExecuteAdapter,
  createOpenAiCompatibleExecuteAdapter,
  type OpenAiCompatibleFetch,
} from "../src/openai-compatible-execute-adapter";

const reference = {
  providerId: "openai",
  keyId: "lpci-openai",
  envNames: ["LPCI_LLM_API_KEY"],
};

function successFetch(content = "answer") {
  return vi.fn(async () => ({
    ok: true,
    status: 200,
    json: async () => ({
      choices: [{ message: { content } }],
      usage: { prompt_tokens: 4, completion_tokens: 2 },
    }),
  })) as unknown as OpenAiCompatibleFetch;
}

describe("OpenAI-compatible execute adapter", () => {
  it("maps one injected fetch response without exposing the secret", async () => {
    const fetchImpl = successFetch();
    const adapter = createOpenAiCompatibleExecuteAdapter({
      providerId: "openai",
      modelId: "gpt-4o",
      endpoint: "https://api.openai.com/v1/chat/completions",
      secret: "fake-test-secret",
      fetchImpl,
    });

    const result = await adapter.execute({
      traceId: "trace-1",
      providerId: "openai",
      modelId: "gpt-4o",
      prompt: "question",
      systemPrompt: "system",
    });

    expect(fetchImpl).toHaveBeenCalledTimes(1);
    expect(result).toEqual({
      text: "answer",
      usage: { inputTokens: 4, outputTokens: 2 },
    });
    expect(JSON.stringify(result)).not.toContain("fake-test-secret");
  });

  it("forwards the adapter AbortSignal to the actual fetch entry", async () => {
    const fetchImpl = successFetch();
    const adapter = createOpenAiCompatibleExecuteAdapter({
      providerId: "openai",
      modelId: "gpt-4o",
      endpoint: "https://api.openai.com/v1/chat/completions",
      secret: "fake-test-secret",
      fetchImpl,
    });
    const controller = new AbortController();
    await adapter.execute({
      traceId: "trace-signal",
      providerId: "openai",
      modelId: "gpt-4o",
      prompt: "question",
      signal: controller.signal,
    });
    expect(fetchImpl).toHaveBeenCalledWith(
      "https://api.openai.com/v1/chat/completions",
      expect.objectContaining({ signal: controller.signal }),
    );
  });

  it("fails identity mismatch before the injected fetch", async () => {
    const fetchImpl = successFetch();
    const adapter = createOpenAiCompatibleExecuteAdapter({
      providerId: "openai",
      modelId: "gpt-4o",
      endpoint: "https://api.openai.com/v1/chat/completions",
      secret: "fake-test-secret",
      fetchImpl,
    });

    await expect(adapter.execute({
      traceId: "trace-2",
      providerId: "alibaba",
      modelId: "gpt-4o",
      prompt: "question",
    })).rejects.toThrow("identity mismatch");
    expect(fetchImpl).not.toHaveBeenCalled();
  });

  it("keeps credential resolution inside the Model Gateway factory", async () => {
    const fetchImpl = successFetch("credential-bound answer");
    const boundary = new CredentialBoundary({ LPCI_LLM_API_KEY: "fake-contained-secret" });
    const adapter = createCredentialBoundOpenAiCompatibleExecuteAdapter({
      credential: boundary,
      credentialReference: reference,
      providerId: "openai",
      modelId: "gpt-4o",
      endpoint: "https://api.openai.com/v1/chat/completions",
      fetchImpl,
    });

    const result = await adapter.execute({
      traceId: "trace-3",
      providerId: "openai",
      modelId: "gpt-4o",
      prompt: "question",
    });
    expect(result.text).toBe("credential-bound answer");
    expect(JSON.stringify(result)).not.toContain("fake-contained-secret");
  });

  it("fails missing credential before adapter or fetch execution", () => {
    const fetchImpl = successFetch();
    expect(() => createCredentialBoundOpenAiCompatibleExecuteAdapter({
      credential: new CredentialBoundary({}),
      credentialReference: reference,
      providerId: "openai",
      modelId: "gpt-4o",
      endpoint: "https://api.openai.com/v1/chat/completions",
      fetchImpl,
    })).toThrow("Credential unavailable");
    expect(fetchImpl).not.toHaveBeenCalled();
  });

  it("shields provider response details on an injected failure", async () => {
    const fetchImpl = vi.fn(async () => ({
      ok: false,
      status: 401,
      json: async () => ({}),
      text: async () => "sensitive provider diagnostic",
    })) as unknown as OpenAiCompatibleFetch;
    const adapter = createOpenAiCompatibleExecuteAdapter({
      providerId: "openai",
      modelId: "gpt-4o",
      endpoint: "https://api.openai.com/v1/chat/completions",
      secret: "fake-test-secret",
      fetchImpl,
    });

    await expect(adapter.execute({
      traceId: "trace-4",
      providerId: "openai",
      modelId: "gpt-4o",
      prompt: "question",
    })).rejects.toThrow("OpenAI-compatible provider request failed");
  });

  // EAFR-R8 adapter boundary residual (BOUNDED_WITH_NAMED_RESIDUAL, disposition
  // recorded in the R8 worker return). This adapter calls its injected
  // `fetchImpl` directly rather than `globalThis.fetch`, so the cvf-web
  // provider-execution-guard installed in the shared test setup -- which wraps
  // `globalThis.fetch` -- cannot observe or deny calls made through it. That
  // guard's destination-classification logic (`classifyDestination`,
  // `PROVIDER_HOSTS`) lives only in `cvf-web/src/test/`, a downstream consumer
  // of this package, not the reverse; importing it here would invert the
  // package dependency direction and is exactly the "second permit list" the
  // R8 work order forbids. No shared, gateway-owned classification source
  // currently exists for this package to import instead. This test documents
  // the bypass as a fact about current behavior, not an approval of it: any
  // permissive fetchImpl, regardless of the endpoint it targets, is honoured.
  it("[EAFR-R8-RESIDUAL] an injected fetchImpl bypasses guard-based destination classification entirely", async () => {
    const unrecognisedEndpoint = "https://not-a-recognised-provider.example.invalid/v1/chat/completions";
    const fetchImpl = successFetch("bypassed the guard");
    const adapter = createOpenAiCompatibleExecuteAdapter({
      providerId: "openai",
      modelId: "gpt-4o",
      endpoint: unrecognisedEndpoint,
      secret: "fake-test-secret",
      fetchImpl,
    });

    const result = await adapter.execute({
      traceId: "trace-r8-residual",
      providerId: "openai",
      modelId: "gpt-4o",
      prompt: "question",
    });

    // The adapter has no opinion about the endpoint's trustworthiness; it
    // forwards whatever fetchImpl the caller supplies to whatever endpoint the
    // caller supplies. This is the residual: closing it requires either a
    // shared, gateway-owned destination policy this adapter can consult, or an
    // architectural change so the guard can observe adapter-level fetch calls.
    expect(fetchImpl).toHaveBeenCalledWith(
      unrecognisedEndpoint,
      expect.anything(),
    );
    expect(result.text).toBe("bypassed the guard");
  });
});
