import { getLocale } from '$lib/i18n/runtime';

let translations = $state<Record<string, Record<string, string>>>({});

export function setTranslations(value: Record<string, Record<string, string>>) {
  translations = value;
}

export function td(uuid: string): string {
  const locale = getLocale();
  return translations[uuid]?.[locale] ?? uuid;
}
