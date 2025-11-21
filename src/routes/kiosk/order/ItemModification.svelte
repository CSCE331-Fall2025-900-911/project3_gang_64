<script lang="ts">
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { getIngredientsForMenuItem, getToppingIngredients } from '$lib/api/ingredient.remote';
  import type { ModalProps } from '$lib/utils/utils';
  import { Button, Modal, ModalBody, HStack, Heading, Text, Icon, toastManager } from '@immich/ui';
  import { mdiTagEdit, mdiRestart } from '@mdi/js';
  import type { MenuItem, Ingredient } from '$lib/db/types';
  import { t } from '$lib/utils/utils';
  import ItemModDeleteToast from './ItemModDeleteToast.svelte';
  import ItemModAddToast from './ItemModAddToast.svelte';

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
    if (hasTopping) {
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
    currentPrice -= ingredient.unitPrice + markup;
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
</script>

<Modal title={t('kiosk_itemModification')} icon={mdiTagEdit} {onClose}>
  <ModalBody>
    <div class="flex flex-row">
      <div class="mr-4 ml-2 flex w-7/12 flex-col">
        <div class="mb-4">
          <Heading size="small" class="mb-2">Base Items:</Heading>
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
          <Heading size="small" class="mb-2">Ice Level:</Heading>
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
          <Heading size="small" class="mb-2">Sugar Level:</Heading>
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
          <Heading size="small" class="mb-2">Toppings:</Heading>
          <div class="grid w-full grid-cols-3 gap-2">
            {#each toppingsList ?? [] as topping}
              <Button onclick={() => addTopping(topping)} shape="round" color="danger" class={levelBtn}>
                {topping.name}
              </Button>
            {/each}
          </div>
        </div>

        <div class="mt-2 flex h-12 w-full flex-row items-center">
          <Button onclick={handleAddToOrder} shape="round" color="primary" class="m-2 h-full w-9/10">
            {t('kiosk_addToCart')}
          </Button>
          <Button
            onclick={restartModification}
            shape="round"
            color="secondary"
            class="flex h-full w-3/20 items-center justify-center"
          >
            <Icon icon={mdiRestart} class="h-full w-full object-contain" />
          </Button>
        </div>
      </div>
      <div class="mr-2 ml-4 flex w-1/3 flex-col">
        <div class="bg-level-1 mb-4 flex flex-1 flex-col overflow-y-auto rounded-xl p-3">
          <div>
            <Heading size="small">{item.name}</Heading>
            <div class="gap-3 pl-4">
              {#each ingredientList as ingredient, index}
                <Text
                  size="small"
                  class="text-muted-foreground cursor-pointer transition hover:text-red-500"
                  onclick={() => removeIngredient(index)}
                >
                  {ingredient.name}
                </Text>
              {/each}
            </div>
          </div>
        </div>

        <div class="shrink-0 gap-2">
          <HStack class="flex justify-between">
            <Heading size="tiny" fontWeight="normal">{t('kiosk_itemTotal')}</Heading>
            <p>${shownPrice.toFixed(2)}</p>
          </HStack>
        </div>
      </div>
    </div>
  </ModalBody>
</Modal>
