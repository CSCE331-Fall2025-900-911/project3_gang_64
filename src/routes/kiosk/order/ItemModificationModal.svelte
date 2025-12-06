<script lang="ts">
  import { getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
  import { slide } from 'svelte/transition';
  import type { Ingredient, MenuItem } from '$lib/db/types';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import { td } from '$lib/contexts/translations.svelte';
  import { toppingsManager } from '$lib/managers/toppings.svelte';
  import {
    Button,
    HStack,
    Heading,
    IconButton,
    Modal,
    ModalBody,
    ModalFooter,
    Text,
    toastManager,
    ModalHeader,
  } from '@immich/ui';
  import { mdiRestart } from '@mdi/js';
  import ItemModAddToast from './ItemModAddToast.svelte';
  import ItemModDeleteToast from './ItemModDeleteToast.svelte';
  import NumberStepper from '$lib/components/NumberStepper.svelte';

  interface Props {
    item: MenuItem;
    currentIngredientList?: Ingredient[];
    currentIceLevel?: string;
    currentSugarLevel?: string;
    currentLessList?: string[];
    currentCartPrice?: number;
    quantity?: number;
    states: { isAdded: boolean };
  }

  let {
    onClose,
    item,
    currentIngredientList = [],
    currentIceLevel = '',
    currentSugarLevel = '',
    currentLessList = [],
    currentCartPrice = item.price,
    quantity = 1,
    states,
  }: ModalProps & Props = $props();

  toppingsManager.load();

  let loading = $state(false);
  let currentPrice = $state(currentCartPrice);
  let shownPrice = $state(currentCartPrice);
  let baseItems = $derived(getIngredientsForMenuItem(item.id).current ?? []);
  // svelte-ignore state_referenced_locally
  let ingredientList = $state(currentIngredientList.length == 0 ? baseItems : currentIngredientList);
  const toppingsList = $derived(toppingsManager.toppings);
  const markup = 0.5;
  const levelOptions = ['None', 'Less', 'Normal', 'Extra'] as const;
  type Level = 'None' | 'Less' | 'Normal' | 'Extra';
  let selectedIce = $state<Level>((currentIceLevel.length === 0 ? 'Normal' : currentIceLevel) as Level);
  let selectedSugar = $state<Level>((currentSugarLevel.length === 0 ? 'Normal' : currentSugarLevel) as Level);
  let selectedIceIndex = $derived(levelOptions.indexOf(selectedIce));
  let selectedSugarIndex = $derived(levelOptions.indexOf(selectedSugar));
  const positive = 1;
  const negative = -1;
  let ingredientSelection = $state<Record<string, Level>>({});
  $effect(() => {
    if (baseItems.length === 0) return;

    for (const ing of baseItems) {
      if (currentLessList.includes(ing.id)) {
        ingredientSelection[ing.id] = 'Less';
        continue;
      }

      const count = ingredientList.filter((x) => x.id === ing.id).length;

      ingredientSelection[ing.id] = count === 2 ? 'Extra' : 'Normal';
    }
  });
  const total = $derived({
    calories: ingredientList.reduce((s, i) => s + (i.calories ?? 0), 0),
    fat_g: ingredientList.reduce((s, i) => s + (i.fat_g ?? 0), 0),
    sodium_g: ingredientList.reduce((s, i) => s + (i.sodium_g ?? 0), 0),
    carbs_g: ingredientList.reduce((s, i) => s + (i.carbs_g ?? 0), 0),
    sugar_g: ingredientList.reduce((s, i) => s + (i.sugar_g ?? 0), 0),
    caffeine_mg: ingredientList.reduce((s, i) => s + (i.caffiene_mg ?? 0), 0),
  });
  const allergenList = $derived(
    Array.from(new Set(ingredientList.flatMap((ing) => (Array.isArray(ing.allergen) ? ing.allergen : [])))).sort(),
  );
  let showNutrition = $state(false);

  function selectOption(ing: Ingredient, option: Level) {
    ingredientSelection[ing.id] = option;
    removeOneIngredient(ing);
    removeOneIngredient(ing);
    currentLessList = currentLessList.filter((x) => x !== ing.id);
    switch (option) {
      case 'Less':
        currentLessList.push(ing.id);
        addOneIngredient(ing);
        break;
      case 'Extra':
        addOneIngredient(ing);
        addOneIngredient(ing);
        break;
      default:
        addOneIngredient(ing);
    }
  }

  async function handleAddToOrder() {
    loading = true;
    currentPrice = currentPrice >= item.price ? currentPrice : item.price;
    await orderManager.addToOrder(
      item,
      ingredientList,
      currentPrice,
      selectedIce,
      selectedSugar,
      currentLessList,
      quantity,
    );
    loading = false;

    states.isAdded = true;

    onClose();
  }

  async function showNutritionInfo() {
    showNutrition = !showNutrition;
  }

  function changeIngredientsList(ingredient: Ingredient, newAmt: number) {
    let oldAmt = ingredientList.filter((i) => i.name === ingredient.name).length;
    if (oldAmt > newAmt) {
      removeOneIngredient(ingredient);

      if (ingredientList.length <= 1) {
        toastManager.custom({ component: ItemModDeleteToast, props: {} }, { timeout: 5000, closable: true });
        return;
      }
    } else {
      addOneIngredient(ingredient);

      if (ingredientList.length == 10) {
        toastManager.custom({ component: ItemModAddToast, props: {} }, { timeout: 5000, closable: true });
        return;
      }
    }
  }

  function removeOneIngredient(target: Ingredient) {
    const index = ingredientList.findIndex((item) => item.id === target.id);
    if (index !== -1) {
      ingredientList.splice(index, 1);
      ingredientList = [...ingredientList];
      updatePricing(target, negative);
    }
  }

  function addOneIngredient(target: Ingredient) {
    ingredientList = [...ingredientList, target];
    updatePricing(target, positive);
  }

  function updatePricing(target: Ingredient, direction: number) {
    const isBaseItem = baseItems.some((i) => i.id === target.id);
    const count = ingredientList.filter((i) => i.id === target.id).length;
    if (!isBaseItem || (count > 1 && direction == positive) || (count >= 1 && direction == negative)) {
      currentPrice += markup * direction;
    }

    currentPrice += target.unitPrice * direction;
    shownPrice = currentPrice >= item.price ? currentPrice : item.price;
  }

  function restartModification() {
    ingredientList = getIngredientsForMenuItem(item.id).current ?? [];
    currentPrice = item.price;
    shownPrice = item.price;
  }
</script>

<Modal {onClose} closeOnBackdropClick size="large">
  <ModalHeader>
    <div class="flex flex-col">
      <div class="flex items-center justify-between">
        <div class="flex flex-col">
          <Heading size="large">{td(item.name)}</Heading>
          <Text>${shownPrice.toFixed(2)}</Text>
        </div>
        <Button onclick={showNutritionInfo} shape="semi-round" {loading}>
          {t('kiosk_nutrition')}
        </Button>
      </div>
      {#if showNutrition}
        <div transition:slide|local class="mt-4">
          <div class="grid grid-cols-2 gap-8">
            <div>
              <Heading size="small" class="mb-2">{t('kiosk_nutrition')}</Heading>

              <div class="bg-level-2 grid grid-cols-3 gap-x-4 gap-y-2 rounded-lg border p-3">
                <Text size="tiny">{t('kiosk_nutrition_calories')}: {total.calories.toFixed(1)}</Text>
                <Text size="tiny">{t('kiosk_nutrition_fat')}: {total.fat_g.toFixed(1)}g</Text>
                <Text size="tiny">{t('kiosk_nutrition_sodium')}: {total.sodium_g.toFixed(1)}g</Text>
                <Text size="tiny">{t('kiosk_nutrition_carbs')}: {total.carbs_g.toFixed(1)}g</Text>
                <Text size="tiny">{t('kiosk_nutrition_sugar')}: {total.sugar_g.toFixed(1)}g</Text>
                <Text size="tiny">{t('kiosk_nutrition_caffeine')}: {total.caffeine_mg.toFixed(1)}mg</Text>
              </div>
            </div>
            <div>
              <Heading size="small" class="mb-2">{t('kiosk_allergens')}</Heading>

              <div class="bg-level-2 grid grid-cols-3 gap-x-4 gap-y-2 rounded-lg border p-3">
                {#if allergenList.length > 0}
                  {#each allergenList as allergen}
                    <Text size="tiny">{td(allergen)}</Text>
                  {/each}
                {:else}
                  <Text size="tiny" class="text-muted-foreground col-span-3">
                    {t('kiosk_allergens_none')}
                  </Text>
                {/if}
              </div>
            </div>
          </div>
        </div>
      {/if}
    </div>
  </ModalHeader>
  <ModalBody>
    <div class="relative">
      <div class="flex flex-row">
        <div class="mr-4 ml-2 flex w-full flex-col">
          <div class="mb-4">
            <Heading size="small" class="mb-2">{t('kiosk_baseItems')}</Heading>
            <div class="w-full gap-2">
              {#each baseItems as ing}
                {#if !td(ing.category).toLowerCase().includes('ice') && !toppingsList?.some((x) => x.id == ing.id)}
                  <div class="mb-2 flex items-center justify-between">
                    <Text>{td(ing.name)}</Text>

                    <div class="flex flex-row">
                      <Button
                        class="w-1/3"
                        shape="semi-round"
                        size="tiny"
                        color={ingredientSelection[ing.id] === 'Less' ? 'primary' : 'secondary'}
                        onclick={() => selectOption(ing, 'Less')}
                      >
                        {t('kiosk_iceLevel_low')}
                      </Button>
                      <Button
                        class="ml-1 w-1/3"
                        shape="semi-round"
                        size="tiny"
                        color={ingredientSelection[ing.id] === 'Normal' ? 'primary' : 'secondary'}
                        onclick={() => selectOption(ing, 'Normal')}
                      >
                        {t('kiosk_iceLevel_normal')}
                      </Button>
                      <Button
                        class="ml-1 w-1/3"
                        shape="semi-round"
                        size="tiny"
                        color={ingredientSelection[ing.id] === 'Extra' ? 'primary' : 'secondary'}
                        onclick={() => selectOption(ing, 'Extra')}
                      >
                        <div class="flex flex-col items-center align-middle">
                          {t('kiosk_iceLevel_high')}
                          <Text size="tiny">+${(ing.unitPrice + markup).toFixed(2)}</Text>
                        </div>
                      </Button>
                    </div>
                  </div>
                {/if}
              {/each}
            </div>
          </div>

          <div class="mb-4">
            <Heading size="small" class="mb-2">{t('kiosk_iceLevel')}</Heading>
            <div class="slider-container">
              <input
                type="range"
                min="0"
                max={levelOptions.length - 1}
                step="1"
                bind:value={selectedIceIndex}
                oninput={() => (selectedIce = levelOptions[selectedIceIndex])}
              />
            </div>
            <div class="labels">
              {#each levelOptions as option}
                <span>{option}</span>
              {/each}
            </div>
          </div>

          <div class="mb-4">
            <Heading size="small" class="mb-2">{t('kiosk_sugarLevel')}</Heading>
            <div class="slider-container">
              <input
                type="range"
                min="0"
                max={levelOptions.length - 1}
                step="1"
                bind:value={selectedSugarIndex}
                oninput={() => (selectedSugar = levelOptions[selectedSugarIndex])}
              />
            </div>
            <div class="labels">
              {#each levelOptions as option}
                <span>{option}</span>
              {/each}
            </div>
          </div>

          <div class="mb-2">
            <Heading size="small" class="mb-2">{t('kiosk_toppings')}</Heading>
            <div class="w-full gap-2">
              {#each toppingsList ?? [] as ing}
                {@const count = ingredientList.filter((i) => i.id == ing.id).length}
                {@const maxAmt = ingredientList.length >= 10 ? -Infinity : ing.currentStock}
                {@const minAmt = ingredientList.length <= 1 ? Infinity : 0}
                <div class="mb-2 flex items-center justify-between">
                  <div class="flex flex-col">
                    <Text>{td(ing.name)}</Text>
                    <Text size="tiny">(+${(ing.unitPrice + markup).toFixed(2)})</Text>
                  </div>
                  <NumberStepper
                    value={count}
                    min={minAmt}
                    max={maxAmt}
                    onChange={(newValue) => changeIngredientsList(ing, newValue)}
                  />
                </div>
              {/each}
            </div>
          </div>
        </div>
      </div>
    </div></ModalBody
  >
  <ModalFooter>
    <HStack class="mt-4 w-full" gap={2}>
      <Button onclick={handleAddToOrder} shape="round" color="danger" class="w-9/10" {loading}>
        {t('kiosk_addToCart')}
      </Button>
      <IconButton
        onclick={restartModification}
        shape="round"
        color="secondary"
        class="w-1/10"
        icon={mdiRestart}
        aria-label={t('kiosk_restartModification')}
      />
    </HStack>
  </ModalFooter>
</Modal>
