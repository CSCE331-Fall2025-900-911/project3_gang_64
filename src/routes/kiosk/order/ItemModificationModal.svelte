<script lang="ts">
  import { getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
  import NumberStepper from '$lib/components/NumberStepper.svelte';
  import { td } from '$lib/contexts/translations.svelte';
  import type { Ingredient, MenuItem } from '$lib/db/types';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { toppingsManager } from '$lib/managers/toppings.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import {
    Button,
    HStack,
    Heading,
    IconButton,
    Modal,
    ModalBody,
    ModalFooter,
    ModalHeader,
    Text,
    toastManager,
  } from '@immich/ui';
  import { mdiListBox, mdiPlus, mdiRestart } from '@mdi/js';
  import { slide } from 'svelte/transition';
  import ItemModValidateToast from './ItemModValidateToast.svelte';

  interface Props {
    item: MenuItem;
    currentIngredientList?: Ingredient[];
    currentIceLevel?: string;
    currentSugarLevel?: string;
    currentCartPrice?: number;
    quantity?: number;
    isEdit?: boolean;
    isCashier?: boolean;
    states: { isAdded: boolean };
  }

  let {
    onClose,
    item,
    currentIngredientList = [],
    currentIceLevel = '',
    currentSugarLevel = '',
    currentCartPrice = item.price,
    quantity = 1,
    isEdit = false,
    isCashier = false,
    states,
  }: ModalProps & Props = $props();

  toppingsManager.load();
  const toppingsList = $derived(toppingsManager.toppings);
  let baseItems = $derived(getIngredientsForMenuItem(item.id).current ?? []);
  // svelte-ignore state_referenced_locally
  let ingredientList = $state(currentIngredientList.length == 0 ? baseItems : currentIngredientList);

  let loading = $state(false);
  let currentPrice = $state(currentCartPrice);
  let shownPrice = $state(currentCartPrice);
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
      const count = ingredientList.filter((x) => x.id === ing.id).length;
      switch (count) {
        case 0:
          ingredientSelection[ing.id] = 'None';
          break;
        case 1:
          ingredientSelection[ing.id] = 'Normal';
          break;
        case 2:
          ingredientSelection[ing.id] = 'Extra';
          break;
      }
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

  //UI Stuff
  const kioskIngredientUI = 'w-full gap-2';
  const cashierIngredientUI = 'grid [grid-template-columns:repeat(auto-fill,minmax(180px,1fr))] gap-5 w-full';
  const cashierIceSugarUI = 'grid [grid-template-columns:repeat(auto-fill,minmax(250px,1fr))] gap-5 w-full';
  const kioskIngredientStructureUI = 'mb-2 flex items-center justify-between';
  const cashierIngredientStructureUI = 'mb-2 flex flex-col items-center min-w-0 max-w-full overflow-hidden';
  const kioskBaseItemButtonsUI = 'flex flex-row';
  const cashierBaseItemButtonsUI = 'mt-1 flex flex-row min-w-0';
  const cashierIceSugarItemButtonsUI = 'mt-1 flex flex-row';

  function selectOption(ing: Ingredient, option: Level) {
    ingredientSelection[ing.id] = option;
    removeOneIngredient(ing);
    removeOneIngredient(ing);
    switch (option) {
      case 'Normal':
        addOneIngredient(ing);
        break;
      case 'Extra':
        addOneIngredient(ing);
        addOneIngredient(ing);
        break;
    }

    if (ingredientList.length <= 1) {
      toastManager.custom(
        { component: ItemModValidateToast, props: { isMax: false } },
        { timeout: 5000, closable: true },
      );
      return;
    } else if (ingredientList.length >= 100) {
      toastManager.custom(
        { component: ItemModValidateToast, props: { isMax: true } },
        { timeout: 5000, closable: true },
      );
      return;
    }
  }

  async function handleAddToOrder() {
    loading = true;
    currentPrice = currentPrice >= item.price ? currentPrice : item.price;
    await orderManager.addToOrder(item, ingredientList, currentPrice, selectedIce, selectedSugar, quantity, isCashier);
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
        toastManager.custom(
          { component: ItemModValidateToast, props: { isMax: false } },
          { timeout: 5000, closable: true },
        );
        return;
      }
    } else {
      addOneIngredient(ingredient);

      if (ingredientList.length == 100) {
        toastManager.custom(
          { component: ItemModValidateToast, props: { isMax: true } },
          { timeout: 5000, closable: true },
        );
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

<Modal {onClose} closeOnBackdropClick size={isCashier ? 'giant' : 'large'}>
  <ModalHeader>
    <div class="flex flex-col">
      <div class="flex items-center justify-between">
        <div class="flex flex-row">
          <Heading size="large">{td(item.name)}</Heading>
        </div>
        {#if !isCashier}
          <Button onclick={showNutritionInfo} shape="semi-round" {loading}>
            {t('kiosk_nutrition')}
          </Button>
        {:else}
          <div class="flex flex-row gap-2">
            <div class="flex flex-row">
              <Text class="text-2xl">Cost:</Text>
        <div class="bg-white px-2 py-1 mx-2 rounded-full">
          <Text class="text-2xl text-black">${shownPrice.toFixed(2)}</Text>
        </div>
            </div>
            <IconButton
              onclick={showNutritionInfo}
              shape="round"
              {loading}
              icon={mdiListBox}
              color="primary"
              aria-label={t('kiosk_nutrition')}
            />
            <IconButton
              onclick={restartModification}
              shape="round"
              {loading}
              icon={mdiRestart}
              color="secondary"
              aria-label={t('kiosk_restartModification')}
            />
            <IconButton
              onclick={handleAddToOrder}
              shape="round"
              {loading}
              icon={mdiPlus}
              color="success"
              aria-label={t('kiosk_addToCart')}
            />
          </div>
        {/if}
      </div>
      {#if showNutrition}
        <div transition:slide|local class="mt-4">
          <div class="grid grid-cols-2 gap-8">
            <div>
              <Heading size="small" class="mb-2">{t('kiosk_nutrition')}</Heading>

              <div class="bg-level-2 grid grid-cols-3 gap-x-4 gap-y-2 rounded-lg border p-3">
                <Text size="small">{t('kiosk_nutrition_calories')}: {total.calories.toFixed(1)}</Text>
                <Text size="small">{t('kiosk_nutrition_fat')}: {total.fat_g.toFixed(1)}g</Text>
                <Text size="small">{t('kiosk_nutrition_sodium')}: {total.sodium_g.toFixed(1)}g</Text>
                <Text size="small">{t('kiosk_nutrition_carbs')}: {total.carbs_g.toFixed(1)}g</Text>
                <Text size="small">{t('kiosk_nutrition_sugar')}: {total.sugar_g.toFixed(1)}g</Text>
                <Text size="small">{t('kiosk_nutrition_caffeine')}: {total.caffeine_mg.toFixed(1)}mg</Text>
              </div>
            </div>
            <div>
              <Heading size="small" class="mb-2">{t('kiosk_allergens')}</Heading>

              <div class="bg-level-2 grid grid-cols-3 gap-x-4 gap-y-2 rounded-lg border p-3">
                {#if allergenList.length > 0}
                  {#each allergenList as allergen}
                    <Text size="small">{td(allergen)}</Text>
                  {/each}
                {:else}
                  <Text size="small" class="text-muted-foreground col-span-3">
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
            <div class={isCashier ? cashierIngredientUI : kioskIngredientUI}>
              {#each baseItems as ing}
                {#if !ing.category.toLowerCase().includes('ice') && !toppingsList?.some((x) => x.id == ing.id)}
                  <div class={isCashier ? cashierIngredientStructureUI : kioskIngredientStructureUI}>
                    <Text>{td(ing.name)}</Text>

                    <div class={isCashier ? cashierBaseItemButtonsUI : kioskBaseItemButtonsUI}>
                      <Button
                        class="w-1/3 py-1"
                        shape="semi-round"
                        size="small"
                        color={ingredientSelection[ing.id] === 'None' ? 'primary' : 'secondary'}
                        onclick={() => selectOption(ing, 'None')}
                        disabled={(ingredientList.length <= 1 ||
                          (ingredientSelection[ing.id] === 'Extra' && ingredientList.length <= 2)) &&
                          ingredientSelection[ing.id] !== 'None'}
                      >
                        {t('kiosk_iceLevel_none')}
                      </Button>
                      <Button
                        class="ml-1 w-1/3 py-1"
                        shape="semi-round"
                        size="small"
                        color={ingredientSelection[ing.id] === 'Normal' ? 'primary' : 'secondary'}
                        onclick={() => selectOption(ing, 'Normal')}
                        disabled={((ingredientList.length >= 100 && ingredientSelection[ing.id] === 'None') ||
                          (ingredientSelection[ing.id] === 'None' && ing.currentStock <= 0)) &&
                          ingredientSelection[ing.id] !== 'Normal'}
                      >
                        {t('kiosk_iceLevel_normal')}
                      </Button>
                      <Button
                        class="ml-1 w-1/3"
                        shape="semi-round"
                        size="small"
                        color={ingredientSelection[ing.id] === 'Extra' ? 'primary' : 'secondary'}
                        onclick={() => selectOption(ing, 'Extra')}
                        disabled={((ingredientList.length >= 100 && ingredientSelection[ing.id] === 'Normal') ||
                          (ingredientList.length >= 9 && ingredientSelection[ing.id] === 'None') ||
                          (ingredientList.filter((i) => i.id == ing.id).length >= ing.currentStock &&
                            ingredientSelection[ing.id] === 'Normal') ||
                          (ingredientSelection[ing.id] === 'None' &&
                            ingredientList.filter((i) => i.id == ing.id).length + 1 >= ing.currentStock)) &&
                          ingredientSelection[ing.id] !== 'Extra'}
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

          <div class="w-full h-1 mb-3 bg-(--immich-ui-primary-600)"></div>
          
          {#if !isCashier}
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
              <div class="labels !text-base">
                <Text>{t('kiosk_sugarLevel_none')}</Text>
                <Text>{t('kiosk_sugarLevel_low')}</Text>
                <Text>{t('kiosk_sugarLevel_normal')}</Text>
                <Text>{t('kiosk_sugarLevel_high')}</Text>
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
              <div class="labels !text-base">
                <Text>{t('kiosk_iceLevel_none')}</Text>
                <Text>{t('kiosk_iceLevel_low')}</Text>
                <Text>{t('kiosk_iceLevel_normal')}</Text>
                <Text>{t('kiosk_iceLevel_high')}</Text>
              </div>
            </div>
          {:else}
            <div class="mb-4">
              <Heading size="small" class="mb-2">{t('kiosk_iceAndSugarLevel')}</Heading>
              <div class={cashierIceSugarUI}>
                <div class="flex flex-col items-start">
                  <div class="flex flex-col items-center">
                    <Text>{t('kiosk_iceLevel')}</Text>
                    <div class={cashierIceSugarItemButtonsUI}>
                      <Button
                        class="w-1/4"
                        shape="semi-round"
                        size="small"
                        color={selectedIce === 'None' ? 'primary' : 'secondary'}
                        onclick={() => (selectedIce = 'None')}
                      >
                        {t('kiosk_iceLevel_none')}
                      </Button>
                      <Button
                        class="ml-1 w-1/4"
                        shape="semi-round"
                        size="small"
                        color={selectedIce === 'Less' ? 'primary' : 'secondary'}
                        onclick={() => (selectedIce = 'Less')}
                      >
                        {t('kiosk_iceLevel_low')}
                      </Button>
                      <Button
                        class="ml-1 w-1/4"
                        shape="semi-round"
                        size="small"
                        color={selectedIce === 'Normal' ? 'primary' : 'secondary'}
                        onclick={() => (selectedIce = 'Normal')}
                      >
                        {t('kiosk_iceLevel_normal')}
                      </Button>
                      <Button
                        class="ml-1 w-1/4"
                        shape="semi-round"
                        size="small"
                        color={selectedIce === 'Extra' ? 'primary' : 'secondary'}
                        onclick={() => (selectedIce = 'Extra')}
                      >
                        {t('kiosk_iceLevel_high')}
                      </Button>
                    </div>
                  </div>
                </div>
                <div class="flex flex-col items-center">
                  <div class="flex flex-col items-center">
                    <Text>{t('kiosk_sugarLevel')}</Text>
                    <div class={cashierIceSugarItemButtonsUI}>
                      <Button
                        class="w-1/4"
                        shape="semi-round"
                        size="small"
                        color={selectedSugar === 'None' ? 'primary' : 'secondary'}
                        onclick={() => (selectedSugar = 'None')}
                      >
                        {t('kiosk_sugarLevel_none')}
                      </Button>
                      <Button
                        class="ml-1 w-1/4"
                        shape="semi-round"
                        size="small"
                        color={selectedSugar === 'Less' ? 'primary' : 'secondary'}
                        onclick={() => (selectedSugar = 'Less')}
                      >
                        {t('kiosk_sugarLevel_low')}
                      </Button>
                      <Button
                        class="ml-1 w-1/4"
                        shape="semi-round"
                        size="small"
                        color={selectedSugar === 'Normal' ? 'primary' : 'secondary'}
                        onclick={() => (selectedSugar = 'Normal')}
                      >
                        {t('kiosk_sugarLevel_normal')}
                      </Button>
                      <Button
                        class="ml-1 w-1/4"
                        shape="semi-round"
                        size="small"
                        color={selectedSugar === 'Extra' ? 'primary' : 'secondary'}
                        onclick={() => (selectedSugar = 'Extra')}
                      >
                        {t('kiosk_sugarLevel_high')}
                      </Button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          {/if}

          <div class="w-full h-1 mb-3 bg-(--immich-ui-primary-600)"></div>

          <div class="mb-2">
            <Heading size="small" class="mb-2">{t('kiosk_toppings')}</Heading>
            <div class={isCashier ? cashierIngredientUI : kioskIngredientUI}>
              {#each toppingsList ?? [] as ing}
                {@const count = ingredientList.filter((i) => i.id == ing.id).length}
                {@const maxAmt = ingredientList.length >= 100 ? -Infinity : ing.currentStock}
                {@const minAmt = ingredientList.length <= 1 ? Infinity : 0}
                <div class={isCashier ? cashierIngredientStructureUI : kioskIngredientStructureUI}>
                  <div class={isCashier ? 'flex flex-col items-center' : 'flex flex-col'}>
                    <Text>{td(ing.name)}</Text>
                    <Text size="small">(+${(ing.unitPrice + markup).toFixed(2)})</Text>
                  </div>
                  <div class={isCashier ? 'scale-85 transform' : ''}>
                    <NumberStepper
                      value={count}
                      min={minAmt}
                      max={maxAmt}
                      onChange={(newValue) => changeIngredientsList(ing, newValue)}
                    />
                  </div>
                </div>
              {/each}
            </div>
          </div>
        </div>
      </div>
    </div>
  </ModalBody>
  {#if !isCashier}
    <ModalFooter>
      <HStack class="mt-4 w-full" gap={2}>
        <Text class="text-2xl">Cost: </Text>
        <div class="bg-(--immich-ui-primary-500) px-2 py-1 rounded-full">
          <Text class="text-2xl text-black">${shownPrice.toFixed(2)}</Text>
        </div>
        <Button onclick={handleAddToOrder} shape="round" color="success" class="w-9/10" {loading}>
          {#if isEdit}
            {t('kiosk_editItem')}
          {:else}
            {t('kiosk_addToCart')}
          {/if}
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
  {/if}
</Modal>
