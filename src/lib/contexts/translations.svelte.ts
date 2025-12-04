import { getLocale } from '$lib/i18n/runtime';
import { createTranslation, updateTranslation, findTranslationByText } from '$lib/api/translate.remote';

let translations = $state<Record<string, Record<string, string>>>({});

export function setTranslations(value: Record<string, Record<string, string>>) {
  translations = value;
}

export function addTranslation(id: string, translation: { en: string; es: string; de: string; fr: string }) {
  translations[id] = translation;
}

export function td(uuid: string): string {
  const locale = getLocale();
  return translations[uuid]?.[locale] ?? uuid;
}

export function createLocaleOnlyTranslation(text: string): { en: string; es: string; de: string; fr: string } {
  const locale = getLocale() as 'en' | 'es' | 'de' | 'fr';
  return {
    en: locale === 'en' ? text : '',
    es: locale === 'es' ? text : '',
    de: locale === 'de' ? text : '',
    fr: locale === 'fr' ? text : '',
  };
}

export async function generateNewTranslation(text: string): Promise<string> {
  const existingTranslationId = await checkForExistingTranslation(text);
  if (existingTranslationId) {
    return existingTranslationId;
  }

  const translation = createLocaleOnlyTranslation(text);
  const translationId = (await createTranslation(translation)).id;
  addTranslation(translationId, translation);
  return translationId;
}

export async function updateExistingTranslation(id: string | undefined, text: string): Promise<string> {
  if (!id) {
    return generateNewTranslation(text);
  }

  const existingTranslationId = await checkForExistingTranslation(text);
  if (existingTranslationId) {
    return existingTranslationId;
  }

  const translation = createLocaleOnlyTranslation(text);
  await updateTranslation({ id, ...translation });
  addTranslation(id, translation);
  return id;
}

export async function checkForExistingTranslation(text: string): Promise<string | null> {
  const locale = getLocale() as 'en' | 'es' | 'de' | 'fr';
  if (await findTranslationByText({ text, locale })) {
    const existingId = await findTranslationByText({ text, locale });
    return existingId;
  }
  return null;
}
