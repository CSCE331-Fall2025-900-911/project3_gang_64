<script lang="ts">
  import { getOrders } from '$lib/api/orders.remote';
  import { getDayOrderCount, getDayRevenue } from '$lib/api/reports.remote';
  import DashboardCard from '$lib/components/DashboardCard.svelte';
  import type { PaymentMethod } from '$lib/db/types';
  import { Heading, Icon, LoadingSpinner } from '@immich/ui';
  import { mdiCardBulleted, mdiCashMultiple, mdiCloudOutline, mdiCurrencyUsd, mdiShoppingOutline } from '@mdi/js';
  import moment from 'moment';
  import { cubicInOut } from 'svelte/easing';
  import { fade } from 'svelte/transition';

  let dailyOrders = getDayOrderCount(moment().toDate());

  let dailyRevenue = getDayRevenue(moment().toDate());
  let lastWeekRevenue = getDayRevenue(moment().subtract(7, 'days').toDate());
  let revenuePercentageChange = $derived(
    dailyRevenue.ready && lastWeekRevenue.ready
      ? ((dailyRevenue.current - lastWeekRevenue.current) / lastWeekRevenue.current) * 100
      : undefined,
  );

  let orders = $derived(getOrders({ page: 0, limit: 10 }));

  function getPaymentMethodIcon(method: PaymentMethod) {
    switch (method) {
      case 'cash':
        return mdiCashMultiple;
      case 'credit':
        return mdiCardBulleted;
    }
  }
</script>

<Heading size="large" class="mt-2 mb-6">Dashboard</Heading>

<div class="flex flex-row gap-4">
  <!-- Total Sales Card -->
  <DashboardCard
    title="Total Sales"
    value={`$${dailyRevenue.current?.toFixed(2)}`}
    percentChange={revenuePercentageChange}
    icon={mdiCurrencyUsd}
    loading={dailyRevenue.loading || lastWeekRevenue.loading}
    error={dailyRevenue.error?.message}
  />

  <!-- Total Orders Card -->
  <!-- TODO: Implement percentage calculation -->
  <DashboardCard title="Total Orders" value={dailyOrders.current} percentChange={-2.89} icon={mdiShoppingOutline} />

  <!-- Total Visitors Card -->
  <DashboardCard title="Weather" value={'67 °F'} icon={mdiCloudOutline} />
</div>

<div class="my-6">
  <Heading size="medium">Recent Orders</Heading>
  {#if orders.loading}
    <div class="flex justify-center">
      <LoadingSpinner size="large" />
    </div>
  {:else if orders.error}
    <p class="text-danger">Error loading orders: {orders.error.message}</p>
  {:else}
    <table class="mt-4 w-full text-start">
      <thead class="mb-4 flex h-12 w-full rounded-md border bg-subtle">
        <tr class="flex w-full place-items-center text-center text-sm font-medium">
          <th class="w-3/12">Order Date</th>
          <th class="w-4/12 text-left">Customer</th>
          <th class="w-3/12">Payment Method</th>
          <th class="w-2/12">Total</th>
        </tr>
      </thead>
      <tbody class="dark:border-immich-dark-gray block w-full overflow-y-auto rounded-md border">
        {#each orders.current as order}
          <tr
            transition:fade={{ duration: 400, easing: cubicInOut }}
            class="dark:text-immich-dark-fg flex w-full place-items-center py-2 text-center odd:bg-subtle/80 even:bg-subtle/20"
          >
            <td class="w-3/12">{order.date}</td>
            <td class="w-4/12 text-left">{order.customer}</td>
            <td class="flex w-3/12 items-center justify-center">
              <Icon icon={getPaymentMethodIcon(order.paymethod)} size="36" />
            </td>
            <td class="w-2/12">${order.total.toFixed(2)}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  {/if}
</div>
