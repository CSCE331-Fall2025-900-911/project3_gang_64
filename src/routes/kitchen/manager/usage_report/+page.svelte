<script lang="ts">
  import { getInventoryUsageForDay } from '$lib/api/reports.remote';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import { td } from '$lib/contexts/translations.svelte';
  import { t } from '$lib/utils/utils';
  import { DatePicker, Heading, LoadingSpinner } from '@immich/ui';
  import { DateTime } from 'luxon';

  let dateFilter = $state<DateTime | undefined>(DateTime.now());

  let usageData = $derived(dateFilter ? getInventoryUsageForDay(dateFilter) : undefined);
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">{t('manager_inventory_usage_title')}</Heading>

  <div class="flex w-1/4 items-end justify-end gap-2">
    <DatePicker bind:value={dateFilter} maxDate={DateTime.now()} />
  </div>
</div>

{#if usageData?.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if usageData?.error}
  <p class="text-danger">{t('manager_inventory_usage_error')}: {usageData.error.message}</p>
{:else if usageData?.current}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-4/12">{t('manager_inventory_usage_table_name')}</TableHeaderCell>
      <TableHeaderCell width="w-4/12">{t('manager_inventory_usage_table_category')}</TableHeaderCell>
      <TableHeaderCell width="w-4/12">{t('manager_inventory_usage_table_usage')}</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each usageData.current as item}
        <TableRow>
          <TableCell width="w-4/12" align="left" class="pl-6">{td(item.ingredientName)}</TableCell>
          <TableCell width="w-4/12">{td(item.ingredientCategory)}</TableCell>
          <TableCell width="w-4/12">{item.usageCount}</TableCell>
        </TableRow>
      {/each}
      {#if usageData.current.length === 0}
        <TableRow>
          <TableCell width="w-full" class="text-center">{t('manager_inventory_usage_no_data')}</TableCell>
        </TableRow>
      {/if}
    </TableBody>
  </Table>
{/if}
