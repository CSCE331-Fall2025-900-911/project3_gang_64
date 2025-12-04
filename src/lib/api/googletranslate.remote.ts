import { query } from '$app/server';
import { env } from '$env/dynamic/private';
import * as v from 'valibot';

const BASE_URL = 'https://translation.googleapis.com/language/translate/v2';

const translateToLocalesParams = v.object({
  text: v.string(),
  locales: v.array(v.string()),
  sourceLocale: v.optional(v.string()),
});

export const translateToLocales = query(translateToLocalesParams, async ({ text, locales, sourceLocale }) => {
  const url = `${BASE_URL}?key=${env.INLANG_GOOGLE_TRANSLATE_API_KEY}`;

  const translations: Record<string, string> = {};

  if (sourceLocale) {
    translations[sourceLocale] = text;
  }

  for (const locale of locales) {
    const payload = {
      q: [text],
      target: locale,
      ...(sourceLocale && { source: sourceLocale }),
      format: 'text',
    };

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(
        `Google Translate API failed for locale ${locale}: ${response.status} - ${response.statusText}. Response: ${errorText}`,
      );
    }

    const result = await response.json();
    translations[locale] = result.data.translations[0].translatedText;
  }

  return translations;
});
