import { localizeHref } from '$lib/i18n/runtime';
import { redirect } from '@sveltejs/kit';

export function load() {
  throw redirect(302, localizeHref('/kiosk/home'));
}
