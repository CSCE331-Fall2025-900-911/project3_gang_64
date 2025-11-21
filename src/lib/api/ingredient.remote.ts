import { command, query } from '$app/server';
import { getDB } from '$lib/db';
import { ingredient, menu, recipe } from '$lib/db/schema';
import { ingredientInsertSchema, ingredientSelectSchema, ingredientUpdateSchema } from '$lib/db/types';
import { eq, or, ilike } from 'drizzle-orm';
import * as v from 'valibot';

export const getIngredients = query(async () => {
  const db = getDB();

  return await db.select().from(ingredient).orderBy(ingredient.name);
});

export const getIngredientsForMenuItem = query(v.string(), async (menuItemId: string) => {
  const db = getDB();

  const ingredients = await db
    .select()
    .from(menu)
    .where(eq(menu.id, menuItemId))
    .orderBy(ingredient.name)
    .leftJoin(recipe, eq(menu.id, recipe.menuItemId))
    .leftJoin(ingredient, eq(recipe.ingredientId, ingredient.id));

  if (!ingredients) {
    throw new Error('Menu item not found');
  }

  return ingredients.map((row) => row.ingredient).filter((r) => r !== null);
});

export const getToppingIngredients = query(async () => {
  const db = getDB();

  return await db
    .select()
    .from(ingredient)
    .where(
      or(ilike(ingredient.name, '%Pearls%'), ilike(ingredient.name, '%Jelly%'), ilike(ingredient.name, '%Ice Cream%')),
    )
    .orderBy(ingredient.name);
});

export const createIngredient = command(ingredientInsertSchema, async (newIngredient) => {
  const db = getDB();
  const created = await db.insert(ingredient).values(newIngredient).returning();

  await getIngredients().refresh();

  return created[0];
});

export const updateIngredient = command(ingredientUpdateSchema, async (updatedIngredient) => {
  if (!updatedIngredient.id) throw new Error('Ingredient ID is required for update');
  const db = getDB();

  await db.update(ingredient).set(updatedIngredient).where(eq(ingredient.id, updatedIngredient.id));
  await getIngredients().refresh();
});

export const updateRecipe = command(
  v.object({
    menuItemId: v.string(),
    ingredients: v.array(ingredientSelectSchema),
  }),
  async (data) => {
    const db = getDB();

    // Delete existing recipe entries for the menu item
    await db.delete(recipe).where(eq(recipe.menuItemId, data.menuItemId));

    // Insert new recipe entries
    for (const ing of data.ingredients) {
      await db.insert(recipe).values({
        menuItemId: data.menuItemId,
        ingredientId: ing.id,
        quantity: 1,
      });
    }
  },
);

export const orderIngredient = command(v.object({ id: v.string(), orderQuantity: v.number() }), async (data) => {
  const db = getDB();

  const ing = await db
    .select()
    .from(ingredient)
    .where(eq(ingredient.id, data.id))
    .limit(1)
    .then((res) => res[0]);

  if (!ing) {
    throw new Error('Ingredient not found');
  }

  const updated = await db
    .update(ingredient)
    .set({ orderStock: ing.orderStock + data.orderQuantity })
    .where(eq(ingredient.id, data.id))
    .returning();

  await getIngredients().refresh();

  return {
    orderStock: updated[0].orderStock,
    currentStock: updated[0].currentStock,
  };
});

export const receiveIngredient = command(v.object({ id: v.string(), receiveQuantity: v.number() }), async (data) => {
  const db = getDB();

  const ing = await db
    .select()
    .from(ingredient)
    .where(eq(ingredient.id, data.id))
    .limit(1)
    .then((res) => res[0]);

  if (!ing) {
    throw new Error('Ingredient not found');
  }

  if (data.receiveQuantity > ing.orderStock) {
    throw new Error('Cannot receive more than ordered stock');
  }

  const updated = await db
    .update(ingredient)
    .set({
      currentStock: ing.currentStock + data.receiveQuantity,
      orderStock: ing.orderStock - data.receiveQuantity,
    })
    .where(eq(ingredient.id, data.id))
    .returning();

  await getIngredients().refresh();

  return {
    currentStock: updated[0].currentStock,
    orderStock: updated[0].orderStock,
  };
});
