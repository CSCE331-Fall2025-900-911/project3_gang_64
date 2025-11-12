<script lang="ts">
  import { fetchCurrentWeather, type CurrentWeatherParams } from '$lib/api/openweather.remote';
  import { getOrders } from '$lib/api/orders.remote';
  import { getDayOrderCount, getDayRevenue } from '$lib/api/reports.remote';
  import DashboardCard from '$lib/components/DashboardCard.svelte';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { PaymentMethod } from '$lib/db/types';
  import { Heading, Icon, LoadingSpinner } from '@immich/ui';
  import {
    mdiCardBulleted,
    mdiCashMultiple,
    mdiCurrencyUsd,
    mdiShoppingOutline,
    mdiTimerSand,
    mdiWeatherCloudy,
    mdiWeatherFog,
    mdiWeatherLightning,
    mdiWeatherPartlyCloudy,
    mdiWeatherRainy,
    mdiWeatherSnowy,
    mdiWeatherSunny,
  } from '@mdi/js';
  import moment from 'moment';
  import { onMount } from 'svelte';

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

  let WEATHER_LOCATION = {
    lat: 30.628,
    lon: -96.334,
    units: 'imperial' as const,
  } satisfies CurrentWeatherParams;

  const iconMap: Record<string, string> = {
    '01d': mdiWeatherSunny,
    '02d': mdiWeatherPartlyCloudy,
    '03d': mdiWeatherCloudy,
    '04d': mdiWeatherCloudy,
    '09d': mdiWeatherRainy,
    '10d': mdiWeatherRainy,
    '11d': mdiWeatherLightning,
    '13d': mdiWeatherSnowy,
    '50d': mdiWeatherFog,
    default: mdiTimerSand,
  };

  const weatherIconPath = $derived.by(() => {
    if (weatherQuery.loading) {
      return iconMap.default;
    }

    const iconCode = weatherData?.weather?.[0]?.icon;

    if (iconCode && iconMap[iconCode]) {
      return iconMap[iconCode];
    }

    return iconMap.default;
  });

  let weatherQuery = $derived(fetchCurrentWeather(WEATHER_LOCATION));

  const weatherData = $derived.by(() => weatherQuery.current);

  function refreshWeather() {
    weatherQuery.refresh();
  }

  onMount(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          WEATHER_LOCATION = {
            ...WEATHER_LOCATION,
            lat: position.coords.latitude,
            lon: position.coords.longitude,
          };
          refreshWeather();
        },
        (error) => {
          console.error('Geolocation error:', error.message);
          refreshWeather();
        },
      );
    } else {
      console.error('Geolocation is not supported by this browser.');
      refreshWeather();
    }
  });
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
  <DashboardCard
    title="Weather"
    loading={weatherQuery.loading}
    value={weatherData?.main.temp ?? '—'}
    icon={weatherIconPath}
  />
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
    <Table>
      <TableHeader>
        <TableHeaderCell width="w-3/12">Order Date</TableHeaderCell>
        <TableHeaderCell width="w-4/12" align="left">Customer</TableHeaderCell>
        <TableHeaderCell width="w-3/12">Payment Method</TableHeaderCell>
        <TableHeaderCell width="w-2/12">Total</TableHeaderCell>
      </TableHeader>
      <TableBody>
        {#each orders.current as order}
          <TableRow>
            <TableCell width="w-3/12">{order.date}</TableCell>
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
