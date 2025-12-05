<script lang="ts">
  import { getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
  import type { Ingredient, MenuItem } from '$lib/db/types';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import { td } from '$lib/contexts/translations.svelte';
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
    modalManager,
    ModalHeader,
  } from '@immich/ui';
  import { mdiRestart } from '@mdi/js';
  import ItemModAddToast from './ItemModAddToast.svelte';
  import ItemModDeleteToast from './ItemModDeleteToast.svelte';
  import NutritionInfoModal from './NutritionInfoModal.svelte';
  import NumberStepper from '$lib/components/NumberStepper.svelte';

  interface Props {
    item: MenuItem;
    states: { isAdded: boolean };
  }

  let { onClose, item, states }: ModalProps & Props = $props();
  let loading = $state(false);
  let currentPrice = $state(item.price);
  let shownPrice = $state(item.price);
  let baseItems = $derived(getIngredientsForMenuItem(item.id).current ?? []);
  // svelte-ignore state_referenced_locally
  let ingredientList = $state(baseItems);
  const markup = 0.5;
  const levelOptions = ['None', 'Less', 'Normal', 'Extra'] as const;
  type Level = 'None' | 'Less' | 'Normal' | 'Extra';
  let selectedIce = $state<Level>('Normal');
  let selectedSugar = $state<Level>('Normal');
  let selectedIceIndex = $derived(levelOptions.indexOf(selectedIce));
  let selectedSugarIndex = $derived(levelOptions.indexOf(selectedSugar));
  const positive = 1;
  const negative = -1;
  let ingredientSelection = $state<Record<string, Level>>({});
  $effect(() => {
    for (const ing of baseItems) {
      if (!ingredientSelection[ing.name]) {
        ingredientSelection[ing.name] = 'Normal';
      }
    }
  });

  function selectOption(ing: Ingredient, option: Level) {
    ingredientSelection[ing.name] = option;
    removeOneIngredient(ing);
    removeOneIngredient(ing);
    switch (option) {
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
    await orderManager.addToOrder(item, ingredientList, currentPrice, selectedIce, selectedSugar);
    loading = false;

    states.isAdded = true;

    onClose();
  }

  async function showNutritionInfo() {
    await modalManager.show(NutritionInfoModal, { ingredientList });
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
    <div class="flex items-center justify-between">
      <div class="flex flex-col">
        <Heading size="large">{td(item.name)}</Heading>
        <Text>${shownPrice.toFixed(2)}</Text>
      </div>
      <div>
        <Button onclick={showNutritionInfo} shape="semi-round" {loading}>
          {t('kiosk_nutrition')}
        </Button>
      </div>
    </div>
  </ModalHeader>
  <ModalBody>
    <div class="flex flex-row">
      <div class="mr-4 ml-2 flex w-full flex-col">
        <div class="mb-4">
          <Heading size="small" class="mb-2">{t('kiosk_baseItems')}</Heading>
          <div class="w-full gap-2">
            {#each baseItems as ing}
              {#if !ing.category.includes('Ice')}
                <div class="mb-2 flex items-center justify-between">
                  <Text>{ing.name}</Text>

                  <div class="flex flex-row">
                    <Button
                      class="w-1/3"
                      shape="semi-round"
                      size="tiny"
                      color={ingredientSelection[ing.name] === 'Less' ? 'primary' : 'secondary'}
                      onclick={() => selectOption(ing, 'Less')}
                    >
                      {t('kiosk_iceLevel_low')}
                    </Button>
                    <Button
                      class="ml-1 w-1/3"
                      shape="semi-round"
                      size="tiny"
                      color={ingredientSelection[ing.name] === 'Normal' ? 'primary' : 'secondary'}
                      onclick={() => selectOption(ing, 'Normal')}
                    >
                      {t('kiosk_iceLevel_normal')}
                    </Button>
                    <Button
                      class="ml-1 w-1/3"
                      shape="semi-round"
                      size="tiny"
                      color={ingredientSelection[ing.name] === 'Extra' ? 'primary' : 'secondary'}
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
            {#each baseItems ?? [] as ing}
              {#if ing.topping}
                {@const count = ingredientList.filter((i) => i.name == ing.name).length}
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
              {/if}
            {/each}
          </div>
        </div>
      </div>
    </div>
  </ModalBody>
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
