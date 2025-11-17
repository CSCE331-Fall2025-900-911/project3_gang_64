import { type Handle } from '@sveltejs/kit';
import { sequence } from '@sveltejs/kit/hooks';
import { handle as authenticationHandle } from './lib/auth/auth';
import { paraglideMiddleware } from '$lib/i18n/server';

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

export const handle: Handle = sequence(authenticationHandle, paraglideHandle, employeePopulation);
