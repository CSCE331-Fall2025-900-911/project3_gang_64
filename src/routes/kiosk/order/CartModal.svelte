<script lang="ts">
  import OrderSummary from '$lib/components/OrderSummary.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { Modal, ModalBody, modalManager } from '@immich/ui';
  import { mdiCart } from '@mdi/js';
  import OrderSubmitDialog from '../../kitchen/cashier/OrderSubmitDialog.svelte';

  function showSubmitDialog() {
    modalManager.show(OrderSubmitDialog);
  }

  let { onClose }: ModalProps = $props();
</script>

<Modal size="large" {onClose} title="Cart" icon={mdiCart}>
  <ModalBody>
    <div class="flex h-full min-h-[80vh] flex-col">
      <OrderSummary {showSubmitDialog} />
    </div>
  </ModalBody>
</Modal>
