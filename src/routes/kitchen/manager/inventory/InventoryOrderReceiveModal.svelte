<script lang="ts">
  import type { Ingredient } from '$lib/db/types';
  import type { ModalProps } from '$lib/utils/utils';
  import {
    Button,
    Field,
    Heading,
    HelperText,
    HStack,
    Modal,
    ModalBody,
    ModalFooter,
    NumberInput,
    VStack,
  } from '@immich/ui';
  import { mdiTruck } from '@mdi/js';

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

  function receiveInventory() {
    currentStock += receiveField;
    orderStock -= receiveField;
    receiveField = 0;

    // TODO: make api calls
  }

  function orderInventory() {
    orderStock += orderField;
    orderField = 0;
    // TODO: make api calls
  }
</script>

<Modal title="Manage Inventory" icon={mdiTruck} {onClose}>
  <ModalBody>
    <HStack gap={4} class="w-full justify-center">
      <VStack gap={2} class="w-1/2 items-center">
        <Heading class="text-left">Current Stock</Heading>
        <Heading class="text-center" fontWeight="normal">{currentStock}</Heading>
      </VStack>
      <div class="h-16 border-l"></div>
      <VStack gap={2} class="w-1/2 items-center">
        <Heading class="text-left">On Order Stock</Heading>
        <Heading class="text-center" fontWeight="normal">{orderStock}</Heading>
      </VStack>
    </HStack>
    <div class="my-4 w-100 border-l"></div>
    <VStack gap={4} class="w-full">
      <Field label="Receive Inventory">
        <HStack gap={4} class="w-full items-start">
          <NumberInput placeholder={'0'} bind:value={receiveField}></NumberInput>
          {#if receiveField > orderStock}
            <HelperText color="danger">Cannot receive more than on order stock</HelperText>
          {/if}
          <Button shape="round" color="success" class="mt-8" disabled={!receiveFieldValid} onclick={receiveInventory}>
            Receive
          </Button>
        </HStack>
      </Field>
      <Field label="Order Inventory">
        <HStack gap={4} class="w-full items-start">
          <NumberInput placeholder={'0'} bind:value={orderField}></NumberInput>
          <Button shape="round" color="success" class="mt-8" disabled={!orderFieldValid} onclick={orderInventory}>
            Place Order
          </Button>
        </HStack>
      </Field>
    </VStack>
  </ModalBody>
  <ModalFooter>
    <Button onclick={onClose} shape="round" color="primary" fullWidth>Close</Button>
  </ModalFooter>
</Modal>
