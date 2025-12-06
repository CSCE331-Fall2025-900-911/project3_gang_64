<script lang="ts">
  import { Card, CardBody, CardHeader, CardTitle, Heading, Text, Label } from '@immich/ui';
  import { t } from '$lib/utils/utils';
  import { getLastZTime, getAllZReportData } from '$lib/api/zreport.remote';
  import { td } from '$lib/contexts/translations.svelte';

  // Get the last Z report time once
  let lastZTime = $state(await getLastZTime());

  // Fetch all Z report data in a single optimized query
  let zReportData = $state(await getAllZReportData(lastZTime));
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
      <Text class="mb-4">{t('manager_reports_z_info')}</Text>

      <div class="mt-4 grid grid-cols-2 gap-4">
        <Label class="text-base font-bold">Total Net Sales:</Label>
        <Label class="text-base font-bold">${zReportData.totalNetSales.toFixed(2)}</Label>

        <Label class="text-base font-bold">Tax:</Label>
        <Label class="text-base font-bold">${zReportData.totalTax.toFixed(2)}</Label>

        <Label class="text-base font-bold">Total Sales:</Label>
        <Label class="text-base font-bold">${zReportData.totalSales.toFixed(2)}</Label>

        <Label class="text-base font-bold">Cash:</Label>
        <Label class="text-base font-bold">${zReportData.cashSales.toFixed(2)}</Label>

        <Label class="text-base font-bold">Credit:</Label>
        <Label class="text-base font-bold">${zReportData.creditSales.toFixed(2)}</Label>
      </div>

      <div class="mt-6">
        <Label class="block text-center text-base font-bold">Sales Categories</Label>
        <div class="mt-4 grid grid-cols-2 gap-4">
          {#each zReportData.categorySubtotals as { category, totalSubtotal }}
            <Label class="text-base">{td(category)}:</Label>
            <Label class="text-base">${totalSubtotal.toFixed(2)}</Label>
          {/each}
        </div>
      </div></CardBody
    >
  </Card>
</div>
