import { command, query } from '$app/server';
import { customer } from '$lib/db/schema';
import { customerInsertSchema, customerSelectSchema, type NewCustomer } from '$lib/db/types';
import { eq, sql } from 'drizzle-orm';
import * as v from 'valibot';
import { getDB } from '../db';

const getCustomerSchema = v.object({
  page: v.optional(v.number(), 1),
  limit: v.optional(v.number(), 50),
});

export const getCustomers = query(getCustomerSchema, async ({ page, limit }) => {
  const db = getDB();

  return await db
    .select()
    .from(customer)
    .orderBy(customer.name)
    .limit(limit)
    .offset(page * limit);
});

export const getCustomerCount = query(async () => {
  const db = getDB();

  return await db
    .select({
      count: sql<number>`COUNT(${customer.id})`,
    })
    .from(customer)
    .then((res) => res[0].count);
});

export const createCustomer = command(customerInsertSchema, async (newCustomer: NewCustomer) => {
  const db = getDB();

  const created = await db.insert(customer).values(newCustomer).returning();
  return created[0];
});

export const deleteCustomer = command(customerSelectSchema.entries.id, async (id) => {
  const db = getDB();
  await db.delete(customer).where(eq(customer.id, id));
});
