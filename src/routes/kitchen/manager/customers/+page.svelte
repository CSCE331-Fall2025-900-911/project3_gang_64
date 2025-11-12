<script lang="ts">
  import { getCustomerCount, getCustomers } from '$lib/api/customer.remote';
  import PageStepper from '$lib/components/PageStepper.svelte';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import { Heading, HStack, IconButton, Input, LoadingSpinner, Select, Text } from '@immich/ui';
  import { mdiMagnify } from '@mdi/js';

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

  let searchField = $state('');
  let searchState = $state('');

  let customers = $derived(getCustomers({ page: customerPage, limit: parseInt(pageSize.value), search: searchState }));

  function searchCustomers() {
    searchState = searchField;
    customerPage = 1;
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">Customers</Heading>

  <div class="flex w-1/4 items-end justify-end gap-2">
    <HStack gap={2}>
      <Input
        placeholder="Search customers..."
        bind:value={searchField}
        onkeydown={(e) => e.key === 'Enter' && searchCustomers()}
      />
      <IconButton icon={mdiMagnify} aria-label="Search" onclick={searchCustomers} />
    </HStack>
  </div>
</div>

{#if customers.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if customers.error}
  <p class="text-danger">Error loading customers: {customers.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-1/3">Customer Name</TableHeaderCell>
      <TableHeaderCell width="w-2/3">Email</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each customers.current as customer}
        <TableRow>
          <TableCell width="w-1/3">{customer.name}</TableCell>
          <TableCell width="w-2/3">{customer.email}</TableCell>
        </TableRow>
      {/each}
    </TableBody>
  </Table>
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
