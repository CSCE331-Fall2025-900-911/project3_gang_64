import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/sveltekit/providers/google';
import { DrizzleAdapter } from '@auth/drizzle-adapter';
import { GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET } from '$env/static/private';
import { getDB } from '../db';

export const { handle, signIn, signOut } = SvelteKitAuth({
  adapter: DrizzleAdapter(getDB()),
  providers: [Google({ clientId: GOOGLE_CLIENT_ID, clientSecret: GOOGLE_CLIENT_SECRET })],
});
