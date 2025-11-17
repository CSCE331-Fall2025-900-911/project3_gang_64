<script lang="ts">
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { AppShell, Button, Heading, HStack, IconButton, modalManager, Text } from '@immich/ui';
  import { mdiTrashCanOutline } from '@mdi/js';
  import OrderSubmitDialog from './KioskOrderSubmit.svelte';

  function showSubmitDialog() {
    modalManager.show(OrderSubmitDialog);
  }

  function removeItem(index: number) {
    orderManager.removeFromOrder(index);
  }

  function duplicateItem(index: number) {
    orderManager.duplicateOrderEntry(index);
  }
</script>

<AppShell>
  <div class="flex flex-col overflow-hidden" style="height: 80vh;">
    <div class="bg-level-1 mt-4 mr-80 ml-80 flex flex-1 flex-col overflow-y-auto rounded-xl p-3">
      {#if orderManager.currentOrder.length == 0}
        <Text class="pt-6 text-center">No items in order</Text>
      {/if}

      {#each orderManager.currentOrder as entry, i}
        <div class="mb-2 flex justify-between border-b pb-2">
          <div>
            <Heading size="small">{entry.menuItem.name}</Heading>
            <div class="gap-3 pl-4">
              {#each entry.ingredients as ingredient}
                <Text size="small" class="text-muted-foreground">
                  {ingredient.name}
                </Text>
              {/each}
            </div>
          </div>
          <div class="flex justify-between gap-4">
            <div class="flex flex-col justify-center">
              <Button onclick={duplicateItem.bind(null, i)}>Duplicate Item</Button>
            </div>

            <div class="flex flex-col justify-center">
              <IconButton
                icon={mdiTrashCanOutline}
                shape="round"
                size="medium"
                color="primary"
                onclick={removeItem.bind(null, i)}
                aria-label={'Remove Item'}
              />
            </div>
            <div class="flex flex-col items-end">
              <Text size="small">${entry.menuItem.price.toFixed(2)}</Text>
            </div>
          </div>
        </div>
      {/each}
    </div>

    <div class="m-4 mr-80 ml-80 shrink-0 gap-2">
      <HStack class="flex justify-between">
        <Heading size="tiny" fontWeight="normal">Subtotal</Heading>
        <p>${orderManager.subtotal.toFixed(2)}</p>
      </HStack>
      <HStack class="flex justify-between">
        <Heading size="tiny" fontWeight="normal">Tax</Heading>
        <p>${orderManager.tax.toFixed(2)}</p>
      </HStack>
      <HStack class="mt-2 flex justify-between">
        <Heading size="small">Total</Heading>
        <p>${orderManager.total.toFixed(2)}</p>
      </HStack>
      <Button class="mt-4 w-full" color="success" onclick={showSubmitDialog} disabled={!orderManager.isValidOrder}
        >Submit Order</Button
      >
    </div>
  </div>
</AppShell>
