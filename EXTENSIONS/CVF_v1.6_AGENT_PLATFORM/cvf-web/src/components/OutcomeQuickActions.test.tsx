import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { OutcomeQuickActions } from './OutcomeQuickActions';

describe('OutcomeQuickActions', () => {
    it('renders the three English outcome buttons', () => {
        render(<OutcomeQuickActions lang="en" onSelectTemplate={vi.fn()} />);

        expect(screen.getByRole('button', { name: 'Create Product Brief' })).toBeTruthy();
        expect(screen.getByRole('button', { name: 'Generate SOP' })).toBeTruthy();
        expect(screen.getByRole('button', { name: 'Analyze Strategy' })).toBeTruthy();
    });

    it('renders Vietnamese labels', () => {
        render(<OutcomeQuickActions lang="vi" onSelectTemplate={vi.fn()} />);

        expect(screen.getByRole('button', { name: 'Tạo Product Brief' })).toBeTruthy();
        expect(screen.getByRole('button', { name: 'Tạo SOP' })).toBeTruthy();
        expect(screen.getByRole('button', { name: 'Phân tích chiến lược' })).toBeTruthy();
    });

    it('selects the matching template id for each action', () => {
        const onSelectTemplate = vi.fn();
        render(<OutcomeQuickActions lang="en" onSelectTemplate={onSelectTemplate} />);

        fireEvent.click(screen.getByRole('button', { name: 'Create Product Brief' }));
        fireEvent.click(screen.getByRole('button', { name: 'Generate SOP' }));
        fireEvent.click(screen.getByRole('button', { name: 'Analyze Strategy' }));

        expect(onSelectTemplate).toHaveBeenNthCalledWith(1, 'app_builder_complete');
        expect(onSelectTemplate).toHaveBeenNthCalledWith(2, 'documentation');
        expect(onSelectTemplate).toHaveBeenNthCalledWith(3, 'strategy_analysis');
    });
});
