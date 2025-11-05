import { GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET } from '$env/static/private';
import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/sveltekit/providers/google';
import { and, eq } from 'drizzle-orm';
import { getDB } from '../db';

import * as schema from '../db/schema';

export const { handle, signIn, signOut } = SvelteKitAuth({
  providers: [Google({ clientId: GOOGLE_CLIENT_ID, clientSecret: GOOGLE_CLIENT_SECRET })],
  session: {
    strategy: 'jwt',
  },
  callbacks: {
    async signIn({ profile }) {
      const email = profile?.email;

      if (!email) return false;

      const db = getDB();
      const employeeRecord = await db
        .select({ email: schema.employee.email, archived: schema.employee.archived })
        .from(schema.employee)
        .where(and(eq(schema.employee.email, email), eq(schema.employee.archived, false)))
        .limit(1);

      return employeeRecord.length > 0;
    },
    async jwt({ token, trigger }) {
      // Add employee data to the token on sign in or update
      if (trigger === 'signIn' || trigger === 'update') {
        const db = getDB();
        const employeeRecord = await db
          .select()
          .from(schema.employee)
          .where(eq(schema.employee.email, token.email!))
          .limit(1);

        if (employeeRecord[0]) {
          token.employee = employeeRecord[0];
        }
      }
      return token;
    },
    async session({ session, token }) {
      // Add employee data to the session
      if (token.employee) {
        session.employee = token.employee as typeof session.employee;
      }
      return session;
    },
  },
  pages: {
    signIn: '/auth/login',
    signOut: '/auth/logout',
    error: '/auth/unauthorized',
  },
});
