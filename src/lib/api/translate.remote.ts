import { command, query } from '$app/server';
import { getDB } from '$lib/db';
import { translation } from '$lib/db/schema';
import { translationInsertSchema, translationUpdateSchema } from '$lib/db/types';
import { invalidateTranslationsCache } from '../../hooks.server';
import { eq } from 'drizzle-orm';
import * as v from 'valibot';

export const getTranslations = query(async () => {
  // Implementation for fetching translations from the database
  const db = getDB();

  return await db.select().from(translation);
});

export const createTranslation = command(translationInsertSchema, async (newTranslation) => {
  const db = getDB();
  const created = await db.insert(translation).values(newTranslation).returning();

  invalidateTranslationsCache();
  await getTranslations().refresh();

  return created[0];
});

export const updateTranslation = command(translationUpdateSchema, async (updatedTranslation) => {
  if (!updatedTranslation.id) throw new Error('Translation ID is required for update');
  const db = getDB();

  await db.update(translation).set(updatedTranslation).where(eq(translation.id, updatedTranslation.id));
  invalidateTranslationsCache();
  await getTranslations().refresh();
});

export const deleteTranslation = command(v.string(), async (id: string) => {
  const db = getDB();
  await db.delete(translation).where(eq(translation.id, id));
  invalidateTranslationsCache();
  await getTranslations().refresh();
});

export const findTranslationByText = query(
  v.object({
    text: v.string(),
    locale: v.union([v.literal('en'), v.literal('es'), v.literal('de'), v.literal('fr')]),
  }),
  async ({ text, locale }) => {
    const db = getDB();
    const result = await db
      .select()
      .from(translation)
      .where(eq(translation[locale], text))
      .limit(1)
      .then((res) => res[0]);

    return result?.id ?? null;
  },
);
