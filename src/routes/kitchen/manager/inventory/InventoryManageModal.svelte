<script lang="ts">
  import { orderIngredient, receiveIngredient } from '$lib/api/ingredient.remote';
  import type { Ingredient } from '$lib/db/types';
  import type { ModalProps } from '$lib/utils/utils';
  import { Button, Field, Heading, HStack, Modal, ModalBody, ModalFooter, NumberInput, VStack } from '@immich/ui';
  import { mdiTruck } from '@mdi/js';
  import { t } from '$lib/utils/utils';

  interface Props extends ModalProps {
    ingredient: Ingredient;
  }

  let { ingredient, onClose }: Props = $props();

  let orderStock = $state(ingredient.orderStock);
  let currentStock = $state(ingredient.currentStock);

  let orderField = $state(0);
  let receiveField = $state(0);
  let orderFieldValid = $derived(orderField > 0);
  let receiveFieldValid = $derived(receiveField > 0 && receiveField <= orderStock);

  let placingOrder = $state(false);
  let receivingInventory = $state(false);

  async function receiveInventory() {
    receivingInventory = true;
    const result = await receiveIngredient({
      id: ingredient.id,
      receiveQuantity: receiveField,
    });

    receiveField = 0;

    orderStock = result.orderStock;
    currentStock = result.currentStock;
    receivingInventory = false;
  }

  async function orderInventory() {
    placingOrder = true;
    const result = await orderIngredient({
      id: ingredient.id,
      orderQuantity: orderField,
    });

    orderField = 0;

    orderStock = result.orderStock;
    currentStock = result.currentStock;
    placingOrder = false;
  }
</script>

<Modal title={t('manager_inventory_manage_title')} icon={mdiTruck} {onClose}>
  <ModalBody>
    <HStack gap={4} class="w-full justify-center">
      <VStack gap={2} class="w-1/2 items-center">
        <Heading class="text-left">{t('manager_inventory_current_stock')}</Heading>
        <Heading class="text-center" fontWeight="normal">{currentStock}</Heading>
      </VStack>
      <div class="h-16 border-l"></div>
      <VStack gap={2} class="w-1/2 items-center">
        <Heading class="text-left">{t('manager_inventory_on_order_stock')}</Heading>
        <Heading class="text-center" fontWeight="normal">{orderStock}</Heading>
      </VStack>
    </HStack>
    <div class="my-4 w-100 border-l"></div>
    <VStack gap={4} class="w-full">
      <Field label={t('manager_inventory_receive_label')}>
        <HStack gap={4} class="w-full items-start">
          <NumberInput placeholder={'0'} bind:value={receiveField} min={0} max={orderStock}></NumberInput>
          <Button
            shape="round"
            color="success"
            class="mt-8"
            disabled={!receiveFieldValid}
            onclick={receiveInventory}
            loading={receivingInventory}
          >
            {t('manager_inventory_receive_btn')}
          </Button>
        </HStack>
      </Field>
      <Field label={t('manager_inventory_order_label')}>
        <HStack gap={4} class="w-full items-start">
          <NumberInput placeholder={'0'} bind:value={orderField} min={0}></NumberInput>
          <Button
            shape="round"
            color="success"
            class="mt-8"
            disabled={!orderFieldValid}
            onclick={orderInventory}
            loading={placingOrder}
          >
            {t('manager_inventory_place_order_btn')}
          </Button>
        </HStack>
      </Field>
    </VStack>
  </ModalBody>
  <ModalFooter>
    <Button onclick={onClose} shape="round" color="primary" fullWidth>{t('manager_inventory_close_btn')}</Button>
  </ModalFooter>
</Modal>
