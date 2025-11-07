import { command, query } from '$app/server';
import { getDB } from '$lib/db';
import { ingredient, menu, recipe } from '$lib/db/schema';
import { ingredientInsertSchema } from '$lib/db/types';
import { eq } from 'drizzle-orm';
import * as v from 'valibot';

export const getIngredients = query(async () => {
  const db = getDB();

  return await db.select().from(ingredient);
});

export const getIngredientsForMenuItem = query(v.string(), async (menuItemId: string) => {
  const db = getDB();

  const ingredients = await db
    .select()
    .from(menu)
    .where(eq(menu.id, menuItemId))
    .leftJoin(recipe, eq(menu.id, recipe.menuItemId))
    .leftJoin(ingredient, eq(recipe.ingredientId, ingredient.id));

  if (!ingredients) {
    throw new Error('Menu item not found');
  }

  return ingredients.map((row) => row.ingredient).filter((r) => r !== null);
});

export const createIngredient = command(ingredientInsertSchema, async (newIngredient) => {
  const db = getDB();
  const created = await db.insert(ingredient).values(newIngredient).returning();

  getIngredients().refresh();

  return created[0];
});
