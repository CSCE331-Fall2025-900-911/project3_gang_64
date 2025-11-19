import { ingredientSelectSchema, menuItemSelectSchema } from '$lib/db/types';
import * as v from 'valibot';

export const OrderEntrySchema = v.object({
  menuItem: menuItemSelectSchema,
  ingredients: v.array(ingredientSelectSchema),
  quantity: v.number(),
});
export type OrderEntry = v.InferInput<typeof OrderEntrySchema>;
