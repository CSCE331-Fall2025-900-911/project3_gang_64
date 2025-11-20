<script lang="ts">
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import { getIngredientsForMenuItem } from '$lib/api/ingredient.remote';
  import type { ModalProps } from '$lib/utils/utils';
  import { Button, Modal, ModalBody, ModalFooter, HStack, Heading, IconButton, Text } from '@immich/ui';
  import NumberStepper from '$lib/components/NumberStepper.svelte';
  import { mdiInvoiceSend, mdiPencil, mdiTrashCan } from '@mdi/js';
  import type { MenuItem } from '$lib/db/types';
  import { t } from '$lib/utils/utils';

  interface Props {
    item: MenuItem;
    states: { isAdded: boolean };
  }

  let { onClose, item, states }: ModalProps & Props = $props();
  let loading = $state(false);
  let currentPrice = $state(item.price);
  let ingredientList = $state(getIngredientsForMenuItem(item.id).current);

  async function handleAddToOrder() {
    loading = true;
    await orderManager.addToOrder(item);
    loading = false;

    states.isAdded = true;

    onClose();
  }

  function cancelItem() {
    states.isAdded = false;

    onClose();
  }
</script>

<Modal title={t('kiosk_itemModification')} icon={mdiInvoiceSend} {onClose}>
  <ModalBody>
    <div class="m-6 flex w-1/3 flex-col">
      <div class="bg-level-1 mb-4 flex flex-1 flex-col overflow-y-auto rounded-xl p-3">
        <div>
          <Heading size="small">{item.name}</Heading>
          <div class="gap-3 pl-4">
            {#each ingredientList as ingredient}
              <Text size="small" class="text-muted-foreground">
                {ingredient.name}
              </Text>
            {/each}
          </div>
        </div>
      </div>

      <div class="shrink-0 gap-2">
        <HStack class="flex justify-between">
          <Heading size="tiny" fontWeight="normal">{t('kiosk_itemTotal')}</Heading>
          <p>${currentPrice.toFixed(2)}</p>
        </HStack>
      </div>
    </div>
  </ModalBody>
  <ModalFooter>
    <div class="grid w-full grid-cols-1 gap-2">
      <Button onclick={cancelItem} shape="round" color="danger">{t('kiosk_cancelItem')}</Button>
      <Button onclick={handleAddToOrder} shape="round" color="primary">{t('kiosk_addToCart')}</Button>
    </div>
  </ModalFooter>
</Modal>
