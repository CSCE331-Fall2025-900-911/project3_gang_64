import { m } from '$lib/i18n/messages';
import { DateTime } from 'luxon';
import { custom } from 'valibot';

export function titleCase(s: string) {
  return s
    .toLowerCase()
    .split(' ')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

export function groupedItems<T>(items: T[], key: (item: T) => string): Record<string, T[]> {
  return items.reduce(
    (acc, item) => {
      const groupKey = key(item);
      if (!acc[groupKey]) {
        acc[groupKey] = [];
      }
      acc[groupKey].push(item);
      return acc;
    },
    {} as Record<string, T[]>,
  );
}

export interface ModalProps {
  onClose: () => void;
}

export function t<K extends keyof typeof m>(key: K, input: Parameters<(typeof m)[K]>[0] = {}): string {
  // @ts-expect-error TypeScript can't infer the type here
  return m[key](input);
}

export const luxonDatetime = custom<DateTime>((input) => (input instanceof DateTime ? input.isValid : false));
