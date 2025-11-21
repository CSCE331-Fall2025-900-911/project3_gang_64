<script lang="ts">
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { t } from '$lib/utils/utils';
  import { Button, Heading, HStack, IconButton, Stack, Text } from '@immich/ui';
  import { mdiPencil, mdiTrashCan } from '@mdi/js';
  import NumberStepper from './NumberStepper.svelte';

  interface Props {
    showSubmitDialog: () => void;
  }
  let { showSubmitDialog }: Props = $props();
</script>

<!-- Order Summary -->
<div class="flex h-full w-full flex-col">
  <div class="bg-level-1 mb-4 flex flex-1 flex-col overflow-y-auto rounded-xl p-3">
    {#if orderManager.currentOrder.length == 0}
      <Text class="pt-6 text-center">{t('cart_noItems')}</Text>
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
        <Stack align="end" gap={2}>
          <Text size="large">${(entry.subtotal * entry.quantity).toFixed(2)}</Text>
          <NumberStepper value={entry.quantity} min={1} onChange={(value) => orderManager.updateQuantity(i, value)} />
          <HStack gap={2}>
            <IconButton
              icon={mdiPencil}
              size="medium"
              color="primary"
              onclick={() => alert('TODO: Edit functionality not yet implemented')}
              aria-label={t('cart_editItem')}
            />
            <IconButton
              icon={mdiTrashCan}
              size="medium"
              color="danger"
              onclick={() => orderManager.removeFromOrder(i)}
              aria-label={t('cart_removeItem')}
            />
          </HStack>
        </Stack>
      </div>
    {/each}
  </div>

  <!-- Order Summary -->
  <div class="shrink-0 gap-2">
    <HStack class="flex justify-between">
      <Heading size="tiny" fontWeight="normal">{t('cart_subtotal')}</Heading>
      <p>${orderManager.subtotal.toFixed(2)}</p>
    </HStack>
    <HStack class="flex justify-between">
      <Heading size="tiny" fontWeight="normal">{t('cart_tax')}</Heading>
      <p>${orderManager.tax.toFixed(2)}</p>
    </HStack>
    <HStack class="mt-2 flex justify-between">
      <Heading size="small">{t('cart_total')}</Heading>
      <p>${orderManager.total.toFixed(2)}</p>
    </HStack>
    <Button class="mt-4 w-full" color="success" onclick={showSubmitDialog} disabled={!orderManager.isValidOrder}
      >{t('cart_submitOrder')}</Button
    >
  </div>
</div>
