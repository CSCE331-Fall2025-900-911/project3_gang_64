import { type Handle } from '@sveltejs/kit';
import { sequence } from '@sveltejs/kit/hooks';
import { handle as authenticationHandle } from './lib/auth/auth';
import { paraglideMiddleware } from '$lib/i18n/server';
import { getDB } from '$lib/db';
import { translation } from '$lib/db/schema';

// Cache translations at module level - loaded once on server startup
let translationsCache: Record<string, Record<string, string>> | null = null;

export function invalidateTranslationsCache() {
  translationsCache = null;
}

async function loadTranslations() {
  if (translationsCache) {
    return translationsCache;
  }

  const db = getDB();
  const translations = await db.select().from(translation);

  translationsCache = translations.reduce(
    (acc, t) => {
      acc[t.id] = {
        en: t.en,
        es: t.es,
        de: t.de,
        fr: t.fr,
      };
      return acc;
    },
    {} as Record<string, Record<string, string>>,
  );

  return translationsCache;
}

async function translationPopulation({ event, resolve }: Parameters<Handle>[0]) {
  event.locals.translations = await loadTranslations();
  return resolve(event);
}

async function employeePopulation({ event, resolve }: Parameters<Handle>[0]) {
  const session = await event.locals.auth();
  event.locals.employee = session?.employee ?? null;
  return resolve(event);
}

const paraglideHandle: Handle = ({ event, resolve }) =>
  paraglideMiddleware(event.request, ({ request: localizedRequest, locale }) => {
    event.request = localizedRequest;
    return resolve(event, {
      transformPageChunk: ({ html }) => {
        return html.replace('%lang%', locale);
      },
    });
  });

export const handle: Handle = sequence(
  authenticationHandle,
  paraglideHandle,
  translationPopulation,
  employeePopulation,
);
