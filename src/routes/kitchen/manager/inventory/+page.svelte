<script lang="ts">
  import { getIngredients } from '$lib/api/ingredient.remote';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { Ingredient } from '$lib/db/types';
  import { Heading, IconButton, Input, LoadingSpinner, modalManager } from '@immich/ui';
  import { mdiMagnify, mdiPencil, mdiPlus, mdiTrashCan, mdiTruck } from '@mdi/js';
  import InventoryItemModal from './InventoryItemModal.svelte';
  import InventoryOrderReceiveModal from './InventoryOrderReceiveModal.svelte';

  let ingredients = getIngredients();
  let searchTerm = $state('');
  let searchedIngredients = $derived(
    ingredients.current?.filter((ingredient) => ingredient.name.toUpperCase().includes(searchTerm.toUpperCase())) || [],
  );

  function showCreateModal() {
    modalManager.show(InventoryItemModal, { mode: { type: 'new' } });
  }

  function showEditModal(ingredient: Ingredient) {
    modalManager.show(InventoryItemModal, { mode: { type: 'edit', item: ingredient } });
  }

  function showTruckModal(ingredient: Ingredient) {
    modalManager.show(InventoryOrderReceiveModal, { ingredient });
  }

  async function confirmDelete(ingredient: Ingredient) {
    const confirm = await modalManager.showDialog({
      title: 'Nice title',
      prompt: 'Are you sure you want to delete this?',
      confirmText: 'Yes, I am',
      confirmColor: 'success',
    });

    if (confirm) {
      // TODO: implement deletion logic
      alert(`deleting ingredients not implemented`);
    }
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">Inventory</Heading>
  <div class="flex w-1/3 items-center gap-2">
    <IconButton icon={mdiPlus} variant="filled" aria-label="Add Employee" style="p-4" onclick={showCreateModal} />
    <Input placeholder="Search" leadingIcon={mdiMagnify} bind:value={searchTerm} />
  </div>
</div>

{#if ingredients.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if ingredients.error}
  <p class="text-danger">Error loading ingredients: {ingredients.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-4/12">Name</TableHeaderCell>
      <TableHeaderCell width="w-3/12">Category</TableHeaderCell>
      <TableHeaderCell width="w-2/12">Current Stock</TableHeaderCell>
      <TableHeaderCell width="w-2/12">Order Stock</TableHeaderCell>
      <TableHeaderCell width="w-2/12">Unit Price</TableHeaderCell>
      <TableHeaderCell width="w-2/12">Actions</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each searchedIngredients as ingredient}
        <TableRow>
          <TableCell width="w-4/12" align="left" class="pl-6">{ingredient.name}</TableCell>
          <TableCell width="w-3/12">{ingredient.category}</TableCell>
          <TableCell width="w-2/12">{ingredient.currentStock}</TableCell>
          <TableCell width="w-2/12">{ingredient.orderStock}</TableCell>
          <TableCell width="w-2/12">${ingredient.unitPrice.toFixed(2)}</TableCell>
          <TableCell width="w-2/12" class="flex gap-2">
            <IconButton
              icon={mdiTruck}
              color="success"
              aria-label="Shipments"
              onclick={() => showTruckModal(ingredient)}
            />
            <IconButton icon={mdiPencil} aria-label="Edit Ingredient" onclick={() => showEditModal(ingredient)} />
            <IconButton
              icon={mdiTrashCan}
              color="danger"
              aria-label="Delete Ingredient"
              onclick={() => confirmDelete(ingredient)}
            />
          </TableCell>
        </TableRow>
      {/each}
    </TableBody>
  </Table>
{/if}
