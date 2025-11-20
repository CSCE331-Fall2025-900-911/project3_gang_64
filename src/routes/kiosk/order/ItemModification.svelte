<script lang="ts">
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { Button, Modal, ModalBody, ModalFooter } from '@immich/ui';
  import { mdiInvoiceSend } from '@mdi/js';
  import type { MenuItem } from '$lib/db/types';
  import { t } from '$lib/utils/utils';

  interface Props {
    item: MenuItem;
    firstAddAction?: () => void;
  }

  let { onClose, item }: ModalProps & Props = $props();
  let loading = $state(false);

  async function handleAddToOrder() {
    loading = true;
    await orderManager.addToOrder(item);
    loading = false;

    onClose();
  }
</script>

<Modal title={t('kiosk_itemModification')} icon={mdiInvoiceSend} {onClose}>
  <ModalBody>
    <!-- Fill this in -->
  </ModalBody>
  <ModalFooter>
    <div class="grid w-full grid-cols-1 gap-2">
      <Button onclick={handleAddToOrder} shape="round" color="primary">{t('kiosk_addToCart')}</Button>
    </div>
  </ModalFooter>
</Modal>
