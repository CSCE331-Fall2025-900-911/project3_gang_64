<script lang="ts">
  import { getOrderCount, getOrders } from '$lib/api/orders.remote';
  import PageStepper from '$lib/components/PageStepper.svelte';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { PaymentMethod } from '$lib/db/types';
  import { Heading, Icon, LoadingSpinner, Select, Text } from '@immich/ui';
  import { mdiCardBulleted, mdiCashMultiple } from '@mdi/js';
  import moment from 'moment';
  import { t } from '$lib/utils/utils';

  const PAGE_OPTIONS = [
    { label: '10', value: '10' },
    { label: '25', value: '25' },
    { label: '50', value: '50' },
    { label: '100', value: '100' },
  ];

  let orderPage = $state(1);
  let totalOrders = await getOrderCount();
  let pageSize = $state(PAGE_OPTIONS[1]); // Default to 25
  let totalPages = $derived(totalOrders ? Math.ceil(totalOrders / parseInt(pageSize.value)) : 0);

  let orders = $derived(getOrders({ page: orderPage - 1, limit: parseInt(pageSize.value) }));

  function getPaymentMethodIcon(method: PaymentMethod) {
    switch (method) {
      case 'cash':
        return mdiCashMultiple;
      case 'credit':
        return mdiCardBulleted;
    }
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">{t('manager_orders_title')}</Heading>

  <!-- TODO: Implement date filtering -->
  <!-- <div class="flex w-1/4 items-end justify-end gap-2">
    <Input placeholder="11/11/2025" leadingIcon={mdiCalendar} />
  </div> -->
</div>

{#if orders.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if orders.error}
  <p class="text-danger">{t('manager_orders_error_loading')}: {orders.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-3/12">{t('manager_orders_table_order_date')}</TableHeaderCell>
      <TableHeaderCell width="w-4/12" align="left">{t('manager_orders_table_customer')}</TableHeaderCell>
      <TableHeaderCell width="w-3/12">{t('manager_orders_table_payment_method')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_orders_table_total')}</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each orders.current as order}
        <TableRow>
          <TableCell width="w-3/12">{moment(order.date).format('LLLL')}</TableCell>
          <TableCell width="w-4/12" align="left">{order.customer}</TableCell>
          <TableCell width="w-3/12" class="flex items-center justify-center">
            <Icon icon={getPaymentMethodIcon(order.paymethod)} size="36" />
          </TableCell>
          <TableCell width="w-2/12">${order.total.toFixed(2)}</TableCell>
        </TableRow>
      {/each}
    </TableBody>
  </Table>
{/if}

<div class="mt-2 flex w-full items-center justify-between">
  <div class="flex w-1/3 items-center gap-2">
    <Text size="large">{t('manager_orders_per_page')}</Text>
    <Select bind:value={pageSize} data={PAGE_OPTIONS}></Select>
  </div>

  <div class="flex w-1/3 items-end justify-end gap-2">
    <PageStepper bind:currentPage={orderPage} {totalPages} />
  </div>
</div>
