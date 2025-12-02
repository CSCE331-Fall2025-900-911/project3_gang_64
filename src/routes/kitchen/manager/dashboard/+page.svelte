<script lang="ts">
  import { fetchCurrentWeather } from '$lib/api/openweather.remote';
  import { getOrders } from '$lib/api/orders.remote';
  import { getDayOrderCount, getDayRevenue } from '$lib/api/reports.remote';
  import DashboardCard from '$lib/components/DashboardCard.svelte';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { PaymentMethod } from '$lib/db/types';
  import { t } from '$lib/utils/utils';
  import { getWeatherIcon, WEATHER_LOCATION } from '$lib/utils/weather';
  import { Heading, Icon, LoadingSpinner } from '@immich/ui';
  import { mdiCardBulleted, mdiCashMultiple, mdiCurrencyUsd, mdiShoppingOutline } from '@mdi/js';
  import { DateTime } from 'luxon';

  let dailyOrders = getDayOrderCount(DateTime.now());
  let lastWeekOrders = getDayOrderCount(DateTime.now().minus({ days: 7 }));
  let ordersPercentageChange = $derived(
    dailyOrders.ready && lastWeekOrders.ready
      ? ((dailyOrders.current - lastWeekOrders.current) / (lastWeekOrders.current || 1)) * 100
      : undefined,
  );

  let dailyRevenue = getDayRevenue(DateTime.now());
  let lastWeekRevenue = getDayRevenue(DateTime.now().minus({ days: 7 }));
  let revenuePercentageChange = $derived(
    dailyRevenue.ready && lastWeekRevenue.ready
      ? ((dailyRevenue.current - lastWeekRevenue.current) / (lastWeekRevenue.current || 1)) * 100
      : undefined,
  );

  let orders = $derived(getOrders({ limit: 10 }));

  function getPaymentMethodIcon(method: PaymentMethod) {
    switch (method) {
      case 'cash':
        return mdiCashMultiple;
      case 'credit':
        return mdiCardBulleted;
    }
  }

  let weatherQuery = $derived(fetchCurrentWeather(WEATHER_LOCATION));
  let weatherIcon = $derived(getWeatherIcon(weatherQuery.current));
</script>

<Heading size="large" class="mt-2 mb-6">{t('manager_dashboard_title')}</Heading>

<div class="flex flex-row gap-4">
  <!-- Total Sales Card -->
  <DashboardCard
    title={t('manager_dashboard_total_sales')}
    value={`$${dailyRevenue.current?.toFixed(2)}`}
    percentChange={revenuePercentageChange}
    icon={mdiCurrencyUsd}
    loading={dailyRevenue.loading || lastWeekRevenue.loading}
    error={dailyRevenue.error?.message}
  />

  <!-- Total Orders Card -->
  <DashboardCard
    title={t('manager_dashboard_total_orders')}
    value={dailyOrders.current}
    percentChange={ordersPercentageChange}
    icon={mdiShoppingOutline}
  />

  <!-- Total Visitors Card -->
  <DashboardCard
    title={t('manager_dashboard_weather')}
    loading={weatherQuery.loading}
    value={`${weatherQuery.current?.main.temp.toFixed(0) ?? '—-'} °F`}
    icon={weatherIcon}
  />
</div>

<div class="my-6">
  <Heading size="medium">{t('manager_dashboard_recent_orders')}</Heading>
  {#if orders.loading}
    <div class="flex justify-center">
      <LoadingSpinner size="large" />
    </div>
  {:else if orders.error}
    <p class="text-danger">{t('manager_dashboard_error_loading_orders')}: {orders.error.message}</p>
  {:else}
    <Table>
      <TableHeader>
        <TableHeaderCell width="w-3/12">{t('manager_dashboard_table_order_date')}</TableHeaderCell>
        <TableHeaderCell width="w-4/12" align="left">{t('manager_dashboard_table_customer')}</TableHeaderCell>
        <TableHeaderCell width="w-3/12">{t('manager_dashboard_table_payment_method')}</TableHeaderCell>
        <TableHeaderCell width="w-2/12">{t('manager_dashboard_table_total')}</TableHeaderCell>
      </TableHeader>
      <TableBody>
        {#each orders.current?.orders as order}
          <TableRow>
            <TableCell width="w-3/12">{order.date.toLocaleString(DateTime.DATETIME_MED)}</TableCell>
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
</div>
