<script lang="ts">
  import { cashierManager } from '$lib/managers/cashier.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { Button, Field, HStack, Input, Modal, ModalBody, ModalFooter, Stack, Text } from '@immich/ui';
  import { mdiInvoiceSend } from '@mdi/js';

  let { onClose }: ModalProps = $props();

  let valid = $derived(
    cashierManager.customerName.trim().length > 0 &&
      cashierManager.currentOrder.length > 0 &&
      cashierManager.paymentMethod,
  );

  function submitOrder() {
    cashierManager.submit();
    onClose();
  }
</script>

<Modal title="Submit Order" icon={mdiInvoiceSend} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder="John Doe" bind:value={cashierManager.customerName} />
      </Field>
      <Text>Payment Method</Text>
      <HStack gap={4}>
        <Button
          class="h-20 flex-1"
          color={cashierManager.paymentMethod === 'cash' ? 'primary' : 'secondary'}
          onclick={() => (cashierManager.paymentMethod = 'cash')}
        >
          Cash
        </Button>
        <Button
          class="h-20 flex-1"
          color={cashierManager.paymentMethod === 'credit' ? 'primary' : 'secondary'}
          onclick={() => (cashierManager.paymentMethod = 'credit')}
        >
          Credit Card
        </Button>
      </HStack>
    </Stack>
  </ModalBody>
  <ModalFooter>
    <div class="grid w-full grid-cols-1 gap-2">
      <Button onclick={submitOrder} shape="round" color="primary" disabled={!valid}>Create</Button>
    </div>
  </ModalFooter>
</Modal>
