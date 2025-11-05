import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/sveltekit/providers/google';
import { DrizzleAdapter } from '@auth/drizzle-adapter';
import { redirect } from '@sveltejs/kit';
import { GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET } from '$env/static/private';
import { getDB } from '../db';
import { eq } from 'drizzle-orm';

import * as schema from '../db/schema';

export const { handle, signIn, signOut } = SvelteKitAuth({
  adapter: DrizzleAdapter(getDB(), {
    usersTable: schema.users,
    accountsTable: schema.accounts,
    sessionsTable: schema.sessions,
    verificationTokensTable: schema.verificationTokens,
  }),
  providers: [Google({ clientId: GOOGLE_CLIENT_ID, clientSecret: GOOGLE_CLIENT_SECRET })],

  callbacks: {
    async signIn({ user, account, profile }) {
      // only provision google ouath account for emplioyees
      if (account?.provider === 'google' && profile?.email) {
        const email = profile.email;
        const db = getDB();
        const employeeRecord = await db
          .select({ email: schema.employee.email })
          .from(schema.employee)
          .where(eq(schema.employee.email, email))
          .limit(1);

        if (employeeRecord.length > 0) {
          console.log(`Employee provisioned: ${email}. Allowing sign-in.`);
          return true;
        }

        console.warn(`Employee NOT provisioned: ${email}. Blocking sign-in.`);
        return false;
      }

      return true;
    },
  },
  pages: {
    error: '/auth/unauthorized', // Redirect to this route on error
  },
});
