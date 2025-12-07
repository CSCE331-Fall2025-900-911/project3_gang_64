<script lang="ts">
  import { Card, CardBody, CardHeader, CardTitle, Heading, Text, Label, Button, LoadingSpinner } from '@immich/ui';
  import { Table, TableHeader, TableHeaderCell, TableBody, TableRow, TableCell } from '$lib/components/Table';
  import { t } from '$lib/utils/utils';
  import { getLastZTime, getAllZReportData, updateZTime, canRunZReport } from '$lib/api/zreport.remote';
  import { getXReportData } from '$lib/api/xreport.remote';
  import { td } from '$lib/contexts/translations.svelte';

  let lastZTime = $state<any>();
  let zReportData = $state<any>();
  let xReportData = $state<any[]>([]);
  let isLoadingZ = $state(true);
  let isLoadingX = $state(true);
  let canRun = $state(false);
  let hasGenerated = $state(false);
  let zReportRunToday = $state(false);

  const clientTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

  (async () => {
    canRun = await canRunZReport();
    isLoadingZ = false;
  })();

  (async () => {
    xReportData = await getXReportData(clientTimezone);
    isLoadingX = false;
  })();

  async function generateZReport() {
    if (!canRun || hasGenerated) return;
    isLoadingZ = true;
    lastZTime = await getLastZTime();
    zReportData = await getAllZReportData(lastZTime);
    await updateZTime();
    await getLastZTime().refresh();
    hasGenerated = true;
    canRun = false;
    isLoadingZ = false;
  }

  function formatHour(hour: number): string {
    if (hour === 0) return '12:00 AM';
    if (hour < 12) return `${hour}:00 AM`;
    if (hour === 12) return '12:00 PM';
    return `${hour - 12}:00 PM`;
  }
</script>

<Heading size="large" class="mt-2 mb-6">{t('manager_reports_title')}</Heading>

<div class="mt-4 flex flex-col gap-4">
  <Card expandable>
    <CardHeader>
      <CardTitle>{t('manager_reports_x_title')}</CardTitle>
    </CardHeader>
    <CardBody>
      {#if isLoadingX}
        <div class="flex items-center justify-center py-8">
          <LoadingSpinner size="large" />
        </div>
      {:else}
        <div class="w-full overflow-x-auto">
          <Table class="min-w-[700px]">
            <TableHeader>
              <TableHeaderCell width="flex-[1_1_100px] min-w-[80px]"
                >{t('manager_reports_x_hour_of_day')}</TableHeaderCell
              >
              <TableHeaderCell width="flex-[1_1_100px] min-w-[80px]">{t('manager_reports_x_sales')}</TableHeaderCell>
              <TableHeaderCell width="flex-[1_1_80px] min-w-[60px]">{t('manager_reports_x_cash')}</TableHeaderCell>
              <TableHeaderCell width="flex-[1_1_80px] min-w-[60px]">{t('manager_reports_x_credit')}</TableHeaderCell>
              <TableHeaderCell width="flex-[1_1_100px] min-w-[80px]"
                >{t('manager_reports_x_tax_collected')}</TableHeaderCell
              >
              <TableHeaderCell width="flex-[1_1_120px] min-w-[100px]"
                >{t('manager_reports_x_avg_items_per_order')}</TableHeaderCell
              >
              <TableHeaderCell width="flex-[1_1_110px] min-w-[90px]"
                >{t('manager_reports_x_avg_order_total')}</TableHeaderCell
              >
            </TableHeader>
            <TableBody class="max-h-[400px]">
              {#each xReportData as row}
                <TableRow>
                  <TableCell width="flex-[1_1_100px] min-w-[80px]">{formatHour(row.hour)}</TableCell>
                  <TableCell width="flex-[1_1_100px] min-w-[80px]">${row.sales.toFixed(2)}</TableCell>
                  <TableCell width="flex-[1_1_80px] min-w-[60px]">{row.cashCount}</TableCell>
                  <TableCell width="flex-[1_1_80px] min-w-[60px]">{row.creditCount}</TableCell>
                  <TableCell width="flex-[1_1_100px] min-w-[80px]">${row.taxCollected.toFixed(2)}</TableCell>
                  <TableCell width="flex-[1_1_120px] min-w-[100px]">{row.avgItemsPerOrder.toFixed(2)}</TableCell>
                  <TableCell width="flex-[1_1_110px] min-w-[90px]">${row.avgOrderTotal.toFixed(2)}</TableCell>
                </TableRow>
              {/each}
            </TableBody>
          </Table>
        </div>
      {/if}
    </CardBody>
  </Card>

  <Card expandable>
    <CardHeader>
      <CardTitle>{t('manager_reports_z_title')}</CardTitle>
    </CardHeader>
    <CardBody>
      <Text class="mb-4 text-base font-bold">{t('manager_reports_z_info')}</Text>

      {#if isLoadingZ}
        <div class="flex items-center justify-center py-8">
          <LoadingSpinner size="large" />
        </div>
      {:else if !hasGenerated}
        <div class="flex flex-col items-center justify-center gap-4 py-8">
          {#if canRun}
            <Button class="w-full" color="primary" onclick={generateZReport}
              >{t('manager_reports_z_generate_button')}</Button
            >
          {:else}
            <Text class="text-center">{t('manager_reports_z_already_generated')}</Text>
          {/if}
        </div>
      {:else}
        <div class="mt-4 grid grid-cols-2 gap-4">
          <Label class="text-base">{t('manager_reports_z_total_net_sales')}:</Label>
          <Label class="text-base">${zReportData.totalNetSales.toFixed(2)}</Label>

          <Label class="text-base">{t('manager_reports_z_tax')}:</Label>
          <Label class="text-base">${zReportData.totalTax.toFixed(2)}</Label>

          <Label class="text-base">{t('manager_reports_z_total_sales')}:</Label>
          <Label class="text-base">${zReportData.totalSales.toFixed(2)}</Label>

          <Label class="text-base">{t('manager_reports_z_cash')}:</Label>
          <Label class="text-base">${zReportData.cashSales.toFixed(2)}</Label>

          <Label class="text-base">{t('manager_reports_z_credit')}:</Label>
          <Label class="text-base">${zReportData.creditSales.toFixed(2)}</Label>
        </div>

        <div class="mt-6">
          <Label class="block text-center text-base font-bold">{t('manager_reports_z_sales_categories')}</Label>
          <div class="mt-4 grid grid-cols-2 gap-4">
            {#each zReportData.categorySubtotals as { category, totalSubtotal }}
              <Label class="text-base">{td(category)}:</Label>
              <Label class="text-base">${totalSubtotal.toFixed(2)}</Label>
            {/each}
          </div>
        </div>
      {/if}</CardBody
    >
  </Card>
</div>
