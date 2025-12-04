<script lang="ts">
  import { getCustomerDetails } from '$lib/api/customer.remote';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { PaymentMethod } from '$lib/db/types';
  import type { ModalProps } from '$lib/utils/utils';
  import { t } from '$lib/utils/utils';
  import { Heading, Icon, IconButton, LoadingSpinner, Modal, ModalBody, modalManager, Stack, Text } from '@immich/ui';
  import { mdiAccount, mdiCardBulleted, mdiCashMultiple, mdiEye } from '@mdi/js';
  import { DateTime } from 'luxon';
  import OrderDetailModal from '../orders/OrderDetailModal.svelte';

  interface Props extends ModalProps {
    customerId: string;
  }

  let { onClose, customerId }: Props = $props();

  const customerDetails = $derived(getCustomerDetails(customerId));

  function getPaymentMethodIcon(method: PaymentMethod) {
    switch (method) {
      case 'cash':
        return mdiCashMultiple;
      case 'credit':
        return mdiCardBulleted;
    }
  }

  function formatDate(date: DateTime) {
    return date.toLocaleString(DateTime.DATETIME_MED);
  }

  function formatCurrency(amount: number) {
    return `$${amount.toFixed(2)}`;
  }

  function showOrderDetails(orderId: string) {
    modalManager.show(OrderDetailModal, { orderId });
  }
</script>

<Modal title={t('manager_customers_detail_title')} icon={mdiAccount} {onClose} size="giant">
  <ModalBody>
    {#if customerDetails.loading}
      <div class="flex justify-center py-8">
        <LoadingSpinner size="large" />
      </div>
    {:else if customerDetails.error}
      <Text class="text-danger">{t('manager_customers_detail_error')}: {customerDetails.error.message}</Text>
    {:else if customerDetails.current}
      {@const customer = customerDetails.current}
      <Stack gap={4}>
        <!-- Customer Info -->
        <div class="bg-level-1 rounded-lg p-4">
          <Heading size="small">{t('manager_customers_detail_info')}</Heading>
          <div class="mt-2 grid grid-cols-2 gap-2">
            <Text class="text-muted-foreground">{t('manager_customers_table_name')}:</Text>
            <Text>{customer.name}</Text>
            <Text class="text-muted-foreground">{t('manager_customers_table_email')}:</Text>
            <Text>{customer.email}</Text>
            <Text class="text-muted-foreground">{t('manager_customers_detail_order_count')}:</Text>
            <Text>{customer.orderCount}</Text>
          </div>
        </div>

        <!-- Orders Table -->
        <div>
          <Heading size="small" class="mb-2">{t('manager_customers_detail_orders')}</Heading>
          {#if customer.orders.length === 0}
            <Text class="text-muted-foreground">{t('manager_customers_detail_no_orders')}</Text>
          {:else}
            <Table>
              <TableHeader>
                <TableHeaderCell width="w-3/12">{t('manager_orders_table_order_date')}</TableHeaderCell>
                <TableHeaderCell width="w-2/12">{t('manager_orders_table_total')}</TableHeaderCell>
                <TableHeaderCell width="w-2/12">{t('manager_orders_table_items')}</TableHeaderCell>
                <TableHeaderCell width="w-3/12">{t('manager_orders_table_payment_method')}</TableHeaderCell>
                <TableHeaderCell width="w-2/12">{t('manager_orders_table_actions')}</TableHeaderCell>
              </TableHeader>
              <TableBody>
                {#each customer.orders as order}
                  <TableRow>
                    <TableCell width="w-3/12">{formatDate(order.date)}</TableCell>
                    <TableCell width="w-2/12">{formatCurrency(order.total)}</TableCell>
                    <TableCell width="w-2/12">{order.itemQuantity}</TableCell>
                    <TableCell width="w-3/12" class="flex items-center justify-center">
                      <Icon icon={getPaymentMethodIcon(order.paymentMethod)} size="36" />
                    </TableCell>
                    <TableCell width="w-2/12" class="flex justify-center">
                      <IconButton
                        icon={mdiEye}
                        aria-label={t('manager_orders_view_details_aria')}
                        onclick={() => showOrderDetails(order.id)}
                      />
                    </TableCell>
                  </TableRow>
                {/each}
              </TableBody>
            </Table>
          {/if}
        </div>
      </Stack>
    {/if}
  </ModalBody>
</Modal>
