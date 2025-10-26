import { env } from '$env/dynamic/private';
import { drizzle } from 'drizzle-orm/node-postgres';

export function getDB() {
  return drizzle(`postgresql://${env.PGUSER}:${env.PGPASSWORD}@${env.PGHOST}:5432/${env.DBNAME}`);
}
