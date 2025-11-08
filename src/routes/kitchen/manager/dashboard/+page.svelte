<script lang='ts'>
  import { Icon, LoadingSpinner } from "@immich/ui";
  import {mdiWeatherHurricane} from "@mdi/js";
  import {getOrderCountDay , getDailyRevenue, getOrders} from '$lib/api/orders.remote'
  import { cubicInOut } from 'svelte/easing';
  import { fade } from 'svelte/transition';
  import { mdiCalendar, mdiCardBulleted, mdiCashMultiple } from '@mdi/js';
  import type { PaymentMethod } from '$lib/db/types';
  import { number } from "valibot";


  let dailyOrders = getOrderCountDay();
  let dailyRevenue = getDailyRevenue();
  //weather place holders
  let temp = 67;
  let tempColor = $state("primary")

  if(temp < 50) {
    tempColor = "cyan-300"
  }

  let orders = $derived(getOrders({ page: 0, limit: 10 }));

    function getPaymentMethodIcon(method: PaymentMethod) {
    switch (method) {
      case 'cash':
        return mdiCashMultiple;
      case 'credit':
        return mdiCardBulleted;
    }
  }

  const ToCurrency = (amnt:number|undefined) => {
    if (typeof amnt === "number") {
        return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
      })
      .format(amnt);
    }

    else return "$0";
    
  }

</script>
<div>
<div class="flex flex-row justify-around">
  <div class = "min-h-[33dvh] bg-subtle min-w-[20dvw] rounded-md p-1">
    <h1 class="text-primary text-lg text-center">Daily Revenue</h1>
    {#if dailyRevenue.loading}
      <div class='flex justify-center'>
        <LoadingSpinner/>
      </div>
    {:else if dailyRevenue.error}
      <p class="text-danger">Error loading orders: {dailyRevenue.error.message}</p>
    {:else}
          <h1 class = 'text-center text-6xl align-middle mt-19 mx-2'>{ToCurrency(dailyRevenue.current)}</h1>
    {/if}
  </div>

  <div class = "min-h-[33dvh] bg-subtle min-w-[20dvw] rounded-md flex flex-col p-1">
    <h1 class="text-primary text-lg text-center">Orders Today</h1>
    <h1 class = 'text-center text-9xl align-middle mt-10'>{dailyOrders.current}</h1>
  </div>

  <div class = "min-h-[33dvh] bg-subtle min-w-[20dvw] rounded-md flex flex-col items-center justify-evenly">
    <h1 class="text-primary text-lg">Weather</h1>
    <Icon icon={mdiWeatherHurricane} size='200'/>
    <div class="flex justify-between w-full">
      <h2 class="text-{tempColor} mx-2">{temp} &degF</h2>
      <h2 class="text-primary mx-2">Hurricane</h2>
    </div>
  </div>
</div>

<h1 class="mr-2 my-5 text-5xl">Recent Orders</h1>
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
</div>