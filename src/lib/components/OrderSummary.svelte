<script lang="ts">
  import { td } from '$lib/contexts/translations.svelte';
  import type { OrderEntry } from '$lib/managers/order_manager.types';
  import type { Ingredient } from '$lib/db/types';
  import { t } from '$lib/utils/utils';
  import { Button, Heading, HStack, IconButton, Stack, Text, modalManager, toastManager } from '@immich/ui';
  import { mdiPencil, mdiTrashCan } from '@mdi/js';
  import NumberStepper from './NumberStepper.svelte';
  import ItemModificationModal from '../../routes/kiosk/order/ItemModificationModal.svelte';
  import ItemModEditToast from '../../routes/kiosk/order/ItemModEditToast.svelte';

  interface Props {
    entries: OrderEntry[];
    subtotal: number;
    tax: number;
    total: number;
    editable?: boolean;
    showSubmitButton?: boolean;
    showSubmitDialog?: () => void;
    onUpdateQuantity?: (index: number, quantity: number) => void;
    onRemoveEntry?: (index: number) => void;
  }

  let {
    entries,
    subtotal,
    tax,
    total,
    editable = true,
    showSubmitButton = true,
    showSubmitDialog,
    onUpdateQuantity,
    onRemoveEntry,
  }: Props = $props();

  const isValidOrder = $derived(entries.length > 0);
  let loading = $state(false);

  // Group ingredients by id and count duplicates
  function groupIngredients(
    ingredients: { id: string; name: string }[],
  ): { id: string; name: string; count: number }[] {
    const counts = new Map<string, { id: string; name: string; count: number }>();
    for (const ing of ingredients) {
      if (counts.has(ing.id)) {
        counts.get(ing.id)!.count++;
      } else {
        counts.set(ing.id, { id: ing.id, name: ing.name, count: 1 });
      }
    }
    return Array.from(counts.values());
  }

  async function showEditDialog(entry: OrderEntry, index: number) {
    loading = true;
    const originalQuantity = entry.quantity;
    const states = { isAdded: false };
    await modalManager.show(ItemModificationModal, {
      item: entry.menuItem,
      currentIngredientList: entry.ingredients,
      currentIceLevel: entry.iceLevel,
      currentSugarLevel: entry.sugarLevel,
      currentSizeLevel: entry.sizeLevel,
      currentCartPrice: entry.subtotal,
      quantity: entry.quantity,
      isEdit: true,
      isCashier: entry.isCashier,
      states,
    });

    if (states.isAdded) {
      entry.quantity -= originalQuantity;
      if (entry.quantity == 0) {
        onRemoveEntry?.(index);
      }

      loading = false;

      toastManager.custom(
        { component: ItemModEditToast, props: { isEdited: true } },
        { timeout: 5000, closable: true },
      );
    } else {
      loading = false;

      toastManager.custom(
        { component: ItemModEditToast, props: { isEdited: false } },
        { timeout: 5000, closable: true },
      );
    }
  }

  function outOfStock(ingList: Ingredient[], quantity: number): boolean {
    for (const ing of ingList) {
      const amountUsed = ingList.filter((i) => i.id === ing.id).length;
      const required = amountUsed * quantity + amountUsed;
      if (required > ing.currentStock) {
        return true;
      }
    }

    return false;
  }

  function getSizeLabel(size: 'Small' | 'Medium' | 'Large' | 'Extra Large' | undefined): string {
    switch (size) {
      case 'Small':
        return '(S)';
      case 'Medium':
        return '(M)';
      case 'Large':
        return '(L)';
      case 'Extra Large':
        return '(XL)';
      default:
        return '(S)';
    }
  }
</script>

<!-- Order Summary -->
<div class="flex h-full w-full flex-col">
  <div class="bg-level-1 mb-4 flex flex-1 flex-col overflow-y-auto rounded-xl p-3">
    {#if entries.length == 0}
      <Text class="pt-2 text-center">{t('cart_noItems')}</Text>
    {/if}

    {#if !loading}
      {#each entries as entry, i}
        <div class="mb-2 flex justify-between border-b pb-2">
          <div>
            <Heading size="small">{td(entry.menuItem.name)} {getSizeLabel(entry.sizeLevel)}</Heading>
            <div class="gap-3 pl-4">
              {#each groupIngredients(entry.ingredients) as ingredient}
                <Text size="small" class="text-muted-foreground">
                  {td(ingredient.name)}
                  {#if ingredient.count > 1}
                    (x{ingredient.count}){/if}
                </Text>
              {/each}
            </div>
          </div>
          <Stack align="end" gap={2}>
            <Text size="large">${(entry.subtotal * entry.quantity).toFixed(2)}</Text>
            {#if editable && onUpdateQuantity}
              {@const max = outOfStock(entry.ingredients, entry.quantity) ? -Infinity : Infinity}
              <NumberStepper value={entry.quantity} min={1} {max} onChange={(value) => onUpdateQuantity(i, value)} />
              <HStack gap={2}>
                <IconButton
                  icon={mdiPencil}
                  size="medium"
                  color="primary"
                  onclick={() => showEditDialog(entry, i)}
                  aria-label={t('cart_editItem')}
                />
                {#if onRemoveEntry}
                  <IconButton
                    icon={mdiTrashCan}
                    size="medium"
                    color="danger"
                    onclick={() => onRemoveEntry(i)}
                    aria-label={t('cart_removeItem')}
                  />
                {/if}
              </HStack>
            {:else if !editable}
              {#if entry.quantity > 1}
                <Text size="small" class="text-muted-foreground">x{entry.quantity}</Text>
              {/if}
            {/if}
          </Stack>
        </div>
      {/each}
    {/if}
  </div>

  <!-- Order Summary -->
  <div class="shrink-0 gap-2">
    <HStack class="flex justify-between">
      <Heading size="tiny" fontWeight="normal">{t('cart_subtotal')}</Heading>
      <p>${subtotal.toFixed(2)}</p>
    </HStack>
    <HStack class="flex justify-between">
      <Heading size="tiny" fontWeight="normal">{t('cart_tax')}</Heading>
      <p>${tax.toFixed(2)}</p>
    </HStack>
    <HStack class="mt-2 flex justify-between">
      <Heading size="small">{t('cart_total')}</Heading>
      <p>${total.toFixed(2)}</p>
    </HStack>
    {#if showSubmitButton && showSubmitDialog}
      <Button class="mt-4 w-full" color="success" onclick={showSubmitDialog} disabled={!isValidOrder}
        >{t('cart_submitOrder')}</Button
      >
    {/if}
  </div>
</div>
