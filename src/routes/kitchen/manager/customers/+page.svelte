<script lang="ts">
  import { getCustomers } from '$lib/api/customer.remote';
  import PageStepper from '$lib/components/PageStepper.svelte';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import { t } from '$lib/utils/utils';
  import { Heading, HStack, IconButton, Input, LoadingSpinner, modalManager, Select, Text } from '@immich/ui';
  import { mdiEye, mdiMagnify } from '@mdi/js';
  import CustomerDetailModal from './CustomerDetailModal.svelte';

  const PAGE_OPTIONS = [
    { label: '10', value: '10' },
    { label: '25', value: '25' },
    { label: '50', value: '50' },
    { label: '100', value: '100' },
  ];

  let customerPage = $state(1);
  let pageSize = $state(PAGE_OPTIONS[1]); // Default to 25

  let searchField = $state('');
  let searchState = $state('');

  let customersData = $derived(
    getCustomers({ page: customerPage - 1, limit: parseInt(pageSize.value), search: searchState }),
  );

  let customers = $derived(customersData.current?.customers || []);
  let totalPages = $derived(customersData.current?.totalPages || 0);

  function searchCustomers() {
    searchState = searchField;
    customerPage = 1;
  }

  function showCustomerDetail(customerId: string) {
    modalManager.show(CustomerDetailModal, { customerId });
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">{t('manager_customers_title')}</Heading>

  <div class="flex w-1/4 items-end justify-end gap-2">
    <HStack gap={2}>
      <Input
        placeholder={t('manager_customers_search_placeholder')}
        bind:value={searchField}
        onkeydown={(e) => e.key === 'Enter' && searchCustomers()}
      />
      <IconButton icon={mdiMagnify} aria-label={t('manager_customers_search_aria')} onclick={searchCustomers} />
    </HStack>
  </div>
</div>

{#if customersData.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if customersData.error}
  <p class="text-danger">{t('manager_customers_error_loading')}: {customersData.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-4/12">{t('manager_customers_table_name')}</TableHeaderCell>
      <TableHeaderCell width="w-6/12" align="left">{t('manager_customers_table_email')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_orders_table_actions')}</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each customers as customer}
        <TableRow>
          <TableCell width="w-4/12">{customer.name}</TableCell>
          <TableCell width="w-6/12" align="left">{customer.email}</TableCell>
          <TableCell width="w-2/12" class="flex justify-center">
            <IconButton
              icon={mdiEye}
              aria-label={t('manager_customers_view_details_aria')}
              onclick={() => showCustomerDetail(customer.id)}
            />
          </TableCell>
        </TableRow>
      {/each}
      {#if customers.length === 0}
        <TableRow>
          <TableCell width="w-full" class="text-center">
            {t('manager_customers_no_results')}
          </TableCell>
        </TableRow>
      {/if}
    </TableBody>
  </Table>
{/if}

<div class="mt-2 flex w-full items-center justify-between">
  <div class="flex w-1/3 items-center gap-2">
    <Text size="large">{t('manager_customers_per_page')}</Text>
    <Select bind:value={pageSize} data={PAGE_OPTIONS}></Select>
  </div>

  {#if totalPages !== 0}
    <div class="flex w-1/3 items-end justify-end gap-2">
      <PageStepper bind:currentPage={customerPage} {totalPages} />
    </div>
  {/if}
</div>
