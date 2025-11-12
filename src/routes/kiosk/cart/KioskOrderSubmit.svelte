<script lang="ts">
  import { kioskManager } from '$lib/managers/kiosk.svelte';
  import type { ModalProps } from '$lib/utils';
  import { Button, Field, HStack, Input, Modal, ModalBody, ModalFooter, Stack, Text } from '@immich/ui';
  import { mdiInvoiceSend } from '@mdi/js';

  let { onClose }: ModalProps = $props();

  let valid = $derived(
    kioskManager.customerName.trim().length > 0 && kioskManager.currentOrder.length > 0 && kioskManager.paymentMethod,
  );

  function submitOrder() {
    kioskManager.submit();
    onClose();
  }
</script>

<Modal title="Submit Order" icon={mdiInvoiceSend} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label="Name">
        <Input placeholder="John Doe" bind:value={kioskManager.customerName} />
      </Field>
      <Text>Payment Method</Text>
      <HStack gap={4}>
        <Button
          class="h-20 flex-1"
          color={kioskManager.paymentMethod === 'cash' ? 'primary' : 'secondary'}
          onclick={() => (kioskManager.paymentMethod = 'cash')}
        >
          Cash
        </Button>
        <Button
          class="h-20 flex-1"
          color={kioskManager.paymentMethod === 'credit' ? 'primary' : 'secondary'}
          onclick={() => (kioskManager.paymentMethod = 'credit')}
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
