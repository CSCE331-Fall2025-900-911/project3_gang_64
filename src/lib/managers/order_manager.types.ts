import type { Ingredient, MenuItem } from '$lib/db/types';

export interface OrderEntry {
  menuItem: MenuItem;
  ingredients: Ingredient[];
}
