<script lang="ts">
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { getIngredientsForMenuItem, getToppingIngredients } from '$lib/api/ingredient.remote';
  import type { ModalProps } from '$lib/utils/utils';
  import { Button, Modal, ModalBody, HStack, Heading, Text, Icon } from '@immich/ui';
  import { mdiTagEdit, mdiRestart } from '@mdi/js';
  import type { MenuItem, Ingredient } from '$lib/db/types';
  import { t } from '$lib/utils/utils';

  interface Props {
    item: MenuItem;
    states: { isAdded: boolean };
  }

  let { onClose, item, states }: ModalProps & Props = $props();
  let loading = $state(false);
  let currentPrice = $state(item.price);
  let shownPrice = $state(item.price);
  let ingredientList = $state(getIngredientsForMenuItem(item.id).current);
  let toppingsList = $derived(getToppingIngredients().current ?? []);
  const markup = 0.5;
  const levelOptions = ['None', 'Low', 'Normal', 'High'];
  const levelBtn = 'flex h-20 items-center justify-center text-center rounded-xl transition';

  let selectedIce = $state('Normal');
  let selectedSugar = $state('Normal');

  function setIce(option: string) {
    selectedIce = option;
  }

  function setSugar(option: string) {
    selectedSugar = option;
  }

  async function handleAddToOrder() {
    loading = true;
    currentPrice = currentPrice >= item.price ? currentPrice : item.price;
    await orderManager.addToOrder(item, ingredientList, currentPrice);
    loading = false;

    states.isAdded = true;

    onClose();
  }

  function addTopping(topping: Ingredient) {
    ingredientList!.push(topping);
    currentPrice += topping.unitPrice + markup;
    shownPrice = currentPrice >= item.price ? currentPrice : item.price;
  }

  function removeIngredient(index: number) {
    const ingredient = ingredientList![index];

    ingredientList!.splice(index, 1);
    currentPrice -= ingredient.unitPrice + markup;
    shownPrice = currentPrice >= item.price ? currentPrice : item.price;
    ingredientList = [...ingredientList!];
  }

  function restartModification() {
    ingredientList = getIngredientsForMenuItem(item.id).current;
    currentPrice = item.price;
    shownPrice = item.price;
  }
</script>

<Modal title={t('kiosk_itemModification')} icon={mdiTagEdit} {onClose}>
  <ModalBody>
    <div class="flex flex-row">
      <div class="mr-4 ml-2 flex w-7/12 flex-col">
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
