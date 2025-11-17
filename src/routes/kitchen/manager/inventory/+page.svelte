<script lang="ts">
  import { getIngredients } from '$lib/api/ingredient.remote';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { Ingredient } from '$lib/db/types';
  import { Heading, IconButton, Input, LoadingSpinner, modalManager } from '@immich/ui';
  import { t } from '$lib/utils/utils';
  import { mdiMagnify, mdiPencil, mdiPlus, mdiTrashCan, mdiTruck } from '@mdi/js';
  import InventoryItemModal from './InventoryItemModal.svelte';
  import InventoryManageModal from './InventoryManageModal.svelte';

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
    modalManager.show(InventoryManageModal, { ingredient });
  }

  async function confirmDelete(ingredient: Ingredient) {
    const confirm = await modalManager.showDialog({
      title: t('manager_delete_ingredient_title'),
      prompt: t('manager_delete_ingredient_prompt'),
      confirmText: t('manager_delete_confirm_yes'),
      confirmColor: 'success',
      icon: mdiTrashCan,
    });

    if (confirm) {
      // TODO: implement deletion logic
      alert(`deleting ingredients not implemented`);
    }
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">{t('manager_inventory_title')}</Heading>
  <div class="flex w-1/3 items-center gap-2">
    <IconButton
      icon={mdiPlus}
      variant="filled"
      aria-label={t('manager_inventory_add_aria')}
      style="p-4"
      onclick={showCreateModal}
    />
    <Input placeholder={t('manager_inventory_search_placeholder')} leadingIcon={mdiMagnify} bind:value={searchTerm} />
  </div>
</div>

{#if ingredients.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if ingredients.error}
  <p class="text-danger">{t('manager_inventory_error_loading')}: {ingredients.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-4/12">{t('manager_inventory_table_name')}</TableHeaderCell>
      <TableHeaderCell width="w-3/12">{t('manager_inventory_table_category')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_inventory_table_current_stock')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_inventory_table_order_stock')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_inventory_table_unit_price')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_inventory_table_actions')}</TableHeaderCell>
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
              aria-label={t('manager_inventory_shipments_aria')}
              onclick={() => showTruckModal(ingredient)}
            />
            <IconButton
              icon={mdiPencil}
              aria-label={t('manager_inventory_edit_aria')}
              onclick={() => showEditModal(ingredient)}
            />
            <IconButton
              icon={mdiTrashCan}
              color="danger"
              aria-label={t('manager_inventory_delete_aria')}
              onclick={() => confirmDelete(ingredient)}
            />
          </TableCell>
        </TableRow>
      {/each}
    </TableBody>
  </Table>
{/if}
