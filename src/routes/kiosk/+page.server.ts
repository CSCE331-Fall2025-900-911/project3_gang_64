import { redirect } from '@sveltejs/kit';
import { orderManager } from '$lib/managers/order_manager.svelte';
import {goto} from '$app/navigation';

export function load() {
  throw redirect(302, '/kiosk/home');
}
