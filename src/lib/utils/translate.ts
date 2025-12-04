import { translateText } from '$lib/api/googletranslate.remote';
import type { MenuItem, Ingredient } from '../db/types';
import { getLocale } from '$lib/i18n/runtime';
import { get } from 'http';

export async function translateMenuItems(menuItems: MenuItem[]): Promise<MenuItem[]> {
  if (getLocale() === 'en') {
    return menuItems;
  }

  const itemNames: string[] = menuItems.map((item) => item.name);

  const translatedNames = await translateText({ segments: itemNames, target: getLocale() });

  return menuItems.map((item, index) => ({
    ...item,
    name: translatedNames[index],
  }));
}

export async function translateIngredients(ingredients: Ingredient[]): Promise<Ingredient[]> {
  if (getLocale() === 'en') {
    return ingredients;
  }

  const itemNames: string[] = ingredients.map((ingredient) => ingredient.name);

  const translatedNames = await translateText({ segments: itemNames, target: getLocale() });

  return ingredients.map((ingredient, index) => ({
    ...ingredient,
    name: translatedNames[index],
  }));
}
