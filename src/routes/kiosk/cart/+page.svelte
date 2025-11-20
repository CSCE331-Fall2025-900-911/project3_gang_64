<script lang="ts">
  import { goto } from '$app/navigation';
  import OrderSummary from '$lib/components/OrderSummary.svelte';
  import { Button, modalManager, Stack, Text } from '@immich/ui';
  import { mdiArrowLeft } from '@mdi/js';
  import OrderSubmitDialog from '../../kitchen/cashier/OrderSubmitDialog.svelte';

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

<!-- 
<div class="flex h-full w-full justify-center">
  <Text class="text-3xl font-bold">Your Cart</Text>
  
</div> -->

<div class="flex h-full w-full justify-center p-6">
  <Stack class="w-1/2" gap={2}>
    <Button
      leadingIcon={mdiArrowLeft}
      onclick={() => goto('/kiosk/order')}
      variant="ghost"
      class="mb-2 self-start p-0"
      color="secondary"
      size="small"
    >
      Back to Ordering
    </Button>
    <Text class="w-full text-3xl font-bold">Your Cart</Text>
    <div class="flex h-full w-full rounded-3xl border p-2">
      <OrderSummary {showSubmitDialog} />
    </div>
  </Stack>
</div>
