import { command, query } from '$app/server';
import { customer } from '$lib/db/schema';
import { customerInsertSchema, customerSelectSchema, type NewCustomer } from '$lib/db/types';
import { eq, like, or, sql } from 'drizzle-orm';
import * as v from 'valibot';
import { getDB } from '../db';

const getCustomerSchema = v.object({
  page: v.optional(v.number(), 1),
  limit: v.optional(v.number(), 50),
  search: v.optional(v.string()),
});

export const getCustomers = query(getCustomerSchema, async ({ page, limit, search }) => {
  const db = getDB();

  return await db
    .select()
    .from(customer)
    .where(search ? or(like(customer.name, `%${search}%`), like(customer.email, `%${search}%`)) : undefined)
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

export const createOrSelectCustomer = command(customerInsertSchema, async (newCustomer: NewCustomer) => {
  const db = getDB();

  // Check if customer already exists
  const existingCustomers = await db.select().from(customer).where(eq(customer.email, newCustomer.email!));

  if (existingCustomers.length > 0) {
    return existingCustomers[0];
  }

  // If not, create a new customer
  return await createCustomer(newCustomer);
});

export const deleteCustomer = command(customerSelectSchema.entries.id, async (id) => {
  const db = getDB();
  await db.delete(customer).where(eq(customer.id, id));
});
