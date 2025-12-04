<script lang="ts">
  import { getOrderDetails } from '$lib/api/orders.remote';
  import OrderSummary from '$lib/components/OrderSummary.svelte';
  import type { PaymentMethod } from '$lib/db/types';
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import { Heading, HStack, Icon, LoadingSpinner, Modal, ModalBody, Stack, Text } from '@immich/ui';
  import { mdiCardBulleted, mdiCashMultiple, mdiReceipt } from '@mdi/js';
  import { DateTime } from 'luxon';

  interface Props extends ModalProps {
    orderId: string;
  }

  let { onClose, orderId }: Props = $props();

  const orderDetails = $derived(getOrderDetails(orderId));

  function getPaymentMethodIcon(method: PaymentMethod) {
    switch (method) {
      case 'cash':
        return mdiCashMultiple;
      case 'credit':
        return mdiCardBulleted;
    }
  }

  // Transform order entries to match OrderEntry type expected by OrderSummary
  const orderEntries = $derived(
    orderDetails.current?.entries.map((entry) => ({
      menuItem: {
        ...entry.menuItem,
        category: '',
        imageUrl: null,
        archived: false,
      },
      ingredients: entry.ingredients.map((ing) => ({
        ...ing,
        currentStock: 0,
        orderStock: 0,
        category: '',
        unitPrice: 0,
        calories: 0,
        fat_g: 0,
        sodium_g: 0,
        carbs_g: 0,
        sugar_g: 0,
        caffiene_mg: 0,
        allergen: [],
      })),
      quantity: entry.quantity,
      subtotal: entry.menuItem.price,
      iceLevel: 'Normal' as const,
      sugarLevel: 'Normal' as const,
    })) || [],
  );
</script>

<Modal title={t('manager_orders_detail_title')} icon={mdiReceipt} {onClose} size="large">
  <ModalBody>
    {#if orderDetails.loading}
      <div class="flex justify-center py-8">
        <LoadingSpinner size="large" />
      </div>
    {:else if orderDetails.error}
      <Text class="text-danger">{t('manager_orders_detail_error')}: {orderDetails.error.message}</Text>
    {:else if orderDetails.current}
      {@const order = orderDetails.current}
      <Stack gap={4}>
        <!-- Customer Info -->
        <div class="bg-level-1 rounded-lg p-4">
          <Heading size="small">{t('manager_orders_detail_customer_info')}</Heading>
          <div class="mt-2 grid grid-cols-2 gap-2">
            <Text class="text-muted-foreground">{t('manager_orders_table_customer')}:</Text>
            <Text>{order.customerName}</Text>
            <Text class="text-muted-foreground">{t('email')}:</Text>
            <Text>{order.customerEmail}</Text>
            <Text class="text-muted-foreground">{t('manager_orders_table_order_date')}:</Text>
            <Text>{order.date.toLocaleString(DateTime.DATETIME_MED)}</Text>
            <Text class="text-muted-foreground">{t('manager_orders_table_payment_method')}:</Text>
            <HStack gap={2}>
              <Icon icon={getPaymentMethodIcon(order.paymentMethod)} size="24" />
              <Text>{t(`order_payment_${order.paymentMethod}`)}</Text>
            </HStack>
          </div>
        </div>

        <!-- Order Items using OrderSummary -->
        <OrderSummary
          entries={orderEntries}
          subtotal={order.subtotal}
          tax={order.tax}
          total={order.total}
          editable={false}
          showSubmitButton={false}
        />
      </Stack>
    {/if}
  </ModalBody>
</Modal>
