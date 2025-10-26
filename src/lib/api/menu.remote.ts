import { query } from '$app/server';
import { getDB } from '$lib/db';
import { menu } from '$lib/db/schema';
import { eq } from 'drizzle-orm';
import * as v from 'valibot';

export const getMenu = query(async () => {
  const db = getDB();

  return await db.select().from(menu);
});

export const getMenuCategory = query(v.string(), async (category: string) => {
  const db = getDB();

  return await db.select().from(menu).where(eq(menu.category, category));
});

export const getMenuCategories = query(async () => {
  const db = getDB();

  return (await db.selectDistinctOn([menu.category], { category: menu.category }).from(menu)).map(
    (row) => row.category,
  );
});
