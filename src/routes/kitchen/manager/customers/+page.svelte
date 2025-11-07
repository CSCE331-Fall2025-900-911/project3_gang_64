<script lang="ts">
  import { getCustomerCount, getCustomers } from '$lib/api/customer.remote';
  import PageStepper from '$lib/components/PageStepper.svelte';
  import { Heading, Input, LoadingSpinner, Select, Text } from '@immich/ui';
  import { mdiMagnify } from '@mdi/js';
  import { cubicInOut } from 'svelte/easing';
  import { fade } from 'svelte/transition';

  const PAGE_OPTIONS = [
    { label: '10', value: '10' },
    { label: '25', value: '25' },
    { label: '50', value: '50' },
    { label: '100', value: '100' },
  ];

  let customerPage = $state(1);
  let totalCustomers = await getCustomerCount();
  let pageSize = $state(PAGE_OPTIONS[1]); // Default to 25
  let totalPages = $derived(totalCustomers ? Math.ceil(totalCustomers / parseInt(pageSize.value)) : 0);

  let customers = $derived(getCustomers({ page: customerPage, limit: parseInt(pageSize.value) }));
</script>

<div class="mb-6 flex items-center justify-between px-2">
  <Heading size="large">Customers</Heading>

  <div class="flex w-1/4 items-end justify-end gap-2">
    <Input placeholder="John Doe" leadingIcon={mdiMagnify} />
  </div>
</div>

{#if customers.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if customers.error}
  <p class="text-danger">Error loading customers: {customers.error.message}</p>
{:else}
  <table class="mt-4 w-full text-start">
    <thead class="mb-4 flex h-12 w-full rounded-md border bg-subtle">
      <tr class="flex w-full place-items-center text-center text-sm font-medium">
        <th class="w-full">Customer Name</th>
      </tr>
    </thead>
    <tbody class="dark:border-immich-dark-gray block w-full overflow-y-auto rounded-md border">
      {#each customers.current as customer}
        <tr
          transition:fade={{ duration: 400, easing: cubicInOut }}
          class="dark:text-immich-dark-fg flex w-full place-items-center py-2 text-center odd:bg-subtle/80 even:bg-subtle/20"
        >
          <td class="w-full">{customer.name}</td>
        </tr>
      {/each}
    </tbody>
  </table>
{/if}

<div class="mt-2 flex w-full items-center justify-between">
  <div class="flex w-1/3 items-center gap-2">
    <Text size="large">Customers per page</Text>
    <Select bind:value={pageSize} data={PAGE_OPTIONS}></Select>
  </div>

  <div class="flex w-1/3 items-end justify-end gap-2">
    <PageStepper bind:currentPage={customerPage} {totalPages} />
  </div>
</div>
