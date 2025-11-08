import moment from 'moment';
import * as v from 'valibot';

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

export const momentValidator = v.custom<moment.Moment>(
  (value): value is moment.Moment => moment.isMoment(value),
  'Must be a Moment object',
);
