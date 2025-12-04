<script lang="ts">
  import { getIngredients, getIngredientsForMenuItem, updateRecipe } from '$lib/api/ingredient.remote';
  import { createMenuItem, updateMenuItem } from '$lib/api/menu.remote';
  import ImageUpload from '$lib/components/ImageUpload.svelte';
  import PriceInput from '$lib/components/PriceInput.svelte';
  import { BlankMenuItem, type CreateOrUpdate, type Ingredient, type MenuItem, type NewMenuItem } from '$lib/db/types';
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import { td } from '$lib/contexts/translations.svelte';

  import {
    Button,
    Field,
    Heading,
    HStack,
    IconButton,
    Input,
    LoadingSpinner,
    Modal,
    ModalBody,
    ModalFooter,
    Select,
    type SelectItem,
    Stack,
    Text,
  } from '@immich/ui';
  import { mdiPlus, mdiSilverware, mdiTrashCan } from '@mdi/js';

  interface Props extends ModalProps {
    mode: CreateOrUpdate<MenuItem>;
  }

  let { onClose, mode }: Props = $props();

  async function submit() {
    submitting = true;

    let createdItem: MenuItem | null = null;

    if (mode.type === 'new') {
      createdItem = await createMenuItem(item);
      if (createdItem) {
        item = createdItem as NewMenuItem;
      } else {
        submitting = false;
        return;
      }
    } else {
      await updateMenuItem({ id: mode.item.id, ...item });
    }

    await updateRecipe({
      menuItemId: item.id!,
      ingredients: recipe,
    });

    onClose();
  }

  function hasIngredient(ingredient: Ingredient): boolean {
    return recipe.some((ing) => ing.id === ingredient.id);
  }

  function addIngredient() {
    if (selectedIngredient) {
      const ing = ingredients.current?.find((i) => i.id === selectedIngredient!.value);

      if (ing) {
        recipe = [...recipe, ing];
        selectedIngredient = undefined;
      }
    }
  }

  function deleteIngredient(ingredient: Ingredient) {
    recipe = recipe.filter((ing) => ing.id !== ingredient.id);
  }

  // We only want to load the existing recipe once
  $effect(() => {
    if (mode.type === 'edit') {
      recipe = existingRecipe.current || [];
    } else {
      recipe = [];
    }
  });

  let item: NewMenuItem = $state(mode.type === 'edit' ? mode.item : BlankMenuItem);
  let submitting = $state(false);

  let existingRecipe = $derived(
    mode.type === 'edit' ? getIngredientsForMenuItem(item.id!) : { loading: false, error: null, current: [] },
  );
  let recipe = $state<Ingredient[]>([]);
  let valid = $derived(td(item.name ?? '').trim().length > 0);

  let ingredients = getIngredients();
  let ingredientOptions = $derived(
    ingredients.current?.map((ing) => ({ label: `${td(ing.name)}`, value: ing.id, disabled: hasIngredient(ing) })) ??
      [],
  );

  let selectedIngredient = $state<SelectItem | undefined>(undefined);
  let ingredientCost = $derived(recipe.reduce((total, ing) => total + (ing.unitPrice ?? 0), 0));
  let profit = $derived(item.price - ingredientCost);

  let nutritionInfo = $derived(
    recipe.length > 0
      ? {
          calories: recipe.reduce((total, ing) => total + (ing.calories ?? 0), 0),
          carbs: recipe.reduce((total, ing) => total + (ing.carbs_g ?? 0), 0),
          fat: recipe.reduce((total, ing) => total + (ing.fat_g ?? 0), 0),
          caffeine: recipe.reduce((total, ing) => total + (ing.caffiene_mg ?? 0), 0),
          sodium: recipe.reduce((total, ing) => total + (ing.sodium_g ?? 0), 0),
          sugar: recipe.reduce((total, ing) => total + (ing.sugar_g ?? 0), 0),
        }
      : null,
  );
</script>

<Modal
  title={mode.type === 'new' ? t('manager_menuitem_create_title') : t('manager_menuitem_edit_title')}
  icon={mdiSilverware}
  {onClose}
  size="giant"
>
  <ModalBody>
    <HStack gap={6} class="items-start">
      <Stack gap={4} class="w-1/2">
        <Stack gap={2}>
          <Text size="medium">{t('manager_menuitem_kiosk_image')}</Text>
          <ImageUpload bind:value={item.imageUrl} />
        </Stack>

        <Field label={t('manager_menuitem_label_name')}>
          <Input placeholder={t('manager_menuitem_placeholder_name')} bind:value={item.name} />
        </Field>

        <Field label={t('manager_menuitem_label_category')}>
          <Input placeholder={t('manager_menuitem_placeholder_category')} bind:value={item.category} />
        </Field>

        <Field label={t('manager_menuitem_label_price')}>
          <PriceInput placeholder={t('manager_menuitem_placeholder_number')} bind:value={item.price} />
        </Field>
        <Stack>
          {#if ingredients.loading || existingRecipe.loading}
            <div class="flex w-full justify-center">
              <LoadingSpinner size="large" />
            </div>
          {:else if ingredients.error || existingRecipe.error}{:else}
            <div class="my-2 h-px w-full bg-gray-300 dark:bg-gray-600"></div>

            <div class="flex w-full items-center justify-between rounded-md border p-2 dark:border-gray-500">
              <HStack class="w-full justify-between">
                <HStack gap={1}>
                  <Text size="small" class="font-semibold">{t('profit')}:</Text>
                  <Text size="small">${profit.toFixed(2)}</Text>
                </HStack>
                <HStack gap={1}>
                  <Text size="small" class="font-semibold">{t('ingredient_cost')}:</Text>
                  <Text size="small">${ingredientCost.toFixed(2)}</Text>
                </HStack>
              </HStack>
            </div>
            <Stack class="flex w-full items-center justify-between rounded-md border p-2 dark:border-gray-500">
              <Heading size="small" class="w-full font-semibold">{t('nutrition_info')}</Heading>
              <Stack class="flex w-full" gap={1} align="start">
                {#if nutritionInfo}
                  <Text size="small">
                    {nutritionInfo.calories} kcal
                  </Text>
                  <Text size="small">
                    {nutritionInfo.carbs}g Carbs
                  </Text>
                  <Text size="small">
                    {nutritionInfo.fat}g Fat
                  </Text>
                  <Text size="small">
                    {nutritionInfo.sugar}g Sugar
                  </Text>
                  <Text size="small">
                    {nutritionInfo.sodium}g Sodium
                  </Text>
                  <Text size="small">
                    {nutritionInfo.caffeine}mg Caffeine
                  </Text>
                {:else}{/if}
              </Stack>
            </Stack>
          {/if}
        </Stack>
      </Stack>

      <Stack gap={2} class="h-full w-1/2" align="start">
        <Heading size="medium">{t('manager_menuitem_recipe')}</Heading>
        {#if ingredients.loading || existingRecipe.loading}
          <div class="flex w-full justify-center">
            <LoadingSpinner size="large" />
          </div>
        {:else if ingredients.error || existingRecipe.error}
          <p class="text-danger">{t('manager_menuitem_error_loading_ingredients')}</p>
        {:else}
          <!-- Add Item Dropdown -->
          <div class="flex w-full items-center justify-between gap-2 rounded-md border p-2">
            <Select
              data={ingredientOptions}
              bind:value={selectedIngredient}
              class="w-full"
              placeholder={t('manager_menuitem_select_ingredient')}
            />
            <IconButton
              icon={mdiPlus}
              size="small"
              color="success"
              aria-label={t('manager_menuitem_add_ingredient_aria')}
              variant="ghost"
              onclick={addIngredient}
            />
          </div>

          {#each recipe as ingredient}
            <div class="flex w-full items-center justify-between rounded-md border p-2 dark:border-gray-500">
              <span>{td(ingredient.name)}</span>
              <div class="flex items-center gap-2">
                <span class="font-semibold">${ingredient.unitPrice.toFixed(2)}</span>
                <IconButton
                  icon={mdiTrashCan}
                  size="small"
                  color="danger"
                  aria-label={t('manager_menuitem_remove_ingredient_aria')}
                  variant="ghost"
                  onclick={() => deleteIngredient(ingredient)}
                />
              </div>
            </div>
          {/each}
        {/if}
      </Stack>
    </HStack>
  </ModalBody>
  <ModalFooter>
    <div class="grid w-full grid-cols-1 gap-2">
      <Button onclick={submit} shape="round" color="primary" disabled={!valid} loading={submitting}
        >{mode.type === 'new' ? t('manager_menuitem_create') : t('manager_menuitem_update')}</Button
      >
    </div>
  </ModalFooter>
</Modal>
