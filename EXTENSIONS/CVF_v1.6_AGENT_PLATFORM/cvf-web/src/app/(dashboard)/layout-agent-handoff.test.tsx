/**
 * @vitest-environment jsdom
 */
// Receiving-side lifecycle of the cvf:openAgent handoff, composed from the actual
// DashboardLayout, AgentChatWithHistory and persisted useChatHistory (synthetic
// localStorage only). Two disclosed leaf modes:
//  - recorder: a transparent AgentChat stand-in that mirrors the hook's once-per-prompt
//    guard and message callback, so session binding is isolated from the send path;
//  - real: the actual AgentChat/useAgentChat with an in-process provider-adapter stub.
// The stub returns fixture text only. This proves client wiring, not AI governance,
// full-mode behaviour, real provider/HTTP/backend cancellation or browser behaviour.
import { StrictMode, useEffect, useRef, useState } from 'react';
import { act, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import DashboardLayout from './layout';
import type { ChatMessage } from '@/lib/agent-chat';
import type { AgentChatProps } from '@/components/AgentChat';

const { probe, chatMode, providerChat, nav, modalsStub, SETTINGS } = vi.hoisted(() => ({
    probe: { delivered: [] as string[], mounts: [] as Array<{ prompt?: string; existing: string[] }>, unmounts: 0 },
    chatMode: { real: false },
    providerChat: vi.fn(),
    nav: { open: null as string | null },
    modalsStub: {
        showUserContext: false, showSettings: false, showAIUsage: false, showApiKeyWizard: false,
        showOnboarding: false, showQuickStart: false, closeAllModals: vi.fn(), openModal: vi.fn(),
        closeModal: vi.fn(), handleOnboardingComplete: vi.fn(),
    },
    SETTINGS: {
        preferences: { defaultProvider: 'alibaba' },
        providers: { alibaba: { apiKey: 'synthetic-key', selectedModel: 'qwen-plus' } },
    },
}));

vi.mock('next/navigation', () => ({
    usePathname: () => '/home',
    useRouter: () => ({ push: vi.fn(), replace: vi.fn() }),
    useSearchParams: () => ({ get: (key: string) => (key === 'open' ? nav.open : null), toString: () => '' }),
}));
vi.mock('@/lib/hooks/useAuth', () => ({
    useAuth: () => ({ userRole: 'admin', userName: 'Fixture', permissions: {}, handleLogout: vi.fn(), impersonation: null, endImpersonation: vi.fn() }),
}));
vi.mock('@/lib/hooks/useModals', () => ({ useModals: () => modalsStub }));
vi.mock('@/lib/store', () => ({ useExecutionStore: () => ({ executions: [] }) }));
vi.mock('@/components/Settings', () => ({
    useSettings: () => ({ settings: SETTINGS, updateProvider: vi.fn(), updatePreferences: vi.fn() }),
}));
vi.mock('@/lib/i18n', () => ({ useLanguage: () => ({ language: 'en', t: (key: string) => key }) }));
vi.mock('@/lib/governed-starter-path', () => ({ buildGovernedStarterHandoff: vi.fn(), saveGovernedStarterHandoff: vi.fn() }));
vi.mock('@/components/CompactHeader', () => ({ default: () => null }));
vi.mock('@/components', async () => ({
    AgentChatWithHistory: (await import('@/components/AgentChatWithHistory')).AgentChatWithHistory,
    Sidebar: () => null, OnboardingWizard: () => null, QuickStart: () => null, UserContextForm: () => null,
    SettingsPage: () => null, AIUsagePanel: () => null, ApiKeyWizard: () => null, MultiAgentPanel: () => null, ToolsPage: () => null,
}));
vi.mock('@/lib/ai-providers', () => ({ createAIProvider: () => ({ chat: providerChat }) }));
vi.mock('@/lib/hooks/useModelPricing', () => ({ useModelPricing: () => ({ pricing: {}, status: 'ready', updatedAt: null }) }));
vi.mock('@/lib/quota-manager', async () => ({
    ...await vi.importActual<typeof import('@/lib/quota-manager')>('@/lib/quota-manager'),
    useQuotaManager: () => ({
        trackUsage: vi.fn(),
        checkBudget: () => ({ ok: true, warning: false, remaining: { daily: Infinity, monthly: Infinity } }),
    }),
}));
vi.mock('@/components/AgentChat', async importOriginal => {
    const actual = await importOriginal<typeof import('@/components/AgentChat')>();
    function Recorder({ initialPrompt, existingMessages, onMessagesChange, onMinimize, onClose }: AgentChatProps) {
        const [messages, setMessages] = useState<ChatMessage[]>(existingMessages ?? []);
        const [draft, setDraft] = useState('');
        const handled = useRef<string | null>(null);
        useEffect(() => {
            probe.mounts.push({ prompt: initialPrompt, existing: (existingMessages ?? []).map(m => m.content) });
            return () => { probe.unmounts += 1; };
            // eslint-disable-next-line react-hooks/exhaustive-deps
        }, []);
        useEffect(() => {
            if (initialPrompt && handled.current !== initialPrompt) {
                handled.current = initialPrompt;
                probe.delivered.push(initialPrompt);
                setMessages(prev => [...prev, { id: `rec-${probe.delivered.length}`, role: 'user', content: initialPrompt, timestamp: new Date() }]);
            }
        }, [initialPrompt]);
        useEffect(() => { if (messages.length > 0) onMessagesChange?.(messages); }, [messages, onMessagesChange]);
        return (
            <div data-testid="chat-recorder">
                <input aria-label="draft" value={draft} onChange={event => setDraft(event.target.value)} />
                <button onClick={onMinimize}>Recorder minimize</button>
                <button onClick={onClose}>Recorder close</button>
            </div>
        );
    }
    return { ...actual, AgentChat: (props: AgentChatProps) => (chatMode.real ? <actual.AgentChat {...props} /> : <Recorder {...props} />) };
});

type SessionView = { id: string; texts: string[] };
const A = 'PROMPT_A';
const B = 'PROMPT_B';

function seedHistory() {
    const when = '2026-01-01T00:00:00.000Z';
    localStorage.setItem('cvf_chat_history', JSON.stringify({
        sessions: [{
            id: 'saved-S0', title: 'Saved unrelated', provider: 'alibaba', createdAt: when, updatedAt: when,
            metadata: { messageCount: 2 },
            messages: [
                { id: 'saved-1', role: 'user', content: 'SAVED_QUESTION', timestamp: when },
                { id: 'saved-2', role: 'assistant', content: 'SAVED_ANSWER', timestamp: when },
            ],
        }],
        activeSessionId: 'saved-S0',
    }));
}
function history() {
    const raw = JSON.parse(localStorage.getItem('cvf_chat_history')!) as {
        activeSessionId: string | null; sessions: Array<{ id: string; messages: Array<{ content: string }> }>;
    };
    const sessions: SessionView[] = raw.sessions.map(s => ({ id: s.id, texts: s.messages.map(m => m.content) }));
    return { active: raw.activeSessionId, sessions };
}
type Snapshot = ReturnType<typeof history>;
const byId = (snapshot: Snapshot, id: string | null) => snapshot.sessions.find(s => s.id === id)!;
const handoff = (prompt?: string) => act(() => {
    window.dispatchEvent(new CustomEvent('cvf:openAgent', { detail: prompt === undefined ? {} : { prompt } }));
});
const press = (name: string) => fireEvent.click(screen.getByRole('button', { name }));
const restore = () => fireEvent.click(screen.getByText('agent.restoreHint'));
const mountShell = (strict = false) => {
    const shell = <DashboardLayout><div>Home witness</div></DashboardLayout>;
    return render(strict ? <StrictMode>{shell}</StrictMode> : shell);
};
const advance = (ms: number) => act(async () => { await vi.advanceTimersByTimeAsync(ms); });
const lastUserSent = (call: number) => {
    const sent = providerChat.mock.calls[call][0] as Array<{ role: string; content: string }>;
    return sent[sent.length - 1].content;
};

beforeEach(() => {
    localStorage.clear();
    document.body.style.overflow = '';
    probe.delivered.length = 0; probe.mounts.length = 0; probe.unmounts = 0;
    chatMode.real = false; nav.open = null;
    providerChat.mockReset();
    providerChat.mockImplementation(async (messages: Array<{ content: string }>) => ({
        text: `STUB_REPLY(${messages[messages.length - 1].content})`, usage: { totalTokens: 3 },
    }));
});
afterEach(() => { vi.useRealTimers(); document.body.style.overflow = ''; });

describe('incoming handoff session binding (recorder leaf)', () => {
    it('delivers the first handoff once to its own ready session, apart from saved history', () => {
        seedHistory();
        mountShell();
        handoff(A);
        expect(probe.delivered).toEqual([A]);
        expect(probe.mounts).toEqual([{ prompt: A, existing: [] }]);
        const h = history();
        expect(h.sessions).toHaveLength(2);
        expect(byId(h, 'saved-S0').texts).toEqual(['SAVED_QUESTION', 'SAVED_ANSWER']);
        expect(h.active).not.toBe('saved-S0');
        expect(byId(h, h.active).texts).toEqual([A]);
    });

    it('keeps session, draft and delivery count across minimize, restore and unrelated rerenders', () => {
        const view = mountShell();
        handoff(A);
        const before = history();
        fireEvent.change(screen.getByLabelText('draft'), { target: { value: 'half-typed' } });
        press('Recorder minimize');
        expect(screen.getByTestId('chat-recorder').closest('[hidden]')).not.toBeNull();
        expect(document.body.style.overflow).toBe('hidden');
        view.rerender(<DashboardLayout><div>Other child</div></DashboardLayout>);
        restore();
        expect(screen.getByTestId('chat-recorder').closest('[hidden]')).toBeNull();
        expect((screen.getByLabelText('draft') as HTMLInputElement).value).toBe('half-typed');
        expect(probe.delivered).toEqual([A]);
        expect(probe.mounts).toHaveLength(1);
        expect(history()).toEqual(before);
    });

    it('does not replay or add a session under StrictMode minimize/restore', () => {
        mountShell(true);
        handoff(A);
        const before = history();
        expect(before.sessions).toHaveLength(1);
        press('Recorder minimize');
        restore();
        expect(probe.delivered).toEqual([A]);
        expect(history()).toEqual(before);
    });

    it('receives a new explicit handoff B in a fresh session while chat A is open', () => {
        seedHistory();
        mountShell();
        handoff(A);
        const aId = history().active;
        handoff(B);
        expect(probe.delivered).toEqual([A, B]);
        expect(probe.mounts[1]).toEqual({ prompt: B, existing: [] });
        const h = history();
        expect(h.sessions).toHaveLength(3);
        expect(h.active).not.toBe(aId);
        expect(byId(h, aId).texts).toEqual([A]);
        expect(byId(h, h.active).texts).toEqual([B]);
        expect(byId(h, 'saved-S0').texts).toEqual(['SAVED_QUESTION', 'SAVED_ANSWER']);
    });

    it('receives B when an ordinary empty chat is already open', () => {
        nav.open = 'agent';
        mountShell();
        expect(probe.mounts).toEqual([{ prompt: undefined, existing: [] }]);
        const ordinary = history();
        expect(ordinary.sessions).toHaveLength(1);
        expect(byId(ordinary, ordinary.active).texts).toEqual([]);
        handoff(B);
        expect(probe.delivered).toEqual([B]);
        const h = history();
        expect(h.sessions).toHaveLength(2);
        expect(byId(h, ordinary.active).texts).toEqual([]);
        expect(h.active).not.toBe(ordinary.active);
        expect(byId(h, h.active).texts).toEqual([B]);
    });

    it('treats two deliberate identical-text handoffs as two sessions, and restore as neither', () => {
        seedHistory();
        mountShell();
        handoff('SAME');
        handoff('SAME');
        expect(probe.delivered).toEqual(['SAME', 'SAME']);
        const h = history();
        const copies = h.sessions.filter(s => s.texts.join() === 'SAME');
        expect(copies).toHaveLength(2);
        expect(new Set(copies.map(s => s.id)).size).toBe(2);
        press('Recorder minimize');
        restore();
        expect(probe.delivered).toEqual(['SAME', 'SAME']);
        expect(history()).toEqual(h);
    });

    it('close clears the incoming prompt and body lock; ordinary reopen does not replay it', () => {
        mountShell();
        handoff(A);
        press('Recorder close');
        expect(screen.queryByTestId('chat-recorder')).toBeNull();
        expect(document.body.style.overflow).toBe('');
        const closed = history();
        expect(byId(closed, closed.active).texts).toEqual([A]);
        handoff();
        expect(probe.mounts[probe.mounts.length - 1].prompt).toBeUndefined();
        expect(probe.delivered).toEqual([A]);
        expect(history().sessions).toHaveLength(1);
    });
});

describe('real AgentChat and useAgentChat receiving seam (in-process provider stub)', () => {
    beforeEach(() => { chatMode.real = true; vi.useFakeTimers(); });

    it('delivers A once and keeps the session through minimize/restore after delivery', async () => {
        mountShell();
        handoff(A);
        await advance(600);
        expect(providerChat).toHaveBeenCalledTimes(1);
        expect(lastUserSent(0)).toBe(A);
        const before = history();
        const session = byId(before, before.active);
        expect(session.texts[0]).toContain('CVF Agent Mode started');
        expect(session.texts.slice(1)).toEqual([A, `STUB_REPLY(${A})`]);
        press('Minimize');
        restore();
        await advance(1500);
        expect(providerChat).toHaveBeenCalledTimes(1);
        expect(history()).toEqual(before);
    });

    it('sends exactly once when minimized before the deferred timer and restored after it', async () => {
        mountShell();
        handoff(A);
        press('Minimize');
        await advance(600);
        restore();
        await advance(1500);
        expect(providerChat).toHaveBeenCalledTimes(1);
        const h = history();
        expect(h.sessions).toHaveLength(1);
        expect(byId(h, h.active).texts.slice(1)).toEqual([A, `STUB_REPLY(${A})`]);
    });

    it('does not dispatch the queued prompt when closed before the timer fires', async () => {
        mountShell();
        handoff(A);
        await advance(200);
        press('Close chat');
        await advance(1500);
        expect(providerChat).not.toHaveBeenCalled();
        expect(document.body.style.overflow).toBe('');
        expect(history().sessions.every(s => !s.texts.includes(A))).toBe(true);
    });

    it('replaces A with B before the timer: only B is sent, in its own session', async () => {
        mountShell();
        handoff(A);
        await advance(200);
        const aId = history().active;
        handoff(B);
        await advance(1500);
        expect(providerChat).toHaveBeenCalledTimes(1);
        expect(lastUserSent(0)).toBe(B);
        const h = history();
        expect(h.active).not.toBe(aId);
        expect(byId(h, aId).texts).toEqual([]);
        expect(byId(h, h.active).texts.slice(1)).toEqual([B, `STUB_REPLY(${B})`]);
    });

    it('sends one user message under StrictMode with rerender and minimize/restore', async () => {
        const view = mountShell(true);
        handoff(A);
        await advance(600);
        press('Minimize');
        view.rerender(<StrictMode><DashboardLayout><div>Other child</div></DashboardLayout></StrictMode>);
        restore();
        await advance(1500);
        expect(providerChat).toHaveBeenCalledTimes(1);
        const h = history();
        expect(h.sessions).toHaveLength(1);
        expect(byId(h, h.active).texts.filter(t => t === A)).toHaveLength(1);
    });
});
