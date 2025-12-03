<script lang="ts">
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import { Modal, ModalBody, Heading, Text, ModalFooter } from '@immich/ui';
  import { mdiInformationBoxOutline } from '@mdi/js';
  import type { Ingredient } from '$lib/db/types';

  interface Props {
    ingredientList: Ingredient[];
  }

  let { onClose, ingredientList }: ModalProps & Props = $props();

  let totalNutrition = $derived.by(() => {
    return {
      calories: ingredientList.reduce((sum, ing) => sum + (ing.calories || 0), 0),
      fat_g: ingredientList.reduce((sum, ing) => sum + (ing.fat_g || 0), 0),
      sodium_g: ingredientList.reduce((sum, ing) => sum + (ing.sodium_g || 0), 0),
      carbs_g: ingredientList.reduce((sum, ing) => sum + (ing.carbs_g || 0), 0),
      sugar_g: ingredientList.reduce((sum, ing) => sum + (ing.sugar_g || 0), 0),
      caffiene_mg: ingredientList.reduce((sum, ing) => sum + (ing.caffiene_mg || 0), 0),
    };
  });

  let allergenList = $derived.by(() => {
    const allergens = new Set<string>();
    ingredientList.forEach((ing) => {
      if (ing.allergen && Array.isArray(ing.allergen)) {
        ing.allergen.forEach((allergen) => allergens.add(allergen));
      }
    });
    return Array.from(allergens).sort();
  });
</script>

<Modal title={t('kiosk_nutritionModal_title')} icon={mdiInformationBoxOutline} {onClose} size="large">
  <ModalBody>
    <Heading size="small" class="mb-2">{t('kiosk_nutrition')}</Heading>
    <div class="flex flex-col gap-1 border-b pb-3 pl-4">
      <Text size="small">{t('kiosk_nutrition_calories')}: {totalNutrition.calories.toFixed(1)}</Text>
      <Text size="small">{t('kiosk_nutrition_fat')}: {totalNutrition.fat_g.toFixed(1)}g</Text>
      <Text size="small">{t('kiosk_nutrition_sodium')}: {totalNutrition.sodium_g.toFixed(1)}g</Text>
      <Text size="small">{t('kiosk_nutrition_carbs')}: {totalNutrition.carbs_g.toFixed(1)}g</Text>
      <Text size="small">{t('kiosk_nutrition_sugar')}: {totalNutrition.sugar_g.toFixed(1)}g</Text>
      <Text size="small">{t('kiosk_nutrition_caffeine')}: {totalNutrition.caffiene_mg.toFixed(1)}mg</Text>
    </div>
    <Heading size="small" class="mt-3 mb-2">{t('kiosk_allergens')}</Heading>
    <div class="flex flex-col gap-1 pl-4">
      {#if allergenList.length > 0}
        {#each allergenList as allergen}
          <Text size="small">{allergen}</Text>
        {/each}
      {:else}
        <Text size="small" class="text-muted-foreground">{t('kiosk_allergens_none')}</Text>
      {/if}
    </div>
    <div class="flex h-screen flex-col"></div>
  </ModalBody>
</Modal>
