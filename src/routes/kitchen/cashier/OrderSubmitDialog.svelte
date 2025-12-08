<script lang="ts">
  import OrderNumberModal from '$lib/components/OrderNumberModal.svelte';
  import { orderManager } from '$lib/managers/order_manager.svelte';
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import { Button, Field, HStack, Input, Modal, ModalBody, ModalFooter, modalManager, Stack, Text } from '@immich/ui';
  import { mdiInvoiceSend } from '@mdi/js';

  interface Props extends ModalProps {
    isCashier: boolean;
  }

  let { onClose, isCashier }: Props = $props();

  let isValidEmail = $derived.by(() => {
    const email = orderManager.customerEmail.trim();
    if (email.length === 0) {
      return false;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  });

  const isValid = $derived(
    isValidEmail &&
      orderManager.customerName.trim().length > 0 &&
      orderManager.currentOrder.length > 0 &&
      orderManager.paymentMethod,
  );
  let submittingOrder = $state(false);

  const handleSubmit = async () => {
    submittingOrder = true;
    await orderManager.submit(isCashier);
    submittingOrder = false;

    await modalManager.show(OrderNumberModal, {
      title: 'Order Submitted Successfully!',
      description: isCashier ? t('order_number') : t('kiosk_orderNumber'),
      number: (Math.floor(Math.random() * 100) + 1).toString(),
    });

    onClose();
    if (!isCashier) {
      window.location.href = '/kiosk/home';
    }
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
        {#if orderManager.customerEmail.trim().length > 0 && !isValidEmail}
          <Text color="danger" size="small">{t('order_invalid_email')}</Text>
        {/if}
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
    <Button fullWidth onclick={handleSubmit} shape="round" color="primary" disabled={!isValid} loading={submittingOrder}
      >{t('order_create')}</Button
    >
  </ModalFooter>
</Modal>
