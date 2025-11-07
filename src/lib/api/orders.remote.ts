import { command, query } from '$app/server';
import { customer, order } from '$lib/db/schema';
import { orderInsertSchema, orderSelectSchema, type NewOrder } from '$lib/db/types';
import { desc, eq, sql, gt } from 'drizzle-orm';
import * as v from 'valibot';
import { getDB } from '../db';

const getOrdersSchema = v.object({
  page: v.optional(v.number(), 1),
  limit: v.optional(v.number(), 50),
});

export const getOrders = query(getOrdersSchema, async ({ page, limit }) => {
  const db = getDB();

  return await db
    .select({
      id: order.id,
      total: order.total,
      date: order.date,
      customer: customer.name,
      paymethod: order.paymentMethod,
    })
    .from(order)
    .innerJoin(customer, eq(order.customerId, customer.id))
    .orderBy(desc(order.date))
    .limit(limit)
    .offset(page * limit);
});

export const getOrderCount = query(async () => {
  const db = getDB();

  return await db
    .select({
      count: sql<number>`COUNT(${order.id})`,
    })
    .from(order)
    .then((res) => res[0].count);
});

export const getOrderCountDay = query(async () => {
  const db = getDB();
  const day = new Date();

  return await db
    .select({
      count: sql<number>`COUNT(${order.id})`,
    })
    .from(order).where(gt(order.date, day.toISOString()))
    .then((res) => res[0].count);
});

export const createOrder = command(orderInsertSchema, async (newOrder: NewOrder) => {
  const db = getDB();

  const created = await db.insert(order).values(newOrder).returning();
  return created[0];
});

export const deleteOrder = command(orderSelectSchema.entries.id, async (id) => {
  const db = getDB();
  await db.delete(order).where(eq(order.id, id));
});
