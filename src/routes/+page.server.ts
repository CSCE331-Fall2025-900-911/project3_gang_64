import { redirect } from '@sveltejs/kit';
import { localizeHref } from '$lib/i18n/runtime';

export function load() {
  throw redirect(302, localizeHref('/auth/directory'));
}
