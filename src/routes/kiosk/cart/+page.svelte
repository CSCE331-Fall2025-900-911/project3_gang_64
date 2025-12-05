<script lang="ts">
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { AppShell, Button, Heading, HStack, IconButton, modalManager, Text } from '@immich/ui';
  import { mdiTrashCanOutline } from '@mdi/js';
  import OrderSubmitDialog from '../../kitchen/cashier/OrderSubmitDialog.svelte';
  import { t } from '$lib/utils/utils';
  import { derived } from 'svelte/store';
  import { onMount } from 'svelte';
  import {goto} from '$app/navigation';

  const timeOutLength = 6;
  let timer = $derived(timeOutLength);
  let countDown: ReturnType<typeof setInterval>;

  function showSubmitDialog() {
    modalManager.show(OrderSubmitDialog);
  }

  function removeItem(index: number) {
    orderManager.removeFromOrder(index);
  }

  function duplicateItem(index: number) {
    orderManager.duplicateOrderEntry(index);
  }

  const resetTimer = () => {
    timer = timeOutLength;
  }

  const listenerSetup = () => {
    const events = ["mousemove", "keydown", "click", "touchstart"];
    events.forEach((ev) => window.addEventListener(ev, resetTimer));

    return () => events.forEach((ev) => window.removeEventListener(ev, resetTimer));
  }

  onMount(() => {
    const listeners = listenerSetup();

    countDown = setInterval(()=> {
      --timer;
      if (timer <= 0) {
        clearInterval(countDown);
        orderManager.clearOrder();
        //goto('/kiosk/home');
      }
    }, 1000);

    return () => {
      listeners();
      clearInterval(countDown);
    }
  });

</script>

<AppShell>
  <div class="flex flex-col overflow-hidden" style="height: 80vh;">
    <div class="bg-level-1 mt-4 mr-80 ml-80 flex flex-1 flex-col overflow-y-auto rounded-xl p-3">
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
          <div class="flex justify-between gap-4">
            <div class="flex flex-col justify-center">
              <Button onclick={duplicateItem.bind(null, i)}>{t('cart_duplicateItem')}</Button>
            </div>

            <div class="flex flex-col justify-center">
              <IconButton
                icon={mdiTrashCanOutline}
                shape="round"
                size="medium"
                color="primary"
                onclick={removeItem.bind(null, i)}
                aria-label={t('cart_removeItem')}
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
</AppShell>
