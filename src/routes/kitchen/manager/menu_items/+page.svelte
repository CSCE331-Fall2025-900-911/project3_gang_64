<script lang="ts">
  import { deleteMenuItem, getMenu } from '$lib/api/menu.remote';
  import { Table, TableBody, TableCell, TableHeader, TableHeaderCell, TableRow } from '$lib/components/Table';
  import type { MenuItem } from '$lib/db/types';
  import { Heading, IconButton, Input, LoadingSpinner, modalManager } from '@immich/ui';
  import { t } from '$lib/utils/utils';
  import { td } from '$lib/contexts/translations.svelte';
  import { mdiMagnify, mdiPencil, mdiTrashCan, mdiPlus } from '@mdi/js';
  import MenuItemModal from './MenuItemModal.svelte';

  let menu = getMenu();
  let searchTerm = $state('');
  let searchedMenuItems = $derived(
    menu.current
      ?.filter((item) => item.archived === false)
      .filter(
        (item) =>
          td(item.name).toUpperCase().includes(searchTerm.toUpperCase()) ||
          td(item.category).toUpperCase().includes(searchTerm.toUpperCase()),
      ) || [],
  );

  async function showDeleteModal(item: MenuItem) {
    const confirm = await modalManager.showDialog({
      title: t('manager_delete_menu_item_title'),
      prompt: `${t('manager_delete_menu_item_prompt')} ${td(item.name)}?`,
      confirmText: t('manager_delete_confirm_text'),
      confirmColor: 'danger',
      icon: mdiTrashCan,
    });

    if (confirm) {
      await deleteMenuItem(item.id);
      item.archived = true;
      searchedMenuItems = searchedMenuItems.filter((i) => i.id !== item.id);
    }
  }

  function showEditModal(item: MenuItem) {
    modalManager.show(MenuItemModal, {
      mode: { type: 'edit', item },
    });
  }

  function showCreateModal() {
    modalManager.show(MenuItemModal, {
      mode: { type: 'new' },
    });
  }
</script>

<div class="mb-6 flex items-center justify-between">
  <Heading size="large">{t('manager_menu_items_title')}</Heading>
  <div class="flex w-1/3 items-center gap-2">
    <IconButton
      icon={mdiPlus}
      variant="filled"
      aria-label={t('manager_menuitem_create_title')}
      style="p-4"
      onclick={showCreateModal}
    />
    <Input placeholder={t('manager_menu_items_search_placeholder')} leadingIcon={mdiMagnify} bind:value={searchTerm} />
  </div>
</div>

{#if menu.loading}
  <div class="flex justify-center">
    <LoadingSpinner size="large" />
  </div>
{:else if menu.error}
  <p class="text-danger">{t('manager_menu_items_error_loading')}: {menu.error.message}</p>
{:else}
  <Table>
    <TableHeader>
      <TableHeaderCell width="w-5/12">{t('manager_menu_items_table_name')}</TableHeaderCell>
      <TableHeaderCell width="w-4/12">{t('manager_menu_items_table_category')}</TableHeaderCell>
      <TableHeaderCell width="w-3/12">{t('manager_menu_items_table_price')}</TableHeaderCell>
      <TableHeaderCell width="w-2/12">{t('manager_menu_items_table_actions')}</TableHeaderCell>
    </TableHeader>
    <TableBody>
      {#each searchedMenuItems as item}
        <TableRow>
          <TableCell width="w-5/12">{td(item.name)}</TableCell>
          <TableCell width="w-4/12">{td(item.category)}</TableCell>
          <TableCell width="w-3/12">${item.price.toFixed(2)}</TableCell>
          <TableCell width="w-2/12" class="flex justify-center gap-2">
            <IconButton
              icon={mdiPencil}
              aria-label={t('manager_menu_items_edit_aria')}
              onclick={() => showEditModal(item)}
            />
            <IconButton
              icon={mdiTrashCan}
              aria-label={t('manager_menu_items_delete_aria')}
              color="danger"
              onclick={() => showDeleteModal(item)}
            />
          </TableCell>
        </TableRow>
      {/each}
    </TableBody>
  </Table>
{/if}
