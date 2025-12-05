import { query } from '$app/server';
import { ingredient, order, orderContent } from '$lib/db/schema';
import { luxonDatetime } from '$lib/utils/utils';
import { eq, gt, sql } from 'drizzle-orm';
import { getDB } from '../db';

export const getDayOrderCount = query(luxonDatetime, async (day) => {
  const db = getDB();

  return await db
    .select({
      count: sql<number>`COUNT(${order.id})`,
    })
    .from(order)
    .where(gt(order.date, day))
    .then((res) => res[0].count);
});

export const getDayRevenue = query(luxonDatetime, async (day) => {
  const db = getDB();

  return await db
    .select({
      total: sql<number>`SUM(${order.total})`,
    })
    .from(order)
    .where(gt(order.date, day))
    .then((res) => res[0].total ?? 0);
});

export const getInventoryUsageForDay = query(luxonDatetime, async (day) => {
  const db = getDB();

  // Get all orders for the specified day
  const dayFilter = eq(sql<string>`DATE(${order.date})`, day);

  // Join order_content with orders and ingredients to get usage counts
  const usage = await db
    .select({
      ingredientId: orderContent.ingredientId,
      ingredientName: ingredient.name,
      ingredientCategory: ingredient.category,
      usageCount: sql<number>`COUNT(${orderContent.ingredientId})`,
    })
    .from(orderContent)
    .innerJoin(order, eq(orderContent.orderId, order.id))
    .innerJoin(ingredient, eq(orderContent.ingredientId, ingredient.id))
    .where(dayFilter)
    .groupBy(orderContent.ingredientId, ingredient.name, ingredient.category)
    .orderBy(sql`COUNT(${orderContent.ingredientId}) DESC`);

  return usage;
});
