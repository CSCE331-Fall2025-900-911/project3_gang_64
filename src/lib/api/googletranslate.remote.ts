import { query } from '$app/server';
import { env } from '$env/dynamic/private';
import * as v from 'valibot';
import { getLocale } from '$lib/i18n/runtime';

const BASE_URL = 'https://translation.googleapis.com/language/translate/v2';

const translateTextParams = v.object({
  segments: v.array(v.string()),
  target: v.string(),
});

export const translateText = query(translateTextParams, async ({ segments }) => {
  const url = `${BASE_URL}?key=${env.INLANG_GOOGLE_TRANSLATE_API_KEY}`;

  if (segments.length > 128) {
    throw new Error('Exceeded maximum number of segments (128).');
  }

  const payload = {
    q: segments,
    target: getLocale,
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
    throw new Error(`Google Translate API failed: ${response.status} - ${response.statusText}. Response: ${errorText}`);
  }

  return await response.json();
});
