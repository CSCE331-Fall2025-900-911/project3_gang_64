<script lang="ts">
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { Button, Field, HStack, Input, Modal, ModalBody, ModalFooter, Stack, Text } from '@immich/ui';
  import { mdiInvoiceSend } from '@mdi/js';

  let { onClose }: ModalProps = $props();

  const isValid = $derived(
    orderManager.customerName.trim().length > 0 && orderManager.currentOrder.length > 0 && orderManager.paymentMethod,
  );

  const handleSubmit = () => {
    orderManager.submit();
    onClose();
  };
</script>

<Modal title="Submit Order" icon={mdiInvoiceSend} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder="John Doe" bind:value={orderManager.customerName} />
      </Field>
      <Field label="Email">
        <Input placeholder="john.doe@example.com" bind:value={orderManager.customerEmail} />
      </Field>
      <Text>Payment Method</Text>
      <HStack gap={4}>
        <Button
          class="w-full"
          color={orderManager.paymentMethod === 'cash' ? 'primary' : 'secondary'}
          onclick={() => (orderManager.paymentMethod = 'cash')}
          size="large"
        >
          Cash
        </Button>
        <Button
          class="w-full"
          color={orderManager.paymentMethod === 'credit' ? 'primary' : 'secondary'}
          onclick={() => (orderManager.paymentMethod = 'credit')}
          size="large"
        >
          Credit
        </Button>
      </HStack>
    </Stack>
  </ModalBody>
  <ModalFooter>
    <div class="grid w-full grid-cols-1 gap-2">
      <Button onclick={handleSubmit} shape="round" color="primary" disabled={!isValid} size="large">Create</Button>
    </div>
  </ModalFooter>
</Modal>
