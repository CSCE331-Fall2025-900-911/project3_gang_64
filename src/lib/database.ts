import { env } from '$env/dynamic/private';
import type { EmployeeTable } from '$lib/types';
import { Kysely, PostgresDialect } from 'kysely';
import { Pool } from 'pg';

const dialect = new PostgresDialect({
	pool: new Pool({
		database: env.DBNAME,
		host: env.PGHOST,
		user: env.PGUSER,
		password: env.PGPASSWORD,
		port: 5432,
		max: 10,
	}),
});

export interface Database {
	employee: EmployeeTable;
}

export const db = new Kysely<Database>({
	dialect,
});
