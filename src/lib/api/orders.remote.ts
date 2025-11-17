import { command, query } from '$app/server';
import { customer, ingredient, order, orderContent } from '$lib/db/schema';
import { orderInsertSchema, orderSelectSchema, type NewOrder } from '$lib/db/types';
import { OrderEntrySchema } from '$lib/managers/order_manager.types';
import { desc, eq, sql } from 'drizzle-orm';
import moment from 'moment';
import { v4 as uuidv4 } from 'uuid';
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

export const createOrder = command(orderInsertSchema, async (newOrder: NewOrder) => {
  const db = getDB();

  const created = await db.insert(order).values(newOrder).returning();
  return created[0];
});

export const deleteOrder = command(orderSelectSchema.entries.id, async (id) => {
  const db = getDB();
  await db.delete(order).where(eq(order.id, id));
});

const submitOrderSchema = v.object({
  customerId: v.string(),
  paymentMethod: v.picklist(['cash', 'credit'] as const),
  order: v.array(OrderEntrySchema),
  employeeId: v.string(),
});

export const submitOrder = command(
  submitOrderSchema,
  async ({ customerId, paymentMethod, order: submittedOrder, employeeId }) => {
    const db = getDB();

    const subtotal = submittedOrder.reduce((sum, entry) => sum + entry.menuItem.price, 0);
    const tax = subtotal * 0.07;
    const total = subtotal + tax;

    const newOrder: NewOrder = {
      customerId,
      subtotal,
      tax,
      total,
      paymentMethod,
      employeeId,
      date: moment().toISOString(),
      itemQuantity: submittedOrder.length,
    };

    const createdOrder = await db.insert(order).values(newOrder).returning();

    // Add order content entries
    for (const entry of submittedOrder) {
      const entryId = uuidv4();

      for (const entryIngredient of entry.ingredients) {
        await db.insert(orderContent).values({
          orderId: createdOrder[0].id,
          menuItemId: entry.menuItem.id,
          ingredientId: entryIngredient.id,
          orderEntryId: entryId,
        });

        // get current ingredient stock and decrement by 1
        const currentIngredient = await db
          .select()
          .from(ingredient)
          .where(eq(ingredient.id, entryIngredient.id))
          .limit(1);

        if (currentIngredient.length === 0) {
          throw new Error(`Ingredient with ID ${entryIngredient.id} not found`);
        }

        // decrement the ingredient quantity
        await db
          .update(ingredient)
          .set({ currentStock: currentIngredient[0].currentStock - 1 })
          .where(eq(ingredient.id, entryIngredient.id));
      }
    }

    return createdOrder[0];
  },
);
