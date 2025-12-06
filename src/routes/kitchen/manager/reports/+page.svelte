<script lang="ts">
  import { Card, CardBody, CardHeader, CardTitle, Heading, Text, Label, Button, LoadingSpinner } from '@immich/ui';
  import { t } from '$lib/utils/utils';
  import { getLastZTime, getAllZReportData, updateZTime, canRunZReport } from '$lib/api/zreport.remote';
  import { td } from '$lib/contexts/translations.svelte';

  let lastZTime = $state<any>();
  let zReportData = $state<any>();
  let isLoading = $state(true);
  let canRun = $state(false);
  let hasGenerated = $state(false);

  (async () => {
    canRun = await canRunZReport();
    isLoading = false;
  })();

  async function generateZReport() {
    if (!canRun || hasGenerated) return;
    isLoading = true;
    lastZTime = await getLastZTime();
    zReportData = await getAllZReportData(lastZTime);
    await updateZTime();
    await getLastZTime().refresh();
    hasGenerated = true;
    canRun = false;
    isLoading = false;
  }
</script>

<Heading size="large" class="mt-2 mb-6">{t('manager_reports_title')}</Heading>

<div class="mt-4 flex flex-col gap-4">
  <Card expandable>
    <CardHeader>
      <CardTitle>{t('manager_reports_x_title')}</CardTitle>
    </CardHeader>
    <CardBody>
      <Text>{t('manager_reports_x_info')}</Text>
    </CardBody>
  </Card>

  <Card expandable>
    <CardHeader>
      <CardTitle>{t('manager_reports_z_title')}</CardTitle>
    </CardHeader>
    <CardBody>
      <Text class="mb-4 text-base font-bold">{t('manager_reports_z_info')}</Text>

      {#if isLoading}
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
