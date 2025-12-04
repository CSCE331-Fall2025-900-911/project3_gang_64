<script lang="ts">
  import OrderSummary from '$lib/components/OrderSummary.svelte';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { Modal, ModalBody, modalManager } from '@immich/ui';
  import { mdiCart } from '@mdi/js';
  import OrderSubmitDialog from '../../kitchen/cashier/OrderSubmitDialog.svelte';

  function showSubmitDialog() {
    modalManager.show(OrderSubmitDialog, { isCashier: false });
  }

  let { onClose }: ModalProps = $props();
</script>

<Modal size="large" {onClose} title="Cart" icon={mdiCart}>
  <ModalBody>
    <div class="flex h-full min-h-[80vh] flex-col">
      <OrderSummary
        entries={orderManager.currentOrder}
        subtotal={orderManager.subtotal}
        tax={orderManager.tax}
        total={orderManager.total}
        editable={true}
        {showSubmitDialog}
        onUpdateQuantity={(i, value) => orderManager.updateQuantity(i, value)}
        onRemoveEntry={(i) => orderManager.removeFromOrder(i)}
      />
    </div>
  </ModalBody>
</Modal>
