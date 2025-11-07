<script lang="ts">
  import { getOrderCount, getOrders } from '$lib/api/orders.remote';
  import PageStepper from '$lib/components/PageStepper.svelte';
  import type { PaymentMethod } from '$lib/db/types';
  import { Heading, Icon, Input, LoadingSpinner, Select, Text } from '@immich/ui';
  import { mdiCalendar, mdiCardBulleted, mdiCashMultiple } from '@mdi/js';
  import { cubicInOut } from 'svelte/easing';
  import { fade } from 'svelte/transition';

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

  let orders = $derived(getOrders({ page: orderPage, limit: parseInt(pageSize.value) }));

  function getPaymentMethodIcon(method: PaymentMethod) {
    switch (method) {
      case 'cash':
        return mdiCashMultiple;
      case 'credit':
        return mdiCardBulleted;
    }
  }
</script>

<div class="mb-6 flex items-center justify-between px-2">
  <Heading size="large">Orders</Heading>

  <div class="flex w-1/4 items-end justify-end gap-2">
    <Input placeholder="11/11/2025" leadingIcon={mdiCalendar} />
  </div>
</div>

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

<div class="mt-2 flex w-full items-center justify-between">
  <div class="flex w-1/3 items-center gap-2">
    <Text size="large">Orders per page</Text>
    <Select bind:value={pageSize} data={PAGE_OPTIONS}></Select>
  </div>

  <div class="flex w-1/3 items-end justify-end gap-2">
    <PageStepper bind:currentPage={orderPage} {totalPages} />
  </div>
</div>
