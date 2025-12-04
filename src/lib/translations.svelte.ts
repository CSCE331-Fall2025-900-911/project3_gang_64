import { getLocale } from '$lib/i18n/runtime';

let translations = $state<Record<string, Record<string, string>>>({});

export function setTranslations(value: Record<string, Record<string, string>>) {
  translations = value;
}

/**
 * Translate a UUID-keyed string using the translations loaded from data.
 * Call setTranslations(data.translations) in your root +layout.svelte first.
 *
 * @param uuid - The UUID key for the translation
 * @param fallback - Optional fallback text if translation not found
 * @returns The translated string in the current locale
 */
export function td(uuid: string, fallback?: string): string {
  const locale = getLocale();
  return translations[uuid]?.[locale] ?? fallback ?? uuid;
}
