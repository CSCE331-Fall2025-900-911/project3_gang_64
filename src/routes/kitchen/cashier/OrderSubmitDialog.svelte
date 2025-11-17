<script lang="ts">
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { Button, Field, HStack, Input, Modal, ModalBody, ModalFooter, Stack, Text } from '@immich/ui';
  import { mdiInvoiceSend } from '@mdi/js';
  import { t } from '$lib/utils/utils';

  let { onClose }: ModalProps = $props();

  const isValid = $derived(
    orderManager.customerName.trim().length > 0 && orderManager.currentOrder.length > 0 && orderManager.paymentMethod,
  );

  const handleSubmit = () => {
    orderManager.submit();
    onClose();
  };
</script>

<Modal title={t('order_submitOrder')} icon={mdiInvoiceSend} {onClose}>
  <ModalBody>
    <Stack gap={4}>
      <Field label={t('order_label_name')}>
        <Input placeholder={t('order_placeholder_name')} bind:value={orderManager.customerName} />
      </Field>
      <Field label={t('order_label_email')}>
        <Input placeholder={t('order_placeholder_email')} bind:value={orderManager.customerEmail} />
      </Field>
      <Text>{t('order_paymentMethod')}</Text>
      <HStack gap={4}>
        <Button
          class="w-full"
          color={orderManager.paymentMethod === 'cash' ? 'primary' : 'secondary'}
          onclick={() => (orderManager.paymentMethod = 'cash')}
          size="large"
        >
          {t('order_payment_cash')}
        </Button>
        <Button
          class="w-full"
          color={orderManager.paymentMethod === 'credit' ? 'primary' : 'secondary'}
          onclick={() => (orderManager.paymentMethod = 'credit')}
          size="large"
        >
          {t('order_payment_credit')}
        </Button>
      </HStack>
    </Stack>
  </ModalBody>
  <ModalFooter>
    <div class="grid w-full grid-cols-1 gap-2">
      <Button onclick={handleSubmit} shape="round" color="primary" disabled={!isValid}>{t('order_create')}</Button>
    </div>
  </ModalFooter>
</Modal>
