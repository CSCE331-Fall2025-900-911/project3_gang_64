<script lang="ts">
  import { getIngredientsForMenuItem, getToppingIngredients } from '$lib/api/ingredient.remote';
  import type { Ingredient, MenuItem } from '$lib/db/types';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import { Button, HStack, Heading, IconButton, Modal, ModalBody, Text, toastManager } from '@immich/ui';
  import { mdiRestart, mdiTagEdit, mdiTrashCan } from '@mdi/js';
  import ItemModAddToast from './ItemModAddToast.svelte';
  import ItemModDeleteToast from './ItemModDeleteToast.svelte';

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
  let toppingsList = $derived(getToppingIngredients().current ?? []);
  const markup = 0.5;
  const levelBtn = 'flex h-20 items-center justify-center text-center rounded-xl transition';
  const levelOptions = ['None', 'Low', 'Normal', 'High'] as const;
  type Level = 'None' | 'Low' | 'Normal' | 'High';
  let selectedIce = $state<Level>('Normal');
  let selectedSugar = $state<Level>('Normal');

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

  function setIce(option: Level) {
    selectedIce = option;
  }

  function setSugar(option: Level) {
    selectedSugar = option;
  }

  async function handleAddToOrder() {
    loading = true;
    currentPrice = currentPrice >= item.price ? currentPrice : item.price;
    await orderManager.addToOrder(item, ingredientList, currentPrice, selectedIce, selectedSugar);
    loading = false;

    states.isAdded = true;

    onClose();
  }

  function addTopping(topping: Ingredient) {
    if (ingredientList.length >= 11) {
      toastManager.custom({ component: ItemModAddToast, props: {} }, { timeout: 5000, closable: true });
      return;
    }
    const hasTopping = ingredientList.some((i) => i.name === topping.name);
    ingredientList!.push(topping);
    currentPrice += topping.unitPrice;
    if ((hasTopping && baseItems.includes(topping)) || !baseItems.includes(topping)) {
      currentPrice += markup;
    }
    shownPrice = currentPrice >= item.price ? currentPrice : item.price;
  }

  function removeIngredient(index: number) {
    if (ingredientList.length <= 1) {
      toastManager.custom({ component: ItemModDeleteToast, props: {} }, { timeout: 5000, closable: true });
      return;
    }
    const ingredient = ingredientList![index];
    ingredientList!.splice(index, 1);
    const hasItem = ingredientList.some((i) => i.name === ingredient.name);
    if ((hasItem && baseItems.includes(ingredient)) || !baseItems.includes(ingredient)) {
      currentPrice -= markup;
    }
    currentPrice -= ingredient.unitPrice;
    shownPrice = currentPrice >= item.price ? currentPrice : item.price;
    ingredientList = [...ingredientList!];
  }

  function restartModification() {
    ingredientList = getIngredientsForMenuItem(item.id).current ?? [];
    currentPrice = item.price;
    shownPrice = item.price;
  }

  function toggleBaseItem(ingredient: Ingredient) {
    const hasItem = ingredientList.some((i) => i.name === ingredient.name);

    if (hasItem) {
      let removedIngredientsAmount = ingredientList.filter((i) => i.name == ingredient.name).length;
      ingredientList = ingredientList.filter((i) => i.name !== ingredient.name);
      currentPrice -= ingredient.unitPrice * removedIngredientsAmount + (removedIngredientsAmount - 1) * markup;
    } else {
      ingredientList = [...ingredientList, ingredient];
      currentPrice += ingredient.unitPrice;
    }

    shownPrice = currentPrice >= item.price ? currentPrice : item.price;
  }

  function validateToppingStock(topping: Ingredient) {
    let currentToppingAmount = ingredientList.filter((i) => i.name == topping.name).length;
    if (currentToppingAmount == topping.currentStock) {
      return true;
    }

    return false;
  }
</script>

<Modal title={t('kiosk_itemModification')} icon={mdiTagEdit} {onClose} size="large">
  <ModalBody>
    <div class="flex flex-row">
      <div class="mr-4 ml-2 flex w-7/12 flex-col">
        <div class="mb-4">
          <Heading size="small" class="mb-2">{t('kiosk_baseItems')}</Heading>
          <div class="grid w-full grid-cols-3 gap-2">
            {#each baseItems as baseIngredients}
              <Button
                shape="round"
                color={ingredientList.some((i) => i.name === baseIngredients.name) ? 'danger' : 'secondary'}
                class={levelBtn}
                onclick={() => toggleBaseItem(baseIngredients)}
              >
                {baseIngredients.name}
              </Button>
            {/each}
          </div>
        </div>
        <div class="mb-4">
          <Heading size="small" class="mb-2">{t('kiosk_iceLevel')}</Heading>
          <div class="grid w-full grid-cols-3 gap-2">
            {#each levelOptions as option}
              <Button
                shape="round"
                color={selectedIce === option ? 'danger' : 'secondary'}
                class={levelBtn}
                onclick={() => setIce(option)}
              >
                {option}
              </Button>
            {/each}
          </div>
        </div>
        <div class="mb-4">
          <Heading size="small" class="mb-2">{t('kiosk_sugarLevel')}</Heading>
          <div class="grid w-full grid-cols-3 gap-2">
            {#each levelOptions as option}
              <Button
                shape="round"
                color={selectedSugar === option ? 'danger' : 'secondary'}
                class={levelBtn}
                onclick={() => setSugar(option)}
              >
                {option}
              </Button>
            {/each}
          </div>
        </div>
        <div class="mb-2">
          <Heading size="small" class="mb-2">{t('kiosk_toppings')}</Heading>
          <div class="grid w-full grid-cols-3 gap-2">
            {#each toppingsList ?? [] as topping}
              <Button
                onclick={() => addTopping(topping)}
                shape="round"
                color="danger"
                disabled={validateToppingStock(topping)}
                class={levelBtn}
              >
                {topping.name}
              </Button>
            {/each}
          </div>
        </div>

        <HStack class="mt-4 w-full" gap={2}>
          <Button onclick={handleAddToOrder} shape="round" color="primary" class="w-9/10" {loading}>
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
      </div>
      <div class="mr-2 ml-4 flex w-1/3 flex-col">
        <div class="bg-level-1 mb-4 flex flex-1 flex-col overflow-y-auto rounded-xl p-3">
          <div class="flex-1">
            <Heading size="medium" class="mb-2">{item.name}</Heading>
            <Heading size="small" class="mb-2">{t('kiosk_ingredients')}</Heading>
            <div class="mb-4 gap-3 border-b pb-3 pl-4">
              {#each ingredientList as ingredient, index}
                <div class="align-items mb-1 flex w-full justify-between">
                  <Text
                    size="small"
                    class="text-muted-foreground cursor-pointer transition hover:text-red-500"
                    onclick={() => removeIngredient(index)}
                  >
                    {ingredient.name}
                  </Text>
                  <IconButton
                    onclick={() => removeIngredient(index)}
                    shape="round"
                    color="danger"
                    class="h-1/8 w-1/8"
                    icon={mdiTrashCan}
                    aria-label={t('kiosk_ingredientDelete')}
                  />
                </div>
              {/each}
            </div>
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
          </div>
          <HStack class="flex-en mt-auto flex justify-between">
            <Heading size="tiny" fontWeight="normal">{t('kiosk_itemTotal')}</Heading>
            <p>${shownPrice.toFixed(2)}</p>
          </HStack>
        </div>
      </div>
    </div>
  </ModalBody>
</Modal>
