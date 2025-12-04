<script lang="ts">
  import { getOrders } from '$lib/api/orders.remote';
  import PageStepper from '$lib/components/PageStepper.svelte';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { PaymentMethod } from '$lib/db/types';
  import { t } from '$lib/utils/utils';
  import { DatePicker, Heading, Icon, IconButton, LoadingSpinner, modalManager, Select, Text } from '@immich/ui';
  import { mdiCardBulleted, mdiCashMultiple, mdiEye } from '@mdi/js';
  import { DateTime } from 'luxon';
  import OrderDetailModal from './OrderDetailModal.svelte';

  const PAGE_OPTIONS = [
    { label: '10', value: '10' },
    { label: '25', value: '25' },
    { label: '50', value: '50' },
    { label: '100', value: '100' },
  ];

  let dateFilter = $state<DateTime | undefined>(DateTime.now());

  let orderPage = $state(1);
  let pageSize = $state(PAGE_OPTIONS[1]); // Default to 25

  let ordersData = $derived(
    getOrders({
      page: orderPage - 1,
      limit: parseInt(pageSize.value),
      date: dateFilter,
    }),
  );

  let orders = $derived(ordersData.current?.orders || []);
  let totalPages = $derived(ordersData.current?.totalPages || 0);

  function getPaymentMethodIcon(method: PaymentMethod) {
    switch (method) {
      case 'cash':
        return mdiCashMultiple;
      case 'credit':
        return mdiCardBulleted;
    }
  }

  function showOrderDetails(orderId: string) {
    modalManager.show(OrderDetailModal, { orderId });
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">{t('manager_orders_title')}</Heading>

  <div class="flex w-1/4 items-end justify-end gap-2">
    <DatePicker bind:value={dateFilter} maxDate={DateTime.now()} />
  </div>
</div>

{#if ordersData.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if ordersData.error}
  <p class="text-danger">{t('manager_orders_error_loading')}: {ordersData.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-3/12">{t('manager_orders_table_order_date')}</TableHeaderCell>
      <TableHeaderCell width="w-3/12" align="left">{t('manager_orders_table_customer')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_orders_table_payment_method')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_orders_table_total')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_orders_table_actions')}</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each orders as order}
        <TableRow>
          <TableCell width="w-3/12">{order.date.toLocaleString(DateTime.DATETIME_MED)}</TableCell>
          <TableCell width="w-3/12" align="left">{order.customer}</TableCell>
          <TableCell width="w-2/12" class="flex items-center justify-center">
            <Icon icon={getPaymentMethodIcon(order.paymethod)} size="36" />
          </TableCell>
          <TableCell width="w-2/12">${order.total.toFixed(2)}</TableCell>
          <TableCell width="w-2/12" class="flex justify-center">
            <IconButton
              icon={mdiEye}
              aria-label={t('manager_orders_view_details_aria')}
              onclick={() => showOrderDetails(order.id)}
            />
          </TableCell>
        </TableRow>
      {/each}
      {#if orders?.length === 0}
        <TableRow>
          <TableCell width="w-full" class="text-center">{t('manager_orders_no_orders')}</TableCell>
        </TableRow>
      {/if}
    </TableBody>
  </Table>
{/if}

<div class="mt-2 flex w-full items-center justify-between">
  <div class="flex w-1/3 items-center gap-2">
    <Text size="large">{t('manager_orders_per_page')}</Text>
    <Select bind:value={pageSize} data={PAGE_OPTIONS}></Select>
  </div>

  {#if totalPages !== 0}
    <div class="flex w-1/3 items-end justify-end gap-2">
      <PageStepper bind:currentPage={orderPage} {totalPages} />
    </div>
  {/if}
</div>
