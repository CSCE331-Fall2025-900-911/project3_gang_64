import { query } from '$app/server';
import { getDB } from '$lib/db';
import { translation } from '$lib/db/schema';

export const getTranslations = query(async () => {
  // Implementation for fetching translations from the database
  const db = getDB();

  return await db.select().from(translation);
});
