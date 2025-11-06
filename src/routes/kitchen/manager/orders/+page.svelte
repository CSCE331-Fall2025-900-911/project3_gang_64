<script lang="ts">
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox, TableSearch, tableBodyRow } from "flowbite-svelte"; 
  import {getOrders} from "$lib/api/orders.remote"
  import { Button } from "@immich/ui";
  import type { OrderRow } from "$lib/db/types";

  let orders:OrderRow[];

  const loadOrders = async() => {
    try {
      orders = await getOrders();
      console.log(orders);
    }
    catch (err) {
      console.error("fuck", err);
    }
  }

  loadOrders()
</script>

<Table>
  <TableHead>
    <TableHeadCell>Order #</TableHeadCell>
    <TableHeadCell>Amount</TableHeadCell>
    <TableHeadCell>Time</TableHeadCell>
    <TableHeadCell>Name</TableHeadCell>
    <TableHeadCell>Customer Contact</TableHeadCell>
    <TableHeadCell>Payment Method</TableHeadCell>
  </TableHead>
{#each orders as order}
  <TableBody>
    <TableBodyRow>
      <TableBodyCell>{order.id}</TableBodyCell>
      <TableBodyCell>${order.total}</TableBodyCell>
      <TableBodyCell>{order.date}</TableBodyCell>
      <TableBodyCell>{order.customer}</TableBodyCell>
      <TableBodyCell>555-555-5555</TableBodyCell>
      <TableBodyCell>{order.paymethod}</TableBodyCell>
    </TableBodyRow>
  </TableBody>
{/each}
</Table>

<!-- <Button on:click={loadOrders}>Click to load order rows to console</Button> -->