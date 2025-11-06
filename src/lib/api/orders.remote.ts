import { command, query } from '$app/server';
import {page} from '$app/stores';
import { order, customer, paymethod } from '$lib/db/schema';
import { orderInsertSchema, orderSelectSchema, type OrderRow, type NewOrder } from '$lib/db/types';
import { eq, desc } from 'drizzle-orm';
import { getDB } from '../db';


// export const userState = $state({page:0});

export const getOrders = query<OrderRow[]>(async () => {
  
  // const pgOffset = userState.page;
  const db = getDB();
  const sql =  `SELECT   "order".id,
	                      "order".total,
	                      "order".date,
	                      customer.name,
	                      "order".payment_method
                FROM "order"
                JOIN customer on customer.id = "order".customer_id
                ORDER BY "order".date DESC;`
  return await db.select({
    id: order.id,
    total: order.total,
    date: order.date,
    customer: customer.name,
    paymethod: order.paymentMethod

  }).from(order).innerJoin(customer, eq(order.customerId, customer.id)).orderBy(desc(order.date)).limit(50).offset(50);
});

export const createOrder = command(orderInsertSchema, async (newOrder: NewOrder) => {
  const db = getDB();

  const created = await db.insert(order).values(newOrder).returning();
  getOrders().refresh();

  return created[0];
});

export const deleteEmployee = command(orderSelectSchema.entries.id, async (id) => {
  const db = getDB();
  await db.delete(order).where(eq(order.id, id));

  getOrders().refresh();
});
