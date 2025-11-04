import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/sveltekit/providers/google';
import { DrizzleAdapter } from '@auth/drizzle-adapter';
import { getDB } from '../db';

export const { handle, signIn, signOut } = SvelteKitAuth({
  adapter: DrizzleAdapter(getDB()),
  providers: [Google],
});
